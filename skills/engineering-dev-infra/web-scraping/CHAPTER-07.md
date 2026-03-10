# CHAPTER 07: JavaScript-Heavy Site Scraping

## Introduction

The modern web has evolved far beyond static HTML pages that can be parsed with simple HTTP requests and regular expressions. Today, Single Page Applications (SPAs), Progressive Web Apps (PWAs), and dynamic web platforms dominate the internet landscape. These applications rely heavily on JavaScript to fetch data, render content, and create interactive user experiences that traditional web scrapers cannot access.

When you visit a site like Twitter, Instagram, Gmail, or any modern e-commerce platform, the HTML you receive in an initial HTTP request is often just a skeleton—a minimal container that loads JavaScript bundles. These scripts then execute in the browser to make API calls, manipulate the DOM, and dynamically render content. This architectural shift presents unique challenges for web scraping that require browser automation tools capable of executing JavaScript just like a real user.

This comprehensive chapter explores the complete toolkit, techniques, and architectural patterns required to scrape JavaScript-heavy websites effectively at production scale. We will dive deep into browser automation with Playwright and Puppeteer, understand complex extraction patterns for dynamic content, master infinite scroll implementations, access Shadow DOM components, capture WebSocket communications, manage browser pools for concurrent scraping, and optimize performance while maintaining system reliability.

## Understanding JavaScript-Rendered Content

Before diving into specific tools and implementations, it is essential to understand fundamentally what makes JavaScript-heavy sites different from traditional static websites. This understanding will inform every architectural decision you make when building scrapers for modern web applications.

### The Fundamental Problem with Traditional Scraping

Traditional web scraping relies on HTTP clients like Python's `requests` or `httpx` to fetch HTML documents, which are then parsed using tools like BeautifulSoup, lxml, or regular expressions. This approach works well for static sites but fails completely for dynamic JavaScript applications.

Consider this example that attempts to scrape tweets using traditional methods:

```python
import requests
from bs4 import BeautifulSoup

# This approach will fail for JS-heavy sites
response = requests.get('https://twitter.com/elonmusk', 
                       headers={'User-Agent': 'Mozilla/5.0'})
soup = BeautifulSoup(response.text, 'html.parser')

# Attempt to find tweets
tweets = soup.find_all('div', {'data-testid': 'tweet'})

print(f"Found {len(tweets)} tweets")
# Output: 0 - No tweets found!
```

The above code executes successfully from a networking perspective—the HTTP request returns a 200 status code and HTML content. However, the content contains no actual tweet data. Twitter's initial HTML is essentially an empty shell that loads JavaScript bundles responsible for fetching and rendering tweets dynamically. The tweets only exist after JavaScript execution, which `requests` cannot perform.

### How Modern Web Applications Work

Understanding the lifecycle of a modern web application helps explain why browser automation is necessary:

**1. Initial Document Request**
When a browser requests a page, the server returns a minimal HTML document. This document typically contains:
- Basic page structure and metadata
- Links to CSS stylesheets
- Script tags pointing to JavaScript bundles
- Root container elements where dynamic content will be injected

**2. JavaScript Bundle Loading and Parsing**
The browser downloads and parses JavaScript files, which can range from a few hundred kilobytes to several megabytes for complex applications. Modern frameworks like React, Vue, Angular, and Svelte compile application code into these bundles.

**3. Initial Rendering and Hydration**
For server-side rendered (SSR) applications, the initial HTML may contain pre-rendered content that JavaScript "hydrates" by attaching event listeners and making interactive. For client-side rendered (CSR) applications, JavaScript renders everything from scratch into empty DOM containers.

**4. API Calls and Data Fetching**
JavaScript makes XHR (XMLHttpRequest) or Fetch API calls to backend services, GraphQL endpoints, or REST APIs to retrieve dynamic data. These calls often include authentication tokens and may be protected against unauthorized access.

**5. Dynamic DOM Manipulation**
As data arrives, JavaScript creates and modifies DOM elements, updates styles, and manages application state. This process continues throughout the user session as they interact with the application.

**6. Event Handling and User Interactions**
User interactions trigger JavaScript event handlers that may fetch additional data, update the UI, or navigate between application views without full page reloads.

For scrapers targeting JavaScript-heavy sites, this means we need tools that can:
- Execute JavaScript in a real browser environment
- Wait for dynamic content to load completely
- Intercept and capture API network requests and responses
- Simulate user interactions like scrolling and clicking
- Manage browser state including cookies, localStorage, and sessionStorage
- Handle memory efficiently for long-running scraping sessions

## Playwright: The Modern Browser Automation Standard

Playwright, developed by Microsoft, has emerged as the leading browser automation framework for modern web scraping. It supports Chromium, Firefox, and WebKit with a unified, consistent API designed for reliability, speed, and maintainability. Playwright's architecture addresses many pain points found in older tools like Selenium and PhantomJS.

### Why Playwright Over Alternatives?

**Playwright vs Selenium:**
- Auto-waiting for elements eliminates flaky tests
- Better handling of modern web features (Web Components, Shadow DOM)
- Faster execution through optimized protocol
- Built-in support for parallel execution
- Superior debugging capabilities

**Playwright vs Puppeteer:**
- Multi-browser support (Firefox, WebKit, not just Chromium)
- More robust auto-waiting mechanisms
- Better handling of modern web platform features
- More active development and Microsoft backing
- Better documentation and tooling

**Playwright vs requests+HTML rendering services:**
- Full control over browser behavior
- No dependency on third-party services
- Better cost control at scale
- More sophisticated interaction capabilities

### Installation and Environment Setup

Installing Playwright requires both the Python package and browser binaries:

```bash
# Install Playwright Python package
pip install playwright

# Install browser binaries (Chromium, Firefox, WebKit)
python -m playwright install

# For CI/CD environments with specific browsers only
python -m playwright install chromium
```

The browser installation downloads approximately 100-200MB per browser type. For production deployments, consider pre-baking Docker images with browsers installed to avoid download delays.

### Basic Playwright Implementation

Here's a comprehensive basic implementation demonstrating proper Playwright patterns:

```python
from playwright.sync_api import sync_playwright, Page, Browser, BrowserContext
from typing import Optional, Dict, Any
import time
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class BasicScraper:
    """Basic Playwright scraper with proper resource management"""
    
    def __init__(self, headless: bool = True):
        self.headless = headless
        self.playwright = None
        self.browser = None
    
    def __enter__(self):
        """Context manager entry - initialize Playwright"""
        self.playwright = sync_playwright().start()
        
        # Launch browser with anti-detection measures
        self.browser = self.playwright.chromium.launch(
            headless=self.headless,
            args=[
                '--disable-blink-features=AutomationControlled',
                '--disable-dev-shm-usage',
                '--no-sandbox',
                '--disable-setuid-sandbox',
                '--disable-infobars',
                '--window-size=1920,1080'
            ]
        )
        
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        """Context manager exit - cleanup resources"""
        if self.browser:
            self.browser.close()
        if self.playwright:
            self.playwright.stop()
    
    def scrape_page(self, url: str, wait_for_selector: Optional[str] = None,
                   timeout: int = 30000) -> Dict[str, Any]:
        """
        Scrape a single page with proper error handling
        
        Args:
            url: Target URL to scrape
            wait_for_selector: CSS selector to wait for
            timeout: Maximum wait time in milliseconds
        
        Returns:
            Dictionary containing page data and metadata
        """
        # Create isolated browser context
        context = self.browser.new_context(
            viewport={'width': 1920, 'height': 1080},
            user_agent='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        )
        
        page = context.new_page()
        
        try:
            logger.info(f"Navigating to {url}")
            
            # Navigate with network idle wait
            response = page.goto(
                url,
                wait_until='networkidle',
                timeout=timeout
            )
            
            # Wait for specific content if specified
            if wait_for_selector:
                logger.info(f"Waiting for selector: {wait_for_selector}")
                page.wait_for_selector(
                    wait_for_selector,
                    state='visible',
                    timeout=timeout
                )
            
            # Additional wait for any remaining dynamic content
            page.wait_for_timeout(2000)
            
            # Extract data
            content = page.content()
            title = page.title()
            
            return {
                'success': True,
                'url': url,
                'title': title,
                'content': content,
                'status_code': response.status if response else None,
                'headers': dict(response.headers) if response else {}
            }
            
        except Exception as e:
            logger.error(f"Error scraping {url}: {e}")
            return {
                'success': False,
                'url': url,
                'error': str(e)
            }
            
        finally:
            # Always cleanup
            page.close()
            context.close()

# Usage example
with BasicScraper(headless=True) as scraper:
    result = scraper.scrape_page(
        'https://example.com',
        wait_for_selector='.content-loaded'
    )
    
    if result['success']:
        print(f"Title: {result['title']}")
        print(f"Content length: {len(result['content'])}")
    else:
        print(f"Failed: {result['error']}")
```

### Advanced Anti-Detection Configuration

Production scraping requires sophisticated anti-detection measures to avoid being identified as automation. Here's a comprehensive configuration:

```python
from playwright.sync_api import sync_playwright, Route, Request
from typing import List, Dict, Optional
import random

class StealthPlaywrightConfig:
    """Production-grade stealth configuration"""
    
    # Realistic viewport sizes
    VIEWPORTS = [
        {'width': 1920, 'height': 1080},  # Full HD
        {'width': 1366, 'height': 768},   # Laptop
        {'width': 1536, 'height': 864},   # Common Windows
        {'width': 1440, 'height': 900},   # MacBook
        {'width': 1280, 'height': 720},   # HD
    ]
    
    # Realistic user agents with version rotation
    USER_AGENTS = [
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36',
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.1 Safari/605.1.15',
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/121.0',
    ]
    
    # Locale and timezone combinations
    LOCALES = [
        {'locale': 'en-US', 'timezone': 'America/New_York'},
        {'locale': 'en-US', 'timezone': 'America/Los_Angeles'},
        {'locale': 'en-GB', 'timezone': 'Europe/London'},
        {'locale': 'en-CA', 'timezone': 'America/Toronto'},
    ]
    
    @classmethod
    def get_random_config(cls) -> Dict:
        """Generate random but realistic browser configuration"""
        viewport = random.choice(cls.VIEWPORTS)
        user_agent = random.choice(cls.USER_AGENTS)
        locale_config = random.choice(cls.LOCALES)
        
        return {
            'viewport': viewport,
            'user_agent': user_agent,
            'locale': locale_config['locale'],
            'timezone_id': locale_config['timezone'],
        }
    
    @classmethod
    def get_launch_options(cls, headless: bool = True) -> Dict:
        """Get browser launch options"""
        return {
            'headless': headless,
            'args': [
                '--disable-blink-features=AutomationControlled',
                '--disable-dev-shm-usage',
                '--disable-web-security',
                '--disable-features=IsolateOrigins,site-per-process',
                '--disable-site-isolation-trials',
                '--no-sandbox',
                '--disable-setuid-sandbox',
                '--disable-infobars',
                '--window-position=0,0',
                '--ignore-certificate-errors',
                '--ignore-certificate-errors-spki-list',
                '--disable-accelerated-2d-canvas',
                '--disable-gpu',
                '--hide-scrollbars',
                '--disable-notifications',
                '--disable-background-timer-throttling',
                '--disable-backgrounding-occluded-windows',
                '--disable-renderer-backgrounding',
            ]
        }
    
    @classmethod
    def get_context_options(cls, proxy: Optional[str] = None) -> Dict:
        """Get browser context options with randomization"""
        config = cls.get_random_config()
        
        options = {
            'viewport': config['viewport'],
            'user_agent': config['user_agent'],
            'locale': config['locale'],
            'timezone_id': config['timezone_id'],
            'permissions': ['geolocation'],
            'geolocation': {
                'latitude': 40.7128 + random.uniform(-0.1, 0.1),
                'longitude': -74.0060 + random.uniform(-0.1, 0.1)
            },
            'extra_http_headers': {
                'Accept-Language': f"{config['locale']},en;q=0.9",
                'Accept-Encoding': 'gzip, deflate, br',
                'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8',
                'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120", "Google Chrome";v="120"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Windows"',
                'Upgrade-Insecure-Requests': '1'
            }
        }
        
        if proxy:
            options['proxy'] = {'server': proxy}
        
        return options
    
    @staticmethod
    def inject_stealth_scripts(page):
        """
        Inject JavaScript to avoid automation detection
        This modifies browser fingerprint to appear more human
        """
        stealth_scripts = """
        // Override webdriver property
        Object.defineProperty(navigator, 'webdriver', {
            get: () => undefined
        });
        
        // Override plugins
        Object.defineProperty(navigator, 'plugins', {
            get: () => [
                {
                    0: {type: "application/x-google-chrome-pdf", suffixes: "pdf", description: "Portable Document Format"},
                    description: "Portable Document Format",
                    filename: "internal-pdf-viewer",
                    length: 1,
                    name: "Chrome PDF Plugin"
                },
                {
                    0: {type: "application/pdf", suffixes: "pdf", description: ""},
                    description: "Portable Document Format",
                    filename: "mhjfbmdgcfjbbpaeojofohoefgiehjai",
                    length: 1,
                    name: "Chrome PDF Viewer"
                },
                {
                    0: {type: "application/x-google-chrome-pdf", suffixes: "pdf", description: "Portable Document Format"},
                    description: "Portable Document Format",
                    filename: "internal-pdf-viewer2",
                    length: 1,
                    name: "Native Client"
                }
            ]
        });
        
        // Override languages
        Object.defineProperty(navigator, 'languages', {
            get: () => ['en-US', 'en']
        });
        
        // Add Chrome runtime
        window.chrome = {
            runtime: {
                OnInstalledReason: {
                    CHROME_UPDATE: "chrome_update",
                    INSTALL: "install",
                    SHARED_MODULE_UPDATE: "shared_module_update",
                    UPDATE: "update"
                },
                OnRestartRequiredReason: {
                    APP_UPDATE: "app_update",
                    OS_UPDATE: "os_update",
                    PERIODIC: "periodic"
                },
                PlatformArch: {
                    ARM: "arm",
                    ARM64: "arm64",
                    MIPS: "mips",
                    MIPS64: "mips64",
                    X86_32: "x86-32",
                    X86_64: "x86-64"
                },
                PlatformNaclArch: {
                    ARM: "arm",
                    MIPS: "mips",
                    MIPS64: "mips64",
                    MIPS64EL: "mips64el",
                    MIPSEL: "mipsel",
                    X86_32: "x86-32",
                    X86_64: "x86-64"
                },
                PlatformOs: {
                    ANDROID: "android",
                    CROS: "cros",
                    LINUX: "linux",
                    MAC: "mac",
                    OPENBSD: "openbsd",
                    WIN: "win"
                },
                RequestUpdateCheckStatus: {
                    NO_UPDATE: "no_update",
                    THROTTLED: "throttled",
                    UPDATE_AVAILABLE: "update_available"
                }
            }
        };
        
        // Override permissions query
        const originalQuery = window.navigator.permissions.query;
        window.navigator.permissions.query = (parameters) => (
            parameters.name === 'notifications' ?
            Promise.resolve({ state: Notification.permission }) :
            originalQuery(parameters)
        );
        
        // Add notification permission
        if (!('Notification' in window)) {
            window.Notification = {
                permission: 'default'
            };
        }
        
        // Override webdriver in navigator
        delete navigator.__proto__.webdriver;
        
        // Canvas fingerprint randomization
        const originalToDataURL = HTMLCanvasElement.prototype.toDataURL;
        HTMLCanvasElement.prototype.toDataURL = function(type) {
            if (type === 'image/png' && this.width > 100 && this.height > 100) {
                // Add subtle noise to canvas
                const ctx = this.getContext('2d');
                const imageData = ctx.getImageData(0, 0, this.width, this.height);
                const data = imageData.data;
                // Modify a few pixels slightly
                for (let i = 0; i < 10; i++) {
                    const idx = Math.floor(Math.random() * data.length / 4) * 4;
                    data[idx] = Math.max(0, Math.min(255, data[idx] + (Math.random() > 0.5 ? 1 : -1)));
                }
                ctx.putImageData(imageData, 0, 0);
            }
            return originalToDataURL.apply(this, arguments);
        };
        """
        
        page.add_init_script(stealth_scripts)

# Usage example
with sync_playwright() as p:
    browser = p.chromium.launch(**StealthPlaywrightConfig.get_launch_options())
    context = browser.new_context(**StealthPlaywrightConfig.get_context_options())
    page = context.new_page()
    
    # Inject stealth scripts
    StealthPlaywrightConfig.inject_stealth_scripts(page)
    
    # Now scrape with reduced detection risk
    page.goto('https://example.com')
```

## Puppeteer: The Google Alternative

While Playwright is the modern recommendation, Puppeteer (developed by Google) remains widely used and may be preferred in some scenarios. Here's a Python implementation using Pyppeteer:

```python
import asyncio
from pyppeteer import launch
from typing import Optional, Dict, Any

class PuppeteerScraper:
    """Puppeteer-based scraper using Pyppeteer"""
    
    def __init__(self, headless: bool = True):
        self.headless = headless
        self.browser = None
    
    async def initialize(self):
        """Initialize browser"""
        self.browser = await launch(
            headless=self.headless,
            args=[
                '--no-sandbox',
                '--disable-setuid-sandbox',
                '--disable-dev-shm-usage',
                '--disable-accelerated-2d-canvas',
                '--disable-gpu',
                '--window-size=1920,1080'
            ]
        )
    
    async def scrape(self, url: str, wait_for: Optional[str] = None) -> Dict[str, Any]:
        """Scrape page using Puppeteer"""
        page = await self.browser.newPage()
        
        try:
            # Set viewport
            await page.setViewport({'width': 1920, 'height': 1080})
            
            # Set user agent
            await page.setUserAgent(
                'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
            )
            
            # Navigate
            response = await page.goto(
                url,
                {'waitUntil': 'networkidle2', 'timeout': 30000}
            )
            
            # Wait for selector if specified
            if wait_for:
                await page.waitForSelector(wait_for, {'timeout': 10000})
            
            # Wait additional time for rendering
            await page.waitForTimeout(2000)
            
            # Extract data
            content = await page.content()
            title = await page.title()
            
            return {
                'success': True,
                'url': url,
                'title': title,
                'content': content,
                'status': response.status if response else None
            }
            
        except Exception as e:
            return {
                'success': False,
                'url': url,
                'error': str(e)
            }
            
        finally:
            await page.close()
    
    async def close(self):
        """Close browser"""
        if self.browser:
            await self.browser.close()

# Async usage
async def main():
    scraper = PuppeteerScraper()
    await scraper.initialize()
    
    try:
        result = await scraper.scrape('https://example.com')
        print(result)
    finally:
        await scraper.close()

# Run
# asyncio.run(main())
```

For production use, Playwright is generally preferred due to better API design, multi-browser support, more active development, and superior auto-waiting mechanisms.

## Single Page Application (SPA) Scraping Patterns

SPAs require specific patterns for reliable data extraction. The key challenge is determining when content has fully loaded.

### Pattern 1: Network Idle Waiting

Wait for network activity to cease before extracting data:

```python
from playwright.sync_api import sync_playwright
import time
from typing import List, Dict

class NetworkIdleScraper:
    """Scraper that waits for network idle"""
    
    def __init__(self):
        self.pending_requests = set()
    
    def scrape_spa(self, url: str, extract_selector: str = None) -> Dict:
        """Scrape SPA waiting for network idle"""
        with sync_playwright() as p:
            browser = p.chromium.launch(headless=True)
            context = browser.new_context(
                viewport={'width': 1920, 'height': 1080}
            )
            page = context.new_page()
            
            # Track network requests
            def handle_request(request):
                self.pending_requests.add(request.url)
            
            def handle_response(response):
                self.pending_requests.discard(response.url)
            
            page.on('request', handle_request)
            page.on('response', handle_response)
            
            try:
                # Navigate to URL
                page.goto(url, wait_until='domcontentloaded')
                
                # Wait for network idle (custom implementation)
                max_wait = 30
                start_time = time.time()
                
                while self.pending_requests and (time.time() - start_time) < max_wait:
                    time.sleep(0.5)
                
                # Additional wait for any final rendering
                page.wait_for_timeout(2000)
                
                # Wait for specific element if provided
                if extract_selector:
                    page.wait_for_selector(extract_selector, state='visible', timeout=10000)
                
                # Extract data
                data = self._extract_data(page)
                
                return {
                    'success': True,
                    'url': url,
                    'data': data
                }
                
            except Exception as e:
                return {
                    'success': False,
                    'url': url,
                    'error': str(e)
                }
                
            finally:
                context.close()
                browser.close()
    
    def _extract_data(self, page) -> List[Dict]:
        """Extract data from page"""
        return page.evaluate("""
            () => {
                const items = [];
                document.querySelectorAll('.product-card, .item, [data-item]').forEach(el => {
                    items.push({
                        title: el.querySelector('h1, h2, h3, .title')?.textContent?.trim(),
                        price: el.querySelector('.price')?.textContent?.trim(),
                        link: el.querySelector('a')?.href
                    });
                });
                return items;
            }
        """)
```

### Pattern 2: API Response Interception

Intercept and extract data directly from API responses:

```python
from playwright.sync_api import sync_playwright, Response
import json
from typing import Dict, List

class APIInterceptScraper:
    """Scraper that intercepts API responses"""
    
    def __init__(self):
        self.captured_data = []
    
    def scrape_with_interception(self, url: str, 
                                 api_patterns: List[str]) -> Dict:
        """
        Scrape by intercepting API calls
        
        Args:
            url: Page URL to scrape
            api_patterns: List of URL patterns to intercept (e.g., ['/api/products', '/graphql'])
        """
        with sync_playwright() as p:
            browser = p.chromium.launch(headless=True)
            context = browser.new_context()
            page = context.new_page()
            
            # Set up response interception
            def handle_response(response: Response):
                try:
                    # Check if response matches our patterns
                    for pattern in api_patterns:
                        if pattern in response.url:
                            # Capture response body
                            body = response.json()
                            self.captured_data.append({
                                'url': response.url,
                                'status': response.status,
                                'data': body
                            })
                            break
                except:
                    pass  # Not JSON response
            
            page.on('response', handle_response)
            
            # Navigate to page
            page.goto(url, wait_until='networkidle')
            
            # Wait for API calls to complete
            page.wait_for_timeout(5000)
            
            context.close()
            browser.close()
            
            return {
                'success': True,
                'intercepted_calls': len(self.captured_data),
                'data': self.captured_data
            }

# Usage
scraper = APIInterceptScraper()
result = scraper.scrape_with_interception(
    'https://example-shop.com/products',
    api_patterns=['/api/products', '/api/items', '/graphql']
)

for call in result['data']:
    print(f"API: {call['url']}")
    print(f"Data: {json.dumps(call['data'], indent=2)[:500]}")
```

### Pattern 3: Wait for DOM Element State

Wait for specific element states indicating content is ready:

```python
from playwright.sync_api import sync_playwright, Page

class ElementStateScraper:
    """Scraper using element state waiting"""
    
    def scrape_with_state_waiting(self, url: str) -> Dict:
        """Scrape using various element state strategies"""
        with sync_playwright() as p:
            browser = p.chromium.launch(headless=True)
            page = browser.new_page()
            
            page.goto(url)
            
            # Strategy 1: Wait for loading spinner to disappear
            try:
                page.wait_for_selector('.loading, .spinner', state='hidden', timeout=10000)
            except:
                pass  # Spinner might not exist
            
            # Strategy 2: Wait for content to be visible
            page.wait_for_selector('.content-loaded, [data-loaded="true"]', 
                                  state='visible', timeout=30000)
            
            # Strategy 3: Wait for minimum element count
            page.wait_for_function("""
                () => document.querySelectorAll('.product-item').length >= 10
            """, timeout=30000)
            
            # Strategy 4: Wait for specific text to appear
            page.wait_for_selector('text="Load complete"', timeout=10000)
            
            # Extract all items
            items = page.locator('.product-item').all()
            
            data = []
            for item in items:
                try:
                    data.append({
                        'name': item.locator('.product-name').text_content(),
                        'price': item.locator('.price').text_content(),
                        'availability': item.locator('.stock-status').text_content()
                    })
                except:
                    continue
            
            browser.close()
            
            return {
                'success': True,
                'item_count': len(data),
                'items': data
            }
```

## Infinite Scroll Handling

Infinite scroll is ubiquitous on social media, e-commerce, and content platforms. Here are comprehensive patterns for handling it.

### Basic Infinite Scroll Implementation

```python
from playwright.sync_api import sync_playwright
import time
from typing import List, Dict

class InfiniteScrollScraper:
    """Basic infinite scroll scraper"""
    
    def scrape(self, url: str, max_items: int = 100, 
               max_scrolls: int = 50) -> List[Dict]:
        """
        Scrape site with infinite scroll
        
        Args:
            url: Starting URL
            max_items: Maximum items to collect
            max_scrolls: Maximum scroll attempts
        """
        with sync_playwright() as p:
            browser = p.chromium.launch(headless=True)
            page = browser.new_page()
            
            page.goto(url, wait_until='networkidle')
            
            all_items = []
            seen_ids = set()
            previous_height = 0
            scroll_count = 0
            
            while scroll_count < max_scrolls and len(all_items) < max_items:
                # Extract items currently visible
                items = page.evaluate("""
                    () => {
                        const items = [];
                        document.querySelectorAll('.item, .product, [data-id]').forEach(el => {
                            const id = el.getAttribute('data-id') || el.id;
                            const title = el.querySelector('.title, h2, h3')?.textContent;
                            const description = el.querySelector('.description, p')?.textContent;
                            
                            if (id && title) {
                                items.push({ id, title, description });
                            }
                        });
                        return items;
                    }
                """)
                
                # Add new items
                for item in items:
                    if item['id'] not in seen_ids:
                        seen_ids.add(item['id'])
                        all_items.append(item)
                
                # Check if we've reached the limit
                if len(all_items) >= max_items:
                    break
                
                # Scroll down
                current_height = page.evaluate('document.body.scrollHeight')
                
                if current_height == previous_height:
                    # No new content loaded
                    break
                
                page.evaluate('window.scrollTo(0, document.body.scrollHeight)')
                
                # Wait for new content to load
                time.sleep(2)
                
                previous_height = current_height
                scroll_count += 1
            
            browser.close()
            
            return all_items[:max_items]
```

### Advanced Infinite Scroll with Progress Tracking

```python
from playwright.sync_api import sync_playwright, Locator
from typing import List, Dict, Callable, Optional
import logging
from dataclasses import dataclass

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

@dataclass
class ScrollConfig:
    """Configuration for infinite scroll scraping"""
    max_items: int = 100
    max_scrolls: int = 50
    scroll_delay: float = 2.0
    item_selector: str = '.item'
    id_attribute: str = 'data-id'
    no_new_content_threshold: int = 3

class AdvancedInfiniteScrollScraper:
    """Production-grade infinite scroll scraper"""
    
    def __init__(self, config: ScrollConfig = None):
        self.config = config or ScrollConfig()
        self.seen_ids = set()
    
    def scrape(self, url: str, extract_fn: Callable[[Locator], Dict]) -> List[Dict]:
        """
        Scrape with infinite scroll using custom extraction function
        
        Args:
            url: URL to scrape
            extract_fn: Function to extract data from each item element
        """
        with sync_playwright() as p:
            browser = p.chromium.launch(headless=True)
            page = browser.new_page()
            
            logger.info(f"Navigating to {url}")
            page.goto(url, wait_until='networkidle')
            
            all_items = []
            scroll_count = 0
            no_new_content_count = 0
            previous_height = 0
            
            while (scroll_count < self.config.max_scrolls and 
                   len(all_items) < self.config.max_items):
                
                # Extract current items
                item_elements = page.locator(self.config.item_selector).all()
                new_items = self._extract_new_items(item_elements, extract_fn)
                
                if not new_items:
                    no_new_content_count += 1
                    logger.info(f"No new content (attempt {no_new_content_count})")
                    
                    if no_new_content_count >= self.config.no_new_content_threshold:
                        logger.info("No new content threshold reached, stopping")
                        break
                else:
                    no_new_content_count = 0
                    all_items.extend(new_items)
                    logger.info(f"Extracted {len(new_items)} new items, "
                              f"total: {len(all_items)}")
                
                # Check limit
                if len(all_items) >= self.config.max_items:
                    logger.info(f"Reached max items ({self.config.max_items})")
                    break
                
                # Scroll down
                current_height = page.evaluate('document.body.scrollHeight')
                
                if current_height == previous_height:
                    logger.info("Reached end of page")
                    break
                
                self._smooth_scroll(page)
                page.wait_for_timeout(int(self.config.scroll_delay * 1000))
                
                previous_height = current_height
                scroll_count += 1
            
            browser.close()
            
            logger.info(f"Scraping complete. Total items: {len(all_items)}")
            return all_items[:self.config.max_items]
    
    def _extract_new_items(self, elements: List[Locator], 
                          extract_fn: Callable) -> List[Dict]:
        """Extract only new items, skipping duplicates"""
        new_items = []
        
        for element in elements:
            try:
                data = extract_fn(element)
                
                # Generate unique ID
                item_id = data.get('id') or data.get('url') or str(hash(str(data)))
                
                if item_id not in self.seen_ids:
                    self.seen_ids.add(item_id)
                    new_items.append(data)
                    
            except Exception as e:
                logger.warning(f"Failed to extract item: {e}")
        
        return new_items
    
    def _smooth_scroll(self, page):
        """Perform smooth scroll to bottom"""
        page.evaluate("""
            () => {
                window.scrollTo({
                    top: document.body.scrollHeight,
                    behavior: 'smooth'
                });
            }
        """)

# Usage example
def extract_product(item: Locator) -> Dict:
    """Extract product data from element"""
    return {
        'id': item.get_attribute('data-product-id'),
        'name': item.locator('.product-title').text_content(),
        'price': item.locator('.price').text_content(),
        'url': item.locator('a').get_attribute('href'),
        'image': item.locator('img').get_attribute('src')
    }

config = ScrollConfig(
    max_items=100,
    max_scrolls=20,
    scroll_delay=2.0,
    item_selector='.product-card'
)

scraper = AdvancedInfiniteScrollScraper(config)
products = scraper.scrape('https://example.com/products', extract_product)
```

### Handling Intersection Observer Loading

Some sites use Intersection Observer API for lazy loading:

```python
from playwright.sync_api import sync_playwright

class IntersectionObserverScraper:
    """Handle sites using Intersection Observer for lazy loading"""
    
    def scrape_with_intersection_observer(self, url: str) -> List[Dict]:
        """Scrape by triggering intersection observers"""
        with sync_playwright() as p:
            browser = p.chromium.launch(headless=True)
            page = browser.new_page()
            
            page.goto(url)
            
            # Inject monitoring script
            page.evaluate("""
                () => {
                    window.intersectionTriggered = new Set();
                    
                    const originalObserve = IntersectionObserver.prototype.observe;
                    IntersectionObserver.prototype.observe = function(target) {
                        window.intersectionTriggered.add(target.id || target.className);
                        return originalObserve.call(this, target);
                    };
                }
            """)
            
            # Scroll gradually to trigger observers
            viewport_height = page.viewport_size['height']
            total_height = page.evaluate('document.body.scrollHeight')
            
            current_position = 0
            while current_position < total_height:
                # Scroll to position
                page.evaluate(f'window.scrollTo(0, {current_position})')
                page.wait_for_timeout(1000)
                
                current_position += viewport_height * 0.8
                
                # Check what was triggered
                triggered = page.evaluate('window.intersectionTriggered.size')
                logger.info(f"Triggered sections: {triggered}")
            
            # Extract all data
            data = page.evaluate("""
                () => {
                    const items = [];
                    document.querySelectorAll('[data-loaded="true"], .loaded').forEach(el => {
                        items.push({
                            id: el.id,
                            content: el.textContent,
                            html: el.innerHTML
                        });
                    });
                    return items;
                }
            """)
            
            browser.close()
            return data
```

## Shadow DOM and Web Components

Shadow DOM encapsulates component markup and styles. Traditional DOM queries won't penetrate Shadow boundaries.

### Understanding Shadow DOM

Shadow DOM creates an encapsulated subtree within an element:

```html
<custom-product-list>
  #shadow-root (open)
    <style>
      /* Styles are scoped to shadow DOM */
      .product-card { border: 1px solid #ccc; }
    </style>
    <div class="product-card">
      <h3 class="title">Product Name</h3>
      <span class="price">$99.99</span>
    </div>
</custom-product-list>
```

### Accessing Shadow DOM with Playwright

```python
from playwright.sync_api import sync_playwright

class ShadowDOMScraper:
    """Scraper for Shadow DOM content"""
    
    def scrape_shadow_dom(self, url: str) -> List[Dict]:
        """Extract data from Shadow DOM components"""
        with sync_playwright() as p:
            browser = p.chromium.launch(headless=True)
            page = browser.new_page()
            page.goto(url)
            
            # Method 1: Using Playwright's pierce selector
            # Pierce selector automatically penetrates shadow roots
            items = page.locator('pierce/.product-card').all()
            
            data = []
            for item in items:
                try:
                    data.append({
                        'title': item.locator('pierce/.title').text_content(),
                        'price': item.locator('pierce/.price').text_content(),
                        'description': item.locator('pierce/.description').text_content()
                    })
                except:
                    continue
            
            browser.close()
            return data
    
    def scrape_shadow_dom_manual(self, url: str) -> List[Dict]:
        """Manually traverse Shadow DOM using JavaScript"""
        with sync_playwright() as p:
            browser = p.chromium.launch(headless=True)
            page = browser.new_page()
            page.goto(url)
            
            # Extract using JavaScript evaluation
            data = page.evaluate("""
                () => {
                    const items = [];
                    
                    // Find all shadow hosts
                    const hosts = document.querySelectorAll('*');
                    
                    hosts.forEach(host => {
                        if (host.shadowRoot) {
                            // Access shadow root
                            const shadow = host.shadowRoot;
                            
                            // Query within shadow DOM
                            shadow.querySelectorAll('.product-card').forEach(card => {
                                items.push({
                                    title: card.querySelector('.title')?.textContent,
                                    price: card.querySelector('.price')?.textContent,
                                    image: card.querySelector('img')?.src
                                });
                            });
                        }
                    });
                    
                    return items;
                }
            """)
            
            browser.close()
            return data
```

### Handling Nested Shadow DOM

```python
from playwright.sync_api import sync_playwright

class NestedShadowDOMScraper:
    """Handle deeply nested Shadow DOM"""
    
    def scrape_nested_shadow(self, url: str) -> List[Dict]:
        """Recursively traverse nested shadow DOM"""
        with sync_playwright() as p:
            browser = p.chromium.launch(headless=True)
            page = browser.new_page()
            page.goto(url)
            
            # Recursive traversal function
            data = page.evaluate("""
                () => {
                    function traverseShadow(root, depth = 0) {
                        const items = [];
                        
                        // Find all elements that might have shadow roots
                        const allElements = root.querySelectorAll('*');
                        
                        for (const el of allElements) {
                            if (el.shadowRoot) {
                                // Found a shadow host, traverse deeper
                                items.push(...traverseShadow(el.shadowRoot, depth + 1));
                            }
                        }
                        
                        // Extract data from this level
                        root.querySelectorAll('.data-item, .card, [data-extract]').forEach(item => {
                            items.push({
                                depth: depth,
                                text: item.textContent?.trim(),
                                data: item.dataset,
                                id: item.id,
                                className: item.className
                            });
                        });
                        
                        return items;
                    }
                    
                    // Start from document root
                    return traverseShadow(document);
                }
            """)
            
            browser.close()
            return data
```

### Web Components with Slots

```python
from playwright.sync_api import sync_playwright

class WebComponentsScraper:
    """Scrape Web Components using slots"""
    
    def scrape_slotted_content(self, url: str) -> List[Dict]:
        """Extract slotted content from Web Components"""
        with sync_playwright() as p:
            browser = p.chromium.launch(headless=True)
            page = browser.new_page()
            page.goto(url)
            
            data = page.evaluate("""
                () => {
                    const components = [];
                    
                    document.querySelectorAll('custom-card, product-card').forEach(component => {
                        const shadowRoot = component.shadowRoot;
                        
                        if (shadowRoot) {
                            const componentData = {
                                tagName: component.tagName,
                                shadowContent: {},
                                slottedContent: {}
                            };
                            
                            // Get shadow DOM content
                            shadowRoot.querySelectorAll('.title, .description').forEach(el => {
                                componentData.shadowContent[el.className] = el.textContent;
                            });
                            
                            // Get slotted content
                            const slots = shadowRoot.querySelectorAll('slot');
                            slots.forEach(slot => {
                                const name = slot.name || 'default';
                                const assigned = slot.assignedNodes();
                                
                                componentData.slottedContent[name] = assigned.map(node => ({
                                    text: node.textContent,
                                    nodeType: node.nodeType
                                }));
                            });
                            
                            components.push(componentData);
                        }
                    });
                    
                    return components;
                }
            """)
            
            browser.close()
            return data
```

## WebSocket Data Capture

Real-time applications use WebSockets for live data. Capturing this requires monitoring WebSocket traffic.

### Basic WebSocket Capture

```python
from playwright.sync_api import sync_playwright, WebSocket
import json
from datetime import datetime
from typing import List, Dict, Callable

class WebSocketScraper:
    """Capture WebSocket messages during scraping"""
    
    def __init__(self):
        self.messages: List[Dict] = []
    
    def scrape_with_ws_capture(self, url: str, duration_seconds: int = 30,
                               message_filter: Callable = None) -> Dict:
        """
        Scrape page while capturing WebSocket traffic
        
        Args:
            url: URL to scrape
            duration_seconds: How long to capture
            message_filter: Optional function to filter messages
        """
        with sync_playwright() as p:
            browser = p.chromium.launch(headless=True)
            context = browser.new_context()
            page = context.new_page()
            
            # Listen for WebSocket connections
            page.on('websocket', self._handle_websocket)
            
            # Navigate to page
            page.goto(url)
            
            # Wait for specified duration
            page.wait_for_timeout(duration_seconds * 1000)
            
            context.close()
            browser.close()
        
        # Filter messages if filter provided
        messages = self.messages
        if message_filter:
            messages = [m for m in messages if message_filter(m)]
        
        return {
            'url': url,
            'duration': duration_seconds,
            'total_messages': len(self.messages),
            'messages': messages
        }
    
    def _handle_websocket(self, ws: WebSocket):
        """Handle WebSocket connection"""
        logger.info(f"WebSocket connected: {ws.url}")
        
        # Listen for messages
        ws.on('framereceived', lambda payload: self._on_message(ws.url, 'received', payload))
        ws.on('framesent', lambda payload: self._on_message(ws.url, 'sent', payload))
        
        ws.on('close', lambda: logger.info(f"WebSocket closed: {ws.url}"))
    
    def _on_message(self, ws_url: str, direction: str, payload: str):
        """Process WebSocket message"""
        try:
            # Try to parse as JSON
            data = json.loads(payload)
            
            self.messages.append({
                'timestamp': datetime.now().isoformat(),
                'ws_url': ws_url,
                'direction': direction,
                'type': 'json',
                'data': data
            })
        except json.JSONDecodeError:
            # Store as text
            self.messages.append({
                'timestamp': datetime.now().isoformat(),
                'ws_url': ws_url,
                'direction': direction,
                'type': 'text',
                'data': payload
            })

# Usage
scraper = WebSocketScraper()
result = scraper.scrape_with_ws_capture('wss://stream.example.com', duration_seconds=60)

# Filter for price updates
price_updates = [
    msg for msg in result['messages']
    if msg['direction'] == 'received'
    and msg['type'] == 'json'
    and 'price' in str(msg['data']).lower()
]
```

## Browser Pool Management

Running multiple browser instances efficiently requires proper pool management.

### Simple Browser Pool

```python
from playwright.sync_api import sync_playwright, Browser
from queue import Queue, Empty
from threading import Lock
import threading

class SimpleBrowserPool:
    """Simple thread-safe browser pool"""
    
    def __init__(self, pool_size: int = 5, headless: bool = True):
        self.pool_size = pool_size
        self.headless = headless
        self.browsers = Queue(maxsize=pool_size)
        self.playwright = sync_playwright().start()
        self.lock = Lock()
        
        # Initialize pool
        self._initialize_pool()
    
    def _initialize_pool(self):
        """Create initial browser instances"""
        for _ in range(self.pool_size):
            browser = self.playwright.chromium.launch(headless=self.headless)
            self.browsers.put(browser)
    
    def get_browser(self, timeout: int = 30) -> Browser:
        """Get browser from pool"""
        return self.browsers.get(timeout=timeout)
    
    def return_browser(self, browser: Browser):
        """Return browser to pool"""
        self.browsers.put(browser)
    
    def close_all(self):
        """Close all browsers"""
        while not self.browsers.empty():
            try:
                browser = self.browsers.get_nowait()
                browser.close()
            except Empty:
                break
        self.playwright.stop()

# Threaded usage example
pool = SimpleBrowserPool(pool_size=5)

def scrape_url(url):
    """Scrape URL using pool browser"""
    browser = pool.get_browser()
    
    try:
        page = browser.new_page()
        page.goto(url, timeout=30000)
        content = page.content()
        page.close()
        return content
    finally:
        pool.return_browser(browser)
```

### Production Browser Pool

```python
from playwright.sync_api import sync_playwright, Browser
from dataclasses import dataclass, field
from datetime import datetime, timedelta
from typing import Optional, Dict
from queue import Queue
from threading import Lock, Thread
import time
import logging

logger = logging.getLogger(__name__)

@dataclass
class BrowserInstance:
    """Browser instance with metadata"""
    browser: Browser
    created_at: datetime = field(default_factory=datetime.now)
    request_count: int = 0
    error_count: int = 0
    last_used: Optional[datetime] = None
    is_healthy: bool = True

class ProductionBrowserPool:
    """Production-grade browser pool with health monitoring"""
    
    def __init__(self, pool_size: int = 5, max_requests_per_browser: int = 100,
                 max_browser_age_hours: int = 1, health_check_interval: int = 60):
        self.pool_size = pool_size
        self.max_requests_per_browser = max_requests_per_browser
        self.max_browser_age = timedelta(hours=max_browser_age_hours)
        self.health_check_interval = health_check_interval
        
        self.browsers: Queue = Queue(maxsize=pool_size)
        self.playwright = sync_playwright().start()
        self.lock = Lock()
        self.is_running = True
        
        self._initialize_pool()
        self._start_health_monitor()
    
    def _initialize_pool(self):
        """Create initial browser instances"""
        logger.info(f"Initializing browser pool with {self.pool_size} browsers")
        
        for i in range(self.pool_size):
            browser = self._create_browser()
            self.browsers.put(BrowserInstance(browser=browser))
            logger.info(f"Browser {i+1}/{self.pool_size} created")
    
    def _create_browser(self) -> Browser:
        """Create new browser instance with anti-detection"""
        return self.playwright.chromium.launch(
            headless=True,
            args=[
                '--disable-blink-features=AutomationControlled',
                '--disable-dev-shm-usage',
                '--no-sandbox'
            ]
        )
    
    def get_browser(self, timeout: int = 30) -> BrowserInstance:
        """Get healthy browser from pool"""
        start_time = time.time()
        
        while time.time() - start_time < timeout:
            try:
                browser_instance = self.browsers.get(timeout=1)
                
                # Check if browser needs rotation
                if self._should_rotate_browser(browser_instance):
                    logger.info("Rotating browser due to age or request count")
                    self._close_browser(browser_instance)
                    browser_instance = BrowserInstance(browser=self._create_browser())
                
                # Update stats
                browser_instance.request_count += 1
                browser_instance.last_used = datetime.now()
                
                return browser_instance
                
            except Empty:
                continue
        
        raise TimeoutError("No browsers available in pool")
    
    def return_browser(self, browser_instance: BrowserInstance):
        """Return browser to pool"""
        if self.is_running and browser_instance.is_healthy:
            self.browsers.put(browser_instance)
    
    def report_error(self, browser_instance: BrowserInstance):
        """Report browser error"""
        browser_instance.error_count += 1
        
        if browser_instance.error_count >= 3:
            logger.warning("Browser has too many errors, recreating")
            self._close_browser(browser_instance)
    
    def _should_rotate_browser(self, browser_instance: BrowserInstance) -> bool:
        """Check if browser should be rotated"""
        age = datetime.now() - browser_instance.created_at
        
        if age > self.max_browser_age:
            return True
        
        if browser_instance.request_count >= self.max_requests_per_browser:
            return True
        
        return False
    
    def _close_browser(self, browser_instance: BrowserInstance):
        """Safely close browser"""
        try:
            browser_instance.browser.close()
        except:
            pass
    
    def _start_health_monitor(self):
        """Start health monitoring thread"""
        def monitor():
            while self.is_running:
                time.sleep(self.health_check_interval)
                self._health_check()
        
        thread = Thread(target=monitor, daemon=True)
        thread.start()
    
    def _health_check(self):
        """Perform health check"""
        current_size = self.browsers.qsize()
        logger.info(f"Health check: Pool size {current_size}/{self.pool_size}")
        
        # Replenish if needed
        while current_size < self.pool_size:
            with self.lock:
                if self.browsers.qsize() < self.pool_size:
                    browser_instance = BrowserInstance(browser=self._create_browser())
                    self.browsers.put(browser_instance)
                    logger.info("Added browser to pool during health check")
            current_size = self.browsers.qsize()
    
    def close(self):
        """Close all browsers and cleanup"""
        logger.info("Closing browser pool")
        self.is_running = False
        
        while not self.browsers.empty():
            try:
                browser_instance = self.browsers.get_nowait()
                self._close_browser(browser_instance)
            except:
                break
        
        self.playwright.stop()
        logger.info("Browser pool closed")
```

## Performance Optimization

Browser automation is resource-intensive. Optimization is critical for production.

### Resource Blocking

```python
from playwright.sync_api import sync_playwright, Route, Request

def create_optimized_page(browser):
    """Create page with unnecessary resources blocked"""
    context = browser.new_context()
    page = context.new_page()
    
    # Block resource types that slow down scraping
    def block_resources(route: Route, request: Request):
        resource_type = request.resource_type
        
        # Block images, fonts, media, stylesheets
        if resource_type in ['image', 'font', 'media', 'stylesheet']:
            route.abort()
            return
        
        # Block analytics and tracking
        blocked_domains = [
            'google-analytics.com',
            'googletagmanager.com',
            'facebook.com/tr',
            'doubleclick.net',
            'googleadservices.com',
            'googlesyndication.com'
        ]
        
        url = request.url
        if any(domain in url for domain in blocked_domains):
            route.abort()
            return
        
        route.continue_()
    
    page.route('**/*', block_resources)
    
    return page
```

### Memory Management

```python
import psutil
import os

class MemoryManagedScraper:
    """Scraper with memory monitoring"""
    
    def __init__(self, max_memory_mb: int = 2000):
        self.max_memory_mb = max_memory_mb
        self.process = psutil.Process(os.getpid())
        self.request_count = 0
        self.restart_interval = 50
    
    def get_memory_usage(self) -> float:
        """Get current memory usage in MB"""
        return self.process.memory_info().rss / 1024 / 1024
    
    def should_restart_browser(self, browser, page) -> bool:
        """Check if browser should be restarted"""
        self.request_count += 1
        
        # Restart after interval
        if self.request_count >= self.restart_interval:
            return True
        
        # Restart if memory limit reached
        current_memory = self.get_memory_usage()
        if current_memory > self.max_memory_mb:
            logger.warning(f"Memory limit reached ({current_memory:.0f}MB), restarting browser")
            return True
        
        return False
```

## Complete Production Example

Here's a comprehensive production-ready scraper combining all techniques:

```python
from playwright.sync_api import sync_playwright
from typing import List, Dict, Optional
from dataclasses import dataclass
from datetime import datetime
import json

@dataclass
class ScrapedResult:
    """Scraping result structure"""
    url: str
    title: str
    items: List[Dict]
    scraped_at: str
    success: bool
    error: Optional[str] = None

class ProductionJSScraper:
    """Production-ready JavaScript site scraper"""
    
    def __init__(self, headless: bool = True, proxy: str = None):
        self.headless = headless
        self.proxy = proxy
        self.playwright = None
        self.browser = None
    
    def __enter__(self):
        self.playwright = sync_playwright().start()
        
        launch_options = {
            'headless': self.headless,
            'args': [
                '--disable-blink-features=AutomationControlled',
                '--disable-dev-shm-usage',
                '--no-sandbox'
            ]
        }
        
        self.browser = self.playwright.chromium.launch(**launch_options)
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.browser:
            self.browser.close()
        if self.playwright:
            self.playwright.stop()
    
    def scrape_infinite_scroll(self, url: str, max_items: int = 100) -> ScrapedResult:
        """Scrape SPA with infinite scroll"""
        context = self.browser.new_context(
            viewport={'width': 1920, 'height': 1080}
        )
        
        page = context.new_page()
        
        # Block unnecessary resources
        page.route('**/*', lambda route, request: 
            route.abort() if request.resource_type in ['image', 'font', 'media']
            else route.continue_()
        )
        
        try:
            page.goto(url, wait_until='networkidle', timeout=30000)
            page.wait_for_selector('.product-item', timeout=10000)
            
            items = self._extract_with_infinite_scroll(page, max_items)
            title = page.title()
            
            return ScrapedResult(
                url=url,
                title=title,
                items=items,
                scraped_at=datetime.now().isoformat(),
                success=True
            )
            
        except Exception as e:
            return ScrapedResult(
                url=url,
                title='',
                items=[],
                scraped_at=datetime.now().isoformat(),
                success=False,
                error=str(e)
            )
        finally:
            context.close()
    
    def _extract_with_infinite_scroll(self, page, max_items: int) -> List[Dict]:
        """Extract items with infinite scroll handling"""
        all_items = []
        seen_ids = set()
        scroll_count = 0
        max_scrolls = 50
        
        while len(all_items) < max_items and scroll_count < max_scrolls:
            items = page.evaluate("""
                () => {
                    const items = [];
                    document.querySelectorAll('.product-item').forEach(item => {
                        items.push({
                            id: item.getAttribute('data-id'),
                            name: item.querySelector('.product-name')?.textContent,
                            price: item.querySelector('.price')?.textContent,
                            url: item.querySelector('a')?.href
                        });
                    });
                    return items;
                }
            """)
            
            new_items = [item for item in items if item['id'] and item['id'] not in seen_ids]
            
            if not new_items:
                scroll_count += 1
                if scroll_count >= 3:
                    break
            else:
                all_items.extend(new_items)
                seen_ids.update(item['id'] for item in new_items)
            
            page.evaluate('window.scrollTo(0, document.body.scrollHeight)')
            page.wait_for_timeout(2000)
            scroll_count += 1
        
        return all_items[:max_items]

# Usage
with ProductionJSScraper(headless=True) as scraper:
    result = scraper.scrape_infinite_scroll('https://example.com/products', max_items=100)
    
    if result.success:
        with open('scraped_data.json', 'w') as f:
            json.dump({
                'url': result.url,
                'title': result.title,
                'items': result.items,
                'scraped_at': result.scraped_at
            }, f, indent=2)
```

## Summary

JavaScript-heavy site scraping requires sophisticated browser automation:

1. **Browser Automation Tools**: Use Playwright for modern, multi-browser support with superior auto-waiting
2. **Stealth Configuration**: Implement anti-detection measures including proper user agents, viewports, and fingerprint randomization
3. **SPA Patterns**: Master network idle waiting, API interception, and element state monitoring
4. **Infinite Scroll**: Handle pagination through scroll-and-extract loops with deduplication
5. **Shadow DOM**: Use pierce selectors or JavaScript evaluation to access encapsulated content
6. **WebSocket Capture**: Monitor WebSocket connections for real-time data sources
7. **Browser Pools**: Manage multiple browser instances with health monitoring and rotation
8. **Performance Optimization**: Block unnecessary resources, manage memory, and reuse contexts

The key to successful JavaScript scraping is understanding how modern web applications work and adapting your approach to match their behavior patterns. With proper tools and techniques, even the most complex SPAs can be scraped reliably at production scale.