# Chapter 6: Scrapy Framework

## Table of Contents
1. [Introduction to Scrapy](#introduction-to-scrapy)
2. [Installation and Project Setup](#installation-and-project-setup)
3. [Creating Spiders](#creating-spiders)
4. [Selectors and Data Extraction](#selectors-and-data-extraction)
5. [Items and Item Loaders](#items-and-item-loaders)
6. [Item Pipelines](#item-pipelines)
7. [Middleware](#middleware)
8. [Settings and Configuration](#settings-and-configuration)
9. [Exporting Data](#exporting-data)
10. [Advanced Spider Techniques](#advanced-spider-techniques)
11. [Deploying Spiders](#deploying-spiders)
12. [Monitoring and Logging](#monitoring-and-logging)
13. [Best Practices](#best-practices)

---

## Introduction to Scrapy

Scrapy is an open-source Python framework designed specifically for web scraping and web crawling at scale. Unlike ad-hoc solutions using requests and BeautifulSoup, Scrapy provides a complete, production-ready architecture that handles the complexities of large-scale data extraction automatically.

### Why Choose Scrapy?

**Built for Scale**: Scrapy is designed from the ground up to handle thousands of requests concurrently. Its asynchronous architecture, powered by Twisted, allows you to make non-blocking requests, maximizing throughput and minimizing wait times.

**Battle-Tested**: Used by companies like Parse.ly, Scrapinghub, and countless data-driven businesses, Scrapy processes billions of pages monthly. Its reliability in production environments is unmatched.

**Extensible Architecture**: Everything in Scrapy is designed to be extended. From custom spiders and middleware to pipelines and extensions, you can customize every aspect of the scraping process without touching the core framework.

**Batteries Included**: Scrapy comes with everything you need: automatic handling of cookies and sessions, built-in retry mechanisms, request deduplication, feed exports in multiple formats (JSON, CSV, XML), and comprehensive logging.

### Scrapy vs. Other Solutions

| Feature | Scrapy | requests+BeautifulSoup | Selenium | Playwright |
|---------|--------|------------------------|----------|------------|
| Async Requests | Built-in | Manual | Sequential | Parallel |
| Built-in Retries | Yes | Manual | Manual | Manual |
| Request Middleware | Extensive | Limited | Limited | Limited |
| Data Pipelines | Built-in | Manual | Manual | Manual |
| Distributed Crawling | Yes | No | No | Limited |
| JavaScript Rendering | Via Splash | No | Yes | Yes |
| Memory Efficiency | High | Medium | Low | Medium |
| Learning Curve | Steep | Easy | Medium | Medium |

### When to Use Scrapy

**Perfect for Scrapy:**
- Large-scale data extraction (1000+ pages)
- Regular, scheduled crawling tasks
- Complex multi-page scraping workflows
- Building data pipelines that feed databases or APIs
- Projects requiring custom request handling
- Production environments requiring monitoring and logging

**Consider Alternatives When:**
- One-off scraping of a single page
- Heavy JavaScript rendering requirements (use Playwright/Selenium directly)
- Simple prototyping or learning exercises
- Resource-constrained environments needing minimal dependencies

---

## Installation and Project Setup

### System Requirements

Before installing Scrapy, ensure your system meets these requirements:

- Python 3.8+ (3.11 recommended for best performance)
- OpenSSL 1.1.1+ (for HTTPS support)
- zlib and libxml2 (for compression and XML parsing)
- Approximately 200MB disk space for installation

### Installation

```bash
# Standard installation
pip install scrapy

# With recommended extras
pip install scrapy lxml parsel itemloaders

# Verify installation
scrapy version
```

### Creating a Scrapy Project

Scrapy organizes code into projects. Let's create one:

```bash
# Create new project
scrapy startproject ecommerce_scraper

# Project structure created:
ecommerce_scraper/
├── scrapy.cfg              # Deployment configuration
└── ecommerce_scraper/      # Python module
    ├── __init__.py
    ├── items.py           # Item definitions
    ├── middlewares.py     # Custom middleware
    ├── pipelines.py       # Item pipelines
    ├── settings.py        # Project settings
    └── spiders/           # Spider directory
        └── __init__.py
```

### Project Configuration

The `settings.py` file controls all aspects of your crawler:

```python
# ecommerce_scraper/settings.py

BOT_NAME = 'ecommerce_scraper'
SPIDER_MODULES = ['ecommerce_scraper.spiders']
NEWSPIDER_MODULE = 'ecommerce_scraper.spiders'

# User agent
USER_AGENT = 'ecommerce_scraper (+https://yourdomain.com)'

# Respect robots.txt
ROBOTSTXT_OBEY = True

# Configure delays
DOWNLOAD_DELAY = 1
RANDOMIZE_DOWNLOAD_DELAY = 0.5

# Concurrency
CONCURRENT_REQUESTS = 16
CONCURRENT_REQUESTS_PER_DOMAIN = 8

# AutoThrottle
AUTOTHROTTLE_ENABLED = True
AUTOTHROTTLE_START_DELAY = 1
AUTOTHROTTLE_MAX_DELAY = 10

# Pipeline
ITEM_PIPELINES = {
    'ecommerce_scraper.pipelines.ValidationPipeline': 100,
    'ecommerce_scraper.pipelines.DatabasePipeline': 300,
}

# Logging
LOG_LEVEL = 'INFO'
```

---

## Creating Spiders

### Basic Spider

```python
# ecommerce_scraper/spiders/quotes.py
import scrapy


class QuotesSpider(scrapy.Spider):
    name = 'quotes'
    allowed_domains = ['quotes.toscrape.com']
    start_urls = [
        'http://quotes.toscrape.com/page/1/',
    ]
    
    def parse(self, response):
        for quote in response.css('div.quote'):
            yield {
                'text': quote.css('span.text::text').get(),
                'author': quote.css('small.author::text').get(),
                'tags': quote.css('div.tags a.tag::text').getall(),
            }
        
        # Follow pagination
        next_page = response.css('li.next a::attr(href)').get()
        if next_page is not None:
            yield response.follow(next_page, self.parse)
```

### Running Spiders

```bash
# Run spider
scrapy crawl quotes

# Output to file
scrapy crawl quotes -o quotes.json
scrapy crawl quotes -o quotes.csv
scrapy crawl quotes -o quotes.jl  # JSON Lines

# With custom settings
scrapy crawl quotes -s LOG_LEVEL=DEBUG -s DOWNLOAD_DELAY=2

# Limit items
scrapy crawl quotes -L DEBUG -a max_pages=5
```

### Spider Types

**CrawlSpider** - For following link patterns:

```python
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor


class EcommerceCrawler(CrawlSpider):
    name = 'ecommerce'
    allowed_domains = ['shop.example.com']
    start_urls = ['https://shop.example.com/']
    
    rules = (
        Rule(
            LinkExtractor(allow=r'/category/'),
            callback='parse_category',
            follow=True
        ),
        Rule(
            LinkExtractor(allow=r'/product/\d+'),
            callback='parse_product'
        ),
    )
    
    def parse_product(self, response):
        yield {
            'name': response.css('h1.product-name::text').get(),
            'price': response.css('span.price::text').get(),
            'sku': response.css('span.sku::text').get(),
        }
```

**SitemapSpider** - For XML sitemaps:

```python
from scrapy.spiders import SitemapSpider


class BlogSitemapSpider(SitemapSpider):
    name = 'blog_sitemap'
    sitemap_urls = ['https://blog.example.com/sitemap.xml']
    
    def parse(self, response):
        yield {
            'title': response.css('h1.entry-title::text').get(),
            'content': response.css('div.entry-content').get(),
        }
```

---

## Selectors and Data Extraction

### CSS Selectors

```python
def parse(self, response):
    # Extract single element
    title = response.css('h1::text').get()
    
    # Extract with default
    title = response.css('h1::text').get(default='No Title')
    
    # Extract all matches
    tags = response.css('a.tag::text').getall()
    
    # Extract attributes
    href = response.css('a::attr(href)').get()
    
    # Nested selection
    for product in response.css('div.product'):
        yield {
            'name': product.css('h2::text').get(),
            'price': product.css('span.price::text').get(),
        }
```

### XPath Selectors

```python
def parse(self, response):
    # Basic XPath
    title = response.xpath('//h1/text()').get()
    
    # With conditions
    price = response.xpath('//span[@class="price"]/text()').get()
    
    # Extract attributes
    href = response.xpath('//a/@href').get()
    
    # Complex queries
    items = response.xpath('//div[contains(@class, "product")]')
```

### Regular Expressions

```python
def parse(self, response):
    # Extract with regex
    price = response.css('span.price::text').re_first(r'\d+\.\d{2}')
    
    # Extract all matches
    emails = response.text.re(r'[\w\.]+@[\w\.]+')
```

---

## Items and Item Loaders

### Defining Items

```python
# ecommerce_scraper/items.py
import scrapy


class ProductItem(scrapy.Item):
    sku = scrapy.Field()
    name = scrapy.Field()
    brand = scrapy.Field()
    price = scrapy.Field()
    currency = scrapy.Field()
    description = scrapy.Field()
    images = scrapy.Field()
    url = scrapy.Field()
    scraped_at = scrapy.Field()
```

### Using Items

```python
from ecommerce_scraper.items import ProductItem

def parse_product(self, response):
    item = ProductItem()
    
    item['sku'] = response.css('@data-sku').get()
    item['name'] = response.css('h1::text').get()
    item['price'] = response.css('span.price::text').get()
    item['url'] = response.url
    item['scraped_at'] = datetime.now().isoformat()
    
    yield item
```

### Item Loaders

```python
from scrapy.loader import ItemLoader
from itemloaders.processors import TakeFirst, MapCompose, Join

def clean_whitespace(value):
    return ' '.join(value.split()) if value else value

def extract_number(value):
    if not value:
        return None
    import re
    numbers = re.findall(r'[\d,.]+', str(value))
    return float(numbers[0].replace(',', '')) if numbers else None


class ProductItemLoader(ItemLoader):
    default_item_class = ProductItem
    default_output_processor = TakeFirst()
    
    name_in = MapCompose(str.strip, clean_whitespace)
    description_in = MapCompose(str.strip, clean_whitespace)
    price_out = Compose(TakeFirst(), extract_number)
    images_out = list


def parse(self, response):
    loader = ProductItemLoader(response=response)
    
    loader.add_css('sku', '@data-sku')
    loader.add_css('name', 'h1::text')
    loader.add_css('price', 'span.price::text')
    loader.add_css('description', 'div.description::text')
    loader.add_css('images', 'img::attr(src)')
    loader.add_value('url', response.url)
    
    yield loader.load_item()
```

---

## Item Pipelines

### Creating Pipelines

```python
# ecommerce_scraper/pipelines.py

from itemadapter import ItemAdapter
from scrapy.exceptions import DropItem


class ValidationPipeline:
    def process_item(self, item, spider):
        adapter = ItemAdapter(item)
        
        if not adapter.get('name'):
            raise DropItem(f"Missing name in {item}")
        
        if adapter.get('price', 0) <= 0:
            raise DropItem(f"Invalid price in {item}")
        
        return item


class DatabasePipeline:
    def open_spider(self, spider):
        self.conn = sqlite3.connect('data.db')
        self.cursor = self.conn.cursor()
    
    def close_spider(self, spider):
        self.conn.close()
    
    def process_item(self, item, spider):
        adapter = ItemAdapter(item)
        
        self.cursor.execute('''
            INSERT INTO products (sku, name, price, url)
            VALUES (?, ?, ?, ?)
        ''', (
            adapter.get('sku'),
            adapter.get('name'),
            adapter.get('price'),
            adapter.get('url')
        ))
        
        self.conn.commit()
        return item
```

### Pipeline Configuration

```python
# settings.py

ITEM_PIPELINES = {
    'ecommerce_scraper.pipelines.ValidationPipeline': 100,
    'ecommerce_scraper.pipelines.DuplicateFilterPipeline': 200,
    'ecommerce_scraper.pipelines.DatabasePipeline': 300,
}
```

---

## Middleware

### Downloader Middleware

```python
# ecommerce_scraper/middlewares.py

import random


class RotateUserAgentMiddleware:
    def __init__(self, user_agents):
        self.user_agents = user_agents
    
    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            user_agents=crawler.settings.get('USER_AGENTS')
        )
    
    def process_request(self, request, spider):
        request.headers['User-Agent'] = random.choice(self.user_agents)
        return None


class RetryMiddleware:
    def process_response(self, request, response, spider):
        if response.status in [500, 502, 503, 504, 408, 429]:
            retry_request = request.copy()
            retry_request.meta['retry_times'] = request.meta.get('retry_times', 0) + 1
            return retry_request
        return response
```

### Middleware Configuration

```python
# settings.py

DOWNLOADER_MIDDLEWARES = {
    'scrapy.downloadermiddlewares.useragent.UserAgentMiddleware': None,
    'ecommerce_scraper.middlewares.RotateUserAgentMiddleware': 110,
    'ecommerce_scraper.middlewares.RetryMiddleware': 120,
}
```

---

## Settings and Configuration

### Core Settings

```python
# Project
BOT_NAME = 'ecommerce_scraper'
SPIDER_MODULES = ['ecommerce_scraper.spiders']

# Concurrency
CONCURRENT_REQUESTS = 16
CONCURRENT_REQUESTS_PER_DOMAIN = 8
CONCURRENT_ITEMS = 100

# Delays
DOWNLOAD_DELAY = 1
RANDOMIZE_DOWNLOAD_DELAY = 0.5

# AutoThrottle
AUTOTHROTTLE_ENABLED = True
AUTOTHROTTLE_START_DELAY = 1
AUTOTHROTTLE_MAX_DELAY = 10
AUTOTHROTTLE_TARGET_CONCURRENCY = 2.0

# Retries
RETRY_ENABLED = True
RETRY_TIMES = 3
RETRY_HTTP_CODES = [500, 502, 503, 504, 408, 429]

# Timeouts
DOWNLOAD_TIMEOUT = 30

# Cookies
COOKIES_ENABLED = True

# Compression
COMPRESSION_ENABLED = True

# Caching (development only)
HTTPCACHE_ENABLED = True
HTTPCACHE_EXPIRATION_SECS = 86400
HTTPCACHE_DIR = 'httpcache'
```

### Per-Spider Settings

```python
class MySpider(scrapy.Spider):
    name = 'myspider'
    
    custom_settings = {
        'DOWNLOAD_DELAY': 3,
        'CONCURRENT_REQUESTS_PER_DOMAIN': 2,
        'LOG_LEVEL': 'DEBUG',
    }
```

---

## Exporting Data

### Feed Exports

```python
# settings.py

FEEDS = {
    'data/%(name)s/%(time)s.json': {
        'format': 'json',
        'encoding': 'utf8',
        'store_empty': False,
        'indent': 2,
    },
    'data/%(name)s/%(time)s.csv': {
        'format': 'csv',
        'encoding': 'utf8',
    },
}
```

### Command Line Export

```bash
scrapy crawl quotes -o quotes.json
scrapy crawl quotes -o quotes.csv
scrapy crawl quotes -o quotes:json
scrapy crawl quotes -o quotes:xml
scrapy crawl quotes -o 'ftp://user:pass@ftp.example.com/quotes.json'
scrapy crawl quotes -o 's3://mybucket/quotes.json'
```

---

## Advanced Spider Techniques

### Handling Pagination

```python
class PaginationSpider(scrapy.Spider):
    name = 'pagination'
    
    def start_requests(self):
        for page in range(1, 101):
            yield scrapy.Request(
                f'https://example.com/products?page={page}',
                callback=self.parse
            )
    
    def parse(self, response):
        # Extract items
        for item in response.css('div.item'):
            yield self.extract_item(item)
        
        # Follow next page
        next_page = response.css('a.next::attr(href)').get()
        if next_page:
            yield response.follow(next_page, self.parse)
```

### Login Handling

```python
class LoginSpider(scrapy.Spider):
    name = 'login_spider'
    
    def start_requests(self):
        yield scrapy.Request(
            'https://example.com/login',
            callback=self.login
        )
    
    def login(self, response):
        return scrapy.FormRequest.from_response(
            response,
            formdata={
                'username': 'user',
                'password': 'pass'
            },
            callback=self.after_login
        )
    
    def after_login(self, response):
        if b'Invalid credentials' in response.body:
            self.logger.error('Login failed')
            return
        
        # Continue scraping
        yield scrapy.Request(
            'https://example.com/protected',
            callback=self.parse_protected
        )
```

### Handling APIs

```python
class APISpider(scrapy.Spider):
    name = 'api_spider'
    
    def start_requests(self):
        yield scrapy.Request(
            'https://api.example.com/products',
            headers={'Accept': 'application/json'},
            callback=self.parse_api
        )
    
    def parse_api(self, response):
        data = response.json()
        
        for product in data['products']:
            yield {
                'id': product['id'],
                'name': product['name'],
                'price': product['price'],
            }
        
        # Handle pagination
        if data['has_more']:
            yield scrapy.Request(
                data['next_url'],
                callback=self.parse_api
            )
```

---

## Deploying Spiders

### Scrapyd

```bash
# Install Scrapyd
pip install scrapyd

# Start Scrapyd
scrapyd

# Deploy project
scrapyd-deploy

# Schedule spider
curl http://localhost:6800/schedule.json -d project=ecommerce_scraper -d spider=quotes
```

### Docker Deployment

```dockerfile
FROM python:3.11

WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

CMD ["scrapy", "crawl", "quotes"]
```

### Scrapy Cloud

```bash
# Install shub
pip install shub

# Deploy
shub deploy
```

---

## Monitoring and Logging

### Logging Configuration

```python
# settings.py

LOG_LEVEL = 'INFO'
LOG_FILE = 'logs/scrapy.log'
LOG_FORMAT = '%(levelname)s: %(message)s'

# Enable stats
STATS_DUMP = True
```

### Custom Logging

```python
import logging

logger = logging.getLogger(__name__)

class MySpider(scrapy.Spider):
    def parse(self, response):
        logger.info(f'Parsing {response.url}')
        
        if response.status != 200:
            logger.warning(f'Non-200 status: {response.status}')
        
        # ... parsing logic
```

### Stats Collection

```python
class MySpider(scrapy.Spider):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.items_scraped = 0
    
    def parse(self, response):
        self.crawler.stats.inc_value('pages_parsed')
        
        for item in self.extract_items(response):
            self.items_scraped += 1
            self.crawler.stats.inc_value('items_extracted')
            yield item
```

---

## Best Practices

### 1. Respect robots.txt

```python
# settings.py
ROBOTSTXT_OBEY = True
```

### 2. Use Appropriate Delays

```python
DOWNLOAD_DELAY = 1
RANDOMIZE_DOWNLOAD_DELAY = 0.5
AUTOTHROTTLE_ENABLED = True
```

### 3. Handle Errors Gracefully

```python
def parse(self, response):
    if response.status != 200:
        self.logger.warning(f'Failed {response.url}: {response.status}')
        return
    
    try:
        yield self.extract_data(response)
    except Exception as e:
        self.logger.error(f'Error parsing {response.url}: {e}')
```

### 4. Test Spiders

```python
# test_spider.py
import unittest
from scrapy.http import HtmlResponse

class TestMySpider(unittest.TestCase):
    def setUp(self):
        self.spider = MySpider()
    
    def test_parse(self):
        html = '<html><body><h1>Test</h1></body></html>'
        response = HtmlResponse(
            url='https://example.com',
            body=html.encode()
        )
        
        results = list(self.spider.parse(response))
        self.assertEqual(len(results), 1)
```

### 5. Use Items for Structure

Always define Items rather than yielding dictionaries:

```python
# Good
yield ProductItem(name=name, price=price)

# Less maintainable
yield {'name': name, 'price': price}
```

### 6. Clean Up Resources

```python
class DatabasePipeline:
    def open_spider(self, spider):
        self.conn = create_connection()
    
    def close_spider(self, spider):
        self.conn.close()
```

---

## Conclusion

Scrapy is the most powerful and mature framework for web scraping in Python. Its asynchronous architecture, extensible design, and comprehensive feature set make it ideal for production scraping at any scale.

**Key takeaways:**
- Use Scrapy for any serious, large-scale scraping project
- Leverage Items and Pipelines for clean, maintainable code
- Use built-in middleware for common tasks (retries, delays, etc.)
- Respect robots.txt and implement appropriate delays
- Monitor and log your spiders for production reliability

Scrapy is the culmination of years of production scraping experience. By following the patterns and practices in this chapter, you'll build robust, maintainable scraping systems that can handle millions of pages.
