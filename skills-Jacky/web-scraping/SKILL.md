# Web Scraping - Comprehensive AI Agent Skill Guide

## Table of Contents

1. [Introduction to Web Scraping](#introduction-to-web-scraping)
2. [Web Scraping Fundamentals](#web-scraping-fundamentals)
3. [HTTP Protocol and Web Communication](#http-protocol-and-web-communication)
4. [HTML Parsing and DOM Navigation](#html-parsing-and-dom-navigation)
5. [CSS Selectors - Complete Guide](#css-selectors-complete-guide)
6. [XPath - Advanced Selection Techniques](#xpath-advanced-selection-techniques)
7. [Python Web Scraping Stack](#python-web-scraping-stack)
8. [Node.js Web Scraping Ecosystem](#nodejs-web-scraping-ecosystem)
9. [Headless Browser Scraping](#headless-browser-scraping)
10. [Anti-Bot Detection Systems](#anti-bot-detection-systems)
11. [Proxy Management and Rotation](#proxy-management-and-rotation)
12. [Browser Fingerprinting and Evasion](#browser-fingerprinting-and-evasion)
13. [JavaScript Rendering Challenges](#javascript-rendering-challenges)
14. [Structured Data Extraction](#structured-data-extraction)
15. [API Reverse Engineering](#api-reverse-engineering)
16. [Data Processing and Normalization](#data-processing-and-normalization)
17. [Storage and Output Formats](#storage-and-output-formats)
18. [Scraping Automation and Scheduling](#scraping-automation-and-scheduling)
19. [Monitoring and Maintenance](#monitoring-and-maintenance)
20. [Legal and Ethical Considerations](#legal-and-ethical-considerations)
21. [Site-Specific Scraping Patterns](#site-specific-scraping-patterns)
22. [Scraping at Scale](#scraping-at-scale)
23. [Cloud Scraping Services](#cloud-scraping-services)
24. [Advanced Techniques and Optimization](#advanced-techniques-and-optimization)
25. [Troubleshooting and Debugging](#troubleshooting-and-debugging)

---

## Introduction to Web Scraping

### What is Web Scraping?

Web scraping, also known as web harvesting or web data extraction, is the automated process of extracting data from websites. Unlike manual data collection, web scraping uses software tools to systematically browse the web, extract specific information, and store it in a structured format for analysis, research, or other purposes.

At its core, web scraping mimics human browsing behavior but does so at scale and speed impossible for manual collection. When you visit a website, your browser sends HTTP requests to servers, receives HTML/CSS/JavaScript responses, renders the page, and displays content. Web scraping automates this entire process, programmatically requesting pages, parsing the received data, extracting relevant information, and storing it for later use.

### Why Web Scraping Matters

In the modern data-driven economy, web scraping has become an essential skill for businesses, researchers, and developers. The web contains vast amounts of publicly accessible data that can provide competitive intelligence, market insights, research data, and business opportunities. Web scraping enables:

**Business Intelligence and Market Research**: Companies scrape competitor websites to monitor pricing, product offerings, marketing strategies, and market positioning. E-commerce businesses track competitor prices in real-time to optimize their own pricing strategies. Market researchers collect product reviews, customer feedback, and sentiment data to understand market trends and consumer preferences.

**Academic and Scientific Research**: Researchers scrape social media platforms, news sites, and online forums to study public opinion, social trends, and information dissemination patterns. Scientists collect environmental data, weather information, and public datasets for analysis. Linguists and NLP researchers build corpora from web content for language analysis and machine learning training.

**Lead Generation and Sales**: Businesses scrape business directories, professional networks, and industry-specific websites to identify potential customers, partners, or job candidates. Real estate agents monitor property listings across multiple platforms. Recruiters aggregate job postings and candidate profiles.

**Content Aggregation and Monitoring**: News aggregators collect articles from thousands of sources to provide comprehensive news coverage. Price comparison websites scrape e-commerce platforms to help consumers find the best deals. Brand monitoring services track mentions of companies and products across the web to manage reputation and respond to customer feedback.

**Financial Analysis and Trading**: Financial analysts scrape earnings reports, SEC filings, and financial news to inform investment decisions. Algorithmic traders collect real-time market data, social media sentiment, and news to execute automated trading strategies. Credit analysts gather business information from multiple sources to assess creditworthiness.

**Machine Learning and AI**: Data scientists scrape web content to build training datasets for machine learning models. Computer vision researchers collect images for image recognition systems. Natural language processing applications require vast amounts of text data that can be collected through web scraping.

### The Web Scraping Landscape

The web scraping landscape has evolved significantly over the past two decades. Early web scraping was relatively straightforward - websites were primarily static HTML pages, and simple tools could easily extract data. Today's web is vastly more complex, presenting both challenges and opportunities for web scrapers.

**Modern Web Challenges**:

The shift from server-side rendered static pages to client-side rendered Single Page Applications (SPAs) has made scraping more complex. Many modern websites use JavaScript frameworks like React, Vue, or Angular that dynamically generate content in the browser, requiring scrapers to execute JavaScript to access data.

Anti-bot technologies have become increasingly sophisticated. Companies invest heavily in protecting their data from scrapers using various detection mechanisms including fingerprinting, behavioral analysis, CAPTCHA challenges, and rate limiting.

Website structures change frequently as companies update designs, refactor code, and deploy new features. Scrapers must be robust and adaptable to handle these changes without breaking.

Legal and ethical considerations have gained prominence. Website terms of service, data protection regulations like GDPR, and legal precedents around scraping continue to evolve, requiring scrapers to navigate complex legal landscapes.

**Modern Web Opportunities**:

Despite these challenges, modern tools and techniques have made sophisticated scraping more accessible. Open-source libraries like Scrapy, Puppeteer, and Playwright provide powerful frameworks for building robust scrapers. Cloud computing enables large-scale distributed scraping operations. Machine learning techniques help with intelligent data extraction and pattern recognition.

APIs and structured data formats like JSON-LD, OpenGraph, and Schema.org make data extraction easier for many sites. GraphQL APIs often expose more data than traditional REST APIs, and mobile apps frequently use APIs that are easier to access than scraping rendered HTML.

### Types of Web Scraping

**Static Web Scraping**: This involves scraping websites where content is rendered server-side and delivered as complete HTML. These sites don't require JavaScript execution to access data. Static scraping is faster, more efficient, and easier to implement using simple HTTP clients and HTML parsers.

**Dynamic Web Scraping**: Modern websites often rely on JavaScript to load and render content dynamically. Dynamic scraping requires tools that can execute JavaScript, wait for content to load, and interact with dynamic elements. This typically involves headless browsers or browser automation tools.

**API Scraping**: Many websites load data through API calls rather than embedding it in HTML. API scraping involves intercepting and replicating these API requests to access data directly in structured formats like JSON. This approach is often more efficient and reliable than parsing HTML.

**Hybrid Scraping**: Real-world scraping projects often combine multiple approaches. You might use API scraping when available, fall back to dynamic scraping for JavaScript-heavy sections, and use static scraping for simple content pages.

### The Scraping Workflow

A typical web scraping project follows a systematic workflow:

**1. Planning and Analysis**: Before writing any code, analyze the target website to understand its structure, identify data sources, and plan your approach. Use browser developer tools to inspect HTML structure, monitor network requests, and identify patterns.

**2. Tool Selection**: Choose appropriate tools based on the website's characteristics. Simple static sites might only need basic HTTP clients and HTML parsers. Complex JavaScript-heavy sites may require full browser automation. Consider factors like speed requirements, scale, and maintenance overhead.

**3. Development**: Build your scraper incrementally, starting with basic data extraction and gradually adding features like pagination handling, error recovery, and data validation. Test thoroughly with small samples before scaling up.

**4. Anti-Bot Evasion**: Implement necessary evasion techniques like proxy rotation, user-agent randomization, and timing delays. Monitor for detection and adjust strategies as needed.

**5. Data Validation and Cleaning**: Ensure extracted data is accurate, complete, and properly formatted. Handle missing values, normalize formats, and validate against expected schemas.

**6. Storage and Export**: Store data in appropriate formats for your use case - databases for large-scale projects, CSV/JSON for analysis, or direct integration with downstream systems.

**7. Monitoring and Maintenance**: Continuously monitor scraper performance, detect when websites change structure, and update scrapers accordingly. Implement alerting for failures and anomalies.

### The Ethics of Web Scraping

Web scraping occupies a complex ethical and legal space. While much web content is publicly accessible, access doesn't automatically imply permission to scrape. Ethical scraping requires balancing business needs with respect for website owners, user privacy, and legal compliance.

**Respect robots.txt**: This file, placed in a website's root directory, specifies which parts of the site should not be accessed by automated tools. While not legally binding in all jurisdictions, respecting robots.txt is considered an ethical best practice.

**Rate Limiting**: Don't overwhelm servers with requests. Implement delays between requests to avoid degrading service for human users. A good rule of thumb is to mimic human browsing patterns.

**Identify Yourself**: Use descriptive user agents that identify your bot and provide contact information. This allows website owners to reach out if your scraper causes issues.

**Respect Privacy**: Be especially careful with personal data. Consider whether the data you're collecting could harm individuals if exposed or misused. Comply with data protection regulations like GDPR.

**Check Terms of Service**: Many websites explicitly prohibit scraping in their terms of service. While the legal enforceability of such terms varies by jurisdiction, violating them can lead to legal action.

**Consider Alternatives**: Before scraping, check if the website offers an official API or data export functionality. Many sites provide legitimate data access methods that are preferable to scraping.

**Add Value**: Use scraped data to create something valuable rather than simply copying and republishing content. Fair use doctrines in many countries protect transformative uses of data.

### Setting Up Your Scraping Environment

Before diving into specific techniques, let's establish a proper development environment for web scraping.

**Python Environment Setup**:

Python is the most popular language for web scraping, offering a rich ecosystem of libraries and tools. Start by setting up a proper Python environment:

```bash
# Create a virtual environment
python3 -m venv scraping-env
source scraping-env/bin/activate  # On Windows: scraping-env\Scripts\activate

# Install essential packages
pip install requests beautifulsoup4 lxml scrapy selenium playwright
pip install pandas numpy # For data processing
pip install fake-useragent python-dotenv  # For utilities
```

**Node.js Environment Setup**:

Node.js offers excellent scraping tools, particularly for JavaScript-heavy sites:

```bash
# Initialize a new Node.js project
npm init -y

# Install essential packages
npm install puppeteer playwright axios cheerio
npm install puppeteer-extra puppeteer-extra-plugin-stealth
npm install @crawlee/puppeteer  # For advanced crawling
```

**Browser Setup**:

For headless browser scraping, you'll need browser binaries:

```bash
# Playwright automatically installs browsers
npx playwright install

# Or install specific browsers
npx playwright install chromium
npx playwright install firefox
npx playwright install webkit
```

**Development Tools**:

Essential tools for web scraping development:

- **Browser DevTools**: Chrome/Firefox developer tools for inspecting pages, monitoring network traffic, and testing selectors
- **Postman/Insomnia**: For testing API endpoints and inspecting requests
- **Charles Proxy/Fiddler**: For intercepting and analyzing HTTP traffic
- **SQLite Browser**: For examining and querying scraped data stored in SQLite
- **Regex101**: Online tool for testing and debugging regular expressions
- **SelectorGadget**: Browser extension for easily generating CSS selectors

---

## Web Scraping Fundamentals

### Understanding the Web Architecture

To become proficient at web scraping, you must understand how the web works at a fundamental level. The modern web is built on a client-server architecture using standardized protocols and data formats.

**The Client-Server Model**:

When you access a website, your browser (the client) communicates with a remote server hosting the website. This communication happens through a series of requests and responses:

1. **DNS Resolution**: Your browser first converts the domain name (e.g., example.com) to an IP address using the Domain Name System (DNS). This lookup happens transparently, but it's crucial - without it, your browser wouldn't know which server to contact.

2. **TCP Connection**: Once the IP address is known, your browser establishes a TCP (Transmission Control Protocol) connection with the server. For HTTPS sites, this includes a TLS handshake to establish encrypted communication.

3. **HTTP Request**: Your browser sends an HTTP request to the server, specifying what resource it wants (the URL path), what methods it supports, what format it prefers, and other metadata in headers.

4. **Server Processing**: The server receives the request, processes it (which might involve database queries, business logic, authentication checks, etc.), and prepares a response.

5. **HTTP Response**: The server sends back an HTTP response containing the requested resource (usually HTML, but could be JSON, images, etc.), along with metadata in response headers indicating content type, caching rules, cookies, and more.

6. **Rendering**: The browser receives the response, parses the HTML, requests additional resources (CSS, JavaScript, images), executes JavaScript, and finally renders the page for the user.

Web scraping replicates these steps programmatically. Understanding each step helps you troubleshoot issues, optimize performance, and evade detection.

**HTTP Protocol Deep Dive**:

HTTP (Hypertext Transfer Protocol) is the foundation of web communication. Modern web scraping requires deep understanding of HTTP/1.1 and HTTP/2 protocols.

**HTTP Methods**:

- **GET**: Retrieves data from the server. This is the most common method for web scraping. GET requests should be idempotent (multiple identical requests have the same effect as a single request) and should not modify server state.

- **POST**: Submits data to the server. Many forms, login pages, and search functionality use POST requests. POST requests can modify server state and are not idempotent. When scraping, you often need to replicate POST requests to submit forms or access data.

- **HEAD**: Identical to GET but only retrieves headers, not the body. Useful for checking if a resource exists or has been modified without downloading the entire content.

- **PUT, DELETE, PATCH**: These methods modify resources on the server. They're rarely needed for scraping but understanding them helps when reverse-engineering APIs.

**HTTP Headers**:

Headers are key-value pairs that provide metadata about the request or response. Understanding and manipulating headers is crucial for successful scraping:

**Request Headers**:

- **User-Agent**: Identifies the client software making the request. Websites often block requests with bot-like user agents. Set this to match a real browser: `Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36`

- **Accept**: Specifies what content types the client can handle: `text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8`

- **Accept-Language**: Indicates preferred languages: `en-US,en;q=0.9`

- **Accept-Encoding**: Specifies supported compression formats: `gzip, deflate, br`

- **Referer**: Indicates the page that linked to the current request. Many sites check this to prevent direct deep-linking or to track navigation paths.

- **Cookie**: Contains cookies previously set by the server, used for session management and tracking.

- **Authorization**: Contains credentials for HTTP authentication.

- **Origin**: Indicates the origin of the request, used in CORS (Cross-Origin Resource Sharing) checks.

- **X-Requested-With**: Often set to `XMLHttpRequest` for AJAX requests. Some sites check this header to distinguish between regular page loads and API calls.

**Response Headers**:

- **Content-Type**: Indicates the type of content in the response: `text/html; charset=UTF-8` or `application/json`

- **Content-Length**: Size of the response body in bytes

- **Set-Cookie**: Instructs the client to store cookies for future requests

- **Location**: Used in redirects to specify the new URL

- **Cache-Control**: Specifies caching policies

- **Content-Encoding**: Indicates compression used (gzip, br, etc.)

- **X-Frame-Options, X-Content-Type-Options, Content-Security-Policy**: Security headers that can affect scraping

**HTTP Status Codes**:

Understanding status codes helps you handle different scenarios appropriately:

**Success Codes (2xx)**:
- **200 OK**: Request succeeded, response contains requested data
- **201 Created**: Resource was successfully created
- **204 No Content**: Request succeeded but no content to return

**Redirection Codes (3xx)**:
- **301 Moved Permanently**: Resource has permanently moved to a new URL
- **302 Found**: Temporary redirect
- **304 Not Modified**: Resource hasn't changed since last request (used with caching)

**Client Error Codes (4xx)**:
- **400 Bad Request**: Server couldn't understand the request
- **401 Unauthorized**: Authentication required
- **403 Forbidden**: Server understood request but refuses to authorize it
- **404 Not Found**: Requested resource doesn't exist
- **429 Too Many Requests**: Rate limit exceeded

**Server Error Codes (5xx)**:
- **500 Internal Server Error**: Generic server error
- **502 Bad Gateway**: Invalid response from upstream server
- **503 Service Unavailable**: Server temporarily unable to handle request
- **504 Gateway Timeout**: Upstream server didn't respond in time

### Cookies and Session Management

Cookies are small pieces of data that servers send to clients and clients include in subsequent requests. They're fundamental to web application state management and critical for scraping authenticated or personalized content.

**How Cookies Work**:

When a server wants to set a cookie, it includes a `Set-Cookie` header in its response:

```
Set-Cookie: sessionId=abc123; Path=/; Domain=.example.com; Expires=Wed, 09 Jun 2027 10:18:14 GMT; Secure; HttpOnly
```

This header tells the browser to store a cookie named `sessionId` with value `abc123`. The additional parameters specify:

- **Path**: Cookie only applies to certain URL paths
- **Domain**: Which domain(s) can receive this cookie
- **Expires/Max-Age**: When the cookie should be deleted
- **Secure**: Cookie should only be sent over HTTPS
- **HttpOnly**: Cookie cannot be accessed by JavaScript (security measure)
- **SameSite**: Controls when cookies are sent in cross-site requests (CSRF protection)

On subsequent requests to matching URLs, the browser automatically includes these cookies in a `Cookie` header:

```
Cookie: sessionId=abc123; userId=42; preferences=darkMode
```

**Cookie Types**:

- **Session Cookies**: Temporary cookies deleted when the browser closes. These don't have an `Expires` or `Max-Age` attribute.

- **Persistent Cookies**: Remain until expiry date or explicit deletion. Used for "remember me" functionality, user preferences, tracking.

- **First-Party Cookies**: Set by the domain you're visiting. Used for authentication, preferences, shopping carts.

- **Third-Party Cookies**: Set by domains other than the one you're visiting. Used for advertising, analytics, social media integration.

**Scraping with Cookies**:

Many websites require cookies for proper functionality:

**Authentication Sessions**: After logging in, the server sets a session cookie that authenticates subsequent requests. You must maintain this cookie throughout your scraping session.

**Personalization**: Some sites customize content based on cookies (location preferences, language settings, etc.). You may need to set specific cookies to access desired content.

**Bot Detection**: Some anti-bot systems set challenge cookies that must be included in subsequent requests.

When scraping, you have several options for handling cookies:

**1. Automatic Cookie Management**: Most HTTP libraries automatically handle cookies:

```python
import requests

session = requests.Session()  # Creates a session that persists cookies
response = session.get('https://example.com/login')  # Cookies automatically stored
response = session.get('https://example.com/protected')  # Cookies automatically sent
```

**2. Manual Cookie Management**: Sometimes you need explicit control:

```python
cookies = {'sessionId': 'abc123', 'userId': '42'}
response = requests.get('https://example.com', cookies=cookies)
```

**3. Cookie Extraction and Reuse**: You can extract cookies from a browser session and use them in your scraper:

```python
# Get cookies from response
cookies = response.cookies.get_dict()

# Save cookies for later use
import pickle
with open('cookies.pkl', 'wb') as f:
    pickle.dump(cookies, f)

# Load and use cookies
with open('cookies.pkl', 'rb') as f:
    cookies = pickle.load(f)
response = requests.get('https://example.com', cookies=cookies)
```

### Understanding HTML Structure

HTML (HyperText Markup Language) is the backbone of web pages. To scrape effectively, you must understand HTML structure intimately.

**HTML Basics**:

HTML documents are composed of nested elements represented by tags:

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Page Title</title>
</head>
<body>
    <header>
        <h1>Main Heading</h1>
        <nav>
            <ul>
                <li><a href="/">Home</a></li>
                <li><a href="/about">About</a></li>
            </ul>
        </nav>
    </header>
    <main>
        <article>
            <h2>Article Title</h2>
            <p>Article content goes here.</p>
        </article>
    </main>
    <footer>
        <p>&copy; 2027 Example Corp</p>
    </footer>
</body>
</html>
```

**Key Concepts**:

- **Elements**: Building blocks of HTML, defined by opening and closing tags: `<p>content</p>`
- **Attributes**: Provide additional information about elements: `<a href="url" class="link" id="nav-home">`
- **Nesting**: Elements contain other elements, creating a tree structure (the DOM)
- **Semantic HTML**: Modern HTML uses semantic tags that describe content purpose: `<article>`, `<nav>`, `<aside>`, `<section>`

**Common HTML Elements for Scraping**:

- **Links**: `<a href="url">Link text</a>` - Extract URLs for crawling, text for navigation
- **Images**: `<img src="url" alt="description">` - Extract image URLs and metadata
- **Tables**: `<table>`, `<tr>`, `<td>` - Structured data perfect for scraping
- **Lists**: `<ul>`, `<ol>`, `<li>` - Organized data items
- **Forms**: `<form>`, `<input>`, `<select>` - Understand for submitting searches/logins
- **Divs and Spans**: `<div>`, `<span>` - Generic containers often styled with CSS classes
- **Data Containers**: `<article>`, `<section>` - Modern semantic containers

**HTML Attributes Important for Scraping**:

- **class**: CSS class names for styling, often used as selectors: `<div class="product-card">`
- **id**: Unique identifier for an element: `<div id="main-content">`
- **data-*** Custom data attributes often contain useful information: `<div data-product-id="12345" data-price="29.99">`
- **href**: Link destination: `<a href="/products/laptop">`
- **src**: Resource URL for images, scripts: `<img src="/images/product.jpg">`
- **title**: Tooltip text, sometimes contains extra information
- **aria-***: Accessibility attributes that sometimes expose data: `<button aria-label="Add to cart">`

**The Document Object Model (DOM)**:

When browsers parse HTML, they create an internal representation called the DOM (Document Object Model). The DOM is a tree structure where each HTML element becomes a node. Understanding the DOM is crucial for scraping because:

1. **Navigation**: You navigate the DOM tree to find elements (parent, children, siblings)
2. **Selection**: CSS selectors and XPath expressions query the DOM
3. **Dynamic Content**: JavaScript modifies the DOM, and you must work with the modified version

**DOM Tree Example**:

```
Document
└── html
    ├── head
    │   ├── title
    │   │   └── "Page Title"
    │   └── meta
    └── body
        ├── header
        │   ├── h1
        │   │   └── "Main Heading"
        │   └── nav
        │       └── ul
        │           ├── li
        │           │   └── a (href="/")
        │           └── li
        │               └── a (href="/about")
        └── main
            └── article
                ├── h2
                └── p
```

Understanding this tree structure helps you write effective selectors and navigate between related elements.

### Inspecting Websites for Scraping

Before writing any code, you must thoroughly inspect your target website. Modern browser developer tools provide everything you need.

**Browser DevTools - The Essential Scraping Tool**:

Chrome DevTools (or Firefox Developer Tools) is your primary analysis tool. Access it by right-clicking on a page and selecting "Inspect" or pressing F12.

**Elements Tab**:

The Elements tab shows the HTML structure of the page. Use it to:

- **Inspect Elements**: Right-click any page element and select "Inspect" to jump directly to its HTML
- **Explore Structure**: Navigate the DOM tree to understand how data is organized
- **Find Selectors**: Right-click an element and "Copy > Copy selector" or "Copy XPath" to get selectors
- **Check Dynamic Content**: See if content is in the initial HTML or loaded dynamically
- **Examine Attributes**: Look for data attributes, IDs, and classes that contain useful information

**Network Tab**:

The Network tab shows all HTTP requests and responses. This is invaluable for:

- **API Discovery**: Identify API endpoints that load data
- **Request Headers**: See what headers the browser sends
- **Request Payload**: Examine POST data, form submissions, and JSON payloads
- **Response Analysis**: View response headers, status codes, and content
- **Resource Timing**: Understand load order and identify bottlenecks
- **Filter Requests**: Filter by type (XHR for AJAX, Doc for documents, etc.)

**Network Tab Workflow**:

1. Open DevTools and switch to Network tab
2. Refresh the page or perform the action you want to scrape (search, login, pagination)
3. Look for XHR/Fetch requests - these often contain JSON data that's easier to parse than HTML
4. Click on requests to view headers, payload, and response
5. Right-click and "Copy as cURL" or "Copy as fetch" to replicate the request in your scraper

**Console Tab**:

The Console allows you to execute JavaScript in the page context:

- **Test Selectors**: Run `document.querySelector()` or `document.querySelectorAll()` to test CSS selectors
- **Extract Data**: Write quick JavaScript to extract data and verify your approach
- **Debug Issues**: Check for JavaScript errors that might affect page rendering
- **Access Variables**: Examine global JavaScript variables that might contain useful data

**Application/Storage Tab**:

This tab shows stored data:

- **Cookies**: View all cookies, their values, expiration, and attributes
- **Local Storage/Session Storage**: JavaScript-accessible storage that might contain data
- **IndexedDB**: Client-side database that some sites use to store data

**Sources Tab**:

View and debug JavaScript code:

- **Examine Scripts**: Read JavaScript source code to understand how the site works
- **Set Breakpoints**: Pause execution to examine variables and logic
- **Search Code**: Find specific functions or API endpoints mentioned in JavaScript

**Performance Tab**:

Analyze page load performance:

- **Understand Load Sequence**: See when different resources load
- **Identify Bottlenecks**: Find slow resources or operations
- **Optimize Scrapers**: Understand what's necessary vs. what you can skip

### URL Structure and Patterns

Understanding URL structure helps you navigate sites and construct queries programmatically.

**URL Anatomy**:

```
https://www.example.com:443/products/search?q=laptop&sort=price&page=2#results
|___| |_________________| |____________| |___| |_________________________| |______|
scheme    domain:port         path      sep          query string          fragment
```

- **Scheme/Protocol**: `https://` or `http://` - use HTTPS when available
- **Domain**: `www.example.com` - the website's address
- **Port**: `:443` - usually omitted (80 for HTTP, 443 for HTTPS)
- **Path**: `/products/search` - identifies the specific resource
- **Query String**: `?q=laptop&sort=price&page=2` - parameters sent to the server
- **Fragment**: `#results` - client-side identifier, not sent to server

**Query String Parameters**:

Query parameters are key-value pairs that pass data to the server:

```
?key1=value1&key2=value2&key3=value3
```

Common patterns in scraping:

- **Search**: `?q=search+term` or `?query=search%20term`
- **Pagination**: `?page=2`, `?offset=20&limit=10`, `?start=20`
- **Sorting**: `?sort=price`, `?order=asc`, `?sortBy=date&direction=desc`
- **Filtering**: `?category=electronics&price_max=1000&brand=apple`
- **Location**: `?city=seattle&state=wa`

**URL Encoding**:

Special characters in URLs must be encoded:
- Space: `%20` or `+`
- `&`: `%26`
- `=`: `%3D`
- `#`: `%23`

Most HTTP libraries handle encoding automatically:

```python
import requests
params = {'q': 'laptop computer', 'price': '< $1000'}
response = requests.get('https://example.com/search', params=params)
# URL becomes: https://example.com/search?q=laptop+computer&price=%3C+%241000
```

**Common URL Patterns in Websites**:

**RESTful URLs**: Clean, hierarchical structure:
```
/products/12345
/users/john-doe/posts
/categories/electronics/laptops
```

**Paginated URLs**:
```
/products?page=2
/search?offset=40&limit=20
/articles/page/3
```

**Filter/Search URLs**:
```
/search?q=laptop&category=electronics&price_min=500&price_max=1500
/listings?location=seattle&bedrooms=2&bathrooms=1
```

**Date-Based URLs**:
```
/archive/2027/02/09
/posts?from=2027-01-01&to=2027-12-31
```

Understanding these patterns helps you:
- Navigate pagination systematically
- Construct search queries programmatically
- Extract data from URLs (like IDs, dates, categories)
- Predict URL structures for pages you haven't seen

### Request/Response Cycle in Detail

Let's examine a complete HTTP transaction to understand what your scraper needs to do:

**1. DNS Resolution**:
```
example.com → 93.184.216.34
```

Your scraper needs to resolve domain names. Most HTTP libraries handle this automatically, but you can specify IP addresses directly if needed (useful for bypassing some protections).

**2. TCP Connection Establishment**:

A three-way handshake establishes the connection:
- Client sends SYN packet
- Server responds with SYN-ACK
- Client sends ACK

For HTTPS, a TLS handshake follows:
- Client sends supported cipher suites
- Server sends certificate
- Client verifies certificate
- Both negotiate encryption keys

This process takes time (100-300ms for distant servers). Connection pooling and keep-alive headers allow reusing connections for multiple requests, significantly improving performance.

**3. HTTP Request**:

```
GET /products/laptop HTTP/1.1
Host: example.com
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
Accept-Language: en-US,en;q=0.9
Accept-Encoding: gzip, deflate, br
Connection: keep-alive
Cookie: sessionId=abc123; userId=42
Referer: https://example.com/
```

**4. Server Processing**:

The server:
- Parses the request
- Authenticates the user (checks session cookie)
- Queries databases
- Executes business logic
- Generates response content
- Applies security headers

**5. HTTP Response**:

```
HTTP/1.1 200 OK
Date: Mon, 09 Feb 2027 23:15:00 GMT
Server: nginx/1.20.0
Content-Type: text/html; charset=UTF-8
Content-Length: 45678
Content-Encoding: gzip
Set-Cookie: lastVisit=2027-02-09; Path=/
Cache-Control: private, max-age=3600
X-Frame-Options: SAMEORIGIN

<!DOCTYPE html>
<html>
...
</html>
```

**6. Response Processing**:

Your scraper must:
- Decompress the response (if gzip/br encoded)
- Parse HTML/JSON
- Extract cookies for future requests
- Follow redirects if needed
- Handle errors gracefully

### Common Scraping Challenges

Even with fundamental knowledge, you'll encounter challenges:

**Challenge 1: Rate Limiting**:

Websites limit request rates to prevent abuse. Symptoms:
- 429 status codes
- Temporary IP bans
- CAPTCHA challenges

Solutions:
- Add delays between requests: `time.sleep(random.uniform(1, 3))`
- Use rotating proxies
- Respect robots.txt crawl-delay directive
- Implement exponential backoff on errors

**Challenge 2: Dynamic Content**:

JavaScript loads content after initial page load. Symptoms:
- Empty elements when parsing HTML
- "Loading..." placeholders
- Content appears in browser but not in scraper

Solutions:
- Use headless browsers (Selenium, Playwright)
- Find and call the underlying API
- Wait for specific elements to appear
- Execute JavaScript in the scraper

**Challenge 3: Pagination**:

Navigating through multiple pages of results. Patterns:
- Sequential page numbers: `/page/1`, `/page/2`
- Offset/limit: `?offset=0&limit=20`, `?offset=20&limit=20`
- Next page URLs in HTML: `<a href="/next-page">`
- Infinite scroll (AJAX loading)

Solutions:
- Extract pagination links from HTML
- Increment page parameters programmatically
- Intercept AJAX requests for infinite scroll
- Look for "total results" to know when to stop

**Challenge 4: Authentication**:

Accessing protected content requires login. Types:
- Form-based authentication (POST to login endpoint)
- OAuth/OAuth2 (redirect-based flow)
- API keys (passed in headers)
- Basic HTTP authentication (username:password)

Solutions:
- Replicate login POST request with correct credentials
- Maintain session cookies after authentication
- Use browser automation for complex auth flows
- Store and reuse authentication tokens

**Challenge 5: Data Extraction Accuracy**:

Getting the exact data you need from complex HTML:
- Similar elements with no unique identifiers
- Inconsistent structure across pages
- Nested data with complex relationships
- Text mixed with HTML tags

Solutions:
- Use multiple selector strategies (ID → class → text content)
- Implement robust selectors that don't break easily
- Validate extracted data
- Use regular expressions for pattern-based extraction
- Normalize and clean data after extraction

### Best Practices for Scraping Fundamentals

**1. Start Small**: Begin with a single page before scaling to thousands. Test thoroughly.

**2. Be Polite**: Respect servers by:
- Adding reasonable delays (1-3 seconds between requests)
- Scraping during off-peak hours when possible
- Using caching to avoid redundant requests
- Identifying your bot with a descriptive user agent

**3. Handle Errors Gracefully**:
```python
import requests
from requests.exceptions import RequestException
import time

def fetch_with_retry(url, max_retries=3):
    for attempt in range(max_retries):
        try:
            response = requests.get(url, timeout=10)
            response.raise_for_status()  # Raise exception for 4xx/5xx
            return response
        except RequestException as e:
            if attempt == max_retries - 1:
                raise
            wait_time = 2 ** attempt  # Exponential backoff
            time.sleep(wait_time)
```

**4. Validate Data**:
```python
def validate_product(product):
    required_fields = ['name', 'price', 'url']
    for field in required_fields:
        if field not in product or not product[field]:
            return False
    
    # Validate price format
    if not isinstance(product['price'], (int, float)):
        return False
    
    # Validate URL format
    if not product['url'].startswith('http'):
        return False
    
    return True
```

**5. Log Everything**:
```python
import logging

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('scraper.log'),
        logging.StreamHandler()
    ]
)

logger = logging.getLogger(__name__)

logger.info(f'Starting scrape of {url}')
logger.warning(f'Received 404 for {url}')
logger.error(f'Failed to parse {url}: {exception}')
```

**6. Respect robots.txt**:
```python
from urllib.robotparser import RobotFileParser

def can_fetch(url, user_agent='*'):
    rp = RobotFileParser()
    rp.set_url(f'{url}/robots.txt')
    rp.read()
    return rp.can_fetch(user_agent, url)

if can_fetch('https://example.com/products'):
    # Proceed with scraping
    pass
else:
    print('Scraping disallowed by robots.txt')
```

---

## HTTP Protocol and Web Communication

### HTTP/1.1 vs HTTP/2 vs HTTP/3

Understanding HTTP protocol versions is crucial for advanced scraping, especially when dealing with modern websites and anti-bot systems.

**HTTP/1.1** (1997-present):

HTTP/1.1 has been the dominant protocol for over two decades. Key characteristics:

- **Text-based Protocol**: Headers and request lines are plain text
- **One Request Per Connection**: Originally, each request required a new TCP connection
- **Keep-Alive**: Connection reuse introduced to reduce overhead
- **Pipelining**: Multiple requests can be sent without waiting for responses (rarely used in practice due to issues)
- **Header Redundancy**: Headers are sent with every request, even if identical to previous requests

For scrapers, HTTP/1.1 is still widely supported and sufficient for most use cases. It's simpler to debug since you can read headers in plain text.

**HTTP/2** (2015-present):

HTTP/2 brought significant performance improvements:

- **Binary Protocol**: More efficient parsing but harder to read/debug
- **Multiplexing**: Multiple requests/responses on a single connection simultaneously
- **Header Compression**: HPACK algorithm reduces redundant header data
- **Server Push**: Servers can proactively send resources
- **Stream Prioritization**: Clients can specify resource importance

For scrapers, HTTP/2 offers:
- Better performance when making many requests
- Reduced connection overhead
- More realistic browser behavior (modern browsers use HTTP/2)

However, some anti-bot systems check for proper HTTP/2 usage. If your scraper uses HTTP/1.1 while browsers use HTTP/2, you may be detected.

**HTTP/3** (2022-present):

HTTP/3 uses QUIC instead of TCP:

- **Built on UDP**: Faster connection establishment
- **Better Performance on Unreliable Networks**: Handles packet loss better
- **Always Encrypted**: TLS 1.3 is mandatory
- **Improved Multiplexing**: No head-of-line blocking

For scrapers, HTTP/3 support is still evolving. Most Python/Node.js libraries don't fully support it yet. However, major websites are adopting it, so future-proof scrapers should consider it.

**Practical Implications for Scraping**:

```python
# HTTP/1.1 scraping (requests library)
import requests
response = requests.get('https://example.com')

# HTTP/2 scraping (httpx library supports HTTP/2)
import httpx
client = httpx.Client(http2=True)
response = client.get('https://example.com')

# Checking protocol version
print(response.http_version)  # HTTP/2, HTTP/1.1, etc.
```

### TLS/SSL and HTTPS

Nearly all modern websites use HTTPS (HTTP over TLS/SSL). Understanding the encryption handshake is important for advanced scraping.

**TLS Handshake Process**:

1. **Client Hello**: Client sends supported TLS versions, cipher suites, and extensions
2. **Server Hello**: Server selects TLS version and cipher suite
3. **Certificate**: Server sends SSL certificate for verification
4. **Key Exchange**: Client and server establish encryption keys
5. **Finished**: Both sides confirm secure connection established

**TLS Fingerprinting**:

Modern anti-bot systems fingerprint TLS handshakes to detect bots. Different browsers and HTTP libraries send different cipher suites, extensions, and TLS versions. If your scraper's TLS fingerprint doesn't match a real browser, you may be detected.

**JA3 Fingerprint**: A hash of TLS parameters that uniquely identifies clients. Many anti-bot systems check JA3 fingerprints.

**Akamai/Cloudflare TLS Fingerprinting**: These services analyze TLS handshakes to identify bots. They check:
- Cipher suite ordering
- TLS extensions and their order
- Elliptic curves
- Compression methods
- ALPN protocols

**Evading TLS Fingerprinting**:

```python
# Using curl_cffi to mimic Chrome's TLS fingerprint
from curl_cffi import requests

response = requests.get('https://example.com', impersonate='chrome110')

# The request will have Chrome's exact TLS fingerprint
```

```javascript
// Using puppeteer (automatically has Chrome's TLS fingerprint)
const puppeteer = require('puppeteer');
const browser = await puppeteer.launch();
const page = await browser.newPage();
await page.goto('https://example.com');
```

**Certificate Verification**:

By default, HTTP libraries verify SSL certificates. Sometimes you need to handle special cases:

```python
import requests

# Disable certificate verification (use with caution!)
response = requests.get('https://example.com', verify=False)

# Use custom CA bundle
response = requests.get('https://example.com', verify='/path/to/ca-bundle.crt')

# Client certificate authentication
response = requests.get('https://example.com', 
                       cert=('/path/to/client.crt', '/path/to/client.key'))
```

### Advanced HTTP Headers

Beyond basic headers, many specialized headers affect scraping:

**Compression Headers**:

```
Accept-Encoding: gzip, deflate, br
Content-Encoding: br
```

- **gzip**: Widely supported, good compression
- **deflate**: Less common
- **br** (Brotli): Best compression, used by modern browsers

Most HTTP libraries automatically decompress responses, but you should include Accept-Encoding to appear browser-like.

**Caching Headers**:

```
Cache-Control: max-age=3600, must-revalidate
ETag: "33a64df551425fcc55e4d42a148795d9f25f89d4"
If-None-Match: "33a64df551425fcc55e4d42a148795d9f25f89d4"
Last-Modified: Mon, 09 Feb 2027 12:00:00 GMT
If-Modified-Since: Mon, 09 Feb 2027 12:00:00 GMT
```

You can implement smart caching to avoid re-downloading unchanged content:

```python
import requests
from datetime import datetime

class CachingScraper:
    def __init__(self):
        self.etags = {}
        self.last_modified = {}
    
    def fetch(self, url):
        headers = {}
        
        # Add conditional headers if we've cached this URL
        if url in self.etags:
            headers['If-None-Match'] = self.etags[url]
        if url in self.last_modified:
            headers['If-Modified-Since'] = self.last_modified[url]
        
        response = requests.get(url, headers=headers)
        
        # 304 means content hasn't changed
        if response.status_code == 304:
            return None  # Use cached data
        
        # Store caching headers for next request
        if 'ETag' in response.headers:
            self.etags[url] = response.headers['ETag']
        if 'Last-Modified' in response.headers:
            self.last_modified[url] = response.headers['Last-Modified']
        
        return response
```

**CORS Headers**:

```
Origin: https://example.com
Access-Control-Allow-Origin: *
Access-Control-Allow-Methods: GET, POST, PUT
Access-Control-Allow-Headers: Content-Type
```

CORS (Cross-Origin Resource Sharing) restricts browser-based API access. However, scrapers aren't bound by CORS since they're not browsers. You can make cross-origin requests freely.

**Security Headers**:

```
Strict-Transport-Security: max-age=31536000; includeSubDomains
X-Frame-Options: SAMEORIGIN
X-Content-Type-Options: nosniff
Content-Security-Policy: default-src 'self'
X-XSS-Protection: 1; mode=block
```

These headers protect against various attacks but rarely affect scrapers directly. However, CSP (Content Security Policy) can affect what content loads on a page, which matters for headless browser scraping.

**Custom Anti-Bot Headers**:

Many sites use custom headers to detect bots:

```
X-Requested-With: XMLHttpRequest  # AJAX requests
X-CSRF-Token: abc123  # CSRF protection
X-API-Key: your-api-key  # API authentication
```

When reverse-engineering API endpoints, you must identify and include these custom headers.

### Connection Management and Pooling

Efficient scrapers reuse connections rather than establishing new ones for each request.

**Connection Pooling in Python**:

```python
import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry

# Create a session with connection pooling
session = requests.Session()

# Configure retry strategy
retry_strategy = Retry(
    total=3,
    status_forcelist=[429, 500, 502, 503, 504],
    method_whitelist=["HEAD", "GET", "OPTIONS"],
    backoff_factor=1  # Wait 1, 2, 4 seconds between retries
)

# Mount adapter with connection pooling
adapter = HTTPAdapter(
    max_retries=retry_strategy,
    pool_connections=10,  # Number of connection pools
    pool_maxsize=20       # Max connections per pool
)

session.mount("http://", adapter)
session.mount("https://", adapter)

# All requests reuse connections
for i in range(100):
    response = session.get(f'https://example.com/page/{i}')
```

**Connection Pooling in Node.js**:

```javascript
const axios = require('axios');
const http = require('http');
const https = require('https');

// Create connection pools
const httpAgent = new http.Agent({ keepAlive: true, maxSockets: 50 });
const httpsAgent = new https.Agent({ keepAlive: true, maxSockets: 50 });

// Use agents for all requests
const client = axios.create({
    httpAgent: httpAgent,
    httpsAgent: httpsAgent
});

// Requests reuse connections
for (let i = 0; i < 100; i++) {
    await client.get(`https://example.com/page/${i}`);
}
```

### Request Timing and Delays

Adding realistic delays prevents detection and respects server resources.

**Simple Delays**:

```python
import time
import random

def scrape_pages(urls):
    for url in urls:
        response = requests.get(url)
        process_response(response)
        
        # Random delay between 1-3 seconds
        time.sleep(random.uniform(1, 3))
```

**Human-Like Timing Patterns**:

Real users don't request pages at constant intervals. Implement variable delays:

```python
import numpy as np

class HumanLikeTiming:
    def __init__(self, mean=2.0, std=0.5):
        self.mean = mean
        self.std = std
    
    def delay(self):
        # Normal distribution around mean
        wait_time = np.random.normal(self.mean, self.std)
        # Ensure positive, with minimum delay
        wait_time = max(0.5, wait_time)
        time.sleep(wait_time)

timer = HumanLikeTiming(mean=2.0, std=0.5)

for url in urls:
    response = requests.get(url)
    process_response(response)
    timer.delay()
```

**Burst Prevention**:

Some anti-bot systems detect burst patterns (many requests in short time). Use token bucket algorithm:

```python
import time

class TokenBucket:
    def __init__(self, rate=10, capacity=10):
        self.rate = rate  # Tokens per second
        self.capacity = capacity
        self.tokens = capacity
        self.last_update = time.time()
    
    def wait_for_token(self):
        while True:
            now = time.time()
            elapsed = now - self.last_update
            
            # Add tokens based on elapsed time
            self.tokens = min(self.capacity, 
                            self.tokens + elapsed * self.rate)
            self.last_update = now
            
            if self.tokens >= 1:
                self.tokens -= 1
                return
            
            # Wait for next token
            time.sleep((1 - self.tokens) / self.rate)

# Allow 10 requests per second max
bucket = TokenBucket(rate=10, capacity=10)

for url in urls:
    bucket.wait_for_token()
    response = requests.get(url)
```

### Handling Redirects

Websites redirect for many reasons. Understanding redirect handling is crucial.

**Redirect Types**:

**301 Moved Permanently**: Resource permanently moved. Update your URLs.

**302 Found / 307 Temporary Redirect**: Temporary move. Don't update URLs.

**303 See Other**: After POST, redirect to GET request.

**307 Temporary Redirect / 308 Permanent Redirect**: Maintain request method (POST stays POST).

**Meta Refresh**: HTML-based redirect: `<meta http-equiv="refresh" content="0;url=https://example.com">`

**JavaScript Redirect**: `window.location.href = 'https://example.com'`

**Handling Redirects in Python**:

```python
# requests follows redirects by default
response = requests.get('https://example.com')
print(response.history)  # List of redirect responses
print(response.url)      # Final URL after redirects

# Disable automatic redirects
response = requests.get('https://example.com', allow_redirects=False)
if response.status_code in (301, 302, 307, 308):
    redirect_url = response.headers['Location']
    # Handle manually
```

**Handling Meta Refresh**:

```python
from bs4 import BeautifulSoup
import re

def extract_meta_refresh(html):
    soup = BeautifulSoup(html, 'lxml')
    meta = soup.find('meta', attrs={'http-equiv': 'refresh'})
    if meta and 'content' in meta.attrs:
        content = meta['content']
        # Parse "0;url=https://example.com"
        match = re.search(r'url=(.*)', content, re.I)
        if match:
            return match.group(1).strip()
    return None

response = requests.get('https://example.com', allow_redirects=False)
redirect_url = extract_meta_refresh(response.text)
if redirect_url:
    response = requests.get(redirect_url)
```

### Session Management

Sessions maintain state across multiple requests, crucial for scraping authenticated content.

**Session Persistence**:

```python
import requests
import pickle

# Create session and login
session = requests.Session()
session.post('https://example.com/login', data={
    'username': 'user',
    'password': 'pass'
})

# Save session for later use
with open('session.pkl', 'wb') as f:
    pickle.dump(session.cookies, f)

# Later, restore session
with open('session.pkl', 'rb') as f:
    cookies = pickle.load(f)

new_session = requests.Session()
new_session.cookies.update(cookies)
response = new_session.get('https://example.com/protected')
```

**Session Validation**:

Sessions expire. Implement validation:

```python
class SessionManager:
    def __init__(self):
        self.session = requests.Session()
        self.authenticated = False
    
    def login(self, username, password):
        response = self.session.post('https://example.com/login', data={
            'username': username,
            'password': password
        })
        self.authenticated = self.check_auth()
        return self.authenticated
    
    def check_auth(self):
        # Try to access protected page
        response = self.session.get('https://example.com/profile')
        # If redirected to login, not authenticated
        return 'login' not in response.url.lower()
    
    def ensure_authenticated(self):
        if not self.authenticated or not self.check_auth():
            # Re-authenticate
            self.login(USERNAME, PASSWORD)
    
    def fetch(self, url):
        self.ensure_authenticated()
        return self.session.get(url)
```

### HTTP Request Methods in Detail

**GET Requests**:

Retrieve data without side effects.

```python
# Simple GET
response = requests.get('https://example.com/api/users')

# GET with query parameters
params = {'page': 2, 'limit': 20, 'sort': 'name'}
response = requests.get('https://example.com/api/users', params=params)
# URL: https://example.com/api/users?page=2&limit=20&sort=name

# GET with custom headers
headers = {
    'User-Agent': 'MyBot/1.0',
    'Accept': 'application/json'
}
response = requests.get('https://example.com/api/users', headers=headers)
```

**POST Requests**:

Submit data, often for forms or API mutations.

```python
# Form-encoded POST
data = {'username': 'user', 'password': 'pass'}
response = requests.post('https://example.com/login', data=data)
# Content-Type: application/x-www-form-urlencoded

# JSON POST
import json
payload = {'name': 'John', 'email': 'john@example.com'}
headers = {'Content-Type': 'application/json'}
response = requests.post('https://example.com/api/users', 
                        data=json.dumps(payload), 
                        headers=headers)

# Or use json parameter (automatically sets Content-Type)
response = requests.post('https://example.com/api/users', json=payload)

# Multipart form data (file uploads)
files = {'file': open('document.pdf', 'rb')}
data = {'description': 'My document'}
response = requests.post('https://example.com/upload', 
                        files=files, 
                        data=data)
```

**PUT/PATCH Requests**:

Update resources.

```python
# PUT - replace entire resource
payload = {'name': 'Jane Doe', 'email': 'jane@example.com'}
response = requests.put('https://example.com/api/users/123', json=payload)

# PATCH - partial update
payload = {'email': 'newemail@example.com'}
response = requests.patch('https://example.com/api/users/123', json=payload)
```

**DELETE Requests**:

Remove resources.

```python
response = requests.delete('https://example.com/api/users/123')
```

**HEAD Requests**:

Get headers without body (useful for checking if resource exists/changed).

```python
response = requests.head('https://example.com/large-file.zip')
content_length = response.headers.get('Content-Length')
last_modified = response.headers.get('Last-Modified')

# Decide whether to download based on headers
if int(content_length) < 100000000:  # Less than 100MB
    response = requests.get('https://example.com/large-file.zip')
```

### Content Negotiation

Websites can serve different content based on client preferences.

**Accept Header**:

```python
# Request JSON
headers = {'Accept': 'application/json'}
response = requests.get('https://example.com/api/data', headers=headers)

# Request XML
headers = {'Accept': 'application/xml'}
response = requests.get('https://example.com/api/data', headers=headers)

# Request HTML (default browser behavior)
headers = {'Accept': 'text/html,application/xhtml+xml'}
response = requests.get('https://example.com', headers=headers)
```

**Accept-Language Header**:

```python
# Request content in Spanish
headers = {'Accept-Language': 'es-ES,es;q=0.9'}
response = requests.get('https://example.com', headers=headers)

# Request multiple languages with preferences
headers = {'Accept-Language': 'en-US,en;q=0.9,fr;q=0.8,de;q=0.7'}
response = requests.get('https://example.com', headers=headers)
```

Some websites detect language from headers and redirect or serve localized content.

### Advanced Timeout Handling

Proper timeout configuration prevents hanging scrapers.

```python
# Simple timeout (seconds)
response = requests.get('https://example.com', timeout=10)

# Separate connect and read timeouts
response = requests.get('https://example.com', timeout=(3, 10))
# 3 seconds to establish connection
# 10 seconds to receive response

# Implement smart timeout handling
import time

def fetch_with_timeout(url, initial_timeout=5, max_timeout=60):
    timeout = initial_timeout
    
    while timeout <= max_timeout:
        try:
            response = requests.get(url, timeout=timeout)
            return response
        except requests.Timeout:
            logging.warning(f'Timeout after {timeout}s, retrying with {timeout*2}s')
            timeout *= 2
    
    raise Exception(f'Failed to fetch {url} within {max_timeout}s')
```

### Handling Different Content Types

Scrapers encounter various content types beyond HTML.

**JSON Responses**:

```python
response = requests.get('https://api.example.com/data')
data = response.json()  # Automatic JSON parsing

# Handle malformed JSON
import json
try:
    data = response.json()
except json.JSONDecodeError:
    logging.error(f'Invalid JSON: {response.text[:200]}')
    data = None
```

**XML Responses**:

```python
import xml.etree.ElementTree as ET

response = requests.get('https://example.com/data.xml')
root = ET.fromstring(response.content)

# Or use lxml for more powerful parsing
from lxml import etree
root = etree.fromstring(response.content)
```

**CSV Responses**:

```python
import csv
import io

response = requests.get('https://example.com/data.csv')
csv_data = csv.DictReader(io.StringIO(response.text))

for row in csv_data:
    print(row['column_name'])
```

**Binary Content (Images, PDFs)**:

```python
response = requests.get('https://example.com/image.jpg')

# Save to file
with open('image.jpg', 'wb') as f:
    f.write(response.content)

# Or process in memory
from PIL import Image
import io
image = Image.open(io.BytesIO(response.content))
```

**Compressed Responses**:

Most libraries automatically decompress, but manual handling:

```python
import gzip
import brotli

response = requests.get('https://example.com', 
                       headers={'Accept-Encoding': 'gzip, br'})

encoding = response.headers.get('Content-Encoding')

if encoding == 'gzip':
    decompressed = gzip.decompress(response.content)
elif encoding == 'br':
    decompressed = brotli.decompress(response.content)
else:
    decompressed = response.content
```

---

## HTML Parsing and DOM Navigation

### Introduction to HTML Parsing

HTML parsing is the process of converting raw HTML text into a structured data format that can be queried and manipulated programmatically. Understanding parsing is fundamental to web scraping success.

**Why Parsing Matters**:

Raw HTML is just a string of text. To extract specific data (product prices, article titles, user reviews), you need to:

1. Parse HTML into a structured tree (DOM)
2. Navigate the tree to find elements of interest
3. Extract data from those elements

**Parsing Approaches**:

**Regular Expressions**: Tempting but dangerous. HTML's nested, context-sensitive structure makes regex unreliable. Only use regex for very simple, controlled cases.

**String Manipulation**: Similarly unreliable. HTML can have inconsistent whitespace, attribute ordering, and nesting that breaks simple string operations.

**Proper HTML Parsers**: The correct approach. Libraries like BeautifulSoup, lxml, and Cheerio understand HTML structure and handle edge cases.

### Python HTML Parsing Libraries

**BeautifulSoup 4**:

BeautifulSoup is the most popular Python HTML parsing library, valued for its ease of use and forgiving parsing.

```python
from bs4 import BeautifulSoup

html = '''
<html>
<body>
    <div class="product">
        <h2 class="title">Laptop Computer</h2>
        <span class="price">$999.99</span>
        <p class="description">High performance laptop</p>
    </div>
</body>
</html>
'''

soup = BeautifulSoup(html, 'lxml')

# Find single element
title = soup.find('h2', class_='title')
print(title.text)  # "Laptop Computer"

# Find all matching elements
products = soup.find_all('div', class_='product')

# CSS selector
price = soup.select_one('.price')
print(price.text)  # "$999.99"

# Get attribute value
link = soup.find('a')
url = link['href'] if link else None
```

**BeautifulSoup Parsers**:

BeautifulSoup supports multiple underlying parsers:

**lxml** (`'lxml'`): Fastest, most features, requires C library
```python
soup = BeautifulSoup(html, 'lxml')
```

**html.parser** (`'html.parser'`): Built-in Python, no dependencies, slower
```python
soup = BeautifulSoup(html, 'html.parser')
```

**html5lib** (`'html5lib'`): Most lenient, handles broken HTML best, slowest
```python
soup = BeautifulSoup(html, 'html5lib')
```

For most scraping, use `'lxml'` for speed. Use `'html5lib'` only for badly broken HTML.

**lxml**:

lxml is a powerful library offering both CSS selectors and XPath support, with excellent performance.

```python
from lxml import html

tree = html.fromstring(html_content)

# XPath selection
titles = tree.xpath('//h2[@class="title"]/text()')

# CSS selection (requires cssselect package)
from lxml.cssselect import CSSSelector
selector = CSSSelector('.product .price')
prices = [el.text for el in selector(tree)]

# Get attribute
links = tree.xpath('//a/@href')
```

**Comparison**: BeautifulSoup vs lxml:

| Feature | BeautifulSoup | lxml |
|---------|---------------|------|
| Ease of Use | Excellent | Good |
| Speed | Moderate | Excellent |
| HTML Handling | Very forgiving | Strict (but has recovery mode) |
| XPath Support | Limited | Full |
| CSS Selectors | Yes | Yes (with cssselect) |
| API Style | Pythonic | Element-tree style |

Recommendation: Start with BeautifulSoup for learning and quick tasks. Use lxml for large-scale, performance-critical scraping.

### DOM Navigation Methods

**Navigating with BeautifulSoup**:

BeautifulSoup provides intuitive navigation methods:

**Downward Navigation** (parent → children):

```python
# Direct children
div = soup.find('div', class_='container')
children = div.children  # Generator of direct children
child_list = list(div.children)

# All descendants
descendants = div.descendants  # Generator of all nested elements

# Specific child by tag
first_p = div.p  # First <p> child
all_ps = div.find_all('p')  # All <p> descendants

# Filtering children
paragraphs = [child for child in div.children if child.name == 'p']
```

**Upward Navigation** (child → parent):

```python
# Direct parent
span = soup.find('span', class_='price')
parent = span.parent

# All ancestors
ancestors = list(span.parents)

# Find specific ancestor
container = span.find_parent('div', class_='container')
```

**Sideways Navigation** (between siblings):

```python
# Next sibling
h2 = soup.find('h2')
next_elem = h2.next_sibling  # May be whitespace NavigableString!
next_tag = h2.find_next_sibling()  # Next tag (skips whitespace)

# Previous sibling
prev_tag = h2.find_previous_sibling()

# All next siblings
all_next = h2.find_next_siblings()

# All previous siblings
all_prev = h2.find_previous_siblings()
```

**Sequential Navigation** (document order):

```python
# Next element in document
next_element = h2.next_element

# All following elements
following = h2.find_all_next()

# Previous element
prev_element = h2.previous_element

# All preceding elements
preceding = h2.find_all_previous()
```

### Finding Elements

**BeautifulSoup Finding Methods**:

**find()** - Find first matching element:

```python
# By tag name
title = soup.find('h1')

# By class
product = soup.find(class_='product')

# By id
header = soup.find(id='main-header')

# By attribute
link = soup.find(attrs={'data-id': '123'})

# By multiple attributes
item = soup.find('div', class_='item', attrs={'data-category': 'electronics'})

# By text content
link = soup.find('a', string='Click here')

# By text pattern (regex)
import re
title = soup.find(string=re.compile(r'laptop', re.I))

# Custom filter function
def has_price_class(tag):
    return tag.has_attr('class') and 'price' in tag['class']

price = soup.find(has_price_class)
```

**find_all()** - Find all matching elements:

```python
# All matching tags
products = soup.find_all('div', class_='product')

# Multiple tag names
headings = soup.find_all(['h1', 'h2', 'h3'])

# Limit results
first_five = soup.find_all('div', class_='product', limit=5)

# Recursive vs direct children
all_divs = soup.find_all('div')  # All divs in document
direct_divs = soup.find_all('div', recursive=False)  # Only direct children
```

**CSS Selectors**:

```python
# select_one() - first match
title = soup.select_one('h2.title')

# select() - all matches
products = soup.select('div.product')

# Complex selectors
prices = soup.select('.product > .price')  # Direct children
links = soup.select('div.product a[href]')  # Has href attribute
featured = soup.select('div.product.featured')  # Multiple classes
```

### Extracting Data from Elements

Once you've found elements, extract their data:

**Text Content**:

```python
element = soup.find('p')

# Get text
text = element.text  # Or element.get_text()

# Get text with custom separator
text = element.get_text(separator=' | ')

# Get text, strip whitespace
text = element.get_text(strip=True)

# Get only direct text (exclude nested elements)
direct_text = element.find(text=True, recursive=False)
```

**Attributes**:

```python
link = soup.find('a')

# Dictionary-style access
url = link['href']
title = link.get('title')  # Returns None if attribute doesn't exist

# Check if attribute exists
if link.has_attr('data-id'):
    item_id = link['data-id']

# Get all attributes
attrs = link.attrs  # Dictionary of all attributes

# Multiple classes (class is a list!)
div = soup.find('div')
classes = div.get('class', [])  # ['product', 'featured']
```

**HTML Content**:

```python
element = soup.find('div')

# Inner HTML (children only)
inner_html = element.decode_contents()

# Outer HTML (includes the element itself)
outer_html = str(element)
# Or: element.prettify() for formatted HTML
```

**Data Attributes**:

```python
# Extract all data-* attributes
element = soup.find('div')
data_attrs = {k: v for k, v in element.attrs.items() if k.startswith('data-')}

# Specific data attribute
product_id = element.get('data-product-id')
price = element.get('data-price')
```

### Handling Malformed HTML

Real-world HTML is often broken. Libraries handle many issues automatically, but you should understand common problems:

**Unclosed Tags**:

```html
<div>
    <p>Paragraph 1
    <p>Paragraph 2
</div>
```

BeautifulSoup automatically closes tags. The parser determines structure:

```python
soup = BeautifulSoup(malformed_html, 'lxml')
# lxml automatically closes <p> tags
```

**Mismatched Tags**:

```html
<div>
    <span>Text</div>
</span>
```

Parsers attempt to correct:

```python
soup = BeautifulSoup(malformed_html, 'html5lib')  # Most forgiving
# html5lib will restructure to valid HTML
```

**Invalid Nesting**:

```html
<p>
    <div>Invalid: block element inside paragraph</div>
</p>
```

Different parsers handle this differently:

```python
# lxml splits the paragraph
soup1 = BeautifulSoup(html, 'lxml')

# html5lib handles according to HTML5 spec
soup2 = BeautifulSoup(html, 'html5lib')
```

**Special Characters and Encoding**:

```python
# Specify encoding explicitly
soup = BeautifulSoup(html, 'lxml', from_encoding='utf-8')

# Let BeautifulSoup detect encoding
soup = BeautifulSoup(html, 'lxml')
print(soup.original_encoding)  # Detected encoding

# Handle encoding errors
html_bytes = response.content
soup = BeautifulSoup(html_bytes, 'lxml', from_encoding='iso-8859-1')
```

### Advanced Parsing Techniques

**Parsing Table Data**:

Tables are common structures for data:

```python
# Simple table parsing
table = soup.find('table')
rows = table.find_all('tr')

data = []
for row in rows:
    cells = row.find_all(['td', 'th'])
    row_data = [cell.get_text(strip=True) for cell in cells]
    data.append(row_data)

# Convert to pandas DataFrame
import pandas as pd
df = pd.DataFrame(data[1:], columns=data[0])  # First row as headers

# Or use pandas directly (handles complex tables)
dfs = pd.read_html(html)  # Returns list of all tables
df = dfs[0]  # First table
```

**Parsing Lists**:

```python
ul = soup.find('ul', class_='items')
items = [li.get_text(strip=True) for li in ul.find_all('li')]

# Ordered lists with data extraction
ol = soup.find('ol')
numbered_items = []
for i, li in enumerate(ol.find_all('li'), 1):
    text = li.get_text(strip=True)
    link = li.find('a')
    url = link['href'] if link else None
    numbered_items.append({
        'number': i,
        'text': text,
        'url': url
    })
```

**Parsing Definition Lists**:

```python
dl = soup.find('dl')
definitions = {}

for dt, dd in zip(dl.find_all('dt'), dl.find_all('dd')):
    term = dt.get_text(strip=True)
    definition = dd.get_text(strip=True)
    definitions[term] = definition
```

**Handling Nested Structures**:

```python
# Extract nested product data
def parse_product(product_div):
    return {
        'name': product_div.find('h2', class_='name').get_text(strip=True),
        'price': product_div.find('span', class_='price').get_text(strip=True),
        'features': [
            li.get_text(strip=True) 
            for li in product_div.find('ul', class_='features').find_all('li')
        ],
        'specs': {
            dt.get_text(strip=True): dd.get_text(strip=True)
            for dt, dd in zip(
                product_div.find_all('dt'),
                product_div.find_all('dd')
            )
        }
    }

products = [parse_product(div) for div in soup.find_all('div', class_='product')]
```

**Parsing with Regular Expressions**:

While regex shouldn't be used to parse HTML structure, it's useful for extracting patterns from text:

```python
import re

# Extract price from text
text = "Price: $999.99 (was $1,299.99)"
price_pattern = r'\$([0-9,]+\.?\d*)'
prices = re.findall(price_pattern, text)
current_price = float(prices[0].replace(',', ''))  # 999.99

# Extract phone numbers
text = "Call us at (555) 123-4567 or (555) 987-6543"
phone_pattern = r'\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}'
phones = re.findall(phone_pattern, text)

# Extract emails
text = "Contact: support@example.com or sales@example.com"
email_pattern = r'[\w\.-]+@[\w\.-]+\.\w+'
emails = re.findall(email_pattern, text)
```

**Handling Comments**:

```python
from bs4 import Comment

# Find all comments
comments = soup.find_all(string=lambda text: isinstance(text, Comment))

# Sometimes data is hidden in comments (anti-scraping technique)
for comment in comments:
    if 'product-data' in comment:
        # Extract and parse data from comment
        data_html = comment.strip()
        data_soup = BeautifulSoup(data_html, 'lxml')
        # Extract data from data_soup
```

**Processing Scripts and Styles**:

```python
# Remove script and style tags before extracting text
for script in soup(['script', 'style']):
    script.decompose()

clean_text = soup.get_text()

# Extract data from script tags (common for JSON data)
script = soup.find('script', {'type': 'application/ld+json'})
if script:
    import json
    structured_data = json.loads(script.string)
```

### Performance Optimization

**Parsing Performance**:

```python
import time

# lxml is fastest
start = time.time()
soup = BeautifulSoup(large_html, 'lxml')
print(f'lxml: {time.time() - start:.3f}s')

# html.parser is slower but no dependencies
start = time.time()
soup = BeautifulSoup(large_html, 'html.parser')
print(f'html.parser: {time.time() - start:.3f}s')

# html5lib is slowest but most accurate
start = time.time()
soup = BeautifulSoup(large_html, 'html5lib')
print(f'html5lib: {time.time() - start:.3f}s')
```

**Efficient Searching**:

```python
# Instead of multiple find calls
title = soup.find('h1')
price = soup.find('span', class_='price')
description = soup.find('p', class_='desc')

# Search once, extract multiple elements
container = soup.find('div', class_='product')
if container:
    title = container.find('h1')
    price = container.find('span', class_='price')
    description = container.find('p', class_='desc')
```

**Limit Search Scope**:

```python
# Bad: Search entire document repeatedly
products = []
for product_div in soup.find_all('div', class_='product'):
    # Each find searches from document root
    name = soup.find('h2', class_='name').text
    price = soup.find('span', class_='price').text
    products.append({'name': name, 'price': price})

# Good: Search within specific element
products = []
for product_div in soup.find_all('div', class_='product'):
    # Each find searches only within product_div
    name = product_div.find('h2', class_='name').text
    price = product_div.find('span', class_='price').text
    products.append({'name': name, 'price': price})
```

**Using SoupStrainer**:

Parse only relevant parts of HTML:

```python
from bs4 import SoupStrainer

# Only parse product divs
strainer = SoupStrainer('div', class_='product')
soup = BeautifulSoup(large_html, 'lxml', parse_only=strainer)

# Now soup only contains product divs
products = soup.find_all('div', class_='product')
```

### Debugging Parsing Issues

**Common Issues**:

**Issue: Element Not Found**:

```python
element = soup.find('div', class_='product')
if element is None:
    # Element doesn't exist
    print("Element not found!")
    # Debug: Print HTML to see actual structure
    print(soup.prettify()[:500])
```

**Issue: Empty Text**:

```python
element = soup.find('span', class_='price')
text = element.get_text(strip=True)
if not text:
    # Element exists but is empty
    # Check if content is in attribute
    price = element.get('data-price')
    # Or check if content loads via JavaScript
```

**Issue: Wrong Element Selected**:

```python
# Multiple elements with same class
prices = soup.find_all('span', class_='price')
print(f'Found {len(prices)} price elements')
for i, price in enumerate(prices):
    print(f'{i}: {price.get_text(strip=True)}')

# Be more specific
current_price = soup.find('span', class_='price current')
original_price = soup.find('span', class_='price original')
```

**Debugging Techniques**:

```python
# 1. Print parsed structure
print(soup.prettify())

# 2. Print specific element
element = soup.find('div', class_='product')
print(element.prettify())

# 3. Inspect element attributes
print(element.attrs)

# 4. Check element name
print(element.name)  # 'div'

# 5. Verify selector
elements = soup.select('.product')
print(f'Selector found {len(elements)} elements')

# 6. Test XPath (with lxml)
from lxml import html
tree = html.fromstring(str(soup))
elements = tree.xpath('//div[@class="product"]')
print(f'XPath found {len(elements)} elements')
```

---

## CSS Selectors - Complete Guide

### Introduction to CSS Selectors

CSS selectors are patterns used to select HTML elements. Originally designed for styling, they're equally powerful for web scraping. CSS selectors offer a concise, readable syntax for finding elements in HTML documents.

**Why Use CSS Selectors for Scraping**:

- **Concise**: More compact than equivalent XPath expressions for many common patterns
- **Familiar**: If you know web development, you already know CSS selectors
- **Fast**: Modern parsers optimize CSS selector performance
- **Readable**: Easy to understand at a glance
- **Browser DevTools**: Can test selectors directly in browser console

### Basic Selectors

**Type Selector** - Select by tag name:

```python
# Select all <p> elements
paragraphs = soup.select('p')

# Select all <a> elements
links = soup.select('a')

# Select all <div> elements
divs = soup.select('div')
```

**Class Selector** - Select by class attribute:

```python
# Select elements with class="product"
products = soup.select('.product')

# Select elements with class="price"
prices = soup.select('.price')

# Multiple classes (element must have both)
featured_products = soup.select('.product.featured')
```

**ID Selector** - Select by ID attribute (should be unique):

```python
# Select element with id="main-content"
main = soup.select_one('#main-content')

# Select element with id="header"
header = soup.select_one('#header')
```

**Universal Selector** - Select all elements:

```python
# Select all elements
all_elements = soup.select('*')

# Rarely useful alone, but powerful in combinations
```

### Attribute Selectors

Select elements based on attributes:

**Has Attribute**:

```python
# Elements with href attribute (any value)
links = soup.select('[href]')

# Elements with data-id attribute
items = soup.select('[data-id]')

# Elements with title attribute
titled = soup.select('[title]')
```

**Attribute Equals** Value:

```python
# Exact match
english_links = soup.select('[lang="en"]')

# Type attribute equals
checkboxes = soup.select('[type="checkbox"]')

# Data attribute equals
product = soup.select_one('[data-id="12345"]')
```

**Attribute Contains Word**:

```python
# Class contains word (use for space-separated values)
# Matches class="btn primary" or class="primary btn"
primary_buttons = soup.select('[class~="primary"]')
```

**Attribute Starts With**:

```python
# href starts with "https"
secure_links = soup.select('[href^="https"]')

# class starts with "icon-"
icons = soup.select('[class^="icon-"]')

# data-category starts with "electronics"
electronics = soup.select('[data-category^="electronics"]')
```

**Attribute Ends With**:

```python
# href ends with ".pdf"
pdf_links = soup.select('[href$=".pdf"]')

# src ends with ".jpg"
jpg_images = soup.select('[src$=".jpg"]')

# class ends with "-badge"
badges = soup.select('[class$="-badge"]')
```

**Attribute Contains Substring**:

```python
# href contains "product"
product_links = soup.select('[href*="product"]')

# class contains "button"
buttons = soup.select('[class*="button"]')

# title contains "download"
download_items = soup.select('[title*="download"]')
```

**Case-Insensitive Attribute Matching**:

```python
# Case-insensitive (add 'i' flag)
links = soup.select('[href$=".PDF" i]')  # Matches .pdf, .PDF, .Pdf
```

### Combinators

Combinators define relationships between selectors:

**Descendant Combinator** (space) - Any descendant:

```python
# All <a> inside <div>
links = soup.select('div a')

# All <span> inside elements with class="product"
prices = soup.select('.product span')

# All <li> inside <ul> inside <nav>
nav_items = soup.select('nav ul li')
```

**Child Combinator** (>) - Direct children only:

```python
# Direct <li> children of <ul>
direct_items = soup.select('ul > li')

# Direct <span> children of .product
prices = soup.select('.product > span')

# Direct <div> children of <body>
top_divs = soup.select('body > div')
```

**Adjacent Sibling Combinator** (+) - Immediately following sibling:

```python
# <p> immediately after <h2>
descriptions = soup.select('h2 + p')

# <span> immediately after <label>
values = soup.select('label + span')
```

**General Sibling Combinator** (~) - Any following sibling:

```python
# All <p> after <h2> (same parent)
all_paragraphs = soup.select('h2 ~ p')

# All <li> after .selected
following_items = soup.select('.selected ~ li')
```

### Pseudo-Classes

Pseudo-classes select elements based on their state or position:

**Structural Pseudo-Classes**:

```python
# First child
first_items = soup.select('li:first-child')

# Last child
last_items = soup.select('li:last-child')

# Only child (no siblings)
singles = soup.select('p:only-child')

# Nth child
second_items = soup.select('li:nth-child(2)')  # Second <li>
even_rows = soup.select('tr:nth-child(even)')  # Even rows
odd_rows = soup.select('tr:nth-child(odd)')   # Odd rows
every_third = soup.select('li:nth-child(3n)')  # Every 3rd item

# Nth from end
second_last = soup.select('li:nth-last-child(2)')

# First of type
first_headings = soup.select('h2:first-of-type')

# Last of type
last_paragraphs = soup.select('p:last-of-type')

# Nth of type
second_divs = soup.select('div:nth-of-type(2)')
```

**State Pseudo-Classes** (limited support in BeautifulSoup):

```python
# Has attribute checked
checked = soup.select('[checked]')  # Use attribute selector instead

# Disabled
disabled = soup.select('[disabled]')
```

**Negation Pseudo-Class**:

```python
# All <div> except those with class="exclude"
divs = soup.select('div:not(.exclude)')

# All <a> except those with rel="nofollow"
links = soup.select('a:not([rel="nofollow"])')

# All <input> except type="hidden"
visible_inputs = soup.select('input:not([type="hidden"])')
```

**Content Pseudo-Class** (BeautifulSoup extension):

```python
# Find elements containing specific text
# Note: Not standard CSS, BeautifulSoup-specific
elements = soup.find_all(string=lambda text: 'search term' in text.lower())
```

### Advanced Selector Patterns

**Multiple Selectors** (comma-separated):

```python
# Select <h1>, <h2>, and <h3>
headings = soup.select('h1, h2, h3')

# Select .price and .cost
prices = soup.select('.price, .cost')

# Select multiple specific elements
important = soup.select('#header, #footer, .sidebar')
```

**Chaining Selectors**:

```python
# <div> with both class="product" and class="featured"
featured_products = soup.select('div.product.featured')

# <a> with class="link" and href attribute
links = soup.select('a.link[href]')

# <input> with type="text" and class="required"
required_inputs = soup.select('input[type="text"].required')
```

**Complex Combinations**:

```python
# Links inside divs with class="product" that have data-id attribute
links = soup.select('div.product[data-id] a')

# Spans with class="price" that are direct children of divs with class="product"
prices = soup.select('div.product > span.price')

# First paragraph after h2 inside article
paras = soup.select('article h2 + p')

# All divs except first and last child
middle_divs = soup.select('div:not(:first-child):not(:last-child)')
```

### Practical Scraping Examples

**Extracting Product Information**:

```python
html = '''
<div class="product" data-id="12345">
    <h2 class="product-name">Laptop Computer</h2>
    <div class="pricing">
        <span class="price current">$999.99</span>
        <span class="price original">$1,299.99</span>
    </div>
    <div class="rating" data-score="4.5">
        <span class="stars">★★★★☆</span>
        <span class="count">(234 reviews)</span>
    </div>
    <ul class="features">
        <li>16GB RAM</li>
        <li>512GB SSD</li>
        <li>Intel Core i7</li>
    </ul>
</div>
'''

soup = BeautifulSoup(html, 'lxml')

# Extract all product data using CSS selectors
product = {
    'id': soup.select_one('.product')['data-id'],
    'name': soup.select_one('.product-name').get_text(strip=True),
    'current_price': soup.select_one('.price.current').get_text(strip=True),
    'original_price': soup.select_one('.price.original').get_text(strip=True),
    'rating': soup.select_one('.rating')['data-score'],
    'review_count': soup.select_one('.count').get_text(strip=True),
    'features': [li.get_text(strip=True) for li in soup.select('.features li')]
}
```

**Navigating Table Data**:

```python
html = '''
<table class="data-table">
    <thead>
        <tr>
            <th>Product</th>
            <th>Price</th>
            <th>Stock</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td class="name">Item 1</td>
            <td class="price">$10.99</td>
            <td class="stock">In Stock</td>
        </tr>
        <tr class="out-of-stock">
            <td class="name">Item 2</td>
            <td class="price">$15.99</td>
            <td class="stock">Out of Stock</td>
        </tr>
    </tbody>
</table>
'''

soup = BeautifulSoup(html, 'lxml')

# Extract table headers
headers = [th.get_text(strip=True) for th in soup.select('table thead th')]

# Extract all rows except out-of-stock
in_stock_rows = soup.select('table tbody tr:not(.out-of-stock)')

products = []
for row in in_stock_rows:
    cells = row.select('td')
    product = {
        'name': cells[0].get_text(strip=True),
        'price': cells[1].get_text(strip=True),
        'stock': cells[2].get_text(strip=True)
    }
    products.append(product)
```

**Extracting Nested Structures**:

```python
html = '''
<div class="article">
    <header>
        <h1 class="title">Article Title</h1>
        <div class="meta">
            <span class="author">John Doe</span>
            <time datetime="2027-02-09">Feb 9, 2027</time>
        </div>
    </header>
    <div class="content">
        <p>First paragraph.</p>
        <p>Second paragraph.</p>
    </div>
    <footer>
        <a href="/articles/1">Permalink</a>
        <span class="tags">
            <a href="/tag/tech">#tech</a>
            <a href="/tag/ai">#ai</a>
        </span>
    </footer>
</div>
'''

soup = BeautifulSoup(html, 'lxml')

article = {
    'title': soup.select_one('.article .title').get_text(strip=True),
    'author': soup.select_one('.meta .author').get_text(strip=True),
    'date': soup.select_one('.meta time')['datetime'],
    'content': '\n\n'.join([p.get_text(strip=True) for p in soup.select('.content p')]),
    'permalink': soup.select_one('footer a[href^="/articles"]')['href'],
    'tags': [a.get_text(strip=True) for a in soup.select('.tags a')]
}
```

### Performance and Best Practices

**Selector Performance**:

Selector performance varies. From fastest to slowest generally:

1. ID selectors: `#id`
2. Class selectors: `.class`
3. Tag selectors: `tag`
4. Attribute selectors: `[attr="value"]`
5. Pseudo-classes: `:nth-child()`, `:not()`
6. Complex combinators: Deep nesting

**Best Practices**:

**1. Be Specific But Not Fragile**:

```python
# Too fragile - breaks if structure changes
bad = soup.select('body > div > div > div > span.price')

# Better - specific to the data you need
good = soup.select('.product .price')

# Even better - use unique identifiers when available
best = soup.select('[data-price]')
```

**2. Prefer IDs and Classes**:

```python
# Fast and reliable
product = soup.select_one('#product-12345')
products = soup.select('.product-card')

# Slower and more fragile
products = soup.select('div[data-type="product"]')
```

**3. Limit Scope**:

```python
# Bad - search entire document repeatedly
for product_div in soup.select('.product'):
    name = soup.select_one('.product-name').text  # Searches whole document!

# Good - search within each product
for product_div in soup.select('.product'):
    name = product_div.select_one('.product-name').text  # Searches only within product_div
```

**4. Use Direct Descendant When Possible**:

```python
# Slower - searches all descendants
prices = soup.select('.product .price')

# Faster - only direct children
prices = soup.select('.product > .price')
```

**5. Combine Selectors Efficiently**:

```python
# Multiple selections
titles = soup.select('h1')
subtitles = soup.select('h2')
headings = titles + subtitles

# Better - single selection
headings = soup.select('h1, h2')
```

### CSS Selectors vs XPath

CSS selectors and XPath can achieve similar results but have different strengths:

**CSS Selectors Are Better For**:

- Simple selections by class, ID, tag
- Parent-to-child navigation
- Concise, readable queries
- Familiarity if you know CSS
- When performance matters (CSS often faster)

**XPath Is Better For**:

- Text content matching
- Complex conditions
- Parent/ancestor navigation (selecting upward)
- Counting and position-based selection
- When you need more power and flexibility

**Equivalent Examples**:

```python
# Select all divs with class "product"
css = soup.select('div.product')
xpath = soup.find_all('div', class_='product')  # BeautifulSoup doesn't natively support XPath

# With lxml (supports XPath)
from lxml import html
tree = html.fromstring(html_content)

# Select by class
css = tree.cssselect('.product')
xpath = tree.xpath('//div[@class="product"]')

# Select by attribute value
css = tree.cssselect('[data-id="12345"]')
xpath = tree.xpath('//*[@data-id="12345"]')

# Select nested elements
css = tree.cssselect('.product .price')
xpath = tree.xpath('//div[@class="product"]//span[@class="price"]')

# Select direct children
css = tree.cssselect('.product > .price')
xpath = tree.xpath('//div[@class="product"]/span[@class="price"]')
```

---

## XPath - Advanced Selection Techniques

### Introduction to XPath

XPath (XML Path Language) is a powerful query language for selecting nodes in XML and HTML documents. While CSS selectors are concise and familiar, XPath offers significantly more power and flexibility for complex selection requirements.

**Why Use XPath**:

- **Text-based selection**: Select elements containing specific text
- **Bidirectional navigation**: Move both down (children) and up (parents/ancestors)
- **Advanced filtering**: Complex conditional logic
- **Functions**: String manipulation, counting, boolean logic
- **Axes**: Flexible navigation in any direction
- **Superior for complex scraping**: When CSS selectors become unwieldy, XPath often provides elegant solutions

**When to Use XPath Over CSS**:

- Need to select based on text content
- Need to navigate to parent/ancestor elements
- Complex conditional logic
- Mathematical operations or counting
- String manipulation in the query itself

### XPath Basics

**XPath Syntax Fundamentals**:

XPath expressions return node-sets, strings, numbers, or booleans. The most common use case is selecting nodes (elements).

**Absolute vs Relative Paths**:

```python
# Absolute path (starts from root)
'/html/body/div/p'  # Fragile - breaks if structure changes

# Relative path (starts from any context)
'//p'  # All <p> elements anywhere in document
'.//p'  # All <p> elements within current context
```

**Selecting Nodes**:

```python
from lxml import html

tree = html.fromstring(html_content)

# Select all <div> elements
divs = tree.xpath('//div')

# Select all <p> elements
paragraphs = tree.xpath('//p')

# Select root element
root = tree.xpath('/html')

# Select from context
product = tree.xpath('//div[@class="product"]')[0]
prices = product.xpath('.//span[@class="price"]')  # Within product only
```

### Node Selection

**Selecting by Tag Name**:

```python
# All paragraphs
paragraphs = tree.xpath('//p')

# All headings (any level)
headings = tree.xpath('//h1 | //h2 | //h3')

# All links
links = tree.xpath('//a')

# All elements (wildcard)
all_elements = tree.xpath('//*')
```

**Selecting by Attribute**:

```python
# Elements with specific attribute value
products = tree.xpath('//div[@class="product"]')

# Elements with any value for attribute
items_with_id = tree.xpath('//div[@id]')

# Multiple attribute conditions
featured_products = tree.xpath('//div[@class="product"][@data-featured="true"]')

# Attribute contains value
links_to_pdf = tree.xpath('//a[contains(@href, ".pdf")]')

# Attribute starts with value
secure_links = tree.xpath('//a[starts-with(@href, "https")]')

# Class attribute (handles multiple classes)
# Class contains "product" (even with other classes)
products = tree.xpath('//div[contains(@class, "product")]')

# Has exact class (may fail if element has multiple classes)
exact_class = tree.xpath('//div[@class="product"]')
```

**Selecting by Position**:

```python
# First element
first_div = tree.xpath('//div[1]')  # Note: XPath is 1-indexed!

# Last element
last_div = tree.xpath('//div[last()]')

# Second element
second_div = tree.xpath('//div[2]')

# First three elements
first_three = tree.xpath('//div[position() <= 3]')

# Elements after the third
after_third = tree.xpath('//div[position() > 3]')
```

**Selecting by Text Content**:

```python
# Elements with exact text
click_here = tree.xpath('//a[text()="Click Here"]')

# Elements containing text
links_with_download = tree.xpath('//a[contains(text(), "Download")]')

# Case-insensitive text search (XPath 2.0+, limited support)
# Use translate() for case-insensitive in XPath 1.0
case_insensitive = tree.xpath('//a[contains(translate(text(), "ABCDEFGHIJKLMNOPQRSTUVWXYZ", "abcdefghijklmnopqrstuvwxyz"), "download")]')

# Normalize whitespace
normalized = tree.xpath('//p[normalize-space(text())="Some text"]')
```

### XPath Axes

Axes define the relationship between the current node and other nodes.

**Child Axis** (`child::` or `/`):

```python
# Direct children
children = tree.xpath('//div/child::p')
# Or simply:
children = tree.xpath('//div/p')
```

**Descendant Axis** (`descendant::` or `//`):

```python
# All descendants
descendants = tree.xpath('//div/descendant::p')
# Or:
descendants = tree.xpath('//div//p')
```

**Parent Axis** (`parent::` or `..`):

```python
# Parent of element
# Find parent div of span with class="price"
parent = tree.xpath('//span[@class="price"]/parent::div')
# Or:
parent = tree.xpath('//span[@class="price"]/..')
```

**Ancestor Axis** (`ancestor::`):

```python
# All ancestors
ancestors = tree.xpath('//span[@class="price"]/ancestor::div')

# Nearest ancestor with specific attribute
container = tree.xpath('//span[@class="price"]/ancestor::div[@class="product"]')
```

**Following-Sibling Axis** (`following-sibling::`):

```python
# All following siblings
siblings = tree.xpath('//h2/following-sibling::p')

# First following sibling
next_para = tree.xpath('//h2/following-sibling::p[1]')

# All following <p> siblings
para_siblings = tree.xpath('//h2/following-sibling::p')
```

**Preceding-Sibling Axis** (`preceding-sibling::`):

```python
# All preceding siblings
prev_siblings = tree.xpath('//p[@class="summary"]/preceding-sibling::p')

# Immediately preceding sibling
prev = tree.xpath('//p[@class="summary"]/preceding-sibling::*[1]')
```

**Following Axis** (`following::`):

```python
# All following elements in document (not just siblings)
following = tree.xpath('//h2[@class="title"]/following::p')
```

**Preceding Axis** (`preceding::`):

```python
# All preceding elements in document
preceding = tree.xpath('//div[@class="footer"]/preceding::a')
```

**Self Axis** (`self::`):

```python
# Current node
self_node = tree.xpath('//div[@class="product"]/self::div')
```

**Attribute Axis** (`@` or `attribute::`):

```python
# All href attributes of links
hrefs = tree.xpath('//a/@href')

# Class attribute of divs
classes = tree.xpath('//div/@class')

# Using attribute axis explicitly
hrefs = tree.xpath('//a/attribute::href')
```

### XPath Predicates

Predicates filter node-sets:

**Numeric Predicates**:

```python
# Position-based selection
first = tree.xpath('//div[@class="product"][1]')
last = tree.xpath('//div[@class="product"][last()]')
second_to_last = tree.xpath('//div[@class="product"][last()-1]')

# Range
first_five = tree.xpath('//div[@class="product"][position() <= 5]')
```

**Attribute Predicates**:

```python
# Has attribute
with_href = tree.xpath('//a[@href]')

# Attribute equals
english = tree.xpath('//div[@lang="en"]')

# Multiple attributes (AND logic)
items = tree.xpath('//div[@class="product"][@data-available="true"]')

# Attribute comparison
expensive = tree.xpath('//div[@data-price > 1000]')
```

**Text Predicates**:

```python
# Exact text
submit = tree.xpath('//button[text()="Submit"]')

# Contains text
download_links = tree.xpath('//a[contains(text(), "Download")]')

# Starts with
pdf_links = tree.xpath('//a[starts-with(text(), "PDF:")]')

# Text length (string-length function)
long_text = tree.xpath('//p[string-length(text()) > 100]')
```

**Boolean Logic**:

```python
# OR condition
headings = tree.xpath('//h1 | //h2 | //h3')

# AND condition (multiple predicates)
items = tree.xpath('//div[@class="product"][price > 100]')

# NOT condition
not_featured = tree.xpath('//div[@class="product"][not(@data-featured)]')
```

### XPath Functions

**String Functions**:

```python
# contains(string, substring)
links = tree.xpath('//a[contains(@href, "example.com")]')
text_with_word = tree.xpath('//p[contains(text(), "laptop")]')

# starts-with(string, prefix)
https_links = tree.xpath('//a[starts-with(@href, "https")]')

# concat(string1, string2, ...)
# Combine attribute values
combined = tree.xpath('concat(//div/@data-first, " ", //div/@data-last)')

# substring(string, start, length)
# Extract substring
codes = tree.xpath('substring(//div/@data-code, 1, 3)')

# string-length(string)
# Get length
long_titles = tree.xpath('//h1[string-length(text()) > 50]')

# normalize-space(string)
# Trim whitespace
trimmed = tree.xpath('//p[normalize-space(text())="Some text"]')

# translate(string, from, to)
# Case conversion (XPath 1.0 doesn't have lower-case())
lower = tree.xpath('//a[contains(translate(@href, "ABCDEFGHIJKLMNOPQRSTUVWXYZ", "abcdefghijklmnopqrstuvwxyz"), "download")]')
```

**Numeric Functions**:

```python
# count(node-set)
# Count elements
product_count = tree.xpath('count(//div[@class="product"])')

# sum(node-set)
# Sum numeric values
total = tree.xpath('sum(//span[@class="price"]/@data-value)')

# number(string)
# Convert to number
price_num = tree.xpath('number(//span[@class="price"]/@data-value)')

# floor(number), ceiling(number), round(number)
rounded = tree.xpath('round(number(//span[@class="price"]/@data-value))')
```

**Boolean Functions**:

```python
# not(boolean)
# Negate condition
no_href = tree.xpath('//a[not(@href)]')

# true(), false()
# Boolean literals
always_true = tree.xpath('//div[true()]')  # All divs

# boolean(object)
# Convert to boolean
has_text = tree.xpath('//p[boolean(text())]')  # Paragraphs with text
```

**Node-Set Functions**:

```python
# last()
# Last position
last_item = tree.xpath('//li[last()]')

# position()
# Current position
even_items = tree.xpath('//li[position() mod 2 = 0]')

# count()
# Count nodes
num_products = tree.xpath('count(//div[@class="product"])')
```

### Advanced XPath Patterns

**Selecting Parent Based on Child**:

```python
# Find div that contains a span with class="price"
product_divs = tree.xpath('//div[.//span[@class="price"]]')

# Find parent div of links containing "Download"
containers = tree.xpath('//a[contains(text(), "Download")]/parent::div')

# Find divs that contain both h2 and p
sections = tree.xpath('//div[.//h2 and .//p]')
```

**Combining Multiple Conditions**:

```python
# Products that are both featured and in-stock
products = tree.xpath('//div[@class="product"][@data-featured="true"][@data-stock="available"]')

# Links that don't have nofollow and start with https
links = tree.xpath('//a[not(@rel="nofollow")][starts-with(@href, "https")]')

# Divs with class containing "product" AND price > 100
items = tree.xpath('//div[contains(@class, "product")][@data-price > 100]')
```

**Text Node Selection**:

```python
# Get all text nodes
text_nodes = tree.xpath('//p/text()')

# Get direct text only (excluding nested elements)
direct_text = tree.xpath('//div[@class="product"]/text()')

# Get all descendant text
all_text = tree.xpath('//div[@class="product"]//text()')

# Filter text nodes
non_empty = tree.xpath('//p/text()[normalize-space()]')
```

**Conditional Selection**:

```python
# If element has attribute, use it; otherwise use default
price = tree.xpath('(//span[@data-price]/@data-price | //span[@class="price"]/text())[1]')

# Select first available element from multiple options
title = tree.xpath('(//h1 | //h2 | //title)[1]')
```

### Practical XPath Examples

**Extracting Data from Complex Tables**:

```python
table_html = '''
<table class="data">
    <thead>
        <tr><th>Product</th><th>Price</th><th>Stock</th></tr>
    </thead>
    <tbody>
        <tr>
            <td>Laptop</td>
            <td>$999</td>
            <td class="in-stock">Available</td>
        </tr>
        <tr>
            <td>Mouse</td>
            <td>$29</td>
            <td class="out-of-stock">Unavailable</td>
        </tr>
    </tbody>
</table>
'''

tree = html.fromstring(table_html)

# Get headers
headers = tree.xpath('//table[@class="data"]//thead//th/text()')

# Get all rows
rows = tree.xpath('//table[@class="data"]//tbody/tr')

# Extract data from each row
products = []
for row in rows:
    product = {
        'name': row.xpath('./td[1]/text()')[0],
        'price': row.xpath('./td[2]/text()')[0],
        'stock': row.xpath('./td[3]/text()')[0],
        'available': bool(row.xpath('./td[contains(@class, "in-stock")]'))
    }
    products.append(product)

# Get only in-stock products
in_stock = tree.xpath('//table//tr[.//td[contains(@class, "in-stock")]]')
```

**Navigating Nested Product Information**:

```python
product_html = '''
<div class="product" data-id="123">
    <div class="header">
        <h2 class="title">Laptop Computer</h2>
        <span class="brand">TechBrand</span>
    </div>
    <div class="pricing">
        <span class="price current" data-value="999">$999.99</span>
        <span class="price original" data-value="1299">$1,299.99</span>
        <span class="discount">Save 23%</span>
    </div>
    <div class="details">
        <ul class="specs">
            <li><strong>RAM:</strong> 16GB</li>
            <li><strong>Storage:</strong> 512GB SSD</li>
            <li><strong>CPU:</strong> Intel i7</li>
        </ul>
    </div>
</div>
'''

tree = html.fromstring(product_html)

# Extract using XPath
product = {
    'id': tree.xpath('//div[@class="product"]/@data-id')[0],
    'title': tree.xpath('//h2[@class="title"]/text()')[0],
    'brand': tree.xpath('//span[@class="brand"]/text()')[0],
    'current_price': tree.xpath('//span[contains(@class, "current")]/@data-value')[0],
    'original_price': tree.xpath('//span[contains(@class, "original")]/@data-value')[0],
    'discount': tree.xpath('//span[@class="discount"]/text()')[0],
    # Extract specs - text after <strong> in each <li>
    'specs': {
        'RAM': tree.xpath('//li[contains(., "RAM")]/text()')[0].strip(),
        'Storage': tree.xpath('//li[contains(., "Storage")]/text()')[0].strip(),
        'CPU': tree.xpath('//li[contains(., "CPU")]/text()')[0].strip()
    }
}
```

**Finding Elements Based on Siblings**:

```python
html_content = '''
<div class="content">
    <h2>Section 1</h2>
    <p>Paragraph 1</p>
    <p>Paragraph 2</p>
    
    <h2>Section 2</h2>
    <p>Paragraph 3</p>
    <p>Paragraph 4</p>
    
    <h2>Section 3</h2>
    <p>Paragraph 5</p>
</div>
'''

tree = html.fromstring(html_content)

# Get all paragraphs under "Section 2"
section2_paras = tree.xpath('//h2[text()="Section 2"]/following-sibling::p[following-sibling::h2]')

# Get all paragraphs between first and second h2
between = tree.xpath('//h2[1]/following-sibling::p[following-sibling::h2[text()="Section 2"]]')

# Get the <p> immediately after each <h2>
first_paras = tree.xpath('//h2/following-sibling::p[1]')
```

**Extracting Data Attributes**:

```python
# All elements with data-* attributes
data_elements = tree.xpath('//*[@*[starts-with(name(), "data-")]]')

# Specific data attribute
product_ids = tree.xpath('//div/@data-product-id')

# Elements where data attribute meets condition
expensive = tree.xpath('//div[@data-price > 1000]')

# Get all data attributes from an element
product = tree.xpath('//div[@class="product"]')[0]
data_attrs = {
    attr: value 
    for attr, value in product.attrib.items() 
    if attr.startswith('data-')
}
```

### XPath Best Practices

**1. Use Relative Paths for Robustness**:

```python
# Fragile - breaks if structure changes
bad = tree.xpath('/html/body/div[2]/div[3]/span[1]')

# Better - selects based on semantics
good = tree.xpath('//span[@class="price"]')

# Even better - specific context
best = tree.xpath('//div[@class="product"]//span[@class="price"]')
```

**2. Be Specific Without Overfitting**:

```python
# Too general - might select wrong elements
too_general = tree.xpath('//span')

# Too specific - fragile
too_specific = tree.xpath('//div/div/div/span[@class="price current sale"]')

# Just right
balanced = tree.xpath('//span[contains(@class, "price")]')
```

**3. Use Axes Wisely**:

```python
# Inefficient - searches entire document
all_ancestors = tree.xpath('//span[@class="price"]/ancestor::*')

# Better - find specific ancestor
product_div = tree.xpath('//span[@class="price"]/ancestor::div[@class="product"]')
```

**4. Cache Common Selections**:

```python
# Bad - re-selects products for each attribute
names = [tree.xpath('//div[@class="product"][%d]//h2/text()' % i)[0] for i in range(1, 11)]

# Good - select once, then extract from each
products = tree.xpath('//div[@class="product"]')
names = [p.xpath('.//h2/text()')[0] for p in products]
```

**5. Handle Missing Elements**:

```python
# Crashes if element doesn't exist
price = tree.xpath('//span[@class="price"]/text()')[0]

# Better - check if exists
prices = tree.xpath('//span[@class="price"]/text()')
price = prices[0] if prices else None

# Or use default
price = tree.xpath('//span[@class="price"]/text()')[0] if tree.xpath('//span[@class="price"]') else 'N/A'
```

### XPath vs CSS Selector Decision Matrix

| Task | Prefer | Example |
|------|--------|---------|
| Select by class/ID | CSS | `.product`, `#header` |
| Select by tag | Either | `div` or `//div` |
| Select by attribute | Either | `[data-id="123"]` or `//*[@data-id="123"]` |
| Select parent element | XPath | `..` or `/parent::div` |
| Select by text content | XPath | `//a[text()="Click"]` |
| Complex conditions | XPath | `//div[@price > 100 and @stock > 0]` |
| Following siblings | Either | `h2 ~ p` or `//h2/following-sibling::p` |
| Count elements | XPath | `count(//div[@class="product"])` |
| String manipulation | XPath | `contains()`, `starts-with()` |
| Simple descendant | CSS | `.product .price` (more concise) |

---

## Python Web Scraping Stack

### Requests Library - HTTP Made Easy

The `requests` library is Python's de facto standard for HTTP operations. Its elegant API makes web scraping significantly easier than using Python's built-in `urllib`.

**Installation**:

```bash
pip install requests
```

**Basic GET Requests**:

```python
import requests

# Simple GET request
response = requests.get('https://example.com')

# Access response properties
print(response.status_code)  # 200
print(response.headers)      # Response headers dict
print(response.text)         # Response body as string
print(response.content)      # Response body as bytes
print(response.encoding)     # Detected encoding
print(response.url)          # Final URL (after redirects)
```

**Request with Parameters**:

```python
# URL parameters
params = {
    'q': 'laptop',
    'page': 2,
    'sort': 'price',
    'min_price': 500
}

response = requests.get('https://example.com/search', params=params)
# URL: https://example.com/search?q=laptop&page=2&sort=price&min_price=500

# Check the actual URL sent
print(response.url)
```

**Custom Headers**:

```python
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.9',
    'Accept-Encoding': 'gzip, deflate, br',
    'Referer': 'https://example.com',
    'DNT': '1'
}

response = requests.get('https://example.com', headers=headers)
```

**POST Requests**:

```python
# Form data (application/x-www-form-urlencoded)
data = {
    'username': 'user@example.com',
    'password': 'secretpassword'
}

response = requests.post('https://example.com/login', data=data)

# JSON data (application/json)
import json

payload = {
    'name': 'John Doe',
    'email': 'john@example.com',
    'age': 30
}

# Method 1: Manual JSON encoding
response = requests.post('https://example.com/api/users',
                        data=json.dumps(payload),
                        headers={'Content-Type': 'application/json'})

# Method 2: Automatic JSON encoding (preferred)
response = requests.post('https://example.com/api/users', json=payload)
```

**Session Management**:

```python
# Create a session (persists cookies, connection pooling)
session = requests.Session()

# Set default headers for all requests in this session
session.headers.update({
    'User-Agent': 'MyBot/1.0',
    'Accept-Language': 'en-US'
})

# Login (session stores cookies)
session.post('https://example.com/login', data={
    'username': 'user',
    'password': 'pass'
})

# Subsequent requests include authentication cookies
response = session.get('https://example.com/dashboard')
response2 = session.get('https://example.com/profile')

# Close session when done (good practice)
session.close()

# Or use context manager
with requests.Session() as session:
    session.post('https://example.com/login', data={'username': 'user', 'password': 'pass'})
    response = session.get('https://example.com/dashboard')
# Session automatically closed
```

**Timeout and Retry**:

```python
# Set timeout (seconds)
response = requests.get('https://example.com', timeout=10)

# Separate connect and read timeouts
response = requests.get('https://example.com', timeout=(3.05, 27))

# Retry logic with exponential backoff
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry

session = requests.Session()

retry_strategy = Retry(
    total=5,  # Total retries
    backoff_factor=1,  # Wait 1, 2, 4, 8, 16 seconds
    status_forcelist=[429, 500, 502, 503, 504],
    method_whitelist=["HEAD", "GET", "OPTIONS", "POST"]
)

adapter = HTTPAdapter(max_retries=retry_strategy)
session.mount("http://", adapter)
session.mount("https://", adapter)

response = session.get('https://example.com')
```

**Proxies**:

```python
# Use proxy
proxies = {
    'http': 'http://proxy.example.com:8080',
    'https': 'https://proxy.example.com:8080'
}

response = requests.get('https://example.com', proxies=proxies)

# Proxy with authentication
proxies = {
    'http': 'http://user:pass@proxy.example.com:8080',
    'https': 'https://user:pass@proxy.example.com:8080'
}

response = requests.get('https://example.com', proxies=proxies)

# SOCKS proxy (requires requests[socks])
proxies = {
    'http': 'socks5://user:pass@proxy.example.com:1080',
    'https': 'socks5://user:pass@proxy.example.com:1080'
}

response = requests.get('https://example.com', proxies=proxies)
```

**Handling Responses**:

```python
response = requests.get('https://api.example.com/data')

# Check status code
if response.status_code == 200:
    print("Success!")
elif response.status_code == 404:
    print("Not found")

# Raise exception for error status codes
response.raise_for_status()  # Raises HTTPError if status >= 400

# JSON response
data = response.json()  # Automatic parsing

# Handle JSON decode errors
try:
    data = response.json()
except json.JSONDecodeError:
    print("Response is not valid JSON")
    print(response.text)

# Binary content (images, files)
with open('image.jpg', 'wb') as f:
    f.write(response.content)

# Streaming large files
with requests.get('https://example.com/large_file.zip', stream=True) as r:
    r.raise_for_status()
    with open('large_file.zip', 'wb') as f:
        for chunk in r.iter_content(chunk_size=8192):
            f.write(chunk)
```

**Advanced Features**:

```python
# Disable SSL verification (use with caution!)
response = requests.get('https://example.com', verify=False)

# Custom CA bundle
response = requests.get('https://example.com', verify='/path/to/ca-bundle.crt')

# Client certificates
response = requests.get('https://example.com', 
                       cert=('/path/to/client.crt', '/path/to/client.key'))

# Disable redirects
response = requests.get('https://example.com', allow_redirects=False)

# Custom cookies
cookies = {'session_id': 'abc123', 'user_id': '42'}
response = requests.get('https://example.com', cookies=cookies)

# Access response cookies
print(response.cookies)
print(response.cookies.get('session_id'))
```

### BeautifulSoup 4 - Elegant HTML Parsing

We've covered BeautifulSoup basics earlier. Here are advanced patterns for scraping:

**Installation**:

```bash
pip install beautifulsoup4 lxml
```

**Complete Scraping Example**:

```python
import requests
from bs4 import BeautifulSoup
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class ProductScraper:
    def __init__(self, base_url):
        self.base_url = base_url
        self.session = requests.Session()
        self.session.headers.update({
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        })
    
    def scrape_product_list(self, page=1):
        url = f'{self.base_url}/products?page={page}'
        logger.info(f'Scraping {url}')
        
        try:
            response = self.session.get(url, timeout=10)
            response.raise_for_status()
        except requests.RequestException as e:
            logger.error(f'Failed to fetch {url}: {e}')
            return []
        
        soup = BeautifulSoup(response.content, 'lxml')
        products = []
        
        for product_div in soup.find_all('div', class_='product-card'):
            try:
                product = self.extract_product(product_div)
                products.append(product)
            except Exception as e:
                logger.error(f'Failed to extract product: {e}')
                continue
        
        logger.info(f'Extracted {len(products)} products from page {page}')
        return products
    
    def extract_product(self, product_div):
        # Extract with fallbacks and validation
        name_elem = product_div.find('h2', class_='product-name')
        name = name_elem.get_text(strip=True) if name_elem else None
        
        price_elem = product_div.find('span', class_='price')
        price_text = price_elem.get_text(strip=True) if price_elem else None
        price = self.parse_price(price_text)
        
        link_elem = product_div.find('a', class_='product-link')
        url = link_elem['href'] if link_elem and link_elem.has_attr('href') else None
        if url and not url.startswith('http'):
            url = self.base_url + url
        
        image_elem = product_div.find('img', class_='product-image')
        image_url = image_elem.get('src') or image_elem.get('data-src') if image_elem else None
        
        rating_elem = product_div.find('div', class_='rating')
        rating = float(rating_elem.get('data-rating', 0)) if rating_elem else None
        
        return {
            'name': name,
            'price': price,
            'url': url,
            'image_url': image_url,
            'rating': rating
        }
    
    def parse_price(self, price_text):
        if not price_text:
            return None
        
        # Remove currency symbols and commas
        import re
        price_str = re.sub(r'[^\d.]', '', price_text)
        
        try:
            return float(price_str)
        except ValueError:
            return None
    
    def scrape_all_pages(self, max_pages=10):
        all_products = []
        
        for page in range(1, max_pages + 1):
            products = self.scrape_product_list(page)
            
            if not products:
                logger.info(f'No products on page {page}, stopping')
                break
            
            all_products.extend(products)
            
            # Respectful delay
            import time
            time.sleep(2)
        
        return all_products

# Usage
scraper = ProductScraper('https://example.com')
products = scraper.scrape_all_pages(max_pages=5)

# Save to JSON
import json
with open('products.json', 'w') as f:
    json.dump(products, f, indent=2)
```

### lxml - High-Performance Parsing

lxml is faster than BeautifulSoup and supports XPath natively.

**Installation**:

```bash
pip install lxml
```

**Basic Usage**:

```python
from lxml import html, etree
import requests

response = requests.get('https://example.com')
tree = html.fromstring(response.content)

# XPath selection
products = tree.xpath('//div[@class="product"]')

for product in products:
    name = product.xpath('.//h2[@class="name"]/text()')[0]
    price = product.xpath('.//span[@class="price"]/text()')[0]
    print(f'{name}: {price}')

# CSS selection (requires cssselect package)
from lxml.cssselect import CSSSelector

selector = CSSSelector('.product .price')
prices = [elem.text for elem in selector(tree)]
```

**XML Parsing**:

```python
from lxml import etree

# Parse XML
xml_content = '''
<products>
    <product id="1">
        <name>Laptop</name>
        <price>999.99</price>
    </product>
    <product id="2">
        <name>Mouse</name>
        <price>29.99</price>
    </product>
</products>
'''

root = etree.fromstring(xml_content.encode('utf-8'))

# XPath with namespaces
for product in root.xpath('//product'):
    product_id = product.get('id')
    name = product.find('name').text
    price = float(product.find('price').text)
    print(f'{product_id}: {name} - ${price}')
```

**Performance Comparison**:

```python
import time
from bs4 import BeautifulSoup
from lxml import html

large_html = requests.get('https://example.com/large-page').content

# lxml
start = time.time()
tree = html.fromstring(large_html)
products = tree.xpath('//div[@class="product"]')
lxml_time = time.time() - start

# BeautifulSoup with lxml parser
start = time.time()
soup = BeautifulSoup(large_html, 'lxml')
products = soup.find_all('div', class_='product')
bs4_time = time.time() - start

print(f'lxml: {lxml_time:.3f}s')
print(f'BeautifulSoup: {bs4_time:.3f}s')
# lxml is typically 2-10x faster
```

### Scrapy - Industrial-Strength Scraping Framework

Scrapy is a complete framework for large-scale scraping projects. It handles requests, parsing, data pipelines, and much more.

**Installation**:

```bash
pip install scrapy
```

**Creating a Scrapy Project**:

```bash
scrapy startproject myproject
cd myproject
scrapy genspider example example.com
```

**Basic Spider**:

```python
# myproject/spiders/example.py

import scrapy

class ProductSpider(scrapy.Spider):
    name = 'products'
    allowed_domains = ['example.com']
    start_urls = ['https://example.com/products']
    
    def parse(self, response):
        # Extract products
        for product in response.css('div.product'):
            yield {
                'name': product.css('h2.name::text').get(),
                'price': product.css('span.price::text').get(),
                'url': product.css('a::attr(href)').get()
            }
        
        # Follow pagination
        next_page = response.css('a.next::attr(href)').get()
        if next_page:
            yield response.follow(next_page, self.parse)
```

**Advanced Spider**:

```python
# myproject/spiders/advanced_product.py

import scrapy
from scrapy.loader import ItemLoader
from itemloaders.processors import TakeFirst, MapCompose, Join
import re

class Product(scrapy.Item):
    name = scrapy.Field()
    price = scrapy.Field()
    url = scrapy.Field()
    image_url = scrapy.Field()
    description = scrapy.Field()
    features = scrapy.Field()
    rating = scrapy.Field()

class AdvancedProductSpider(scrapy.Spider):
    name = 'advanced_products'
    allowed_domains = ['example.com']
    
    custom_settings = {
        'CONCURRENT_REQUESTS': 16,
        'DOWNLOAD_DELAY': 1,
        'RANDOMIZE_DOWNLOAD_DELAY': True,
        'USER_AGENT': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36',
        'ROBOTSTXT_OBEY': True
    }
    
    def start_requests(self):
        # Start with category pages
        categories = ['electronics', 'computers', 'accessories']
        for category in categories:
            url = f'https://example.com/category/{category}'
            yield scrapy.Request(url, callback=self.parse_category,
                               meta={'category': category})
    
    def parse_category(self, response):
        category = response.meta['category']
        
        # Extract product links
        for product_url in response.css('div.product a::attr(href)').getall():
            yield response.follow(product_url, callback=self.parse_product,
                                meta={'category': category})
        
        # Follow pagination
        next_page = response.css('a.pagination-next::attr(href)').get()
        if next_page:
            yield response.follow(next_page, callback=self.parse_category,
                                meta={'category': category})
    
    def parse_product(self, response):
        loader = ItemLoader(item=Product(), response=response)
        
        loader.add_css('name', 'h1.product-name::text')
        loader.add_css('price', 'span.price::text', re=r'\d+\.\d+')
        loader.add_value('url', response.url)
        loader.add_css('image_url', 'img.product-image::attr(src)')
        loader.add_css('description', 'div.description p::text')
        loader.add_css('features', 'ul.features li::text')
        loader.add_css('rating', 'div.rating::attr(data-rating)')
        
        yield loader.load_item()
```

**Scrapy Settings and Configuration**:

```python
# myproject/settings.py

BOT_NAME = 'myproject'

SPIDER_MODULES = ['myproject.spiders']
NEWSPIDER_MODULE = 'myproject.spiders'

# Crawl responsibly
ROBOTSTXT_OBEY = True
CONCURRENT_REQUESTS = 16
DOWNLOAD_DELAY = 2
RANDOMIZE_DOWNLOAD_DELAY = True

# User agent
USER_AGENT = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'

# Auto-throttle
AUTOTHROTTLE_ENABLED = True
AUTOTHROTTLE_START_DELAY = 1
AUTOTHROTTLE_MAX_DELAY = 10
AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0

# Enable middleware
DOWNLOADER_MIDDLEWARES = {
    'scrapy.downloadermiddlewares.useragent.UserAgentMiddleware': None,
    'scrapy_user_agents.middlewares.RandomUserAgentMiddleware': 400,
    'scrapy.downloadermiddlewares.retry.RetryMiddleware': 90,
    'scrapy.downloadermiddlewares.httpproxy.HttpProxyMiddleware': 110,
}

# Enable pipelines
ITEM_PIPELINES = {
    'myproject.pipelines.ValidationPipeline': 300,
    'myproject.pipelines.CleaningPipeline': 400,
    'myproject.pipelines.DatabasePipeline': 500,
}

# Export format
FEED_FORMAT = 'json'
FEED_URI = 'output/%(name)s_%(time)s.json'
FEED_EXPORT_ENCODING = 'utf-8'
```

**Scrapy Pipelines for Data Processing**:

```python
# myproject/pipelines.py

import re
from scrapy.exceptions import DropItem
import sqlite3

class ValidationPipeline:
    def process_item(self, item, spider):
        # Validate required fields
        required = ['name', 'price', 'url']
        for field in required:
            if not item.get(field):
                raise DropItem(f'Missing {field} in {item}')
        return item

class CleaningPipeline:
    def process_item(self, item, spider):
        # Clean price
        if item.get('price'):
            price_str = re.sub(r'[^\d.]', '', item['price'])
            item['price'] = float(price_str)
        
        # Clean name
        if item.get('name'):
            item['name'] = item['name'].strip()
        
        # Ensure full URL for images
        if item.get('image_url') and not item['image_url'].startswith('http'):
            item['image_url'] = response.urljoin(item['image_url'])
        
        return item

class DatabasePipeline:
    def open_spider(self, spider):
        self.conn = sqlite3.connect('products.db')
        self.cursor = self.conn.cursor()
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS products (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT,
                price REAL,
                url TEXT UNIQUE,
                image_url TEXT,
                description TEXT,
                rating REAL
            )
        ''')
        self.conn.commit()
    
    def close_spider(self, spider):
        self.conn.close()
    
    def process_item(self, item, spider):
        try:
            self.cursor.execute('''
                INSERT OR REPLACE INTO products (name, price, url, image_url, description, rating)
                VALUES (?, ?, ?, ?, ?, ?)
            ''', (
                item.get('name'),
                item.get('price'),
                item.get('url'),
                item.get('image_url'),
                item.get('description'),
                item.get('rating')
            ))
            self.conn.commit()
        except Exception as e:
            spider.logger.error(f'Error saving item: {e}')
        
        return item
```

**Running Scrapy**:

```bash
# Run spider
scrapy crawl products

# Output to JSON
scrapy crawl products -o products.json

# Output to CSV
scrapy crawl products -o products.csv

# Run with custom settings
scrapy crawl products -s CONCURRENT_REQUESTS=32 -s DOWNLOAD_DELAY=0.5
```

### Selenium - Browser Automation

Selenium drives real browsers for scraping JavaScript-heavy sites.

**Installation**:

```bash
pip install selenium webdriver-manager
```

**Basic Selenium Usage**:

```python
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# Setup Chrome driver
options = webdriver.ChromeOptions()
options.add_argument('--headless')  # Run without GUI
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
options.add_argument('user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36')

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), 
                         options=options)

try:
    # Navigate to page
    driver.get('https://example.com/products')
    
    # Wait for element to load
    wait = WebDriverWait(driver, 10)
    products = wait.until(
        EC.presence_of_all_elements_located((By.CLASS_NAME, 'product'))
    )
    
    # Extract data
    for product in products:
        name = product.find_element(By.CLASS_NAME, 'name').text
        price = product.find_element(By.CLASS_NAME, 'price').text
        print(f'{name}: {price}')
    
    # Handle pagination
    while True:
        try:
            next_button = driver.find_element(By.CLASS_NAME, 'next-page')
            next_button.click()
            
            # Wait for new content
            wait.until(EC.staleness_of(products[0]))
            products = driver.find_elements(By.CLASS_NAME, 'product')
            
            # Extract from new page
            for product in products:
                name = product.find_element(By.CLASS_NAME, 'name').text
                price = product.find_element(By.CLASS_NAME, 'price').text
                print(f'{name}: {price}')
        except:
            break  # No more pages

finally:
    driver.quit()
```

**Advanced Selenium Patterns**:

```python
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time

class SeleniumScraper:
    def __init__(self, headless=True):
        options = webdriver.ChromeOptions()
        if headless:
            options.add_argument('--headless')
        options.add_argument('--no-sandbox')
        options.add_argument('--disable-dev-shm-usage')
        options.add_argument('--disable-blink-features=AutomationControlled')
        options.add_experimental_option("excludeSwitches", ["enable-automation"])
        options.add_experimental_option('useAutomationExtension', False)
        
        self.driver = webdriver.Chrome(options=options)
        self.wait = WebDriverWait(self.driver, 10)
    
    def login(self, url, username, password):
        self.driver.get(url)
        
        # Fill login form
        username_field = self.wait.until(
            EC.presence_of_element_located((By.ID, 'username'))
        )
        username_field.send_keys(username)
        
        password_field = self.driver.find_element(By.ID, 'password')
        password_field.send_keys(password)
        
        # Submit
        password_field.send_keys(Keys.RETURN)
        
        # Wait for redirect
        self.wait.until(EC.url_changes(url))
    
    def handle_dropdown(self, dropdown_id, option_text):
        dropdown = Select(self.driver.find_element(By.ID, dropdown_id))
        dropdown.select_by_visible_text(option_text)
    
    def scroll_to_bottom(self):
        # Useful for infinite scroll pages
        last_height = self.driver.execute_script("return document.body.scrollHeight")
        
        while True:
            # Scroll down
            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            
            # Wait for content to load
            time.sleep(2)
            
            # Check if reached bottom
            new_height = self.driver.execute_script("return document.body.scrollHeight")
            if new_height == last_height:
                break
            last_height = new_height
    
    def take_screenshot(self, filename):
        self.driver.save_screenshot(filename)
    
    def execute_js(self, script):
        return self.driver.execute_script(script)
    
    def hover_element(self, element):
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()
    
    def close(self):
        self.driver.quit()

# Usage
scraper = SeleniumScraper(headless=True)
try:
    scraper.login('https://example.com/login', 'user', 'pass')
    scraper.driver.get('https://example.com/data')
    scraper.scroll_to_bottom()
    
    # Extract data
    elements = scraper.driver.find_elements(By.CLASS_NAME, 'item')
    data = [el.text for el in elements]
    
finally:
    scraper.close()
```

### Playwright for Python - Modern Browser Automation

Playwright is a modern alternative to Selenium with better performance and API.

**Installation**:

```bash
pip install playwright
playwright install
```

**Basic Playwright Usage**:

```python
from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    # Launch browser
    browser = p.chromium.launch(headless=True)
    page = browser.new_page()
    
    # Navigate
    page.goto('https://example.com/products')
    
    # Wait for content
    page.wait_for_selector('.product')
    
    # Extract data
    products = page.query_selector_all('.product')
    
    for product in products:
        name = product.query_selector('.name').inner_text()
        price = product.query_selector('.price').inner_text()
        print(f'{name}: {price}')
    
    browser.close()
```

**Advanced Playwright Features**:

```python
from playwright.sync_api import sync_playwright
import json

def scrape_with_playwright():
    with sync_playwright() as p:
        # Launch with custom options
        browser = p.chromium.launch(
            headless=True,
            args=[
                '--no-sandbox',
                '--disable-setuid-sandbox',
                '--disable-dev-shm-usage'
            ]
        )
        
        # Create context with custom settings
        context = browser.new_context(
            viewport={'width': 1920, 'height': 1080},
            user_agent='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36',
            locale='en-US',
            timezone_id='America/New_York'
        )
        
        page = context.new_page()
        
        # Intercept network requests
        def handle_request(request):
            print(f'Request: {request.url}')
        
        def handle_response(response):
            if 'api/products' in response.url:
                # Extract JSON data from API response
                data = response.json()
                print(f'API Data: {data}')
        
        page.on('request', handle_request)
        page.on('response', handle_response)
        
        # Navigate
        page.goto('https://example.com/products', wait_until='networkidle')
        
        # Take screenshot
        page.screenshot(path='screenshot.png', full_page=True)
        
        # Execute JavaScript
        result = page.evaluate('''() => {
            return {
                title: document.title,
                products: Array.from(document.querySelectorAll('.product')).map(el => ({
                    name: el.querySelector('.name').textContent,
                    price: el.querySelector('.price').textContent
                }))
            };
        }''')
        
        print(json.dumps(result, indent=2))
        
        # Handle infinite scroll
        for _ in range(5):
            page.evaluate('window.scrollTo(0, document.body.scrollHeight)')
            page.wait_for_timeout(1000)
        
        # Fill forms
        page.fill('input[name="search"]', 'laptop')
        page.click('button[type="submit"]')
        page.wait_for_load_state('networkidle')
        
        # Extract final data
        products = page.query_selector_all('.product')
        data = []
        for product in products:
            data.append({
                'name': product.query_selector('.name').inner_text(),
                'price': product.query_selector('.price').inner_text(),
                'url': product.query_selector('a').get_attribute('href')
            })
        
        browser.close()
        return data

# Run scraper
products = scrape_with_playwright()
```

**Playwright Async API**:

```python
import asyncio
from playwright.async_api import async_playwright

async def scrape_async():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page()
        
        await page.goto('https://example.com/products')
        await page.wait_for_selector('.product')
        
        products = await page.query_selector_all('.product')
        
        data = []
        for product in products:
            name = await product.query_selector('.name')
            price = await product.query_selector('.price')
            
            data.append({
                'name': await name.inner_text(),
                'price': await price.inner_text()
            })
        
        await browser.close()
        return data

# Run async scraper
products = asyncio.run(scrape_async())
```

---

## Node.js Web Scraping Ecosystem

### Axios - HTTP Client for Node.js

Axios is the most popular HTTP client for Node.js, offering a clean Promise-based API.

**Installation**:

```bash
npm install axios
```

**Basic Axios Usage**:

```javascript
const axios = require('axios');

// Simple GET request
axios.get('https://example.com/api/products')
    .then(response => {
        console.log(response.data);
        console.log(response.status);
        console.log(response.headers);
    })
    .catch(error => {
        console.error('Error:', error.message);
    });

// Async/await
async function fetchProducts() {
    try {
        const response = await axios.get('https://example.com/api/products');
        return response.data;
    } catch (error) {
        console.error('Error:', error.message);
        throw error;
    }
}

// GET with parameters
axios.get('https://example.com/search', {
    params: {
        q: 'laptop',
        page: 2,
        sort: 'price'
    }
})
.then(response => console.log(response.data));

// POST request
axios.post('https://example.com/api/users', {
    name: 'John Doe',
    email: 'john@example.com'
})
.then(response => console.log(response.data));

// Custom headers
axios.get('https://example.com', {
    headers: {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36',
        'Accept': 'application/json',
        'Authorization': 'Bearer token123'
    }
})
.then(response => console.log(response.data));
```

**Advanced Axios Configuration**:

```javascript
const axios = require('axios');

// Create instance with default config
const client = axios.create({
    baseURL: 'https://api.example.com',
    timeout: 10000,
    headers: {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36',
        'Accept': 'application/json'
    }
});

// Add request interceptor
client.interceptors.request.use(
    config => {
        console.log(`Requesting: ${config.url}`);
        // Add auth token
        config.headers.Authorization = `Bearer ${getToken()}`;
        return config;
    },
    error => Promise.reject(error)
);

// Add response interceptor
client.interceptors.response.use(
    response => {
        console.log(`Response: ${response.status}`);
        return response;
    },
    error => {
        if (error.response) {
            console.error(`Error ${error.response.status}: ${error.response.data}`);
        }
        return Promise.reject(error);
    }
);

// Usage
async function scrapeAPI() {
    try {
        const response = await client.get('/products', {
            params: { category: 'electronics' }
        });
        return response.data;
    } catch (error) {
        console.error('Scraping failed:', error.message);
        throw error;
    }
}
```

**Axios with Retry Logic**:

```javascript
const axios = require('axios');
const axiosRetry = require('axios-retry');

const client = axios.create();

axiosRetry(client, {
    retries: 3,
    retryDelay: axiosRetry.exponentialDelay,
    retryCondition: (error) => {
        return axiosRetry.isNetworkOrIdempotentRequestError(error) ||
               error.response?.status === 429;
    }
});

async function fetchWithRetry(url) {
    const response = await client.get(url);
    return response.data;
}
```

### Cheerio - Fast HTML Parsing

Cheerio is a fast, flexible jQuery-like library for parsing HTML in Node.js.

**Installation**:

```bash
npm install cheerio axios
```

**Basic Cheerio Usage**:

```javascript
const axios = require('axios');
const cheerio = require('cheerio');

async function scrapeProducts() {
    // Fetch HTML
    const response = await axios.get('https://example.com/products');
    const html = response.data;
    
    // Load HTML into Cheerio
    const $ = cheerio.load(html);
    
    // Extract data
    const products = [];
    
    $('.product').each((index, element) => {
        const $element = $(element);
        
        const product = {
            name: $element.find('.name').text().trim(),
            price: $element.find('.price').text().trim(),
            url: $element.find('a').attr('href'),
            imageUrl: $element.find('img').attr('src'),
            rating: parseFloat($element.find('.rating').attr('data-rating'))
        };
        
        products.push(product);
    });
    
    return products;
}

scrapeProducts()
    .then(products => {
        console.log(`Scraped ${products.length} products`);
        console.log(JSON.stringify(products, null, 2));
    })
    .catch(error => {
        console.error('Error:', error.message);
    });
```

**Advanced Cheerio Patterns**:

```javascript
const cheerio = require('cheerio');

function extractProductDetails(html) {
    const $ = cheerio.load(html);
    
    // CSS selectors
    const name = $('h1.product-name').text();
    const price = $('.price.current').text();
    
    // Attribute extraction
    const productId = $('.product').attr('data-id');
    const imageUrl = $('img.main-image').attr('src');
    
    // Multiple elements
    const features = [];
    $('ul.features li').each((i, el) => {
        features.push($(el).text().trim());
    });
    
    // Navigate DOM
    const description = $('.description').find('p').first().text();
    const siblings = $('.price').siblings('.discount').text();
    const parent = $('.price').parent().attr('class');
    
    // Filter elements
    const inStockItems = $('.product').filter((i, el) => {
        return $(el).find('.stock').text() === 'In Stock';
    });
    
    // Map elements
    const prices = $('.product .price').map((i, el) => {
        return $(el).text().replace(/[^0-9.]/g, '');
    }).get();
    
    // Check existence
    const hasDiscount = $('.discount').length > 0;
    
    // HTML content
    const innerHtml = $('.description').html();
    
    // Extract from data attributes
    const metadata = {};
    $('.product').each((i, el) => {
        const $el = $(el);
        $.each($el[0].attribs, (key, value) => {
            if (key.startsWith('data-')) {
                metadata[key.replace('data-', '')] = value;
            }
        });
    });
    
    return {
        name,
        price,
        productId,
        imageUrl,
        features,
        description,
        metadata,
        hasDiscount
    };
}
```

**Cheerio with Pagination**:

```javascript
const axios = require('axios');
const cheerio = require('cheerio');

async function scrapeAllPages(baseUrl, maxPages = 10) {
    const allProducts = [];
    
    for (let page = 1; page <= maxPages; page++) {
        const url = `${baseUrl}?page=${page}`;
        console.log(`Scraping page ${page}: ${url}`);
        
        try {
            const response = await axios.get(url);
            const $ = cheerio.load(response.data);
            
            const products = [];
            $('.product').each((i, el) => {
                const $el = $(el);
                products.push({
                    name: $el.find('.name').text().trim(),
                    price: $el.find('.price').text().trim(),
                    url: $el.find('a').attr('href')
                });
            });
            
            if (products.length === 0) {
                console.log(`No products on page ${page}, stopping`);
                break;
            }
            
            allProducts.push(...products);
            
            // Check for next page
            const nextPage = $('a.next-page').attr('href');
            if (!nextPage) {
                console.log('No next page link, stopping');
                break;
            }
            
            // Respectful delay
            await new Promise(resolve => setTimeout(resolve, 2000));
            
        } catch (error) {
            console.error(`Error on page ${page}:`, error.message);
            break;
        }
    }
    
    return allProducts;
}

scrapeAllPages('https://example.com/products', 5)
    .then(products => {
        console.log(`Total products scraped: ${products.length}`);
    });
```

### Puppeteer - Headless Chrome for Node.js

Puppeteer provides a high-level API to control Chrome/Chromium.

**Installation**:

```bash
npm install puppeteer
```

**Basic Puppeteer Usage**:

```javascript
const puppeteer = require('puppeteer');

(async () => {
    // Launch browser
    const browser = await puppeteer.launch({
        headless: true,
        args: ['--no-sandbox', '--disable-setuid-sandbox']
    });
    
    const page = await browser.newPage();
    
    // Set viewport
    await page.setViewport({ width: 1920, height: 1080 });
    
    // Navigate
    await page.goto('https://example.com/products', {
        waitUntil: 'networkidle2'
    });
    
    // Extract data
    const products = await page.evaluate(() => {
        const items = [];
        document.querySelectorAll('.product').forEach(product => {
            items.push({
                name: product.querySelector('.name').textContent,
                price: product.querySelector('.price').textContent,
                url: product.querySelector('a').href
            });
        });
        return items;
    });
    
    console.log(`Scraped ${products.length} products`);
    console.log(products);
    
    await browser.close();
})();
```

**Advanced Puppeteer Patterns**:

```javascript
const puppeteer = require('puppeteer');

class PuppeteerScraper {
    async initialize() {
        this.browser = await puppeteer.launch({
            headless: true,
            args: [
                '--no-sandbox',
                '--disable-setuid-sandbox',
                '--disable-dev-shm-usage',
                '--disable-accelerated-2d-canvas',
                '--disable-gpu'
            ]
        });
        
        this.page = await this.browser.newPage();
        
        // Set user agent
        await this.page.setUserAgent(
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
        );
        
        // Block unnecessary resources
        await this.page.setRequestInterception(true);
        this.page.on('request', (request) => {
            const resourceType = request.resourceType();
            if (['image', 'stylesheet', 'font', 'media'].includes(resourceType)) {
                request.abort();
            } else {
                request.continue();
            }
        });
    }
    
    async login(url, username, password) {
        await this.page.goto(url);
        
        await this.page.type('#username', username);
        await this.page.type('#password', password);
        await this.page.click('button[type="submit"]');
        
        await this.page.waitForNavigation();
    }
    
    async scrapeProducts(url) {
        await this.page.goto(url, { waitUntil: 'networkidle2' });
        
        // Wait for products to load
        await this.page.waitForSelector('.product');
        
        // Handle infinite scroll
        await this.autoScroll();
        
        // Extract data
        const products = await this.page.evaluate(() => {
            const items = [];
            document.querySelectorAll('.product').forEach(product => {
                items.push({
                    name: product.querySelector('.name')?.textContent || '',
                    price: product.querySelector('.price')?.textContent || '',
                    url: product.querySelector('a')?.href || '',
                    imageUrl: product.querySelector('img')?.src || '',
                    rating: product.querySelector('.rating')?.getAttribute('data-rating') || null
                });
            });
            return items;
        });
        
        return products;
    }
    
    async autoScroll() {
        await this.page.evaluate(async () => {
            await new Promise((resolve) => {
                let totalHeight = 0;
                const distance = 100;
                const timer = setInterval(() => {
                    const scrollHeight = document.body.scrollHeight;
                    window.scrollBy(0, distance);
                    totalHeight += distance;
                    
                    if (totalHeight >= scrollHeight) {
                        clearInterval(timer);
                        resolve();
                    }
                }, 100);
            });
        });
    }
    
    async takeScreenshot(path) {
        await this.page.screenshot({
            path,
            fullPage: true
        });
    }
    
    async interceptAPIRequests() {
        const apiData = [];
        
        this.page.on('response', async (response) => {
            const url = response.url();
            if (url.includes('/api/') && response.status() === 200) {
                try {
                    const data = await response.json();
                    apiData.push({ url, data });
                } catch (e) {
                    // Not JSON
                }
            }
        });
        
        return apiData;
    }
    
    async close() {
        if (this.browser) {
            await this.browser.close();
        }
    }
}

// Usage
(async () => {
    const scraper = new PuppeteerScraper();
    await scraper.initialize();
    
    try {
        await scraper.login('https://example.com/login', 'user', 'pass');
        const products = await scraper.scrapeProducts('https://example.com/products');
        console.log(`Scraped ${products.length} products`);
        
        await scraper.takeScreenshot('screenshot.png');
    } finally {
        await scraper.close();
    }
})();
```

**Puppeteer Stealth Plugin**:

```javascript
const puppeteer = require('puppeteer-extra');
const StealthPlugin = require('puppeteer-extra-plugin-stealth');

puppeteer.use(StealthPlugin());

(async () => {
    const browser = await puppeteer.launch({ headless: true });
    const page = await browser.newPage();
    
    // Navigate with stealth
    await page.goto('https://example.com');
    
    // The stealth plugin makes the browser harder to detect
    const isDetected = await page.evaluate(() => {
        return navigator.webdriver;
    });
    
    console.log('Detected as bot:', isDetected);  // Should be false
    
    await browser.close();
})();
```

### Playwright for Node.js

Playwright offers similar functionality to Puppeteer but supports multiple browsers.

**Installation**:

```bash
npm install playwright
```

**Basic Playwright Usage**:

```javascript
const { chromium } = require('playwright');

(async () => {
    const browser = await chromium.launch({ headless: true });
    const page = await browser.newPage();
    
    await page.goto('https://example.com/products');
    
    // Wait for selector
    await page.waitForSelector('.product');
    
    // Extract data
    const products = await page.$$eval('.product', products => {
        return products.map(product => ({
            name: product.querySelector('.name').textContent,
            price: product.querySelector('.price').textContent,
            url: product.querySelector('a').href
        }));
    });
    
    console.log(products);
    
    await browser.close();
})();
```

**Advanced Playwright Features**:

```javascript
const { chromium } = require('playwright');

async function scrapeWithPlaywright() {
    const browser = await chromium.launch({
        headless: true,
        args: ['--no-sandbox']
    });
    
    const context = await browser.newContext({
        viewport: { width: 1920, height: 1080 },
        userAgent: 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36',
        locale: 'en-US',
        timezoneId: 'America/New_York'
    });
    
    const page = await context.newPage();
    
    // Intercept requests
    await page.route('**/*', (route) => {
        const resourceType = route.request().resourceType();
        if (['image', 'stylesheet', 'font'].includes(resourceType)) {
            route.abort();
        } else {
            route.continue();
        }
    });
    
    // Listen to API responses
    page.on('response', async (response) => {
        if (response.url().includes('/api/products')) {
            const data = await response.json();
            console.log('API Data:', data);
        }
    });
    
    await page.goto('https://example.com/products', {
        waitUntil: 'networkidle'
    });
    
    // Handle pagination
    let allProducts = [];
    let hasNextPage = true;
    
    while (hasNextPage) {
        // Extract products from current page
        const products = await page.$$eval('.product', els => {
            return els.map(el => ({
                name: el.querySelector('.name').textContent,
                price: el.querySelector('.price').textContent
            }));
        });
        
        allProducts.push(...products);
        
        // Try to click next page
        try {
            await page.click('a.next-page', { timeout: 5000 });
            await page.waitForLoadState('networkidle');
        } catch {
            hasNextPage = false;
        }
    }
    
    await browser.close();
    return allProducts;
}

scrapeWithPlaywright()
    .then(products => {
        console.log(`Total products: ${products.length}`);
    })
    .catch(console.error);
```

### Crawlee - Web Scraping Framework

Crawlee (formerly Apify SDK) is a comprehensive web scraping and crawling framework.

**Installation**:

```bash
npm install crawlee
```

**Basic Crawlee Usage**:

```javascript
const { CheerioCrawler, Dataset } = require('crawlee');

const crawler = new CheerioCrawler({
    maxRequestsPerCrawl: 100,
    requestHandlerTimeoutSecs: 120,
    
    async requestHandler({ request, $, enqueueLinks }) {
        console.log(`Processing: ${request.url}`);
        
        // Extract products
        const products = [];
        $('.product').each((i, el) => {
            products.push({
                name: $(el).find('.name').text(),
                price: $(el).find('.price').text(),
                url: $(el).find('a').attr('href')
            });
        });
        
        // Save to dataset
        await Dataset.pushData(products);
        
        // Enqueue pagination links
        await enqueueLinks({
            selector: 'a.next-page',
            label: 'LISTING'
        });
    },
    
    failedRequestHandler({ request }) {
        console.error(`Request ${request.url} failed`);
    }
});

await crawler.run(['https://example.com/products']);
```

**Playwright Crawler with Crawlee**:

```javascript
const { PlaywrightCrawler, Dataset } = require('crawlee');

const crawler = new PlaywrightCrawler({
    launchContext: {
        launchOptions: {
            headless: true
        }
    },
    
    async requestHandler({ request, page, enqueueLinks }) {
        console.log(`Processing: ${request.url}`);
        
        // Wait for content
        await page.waitForSelector('.product');
        
        // Handle infinite scroll
        await page.evaluate(async () => {
            await new Promise((resolve) => {
                let totalHeight = 0;
                const distance = 100;
                const timer = setInterval(() => {
                    window.scrollBy(0, distance);
                    totalHeight += distance;
                    
                    if (totalHeight >= document.body.scrollHeight) {
                        clearInterval(timer);
                        resolve();
                    }
                }, 100);
            });
        });
        
        // Extract data
        const products = await page.$$eval('.product', els => {
            return els.map(el => ({
                name: el.querySelector('.name').textContent,
                price: el.querySelector('.price').textContent,
                url: el.querySelector('a').href
            }));
        });
        
        await Dataset.pushData(products);
        
        // Enqueue links
        await enqueueLinks({
            selector: 'a.category-link'
        });
    }
});

await crawler.run(['https://example.com/products']);
```

---

## Headless Browser Scraping

### Chrome Headless Deep Dive

Chrome headless mode runs the full Chrome browser without a GUI, enabling JavaScript execution and realistic browsing behavior.

**Why Use Headless Browsers**:

1. **JavaScript Execution**: Required for SPAs (Single Page Applications) built with React, Vue, Angular
2. **Dynamic Content**: Handles AJAX-loaded content, infinite scroll, lazy loading
3. **Realistic Behavior**: Acts like a real browser, harder to detect
4. **Screenshots/PDFs**: Can capture visual content
5. **Complex Interactions**: Handle hover menus, dropdowns, multi-step forms

**Performance Considerations**:

Headless browsers are significantly slower than simple HTTP requests:
- HTTP request: 50-200ms
- Headless browser: 2-10 seconds per page

Use headless browsers only when necessary. For many sites, you can:
1. Find the API endpoints the JavaScript calls
2. Replicate those API calls directly
3. Avoid the overhead of running a full browser

**Optimization Strategies**:

```javascript
const puppeteer = require('puppeteer');

async function optimizedScraping() {
    const browser = await puppeteer.launch({
        headless: true,
        args: [
            '--no-sandbox',
            '--disable-setuid-sandbox',
            '--disable-dev-shm-usage',
            '--disable-accelerated-2d-canvas',
            '--no-first-run',
            '--no-zygote',
            '--single-process',  // For Docker
            '--disable-gpu'
        ]
    });
    
    const page = await browser.newPage();
    
    // Reduce page size by blocking unnecessary resources
    await page.setRequestInterception(true);
    page.on('request', (req) => {
        const resourceType = req.resourceType();
        const blockList = ['image', 'stylesheet', 'font', 'media'];
        
        if (blockList.includes(resourceType)) {
            req.abort();
        } else {
            req.continue();
        }
    });
    
    // Disable JavaScript features that aren't needed
    await page.evaluateOnNewDocument(() => {
        // Disable animations
        document.addEventListener('DOMContentLoaded', () => {
            const style = document.createElement('style');
            style.textContent = `
                * {
                    animation-duration: 0s !important;
                    transition-duration: 0s !important;
                }
            `;
            document.head.appendChild(style);
        });
    });
    
    // Navigate with optimized wait
    await page.goto('https://example.com/products', {
        waitUntil: 'domcontentloaded'  // Don't wait for all resources
    });
    
    // Extract data as soon as DOM is ready
    const products = await page.evaluate(() => {
        // Fast data extraction
        return Array.from(document.querySelectorAll('.product'), el => ({
            name: el.querySelector('.name')?.textContent,
            price: el.querySelector('.price')?.textContent
        }));
    });
    
    await browser.close();
    return products;
}
```

### Stealth Techniques for Headless Browsers

Anti-bot systems detect headless browsers through various signals. Here's how to evade detection:

**1. Navigator Properties**:

Headless browsers have telltale navigator properties:

```javascript
// Puppeteer Stealth
const puppeteer = require('puppeteer-extra');
const StealthPlugin = require('puppeteer-extra-plugin-stealth');

puppeteer.use(StealthPlugin());

const browser = await puppeteer.launch({ headless: true });
```

**2. Manual Evasion**:

```javascript
const browser = await puppeteer.launch({ headless: true });
const page = await browser.newPage();

// Override navigator properties
await page.evaluateOnNewDocument(() => {
    // Remove webdriver flag
    Object.defineProperty(navigator, 'webdriver', {
        get: () => false
    });
    
    // Mock plugins
    Object.defineProperty(navigator, 'plugins', {
        get: () => [1, 2, 3, 4, 5]
    });
    
    // Mock languages
    Object.defineProperty(navigator, 'languages', {
        get: () => ['en-US', 'en']
    });
    
    // Chrome specific
    window.chrome = {
        runtime: {}
    };
    
    // Permissions
    const originalQuery = window.navigator.permissions.query;
    window.navigator.permissions.query = (parameters) => (
        parameters.name === 'notifications' ?
            Promise.resolve({ state: Notification.permission }) :
            originalQuery(parameters)
    );
});
```

**3. Playwright Stealth**:

Playwright is harder to detect by default:

```javascript
const { chromium } = require('playwright');

const browser = await chromium.launch({
    headless: true,
    args: [
        '--disable-blink-features=AutomationControlled'
    ]
});

const context = await browser.newContext({
    userAgent: 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36',
    viewport: { width: 1920, height: 1080 },
    locale: 'en-US',
    timezoneId: 'America/New_York',
    permissions: ['geolocation']
});
```

**4. Realistic User Behavior**:

```javascript
async function humanLikeInteraction(page) {
    // Random mouse movements
    await page.mouse.move(
        Math.random() * 1920,
        Math.random() * 1080
    );
    
    // Random delays
    await page.waitForTimeout(Math.random() * 2000 + 1000);
    
    // Random scrolling
    await page.evaluate(() => {
        window.scrollBy(0, Math.random() * 500);
    });
    
    await page.waitForTimeout(Math.random() * 1000 + 500);
}
```

### Handling JavaScript-Heavy Sites

**Wait Strategies**:

Different waiting strategies for different scenarios:

```python
# Selenium
from selenium.webdriver.support import expected_conditions as EC

# Wait for element
wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'product')))

# Wait for element to be visible
wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'product')))

# Wait for element to be clickable
wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'button')))

# Wait for specific text
wait.until(EC.text_to_be_present_in_element((By.CLASS_NAME, 'status'), 'Loaded'))

# Custom condition
wait.until(lambda driver: len(driver.find_elements(By.CLASS_NAME, 'product')) > 10)
```

```javascript
// Puppeteer
// Wait for selector
await page.waitForSelector('.product');

// Wait for function
await page.waitForFunction(() => {
    return document.querySelectorAll('.product').length > 10;
});

// Wait for navigation
await Promise.all([
    page.click('a.link'),
    page.waitForNavigation()
]);

// Wait for specific network response
await page.waitForResponse(response => {
    return response.url().includes('/api/products') && response.status() === 200;
});

// Wait for timeout (last resort)
await page.waitForTimeout(5000);
```

**Handling AJAX Requests**:

```javascript
// Intercept and extract data from AJAX
const puppeteer = require('puppeteer');

const browser = await puppeteer.launch();
const page = await browser.newPage();

// Collect API responses
const apiData = [];

page.on('response', async (response) => {
    const url = response.url();
    
    if (url.includes('/api/products') && response.status() === 200) {
        try {
            const data = await response.json();
            apiData.push(data);
            console.log('Captured API data:', data);
        } catch (e) {
            // Not JSON
        }
    }
});

await page.goto('https://example.com/products');

// apiData now contains the JSON responses
console.log('Total API calls captured:', apiData.length);
```

### Browser Fingerprinting

Modern anti-bot systems fingerprint browsers based on dozens of attributes. Here's a comprehensive evasion guide:

**Canvas Fingerprinting**:

```javascript
await page.evaluateOnNewDocument(() => {
    // Canvas fingerprinting evasion
    const originalToDataURL = HTMLCanvasElement.prototype.toDataURL;
    HTMLCanvasElement.prototype.toDataURL = function(type) {
        // Add noise to canvas
        const context = this.getContext('2d');
        const imageData = context.getImageData(0, 0, this.width, this.height);
        
        for (let i = 0; i < imageData.data.length; i += 4) {
            imageData.data[i] += Math.floor(Math.random() * 10) - 5;
        }
        
        context.putImageData(imageData, 0, 0);
        return originalToDataURL.apply(this, arguments);
    };
});
```

**WebGL Fingerprinting**:

```javascript
await page.evaluateOnNewDocument(() => {
    const getParameter = WebGLRenderingContext.prototype.getParameter;
    WebGLRenderingContext.prototype.getParameter = function(parameter) {
        // Spoof WebGL vendor and renderer
        if (parameter === 37445) {
            return 'Intel Inc.';
        }
        if (parameter === 37446) {
            return 'Intel Iris OpenGL Engine';
        }
        return getParameter.apply(this, arguments);
    };
});
```

**AudioContext Fingerprinting**:

```javascript
await page.evaluateOnNewDocument(() => {
    const audioContext = window.AudioContext || window.webkitAudioContext;
    if (audioContext) {
        const originalCreateAnalyser = audioContext.prototype.createAnalyser;
        audioContext.prototype.createAnalyser = function() {
            const analyser = originalCreateAnalyser.apply(this, arguments);
            const originalGetFloatFrequencyData = analyser.getFloatFrequencyData;
            analyser.getFloatFrequencyData = function(array) {
                originalGetFloatFrequencyData.apply(this, arguments);
                // Add noise
                for (let i = 0; i < array.length; i++) {
                    array[i] += Math.random() * 0.0001;
                }
            };
            return analyser;
        };
    }
});
```

**Font Fingerprinting**:

```javascript
await page.evaluateOnNewDocument(() => {
    // Randomize font measurements
    const originalOffsetWidth = Object.getOwnPropertyDescriptor(
        HTMLElement.prototype,
        'offsetWidth'
    );
    
    Object.defineProperty(HTMLElement.prototype, 'offsetWidth', {
        get() {
            const width = originalOffsetWidth.get.call(this);
            return width + Math.floor(Math.random() * 3) - 1;
        }
    });
});
```

### Browser Pools for Scalability

For large-scale scraping, maintain a pool of browser instances:

```javascript
const puppeteer = require('puppeteer');

class BrowserPool {
    constructor(size = 5) {
        this.size = size;
        this.browsers = [];
        this.available = [];
        this.queue = [];
    }
    
    async initialize() {
        for (let i = 0; i < this.size; i++) {
            const browser = await puppeteer.launch({
                headless: true,
                args: ['--no-sandbox']
            });
            this.browsers.push(browser);
            this.available.push(browser);
        }
    }
    
    async acquire() {
        if (this.available.length > 0) {
            return this.available.pop();
        }
        
        // Wait for available browser
        return new Promise((resolve) => {
            this.queue.push(resolve);
        });
    }
    
    release(browser) {
        if (this.queue.length > 0) {
            const resolve = this.queue.shift();
            resolve(browser);
        } else {
            this.available.push(browser);
        }
    }
    
    async closeAll() {
        await Promise.all(this.browsers.map(b => b.close()));
    }
}

// Usage
const pool = new BrowserPool(5);
await pool.initialize();

async function scrapeWithPool(url) {
    const browser = await pool.acquire();
    
    try {
        const page = await browser.newPage();
        await page.goto(url);
        
        const data = await page.evaluate(() => {
            // Extract data
            return { title: document.title };
        });
        
        await page.close();
        return data;
    } finally {
        pool.release(browser);
    }
}

// Scrape multiple URLs concurrently
const urls = ['url1', 'url2', 'url3', 'url4', 'url5', 'url6', 'url7', 'url8'];
const results = await Promise.all(urls.map(url => scrapeWithPool(url)));

await pool.closeAll();
```

---

## Anti-Bot Detection Systems

### Understanding Anti-Bot Technologies

Modern websites employ sophisticated systems to detect and block bots. Understanding these systems is crucial for successful scraping.

**Detection Layers**:

1. **Network Layer**: IP reputation, rate limiting, geographic restrictions
2. **TLS Layer**: TLS fingerprinting (JA3/JA4)
3. **HTTP Layer**: User-Agent, headers, cookies
4. **Browser Layer**: JavaScript challenges, browser fingerprinting
5. **Behavioral Layer**: Mouse movements, typing patterns, navigation patterns

### Cloudflare Bot Protection

Cloudflare is one of the most common anti-bot systems, protecting millions of websites.

**Cloudflare Detection Mechanisms**:

**1. Challenge Page (JavaScript Challenge)**:
- Presents a "Checking your browser" page
- Executes JavaScript to verify browser capabilities
- Sets challenge cookies upon success

**2. CAPTCHA Challenge**:
- Presents visual or behavioral CAPTCHA
- Requires human interaction

**3. Rate Limiting**:
- Monitors request frequency per IP
- Temporarily blocks suspicious IPs

**4. TLS Fingerprinting**:
- Analyzes TLS handshake characteristics
- Compares against known bot signatures

**Bypassing Cloudflare**:

**Method 1: Use Real Browsers**:

```python
# Using Playwright with stealth
from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch()
    context = browser.new_context(
        user_agent='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
    )
    page = context.new_page()
    
    # Navigate and wait for Cloudflare check
    page.goto('https://cloudflare-protected-site.com')
    page.wait_for_load_state('networkidle')
    
    # Now the page is accessible
    content = page.content()
```

**Method 2: Extract Cookies from Browser**:

```python
# Get cookies after manually solving challenge
import pickle
from selenium import webdriver

driver = webdriver.Chrome()
driver.get('https://cloudflare-protected-site.com')

# Wait for manual challenge completion
input("Press Enter after solving challenge...")

# Save cookies
cookies = driver.get_cookies()
with open('cf_cookies.pkl', 'wb') as f:
    pickle.dump(cookies, f)

driver.quit()

# Use cookies in requests
import requests

with open('cf_cookies.pkl', 'rb') as f:
    cookies = pickle.load(f)

session = requests.Session()
for cookie in cookies:
    session.cookies.set(cookie['name'], cookie['value'])

response = session.get('https://cloudflare-protected-site.com')
```

**Method 3: Third-Party Services**:

```python
# Using ScraperAPI (bypasses Cloudflare)
import requests

api_key = 'your_scraperapi_key'
url = 'https://cloudflare-protected-site.com'

response = requests.get(
    'http://api.scraperapi.com',
    params={
        'api_key': api_key,
        'url': url
    }
)

# ScraperAPI handles Cloudflare bypass
print(response.text)
```

**Method 4: cloudscraper Library**:

```python
import cloudscraper

scraper = cloudscraper.create_scraper()
response = scraper.get('https://cloudflare-protected-site.com')

# Automatically handles JavaScript challenge
print(response.text)
```

### Akamai Bot Manager

Akamai provides enterprise-grade bot protection.

**Akamai Detection Methods**:
- Sensor data collection (mouse movements, keystrokes)
- Browser fingerprinting
- Behavioral analysis
- Machine learning-based detection

**Bypassing Akamai**:

Akamai is significantly harder to bypass than Cloudflare. Strategies:

**1. Use Real Browsers with Stealth**:

```javascript
const puppeteer = require('puppeteer-extra');
const StealthPlugin = require('puppeteer-extra-plugin-stealth');

puppeteer.use(StealthPlugin());

const browser = await puppeteer.launch({ headless: false });  // Headed mode is harder to detect
const page = await browser.newPage();

// Add realistic behavior
await page.evaluateOnNewDocument(() => {
    // Spoof timezone
    Object.defineProperty(Date.prototype, 'getTimezoneOffset', {
        value: function() {
            return -300;  // EST
        }
    });
});

await page.goto('https://akamai-protected-site.com');

// Simulate human behavior
await page.mouse.move(100, 200);
await page.waitForTimeout(Math.random() * 2000 + 1000);
await page.mouse.move(300, 400);

// Extract data
const content = await page.content();
```

**2. Residential Proxies**:

Akamai heavily weights IP reputation. Residential proxies are essential:

```python
import requests

proxies = {
    'http': 'http://user:pass@residential-proxy.com:8000',
    'https': 'http://user:pass@residential-proxy.com:8000'
}

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
}

response = requests.get(
    'https://akamai-protected-site.com',
    proxies=proxies,
    headers=headers
)
```

**3. Session Persistence**:

Maintain long-lived sessions with consistent behavior:

```python
import requests
import time
import random

session = requests.Session()

# Establish session gradually
session.get('https://akamai-protected-site.com')
time.sleep(random.uniform(2, 5))

session.get('https://akamai-protected-site.com/category')
time.sleep(random.uniform(2, 5))

# Now access target page
response = session.get('https://akamai-protected-site.com/data')
```

### PerimeterX (HUMAN Security)

PerimeterX provides behavioral-based bot detection.

**Detection Methods**:
- JavaScript challenges
- Behavioral biometrics
- Device fingerprinting
- Risk scoring

**Bypassing PerimeterX**:

```javascript
const puppeteer = require('puppeteer-extra');
const StealthPlugin = require('puppeteer-extra-plugin-stealth');
const AdblockerPlugin = require('puppeteer-extra-plugin-adblocker');

puppeteer.use(StealthPlugin());
puppeteer.use(AdblockerPlugin({ blockTrackers: true }));

async function bypassPerimeterX() {
    const browser = await puppeteer.launch({
        headless: false,
        args: [
            '--disable-blink-features=AutomationControlled',
            '--disable-features=IsolateOrigins,site-per-process'
        ]
    });
    
    const page = await browser.newPage();
    
    // Set realistic viewport
    await page.setViewport({
        width: 1920 + Math.floor(Math.random() * 100),
        height: 1080 + Math.floor(Math.random() * 100)
    });
    
    // Override navigator properties
    await page.evaluateOnNewDocument(() => {
        Object.defineProperty(navigator, 'webdriver', {
            get: () => undefined
        });
        
        Object.defineProperty(navigator, 'plugins', {
            get: () => [1, 2, 3, 4, 5]
        });
        
        // Randomize hardware concurrency
        Object.defineProperty(navigator, 'hardwareConcurrency', {
            get: () => 4 + Math.floor(Math.random() * 4)
        });
    });
    
    await page.goto('https://perimeterx-protected-site.com', {
        waitUntil: 'networkidle0'
    });
    
    // Simulate human behavior
    await page.mouse.move(
        Math.random() * 1920,
        Math.random() * 1080,
        { steps: 10 }
    );
    
    await page.waitForTimeout(Math.random() * 3000 + 2000);
    
    // Scroll naturally
    await page.evaluate(() => {
        window.scrollBy({
            top: 300,
            behavior: 'smooth'
        });
    });
    
    await page.waitForTimeout(1000);
    
    // Extract data
    const data = await page.evaluate(() => {
        return {
            title: document.title,
            content: document.body.innerText
        };
    });
    
    return data;
}
```

### DataDome

DataDome uses AI/ML for bot detection.

**Detection Methods**:
- Real-time ML model scoring
- Device fingerprinting
- Behavioral analysis
- Bot signature detection

**Bypassing DataDome**:

DataDome is particularly challenging. Best approaches:

**1. Residential Proxies + Real Browsers**:

```python
from playwright.sync_api import sync_playwright

def scrape_datadome_protected():
    with sync_playwright() as p:
        browser = p.chromium.launch(
            headless=False,
            proxy={
                'server': 'http://residential-proxy.com:8000',
                'username': 'user',
                'password': 'pass'
            }
        )
        
        context = browser.new_context(
            user_agent='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36',
            viewport={'width': 1920, 'height': 1080},
            locale='en-US',
            timezone_id='America/New_York'
        )
        
        page = context.new_page()
        page.goto('https://datadome-protected-site.com')
        
        # Wait for bot check
        page.wait_for_load_state('networkidle')
        
        # Extract data
        content = page.content()
        
        browser.close()
        return content
```

**2. Solve DataDome Challenges**:

DataDome sometimes presents CAPTCHA challenges. Use CAPTCHA solving services:

```python
import requests
from twocaptcha import TwoCaptcha

def solve_datadome_captcha(site_url, captcha_url):
    solver = TwoCaptcha('your_2captcha_api_key')
    
    try:
        result = solver.funcaptcha(
            sitekey='DataDome_site_key',
            url=site_url
        )
        
        return result['code']
    except Exception as e:
        print(f'Error solving CAPTCHA: {e}')
        return None

# Use solved CAPTCHA token
captcha_token = solve_datadome_captcha('https://example.com', 'captcha_url')

if captcha_token:
    # Include token in request
    response = requests.post(
        'https://example.com/verify',
        data={'captcha_token': captcha_token}
    )
```

### reCAPTCHA and hCaptcha

**reCAPTCHA v2**:

Presents image-based challenges.

```python
from twocaptcha import TwoCaptcha

solver = TwoCaptcha('your_api_key')

result = solver.recaptcha(
    sitekey='6Le-wvkSAAAAAPBMRTvw0Q4Muexq9bi0DJwx_mJ-',
    url='https://www.google.com/recaptcha/api2/demo'
)

captcha_response = result['code']

# Use captcha_response in form submission
```

**reCAPTCHA v3**:

Invisible, score-based system (0.0 to 1.0):

- 0.0-0.4: Likely bot
- 0.5-0.7: Suspicious
- 0.8-1.0: Likely human

Bypass strategies:
1. Use real browsers with human-like behavior
2. Build up account reputation over time
3. Use services like 2Captcha that can solve v3

**hCaptcha**:

Similar to reCAPTCHA v2:

```python
result = solver.hcaptcha(
    sitekey='hcaptcha_site_key',
    url='https://example.com'
)

captcha_response = result['code']
```

### General Anti-Bot Evasion Strategies

**1. Rotate User Agents**:

```python
from fake_useragent import UserAgent

ua = UserAgent()

headers = {
    'User-Agent': ua.random
}

response = requests.get('https://example.com', headers=headers)
```

**2. Rotate Proxies**:

```python
import random

proxies_list = [
    {'http': 'http://proxy1:8000', 'https': 'http://proxy1:8000'},
    {'http': 'http://proxy2:8000', 'https': 'http://proxy2:8000'},
    {'http': 'http://proxy3:8000', 'https': 'http://proxy3:8000'},
]

def get_random_proxy():
    return random.choice(proxies_list)

response = requests.get('https://example.com', proxies=get_random_proxy())
```

**3. Implement Random Delays**:

```python
import time
import random

def random_delay(min_seconds=1, max_seconds=5):
    time.sleep(random.uniform(min_seconds, max_seconds))

for url in urls:
    response = requests.get(url)
    process_data(response)
    random_delay(2, 5)
```

**4. Respect Rate Limits**:

```python
from ratelimit import limits, sleep_and_retry

@sleep_and_retry
@limits(calls=10, period=60)  # 10 calls per minute
def fetch_url(url):
    return requests.get(url)

for url in urls:
    response = fetch_url(url)
```

**5. Session Management**:

```python
session = requests.Session()

# Build session gradually
session.get('https://example.com')
time.sleep(2)

session.get('https://example.com/about')
time.sleep(2)

# Now scrape target
response = session.get('https://example.com/data')
```

---

## Proxy Management and Rotation

### Types of Proxies

**Datacenter Proxies**:
- Fast and cheap
- Shared IP pools
- Easily detected and blocked
- Good for: Low-security sites, high-volume scraping

**Residential Proxies**:
- Real residential IPs
- Harder to detect
- More expensive
- Good for: Protected sites, e-commerce, social media

**ISP Proxies** (Static Residential):
- Datacenter-hosted with residential IPs
- Fast like datacenter, trusted like residential
- Medium price
- Good for: Balance of speed and trust

**Mobile Proxies**:
- IPs from mobile carriers (4G/5G)
- Very hard to block (many users share same IP)
- Most expensive
- Good for: Social media, mobile-focused sites

### Proxy Providers

**Top Proxy Services**:

1. **Bright Data** (formerly Luminati)
   - Largest residential network
   - Premium quality
   - Expensive

2. **Oxylabs**
   - High-quality residential and datacenter
   - Good for enterprise

3. **SmartProxy**
   - Affordable residential
   - Good for mid-scale projects

4. **Proxy-Cheap**
   - Budget residential
   - Good for testing

5. **NetNut**
   - ISP proxies
   - Good balance of speed/trust

### Proxy Rotation Strategies

**Simple Rotation**:

```python
import requests
import random

proxy_list = [
    'http://user:pass@proxy1.com:8000',
    'http://user:pass@proxy2.com:8000',
    'http://user:pass@proxy3.com:8000',
    'http://user:pass@proxy4.com:8000',
    'http://user:pass@proxy5.com:8000',
]

def get_with_random_proxy(url):
    proxy = random.choice(proxy_list)
    proxies = {
        'http': proxy,
        'https': proxy
    }
    
    try:
        response = requests.get(url, proxies=proxies, timeout=10)
        return response
    except Exception as e:
        print(f'Proxy {proxy} failed: {e}')
        return None

# Usage
response = get_with_random_proxy('https://example.com')
```

**Round-Robin Rotation**:

```python
from itertools import cycle
import requests

proxy_pool = cycle([
    'http://user:pass@proxy1.com:8000',
    'http://user:pass@proxy2.com:8000',
    'http://user:pass@proxy3.com:8000',
])

def get_with_next_proxy(url):
    proxy = next(proxy_pool)
    proxies = {
        'http': proxy,
        'https': proxy
    }
    
    response = requests.get(url, proxies=proxies, timeout=10)
    return response

# Each request uses next proxy in sequence
for url in urls:
    response = get_with_next_proxy(url)
```

**Smart Proxy Manager**:

```python
import requests
import time
from collections import defaultdict

class ProxyManager:
    def __init__(self, proxies):
        self.proxies = proxies
        self.failures = defaultdict(int)
        self.success_count = defaultdict(int)
        self.last_used = {}
        self.cooldown = 60  # seconds between reuses
    
    def get_best_proxy(self):
        now = time.time()
        
        # Filter out recently used proxies
        available = [
            p for p in self.proxies
            if (now - self.last_used.get(p, 0)) >= self.cooldown
        ]
        
        if not available:
            available = self.proxies
        
        # Sort by success rate
        available.sort(
            key=lambda p: self.success_count[p] / (self.failures[p] + 1),
            reverse=True
        )
        
        return available[0]
    
    def mark_success(self, proxy):
        self.success_count[proxy] += 1
        self.last_used[proxy] = time.time()
    
    def mark_failure(self, proxy):
        self.failures[proxy] += 1
        
        # Remove proxy if too many failures
        if self.failures[proxy] > 10:
            self.proxies.remove(proxy)
            print(f'Removed failing proxy: {proxy}')
    
    def fetch(self, url, max_retries=3):
        for attempt in range(max_retries):
            proxy = self.get_best_proxy()
            proxies = {
                'http': proxy,
                'https': proxy
            }
            
            try:
                response = requests.get(url, proxies=proxies, timeout=10)
                response.raise_for_status()
                self.mark_success(proxy)
                return response
            except Exception as e:
                print(f'Attempt {attempt + 1} failed with {proxy}: {e}')
                self.mark_failure(proxy)
        
        raise Exception(f'All proxies failed for {url}')

# Usage
proxies = [
    'http://user:pass@proxy1.com:8000',
    'http://user:pass@proxy2.com:8000',
    'http://user:pass@proxy3.com:8000',
]

manager = ProxyManager(proxies)

for url in urls:
    try:
        response = manager.fetch(url)
        print(f'Success: {url}')
    except Exception as e:
        print(f'Failed: {url} - {e}')
```

### Proxy Authentication

**Basic Authentication**:

```python
# In URL
proxy = 'http://username:password@proxy.com:8000'

# Or separate
proxies = {
    'http': 'http://proxy.com:8000',
    'https': 'http://proxy.com:8000'
}

auth = ('username', 'password')

response = requests.get('https://example.com', proxies=proxies, auth=auth)
```

**IP Whitelist Authentication**:

Some providers allow authentication by whitelisting your IP:

```python
# No auth needed in request
proxy = 'http://proxy.com:8000'
proxies = {
    'http': proxy,
    'https': proxy
}

response = requests.get('https://example.com', proxies=proxies)
```

### Testing Proxies

```python
import requests
import concurrent.futures

def test_proxy(proxy):
    proxies = {
        'http': proxy,
        'https': proxy
    }
    
    try:
        response = requests.get(
            'http://httpbin.org/ip',
            proxies=proxies,
            timeout=10
        )
        
        if response.status_code == 200:
            data = response.json()
            return {
                'proxy': proxy,
                'working': True,
                'ip': data['origin'],
                'response_time': response.elapsed.total_seconds()
            }
    except Exception as e:
        return {
            'proxy': proxy,
            'working': False,
            'error': str(e)
        }

def test_proxy_list(proxies, max_workers=10):
    with concurrent.futures.ThreadPoolExecutor(max_workers=max_workers) as executor:
        results = list(executor.map(test_proxy, proxies))
    
    working = [r for r in results if r['working']]
    failed = [r for r in results if not r['working']]
    
    print(f'Working: {len(working)}/{len(proxies)}')
    print(f'Failed: {len(failed)}/{len(proxies)}')
    
    return working, failed

# Test proxies
proxies_to_test = [
    'http://user:pass@proxy1.com:8000',
    'http://user:pass@proxy2.com:8000',
    'http://user:pass@proxy3.com:8000',
]

working, failed = test_proxy_list(proxies_to_test)

for proxy_info in working:
    print(f"✓ {proxy_info['proxy']} - {proxy_info['ip']} - {proxy_info['response_time']:.2f}s")

for proxy_info in failed:
    print(f"✗ {proxy_info['proxy']} - {proxy_info['error']}")
```

### Proxy APIs

Many providers offer APIs for dynamic proxy access:

**Bright Data API**:

```python
import requests

# Bright Data gives you a single entry point that rotates automatically
proxy_host = 'zproxy.lum-superproxy.io'
proxy_port = 22225
username = 'lum-customer-USERNAME-zone-ZONE'
password = 'PASSWORD'

proxy = f'http://{username}:{password}@{proxy_host}:{proxy_port}'

proxies = {
    'http': proxy,
    'https': proxy
}

# Each request automatically uses a different IP
response1 = requests.get('http://lumtest.com/myip.json', proxies=proxies)
response2 = requests.get('http://lumtest.com/myip.json', proxies=proxies)

print(response1.json())  # Different IP
print(response2.json())  # Different IP
```

**Oxylabs API**:

```python
proxy_host = 'pr.oxylabs.io'
proxy_port = 7777
username = 'customer-USERNAME'
password = 'PASSWORD'

proxy = f'http://{username}:{password}@{proxy_host}:{proxy_port}'

proxies = {
    'http': proxy,
    'https': proxy
}

response = requests.get('https://ip.oxylabs.io', proxies=proxies)
print(response.text)
```

### Residential Proxy Rotation

```python
import requests
import time

class ResidentialProxyRotator:
    def __init__(self, provider_url, username, password):
        self.proxy_url = f'http://{username}:{password}@{provider_url}'
        self.session = requests.Session()
        self.request_count = 0
        self.rotation_threshold = 10  # Rotate every 10 requests
    
    def get_proxies(self):
        return {
            'http': self.proxy_url,
            'https': self.proxy_url
        }
    
    def fetch(self, url, **kwargs):
        proxies = self.get_proxies()
        
        try:
            response = self.session.get(url, proxies=proxies, **kwargs)
            self.request_count += 1
            
            # Force rotation after threshold
            if self.request_count >= self.rotation_threshold:
                self.session.close()
                self.session = requests.Session()
                self.request_count = 0
            
            return response
        except Exception as e:
            print(f'Request failed: {e}')
            # Force new session on error
            self.session.close()
            self.session = requests.Session()
            self.request_count = 0
            raise

# Usage
rotator = ResidentialProxyRotator(
    'residential-proxy.com:8000',
    'username',
    'password'
)

for url in urls:
    response = rotator.fetch(url)
    print(f'Scraped {url} - Status: {response.status_code}')
    time.sleep(1)
```

### Proxy Performance Monitoring

```python
import requests
import time
from collections import defaultdict
import statistics

class ProxyPerformanceMonitor:
    def __init__(self):
        self.metrics = defaultdict(lambda: {
            'requests': 0,
            'successes': 0,
            'failures': 0,
            'response_times': [],
            'last_failure': None
        })
    
    def record_request(self, proxy, success, response_time=None, error=None):
        metrics = self.metrics[proxy]
        metrics['requests'] += 1
        
        if success:
            metrics['successes'] += 1
            if response_time:
                metrics['response_times'].append(response_time)
        else:
            metrics['failures'] += 1
            metrics['last_failure'] = time.time()
    
    def get_stats(self, proxy):
        metrics = self.metrics[proxy]
        
        if not metrics['requests']:
            return None
        
        success_rate = metrics['successes'] / metrics['requests']
        avg_response_time = (
            statistics.mean(metrics['response_times'])
            if metrics['response_times'] else None
        )
        
        return {
            'proxy': proxy,
            'requests': metrics['requests'],
            'success_rate': success_rate,
            'avg_response_time': avg_response_time,
            'failures': metrics['failures']
        }
    
    def get_best_proxies(self, min_requests=10):
        stats = []
        for proxy in self.metrics:
            proxy_stats = self.get_stats(proxy)
            if proxy_stats and proxy_stats['requests'] >= min_requests:
                stats.append(proxy_stats)
        
        # Sort by success rate, then by response time
        stats.sort(
            key=lambda x: (x['success_rate'], -x['avg_response_time']),
            reverse=True
        )
        
        return stats

# Usage
monitor = ProxyPerformanceMonitor()

for url in urls:
    proxy = select_proxy()
    start = time.time()
    
    try:
        response = requests.get(url, proxies={'http': proxy}, timeout=10)
        response.raise_for_status()
        
        response_time = time.time() - start
        monitor.record_request(proxy, True, response_time)
    except Exception as e:
        monitor.record_request(proxy, False, error=str(e))

# Get performance report
best_proxies = monitor.get_best_proxies()
for stats in best_proxies[:5]:
    print(f"{stats['proxy']}: {stats['success_rate']:.2%} success, {stats['avg_response_time']:.2f}s avg")
```


---

## Browser Fingerprinting and Evasion

### What is Browser Fingerprinting?

Browser fingerprinting is the technique of collecting information about a browser's configuration and characteristics to create a unique identifier (fingerprint). Modern anti-bot systems use fingerprinting to detect automated browsers, even when using proxies or changing IP addresses.

**Common Fingerprinting Vectors**:

1. **User-Agent String**: Browser, OS, version information
2. **Screen Resolution & Color Depth**: Display characteristics
3. **Timezone**: User's timezone offset
4. **Language**: Browser and system language settings  
5. **Plugins**: Installed browser plugins
6. **Fonts**: Available system fonts
7. **Canvas Fingerprinting**: Rendering patterns of canvas elements
8. **WebGL Fingerprinting**: Graphics card and driver information
9. **AudioContext Fingerprinting**: Audio processing characteristics
10. **WebRTC**: Local and public IP addresses
11. **Battery API**: Device battery status
12. **Hardware Concurrency**: CPU core count
13. **Platform**: Operating system platform
14. **Do Not Track**: DNT header value
15. **HTTP Headers**: Accept headers, encoding, etc.

### Testing Your Fingerprint

Before implementing evasion, test your current fingerprint:

**Testing Sites**:
- https://browserleaks.com/
- https://pixelscan.net/
- https://amiunique.org/
- https://coveryourtracks.eff.org/
- https://www.deviceinfo.me/

**Testing Script**:

```javascript
// Test your browser fingerprint
async function testFingerprint() {
    const fp = {
        userAgent: navigator.userAgent,
        platform: navigator.platform,
        language: navigator.language,
        languages: navigator.languages,
        hardwareConcurrency: navigator.hardwareConcurrency,
        deviceMemory: navigator.deviceMemory,
        screen: {
            width: screen.width,
            height: screen.height,
            availWidth: screen.availWidth,
            availHeight: screen.availHeight,
            colorDepth: screen.colorDepth,
            pixelDepth: screen.pixelDepth
        },
        timezone: Intl.DateTimeFormat().resolvedOptions().timeZone,
        timezoneOffset: new Date().getTimezoneOffset(),
        plugins: Array.from(navigator.plugins).map(p => p.name),
        mimeTypes: Array.from(navigator.mimeTypes).map(m => m.type),
        vendor: navigator.vendor,
        product: navigator.product,
        doNotTrack: navigator.doNotTrack,
        cookieEnabled: navigator.cookieEnabled,
        webdriver: navigator.webdriver
    };
    
    // Canvas fingerprint
    const canvas = document.createElement('canvas');
    const ctx = canvas.getContext('2d');
    ctx.fillStyle = 'rgb(255,0,255)';
    ctx.beginPath();
    ctx.rect(20, 20, 150, 100);
    ctx.fill();
    ctx.fillStyle = 'rgb(0,255,255)';
    ctx.font = '18pt Arial';
    ctx.fillText('Fingerprint Test', 50, 50);
    fp.canvas = canvas.toDataURL();
    
    // WebGL fingerprint
    const gl = canvas.getContext('webgl');
    if (gl) {
        const debugInfo = gl.getExtension('WEBGL_debug_renderer_info');
        fp.webgl = {
            vendor: gl.getParameter(gl.VENDOR),
            renderer: gl.getParameter(gl.RENDERER),
            unmaskedVendor: debugInfo ? gl.getParameter(debugInfo.UNMASKED_VENDOR_WEBGL) : null,
            unmaskedRenderer: debugInfo ? gl.getParameter(debugInfo.UNMASKED_RENDERER_WEBGL) : null
        };
    }
    
    return fp;
}

testFingerprint().then(fp => console.log(JSON.stringify(fp, null, 2)));
```

### Comprehensive Fingerprint Evasion

**1. User-Agent Evasion**:

```python
# Python - requests
from fake_useragent import UserAgent

ua = UserAgent()
headers = {
    'User-Agent': ua.random
}

response = requests.get('https://example.com', headers=headers)
```

```javascript
// Node.js - Puppeteer
const puppeteer = require('puppeteer');

const browser = await puppeteer.launch();
const page = await browser.newPage();

await page.setUserAgent(
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
);
```

**2. Screen Resolution Randomization**:

```javascript
await page.setViewport({
    width: 1920 + Math.floor(Math.random() * 200) - 100,
    height: 1080 + Math.floor(Math.random() * 200) - 100,
    deviceScaleFactor: 1 + Math.random() * 0.5
});
```

**3. Timezone Spoofing**:

```javascript
await page.evaluateOnNewDocument((tz) => {
    // Spoof timezone
    Object.defineProperty(Intl.DateTimeFormat.prototype, 'resolvedOptions', {
        value: function() {
            return { timeZone: tz };
        }
    });
    
    // Spoof timezone offset
    const offset = new Date().getTimezoneOffset();
    const fakeOffset = -300;  // EST
    Object.defineProperty(Date.prototype, 'getTimezoneOffset', {
        value: function() {
            return fakeOffset;
        }
    });
}, 'America/New_York');
```

**4. Language Spoofing**:

```javascript
const context = await browser.newContext({
    locale: 'en-US',
    extraHTTPHeaders: {
        'Accept-Language': 'en-US,en;q=0.9'
    }
});

await page.evaluateOnNewDocument(() => {
    Object.defineProperty(navigator, 'language', {
        get: function() { return 'en-US'; }
    });
    
    Object.defineProperty(navigator, 'languages', {
        get: function() { return ['en-US', 'en']; }
    });
});
```

**5. WebDriver Detection Evasion**:

```javascript
await page.evaluateOnNewDocument(() => {
    // Remove webdriver property
    delete Object.getPrototypeOf(navigator).webdriver;
    Object.defineProperty(navigator, 'webdriver', {
        get: () => false
    });
    
    // Remove automation flags
    window.navigator.chrome = {
        runtime: {}
    };
    
    // Spoof permissions
    const originalQuery = window.navigator.permissions.query;
    window.navigator.permissions.query = (parameters) => (
        parameters.name === 'notifications' ?
            Promise.resolve({ state: Notification.permission }) :
            originalQuery(parameters)
    );
});
```

**6. Plugin Spoofing**:

```javascript
await page.evaluateOnNewDocument(() => {
    Object.defineProperty(navigator, 'plugins', {
        get: () => {
            const plugins = [
                {
                    name: 'Chrome PDF Plugin',
                    filename: 'internal-pdf-viewer',
                    description: 'Portable Document Format'
                },
                {
                    name: 'Chrome PDF Viewer',
                    filename: 'mhjfbmdgcfjbbpaeojofohoefgiehjai',
                    description: ''
                },
                {
                    name: 'Native Client',
                    filename: 'internal-nacl-plugin',
                    description: ''
                }
            ];
            return plugins;
        }
    });
    
    Object.defineProperty(navigator, 'mimeTypes', {
        get: () => {
            const mimes = [
                {
                    type: 'application/pdf',
                    suffixes: 'pdf',
                    description: 'Portable Document Format'
                }
            ];
            return mimes;
        }
    });
});
```

**7. Hardware Fingerprint Randomization**:

```javascript
await page.evaluateOnNewDocument(() => {
    // Randomize hardware concurrency (CPU cores)
    const cores = 4 + Math.floor(Math.random() * 8);  // 4-12 cores
    Object.defineProperty(navigator, 'hardwareConcurrency', {
        get: () => cores
    });
    
    // Randomize device memory
    const memory = Math.pow(2, Math.floor(Math.random() * 3) + 2);  // 4, 8, or 16 GB
    Object.defineProperty(navigator, 'deviceMemory', {
        get: () => memory
    });
    
    // Randomize battery API
    if ('getBattery' in navigator) {
        navigator.getBattery = () => Promise.resolve({
            charging: Math.random() > 0.5,
            chargingTime: Math.random() * 10000,
            dischargingTime: Math.random() * 10000,
            level: Math.random()
        });
    }
});
```

**8. Canvas Fingerprinting Evasion**:

```javascript
await page.evaluateOnNewDocument(() => {
    const originalToDataURL = HTMLCanvasElement.prototype.toDataURL;
    const originalToBlob = HTMLCanvasElement.prototype.toBlob;
    const originalGetImageData = CanvasRenderingContext2D.prototype.getImageData;
    
    // Add noise to canvas
    const addNoise = (imageData) => {
        const data = imageData.data;
        for (let i = 0; i < data.length; i += 4) {
            data[i] = Math.min(255, Math.max(0, data[i] + Math.floor(Math.random() * 10) - 5));
            data[i + 1] = Math.min(255, Math.max(0, data[i + 1] + Math.floor(Math.random() * 10) - 5));
            data[i + 2] = Math.min(255, Math.max(0, data[i + 2] + Math.floor(Math.random() * 10) - 5));
        }
        return imageData;
    };
    
    // Override toDataURL
    HTMLCanvasElement.prototype.toDataURL = function() {
        const context = this.getContext('2d');
        if (context) {
            const imageData = context.getImageData(0, 0, this.width, this.height);
            addNoise(imageData);
            context.putImageData(imageData, 0, 0);
        }
        return originalToDataURL.apply(this, arguments);
    };
    
    // Override getImageData
    CanvasRenderingContext2D.prototype.getImageData = function() {
        const imageData = originalGetImageData.apply(this, arguments);
        return addNoise(imageData);
    };
});
```

**9. WebGL Fingerprinting Evasion**:

```javascript
await page.evaluateOnNewDocument(() => {
    const getParameter = WebGLRenderingContext.prototype.getParameter;
    
    WebGLRenderingContext.prototype.getParameter = function(parameter) {
        // VENDOR
        if (parameter === 37445) {
            return 'Intel Inc.';
        }
        // RENDERER
        if (parameter === 37446) {
            return 'Intel Iris OpenGL Engine';
        }
        return getParameter.apply(this, arguments);
    };
    
    // Also handle WebGL2
    if (typeof WebGL2RenderingContext !== 'undefined') {
        const getParameter2 = WebGL2RenderingContext.prototype.getParameter;
        WebGL2RenderingContext.prototype.getParameter = function(parameter) {
            if (parameter === 37445) {
                return 'Intel Inc.';
            }
            if (parameter === 37446) {
                return 'Intel Iris OpenGL Engine';
            }
            return getParameter2.apply(this, arguments);
        };
    }
    
    // Disable WebGL extensions that leak info
    const getSupportedExtensions = WebGLRenderingContext.prototype.getSupportedExtensions;
    WebGLRenderingContext.prototype.getSupportedExtensions = function() {
        const extensions = getSupportedExtensions.apply(this, arguments);
        return extensions.filter(ext => ext !== 'WEBGL_debug_renderer_info');
    };
});
```

**10. AudioContext Fingerprinting Evasion**:

```javascript
await page.evaluateOnNewDocument(() => {
    const audioContext = window.AudioContext || window.webkitAudioContext;
    
    if (audioContext) {
        const OriginalAnalyserNode = window.AnalyserNode || window.webkitAnalyserNode;
        
        const proxy = new Proxy(OriginalAnalyserNode.prototype.getFloatFrequencyData, {
            apply(target, thisArg, args) {
                const result = Reflect.apply(target, thisArg, args);
                const array = args[0];
                
                // Add noise to audio data
                for (let i = 0; i < array.length; i++) {
                    array[i] += Math.random() * 0.0001 - 0.00005;
                }
                
                return result;
            }
        });
        
        OriginalAnalyserNode.prototype.getFloatFrequencyData = proxy;
    }
});
```

**11. WebRTC IP Leak Prevention**:

```javascript
await page.evaluateOnNewDocument(() => {
    // Disable WebRTC to prevent IP leak
    if (RTCPeerConnection) {
        const OriginalRTCPeerConnection = RTCPeerConnection;
        RTCPeerConnection = function(...args) {
            throw new Error('WebRTC is disabled');
        };
        RTCPeerConnection.prototype = OriginalRTCPeerConnection.prototype;
    }
    
    if (webkitRTCPeerConnection) {
        webkitRTCPeerConnection = undefined;
    }
    
    if (mozRTCPeerConnection) {
        mozRTCPeerConnection = undefined;
    }
});
```

**12. Font Fingerprinting Evasion**:

```javascript
await page.evaluateOnNewDocument(() => {
    // Randomize font measurements
    const originalOffsetWidth = Object.getOwnPropertyDescriptor(
        HTMLElement.prototype,
        'offsetWidth'
    );
    
    const originalOffsetHeight = Object.getOwnPropertyDescriptor(
        HTMLElement.prototype,
        'offsetHeight'
    );
    
    Object.defineProperty(HTMLElement.prototype, 'offsetWidth', {
        get() {
            const width = originalOffsetWidth.get.call(this);
            const noise = Math.floor(Math.random() * 3) - 1;  // -1, 0, or 1
            return width + noise;
        }
    });
    
    Object.defineProperty(HTMLElement.prototype, 'offsetHeight', {
        get() {
            const height = originalOffsetHeight.get.call(this);
            const noise = Math.floor(Math.random() * 3) - 1;
            return height + noise;
        }
    });
});
```

### Complete Stealth Configuration

Putting it all together:

```javascript
const puppeteer = require('puppeteer-extra');
const StealthPlugin = require('puppeteer-extra-plugin-stealth');

// Use stealth plugin
puppeteer.use(StealthPlugin());

async function createStealthBrowser() {
    const browser = await puppeteer.launch({
        headless: false,  // Headless mode is easier to detect
        args: [
            '--no-sandbox',
            '--disable-setuid-sandbox',
            '--disable-blink-features=AutomationControlled',
            '--disable-features=IsolateOrigins,site-per-process',
            '--disable-web-security',
            '--disable-features=VizDisplayCompositor'
        ],
        ignoreDefaultArgs: ['--enable-automation'],
        defaultViewport: null
    });
    
    const page = await browser.newPage();
    
    // Set realistic user agent
    await page.setUserAgent(
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
    );
    
    // Set viewport with variation
    await page.setViewport({
        width: 1920 + Math.floor(Math.random() * 200) - 100,
        height: 1080 + Math.floor(Math.random() * 200) - 100,
        deviceScaleFactor: 1 + Math.random() * 0.5
    });
    
    // Apply all fingerprint evasions
    await page.evaluateOnNewDocument(() => {
        // All the evasion code from above goes here...
        // Combine all techniques for comprehensive protection
    });
    
    return { browser, page };
}

// Usage
const { browser, page } = await createStealthBrowser();
await page.goto('https://example.com');

// Test fingerprint
const fpTest = await page.goto('https://pixelscan.net/');
```

### Python Stealth Configuration

```python
from playwright.sync_api import sync_playwright

def create_stealth_browser():
    with sync_playwright() as p:
        browser = p.chromium.launch(
            headless=False,
            args=[
                '--disable-blink-features=AutomationControlled',
                '--disable-features=IsolateOrigins,site-per-process'
            ]
        )
        
        context = browser.new_context(
            viewport={'width': 1920, 'height': 1080},
            user_agent='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36',
            locale='en-US',
            timezone_id='America/New_York',
            permissions=['geolocation'],
            geolocation={'latitude': 40.7128, 'longitude': -74.0060},
            color_scheme='light'
        )
        
        page = context.new_page()
        
        # Add stealth scripts
        page.add_init_script("""
            // Remove webdriver property
            Object.defineProperty(navigator, 'webdriver', {
                get: () => false
            });
            
            // Mock plugins
            Object.defineProperty(navigator, 'plugins', {
                get: () => [1, 2, 3, 4, 5]
            });
            
            // Chrome runtime
            window.chrome = { runtime: {} };
        """)
        
        return browser, context, page

# Usage
browser, context, page = create_stealth_browser()
page.goto('https://example.com')
```

---

## JavaScript Rendering Challenges

### Single Page Applications (SPAs)

Modern websites built with React, Vue, Angular, or similar frameworks dynamically generate content using JavaScript. Traditional HTTP clients can't access this content.

**Characteristics of SPAs**:
- Initial HTML is minimal/empty
- Content loads via JavaScript after page load
- State management on client-side
- API calls to fetch data
- Virtual DOM manipulation

**Identifying SPAs**:

```python
import requests
from bs4 import BeautifulSoup

response = requests.get('https://example.com')
soup = BeautifulSoup(response.content, 'lxml')

# Check if content is minimal
body_text = soup.body.get_text(strip=True) if soup.body else ''

if len(body_text) < 100:
    print("Likely an SPA - minimal initial content")

# Check for common SPA frameworks
if soup.find('div', id='root') or soup.find('div', id='app'):
    print("React/Vue app detected")

# Check for framework scripts
scripts = [script.get('src', '') for script in soup.find_all('script')]
for script in scripts:
    if any(fw in script for fw in ['react', 'vue', 'angular', 'bundle', 'app']):
        print(f"Framework detected in: {script}")
```

**Scraping SPAs - Method 1: Headless Browser**:

```python
from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page()
    
    # Navigate and wait for JavaScript to execute
    page.goto('https://spa-example.com', wait_until='networkidle')
    
    # Wait for specific content to load
    page.wait_for_selector('.product-card')
    
    # Extract data after JavaScript execution
    products = page.query_selector_all('.product-card')
    
    data = []
    for product in products:
        data.append({
            'name': product.query_selector('.name').inner_text(),
            'price': product.query_selector('.price').inner_text()
        })
    
    browser.close()
```

**Scraping SPAs - Method 2: API Interception**:

Often more efficient than rendering the full page:

```javascript
const puppeteer = require('puppeteer');

async function interceptSPAData() {
    const browser = await puppeteer.launch();
    const page = await browser.newPage();
    
    // Collect API responses
    const apiData = [];
    
    page.on('response', async (response) => {
        const url = response.url();
        
        // Identify API endpoints
        if (url.includes('/api/') || url.includes('/graphql') || response.headers()['content-type']?.includes('application/json')) {
            try {
                const data = await response.json();
                apiData.push({
                    url: url,
                    data: data
                });
                console.log(`Captured API data from: ${url}`);
            } catch (e) {
                // Not JSON or already consumed
            }
        }
    });
    
    await page.goto('https://spa-example.com');
    
    // Wait for all API calls to complete
    await page.waitForTimeout(5000);
    
    await browser.close();
    
    return apiData;
}

interceptSPAData().then(data => {
    console.log(`Collected ${data.length} API responses`);
    console.log(JSON.stringify(data, null, 2));
});
```

**Scraping SPAs - Method 3: Reverse Engineer API**:

Find and call the API directly:

```python
import requests

# After identifying the API endpoint from browser DevTools
api_url = 'https://spa-example.com/api/products'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36',
    'Accept': 'application/json',
    'Referer': 'https://spa-example.com',
    # Add any required auth headers
    'Authorization': 'Bearer token123'
}

params = {
    'page': 1,
    'limit': 50,
    'category': 'electronics'
}

response = requests.get(api_url, headers=headers, params=params)
data = response.json()

# Data is already in structured JSON format!
products = data['products']
for product in products:
    print(f"{product['name']}: ${product['price']}")
```

### Infinite Scroll

Many modern sites use infinite scroll to load content as you scroll down.

**Detecting Infinite Scroll**:

```python
# Check for scroll event listeners in JavaScript
page.evaluate("""
    () => {
        const hasScrollListener = window.onscroll !== null || 
                                 document.onscroll !== null;
        return hasScrollListener;
    }
""")
```

**Handling Infinite Scroll - Selenium**:

```python
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get('https://infinite-scroll-site.com')

# Get initial scroll height
last_height = driver.execute_script("return document.body.scrollHeight")

all_items = []

while True:
    # Scroll to bottom
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    
    # Wait for new content to load
    time.sleep(2)
    
    # Extract items
    items = driver.find_elements(By.CLASS_NAME, 'item')
    all_items.extend([item.text for item in items])
    
    # Calculate new scroll height
    new_height = driver.execute_script("return document.body.scrollHeight")
    
    # Check if reached bottom
    if new_height == last_height:
        break
    
    last_height = new_height

driver.quit()

print(f"Collected {len(all_items)} items")
```

**Handling Infinite Scroll - Puppeteer**:

```javascript
async function scrapeInfiniteScroll(url) {
    const browser = await puppeteer.launch();
    const page = await browser.newPage();
    
    await page.goto(url, { waitUntil: 'networkidle2' });
    
    // Auto scroll to bottom
    await page.evaluate(async () => {
        await new Promise((resolve) => {
            let totalHeight = 0;
            const distance = 100;
            
            const timer = setInterval(() => {
                const scrollHeight = document.body.scrollHeight;
                window.scrollBy(0, distance);
                totalHeight += distance;
                
                // Check if reached bottom
                if (totalHeight >= scrollHeight) {
                    clearInterval(timer);
                    resolve();
                }
            }, 100);
        });
    });
    
    // Extract all items after scrolling
    const items = await page.$$eval('.item', items => {
        return items.map(item => ({
            title: item.querySelector('.title')?.textContent,
            price: item.querySelector('.price')?.textContent
        }));
    });
    
    await browser.close();
    return items;
}
```

**Optimized Infinite Scroll with Item Detection**:

```javascript
async function smartInfiniteScroll(page, selector, maxScrolls = 50) {
    let previousCount = 0;
    let noChangeCount = 0;
    let scrollCount = 0;
    
    while (scrollCount < maxScrolls) {
        // Get current item count
        const currentCount = await page.$$eval(selector, items => items.length);
        
        // Scroll down
        await page.evaluate(() => {
            window.scrollBy(0, window.innerHeight);
        });
        
        // Wait for potential new items
        await page.waitForTimeout(1000);
        
        // Check if new items loaded
        if (currentCount === previousCount) {
            noChangeCount++;
            if (noChangeCount >= 3) {
                // No new items after 3 scrolls, assume we're done
                break;
            }
        } else {
            noChangeCount = 0;
        }
        
        previousCount = currentCount;
        scrollCount++;
        
        console.log(`Scroll ${scrollCount}: ${currentCount} items`);
    }
    
    return previousCount;
}
```

### Lazy Loading Images

Many sites lazy-load images to improve performance. The `src` attribute might be empty or placeholder initially.

**Identifying Lazy Loading**:

```html
<!-- Common lazy loading patterns -->
<img data-src="actual-image.jpg" src="placeholder.jpg">
<img data-lazy="actual-image.jpg" src="">
<img loading="lazy" src="actual-image.jpg">
<img class="lazyload" data-src="actual-image.jpg">
```

**Extracting Lazy-Loaded Images**:

```python
from bs4 import BeautifulSoup

soup = BeautifulSoup(html, 'lxml')

for img in soup.find_all('img'):
    # Try different attributes where actual URL might be
    url = (img.get('data-src') or 
           img.get('data-lazy') or 
           img.get('data-original') or 
           img.get('src'))
    
    if url:
        print(url)
```

**With Headless Browser**:

```javascript
async function extractLazyImages(page) {
    // Scroll to trigger lazy loading
    await page.evaluate(async () => {
        await new Promise((resolve) => {
            let totalHeight = 0;
            const distance = 100;
            
            const timer = setInterval(() => {
                window.scrollBy(0, distance);
                totalHeight += distance;
                
                if (totalHeight >= document.body.scrollHeight) {
                    clearInterval(timer);
                    setTimeout(resolve, 2000);  // Wait for images to load
                }
            }, 100);
        });
    });
    
    // Extract image URLs
    const imageUrls = await page.$$eval('img', imgs => {
        return imgs.map(img => img.src || img.dataset.src || img.dataset.lazy);
    });
    
    return imageUrls.filter(url => url && !url.includes('placeholder'));
}
```

### AJAX Pagination

Some sites load pages dynamically via AJAX without changing the URL.

**Detecting AJAX Pagination**:

```javascript
// In browser console
let ajaxCalls = [];

const originalXHR = window.XMLHttpRequest;
window.XMLHttpRequest = function() {
    const xhr = new originalXHR();
    const originalOpen = xhr.open;
    
    xhr.open = function(method, url) {
        console.log(`AJAX ${method}: ${url}`);
        ajaxCalls.push({ method, url });
        return originalOpen.apply(this, arguments);
    };
    
    return xhr;
};

// Click next page and observe AJAX calls
```

**Scraping AJAX Pagination**:

```python
from playwright.sync_api import sync_playwright

def scrape_ajax_pagination():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        
        # Intercept API requests
        api_calls = []
        
        def handle_response(response):
            if 'api' in response.url or response.request.resource_type == 'xhr':
                api_calls.append({
                    'url': response.url,
                    'status': response.status
                })
        
        page.on('response', handle_response)
        
        page.goto('https://example.com/products')
        
        all_products = []
        
        for page_num in range(1, 6):  # Scrape 5 pages
            # Wait for products to load
            page.wait_for_selector('.product')
            
            # Extract products
            products = page.query_selector_all('.product')
            for product in products:
                all_products.append({
                    'name': product.query_selector('.name').inner_text(),
                    'price': product.query_selector('.price').inner_text()
                })
            
            # Click next page button
            next_button = page.query_selector('button.next-page')
            if next_button:
                next_button.click()
                # Wait for AJAX to complete
                page.wait_for_load_state('networkidle')
            else:
                break
        
        browser.close()
        
        print(f"API calls made: {len(api_calls)}")
        print(f"Products collected: {len(all_products)}")
        
        return all_products
```

### Dynamic Content Loading

Content that changes based on user interaction (hover, click, etc.)

**Hover Menus**:

```python
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get('https://example.com')

# Find element to hover over
menu = driver.find_element(By.CLASS_NAME, 'dropdown-menu')

# Hover over it
actions = ActionChains(driver)
actions.move_to_element(menu).perform()

# Wait for submenu to appear
time.sleep(1)

# Extract submenu items
submenu_items = driver.find_elements(By.CLASS_NAME, 'submenu-item')
for item in submenu_items:
    print(item.text)

driver.quit()
```

**Click-to-Reveal Content**:

```javascript
async function scrapeHiddenContent(page) {
    // Find all "Show more" buttons
    const buttons = await page.$$('button.show-more');
    
    for (const button of buttons) {
        // Click button
        await button.click();
        
        // Wait for content to appear
        await page.waitForTimeout(500);
    }
    
    // Now extract all revealed content
    const content = await page.$$eval('.content', els => {
        return els.map(el => el.textContent);
    });
    
    return content;
}
```

### Handling Modals and Popups

**Closing Cookie Consent Popups**:

```python
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get('https://example.com')

try:
    # Wait for cookie popup
    accept_button = WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable((By.ID, 'accept-cookies'))
    )
    accept_button.click()
except:
    # No popup or already accepted
    pass

# Continue scraping
```

**Handling Login Modals**:

```javascript
async function handleLoginModal(page, username, password) {
    // Wait for login modal
    await page.waitForSelector('#login-modal');
    
    // Fill credentials
    await page.type('#username', username);
    await page.type('#password', password);
    
    // Submit
    await page.click('button[type="submit"]');
    
    // Wait for modal to close
    await page.waitForSelector('#login-modal', { state: 'hidden' });
    
    // Wait for page to load after login
    await page.waitForLoadState('networkidle');
}
```

### Server-Side Rendering (SSR) vs Client-Side Rendering (CSR)

**SSR Detection**:

```python
import requests
from bs4 import BeautifulSoup

def is_server_rendered(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'lxml')
    
    # Check if meaningful content exists in initial HTML
    body_text = soup.body.get_text(strip=True) if soup.body else ''
    
    # If body has substantial content, likely SSR
    if len(body_text) > 1000:
        return True
    
    # Check for framework-specific SSR markers
    if soup.find(attrs={'data-reactroot': True}) or soup.find(attrs={'data-server-rendered': True}):
        return True
    
    return False

if is_server_rendered('https://example.com'):
    print("Server-side rendered - can scrape with simple HTTP requests")
else:
    print("Client-side rendered - need headless browser")
```

### JavaScript Wait Strategies

**Wait for Specific Element**:

```python
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Wait for element to be present
wait = WebDriverWait(driver, 10)
element = wait.until(
    EC.presence_of_element_located((By.CLASS_NAME, 'product'))
)

# Wait for element to be visible
element = wait.until(
    EC.visibility_of_element_located((By.CLASS_NAME, 'product'))
)

# Wait for element to be clickable
element = wait.until(
    EC.element_to_be_clickable((By.CLASS_NAME, 'button'))
)
```

**Wait for Multiple Elements**:

```python
# Wait for at least 10 products to load
wait.until(lambda driver: len(driver.find_elements(By.CLASS_NAME, 'product')) >= 10)
```

**Wait for Text Content**:

```python
# Wait for specific text to appear
wait.until(
    EC.text_to_be_present_in_element(
        (By.CLASS_NAME, 'status'),
        'Loaded'
    )
)
```

**Wait for Network Idle**:

```javascript
// Playwright
await page.goto('https://example.com', { waitUntil: 'networkidle' });

// Puppeteer
await page.goto('https://example.com', { waitUntil: 'networkidle2' });
```

**Custom Wait Conditions**:

```python
def wait_for_ajax(driver):
    return driver.execute_script("return jQuery.active == 0")

def wait_for_angular(driver):
    return driver.execute_script("return window.angular === undefined || angular.element(document).injector().get('$http').pendingRequests.length === 0")

# Use custom wait
wait.until(wait_for_ajax)
```

---

## Structured Data Extraction

### Extracting Table Data

Tables are one of the most structured data formats on the web.

**Simple Table Extraction**:

```python
import pandas as pd

# Pandas can automatically extract tables
dfs = pd.read_html('https://example.com/data-table')

# Returns list of all tables on page
for i, df in enumerate(dfs):
    print(f"Table {i}:")
    print(df.head())
    
# Save to CSV
dfs[0].to_csv('table_data.csv', index=False)
```

**Manual Table Extraction**:

```python
from bs4 import BeautifulSoup
import requests

response = requests.get('https://example.com/table')
soup = BeautifulSoup(response.content, 'lxml')

table = soup.find('table', class_='data-table')

# Extract headers
headers = [th.get_text(strip=True) for th in table.find('thead').find_all('th')]

# Extract rows
rows = []
for tr in table.find('tbody').find_all('tr'):
    row = [td.get_text(strip=True) for td in tr.find_all('td')]
    rows.append(row)

# Create DataFrame
import pandas as pd
df = pd.DataFrame(rows, columns=headers)

print(df)
```

**Handling Complex Tables**:

```python
def extract_complex_table(table):
    data = []
    
    # Handle tables with rowspan/colspan
    rows = table.find_all('tr')
    
    for row in rows:
        row_data = {}
        cells = row.find_all(['td', 'th'])
        
        for i, cell in enumerate(cells):
            # Get text content
            text = cell.get_text(strip=True)
            
            # Check for links
            link = cell.find('a')
            if link:
                row_data[f'link_{i}'] = link.get('href')
            
            # Check for images
            img = cell.find('img')
            if img:
                row_data[f'image_{i}'] = img.get('src')
            
            # Store text
            row_data[f'col_{i}'] = text
            
            # Check for rowspan/colspan
            rowspan = cell.get('rowspan')
            colspan = cell.get('colspan')
            
            if rowspan:
                row_data[f'col_{i}_rowspan'] = int(rowspan)
            if colspan:
                row_data[f'col_{i}_colspan'] = int(colspan)
        
        data.append(row_data)
    
    return data
```

### Extracting List Data

**Ordered and Unordered Lists**:

```python
# Extract list items
ul = soup.find('ul', class_='items')
items = [li.get_text(strip=True) for li in ul.find_all('li')]

# Extract with links
ul = soup.find('ul', class_='items')
items_with_links = []
for li in ul.find_all('li'):
    link = li.find('a')
    items_with_links.append({
        'text': li.get_text(strip=True),
        'url': link.get('href') if link else None
    })
```

**Nested Lists**:

```python
def extract_nested_list(ul):
    items = []
    
    for li in ul.find_all('li', recursive=False):  # Only direct children
        item = {
            'text': li.find(text=True, recursive=False).strip()
        }
        
        # Check for nested list
        nested_ul = li.find('ul')
        if nested_ul:
            item['children'] = extract_nested_list(nested_ul)
        
        items.append(item)
    
    return items

# Usage
main_list = soup.find('ul', class_='main-menu')
data = extract_nested_list(main_list)
```

### Extracting Product Data

**Comprehensive Product Scraper**:

```python
class ProductExtractor:
    def __init__(self, soup):
        self.soup = soup
    
    def extract_basic_info(self):
        return {
            'name': self.extract_name(),
            'price': self.extract_price(),
            'currency': self.extract_currency(),
            'availability': self.extract_availability(),
            'sku': self.extract_sku(),
            'brand': self.extract_brand()
        }
    
    def extract_name(self):
        # Try multiple selectors
        selectors = [
            ('h1', {'class': 'product-name'}),
            ('h1', {'class': 'product-title'}),
            ('div', {'class': 'product-name'}),
            ('[itemprop="name"]', {})
        ]
        
        for tag, attrs in selectors:
            elem = self.soup.find(tag, attrs) if attrs else self.soup.select_one(tag)
            if elem:
                return elem.get_text(strip=True)
        
        return None
    
    def extract_price(self):
        # Try multiple patterns
        price_elem = (
            self.soup.find('span', class_=re.compile(r'price')) or
            self.soup.find(attrs={'itemprop': 'price'}) or
            self.soup.select_one('[data-price]')
        )
        
        if not price_elem:
            return None
        
        # Get price from attribute or text
        price_text = (
            price_elem.get('data-price') or
            price_elem.get('content') or
            price_elem.get_text()
        )
        
        # Parse price
        import re
        match = re.search(r'[\d,]+\.?\d*', price_text.replace(',', ''))
        if match:
            return float(match.group(0))
        
        return None
    
    def extract_currency(self):
        # Look for currency symbols or codes
        price_elem = self.soup.find('span', class_=re.compile(r'price'))
        if price_elem:
            text = price_elem.get_text()
            
            # Check for common symbols
            if '$' in text:
                return 'USD'
            elif '€' in text:
                return 'EUR'
            elif '£' in text:
                return 'GBP'
            
            # Check for currency code
            import re
            match = re.search(r'\b(USD|EUR|GBP|CAD|AUD)\b', text)
            if match:
                return match.group(1)
        
        return None
    
    def extract_images(self):
        images = []
        
        # Main product image
        main_img = self.soup.find('img', class_=re.compile(r'product.*image|main.*image'))
        if main_img:
            images.append({
                'url': main_img.get('src') or main_img.get('data-src'),
                'alt': main_img.get('alt'),
                'type': 'main'
            })
        
        # Thumbnail images
        thumbnails = self.soup.find_all('img', class_=re.compile(r'thumbnail'))
        for thumb in thumbnails:
            images.append({
                'url': thumb.get('src') or thumb.get('data-src'),
                'alt': thumb.get('alt'),
                'type': 'thumbnail'
            })
        
        return images
    
    def extract_description(self):
        desc_elem = (
            self.soup.find('div', class_=re.compile(r'description')) or
            self.soup.find(attrs={'itemprop': 'description'}) or
            self.soup.find('div', id='description')
        )
        
        if desc_elem:
            # Get text, preserving line breaks
            return desc_elem.get_text('\n', strip=True)
        
        return None
    
    def extract_specs(self):
        specs = {}
        
        # Look for spec tables
        spec_table = self.soup.find('table', class_=re.compile(r'spec'))
        if spec_table:
            for row in spec_table.find_all('tr'):
                cells = row.find_all(['td', 'th'])
                if len(cells) == 2:
                    key = cells[0].get_text(strip=True)
                    value = cells[1].get_text(strip=True)
                    specs[key] = value
        
        # Look for spec lists
        spec_list = self.soup.find('ul', class_=re.compile(r'spec'))
        if spec_list:
            for li in spec_list.find_all('li'):
                text = li.get_text(strip=True)
                if ':' in text:
                    key, value = text.split(':', 1)
                    specs[key.strip()] = value.strip()
        
        return specs
    
    def extract_reviews(self):
        reviews = []
        
        review_elements = self.soup.find_all('div', class_=re.compile(r'review'))
        
        for review_elem in review_elements:
            review = {
                'author': self.extract_review_author(review_elem),
                'rating': self.extract_review_rating(review_elem),
                'date': self.extract_review_date(review_elem),
                'title': self.extract_review_title(review_elem),
                'text': self.extract_review_text(review_elem)
            }
            reviews.append(review)
        
        return reviews
    
    def extract_review_author(self, review_elem):
        author = review_elem.find('span', class_=re.compile(r'author|name'))
        return author.get_text(strip=True) if author else None
    
    def extract_review_rating(self, review_elem):
        rating_elem = review_elem.find(class_=re.compile(r'rating|stars'))
        if rating_elem:
            # Try data attribute
            rating = rating_elem.get('data-rating')
            if rating:
                return float(rating)
            
            # Try aria-label
            label = rating_elem.get('aria-label')
            if label:
                import re
                match = re.search(r'([\d.]+)', label)
                if match:
                    return float(match.group(1))
            
            # Count filled stars
            filled_stars = len(rating_elem.find_all(class_=re.compile(r'filled|active')))
            if filled_stars > 0:
                return float(filled_stars)
        
        return None
    
    def extract_all(self):
        return {
            **self.extract_basic_info(),
            'images': self.extract_images(),
            'description': self.extract_description(),
            'specs': self.extract_specs(),
            'reviews': self.extract_reviews()
        }

# Usage
response = requests.get('https://example.com/product/12345')
soup = BeautifulSoup(response.content, 'lxml')

extractor = ProductExtractor(soup)
product_data = extractor.extract_all()

print(json.dumps(product_data, indent=2))
```

### Extracting Contact Information

```python
import re

class ContactExtractor:
    def __init__(self, text):
        self.text = text
    
    def extract_emails(self):
        pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
        return re.findall(pattern, self.text)
    
    def extract_phones(self):
        # US phone numbers
        patterns = [
            r'\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}',  # (123) 456-7890
            r'\+1[-.\s]?\d{3}[-.\s]?\d{3}[-.\s]?\d{4}',  # +1-123-456-7890
            r'\d{3}-\d{3}-\d{4}'  # 123-456-7890
        ]
        
        phones = []
        for pattern in patterns:
            phones.extend(re.findall(pattern, self.text))
        
        return list(set(phones))  # Remove duplicates
    
    def extract_addresses(self):
        # Simple address pattern (can be improved)
        pattern = r'\d+\s+[\w\s]+(?:Street|St|Avenue|Ave|Road|Rd|Boulevard|Blvd|Lane|Ln|Drive|Dr|Court|Ct|Circle|Cir)\.?(?:\s+(?:Suite|Ste|Unit|#)\s*\w+)?'
        return re.findall(pattern, self.text, re.IGNORECASE)
    
    def extract_social_media(self):
        social = {}
        
        # Facebook
        fb_pattern = r'(?:https?://)?(?:www\.)?facebook\.com/[\w\.]+'
        fb_matches = re.findall(fb_pattern, self.text)
        if fb_matches:
            social['facebook'] = fb_matches
        
        # Twitter
        twitter_pattern = r'(?:https?://)?(?:www\.)?twitter\.com/[\w\.]+'
        twitter_matches = re.findall(twitter_pattern, self.text)
        if twitter_matches:
            social['twitter'] = twitter_matches
        
        # LinkedIn
        linkedin_pattern = r'(?:https?://)?(?:www\.)?linkedin\.com/(?:in|company)/[\w\-]+'
        linkedin_matches = re.findall(linkedin_pattern, self.text)
        if linkedin_matches:
            social['linkedin'] = linkedin_matches
        
        # Instagram
        instagram_pattern = r'(?:https?://)?(?:www\.)?instagram\.com/[\w\.]+'
        instagram_matches = re.findall(instagram_pattern, self.text)
        if instagram_matches:
            social['instagram'] = instagram_matches
        
        return social
    
    def extract_all(self):
        return {
            'emails': self.extract_emails(),
            'phones': self.extract_phones(),
            'addresses': self.extract_addresses(),
            'social_media': self.extract_social_media()
        }

# Usage
html = requests.get('https://example.com/contact').text
soup = BeautifulSoup(html, 'lxml')
text = soup.get_text()

extractor = ContactExtractor(text)
contact_info = extractor.extract_all()

print(json.dumps(contact_info, indent=2))
```

### Extracting Dates and Times

```python
from dateutil import parser
import re

class DateExtractor:
    def __init__(self, text):
        self.text = text
    
    def extract_dates(self):
        dates = []
        
        # Try parsing with dateutil
        words = self.text.split()
        for i, word in enumerate(words):
            try:
                # Try parsing current word and next few words
                for length in range(1, min(5, len(words) - i + 1)):
                    phrase = ' '.join(words[i:i+length])
                    date = parser.parse(phrase, fuzzy=True)
                    dates.append(date.isoformat())
            except:
                pass
        
        # Also try regex patterns
        patterns = [
            r'\d{4}-\d{2}-\d{2}',  # YYYY-MM-DD
            r'\d{2}/\d{2}/\d{4}',  # MM/DD/YYYY
            r'\d{2}-\d{2}-\d{4}',  # DD-MM-YYYY
        ]
        
        for pattern in patterns:
            matches = re.findall(pattern, self.text)
            for match in matches:
                try:
                    date = parser.parse(match)
                    dates.append(date.isoformat())
                except:
                    pass
        
        return list(set(dates))  # Remove duplicates
    
    def extract_times(self):
        patterns = [
            r'\d{1,2}:\d{2}\s*(?:AM|PM|am|pm)',  # 3:45 PM
            r'\d{1,2}:\d{2}:\d{2}',  # 15:45:30
        ]
        
        times = []
        for pattern in patterns:
            times.extend(re.findall(pattern, self.text))
        
        return times

# Usage
text = "The event is on 2027-02-15 at 3:30 PM. Registration closes 02/10/2027."
extractor = DateExtractor(text)
print(extractor.extract_dates())
print(extractor.extract_times())
```

### Structured Data with Schema.org

Many sites embed structured data using Schema.org markup (JSON-LD, Microdata, RDFa).

**Extracting JSON-LD**:

```python
import json

def extract_json_ld(soup):
    scripts = soup.find_all('script', type='application/ld+json')
    
    structured_data = []
    for script in scripts:
        try:
            data = json.loads(script.string)
            structured_data.append(data)
        except json.JSONDecodeError:
            pass
    
    return structured_data

# Usage
soup = BeautifulSoup(html, 'lxml')
json_ld_data = extract_json_ld(soup)

for data in json_ld_data:
    print(json.dumps(data, indent=2))
    
    # Access specific schema types
    if data.get('@type') == 'Product':
        print(f"Product: {data.get('name')}")
        print(f"Price: {data.get('offers', {}).get('price')}")
```

**Extracting Microdata**:

```python
def extract_microdata(soup):
    items = []
    
    # Find all elements with itemscope
    item_elements = soup.find_all(attrs={'itemscope': True})
    
    for elem in item_elements:
        item = {
            'type': elem.get('itemtype'),
            'properties': {}
        }
        
        # Find all properties
        props = elem.find_all(attrs={'itemprop': True})
        for prop in props:
            prop_name = prop.get('itemprop')
            
            # Get value from different attributes
            value = (
                prop.get('content') or
                prop.get('href') or
                prop.get('src') or
                prop.get_text(strip=True)
            )
            
            item['properties'][prop_name] = value
        
        items.append(item)
    
    return items

# Usage
microdata = extract_microdata(soup)
for item in microdata:
    print(f"Type: {item['type']}")
    for key, value in item['properties'].items():
        print(f"  {key}: {value}")
```


---

## API Reverse Engineering

### Introduction to API Reverse Engineering

Many modern websites load data through APIs rather than embedding it in HTML. Accessing these APIs directly is often more efficient than parsing HTML. API reverse engineering is the process of discovering and understanding these hidden APIs.

**Why Reverse Engineer APIs?**

1. **Efficiency**: JSON/XML data is easier to parse than HTML
2. **Reliability**: API responses are more stable than HTML structure
3. **Performance**: Faster than loading full pages with browsers
4. **Completeness**: APIs often expose more data than visible on the page
5. **Pagination**: Easier to navigate large datasets

### Using Browser DevTools for API Discovery

**Network Tab Workflow**:

1. Open Chrome DevTools (F12)
2. Go to Network tab
3. Filter by XHR/Fetch (API requests)
4. Perform action on website (search, pagination, load more)
5. Identify relevant API requests
6. Inspect request headers, payload, and response

**Example - Finding Product API**:

```
1. Visit e-commerce site
2. Open DevTools Network tab
3. Clear existing requests
4. Search for "laptop"
5. Look for XHR requests containing "search", "api", "product"
6. Click on request to view details:
   - Request URL: https://example.com/api/products/search
   - Method: POST
   - Headers: Authorization, Content-Type
   - Payload: {"query": "laptop", "page": 1, "limit": 20}
   - Response: JSON with product data
```

### Analyzing API Requests

**Request Components**:

```python
import requests

# Replicate discovered API request
url = 'https://example.com/api/products/search'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36',
    'Content-Type': 'application/json',
    'Accept': 'application/json',
    'Referer': 'https://example.com/search',
    'Origin': 'https://example.com',
    # Sometimes required
    'X-Requested-With': 'XMLHttpRequest',
    # API key or auth token
    'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...'
}

payload = {
    'query': 'laptop',
    'page': 1,
    'limit': 20,
    'filters': {
        'category': 'electronics',
        'price_max': 2000
    },
    'sort': 'price_asc'
}

response = requests.post(url, json=payload, headers=headers)

# Parse JSON response
data = response.json()
products = data['results']

for product in products:
    print(f"{product['name']}: ${product['price']}")
```

### Identifying Authentication

**Common Auth Methods**:

**1. Bearer Token (JWT)**:

```python
# Usually in Authorization header
headers = {
    'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ.SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c'
}
```

**2. API Key**:

```python
# In header
headers = {
    'X-API-Key': 'abc123def456',
    'API-Key': 'abc123def456'
}

# Or in query params
params = {
    'api_key': 'abc123def456',
    'key': 'abc123def456'
}
```

**3. Session Cookie**:

```python
# Login first to get session cookie
session = requests.Session()

session.post('https://example.com/api/login', json={
    'username': 'user',
    'password': 'pass'
})

# Session cookie is stored, use for subsequent requests
response = session.get('https://example.com/api/protected')
```

**4. Basic Auth**:

```python
from requests.auth import HTTPBasicAuth

auth = HTTPBasicAuth('username', 'password')
response = requests.get('https://example.com/api/data', auth=auth)
```

**5. OAuth**:

```python
# More complex, requires OAuth flow
from requests_oauthlib import OAuth2Session

client_id = 'your_client_id'
client_secret = 'your_client_secret'
redirect_uri = 'http://localhost:8080/callback'

oauth = OAuth2Session(client_id, redirect_uri=redirect_uri)
authorization_url, state = oauth.authorization_url('https://provider.com/oauth/authorize')

# User authorizes, gets callback with code
# Exchange code for token
token = oauth.fetch_token(
    'https://provider.com/oauth/token',
    code='authorization_code',
    client_secret=client_secret
)

# Use token for API requests
response = oauth.get('https://example.com/api/data')
```

### Extracting Auth Tokens

**From JavaScript**:

```javascript
// In browser console
// Check localStorage
console.log(localStorage);
Object.keys(localStorage).forEach(key => {
    console.log(key, localStorage.getItem(key));
});

// Check sessionStorage
console.log(sessionStorage);

// Check cookies
console.log(document.cookie);

// Check global variables
console.log(window);
// Look for variables like: window.apiKey, window.token, window.auth, etc.
```

**From Network Requests**:

```python
# Using Selenium to extract token from browser
from selenium import webdriver

driver = webdriver.Chrome()
driver.get('https://example.com')

# Login
driver.find_element_by_id('username').send_keys('user')
driver.find_element_by_id('password').send_keys('pass')
driver.find_element_by_id('submit').click()

# Wait for login
time.sleep(2)

# Extract token from localStorage
token = driver.execute_script("return localStorage.getItem('auth_token');")

print(f"Token: {token}")

# Or extract from cookies
cookies = driver.get_cookies()
for cookie in cookies:
    if 'auth' in cookie['name'].lower():
        print(f"Auth cookie: {cookie['name']} = {cookie['value']}")

driver.quit()

# Use extracted token
headers = {'Authorization': f'Bearer {token}'}
response = requests.get('https://example.com/api/data', headers=headers)
```

### GraphQL API Reverse Engineering

GraphQL APIs are increasingly common and offer powerful querying capabilities.

**Discovering GraphQL Endpoint**:

```
Common endpoints:
/graphql
/api/graphql
/v1/graphql
/gql
```

**GraphQL Introspection**:

```python
import requests
import json

def introspect_graphql(url):
    introspection_query = """
    query IntrospectionQuery {
        __schema {
            types {
                name
                kind
                description
                fields {
                    name
                    description
                    type {
                        name
                        kind
                    }
                    args {
                        name
                        type {
                            name
                        }
                    }
                }
            }
            queryType {
                name
            }
            mutationType {
                name
            }
        }
    }
    """
    
    response = requests.post(
        url,
        json={'query': introspection_query},
        headers={'Content-Type': 'application/json'}
    )
    
    schema = response.json()
    return schema

# Usage
schema = introspect_graphql('https://example.com/graphql')

# Explore available types and fields
for type_info in schema['data']['__schema']['types']:
    if type_info['name'] == 'Product':
        print(f"Product fields:")
        for field in type_info['fields']:
            print(f"  - {field['name']}: {field['type']['name']}")
```

**Querying GraphQL API**:

```python
def query_graphql(url, query, variables=None):
    payload = {'query': query}
    if variables:
        payload['variables'] = variables
    
    response = requests.post(
        url,
        json=payload,
        headers={'Content-Type': 'application/json'}
    )
    
    return response.json()

# Example query
query = """
query GetProducts($category: String!, $limit: Int!) {
    products(category: $category, limit: $limit) {
        id
        name
        price
        description
        images {
            url
            alt
        }
        reviews {
            rating
            text
            author
        }
    }
}
"""

variables = {
    'category': 'electronics',
    'limit': 20
}

result = query_graphql('https://example.com/graphql', query, variables)
products = result['data']['products']

for product in products:
    print(f"{product['name']}: ${product['price']}")
```

**GraphQL Mutations**:

```python
# Mutation example (create/update/delete data)
mutation = """
mutation AddToCart($productId: ID!, $quantity: Int!) {
    addToCart(productId: $productId, quantity: $quantity) {
        cart {
            id
            items {
                product {
                    name
                    price
                }
                quantity
            }
            total
        }
    }
}
"""

variables = {
    'productId': '12345',
    'quantity': 2
}

result = query_graphql('https://example.com/graphql', mutation, variables)
```

### Mobile App API Interception

Mobile apps often use APIs that are easier to access than web scraping.

**Method 1: HTTP Proxy (Charles/Mitmproxy)**:

```bash
# Install mitmproxy
pip install mitmproxy

# Start proxy
mitmproxy -p 8080

# Configure phone to use proxy:
# Settings > WiFi > Configure Proxy
# Host: Computer's IP
# Port: 8080

# Install mitmproxy certificate on phone
# Browse to mitm.it on phone

# Use app, observe requests in mitmproxy
```

**Method 2: Android APK Analysis**:

```bash
# Decompile APK
apktool d app.apk

# Extract strings (look for API endpoints)
grep -r "https://" app/

# Look in res/values/strings.xml
cat app/res/values/strings.xml | grep "api"

# Analyze network code
# Look for Java/Kotlin files with HTTP/API calls
find app/ -name "*.smali" | xargs grep -l "http"
```

**Method 3: Frida for Runtime Hooking**:

```javascript
// Frida script to intercept HTTP requests
Java.perform(function() {
    var OkHttpClient = Java.use('okhttp3.OkHttpClient');
    var Request = Java.use('okhttp3.Request');
    
    OkHttpClient.newCall.overload('okhttp3.Request').implementation = function(request) {
        console.log('URL: ' + request.url().toString());
        console.log('Method: ' + request.method());
        console.log('Headers: ' + request.headers().toString());
        
        var response = this.newCall(request);
        return response;
    };
});

// Run frida
// frida -U -f com.example.app -l script.js
```

### Analyzing API Responses

**Understanding Pagination**:

```python
# Offset-based pagination
def scrape_offset_pagination(base_url):
    all_results = []
    offset = 0
    limit = 100
    
    while True:
        response = requests.get(f'{base_url}?offset={offset}&limit={limit}')
        data = response.json()
        
        results = data['results']
        if not results:
            break
        
        all_results.extend(results)
        offset += limit
        
        # Check if more pages available
        if len(results) < limit:
            break
    
    return all_results

# Page-based pagination
def scrape_page_pagination(base_url):
    all_results = []
    page = 1
    
    while True:
        response = requests.get(f'{base_url}?page={page}')
        data = response.json()
        
        results = data['results']
        if not results:
            break
        
        all_results.extend(results)
        
        # Check if has next page
        if not data.get('has_next') or page >= data.get('total_pages', 0):
            break
        
        page += 1
    
    return all_results

# Cursor-based pagination
def scrape_cursor_pagination(base_url):
    all_results = []
    cursor = None
    
    while True:
        params = {}
        if cursor:
            params['cursor'] = cursor
        
        response = requests.get(base_url, params=params)
        data = response.json()
        
        results = data['results']
        all_results.extend(results)
        
        cursor = data.get('next_cursor')
        if not cursor:
            break
    
    return all_results
```

**Handling Rate Limits**:

```python
import time
from functools import wraps

def rate_limit(calls_per_second=1):
    min_interval = 1.0 / calls_per_second
    last_called = [0.0]
    
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            elapsed = time.time() - last_called[0]
            wait_time = min_interval - elapsed
            
            if wait_time > 0:
                time.sleep(wait_time)
            
            result = func(*args, **kwargs)
            last_called[0] = time.time()
            return result
        
        return wrapper
    return decorator

@rate_limit(calls_per_second=2)  # Max 2 calls per second
def call_api(url):
    return requests.get(url).json()

# Usage - automatically rate limited
for i in range(100):
    data = call_api(f'https://api.example.com/items/{i}')
```

**Handling API Errors**:

```python
def robust_api_call(url, max_retries=3, backoff_factor=2):
    for attempt in range(max_retries):
        try:
            response = requests.get(url, timeout=10)
            
            # Check status code
            if response.status_code == 200:
                return response.json()
            elif response.status_code == 429:
                # Rate limited
                retry_after = int(response.headers.get('Retry-After', 60))
                print(f'Rate limited. Waiting {retry_after} seconds...')
                time.sleep(retry_after)
                continue
            elif response.status_code in [500, 502, 503, 504]:
                # Server error, retry
                wait_time = backoff_factor ** attempt
                print(f'Server error. Retrying in {wait_time}s...')
                time.sleep(wait_time)
                continue
            else:
                # Other error
                print(f'Error {response.status_code}: {response.text}')
                return None
        
        except requests.RequestException as e:
            if attempt == max_retries - 1:
                raise
            
            wait_time = backoff_factor ** attempt
            print(f'Request failed: {e}. Retrying in {wait_time}s...')
            time.sleep(wait_time)
    
    return None
```

### Reverse Engineering JavaScript

Sometimes API details are embedded in JavaScript code.

**Extracting API Endpoints from JS**:

```python
import re
import requests

def extract_api_endpoints(js_url):
    response = requests.get(js_url)
    js_code = response.text
    
    # Find URLs
    url_pattern = r'https?://[a-zA-Z0-9\.\-/\_]+'
    urls = re.findall(url_pattern, js_code)
    
    # Filter for API endpoints
    api_endpoints = [
        url for url in urls
        if any(keyword in url.lower() for keyword in ['api', 'graphql', 'rest', 'v1', 'v2'])
    ]
    
    return list(set(api_endpoints))

# Find all JS files
soup = BeautifulSoup(html, 'lxml')
scripts = soup.find_all('script', src=True)

for script in scripts:
    js_url = script['src']
    if not js_url.startswith('http'):
        js_url = urljoin(base_url, js_url)
    
    endpoints = extract_api_endpoints(js_url)
    if endpoints:
        print(f"Found endpoints in {js_url}:")
        for endpoint in endpoints:
            print(f"  - {endpoint}")
```

**Extracting API Keys from JS**:

```python
def find_api_keys(js_code):
    patterns = {
        'api_key': r'api[_-]?key["\']?\s*[:=]\s*["\']([a-zA-Z0-9_\-]+)["\']',
        'api_token': r'token["\']?\s*[:=]\s*["\']([a-zA-Z0-9_\-\.]+)["\']',
        'client_id': r'client[_-]?id["\']?\s*[:=]\s*["\']([a-zA-Z0-9_\-]+)["\']',
        'secret': r'secret["\']?\s*[:=]\s*["\']([a-zA-Z0-9_\-]+)["\']'
    }
    
    found_keys = {}
    for key_type, pattern in patterns.items():
        matches = re.findall(pattern, js_code, re.IGNORECASE)
        if matches:
            found_keys[key_type] = matches
    
    return found_keys

# Usage
response = requests.get('https://example.com/js/app.js')
keys = find_api_keys(response.text)

for key_type, values in keys.items():
    print(f"{key_type}: {values}")
```

### Building API Client Classes

Once you've reverse-engineered an API, create a reusable client:

```python
class ExampleAPIClient:
    def __init__(self, api_key=None):
        self.base_url = 'https://api.example.com/v1'
        self.api_key = api_key
        self.session = requests.Session()
        
        if api_key:
            self.session.headers['X-API-Key'] = api_key
        
        self.session.headers.update({
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36',
            'Accept': 'application/json',
            'Content-Type': 'application/json'
        })
    
    def _request(self, method, endpoint, **kwargs):
        url = f'{self.base_url}/{endpoint}'
        
        try:
            response = self.session.request(method, url, **kwargs)
            response.raise_for_status()
            return response.json()
        except requests.RequestException as e:
            print(f'API request failed: {e}')
            return None
    
    def get_products(self, category=None, page=1, limit=50):
        params = {
            'page': page,
            'limit': limit
        }
        if category:
            params['category'] = category
        
        return self._request('GET', 'products', params=params)
    
    def get_product(self, product_id):
        return self._request('GET', f'products/{product_id}')
    
    def search_products(self, query, **filters):
        payload = {
            'query': query,
            **filters
        }
        return self._request('POST', 'products/search', json=payload)
    
    def get_product_reviews(self, product_id, page=1):
        return self._request('GET', f'products/{product_id}/reviews', params={'page': page})

# Usage
client = ExampleAPIClient(api_key='your_api_key')

# Get products
products = client.get_products(category='electronics', page=1)
for product in products['results']:
    print(f"{product['name']}: ${product['price']}")

# Search
results = client.search_products('laptop', price_max=2000, sort='price_asc')

# Get reviews
reviews = client.get_product_reviews(product_id='12345', page=1)
```

---

## Data Processing and Normalization

### Data Cleaning Fundamentals

Raw scraped data often needs cleaning before use.

**Common Cleaning Tasks**:

```python
class DataCleaner:
    @staticmethod
    def clean_price(price_str):
        """Extract numeric price from string"""
        import re
        
        if not price_str:
            return None
        
        # Remove currency symbols and text
        price_str = re.sub(r'[^\d.,]', '', str(price_str))
        
        # Handle different decimal separators
        price_str = price_str.replace(',', '.')
        
        # Remove all but last dot (for thousands separator)
        parts = price_str.split('.')
        if len(parts) > 2:
            price_str = ''.join(parts[:-1]) + '.' + parts[-1]
        
        try:
            return float(price_str)
        except ValueError:
            return None
    
    @staticmethod
    def clean_text(text):
        """Clean and normalize text"""
        if not text:
            return ''
        
        # Convert to string
        text = str(text)
        
        # Remove extra whitespace
        text = ' '.join(text.split())
        
        # Remove zero-width characters
        text = text.replace('\u200b', '').replace('\ufeff', '')
        
        # Normalize unicode
        import unicodedata
        text = unicodedata.normalize('NFKC', text)
        
        return text.strip()
    
    @staticmethod
    def clean_url(url, base_url=None):
        """Clean and normalize URL"""
        from urllib.parse import urljoin, urlparse, urlunparse
        
        if not url:
            return None
        
        # Remove whitespace
        url = url.strip()
        
        # Make absolute if relative
        if base_url and not url.startswith('http'):
            url = urljoin(base_url, url)
        
        # Remove fragments
        parsed = urlparse(url)
        url = urlunparse(parsed._replace(fragment=''))
        
        return url
    
    @staticmethod
    def parse_date(date_str):
        """Parse date from various formats"""
        from dateutil import parser
        
        if not date_str:
            return None
        
        try:
            return parser.parse(date_str)
        except:
            return None
    
    @staticmethod
    def extract_number(text):
        """Extract first number from text"""
        import re
        
        match = re.search(r'\d+\.?\d*', str(text))
        if match:
            try:
                return float(match.group(0))
            except:
                return None
        return None

# Usage
cleaner = DataCleaner()

# Clean prices
print(cleaner.clean_price('$1,299.99'))  # 1299.99
print(cleaner.clean_price('€ 1.299,99'))  # 1299.99
print(cleaner.clean_price('Price: 999'))  # 999.0

# Clean text
print(cleaner.clean_text('  Multiple   spaces  '))  # 'Multiple spaces'

# Clean URLs
print(cleaner.clean_url('/products/123', 'https://example.com'))  # 'https://example.com/products/123'

# Parse dates
print(cleaner.parse_date('Feb 9, 2027'))  # datetime object
```

### Handling Missing Data

```python
import pandas as pd

def handle_missing_data(df):
    # 1. Identify missing data
    print("Missing data summary:")
    print(df.isnull().sum())
    
    # 2. Drop rows with too many missing values
    threshold = len(df.columns) * 0.5  # Drop if >50% missing
    df = df.dropna(thresh=threshold)
    
    # 3. Fill missing values
    # For numeric columns - fill with median
    numeric_columns = df.select_dtypes(include=['number']).columns
    for col in numeric_columns:
        df[col].fillna(df[col].median(), inplace=True)
    
    # For categorical - fill with mode or 'Unknown'
    categorical_columns = df.select_dtypes(include=['object']).columns
    for col in categorical_columns:
        mode_value = df[col].mode()[0] if not df[col].mode().empty else 'Unknown'
        df[col].fillna(mode_value, inplace=True)
    
    # 4. Forward fill for time series
    # df = df.fillna(method='ffill')
    
    return df

# Usage
df = pd.DataFrame({
    'product': ['A', 'B', None, 'D'],
    'price': [10.99, None, 15.99, 12.99],
    'stock': [10, 5, None, 8]
})

df_cleaned = handle_missing_data(df)
```

### Data Validation

```python
class DataValidator:
    @staticmethod
    def validate_product(product):
        """Validate product data"""
        errors = []
        
        # Required fields
        required = ['name', 'price', 'url']
        for field in required:
            if field not in product or not product[field]:
                errors.append(f'Missing required field: {field}')
        
        # Price validation
        if 'price' in product:
            try:
                price = float(product['price'])
                if price < 0:
                    errors.append('Price cannot be negative')
                if price > 1000000:
                    errors.append('Price seems unrealistically high')
            except (ValueError, TypeError):
                errors.append('Invalid price format')
        
        # URL validation
        if 'url' in product:
            if not product['url'].startswith('http'):
                errors.append('Invalid URL format')
        
        # Email validation
        if 'email' in product:
            import re
            email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[A-Z|a-z]{2,}$'
            if not re.match(email_pattern, product['email']):
                errors.append('Invalid email format')
        
        return len(errors) == 0, errors
    
    @staticmethod
    def validate_batch(products):
        """Validate batch of products"""
        results = {
            'valid': [],
            'invalid': []
        }
        
        for product in products:
            is_valid, errors = DataValidator.validate_product(product)
            
            if is_valid:
                results['valid'].append(product)
            else:
                results['invalid'].append({
                    'product': product,
                    'errors': errors
                })
        
        return results

# Usage
products = [
    {'name': 'Laptop', 'price': 999.99, 'url': 'https://example.com/laptop'},
    {'name': 'Mouse', 'price': -10, 'url': 'invalid-url'},  # Invalid
    {'name': '', 'price': 29.99, 'url': 'https://example.com/mouse'},  # Invalid
]

results = DataValidator.validate_batch(products)
print(f"Valid: {len(results['valid'])}")
print(f"Invalid: {len(results['invalid'])}")

for invalid in results['invalid']:
    print(f"Product: {invalid['product']}")
    print(f"Errors: {invalid['errors']}")
```

### Deduplication

```python
def deduplicate_products(products):
    """Remove duplicate products"""
    seen = set()
    unique = []
    
    for product in products:
        # Create identifier (e.g., URL or product ID)
        identifier = product.get('url') or product.get('id')
        
        if identifier and identifier not in seen:
            seen.add(identifier)
            unique.append(product)
    
    return unique

# Fuzzy deduplication (for similar but not identical items)
from difflib import SequenceMatcher

def fuzzy_deduplicate(products, threshold=0.9):
    """Remove similar products based on name similarity"""
    unique = []
    
    for product in products:
        is_duplicate = False
        
        for existing in unique:
            # Compare names
            similarity = SequenceMatcher(
                None,
                product.get('name', '').lower(),
                existing.get('name', '').lower()
            ).ratio()
            
            if similarity >= threshold:
                is_duplicate = True
                break
        
        if not is_duplicate:
            unique.append(product)
    
    return unique

# Usage
products = [
    {'name': 'Laptop Computer', 'price': 999},
    {'name': 'Laptop Computer', 'price': 999},  # Exact duplicate
    {'name': 'Laptop PC', 'price': 999},  # Similar
]

unique = deduplicate_products(products)  # Removes exact duplicates
fuzzy_unique = fuzzy_deduplicate(products, threshold=0.85)  # Removes similar
```

### Text Normalization

```python
import re
import unicodedata

class TextNormalizer:
    @staticmethod
    def normalize(text):
        """Comprehensive text normalization"""
        if not text:
            return ''
        
        # Convert to string
        text = str(text)
        
        # Unicode normalization
        text = unicodedata.normalize('NFKC', text)
        
        # Convert to lowercase
        text = text.lower()
        
        # Remove HTML entities
        import html
        text = html.unescape(text)
        
        # Remove HTML tags
        text = re.sub(r'<[^>]+>', '', text)
        
        # Remove URLs
        text = re.sub(r'http\S+|www.\S+', '', text)
        
        # Remove email addresses
        text = re.sub(r'\S+@\S+', '', text)
        
        # Remove special characters but keep spaces
        text = re.sub(r'[^a-z0-9\s]', '', text)
        
        # Remove extra whitespace
        text = ' '.join(text.split())
        
        return text
    
    @staticmethod
    def normalize_phone(phone):
        """Normalize phone number"""
        # Remove all non-numeric
        digits = re.sub(r'\D', '', phone)
        
        # Format as (XXX) XXX-XXXX for US numbers
        if len(digits) == 10:
            return f'({digits[:3]}) {digits[3:6]}-{digits[6:]}'
        elif len(digits) == 11 and digits[0] == '1':
            return f'+1 ({digits[1:4]}) {digits[4:7]}-{digits[7:]}'
        
        return phone
    
    @staticmethod
    def normalize_address(address):
        """Normalize address"""
        # Common abbreviations
        replacements = {
            r'\bstreet\b': 'st',
            r'\bavenue\b': 'ave',
            r'\broad\b': 'rd',
            r'\bdrive\b': 'dr',
            r'\blane\b': 'ln',
            r'\bcourt\b': 'ct',
            r'\bapartment\b': 'apt',
            r'\bsuite\b': 'ste',
            r'\bnorth\b': 'n',
            r'\bsouth\b': 's',
            r'\beast\b': 'e',
            r'\bwest\b': 'w',
        }
        
        address = address.lower()
        for pattern, replacement in replacements.items():
            address = re.sub(pattern, replacement, address, flags=re.IGNORECASE)
        
        # Remove extra whitespace
        address = ' '.join(address.split())
        
        return address

# Usage
normalizer = TextNormalizer()

print(normalizer.normalize('  HELLO <b>World</b>!!!  '))  # 'hello world'
print(normalizer.normalize_phone('555-123-4567'))  # '(555) 123-4567'
print(normalizer.normalize_address('123 Main Street Apartment 4B'))  # '123 main st apt 4b'
```

### Data Transformation

```python
import pandas as pd

def transform_scraped_data(raw_data):
    """Transform raw scraped data into clean structured format"""
    df = pd.DataFrame(raw_data)
    
    # 1. Clean column names
    df.columns = df.columns.str.lower().str.replace(' ', '_')
    
    # 2. Convert data types
    if 'price' in df.columns:
        df['price'] = df['price'].apply(DataCleaner.clean_price)
    
    if 'date' in df.columns:
        df['date'] = pd.to_datetime(df['date'], errors='coerce')
    
    # 3. Create derived columns
    if 'price' in df.columns and 'original_price' in df.columns:
        df['discount'] = df['original_price'] - df['price']
        df['discount_percent'] = (df['discount'] / df['original_price'] * 100).round(2)
    
    # 4. Categorize data
    if 'price' in df.columns:
        df['price_category'] = pd.cut(
            df['price'],
            bins=[0, 50, 200, 1000, float('inf')],
            labels=['Budget', 'Mid-range', 'Premium', 'Luxury']
        )
    
    # 5. Extract features from text
    if 'name' in df.columns:
        df['name_length'] = df['name'].str.len()
        df['word_count'] = df['name'].str.split().str.len()
    
    # 6. Handle duplicates
    df = df.drop_duplicates(subset=['url'], keep='first')
    
    # 7. Sort
    if 'price' in df.columns:
        df = df.sort_values('price')
    
    return df

# Usage
raw_data = [
    {'name': 'Product 1', 'price': '$999.99', 'original_price': '$1299.99', 'url': 'https://example.com/1'},
    {'name': 'Product 2', 'price': '$49.99', 'original_price': '$79.99', 'url': 'https://example.com/2'},
]

df = transform_scraped_data(raw_data)
print(df)
```

### Pandas Advanced Processing

```python
import pandas as pd

def advanced_data_processing(df):
    # 1. Group and aggregate
    if 'category' in df.columns:
        category_stats = df.groupby('category').agg({
            'price': ['mean', 'min', 'max', 'count'],
            'rating': 'mean'
        }).round(2)
        
        print("Category Statistics:")
        print(category_stats)
    
    # 2. Pivot tables
    if 'category' in df.columns and 'brand' in df.columns:
        pivot = pd.pivot_table(
            df,
            values='price',
            index='category',
            columns='brand',
            aggfunc='mean'
        )
        print("\nPrice by Category and Brand:")
        print(pivot)
    
    # 3. Time series analysis
    if 'date' in df.columns:
        df['date'] = pd.to_datetime(df['date'])
        df = df.set_index('date')
        
        # Resample to daily/weekly/monthly
        daily_avg = df['price'].resample('D').mean()
        weekly_avg = df['price'].resample('W').mean()
        
        print("\nDaily average price:")
        print(daily_avg.head())
    
    # 4. Rolling statistics
    if 'price' in df.columns:
        df['price_7day_avg'] = df['price'].rolling(window=7).mean()
        df['price_7day_std'] = df['price'].rolling(window=7).std()
    
    # 5. Correlation analysis
    numeric_cols = df.select_dtypes(include=['number']).columns
    if len(numeric_cols) > 1:
        correlation = df[numeric_cols].corr()
        print("\nCorrelation Matrix:")
        print(correlation)
    
    return df
```

---

## Storage and Output Formats

### CSV Output

**Basic CSV Writing**:

```python
import csv

products = [
    {'name': 'Laptop', 'price': 999.99, 'stock': 10},
    {'name': 'Mouse', 'price': 29.99, 'stock': 50},
]

# Write to CSV
with open('products.csv', 'w', newline='', encoding='utf-8') as f:
    fieldnames = ['name', 'price', 'stock']
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    
    writer.writeheader()
    writer.writerows(products)

# Using pandas (easier for large datasets)
import pandas as pd

df = pd.DataFrame(products)
df.to_csv('products.csv', index=False, encoding='utf-8')
```

**Advanced CSV Options**:

```python
# Custom delimiter
df.to_csv('products.tsv', sep='\t', index=False)

# Quote handling
df.to_csv('products.csv', quoting=csv.QUOTE_ALL)  # Quote all fields
df.to_csv('products.csv', quoting=csv.QUOTE_MINIMAL)  # Quote only when needed

# Handle missing values
df.to_csv('products.csv', na_rep='N/A')

# Append to existing file
df.to_csv('products.csv', mode='a', header=False, index=False)

# Compression
df.to_csv('products.csv.gz', compression='gzip', index=False)
```

### JSON Output

**Basic JSON Writing**:

```python
import json

products = [
    {'name': 'Laptop', 'price': 999.99},
    {'name': 'Mouse', 'price': 29.99},
]

# Write to JSON
with open('products.json', 'w', encoding='utf-8') as f:
    json.dump(products, f, indent=2, ensure_ascii=False)

# Single-line JSON (smaller file size)
with open('products.json', 'w') as f:
    json.dump(products, f, separators=(',', ':'))

# Pretty print
print(json.dumps(products, indent=2))
```

**JSON Lines (JSONL)**:

Better for large datasets - each line is a separate JSON object:

```python
# Write JSONL
with open('products.jsonl', 'w', encoding='utf-8') as f:
    for product in products:
        f.write(json.dumps(product) + '\n')

# Read JSONL
products = []
with open('products.jsonl', 'r', encoding='utf-8') as f:
    for line in f:
        products.append(json.loads(line))

# Using pandas
df.to_json('products.jsonl', orient='records', lines=True)
df_loaded = pd.read_json('products.jsonl', orient='records', lines=True)
```

### SQLite Storage

**Basic SQLite Usage**:

```python
import sqlite3

# Connect to database (creates if doesn't exist)
conn = sqlite3.connect('products.db')
cursor = conn.cursor()

# Create table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS products (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        price REAL NOT NULL,
        url TEXT UNIQUE,
        scraped_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
''')

# Insert data
products = [
    ('Laptop', 999.99, 'https://example.com/laptop'),
    ('Mouse', 29.99, 'https://example.com/mouse'),
]

cursor.executemany(
    'INSERT OR REPLACE INTO products (name, price, url) VALUES (?, ?, ?)',
    products
)

conn.commit()

# Query data
cursor.execute('SELECT * FROM products WHERE price < 1000')
results = cursor.fetchall()

for row in results:
    print(row)

conn.close()
```

**Using Pandas with SQLite**:

```python
import pandas as pd
import sqlite3

# Write DataFrame to SQLite
conn = sqlite3.connect('products.db')
df.to_sql('products', conn, if_exists='replace', index=False)

# Read from SQLite
df = pd.read_sql_query('SELECT * FROM products WHERE price > 50', conn)

# Append instead of replace
df.to_sql('products', conn, if_exists='append', index=False)

conn.close()
```

**SQLite with Context Manager**:

```python
import sqlite3
from contextlib import closing

def save_to_sqlite(data, db_path='products.db'):
    with closing(sqlite3.connect(db_path)) as conn:
        with conn:
            cursor = conn.cursor()
            
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS products (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT,
                    price REAL,
                    url TEXT UNIQUE
                )
            ''')
            
            cursor.executemany(
                'INSERT OR IGNORE INTO products (name, price, url) VALUES (?, ?, ?)',
                [(d['name'], d['price'], d['url']) for d in data]
            )
```

### PostgreSQL/MySQL Storage

**PostgreSQL with psycopg2**:

```python
import psycopg2
from psycopg2.extras import execute_values

# Connect
conn = psycopg2.connect(
    host="localhost",
    database="scraping_db",
    user="user",
    password="password"
)

cursor = conn.cursor()

# Create table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS products (
        id SERIAL PRIMARY KEY,
        name VARCHAR(255),
        price DECIMAL(10, 2),
        url VARCHAR(500) UNIQUE,
        scraped_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
''')

# Bulk insert
data = [
    ('Laptop', 999.99, 'https://example.com/laptop'),
    ('Mouse', 29.99, 'https://example.com/mouse'),
]

execute_values(
    cursor,
    'INSERT INTO products (name, price, url) VALUES %s ON CONFLICT (url) DO NOTHING',
    data
)

conn.commit()
cursor.close()
conn.close()
```

**Using SQLAlchemy (ORM)**:

```python
from sqlalchemy import create_engine, Column, Integer, String, Float, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from datetime import datetime

Base = declarative_base()

class Product(Base):
    __tablename__ = 'products'
    
    id = Column(Integer, primary_key=True)
    name = Column(String(255))
    price = Column(Float)
    url = Column(String(500), unique=True)
    scraped_at = Column(DateTime, default=datetime.utcnow)

# Create engine
engine = create_engine('postgresql://user:pass@localhost/scraping_db')
Base.metadata.create_all(engine)

# Create session
Session = sessionmaker(bind=engine)
session = Session()

# Insert data
product = Product(name='Laptop', price=999.99, url='https://example.com/laptop')
session.add(product)
session.commit()

# Query data
products = session.query(Product).filter(Product.price < 1000).all()
for p in products:
    print(f'{p.name}: ${p.price}')

session.close()
```

### MongoDB Storage

**Using PyMongo**:

```python
from pymongo import MongoClient
from datetime import datetime

# Connect
client = MongoClient('mongodb://localhost:27017/')
db = client['scraping_db']
collection = db['products']

# Insert one
product = {
    'name': 'Laptop',
    'price': 999.99,
    'url': 'https://example.com/laptop',
    'scraped_at': datetime.utcnow()
}

result = collection.insert_one(product)
print(f'Inserted ID: {result.inserted_id}')

# Insert many
products = [
    {'name': 'Laptop', 'price': 999.99},
    {'name': 'Mouse', 'price': 29.99},
]

result = collection.insert_many(products)

# Query
products = collection.find({'price': {'$lt': 1000}})
for product in products:
    print(product)

# Update
collection.update_one(
    {'url': 'https://example.com/laptop'},
    {'$set': {'price': 899.99}},
    upsert=True  # Insert if doesn't exist
)

# Delete
collection.delete_many({'price': {'$lt': 10}})

client.close()
```

### Excel Output

**Using openpyxl**:

```python
from openpyxl import Workbook
from openpyxl.styles import Font, PatternFill

# Create workbook
wb = Workbook()
ws = wb.active
ws.title = "Products"

# Headers
headers = ['Name', 'Price', 'Stock', 'URL']
ws.append(headers)

# Style headers
for cell in ws[1]:
    cell.font = Font(bold=True)
    cell.fill = PatternFill(start_color="DDDDDD", end_color="DDDDDD", fill_type="solid")

# Add data
products = [
    ['Laptop', 999.99, 10, 'https://example.com/laptop'],
    ['Mouse', 29.99, 50, 'https://example.com/mouse'],
]

for product in products:
    ws.append(product)

# Auto-adjust column widths
for column in ws.columns:
    max_length = 0
    column_letter = column[0].column_letter
    for cell in column:
        if cell.value:
            max_length = max(max_length, len(str(cell.value)))
    ws.column_dimensions[column_letter].width = max_length + 2

wb.save('products.xlsx')
```

**Using Pandas**:

```python
# Write to Excel
df.to_excel('products.xlsx', index=False, sheet_name='Products')

# Multiple sheets
with pd.ExcelWriter('products.xlsx') as writer:
    df_electronics.to_excel(writer, sheet_name='Electronics', index=False)
    df_books.to_excel(writer, sheet_name='Books', index=False)

# With formatting
with pd.ExcelWriter('products.xlsx', engine='openpyxl') as writer:
    df.to_excel(writer, sheet_name='Products', index=False)
    
    workbook = writer.book
    worksheet = writer.sheets['Products']
    
    # Format headers
    for cell in worksheet[1]:
        cell.font = Font(bold=True)
```

### Google Sheets Integration

**Using gspread**:

```python
import gspread
from oauth2client.service_account import ServiceAccountCredentials

# Setup
scope = ['https://spreadsheets.google.com/feeds',
         'https://www.googleapis.com/auth/drive']

creds = ServiceAccountCredentials.from_json_keyfile_name('credentials.json', scope)
client = gspread.authorize(creds)

# Open spreadsheet
sheet = client.open('Products').sheet1

# Write data
products = [
    ['Name', 'Price', 'Stock'],
    ['Laptop', 999.99, 10],
    ['Mouse', 29.99, 50]
]

sheet.update('A1', products)

# Append rows
sheet.append_row(['Keyboard', 79.99, 25])

# Read data
all_values = sheet.get_all_values()
print(all_values)

# Update cell
sheet.update_cell(2, 2, 899.99)  # Row 2, Column 2

# Batch update (more efficient)
cell_list = sheet.range('B2:B3')
cell_list[0].value = 899.99
cell_list[1].value = 24.99
sheet.update_cells(cell_list)
```

### Cloud Storage (AWS S3)

**Using boto3**:

```python
import boto3
import json

# Setup
s3 = boto3.client('s3',
    aws_access_key_id='YOUR_ACCESS_KEY',
    aws_secret_access_key='YOUR_SECRET_KEY'
)

bucket_name = 'scraping-data'

# Upload JSON
data = {'products': products}
s3.put_object(
    Bucket=bucket_name,
    Key='products/2027-02-09.json',
    Body=json.dumps(data),
    ContentType='application/json'
)

# Upload CSV
with open('products.csv', 'rb') as f:
    s3.upload_fileobj(f, bucket_name, 'products/2027-02-09.csv')

# Download
obj = s3.get_object(Bucket=bucket_name, Key='products/2027-02-09.json')
data = json.loads(obj['Body'].read())

# List objects
response = s3.list_objects_v2(Bucket=bucket_name, Prefix='products/')
for obj in response.get('Contents', []):
    print(obj['Key'])
```

