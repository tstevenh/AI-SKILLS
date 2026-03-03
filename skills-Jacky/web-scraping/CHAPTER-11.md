# CHAPTER 11: Production Scraping Architecture

## Introduction

Running web scrapers in production requires far more than just writing extraction code. A production-grade scraping system must handle scheduling, monitoring, failure recovery, data storage, scaling, and cost management while operating reliably 24/7.

This chapter covers the architecture and implementation patterns needed to build production scraping systems. We'll explore microservices design, job scheduling with Celery and APScheduler, failure recovery mechanisms, monitoring with Prometheus and Grafana, database design, API layers, horizontal scaling strategies, and cost tracking.

## Microservices Design for Scraping

### Why Microservices?

Traditional monolithic scrapers fail under production load because:

1. **Single points of failure**: One component fails, everything stops
2. **Scaling limitations**: Can't scale individual components independently
3. **Technology lock-in**: Forced to use one stack
4. **Deployment complexity**: All-or-nothing deployments
5. **Maintenance nightmare**: Tight coupling makes changes risky

Microservices separate concerns into independent services:

- **Scheduler**: Decides what and when to scrape
- **Workers**: Execute scraping tasks
- **Storage**: Persists scraped data
- **Queue**: Manages job distribution
- **Monitoring**: Tracks system health
- **API**: Serves data to consumers

### Microservices Architecture Diagram

```
┌─────────────────────────────────────────────────────────────────┐
│                        Production Scraping System                │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│   ┌──────────┐    ┌──────────┐    ┌──────────┐                │
│   │  Admin   │    │  API     │    │  Web UI  │                │
│   │  Panel   │    │  Gateway │    │          │                │
│   └────┬─────┘    └────┬─────┘    └────┬─────┘                │
│        │               │               │                        │
│        └───────────────┼───────────────┘                        │
│                        │                                       │
│              ┌─────────▼─────────┐                            │
│              │   Job Queue       │                            │
│              │   (Redis/RabbitMQ)│                            │
│              └─────────┬─────────┘                            │
│                        │                                       │
│        ┌───────────────┼───────────────┐                       │
│        │               │               │                        │
│   ┌────▼─────┐   ┌────▼─────┐   ┌────▼─────┐                 │
│   │  Worker  │   │  Worker  │   │  Worker  │                 │
│   │   #1     │   │   #2     │   │   #3     │                 │
│   └────┬─────┘   └────┬─────┘   └────┬─────┘                 │
│        │              │              │                         │
│        └──────────────┼──────────────┘                         │
│                       │                                        │
│              ┌────────▼────────┐                              │
│              │   Data Store    │                              │
│              │ (PostgreSQL/Mongo)│                            │
│              └────────┬────────┘                              │
│                       │                                        │
│              ┌────────▼────────┐                              │
│              │   Monitoring    │                              │
│              │(Prometheus/Grafana│                            │
│              └─────────────────┘                              │
└─────────────────────────────────────────────────────────────────┘
```

### Service Definitions

```python
# services/scheduler_service.py
from typing import List, Dict
from datetime import datetime, timedelta
import schedule
import time
import json
from dataclasses import dataclass
from enum import Enum

class TaskPriority(Enum):
    LOW = 1
    MEDIUM = 2
    HIGH = 3
    CRITICAL = 4

@dataclass
class ScrapingTask:
    """Definition of a scraping task"""
    id: str
    url: str
    scraper_type: str
    priority: TaskPriority
    schedule: str  # cron expression
    retry_count: int = 0
    max_retries: int = 3
    created_at: datetime = None
    
    def __post_init__(self):
        if self.created_at is None:
            self.created_at = datetime.now()

class SchedulerService:
    """Central scheduler for all scraping tasks"""
    
    def __init__(self, task_queue, task_store):
        self.task_queue = task_queue
        self.task_store = task_store
        self.tasks: Dict[str, ScrapingTask] = {}
        self.running = False
    
    def register_task(self, task: ScrapingTask):
        """Register a new scraping task"""
        self.tasks[task.id] = task
        
        # Store in database
        self.task_store.save_task(task)
        
        # Schedule job
        self._schedule_task(task)
    
    def _schedule_task(self, task: ScrapingTask):
        """Schedule task using cron expression"""
        # Parse cron and schedule
        # This is simplified - use croniter library in production
        schedule.every(1).hour.do(self._enqueue_task, task)
    
    def _enqueue_task(self, task: ScrapingTask):
        """Add task to queue"""
        job = {
            'task_id': task.id,
            'url': task.url,
            'scraper_type': task.scraper_type,
            'priority': task.priority.value,
            'retry_count': task.retry_count,
            'created_at': task.created_at.isoformat()
        }
        
        self.task_queue.enqueue(job, priority=task.priority.value)
        print(f"Enqueued task {task.id} for {task.url}")
    
    def run_pending(self):
        """Run pending scheduled tasks"""
        schedule.run_pending()
    
    def start(self):
        """Start scheduler loop"""
        self.running = True
        print("Scheduler started")
        
        while self.running:
            self.run_pending()
            time.sleep(1)
    
    def stop(self):
        """Stop scheduler"""
        self.running = False
        print("Scheduler stopped")
```

```python
# services/worker_service.py
from typing import Dict, Optional
import json
import time
import traceback
from datetime import datetime
from dataclasses import dataclass

@dataclass
class ScrapingResult:
    """Result of a scraping job"""
    task_id: str
    success: bool
    data: Optional[Dict]
    error: Optional[str]
    duration_ms: int
    timestamp: datetime
    bytes_downloaded: int = 0
    status_code: Optional[int] = None

class WorkerService:
    """Worker that executes scraping tasks"""
    
    def __init__(self, task_queue, result_store, scraper_registry):
        self.task_queue = task_queue
        self.result_store = result_store
        self.scraper_registry = scraper_registry
        self.running = False
        self.worker_id = f"worker_{time.time()}"
    
    def start(self):
        """Start worker loop"""
        self.running = True
        print(f"Worker {self.worker_id} started")
        
        while self.running:
            try:
                # Get job from queue
                job = self.task_queue.dequeue(timeout=5)
                
                if job:
                    self._process_job(job)
                    
            except Exception as e:
                print(f"Worker error: {e}")
                time.sleep(1)
    
    def _process_job(self, job: Dict):
        """Process a single scraping job"""
        start_time = time.time()
        task_id = job['task_id']
        scraper_type = job['scraper_type']
        url = job['url']
        
        print(f"Processing job {task_id}: {url}")
        
        try:
            # Get appropriate scraper
            scraper = self.scraper_registry.get(scraper_type)
            
            if not scraper:
                raise ValueError(f"Unknown scraper type: {scraper_type}")
            
            # Execute scraping
            data = scraper.scrape(url)
            
            # Calculate metrics
            duration_ms = int((time.time() - start_time) * 1000)
            bytes_downloaded = len(json.dumps(data)) if data else 0
            
            # Create result
            result = ScrapingResult(
                task_id=task_id,
                success=True,
                data=data,
                error=None,
                duration_ms=duration_ms,
                timestamp=datetime.now(),
                bytes_downloaded=bytes_downloaded,
                status_code=200
            )
            
        except Exception as e:
            duration_ms = int((time.time() - start_time) * 1000)
            
            result = ScrapingResult(
                task_id=task_id,
                success=False,
                data=None,
                error=str(e),
                duration_ms=duration_ms,
                timestamp=datetime.now(),
                status_code=None
            )
            
            print(f"Job {task_id} failed: {e}")
            traceback.print_exc()
        
        # Store result
        self.result_store.save_result(result)
        
        # Update metrics
        self._update_metrics(result)
    
    def _update_metrics(self, result: ScrapingResult):
        """Update worker metrics"""
        # Send to monitoring service
        pass
    
    def stop(self):
        """Stop worker"""
        self.running = False
        print(f"Worker {self.worker_id} stopped")
```

## Job Scheduling

### Celery for Distributed Task Processing

Celery is the industry standard for distributed task queues in Python.

```python
# celery_app.py
from celery import Celery
from celery.signals import task_failure, task_success
import os

# Configure Celery
app = Celery(
    'scraping_tasks',
    broker=os.getenv('CELERY_BROKER_URL', 'redis://localhost:6379/0'),
    backend=os.getenv('CELERY_RESULT_BACKEND', 'redis://localhost:6379/0')
)

app.conf.update(
    task_serializer='json',
    accept_content=['json'],
    result_serializer='json',
    timezone='UTC',
    enable_utc=True,
    task_track_started=True,
    task_time_limit=300,  # 5 minute hard limit
    task_soft_time_limit=240,  # 4 minute soft limit
    worker_prefetch_multiplier=1,  # Don't prefetch tasks
    worker_max_tasks_per_child=50,  # Restart workers periodically
)

# Scraping tasks
@app.task(bind=True, max_retries=3, default_retry_delay=60)
def scrape_url(self, url: str, scraper_type: str, metadata: dict = None):
    """Scrape a single URL"""
    from scrapers import get_scraper
    
    try:
        scraper = get_scraper(scraper_type)
        result = scraper.scrape(url)
        
        # Store result
        store_result.delay(url, result, metadata)
        
        return {
            'url': url,
            'status': 'success',
            'items_count': len(result) if isinstance(result, list) else 1
        }
        
    except Exception as exc:
        # Retry with exponential backoff
        self.retry(exc=exc, countdown=60 * (2 ** self.request.retries))

@app.task
def store_result(url: str, data: dict, metadata: dict = None):
    """Store scraping result"""
    from storage import DataStore
    
    store = DataStore()
    store.save(url, data, metadata)
    
    return {'status': 'stored', 'url': url}

@app.task
def scrape_batch(urls: list, scraper_type: str):
    """Scrape multiple URLs in batch"""
    results = []
    
    for url in urls:
        # Create subtask for each URL
        result = scrape_url.delay(url, scraper_type)
        results.append(result.id)
    
    return {
        'batch_id': scrape_batch.request.id,
        'tasks_created': len(results),
        'task_ids': results
    }

@app.task
def scheduled_crawl(site_config: dict):
    """Scheduled crawling task"""
    from crawler import Crawler
    
    crawler = Crawler(site_config)
    urls = crawler.discover_urls()
    
    # Create batch task
    return scrape_batch.delay(
        urls=urls,
        scraper_type=site_config['scraper_type']
    )

# Monitoring signals
@task_success.connect
def handle_success(sender=None, result=None, **kwargs):
    """Handle successful task"""
    print(f"Task {sender.request.id} succeeded")
    # Send metrics to monitoring

@task_failure.connect
def handle_failure(sender=None, task_id=None, exception=None, **kwargs):
    """Handle failed task"""
    print(f"Task {task_id} failed: {exception}")
    # Alert on critical failures
```

```python
# celery_beat_schedule.py
from celery.schedules import crontab

# Periodic task schedule
beat_schedule = {
    'scrape-amazon-hourly': {
        'task': 'celery_app.scheduled_crawl',
        'schedule': crontab(minute=0, hour='*/1'),
        'args': ([{
            'site': 'amazon',
            'scraper_type': 'amazon_product',
            'category': 'electronics'
        }],)
    },
    'scrape-news-daily': {
        'task': 'celery_app.scheduled_crawl',
        'schedule': crontab(minute=0, hour=6),
        'args': ([{
            'site': 'news_sites',
            'scraper_type': 'news_article',
            'feeds': ['tech', 'business']
        }],)
    },
    'cleanup-old-data': {
        'task': 'maintenance.cleanup_old_data',
        'schedule': crontab(minute=0, hour=2),
        'args': (30,)  # Keep 30 days
    }
}
```

### APScheduler for In-Process Scheduling

For simpler deployments, APScheduler runs inside your application.

```python
# scheduler.py
from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.triggers.cron import CronTrigger
from apscheduler.triggers.interval import IntervalTrigger
from apscheduler.events import EVENT_JOB_EXECUTED, EVENT_JOB_ERROR
import logging

logging.basicConfig()
logging.getLogger('apscheduler').setLevel(logging.DEBUG)

class ScrapingScheduler:
    """APScheduler wrapper for scraping tasks"""
    
    def __init__(self):
        self.scheduler = BackgroundScheduler(
            job_defaults={
                'coalesce': True,  # Run once if multiple missed
                'max_instances': 1,  # Only one instance at a time
                'misfire_grace_time': 300  # 5 minute grace period
            }
        )
        self.scheduler.add_listener(
            self._job_listener,
            EVENT_JOB_EXECUTED | EVENT_JOB_ERROR
        )
    
    def _job_listener(self, event):
        """Listen for job events"""
        if event.exception:
            print(f"Job {event.job_id} crashed: {event.exception}")
        else:
            print(f"Job {event.job_id} executed successfully")
    
    def add_cron_job(self, func, job_id: str, cron: str, args=None, kwargs=None):
        """Add cron-scheduled job"""
        trigger = CronTrigger.from_crontab(cron)
        
        self.scheduler.add_job(
            func=func,
            trigger=trigger,
            id=job_id,
            args=args or [],
            kwargs=kwargs or {},
            replace_existing=True
        )
        
        print(f"Added cron job: {job_id} ({cron})")
    
    def add_interval_job(self, func, job_id: str, minutes: int, 
                        args=None, kwargs=None):
        """Add interval-scheduled job"""
        trigger = IntervalTrigger(minutes=minutes)
        
        self.scheduler.add_job(
            func=func,
            trigger=trigger,
            id=job_id,
            args=args or [],
            kwargs=kwargs or {},
            replace_existing=True
        )
        
        print(f"Added interval job: {job_id} (every {minutes} min)")
    
    def remove_job(self, job_id: str):
        """Remove scheduled job"""
        self.scheduler.remove_job(job_id)
        print(f"Removed job: {job_id}")
    
    def get_jobs(self):
        """Get all scheduled jobs"""
        return self.scheduler.get_jobs()
    
    def start(self):
        """Start scheduler"""
        self.scheduler.start()
        print("Scheduler started")
    
    def shutdown(self, wait=True):
        """Shutdown scheduler"""
        self.scheduler.shutdown(wait=wait)
        print("Scheduler shutdown")

# Usage
def scrape_amazon():
    """Amazon scraping task"""
    print("Scraping Amazon...")
    # Actual scraping logic

scheduler = ScrapingScheduler()

# Add jobs
scheduler.add_cron_job(
    scrape_amazon,
    'amazon-hourly',
    '0 * * * *'  # Every hour
)

scheduler.add_interval_job(
    scrape_amazon,
    'amazon-frequent',
    minutes=30
)

# Start
scheduler.start()

# Keep running
try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    scheduler.shutdown()
```

### System Cron for Simple Scheduling

For basic needs, system cron is still effective.

```bash
# /etc/cron.d/scraping
# Run scrapers at scheduled times

# Scrape every hour
0 * * * * scraper /opt/scraper/venv/bin/python /opt/scraper/jobs/amazon.py >> /var/log/scraper/amazon.log 2>&1

# Scrape daily at 6 AM
0 6 * * * scraper /opt/scraper/venv/bin/python /opt/scraper/jobs/news.py >> /var/log/scraper/news.log 2>&1

# Cleanup weekly
0 2 * * 0 scraper /opt/scraper/venv/bin/python /opt/scraper/jobs/cleanup.py >> /var/log/scraper/cleanup.log 2>&1
```

```python
# jobs/amazon.py
#!/usr/bin/env python3
"""Amazon scraping job - designed to be run by cron"""
import sys
import logging
from pathlib import Path

# Setup logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

def main():
    """Main job function"""
    try:
        from scrapers.amazon_scraper import AmazonScraper
        from storage import DataStore
        
        logger.info("Starting Amazon scrape job")
        
        # Load configuration
        config = load_config()
        
        # Initialize scraper
        scraper = AmazonScraper(config)
        
        # Scrape
        results = scraper.scrape_categories(config['categories'])
        
        # Store results
        store = DataStore()
        store.save_batch(results)
        
        logger.info(f"Successfully scraped {len(results)} items")
        
        return 0
        
    except Exception as e:
        logger.exception("Scrape job failed")
        return 1

def load_config():
    """Load job configuration"""
    import json
    
    config_path = Path(__file__).parent / 'config' / 'amazon.json'
    
    with open(config_path) as f:
        return json.load(f)

if __name__ == '__main__':
    sys.exit(main())
```

## Failure Recovery and Retry Logic

### Exponential Backoff with Jitter

```python
import random
import time
from functools import wraps
from typing import Callable, Type, Tuple

def exponential_backoff(
    max_retries: int = 3,
    base_delay: float = 1.0,
    max_delay: float = 60.0,
    exceptions: Tuple[Type[Exception], ...] = (Exception,),
    on_retry: Callable = None
):
    """Decorator for retry with exponential backoff and jitter"""
    
    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args, **kwargs):
            last_exception = None
            
            for attempt in range(max_retries + 1):
                try:
                    return func(*args, **kwargs)
                    
                except exceptions as e:
                    last_exception = e
                    
                    if attempt == max_retries:
                        # Final attempt failed
                        raise last_exception
                    
                    # Calculate delay with exponential backoff and jitter
                    delay = min(base_delay * (2 ** attempt), max_delay)
                    jitter = random.uniform(0, delay * 0.1)  # 10% jitter
                    total_delay = delay + jitter
                    
                    if on_retry:
                        on_retry(attempt + 1, max_retries, e, total_delay)
                    
                    print(f"Attempt {attempt + 1} failed: {e}. "
                          f"Retrying in {total_delay:.2f}s...")
                    
                    time.sleep(total_delay)
            
            raise last_exception
        
        return wrapper
    return decorator

# Usage
@exponential_backoff(
    max_retries=3,
    base_delay=2.0,
    exceptions=(ConnectionError, TimeoutError)
)
def fetch_page(url: str) -> str:
    """Fetch page with retry logic"""
    import requests
    
    response = requests.get(url, timeout=10)
    response.raise_for_status()
    return response.text

# Circuit Breaker Pattern
class CircuitBreaker:
    """Circuit breaker pattern for fault tolerance"""
    
    def __init__(
        self,
        failure_threshold: int = 5,
        recovery_timeout: float = 60.0,
        half_open_max_calls: int = 3
    ):
        self.failure_threshold = failure_threshold
        self.recovery_timeout = recovery_timeout
        self.half_open_max_calls = half_open_max_calls
        
        self.failure_count = 0
        self.last_failure_time = None
        self.state = 'CLOSED'  # CLOSED, OPEN, HALF_OPEN
        self.half_open_calls = 0
    
    def call(self, func: Callable, *args, **kwargs):
        """Call function with circuit breaker protection"""
        
        if self.state == 'OPEN':
            # Check if recovery timeout has passed
            if self._should_attempt_reset():
                self.state = 'HALF_OPEN'
                self.half_open_calls = 0
            else:
                raise CircuitBreakerOpenError(
                    "Circuit breaker is OPEN - service unavailable"
                )
        
        if self.state == 'HALF_OPEN':
            if self.half_open_calls >= self.half_open_max_calls:
                raise CircuitBreakerOpenError(
                    "Circuit breaker HALF_OPEN limit reached"
                )
            self.half_open_calls += 1
        
        try:
            result = func(*args, **kwargs)
            self._on_success()
            return result
            
        except Exception as e:
            self._on_failure()
            raise e
    
    def _should_attempt_reset(self) -> bool:
        """Check if enough time has passed to try reset"""
        if self.last_failure_time is None:
            return True
        
        elapsed = time.time() - self.last_failure_time
        return elapsed >= self.recovery_timeout
    
    def _on_success(self):
        """Handle successful call"""
        if self.state == 'HALF_OPEN':
            # Reset circuit
            self.state = 'CLOSED'
            self.failure_count = 0
            self.half_open_calls = 0
    
    def _on_failure(self):
        """Handle failed call"""
        self.failure_count += 1
        self.last_failure_time = time.time()
        
        if self.state == 'CLOSED' and self.failure_count >= self.failure_threshold:
            self.state = 'OPEN'
            print(f"Circuit breaker opened after {self.failure_count} failures")
        
        elif self.state == 'HALF_OPEN':
            self.state = 'OPEN'
            print("Circuit breaker re-opened in HALF_OPEN state")

class CircuitBreakerOpenError(Exception):
    """Circuit breaker is open"""
    pass

# Usage
cb = CircuitBreaker(failure_threshold=3, recovery_timeout=30)

def call_api():
    # This might fail
    import random
    if random.random() < 0.7:
        raise ConnectionError("API unavailable")
    return "Success"

# Wrap calls with circuit breaker
try:
    result = cb.call(call_api)
    print(f"Result: {result}")
except CircuitBreakerOpenError as e:
    print(f"Circuit open: {e}")
```

### Dead Letter Queue

```python
from typing import Dict, Any
from datetime import datetime
import json

class DeadLetterQueue:
    """Store failed jobs for later analysis and replay"""
    
    def __init__(self, storage_backend):
        self.storage = storage_backend
    
    def enqueue_failed(self, job: Dict[str, Any], error: Exception, 
                       context: Dict = None):
        """Add failed job to DLQ"""
        failed_job = {
            'original_job': job,
            'error': {
                'type': type(error).__name__,
                'message': str(error),
                'traceback': traceback.format_exc()
            },
            'context': context or {},
            'failed_at': datetime.now().isoformat(),
            'retry_count': job.get('retry_count', 0),
            'status': 'failed'
        }
        
        self.storage.save(failed_job)
        
        # Alert if critical
        if job.get('priority') == 'critical':
            self._alert_critical_failure(job, error)
    
    def retry_failed(self, job_id: str = None, max_age_hours: int = 24):
        """Retry failed jobs"""
        cutoff = datetime.now() - timedelta(hours=max_age_hours)
        
        if job_id:
            # Retry specific job
            failed_job = self.storage.get(job_id)
            if failed_job:
                return self._retry_job(failed_job)
        else:
            # Retry all recent failed jobs
            failed_jobs = self.storage.get_all(
                status='failed',
                failed_after=cutoff
            )
            
            results = []
            for job in failed_jobs:
                result = self._retry_job(job)
                results.append(result)
            
            return results
    
    def _retry_job(self, failed_job: Dict) -> Dict:
        """Retry a single failed job"""
        job = failed_job['original_job']
        job['retry_count'] = failed_job.get('retry_count', 0) + 1
        
        try:
            # Re-submit to main queue
            self.task_queue.enqueue(job)
            
            # Mark as retried
            failed_job['status'] = 'retried'
            failed_job['retried_at'] = datetime.now().isoformat()
            self.storage.update(failed_job)
            
            return {'success': True, 'job_id': job['id']}
            
        except Exception as e:
            return {'success': False, 'error': str(e)}
    
    def _alert_critical_failure(self, job: Dict, error: Exception):
        """Alert on critical job failure"""
        # Send to monitoring/alerting system
        pass
    
    def get_stats(self) -> Dict:
        """Get DLQ statistics"""
        return {
            'total_failed': self.storage.count(status='failed'),
            'retried': self.storage.count(status='retried'),
            'permanently_failed': self.storage.count(status='failed', retry_count__gte=5)
        }
```

## Monitoring and Alerting

### Prometheus Metrics

```python
# monitoring/metrics.py
from prometheus_client import Counter, Histogram, Gauge, Info, start_http_server
import time

# Define metrics
scraping_jobs_total = Counter(
    'scraping_jobs_total',
    'Total scraping jobs executed',
    ['status', 'scraper_type', 'site']
)

scraping_duration_seconds = Histogram(
    'scraping_duration_seconds',
    'Time spent scraping',
    ['scraper_type', 'site'],
    buckets=[1, 5, 10, 30, 60, 120, 300, 600]
)

scraping_items_scraped = Counter(
    'scraping_items_scraped_total',
    'Total items scraped',
    ['scraper_type', 'site']
)

scraping_errors_total = Counter(
    'scraping_errors_total',
    'Total scraping errors',
    ['error_type', 'scraper_type']
)

active_scrapers = Gauge(
    'scraping_active_scrapers',
    'Number of currently running scrapers',
    ['scraper_type']
)

queue_size = Gauge(
    'scraping_queue_size',
    'Current queue size',
    ['queue_name']
)

scraper_info = Info(
    'scraping_version',
    'Scraper version information'
)

class MetricsCollector:
    """Collect and expose Prometheus metrics"""
    
    def __init__(self, port: int = 8000):
        self.port = port
        self._started = False
    
    def start(self):
        """Start metrics server"""
        if not self._started:
            start_http_server(self.port)
            self._started = True
            
            # Set version info
            scraper_info.info({'version': '1.0.0', 'build': 'abc123'})
            
            print(f"Metrics server started on port {self.port}")
    
    def record_job_start(self, scraper_type: str, site: str):
        """Record job start"""
        active_scrapers.labels(scraper_type=scraper_type).inc()
    
    def record_job_complete(self, scraper_type: str, site: str, 
                           items_count: int, duration: float, 
                           success: bool = True):
        """Record job completion"""
        status = 'success' if success else 'failure'
        
        scraping_jobs_total.labels(
            status=status,
            scraper_type=scraper_type,
            site=site
        ).inc()
        
        scraping_duration_seconds.labels(
            scraper_type=scraper_type,
            site=site
        ).observe(duration)
        
        scraping_items_scraped.labels(
            scraper_type=scraper_type,
            site=site
        ).inc(items_count)
        
        active_scrapers.labels(scraper_type=scraper_type).dec()
    
    def record_error(self, error_type: str, scraper_type: str):
        """Record error"""
        scraping_errors_total.labels(
            error_type=error_type,
            scraper_type=scraper_type
        ).inc()
    
    def set_queue_size(self, queue_name: str, size: int):
        """Update queue size gauge"""
        queue_size.labels(queue_name=queue_name).set(size)

# Usage
collector = MetricsCollector(port=8000)
collector.start()

@contextmanager
def timed_scrape(scraper_type: str, site: str):
    """Context manager for timing scrapes"""
    collector.record_job_start(scraper_type, site)
    start = time.time()
    
    try:
        yield
        success = True
        items_count = 0  # Set based on actual results
        
    except Exception as e:
        success = False
        collector.record_error(type(e).__name__, scraper_type)
        raise
        
    finally:
        duration = time.time() - start
        collector.record_job_complete(
            scraper_type, site, items_count, duration, success
        )

# Example
with timed_scrape('amazon', 'amazon.com'):
    # Do scraping
    results = scrape_amazon()
```

### Grafana Dashboard Configuration

```json
{
  "dashboard": {
    "title": "Scraping System Dashboard",
    "panels": [
      {
        "title": "Jobs Per Minute",
        "type": "graph",
        "targets": [
          {
            "expr": "rate(scraping_jobs_total[1m])",
            "legendFormat": "{{status}} - {{scraper_type}}"
          }
        ]
      },
      {
        "title": "Scraping Duration",
        "type": "graph",
        "targets": [
          {
            "expr": "histogram_quantile(0.95, rate(scraping_duration_seconds_bucket[5m]))",
            "legendFormat": "95th percentile - {{scraper_type}}"
          }
        ]
      },
      {
        "title": "Error Rate",
        "type": "graph",
        "targets": [
          {
            "expr": "rate(scraping_errors_total[5m])",
            "legendFormat": "{{error_type}}"
          }
        ]
      },
      {
        "title": "Items Scraped",
        "type": "stat",
        "targets": [
          {
            "expr": "scraping_items_scraped_total",
            "legendFormat": "{{scraper_type}}"
          }
        ]
      },
      {
        "title": "Queue Size",
        "type": "graph",
        "targets": [
          {
            "expr": "scraping_queue_size",
            "legendFormat": "{{queue_name}}"
          }
        ]
      }
    ]
  }
}
```

### Alerting Configuration

```yaml
# alerts/alert_rules.yml
groups:
  - name: scraping_alerts
    interval: 30s
    rules:
      - alert: HighErrorRate
        expr: |
          (
            sum(rate(scraping_errors_total[5m])) 
            / 
            sum(rate(scraping_jobs_total[5m]))
          ) > 0.1
        for: 5m
        labels:
          severity: warning
        annotations:
          summary: "High error rate in scraping system"
          description: "Error rate is above 10% for 5 minutes"
      
      - alert: NoJobsRunning
        expr: |
          sum(scraping_jobs_total) == 0
        for: 10m
        labels:
          severity: critical
        annotations:
          summary: "No scraping jobs running"
          description: "No jobs have run in the last 10 minutes"
      
      - alert: QueueBacklog
        expr: |
          scraping_queue_size > 1000
        for: 5m
        labels:
          severity: warning
        annotations:
          summary: "Queue backlog detected"
          description: "Queue size is {{ $value }} items"
      
      - alert: ScrapeDurationTooHigh
        expr: |
          histogram_quantile(0.95, rate(scraping_duration_seconds_bucket[5m])) > 300
        for: 10m
        labels:
          severity: warning
        annotations:
          summary: "Scrape duration is too high"
          description: "95th percentile scrape time is above 5 minutes"
```

```python
# alerting/alerter.py
import requests
from typing import List
from datetime import datetime

class AlertManager:
    """Send alerts to various channels"""
    
    def __init__(self, config: dict):
        self.config = config
        self.slack_webhook = config.get('slack_webhook')
        self.email_api = config.get('email_api')
        self.pagerduty_key = config.get('pagerduty_key')
    
    def send_alert(self, alert: dict, channels: List[str] = None):
        """Send alert to specified channels"""
        channels = channels or ['slack']
        
        for channel in channels:
            method = getattr(self, f'_send_{channel}', None)
            if method:
                try:
                    method(alert)
                except Exception as e:
                    print(f"Failed to send alert to {channel}: {e}")
    
    def _send_slack(self, alert: dict):
        """Send alert to Slack"""
        if not self.slack_webhook:
            return
        
        color = {
            'critical': '#FF0000',
            'warning': '#FFA500',
            'info': '#00FF00'
        }.get(alert.get('severity'), '#808080')
        
        payload = {
            "attachments": [
                {
                    "color": color,
                    "title": alert.get('title', 'Alert'),
                    "text": alert.get('message', ''),
                    "fields": [
                        {"title": "Severity", "value": alert.get('severity'), "short": True},
                        {"title": "Time", "value": datetime.now().isoformat(), "short": True}
                    ],
                    "footer": "Scraping System"
                }
            ]
        }
        
        requests.post(self.slack_webhook, json=payload)
    
    def _send_pagerduty(self, alert: dict):
        """Send alert to PagerDuty"""
        if not self.pagerduty_key:
            return
        
        payload = {
            "routing_key": self.pagerduty_key,
            "event_action": "trigger",
            "dedup_key": alert.get('id'),
            "payload": {
                "summary": alert.get('title'),
                "severity": alert.get('severity', 'warning'),
                "source": alert.get('source', 'scraping-system'),
                "custom_details": alert
            }
        }
        
        requests.post(
            "https://events.pagerduty.com/v2/enqueue",
            json=payload
        )
```

## Database Design for Scraped Data

### PostgreSQL Schema

```sql
-- migrations/001_initial.sql
-- Core tables for scraped data storage

CREATE TABLE sources (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL UNIQUE,
    url VARCHAR(500),
    scraper_type VARCHAR(100) NOT NULL,
    config JSONB DEFAULT '{}',
    is_active BOOLEAN DEFAULT true,
    created_at TIMESTAMP DEFAULT NOW(),
    updated_at TIMESTAMP DEFAULT NOW()
);

CREATE TABLE scraping_jobs (
    id SERIAL PRIMARY KEY,
    source_id INTEGER REFERENCES sources(id),
    status VARCHAR(50) DEFAULT 'pending',
    started_at TIMESTAMP,
    completed_at TIMESTAMP,
    duration_ms INTEGER,
    items_count INTEGER DEFAULT 0,
    error_message TEXT,
    metadata JSONB DEFAULT '{}',
    created_at TIMESTAMP DEFAULT NOW()
);

CREATE TABLE scraped_items (
    id SERIAL PRIMARY KEY,
    job_id INTEGER REFERENCES scraping_jobs(id),
    source_id INTEGER REFERENCES sources(id),
    url TEXT NOT NULL,
    title TEXT,
    content JSONB NOT NULL,
    raw_html TEXT,
    hash VARCHAR(64),
    scraped_at TIMESTAMP DEFAULT NOW(),
    updated_at TIMESTAMP DEFAULT NOW(),
    is_duplicate BOOLEAN DEFAULT false,
    quality_score FLOAT DEFAULT 0.0
);

CREATE TABLE url_queue (
    id SERIAL PRIMARY KEY,
    source_id INTEGER REFERENCES sources(id),
    url TEXT NOT NULL,
    status VARCHAR(50) DEFAULT 'pending',
    priority INTEGER DEFAULT 5,
    retry_count INTEGER DEFAULT 0,
    scheduled_at TIMESTAMP DEFAULT NOW(),
    last_attempt_at TIMESTAMP,
    created_at TIMESTAMP DEFAULT NOW()
);

CREATE TABLE change_log (
    id SERIAL PRIMARY KEY,
    item_id INTEGER REFERENCES scraped_items(id),
    field_name VARCHAR(100),
    old_value JSONB,
    new_value JSONB,
    changed_at TIMESTAMP DEFAULT NOW()
);

-- Indexes for performance
CREATE INDEX idx_scraped_items_source ON scraped_items(source_id);
CREATE INDEX idx_scraped_items_scraped_at ON scraped_items(scraped_at);
CREATE INDEX idx_scraped_items_hash ON scraped_items(hash);
CREATE INDEX idx_url_queue_status ON url_queue(status);
CREATE INDEX idx_url_queue_scheduled ON url_queue(scheduled_at);
CREATE INDEX idx_jobs_source_status ON scraping_jobs(source_id, status);

-- GIN indexes for JSONB
CREATE INDEX idx_scraped_items_content ON scraped_items USING GIN(content);
CREATE INDEX idx_sources_config ON sources USING GIN(config);
```

### Python Models

```python
# models.py
from sqlalchemy import create_engine, Column, Integer, String, DateTime, Text, Float, Boolean, ForeignKey, JSON
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from datetime import datetime

Base = declarative_base()

class Source(Base):
    """Scraping source definition"""
    __tablename__ = 'sources'
    
    id = Column(Integer, primary_key=True)
    name = Column(String(255), unique=True, nullable=False)
    url = Column(String(500))
    scraper_type = Column(String(100), nullable=False)
    config = Column(JSON, default={})
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    jobs = relationship('ScrapingJob', back_populates='source')
    items = relationship('ScrapedItem', back_populates='source')

class ScrapingJob(Base):
    """Record of a scraping job execution"""
    __tablename__ = 'scraping_jobs'
    
    id = Column(Integer, primary_key=True)
    source_id = Column(Integer, ForeignKey('sources.id'))
    status = Column(String(50), default='pending')
    started_at = Column(DateTime)
    completed_at = Column(DateTime)
    duration_ms = Column(Integer)
    items_count = Column(Integer, default=0)
    error_message = Column(Text)
    metadata = Column(JSON, default={})
    created_at = Column(DateTime, default=datetime.utcnow)
    
    source = relationship('Source', back_populates='jobs')
    items = relationship('ScrapedItem', back_populates='job')

class ScrapedItem(Base):
    """Individual scraped item"""
    __tablename__ = 'scraped_items'
    
    id = Column(Integer, primary_key=True)
    job_id = Column(Integer, ForeignKey('scraping_jobs.id'))
    source_id = Column(Integer, ForeignKey('sources.id'))
    url = Column(Text, nullable=False)
    title = Column(Text)
    content = Column(JSON, nullable=False)
    raw_html = Column(Text)
    hash = Column(String(64))
    scraped_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    is_duplicate = Column(Boolean, default=False)
    quality_score = Column(Float, default=0.0)
    
    job = relationship('ScrapingJob', back_populates='items')
    source = relationship('Source', back_populates='items')

# Data access layer
class DataStore:
    """High-level data store for scraped data"""
    
    def __init__(self, db_url: str):
        self.engine = create_engine(db_url)
        Session = sessionmaker(bind=self.engine)
        self.session = Session()
    
    def create_job(self, source_id: int, metadata: dict = None) -> ScrapingJob:
        """Create new scraping job record"""
        job = ScrapingJob(
            source_id=source_id,
            metadata=metadata or {},
            started_at=datetime.utcnow(),
            status='running'
        )
        self.session.add(job)
        self.session.commit()
        return job
    
    def save_item(self, job: ScrapingJob, url: str, content: dict, 
                  title: str = None, raw_html: str = None):
        """Save scraped item"""
        import hashlib
        
        # Calculate hash for deduplication
        content_str = str(sorted(content.items()))
        content_hash = hashlib.sha256(content_str.encode()).hexdigest()
        
        item = ScrapedItem(
            job_id=job.id,
            source_id=job.source_id,
            url=url,
            title=title,
            content=content,
            raw_html=raw_html,
            hash=content_hash,
            scraped_at=datetime.utcnow()
        )
        
        self.session.add(item)
        job.items_count += 1
        
        self.session.commit()
        return item
    
    def complete_job(self, job: ScrapingJob, success: bool = True, 
                     error: str = None):
        """Mark job as complete"""
        job.status = 'completed' if success else 'failed'
        job.completed_at = datetime.utcnow()
        
        if job.started_at:
            duration = (job.completed_at - job.started_at).total_seconds() * 1000
            job.duration_ms = int(duration)
        
        if error:
            job.error_message = error
        
        self.session.commit()
    
    def get_recent_items(self, source_id: int = None, 
                        limit: int = 100) -> list:
        """Get recent scraped items"""
        query = self.session.query(ScrapedItem)
        
        if source_id:
            query = query.filter(ScrapedItem.source_id == source_id)
        
        return query.order_by(ScrapedItem.scraped_at.desc()).limit(limit).all()
    
    def find_duplicates(self, source_id: int) -> list:
        """Find duplicate items"""
        from sqlalchemy import func
        
        return self.session.query(
            ScrapedItem.hash,
            func.count(ScrapedItem.id).label('count')
        ).filter(
            ScrapedItem.source_id == source_id
        ).group_by(
            ScrapedItem.hash
        ).having(
            func.count(ScrapedItem.id) > 1
        ).all()
```

## API Layer for Consumers

### FastAPI Implementation

```python
# api/main.py
from fastapi import FastAPI, HTTPException, Depends, Query
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field
from typing import List, Optional
from datetime import datetime
from enum import Enum

app = FastAPI(
    title="Scraping Data API",
    description="API for accessing scraped data",
    version="1.0.0"
)

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Models
class ItemResponse(BaseModel):
    id: int
    url: str
    title: Optional[str]
    content: dict
    scraped_at: datetime
    source: str
    
    class Config:
        orm_mode = True

class ScrapingRequest(BaseModel):
    url: str = Field(..., description="URL to scrape")
    scraper_type: str = Field(default="generic", description="Type of scraper to use")
    priority: int = Field(default=5, ge=1, le=10)
    metadata: Optional[dict] = Field(default=None)

class JobResponse(BaseModel):
    job_id: str
    status: str
    message: str

# Dependencies
def get_db():
    """Database dependency"""
    from models import DataStore
    store = DataStore("postgresql://user:pass@localhost/scraping")
    try:
        yield store
    finally:
        store.session.close()

# Routes
@app.get("/")
def root():
    return {"message": "Scraping Data API", "version": "1.0.0"}

@app.get("/health")
def health():
    return {"status": "healthy", "timestamp": datetime.utcnow().isoformat()}

@app.get("/items", response_model=List[ItemResponse])
def get_items(
    source: Optional[str] = None,
    limit: int = Query(20, ge=1, le=100),
    offset: int = Query(0, ge=0),
    db: DataStore = Depends(get_db)
):
    """Get scraped items with optional filtering"""
    from models import ScrapedItem, Source
    
    query = db.session.query(ScrapedItem).join(Source)
    
    if source:
        query = query.filter(Source.name == source)
    
    items = query.order_by(ScrapedItem.scraped_at.desc()).offset(offset).limit(limit).all()
    
    return [
        ItemResponse(
            id=item.id,
            url=item.url,
            title=item.title,
            content=item.content,
            scraped_at=item.scraped_at,
            source=item.source.name
        )
        for item in items
    ]

@app.get("/items/{item_id}", response_model=ItemResponse)
def get_item(item_id: int, db: DataStore = Depends(get_db)):
    """Get specific item by ID"""
    from models import ScrapedItem
    
    item = db.session.query(ScrapedItem).filter(ScrapedItem.id == item_id).first()
    
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    
    return ItemResponse(
        id=item.id,
        url=item.url,
        title=item.title,
        content=item.content,
        scraped_at=item.scraped_at,
        source=item.source.name
    )

@app.post("/scrape", response_model=JobResponse)
def request_scrape(request: ScrapingRequest):
    """Request a new scraping job"""
    from celery_app import scrape_url
    
    # Submit to queue
    task = scrape_url.delay(
        url=request.url,
        scraper_type=request.scraper_type,
        metadata=request.metadata
    )
    
    return JobResponse(
        job_id=task.id,
        status="queued",
        message=f"Scraping job queued for {request.url}"
    )

@app.get("/scrape/status/{job_id}")
def get_job_status(job_id: str):
    """Get status of scraping job"""
    from celery_app import app
    
    result = app.AsyncResult(job_id)
    
    return {
        "job_id": job_id,
        "status": result.status,
        "result": result.result if result.ready() else None
    }

@app.get("/sources")
def get_sources(db: DataStore = Depends(get_db)):
    """Get available scraping sources"""
    from models import Source
    
    sources = db.session.query(Source).filter(Source.is_active == True).all()
    
    return [
        {
            "id": s.id,
            "name": s.name,
            "url": s.url,
            "scraper_type": s.scraper_type
        }
        for s in sources
    ]

@app.get("/stats")
def get_stats(db: DataStore = Depends(get_db)):
    """Get scraping statistics"""
    from models import ScrapedItem, ScrapingJob
    from sqlalchemy import func
    
    total_items = db.session.query(ScrapedItem).count()
    total_jobs = db.session.query(ScrapingJob).count()
    
    recent_items = db.session.query(ScrapedItem).filter(
        ScrapedItem.scraped_at > datetime.utcnow() - __import__('datetime').timedelta(days=1)
    ).count()
    
    return {
        "total_items": total_items,
        "total_jobs": total_jobs,
        "items_last_24h": recent_items
    }
```

## Horizontal Scaling

### Docker Compose for Local Development

```yaml
# docker-compose.yml
version: '3.8'

services:
  redis:
    image: redis:7-alpine
    ports:
      - "6379:6379"
    volumes:
      - redis_data:/data

  postgres:
    image: postgres:15
    environment:
      POSTGRES_USER: scraper
      POSTGRES_PASSWORD: scraper
      POSTGRES_DB: scraping
    ports:
      - "5432:5432"
    volumes:
      - postgres_data:/var/lib/postgresql/data

  scheduler:
    build: .
    command: python scheduler.py
    depends_on:
      - redis
      - postgres
    environment:
      - CELERY_BROKER_URL=redis://redis:6379/0
      - DATABASE_URL=postgresql://scraper:scraper@postgres/scraping
    volumes:
      - ./:/app

  worker:
    build: .
    command: celery -A celery_app worker --loglevel=info
    depends_on:
      - redis
      - postgres
    environment:
      - CELERY_BROKER_URL=redis://redis:6379/0
      - DATABASE_URL=postgresql://scraper:scraper@postgres/scraping
    deploy:
      replicas: 3
    volumes:
      - ./:/app

  beat:
    build: .
    command: celery -A celery_app beat --loglevel=info
    depends_on:
      - redis
    environment:
      - CELERY_BROKER_URL=redis://redis:6379/0

  api:
    build: .
    command: uvicorn api.main:app --host 0.0.0.0 --port 8000
    ports:
      - "8000:8000"
    depends_on:
      - postgres
    environment:
      - DATABASE_URL=postgresql://scraper:scraper@postgres/scraping
    volumes:
      - ./:/app

  prometheus:
    image: prom/prometheus
    ports:
      - "9090:9090"
    volumes:
      - ./monitoring/prometheus.yml:/etc/prometheus/prometheus.yml

volumes:
  redis_data:
  postgres_data:
```

### Kubernetes Deployment

```yaml
# k8s/worker-deployment.yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: scraper-worker
  labels:
    app: scraper-worker
spec:
  replicas: 5
  selector:
    matchLabels:
      app: scraper-worker
  template:
    metadata:
      labels:
        app: scraper-worker
    spec:
      containers:
      - name: worker
        image: scraper:latest
        command: ["celery", "-A", "celery_app", "worker", "--loglevel=info"]
        env:
        - name: CELERY_BROKER_URL
          valueFrom:
            secretKeyRef:
              name: scraper-secrets
              key: redis-url
        - name: DATABASE_URL
          valueFrom:
            secretKeyRef:
              name: scraper-secrets
              key: database-url
        resources:
          requests:
            memory: "512Mi"
            cpu: "250m"
          limits:
            memory: "1Gi"
            cpu: "500m"
        livenessProbe:
          exec:
            command:
            - celery
            - inspect
            - ping
          initialDelaySeconds: 30
          periodSeconds: 30
---
apiVersion: autoscaling/v2
kind: HorizontalPodAutoscaler
metadata:
  name: scraper-worker-hpa
spec:
  scaleTargetRef:
    apiVersion: apps/v1
    kind: Deployment
    name: scraper-worker
  minReplicas: 3
  maxReplicas: 20
  metrics:
  - type: Resource
    resource:
      name: cpu
      target:
        type: Utilization
        averageUtilization: 70
```

## Cost Tracking

### Cost Calculator

```python
# cost_tracking/calculator.py
from dataclasses import dataclass
from typing import Dict, List
from datetime import datetime, timedelta

@dataclass
class ResourceCost:
    resource_type: str  # compute, storage, bandwidth, proxy
    provider: str
    unit_cost: float
    unit: str  # per_hour, per_gb, per_request
    quantity: float

class CostCalculator:
    """Calculate total scraping costs"""
    
    def __init__(self):
        self.costs: List[ResourceCost] = []
    
    def add_compute_cost(self, instance_type: str, hours: float, provider: str = "aws"):
        """Add compute resource cost"""
        # Pricing per hour
        prices = {
            't3.medium': 0.0416,
            't3.large': 0.0832,
            'c5.large': 0.085,
            'c5.xlarge': 0.17
        }
        
        unit_cost = prices.get(instance_type, 0.05)
        
        self.costs.append(ResourceCost(
            resource_type='compute',
            provider=provider,
            unit_cost=unit_cost,
            unit='per_hour',
            quantity=hours
        ))
    
    def add_storage_cost(self, gb: float, provider: str = "aws"):
        """Add storage cost"""
        # $0.10 per GB-month for EBS
        unit_cost = 0.10
        
        self.costs.append(ResourceCost(
            resource_type='storage',
            provider=provider,
            unit_cost=unit_cost,
            unit='per_gb_month',
            quantity=gb
        ))
    
    def add_bandwidth_cost(self, gb: float, provider: str = "aws"):
        """Add bandwidth cost"""
        # First 1GB free, then $0.09 per GB
        if gb <= 1:
            return
        
        cost_gb = gb - 1
        unit_cost = 0.09
        
        self.costs.append(ResourceCost(
            resource_type='bandwidth',
            provider=provider,
            unit_cost=unit_cost,
            unit='per_gb',
            quantity=cost_gb
        ))
    
    def add_proxy_cost(self, gb: float, provider: str = "brightdata"):
        """Add proxy cost"""
        # Residential proxy pricing
        prices = {
            'brightdata': 10.0,
            'oxylabs': 8.0,
            'smartproxy': 12.5,
            'iproyal': 2.4
        }
        
        unit_cost = prices.get(provider, 10.0)
        
        self.costs.append(ResourceCost(
            resource_type='proxy',
            provider=provider,
            unit_cost=unit_cost,
            unit='per_gb',
            quantity=gb
        ))
    
    def calculate_total(self) -> Dict:
        """Calculate total costs"""
        total_by_type = {}
        grand_total = 0
        
        for cost in self.costs:
            amount = cost.unit_cost * cost.quantity
            grand_total += amount
            
            if cost.resource_type not in total_by_type:
                total_by_type[cost.resource_type] = 0
            total_by_type[cost.resource_type] += amount
        
        return {
            'grand_total': grand_total,
            'by_resource_type': total_by_type,
            'details': [
                {
                    'resource': c.resource_type,
                    'provider': c.provider,
                    'quantity': c.quantity,
                    'unit': c.unit,
                    'cost': c.unit_cost * c.quantity
                }
                for c in self.costs
            ]
        }

# Usage
calc = CostCalculator()

# Calculate monthly costs
calc.add_compute_cost('c5.large', 720 * 3)  # 3 instances running 24/7
calc.add_storage_cost(500)  # 500 GB storage
calc.add_bandwidth_cost(500)  # 500 GB transfer
calc.add_proxy_cost(100, provider='brightdata')  # 100 GB proxy traffic

total = calc.calculate_total()
print(f"Total monthly cost: ${total['grand_total']:.2f}")
print(f"By type: {total['by_resource_type']}")
```

## Summary

Production scraping architecture requires:

1. **Microservices Design**: Separate concerns into scheduler, workers, storage, and API
2. **Job Scheduling**: Use Celery for distributed tasks, APScheduler for simple needs, or cron for basics
3. **Failure Recovery**: Implement exponential backoff, circuit breakers, and dead letter queues
4. **Monitoring**: Track metrics with Prometheus, visualize with Grafana, alert on anomalies
5. **Database Design**: Proper schema design for scraped data with change tracking
6. **API Layer**: RESTful API for data consumers using FastAPI or similar
7. **Horizontal Scaling**: Deploy with Docker Compose locally, Kubernetes in production
8. **Cost Tracking**: Monitor and optimize infrastructure and proxy costs

A well-architected production system ensures reliability, scalability, and maintainability for long-term scraping operations.