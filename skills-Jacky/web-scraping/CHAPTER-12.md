# Chapter 12: Building Production Scraping Pipelines

## Table of Contents
1. [Introduction to Production Pipelines](#introduction)
2. [Architecture Design](#architecture-design)
3. [Data Quality and Validation](#data-quality)
4. [Error Handling and Recovery](#error-handling)
5. [Monitoring and Alerting](#monitoring)
6. [Scheduling and Orchestration](#scheduling)
7. [Data Storage Strategies](#storage)
8. [Complete Pipeline Examples](#examples)

---

## Introduction to Production Pipelines

Moving from a prototype scraper to a production pipeline requires careful consideration of reliability, maintainability, monitoring, and data quality. A production pipeline must handle failures gracefully, recover from crashes, alert operators to problems, and produce consistently high-quality data.

### What Makes a Pipeline "Production-Ready"

A production scraping pipeline differs from a quick script in several important ways:

1. **Reliability** - It runs unattended and recovers from failures automatically
2. **Observability** - You can see what it's doing and how it's performing at any time
3. **Data Quality** - Output data is validated, cleaned, and consistent
4. **Scalability** - It can handle increasing workloads without rewriting
5. **Maintainability** - Other developers can understand and modify it
6. **Security** - Credentials are managed properly, and the system doesn't leak data

### Pipeline Architecture Patterns

The most common architecture for production scraping is the ETL (Extract, Transform, Load) pattern:

```
[URL Source] -> [Fetcher] -> [Parser] -> [Validator] -> [Transformer] -> [Loader] -> [Storage]
     |              |            |            |               |              |
     v              v            v            v               v              v
  [Queue]       [Cache]     [Errors]     [Rejects]      [Enrichment]   [Backup]
```

Each component has a clear responsibility and can be tested independently.

---

## Architecture Design

### Component-Based Architecture

```python
from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from typing import List, Dict, Any, Optional, Generator
from datetime import datetime
import json
import logging
import hashlib

logger = logging.getLogger(__name__)


@dataclass
class ScrapedItem:
    """Base class for scraped data items"""
    url: str
    raw_data: Dict[str, Any]
    cleaned_data: Dict[str, Any] = field(default_factory=dict)
    metadata: Dict[str, Any] = field(default_factory=dict)
    errors: List[str] = field(default_factory=list)
    scraped_at: str = field(default_factory=lambda: datetime.now().isoformat())
    
    @property
    def fingerprint(self):
        """Generate unique fingerprint for deduplication"""
        content = json.dumps(self.raw_data, sort_keys=True)
        return hashlib.md5(content.encode()).hexdigest()
    
    @property
    def is_valid(self):
        return len(self.errors) == 0


class BaseFetcher(ABC):
    """Abstract base class for content fetchers"""
    
    @abstractmethod
    def fetch(self, url: str) -> Optional[str]:
        """Fetch content from URL"""
        pass
    
    @abstractmethod
    def fetch_batch(self, urls: List[str]) -> Dict[str, Optional[str]]:
        """Fetch multiple URLs"""
        pass


class BaseParser(ABC):
    """Abstract base class for content parsers"""
    
    @abstractmethod
    def parse(self, html: str, url: str) -> List[ScrapedItem]:
        """Parse HTML and extract items"""
        pass


class BaseValidator(ABC):
    """Abstract base class for data validators"""
    
    @abstractmethod
    def validate(self, item: ScrapedItem) -> ScrapedItem:
        """Validate item, adding errors if invalid"""
        pass


class BaseTransformer(ABC):
    """Abstract base class for data transformers"""
    
    @abstractmethod
    def transform(self, item: ScrapedItem) -> ScrapedItem:
        """Transform item data"""
        pass


class BaseLoader(ABC):
    """Abstract base class for data loaders"""
    
    @abstractmethod
    def load(self, items: List[ScrapedItem]) -> int:
        """Load items to storage, return count loaded"""
        pass


class ScrapingPipeline:
    """Orchestrate the complete scraping pipeline"""
    
    def __init__(self):
        self.fetcher: Optional[BaseFetcher] = None
        self.parser: Optional[BaseParser] = None
        self.validators: List[BaseValidator] = []
        self.transformers: List[BaseTransformer] = []
        self.loaders: List[BaseLoader] = []
        self.stats = PipelineStats()
    
    def set_fetcher(self, fetcher: BaseFetcher):
        self.fetcher = fetcher
        return self
    
    def set_parser(self, parser: BaseParser):
        self.parser = parser
        return self
    
    def add_validator(self, validator: BaseValidator):
        self.validators.append(validator)
        return self
    
    def add_transformer(self, transformer: BaseTransformer):
        self.transformers.append(transformer)
        return self
    
    def add_loader(self, loader: BaseLoader):
        self.loaders.append(loader)
        return self
    
    def run(self, urls: List[str]) -> PipelineStats:
        """Execute the complete pipeline"""
        logger.info(f"Starting pipeline with {len(urls)} URLs")
        self.stats.start()
        
        # Fetch
        for url in urls:
            try:
                html = self.fetcher.fetch(url)
                if not html:
                    self.stats.record_fetch_error(url)
                    continue
                
                self.stats.record_fetch_success(url)
                
                # Parse
                items = self.parser.parse(html, url)
                self.stats.record_parsed(len(items))
                
                # Validate
                valid_items = []
                for item in items:
                    for validator in self.validators:
                        item = validator.validate(item)
                    
                    if item.is_valid:
                        valid_items.append(item)
                    else:
                        self.stats.record_validation_error(item)
                
                # Transform
                transformed_items = []
                for item in valid_items:
                    for transformer in self.transformers:
                        item = transformer.transform(item)
                    transformed_items.append(item)
                
                # Load
                for loader in self.loaders:
                    count = loader.load(transformed_items)
                    self.stats.record_loaded(count)
                
            except Exception as e:
                logger.error(f"Pipeline error for {url}: {e}")
                self.stats.record_error(url, str(e))
        
        self.stats.finish()
        return self.stats


@dataclass
class PipelineStats:
    """Track pipeline execution statistics"""
    start_time: Optional[datetime] = None
    end_time: Optional[datetime] = None
    urls_processed: int = 0
    fetch_successes: int = 0
    fetch_errors: int = 0
    items_parsed: int = 0
    items_validated: int = 0
    validation_errors: int = 0
    items_loaded: int = 0
    errors: List[Dict] = field(default_factory=list)
    
    def start(self):
        self.start_time = datetime.now()
    
    def finish(self):
        self.end_time = datetime.now()
    
    def record_fetch_success(self, url):
        self.urls_processed += 1
        self.fetch_successes += 1
    
    def record_fetch_error(self, url):
        self.urls_processed += 1
        self.fetch_errors += 1
    
    def record_parsed(self, count):
        self.items_parsed += count
    
    def record_validation_error(self, item):
        self.validation_errors += 1
    
    def record_loaded(self, count):
        self.items_loaded += count
    
    def record_error(self, url, error):
        self.errors.append({'url': url, 'error': error})
    
    @property
    def duration(self):
        if self.start_time and self.end_time:
            return (self.end_time - self.start_time).total_seconds()
        return 0
    
    def summary(self):
        return {
            'duration_seconds': self.duration,
            'urls_processed': self.urls_processed,
            'fetch_success_rate': self.fetch_successes / max(1, self.urls_processed),
            'items_parsed': self.items_parsed,
            'items_loaded': self.items_loaded,
            'validation_errors': self.validation_errors,
            'total_errors': len(self.errors),
        }
```

### Implementing Pipeline Components

```python
import requests
from bs4 import BeautifulSoup
import time
import random


class RequestsFetcher(BaseFetcher):
    """Fetcher using requests library"""
    
    def __init__(self, delay_range=(1, 3), max_retries=3):
        self.session = requests.Session()
        self.session.headers.update({
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            'Accept-Language': 'en-US,en;q=0.5',
        })
        self.delay_range = delay_range
        self.max_retries = max_retries
    
    def fetch(self, url: str) -> Optional[str]:
        for attempt in range(self.max_retries):
            try:
                time.sleep(random.uniform(*self.delay_range))
                response = self.session.get(url, timeout=30)
                response.raise_for_status()
                
                if response.encoding == 'ISO-8859-1':
                    response.encoding = response.apparent_encoding
                
                return response.text
                
            except requests.RequestException as e:
                logger.warning(f"Fetch attempt {attempt + 1} failed for {url}: {e}")
                if attempt == self.max_retries - 1:
                    return None
                time.sleep(2 ** attempt)
        
        return None
    
    def fetch_batch(self, urls: List[str]) -> Dict[str, Optional[str]]:
        results = {}
        for url in urls:
            results[url] = self.fetch(url)
        return results


class ProductParser(BaseParser):
    """Parser for e-commerce product pages"""
    
    def parse(self, html: str, url: str) -> List[ScrapedItem]:
        soup = BeautifulSoup(html, 'lxml')
        items = []
        
        for product in soup.select('.product-card, .product-item'):
            raw_data = {
                'name': self._safe_text(product, 'h2, h3, .product-name'),
                'price': self._safe_text(product, '.price, .product-price'),
                'image': self._safe_attr(product, 'img', 'src'),
                'link': self._safe_attr(product, 'a', 'href'),
                'rating': self._safe_text(product, '.rating, .stars'),
                'review_count': self._safe_text(product, '.review-count'),
            }
            
            item = ScrapedItem(url=url, raw_data=raw_data)
            items.append(item)
        
        return items
    
    def _safe_text(self, parent, selector, default=None):
        element = parent.select_one(selector)
        return element.get_text(strip=True) if element else default
    
    def _safe_attr(self, parent, selector, attr, default=None):
        element = parent.select_one(selector)
        return element.get(attr) if element else default


class RequiredFieldsValidator(BaseValidator):
    """Validate that required fields are present"""
    
    def __init__(self, required_fields):
        self.required_fields = required_fields
    
    def validate(self, item: ScrapedItem) -> ScrapedItem:
        for field in self.required_fields:
            if not item.raw_data.get(field):
                item.errors.append(f"Missing required field: {field}")
        return item


class PriceValidator(BaseValidator):
    """Validate price data"""
    
    def __init__(self, min_price=0.01, max_price=1000000):
        self.min_price = min_price
        self.max_price = max_price
    
    def validate(self, item: ScrapedItem) -> ScrapedItem:
        price = item.raw_data.get('price')
        if price:
            import re
            numbers = re.findall(r'[\d,.]+', str(price))
            if numbers:
                try:
                    price_float = float(numbers[0].replace(',', ''))
                    if price_float < self.min_price or price_float > self.max_price:
                        item.errors.append(f"Price out of range: {price_float}")
                except ValueError:
                    item.errors.append(f"Invalid price format: {price}")
        return item


class DataCleaningTransformer(BaseTransformer):
    """Clean and normalize data"""
    
    def transform(self, item: ScrapedItem) -> ScrapedItem:
        import re
        
        cleaned = {}
        
        # Clean name
        name = item.raw_data.get('name', '')
        cleaned['name'] = ' '.join(name.split()).strip()
        
        # Clean price
        price = item.raw_data.get('price', '')
        numbers = re.findall(r'[\d,.]+', str(price))
        cleaned['price'] = float(numbers[0].replace(',', '')) if numbers else None
        
        # Clean URL
        link = item.raw_data.get('link', '')
        if link and not link.startswith('http'):
            from urllib.parse import urljoin
            cleaned['url'] = urljoin(item.url, link)
        else:
            cleaned['url'] = link
        
        # Copy other fields
        cleaned['image'] = item.raw_data.get('image')
        cleaned['rating'] = item.raw_data.get('rating')
        cleaned['review_count'] = item.raw_data.get('review_count')
        cleaned['source_url'] = item.url
        
        item.cleaned_data = cleaned
        return item


class JSONFileLoader(BaseLoader):
    """Load items to JSON file"""
    
    def __init__(self, filepath):
        self.filepath = filepath
        self.existing_data = self._load_existing()
    
    def _load_existing(self):
        try:
            with open(self.filepath, 'r') as f:
                return json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            return []
    
    def load(self, items: List[ScrapedItem]) -> int:
        new_data = [item.cleaned_data for item in items if item.cleaned_data]
        self.existing_data.extend(new_data)
        
        with open(self.filepath, 'w', encoding='utf-8') as f:
            json.dump(self.existing_data, f, indent=2, ensure_ascii=False)
        
        return len(new_data)


class SQLiteLoader(BaseLoader):
    """Load items to SQLite database"""
    
    def __init__(self, db_path, table_name='products'):
        import sqlite3
        self.conn = sqlite3.connect(db_path)
        self.table_name = table_name
        self._create_table()
    
    def _create_table(self):
        self.conn.execute(f'''
            CREATE TABLE IF NOT EXISTS {self.table_name} (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT,
                price REAL,
                url TEXT UNIQUE,
                image TEXT,
                rating TEXT,
                review_count TEXT,
                source_url TEXT,
                scraped_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        ''')
        self.conn.commit()
    
    def load(self, items: List[ScrapedItem]) -> int:
        loaded = 0
        for item in items:
            data = item.cleaned_data
            if not data:
                continue
            
            try:
                self.conn.execute(f'''
                    INSERT OR REPLACE INTO {self.table_name} 
                    (name, price, url, image, rating, review_count, source_url)
                    VALUES (?, ?, ?, ?, ?, ?, ?)
                ''', (
                    data.get('name'),
                    data.get('price'),
                    data.get('url'),
                    data.get('image'),
                    data.get('rating'),
                    data.get('review_count'),
                    data.get('source_url'),
                ))
                loaded += 1
            except Exception as e:
                logger.error(f"Failed to load item: {e}")
        
        self.conn.commit()
        return loaded
    
    def close(self):
        self.conn.close()
```

### Running the Complete Pipeline

```python
def main():
    """Example: Run complete scraping pipeline"""
    
    # Build pipeline
    pipeline = ScrapingPipeline()
    pipeline.set_fetcher(RequestsFetcher(delay_range=(1, 3)))
    pipeline.set_parser(ProductParser())
    pipeline.add_validator(RequiredFieldsValidator(['name', 'price']))
    pipeline.add_validator(PriceValidator(min_price=0.01))
    pipeline.add_transformer(DataCleaningTransformer())
    pipeline.add_loader(JSONFileLoader('output/products.json'))
    pipeline.add_loader(SQLiteLoader('output/products.db'))
    
    # Define URLs to scrape
    urls = [
        'https://example-shop.com/category/electronics?page=1',
        'https://example-shop.com/category/electronics?page=2',
        'https://example-shop.com/category/electronics?page=3',
    ]
    
    # Run
    stats = pipeline.run(urls)
    
    # Report
    print(json.dumps(stats.summary(), indent=2))


# main()
```

---

## Data Quality and Validation

### Multi-Level Validation

```python
class SchemaValidator(BaseValidator):
    """Validate items against a schema definition"""
    
    def __init__(self, schema):
        self.schema = schema
    
    def validate(self, item: ScrapedItem) -> ScrapedItem:
        for field_name, rules in self.schema.items():
            value = item.raw_data.get(field_name)
            
            # Required check
            if rules.get('required') and not value:
                item.errors.append(f"Required field '{field_name}' is missing")
                continue
            
            if value is None:
                continue
            
            # Type check
            expected_type = rules.get('type')
            if expected_type and not isinstance(value, expected_type):
                item.errors.append(f"Field '{field_name}' expected {expected_type}, got {type(value)}")
            
            # Min/max length
            min_len = rules.get('min_length')
            if min_len and len(str(value)) < min_len:
                item.errors.append(f"Field '{field_name}' too short (min {min_len})")
            
            max_len = rules.get('max_length')
            if max_len and len(str(value)) > max_len:
                item.errors.append(f"Field '{field_name}' too long (max {max_len})")
            
            # Pattern match
            pattern = rules.get('pattern')
            if pattern:
                import re
                if not re.match(pattern, str(value)):
                    item.errors.append(f"Field '{field_name}' doesn't match pattern")
        
        return item


# Usage
product_schema = {
    'name': {'required': True, 'type': str, 'min_length': 2, 'max_length': 500},
    'price': {'required': True, 'type': str, 'pattern': r'.*\d+.*'},
    'image': {'required': False, 'type': str, 'pattern': r'^https?://.*'},
}

validator = SchemaValidator(product_schema)
```

### Deduplication Pipeline

```python
class DeduplicationPipeline:
    """Remove duplicate items based on configurable keys"""
    
    def __init__(self, dedup_fields=None, strategy='keep_first'):
        self.dedup_fields = dedup_fields or ['url']
        self.strategy = strategy
        self.seen = {}
    
    def process(self, items: List[ScrapedItem]) -> List[ScrapedItem]:
        unique_items = []
        
        for item in items:
            key = self._generate_key(item)
            
            if key not in self.seen:
                self.seen[key] = item
                unique_items.append(item)
            elif self.strategy == 'keep_latest':
                # Replace with newer item
                self.seen[key] = item
                unique_items = [i for i in unique_items if self._generate_key(i) != key]
                unique_items.append(item)
        
        return unique_items
    
    def _generate_key(self, item):
        values = []
        for field in self.dedup_fields:
            value = item.raw_data.get(field) or item.cleaned_data.get(field, '')
            values.append(str(value))
        
        key_str = '|'.join(values)
        return hashlib.md5(key_str.encode()).hexdigest()
```

---

## Error Handling and Recovery

### Checkpoint and Resume

```python
class CheckpointManager:
    """Save and restore pipeline progress for crash recovery"""
    
    def __init__(self, checkpoint_file='checkpoint.json'):
        self.checkpoint_file = checkpoint_file
        self.state = self._load()
    
    def _load(self):
        try:
            with open(self.checkpoint_file, 'r') as f:
                return json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            return {
                'completed_urls': [],
                'failed_urls': [],
                'last_url': None,
                'items_scraped': 0,
                'last_save': None,
            }
    
    def save(self):
        self.state['last_save'] = datetime.now().isoformat()
        with open(self.checkpoint_file, 'w') as f:
            json.dump(self.state, f, indent=2)
    
    def mark_completed(self, url):
        self.state['completed_urls'].append(url)
        self.state['last_url'] = url
        self.state['items_scraped'] += 1
        
        # Auto-save every 10 URLs
        if len(self.state['completed_urls']) % 10 == 0:
            self.save()
    
    def mark_failed(self, url, error):
        self.state['failed_urls'].append({
            'url': url,
            'error': error,
            'timestamp': datetime.now().isoformat(),
        })
    
    def get_remaining_urls(self, all_urls):
        completed = set(self.state['completed_urls'])
        return [url for url in all_urls if url not in completed]
    
    def reset(self):
        self.state = {
            'completed_urls': [],
            'failed_urls': [],
            'last_url': None,
            'items_scraped': 0,
            'last_save': None,
        }
        self.save()
```

---

## Monitoring and Alerting

### Pipeline Monitor

```python
class PipelineMonitor:
    """Monitor pipeline health and performance"""
    
    def __init__(self):
        self.metrics = {
            'requests_total': 0,
            'requests_success': 0,
            'requests_failed': 0,
            'items_scraped': 0,
            'items_validated': 0,
            'items_rejected': 0,
            'items_loaded': 0,
            'errors': [],
            'response_times': [],
        }
        self.alerts = []
    
    def record_request(self, url, status, response_time):
        self.metrics['requests_total'] += 1
        
        if 200 <= status < 400:
            self.metrics['requests_success'] += 1
        else:
            self.metrics['requests_failed'] += 1
        
        self.metrics['response_times'].append(response_time)
        
        # Alert on high failure rate
        total = self.metrics['requests_total']
        if total > 10:
            fail_rate = self.metrics['requests_failed'] / total
            if fail_rate > 0.3:
                self.alert('HIGH_FAILURE_RATE', f"Failure rate: {fail_rate:.1%}")
    
    def record_item(self, item, stage):
        self.metrics[f'items_{stage}'] += 1
    
    def record_error(self, error_type, message):
        self.metrics['errors'].append({
            'type': error_type,
            'message': message,
            'timestamp': datetime.now().isoformat(),
        })
    
    def alert(self, alert_type, message):
        alert = {
            'type': alert_type,
            'message': message,
            'timestamp': datetime.now().isoformat(),
        }
        self.alerts.append(alert)
        logger.warning(f"ALERT [{alert_type}]: {message}")
    
    def get_dashboard(self):
        """Get current metrics dashboard"""
        response_times = self.metrics['response_times']
        
        return {
            'requests': {
                'total': self.metrics['requests_total'],
                'success': self.metrics['requests_success'],
                'failed': self.metrics['requests_failed'],
                'success_rate': self.metrics['requests_success'] / max(1, self.metrics['requests_total']),
            },
            'items': {
                'scraped': self.metrics['items_scraped'],
                'validated': self.metrics['items_validated'],
                'rejected': self.metrics['items_rejected'],
                'loaded': self.metrics['items_loaded'],
            },
            'performance': {
                'avg_response_time': sum(response_times) / max(1, len(response_times)),
                'min_response_time': min(response_times) if response_times else 0,
                'max_response_time': max(response_times) if response_times else 0,
            },
            'errors': len(self.metrics['errors']),
            'alerts': len(self.alerts),
        }
```

---

## Scheduling and Orchestration

### Cron-Based Scheduling

```python
import schedule
import time
from datetime import datetime


class ScrapingScheduler:
    """Schedule and orchestrate scraping jobs"""
    
    def __init__(self):
        self.jobs = {}
    
    def add_daily_job(self, name, pipeline_func, hour=6, minute=0):
        """Run job daily at specified time"""
        schedule.every().day.at(f"{hour:02d}:{minute:02d}").do(
            self._run_job, name, pipeline_func
        )
        self.jobs[name] = {
            'schedule': f'Daily at {hour:02d}:{minute:02d}',
            'last_run': None,
            'status': 'scheduled',
        }
    
    def add_interval_job(self, name, pipeline_func, hours=1):
        """Run job every N hours"""
        schedule.every(hours).hours.do(
            self._run_job, name, pipeline_func
        )
        self.jobs[name] = {
            'schedule': f'Every {hours} hours',
            'last_run': None,
            'status': 'scheduled',
        }
    
    def _run_job(self, name, pipeline_func):
        """Execute a scraping job"""
        logger.info(f"Starting job: {name}")
        self.jobs[name]['status'] = 'running'
        self.jobs[name]['last_run'] = datetime.now().isoformat()
        
        try:
            result = pipeline_func()
            self.jobs[name]['status'] = 'completed'
            self.jobs[name]['last_result'] = str(result)
            logger.info(f"Job completed: {name}")
        except Exception as e:
            self.jobs[name]['status'] = 'failed'
            self.jobs[name]['last_error'] = str(e)
            logger.error(f"Job failed: {name} - {e}")
    
    def run(self):
        """Start the scheduler loop"""
        logger.info("Scheduler started")
        while True:
            schedule.run_pending()
            time.sleep(60)
```

---

## Data Storage Strategies

### Multi-Backend Storage

```python
class StorageManager:
    """Manage multiple storage backends"""
    
    def __init__(self):
        self.backends = {}
    
    def add_backend(self, name, backend):
        self.backends[name] = backend
    
    def store(self, items, backends=None):
        """Store items to specified backends (or all)"""
        target_backends = backends or list(self.backends.keys())
        results = {}
        
        for name in target_backends:
            if name in self.backends:
                try:
                    count = self.backends[name].store(items)
                    results[name] = {'success': True, 'count': count}
                except Exception as e:
                    results[name] = {'success': False, 'error': str(e)}
        
        return results


class CSVBackend:
    """CSV file storage backend"""
    
    def __init__(self, filepath, fieldnames=None):
        self.filepath = filepath
        self.fieldnames = fieldnames
        self._initialized = False
    
    def store(self, items):
        import csv
        
        if not items:
            return 0
        
        data = [item.cleaned_data for item in items if item.cleaned_data]
        if not data:
            return 0
        
        fieldnames = self.fieldnames or list(data[0].keys())
        
        mode = 'a' if self._initialized else 'w'
        with open(self.filepath, mode, newline='', encoding='utf-8') as f:
            writer = csv.DictWriter(f, fieldnames=fieldnames, extrasaction='ignore')
            if not self._initialized:
                writer.writeheader()
                self._initialized = True
            writer.writerows(data)
        
        return len(data)


class ElasticsearchBackend:
    """Elasticsearch storage backend"""
    
    def __init__(self, hosts, index_name):
        from elasticsearch import Elasticsearch, helpers
        self.es = Elasticsearch(hosts)
        self.index_name = index_name
        self.helpers = helpers
    
    def store(self, items):
        actions = []
        for item in items:
            if item.cleaned_data:
                actions.append({
                    '_index': self.index_name,
                    '_source': {
                        **item.cleaned_data,
                        'scraped_at': item.scraped_at,
                    },
                })
        
        if actions:
            success, errors = self.helpers.bulk(self.es, actions)
            return success
        return 0
```

This chapter provides a complete framework for building production-grade scraping pipelines. The component-based architecture makes it easy to test individual pieces, swap implementations, and scale the system as requirements grow. Combined with proper monitoring, error handling, and scheduling, these patterns enable reliable, unattended scraping operations.
