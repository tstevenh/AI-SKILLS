# Chapter 4: JavaScript-Rendered Content

## Table of Contents
1. [Introduction to JavaScript-Rendered Content](#introduction-to-javascript-rendered-content)
2. [Understanding the Problem](#understanding-the-problem)
3. [Tools Overview](#tools-overview)
4. [Selenium WebDriver](#selenium-webdriver)
5. [Playwright](#playwright)
6. [Puppeteer](#puppeteer)
7. [Scrapy with Splash](#scrapy-with-splash)
8. [Reverse Engineering APIs](#reverse-engineering-apis)
9. [Handling AJAX Requests](#handling-ajax-requests)
10. [Waiting Strategies](#waiting-strategies)
11. [Performance Optimization](#performance-optimization)
12. [Real-World Examples](#real-world-examples)
13. [Best Practices](#best-practices)

---

## Introduction to JavaScript-Rendered Content

Modern web applications increasingly rely on JavaScript to render content dynamically. When you request a webpage, the server often returns a minimal HTML shell that contains JavaScript code. This JavaScript then executes in the browser to fetch and display the actual content. This approach powers single-page applications (SPAs), infinite scroll feeds, dynamic forms, and interactive dashboards.

For web scrapers, this creates a fundamental challenge. Traditional HTTP requests return the initial HTML before JavaScript execution, meaning much of the content you see in a browser is missing. This chapter explores techniques and tools for scraping JavaScript-rendered content effectively.

### Why JavaScript Rendering Exists

JavaScript rendering serves several purposes:

1. **Improved User Experience** - Content loads progressively, making pages feel faster
2. **Reduced Server Load** - Initial page loads are smaller; data fetches happen on demand
3. **Dynamic Content** - Real-time updates, personalized content, and interactive features
4. **API-First Architecture** - Frontend and backend separation enables mobile apps and third-party integrations
5. **SEO Optimization** - Modern frameworks support server-side rendering for crawlers while keeping dynamic features for users

### The Scraping Challenge

Consider this scenario:

```python
import requests
from bs4 import BeautifulSoup

# Request a React-based e-commerce site
url = 'https://modern-shop.example.com/products'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# Try to find products
products = soup.find_all('div', class_='product-card')
print(f"Found {len(products)} products")  # Output: Found 0 products
```

The server response contains:

```html
<!DOCTYPE html>
<html>
<head>
    <script src="/app.bundle.js"></script>
</head>
<body>
    <div id="root"></div>
    <script>
        ReactDOM.render(<App />, document.getElementById('root'));
    </script>
</body>
</html>
```

The actual product data is loaded by JavaScript after the initial page load. Your scraper needs to either:
1. Execute the JavaScript to render the content
2. Intercept the API calls the JavaScript makes
3. Find an alternative data source

---

## Understanding the Problem

### How JavaScript Rendering Works

When you visit a JavaScript-heavy website:

1. **Initial Request** - Browser requests HTML from server
2. **HTML Download** - Server returns HTML shell with JavaScript references
3. **Resource Loading** - Browser downloads JavaScript, CSS, and other resources
4. **JavaScript Execution** - Browser executes JavaScript code
5. **Data Fetching** - JavaScript makes API calls to get content
6. **DOM Manipulation** - JavaScript renders content into the page
7. **User Interaction** - JavaScript handles clicks, scrolls, and form submissions

### Detecting JavaScript-Rendered Content

Before choosing a strategy, determine if a site uses JavaScript rendering:

**Method 1: Compare view-source vs. rendered page**
```python
import requests

url = 'https://example.com'

# Get source HTML
response = requests.get(url)
source_html = response.text

# Search for content in source
if 'specific-content' in source_html:
    print("Content is in initial HTML")
else:
    print("Content may be JavaScript-rendered")
```

**Method 2: Check for common JavaScript frameworks**
```python
framework_indicators = {
    'React': ['react', 'reactroot', '__react'],
    'Vue': ['vue', '__vue__', 'data-v-'],
    'Angular': ['ng-', '_ngcontent', 'angular'],
    'Next.js': ['__NEXT_DATA__'],
    'Nuxt.js': ['__nuxt', '__NUXT__'],
}

for framework, indicators in framework_indicators.items():
    for indicator in indicators:
        if indicator in source_html.lower():
            print(f"Detected: {framework}")
            break
```

**Method 3: Network analysis**
- Open browser DevTools (F12)
- Go to Network tab
- Reload page
- Look for XHR/Fetch requests that return JSON data

### Types of JavaScript Rendering

**Client-Side Rendering (CSR)**
- Server sends minimal HTML
- JavaScript fetches data and renders everything
- Examples: React SPA, Vue SPA

**Server-Side Rendering (SSR)**
- Server renders initial HTML with content
- JavaScript hydrates the page for interactivity
- Examples: Next.js, Nuxt.js with SSR enabled

**Static Site Generation (SSG)**
- HTML pre-rendered at build time
- JavaScript adds interactivity
- Examples: Gatsby, Next.js static export

**Incremental Static Regeneration (ISR)**
- Combination of SSG with periodic revalidation
- Content served statically, updated in background

---

## Tools Overview

### Browser Automation Tools

| Tool | Best For | Pros | Cons |
|------|----------|------|------|
| Selenium | Legacy support, multi-browser | Mature, wide browser support | Slower, resource intensive |
| Playwright | Modern web apps, testing | Fast, auto-waits, multiple browsers | Newer, smaller community |
| Puppeteer | Chrome-specific scraping | Fast, full Chrome API | Chrome-only (mostly) |

### Hybrid Approaches

| Tool | Best For | Pros | Cons |
|------|----------|------|------|
| Splash | Scrapy integration | Lightweight, Lua scripts | Less powerful than full browsers |
| Playwright + Scrapy | Production scraping | Best of both worlds | More complex setup |

### API Interception

- **Direct API calls** - Bypass browser entirely
- **Network interception** - Capture requests browser makes
- **Reverse engineering** - Understand and replicate API calls

---

## Selenium WebDriver

Selenium is the veteran of browser automation. It supports multiple browsers and programming languages, making it ideal for cross-browser testing and legacy scraping tasks.

### Installation

```bash
pip install selenium webdriver-manager
```

### Basic Usage

```python
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Setup Chrome options
chrome_options = Options()
chrome_options.add_argument('--headless')  # Run without GUI
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')

# Initialize driver
driver = webdriver.Chrome(
    service=Service(ChromeDriverManager().install()),
    options=chrome_options
)

# Navigate to page
driver.get('https://example.com')

# Wait for element to load
wait = WebDriverWait(driver, 10)
element = wait.until(
    EC.presence_of_element_located((By.CLASS_NAME, 'product-card'))
)

# Extract data
products = driver.find_elements(By.CLASS_NAME, 'product-card')
for product in products:
    title = product.find_element(By.TAG_NAME, 'h2').text
    price = product.find_element(By.CLASS_NAME, 'price').text
    print(f"{title}: {price}")

# Cleanup
driver.quit()
```

### Handling Dynamic Content

**Waiting for elements:**
```python
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

wait = WebDriverWait(driver, 10)

# Wait for element to be present
element = wait.until(EC.presence_of_element_located((By.ID, 'content')))

# Wait for element to be clickable
button = wait.until(EC.element_to_be_clickable((By.ID, 'load-more')))

# Wait for element to be visible
visible = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'results')))
```

**Handling infinite scroll:**
```python
def scroll_to_bottom(driver, pause_time=2):
    """Scroll to bottom of page to trigger lazy loading"""
    last_height = driver.execute_script('return document.body.scrollHeight')
    
    while True:
        # Scroll down
        driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')
        
        # Wait for content to load
        time.sleep(pause_time)
        
        # Calculate new scroll height
        new_height = driver.execute_script('return document.body.scrollHeight')
        
        if new_height == last_height:
            break
        
        last_height = new_height
```

**Clicking and interacting:**
```python
# Click a button
button = driver.find_element(By.ID, 'load-more')
button.click()

# Fill a form
search_box = driver.find_element(By.NAME, 'q')
search_box.send_keys('search term')
search_box.submit()

# Select from dropdown
from selenium.webdriver.support.ui import Select
select = Select(driver.find_element(By.ID, 'category'))
select.select_by_visible_text('Electronics')
```

### Advanced Selenium Techniques

**Taking screenshots:**
```python
# Full page screenshot
driver.save_screenshot('page.png')

# Element screenshot
element = driver.find_element(By.CLASS_NAME, 'product')
element.screenshot('product.png')
```

**Executing JavaScript:**
```python
# Execute custom JavaScript
driver.execute_script('window.scrollTo(0, 500);')

# Return values from JavaScript
title = driver.execute_script('return document.title;')

# Modify page
driver.execute_script("document.body.style.backgroundColor = 'red';")
```

**Handling cookies and sessions:**
```python
# Get cookies
cookies = driver.get_cookies()

# Add cookie
driver.add_cookie({'name': 'session', 'value': 'abc123'})

# Delete cookie
driver.delete_cookie('session')
```

**Working with frames and iframes:**
```python
# Switch to iframe
driver.switch_to.frame('frame-name')
driver.switch_to.frame(0)  # By index
driver.switch_to.frame(driver.find_element(By.TAG_NAME, 'iframe'))

# Switch back to main content
driver.switch_to.default_content()
```

**Handling alerts and popups:**
```python
# Accept alert
alert = driver.switch_to.alert
alert.accept()

# Dismiss alert
alert.dismiss()

# Send text to prompt
alert.send_keys('text')
```

### Selenium Best Practices

```python
from selenium.webdriver.remote.remote_connection import LOGGER
import logging

# Reduce Selenium logging
LOGGER.setLevel(logging.WARNING)

class BaseSeleniumScraper:
    def __init__(self, headless=True):
        self.options = Options()
        if headless:
            self.options.add_argument('--headless')
        self.options.add_argument('--no-sandbox')
        self.options.add_argument('--disable-dev-shm-usage')
        self.options.add_argument('--disable-gpu')
        self.options.add_argument('--window-size=1920,1080')
        self.options.add_argument('--user-agent=Mozilla/5.0...')
        
        self.driver = None
    
    def __enter__(self):
        self.driver = webdriver.Chrome(
            service=Service(ChromeDriverManager().install()),
            options=self.options
        )
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.driver:
            self.driver.quit()
    
    def get(self, url, wait_for=None, timeout=10):
        self.driver.get(url)
        if wait_for:
            WebDriverWait(self.driver, timeout).until(
                EC.presence_of_element_located(wait_for)
            )
        return self.driver.page_source

# Usage
with BaseSeleniumScraper() as scraper:
    html = scraper.get(
        'https://example.com',
        wait_for=(By.CLASS_NAME, 'content')
    )
```

---

## Playwright

Playwright is Microsoft's modern browser automation library. It's faster than Selenium, has better auto-waiting, and supports multiple browsers (Chromium, Firefox, WebKit) with a consistent API.

### Installation

```bash
pip install playwright
playwright install
```

### Basic Usage

```python
from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    # Launch browser
    browser = p.chromium.launch(headless=True)
    context = browser.new_context(
        viewport={'width': 1920, 'height': 1080},
        user_agent='Mozilla/5.0...'
    )
    page = context.new_page()
    
    # Navigate
    page.goto('https://example.com')
    
    # Wait for element
    page.wait_for_selector('.product-card')
    
    # Extract data
    products = page.query_selector_all('.product-card')
    for product in products:
        title = product.query_selector('h2').inner_text()
        price = product.query_selector('.price').inner_text()
        print(f"{title}: {price}")
    
    # Cleanup
    browser.close()
```

### Playwright's Auto-Waiting

One of Playwright's best features is automatic waiting:

```python
# Playwright automatically waits for element to be actionable
page.click('button#submit')  # Waits for button to be visible and enabled

# Automatically waits for navigation
page.click('a.next-page')  # Waits for navigation to complete

# Fill form with automatic waiting
page.fill('input[name="search"]', 'query')
```

### Advanced Playwright Features

**Network interception:**
```python
# Intercept and modify requests
def handle_route(route, request):
    if request.resource_type == 'image':
        route.abort()  # Block images
    else:
        route.continue_()

page.route('**/*', handle_route)

# Intercept API responses
api_data = []
def handle_response(response):
    if '/api/products' in response.url:
        api_data.append(response.json())

page.on('response', handle_response)
```

**Authentication and state:**
```python
# Save authentication state
context = browser.new_context()
page = context.new_page()
page.goto('https://example.com/login')
page.fill('input[name="username"]', 'user')
page.fill('input[name="password"]', 'pass')
page.click('button[type="submit"]')

# Save storage state
context.storage_state(path='auth.json')

# Later, restore state
context = browser.new_context(storage_state='auth.json')
```

**Screenshots and PDFs:**
```python
# Screenshot
page.screenshot(path='page.png', full_page=True)

# Element screenshot
element = page.query_selector('.product')
element.screenshot(path='product.png')

# PDF (Chromium only)
page.pdf(path='page.pdf')
```

**Mobile emulation:**
```python
iphone = p.devices['iPhone 13']
browser = p.chromium.launch()
context = browser.new_context(**iphone)
page = context.new_page()
page.goto('https://example.com')
```

**Parallel execution:**
```python
from playwright.async_api import async_playwright
import asyncio

async def scrape_url(context, url):
    page = await context.new_page()
    await page.goto(url)
    content = await page.content()
    await page.close()
    return content

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        context = await browser.new_context()
        
        urls = ['https://example.com/1', 'https://example.com/2']
        results = await asyncio.gather(*[
            scrape_url(context, url) for url in urls
        ])
        
        await browser.close()

asyncio.run(main())
```

### Playwright vs Selenium

```python
# Selenium - more verbose, manual waiting
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get('https://example.com')
wait = WebDriverWait(driver, 10)
element = wait.until(EC.element_to_be_clickable((By.ID, 'submit')))
element.click()

# Playwright - auto-waiting, cleaner
from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page()
    page.goto('https://example.com')
    page.click('#submit')  # Auto-waits
    browser.close()
```

---

## Puppeteer

Puppeteer is a Node.js library for controlling Chrome/Chromium. While it's not Python-native, it's worth mentioning for Python developers working in mixed environments.

### Using Puppeteer from Python

```python
# Using pyppeteer (unofficial Python port)
from pyppeteer import launch
import asyncio

async def main():
    browser = await launch(headless=True)
    page = await browser.newPage()
    
    await page.goto('https://example.com')
    await page.waitForSelector('.product')
    
    products = await page.querySelectorAll('.product')
    for product in products:
        title = await page.evaluate('el => el.textContent', product)
        print(title)
    
    await browser.close()

asyncio.run(main())
```

**Note:** Pyppeteer is less maintained than Playwright. For Python projects, Playwright is generally preferred.

---

## Scrapy with Splash

Splash is a lightweight, headless web browser specifically designed for web scraping. It integrates well with Scrapy.

### Setting Up Splash

```bash
# Run Splash with Docker
docker run -p 8050:8050 scrapinghub/splash
```

### Using Splash with Scrapy

```python
import scrapy
from scrapy_splash import SplashRequest

class JSSpider(scrapy.Spider):
    name = 'js_spider'
    
    def start_requests(self):
        yield SplashRequest(
            'https://example.com',
            callback=self.parse,
            args={'wait': 2}  # Wait 2 seconds for JS to execute
        )
    
    def parse(self, response):
        # Response contains rendered HTML
        products = response.css('.product-card')
        for product in products:
            yield {
                'title': product.css('h2::text').get(),
                'price': product.css('.price::text').get(),
            }
```

### Splash Lua Scripts

For more control, use Lua scripts:

```lua
function main(splash, args)
    -- Go to page
    splash:go(args.url)
    
    -- Wait for element
    splash:wait_for_selector(".product-list")
    
    -- Scroll to load more content
    for i=1,5 do
        splash:runjs("window.scrollTo(0, document.body.scrollHeight)")
        splash:wait(1)
    end
    
    -- Return HTML
    return splash:html()
end
```

```python
script = """
function main(splash, args)
    splash:go(args.url)
    splash:wait_for_selector(".product-list")
    return splash:html()
end
"""

yield SplashRequest(
    url,
    callback=self.parse,
    endpoint='execute',
    args={'lua_source': script}
)
```

---

## Reverse Engineering APIs

Often, the most efficient approach is to bypass the browser entirely and call the APIs that power the JavaScript.

### Finding API Endpoints

1. **Browser DevTools Network Tab**
   - Open DevTools (F12)
   - Go to Network tab
   - Filter by XHR/Fetch
   - Trigger the action (click, scroll)
   - Examine the request

2. **Looking at page source**
   ```javascript
   // Look for window.__INITIAL_STATE__ or similar
   window.__INITIAL_STATE__ = {"products": [...]}
   ```

3. **Analyzing JavaScript bundles**
   - Search for `fetch(` or `axios.get(` patterns
   - Look for API base URLs

### Example: Extracting from Initial State

```python
import requests
import re
import json

url = 'https://shop.example.com'
response = requests.get(url)

# Look for initial state
match = re.search(r'window\.__INITIAL_STATE__\s*=\s*({.+?});', response.text)
if match:
    data = json.loads(match.group(1))
    products = data['products']
```

### Example: Direct API Call

```python
import requests

# Found by analyzing network requests
api_url = 'https://api.example.com/v1/products'

headers = {
    'Accept': 'application/json',
    'X-Requested-With': 'XMLHttpRequest',
    'User-Agent': 'Mozilla/5.0...'
}

response = requests.get(api_url, headers=headers)
data = response.json()

for product in data['products']:
    print(product['name'], product['price'])
```

### Handling Authentication

```python
# Session-based
session = requests.Session()
session.get('https://example.com/login')
session.post('https://example.com/login', data={
    'username': 'user',
    'password': 'pass'
})

# Token-based
response = requests.post('https://api.example.com/auth', json={
    'username': 'user',
    'password': 'pass'
})
token = response.json()['token']

headers = {'Authorization': f'Bearer {token}'}
products = requests.get('https://api.example.com/products', headers=headers)
```

---

## Handling AJAX Requests

### Waiting for AJAX Completion

```python
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Wait for specific element that AJAX loads
wait = WebDriverWait(driver, 10)
wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'loaded-content')))

# Or wait for jQuery AJAX to complete (if jQuery is used)
wait.until(lambda d: d.execute_script('return jQuery.active == 0'))
```

### Intercepting AJAX with Playwright

```python
from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page()
    
    # Store API responses
    api_responses = []
    
    def handle_response(response):
        if 'api' in response.url:
            api_responses.append({
                'url': response.url,
                'data': response.json()
            })
    
    page.on('response', handle_response)
    
    page.goto('https://example.com')
    page.click('button.load-data')
    
    # API responses now contain the data
    print(api_responses)
    
    browser.close()
```

---

## Waiting Strategies

### Implicit Waits (Selenium)

```python
driver.implicitly_wait(10)  # Wait up to 10 seconds for elements
```

### Explicit Waits (Recommended)

```python
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

wait = WebDriverWait(driver, 10)

# Wait for element to exist
element = wait.until(EC.presence_of_element_located((By.ID, 'content')))

# Wait for element to be visible
element = wait.until(EC.visibility_of_element_located((By.ID, 'content')))

# Wait for element to be clickable
element = wait.until(EC.element_to_be_clickable((By.ID, 'button')))

# Wait for text to appear
element = wait.until(EC.text_to_be_present_in_element((By.ID, 'status'), 'Ready'))

# Custom condition
def custom_condition(driver):
    return driver.execute_script('return document.readyState') == 'complete'

wait.until(custom_condition)
```

### Common Expected Conditions

```python
# Element selection strategies
EC.presence_of_element_located((By.ID, 'id'))
EC.visibility_of_element_located((By.CLASS_NAME, 'class'))
EC.element_to_be_clickable((By.CSS_SELECTOR, '.button'))
EC.text_to_be_present_in_element((By.TAG_NAME, 'h1'), 'Welcome')
EC.title_contains('Page Title')
EC.url_contains('/products')
EC.number_of_windows_to_be(2)
EC.alert_is_present()
```

### Playwright's Built-in Waiting

```python
# Playwright automatically waits
page.click('button')  # Waits for button to be visible and enabled
page.fill('input', 'text')  # Waits for input to be ready

# Explicit waits when needed
page.wait_for_selector('.content')
page.wait_for_load_state('networkidle')  # Wait for network to be idle
page.wait_for_function('() => window.loaded === true')
```

---

## Performance Optimization

### Reducing Resource Usage

```python
# Block unnecessary resources
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_experimental_option('prefs', {
    'profile.managed_default_content_settings.images': 2,  # Block images
    'profile.default_content_setting_values.notifications': 2,
})

# Disable CSS (if not needed)
options.add_experimental_option('prefs', {
    'profile.managed_default_content_settings.stylesheets': 2,
})
```

```python
# Playwright - block resources
page.route('**/*.{png,jpg,jpeg,gif,svg}', lambda route: route.abort())
page.route('**/*.{css,woff,woff2}', lambda route: route.abort())
```

### Parallel Processing

```python
from concurrent.futures import ThreadPoolExecutor
from selenium import webdriver

def scrape_url(url):
    driver = webdriver.Chrome()
    try:
        driver.get(url)
        return driver.page_source
    finally:
        driver.quit()

urls = ['https://example.com/1', 'https://example.com/2', ...]

with ThreadPoolExecutor(max_workers=4) as executor:
    results = executor.map(scrape_url, urls)
```

### Reusing Browser Instances

```python
# Don't create new browser for each URL
browser = webdriver.Chrome()

try:
    for url in urls:
        browser.get(url)
        data = extract_data(browser.page_source)
        save(data)
finally:
    browser.quit()
```

### Headless vs Headful

```python
# Headless - faster, less resource usage
options.add_argument('--headless')

# Headful - useful for debugging
# Remove --headless flag
```

---

## Real-World Examples

### Example 1: Scraping an E-commerce SPA

```python
from playwright.sync_api import sync_playwright

def scrape_ecommerce(url):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        context = browser.new_context()
        page = context.new_page()
        
        page.goto(url)
        
        # Wait for products to load
        page.wait_for_selector('.product-grid')
        
        # Handle infinite scroll
        last_count = 0
        while True:
            products = page.query_selector_all('.product-card')
            if len(products) == last_count:
                break
            
            last_count = len(products)
            page.evaluate('window.scrollTo(0, document.body.scrollHeight)')
            page.wait_for_timeout(2000)
        
        # Extract data
        results = []
        for product in page.query_selector_all('.product-card'):
            results.append({
                'name': product.query_selector('.name').inner_text(),
                'price': product.query_selector('.price').inner_text(),
                'image': product.query_selector('img').get_attribute('src'),
            })
        
        browser.close()
        return results
```

### Example 2: Scraping a React Application

```python
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def scrape_react_app(url):
    driver = webdriver.Chrome()
    driver.get(url)
    
    # Wait for React to render
    wait = WebDriverWait(driver, 10)
    wait.until(EC.presence_of_element_located((By.ID, 'root')))
    
    # Wait for data to load
    wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'user-card')))
    
    # Extract from React-rendered content
    users = driver.find_elements(By.CLASS_NAME, 'user-card')
    data = []
    for user in users:
        data.append({
            'name': user.find_element(By.CLASS_NAME, 'name').text,
            'email': user.find_element(By.CLASS_NAME, 'email').text,
        })
    
    driver.quit()
    return data
```

### Example 3: Intercepting GraphQL Queries

```python
from playwright.sync_api import sync_playwright
import json

def intercept_graphql(url):
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        
        graphql_data = []
        
        def handle_response(response):
            if 'graphql' in response.url:
                try:
                    data = response.json()
                    graphql_data.append(data)
                except:
                    pass
        
        page.on('response', handle_response)
        page.goto(url)
        
        # Trigger GraphQL query by clicking
        page.click('button.load-users')
        page.wait_for_timeout(2000)
        
        browser.close()
        return graphql_data
```

---

## Best Practices

### 1. Prefer API Calls Over Browser Automation

Always check if you can call the API directly before using a browser:

```python
# Good: Direct API call
response = requests.get('https://api.example.com/products')
data = response.json()

# Slower but necessary: Browser automation
# Only use when API isn't available or requires complex authentication
```

### 2. Use Appropriate Waiting Strategies

```python
# Don't use time.sleep()
time.sleep(5)  # Bad - wastes time or fails if slow

# Do use explicit waits
wait.until(EC.presence_of_element_located((By.ID, 'content')))
```

### 3. Clean Up Resources

```python
# Always close browsers
from contextlib import contextmanager

@contextmanager
def managed_browser():
    driver = webdriver.Chrome()
    try:
        yield driver
    finally:
        driver.quit()

with managed_browser() as driver:
    driver.get('https://example.com')
```

### 4. Handle Failures Gracefully

```python
from selenium.common.exceptions import TimeoutException, NoSuchElementException

def safe_find(driver, by, value, default=None):
    try:
        return driver.find_element(by, value)
    except NoSuchElementException:
        return default

def safe_scrape(url):
    try:
        driver.get(url)
        element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, 'content'))
        )
        return element.text
    except TimeoutException:
        print(f"Timeout loading {url}")
        return None
```

### 5. Respect Website Resources

```python
import time
import random

# Add random delays
time.sleep(random.uniform(1, 3))

# Don't run too many parallel browsers
max_workers = 4

# Cache results when possible
from functools import lru_cache
```

### 6. Monitor and Log

```python
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def scrape_with_logging(url):
    logger.info(f"Starting scrape of {url}")
    try:
        driver.get(url)
        logger.info(f"Page loaded: {driver.title}")
        # ... scraping logic
        logger.info(f"Successfully scraped {url}")
    except Exception as e:
        logger.error(f"Failed to scrape {url}: {e}")
        raise
```

### 7. Test Your Selectors

```python
def test_selectors():
    html = """
    <div class="product">
        <h2>Test Product</h2>
        <span class="price">$10.00</span>
    </div>
    """
    
    from bs4 import BeautifulSoup
    soup = BeautifulSoup(html, 'lxml')
    
    # Test your selectors
    assert soup.select_one('.product h2').text == 'Test Product'
    assert soup.select_one('.price').text == '$10.00'
    
    print("All selector tests passed!")
```

---

## Conclusion

JavaScript-rendered content presents unique challenges for web scrapers, but with the right tools and techniques, you can extract data from even the most dynamic websites.

**Key takeaways:**
- Always check if direct API access is possible before using browser automation
- Playwright is generally preferred for new projects due to its auto-waiting and performance
- Selenium remains valuable for cross-browser testing and legacy support
- Splash is ideal for Scrapy-based workflows
- Proper waiting strategies are crucial for reliable scraping
- Always clean up browser resources to prevent memory leaks

In the next chapter, we'll explore advanced anti-detection techniques to avoid being blocked while scraping JavaScript-heavy sites.
