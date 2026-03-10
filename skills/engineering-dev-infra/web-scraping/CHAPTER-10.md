# CHAPTER 10: Proxy Infrastructure and IP Management

## Introduction

At scale, web scraping without proxies is impossible. Websites track IP addresses, implement rate limits, and ban suspicious traffic. A robust proxy infrastructure is the foundation of production scraping systems.

This chapter covers everything you need to know about proxy infrastructure: residential vs datacenter vs mobile proxies, rotation strategies, geo-targeting, provider comparisons, building proxy pools, monitoring health, managing costs, and maintaining fingerprint consistency.

## Understanding Proxy Types

### Residential Proxies

Residential proxies use IP addresses assigned to real homes by ISPs. They're the gold standard for scraping.

**Advantages:**
- Highest success rate - appear as real users
- Rarely blacklisted
- Best for platforms with strict anti-bot measures
- Support geo-targeting by city/state

**Disadvantages:**
- Most expensive ($3-15 per GB)
- Slower speeds (varies by source)
- Limited bandwidth
- Potential for unstable connections

**Best for:**
- Social media (Facebook, Instagram, LinkedIn)
- E-commerce (Amazon, eBay)
- Search engines (Google)
- Sites with aggressive bot detection

### Datacenter Proxies

Datacenter proxies come from cloud providers and hosting companies.

**Advantages:**
- Fast and reliable
- Cheaper ($1-3 per GB or $1-5 per IP/month)
- Unlimited bandwidth often available
- High stability

**Disadvantages:**
- Easily detected (IP ranges known)
- Higher ban rates
- Less effective against sophisticated sites
- Limited geo-targeting

**Best for:**
- News sites and blogs
- Public data aggregation
- APIs without strict limits
- Price monitoring on smaller sites

### Mobile Proxies

Mobile proxies use IP addresses from cellular networks (4G/5G).

**Advantages:**
- Highest trust score
- Very difficult to block (IPs shared by many users)
- Best for mobile-specific content
- Rotating IPs built-in (carrier NAT)

**Disadvantages:**
- Most expensive ($50-150 per IP/month)
- Limited availability
- Variable speeds
- Complex setup

**Best for:**
- Instagram, TikTok, Snapchat
- Mobile app scraping
- SMS verification
- Accounts requiring mobile IPs

### ISP Proxies (Static Residential)

Hybrid between residential and datacenter - datacenter speed with residential IPs.

**Advantages:**
- Fast like datacenter
- Trusted like residential
- No bandwidth limits typically
- Good value

**Disadvantages:**
- More expensive than datacenter
- Smaller IP pools
- Limited providers
- Can still be detected

**Best for:**
- Sneaker bots
- Ticket purchasing
- E-commerce at scale

## Proxy Rotation Strategies

### Round-Robin Rotation

Simplest strategy - cycle through proxies sequentially.

```python
from typing import List, Optional
import itertools
from threading import Lock

class RoundRobinProxyManager:
    """Simple round-robin proxy rotation"""
    
    def __init__(self, proxies: List[str]):
        self.proxies = proxies
        self.proxy_cycle = itertools.cycle(proxies)
        self.lock = Lock()
    
    def get_proxy(self) -> str:
        """Get next proxy in rotation"""
        with self.lock:
            return next(self.proxy_cycle)
    
    def get_proxy_dict(self) -> dict:
        """Get proxy in requests format"""
        proxy = self.get_proxy()
        return {
            'http': proxy,
            'https': proxy
        }

# Usage
proxies = [
    'http://user:pass@proxy1.com:8080',
    'http://user:pass@proxy2.com:8080',
    'http://user:pass@proxy3.com:8080'
]

manager = RoundRobinProxyManager(proxies)

for i in range(10):
    proxy = manager.get_proxy()
    print(f"Request {i+1}: {proxy}")
```

### Random Rotation

Select random proxy for each request.

```python
import random
from threading import Lock

class RandomProxyManager:
    """Random proxy selection"""
    
    def __init__(self, proxies: List[str]):
        self.proxies = proxies
        self.lock = Lock()
    
    def get_proxy(self) -> str:
        """Get random proxy"""
        with self.lock:
            return random.choice(self.proxies)
    
    def get_proxy_dict(self) -> dict:
        """Get proxy in requests format"""
        proxy = self.get_proxy()
        return {
            'http': proxy,
            'https': proxy
        }

# Usage
manager = RandomProxyManager(proxies)
proxy = manager.get_proxy()
```

### Sticky Session Rotation

Keep same proxy for a session, then rotate.

```python
import time
from typing import Optional
from dataclasses import dataclass
from threading import Lock

@dataclass
class ProxySession:
    """Proxy session with expiry"""
    proxy: str
    started_at: float
    request_count: int = 0

class StickySessionProxyManager:
    """Maintain proxy sessions with configurable duration"""
    
    def __init__(self, proxies: List[str], session_duration: int = 300,
                 max_requests_per_session: int = 50):
        self.proxies = proxies
        self.session_duration = session_duration
        self.max_requests_per_session = max_requests_per_session
        self.sessions = {}  # thread_id -> ProxySession
        self.proxy_index = 0
        self.lock = Lock()
    
    def get_proxy(self, session_id: Optional[str] = None) -> str:
        """Get proxy for session"""
        if session_id is None:
            import threading
            session_id = str(threading.get_ident())
        
        with self.lock:
            now = time.time()
            
            # Check if session exists and is still valid
            if session_id in self.sessions:
                session = self.sessions[session_id]
                
                # Check expiry conditions
                session_expired = (now - session.started_at) > self.session_duration
                max_requests = session.request_count >= self.max_requests_per_session
                
                if not session_expired and not max_requests:
                    session.request_count += 1
                    return session.proxy
            
            # Create new session
            proxy = self.proxies[self.proxy_index]
            self.proxy_index = (self.proxy_index + 1) % len(self.proxies)
            
            self.sessions[session_id] = ProxySession(
                proxy=proxy,
                started_at=now,
                request_count=1
            )
            
            return proxy
    
    def clear_session(self, session_id: Optional[str] = None):
        """Manually clear session"""
        if session_id is None:
            import threading
            session_id = str(threading.get_ident())
        
        with self.lock:
            if session_id in self.sessions:
                del self.sessions[session_id]

# Usage
manager = StickySessionProxyManager(
    proxies=proxies,
    session_duration=300,  # 5 minutes
    max_requests_per_session=50
)

# Same session will get same proxy
session_id = "user_123"
for i in range(5):
    proxy = manager.get_proxy(session_id)
    print(f"Request {i+1}: {proxy}")
```

### Smart Rotation (Least Recently Used)

Track proxy usage and prefer least recently used proxies.

```python
from collections import OrderedDict
import time

class SmartProxyManager:
    """LRU-based proxy rotation with health tracking"""
    
    def __init__(self, proxies: List[str], cooldown_seconds: int = 60):
        self.proxies = OrderedDict()
        self.cooldown_seconds = cooldown_seconds
        
        # Initialize proxy tracking
        for proxy in proxies:
            self.proxies[proxy] = {
                'last_used': 0,
                'success_count': 0,
                'fail_count': 0,
                'total_requests': 0,
                'is_banned': False
            }
        
        self.lock = Lock()
    
    def get_proxy(self) -> str:
        """Get least recently used proxy"""
        with self.lock:
            now = time.time()
            
            # Find available proxy
            for proxy, stats in self.proxies.items():
                if stats['is_banned']:
                    continue
                
                time_since_use = now - stats['last_used']
                
                if time_since_use >= self.cooldown_seconds:
                    stats['last_used'] = now
                    stats['total_requests'] += 1
                    return proxy
            
            # If no proxy available after cooldown, use least recently used
            proxy = min(
                [p for p, s in self.proxies.items() if not s['is_banned']],
                key=lambda p: self.proxies[p]['last_used']
            )
            
            self.proxies[proxy]['last_used'] = now
            self.proxies[proxy]['total_requests'] += 1
            
            return proxy
    
    def report_success(self, proxy: str):
        """Report successful request"""
        with self.lock:
            if proxy in self.proxies:
                self.proxies[proxy]['success_count'] += 1
    
    def report_failure(self, proxy: str):
        """Report failed request"""
        with self.lock:
            if proxy in self.proxies:
                stats = self.proxies[proxy]
                stats['fail_count'] += 1
                
                # Ban if failure rate too high
                if stats['total_requests'] > 10:
                    failure_rate = stats['fail_count'] / stats['total_requests']
                    if failure_rate > 0.5:
                        stats['is_banned'] = True
                        print(f"Proxy {proxy} banned due to high failure rate")
    
    def get_stats(self) -> dict:
        """Get proxy statistics"""
        with self.lock:
            return {
                proxy: {
                    'success_rate': (stats['success_count'] / stats['total_requests'] * 100)
                    if stats['total_requests'] > 0 else 0,
                    'total_requests': stats['total_requests'],
                    'is_banned': stats['is_banned']
                }
                for proxy, stats in self.proxies.items()
            }
    
    def unban_all(self):
        """Unban all proxies"""
        with self.lock:
            for stats in self.proxies.values():
                stats['is_banned'] = False

# Usage
manager = SmartProxyManager(proxies, cooldown_seconds=30)

for i in range(100):
    proxy = manager.get_proxy()
    
    # Simulate request
    import random
    success = random.random() > 0.2
    
    if success:
        manager.report_success(proxy)
    else:
        manager.report_failure(proxy)

# Check stats
stats = manager.get_stats()
for proxy, data in stats.items():
    print(f"{proxy}: {data['success_rate']:.1f}% success, "
          f"{data['total_requests']} requests, "
          f"banned: {data['is_banned']}")
```

## Geo-Targeting

Target specific countries, states, or cities.

```python
from typing import Optional, List
from dataclasses import dataclass

@dataclass
class GeoProxy:
    """Proxy with geographic metadata"""
    url: str
    country: str
    state: Optional[str] = None
    city: Optional[str] = None

class GeoProxyManager:
    """Manage proxies with geographic targeting"""
    
    def __init__(self, proxies: List[GeoProxy]):
        self.proxies = proxies
        self._index_by_country = self._build_country_index()
        self._index_by_state = self._build_state_index()
    
    def _build_country_index(self) -> dict:
        """Index proxies by country"""
        index = {}
        for proxy in self.proxies:
            if proxy.country not in index:
                index[proxy.country] = []
            index[proxy.country].append(proxy)
        return index
    
    def _build_state_index(self) -> dict:
        """Index proxies by state"""
        index = {}
        for proxy in self.proxies:
            if proxy.state:
                key = f"{proxy.country}:{proxy.state}"
                if key not in index:
                    index[key] = []
                index[key].append(proxy)
        return index
    
    def get_proxy_by_country(self, country: str) -> Optional[str]:
        """Get random proxy from country"""
        proxies = self._index_by_country.get(country, [])
        if proxies:
            return random.choice(proxies).url
        return None
    
    def get_proxy_by_state(self, country: str, state: str) -> Optional[str]:
        """Get random proxy from state"""
        key = f"{country}:{state}"
        proxies = self._index_by_state.get(key, [])
        if proxies:
            return random.choice(proxies).url
        return None
    
    def get_all_countries(self) -> List[str]:
        """Get list of available countries"""
        return list(self._index_by_country.keys())
    
    def get_proxy_count_by_country(self) -> dict:
        """Get proxy count per country"""
        return {
            country: len(proxies)
            for country, proxies in self._index_by_country.items()
        }

# Usage
proxies = [
    GeoProxy('http://user:pass@proxy1.com:8080', 'US', 'CA', 'Los Angeles'),
    GeoProxy('http://user:pass@proxy2.com:8080', 'US', 'NY', 'New York'),
    GeoProxy('http://user:pass@proxy3.com:8080', 'UK', 'England', 'London'),
    GeoProxy('http://user:pass@proxy4.com:8080', 'DE', 'Bavaria', 'Munich'),
]

manager = GeoProxyManager(proxies)

# Get US proxy
us_proxy = manager.get_proxy_by_country('US')
print(f"US proxy: {us_proxy}")

# Get California proxy
ca_proxy = manager.get_proxy_by_state('US', 'CA')
print(f"California proxy: {ca_proxy}")

# Get stats
print(f"Countries: {manager.get_all_countries()}")
print(f"Counts: {manager.get_proxy_count_by_country()}")
```

## Provider Comparison

### Major Proxy Providers

**BrightData (formerly Luminati)**
- Largest residential proxy network (72M+ IPs)
- Pricing: $8.40-$15/GB (residential), $0.60-$1.20/GB (datacenter)
- Best for: Enterprise scraping, high-volume
- Pros: Massive pool, excellent geo-targeting, reliable
- Cons: Expensive, complex pricing

**Oxylabs**
- 100M+ residential IPs
- Pricing: Custom (typically $3-10/GB residential)
- Best for: Enterprise, compliance-focused projects
- Pros: Good documentation, reliable, compliant
- Cons: Expensive, minimum commitments

**SmartProxy**
- 40M+ residential IPs
- Pricing: $12.50/GB (residential), $30/month for 5 IPs (datacenter)
- Best for: Mid-sized operations
- Pros: Good balance of price/quality, flexible plans
- Cons: Smaller pool than top tier

**NetNut**
- ISP/residential hybrid
- Pricing: $300/20GB (residential)
- Best for: High-speed residential needs
- Pros: Fast, reliable, good for SEO tools
- Cons: Smaller pool, limited locations

**IPRoyal**
- Budget-friendly option
- Pricing: $2.40/GB (residential), $1.75/IP/month (datacenter)
- Best for: Small-scale scraping, testing
- Pros: Cheap, easy to start
- Cons: Smaller pool, less reliable

### Provider Selection Matrix

```python
from dataclasses import dataclass
from typing import List

@dataclass
class ProviderSpecs:
    """Provider specifications"""
    name: str
    proxy_type: str
    price_per_gb: float
    ip_pool_size: int  # millions
    min_commitment: float  # USD
    geo_targeting: bool
    success_rate: float  # estimated %
    
class ProviderSelector:
    """Select best provider for your needs"""
    
    PROVIDERS = [
        ProviderSpecs('BrightData', 'residential', 10.0, 72, 500, True, 95),
        ProviderSpecs('Oxylabs', 'residential', 8.0, 100, 1000, True, 95),
        ProviderSpecs('SmartProxy', 'residential', 12.5, 40, 75, True, 90),
        ProviderSpecs('NetNut', 'isp', 15.0, 10, 300, True, 93),
        ProviderSpecs('IPRoyal', 'residential', 2.4, 2, 0, True, 85),
        ProviderSpecs('BrightData DC', 'datacenter', 1.0, None, 500, False, 80),
        ProviderSpecs('Webshare', 'datacenter', 0.0, None, 0, False, 75),
    ]
    
    @classmethod
    def find_best(cls, monthly_budget: float, monthly_gb: float,
                 min_success_rate: float = 85) -> List[ProviderSpecs]:
        """Find providers matching criteria"""
        
        matching = []
        
        for provider in cls.PROVIDERS:
            # Check success rate
            if provider.success_rate < min_success_rate:
                continue
            
            # Calculate monthly cost
            monthly_cost = provider.price_per_gb * monthly_gb
            
            # Check budget
            if monthly_cost > monthly_budget:
                continue
            
            # Check minimum commitment
            if provider.min_commitment > monthly_budget:
                continue
            
            matching.append(provider)
        
        # Sort by value (success rate / price)
        matching.sort(
            key=lambda p: p.success_rate / p.price_per_gb if p.price_per_gb > 0 else 999,
            reverse=True
        )
        
        return matching

# Usage
budget = 500  # $500/month
monthly_gb = 50  # 50 GB/month

providers = ProviderSelector.find_best(
    monthly_budget=budget,
    monthly_gb=monthly_gb,
    min_success_rate=90
)

print(f"Recommended providers for ${budget}/month, {monthly_gb}GB:")
for p in providers:
    monthly_cost = p.price_per_gb * monthly_gb
    print(f"- {p.name}: ${monthly_cost:.2f}/month, "
          f"{p.success_rate}% success rate, "
          f"{p.ip_pool_size}M IPs")
```

## Building Proxy Pools

### Proxy Pool Manager

```python
import requests
from typing import List, Optional, Dict
from dataclasses import dataclass, field
from datetime import datetime, timedelta
import time
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

@dataclass
class ProxyStatus:
    """Track proxy health"""
    proxy: str
    is_alive: bool = True
    last_check: datetime = field(default_factory=datetime.now)
    response_time: float = 0.0
    success_count: int = 0
    fail_count: int = 0
    consecutive_failures: int = 0
    
    @property
    def success_rate(self) -> float:
        total = self.success_count + self.fail_count
        if total == 0:
            return 0.0
        return (self.success_count / total) * 100

class ProxyPool:
    """Production-grade proxy pool with health monitoring"""
    
    def __init__(self, proxies: List[str], test_url: str = 'http://httpbin.org/ip',
                 test_interval: int = 300, max_consecutive_failures: int = 3):
        self.test_url = test_url
        self.test_interval = test_interval
        self.max_consecutive_failures = max_consecutive_failures
        
        # Initialize proxy statuses
        self.proxies = {
            proxy: ProxyStatus(proxy=proxy)
            for proxy in proxies
        }
        
        self.lock = Lock()
        
        # Run initial health check
        self.health_check_all()
    
    def health_check_all(self):
        """Check health of all proxies"""
        logger.info("Running health check on all proxies")
        
        for proxy in list(self.proxies.keys()):
            self.health_check(proxy)
    
    def health_check(self, proxy: str) -> bool:
        """Check if proxy is alive"""
        status = self.proxies.get(proxy)
        if not status:
            return False
        
        try:
            start_time = time.time()
            
            response = requests.get(
                self.test_url,
                proxies={'http': proxy, 'https': proxy},
                timeout=10
            )
            
            response_time = time.time() - start_time
            
            if response.status_code == 200:
                with self.lock:
                    status.is_alive = True
                    status.last_check = datetime.now()
                    status.response_time = response_time
                    status.consecutive_failures = 0
                
                logger.debug(f"Proxy {proxy} alive ({response_time:.2f}s)")
                return True
            else:
                raise Exception(f"Status code: {response.status_code}")
                
        except Exception as e:
            logger.warning(f"Proxy {proxy} failed: {e}")
            
            with self.lock:
                status.consecutive_failures += 1
                
                if status.consecutive_failures >= self.max_consecutive_failures:
                    status.is_alive = False
                    logger.warning(f"Proxy {proxy} marked as dead")
            
            return False
    
    def get_proxy(self) -> Optional[str]:
        """Get a healthy proxy"""
        with self.lock:
            # Filter alive proxies
            alive_proxies = [
                proxy for proxy, status in self.proxies.items()
                if status.is_alive
            ]
            
            if not alive_proxies:
                logger.error("No alive proxies available!")
                return None
            
            # Select proxy with best success rate and lowest recent usage
            best_proxy = min(
                alive_proxies,
                key=lambda p: (
                    -self.proxies[p].success_rate,  # Prefer high success rate
                    (datetime.now() - self.proxies[p].last_check).total_seconds()  # Prefer recently checked
                )
            )
            
            return best_proxy
    
    def report_success(self, proxy: str):
        """Report successful request"""
        with self.lock:
            if proxy in self.proxies:
                self.proxies[proxy].success_count += 1
                self.proxies[proxy].consecutive_failures = 0
    
    def report_failure(self, proxy: str):
        """Report failed request"""
        with self.lock:
            if proxy in self.proxies:
                status = self.proxies[proxy]
                status.fail_count += 1
                status.consecutive_failures += 1
                
                # Mark dead if too many failures
                if status.consecutive_failures >= self.max_consecutive_failures:
                    status.is_alive = False
                    logger.warning(f"Proxy {proxy} marked as dead after failures")
    
    def get_stats(self) -> Dict:
        """Get pool statistics"""
        with self.lock:
            total = len(self.proxies)
            alive = sum(1 for s in self.proxies.values() if s.is_alive)
            
            avg_success_rate = sum(
                s.success_rate for s in self.proxies.values()
            ) / total if total > 0 else 0
            
            avg_response_time = sum(
                s.response_time for s in self.proxies.values() if s.response_time > 0
            ) / max(1, sum(1 for s in self.proxies.values() if s.response_time > 0))
            
            return {
                'total_proxies': total,
                'alive_proxies': alive,
                'dead_proxies': total - alive,
                'avg_success_rate': avg_success_rate,
                'avg_response_time': avg_response_time
            }
    
    def get_detailed_stats(self) -> List[Dict]:
        """Get detailed stats for each proxy"""
        with self.lock:
            return [
                {
                    'proxy': status.proxy,
                    'is_alive': status.is_alive,
                    'success_rate': status.success_rate,
                    'response_time': status.response_time,
                    'total_requests': status.success_count + status.fail_count
                }
                for status in sorted(
                    self.proxies.values(),
                    key=lambda s: s.success_rate,
                    reverse=True
                )
            ]

# Usage
proxies = [
    'http://user:pass@proxy1.com:8080',
    'http://user:pass@proxy2.com:8080',
    'http://user:pass@proxy3.com:8080'
]

pool = ProxyPool(proxies, test_interval=300)

# Get proxy for request
proxy = pool.get_proxy()

if proxy:
    try:
        response = requests.get(
            'https://example.com',
            proxies={'http': proxy, 'https': proxy},
            timeout=10
        )
        pool.report_success(proxy)
    except:
        pool.report_failure(proxy)

# Get stats
stats = pool.get_stats()
print(f"Pool stats: {stats}")

detailed = pool.get_detailed_stats()
for stat in detailed:
    print(f"{stat['proxy']}: {stat['success_rate']:.1f}% success, "
          f"{stat['response_time']:.2f}s, "
          f"alive: {stat['is_alive']}")
```

## IP Reputation Management

Track and manage IP reputation.

```python
from collections import defaultdict
from datetime import datetime, timedelta

class IPReputationTracker:
    """Track IP reputation across platforms"""
    
    def __init__(self):
        self.reputation = defaultdict(lambda: {
            'captcha_count': 0,
            'ban_count': 0,
            'block_count': 0,
            'success_count': 0,
            'last_captcha': None,
            'last_ban': None,
            'cooldown_until': None
        })
    
    def report_captcha(self, ip: str, platform: str):
        """Report CAPTCHA challenge"""
        key = f"{ip}:{platform}"
        self.reputation[key]['captcha_count'] += 1
        self.reputation[key]['last_captcha'] = datetime.now()
        
        # Set cooldown
        self.reputation[key]['cooldown_until'] = datetime.now() + timedelta(hours=1)
    
    def report_ban(self, ip: str, platform: str, duration_hours: int = 24):
        """Report IP ban"""
        key = f"{ip}:{platform}"
        self.reputation[key]['ban_count'] += 1
        self.reputation[key]['last_ban'] = datetime.now()
        
        # Set cooldown
        self.reputation[key]['cooldown_until'] = datetime.now() + timedelta(hours=duration_hours)
    
    def report_success(self, ip: str, platform: str):
        """Report successful request"""
        key = f"{ip}:{platform}"
        self.reputation[key]['success_count'] += 1
    
    def is_available(self, ip: str, platform: str) -> bool:
        """Check if IP is available for use"""
        key = f"{ip}:{platform}"
        rep = self.reputation[key]
        
        if rep['cooldown_until']:
            if datetime.now() < rep['cooldown_until']:
                return False
        
        return True
    
    def get_reputation_score(self, ip: str, platform: str) -> float:
        """Calculate reputation score (0-100)"""
        key = f"{ip}:{platform}"
        rep = self.reputation[key]
        
        total_requests = (
            rep['success_count'] +
            rep['captcha_count'] +
            rep['ban_count'] +
            rep['block_count']
        )
        
        if total_requests == 0:
            return 100.0  # New IP
        
        # Weight different events
        score = (
            rep['success_count'] * 1.0 -
            rep['captcha_count'] * 0.5 -
            rep['block_count'] * 1.0 -
            rep['ban_count'] * 2.0
        ) / total_requests * 100
        
        return max(0, min(100, score))
    
    def get_best_ip(self, ips: List[str], platform: str) -> Optional[str]:
        """Get best IP for platform"""
        available = [
            ip for ip in ips
            if self.is_available(ip, platform)
        ]
        
        if not available:
            return None
        
        # Select IP with best reputation
        best_ip = max(
            available,
            key=lambda ip: self.get_reputation_score(ip, platform)
        )
        
        return best_ip

# Usage
tracker = IPReputationTracker()

ips = ['1.2.3.4', '5.6.7.8', '9.10.11.12']
platform = 'instagram'

# Simulate usage
tracker.report_success(ips[0], platform)
tracker.report_success(ips[0], platform)
tracker.report_captcha(ips[0], platform)

tracker.report_success(ips[1], platform)
tracker.report_ban(ips[1], platform)

tracker.report_success(ips[2], platform)

# Get best IP
best = tracker.get_best_ip(ips, platform)
print(f"Best IP: {best}")

for ip in ips:
    score = tracker.get_reputation_score(ip, platform)
    available = tracker.is_available(ip, platform)
    print(f"{ip}: Score {score:.1f}, Available: {available}")
```

## Cost Optimization

Track and optimize proxy costs.

```python
from dataclasses import dataclass
from typing import Dict, List
from datetime import datetime

@dataclass
class UsageRecord:
    """Proxy usage record"""
    proxy: str
    timestamp: datetime
    bytes_used: int
    success: bool
    platform: str

class ProxyCostTracker:
    """Track and optimize proxy costs"""
    
    def __init__(self, price_per_gb: float):
        self.price_per_gb = price_per_gb
        self.usage_records: List[UsageRecord] = []
    
    def record_usage(self, proxy: str, bytes_used: int, success: bool, platform: str):
        """Record proxy usage"""
        self.usage_records.append(UsageRecord(
            proxy=proxy,
            timestamp=datetime.now(),
            bytes_used=bytes_used,
            success=success,
            platform=platform
        ))
    
    def get_total_cost(self) -> float:
        """Calculate total cost"""
        total_bytes = sum(r.bytes_used for r in self.usage_records)
        total_gb = total_bytes / (1024 ** 3)
        return total_gb * self.price_per_gb
    
    def get_cost_by_platform(self) -> Dict[str, float]:
        """Calculate cost per platform"""
        platform_bytes = {}
        
        for record in self.usage_records:
            if record.platform not in platform_bytes:
                platform_bytes[record.platform] = 0
            platform_bytes[record.platform] += record.bytes_used
        
        return {
            platform: (bytes_used / (1024 ** 3)) * self.price_per_gb
            for platform, bytes_used in platform_bytes.items()
        }
    
    def get_cost_per_success(self) -> float:
        """Calculate cost per successful request"""
        total_cost = self.get_total_cost()
        success_count = sum(1 for r in self.usage_records if r.success)
        
        if success_count == 0:
            return 0.0
        
        return total_cost / success_count
    
    def get_waste_analysis(self) -> Dict:
        """Analyze wasted bandwidth"""
        failed_bytes = sum(
            r.bytes_used for r in self.usage_records if not r.success
        )
        total_bytes = sum(r.bytes_used for r in self.usage_records)
        
        if total_bytes == 0:
            return {'wasted_percentage': 0, 'wasted_cost': 0}
        
        wasted_percentage = (failed_bytes / total_bytes) * 100
        wasted_gb = failed_bytes / (1024 ** 3)
        wasted_cost = wasted_gb * self.price_per_gb
        
        return {
            'wasted_percentage': wasted_percentage,
            'wasted_cost': wasted_cost,
            'wasted_gb': wasted_gb
        }
    
    def get_optimization_report(self) -> str:
        """Generate cost optimization report"""
        total_cost = self.get_total_cost()
        cost_by_platform = self.get_cost_by_platform()
        cost_per_success = self.get_cost_per_success()
        waste = self.get_waste_analysis()
        
        report = f"""
Proxy Cost Report
=================
Total Cost: ${total_cost:.2f}

Cost by Platform:
"""
        for platform, cost in sorted(cost_by_platform.items(), key=lambda x: x[1], reverse=True):
            report += f"  {platform}: ${cost:.2f}\n"
        
        report += f"""
Efficiency:
  Cost per success: ${cost_per_success:.4f}
  Wasted bandwidth: {waste['wasted_gb']:.2f} GB ({waste['wasted_percentage']:.1f}%)
  Wasted cost: ${waste['wasted_cost']:.2f}

Recommendations:
"""
        
        if waste['wasted_percentage'] > 20:
            report += "  - High waste detected. Improve proxy rotation strategy.\n"
        
        if cost_per_success > 0.01:
            report += "  - Cost per success is high. Consider cheaper proxy tier.\n"
        
        return report

# Usage
tracker = ProxyCostTracker(price_per_gb=10.0)

# Simulate usage
tracker.record_usage('proxy1', 1024*1024*10, True, 'amazon')  # 10MB success
tracker.record_usage('proxy2', 1024*1024*5, False, 'amazon')  # 5MB failed
tracker.record_usage('proxy1', 1024*1024*20, True, 'google')  # 20MB success

print(tracker.get_optimization_report())
```

## Fingerprint Consistency

Maintain consistent browser fingerprints when using proxies.

```python
from playwright.sync_api import sync_playwright
from typing import Dict, Optional

class FingerprintManager:
    """Manage browser fingerprints for proxy sessions"""
    
    def __init__(self):
        self.fingerprints = {}
    
    def get_fingerprint(self, proxy: str) -> Dict:
        """Get or create fingerprint for proxy"""
        if proxy not in self.fingerprints:
            self.fingerprints[proxy] = self._generate_fingerprint()
        
        return self.fingerprints[proxy]
    
    def _generate_fingerprint(self) -> Dict:
        """Generate consistent fingerprint"""
        import random
        
        user_agents = [
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
            'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
        ]
        
        screen_resolutions = [
            {'width': 1920, 'height': 1080},
            {'width': 1366, 'height': 768},
            {'width': 2560, 'height': 1440}
        ]
        
        return {
            'user_agent': random.choice(user_agents),
            'viewport': random.choice(screen_resolutions),
            'locale': 'en-US',
            'timezone': 'America/New_York',
            'platform': 'Win32'
        }
    
    def create_browser_context(self, browser, proxy: str):
        """Create browser context with consistent fingerprint"""
        fingerprint = self.get_fingerprint(proxy)
        
        context = browser.new_context(
            viewport=fingerprint['viewport'],
            user_agent=fingerprint['user_agent'],
            locale=fingerprint['locale'],
            timezone_id=fingerprint['timezone'],
            proxy={'server': proxy}
        )
        
        return context

# Usage
with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    
    manager = FingerprintManager()
    proxy = 'http://user:pass@proxy1.com:8080'
    
    # Create context with consistent fingerprint
    context = manager.create_browser_context(browser, proxy)
    page = context.new_page()
    
    # Use the page...
    page.goto('https://example.com')
    
    context.close()
    browser.close()
```

## Summary

Effective proxy infrastructure requires:

1. **Proxy Type Selection**: Choose residential, datacenter, mobile, or ISP based on needs
2. **Rotation Strategy**: Implement round-robin, random, sticky, or smart rotation
3. **Geo-Targeting**: Target specific countries, states, or cities
4. **Provider Selection**: Compare providers on price, pool size, and reliability
5. **Pool Management**: Build robust proxy pools with health monitoring
6. **Reputation Tracking**: Monitor and manage IP reputation across platforms
7. **Cost Optimization**: Track usage and optimize spending
8. **Fingerprint Consistency**: Maintain consistent browser fingerprints per proxy

A well-designed proxy infrastructure is the backbone of scalable, reliable web scraping operations.