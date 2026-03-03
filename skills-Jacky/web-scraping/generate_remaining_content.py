#!/usr/bin/env python3
"""
Generate remaining comprehensive content for web scraping skill guide.
This will create content for all remaining sections to reach 100,000+ words.
"""

import sys

# Define comprehensive content structure for each remaining section
# Each section will be extremely detailed

remaining_content = """

---

## Scraping Automation and Scheduling

### Introduction to Scraping Automation

Automation transforms one-time scraping scripts into reliable, recurring data collection systems. Automated scrapers run on schedules, handle errors gracefully, and alert you to issues without manual intervention.

**Benefits of Automation**:
- **Consistency**: Regular data collection at defined intervals
- **Efficiency**: No manual intervention required
- **Scalability**: Handle multiple scraping tasks simultaneously  
- **Reliability**: Automatic retry and error handling
- **Timeliness**: Collect data when it's most relevant

**Automation Challenges**:
- **Site Changes**: Websites update structure, breaking scrapers
- **Rate Limiting**: Automated scrapers may trigger anti-bot measures more easily
- **Resource Management**: Long-running scrapers need proper resource cleanup
- **Error Handling**: Must handle all edge cases autonomously
- **Monitoring**: Need systems to detect and alert on failures

### Cron Jobs for Scheduling

Cron is Unix/Linux's built-in job scheduler, ideal for running scrapers on regular schedules.

**Cron Syntax**:
```
* * * * * command
│ │ │ │ │
│ │ │ │ └─── Day of week (0-7, Sunday=0 or 7)
│ │ │ └───── Month (1-12)
│ │ └─────── Day of month (1-31)
│ └───────── Hour (0-23)
└─────────── Minute (0-59)
```

**Common Cron Patterns**:

```bash
# Every minute
* * * * * /path/to/scraper.py

# Every 5 minutes
*/5 * * * * /path/to/scraper.py

# Every hour at minute 30
30 * * * * /path/to/scraper.py

# Daily at 2 AM
0 2 * * * /path/to/scraper.py

# Every Monday at 9 AM
0 9 * * 1 /path/to/scraper.py

# First day of every month at midnight
0 0 1 * * /path/to/scraper.py

# Every weekday at 6 PM
0 18 * * 1-5 /path/to/scraper.py

# Multiple times per day
0 6,12,18 * * * /path/to/scraper.py
```

**Setting Up Cron Jobs**:

```bash
# Edit crontab
crontab -e

# Add job with output redirection
0 2 * * * cd /path/to/project && python3 scraper.py >> /var/log/scraper.log 2>&1

# View existing cron jobs
crontab -l

# Remove all cron jobs
crontab -r
```

**Python Wrapper for Cron**:

```python
#!/usr/bin/env python3
# scraper_cron.py

import sys
import logging
from datetime import datetime
import traceback

# Setup logging
logging.basicConfig(
    filename='/var/log/scraper.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def main():
    try:
        logging.info('Starting scraper job')
        
        # Import and run your scraper
        from my_scraper import scrape_products
        
        results = scrape_products()
        
        logging.info(f'Scraper completed successfully. Collected {len(results)} items')
        
    except Exception as e:
        logging.error(f'Scraper failed: {str(e)}')
        logging.error(traceback.format_exc())
        sys.exit(1)

if __name__ == '__main__':
    main()
```

### Python Schedule Library

The `schedule` library provides a more Pythonic way to schedule tasks.

**Installation**:
```bash
pip install schedule
```

**Basic Usage**:

```python
import schedule
import time

def job():
    print("Running scraper...")
    # Your scraping code here

# Schedule jobs
schedule.every(10).minutes.do(job)
schedule.every().hour.do(job)
schedule.every().day.at("10:30").do(job)
schedule.every().monday.do(job)
schedule.every().wednesday.at("13:15").do(job)

# Run schedule loop
while True:
    schedule.run_pending()
    time.sleep(1)
```

**Advanced Scheduling**:

```python
import schedule
import time
from datetime import datetime
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class ScheduledScraper:
    def __init__(self):
        self.last_run = None
        self.run_count = 0
    
    def scrape_products(self):
        try:
            logger.info(f'Starting scrape #{self.run_count + 1}')
            
            # Your scraping logic
            results = []  # scraping results
            
            self.last_run = datetime.now()
            self.run_count += 1
            
            logger.info(f'Completed scrape. Total runs: {self.run_count}')
            
            return results
        
        except Exception as e:
            logger.error(f'Scrape failed: {e}')
            # Send alert
            self.send_alert(str(e))
    
    def scrape_prices(self):
        logger.info('Scraping prices...')
        # Price scraping logic
    
    def generate_report(self):
        logger.info('Generating daily report...')
        # Report generation logic
    
    def send_alert(self, message):
        # Send email/SMS alert
        pass

# Setup
scraper = ScheduledScraper()

# Schedule different tasks
schedule.every(30).minutes.do(scraper.scrape_prices)
schedule.every(2).hours.do(scraper.scrape_products)
schedule.every().day.at("08:00").do(scraper.generate_report)

# Run with error handling
while True:
    try:
        schedule.run_pending()
        time.sleep(60)  # Check every minute
    except KeyboardInterrupt:
        logger.info('Scheduler stopped by user')
        break
    except Exception as e:
        logger.error(f'Scheduler error: {e}')
        time.sleep(60)  # Wait before retrying
```

### Celery for Distributed Task Queue

Celery is a powerful distributed task queue for handling complex scraping workflows.

**Installation**:
```bash
pip install celery redis
```

**Basic Setup**:

```python
# celery_app.py

from celery import Celery

# Configure Celery
app = Celery('scraper', 
             broker='redis://localhost:6379/0',
             backend='redis://localhost:6379/0')

app.conf.update(
    task_serializer='json',
    accept_content=['json'],
    result_serializer='json',
    timezone='UTC',
    enable_utc=True,
)

@app.task
def scrape_product(product_url):
    # Scraping logic
    import requests
    from bs4 import BeautifulSoup
    
    response = requests.get(product_url)
    soup = BeautifulSoup(response.content, 'lxml')
    
    # Extract data
    product = {
        'name': soup.find('h1').get_text(strip=True),
        'price': soup.find('span', class_='price').get_text(strip=True)
    }
    
    return product

@app.task
def scrape_category(category_url):
    # Get all product URLs from category
    product_urls = get_product_urls(category_url)
    
    # Queue individual product scraping tasks
    for url in product_urls:
        scrape_product.delay(url)

def get_product_urls(category_url):
    # Extract product URLs logic
    return []
```

**Running Workers**:

```bash
# Start Celery worker
celery -A celery_app worker --loglevel=info

# Start multiple workers
celery -A celery_app worker --loglevel=info --concurrency=10

# Start worker with specific queue
celery -A celery_app worker -Q high_priority,low_priority
```

**Using Celery Beat for Periodic Tasks**:

```python
# celery_app.py (continued)

from celery.schedules import crontab

app.conf.beat_schedule = {
    'scrape-prices-every-30-minutes': {
        'task': 'celery_app.scrape_prices',
        'schedule': 30.0 * 60,  # 30 minutes in seconds
    },
    'scrape-products-daily': {
        'task': 'celery_app.scrape_all_products',
        'schedule': crontab(hour=2, minute=0),  # 2 AM daily
    },
    'generate-report-weekly': {
        'task': 'celery_app.generate_weekly_report',
        'schedule': crontab(hour=8, minute=0, day_of_week=1),  # Monday 8 AM
    },
}

@app.task
def scrape_prices():
    # Price scraping logic
    pass

@app.task
def scrape_all_products():
    # Full product scraping logic
    pass

@app.task
def generate_weekly_report():
    # Report generation logic
    pass
```

**Start Celery Beat**:

```bash
# Start beat scheduler
celery -A celery_app beat --loglevel=info
```

**Task Chains and Workflows**:

```python
from celery import chain, group, chord

# Chain: Execute tasks sequentially
workflow = chain(
    scrape_category.s('https://example.com/category'),
    process_results.s(),
    save_to_database.s()
)
workflow.apply_async()

# Group: Execute tasks in parallel
jobs = group(
    scrape_product.s(url) for url in product_urls
)
result = jobs.apply_async()

# Chord: Execute tasks in parallel, then callback
callback = chord(
    (scrape_product.s(url) for url in product_urls),
    aggregate_results.s()
)
callback.apply_async()
```

### APScheduler (Advanced Python Scheduler)

APScheduler is more flexible than the schedule library, supporting multiple execution backends.

**Installation**:
```bash
pip install apscheduler
```

**Basic Usage**:

```python
from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.triggers.cron import CronTrigger
import time

def scrape_job():
    print("Scraping...")
    # Your scraping logic

# Create scheduler
scheduler = BackgroundScheduler()

# Add jobs with different triggers
# Interval trigger
scheduler.add_job(scrape_job, 'interval', minutes=30, id='scrape_interval')

# Cron trigger
scheduler.add_job(
    scrape_job, 
    CronTrigger(hour=2, minute=0),
    id='scrape_daily'
)

# Date trigger (run once at specific time)
from datetime import datetime, timedelta
run_date = datetime.now() + timedelta(hours=1)
scheduler.add_job(scrape_job, 'date', run_date=run_date)

# Start scheduler
scheduler.start()

try:
    # Keep script running
    while True:
        time.sleep(1)
except (KeyboardInterrupt, SystemExit):
    scheduler.shutdown()
```

**Advanced APScheduler Features**:

```python
from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.jobstores.sqlalchemy import SQLAlchemyJobStore
from apscheduler.executors.pool import ThreadPoolExecutor, ProcessPoolExecutor
import logging

# Configure logging
logging.basicConfig()
logging.getLogger('apscheduler').setLevel(logging.DEBUG)

# Job stores (persist jobs across restarts)
jobstores = {
    'default': SQLAlchemyJobStore(url='sqlite:///jobs.sqlite')
}

# Executors
executors = {
    'default': ThreadPoolExecutor(20),
    'processpool': ProcessPoolExecutor(5)
}

# Job defaults
job_defaults = {
    'coalesce': False,  # Run all missed executions
    'max_instances': 3  # Max concurrent instances per job
}

# Create scheduler
scheduler = BackgroundScheduler(
    jobstores=jobstores,
    executors=executors,
    job_defaults=job_defaults
)

# Add job with advanced options
scheduler.add_job(
    scrape_job,
    'cron',
    hour=2,
    minute=0,
    id='scrape_daily',
    replace_existing=True,
    misfire_grace_time=3600  # Allow 1 hour late execution
)

scheduler.start()
```

### Docker for Scraper Deployment

Docker ensures your scraper runs consistently across environments.

**Dockerfile**:

```dockerfile
FROM python:3.9-slim

WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Install Chrome for Selenium/Playwright
RUN apt-get update && apt-get install -y \\
    wget \\
    gnupg \\
    && wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add - \\
    && echo "deb http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google.list \\
    && apt-get update \\
    && apt-get install -y google-chrome-stable \\
    && rm -rf /var/lib/apt/lists/*

# Copy application
COPY . .

# Run scraper
CMD ["python", "scraper.py"]
```

**docker-compose.yml**:

```yaml
version: '3.8'

services:
  scraper:
    build: .
    volumes:
      - ./data:/app/data
      - ./logs:/app/logs
    environment:
      - PYTHONUNBUFFERED=1
    restart: unless-stopped
  
  redis:
    image: redis:alpine
    ports:
      - "6379:6379"
  
  celery_worker:
    build: .
    command: celery -A celery_app worker --loglevel=info
    depends_on:
      - redis
    volumes:
      - ./data:/app/data
  
  celery_beat:
    build: .
    command: celery -A celery_app beat --loglevel=info
    depends_on:
      - redis
      - celery_worker
```

**Running with Docker**:

```bash
# Build and run
docker-compose up -d

# View logs
docker-compose logs -f scraper

# Stop
docker-compose down

# Rebuild after changes
docker-compose up -d --build
```

### Cloud Deployment

**AWS Lambda for Serverless Scraping**:

```python
# lambda_function.py

import json
import requests
from bs4 import BeautifulSoup

def lambda_handler(event, context):
    url = event.get('url', 'https://example.com')
    
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'lxml')
        
        # Extract data
        data = {
            'title': soup.find('h1').get_text(strip=True),
            'price': soup.find('span', class_='price').get_text(strip=True)
        }
        
        return {
            'statusCode': 200,
            'body': json.dumps(data)
        }
    
    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps({'error': str(e)})
        }
```

**AWS EventBridge for Scheduling**:

```bash
# Create EventBridge rule to trigger Lambda every hour
aws events put-rule \\
    --name scraper-hourly \\
    --schedule-expression "rate(1 hour)"

# Add Lambda as target
aws events put-targets \\
    --rule scraper-hourly \\
    --targets "Id"="1","Arn"="arn:aws:lambda:REGION:ACCOUNT:function:scraper"
```

**Google Cloud Functions**:

```python
# main.py

import requests
from bs4 import BeautifulSoup

def scraper(request):
    url = request.args.get('url', 'https://example.com')
    
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'lxml')
    
    data = {
        'title': soup.find('h1').get_text(strip=True)
    }
    
    return data
```

**Google Cloud Scheduler**:

```bash
# Create scheduled job
gcloud scheduler jobs create http scraper-job \\
    --schedule="0 */2 * * *" \\
    --uri="https://REGION-PROJECT.cloudfunctions.net/scraper" \\
    --http-method=GET
```

---

## Monitoring and Maintenance

### Why Monitoring Matters

Scrapers break. Websites change structure, add anti-bot measures, or go offline. Without monitoring, you won't know until you need the data and it's missing.

**What to Monitor**:
- **Execution Success/Failure**: Did the scraper run?
- **Data Quality**: Is extracted data valid and complete?
- **Performance**: How long does scraping take?
- **Error Rates**: What types of errors occur?
- **Data Freshness**: When was data last updated?
- **Resource Usage**: CPU, memory, bandwidth consumption

### Logging Best Practices

Comprehensive logging is the foundation of scraper monitoring.

**Python Logging Setup**:

```python
import logging
from logging.handlers import RotatingFileHandler, TimedRotatingFileHandler
import sys

def setup_logging(log_file='scraper.log', level=logging.INFO):
    # Create logger
    logger = logging.getLogger('scraper')
    logger.setLevel(level)
    
    # Console handler
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setLevel(logging.INFO)
    console_format = logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S'
    )
    console_handler.setFormatter(console_format)
    
    # File handler with rotation
    file_handler = RotatingFileHandler(
        log_file,
        maxBytes=10*1024*1024,  # 10MB
        backupCount=5
    )
    file_handler.setLevel(logging.DEBUG)
    file_format = logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(funcName)s:%(lineno)d - %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S'
    )
    file_handler.setFormatter(file_format)
    
    # Add handlers
    logger.addHandler(console_handler)
    logger.addHandler(file_handler)
    
    return logger

# Usage
logger = setup_logging()

logger.info('Scraper started')
logger.debug('Processing URL: https://example.com')
logger.warning('Slow response time: 5.2s')
logger.error('Failed to extract price')
logger.critical('Database connection lost')
```

**Structured Logging with JSON**:

```python
import json
import logging
from datetime import datetime

class JSONFormatter(logging.Formatter):
    def format(self, record):
        log_data = {
            'timestamp': datetime.utcnow().isoformat(),
            'level': record.levelname,
            'logger': record.name,
            'message': record.getMessage(),
            'module': record.module,
            'function': record.funcName,
            'line': record.lineno
        }
        
        # Add exception info if present
        if record.exc_info:
            log_data['exception'] = self.formatException(record.exc_info)
        
        # Add custom fields
        if hasattr(record, 'url'):
            log_data['url'] = record.url
        if hasattr(record, 'duration'):
            log_data['duration'] = record.duration
        
        return json.dumps(log_data)

# Setup
handler = logging.FileHandler('scraper.json.log')
handler.setFormatter(JSONFormatter())

logger = logging.getLogger('scraper')
logger.addHandler(handler)

# Usage with custom fields
extra = {'url': 'https://example.com', 'duration': 1.5}
logger.info('Page scraped successfully', extra=extra)
```

### Performance Metrics

Track scraper performance over time to identify degradation.

**Metrics Collection**:

```python
import time
import statistics
from collections import defaultdict
from datetime import datetime

class ScraperMetrics:
    def __init__(self):
        self.metrics = defaultdict(list)
        self.start_time = None
    
    def start_timer(self):
        self.start_time = time.time()
    
    def end_timer(self, metric_name):
        if self.start_time:
            duration = time.time() - self.start_time
            self.metrics[metric_name].append(duration)
            self.start_time = None
            return duration
    
    def record(self, metric_name, value):
        self.metrics[metric_name].append(value)
    
    def get_stats(self, metric_name):
        values = self.metrics[metric_name]
        if not values:
            return None
        
        return {
            'count': len(values),
            'mean': statistics.mean(values),
            'median': statistics.median(values),
            'min': min(values),
            'max': max(values),
            'stdev': statistics.stdev(values) if len(values) > 1 else 0
        }
    
    def report(self):
        report = {
            'timestamp': datetime.now().isoformat(),
            'metrics': {}
        }
        
        for metric_name in self.metrics:
            report['metrics'][metric_name] = self.get_stats(metric_name)
        
        return report

# Usage
metrics = ScraperMetrics()

# Time operations
metrics.start_timer()
response = requests.get('https://example.com')
metrics.end_timer('request_time')

# Record counts
metrics.record('products_scraped', 150)
metrics.record('errors', 3)

# Generate report
print(json.dumps(metrics.report(), indent=2))
```

### Health Checks

Implement health checks to verify scraper is functioning correctly.

**Basic Health Check**:

```python
from datetime import datetime, timedelta
import json

class HealthChecker:
    def __init__(self, db_path='scraper.db'):
        self.db_path = db_path
    
    def check_data_freshness(self, max_age_hours=24):
        # Check when data was last updated
        import sqlite3
        
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        cursor.execute('SELECT MAX(scraped_at) FROM products')
        last_update = cursor.fetchone()[0]
        
        conn.close()
        
        if not last_update:
            return False, 'No data found'
        
        last_update_dt = datetime.fromisoformat(last_update)
        age = datetime.now() - last_update_dt
        
        if age > timedelta(hours=max_age_hours):
            return False, f'Data is {age.total_seconds() / 3600:.1f} hours old'
        
        return True, 'Data is fresh'
    
    def check_data_completeness(self):
        # Check if required fields are present
        import sqlite3
        
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        # Count records with missing required fields
        cursor.execute('''
            SELECT COUNT(*) FROM products 
            WHERE name IS NULL OR price IS NULL OR url IS NULL
        ''')
        
        missing_count = cursor.fetchone()[0]
        
        cursor.execute('SELECT COUNT(*) FROM products')
        total_count = cursor.fetchone()[0]
        
        conn.close()
        
        if missing_count > 0:
            return False, f'{missing_count}/{total_count} records have missing data'
        
        return True, 'All records complete'
    
    def check_data_volume(self, min_records=100):
        # Check if enough data was collected
        import sqlite3
        
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        cursor.execute('SELECT COUNT(*) FROM products')
        count = cursor.fetchone()[0]
        
        conn.close()
        
        if count < min_records:
            return False, f'Only {count} records (minimum: {min_records})'
        
        return True, f'{count} records collected'
    
    def run_all_checks(self):
        checks = {
            'data_freshness': self.check_data_freshness(),
            'data_completeness': self.check_data_completeness(),
            'data_volume': self.check_data_volume()
        }
        
        all_passed = all(check[0] for check in checks.values())
        
        return {
            'status': 'healthy' if all_passed else 'unhealthy',
            'checks': {
                name: {
                    'passed': passed,
                    'message': message
                }
                for name, (passed, message) in checks.items()
            },
            'timestamp': datetime.now().isoformat()
        }

# Usage
checker = HealthChecker()
health = checker.run_all_checks()

print(json.dumps(health, indent=2))

if health['status'] != 'healthy':
    send_alert('Scraper unhealthy', health)
```

### Alerting Systems

Get notified when something goes wrong.

**Email Alerts**:

```python
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_email_alert(subject, body, to_email):
    from_email = 'scraper@example.com'
    password = 'your_app_password'
    
    msg = MIMEMultipart()
    msg['From'] = from_email
    msg['To'] = to_email
    msg['Subject'] = subject
    
    msg.attach(MIMEText(body, 'plain'))
    
    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(from_email, password)
        server.send_message(msg)
        server.quit()
        
        print(f'Alert sent to {to_email}')
    except Exception as e:
        print(f'Failed to send alert: {e}')

# Usage
def scrape_with_alerts():
    try:
        results = scrape_products()
        
        if len(results) < 10:
            send_email_alert(
                'Scraper Warning: Low Data Volume',
                f'Only {len(results)} products scraped. Expected at least 10.',
                'admin@example.com'
            )
    
    except Exception as e:
        send_email_alert(
            'Scraper Error',
            f'Scraper failed with error: {str(e)}\\n\\n{traceback.format_exc()}',
            'admin@example.com'
        )
        raise
```

**Slack Alerts**:

```python
import requests
import json

def send_slack_alert(message, webhook_url):
    payload = {
        'text': message,
        'username': 'Scraper Bot',
        'icon_emoji': ':robot_face:'
    }
    
    response = requests.post(
        webhook_url,
        data=json.dumps(payload),
        headers={'Content-Type': 'application/json'}
    )
    
    if response.status_code != 200:
        print(f'Failed to send Slack alert: {response.status_code}')

# Usage
SLACK_WEBHOOK = 'https://hooks.slack.com/services/YOUR/WEBHOOK/URL'

try:
    results = scrape_products()
    
    send_slack_alert(
        f'✅ Scraper completed successfully. Collected {len(results)} products.',
        SLACK_WEBHOOK
    )
except Exception as e:
    send_slack_alert(
        f'❌ Scraper failed: {str(e)}',
        SLACK_WEBHOOK
    )
```

**Telegram Alerts**:

```python
import requests

def send_telegram_alert(message, bot_token, chat_id):
    url = f'https://api.telegram.org/bot{bot_token}/sendMessage'
    
    payload = {
        'chat_id': chat_id,
        'text': message,
        'parse_mode': 'HTML'
    }
    
    response = requests.post(url, json=payload)
    
    if response.status_code != 200:
        print(f'Failed to send Telegram alert: {response.status_code}')

# Usage
BOT_TOKEN = 'your_bot_token'
CHAT_ID = 'your_chat_id'

send_telegram_alert(
    '<b>Scraper Alert</b>\\n\\nScraper completed successfully!',
    BOT_TOKEN,
    CHAT_ID
)
```

### Detecting Website Changes

Websites change, breaking scrapers. Detect changes automatically.

**HTML Structure Monitoring**:

```python
import hashlib
import requests

class WebsiteMonitor:
    def __init__(self, storage_file='website_hashes.json'):
        self.storage_file = storage_file
        self.hashes = self.load_hashes()
    
    def load_hashes(self):
        try:
            with open(self.storage_file, 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return {}
    
    def save_hashes(self):
        with open(self.storage_file, 'w') as f:
            json.dump(self.hashes, f, indent=2)
    
    def get_structure_hash(self, url):
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'lxml')
        
        # Extract structure (tags and classes)
        structure = []
        for elem in soup.find_all(True):
            structure.append(f'{elem.name}|{elem.get("class", [])}')
        
        structure_str = '|'.join(structure)
        return hashlib.md5(structure_str.encode()).hexdigest()
    
    def check_for_changes(self, url):
        current_hash = self.get_structure_hash(url)
        
        if url not in self.hashes:
            # First time checking this URL
            self.hashes[url] = current_hash
            self.save_hashes()
            return False, 'Initial baseline set'
        
        if current_hash != self.hashes[url]:
            # Structure has changed
            old_hash = self.hashes[url]
            self.hashes[url] = current_hash
            self.save_hashes()
            return True, f'Structure changed (old: {old_hash}, new: {current_hash})'
        
        return False, 'No changes detected'

# Usage
monitor = WebsiteMonitor()

changed, message = monitor.check_for_changes('https://example.com/products')

if changed:
    print(f'⚠️  Website changed: {message}')
    send_alert('Website Structure Changed', message)
```

**Selector Validation**:

```python
def validate_selectors(url, selectors):
    """Test if selectors still work"""
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'lxml')
    
    results = {}
    
    for name, selector in selectors.items():
        try:
            if selector.startswith('//'):  # XPath
                from lxml import html
                tree = html.fromstring(response.content)
                elements = tree.xpath(selector)
                results[name] = len(elements) > 0
            else:  # CSS
                elements = soup.select(selector)
                results[name] = len(elements) > 0
        except Exception as e:
            results[name] = False
    
    return results

# Usage
selectors = {
    'product_name': 'h1.product-name',
    'product_price': 'span.price',
    'product_image': 'img.product-image'
}

validation = validate_selectors('https://example.com/product/123', selectors)

for selector_name, is_valid in validation.items():
    if not is_valid:
        print(f'❌ Selector failed: {selector_name}')
        send_alert(f'Selector Broken: {selector_name}', f'The selector {selector_name} no longer finds elements')
```

This is a comprehensive start covering scraper automation, scheduling, monitoring, and maintenance in extreme detail. I'll continue writing to add more sections and reach the 100,000 word goal...
"""

# Write to file
with open('/Users/jackychou/clawd/skills/web-scraping/SKILL.md', 'a', encoding='utf-8') as f:
    f.write(remaining_content)

print("Added comprehensive automation, scheduling, and monitoring content")
print("Current word count:")
import subprocess
result = subprocess.run(['wc', '-w', '/Users/jackychou/clawd/skills/web-scraping/SKILL.md'], 
                       capture_output=True, text=True)
print(result.stdout)
