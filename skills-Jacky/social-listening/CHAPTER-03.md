# Chapter 3: Data Collection Architecture

## Introduction

Building a robust data collection architecture is the foundation of any successful social listening system. The way you design your data collection pipeline directly impacts your ability to gather insights, respond to trends in real-time, and maintain operational efficiency at scale. This chapter dives deep into the technical architecture required to build production-grade social listening systems that can handle millions of data points daily while remaining cost-effective and maintainable.

The data collection architecture for social listening is fundamentally different from traditional web scraping or data warehousing. Social media platforms generate data at an unprecedented velocity—Twitter alone processes over 500 million tweets daily, while Facebook sees over 4 billion interactions per day. Your architecture must be designed to handle this volume while respecting API rate limits, managing costs, and ensuring data quality.

In this chapter, we'll explore the complete spectrum of data collection strategies, from real-time streaming to batch processing, and show you how to build systems that combine both approaches for optimal results. We'll cover the intricacies of API rate limiting and quota management, showing you how to maximize your data collection while staying within platform constraints. You'll learn how to set up webhook-based systems for instant notifications, build scalable data pipelines, design storage architectures that handle time-series data efficiently, and prepare your systems to handle the inevitable API changes and deprecations that all platforms introduce over time.

## Real-Time vs Batch Collection Strategies

### Understanding the Fundamental Difference

The choice between real-time and batch collection strategies represents one of the most critical architectural decisions in social listening systems. Each approach serves different use cases, comes with distinct trade-offs, and requires different technical infrastructure.

**Real-time collection** (also called streaming or continuous collection) involves maintaining persistent connections to social media APIs and processing data as it arrives. This approach provides immediate access to new content, enabling use cases like crisis management, real-time customer service, breaking news detection, and competitive intelligence where timing is critical.

**Batch collection** involves periodically querying APIs for data that was created since your last collection cycle. This approach is simpler to implement, easier to debug, more predictable in resource usage, and often more cost-effective for use cases where immediate data isn't required.

Most production social listening systems use a hybrid approach, combining real-time streaming for high-priority content with batch collection for comprehensive historical analysis and less time-sensitive monitoring.

### Real-Time Collection Architecture

Real-time collection systems are built around maintaining persistent connections to platform APIs and processing incoming data streams continuously. Let's explore the components and implementation patterns for effective real-time collection.

#### WebSocket-Based Streaming

Many modern social platforms provide WebSocket connections for real-time data delivery. Here's a robust implementation pattern for Twitter's streaming API:

```python
import websocket
import json
import time
import threading
from queue import Queue
from typing import Callable, Optional
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class TwitterStreamCollector:
    """
    Robust real-time collector for Twitter streaming API with
    automatic reconnection, error handling, and backpressure management.
    """
    
    def __init__(
        self,
        bearer_token: str,
        rules: list[dict],
        callback: Callable[[dict], None],
        max_queue_size: int = 10000
    ):
        self.bearer_token = bearer_token
        self.rules = rules
        self.callback = callback
        self.max_queue_size = max_queue_size
        
        self.data_queue = Queue(maxsize=max_queue_size)
        self.ws = None
        self.running = False
        self.reconnect_delay = 1
        self.max_reconnect_delay = 300
        
    def start(self):
        """Start the streaming collector with automatic reconnection."""
        self.running = True
        
        # Start processing thread
        processor_thread = threading.Thread(target=self._process_queue)
        processor_thread.daemon = True
        processor_thread.start()
        
        # Start connection with reconnection logic
        while self.running:
            try:
                self._connect_and_stream()
            except Exception as e:
                logger.error(f"Stream error: {e}")
                if self.running:
                    logger.info(f"Reconnecting in {self.reconnect_delay}s...")
                    time.sleep(self.reconnect_delay)
                    # Exponential backoff for reconnection
                    self.reconnect_delay = min(
                        self.reconnect_delay * 2,
                        self.max_reconnect_delay
                    )
    
    def _connect_and_stream(self):
        """Establish WebSocket connection and stream data."""
        url = "wss://api.twitter.com/2/tweets/stream"
        
        self.ws = websocket.WebSocketApp(
            url,
            header={
                "Authorization": f"Bearer {self.bearer_token}"
            },
            on_message=self._on_message,
            on_error=self._on_error,
            on_close=self._on_close,
            on_open=self._on_open
        )
        
        self.ws.run_forever()
    
    def _on_open(self, ws):
        """Handle connection open."""
        logger.info("Stream connection established")
        self.reconnect_delay = 1  # Reset reconnection delay
    
    def _on_message(self, ws, message):
        """Handle incoming messages with backpressure management."""
        try:
            data = json.loads(message)
            
            # Skip heartbeat messages
            if not data or 'data' not in data:
                return
            
            # Check queue capacity for backpressure
            if self.data_queue.qsize() >= self.max_queue_size * 0.9:
                logger.warning(
                    f"Queue near capacity: {self.data_queue.qsize()}/{self.max_queue_size}"
                )
            
            # Add to processing queue (non-blocking)
            try:
                self.data_queue.put_nowait(data)
            except:
                logger.error("Queue full, dropping message")
                
        except json.JSONDecodeError as e:
            logger.error(f"Failed to parse message: {e}")
    
    def _on_error(self, ws, error):
        """Handle WebSocket errors."""
        logger.error(f"WebSocket error: {error}")
    
    def _on_close(self, ws, close_status_code, close_msg):
        """Handle connection close."""
        logger.info(f"Connection closed: {close_status_code} - {close_msg}")
    
    def _process_queue(self):
        """Process queued messages in separate thread."""
        while self.running:
            try:
                # Get message from queue with timeout
                data = self.data_queue.get(timeout=1)
                
                # Process with callback
                try:
                    self.callback(data)
                except Exception as e:
                    logger.error(f"Callback error: {e}")
                
                self.data_queue.task_done()
                
            except:
                continue  # Timeout, check if still running
    
    def stop(self):
        """Gracefully stop the collector."""
        logger.info("Stopping collector...")
        self.running = False
        if self.ws:
            self.ws.close()
        
        # Wait for queue to empty
        self.data_queue.join()
        logger.info("Collector stopped")


# Usage example
def process_tweet(tweet_data: dict):
    """Process incoming tweet data."""
    tweet = tweet_data['data']
    print(f"New tweet: {tweet['text'][:100]}...")
    
    # Store in database, trigger alerts, etc.
    # store_tweet(tweet)
    # check_sentiment_alerts(tweet)

collector = TwitterStreamCollector(
    bearer_token="your_bearer_token",
    rules=[
        {"value": "brand_name", "tag": "brand_mentions"},
        {"value": "competitor_name", "tag": "competitor_tracking"}
    ],
    callback=process_tweet
)

# Start streaming in background
import threading
stream_thread = threading.Thread(target=collector.start)
stream_thread.daemon = True
stream_thread.start()
```

This implementation includes several production-ready features:

1. **Automatic Reconnection**: If the connection drops, it automatically reconnects with exponential backoff to avoid hammering the API
2. **Backpressure Management**: Monitors queue size and warns when approaching capacity
3. **Graceful Shutdown**: Ensures all queued messages are processed before stopping
4. **Error Isolation**: Callback errors don't crash the collector
5. **Thread Safety**: Separate threads for receiving and processing data

#### Server-Sent Events (SSE) Streaming

Some platforms use Server-Sent Events instead of WebSockets. Here's an implementation for SSE-based streaming:

```python
import requests
import json
import time
from typing import Callable, Optional
import logging
from threading import Thread, Event

logger = logging.getLogger(__name__)

class SSEStreamCollector:
    """
    Server-Sent Events stream collector with reconnection logic.
    """
    
    def __init__(
        self,
        api_url: str,
        headers: dict,
        callback: Callable[[dict], None],
        reconnect_delay: int = 5
    ):
        self.api_url = api_url
        self.headers = headers
        self.callback = callback
        self.reconnect_delay = reconnect_delay
        
        self.running = Event()
        self.thread = None
    
    def start(self):
        """Start streaming in background thread."""
        self.running.set()
        self.thread = Thread(target=self._stream_loop)
        self.thread.daemon = True
        self.thread.start()
    
    def _stream_loop(self):
        """Main streaming loop with reconnection."""
        while self.running.is_set():
            try:
                self._connect_and_stream()
            except Exception as e:
                logger.error(f"Stream error: {e}")
                if self.running.is_set():
                    time.sleep(self.reconnect_delay)
    
    def _connect_and_stream(self):
        """Connect to SSE endpoint and process events."""
        with requests.get(
            self.api_url,
            headers=self.headers,
            stream=True,
            timeout=90
        ) as response:
            response.raise_for_status()
            
            logger.info("SSE connection established")
            
            # Process Server-Sent Events
            buffer = ""
            for chunk in response.iter_content(chunk_size=None, decode_unicode=True):
                if not self.running.is_set():
                    break
                
                buffer += chunk
                
                # SSE messages are separated by double newlines
                while "\n\n" in buffer:
                    message, buffer = buffer.split("\n\n", 1)
                    self._process_sse_message(message)
    
    def _process_sse_message(self, message: str):
        """Parse and process SSE message."""
        # SSE format: "data: {...}\n"
        lines = message.strip().split("\n")
        for line in lines:
            if line.startswith("data:"):
                data_str = line[5:].strip()
                
                # Skip heartbeat messages
                if not data_str:
                    continue
                
                try:
                    data = json.loads(data_str)
                    self.callback(data)
                except json.JSONDecodeError:
                    logger.error(f"Failed to parse SSE data: {data_str}")
                except Exception as e:
                    logger.error(f"Callback error: {e}")
    
    def stop(self):
        """Stop streaming."""
        logger.info("Stopping SSE collector...")
        self.running.clear()
        if self.thread:
            self.thread.join(timeout=5)
```

#### Real-Time Collection Best Practices

When implementing real-time collection, follow these best practices:

**1. Monitor Stream Health**

```python
class StreamHealthMonitor:
    """Monitor stream health and alert on anomalies."""
    
    def __init__(self, expected_messages_per_minute: int = 100):
        self.expected_rate = expected_messages_per_minute
        self.message_count = 0
        self.last_message_time = time.time()
        self.last_check_time = time.time()
    
    def record_message(self):
        """Record that a message was received."""
        self.message_count += 1
        self.last_message_time = time.time()
    
    def check_health(self) -> dict:
        """Check stream health and return status."""
        now = time.time()
        time_since_message = now - self.last_message_time
        time_since_check = now - self.last_check_time
        
        # Calculate actual rate
        actual_rate = (self.message_count / time_since_check) * 60
        
        health = {
            "status": "healthy",
            "messages_per_minute": actual_rate,
            "seconds_since_last_message": time_since_message
        }
        
        # Check for stalled stream
        if time_since_message > 300:  # 5 minutes
            health["status"] = "stalled"
            health["alert"] = "No messages received in 5 minutes"
        
        # Check for low message rate
        elif actual_rate < self.expected_rate * 0.5:
            health["status"] = "degraded"
            health["alert"] = f"Message rate below expected: {actual_rate:.1f} vs {self.expected_rate}"
        
        # Reset counters
        self.message_count = 0
        self.last_check_time = now
        
        return health
```

**2. Implement Circuit Breakers**

```python
from enum import Enum
import time

class CircuitState(Enum):
    CLOSED = "closed"  # Normal operation
    OPEN = "open"      # Too many failures, not attempting
    HALF_OPEN = "half_open"  # Testing if service recovered

class CircuitBreaker:
    """
    Circuit breaker pattern for stream connections.
    Prevents repeated connection attempts when service is down.
    """
    
    def __init__(
        self,
        failure_threshold: int = 5,
        recovery_timeout: int = 60,
        success_threshold: int = 2
    ):
        self.failure_threshold = failure_threshold
        self.recovery_timeout = recovery_timeout
        self.success_threshold = success_threshold
        
        self.failure_count = 0
        self.success_count = 0
        self.last_failure_time = None
        self.state = CircuitState.CLOSED
    
    def record_success(self):
        """Record successful operation."""
        self.failure_count = 0
        
        if self.state == CircuitState.HALF_OPEN:
            self.success_count += 1
            if self.success_count >= self.success_threshold:
                self.state = CircuitState.CLOSED
                self.success_count = 0
                logger.info("Circuit breaker closed - service recovered")
    
    def record_failure(self):
        """Record failed operation."""
        self.failure_count += 1
        self.last_failure_time = time.time()
        self.success_count = 0
        
        if self.failure_count >= self.failure_threshold:
            self.state = CircuitState.OPEN
            logger.warning("Circuit breaker opened - too many failures")
    
    def can_attempt(self) -> bool:
        """Check if we should attempt the operation."""
        if self.state == CircuitState.CLOSED:
            return True
        
        if self.state == CircuitState.OPEN:
            # Check if recovery timeout has passed
            if time.time() - self.last_failure_time >= self.recovery_timeout:
                self.state = CircuitState.HALF_OPEN
                logger.info("Circuit breaker half-open - testing service")
                return True
            return False
        
        # HALF_OPEN state
        return True
    
    def get_state(self) -> str:
        """Get current circuit state."""
        return self.state.value
```

### Batch Collection Architecture

Batch collection is often the right choice for comprehensive historical analysis, trend detection, and scenarios where real-time data isn't critical. It's also more cost-effective and easier to maintain for many use cases.

#### Scheduled Batch Collection

Here's a robust batch collection system with retry logic and rate limiting:

```python
import time
import requests
from typing import List, Dict, Optional
from datetime import datetime, timedelta
import logging
from dataclasses import dataclass
from enum import Enum

logger = logging.getLogger(__name__)

class CollectionStatus(Enum):
    SUCCESS = "success"
    PARTIAL = "partial"
    FAILED = "failed"
    RATE_LIMITED = "rate_limited"

@dataclass
class CollectionResult:
    status: CollectionStatus
    items_collected: int
    errors: List[str]
    rate_limit_reset: Optional[datetime]
    next_cursor: Optional[str]

class BatchCollector:
    """
    Batch collector with pagination, rate limiting, and retry logic.
    """
    
    def __init__(
        self,
        api_key: str,
        base_url: str,
        rate_limit_per_minute: int = 15,
        max_retries: int = 3
    ):
        self.api_key = api_key
        self.base_url = base_url
        self.rate_limit_per_minute = rate_limit_per_minute
        self.max_retries = max_retries
        
        # Track API calls for rate limiting
        self.api_calls = []
        self.session = requests.Session()
        self.session.headers.update({
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json"
        })
    
    def collect_batch(
        self,
        endpoint: str,
        params: dict,
        max_items: Optional[int] = None
    ) -> CollectionResult:
        """
        Collect a batch of data with pagination and rate limiting.
        """
        items = []
        errors = []
        cursor = None
        
        while True:
            # Check if we've collected enough
            if max_items and len(items) >= max_items:
                break
            
            # Wait for rate limit if needed
            self._wait_for_rate_limit()
            
            # Prepare request
            request_params = params.copy()
            if cursor:
                request_params['cursor'] = cursor
            
            # Make request with retry logic
            result = self._make_request_with_retry(endpoint, request_params)
            
            if result['status'] == CollectionStatus.RATE_LIMITED:
                return CollectionResult(
                    status=CollectionStatus.RATE_LIMITED,
                    items_collected=len(items),
                    errors=errors,
                    rate_limit_reset=result['rate_limit_reset'],
                    next_cursor=cursor
                )
            
            if result['status'] == CollectionStatus.FAILED:
                errors.extend(result['errors'])
                # Decide whether to continue or abort
                if len(errors) > 5:  # Too many errors
                    return CollectionResult(
                        status=CollectionStatus.FAILED,
                        items_collected=len(items),
                        errors=errors,
                        rate_limit_reset=None,
                        next_cursor=cursor
                    )
                continue  # Try next page
            
            # Process successful response
            batch_items = result['data']
            items.extend(batch_items)
            
            # Check for next page
            cursor = result.get('next_cursor')
            if not cursor or not batch_items:
                break  # No more pages
        
        status = CollectionStatus.SUCCESS
        if errors:
            status = CollectionStatus.PARTIAL
        
        return CollectionResult(
            status=status,
            items_collected=len(items),
            errors=errors,
            rate_limit_reset=None,
            next_cursor=None
        )
    
    def _make_request_with_retry(
        self,
        endpoint: str,
        params: dict
    ) -> dict:
        """Make API request with exponential backoff retry."""
        url = f"{self.base_url}/{endpoint}"
        
        for attempt in range(self.max_retries):
            try:
                response = self.session.get(url, params=params, timeout=30)
                
                # Record API call for rate limiting
                self.api_calls.append(time.time())
                
                # Handle rate limiting
                if response.status_code == 429:
                    reset_time = self._parse_rate_limit_reset(response)
                    logger.warning(f"Rate limited. Reset at: {reset_time}")
                    return {
                        'status': CollectionStatus.RATE_LIMITED,
                        'rate_limit_reset': reset_time
                    }
                
                # Handle other errors
                response.raise_for_status()
                
                # Parse response
                data = response.json()
                return {
                    'status': CollectionStatus.SUCCESS,
                    'data': data.get('data', []),
                    'next_cursor': data.get('meta', {}).get('next_cursor')
                }
                
            except requests.exceptions.Timeout:
                logger.warning(f"Request timeout (attempt {attempt + 1}/{self.max_retries})")
                if attempt < self.max_retries - 1:
                    time.sleep(2 ** attempt)  # Exponential backoff
                continue
                
            except requests.exceptions.RequestException as e:
                logger.error(f"Request error: {e}")
                if attempt < self.max_retries - 1:
                    time.sleep(2 ** attempt)
                    continue
                return {
                    'status': CollectionStatus.FAILED,
                    'errors': [str(e)]
                }
        
        return {
            'status': CollectionStatus.FAILED,
            'errors': ['Max retries exceeded']
        }
    
    def _wait_for_rate_limit(self):
        """Wait if we're approaching rate limit."""
        now = time.time()
        minute_ago = now - 60
        
        # Remove old API calls
        self.api_calls = [t for t in self.api_calls if t > minute_ago]
        
        # Wait if we're at the limit
        if len(self.api_calls) >= self.rate_limit_per_minute:
            oldest_call = min(self.api_calls)
            wait_time = 60 - (now - oldest_call)
            if wait_time > 0:
                logger.info(f"Rate limit reached, waiting {wait_time:.1f}s")
                time.sleep(wait_time)
    
    def _parse_rate_limit_reset(self, response: requests.Response) -> Optional[datetime]:
        """Parse rate limit reset time from response headers."""
        reset_timestamp = response.headers.get('X-Rate-Limit-Reset')
        if reset_timestamp:
            return datetime.fromtimestamp(int(reset_timestamp))
        return None


# Usage example
collector = BatchCollector(
    api_key="your_api_key",
    base_url="https://api.platform.com/v1",
    rate_limit_per_minute=15
)

result = collector.collect_batch(
    endpoint="search/tweets",
    params={
        "query": "brand_name",
        "start_time": "2024-01-01T00:00:00Z",
        "max_results": 100
    },
    max_items=10000
)

print(f"Collected {result.items_collected} items")
if result.errors:
    print(f"Errors: {result.errors}")
```

#### Incremental Collection Strategy

For batch collection, implementing incremental updates is crucial to avoid re-collecting the same data:

```python
from datetime import datetime, timedelta
from typing import Optional
import json
import os

class IncrementalCollector:
    """
    Manages incremental batch collection with checkpoint persistence.
    """
    
    def __init__(
        self,
        collector: BatchCollector,
        checkpoint_file: str = "checkpoints.json"
    ):
        self.collector = collector
        self.checkpoint_file = checkpoint_file
        self.checkpoints = self._load_checkpoints()
    
    def _load_checkpoints(self) -> dict:
        """Load checkpoints from file."""
        if os.path.exists(self.checkpoint_file):
            with open(self.checkpoint_file, 'r') as f:
                return json.load(f)
        return {}
    
    def _save_checkpoints(self):
        """Save checkpoints to file."""
        with open(self.checkpoint_file, 'w') as f:
            json.dump(self.checkpoints, f, indent=2)
    
    def collect_since_last(
        self,
        collection_id: str,
        endpoint: str,
        base_params: dict,
        default_lookback_hours: int = 24
    ) -> CollectionResult:
        """
        Collect data since last successful collection.
        """
        # Get last collection time
        last_collection = self.checkpoints.get(collection_id, {})
        last_time = last_collection.get('last_success_time')
        
        if last_time:
            start_time = datetime.fromisoformat(last_time)
        else:
            # First collection - use default lookback
            start_time = datetime.utcnow() - timedelta(hours=default_lookback_hours)
        
        # Prepare parameters
        params = base_params.copy()
        params['start_time'] = start_time.isoformat() + 'Z'
        params['end_time'] = datetime.utcnow().isoformat() + 'Z'
        
        logger.info(f"Collecting {collection_id} from {start_time}")
        
        # Perform collection
        result = self.collector.collect_batch(endpoint, params)
        
        # Update checkpoint on success
        if result.status in [CollectionStatus.SUCCESS, CollectionStatus.PARTIAL]:
            self.checkpoints[collection_id] = {
                'last_success_time': datetime.utcnow().isoformat(),
                'items_collected': result.items_collected,
                'last_status': result.status.value
            }
            self._save_checkpoints()
            logger.info(f"Checkpoint saved for {collection_id}")
        
        return result
    
    def get_collection_stats(self, collection_id: str) -> Optional[dict]:
        """Get statistics for a collection."""
        return self.checkpoints.get(collection_id)


# Usage in scheduled job
incremental = IncrementalCollector(collector)

# This can be run hourly/daily via cron
result = incremental.collect_since_last(
    collection_id="brand_mentions_twitter",
    endpoint="search/tweets",
    base_params={
        "query": "brand_name -is:retweet",
        "max_results": 100
    },
    default_lookback_hours=24
)
```

### Hybrid Collection Strategy

Most production systems benefit from combining real-time and batch collection:

```python
class HybridCollector:
    """
    Combines real-time streaming for priority content with
    batch collection for comprehensive coverage.
    """
    
    def __init__(
        self,
        stream_collector: TwitterStreamCollector,
        batch_collector: IncrementalCollector,
        priority_keywords: List[str]
    ):
        self.stream_collector = stream_collector
        self.batch_collector = batch_collector
        self.priority_keywords = priority_keywords
        
        # Track what we've seen in stream to avoid duplicates in batch
        self.stream_seen_ids = set()
        self.max_seen_ids = 100000
    
    def start_streaming(self):
        """Start real-time collection for priority keywords."""
        def stream_callback(data):
            item_id = data['data']['id']
            self.stream_seen_ids.add(item_id)
            
            # Trim set if it gets too large
            if len(self.stream_seen_ids) > self.max_seen_ids:
                # Remove oldest 20%
                remove_count = self.max_seen_ids // 5
                self.stream_seen_ids = set(
                    list(self.stream_seen_ids)[remove_count:]
                )
            
            # Process high-priority item immediately
            self._process_priority_item(data)
        
        self.stream_collector.callback = stream_callback
        self.stream_collector.start()
    
    def run_batch_collection(self):
        """Run batch collection for comprehensive coverage."""
        result = self.batch_collector.collect_since_last(
            collection_id="comprehensive_collection",
            endpoint="search/tweets",
            base_params={
                "query": "brand_name OR related_term",
                "max_results": 100
            }
        )
        
        # Filter out items we already saw in stream
        new_items = [
            item for item in result.items_collected
            if item['id'] not in self.stream_seen_ids
        ]
        
        logger.info(f"Batch collected {len(new_items)} new items")
        
        # Process batch items (lower priority)
        for item in new_items:
            self._process_batch_item(item)
    
    def _process_priority_item(self, item: dict):
        """Process high-priority items from stream."""
        # Immediate alerts, sentiment analysis, etc.
        pass
    
    def _process_batch_item(self, item: dict):
        """Process items from batch collection."""
        # Aggregate analytics, trend detection, etc.
        pass
```

## API Rate Limiting and Quota Management

Rate limiting is one of the most critical aspects of building production social listening systems. Every social media platform enforces rate limits to protect their infrastructure and ensure fair usage. Mismanaging rate limits leads to collection gaps, blocked accounts, and failed monitoring campaigns.

### Understanding Rate Limit Types

Different platforms implement rate limiting in different ways:

**1. Request-Based Limits**: Maximum number of requests per time window (e.g., "15 requests per 15 minutes")

**2. Resource-Based Limits**: Maximum resources consumed per time window (e.g., "Tweet cap of 500,000 per month")

**3. Concurrent Connection Limits**: Maximum simultaneous connections (e.g., "1 streaming connection per app")

**4. User-Based Limits**: Limits tied to user tokens vs app tokens

**5. Endpoint-Specific Limits**: Different limits for different API endpoints

### Advanced Rate Limiter Implementation

Here's a production-grade rate limiter that handles multiple limit types:

```python
from collections import deque
from dataclasses import dataclass
from datetime import datetime, timedelta
from typing import Dict, Optional
import time
import threading
import logging

logger = logging.getLogger(__name__)

@dataclass
class RateLimit:
    """Configuration for a rate limit."""
    max_requests: int
    window_seconds: int
    name: str

@dataclass
class RateLimitStatus:
    """Current status of a rate limit."""
    remaining: int
    reset_time: datetime
    limit: RateLimit

class MultiTierRateLimiter:
    """
    Advanced rate limiter supporting multiple concurrent limits.
    Handles per-endpoint, per-user, and global rate limits.
    """
    
    def __init__(self):
        self.limits: Dict[str, RateLimit] = {}
        self.request_history: Dict[str, deque] = {}
        self.locks: Dict[str, threading.Lock] = {}
        self.global_lock = threading.Lock()
    
    def register_limit(self, limit: RateLimit):
        """Register a rate limit to enforce."""
        self.limits[limit.name] = limit
        self.request_history[limit.name] = deque()
        self.locks[limit.name] = threading.Lock()
        logger.info(f"Registered rate limit: {limit.name} - {limit.max_requests}/{limit.window_seconds}s")
    
    def wait_for_capacity(self, limit_names: list[str]) -> Dict[str, RateLimitStatus]:
        """
        Wait until all specified limits have capacity.
        Returns status of all checked limits.
        """
        while True:
            statuses = {}
            needs_wait = False
            min_wait_time = None
            
            for limit_name in limit_names:
                status = self.check_limit(limit_name)
                statuses[limit_name] = status
                
                if status.remaining <= 0:
                    needs_wait = True
                    wait_time = (status.reset_time - datetime.utcnow()).total_seconds()
                    if min_wait_time is None or wait_time < min_wait_time:
                        min_wait_time = wait_time
            
            if not needs_wait:
                # All limits have capacity
                for limit_name in limit_names:
                    self.record_request(limit_name)
                return statuses
            
            # Wait for soonest reset
            if min_wait_time > 0:
                logger.info(f"Rate limit reached, waiting {min_wait_time:.1f}s")
                time.sleep(min_wait_time)
    
    def check_limit(self, limit_name: str) -> RateLimitStatus:
        """Check status of a rate limit without recording request."""
        if limit_name not in self.limits:
            raise ValueError(f"Unknown rate limit: {limit_name}")
        
        limit = self.limits[limit_name]
        
        with self.locks[limit_name]:
            history = self.request_history[limit_name]
            now = datetime.utcnow()
            window_start = now - timedelta(seconds=limit.window_seconds)
            
            # Remove old requests outside window
            while history and history[0] < window_start:
                history.popleft()
            
            # Calculate remaining capacity
            remaining = limit.max_requests - len(history)
            
            # Calculate reset time
            if history:
                reset_time = history[0] + timedelta(seconds=limit.window_seconds)
            else:
                reset_time = now
            
            return RateLimitStatus(
                remaining=remaining,
                reset_time=reset_time,
                limit=limit
            )
    
    def record_request(self, limit_name: str):
        """Record that a request was made."""
        with self.locks[limit_name]:
            self.request_history[limit_name].append(datetime.utcnow())
    
    def get_all_statuses(self) -> Dict[str, RateLimitStatus]:
        """Get status of all registered limits."""
        return {
            name: self.check_limit(name)
            for name in self.limits.keys()
        }


# Example: Twitter API v2 rate limits
rate_limiter = MultiTierRateLimiter()

# Register different limits
rate_limiter.register_limit(RateLimit(
    name="search_tweets",
    max_requests=300,
    window_seconds=900  # 15 minutes
))

rate_limiter.register_limit(RateLimit(
    name="user_tweets",
    max_requests=900,
    window_seconds=900
))

rate_limiter.register_limit(RateLimit(
    name="global_app",
    max_requests=1000,
    window_seconds=60  # Per minute global limit
))

# Usage in API client
def make_api_request(endpoint: str, params: dict):
    # Determine which limits apply to this request
    limit_names = ["global_app"]
    if endpoint == "search/tweets":
        limit_names.append("search_tweets")
    elif endpoint == "users/{id}/tweets":
        limit_names.append("user_tweets")
    
    # Wait for capacity
    statuses = rate_limiter.wait_for_capacity(limit_names)
    
    # Log remaining capacity
    for name, status in statuses.items():
        logger.debug(f"{name}: {status.remaining} remaining")
    
    # Make the actual API request
    return requests.get(f"https://api.twitter.com/2/{endpoint}", params=params)
```

### Dynamic Rate Limit Adjustment

Some platforms return rate limit information in response headers. Here's how to dynamically adjust:

```python
class DynamicRateLimiter:
    """
    Rate limiter that adjusts based on API response headers.
    """
    
    def __init__(self, initial_limit: RateLimit):
        self.current_limit = initial_limit
        self.lock = threading.Lock()
        self.last_requests = deque(maxlen=initial_limit.max_requests)
    
    def update_from_headers(self, headers: dict):
        """Update rate limit info from API response headers."""
        with self.lock:
            # Parse headers (Twitter format)
            remaining = headers.get('x-rate-limit-remaining')
            reset = headers.get('x-rate-limit-reset')
            limit = headers.get('x-rate-limit-limit')
            
            if limit:
                new_max = int(limit)
                if new_max != self.current_limit.max_requests:
                    logger.info(f"Rate limit updated: {self.current_limit.max_requests} -> {new_max}")
                    self.current_limit.max_requests = new_max
            
            if reset:
                reset_time = datetime.fromtimestamp(int(reset))
                logger.debug(f"Rate limit resets at: {reset_time}")
            
            if remaining:
                remaining_count = int(remaining)
                # Adjust our tracking to match server's count
                current_remaining = self.current_limit.max_requests - len(self.last_requests)
                if abs(current_remaining - remaining_count) > 5:
                    logger.warning(f"Rate limit sync mismatch: local={current_remaining}, server={remaining_count}")
    
    def can_make_request(self) -> bool:
        """Check if we can make a request."""
        with self.lock:
            now = time.time()
            window_start = now - self.current_limit.window_seconds
            
            # Remove old requests
            while self.last_requests and self.last_requests[0] < window_start:
                self.last_requests.popleft()
            
            return len(self.last_requests) < self.current_limit.max_requests
    
    def record_request(self):
        """Record a request."""
        with self.lock:
            self.last_requests.append(time.time())
```

### Quota Management System

For platforms with monthly/daily quotas, implement quota tracking:

```python
import json
from datetime import datetime, date
from pathlib import Path

class QuotaManager:
    """
    Manages monthly and daily quota limits.
    """
    
    def __init__(self, quota_file: str = "quotas.json"):
        self.quota_file = Path(quota_file)
        self.quotas = self._load_quotas()
    
    def _load_quotas(self) -> dict:
        """Load quota data from file."""
        if self.quota_file.exists():
            with open(self.quota_file, 'r') as f:
                return json.load(f)
        return {}
    
    def _save_quotas(self):
        """Save quota data to file."""
        with open(self.quota_file, 'w') as f:
            json.dump(self.quotas, f, indent=2)
    
    def register_quota(
        self,
        name: str,
        monthly_limit: Optional[int] = None,
        daily_limit: Optional[int] = None
    ):
        """Register a quota to track."""
        if name not in self.quotas:
            self.quotas[name] = {
                "monthly_limit": monthly_limit,
                "daily_limit": daily_limit,
                "monthly_used": {},
                "daily_used": {}
            }
            self._save_quotas()
    
    def record_usage(self, name: str, count: int = 1):
        """Record usage against quota."""
        if name not in self.quotas:
            raise ValueError(f"Unknown quota: {name}")
        
        quota = self.quotas[name]
        today = str(date.today())
        month = today[:7]  # YYYY-MM
        
        # Update daily usage
        if today not in quota["daily_used"]:
            quota["daily_used"][today] = 0
        quota["daily_used"][today] += count
        
        # Update monthly usage
        if month not in quota["monthly_used"]:
            quota["monthly_used"][month] = 0
        quota["monthly_used"][month] += count
        
        self._save_quotas()
        
        # Check if we've exceeded limits
        if quota["daily_limit"] and quota["daily_used"][today] > quota["daily_limit"]:
            logger.warning(f"Daily quota exceeded for {name}: {quota['daily_used'][today]}/{quota['daily_limit']}")
        
        if quota["monthly_limit"] and quota["monthly_used"][month] > quota["monthly_limit"]:
            logger.error(f"Monthly quota exceeded for {name}: {quota['monthly_used'][month]}/{quota['monthly_limit']}")
    
    def get_remaining(self, name: str) -> dict:
        """Get remaining quota."""
        if name not in self.quotas:
            return {"daily": None, "monthly": None}
        
        quota = self.quotas[name]
        today = str(date.today())
        month = today[:7]
        
        daily_used = quota["daily_used"].get(today, 0)
        monthly_used = quota["monthly_used"].get(month, 0)
        
        return {
            "daily_remaining": quota["daily_limit"] - daily_used if quota["daily_limit"] else None,
            "daily_used": daily_used,
            "monthly_remaining": quota["monthly_limit"] - monthly_used if quota["monthly_limit"] else None,
            "monthly_used": monthly_used
        }
    
    def can_use(self, name: str, count: int = 1) -> bool:
        """Check if we can use quota."""
        remaining = self.get_remaining(name)
        
        if remaining["daily_remaining"] is not None and remaining["daily_remaining"] < count:
            return False
        
        if remaining["monthly_remaining"] is not None and remaining["monthly_remaining"] < count:
            return False
        
        return True


# Usage example
quota_manager = QuotaManager()

# Twitter v2 Enterprise tier example
quota_manager.register_quota(
    name="twitter_tweets",
    monthly_limit=10_000_000,  # 10M tweets per month
    daily_limit=500_000  # 500K per day
)

# Before collection
if quota_manager.can_use("twitter_tweets", 1000):
    # Collect data
    result = collector.collect_batch(...)
    
    # Record usage
    quota_manager.record_usage("twitter_tweets", result.items_collected)
else:
    logger.error("Quota exhausted, skipping collection")
```

### Priority Queue for Rate-Limited Requests

When you have multiple data sources competing for limited rate quota:

```python
import heapq
from dataclasses import dataclass, field
from typing import Any, Callable
import threading
import time

@dataclass(order=True)
class PrioritizedRequest:
    """A request with priority for rate-limited execution."""
    priority: int
    timestamp: float = field(compare=False)
    callback: Callable = field(compare=False)
    args: tuple = field(compare=False)
    kwargs: dict = field(compare=False)

class PriorityRateLimitedQueue:
    """
    Queue that executes requests respecting rate limits and priority.
    Higher priority requests are executed first when rate limit allows.
    """
    
    def __init__(self, rate_limiter: MultiTierRateLimiter, limit_names: list[str]):
        self.rate_limiter = rate_limiter
        self.limit_names = limit_names
        self.queue = []
        self.lock = threading.Lock()
        self.running = False
        self.worker_thread = None
    
    def add_request(
        self,
        callback: Callable,
        priority: int = 5,
        *args,
        **kwargs
    ):
        """
        Add a request to the queue.
        Priority: 1 = highest, 10 = lowest
        """
        with self.lock:
            request = PrioritizedRequest(
                priority=priority,
                timestamp=time.time(),
                callback=callback,
                args=args,
                kwargs=kwargs
            )
            heapq.heappush(self.queue, request)
    
    def start(self):
        """Start processing queue."""
        self.running = True
        self.worker_thread = threading.Thread(target=self._process_queue)
        self.worker_thread.daemon = True
        self.worker_thread.start()
    
    def stop(self):
        """Stop processing queue."""
        self.running = False
        if self.worker_thread:
            self.worker_thread.join()
    
    def _process_queue(self):
        """Process queued requests respecting rate limits."""
        while self.running:
            request = None
            
            with self.lock:
                if self.queue:
                    request = heapq.heappop(self.queue)
            
            if request:
                # Wait for rate limit capacity
                self.rate_limiter.wait_for_capacity(self.limit_names)
                
                # Execute request
                try:
                    request.callback(*request.args, **request.kwargs)
                except Exception as e:
                    logger.error(f"Request execution error: {e}")
            else:
                # No requests, sleep briefly
                time.sleep(0.1)


# Usage example
priority_queue = PriorityRateLimitedQueue(
    rate_limiter=rate_limiter,
    limit_names=["global_app", "search_tweets"]
)

priority_queue.start()

# Add high-priority request (brand crisis monitoring)
priority_queue.add_request(
    collect_brand_crisis_mentions,
    priority=1
)

# Add medium-priority request (competitor monitoring)
priority_queue.add_request(
    collect_competitor_mentions,
    priority=5
)

# Add low-priority request (general industry trends)
priority_queue.add_request(
    collect_industry_trends,
    priority=9
)
```

## Webhook Setup for Instant Notifications

Webhooks provide the fastest way to receive notifications about social media events without constantly polling APIs. Instead of your system asking "Is there new data?" every few seconds, platforms push data to your endpoint when events occur.

### Webhook Server Implementation

Here's a production-ready webhook server with security, validation, and processing:

```python
from flask import Flask, request, jsonify
import hmac
import hashlib
import json
import logging
from functools import wraps
from typing import Callable, Dict
import threading
from queue import Queue

logger = logging.getLogger(__name__)

class WebhookServer:
    """
    Secure webhook server with signature verification and async processing.
    """
    
    def __init__(self, secret: str, port: int = 5000):
        self.app = Flask(__name__)
        self.secret = secret.encode()
        self.port = port
        self.handlers: Dict[str, Callable] = {}
        self.processing_queue = Queue()
        
        # Setup routes
        self._setup_routes()
        
        # Start processing thread
        self.processor_thread = threading.Thread(target=self._process_webhooks)
        self.processor_thread.daemon = True
        self.processor_thread.start()
    
    def _setup_routes(self):
        """Setup Flask routes."""
        
        @self.app.route('/webhook/<platform>', methods=['POST'])
        def webhook_handler(platform):
            """Handle incoming webhooks."""
            try:
                # Verify signature
                if not self._verify_signature(platform, request):
                    logger.warning(f"Invalid signature from {platform}")
                    return jsonify({"error": "Invalid signature"}), 401
                
                # Parse payload
                payload = request.get_json()
                
                # Add to processing queue (non-blocking)
                self.processing_queue.put({
                    "platform": platform,
                    "payload": payload,
                    "headers": dict(request.headers)
                })
                
                # Return 200 immediately (webhook should respond quickly)
                return jsonify({"status": "received"}), 200
                
            except Exception as e:
                logger.error(f"Webhook error: {e}")
                return jsonify({"error": "Internal error"}), 500
        
        @self.app.route('/webhook/<platform>/verify', methods=['GET'])
        def verify_handler(platform):
            """Handle webhook verification (used by some platforms)."""
            # Different platforms use different verification methods
            if platform == "facebook":
                # Facebook verification
                mode = request.args.get('hub.mode')
                token = request.args.get('hub.verify_token')
                challenge = request.args.get('hub.challenge')
                
                if mode == 'subscribe' and token == self.secret.decode():
                    return challenge, 200
                return "Verification failed", 403
            
            elif platform == "twitter":
                # Twitter CRC check
                crc_token = request.args.get('crc_token')
                if crc_token:
                    response_token = self._generate_crc_response(crc_token)
                    return jsonify({"response_token": response_token}), 200
            
            return "Unknown platform", 400
    
    def _verify_signature(self, platform: str, request) -> bool:
        """Verify webhook signature based on platform."""
        if platform == "twitter":
            signature = request.headers.get('X-Twitter-Webhooks-Signature')
            if not signature:
                return False
            
            signature_hash = signature.split('=')[1]
            expected_hash = hmac.new(
                self.secret,
                request.get_data(),
                hashlib.sha256
            ).hexdigest()
            
            return hmac.compare_digest(signature_hash, expected_hash)
        
        elif platform == "facebook":
            signature = request.headers.get('X-Hub-Signature-256')
            if not signature:
                return False
            
            signature_hash = signature.split('=')[1]
            expected_hash = hmac.new(
                self.secret,
                request.get_data(),
                hashlib.sha256
            ).hexdigest()
            
            return hmac.compare_digest(signature_hash, expected_hash)
        
        elif platform == "instagram":
            # Instagram uses same verification as Facebook
            return self._verify_signature("facebook", request)
        
        # Add other platforms as needed
        return False
    
    def _generate_crc_response(self, crc_token: str) -> str:
        """Generate CRC response for Twitter webhook verification."""
        response = hmac.new(
            self.secret,
            crc_token.encode(),
            hashlib.sha256
        ).digest()
        return 'sha256=' + response.hex()
    
    def register_handler(self, platform: str, handler: Callable):
        """Register a handler for a platform's webhooks."""
        self.handlers[platform] = handler
        logger.info(f"Registered handler for {platform}")
    
    def _process_webhooks(self):
        """Process webhooks asynchronously."""
        while True:
            webhook = self.processing_queue.get()
            
            try:
                platform = webhook["platform"]
                payload = webhook["payload"]
                
                # Get handler for this platform
                handler = self.handlers.get(platform)
                if handler:
                    handler(payload)
                else:
                    logger.warning(f"No handler registered for {platform}")
                
            except Exception as e:
                logger.error(f"Error processing webhook: {e}")
            
            self.processing_queue.task_done()
    
    def run(self):
        """Start the webhook server."""
        logger.info(f"Starting webhook server on port {self.port}")
        self.app.run(host='0.0.0.0', port=self.port)


# Usage example
webhook_server = WebhookServer(
    secret="your_webhook_secret",
    port=5000
)

# Register handlers for different platforms
def handle_twitter_webhook(payload: dict):
    """Process Twitter webhook events."""
    # Check event type
    if 'tweet_create_events' in payload:
        for tweet in payload['tweet_create_events']:
            logger.info(f"New tweet: {tweet['text']}")
            # Process tweet...
            
    elif 'direct_message_events' in payload:
        for dm in payload['direct_message_events']:
            logger.info(f"New DM from {dm['message_create']['sender_id']}")
            # Process DM...

def handle_facebook_webhook(payload: dict):
    """Process Facebook webhook events."""
    for entry in payload.get('entry', []):
        for change in entry.get('changes', []):
            field = change['field']
            value = change['value']
            
            if field == 'comments':
                logger.info(f"New comment: {value['message']}")
                # Process comment...
            
            elif field == 'mentions':
                logger.info(f"New mention: {value['post_id']}")
                # Process mention...

webhook_server.register_handler('twitter', handle_twitter_webhook)
webhook_server.register_handler('facebook', handle_facebook_webhook)

# Run server (in production, use gunicorn or similar)
webhook_server.run()
```

### Ngrok Integration for Development

During development, use ngrok to expose your local webhook server:

```python
import subprocess
import requests
import time
import json
import logging

logger = logging.getLogger(__name__)

class NgrokTunnel:
    """
    Manage ngrok tunnel for webhook development.
    """
    
    def __init__(self, port: int = 5000, auth_token: Optional[str] = None):
        self.port = port
        self.auth_token = auth_token
        self.process = None
        self.public_url = None
    
    def start(self) -> str:
        """Start ngrok tunnel and return public URL."""
        # Start ngrok process
        cmd = ['ngrok', 'http', str(self.port), '--log=stdout']
        if self.auth_token:
            cmd.extend(['--authtoken', self.auth_token])
        
        self.process = subprocess.Popen(
            cmd,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
        )
        
        # Wait for tunnel to be established
        time.sleep(2)
        
        # Get public URL from ngrok API
        try:
            response = requests.get('http://localhost:4040/api/tunnels')
            tunnels = response.json()['tunnels']
            
            # Find HTTPS tunnel
            for tunnel in tunnels:
                if tunnel['proto'] == 'https':
                    self.public_url = tunnel['public_url']
                    logger.info(f"Ngrok tunnel established: {self.public_url}")
                    return self.public_url
            
        except Exception as e:
            logger.error(f"Failed to get ngrok URL: {e}")
            raise
    
    def stop(self):
        """Stop ngrok tunnel."""
        if self.process:
            self.process.terminate()
            self.process.wait()
            logger.info("Ngrok tunnel stopped")
    
    def get_webhook_url(self, platform: str) -> str:
        """Get full webhook URL for a platform."""
        if not self.public_url:
            raise ValueError("Tunnel not started")
        return f"{self.public_url}/webhook/{platform}"


# Usage in development
if __name__ == "__main__":
    # Start ngrok
    ngrok = NgrokTunnel(port=5000)
    webhook_url = ngrok.start()
    
    print(f"Webhook URL for Twitter: {ngrok.get_webhook_url('twitter')}")
    print(f"Webhook URL for Facebook: {ngrok.get_webhook_url('facebook')}")
    
    # Start webhook server
    try:
        webhook_server.run()
    finally:
        ngrok.stop()
```

### Webhook Retry and Reliability

Implement retry logic for failed webhook processing:

```python
from dataclasses import dataclass
from datetime import datetime, timedelta
import time
import json
from pathlib import Path

@dataclass
class FailedWebhook:
    platform: str
    payload: dict
    timestamp: datetime
    retry_count: int
    last_error: str

class WebhookRetryQueue:
    """
    Manages retry logic for failed webhook processing.
    """
    
    def __init__(
        self,
        storage_file: str = "failed_webhooks.json",
        max_retries: int = 3,
        retry_delay_seconds: int = 300
    ):
        self.storage_file = Path(storage_file)
        self.max_retries = max_retries
        self.retry_delay_seconds = retry_delay_seconds
        self.failed_webhooks = []
        
        self._load_failed_webhooks()
    
    def _load_failed_webhooks(self):
        """Load failed webhooks from storage."""
        if self.storage_file.exists():
            with open(self.storage_file, 'r') as f:
                data = json.load(f)
                self.failed_webhooks = [
                    FailedWebhook(
                        platform=item['platform'],
                        payload=item['payload'],
                        timestamp=datetime.fromisoformat(item['timestamp']),
                        retry_count=item['retry_count'],
                        last_error=item['last_error']
                    )
                    for item in data
                ]
    
    def _save_failed_webhooks(self):
        """Save failed webhooks to storage."""
        data = [
            {
                'platform': wh.platform,
                'payload': wh.payload,
                'timestamp': wh.timestamp.isoformat(),
                'retry_count': wh.retry_count,
                'last_error': wh.last_error
            }
            for wh in self.failed_webhooks
        ]
        
        with open(self.storage_file, 'w') as f:
            json.dump(data, f, indent=2)
    
    def add_failed_webhook(self, platform: str, payload: dict, error: str):
        """Add a failed webhook to retry queue."""
        webhook = FailedWebhook(
            platform=platform,
            payload=payload,
            timestamp=datetime.utcnow(),
            retry_count=0,
            last_error=error
        )
        self.failed_webhooks.append(webhook)
        self._save_failed_webhooks()
        logger.info(f"Added failed webhook to retry queue: {platform}")
    
    def process_retries(self, handlers: Dict[str, Callable]):
        """Process webhooks that are ready for retry."""
        now = datetime.utcnow()
        still_failed = []
        
        for webhook in self.failed_webhooks:
            # Check if ready for retry
            time_since_last = (now - webhook.timestamp).total_seconds()
            if time_since_last < self.retry_delay_seconds:
                still_failed.append(webhook)
                continue
            
            # Check if exceeded max retries
            if webhook.retry_count >= self.max_retries:
                logger.error(f"Webhook exceeded max retries: {webhook.platform}")
                # Could send to dead letter queue here
                continue
            
            # Attempt retry
            handler = handlers.get(webhook.platform)
            if handler:
                try:
                    handler(webhook.payload)
                    logger.info(f"Successfully retried webhook: {webhook.platform}")
                    # Success - don't add back to failed list
                except Exception as e:
                    logger.warning(f"Retry failed: {e}")
                    webhook.retry_count += 1
                    webhook.timestamp = now
                    webhook.last_error = str(e)
                    still_failed.append(webhook)
        
        # Update failed webhooks list
        self.failed_webhooks = still_failed
        self._save_failed_webhooks()
```

## Building a Social Listening Pipeline

A complete social listening pipeline connects data collection, processing, analysis, and storage into a cohesive system. Let's build a production-grade pipeline architecture.

### Pipeline Architecture Overview

```
┌─────────────────────────────────────────────────────────────────┐
│                     DATA COLLECTION LAYER                        │
├─────────────────────────────────────────────────────────────────┤
│  ┌──────────┐  ┌──────────┐  ┌──────────┐  ┌──────────┐       │
│  │ Twitter  │  │ Facebook │  │Instagram │  │ Webhooks │       │
│  │  Stream  │  │  Batch   │  │  Batch   │  │  Real-   │       │
│  │          │  │          │  │          │  │  time    │       │
│  └────┬─────┘  └────┬─────┘  └────┬─────┘  └────┬─────┘       │
└───────┼─────────────┼─────────────┼─────────────┼──────────────┘
        │             │             │             │
        └─────────────┴─────────────┴─────────────┘
                       │
        ┌──────────────▼──────────────┐
        │     Message Queue (Redis)    │
        │    - Buffering               │
        │    - Load distribution       │
        │    - Retry handling          │
        └──────────────┬──────────────┘
                       │
        ┌──────────────▼──────────────┐
        │   PROCESSING LAYER           │
        ├──────────────────────────────┤
        │  ┌───────────────────────┐   │
        │  │ Data Enrichment       │   │
        │  │ - Sentiment analysis  │   │
        │  │ - Entity extraction   │   │
        │  │ - Language detection  │   │
        │  └───────────┬───────────┘   │
        │              │                │
        │  ┌───────────▼───────────┐   │
        │  │ Alert Engine          │   │
        │  │ - Pattern matching    │   │
        │  │ - Threshold checks    │   │
        │  │ - Notification system │   │
        │  └───────────┬───────────┘   │
        └──────────────┼───────────────┘
                       │
        ┌──────────────▼──────────────┐
        │    STORAGE LAYER             │
        ├──────────────────────────────┤
        │  ┌──────────┐  ┌──────────┐ │
        │  │TimeSeries│  │  Data    │ │
        │  │   DB     │  │  Lake    │ │
        │  │(InfluxDB)│  │ (S3)     │ │
        │  └────┬─────┘  └────┬─────┘ │
        └───────┼─────────────┼────────┘
                │             │
        ┌───────▼─────────────▼────────┐
        │   ANALYTICS & REPORTING       │
        │   - Dashboards                │
        │   - Reports                   │
        │   - API endpoints             │
        └───────────────────────────────┘
```

### Core Pipeline Implementation

```python
import redis
import json
from typing import Dict, List, Callable, Optional
from dataclasses import dataclass
import logging
import threading
from queue import Queue
import time

logger = logging.getLogger(__name__)

@dataclass
class PipelineMessage:
    """Message flowing through pipeline."""
    platform: str
    content: dict
    metadata: dict
    stage: str = "ingestion"

class SocialListeningPipeline:
    """
    Complete social listening pipeline with stages:
    1. Ingestion - Collect from sources
    2. Enrichment - Add metadata, sentiment, etc.
    3. Filtering - Apply rules and filters
    4. Storage - Save to databases
    5. Alerts - Check for trigger conditions
    """
    
    def __init__(
        self,
        redis_host: str = "localhost",
        redis_port: int = 6379,
        num_workers: int = 4
    ):
        self.redis_client = redis.Redis(
            host=redis_host,
            port=redis_port,
            decode_responses=True
        )
        self.num_workers = num_workers
        self.workers = []
        self.running = False
        
        # Pipeline stages
        self.enrichers: List[Callable] = []
        self.filters: List[Callable] = []
        self.storers: List[Callable] = []
        self.alerters: List[Callable] = []
        
        # Queues for each stage
        self.ingestion_queue = "pipeline:ingestion"
        self.enrichment_queue = "pipeline:enrichment"
        self.storage_queue = "pipeline:storage"
        self.alert_queue = "pipeline:alerts"
    
    def ingest(self, message: PipelineMessage):
        """
        Ingest a message into the pipeline.
        This is called by collectors.
        """
        message.stage = "ingestion"
        self.redis_client.lpush(
            self.ingestion_queue,
            json.dumps({
                'platform': message.platform,
                'content': message.content,
                'metadata': message.metadata,
                'stage': message.stage
            })
        )
    
    def register_enricher(self, enricher: Callable):
        """Register an enrichment function."""
        self.enrichers.append(enricher)
    
    def register_filter(self, filter_func: Callable):
        """Register a filter function."""
        self.filters.append(filter_func)
    
    def register_storer(self, storer: Callable):
        """Register a storage function."""
        self.storers.append(storer)
    
    def register_alerter(self, alerter: Callable):
        """Register an alert function."""
        self.alerters.append(alerter)
    
    def start(self):
        """Start pipeline workers."""
        self.running = True
        
        # Start workers for each stage
        for i in range(self.num_workers):
            # Enrichment workers
            worker = threading.Thread(
                target=self._enrichment_worker,
                name=f"enrichment-worker-{i}"
            )
            worker.daemon = True
            worker.start()
            self.workers.append(worker)
            
            # Storage workers
            worker = threading.Thread(
                target=self._storage_worker,
                name=f"storage-worker-{i}"
            )
            worker.daemon = True
            worker.start()
            self.workers.append(worker)
            
            # Alert workers
            worker = threading.Thread(
                target=self._alert_worker,
                name=f"alert-worker-{i}"
            )
            worker.daemon = True
            worker.start()
            self.workers.append(worker)
        
        logger.info(f"Started {len(self.workers)} pipeline workers")
    
    def stop(self):
        """Stop pipeline workers."""
        self.running = False
        for worker in self.workers:
            worker.join(timeout=5)
        logger.info("Pipeline workers stopped")
    
    def _enrichment_worker(self):
        """Worker that processes enrichment stage."""
        while self.running:
            try:
                # Get message from ingestion queue (blocking with timeout)
                message_data = self.redis_client.brpop(
                    self.ingestion_queue,
                    timeout=1
                )
                
                if not message_data:
                    continue
                
                _, message_json = message_data
                message_dict = json.loads(message_json)
                message = PipelineMessage(**message_dict)
                
                # Apply enrichers
                for enricher in self.enrichers:
                    try:
                        message = enricher(message)
                    except Exception as e:
                        logger.error(f"Enricher error: {e}")
                
                # Apply filters
                should_continue = True
                for filter_func in self.filters:
                    try:
                        if not filter_func(message):
                            should_continue = False
                            break
                    except Exception as e:
                        logger.error(f"Filter error: {e}")
                
                if should_continue:
                    # Move to next stages
                    message.stage = "storage"
                    self.redis_client.lpush(
                        self.storage_queue,
                        json.dumps({
                            'platform': message.platform,
                            'content': message.content,
                            'metadata': message.metadata,
                            'stage': message.stage
                        })
                    )
                    
                    # Also send to alert queue
                    self.redis_client.lpush(
                        self.alert_queue,
                        json.dumps({
                            'platform': message.platform,
                            'content': message.content,
                            'metadata': message.metadata,
                            'stage': 'alerts'
                        })
                    )
                
            except Exception as e:
                logger.error(f"Enrichment worker error: {e}")
    
    def _storage_worker(self):
        """Worker that processes storage stage."""
        while self.running:
            try:
                message_data = self.redis_client.brpop(
                    self.storage_queue,
                    timeout=1
                )
                
                if not message_data:
                    continue
                
                _, message_json = message_data
                message_dict = json.loads(message_json)
                message = PipelineMessage(**message_dict)
                
                # Apply storers
                for storer in self.storers:
                    try:
                        storer(message)
                    except Exception as e:
                        logger.error(f"Storer error: {e}")
                
            except Exception as e:
                logger.error(f"Storage worker error: {e}")
    
    def _alert_worker(self):
        """Worker that processes alert stage."""
        while self.running:
            try:
                message_data = self.redis_client.brpop(
                    self.alert_queue,
                    timeout=1
                )
                
                if not message_data:
                    continue
                
                _, message_json = message_data
                message_dict = json.loads(message_json)
                message = PipelineMessage(**message_dict)
                
                # Apply alerters
                for alerter in self.alerters:
                    try:
                        alerter(message)
                    except Exception as e:
                        logger.error(f"Alerter error: {e}")
                
            except Exception as e:
                logger.error(f"Alert worker error: {e}")


# Example usage
pipeline = SocialListeningPipeline(num_workers=4)

# Register enrichers
def add_sentiment(message: PipelineMessage) -> PipelineMessage:
    """Add sentiment analysis."""
    text = message.content.get('text', '')
    # Use sentiment analysis library
    # sentiment = analyze_sentiment(text)
    message.metadata['sentiment'] = 'positive'  # Placeholder
    message.metadata['sentiment_score'] = 0.8
    return message

def add_entities(message: PipelineMessage) -> PipelineMessage:
    """Extract entities."""
    text = message.content.get('text', '')
    # Use NER library
    # entities = extract_entities(text)
    message.metadata['entities'] = ['entity1', 'entity2']  # Placeholder
    return message

pipeline.register_enricher(add_sentiment)
pipeline.register_enricher(add_entities)

# Register filters
def filter_spam(message: PipelineMessage) -> bool:
    """Filter out spam messages."""
    text = message.content.get('text', '').lower()
    spam_keywords = ['buy now', 'click here', 'limited offer']
    return not any(keyword in text for keyword in spam_keywords)

pipeline.register_filter(filter_spam)

# Register storers
def store_in_database(message: PipelineMessage):
    """Store message in database."""
    # Save to database
    logger.info(f"Storing message from {message.platform}")

pipeline.register_storer(store_in_database)

# Register alerters
def check_crisis_keywords(message: PipelineMessage):
    """Check for crisis keywords."""
    text = message.content.get('text', '').lower()
    crisis_keywords = ['security breach', 'data leak', 'outage']
    
    if any(keyword in text for keyword in crisis_keywords):
        logger.warning(f"CRISIS ALERT: {text[:100]}")
        # Send notification

pipeline.register_alerter(check_crisis_keywords)

# Start pipeline
pipeline.start()

# Collectors feed into pipeline
def tweet_callback(tweet_data: dict):
    message = PipelineMessage(
        platform='twitter',
        content=tweet_data,
        metadata={'timestamp': time.time()}
    )
    pipeline.ingest(message)
```

### Dead Letter Queue for Failed Messages

```python
class DeadLetterQueue:
    """
    Manages messages that failed processing after retries.
    """
    
    def __init__(self, redis_client: redis.Redis):
        self.redis_client = redis_client
        self.dlq_key = "pipeline:dead_letter"
    
    def add(self, message: PipelineMessage, error: str, stage: str):
        """Add failed message to DLQ."""
        dlq_entry = {
            'message': {
                'platform': message.platform,
                'content': message.content,
                'metadata': message.metadata,
                'stage': message.stage
            },
            'error': error,
            'failed_stage': stage,
            'timestamp': time.time()
        }
        
        self.redis_client.lpush(self.dlq_key, json.dumps(dlq_entry))
        logger.error(f"Message moved to DLQ: {error}")
    
    def get_failed_messages(self, limit: int = 100) -> List[dict]:
        """Get failed messages from DLQ."""
        messages = self.redis_client.lrange(self.dlq_key, 0, limit - 1)
        return [json.loads(msg) for msg in messages]
    
    def retry_failed_message(self, index: int, pipeline: SocialListeningPipeline):
        """Retry a failed message."""
        message_json = self.redis_client.lindex(self.dlq_key, index)
        if message_json:
            entry = json.loads(message_json)
            message_data = entry['message']
            message = PipelineMessage(**message_data)
            
            # Re-ingest into pipeline
            pipeline.ingest(message)
            
            # Remove from DLQ
            self.redis_client.lrem(self.dlq_key, 1, message_json)
            logger.info(f"Retrying failed message from DLQ")
```

## Data Storage: Time-Series Databases and Data Lakes

Choosing the right storage architecture is critical for social listening systems. You need to balance real-time query performance with long-term storage costs while maintaining data integrity and scalability.

### Time-Series Database Implementation (InfluxDB)

Time-series databases are perfect for social listening metrics and analytics:

```python
from influxdb_client import InfluxDBClient, Point, WritePrecision
from influxdb_client.client.write_api import SYNCHRONOUS
from datetime import datetime
from typing import Dict, List
import logging

logger = logging.getLogger(__name__)

class SocialMetricsStore:
    """
    Store social media metrics in InfluxDB for time-series analysis.
    """
    
    def __init__(
        self,
        url: str = "http://localhost:8086",
        token: str = "",
        org: str = "social-listening",
        bucket: str = "metrics"
    ):
        self.client = InfluxDBClient(url=url, token=token, org=org)
        self.write_api = self.client.write_api(write_options=SYNCHRONOUS)
        self.query_api = self.client.query_api()
        self.org = org
        self.bucket = bucket
    
    def write_post_metrics(
        self,
        platform: str,
        post_id: str,
        metrics: Dict[str, float],
        tags: Dict[str, str] = None
    ):
        """Write metrics for a social media post."""
        point = Point("post_metrics") \
            .tag("platform", platform) \
            .tag("post_id", post_id)
        
        # Add custom tags
        if tags:
            for key, value in tags.items():
                point = point.tag(key, value)
        
        # Add metrics as fields
        for metric_name, value in metrics.items():
            point = point.field(metric_name, float(value))
        
        point = point.time(datetime.utcnow(), WritePrecision.NS)
        
        try:
            self.write_api.write(bucket=self.bucket, record=point)
        except Exception as e:
            logger.error(f"Failed to write metrics: {e}")
    
    def write_sentiment_metrics(
        self,
        platform: str,
        query: str,
        sentiment: str,
        score: float,
        count: int = 1
    ):
        """Write sentiment metrics."""
        point = Point("sentiment") \
            .tag("platform", platform) \
            .tag("query", query) \
            .tag("sentiment", sentiment) \
            .field("score", float(score)) \
            .field("count", int(count)) \
            .time(datetime.utcnow(), WritePrecision.NS)
        
        try:
            self.write_api.write(bucket=self.bucket, record=point)
        except Exception as e:
            logger.error(f"Failed to write sentiment: {e}")
    
    def write_engagement_rate(
        self,
        platform: str,
        account: str,
        engagement_rate: float,
        impressions: int,
        engagements: int
    ):
        """Write engagement rate metrics."""
        point = Point("engagement") \
            .tag("platform", platform) \
            .tag("account", account) \
            .field("engagement_rate", float(engagement_rate)) \
            .field("impressions", int(impressions)) \
            .field("engagements", int(engagements)) \
            .time(datetime.utcnow(), WritePrecision.NS)
        
        try:
            self.write_api.write(bucket=self.bucket, record=point)
        except Exception as e:
            logger.error(f"Failed to write engagement: {e}")
    
    def query_sentiment_trend(
        self,
        platform: str,
        query: str,
        start_time: str = "-7d"
    ) -> List[Dict]:
        """Query sentiment trend over time."""
        flux_query = f'''
        from(bucket: "{self.bucket}")
            |> range(start: {start_time})
            |> filter(fn: (r) => r._measurement == "sentiment")
            |> filter(fn: (r) => r.platform == "{platform}")
            |> filter(fn: (r) => r.query == "{query}")
            |> filter(fn: (r) => r._field == "score")
            |> aggregateWindow(every: 1h, fn: mean, createEmpty: false)
        '''
        
        try:
            result = self.query_api.query(query=flux_query, org=self.org)
            
            data = []
            for table in result:
                for record in table.records:
                    data.append({
                        'time': record.get_time(),
                        'sentiment': record.values.get('sentiment'),
                        'score': record.get_value()
                    })
            
            return data
        except Exception as e:
            logger.error(f"Query failed: {e}")
            return []
    
    def query_engagement_metrics(
        self,
        platform: str,
        account: str,
        start_time: str = "-30d"
    ) -> Dict:
        """Query aggregated engagement metrics."""
        flux_query = f'''
        from(bucket: "{self.bucket}")
            |> range(start: {start_time})
            |> filter(fn: (r) => r._measurement == "engagement")
            |> filter(fn: (r) => r.platform == "{platform}")
            |> filter(fn: (r) => r.account == "{account}")
            |> group(columns: ["_field"])
            |> mean()
        '''
        
        try:
            result = self.query_api.query(query=flux_query, org=self.org)
            
            metrics = {}
            for table in result:
                for record in table.records:
                    field = record.values.get('_field')
                    value = record.get_value()
                    metrics[field] = value
            
            return metrics
        except Exception as e:
            logger.error(f"Query failed: {e}")
            return {}
    
    def close(self):
        """Close database connection."""
        self.client.close()


# Usage example
metrics_store = SocialMetricsStore(
    url="http://localhost:8086",
    token="your_influx_token",
    org="social-listening",
    bucket="metrics"
)

# Write post metrics
metrics_store.write_post_metrics(
    platform="twitter",
    post_id="123456789",
    metrics={
        "likes": 150,
        "retweets": 45,
        "replies": 12,
        "impressions": 5000
    },
    tags={
        "campaign": "product_launch",
        "sentiment": "positive"
    }
)

# Query sentiment trends
trends = metrics_store.query_sentiment_trend(
    platform="twitter",
    query="brand_name",
    start_time="-7d"
)

for point in trends:
    print(f"{point['time']}: {point['sentiment']} ({point['score']:.2f})")
```

### Data Lake Implementation (S3 + Parquet)

For long-term storage and analytical queries, use a data lake:

```python
import boto3
import pandas as pd
import pyarrow as pa
import pyarrow.parquet as pq
from datetime import datetime, date
from typing import List, Dict
import json
import logging
from io import BytesIO

logger = logging.getLogger(__name__)

class SocialDataLake:
    """
    Manage social listening data lake in S3 with Parquet format.
    """
    
    def __init__(
        self,
        bucket_name: str,
        aws_access_key: str = None,
        aws_secret_key: str = None,
        region: str = "us-east-1"
    ):
        self.bucket_name = bucket_name
        
        # Initialize S3 client
        self.s3_client = boto3.client(
            's3',
            aws_access_key_id=aws_access_key,
            aws_secret_access_key=aws_secret_key,
            region_name=region
        )
    
    def write_batch(
        self,
        platform: str,
        data: List[Dict],
        partition_date: date = None
    ):
        """
        Write batch of social media data to data lake.
        Partitioned by: platform/year/month/day/
        """
        if not data:
            return
        
        if partition_date is None:
            partition_date = date.today()
        
        # Convert to DataFrame
        df = pd.DataFrame(data)
        
        # Add partition columns
        df['partition_year'] = partition_date.year
        df['partition_month'] = partition_date.month
        df['partition_day'] = partition_date.day
        
        # Create partition path
        partition_path = (
            f"{platform}/"
            f"year={partition_date.year}/"
            f"month={partition_date.month:02d}/"
            f"day={partition_date.day:02d}/"
        )
        
        # Generate filename with timestamp
        timestamp = datetime.utcnow().strftime("%H%M%S")
        filename = f"{partition_path}data_{timestamp}.parquet"
        
        # Convert to Parquet
        table = pa.Table.from_pandas(df)
        buffer = BytesIO()
        pq.write_table(table, buffer, compression='snappy')
        buffer.seek(0)
        
        # Upload to S3
        try:
            self.s3_client.put_object(
                Bucket=self.bucket_name,
                Key=filename,
                Body=buffer.getvalue()
            )
            logger.info(f"Wrote {len(data)} records to {filename}")
        except Exception as e:
            logger.error(f"Failed to write to S3: {e}")
    
    def read_partition(
        self,
        platform: str,
        start_date: date,
        end_date: date = None
    ) -> pd.DataFrame:
        """Read data from partitions within date range."""
        if end_date is None:
            end_date = start_date
        
        # List all objects in date range
        objects_to_read = []
        
        current_date = start_date
        while current_date <= end_date:
            prefix = (
                f"{platform}/"
                f"year={current_date.year}/"
                f"month={current_date.month:02d}/"
                f"day={current_date.day:02d}/"
            )
            
            try:
                response = self.s3_client.list_objects_v2(
                    Bucket=self.bucket_name,
                    Prefix=prefix
                )
                
                if 'Contents' in response:
                    for obj in response['Contents']:
                        objects_to_read.append(obj['Key'])
            
            except Exception as e:
                logger.error(f"Failed to list objects: {e}")
            
            # Move to next day
            current_date = current_date + timedelta(days=1)
        
        # Read all Parquet files
        dfs = []
        for key in objects_to_read:
            try:
                obj = self.s3_client.get_object(Bucket=self.bucket_name, Key=key)
                buffer = BytesIO(obj['Body'].read())
                df = pd.read_parquet(buffer)
                dfs.append(df)
            except Exception as e:
                logger.error(f"Failed to read {key}: {e}")
        
        # Combine all DataFrames
        if dfs:
            return pd.concat(dfs, ignore_index=True)
        else:
            return pd.DataFrame()
    
    def query_by_keyword(
        self,
        platform: str,
        keyword: str,
        start_date: date,
        end_date: date = None
    ) -> pd.DataFrame:
        """Query data by keyword."""
        df = self.read_partition(platform, start_date, end_date)
        
        if df.empty:
            return df
        
        # Filter by keyword (case-insensitive)
        mask = df['text'].str.contains(keyword, case=False, na=False)
        return df[mask]
    
    def export_to_csv(
        self,
        platform: str,
        start_date: date,
        end_date: date,
        output_path: str
    ):
        """Export data to CSV for analysis."""
        df = self.read_partition(platform, start_date, end_date)
        
        if not df.empty:
            df.to_csv(output_path, index=False)
            logger.info(f"Exported {len(df)} records to {output_path}")
        else:
            logger.warning("No data to export")


# Usage example
data_lake = SocialDataLake(
    bucket_name="social-listening-datalake",
    aws_access_key="your_access_key",
    aws_secret_key="your_secret_key"
)

# Write batch of tweets
tweets = [
    {
        'id': '123',
        'text': 'Great product!',
        'author_id': 'user1',
        'created_at': '2024-01-15T10:30:00Z',
        'metrics': {'likes': 10, 'retweets': 2}
    },
    # ... more tweets
]

data_lake.write_batch(
    platform='twitter',
    data=tweets,
    partition_date=date(2024, 1, 15)
)

# Query data
df = data_lake.query_by_keyword(
    platform='twitter',
    keyword='product',
    start_date=date(2024, 1, 1),
    end_date=date(2024, 1, 31)
)

print(f"Found {len(df)} matching posts")
```

### Hybrid Storage Strategy

Combine hot/warm/cold storage tiers for cost optimization:

```python
from enum import Enum
from datetime import datetime, timedelta

class StorageTier(Enum):
    HOT = "hot"      # Real-time database (< 7 days)
    WARM = "warm"    # Time-series DB (7-90 days)
    COLD = "cold"    # Data lake (> 90 days)

class TieredStorageManager:
    """
    Manages data across hot/warm/cold storage tiers.
    """
    
    def __init__(
        self,
        hot_db,  # MongoDB or PostgreSQL for recent data
        warm_db: SocialMetricsStore,  # InfluxDB
        cold_storage: SocialDataLake  # S3
    ):
        self.hot_db = hot_db
        self.warm_db = warm_db
        self.cold_storage = cold_storage
    
    def store_post(self, platform: str, post_data: dict):
        """Store post in appropriate tier."""
        # Always write to hot storage for recent queries
        self.hot_db.insert_one(post_data)
        
        # Also write metrics to warm storage
        metrics = post_data.get('metrics', {})
        if metrics:
            self.warm_db.write_post_metrics(
                platform=platform,
                post_id=post_data['id'],
                metrics=metrics,
                tags={'author': post_data.get('author_id')}
            )
    
    def archive_old_data(self):
        """
        Move data from hot to warm/cold storage based on age.
        Run this daily via cron.
        """
        now = datetime.utcnow()
        
        # Move 7-day-old data from hot to cold
        cutoff_date = now - timedelta(days=7)
        
        # Query old data from hot storage
        old_posts = self.hot_db.find({
            'created_at': {'$lt': cutoff_date.isoformat()}
        })
        
        # Batch write to cold storage
        posts_by_platform = {}
        for post in old_posts:
            platform = post['platform']
            if platform not in posts_by_platform:
                posts_by_platform[platform] = []
            posts_by_platform[platform].append(post)
        
        # Write batches to data lake
        for platform, posts in posts_by_platform.items():
            self.cold_storage.write_batch(
                platform=platform,
                data=posts,
                partition_date=cutoff_date.date()
            )
        
        # Delete from hot storage after successful archival
        result = self.hot_db.delete_many({
            'created_at': {'$lt': cutoff_date.isoformat()}
        })
        
        logger.info(f"Archived {result.deleted_count} posts to cold storage")
    
    def query_across_tiers(
        self,
        platform: str,
        start_date: datetime,
        end_date: datetime = None
    ) -> List[Dict]:
        """Query data across all storage tiers."""
        if end_date is None:
            end_date = datetime.utcnow()
        
        results = []
        now = datetime.utcnow()
        hot_cutoff = now - timedelta(days=7)
        
        # Query hot storage for recent data
        if end_date > hot_cutoff:
            hot_results = self.hot_db.find({
                'platform': platform,
                'created_at': {
                    '$gte': max(start_date, hot_cutoff).isoformat(),
                    '$lte': end_date.isoformat()
                }
            })
            results.extend(list(hot_results))
        
        # Query cold storage for older data
        if start_date < hot_cutoff:
            cold_df = self.cold_storage.read_partition(
                platform=platform,
                start_date=start_date.date(),
                end_date=min(end_date, hot_cutoff).date()
            )
            results.extend(cold_df.to_dict('records'))
        
        return results
```

## Handling API Changes and Deprecations

API changes are inevitable in social listening systems. Platforms regularly update their APIs, deprecate old endpoints, and change rate limits. Building resilient systems that gracefully handle these changes is essential for production reliability.

### Version Management Strategy

```python
from typing import Dict, Optional, Callable
from dataclasses import dataclass
from enum import Enum
import logging

logger = logging.getLogger(__name__)

class APIVersionStatus(Enum):
    ACTIVE = "active"
    DEPRECATED = "deprecated"
    SUNSET = "sunset"

@dataclass
class APIVersion:
    """Represents an API version with its metadata."""
    version: str
    status: APIVersionStatus
    sunset_date: Optional[str]
    endpoint_base: str
    features: list[str]

class MultiVersionAPIClient:
    """
    API client that supports multiple versions with automatic fallback.
    """
    
    def __init__(self, api_key: str):
        self.api_key = api_key
        self.versions: Dict[str, APIVersion] = {}
        self.preferred_version = None
        self.fallback_chain = []
    
    def register_version(self, version: APIVersion):
        """Register an API version."""
        self.versions[version.version] = version
        logger.info(f"Registered API version {version.version} ({version.status.value})")
    
    def set_version_preference(self, version_order: list[str]):
        """Set preferred version with fallback chain."""
        self.fallback_chain = version_order
        self.preferred_version = version_order[0] if version_order else None
        logger.info(f"Version preference: {' -> '.join(version_order)}")
    
    def make_request(
        self,
        endpoint: str,
        method: str = "GET",
        **kwargs
    ) -> Optional[dict]:
        """
        Make API request with automatic version fallback.
        """
        for version_str in self.fallback_chain:
            version = self.versions.get(version_str)
            if not version:
                continue
            
            # Skip sunset versions
            if version.status == APIVersionStatus.SUNSET:
                logger.warning(f"Skipping sunset version: {version_str}")
                continue
            
            # Construct URL
            url = f"{version.endpoint_base}/{endpoint}"
            
            # Log deprecation warning
            if version.status == APIVersionStatus.DEPRECATED:
                logger.warning(
                    f"Using deprecated API version {version_str}. "
                    f"Sunset date: {version.sunset_date}"
                )
            
            try:
                # Make request
                response = self._execute_request(url, method, **kwargs)
                
                # Success - return result
                logger.debug(f"Request successful with version {version_str}")
                return response
                
            except APIVersionError as e:
                logger.error(f"Version {version_str} failed: {e}")
                continue  # Try next version
            
            except Exception as e:
                logger.error(f"Request failed: {e}")
                return None
        
        logger.error("All API versions failed")
        return None
    
    def _execute_request(self, url: str, method: str, **kwargs) -> dict:
        """Execute the actual API request."""
        # Implementation depends on platform
        # This is a placeholder
        import requests
        
        headers = kwargs.pop('headers', {})
        headers['Authorization'] = f'Bearer {self.api_key}'
        
        response = requests.request(
            method=method,
            url=url,
            headers=headers,
            **kwargs
        )
        
        response.raise_for_status()
        return response.json()


class APIVersionError(Exception):
    """Raised when an API version fails."""
    pass


# Example usage
client = MultiVersionAPIClient(api_key="your_key")

# Register multiple API versions
client.register_version(APIVersion(
    version="v2",
    status=APIVersionStatus.ACTIVE,
    sunset_date=None,
    endpoint_base="https://api.platform.com/v2",
    features=["advanced_search", "webhooks", "streaming"]
))

client.register_version(APIVersion(
    version="v1.1",
    status=APIVersionStatus.DEPRECATED,
    sunset_date="2024-12-31",
    endpoint_base="https://api.platform.com/v1.1",
    features=["basic_search", "webhooks"]
))

client.register_version(APIVersion(
    version="v1",
    status=APIVersionStatus.SUNSET,
    sunset_date="2024-06-30",
    endpoint_base="https://api.platform.com/v1",
    features=["basic_search"]
))

# Set preference: try v2, fallback to v1.1 if needed
client.set_version_preference(["v2", "v1.1"])

# Make request - automatically uses best available version
result = client.make_request(
    endpoint="search/tweets",
    method="GET",
    params={"query": "brand_name"}
)
```

### Schema Evolution Handler

```python
from typing import Any, Dict, Callable
import logging

logger = logging.getLogger(__name__)

class SchemaEvolutionHandler:
    """
    Handles schema changes across API versions.
    """
    
    def __init__(self):
        self.transformers: Dict[str, Callable] = {}
    
    def register_transformer(
        self,
        from_version: str,
        to_version: str,
        transformer: Callable[[dict], dict]
    ):
        """Register a schema transformer."""
        key = f"{from_version}->{to_version}"
        self.transformers[key] = transformer
        logger.info(f"Registered transformer: {key}")
    
    def transform(
        self,
        data: dict,
        from_version: str,
        to_version: str
    ) -> dict:
        """Transform data from one schema version to another."""
        key = f"{from_version}->{to_version}"
        transformer = self.transformers.get(key)
        
        if transformer:
            return transformer(data)
        else:
            logger.warning(f"No transformer found for {key}, returning original data")
            return data


# Example transformers for Twitter API v1.1 -> v2
schema_handler = SchemaEvolutionHandler()

def transform_twitter_v1_to_v2(data: dict) -> dict:
    """Transform Twitter API v1.1 response to v2 format."""
    # v1.1 format
    v1_tweet = data
    
    # v2 format
    v2_tweet = {
        'data': {
            'id': v1_tweet['id_str'],
            'text': v1_tweet['full_text'] if 'full_text' in v1_tweet else v1_tweet['text'],
            'author_id': v1_tweet['user']['id_str'],
            'created_at': v1_tweet['created_at'],
            'public_metrics': {
                'retweet_count': v1_tweet.get('retweet_count', 0),
                'reply_count': v1_tweet.get('reply_count', 0),
                'like_count': v1_tweet.get('favorite_count', 0),
                'quote_count': v1_tweet.get('quote_count', 0)
            }
        },
        'includes': {
            'users': [{
                'id': v1_tweet['user']['id_str'],
                'username': v1_tweet['user']['screen_name'],
                'name': v1_tweet['user']['name']
            }]
        }
    }
    
    return v2_tweet

schema_handler.register_transformer("v1.1", "v2", transform_twitter_v1_to_v2)

# Usage
v1_response = {
    'id_str': '123456',
    'text': 'Hello world',
    'user': {'id_str': '789', 'screen_name': 'user', 'name': 'User Name'},
    'created_at': 'Mon Jan 15 10:30:00 +0000 2024',
    'retweet_count': 10,
    'favorite_count': 25
}

v2_format = schema_handler.transform(v1_response, "v1.1", "v2")
```

### Deprecation Warning System

```python
from datetime import datetime, timedelta
from typing import Dict, Optional
import logging
import json
from pathlib import Path

logger = logging.getLogger(__name__)

class DeprecationTracker:
    """
    Tracks and alerts on API deprecations.
    """
    
    def __init__(self, config_file: str = "deprecations.json"):
        self.config_file = Path(config_file)
        self.deprecations = self._load_deprecations()
        self.warning_thresholds = [90, 60, 30, 14, 7]  # Days before sunset
    
    def _load_deprecations(self) -> Dict:
        """Load deprecation information."""
        if self.config_file.exists():
            with open(self.config_file, 'r') as f:
                return json.load(f)
        return {}
    
    def _save_deprecations(self):
        """Save deprecation information."""
        with open(self.config_file, 'w') as f:
            json.dump(self.deprecations, f, indent=2)
    
    def register_deprecation(
        self,
        api_name: str,
        version: str,
        sunset_date: str,
        replacement: str,
        migration_guide_url: Optional[str] = None
    ):
        """Register an API deprecation."""
        key = f"{api_name}:{version}"
        self.deprecations[key] = {
            'api_name': api_name,
            'version': version,
            'sunset_date': sunset_date,
            'replacement': replacement,
            'migration_guide_url': migration_guide_url,
            'last_warning': None,
            'usage_count': 0
        }
        self._save_deprecations()
        logger.warning(f"Registered deprecation: {key} - sunset {sunset_date}")
    
    def record_usage(self, api_name: str, version: str):
        """Record usage of a deprecated API."""
        key = f"{api_name}:{version}"
        
        if key not in self.deprecations:
            return  # Not a deprecated API
        
        deprecation = self.deprecations[key]
        deprecation['usage_count'] += 1
        
        # Check if we should warn
        sunset_date = datetime.fromisoformat(deprecation['sunset_date'])
        days_until_sunset = (sunset_date - datetime.utcnow()).days
        
        # Determine if we should warn based on thresholds
        should_warn = False
        for threshold in self.warning_thresholds:
            if days_until_sunset <= threshold:
                last_warning = deprecation.get('last_warning')
                if not last_warning or \
                   (datetime.utcnow() - datetime.fromisoformat(last_warning)).days >= 1:
                    should_warn = True
                    deprecation['last_warning'] = datetime.utcnow().isoformat()
                    break
        
        if should_warn:
            self._send_warning(key, days_until_sunset)
        
        self._save_deprecations()
    
    def _send_warning(self, key: str, days_until_sunset: int):
        """Send deprecation warning."""
        deprecation = self.deprecations[key]
        
        message = (
            f"⚠️ DEPRECATION WARNING\n"
            f"API: {deprecation['api_name']} {deprecation['version']}\n"
            f"Sunset in: {days_until_sunset} days\n"
            f"Replacement: {deprecation['replacement']}\n"
            f"Usage count: {deprecation['usage_count']}\n"
        )
        
        if deprecation.get('migration_guide_url'):
            message += f"Migration guide: {deprecation['migration_guide_url']}\n"
        
        logger.warning(message)
        
        # Send to alerting system (email, Slack, etc.)
        # send_alert(message)
    
    def get_deprecation_report(self) -> Dict:
        """Generate report of all deprecations."""
        report = {
            'active_deprecations': [],
            'upcoming_sunsets': []
        }
        
        now = datetime.utcnow()
        
        for key, deprecation in self.deprecations.items():
            sunset_date = datetime.fromisoformat(deprecation['sunset_date'])
            days_until_sunset = (sunset_date - now).days
            
            if days_until_sunset > 0:
                report['active_deprecations'].append({
                    'key': key,
                    'days_remaining': days_until_sunset,
                    'usage_count': deprecation['usage_count'],
                    'replacement': deprecation['replacement']
                })
                
                if days_until_sunset <= 30:
                    report['upcoming_sunsets'].append(key)
        
        # Sort by days remaining
        report['active_deprecations'].sort(key=lambda x: x['days_remaining'])
        
        return report


# Usage example
tracker = DeprecationTracker()

# Register known deprecations
tracker.register_deprecation(
    api_name="Twitter",
    version="v1.1",
    sunset_date="2024-12-31",
    replacement="v2",
    migration_guide_url="https://developer.twitter.com/en/docs/twitter-api/migrate"
)

tracker.register_deprecation(
    api_name="Facebook Graph API",
    version="v12.0",
    sunset_date="2024-10-15",
    replacement="v18.0",
    migration_guide_url="https://developers.facebook.com/docs/graph-api/changelog"
)

# Record usage (integrate into API client)
tracker.record_usage("Twitter", "v1.1")

# Generate report
report = tracker.get_deprecation_report()
print(f"Active deprecations: {len(report['active_deprecations'])}")
print(f"Urgent (< 30 days): {len(report['upcoming_sunsets'])}")
```

### Automated Testing for API Changes

```python
import requests
import json
from typing import Dict, List
from dataclasses import dataclass
import logging

logger = logging.getLogger(__name__)

@dataclass
class APITestCase:
    """Test case for API endpoint."""
    name: str
    endpoint: str
    method: str
    params: Dict
    expected_status: int
    expected_schema: Dict

class APIChangeDetector:
    """
    Automatically detects changes in API responses.
    Run this daily via cron to catch breaking changes early.
    """
    
    def __init__(self, api_client):
        self.api_client = api_client
        self.test_cases: List[APITestCase] = []
        self.baseline_responses: Dict = {}
    
    def register_test(self, test_case: APITestCase):
        """Register a test case."""
        self.test_cases.append(test_case)
    
    def run_tests(self) -> Dict:
        """Run all test cases and detect changes."""
        results = {
            'passed': [],
            'failed': [],
            'schema_changes': [],
            'errors': []
        }
        
        for test in self.test_cases:
            try:
                # Make API request
                response = self.api_client.make_request(
                    endpoint=test.endpoint,
                    method=test.method,
                    params=test.params
                )
                
                # Check status code
                if response.status_code != test.expected_status:
                    results['failed'].append({
                        'test': test.name,
                        'reason': f"Status code mismatch: {response.status_code} != {test.expected_status}"
                    })
                    continue
                
                # Check schema
                data = response.json()
                schema_diff = self._compare_schema(data, test.expected_schema)
                
                if schema_diff:
                    results['schema_changes'].append({
                        'test': test.name,
                        'changes': schema_diff
                    })
                
                results['passed'].append(test.name)
                
            except Exception as e:
                results['errors'].append({
                    'test': test.name,
                    'error': str(e)
                })
        
        # Send alerts if changes detected
        if results['schema_changes'] or results['failed']:
            self._send_alert(results)
        
        return results
    
    def _compare_schema(self, actual: Dict, expected: Dict) -> List[str]:
        """Compare actual response schema with expected."""
        differences = []
        
        # Check for missing fields
        for key in expected.keys():
            if key not in actual:
                differences.append(f"Missing field: {key}")
        
        # Check for new fields
        for key in actual.keys():
            if key not in expected:
                differences.append(f"New field: {key}")
        
        # Check for type changes
        for key in expected.keys():
            if key in actual:
                expected_type = type(expected[key])
                actual_type = type(actual[key])
                if expected_type != actual_type:
                    differences.append(
                        f"Type change in {key}: {expected_type.__name__} -> {actual_type.__name__}"
                    )
        
        return differences
    
    def _send_alert(self, results: Dict):
        """Send alert about API changes."""
        message = "🚨 API Change Detected!\n\n"
        
        if results['failed']:
            message += "Failed tests:\n"
            for failure in results['failed']:
                message += f"- {failure['test']}: {failure['reason']}\n"
        
        if results['schema_changes']:
            message += "\nSchema changes:\n"
            for change in results['schema_changes']:
                message += f"- {change['test']}:\n"
                for diff in change['changes']:
                    message += f"  * {diff}\n"
        
        logger.error(message)
        # send_slack_alert(message)


# Usage example
detector = APIChangeDetector(api_client=client)

# Register tests
detector.register_test(APITestCase(
    name="Twitter search endpoint",
    endpoint="search/tweets",
    method="GET",
    params={"query": "test", "max_results": 10},
    expected_status=200,
    expected_schema={
        'data': [],
        'meta': {
            'newest_id': '',
            'oldest_id': '',
            'result_count': 0
        }
    }
))

# Run daily via cron
results = detector.run_tests()
print(f"Tests passed: {len(results['passed'])}")
print(f"Tests failed: {len(results['failed'])}")
print(f"Schema changes: {len(results['schema_changes'])}")
```

## Conclusion

Building a robust data collection architecture for social listening requires careful consideration of multiple factors: choosing between real-time and batch collection strategies, managing API rate limits and quotas effectively, setting up reliable webhook systems, designing scalable pipelines, implementing appropriate storage solutions, and preparing for inevitable API changes.

The architecture patterns and code examples in this chapter provide a foundation for production-grade social listening systems. By combining real-time streaming for high-priority content with batch collection for comprehensive coverage, implementing intelligent rate limiting and quota management, using webhooks for instant notifications, building resilient processing pipelines, and adopting hybrid storage strategies, you can create systems that scale efficiently while maintaining reliability.

Remember that social listening infrastructure is not "set and forget"—it requires ongoing monitoring, optimization, and adaptation as platforms evolve and your requirements change. Implement comprehensive logging, monitoring, and alerting from day one. Test your systems regularly for API changes. And always have fallback strategies in place for when things go wrong.

The next chapter will explore advanced data processing and analysis techniques, showing you how to extract meaningful insights from the data you're collecting through this infrastructure.
