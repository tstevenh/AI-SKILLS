# Chapter 3: HTML Parsing with BeautifulSoup

## The Definitive Guide to Extracting Data from Web Pages

---

## Table of Contents

1. [Introduction to HTML Parsing](#1-introduction-to-html-parsing)
2. [Installation and Setup](#2-installation-and-setup)
3. [Creating BeautifulSoup Objects](#3-creating-beautifulsoup-objects)
4. [Understanding the Parse Tree](#4-understanding-the-parse-tree)
5. [Navigating the DOM](#5-navigating-the-dom)
6. [Searching the Tree: find() and find_all()](#6-searching-the-tree-find-and-find_all)
7. [CSS Selectors](#7-css-selectors)
8. [Extracting Text and Attributes](#8-extracting-text-and-attributes)
9. [Working with HTML Tables](#9-working-with-html-tables)
10. [Real-World Scraping Scenarios](#10-real-world-scraping-scenarios)
11. [Handling Malformed HTML](#11-handling-malformed-html)
12. [Modifying the Parse Tree](#12-modifying-the-parse-tree)
13. [Advanced Techniques](#13-advanced-techniques)
14. [Performance Optimization](#14-performance-optimization)
15. [Common Pitfalls and Solutions](#15-common-pitfalls-and-solutions)
16. [Integration Patterns](#16-integration-patterns)
17. [Best Practices](#17-best-practices)
18. [Practice Exercises](#18-practice-exercises)

---

## 1. Introduction to HTML Parsing

HTML parsing is the foundational skill of web scraping. Every web page you visit is ultimately an HTML document — a structured tree of elements containing text, links, images, and data. Before you can extract any information from a web page, you need to parse that HTML into a structured representation you can query programmatically. That's where BeautifulSoup comes in.

### What is HTML Parsing?

When your browser receives an HTML document from a web server, it parses the raw text into a Document Object Model (DOM) — a tree-like structure where every element, attribute, and piece of text becomes a node. HTML parsing in Python works the same way: you take raw HTML text and convert it into a navigable, searchable tree structure.

Consider this simple HTML:

```html
<html>
  <head><title>My Page</title></head>
  <body>
    <h1 class="title">Welcome</h1>
    <p>This is a paragraph with a <a href="/link">link</a>.</p>
  </body>
</html>
```

A parser converts this text into a tree:

```
html
├── head
│   └── title
│       └── "My Page"
└── body
    ├── h1 (class="title")
    │   └── "Welcome"
    └── p
        ├── "This is a paragraph with a "
        ├── a (href="/link")
        │   └── "link"
        └── "."
```

Once you have this tree, you can traverse it, search it, and extract exactly the data you need.

### Why BeautifulSoup?

Python has several HTML parsing options:

| Library | Speed | Ease of Use | Handles Bad HTML | Best For |
|---------|-------|-------------|------------------|----------|
| BeautifulSoup | Medium | Excellent | Excellent | General scraping |
| lxml | Fast | Medium | Good | Performance-critical |
| html.parser | Slow | Medium | Fair | No dependencies |
| html5lib | Slowest | Medium | Best | Standards compliance |
| Selectolax | Fastest | Medium | Good | High-volume parsing |

BeautifulSoup stands out because it provides an incredibly intuitive API for navigating and searching HTML. It's not actually a parser itself — it's a wrapper that sits on top of various parsers (html.parser, lxml, html5lib) and provides a uniform, Pythonic interface. This means you get the best of both worlds: an easy-to-use API with the parser engine of your choice.

BeautifulSoup has been the go-to HTML parsing library in Python for over 15 years. Its API is so well-designed that even complex extraction tasks can often be accomplished in a single line of code. It handles malformed HTML gracefully, provides multiple ways to search for elements, and integrates seamlessly with the rest of the Python ecosystem.

### When to Use BeautifulSoup vs. Other Approaches

BeautifulSoup is the right choice when:

- **You're scraping static HTML** — pages where the content is in the HTML source
- **The HTML is messy** — real-world HTML is rarely perfect, and BS4 handles it gracefully
- **You need readable, maintainable code** — BS4's API is self-documenting
- **You're doing moderate-scale scraping** — hundreds to thousands of pages
- **You need quick prototyping** — BS4 lets you go from idea to extraction in minutes

Consider alternatives when:

- **You need maximum speed** — lxml or selectolax parse faster for high-volume work
- **The page requires JavaScript** — you'll need Playwright/Selenium first, then BS4
- **You're doing simple regex extraction** — sometimes a regex is faster for trivial patterns
- **You're working with XML** — lxml is generally better for strict XML parsing

In practice, most professional scrapers use BeautifulSoup for the parsing layer, even when they use other tools for fetching (requests, httpx, Playwright) or orchestration (Scrapy, custom frameworks).

---

## 2. Installation and Setup

### Installing BeautifulSoup

BeautifulSoup 4 (the current version) is distributed as the `beautifulsoup4` package:

```bash
# Basic installation
pip install beautifulsoup4

# With lxml parser (recommended)
pip install beautifulsoup4 lxml

# With html5lib parser (most lenient)
pip install beautifulsoup4 html5lib

# Full scraping stack
pip install beautifulsoup4 lxml requests httpx
```

### Import Conventions

```python
# Standard import
from bs4 import BeautifulSoup

# Common alias
from bs4 import BeautifulSoup as BS

# Import specific classes (rarely needed)
from bs4 import NavigableString, Tag, Comment

# Full import for advanced work
from bs4 import BeautifulSoup, Tag, NavigableString, Comment, ProcessingInstruction
```

The standard convention is `from bs4 import BeautifulSoup` — virtually every tutorial, Stack Overflow answer, and production codebase uses this import. Stick with it for consistency.

### Choosing a Parser

BeautifulSoup supports four parsers, each with different tradeoffs:

```python
# Python's built-in parser (no extra install needed)
soup = BeautifulSoup(html, 'html.parser')

# lxml's HTML parser (fastest, recommended)
soup = BeautifulSoup(html, 'lxml')

# lxml's XML parser
soup = BeautifulSoup(html, 'lxml-xml')  # or 'xml'

# html5lib (most lenient, slowest)
soup = BeautifulSoup(html, 'html5lib')
```

**Our recommendation: Always use `lxml`.** It's the fastest parser, handles malformed HTML well, and is the de facto standard in production scraping. The only reason to use `html5lib` is when you need browser-level HTML correction for extremely broken markup. The built-in `html.parser` is fine for simple scripts where you don't want extra dependencies, but it's noticeably slower and occasionally handles edge cases differently.

Here's a comparison of how different parsers handle the same broken HTML:

```python
from bs4 import BeautifulSoup

broken_html = "<p>First<p>Second<p>Third"

# html.parser
soup = BeautifulSoup(broken_html, 'html.parser')
print(soup)
# <p>First</p><p>Second</p><p>Third</p>

# lxml
soup = BeautifulSoup(broken_html, 'lxml')
print(soup)
# <html><body><p>First</p><p>Second</p><p>Third</p></body></html>

# html5lib
soup = BeautifulSoup(broken_html, 'html5lib')
print(soup)
# <html><head></head><body><p>First</p><p>Second</p><p>Third</p></body></html>
```

Notice how lxml and html5lib wrap the content in a full HTML document structure, while html.parser leaves it as-is. This matters when you're searching for elements — with lxml, you'll always have `<html>` and `<body>` tags even if the original HTML didn't have them.

### Project Setup Template

Here's a starter template for any scraping project:

```python
"""Web scraping module with BeautifulSoup."""

import requests
from bs4 import BeautifulSoup
from typing import Optional


# Constants
PARSER = 'lxml'
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) '
                  'AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/120.0.0.0 Safari/537.36'
}


def fetch_and_parse(url: str, **kwargs) -> Optional[BeautifulSoup]:
    """Fetch a URL and return a BeautifulSoup object."""
    try:
        response = requests.get(url, headers=HEADERS, timeout=30, **kwargs)
        response.raise_for_status()
        return BeautifulSoup(response.text, PARSER)
    except requests.RequestException as e:
        print(f"Error fetching {url}: {e}")
        return None


def parse_html(html: str) -> BeautifulSoup:
    """Parse an HTML string into a BeautifulSoup object."""
    return BeautifulSoup(html, PARSER)
```

---

## 3. Creating BeautifulSoup Objects

### From a String

The most basic way to create a BeautifulSoup object:

```python
from bs4 import BeautifulSoup

html = """
<html>
<head><title>Test Page</title></head>
<body>
    <div id="content">
        <h1>Hello World</h1>
        <p class="intro">Welcome to my page.</p>
        <p class="body-text">This is the main content.</p>
    </div>
</body>
</html>
"""

soup = BeautifulSoup(html, 'lxml')
```

### From an HTTP Response

The most common real-world pattern:

```python
import requests
from bs4 import BeautifulSoup

response = requests.get('https://example.com')
soup = BeautifulSoup(response.text, 'lxml')

# IMPORTANT: Use response.text (decoded string), not response.content (bytes)
# Unless you want BeautifulSoup to handle encoding detection:
soup = BeautifulSoup(response.content, 'lxml')  # BS4 detects encoding
```

### From a File

```python
from bs4 import BeautifulSoup

# Reading from a saved HTML file
with open('page.html', 'r', encoding='utf-8') as f:
    soup = BeautifulSoup(f, 'lxml')

# Note: You can pass the file object directly — no need to read() first
# This is more memory-efficient for large files
```

### From httpx (Async)

```python
import httpx
from bs4 import BeautifulSoup

async def fetch_page(url: str) -> BeautifulSoup:
    async with httpx.AsyncClient() as client:
        response = await client.get(url)
        return BeautifulSoup(response.text, 'lxml')
```

### Encoding Handling

Encoding issues are one of the most common sources of garbled text in scraping. BeautifulSoup handles encoding intelligently:

```python
from bs4 import BeautifulSoup

# BeautifulSoup auto-detects encoding from the HTML meta tags
html_with_encoding = '<meta charset="utf-8"><p>Héllo Wörld</p>'
soup = BeautifulSoup(html_with_encoding, 'lxml')
print(soup.p.text)  # Héllo Wörld

# Force a specific encoding when passing bytes
response = requests.get('https://example.com')
soup = BeautifulSoup(response.content, 'lxml', from_encoding='utf-8')

# Check what encoding BeautifulSoup detected
print(soup.original_encoding)  # 'utf-8'

# For pages with incorrect encoding declarations:
response = requests.get('https://some-chinese-site.com')
# If the site declares gb2312 but is actually gb18030:
soup = BeautifulSoup(response.content, 'lxml', from_encoding='gb18030')
```

### Suppressing the Parser Warning

If you don't specify a parser, BeautifulSoup will warn you:

```python
# This triggers a warning:
soup = BeautifulSoup(html)
# UserWarning: No parser was explicitly specified...

# Always specify the parser to avoid the warning:
soup = BeautifulSoup(html, 'lxml')
```

---

## 4. Understanding the Parse Tree

### Types of Objects

BeautifulSoup represents HTML as four types of objects:

```python
from bs4 import BeautifulSoup, Tag, NavigableString, Comment

html = """
<div id="main">
    <!-- This is a comment -->
    <p>Hello <b>world</b></p>
</div>
"""
soup = BeautifulSoup(html, 'lxml')

# 1. BeautifulSoup — the document itself
print(type(soup))  # <class 'bs4.BeautifulSoup'>
print(soup.name)   # '[document]'

# 2. Tag — an HTML element
div = soup.find('div')
print(type(div))   # <class 'bs4.element.Tag'>
print(div.name)    # 'div'

# 3. NavigableString — text within a tag
p = soup.find('p')
text = p.string  # None (because p has mixed content)
b = soup.find('b')
text = b.string
print(type(text))  # <class 'bs4.element.NavigableString'>
print(text)        # 'world'

# 4. Comment — an HTML comment
comment = soup.find(string=lambda t: isinstance(t, Comment))
print(type(comment))  # <class 'bs4.element.Comment'>
print(comment)         # ' This is a comment '
```

### Tag Attributes

Every Tag object has a name and a dictionary of attributes:

```python
html = '<a href="https://example.com" class="link external" id="main-link" data-id="42">Click</a>'
soup = BeautifulSoup(html, 'lxml')
tag = soup.find('a')

# Access attributes like a dictionary
print(tag['href'])      # 'https://example.com'
print(tag['id'])        # 'main-link'
print(tag['data-id'])   # '42'
print(tag['class'])     # ['link', 'external'] — NOTE: class returns a list!

# Get attribute with default (avoids KeyError)
print(tag.get('href'))           # 'https://example.com'
print(tag.get('title'))          # None
print(tag.get('title', 'N/A'))   # 'N/A'

# Check if attribute exists
print(tag.has_attr('href'))   # True
print(tag.has_attr('title'))  # False

# Get all attributes
print(tag.attrs)  # {'href': 'https://example.com', 'class': ['link', 'external'], 'id': 'main-link', 'data-id': '42'}

# Multi-valued attributes (class, rel, etc.) return lists
# Single-valued attributes return strings
```

**Critical note about `class`:** In HTML, the `class` attribute can contain multiple space-separated values. BeautifulSoup always returns `class` as a **list**, even if there's only one class. This catches many beginners off guard:

```python
tag = BeautifulSoup('<div class="container">', 'lxml').div
print(tag['class'])      # ['container'] — a list, not a string!
print(tag['class'][0])   # 'container'
```

### The .string Property vs .text vs get_text()

This is one of the most confusing aspects of BeautifulSoup for beginners. There are three ways to get text, and they behave differently:

```python
html = """
<div>
    <p>Simple text</p>
    <p>Text with <b>bold</b> inside</p>
    <p>  Whitespace  text  </p>
</div>
"""
soup = BeautifulSoup(html, 'lxml')

# --- .string ---
# Returns NavigableString if tag has EXACTLY ONE text child
# Returns None if tag has multiple children
p1 = soup.find_all('p')[0]
print(p1.string)  # 'Simple text'

p2 = soup.find_all('p')[1]
print(p2.string)  # None (because p has mixed content: text + <b> + text)

# --- .text (property) ---
# Returns all text concatenated, including descendants
print(p2.text)  # 'Text with bold inside'

# --- .get_text() (method) ---
# Same as .text but with options
print(p2.get_text())           # 'Text with bold inside'
print(p2.get_text(separator=' '))  # 'Text with bold inside'
print(p2.get_text(separator='|'))  # 'Text with |bold| inside'
print(p2.get_text(strip=True))    # 'Text withboldinside'

# get_text() with both separator and strip:
div = soup.find('div')
print(div.get_text(separator=' ', strip=True))
# 'Simple text Text with bold inside Whitespace text'
```

**Rule of thumb:**
- Use `.string` when you expect a tag to contain only text (leaf nodes)
- Use `.get_text(separator=' ', strip=True)` for everything else — it's the most reliable
- Avoid `.text` in production code because it concatenates without separators

### The .strings and .stripped_strings Generators

For fine-grained control over text extraction:

```python
html = """
<div>
    <p>First paragraph</p>
    <p>Second paragraph</p>
    <p>  Third with spaces  </p>
</div>
"""
soup = BeautifulSoup(html, 'lxml')
div = soup.find('div')

# .strings yields all NavigableString descendants
for s in div.strings:
    print(repr(s))
# '\n    '
# 'First paragraph'
# '\n    '
# 'Second paragraph'
# '\n    '
# '  Third with spaces  '
# '\n'

# .stripped_strings strips whitespace and skips empty strings
for s in div.stripped_strings:
    print(repr(s))
# 'First paragraph'
# 'Second paragraph'
# 'Third with spaces'
```

---

## 5. Navigating the DOM

### Going Down: Children and Descendants

```python
html = """
<div id="container">
    <ul>
        <li>Item 1</li>
        <li>Item 2
            <ul>
                <li>Subitem 2a</li>
                <li>Subitem 2b</li>
            </ul>
        </li>
        <li>Item 3</li>
    </ul>
</div>
"""
soup = BeautifulSoup(html, 'lxml')
container = soup.find('div', id='container')

# Direct tag access (first matching child of that name)
print(container.ul)        # The <ul> tag
print(container.ul.li)     # First <li> — "Item 1"

# .children — direct children only (includes NavigableStrings)
for child in container.children:
    print(type(child).__name__, repr(child.name) if hasattr(child, 'name') else repr(str(child).strip()[:30]))

# .contents — same as children but as a list
print(len(container.contents))  # Includes whitespace text nodes

# .descendants — ALL descendants recursively
for desc in container.descendants:
    if isinstance(desc, str):
        text = desc.strip()
        if text:
            print(f"  Text: {text}")
    else:
        print(f"  Tag: <{desc.name}>")
```

### Going Up: Parents and Ancestors

```python
html = """
<html>
<body>
    <div class="wrapper">
        <article>
            <p id="target">Find my parents</p>
        </article>
    </div>
</body>
</html>
"""
soup = BeautifulSoup(html, 'lxml')
target = soup.find('p', id='target')

# .parent — immediate parent
print(target.parent.name)  # 'article'

# .parents — all ancestors
for parent in target.parents:
    print(parent.name)
# article
# div
# body
# html
# [document]
```

### Going Sideways: Siblings

```python
html = """
<div>
    <h2>Title</h2>
    <p>First paragraph</p>
    <p>Second paragraph</p>
    <p>Third paragraph</p>
    <footer>End</footer>
</div>
"""
soup = BeautifulSoup(html, 'lxml')
first_p = soup.find('p')

# .next_sibling / .previous_sibling
# WARNING: These include NavigableString (whitespace) nodes!
print(repr(first_p.next_sibling))           # '\n    ' (whitespace!)
print(first_p.next_sibling.next_sibling)     # <p>Second paragraph</p>

# .next_siblings / .previous_siblings (generators)
for sib in first_p.next_siblings:
    if sib.name:  # Skip whitespace text nodes
        print(sib)

# BETTER: .find_next_sibling() / .find_next_siblings() — skips text nodes
print(first_p.find_next_sibling('p'))   # <p>Second paragraph</p>
print(first_p.find_next_sibling('footer'))  # <footer>End</footer>

# Get all p siblings
all_p_siblings = first_p.find_next_siblings('p')
for p in all_p_siblings:
    print(p.text)
# Second paragraph
# Third paragraph
```

### Going Forward and Backward in Document Order

```python
html = """
<div>
    <p>One</p>
    <p>Two</p>
</div>
<div>
    <p>Three</p>
</div>
"""
soup = BeautifulSoup(html, 'lxml')
p_one = soup.find('p')

# .next_element — next thing in the document (could be text or tag)
print(p_one.next_element)  # 'One' (the NavigableString inside <p>)

# .find_next() — next matching element in document order
print(p_one.find_next('p'))  # <p>Two</p>

# .find_all_next() — all matching elements after this one
for p in p_one.find_all_next('p'):
    print(p.text)
# Two
# Three

# .find_previous() — works the same way, going backward
p_three = soup.find_all('p')[-1]
print(p_three.find_previous('p').text)  # 'Two'
```

---

## 6. Searching the Tree: find() and find_all()

These are the workhorses of BeautifulSoup. Master them and you can extract almost anything.

### find() — First Match

```python
html = """
<div class="products">
    <div class="product" data-id="1">
        <h3 class="name">Widget A</h3>
        <span class="price">$19.99</span>
        <p class="description">A fine widget.</p>
    </div>
    <div class="product" data-id="2">
        <h3 class="name">Widget B</h3>
        <span class="price">$29.99</span>
        <p class="description">A better widget.</p>
    </div>
</div>
"""
soup = BeautifulSoup(html, 'lxml')

# Find first matching tag
first_product = soup.find('div', class_='product')
print(first_product['data-id'])  # '1'

# find() returns None if nothing matches (not an exception)
result = soup.find('div', class_='nonexistent')
print(result)  # None

# This is why you should always check before accessing:
result = soup.find('div', class_='nonexistent')
if result:
    print(result.text)
else:
    print("Not found")
```

### find_all() — All Matches

```python
# Find all matching tags
products = soup.find_all('div', class_='product')
print(len(products))  # 2

for product in products:
    name = product.find('h3', class_='name').text
    price = product.find('span', class_='price').text
    print(f"{name}: {price}")
# Widget A: $19.99
# Widget B: $29.99
```

### Search Filters

BeautifulSoup's search methods accept various types of filters:

#### By Tag Name (String)

```python
# Find all <a> tags
links = soup.find_all('a')

# Find all <p> tags
paragraphs = soup.find_all('p')
```

#### By Multiple Tag Names (List)

```python
# Find all headings
headings = soup.find_all(['h1', 'h2', 'h3', 'h4', 'h5', 'h6'])

# Find all links and images
media = soup.find_all(['a', 'img'])
```

#### By Regular Expression

```python
import re

# Find all tags starting with 'h' (headings)
headings = soup.find_all(re.compile(r'^h\d'))

# Find all tags containing 'div' in their name
divs = soup.find_all(re.compile('div'))

# Find all tags with class matching a pattern
items = soup.find_all(class_=re.compile(r'item-\d+'))
```

#### By Function (Lambda)

```python
# Find all tags with exactly 2 attributes
tags = soup.find_all(lambda tag: len(tag.attrs) == 2)

# Find all divs that have an id but no class
divs = soup.find_all(lambda tag: tag.name == 'div' and tag.has_attr('id') and not tag.has_attr('class'))

# Find all tags with text longer than 100 characters
long_text = soup.find_all(lambda tag: tag.string and len(tag.string) > 100)

# Find all empty tags
empty = soup.find_all(lambda tag: not tag.contents or all(str(c).strip() == '' for c in tag.contents))
```

#### By True (Any Tag)

```python
# Find ALL tags (not text nodes)
all_tags = soup.find_all(True)
print(len(all_tags))

# Useful for counting or inspecting document structure
for tag in soup.find_all(True):
    print(tag.name)
```

### Filtering by Attributes

```python
html = """
<div>
    <a href="/page1" class="nav-link active" id="link1">Page 1</a>
    <a href="/page2" class="nav-link" id="link2">Page 2</a>
    <a href="https://external.com" class="external-link" target="_blank">External</a>
    <a href="/page3" class="nav-link disabled" data-category="main">Page 3</a>
</div>
"""
soup = BeautifulSoup(html, 'lxml')

# By class (use class_ because class is a Python keyword)
nav_links = soup.find_all('a', class_='nav-link')
print(len(nav_links))  # 3 (includes 'nav-link active' and 'nav-link disabled')

# IMPORTANT: class_ matching is partial — 'nav-link' matches any tag
# where 'nav-link' is one of the classes. It's not an exact match.

# By id
link = soup.find('a', id='link1')

# By any attribute using attrs dict
external = soup.find_all('a', attrs={'target': '_blank'})

# By data-* attributes (must use attrs dict)
categorized = soup.find_all('a', attrs={'data-category': 'main'})

# By href
internal_links = soup.find_all('a', href=re.compile(r'^/'))
external_links = soup.find_all('a', href=re.compile(r'^https?://'))

# Multiple attribute filters
specific = soup.find_all('a', class_='nav-link', id='link2')
```

### The `string` Parameter

Search by text content:

```python
html = """
<div>
    <p>Hello World</p>
    <p>Hello Python</p>
    <p>Goodbye World</p>
</div>
"""
soup = BeautifulSoup(html, 'lxml')

# Exact match
hello = soup.find('p', string='Hello World')
print(hello)  # <p>Hello World</p>

# Regex match
hellos = soup.find_all('p', string=re.compile(r'^Hello'))
print(len(hellos))  # 2

# Any string containing 'World'
worlds = soup.find_all('p', string=re.compile('World'))
print(len(worlds))  # 2

# CAVEAT: string only matches tags with DIRECT text content
# It won't match <p>Hello <b>World</b></p> because .string is None
```

### The `limit` Parameter

```python
# Only return first 5 matches
first_five = soup.find_all('a', limit=5)

# find() is equivalent to find_all(limit=1)[0]
# but returns None instead of empty list if no match
```

### The `recursive` Parameter

```python
html = """
<div id="outer">
    <div id="inner">
        <p>Deep paragraph</p>
    </div>
    <p>Shallow paragraph</p>
</div>
"""
soup = BeautifulSoup(html, 'lxml')
outer = soup.find('div', id='outer')

# recursive=True (default) — searches all descendants
all_p = outer.find_all('p', recursive=True)
print(len(all_p))  # 2

# recursive=False — searches only direct children
direct_p = outer.find_all('p', recursive=False)
print(len(direct_p))  # 1 (only "Shallow paragraph")
```

---

## 7. CSS Selectors

BeautifulSoup supports CSS selectors via the `.select()` and `.select_one()` methods. If you're familiar with CSS or jQuery, this is often the fastest way to find elements.

### Basic Selectors

```python
html = """
<div id="main" class="container">
    <header class="site-header">
        <nav>
            <a href="/" class="logo">Home</a>
            <a href="/about" class="nav-item">About</a>
            <a href="/contact" class="nav-item active">Contact</a>
        </nav>
    </header>
    <main>
        <article class="post" data-id="1">
            <h2>First Post</h2>
            <p class="excerpt">This is the first post.</p>
            <div class="tags">
                <span class="tag">python</span>
                <span class="tag">scraping</span>
            </div>
        </article>
        <article class="post featured" data-id="2">
            <h2>Second Post</h2>
            <p class="excerpt">This is featured.</p>
            <div class="tags">
                <span class="tag">data</span>
            </div>
        </article>
    </main>
    <footer>
        <p>&copy; 2024</p>
    </footer>
</div>
"""
soup = BeautifulSoup(html, 'lxml')

# By tag name
articles = soup.select('article')

# By class
tags = soup.select('.tag')

# By ID
main = soup.select_one('#main')

# By attribute
featured = soup.select('article[data-id="2"]')

# By attribute presence
with_data = soup.select('[data-id]')

# By attribute prefix
starts_with = soup.select('a[href^="/"]')  # href starts with /

# By attribute suffix
ends_with = soup.select('a[href$="act"]')  # href ends with "act"

# By attribute contains
contains = soup.select('a[href*="about"]')  # href contains "about"
```

### Combinators

```python
# Descendant (space) — any depth
nav_links = soup.select('nav a')

# Child (>) — direct children only
direct_children = soup.select('nav > a')

# Adjacent sibling (+) — immediately following sibling
h2_then_p = soup.select('h2 + p')

# General sibling (~) — any following sibling
h2_siblings = soup.select('h2 ~ div')
```

### Pseudo-classes

```python
# :first-child
first_article = soup.select('article:first-child')

# :last-child
last_tag = soup.select('.tag:last-child')

# :nth-child()
second_article = soup.select('article:nth-child(2)')
even_items = soup.select('li:nth-child(even)')
odd_items = soup.select('li:nth-child(odd)')

# :not()
non_active = soup.select('a.nav-item:not(.active)')

# :has() — select parent based on children (BS4 supports this!)
articles_with_tags = soup.select('article:has(.tag)')
```

### Complex Selectors

```python
# Combining multiple selectors
result = soup.select('article.post.featured h2')
# Gets <h2> inside articles with both 'post' and 'featured' classes

# Multiple selectors (comma = OR)
links_and_buttons = soup.select('a, button')

# Chaining for precision
result = soup.select('#main > main > article:first-child .excerpt')

# Real-world examples:
# Get all external links in the main content
external = soup.select('main a[href^="http"]')

# Get text from specific table cells
cells = soup.select('table.data tbody tr td:nth-child(2)')

# Get all images with alt text
imgs_with_alt = soup.select('img[alt]:not([alt=""])')
```

### select_one() vs select()

```python
# select_one() — returns first match or None (like find())
first = soup.select_one('article.post')

# select() — returns list of all matches (like find_all())
all_posts = soup.select('article.post')

# Use select_one() when you expect a single element:
title = soup.select_one('h1')
if title:
    print(title.text)
```

### When to Use CSS Selectors vs find()/find_all()

**Prefer CSS selectors when:**
- You already know CSS selectors (most web developers do)
- You need complex nested queries (descendant, child, sibling combinators)
- You want concise code
- You're translating from browser DevTools (where you copy CSS selectors)

**Prefer find()/find_all() when:**
- You need regex matching on attributes
- You need lambda/function filters
- You need the `recursive=False` parameter
- You need `string` parameter for text matching
- The element is easily identifiable by a single attribute

In practice, the best scrapers use both freely, choosing whichever is more readable for each specific extraction.

---

## 8. Extracting Text and Attributes

### Text Extraction Patterns

```python
html = """
<div class="product-card">
    <h3 class="title">
        Premium Widget
        <span class="badge">New!</span>
    </h3>
    <div class="price">
        <span class="currency">$</span>
        <span class="amount">49.99</span>
        <small class="note">+ tax</small>
    </div>
    <p class="description">
        This is a <strong>premium</strong> widget with
        <em>exceptional</em> quality.
    </p>
    <ul class="features">
        <li>Feature 1</li>
        <li>Feature 2</li>
        <li>Feature 3</li>
    </ul>
</div>
"""
soup = BeautifulSoup(html, 'lxml')
card = soup.find('div', class_='product-card')

# Get the product title (without badge text)
title_tag = card.find('h3', class_='title')

# Method 1: get_text() gets ALL nested text (includes "New!")
print(title_tag.get_text(strip=True))  # 'Premium WidgetNew!'

# Method 2: Get only direct text using .find(string=True, recursive=False)
# Actually, better approach:
direct_text = title_tag.find(string=True, recursive=False)
print(direct_text.strip())  # 'Premium Widget'

# Method 3: Use NavigableString filtering
direct_texts = [s.strip() for s in title_tag.strings if s.strip() and s.parent == title_tag]
print(direct_texts[0])  # 'Premium Widget'

# Get the price
currency = card.select_one('.currency').text  # '$'
amount = card.select_one('.amount').text       # '49.99'
full_price = f"{currency}{amount}"             # '$49.99'

# Get description as clean text
desc = card.find('p', class_='description').get_text(separator=' ', strip=True)
print(desc)  # 'This is a premium widget with exceptional quality.'

# Get features as a list
features = [li.text.strip() for li in card.select('.features li')]
print(features)  # ['Feature 1', 'Feature 2', 'Feature 3']
```

### Extracting Links

```python
html = """
<div>
    <a href="/relative/path">Relative Link</a>
    <a href="https://example.com/absolute">Absolute Link</a>
    <a href="//cdn.example.com/resource">Protocol-relative</a>
    <a href="mailto:test@example.com">Email Link</a>
    <a href="javascript:void(0)">JS Link</a>
    <a href="#section">Anchor Link</a>
    <a>No href at all</a>
</div>
"""
soup = BeautifulSoup(html, 'lxml')

# Basic link extraction
for a in soup.find_all('a'):
    href = a.get('href')  # Use .get() to handle missing href
    text = a.get_text(strip=True)
    print(f"{text}: {href}")

# Filter to only real links (not mailto, javascript, anchors)
from urllib.parse import urljoin

base_url = 'https://example.com'

def extract_links(soup, base_url):
    """Extract and normalize all navigable links."""
    links = []
    for a in soup.find_all('a', href=True):  # href=True filters out tags without href
        href = a['href']
        
        # Skip non-navigable links
        if href.startswith(('javascript:', 'mailto:', 'tel:', '#')):
            continue
        
        # Resolve relative URLs
        full_url = urljoin(base_url, href)
        
        links.append({
            'url': full_url,
            'text': a.get_text(strip=True),
        })
    
    return links

links = extract_links(soup, base_url)
for link in links:
    print(f"{link['text']}: {link['url']}")
```

### Extracting Images

```python
html = """
<div class="gallery">
    <img src="/images/photo1.jpg" alt="Photo 1" width="800" height="600">
    <img src="/images/photo2.jpg" alt="Photo 2" loading="lazy" data-src="/images/photo2-hd.jpg">
    <img src="data:image/gif;base64,R0lGODlhAQABAAD/ACwAAAAAAQABAAACADs=" data-src="/images/photo3.jpg" alt="Lazy loaded">
    <picture>
        <source srcset="/images/photo4.webp" type="image/webp">
        <source srcset="/images/photo4.jpg" type="image/jpeg">
        <img src="/images/photo4.jpg" alt="Photo 4">
    </picture>
</div>
"""
soup = BeautifulSoup(html, 'lxml')

def extract_images(soup, base_url=''):
    """Extract all images, handling lazy loading patterns."""
    images = []
    for img in soup.find_all('img'):
        # Try multiple src attributes (lazy loading patterns)
        src = (
            img.get('data-src') or 
            img.get('data-lazy-src') or
            img.get('data-original') or
            img.get('src', '')
        )
        
        # Skip base64 placeholder images
        if src.startswith('data:'):
            src = img.get('data-src', '')
        
        if src and not src.startswith('data:'):
            full_url = urljoin(base_url, src) if base_url else src
            images.append({
                'url': full_url,
                'alt': img.get('alt', ''),
                'width': img.get('width'),
                'height': img.get('height'),
            })
    
    return images

images = extract_images(soup, 'https://example.com')
for img in images:
    print(f"{img['alt']}: {img['url']}")
```

### Extracting Structured Data (JSON-LD, Meta Tags)

```python
import json

html = """
<html>
<head>
    <title>Product Page - Widget Pro</title>
    <meta name="description" content="The best widget money can buy">
    <meta property="og:title" content="Widget Pro">
    <meta property="og:price:amount" content="49.99">
    <meta property="og:price:currency" content="USD">
    <script type="application/ld+json">
    {
        "@context": "https://schema.org",
        "@type": "Product",
        "name": "Widget Pro",
        "price": "49.99",
        "currency": "USD",
        "rating": {
            "@type": "AggregateRating",
            "ratingValue": "4.5",
            "reviewCount": "127"
        }
    }
    </script>
</head>
<body>...</body>
</html>
"""
soup = BeautifulSoup(html, 'lxml')

# Extract meta tags
def get_meta(soup, name=None, property=None):
    """Get content of a meta tag by name or property."""
    if name:
        tag = soup.find('meta', attrs={'name': name})
    elif property:
        tag = soup.find('meta', attrs={'property': property})
    else:
        return None
    return tag['content'] if tag else None

print(get_meta(soup, name='description'))         # 'The best widget money can buy'
print(get_meta(soup, property='og:title'))         # 'Widget Pro'
print(get_meta(soup, property='og:price:amount'))  # '49.99'

# Extract JSON-LD structured data
def get_json_ld(soup):
    """Extract all JSON-LD scripts from the page."""
    scripts = soup.find_all('script', type='application/ld+json')
    results = []
    for script in scripts:
        try:
            data = json.loads(script.string)
            results.append(data)
        except (json.JSONDecodeError, TypeError):
            continue
    return results

json_ld = get_json_ld(soup)
for data in json_ld:
    print(json.dumps(data, indent=2))
```

---

## 9. Working with HTML Tables

Tables are one of the most common data structures you'll encounter in scraping. Government data, financial reports, sports statistics, comparison charts — they're all in tables.

### Basic Table Extraction

```python
html = """
<table class="data-table">
    <thead>
        <tr>
            <th>Name</th>
            <th>Age</th>
            <th>City</th>
            <th>Score</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>Alice</td>
            <td>28</td>
            <td>New York</td>
            <td>95.5</td>
        </tr>
        <tr>
            <td>Bob</td>
            <td>34</td>
            <td>San Francisco</td>
            <td>87.2</td>
        </tr>
        <tr>
            <td>Charlie</td>
            <td>22</td>
            <td>Chicago</td>
            <td>91.8</td>
        </tr>
    </tbody>
</table>
"""
soup = BeautifulSoup(html, 'lxml')
table = soup.find('table', class_='data-table')

# Extract headers
headers = [th.get_text(strip=True) for th in table.find('thead').find_all('th')]
print(headers)  # ['Name', 'Age', 'City', 'Score']

# Extract rows
rows = []
for tr in table.find('tbody').find_all('tr'):
    cells = [td.get_text(strip=True) for td in tr.find_all('td')]
    rows.append(cells)

print(rows)
# [['Alice', '28', 'New York', '95.5'],
#  ['Bob', '34', 'San Francisco', '87.2'],
#  ['Charlie', '22', 'Chicago', '91.8']]

# Convert to list of dicts
data = [dict(zip(headers, row)) for row in rows]
print(data)
# [{'Name': 'Alice', 'Age': '28', 'City': 'New York', 'Score': '95.5'}, ...]
```

### Generic Table Parser

```python
def parse_table(table_element):
    """Parse any HTML table into a list of dictionaries.
    
    Handles:
    - Tables with <thead>/<tbody> or without
    - Tables with <th> in first row or standalone
    - Colspan and rowspan (basic handling)
    """
    # Try to get headers from <thead>
    thead = table_element.find('thead')
    if thead:
        headers = [th.get_text(strip=True) for th in thead.find_all(['th', 'td'])]
        body_rows = table_element.find('tbody', recursive=False)
        if body_rows:
            rows = body_rows.find_all('tr')
        else:
            rows = table_element.find_all('tr')[1:]  # Skip header row
    else:
        # Try first row as header
        all_rows = table_element.find_all('tr')
        if not all_rows:
            return []
        
        first_row = all_rows[0]
        if first_row.find('th'):
            headers = [th.get_text(strip=True) for th in first_row.find_all('th')]
            rows = all_rows[1:]
        else:
            # No headers detected, use column indices
            num_cols = len(first_row.find_all('td'))
            headers = [f'col_{i}' for i in range(num_cols)]
            rows = all_rows
    
    # Parse data rows
    data = []
    for tr in rows:
        cells = [td.get_text(strip=True) for td in tr.find_all(['td', 'th'])]
        if len(cells) == len(headers):
            data.append(dict(zip(headers, cells)))
        elif cells:  # Handle row length mismatch
            row_dict = {}
            for i, cell in enumerate(cells):
                key = headers[i] if i < len(headers) else f'col_{i}'
                row_dict[key] = cell
            data.append(row_dict)
    
    return data


# Usage
table = soup.find('table')
data = parse_table(table)
for row in data:
    print(row)
```

### Tables with Colspan and Rowspan

These are trickier but common in real-world tables:

```python
html = """
<table>
    <tr>
        <th>Name</th>
        <th colspan="2">Contact</th>
        <th>Score</th>
    </tr>
    <tr>
        <td>Alice</td>
        <td>alice@email.com</td>
        <td>555-0001</td>
        <td>95</td>
    </tr>
</table>
"""
soup = BeautifulSoup(html, 'lxml')

# For colspan, you might need to expand headers
def expand_headers(header_row):
    """Expand headers accounting for colspan."""
    headers = []
    for th in header_row.find_all(['th', 'td']):
        text = th.get_text(strip=True)
        colspan = int(th.get('colspan', 1))
        if colspan > 1:
            for i in range(colspan):
                headers.append(f"{text}_{i+1}" if colspan > 1 else text)
        else:
            headers.append(text)
    return headers

table = soup.find('table')
first_row = table.find('tr')
headers = expand_headers(first_row)
print(headers)  # ['Name', 'Contact_1', 'Contact_2', 'Score']
```

### Converting Tables to Pandas DataFrames

```python
import pandas as pd
from bs4 import BeautifulSoup

html = """
<table id="financial-data">
    <thead>
        <tr><th>Quarter</th><th>Revenue</th><th>Profit</th><th>Growth</th></tr>
    </thead>
    <tbody>
        <tr><td>Q1 2024</td><td>$1.2M</td><td>$240K</td><td>12%</td></tr>
        <tr><td>Q2 2024</td><td>$1.5M</td><td>$320K</td><td>25%</td></tr>
        <tr><td>Q3 2024</td><td>$1.3M</td><td>$195K</td><td>-13%</td></tr>
        <tr><td>Q4 2024</td><td>$1.8M</td><td>$405K</td><td>38%</td></tr>
    </tbody>
</table>
"""

# Method 1: Using pandas read_html (easiest)
dfs = pd.read_html(html)
df = dfs[0]
print(df)

# Method 2: Using BeautifulSoup + pandas (more control)
soup = BeautifulSoup(html, 'lxml')
table = soup.find('table', id='financial-data')
data = parse_table(table)  # Using our function from above
df = pd.DataFrame(data)

# Clean up the data
df['Revenue'] = df['Revenue'].str.replace(r'[$KM]', '', regex=True).astype(float)
df['Growth'] = df['Growth'].str.replace('%', '').astype(float)
print(df)
```

---

## 10. Real-World Scraping Scenarios

### Scenario 1: E-Commerce Product Listings

```python
"""Scrape product listings from an e-commerce category page."""

import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
from dataclasses import dataclass
from typing import Optional


@dataclass
class Product:
    name: str
    price: float
    original_price: Optional[float]
    url: str
    image_url: str
    rating: Optional[float]
    review_count: int
    in_stock: bool


def scrape_product_listing(html: str, base_url: str) -> list[Product]:
    """Parse a product listing page and extract all products.
    
    This pattern works for sites like Amazon, Best Buy, Target, etc.
    The selectors need to be adjusted per site.
    """
    soup = BeautifulSoup(html, 'lxml')
    products = []
    
    for card in soup.select('.product-card, .s-result-item, [data-component-type="product"]'):
        try:
            # Product name
            name_el = card.select_one('.product-title, h2 a, .s-title')
            if not name_el:
                continue
            name = name_el.get_text(strip=True)
            
            # Product URL
            link_el = card.select_one('a[href*="/product"], h2 a, .product-title a')
            url = urljoin(base_url, link_el['href']) if link_el else ''
            
            # Price extraction (handles various formats)
            price = extract_price(card)
            if price is None:
                continue
            
            # Original price (for sale items)
            original_el = card.select_one('.original-price, .was-price, .a-text-price')
            original_price = parse_price(original_el.get_text()) if original_el else None
            
            # Image
            img_el = card.select_one('img')
            image_url = ''
            if img_el:
                image_url = img_el.get('data-src') or img_el.get('src', '')
                image_url = urljoin(base_url, image_url)
            
            # Rating
            rating = None
            rating_el = card.select_one('[class*="rating"], .star-rating')
            if rating_el:
                # Try aria-label first: "4.5 out of 5 stars"
                aria = rating_el.get('aria-label', '')
                if aria:
                    import re
                    match = re.search(r'([\d.]+)\s*(?:out of|/)', aria)
                    if match:
                        rating = float(match.group(1))
            
            # Review count
            review_count = 0
            review_el = card.select_one('.review-count, [class*="review"]')
            if review_el:
                import re
                match = re.search(r'([\d,]+)', review_el.get_text())
                if match:
                    review_count = int(match.group(1).replace(',', ''))
            
            # Stock status
            stock_el = card.select_one('.stock-status, .availability')
            in_stock = True
            if stock_el:
                stock_text = stock_el.get_text(strip=True).lower()
                in_stock = 'out of stock' not in stock_text
            
            products.append(Product(
                name=name,
                price=price,
                original_price=original_price,
                url=url,
                image_url=image_url,
                rating=rating,
                review_count=review_count,
                in_stock=in_stock,
            ))
            
        except Exception as e:
            print(f"Error parsing product card: {e}")
            continue
    
    return products


def extract_price(element) -> Optional[float]:
    """Extract price from various HTML patterns."""
    import re
    
    # Try structured price elements
    for selector in ['.price-current', '.sale-price', '.a-price .a-offscreen', '.price']:
        price_el = element.select_one(selector)
        if price_el:
            return parse_price(price_el.get_text())
    
    # Fallback: find any text that looks like a price
    text = element.get_text()
    match = re.search(r'\$[\d,]+\.?\d*', text)
    if match:
        return parse_price(match.group())
    
    return None


def parse_price(text: str) -> Optional[float]:
    """Convert a price string to float."""
    import re
    if not text:
        return None
    cleaned = re.sub(r'[^\d.]', '', text)
    try:
        return float(cleaned)
    except ValueError:
        return None
```

### Scenario 2: News Article Extraction

```python
"""Extract article content from news websites."""

from bs4 import BeautifulSoup
from dataclasses import dataclass
from datetime import datetime
from typing import Optional
import re


@dataclass
class Article:
    title: str
    author: Optional[str]
    date: Optional[str]
    content: str
    summary: Optional[str]
    tags: list[str]
    images: list[dict]


def extract_article(html: str, url: str = '') -> Article:
    """Extract article content from a news page.
    
    Uses common patterns found across most news sites.
    Works well for WordPress, Medium, and similar CMS-based sites.
    """
    soup = BeautifulSoup(html, 'lxml')
    
    # Title — try multiple common patterns
    title = ''
    for selector in ['h1.entry-title', 'h1.article-title', 'h1.post-title', 
                      'article h1', '.headline h1', 'h1']:
        el = soup.select_one(selector)
        if el:
            title = el.get_text(strip=True)
            break
    
    # If still no title, fall back to <title> tag
    if not title:
        title_tag = soup.find('title')
        if title_tag:
            title = title_tag.get_text(strip=True).split('|')[0].strip()
    
    # Author
    author = None
    for selector in ['.author-name', '.byline a', '[rel="author"]', 
                      '.post-author', 'meta[name="author"]']:
        el = soup.select_one(selector)
        if el:
            if el.name == 'meta':
                author = el.get('content')
            else:
                author = el.get_text(strip=True)
            break
    
    # Date
    date = None
    # Try <time> tag first
    time_el = soup.find('time')
    if time_el:
        date = time_el.get('datetime') or time_el.get_text(strip=True)
    else:
        # Try meta tags
        for prop in ['article:published_time', 'datePublished', 'date']:
            meta = soup.find('meta', attrs={'property': prop}) or soup.find('meta', attrs={'name': prop})
            if meta:
                date = meta.get('content')
                break
    
    # Main content — the critical extraction
    content = extract_article_body(soup)
    
    # Summary/excerpt
    summary = None
    meta_desc = soup.find('meta', attrs={'name': 'description'})
    if meta_desc:
        summary = meta_desc.get('content')
    
    # Tags/categories
    tags = []
    for tag_el in soup.select('.tag a, .tags a, .post-tags a, [rel="tag"]'):
        tag_text = tag_el.get_text(strip=True)
        if tag_text and tag_text not in tags:
            tags.append(tag_text)
    
    # Images in article
    images = extract_article_images(soup, url)
    
    return Article(
        title=title,
        author=author,
        date=date,
        content=content,
        summary=summary,
        tags=tags,
        images=images,
    )


def extract_article_body(soup: BeautifulSoup) -> str:
    """Extract the main article text, removing ads and navigation."""
    
    # Find the article container
    article = None
    for selector in ['article .entry-content', 'article .post-content',
                      '.article-body', '.story-body', 'article',
                      '.post-content', '.entry-content', '#article-body',
                      'main .content', '[itemprop="articleBody"]']:
        article = soup.select_one(selector)
        if article:
            break
    
    if not article:
        # Last resort: find the largest text block
        article = soup.find('body') or soup
    
    # Remove unwanted elements before extracting text
    for unwanted in article.select(
        'script, style, nav, .ad, .advertisement, .social-share, '
        '.related-posts, .comments, .sidebar, .newsletter-signup, '
        '.popup, [class*="promo"], [class*="banner"], figure figcaption'
    ):
        unwanted.decompose()
    
    # Extract paragraphs
    paragraphs = []
    for p in article.find_all(['p', 'h2', 'h3', 'h4', 'blockquote', 'li']):
        text = p.get_text(separator=' ', strip=True)
        if len(text) > 20:  # Skip very short fragments (likely UI elements)
            if p.name in ('h2', 'h3', 'h4'):
                paragraphs.append(f"\n## {text}\n")
            elif p.name == 'blockquote':
                paragraphs.append(f"> {text}")
            elif p.name == 'li':
                paragraphs.append(f"• {text}")
            else:
                paragraphs.append(text)
    
    return '\n\n'.join(paragraphs)


def extract_article_images(soup, base_url):
    """Extract images from the article content."""
    from urllib.parse import urljoin
    images = []
    article = soup.select_one('article, .entry-content, .post-content') or soup
    
    for img in article.find_all('img'):
        src = img.get('data-src') or img.get('src', '')
        if src and not src.startswith('data:'):
            images.append({
                'url': urljoin(base_url, src),
                'alt': img.get('alt', ''),
                'caption': '',
            })
            # Check for caption
            figcaption = img.find_parent('figure')
            if figcaption:
                cap = figcaption.find('figcaption')
                if cap:
                    images[-1]['caption'] = cap.get_text(strip=True)
    
    return images
```

### Scenario 3: Job Board Scraping

```python
"""Scrape job listings from a job board."""

from bs4 import BeautifulSoup
from dataclasses import dataclass, field
from typing import Optional
import re


@dataclass
class JobListing:
    title: str
    company: str
    location: str
    salary: Optional[str]
    job_type: Optional[str]  # Full-time, Part-time, Contract
    description: str
    url: str
    posted_date: Optional[str]
    tags: list[str] = field(default_factory=list)


def scrape_job_listings(html: str, base_url: str) -> list[JobListing]:
    """Parse job listing cards from a search results page."""
    soup = BeautifulSoup(html, 'lxml')
    jobs = []
    
    # Common job card selectors across various job boards
    for card in soup.select('.job-card, .job-listing, .job-result, .jobsearch-result, [data-job-id]'):
        try:
            # Title
            title_el = card.select_one('h2 a, h3 a, .job-title a, .title a')
            if not title_el:
                title_el = card.select_one('h2, h3, .job-title, .title')
            if not title_el:
                continue
            title = title_el.get_text(strip=True)
            
            # URL
            link = card.select_one('a[href]')
            url = urljoin(base_url, link['href']) if link else ''
            
            # Company
            company = ''
            for sel in ['.company-name', '.employer', '[data-company]', '.company']:
                el = card.select_one(sel)
                if el:
                    company = el.get_text(strip=True)
                    break
            
            # Location
            location = ''
            for sel in ['.location', '.job-location', '[data-location]']:
                el = card.select_one(sel)
                if el:
                    location = el.get_text(strip=True)
                    break
            
            # Salary
            salary = None
            salary_el = card.select_one('.salary, .compensation, [data-salary]')
            if salary_el:
                salary = salary_el.get_text(strip=True)
            else:
                # Try to find salary in text
                text = card.get_text()
                salary_match = re.search(r'\$[\d,]+(?:\s*[-–]\s*\$[\d,]+)?(?:\s*(?:per|/)\s*(?:year|hour|yr|hr))?', text)
                if salary_match:
                    salary = salary_match.group()
            
            # Job type
            job_type = None
            for sel in ['.job-type', '.employment-type', '.badge']:
                el = card.select_one(sel)
                if el:
                    text = el.get_text(strip=True).lower()
                    if any(t in text for t in ['full-time', 'part-time', 'contract', 'remote']):
                        job_type = el.get_text(strip=True)
                        break
            
            # Description snippet
            desc_el = card.select_one('.description, .snippet, .summary')
            description = desc_el.get_text(strip=True) if desc_el else ''
            
            # Posted date
            date_el = card.select_one('.date, .posted-date, time')
            posted_date = None
            if date_el:
                posted_date = date_el.get('datetime') or date_el.get_text(strip=True)
            
            # Tags/skills
            tags = [tag.get_text(strip=True) for tag in card.select('.tag, .skill, .badge')]
            
            jobs.append(JobListing(
                title=title,
                company=company,
                location=location,
                salary=salary,
                job_type=job_type,
                description=description,
                url=url,
                posted_date=posted_date,
                tags=tags,
            ))
            
        except Exception as e:
            print(f"Error parsing job card: {e}")
            continue
    
    return jobs
```

### Scenario 4: Pagination Handling

```python
"""Handle paginated content."""

from bs4 import BeautifulSoup
import requests
from urllib.parse import urljoin
from typing import Generator, Optional
import time


def get_next_page_url(soup: BeautifulSoup, current_url: str) -> Optional[str]:
    """Find the 'next page' URL from common pagination patterns."""
    
    # Pattern 1: <a rel="next">
    next_link = soup.find('a', rel='next')
    if next_link and next_link.get('href'):
        return urljoin(current_url, next_link['href'])
    
    # Pattern 2: <a class="next"> or similar
    for selector in ['a.next', '.pagination .next a', '.pager .next a', 
                      'a[aria-label="Next"]', 'a[aria-label="Next page"]',
                      '.nav-next a']:
        next_link = soup.select_one(selector)
        if next_link and next_link.get('href'):
            return urljoin(current_url, next_link['href'])
    
    # Pattern 3: Link with "Next" or ">" text
    for a in soup.find_all('a'):
        text = a.get_text(strip=True)
        if text in ('Next', 'Next →', '›', '»', 'Next Page', '>'):
            href = a.get('href')
            if href and href != '#':
                return urljoin(current_url, href)
    
    return None  # No next page found


def paginated_scrape(
    start_url: str,
    parse_page,  # Callable that takes soup and returns data
    max_pages: int = 50,
    delay: float = 1.0,
    headers: dict = None,
) -> Generator:
    """Scrape through paginated results."""
    url = start_url
    page = 0
    session = requests.Session()
    if headers:
        session.headers.update(headers)
    
    while url and page < max_pages:
        print(f"Scraping page {page + 1}: {url}")
        
        try:
            response = session.get(url, timeout=30)
            response.raise_for_status()
        except requests.RequestException as e:
            print(f"Error fetching page: {e}")
            break
        
        soup = BeautifulSoup(response.text, 'lxml')
        
        # Parse this page's data
        items = parse_page(soup)
        if not items:
            print("No items found on page, stopping.")
            break
        
        yield from items
        
        # Find next page
        url = get_next_page_url(soup, url)
        page += 1
        
        if url:
            time.sleep(delay)
    
    print(f"Scraped {page} pages total.")


# Usage example:
def parse_products_page(soup):
    """Parse product cards from a single page."""
    products = []
    for card in soup.select('.product-card'):
        name = card.select_one('.name')
        price = card.select_one('.price')
        if name and price:
            products.append({
                'name': name.get_text(strip=True),
                'price': price.get_text(strip=True),
            })
    return products

# Scrape all pages
# for product in paginated_scrape('https://shop.example.com/products', parse_products_page):
#     print(product)
```

### Scenario 5: Form Data Extraction

```python
"""Extract form fields for automated submission."""

from bs4 import BeautifulSoup


def extract_form_data(soup: BeautifulSoup, form_selector: str = 'form') -> dict:
    """Extract all form fields and their default values.
    
    Useful for understanding what data a form expects,
    or for preparing form submissions with requests.
    """
    form = soup.select_one(form_selector)
    if not form:
        return {}
    
    data = {
        'action': form.get('action', ''),
        'method': form.get('method', 'GET').upper(),
        'fields': {},
    }
    
    # Input fields
    for input_tag in form.find_all('input'):
        name = input_tag.get('name')
        if not name:
            continue
        
        input_type = input_tag.get('type', 'text').lower()
        value = input_tag.get('value', '')
        
        if input_type in ('text', 'hidden', 'email', 'password', 'number', 'tel', 'url'):
            data['fields'][name] = value
        elif input_type == 'checkbox':
            if input_tag.has_attr('checked'):
                data['fields'][name] = value or 'on'
        elif input_type == 'radio':
            if input_tag.has_attr('checked'):
                data['fields'][name] = value
            elif name not in data['fields']:
                data['fields'][name] = None  # No default selected
    
    # Select/dropdown fields
    for select in form.find_all('select'):
        name = select.get('name')
        if not name:
            continue
        selected = select.find('option', selected=True)
        if selected:
            data['fields'][name] = selected.get('value', selected.get_text(strip=True))
        else:
            first_option = select.find('option')
            data['fields'][name] = first_option.get('value', '') if first_option else ''
    
    # Textarea fields
    for textarea in form.find_all('textarea'):
        name = textarea.get('name')
        if name:
            data['fields'][name] = textarea.get_text()
    
    return data
```

---

## 11. Handling Malformed HTML

Real-world HTML is messy. Sites have unclosed tags, mismatched quotes, invalid nesting, and all sorts of structural issues. BeautifulSoup handles most of this gracefully, but there are patterns you should know.

### Common Malformed HTML Patterns

```python
from bs4 import BeautifulSoup

# Unclosed tags
html = "<p>First paragraph<p>Second paragraph<p>Third"
soup = BeautifulSoup(html, 'lxml')
print(soup.prettify())
# lxml automatically closes the <p> tags

# Mismatched tags
html = "<div><p>Text</div></p>"
soup = BeautifulSoup(html, 'lxml')
print(soup.prettify())
# Parser fixes the nesting

# Missing quotes on attributes
html = '<div class=container id=main>Content</div>'
soup = BeautifulSoup(html, 'lxml')
div = soup.find('div')
print(div['class'])  # ['container']
print(div['id'])     # 'main'

# Broken entities
html = "<p>Price: $5 &amp sales &lt; 100</p>"
soup = BeautifulSoup(html, 'lxml')
print(soup.p.text)  # 'Price: $5 & sales < 100'

# Mixed content with stray text
html = """
<table>
Some stray text
<tr><td>Data</td></tr>
More stray text
</table>
"""
soup = BeautifulSoup(html, 'lxml')
# The parser will handle this, but results vary by parser
```

### Parser Differences on Edge Cases

```python
# This demonstrates why parser choice matters

# Self-closing tags in non-void elements
html = "<div/><p>Text</p>"

# html.parser: treats <div/> differently
soup_hp = BeautifulSoup(html, 'html.parser')
print(soup_hp)  # <div/><p>Text</p> (may vary)

# lxml: normalizes it
soup_lxml = BeautifulSoup(html, 'lxml')
print(soup_lxml.body)  # <body><div></div><p>Text</p></body>

# Conclusion: lxml is the safest bet for most real-world scraping
```

### Pre-Processing Broken HTML

Sometimes you need to clean HTML before parsing:

```python
import re
from bs4 import BeautifulSoup


def clean_html(html: str) -> str:
    """Pre-process HTML to handle common issues."""
    
    # Remove null bytes (some servers send these)
    html = html.replace('\x00', '')
    
    # Fix common encoding issues
    html = html.replace('â€™', "'")
    html = html.replace('â€"', "—")
    html = html.replace('â€œ', '"')
    html = html.replace('â€\x9d', '"')
    
    # Remove JavaScript that might interfere with parsing
    html = re.sub(r'<script[^>]*>.*?</script>', '', html, flags=re.DOTALL | re.IGNORECASE)
    
    # Remove style blocks
    html = re.sub(r'<style[^>]*>.*?</style>', '', html, flags=re.DOTALL | re.IGNORECASE)
    
    # Remove HTML comments (sometimes contain broken markup)
    html = re.sub(r'<!--.*?-->', '', html, flags=re.DOTALL)
    
    return html


# Usage
raw_html = requests.get('https://messy-site.com').text
cleaned = clean_html(raw_html)
soup = BeautifulSoup(cleaned, 'lxml')
```

### Using html5lib for Maximum Tolerance

```python
# html5lib parses HTML exactly like a browser would
# It's the slowest parser but handles the worst HTML

really_broken = """
<html>
<div>
<p>Paragraph 1
<p>Paragraph 2
<table>
<tr><td>Cell 1<td>Cell 2
<tr><td>Cell 3
</table>
<span>
unclosed span
"""

soup = BeautifulSoup(really_broken, 'html5lib')
print(soup.prettify())
# html5lib produces a perfectly valid HTML5 document
# Every tag is properly opened and closed
```

---

## 12. Modifying the Parse Tree

BeautifulSoup isn't just for reading HTML — you can also modify the tree. This is useful for cleaning content, removing unwanted elements, or preparing HTML for further processing.

### Removing Elements

```python
from bs4 import BeautifulSoup

html = """
<article>
    <h1>Article Title</h1>
    <div class="ad">Buy our stuff!</div>
    <p>First paragraph of the article.</p>
    <div class="social-share">Share on Twitter</div>
    <p>Second paragraph.</p>
    <script>trackPageView();</script>
    <div class="related">Related articles...</div>
    <p>Third paragraph.</p>
</article>
"""
soup = BeautifulSoup(html, 'lxml')
article = soup.find('article')

# .decompose() — removes the tag AND its contents from the tree entirely
for ad in article.select('.ad, .social-share, .related, script'):
    ad.decompose()

print(article.get_text(separator='\n', strip=True))
# Article Title
# First paragraph of the article.
# Second paragraph.
# Third paragraph.

# .extract() — removes but returns the element (useful if you need it later)
html = '<div><p>Keep</p><p class="remove">Remove</p></div>'
soup = BeautifulSoup(html, 'lxml')
removed = soup.find('p', class_='remove').extract()
print(soup.div)    # <div><p>Keep</p></div>
print(removed)     # <p class="remove">Remove</p>
```

### Modifying Tags

```python
from bs4 import BeautifulSoup

html = '<div><p class="old">Old text</p></div>'
soup = BeautifulSoup(html, 'lxml')
p = soup.find('p')

# Change text
p.string = "New text"
print(p)  # <p class="old">New text</p>

# Change attributes
p['class'] = ['new-class']
p['id'] = 'my-paragraph'
print(p)  # <p class="new-class" id="my-paragraph">New text</p>

# Remove an attribute
del p['class']
print(p)  # <p id="my-paragraph">New text</p>

# Change the tag name
p.name = 'div'
print(p)  # <div id="my-paragraph">New text</div>
```

### Adding New Elements

```python
from bs4 import BeautifulSoup, Tag

html = '<div id="container"><p>Existing</p></div>'
soup = BeautifulSoup(html, 'lxml')
container = soup.find('div', id='container')

# Create a new tag
new_tag = soup.new_tag('p', attrs={'class': 'added'})
new_tag.string = 'New paragraph'

# Append (add to end)
container.append(new_tag)

# Insert at specific position
another = soup.new_tag('h2')
another.string = 'New Heading'
container.insert(0, another)  # Insert at beginning

print(container.prettify())
# <div id="container">
#  <h2>New Heading</h2>
#  <p>Existing</p>
#  <p class="added">New paragraph</p>
# </div>
```

### Wrapping and Unwrapping

```python
from bs4 import BeautifulSoup

# Wrap — surround a tag with another tag
html = '<p>Important text</p>'
soup = BeautifulSoup(html, 'lxml')
p = soup.find('p')
wrapper = soup.new_tag('div', attrs={'class': 'highlight'})
p.wrap(wrapper)
print(soup.body)
# <body><div class="highlight"><p>Important text</p></div></body>

# Unwrap — replace a tag with its contents
html = '<p>Text with <span class="unwanted">extra</span> wrapper</p>'
soup = BeautifulSoup(html, 'lxml')
span = soup.find('span')
span.unwrap()
print(soup.p)  # <p>Text with extra wrapper</p>
```

### Replace With

```python
from bs4 import BeautifulSoup

html = '<p>Old <b>bold</b> text</p>'
soup = BeautifulSoup(html, 'lxml')

# Replace a tag with a string
bold = soup.find('b')
bold.replace_with('**bold**')
print(soup.p)  # <p>Old **bold** text</p>

# Replace with another tag
html = '<div><img src="photo.jpg" alt="Photo"></div>'
soup = BeautifulSoup(html, 'lxml')
img = soup.find('img')
new_p = soup.new_tag('p')
new_p.string = f"[Image: {img.get('alt', 'No alt')}]"
img.replace_with(new_p)
print(soup.div)  # <div><p>[Image: Photo]</p></div>
```

### Practical Use: HTML to Clean Markdown

```python
from bs4 import BeautifulSoup
import re


def html_to_markdown(html: str) -> str:
    """Convert HTML content to basic Markdown."""
    soup = BeautifulSoup(html, 'lxml')
    
    # Remove unwanted elements
    for tag in soup.select('script, style, nav, .ad'):
        tag.decompose()
    
    # Convert headings
    for i in range(1, 7):
        for h in soup.find_all(f'h{i}'):
            prefix = '#' * i
            h.replace_with(f"\n{prefix} {h.get_text(strip=True)}\n")
    
    # Convert bold
    for b in soup.find_all(['b', 'strong']):
        b.replace_with(f"**{b.get_text()}**")
    
    # Convert italic
    for i in soup.find_all(['i', 'em']):
        i.replace_with(f"*{i.get_text()}*")
    
    # Convert links
    for a in soup.find_all('a'):
        href = a.get('href', '')
        text = a.get_text(strip=True)
        a.replace_with(f"[{text}]({href})")
    
    # Convert images
    for img in soup.find_all('img'):
        alt = img.get('alt', '')
        src = img.get('src', '')
        img.replace_with(f"![{alt}]({src})")
    
    # Convert lists
    for li in soup.find_all('li'):
        li.replace_with(f"- {li.get_text(strip=True)}\n")
    
    # Convert blockquotes
    for bq in soup.find_all('blockquote'):
        lines = bq.get_text(strip=True).split('\n')
        bq.replace_with('\n'.join(f"> {line}" for line in lines))
    
    # Convert code blocks
    for code in soup.find_all('pre'):
        code.replace_with(f"\n```\n{code.get_text()}\n```\n")
    
    for code in soup.find_all('code'):
        code.replace_with(f"`{code.get_text()}`")
    
    # Get final text
    text = soup.get_text(separator='\n')
    
    # Clean up whitespace
    text = re.sub(r'\n{3,}', '\n\n', text)
    text = re.sub(r' {2,}', ' ', text)
    
    return text.strip()
```

---

## 13. Advanced Techniques

### Using SoupStrainer for Partial Parsing

When you only need a portion of a large HTML document, SoupStrainer can significantly improve performance by only parsing the elements you care about:

```python
from bs4 import BeautifulSoup, SoupStrainer

html = """
<html>
<head><title>Huge Page</title><!-- lots of meta, scripts, styles --></head>
<body>
    <nav><!-- huge navigation --></nav>
    <div class="content">
        <p class="data">Important data 1</p>
        <p class="data">Important data 2</p>
        <p class="data">Important data 3</p>
    </div>
    <footer><!-- huge footer --></footer>
</body>
</html>
"""

# Only parse <p> tags with class "data"
strainer = SoupStrainer('p', class_='data')
soup = BeautifulSoup(html, 'lxml', parse_only=strainer)

# The soup only contains matching elements — everything else was never parsed
for p in soup.find_all('p'):
    print(p.text)
# Important data 1
# Important data 2
# Important data 3

# This is MUCH faster for large documents where you only need specific elements

# More strainer examples:
only_links = SoupStrainer('a')
only_divs_with_id = SoupStrainer('div', id=True)
only_specific_class = SoupStrainer(class_='product-card')
```

### Encoding Output

```python
from bs4 import BeautifulSoup

html = '<p>Héllo Wörld — "quotes" & ampersands</p>'
soup = BeautifulSoup(html, 'lxml')

# Pretty print with specific encoding
print(soup.prettify())  # UTF-8 string
print(soup.prettify(encoding='utf-8'))  # bytes

# Encode for specific output
print(soup.encode('utf-8'))   # b'<html>...'
print(soup.encode('ascii'))   # Uses entities for non-ASCII: &eacute;

# Minimal entity encoding
print(soup.encode(formatter='minimal'))  # Only encode & < >
print(soup.decode(formatter='html'))     # Full HTML entity encoding
```

### Custom Formatters

```python
from bs4 import BeautifulSoup
from bs4.formatter import HTMLFormatter

html = '<a href="/path?a=1&b=2">Link</a>'
soup = BeautifulSoup(html, 'lxml')

# Default: encodes & as &amp; in attributes
print(soup.a.decode())  # <a href="/path?a=1&amp;b=2">Link</a>

# Custom formatter that preserves & in URLs
class URLPreservingFormatter(HTMLFormatter):
    def attributes(self, tag):
        for key, val in tag.attrs.items():
            yield key, val

formatter = URLPreservingFormatter()
print(soup.a.decode(formatter=formatter))
```

### Using BeautifulSoup with Playwright/Selenium Output

When you use browser automation to render JavaScript-heavy pages, you still need to parse the resulting HTML:

```python
# With Playwright (async)
from playwright.async_api import async_playwright
from bs4 import BeautifulSoup

async def scrape_spa(url: str):
    """Scrape a Single Page Application."""
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page()
        await page.goto(url, wait_until='networkidle')
        
        # Wait for specific content to load
        await page.wait_for_selector('.product-grid')
        
        # Get the fully rendered HTML
        html = await page.content()
        await browser.close()
    
    # Now parse with BeautifulSoup
    soup = BeautifulSoup(html, 'lxml')
    products = soup.select('.product-card')
    
    return [
        {
            'name': p.select_one('.name').text.strip(),
            'price': p.select_one('.price').text.strip(),
        }
        for p in products
    ]


# With Selenium
from selenium import webdriver
from bs4 import BeautifulSoup

def scrape_with_selenium(url: str):
    """Get rendered page source and parse with BS4."""
    driver = webdriver.Chrome()
    driver.get(url)
    
    # Wait for content
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC
    from selenium.webdriver.common.by import By
    
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, '.product-grid'))
    )
    
    # Get rendered HTML
    html = driver.page_source
    driver.quit()
    
    # Parse
    soup = BeautifulSoup(html, 'lxml')
    return soup
```

### Extracting Data from Inline JavaScript

Sometimes data is embedded in JavaScript variables within the HTML:

```python
import re
import json
from bs4 import BeautifulSoup

html = """
<html>
<head>
<script>
    window.__INITIAL_STATE__ = {"products":[{"id":1,"name":"Widget","price":29.99},{"id":2,"name":"Gadget","price":49.99}]};
    var config = {apiKey: "abc123", baseUrl: "/api"};
</script>
</head>
<body>...</body>
</html>
"""

soup = BeautifulSoup(html, 'lxml')

def extract_js_variable(soup, variable_name):
    """Extract a JavaScript variable's value from script tags."""
    for script in soup.find_all('script'):
        if script.string and variable_name in script.string:
            # Try to extract JSON-like assignment
            pattern = rf'{re.escape(variable_name)}\s*=\s*(\{{.*?\}}|\[.*?\])'
            match = re.search(pattern, script.string, re.DOTALL)
            if match:
                try:
                    return json.loads(match.group(1))
                except json.JSONDecodeError:
                    # Try fixing common JS-to-JSON issues
                    js_text = match.group(1)
                    # Replace single quotes with double quotes
                    js_text = re.sub(r"'", '"', js_text)
                    # Quote unquoted keys
                    js_text = re.sub(r'(\w+)\s*:', r'"\1":', js_text)
                    try:
                        return json.loads(js_text)
                    except json.JSONDecodeError:
                        return None
    return None


# Extract the initial state
state = extract_js_variable(soup, 'window.__INITIAL_STATE__')
if state:
    for product in state['products']:
        print(f"{product['name']}: ${product['price']}")
# Widget: $29.99
# Gadget: $49.99
```

### Extracting Data from Embedded JSON (Next.js, Nuxt, etc.)

Modern frameworks often embed data in the HTML as JSON:

```python
from bs4 import BeautifulSoup
import json

html = """
<html>
<body>
    <div id="__NEXT_DATA__">
        <script id="__NEXT_DATA__" type="application/json">
        {"props":{"pageProps":{"products":[{"name":"Widget","price":29.99}]}}}
        </script>
    </div>
</body>
</html>
"""

soup = BeautifulSoup(html, 'lxml')

# Next.js data
next_data = soup.find('script', id='__NEXT_DATA__')
if next_data:
    data = json.loads(next_data.string)
    products = data['props']['pageProps']['products']
    print(products)

# Nuxt.js data
nuxt_data = soup.find('script', string=re.compile(r'window\.__NUXT__'))
if nuxt_data:
    match = re.search(r'window\.__NUXT__\s*=\s*(.+?)(?:;?\s*$)', nuxt_data.string, re.DOTALL)
    if match:
        # Nuxt data is often a JS expression, not pure JSON
        # May need eval or custom parsing
        pass
```

### Processing Multiple HTML Files in Parallel

```python
from bs4 import BeautifulSoup
import concurrent.futures
import requests
from typing import Callable


def parallel_scrape(
    urls: list[str],
    parse_fn: Callable[[BeautifulSoup], dict],
    max_workers: int = 5,
    headers: dict = None,
) -> list[dict]:
    """Fetch and parse multiple URLs in parallel."""
    
    session = requests.Session()
    if headers:
        session.headers.update(headers)
    
    def fetch_and_parse(url: str) -> dict:
        try:
            response = session.get(url, timeout=30)
            response.raise_for_status()
            soup = BeautifulSoup(response.text, 'lxml')
            result = parse_fn(soup)
            result['_url'] = url
            result['_status'] = 'success'
            return result
        except Exception as e:
            return {'_url': url, '_status': 'error', '_error': str(e)}
    
    results = []
    with concurrent.futures.ThreadPoolExecutor(max_workers=max_workers) as executor:
        futures = {executor.submit(fetch_and_parse, url): url for url in urls}
        for future in concurrent.futures.as_completed(futures):
            results.append(future.result())
    
    return results


# Usage:
def parse_product_page(soup):
    title = soup.select_one('h1')
    price = soup.select_one('.price')
    return {
        'title': title.get_text(strip=True) if title else '',
        'price': price.get_text(strip=True) if price else '',
    }

# results = parallel_scrape(product_urls, parse_product_page)
```

---

## 14. Performance Optimization

### Parser Speed Comparison

```python
import time
from bs4 import BeautifulSoup

# Generate a large HTML document for testing
large_html = '<html><body>' + '<div class="item"><p>Text</p></div>' * 10000 + '</body></html>'

parsers = ['html.parser', 'lxml', 'html5lib']

for parser in parsers:
    start = time.time()
    soup = BeautifulSoup(large_html, parser)
    items = soup.find_all('div', class_='item')
    elapsed = time.time() - start
    print(f"{parser}: {elapsed:.3f}s ({len(items)} items found)")

# Typical results:
# lxml: 0.15s (10000 items found)
# html.parser: 0.45s (10000 items found)
# html5lib: 2.50s (10000 items found)
```

### Memory Optimization

```python
from bs4 import BeautifulSoup, SoupStrainer

large_html = '...'  # Imagine a 10MB HTML file

# BAD: Parse entire document when you only need links
soup = BeautifulSoup(large_html, 'lxml')
links = soup.find_all('a')

# GOOD: Only parse <a> tags
strainer = SoupStrainer('a')
soup = BeautifulSoup(large_html, 'lxml', parse_only=strainer)
links = soup.find_all('a')

# For very large files, process in chunks if possible
# (though this only works for certain HTML structures)
```

### Search Optimization

```python
from bs4 import BeautifulSoup

soup = BeautifulSoup(html, 'lxml')

# SLOW: Searching the entire document repeatedly
for i in range(1000):
    soup.find('div', class_='product', attrs={'data-id': str(i)})

# FAST: Narrow the search scope first
products_container = soup.find('div', class_='products')
for i in range(1000):
    products_container.find('div', attrs={'data-id': str(i)})

# FAST: Use CSS selectors for complex queries (often faster than chained find())
results = soup.select('#products .product[data-active="true"] .price')

# FAST: Use find_all() once instead of find() in a loop
all_products = {
    p['data-id']: p 
    for p in soup.find_all('div', class_='product')
}
product_42 = all_products.get('42')

# AVOID: Using recursive when you don't need it
# If you know the structure, use recursive=False to limit depth
container = soup.find('div', id='products')
# Only search direct children, not all descendants:
direct_products = container.find_all('div', class_='product', recursive=False)
```

### Lazy Evaluation Patterns

```python
from bs4 import BeautifulSoup
from typing import Generator


def lazy_extract(soup: BeautifulSoup, selector: str) -> Generator:
    """Lazily extract data from elements matching selector.
    
    Uses generator to avoid building large lists in memory.
    """
    for element in soup.select(selector):
        yield {
            'text': element.get_text(strip=True),
            'attrs': dict(element.attrs),
        }


# Only processes elements as you consume them
for item in lazy_extract(soup, '.product-card'):
    if item['text'].startswith('Widget'):
        print(item)
        break  # Stops processing remaining elements
```

---

## 15. Common Pitfalls and Solutions

### Pitfall 1: AttributeError on None

The number one BeautifulSoup error:

```python
# THE BUG:
soup = BeautifulSoup('<div>No h1 here</div>', 'lxml')
title = soup.find('h1').text  # AttributeError: 'NoneType' object has no attribute 'text'

# THE FIX: Always check for None
title_el = soup.find('h1')
title = title_el.text if title_el else 'No title'

# OR use a helper function
def safe_text(soup, selector, default=''):
    """Safely extract text from a CSS selector."""
    el = soup.select_one(selector)
    return el.get_text(strip=True) if el else default

title = safe_text(soup, 'h1', 'No title')
```

### Pitfall 2: Class Matching Confusion

```python
html = '<div class="product card featured">Content</div>'
soup = BeautifulSoup(html, 'lxml')

# This finds it (partial class match):
soup.find('div', class_='product')  # ✓ Found

# This also finds it:
soup.find('div', class_='featured')  # ✓ Found

# This does NOT find it (exact string match won't work):
soup.find('div', class_='product card featured')  # ✓ Actually works!

# To match multiple classes:
soup.find('div', class_=['product', 'featured'])  # ✗ Finds tags with EITHER class

# For exact multi-class matching, use CSS selector:
soup.select_one('div.product.card.featured')  # ✓ Must have ALL three classes
```

### Pitfall 3: .string Returns None for Mixed Content

```python
html = '<p>Hello <b>World</b></p>'
soup = BeautifulSoup(html, 'lxml')

p = soup.find('p')
print(p.string)  # None! Not 'Hello World'

# Why? .string only works when a tag has exactly ONE text child
# <p> has three children: 'Hello ', <b>, and nothing after <b>

# Use .get_text() instead:
print(p.get_text())  # 'Hello World'
```

### Pitfall 4: next_sibling Returns Whitespace

```python
html = """
<div>
    <p>First</p>
    <p>Second</p>
</div>
"""
soup = BeautifulSoup(html, 'lxml')
first_p = soup.find('p')

# This is whitespace, not the second <p>!
print(repr(first_p.next_sibling))  # '\n    '

# Solutions:
# 1. Use find_next_sibling()
print(first_p.find_next_sibling('p'))  # <p>Second</p>

# 2. Filter siblings manually
next_tag = first_p.next_sibling
while next_tag and isinstance(next_tag, str):
    next_tag = next_tag.next_sibling
print(next_tag)  # <p>Second</p>
```

### Pitfall 5: Encoding Issues

```python
# Response encoding mismatch
import requests

response = requests.get('https://some-site.com')
# requests guesses encoding, sometimes wrong

# Check what requests thinks:
print(response.encoding)  # might be 'ISO-8859-1' (wrong!)

# Check what the page declares:
# Look at response headers and HTML meta tags

# Fix 1: Let BeautifulSoup detect from content
soup = BeautifulSoup(response.content, 'lxml')  # Use .content (bytes), not .text

# Fix 2: Force correct encoding
response.encoding = 'utf-8'
soup = BeautifulSoup(response.text, 'lxml')

# Fix 3: Use apparent_encoding
response.encoding = response.apparent_encoding
soup = BeautifulSoup(response.text, 'lxml')
```

### Pitfall 6: Dynamic Content Not in HTML Source

```python
# You see data on the page but can't find it in BeautifulSoup
# This means the content is loaded by JavaScript AFTER the initial HTML

# Solution 1: Check for data in script tags
import json
for script in soup.find_all('script'):
    if script.string and 'products' in (script.string or ''):
        # Try to extract JSON from the script
        pass

# Solution 2: Check the Network tab for API calls
# Often, JavaScript loads data from an API endpoint
# You can call that API directly with requests

# Solution 3: Use a browser automation tool
# Playwright or Selenium to render the page, then parse with BS4
```

### Pitfall 7: find_all() vs select() Differences

```python
html = '<div class="a b"><div class="a"></div></div>'
soup = BeautifulSoup(html, 'lxml')

# find_all with class_ matches ANY tag containing that class
result1 = soup.find_all('div', class_='a')
print(len(result1))  # 2 (both divs have class 'a')

# CSS selector .a.b matches only tags with BOTH classes
result2 = soup.select('div.a.b')
print(len(result2))  # 1

# Be aware of this difference when building selectors!
```

### Pitfall 8: Stale References After Modifications

```python
html = '<ul><li>1</li><li>2</li><li>3</li></ul>'
soup = BeautifulSoup(html, 'lxml')

# DON'T modify while iterating
items = soup.find_all('li')
for item in items:
    item.decompose()  # This can cause issues!

# DO collect first, then modify
items = soup.find_all('li')
for item in list(items):  # list() creates a copy
    item.decompose()  # Safe!

# Or use a while loop
while True:
    item = soup.find('li')
    if not item:
        break
    item.decompose()
```

---

## 16. Integration Patterns

### Pattern 1: Requests + BeautifulSoup Session

```python
"""Production-ready scraping session with retries and rate limiting."""

import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry
from bs4 import BeautifulSoup
import time
from typing import Optional


class ScrapingSession:
    def __init__(
        self,
        base_url: str = '',
        delay: float = 1.0,
        max_retries: int = 3,
        headers: dict = None,
    ):
        self.base_url = base_url
        self.delay = delay
        self.last_request_time = 0
        
        # Configure session with retries
        self.session = requests.Session()
        retry_strategy = Retry(
            total=max_retries,
            backoff_factor=1,
            status_forcelist=[429, 500, 502, 503, 504],
        )
        adapter = HTTPAdapter(max_retries=retry_strategy)
        self.session.mount('http://', adapter)
        self.session.mount('https://', adapter)
        
        # Default headers
        self.session.headers.update(headers or {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) '
                          'AppleWebKit/537.36 Chrome/120.0.0.0 Safari/537.36',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            'Accept-Language': 'en-US,en;q=0.9',
        })
    
    def _rate_limit(self):
        """Enforce delay between requests."""
        elapsed = time.time() - self.last_request_time
        if elapsed < self.delay:
            time.sleep(self.delay - elapsed)
        self.last_request_time = time.time()
    
    def get_soup(self, url: str, **kwargs) -> Optional[BeautifulSoup]:
        """Fetch a URL and return parsed BeautifulSoup object."""
        self._rate_limit()
        
        try:
            response = self.session.get(url, timeout=30, **kwargs)
            response.raise_for_status()
            return BeautifulSoup(response.text, 'lxml')
        except requests.RequestException as e:
            print(f"Error fetching {url}: {e}")
            return None
    
    def get_all_pages(self, start_url: str, parse_fn, next_page_fn=None, max_pages=50):
        """Iterate through paginated results."""
        url = start_url
        page = 0
        all_data = []
        
        while url and page < max_pages:
            soup = self.get_soup(url)
            if not soup:
                break
            
            data = parse_fn(soup)
            if not data:
                break
            
            all_data.extend(data)
            
            if next_page_fn:
                url = next_page_fn(soup, url)
            else:
                url = get_next_page_url(soup, url)
            
            page += 1
        
        return all_data


# Usage:
scraper = ScrapingSession(delay=2.0)
soup = scraper.get_soup('https://example.com/products')
if soup:
    products = soup.select('.product')
    for p in products:
        print(p.select_one('.name').text)
```

### Pattern 2: Async with httpx

```python
"""Async scraping with httpx and BeautifulSoup."""

import httpx
from bs4 import BeautifulSoup
import asyncio
from typing import Optional


class AsyncScraper:
    def __init__(self, max_concurrent: int = 5, delay: float = 0.5):
        self.semaphore = asyncio.Semaphore(max_concurrent)
        self.delay = delay
        self.client = None
    
    async def __aenter__(self):
        self.client = httpx.AsyncClient(
            timeout=30,
            follow_redirects=True,
            headers={
                'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) '
                              'AppleWebKit/537.36 Chrome/120.0.0.0 Safari/537.36',
            },
        )
        return self
    
    async def __aexit__(self, *args):
        await self.client.aclose()
    
    async def get_soup(self, url: str) -> Optional[BeautifulSoup]:
        """Fetch and parse a single URL with rate limiting."""
        async with self.semaphore:
            try:
                response = await self.client.get(url)
                response.raise_for_status()
                await asyncio.sleep(self.delay)
                return BeautifulSoup(response.text, 'lxml')
            except httpx.HTTPError as e:
                print(f"Error: {url} - {e}")
                return None
    
    async def scrape_urls(self, urls: list[str], parse_fn) -> list:
        """Scrape multiple URLs concurrently."""
        tasks = [self._scrape_one(url, parse_fn) for url in urls]
        return await asyncio.gather(*tasks)
    
    async def _scrape_one(self, url: str, parse_fn) -> dict:
        soup = await self.get_soup(url)
        if soup:
            result = parse_fn(soup)
            result['_url'] = url
            return result
        return {'_url': url, '_error': 'Failed to fetch'}


# Usage:
async def main():
    urls = [f'https://example.com/product/{i}' for i in range(1, 101)]
    
    def parse_product(soup):
        return {
            'title': safe_text(soup, 'h1'),
            'price': safe_text(soup, '.price'),
        }
    
    async with AsyncScraper(max_concurrent=5, delay=1.0) as scraper:
        results = await scraper.scrape_urls(urls, parse_product)
    
    for r in results:
        print(r)

# asyncio.run(main())
```

### Pattern 3: Data Pipeline with BeautifulSoup

```python
"""Structured data extraction pipeline."""

import csv
import json
from bs4 import BeautifulSoup
from dataclasses import dataclass, asdict
from typing import List


@dataclass
class ScrapedItem:
    """Base class for scraped data."""
    source_url: str = ''
    scraped_at: str = ''


@dataclass
class ProductItem(ScrapedItem):
    name: str = ''
    price: float = 0.0
    category: str = ''
    sku: str = ''
    description: str = ''
    image_url: str = ''
    in_stock: bool = True


class DataPipeline:
    """Process and export scraped data."""
    
    def __init__(self):
        self.items: List[ScrapedItem] = []
        self.errors: List[dict] = []
    
    def process(self, item: ScrapedItem) -> ScrapedItem:
        """Clean and validate an item."""
        # Clean text fields
        for field_name, field_value in item.__dict__.items():
            if isinstance(field_value, str):
                setattr(item, field_name, field_value.strip())
        
        self.items.append(item)
        return item
    
    def to_csv(self, filepath: str):
        """Export items to CSV."""
        if not self.items:
            return
        
        with open(filepath, 'w', newline='', encoding='utf-8') as f:
            writer = csv.DictWriter(f, fieldnames=asdict(self.items[0]).keys())
            writer.writeheader()
            for item in self.items:
                writer.writerow(asdict(item))
        
        print(f"Exported {len(self.items)} items to {filepath}")
    
    def to_json(self, filepath: str):
        """Export items to JSON."""
        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump([asdict(item) for item in self.items], f, indent=2)
        
        print(f"Exported {len(self.items)} items to {filepath}")


# Usage:
pipeline = DataPipeline()

for url in product_urls:
    soup = scraper.get_soup(url)
    if not soup:
        continue
    
    item = ProductItem(
        source_url=url,
        name=safe_text(soup, 'h1.product-title'),
        price=float(safe_text(soup, '.price', '0').replace('$', '')),
        category=safe_text(soup, '.breadcrumb li:last-child'),
        sku=safe_text(soup, '.sku-value'),
        description=safe_text(soup, '.product-description'),
    )
    pipeline.process(item)

pipeline.to_csv('products.csv')
pipeline.to_json('products.json')
```

---

## 17. Best Practices

### 1. Always Specify the Parser

```python
# BAD — triggers warning, behavior may vary across systems
soup = BeautifulSoup(html)

# GOOD — explicit and predictable
soup = BeautifulSoup(html, 'lxml')
```

### 2. Use Defensive Extraction

```python
# BAD — will crash if element doesn't exist
title = soup.find('h1').text
price = soup.find('.price')['data-value']

# GOOD — handles missing elements gracefully
title_el = soup.find('h1')
title = title_el.get_text(strip=True) if title_el else ''

price_el = soup.find(class_='price')
price = price_el.get('data-value', '0') if price_el else '0'

# BEST — use a helper function
def safe_select(soup, selector, attr=None, default=''):
    """Safely extract text or attribute from a CSS selector."""
    el = soup.select_one(selector)
    if not el:
        return default
    if attr:
        return el.get(attr, default)
    return el.get_text(strip=True)

title = safe_select(soup, 'h1')
price = safe_select(soup, '.price', attr='data-value', default='0')
url = safe_select(soup, 'a.product-link', attr='href')
```

### 3. Separate Fetching from Parsing

```python
# BAD — mixing concerns
def get_products(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'lxml')
    return [p.text for p in soup.select('.product')]

# GOOD — separate concerns, easier to test
def fetch_html(url: str) -> str:
    """Fetch HTML from a URL."""
    response = requests.get(url, headers=HEADERS, timeout=30)
    response.raise_for_status()
    return response.text

def parse_products(html: str) -> list[dict]:
    """Parse product data from HTML string."""
    soup = BeautifulSoup(html, 'lxml')
    products = []
    for card in soup.select('.product-card'):
        products.append({
            'name': safe_select(card, '.name'),
            'price': safe_select(card, '.price'),
        })
    return products

# Now you can test parse_products() with saved HTML files!
```

### 4. Use CSS Selectors for Complex Queries

```python
# Verbose chained find() calls:
container = soup.find('div', id='main')
sidebar = container.find('div', class_='sidebar')
nav = sidebar.find('nav')
links = nav.find_all('a')

# Clean CSS selector:
links = soup.select('#main .sidebar nav a')
```

### 5. Handle Errors at the Right Level

```python
def scrape_product_page(url: str) -> dict:
    """Scrape a single product page with proper error handling."""
    result = {'url': url, 'status': 'error'}
    
    try:
        response = requests.get(url, timeout=30, headers=HEADERS)
        response.raise_for_status()
    except requests.RequestException as e:
        result['error'] = f'Fetch error: {e}'
        return result
    
    try:
        soup = BeautifulSoup(response.text, 'lxml')
    except Exception as e:
        result['error'] = f'Parse error: {e}'
        return result
    
    try:
        result['name'] = safe_select(soup, 'h1.product-title')
        result['price'] = safe_select(soup, '.price')
        result['description'] = safe_select(soup, '.description')
        result['status'] = 'success'
    except Exception as e:
        result['error'] = f'Extraction error: {e}'
    
    return result
```

### 6. Log What You Scrape

```python
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger('scraper')

def scrape_with_logging(url):
    logger.info(f"Scraping: {url}")
    
    soup = scraper.get_soup(url)
    if not soup:
        logger.warning(f"Failed to fetch: {url}")
        return None
    
    products = soup.select('.product-card')
    logger.info(f"Found {len(products)} products on {url}")
    
    if not products:
        logger.warning(f"No products found on {url} — selector may be wrong")
        # Log a snippet of the HTML for debugging
        logger.debug(f"Page title: {soup.title.string if soup.title else 'N/A'}")
        logger.debug(f"Body classes: {soup.body.get('class', []) if soup.body else 'N/A'}")
    
    return products
```

### 7. Cache HTML During Development

```python
import hashlib
import os

CACHE_DIR = '.html_cache'


def get_soup_cached(url: str, force_refresh: bool = False) -> BeautifulSoup:
    """Fetch and parse with local file caching.
    
    Saves HTTP requests during development/debugging.
    """
    os.makedirs(CACHE_DIR, exist_ok=True)
    
    # Create a filename from the URL
    url_hash = hashlib.md5(url.encode()).hexdigest()
    cache_path = os.path.join(CACHE_DIR, f'{url_hash}.html')
    
    if not force_refresh and os.path.exists(cache_path):
        with open(cache_path, 'r', encoding='utf-8') as f:
            html = f.read()
    else:
        response = requests.get(url, headers=HEADERS, timeout=30)
        response.raise_for_status()
        html = response.text
        with open(cache_path, 'w', encoding='utf-8') as f:
            f.write(html)
    
    return BeautifulSoup(html, 'lxml')
```

### 8. Version Your Selectors

```python
"""When scraping sites that change their HTML frequently,
keep selectors organized and easy to update."""

# selectors.py
SELECTORS = {
    'amazon': {
        'product_card': '.s-result-item[data-component-type="s-search-result"]',
        'title': 'h2 a span',
        'price_whole': '.a-price-whole',
        'price_fraction': '.a-price-fraction',
        'rating': '.a-icon-star-small .a-icon-alt',
        'review_count': '.s-underline-text',
        'image': '.s-image',
        # Updated: 2024-01-15
    },
    'ebay': {
        'product_card': '.s-item',
        'title': '.s-item__title',
        'price': '.s-item__price',
        'shipping': '.s-item__shipping',
        # Updated: 2024-01-10
    },
}


def get_selector(site: str, field: str) -> str:
    """Get a CSS selector for a specific site and field."""
    return SELECTORS.get(site, {}).get(field, '')
```

---

## 18. Practice Exercises

### Exercise 1: Basic Extraction

Given this HTML, extract all product names and prices:

```python
html = """
<div class="products">
    <div class="product">
        <h3>Laptop Pro 15</h3>
        <span class="price">$1,299.99</span>
        <span class="stock in-stock">In Stock</span>
    </div>
    <div class="product">
        <h3>Wireless Mouse</h3>
        <span class="price">$29.99</span>
        <span class="stock out-of-stock">Out of Stock</span>
    </div>
    <div class="product">
        <h3>USB-C Hub</h3>
        <span class="price">$49.99</span>
        <span class="stock in-stock">In Stock</span>
    </div>
</div>
"""

# Your solution:
from bs4 import BeautifulSoup

soup = BeautifulSoup(html, 'lxml')
for product in soup.select('.product'):
    name = product.find('h3').get_text(strip=True)
    price = product.select_one('.price').get_text(strip=True)
    in_stock = 'in-stock' in product.select_one('.stock')['class']
    print(f"{name}: {price} ({'In Stock' if in_stock else 'Out of Stock'})")
```

### Exercise 2: Table to CSV

Extract the data from this table and write it to a CSV file:

```python
html = """
<table id="sales-data">
    <thead>
        <tr>
            <th>Month</th>
            <th>Units Sold</th>
            <th>Revenue</th>
            <th>Profit Margin</th>
        </tr>
    </thead>
    <tbody>
        <tr><td>January</td><td>1,234</td><td>$45,678</td><td>23.5%</td></tr>
        <tr><td>February</td><td>1,567</td><td>$52,345</td><td>25.1%</td></tr>
        <tr><td>March</td><td>2,345</td><td>$78,901</td><td>28.7%</td></tr>
        <tr><td>April</td><td>1,890</td><td>$63,456</td><td>24.2%</td></tr>
    </tbody>
</table>
"""

# Solution:
import csv
from bs4 import BeautifulSoup

soup = BeautifulSoup(html, 'lxml')
table = soup.find('table', id='sales-data')

headers = [th.text for th in table.select('thead th')]
rows = []
for tr in table.select('tbody tr'):
    row = [td.text for td in tr.find_all('td')]
    rows.append(row)

with open('sales_data.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(headers)
    writer.writerows(rows)

print(f"Written {len(rows)} rows to sales_data.csv")
```

### Exercise 3: Nested Data Extraction

Extract the full hierarchy from this nested list:

```python
html = """
<ul class="category-tree">
    <li>
        <a href="/electronics">Electronics</a>
        <ul>
            <li>
                <a href="/electronics/phones">Phones</a>
                <ul>
                    <li><a href="/electronics/phones/iphone">iPhone</a></li>
                    <li><a href="/electronics/phones/android">Android</a></li>
                </ul>
            </li>
            <li><a href="/electronics/laptops">Laptops</a></li>
        </ul>
    </li>
    <li>
        <a href="/clothing">Clothing</a>
        <ul>
            <li><a href="/clothing/mens">Men's</a></li>
            <li><a href="/clothing/womens">Women's</a></li>
        </ul>
    </li>
</ul>
"""

# Solution:
from bs4 import BeautifulSoup


def parse_category_tree(ul_element, depth=0):
    """Recursively parse a nested category list."""
    categories = []
    
    for li in ul_element.find_all('li', recursive=False):
        link = li.find('a', recursive=False)
        if not link:
            continue
        
        category = {
            'name': link.get_text(strip=True),
            'url': link.get('href', ''),
            'depth': depth,
            'children': [],
        }
        
        # Check for nested <ul>
        sub_ul = li.find('ul', recursive=False)
        if sub_ul:
            category['children'] = parse_category_tree(sub_ul, depth + 1)
        
        categories.append(category)
    
    return categories


soup = BeautifulSoup(html, 'lxml')
tree = parse_category_tree(soup.find('ul', class_='category-tree'))

def print_tree(categories, indent=0):
    for cat in categories:
        print(f"{'  ' * indent}├── {cat['name']} ({cat['url']})")
        print_tree(cat['children'], indent + 1)

print_tree(tree)
# ├── Electronics (/electronics)
#   ├── Phones (/electronics/phones)
#     ├── iPhone (/electronics/phones/iphone)
#     ├── Android (/electronics/phones/android)
#   ├── Laptops (/electronics/laptops)
# ├── Clothing (/clothing)
#   ├── Men's (/clothing/mens)
#   ├── Women's (/clothing/womens)
```

### Exercise 4: Multi-Source Data Aggregation

Build a scraper that combines data from multiple page sections:

```python
html_exercise4 = """
<html>
<body>
    <div class="product-page">
        <div class="breadcrumb">
            <a href="/">Home</a> > <a href="/electronics">Electronics</a> > <a href="/electronics/phones">Phones</a>
        </div>
        
        <h1 class="product-title">SuperPhone X Pro Max</h1>
        
        <div class="product-gallery">
            <img src="/img/main.jpg" alt="SuperPhone front view" class="main-image">
            <div class="thumbnails">
                <img src="/img/thumb1.jpg" alt="Side view">
                <img src="/img/thumb2.jpg" alt="Back view">
                <img src="/img/thumb3.jpg" alt="Box contents">
            </div>
        </div>
        
        <div class="product-info">
            <div class="price-box">
                <span class="current-price">$999.99</span>
                <span class="original-price">$1,199.99</span>
                <span class="discount">-17%</span>
            </div>
            
            <div class="rating">
                <span class="stars" data-rating="4.7">★★★★★</span>
                <span class="review-count">2,847 reviews</span>
            </div>
            
            <div class="availability in-stock">
                <span>✓ In Stock</span>
                <span class="shipping">Free shipping</span>
            </div>
        </div>
        
        <div class="specifications">
            <table>
                <tr><th>Display</th><td>6.7" OLED</td></tr>
                <tr><th>Processor</th><td>A17 Bionic</td></tr>
                <tr><th>RAM</th><td>8 GB</td></tr>
                <tr><th>Storage</th><td>256 GB</td></tr>
                <tr><th>Battery</th><td>4,500 mAh</td></tr>
                <tr><th>Camera</th><td>48 MP + 12 MP + 12 MP</td></tr>
            </table>
        </div>
        
        <div class="reviews">
            <div class="review" data-rating="5">
                <span class="reviewer">John D.</span>
                <span class="date">2024-01-15</span>
                <p class="review-text">Amazing phone! Best I've ever owned.</p>
            </div>
            <div class="review" data-rating="4">
                <span class="reviewer">Sarah M.</span>
                <span class="date">2024-01-10</span>
                <p class="review-text">Great phone but battery could be better.</p>
            </div>
            <div class="review" data-rating="5">
                <span class="reviewer">Alex K.</span>
                <span class="date">2024-01-05</span>
                <p class="review-text">Worth every penny. Camera is incredible.</p>
            </div>
        </div>
    </div>
</body>
</html>
"""

# Solution:
from bs4 import BeautifulSoup
import re
import json


def scrape_product_page_ex4(html: str) -> dict:
    """Extract complete product data from a product detail page."""
    soup = BeautifulSoup(html, 'lxml')
    
    product = {}
    
    # Breadcrumb (category path)
    breadcrumbs = [a.get_text(strip=True) for a in soup.select('.breadcrumb a')]
    product['category_path'] = breadcrumbs
    
    # Title
    product['title'] = safe_text_ex(soup, 'h1.product-title')
    
    # Images
    main_img = soup.select_one('.main-image')
    product['main_image'] = main_img['src'] if main_img else ''
    product['thumbnails'] = [img['src'] for img in soup.select('.thumbnails img')]
    
    # Pricing
    product['price'] = parse_price_val(safe_text_ex(soup, '.current-price'))
    product['original_price'] = parse_price_val(safe_text_ex(soup, '.original-price'))
    product['discount'] = safe_text_ex(soup, '.discount')
    
    # Rating
    stars_el = soup.select_one('.stars')
    product['rating'] = float(stars_el['data-rating']) if stars_el else None
    review_text = safe_text_ex(soup, '.review-count')
    match = re.search(r'([\d,]+)', review_text)
    product['review_count'] = int(match.group(1).replace(',', '')) if match else 0
    
    # Availability
    avail = soup.select_one('.availability')
    product['in_stock'] = 'in-stock' in avail.get('class', []) if avail else False
    product['shipping'] = safe_text_ex(soup, '.shipping')
    
    # Specifications
    specs = {}
    for row in soup.select('.specifications tr'):
        th = row.find('th')
        td = row.find('td')
        if th and td:
            specs[th.get_text(strip=True)] = td.get_text(strip=True)
    product['specifications'] = specs
    
    # Reviews
    reviews = []
    for review_div in soup.select('.review'):
        reviews.append({
            'reviewer': safe_text_ex(review_div, '.reviewer'),
            'date': safe_text_ex(review_div, '.date'),
            'rating': int(review_div.get('data-rating', 0)),
            'text': safe_text_ex(review_div, '.review-text'),
        })
    product['reviews'] = reviews
    
    return product


def safe_text_ex(soup, selector, default=''):
    el = soup.select_one(selector)
    return el.get_text(strip=True) if el else default


def parse_price_val(text):
    cleaned = re.sub(r'[^\d.]', '', text)
    try:
        return float(cleaned)
    except ValueError:
        return None


# Run it
product = scrape_product_page_ex4(html_exercise4)
print(json.dumps(product, indent=2))
```

### Exercise 5: Building a Complete Scraping Script

Here's a full end-to-end scraping script that demonstrates everything we've learned:

```python
"""
Complete scraping script: Fetch, parse, and export data.
Demonstrates all BeautifulSoup concepts from this chapter.
"""

import requests
from bs4 import BeautifulSoup
import csv
import json
import time
import logging
import re
from dataclasses import dataclass, asdict, field
from typing import Optional, List
from urllib.parse import urljoin

# Setup logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s [%(levelname)s] %(message)s'
)
logger = logging.getLogger(__name__)

# Constants
PARSER = 'lxml'
BASE_URL = 'https://books.toscrape.com'  # A site designed for scraping practice
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (educational scraper)'
}


@dataclass
class Book:
    title: str
    price: float
    rating: int
    availability: str
    url: str
    image_url: str
    category: str = ''
    description: str = ''
    upc: str = ''


def safe_text_final(element, selector, default=''):
    """Safely extract text from a CSS selector."""
    if element is None:
        return default
    el = element.select_one(selector) if isinstance(selector, str) else selector
    return el.get_text(strip=True) if el else default


RATING_MAP = {
    'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5
}


def parse_rating(element) -> int:
    """Extract star rating from class name."""
    star_el = element.select_one('.star-rating')
    if star_el:
        classes = star_el.get('class', [])
        for cls in classes:
            if cls.lower() in RATING_MAP:
                return RATING_MAP[cls.lower()]
    return 0


def parse_listing_page(soup: BeautifulSoup) -> List[dict]:
    """Parse a category/listing page for book cards."""
    books = []
    
    for article in soup.select('article.product_pod'):
        title_el = article.select_one('h3 a')
        price_el = article.select_one('.price_color')
        
        if not title_el or not price_el:
            continue
        
        title = title_el.get('title', title_el.get_text(strip=True))
        price_text = price_el.get_text(strip=True)
        price = float(re.sub(r'[^0-9.]', '', price_text))
        
        rating = parse_rating(article)
        
        availability_el = article.select_one('.availability')
        availability = availability_el.get_text(strip=True) if availability_el else 'Unknown'
        
        detail_url = title_el.get('href', '')
        detail_url = urljoin(BASE_URL + '/catalogue/', detail_url)
        
        img_el = article.select_one('img')
        image_url = urljoin(BASE_URL, img_el['src']) if img_el else ''
        
        books.append({
            'title': title,
            'price': price,
            'rating': rating,
            'availability': availability,
            'url': detail_url,
            'image_url': image_url,
        })
    
    return books


def get_next_page(soup: BeautifulSoup, current_url: str) -> Optional[str]:
    """Find the next page URL."""
    next_btn = soup.select_one('.next a')
    if next_btn:
        return urljoin(current_url, next_btn['href'])
    return None


def parse_detail_page(soup: BeautifulSoup) -> dict:
    """Parse a book detail page for additional info."""
    info = {}
    
    # Description
    desc_el = soup.select_one('#product_description ~ p')
    info['description'] = desc_el.get_text(strip=True) if desc_el else ''
    
    # Category from breadcrumb
    breadcrumbs = soup.select('.breadcrumb li a')
    if len(breadcrumbs) >= 3:
        info['category'] = breadcrumbs[2].get_text(strip=True)
    
    # Product information table
    for row in soup.select('.table-striped tr'):
        th = row.find('th')
        td = row.find('td')
        if th and td:
            key = th.get_text(strip=True)
            val = td.get_text(strip=True)
            if key == 'UPC':
                info['upc'] = val
    
    return info


def main():
    """Main scraping function."""
    session = requests.Session()
    session.headers.update(HEADERS)
    
    all_books = []
    url = f'{BASE_URL}/catalogue/page-1.html'
    page_num = 1
    max_pages = 5  # Limit for demonstration
    
    while url and page_num <= max_pages:
        logger.info(f"Scraping page {page_num}: {url}")
        
        try:
            response = session.get(url, timeout=30)
            response.raise_for_status()
        except requests.RequestException as e:
            logger.error(f"Failed to fetch page {page_num}: {e}")
            break
        
        soup = BeautifulSoup(response.text, PARSER)
        books = parse_listing_page(soup)
        logger.info(f"Found {len(books)} books on page {page_num}")
        
        all_books.extend(books)
        
        url = get_next_page(soup, url)
        page_num += 1
        time.sleep(1)  # Be polite
    
    # Optionally fetch detail pages for more info
    logger.info(f"Fetching details for {min(5, len(all_books))} books...")
    for book in all_books[:5]:  # Limit for demonstration
        try:
            response = session.get(book['url'], timeout=30)
            response.raise_for_status()
            detail_soup = BeautifulSoup(response.text, PARSER)
            details = parse_detail_page(detail_soup)
            book.update(details)
            time.sleep(1)
        except requests.RequestException as e:
            logger.warning(f"Failed to fetch detail page: {e}")
    
    # Export results
    logger.info(f"Total books scraped: {len(all_books)}")
    
    # To JSON
    with open('books.json', 'w', encoding='utf-8') as f:
        json.dump(all_books, f, indent=2, ensure_ascii=False)
    logger.info("Exported to books.json")
    
    # To CSV
    if all_books:
        keys = all_books[0].keys()
        with open('books.csv', 'w', newline='', encoding='utf-8') as f:
            writer = csv.DictWriter(f, fieldnames=keys)
            writer.writeheader()
            writer.writerows(all_books)
        logger.info("Exported to books.csv")


if __name__ == '__main__':
    main()
```

---

## Summary

In this chapter, you've learned the complete toolkit for HTML parsing with BeautifulSoup:

1. **Setup** — Installing BS4, choosing parsers, and creating soup objects from strings, files, and HTTP responses
2. **The Parse Tree** — Understanding Tags, NavigableStrings, Comments, and how .string vs .text vs .get_text() differ
3. **Navigation** — Moving through the DOM via children, parents, siblings, and document order
4. **Searching** — Using find(), find_all() with strings, lists, regex, functions, and attribute filters
5. **CSS Selectors** — Leveraging select() and select_one() for concise, powerful element queries
6. **Data Extraction** — Pulling text, attributes, links, images, meta tags, JSON-LD, and structured data
7. **Tables** — Parsing HTML tables into structured data and DataFrames
8. **Real-World Scenarios** — E-commerce, news, job boards, pagination, and form extraction
9. **Malformed HTML** — Handling broken markup with different parsers and pre-processing
10. **Tree Modification** — Removing, adding, wrapping, and replacing elements
11. **Advanced Techniques** — SoupStrainer, JavaScript data extraction, browser automation integration
12. **Performance** — Parser benchmarks, memory optimization, and search efficiency
13. **Pitfalls** — The 8 most common mistakes and how to avoid them
14. **Integration** — Production patterns with requests, httpx, and data pipelines
15. **Best Practices** — Defensive coding, separation of concerns, caching, and selector management

BeautifulSoup is your Swiss Army knife for HTML parsing. Combined with good fetching practices (Chapter 2) and the scraping patterns we'll explore in later chapters, you now have the core skills to extract data from virtually any web page.

**Next up:** Chapter 4 — Advanced Selectors and XPath, where we'll dive deep into lxml's XPath support for even more powerful element selection.

---

*Chapter 3 of the Indexsy Web Scraping Skills Series*
*Last updated: February 2026*