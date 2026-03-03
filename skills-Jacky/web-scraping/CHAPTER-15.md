# Chapter 15: Testing and Quality Assurance

## Table of Contents
1. [Introduction to Testing](#introduction)
2. [Unit Testing for Scrapers](#unit-testing)
3. [Integration Testing](#integration-testing)
4. [Test Fixtures and Mocking](#fixtures)
5. [Spider Contracts](#contracts)
6. [Regression Testing](#regression)
7. [Performance Testing](#performance)
8. [CI/CD for Scraping](#cicd)

---

## Introduction to Testing

Testing web scrapers presents unique challenges: external dependencies on websites, changing HTML structures, and network variability. A comprehensive testing strategy combines unit tests for parsing logic, integration tests with recorded responses, and contract tests that validate spider behavior against real URLs.

### Testing Pyramid for Scraping

```
        /\\
       /  \\\n      / E2E \\      <- Full spider runs on test URLs
     /--------\\
    / Integration\\  <- Parser + HTTP client with mocks
   /--------------\\
  /   Unit Tests    \\ <- Pure parsing functions, selectors
 /--------------------\\
```

---

## Unit Testing for Scrapers

### Testing HTML Parsing

```python
import unittest
from bs4 import BeautifulSoup
from typing import Dict, List, Optional


class ProductParser:
    """Parser to test"""
    
    def parse_product(self, html: str) -> Optional[Dict]:
        soup = BeautifulSoup(html, 'html.parser')
        
        name = soup.select_one('h1.product-name')
        price = soup.select_one('.price')
        
        if not name or not price:
            return None
        
        return {
            'name': name.get_text(strip=True),
            'price': self._parse_price(price.get_text()),
            'currency': 'USD',
        }
    
    def _parse_price(self, price_text: str) -> float:
        import re
        numbers = re.findall(r'[\\d.]+', price_text.replace(',', ''))
        return float(numbers[0]) if numbers else 0.0


class TestProductParser(unittest.TestCase):
    """Unit tests for ProductParser"""
    
    def setUp(self):
        self.parser = ProductParser()
    
    def test_parse_valid_product(self):
        """Test parsing a valid product HTML"""
        html = '''
        <html>
            <body>
                <h1 class="product-name">Test Product</h1>
                <span class="price">$99.99</span>
            </body>
        </html>
        '''
        
        result = self.parser.parse_product(html)
        
        self.assertIsNotNone(result)
        self.assertEqual(result['name'], 'Test Product')
        self.assertEqual(result['price'], 99.99)
        self.assertEqual(result['currency'], 'USD')
    
    def test_parse_missing_name(self):
        """Test parsing when product name is missing"""
        html = '''
        <html>
            <body>
                <span class="price">$99.99</span>
            </body>
        </html>
        '''
        
        result = self.parser.parse_product(html)
        self.assertIsNone(result)
    
    def test_parse_price_with_commas(self):
        """Test parsing price with thousands separator"""
        html = '''
        <html>
            <body>
                <h1 class="product-name">Expensive Item</h1>
                <span class="price">$1,299.99</span>
            </body>
        </html>
        '''
        
        result = self.parser.parse_product(html)
        self.assertEqual(result['price'], 1299.99)
    
    def test_parse_price_variations(self):
        """Test various price formats"""
        test_cases = [
            ('$99.99', 99.99),
            ('$1,234.56', 1234.56),
            ('Price: $50', 50.0),
            ('USD 100.00', 100.0),
        ]
        
        for price_text, expected in test_cases:
            result = self.parser._parse_price(price_text)
            self.assertEqual(result, expected, f"Failed for: {price_text}")


class TestSelectors(unittest.TestCase):
    """Test CSS/XPath selectors in isolation"""
    
    def setUp(self):
        self.sample_html = '''
        <div class="product-list">
            <article class="product" data-id="123">
                <h2>Name 1</h2>
                <span class="price">$10</span>
            </article>
            <article class="product" data-id="456">
                <h2>Name 2</h2>
                <span class="price">$20</span>
            </article>
        </div>
        '''
        self.soup = BeautifulSoup(self.sample_html, 'html.parser')
    
    def test_product_count(self):
        """Test correct number of products selected"""
        products = self.soup.select('.product')
        self.assertEqual(len(products), 2)
    
    def test_data_attribute_extraction(self):
        """Test extracting data attributes"""
        products = self.soup.select('.product')
        ids = [p.get('data-id') for p in products]
        self.assertEqual(ids, ['123', '456'])
    
    def test_nested_selection(self):
        """Test nested element selection"""
        first_product = self.soup.select_one('.product')
        name = first_product.select_one('h2').get_text()
        self.assertEqual(name, 'Name 1')
```

### Testing with Pytest

```python
import pytest
from bs4 import BeautifulSoup


@pytest.fixture
def sample_product_html():
    """Fixture providing sample HTML"""
    return '''
    <article class="product">
        <h1 class="name">Test Product</h1>
        <p class="description">A great product</p>
        <span class="price" data-currency="USD">$99.99</span>
        <ul class="features">
            <li>Feature 1</li>
            <li>Feature 2</li>
        </ul>
    </article>
    '''


@pytest.fixture
def parser():
    """Fixture providing parser instance"""
    return ProductParser()


def test_extract_features(parser, sample_product_html):
    """Test extracting list items"""
    soup = BeautifulSoup(sample_product_html, 'html.parser')
    features = [li.get_text() for li in soup.select('.features li')]
    
    assert features == ['Feature 1', 'Feature 2']
    assert len(features) == 2


def test_data_attribute(parser, sample_product_html):
    """Test extracting data attributes"""
    soup = BeautifulSoup(sample_product_html, 'html.parser')
    price_elem = soup.select_one('.price')
    
    assert price_elem.get('data-currency') == 'USD'


@pytest.mark.parametrize("input_text,expected", [
    ("$99.99", 99.99),
    ("$1,234.56", 1234.56),
    ("Price: €50", 50.0),
    ("100 USD", 100.0),
])
def test_price_parsing(parser, input_text, expected):
    """Test price parsing with various formats"""
    result = parser._parse_price(input_text)
    assert result == expected


# Fixtures for different HTML structures
@pytest.fixture
def out_of_stock_html():
    return '''
    <div class="product">
        <h1>Product Name</h1>
        <span class="availability out-of-stock">Sold Out</span>
    </div>
    '''


@pytest.fixture
def on_sale_html():
    return '''
    <div class="product">
        <h1>Product Name</h1>
        <span class="original-price">$200</span>
        <span class="sale-price">$150</span>
        <span class="discount">25% off</span>
    </div>
    '''


def test_availability_extraction(out_of_stock_html):
    """Test extracting stock status"""
    soup = BeautifulSoup(out_of_stock_html, 'html.parser')
    status = soup.select_one('.availability')
    
    assert 'out-of-stock' in status.get('class', [])
    assert status.get_text() == 'Sold Out'
```

---

## Integration Testing

### Testing with Recorded Responses

```python
import unittest
from unittest.mock import patch, Mock
import json
import os


class TestWithRecordedResponses(unittest.TestCase):
    """Integration tests using recorded HTTP responses"""
    
    RECORDINGS_DIR = 'test/fixtures/recordings'
    
    def setUp(self):
        os.makedirs(self.RECORDINGS_DIR, exist_ok=True)
    
    def _load_recording(self, name):
        """Load recorded response"""
        path = os.path.join(self.RECORDINGS_DIR, f'{name}.json')
        with open(path, 'r') as f:
            return json.load(f)
    
    def _save_recording(self, name, response_data):
        """Save response for future tests"""
        path = os.path.join(self.RECORDINGS_DIR, f'{name}.json')
        with open(path, 'w') as f:
            json.dump(response_data, f, indent=2)
    
    @patch('requests.get')
    def test_fetch_product_page(self, mock_get):
        """Test fetching with mocked response"""
        # Load or create recording
        recording_name = 'product_page_example'
        
        try:
            recording = self._load_recording(recording_name)
        except FileNotFoundError:
            # Create recording from real request (run once)
            import requests
            response = requests.get('https://example.com/product/123')
            recording = {
                'url': response.url,
                'status_code': response.status_code,
                'headers': dict(response.headers),
                'body': response.text,
            }
            self._save_recording(recording_name, recording)
        
        # Configure mock
        mock_response = Mock()
        mock_response.status_code = recording['status_code']
        mock_response.text = recording['body']
        mock_response.headers = recording['headers']
        mock_get.return_value = mock_response
        
        # Test the fetch
        from myscraper import fetch_product
        result = fetch_product('https://example.com/product/123')
        
        self.assertIsNotNone(result)
        mock_get.assert_called_once()


# Using responses library for cleaner HTTP mocking
class TestWithResponsesLibrary(unittest.TestCase):
    """Tests using the responses library"""
    
    def setUp(self):
        import responses
        self.responses = responses
        self.responses.start()
    
    def tearDown(self):
        self.responses.stop()
        self.responses.reset()
    
    def test_api_client(self):
        """Test API client with mocked responses"""
        # Mock the API response
        self.responses.add(
            self.responses.GET,
            'https://api.example.com/products/123',
            json={
                'id': '123',
                'name': 'Test Product',
                'price': 99.99,
            },
            status=200
        )
        
        from myscraper import APIClient
        client = APIClient()
        product = client.get_product('123')
        
        self.assertEqual(product['name'], 'Test Product')
        self.assertEqual(product['price'], 99.99)


# VCR.py for automatic recording
class TestWithVCR(unittest.TestCase):
    """Tests using VCR.py for automatic recording/replay"""
    
    def test_with_vcr(self):
        """Test automatically records and replays HTTP"""
        import vcr
        
        with vcr.use_cassette('fixtures/vcr_cassettes/product_fetch.yaml'):
            import requests
            response = requests.get('https://api.example.com/products/123')
            
            # First run: makes real request and records
            # Subsequent runs: replays recorded response
            self.assertEqual(response.status_code, 200)
```

---

## Test Fixtures and Mocking

### Comprehensive Fixture System

```python
import pytest
import json
from pathlib import Path


@pytest.fixture(scope='session')
def test_data_dir():
    """Return path to test data directory"""
    return Path(__file__).parent / 'fixtures'


@pytest.fixture
def load_html(test_data_dir):
    """Factory fixture for loading HTML fixtures"""
    def _load(filename):
        path = test_data_dir / 'html' / filename
        return path.read_text(encoding='utf-8')
    return _load


@pytest.fixture
def load_json(test_data_dir):
    """Factory fixture for loading JSON fixtures"""
    def _load(filename):
        path = test_data_dir / 'json' / filename
        return json.loads(path.read_text())
    return _load


# Example usage
def test_with_fixtures(load_html, load_json):
    """Test using fixture files"""
    html = load_html('product_page.html')
    expected = load_json('expected_product.json')
    
    result = parse_product(html)
    assert result == expected


# Mocking external services
@pytest.fixture
def mock_proxy_pool():
    """Mock proxy pool for testing"""
    from unittest.mock import MagicMock
    
    pool = MagicMock()
    pool.get_proxy.return_value = 'http://proxy.example.com:8080'
    pool.report_success = MagicMock()
    pool.report_failure = MagicMock()
    return pool


@pytest.fixture
def mock_storage():
    """Mock storage backend"""
    from unittest.mock import MagicMock
    
    storage = MagicMock()
    storage.save = MagicMock(return_value=True)
    storage.exists = MagicMock(return_value=False)
    return storage


def test_scraper_with_mocks(mock_proxy_pool, mock_storage):
    """Test scraper with mocked dependencies"""
    from myscraper import ProductScraper
    
    scraper = ProductScraper(
        proxy_pool=mock_proxy_pool,
        storage=mock_storage
    )
    
    # Test logic here
    # mock_proxy_pool.get_proxy.assert_called()
    # mock_storage.save.assert_called_with(expected_data)
```

---

## Spider Contracts

### Scrapy Contracts

```python
import scrapy
from scrapy.contracts import Contract
from scrapy.exceptions import ContractFail


class UrlCountContract(Contract):
    """Contract to verify number of URLs extracted"""
    name = 'url_count'
    
    def post_process(self, output):
        urls = [x for x in output if isinstance(x, scrapy.Request)]
        expected = int(self.args[0])
        
        if len(urls) < expected:
            raise ContractFail(f"Expected {expected} URLs, got {len(urls)}")


class ItemFieldContract(Contract):
    """Contract to verify item fields"""
    name = 'fields'
    
    def post_process(self, output):
        items = [x for x in output if not isinstance(x, scrapy.Request)]
        required_fields = self.args
        
        for item in items:
            for field in required_fields:
                if field not in item or not item[field]:
                    raise ContractFail(f"Missing or empty field: {field}")


class ProductSpider(scrapy.Spider):
    name = 'products'
    
    def parse(self, response):
        """
        Parse product listing page
        
        @url https://example.com/products
        @returns items 10 50
        @returns requests 0 5
        @fields name price url
        @url_count 1
        """
        for product in response.css('.product'):
            yield {
                'name': product.css('h2::text').get(),
                'price': product.css('.price::text').get(),
                'url': product.css('a::attr(href)').get(),
            }
        
        next_page = response.css('a.next::attr(href)').get()
        if next_page:
            yield response.follow(next_page, self.parse)


# Running contracts
# scrapy check products
```

---

## Regression Testing

### Detecting Website Changes

```python
import hashlib
import json
from datetime import datetime
from pathlib import Path


class StructureFingerprint:
    """Fingerprint website structure for change detection"""
    
    def __init__(self, storage_dir='test/fingerprints'):
        self.storage_dir = Path(storage_dir)
        self.storage_dir.mkdir(parents=True, exist_ok=True)
    
    def fingerprint_structure(self, html: str) -> dict:
        """Create structural fingerprint of HTML"""
        from bs4 import BeautifulSoup
        soup = BeautifulSoup(html, 'html.parser')
        
        # Extract structure without content
        structure = {
            'selectors': {},
            'tags': {},
            'classes': set(),
            'ids': set(),
        }
        
        for element in soup.find_all(True):
            tag = element.name
            structure['tags'][tag] = structure['tags'].get(tag, 0) + 1
            
            if element.get('class'):
                structure['classes'].update(element['class'])
            if element.get('id'):
                structure['ids'].add(element['id'])
        
        structure['classes'] = sorted(structure['classes'])
        structure['ids'] = sorted(structure['ids'])
        
        return structure
    
    def save_fingerprint(self, url: str, html: str):
        """Save fingerprint for URL"""
        fingerprint = self.fingerprint_structure(html)
        
        url_hash = hashlib.md5(url.encode()).hexdigest()
        filepath = self.storage_dir / f'{url_hash}.json'
        
        data = {
            'url': url,
            'timestamp': datetime.now().isoformat(),
            'fingerprint': fingerprint,
        }
        
        filepath.write_text(json.dumps(data, indent=2))
    
    def compare_fingerprint(self, url: str, html: str) -> dict:
        """Compare current structure to saved fingerprint"""
        url_hash = hashlib.md5(url.encode()).hexdigest()
        filepath = self.storage_dir / f'{url_hash}.json'
        
        if not filepath.exists():
            return {'status': 'new', 'changes': []}
        
        saved = json.loads(filepath.read_text())
        current = self.fingerprint_structure(html)
        
        changes = []
        
        # Compare tag counts
        saved_tags = saved['fingerprint']['tags']
        for tag, count in current['tags'].items():
            saved_count = saved_tags.get(tag, 0)
            if abs(count - saved_count) > saved_count * 0.2:  # 20% threshold
                changes.append(f"Tag '{tag}' count changed: {saved_count} -> {count}")
        
        # Compare classes
        saved_classes = set(saved['fingerprint']['classes'])
        current_classes = set(current['classes'])
        
        removed_classes = saved_classes - current_classes
        added_classes = current_classes - saved_classes
        
        if removed_classes:
            changes.append(f"Removed classes: {removed_classes}")
        if added_classes:
            changes.append(f"Added classes: {added_classes}")
        
        return {
            'status': 'changed' if changes else 'unchanged',
            'changes': changes,
        }


class RegressionTestSuite:
    """Suite for regression testing"""
    
    def __init__(self, spider_class, test_urls):
        self.spider_class = spider_class
        self.test_urls = test_urls
        self.fingerprinter = StructureFingerprint()
    
    def run_regression_tests(self):
        """Run all regression tests"""
        import requests
        
        results = []
        for url in self.test_urls:
            try:
                response = requests.get(url, timeout=30)
                comparison = self.fingerprinter.compare_fingerprint(
                    url, response.text
                )
                
                results.append({
                    'url': url,
                    **comparison,
                })
                
                # Update fingerprint
                self.fingerprinter.save_fingerprint(url, response.text)
                
            except Exception as e:
                results.append({
                    'url': url,
                    'status': 'error',
                    'error': str(e),
                })
        
        return results
```

---

## Performance Testing

### Benchmarking Scrapers

```python
import time
import statistics
from contextlib import contextmanager
from typing import List, Callable
import pytest


@contextmanager
def timed_execution(name: str):
    """Context manager for timing code blocks"""
    start = time.perf_counter()
    yield
    elapsed = time.perf_counter() - start
    print(f"{name}: {elapsed:.4f}s")


class PerformanceBenchmark:
    """Benchmark scraper performance"""
    
    def __init__(self, iterations=10):
        self.iterations = iterations
        self.results = []
    
    def benchmark(self, func: Callable, *args, **kwargs) -> dict:
        """Benchmark a function"""
        times = []
        
        for _ in range(self.iterations):
            start = time.perf_counter()
            func(*args, **kwargs)
            elapsed = time.perf_counter() - start
            times.append(elapsed)
        
        return {
            'mean': statistics.mean(times),
            'median': statistics.median(times),
            'stdev': statistics.stdev(times) if len(times) > 1 else 0,
            'min': min(times),
            'max': max(times),
            'iterations': self.iterations,
        }
    
    def benchmark_parser(self, parser, html: str) -> dict:
        """Benchmark HTML parser"""
        return self.benchmark(parser.parse, html)


@pytest.mark.benchmark
class TestParserPerformance:
    """Performance tests for parsers"""
    
    @pytest.fixture
ndef large_html(self):
        """Generate large HTML document"""
        products = []
        for i in range(1000):
            products.append(f'''
                <div class="product" data-id="{i}">
                    <h2>Product {i}</h2>
                    <p class="description">Description for product {i}</p>
                    <span class="price">${i * 10}.99</span>
                </div>
            ''')
        
        return f'<html><body>{"".join(products)}</body></html>'
    
    def test_parse_performance(self, large_html):
        """Test parser handles large documents efficiently"""
        from myscraper import ProductParser
        
        parser = ProductParser()
        benchmark = PerformanceBenchmark(iterations=5)
        
        result = benchmark.benchmark_parser(parser, large_html)
        
        # Assert reasonable performance
        assert result['mean'] < 1.0  # Should parse in under 1 second
        assert result['stdev'] < result['mean'] * 0.2  # Consistent performance


# Memory usage testing
import tracemalloc


def test_memory_usage():
    """Test memory usage remains bounded"""
    tracemalloc.start()
    
    # Run parser multiple times
    from myscraper import ProductParser
    parser = ProductParser()
    
    for _ in range(100):
        html = '<div>' + '<p>Text</p>' * 1000 + '</div>'
        parser.parse(html)
    
    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    
    # Memory should not grow unbounded
    print(f"Current: {current / 1024 / 1024:.2f} MB")
    print(f"Peak: {peak / 1024 / 1024:.2f} MB")


# Concurrent performance testing
import asyncio


async def test_concurrent_requests():
    """Test performance under concurrent load"""
    import aiohttp
    
    async def fetch(session, url):
        async with session.get(url) as response:
            return await response.text()
    
    urls = ['https://example.com'] * 10
    
    start = time.time()
    async with aiohttp.ClientSession() as session:
        await asyncio.gather(*[fetch(session, url) for url in urls])
    elapsed = time.time() - start
    
    print(f"10 concurrent requests: {elapsed:.2f}s")
```

---

## CI/CD for Scraping

### GitHub Actions Workflow

```yaml
# .github/workflows/test.yml
name: Test Scrapers

on:
  push:
    branches: [ main, develop ]
  pull_request:
    branches: [ main ]

jobs:
  test:
    runs-on: ubuntu-latest
    
    steps:
    - uses: actions/checkout@v3
    
    - name: Set up Python
      uses: actions/setup-python@v4
      with:
        python-version: '3.10'
    
    - name: Install dependencies
      run: |
        python -m pip install --upgrade pip
        pip install -r requirements.txt
        pip install -r requirements-test.txt
    
    - name: Run unit tests
      run: pytest tests/unit/ -v --cov=myscraper --cov-report=xml
    
    - name: Run integration tests
      run: pytest tests/integration/ -v
      env:
        TEST_MODE: ci
    
    - name: Run spider contracts
      run: scrapy check
    
    - name: Upload coverage
      uses: codecov/codecov-action@v3
      with:
        file: ./coverage.xml

  regression:
    runs-on: ubuntu-latest
    needs: test
    if: github.event_name == 'schedule'  # Run nightly
    
    steps:
    - uses: actions/checkout@v3
    
    - name: Run regression tests
      run: python -m pytest tests/regression/ -v
    
    - name: Check for website changes
      run: python scripts/check_structure_changes.py
    
    - name: Notify on failure
      if: failure()
      uses: slack/notify-action@v1
      with:
        webhook: ${{ secrets.SLACK_WEBHOOK }}
        message: "Regression tests failed!"

  performance:
    runs-on: ubuntu-latest
    needs: test
    if: contains(github.event.head_commit.message, '[perf]')
    
    steps:
    - uses: actions/checkout@v3
    
    - name: Run performance benchmarks
      run: pytest tests/performance/ --benchmark-only
    
    - name: Upload benchmark results
      uses: actions/upload-artifact@v3
      with:
        name: benchmark-results
        path: .benchmarks/
```

### Pre-commit Hooks

```yaml
# .pre-commit-config.yaml
repos:
  - repo: https://github.com/pre-commit/pre-commit-hooks
    rev: v4.4.0
    hooks:
      - id: trailing-whitespace
      - id: end-of-file-fixer
      - id: check-yaml
      - id: check-json
  
  - repo: https://github.com/psf/black
    rev: 23.3.0
    hooks:
      - id: black
  
  - repo: https://github.com/pycqa/flake8
    rev: 6.0.0
    hooks:
      - id: flake8
  
  - repo: https://github.com/pycqa/isort
    rev: 5.12.0
    hooks:
      - id: isort
  
  - repo: local
    hooks:
      - id: test-spider-contracts
        name: Test Spider Contracts
        entry: scrapy check
        language: system
        pass_filenames: false
        always_run: true
```

This chapter provides comprehensive testing strategies for web scraping systems. From unit tests for parsing functions to integration tests with recorded responses, regression tests for detecting website changes, and CI/CD pipelines for automated testing, these practices ensure your scrapers remain reliable and maintainable over time.
