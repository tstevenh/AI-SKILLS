# Chapter 5: Advanced Anti-Detection

## Table of Contents
1. [Introduction to Anti-Detection](#introduction-to-anti-detection)
2. [Understanding Bot Detection](#understanding-bot-detection)
3. [Request Fingerprinting](#request-fingerprinting)
4. [Proxy Rotation](#proxy-rotation)
5. [User Agent Rotation](#user-agent-rotation)
6. [Browser Fingerprint Randomization](#browser-fingerprint-randomization)
7. [Behavioral Mimicry](#behavioral-mimicry)
8. [CAPTCHA Handling](#captcha-handling)
9. [Session Management](#session-management)
10. [Advanced Evasion Techniques](#advanced-evasion-techniques)
11. [Testing and Validation](#testing-and-validation)
12. [Ethical and Legal Considerations](#ethical-and-legal-considerations)

---

## Introduction to Anti-Detection

As web scraping has become more prevalent, websites have developed sophisticated mechanisms to detect and block automated access. These anti-bot systems analyze requests for patterns that distinguish humans from bots. Understanding and circumventing these detection mechanisms—while staying within ethical and legal boundaries—is essential for large-scale, production scraping operations.

### Why Anti-Detection Matters

Consider a typical scraping scenario: you've built a scraper that successfully extracts data from a website during development. However, when you deploy it at scale, you encounter:

- IP bans after a few hundred requests
- CAPTCHA challenges on every page
- 403 Forbidden errors
- Rate limiting
- Honey pot traps
- JavaScript challenges

These defenses exist because:

1. **Resource Protection** - Bots consume bandwidth and server resources
2. **Data Protection** - Companies want to protect their proprietary data
3. **Security** - Bots may attempt injection attacks or credential stuffing
4. **Competitive Advantage** - Preventing competitors from monitoring prices/inventory
5. **User Experience** - Ensuring fair access for human users

### The Arms Race

Web scraping and bot detection exist in a constant arms race:

1. **Scrapers** automate simple HTTP requests
2. **Detectors** identify missing headers or cookie behavior
3. **Scrapers** add proper headers and session handling
4. **Detectors** use JavaScript fingerprinting
5. **Scrapers** adopt headless browsers
6. **Detectors** detect WebDriver properties
7. **Scrapers** patch or hide WebDriver signatures
8. **Detectors** analyze behavior patterns
9. **Scrapers** introduce random delays and human-like behavior

This chapter covers current best practices for evading detection while maintaining respect for website terms of service and robots.txt directives.

---

## Understanding Bot Detection

### Detection Techniques Overview

Modern bot detection systems use multiple layers of analysis:

**Network Layer:**
- IP address reputation and geolocation
- Request frequency and patterns
- TCP/IP fingerprinting
- TLS fingerprinting

**Application Layer:**
- HTTP header analysis
- Cookie and session behavior
- JavaScript execution tests
- Canvas/WebGL fingerprinting

**Behavioral Layer:**
- Mouse movement patterns
- Keystroke dynamics
- Page interaction sequences
- Time-on-page metrics

**Cross-Layer Analysis:**
- Correlation across requests
- Historical behavior matching
- Machine learning classification

### Common Detection Signals

**Missing Headers:**
```python
# Bot-like request
requests.get('https://example.com')

# Sends minimal headers:
# User-Agent: python-requests/2.28.1
# Accept-Encoding: gzip, deflate
# Accept: */*
# Connection: keep-alive
```

**Inconsistent Headers:**
```python
# Mismatched User-Agent and Accept headers
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36',
    'Accept': 'text/html',  # Chrome would send more complex Accept header
}
```

**WebDriver Detection:**
```javascript
// Websites check for WebDriver properties
if (window.navigator.webdriver) {
    console.log("Bot detected!");
}

// Or check for missing plugins
if (navigator.plugins.length === 0) {
    console.log("Likely headless browser");
}
```

### Detection Response Types

| Response | Meaning | Typical Cause |
|----------|---------|---------------|
| 200 OK with CAPTCHA | Suspicion triggered | Moderate risk signals |
| 403 Forbidden | Access denied | Clear bot signals, IP blacklist |
| 429 Too Many Requests | Rate limited | Request frequency too high |
| 503 Service Unavailable | Protection active | DDoS protection (Cloudflare, etc.) |
| JavaScript challenge | Bot verification | Automated browser detection |
| Honeypot trap | Bot confirmed | Clicked hidden link/form |

---

## Request Fingerprinting

### HTTP Headers Analysis

Websites analyze headers for consistency:

```python
# Real Chrome headers (simplified)
chrome_headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.5',
    'Accept-Encoding': 'gzip, deflate, br',
    'DNT': '1',
    'Connection': 'keep-alive',
    'Upgrade-Insecure-Requests': '1',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'none',
    'Sec-Fetch-User': '?1',
    'Cache-Control': 'max-age=0',
}
```

### Header Consistency

```python
import requests
from fake_useragent import UserAgent

class StealthSession(requests.Session):
    def __init__(self):
        super().__init__()
        self.ua = UserAgent()
        self._set_headers()
    
    def _set_headers(self):
        """Set consistent headers based on User-Agent"""
        user_agent = self.ua.chrome
        
        # Headers must be consistent with User-Agent
        if 'Chrome' in user_agent:
            self.headers.update({
                'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
                'Accept-Language': 'en-US,en;q=0.9',
                'Accept-Encoding': 'gzip, deflate, br',
                'Upgrade-Insecure-Requests': '1',
                'Sec-Fetch-Dest': 'document',
                'Sec-Fetch-Mode': 'navigate',
                'Sec-Fetch-Site': 'none',
                'Sec-Fetch-User': '?1',
            })
        elif 'Firefox' in user_agent:
            self.headers.update({
                'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
                'Accept-Language': 'en-US,en;q=0.5',
                'Accept-Encoding': 'gzip, deflate, br',
                'Upgrade-Insecure-Requests': '1',
                'DNT': '1',
            })
        
        self.headers['User-Agent'] = user_agent
```

### TLS/JA3 Fingerprinting

TLS handshake patterns can identify clients:

```python
# Use curl_cffi to match browser TLS fingerprint
from curl_cffi import requests

# This matches Chrome's TLS fingerprint
response = requests.get('https://example.com', impersonate="chrome110")
```

### HTTP/2 Fingerprinting

Modern browsers use HTTP/2 with specific behaviors:

```python
# httpx supports HTTP/2
import httpx

client = httpx.Client(http2=True)
response = client.get('https://example.com')
```

---

## Proxy Rotation

### Why Use Proxies

- **IP Rotation** - Distribute requests across multiple IPs
- **Geolocation** - Access geo-restricted content
- **Rate Limit Evasion** - Each IP has its own quota
- **Ban Recovery** - Continue scraping when one IP is blocked

### Types of Proxies

| Type | Use Case | Reliability | Cost |
|------|----------|-------------|------|
| Datacenter | High volume | Medium | Low |
| Residential | Sensitive sites | High | High |
| Mobile | Strictest sites | Very High | Very High |
| ISP (Static Residential) | Balanced | High | Medium |

### Implementing Proxy Rotation

```python
import requests
import random
from itertools import cycle

class ProxyRotator:
    def __init__(self, proxies):
        self.proxies = proxies
        self.proxy_pool = cycle(proxies)
        self.failed_proxies = set()
    
    def get_proxy(self):
        """Get next working proxy"""
        attempts = 0
        while attempts < len(self.proxies):
            proxy = next(self.proxy_pool)
            if proxy not in self.failed_proxies:
                return proxy
            attempts += 1
        return None
    
    def mark_failed(self, proxy):
        """Mark proxy as failed"""
        self.failed_proxies.add(proxy)
```

```python
class ScrapingSession:
    def __init__(self, proxy_list):
        self.session = requests.Session()
        self.proxy_rotator = ProxyRotator(proxy_list)
        self.current_proxy = None
    
    def request(self, url, **kwargs):
        if not self.current_proxy:
            self.current_proxy = self.proxy_rotator.get_proxy()
        
        proxies = {
            'http': self.current_proxy,
            'https': self.current_proxy
        }
        
        try:
            response = self.session.get(url, proxies=proxies, timeout=30, **kwargs)
            
            if response.status_code == 403:
                # Proxy blocked, rotate
                self.proxy_rotator.mark_failed(self.current_proxy)
                self.current_proxy = self.proxy_rotator.get_proxy()
                return self.request(url, **kwargs)
            
            return response
            
        except requests.exceptions.ProxyError:
            self.proxy_rotator.mark_failed(self.current_proxy)
            self.current_proxy = self.proxy_rotator.get_proxy()
            return self.request(url, **kwargs)
```

### Commercial Proxy Services

```python
# Bright Data (formerly Luminati)
import requests

proxy = 'http://user:pass@brd.superproxy.io:22225'
proxies = {'http': proxy, 'https': proxy}

response = requests.get('https://example.com', proxies=proxies)

# Smartproxy
proxy = 'http://user:pass@gate.smartproxy.com:7000'

# Oxylabs
proxy = 'http://user:pass@pr.oxylabs.io:7777'
```

### Proxy Best Practices

```python
class SmartProxyManager:
    def __init__(self, proxies):
        self.proxies = proxies
        self.usage_count = {p: 0 for p in proxies}
        self.banned_proxies = set()
    
    def get_proxy(self):
        """Get least-used working proxy"""
        available = [
            p for p in self.proxies 
            if p not in self.banned_proxies
        ]
        
        if not available:
            raise Exception("No available proxies")
        
        # Select least used
        proxy = min(available, key=lambda p: self.usage_count[p])
        self.usage_count[proxy] += 1
        
        return proxy
    
    def ban_proxy(self, proxy, duration_minutes=60):
        """Temporary ban proxy"""
        self.banned_proxies.add(proxy)
        # Could schedule unban after duration
    
    def report_success(self, proxy):
        """Track successful requests"""
        pass  # Could implement scoring
    
    def report_failure(self, proxy, error_type):
        """Track failures"""
        if error_type in ['banned', 'blocked']:
            self.ban_proxy(proxy)
```

---

## User Agent Rotation

### The Importance of User Agents

The User-Agent string is the most commonly checked header. Using outdated or generic User-Agent strings is a clear bot indicator.

### Realistic User Agent Rotation

```python
from fake_useragent import UserAgent
import random

class UserAgentRotator:
    def __init__(self):
        self.ua = UserAgent()
        self.recent_agents = []
        self.max_history = 10
    
    def get_user_agent(self, browser=None):
        """Get random User-Agent, avoiding recent repeats"""
        attempts = 0
        while attempts < 20:
            if browser == 'chrome':
                agent = self.ua.chrome
            elif browser == 'firefox':
                agent = self.ua.firefox
            elif browser == 'safari':
                agent = self.ua.safari
            else:
                agent = self.ua.random
            
            if agent not in self.recent_agents:
                self.recent_agents.append(agent)
                if len(self.recent_agents) > self.max_history:
                    self.recent_agents.pop(0)
                return agent
            
            attempts += 1
        
        return self.ua.random
```

### Platform-Specific User Agents

```python
USER_AGENTS = {
    'desktop_chrome': [
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.0',
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.0',
    ],
    'desktop_firefox': [
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/121.0',
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:109.0) Gecko/20100101 Firefox/121.0',
    ],
    'mobile_ios': [
        'Mozilla/5.0 (iPhone; CPU iPhone OS 17_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.2 Mobile/15E148 Safari/604.1',
    ],
    'mobile_android': [
        'Mozilla/5.0 (Linux; Android 14; SM-S918B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Mobile Safari/537.0',
    ],
}
```

---

## Browser Fingerprint Randomization

### WebDriver Detection Evasion

When using Selenium or Playwright, websites can detect automation through JavaScript:

```python
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service

def create_stealth_driver():
    options = Options()
    
    # Basic stealth options
    options.add_argument('--disable-blink-features=AutomationControlled')
    options.add_experimental_option('excludeSwitches', ['enable-automation'])
    options.add_experimental_option('useAutomationExtension', False)
    
    # Random window size (not headless default)
    import random
    width = random.randint(1200, 1920)
    height = random.randint(800, 1080)
    options.add_argument(f'--window-size={width},{height}')
    
    # Other stealth options
    options.add_argument('--disable-web-security')
    options.add_argument('--disable-features=IsolateOrigins,site-per-process')
    options.add_argument('--disable-site-isolation-trials')
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument('--no-sandbox')
    
    driver = webdriver.Chrome(options=options)
    
    # Execute CDP commands to modify navigator.webdriver
    driver.execute_cdp_cmd('Page.addScriptToEvaluateOnNewDocument', {
        'source': '''
            Object.defineProperty(navigator, 'webdriver', {
                get: () => undefined
            });
            
            Object.defineProperty(navigator, 'plugins', {
                get: () => [1, 2, 3, 4, 5]
            });
            
            window.chrome = {
                runtime: {}
            };
        '''
    })
    
    return driver
```

### Playwright Stealth

```python
from playwright.sync_api import sync_playwright

def create_stealth_context(browser):
    """Create context with anti-detection measures"""
    context = browser.new_context(
        viewport={'width': 1920, 'height': 1080},
        user_agent='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36',
        locale='en-US',
        timezone_id='America/New_York',
        
        # Disable automation features
        bypass_csp=True,
        java_script_enabled=True,
        
        # Grant permissions like real user
        permissions=['notifications'],
    )
    
    # Add scripts to evade detection
    context.add_init_script("""
        Object.defineProperty(navigator, 'webdriver', {
            get: () => false,
        });
        
        Object.defineProperty(navigator, 'plugins', {
            get: () => [
                {name: 'Chrome PDF Plugin'},
                {name: 'Native Client'},
                {name: 'Widevine Content Decryption Module'}
            ],
        });
        
        // Fake chrome object
        window.chrome = { runtime: {} };
        
        // Remove Playwright-specific properties
        delete navigator.__proto__.webdriver;
    """)
    
    return context
```

### Using Undetected Chromedriver

```bash
pip install undetected-chromedriver
```

```python
import undetected_chromedriver as uc

def create_undetected_driver():
    options = uc.ChromeOptions()
    options.add_argument('--disable-blink-features=AutomationControlled')
    
    driver = uc.Chrome(options=options)
    return driver
```

### Canvas Fingerprint Randomization

```python
# Inject script to randomize canvas fingerprint
stealth_script = """
const originalToDataURL = HTMLCanvasElement.prototype.toDataURL;
const originalGetImageData = CanvasRenderingContext2D.prototype.getImageData;

// Add subtle noise to canvas operations
CanvasRenderingContext2D.prototype.getImageData = function(...args) {
    const imageData = originalGetImageData.apply(this, args);
    
    // Add imperceptible noise
    for (let i = 0; i < imageData.data.length; i += 4) {
        imageData.data[i] += Math.random() > 0.5 ? 1 : 0;     // R
        imageData.data[i+1] += Math.random() > 0.5 ? 1 : 0;   // G
        imageData.data[i+2] += Math.random() > 0.5 ? 1 : 0;   // B
    }
    
    return imageData;
};
"""

driver.execute_cdp_cmd('Page.addScriptToEvaluateOnNewDocument', {
    'source': stealth_script
})
```

---

## Behavioral Mimicry

### Request Timing Patterns

Humans don't make requests at perfectly regular intervals:

```python
import time
import random

def human_like_delay(min_seconds=1, max_seconds=5):
    """Random delay that mimics human behavior"""
    # Use beta distribution for realistic patterns
    delay = random.betavariate(2, 5) * (max_seconds - min_seconds) + min_seconds
    time.sleep(delay)

def variable_delay_between_actions():
    """Different delays for different actions"""
    delays = {
        'page_load': (2, 5),      # 2-5 seconds after page load
        'scroll': (0.5, 2),       # 0.5-2 seconds between scrolls
        'click': (1, 3),          # 1-3 seconds before clicking
        'form_fill': (0.2, 1),    # 0.2-1 seconds between keystrokes
    }
    return delays
```

### Mouse Movement Simulation

```python
from selenium.webdriver.common.action_chains import ActionChains
import random
import math

def human_like_mouse_move(driver, element):
    """Move mouse to element with human-like curve"""
    action = ActionChains(driver)
    
    # Get element location
    location = element.location
    size = element.size
    target_x = location['x'] + size['width'] / 2
    target_y = location['y'] + size['height'] / 2
    
    # Get current mouse position (approximate)
    current_x = random.randint(0, 1920)
    current_y = random.randint(0, 1080)
    
    # Generate Bezier curve points
    points = generate_bezier_points(
        (current_x, current_y),
        (target_x, target_y),
        num_points=random.randint(10, 20)
    )
    
    # Move through points with variable speed
    for point in points:
        action.move_by_offset(point[0] - current_x, point[1] - current_y)
        action.pause(random.uniform(0.01, 0.05))
        current_x, current_y = point
    
    action.perform()

def generate_bezier_points(start, end, num_points=15):
    """Generate points along a Bezier curve"""
    # Control point creates curve
    control = (
        (start[0] + end[0]) / 2 + random.randint(-100, 100),
        (start[1] + end[1]) / 2 + random.randint(-100, 100)
    )
    
    points = []
    for t in [i / (num_points - 1) for i in range(num_points)]:
        x = (1-t)**2 * start[0] + 2*(1-t)*t * control[0] + t**2 * end[0]
        y = (1-t)**2 * start[1] + 2*(1-t)*t * control[1] + t**2 * end[1]
        points.append((x, y))
    
    return points
```

### Scroll Behavior

```python
def human_like_scroll(driver, direction='down', amount=None):
    """Scroll with human-like behavior"""
    if amount is None:
        amount = random.randint(300, 800)
    
    # Scroll in multiple small movements
    remaining = amount
    while remaining > 0:
        scroll_step = min(remaining, random.randint(50, 150))
        driver.execute_script(f'window.scrollBy(0, {scroll_step});')
        remaining -= scroll_step
        
        # Variable pause between scrolls
        time.sleep(random.uniform(0.1, 0.5))
    
    # Sometimes pause to "read"
    if random.random() < 0.3:
        time.sleep(random.uniform(1, 3))
```

### Form Filling Simulation

```python
def type_like_human(element, text):
    """Type text with human-like timing"""
    for char in text:
        element.send_keys(char)
        # Variable typing speed
        delay = random.gauss(0.1, 0.05)
        delay = max(0.02, min(0.3, delay))  # Clamp between 20ms and 300ms
        time.sleep(delay)
        
        # Occasionally pause (thinking)
        if random.random() < 0.05:
            time.sleep(random.uniform(0.5, 1.5))
```

---

## CAPTCHA Handling

### Types of CAPTCHAs

| Type | Description | Approach |
|------|-------------|----------|
| Image-based | Click on images matching criteria | Avoid or use solving service |
| Text/Character | Type distorted characters | OCR or solving service |
| reCAPTCHA v2 | "I'm not a robot" checkbox | Advanced evasion or solving |
| reCAPTCHA v3 | Invisible scoring | Behavioral mimicry |
| hCaptcha | Image classification | Similar to reCAPTCHA |
| Geetest | Slider puzzles | Specialized solvers |

### Avoiding CAPTCHAs

The best CAPTCHA strategy is avoiding them:

```python
# 1. Use good proxies
residential_proxy = 'http://user:pass@residential.proxy:1234'

# 2. Rotate user agents properly
headers = {'User-Agent': get_realistic_user_agent()}

# 3. Add appropriate delays
time.sleep(random.uniform(2, 5))

# 4. Use session cookies
session = requests.Session()
session.get('https://example.com')  # Get cookies first

# 5. Mimic referrer chain
headers['Referer'] = 'https://google.com/search?q=example'
```

### CAPTCHA Solving Services

When avoidance fails, use solving services:

```python
# 2Captcha integration
import requests

def solve_recaptcha(site_key, page_url, api_key):
    """Submit CAPTCHA to 2Captcha"""
    
    # Submit CAPTCHA
    submit_url = 'http://2captcha.com/in.php'
    data = {
        'key': api_key,
        'method': 'userrecaptcha',
        'googlekey': site_key,
        'pageurl': page_url,
        'json': 1
    }
    
    response = requests.post(submit_url, data=data)
    result = response.json()
    
    if result['status'] != 1:
        raise Exception(f"CAPTCHA submit failed: {result['request']}")
    
    captcha_id = result['request']
    
    # Poll for result
    result_url = f'http://2captcha.com/res.php?key={api_key}&action=get&id={captcha_id}&json=1'
    
    for _ in range(30):  # Try for 5 minutes
        time.sleep(10)
        response = requests.get(result_url)
        result = response.json()
        
        if result['status'] == 1:
            return result['request']  # The solution token
    
    raise Exception("CAPTCHA solving timeout")
```

### Playwright with reCAPTCHA

```python
from playwright.sync_api import sync_playwright

def handle_recaptcha(page, api_key):
    """Handle reCAPTCHA detection and solving"""
    
    # Check if reCAPTCHA is present
    recaptcha_frame = page.query_selector('iframe[src*="recaptcha"]')
    
    if recaptcha_frame:
        # Get site key
        site_key = page.evaluate('''() => {
            const el = document.querySelector('.g-recaptcha');
            return el ? el.getAttribute('data-sitekey') : null;
        }''')
        
        if site_key:
            # Solve CAPTCHA
            solution = solve_recaptcha(site_key, page.url, api_key)
            
            # Inject solution
            page.evaluate(f'''(token) => {{
                document.getElementById('g-recaptcha-response').innerHTML = token;
            }}''', solution)
            
            return True
    
    return False
```

---

## Session Management

### Cookie Persistence

```python
import pickle
import os

class PersistentSession:
    def __init__(self, cookie_file='cookies.pkl'):
        self.session = requests.Session()
        self.cookie_file = cookie_file
        self.load_cookies()
    
    def load_cookies(self):
        if os.path.exists(self.cookie_file):
            with open(self.cookie_file, 'rb') as f:
                cookies = pickle.load(f)
                self.session.cookies.update(cookies)
    
    def save_cookies(self):
        with open(self.cookie_file, 'wb') as f:
            pickle.dump(self.session.cookies, f)
    
    def get(self, url, **kwargs):
        response = self.session.get(url, **kwargs)
        self.save_cookies()
        return response
```

### Realistic Session Flow

```python
class RealisticSession:
    def __init__(self):
        self.session = requests.Session()
        self.visited_pages = []
        self.current_page = None
    
    def visit(self, url, referer=None):
        """Visit page with realistic headers"""
        headers = {
            'User-Agent': get_random_user_agent(),
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            'Accept-Language': 'en-US,en;q=0.5',
            'Accept-Encoding': 'gzip, deflate, br',
            'DNT': '1',
            'Connection': 'keep-alive',
            'Upgrade-Insecure-Requests': '1',
        }
        
        if referer or self.current_page:
            headers['Referer'] = referer or self.current_page
        
        response = self.session.get(url, headers=headers)
        
        self.visited_pages.append(url)
        self.current_page = url
        
        return response
    
    def click_link(self, link_url):
        """Click link from current page"""
        return self.visit(link_url, referer=self.current_page)
```

---

## Advanced Evasion Techniques

### DNS Resolution Rotation

```python
import socket
import dns.resolver

def rotate_dns_servers():
    """Use different DNS servers to resolve domains"""
    dns_servers = [
        '8.8.8.8',      # Google
        '1.1.1.1',      # Cloudflare
        '9.9.9.9',      # Quad9
    ]
    
    resolver = dns.resolver.Resolver()
    resolver.nameservers = [random.choice(dns_servers)]
    
    return resolver
```

### TLS Fingerprint Evasion

```python
# Using curl_cffi for matching browser TLS
from curl_cffi import requests

# Matches Chrome 110 TLS fingerprint
response = requests.get(
    'https://example.com',
    impersonate="chrome110"
)
```

### WebGL and Canvas Evasion

```python
stealth_script = """
// Override WebGL parameters
const getParameter = WebGLRenderingContext.prototype.getParameter;
WebGLRenderingContext.prototype.getParameter = function(parameter) {
    // UNMASKED_VENDOR_WEBGL
    if (parameter === 37445) {
        return 'Intel Inc.';
    }
    // UNMASKED_RENDERER_WEBGL
    if (parameter === 37446) {
        return 'Intel Iris OpenGL Engine';
    }
    return getParameter(parameter);
};

// Randomize canvas fingerprint subtly
const toDataURL = HTMLCanvasElement.prototype.toDataURL;
HTMLCanvasElement.prototype.toDataURL = function(...args) {
    const result = toDataURL.apply(this, args);
    // Could add subtle modifications here
    return result;
};
"""
```

### Font Fingerprint Protection

```python
stealth_script += """
// Add common fonts that might be missing in headless
Object.defineProperty(document, 'fonts', {
    get: () => ({
        check: () => true,
        load: () => Promise.resolve(),
        ready: Promise.resolve(),
    }),
});
"""
```

---

## Testing and Validation

### Bot Detection Testing

```python
def test_stealth(driver):
    """Test if bot detection is evaded"""
    
    # Test navigator.webdriver
    webdriver_detected = driver.execute_script('return navigator.webdriver;')
    print(f"navigator.webdriver: {webdriver_detected}")
    
    # Test plugins
    plugins = driver.execute_script('return navigator.plugins.length;')
    print(f"navigator.plugins.length: {plugins}")
    
    # Test chrome object
    has_chrome = driver.execute_script('return !!window.chrome;')
    print(f"window.chrome exists: {has_chrome}")
    
    # Test permissions
    permissions = driver.execute_script('''
        return navigator.permissions.query({name: 'notifications'})
            .then(p => p.state);
    ''')
    print(f"Permissions query works: {permissions}")
    
    # Visit bot detection test site
    driver.get('https://bot.sannysoft.com/')
    time.sleep(5)
    driver.save_screenshot('bot_test.png')
```

### Fingerprint Consistency Check

```python
def check_fingerprint_consistency(driver):
    """Verify fingerprint is consistent"""
    
    checks = {
        'user_agent': driver.execute_script('return navigator.userAgent;'),
        'platform': driver.execute_script('return navigator.platform;'),
        'language': driver.execute_script('return navigator.language;'),
        'hardware_concurrency': driver.execute_script('return navigator.hardwareConcurrency;'),
        'max_touch_points': driver.execute_script('return navigator.maxTouchPoints;'),
    }
    
    # Verify User-Agent matches platform
    if 'Win' in checks['user_agent'] and 'Win' not in checks['platform']:
        print("WARNING: User-Agent/Platform mismatch")
    
    if 'Mac' in checks['user_agent'] and 'Mac' not in checks['platform']:
        print("WARNING: User-Agent/Platform mismatch")
    
    return checks
```

---

## Ethical and Legal Considerations

### Respecting robots.txt

```python
from urllib.robotparser import RobotFileParser

def check_robots_txt(url):
    """Check if URL is allowed by robots.txt"""
    rp = RobotFileParser()
    rp.set_url(urljoin(url, '/robots.txt'))
    rp.read()
    
    return rp.can_fetch('*', url)
```

### Rate Limiting Best Practices

```python
class EthicalScraper:
    def __init__(self, requests_per_second=1):
        self.min_delay = 1 / requests_per_second
        self.last_request_time = 0
    
    def request(self, url):
        # Ensure minimum delay
        elapsed = time.time() - self.last_request_time
        if elapsed < self.min_delay:
            time.sleep(self.min_delay - elapsed)
        
        # Respect robots.txt
        if not check_robots_txt(url):
            raise Exception(f"URL blocked by robots.txt: {url}")
        
        response = requests.get(url)
        self.last_request_time = time.time()
        
        return response
```

### Terms of Service Compliance

Always review website Terms of Service before scraping:

1. Check if scraping is explicitly prohibited
2. Understand data usage restrictions
3. Comply with copyright and trademark laws
4. Respect data protection regulations (GDPR, CCPA)

---

## Conclusion

Anti-detection is a sophisticated field requiring constant adaptation as detection technologies evolve. The techniques in this chapter provide a foundation for evading most common bot detection systems while maintaining ethical scraping practices.

**Key takeaways:**
- Use rotating proxies and user agents for basic evasion
- Employ headless browsers with stealth patches for advanced sites
- Mimic human behavior through timing, mouse movements, and scroll patterns
- Consider CAPTCHA solving services as a last resort
- Always test your evasion techniques before production deployment
- Respect robots.txt and website terms of service

Remember: The goal is not to maliciously attack websites but to access publicly available data responsibly. When in doubt, contact the website owner for API access or permission to scrape.
