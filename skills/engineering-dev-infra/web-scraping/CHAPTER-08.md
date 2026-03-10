# CHAPTER 08: Scraping Specific Platforms

## Introduction

While general scraping principles apply across websites, major platforms present unique challenges that require specialized approaches. Each platform has its own anti-bot measures, data structures, rate limits, and Terms of Service considerations.

This chapter provides battle-tested strategies for scraping the most common platforms: Amazon, Google SERPs, LinkedIn, Twitter/X, Instagram, Reddit, real estate sites, and job boards. We'll cover the technical challenges, anti-bot countermeasures, optimal data structures, and working code examples for each.

**Legal Disclaimer**: Always review and comply with each platform's Terms of Service and robots.txt. This chapter is for educational purposes and legitimate use cases like price monitoring, research, and personal data management.

## Amazon Product Data Extraction

Amazon is one of the most scraped e-commerce sites, and also one of the most challenging.

### Challenges

1. **Aggressive bot detection**: CAPTCHAs, IP bans, browser fingerprinting
2. **Dynamic pricing**: Prices change based on location, browsing history, time
3. **Complex page structure**: Multiple formats for product pages
4. **Rate limiting**: Very strict limits on request frequency
5. **JavaScript rendering**: Many elements loaded dynamically

### Anti-Bot Measures

- **Request signing**: Some API endpoints require signatures
- **Browser fingerprinting**: Canvas, WebGL, audio fingerprinting
- **Behavioral analysis**: Mouse movements, scroll patterns, timing
- **IP reputation**: Datacenter IPs often blocked immediately
- **CAPTCHA**: Frequent challenges, especially for high-value items

### Approach: Playwright + Residential Proxies

```python
from playwright.sync_api import sync_playwright
from typing import Dict, Optional
import random
import time
import json

class AmazonScraper:
    """Amazon product scraper with anti-detection measures"""
    
    BASE_URL = 'https://www.amazon.com'
    
    def __init__(self, proxy: Optional[str] = None):
        self.proxy = proxy
        self.playwright = None
        self.browser = None
        self.context = None
    
    def __enter__(self):
        self.playwright = sync_playwright().start()
        
        launch_options = {
            'headless': True,
            'args': [
                '--disable-blink-features=AutomationControlled',
                '--disable-dev-shm-usage'
            ]
        }
        
        self.browser = self.playwright.chromium.launch(**launch_options)
        
        # Context options
        context_options = {
            'viewport': {'width': 1920, 'height': 1080},
            'user_agent': self._get_user_agent(),
            'locale': 'en-US',
            'timezone_id': 'America/New_York'
        }
        
        if self.proxy:
            context_options['proxy'] = {'server': self.proxy}
        
        self.context = self.browser.new_context(**context_options)
        
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.context:
            self.context.close()
        if self.browser:
            self.browser.close()
        if self.playwright:
            self.playwright.stop()
    
    def _get_user_agent(self) -> str:
        """Get random realistic user agent"""
        agents = [
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
            'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
        ]
        return random.choice(agents)
    
    def search_products(self, query: str, max_pages: int = 3) -> list:
        """Search Amazon and extract product listings"""
        page = self.context.new_page()
        all_products = []
        
        try:
            # Navigate to search
            search_url = f"{self.BASE_URL}/s?k={query.replace(' ', '+')}"
            page.goto(search_url, wait_until='networkidle', timeout=30000)
            
            # Random wait to appear human
            time.sleep(random.uniform(2, 4))
            
            for page_num in range(max_pages):
                # Check for CAPTCHA
                if self._is_captcha_page(page):
                    print("CAPTCHA detected, stopping")
                    break
                
                # Extract products from current page
                products = self._extract_search_results(page)
                all_products.extend(products)
                
                print(f"Page {page_num + 1}: Found {len(products)} products")
                
                # Navigate to next page
                if page_num < max_pages - 1:
                    try:
                        next_button = page.locator('.s-pagination-next')
                        if next_button.count() > 0 and not next_button.get_attribute('aria-disabled'):
                            next_button.click()
                            page.wait_for_load_state('networkidle')
                            time.sleep(random.uniform(2, 4))
                        else:
                            break
                    except:
                        break
            
            return all_products
            
        finally:
            page.close()
    
    def _extract_search_results(self, page) -> list:
        """Extract product data from search results page"""
        products = page.evaluate("""
            () => {
                const results = [];
                
                document.querySelectorAll('[data-component-type="s-search-result"]').forEach(item => {
                    const asin = item.getAttribute('data-asin');
                    const titleEl = item.querySelector('h2 a span');
                    const priceWhole = item.querySelector('.a-price-whole');
                    const priceFraction = item.querySelector('.a-price-fraction');
                    const ratingEl = item.querySelector('.a-icon-star-small span');
                    const reviewsEl = item.querySelector('span[aria-label*="stars"] + span');
                    const imageEl = item.querySelector('img.s-image');
                    const linkEl = item.querySelector('h2 a');
                    
                    if (asin && titleEl) {
                        results.push({
                            asin: asin,
                            title: titleEl.textContent,
                            price: priceWhole && priceFraction ? 
                                `${priceWhole.textContent}${priceFraction.textContent}` : null,
                            rating: ratingEl ? ratingEl.textContent : null,
                            reviews: reviewsEl ? reviewsEl.textContent : null,
                            image: imageEl ? imageEl.src : null,
                            url: linkEl ? linkEl.href : null
                        });
                    }
                });
                
                return results;
            }
        """)
        
        return products
    
    def get_product_details(self, asin: str) -> Optional[Dict]:
        """Get detailed product information"""
        page = self.context.new_page()
        
        try:
            url = f"{self.BASE_URL}/dp/{asin}"
            page.goto(url, wait_until='networkidle', timeout=30000)
            
            # Random human-like wait
            time.sleep(random.uniform(2, 4))
            
            # Check for CAPTCHA
            if self._is_captcha_page(page):
                print("CAPTCHA detected")
                return None
            
            # Extract detailed data
            product = page.evaluate("""
                () => {
                    const data = {};
                    
                    // Title
                    const titleEl = document.querySelector('#productTitle');
                    data.title = titleEl ? titleEl.textContent.trim() : null;
                    
                    // Price
                    const priceEl = document.querySelector('.a-price .a-offscreen');
                    data.price = priceEl ? priceEl.textContent : null;
                    
                    // Rating
                    const ratingEl = document.querySelector('#acrPopover');
                    data.rating = ratingEl ? ratingEl.getAttribute('title') : null;
                    
                    // Review count
                    const reviewEl = document.querySelector('#acrCustomerReviewText');
                    data.reviews = reviewEl ? reviewEl.textContent : null;
                    
                    // Availability
                    const availEl = document.querySelector('#availability span');
                    data.availability = availEl ? availEl.textContent.trim() : null;
                    
                    // Features
                    const features = [];
                    document.querySelectorAll('#feature-bullets li span').forEach(el => {
                        const text = el.textContent.trim();
                        if (text) features.push(text);
                    });
                    data.features = features;
                    
                    // Description
                    const descEl = document.querySelector('#productDescription p');
                    data.description = descEl ? descEl.textContent.trim() : null;
                    
                    // Images
                    const images = [];
                    document.querySelectorAll('#altImages img').forEach(img => {
                        const src = img.src;
                        if (src && !src.includes('play-icon')) {
                            images.push(src.replace('_SS40_', '_SS500_'));
                        }
                    });
                    data.images = images;
                    
                    // Product details
                    const details = {};
                    document.querySelectorAll('#productDetails_detailBullets_sections1 tr').forEach(row => {
                        const label = row.querySelector('th');
                        const value = row.querySelector('td');
                        if (label && value) {
                            details[label.textContent.trim()] = value.textContent.trim();
                        }
                    });
                    data.details = details;
                    
                    return data;
                }
            """)
            
            product['asin'] = asin
            product['url'] = url
            
            return product
            
        except Exception as e:
            print(f"Error getting product {asin}: {e}")
            return None
        
        finally:
            page.close()
    
    def _is_captcha_page(self, page) -> bool:
        """Check if page shows CAPTCHA"""
        try:
            return page.locator('form[action*="validateCaptcha"]').count() > 0
        except:
            return False

# Usage
proxy = 'http://username:password@proxy-server.com:port'

with AmazonScraper(proxy=proxy) as scraper:
    # Search for products
    products = scraper.search_products('laptop', max_pages=3)
    print(f"Found {len(products)} products")
    
    # Get detailed info for first product
    if products:
        asin = products[0]['asin']
        details = scraper.get_product_details(asin)
        
        if details:
            print(json.dumps(details, indent=2))
```

### Data Structure

```python
from dataclasses import dataclass
from typing import List, Optional
from datetime import datetime

@dataclass
class AmazonProduct:
    """Amazon product data structure"""
    asin: str
    title: str
    price: Optional[float]
    currency: str
    rating: Optional[float]
    review_count: Optional[int]
    availability: str
    features: List[str]
    description: Optional[str]
    images: List[str]
    category: Optional[str]
    brand: Optional[str]
    seller: Optional[str]
    url: str
    scraped_at: datetime
    
    def to_dict(self):
        return {
            'asin': self.asin,
            'title': self.title,
            'price': self.price,
            'currency': self.currency,
            'rating': self.rating,
            'review_count': self.review_count,
            'availability': self.availability,
            'features': self.features,
            'description': self.description,
            'images': self.images,
            'category': self.category,
            'brand': self.brand,
            'seller': self.seller,
            'url': self.url,
            'scraped_at': self.scraped_at.isoformat()
        }
```

## Google SERP Scraping

Google Search Engine Results Pages are notoriously difficult to scrape.

### Challenges

1. **Very aggressive bot detection**: Google leads the industry
2. **Personalized results**: Results vary by location, history, device
3. **Frequent HTML changes**: Selectors break regularly
4. **Rate limiting**: Strict limits, IP bans common
5. **Legal concerns**: Google's ToS explicitly prohibit automated access

### Anti-Bot Measures

- **reCAPTCHA**: Frequent challenges
- **IP fingerprinting**: Sophisticated detection
- **Browser fingerprinting**: Advanced techniques
- **Cookie tracking**: Behavioral analysis
- **HTTP/2 fingerprinting**: Protocol-level detection

### Approach: Search API + Fallback Scraper

For production, use Google Custom Search API or SERPApi. For educational purposes:

```python
from playwright.sync_api import sync_playwright
import random
import time
from typing import List, Dict
from urllib.parse import quote_plus

class GoogleSerpScraper:
    """Google SERP scraper (use APIs in production!)"""
    
    def __init__(self, proxy: Optional[str] = None):
        self.proxy = proxy
    
    def search(self, query: str, num_results: int = 10) -> List[Dict]:
        """Search Google and extract results"""
        with sync_playwright() as p:
            # Launch with maximum stealth
            browser = p.chromium.launch(
                headless=False,  # Headless more easily detected
                args=[
                    '--disable-blink-features=AutomationControlled',
                    '--disable-dev-shm-usage',
                    '--no-sandbox'
                ]
            )
            
            context_options = {
                'viewport': {'width': 1920, 'height': 1080},
                'user_agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
                'locale': 'en-US',
                'timezone_id': 'America/New_York'
            }
            
            if self.proxy:
                context_options['proxy'] = {'server': self.proxy}
            
            context = browser.new_context(**context_options)
            page = context.new_page()
            
            # Inject stealth scripts
            page.add_init_script("""
                Object.defineProperty(navigator, 'webdriver', {
                    get: () => undefined
                });
                
                window.chrome = { runtime: {} };
                
                Object.defineProperty(navigator, 'plugins', {
                    get: () => [1, 2, 3, 4, 5]
                });
            """)
            
            try:
                # Navigate to Google
                page.goto('https://www.google.com', wait_until='networkidle')
                
                # Random wait
                time.sleep(random.uniform(1, 3))
                
                # Accept cookies if prompted
                try:
                    page.locator('button:has-text("Accept all")').click(timeout=3000)
                    time.sleep(1)
                except:
                    pass
                
                # Search
                search_box = page.locator('textarea[name="q"]')
                
                # Human-like typing
                for char in query:
                    search_box.type(char, delay=random.randint(50, 150))
                
                time.sleep(random.uniform(0.5, 1.5))
                
                # Submit search
                search_box.press('Enter')
                page.wait_for_load_state('networkidle')
                
                time.sleep(random.uniform(2, 4))
                
                # Extract results
                results = page.evaluate("""
                    () => {
                        const results = [];
                        
                        // Organic results
                        document.querySelectorAll('div.g').forEach(item => {
                            const linkEl = item.querySelector('a');
                            const titleEl = item.querySelector('h3');
                            const snippetEl = item.querySelector('.VwiC3b');
                            
                            if (linkEl && titleEl) {
                                results.push({
                                    title: titleEl.textContent,
                                    url: linkEl.href,
                                    snippet: snippetEl ? snippetEl.textContent : '',
                                    type: 'organic'
                                });
                            }
                        });
                        
                        // Featured snippet
                        const featuredSnippet = document.querySelector('.xpdopen');
                        if (featuredSnippet) {
                            const titleEl = featuredSnippet.querySelector('h3');
                            const snippetEl = featuredSnippet.querySelector('.hgKElc');
                            const linkEl = featuredSnippet.querySelector('a');
                            
                            results.unshift({
                                title: titleEl ? titleEl.textContent : '',
                                url: linkEl ? linkEl.href : '',
                                snippet: snippetEl ? snippetEl.textContent : '',
                                type: 'featured_snippet'
                            });
                        }
                        
                        // People Also Ask
                        const paa = [];
                        document.querySelectorAll('.related-question-pair').forEach(item => {
                            const questionEl = item.querySelector('.CSkcDe');
                            if (questionEl) {
                                paa.push({
                                    question: questionEl.textContent,
                                    type: 'people_also_ask'
                                });
                            }
                        });
                        
                        return {
                            organic: results,
                            people_also_ask: paa
                        };
                    }
                """)
                
                return results
                
            finally:
                context.close()
                browser.close()

# Usage (educational only - use APIs in production)
scraper = GoogleSerpScraper()
results = scraper.search('python web scraping', num_results=10)
```

### Better Approach: Use APIs

```python
import requests
from typing import List, Dict

class SERPApiClient:
    """Use SERPApi for reliable Google scraping"""
    
    def __init__(self, api_key: str):
        self.api_key = api_key
        self.base_url = 'https://serpapi.com/search'
    
    def search(self, query: str, location: str = 'United States', 
               num: int = 10) -> Dict:
        """Search Google via SERPApi"""
        params = {
            'q': query,
            'location': location,
            'num': num,
            'api_key': self.api_key,
            'engine': 'google'
        }
        
        response = requests.get(self.base_url, params=params)
        response.raise_for_status()
        
        return response.json()
    
    def parse_results(self, data: Dict) -> List[Dict]:
        """Parse SERPApi response"""
        results = []
        
        # Organic results
        for item in data.get('organic_results', []):
            results.append({
                'position': item.get('position'),
                'title': item.get('title'),
                'url': item.get('link'),
                'snippet': item.get('snippet'),
                'type': 'organic'
            })
        
        # Featured snippet
        if 'answer_box' in data:
            results.insert(0, {
                'position': 0,
                'title': data['answer_box'].get('title'),
                'url': data['answer_box'].get('link'),
                'snippet': data['answer_box'].get('answer') or data['answer_box'].get('snippet'),
                'type': 'featured_snippet'
            })
        
        return results

# Usage
client = SERPApiClient(api_key='your_api_key')
data = client.search('best laptops 2024')
results = client.parse_results(data)
```

## LinkedIn Profile Scraping

LinkedIn actively combats scraping with sophisticated detection.

### Challenges

1. **Login required**: Most content behind authentication
2. **Aggressive rate limiting**: Very strict
3. **Account bans**: Scraping accounts frequently banned
4. **Dynamic content**: Heavy JavaScript rendering
5. **Legal issues**: LinkedIn has sued scrapers

### Approach: Authenticated Session + Stealth

```python
from playwright.sync_api import sync_playwright
import time
import random
import json
from typing import Dict, Optional

class LinkedInScraper:
    """LinkedIn scraper with authentication"""
    
    def __init__(self, email: str, password: str, session_file: str = 'linkedin_session.json'):
        self.email = email
        self.password = password
        self.session_file = session_file
    
    def __enter__(self):
        self.playwright = sync_playwright().start()
        
        # Use persistent context to save session
        self.context = self.playwright.chromium.launch_persistent_context(
            user_data_dir='./linkedin_profile',
            headless=False,
            args=['--disable-blink-features=AutomationControlled']
        )
        
        self.page = self.context.pages[0] if self.context.pages else self.context.new_page()
        
        # Check if already logged in
        if not self._is_logged_in():
            self._login()
        
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.context:
            self.context.close()
        if self.playwright:
            self.playwright.stop()
    
    def _is_logged_in(self) -> bool:
        """Check if already logged in"""
        self.page.goto('https://www.linkedin.com/feed/', wait_until='networkidle')
        time.sleep(2)
        
        # Check for feed content
        return self.page.locator('.feed-identity-module').count() > 0
    
    def _login(self):
        """Login to LinkedIn"""
        print("Logging in...")
        
        self.page.goto('https://www.linkedin.com/login', wait_until='networkidle')
        time.sleep(random.uniform(2, 4))
        
        # Enter email
        email_input = self.page.locator('#username')
        for char in self.email:
            email_input.type(char, delay=random.randint(50, 150))
        
        time.sleep(random.uniform(0.5, 1))
        
        # Enter password
        password_input = self.page.locator('#password')
        for char in self.password:
            password_input.type(char, delay=random.randint(50, 150))
        
        time.sleep(random.uniform(0.5, 1))
        
        # Submit
        self.page.locator('button[type="submit"]').click()
        self.page.wait_for_load_state('networkidle')
        
        time.sleep(5)
        
        # Handle 2FA if needed (manual intervention)
        if 'checkpoint' in self.page.url:
            print("2FA required - please complete manually")
            input("Press Enter after completing 2FA...")
        
        print("Logged in successfully")
    
    def get_profile(self, profile_url: str) -> Optional[Dict]:
        """Scrape LinkedIn profile"""
        print(f"Scraping profile: {profile_url}")
        
        try:
            self.page.goto(profile_url, wait_until='networkidle')
            time.sleep(random.uniform(3, 5))
            
            # Scroll to load all sections
            self._scroll_to_bottom()
            
            # Extract profile data
            profile = self.page.evaluate("""
                () => {
                    const data = {};
                    
                    // Name
                    const nameEl = document.querySelector('h1');
                    data.name = nameEl ? nameEl.textContent.trim() : null;
                    
                    // Headline
                    const headlineEl = document.querySelector('.text-body-medium');
                    data.headline = headlineEl ? headlineEl.textContent.trim() : null;
                    
                    // Location
                    const locationEl = document.querySelector('.text-body-small.inline.t-black--light');
                    data.location = locationEl ? locationEl.textContent.trim() : null;
                    
                    // About
                    const aboutEl = document.querySelector('#about ~ * .inline-show-more-text');
                    data.about = aboutEl ? aboutEl.textContent.trim() : null;
                    
                    // Experience
                    const experience = [];
                    document.querySelectorAll('#experience ~ * .pvs-list__item--line-separated').forEach(item => {
                        const titleEl = item.querySelector('.mr1.t-bold span');
                        const companyEl = item.querySelector('.t-14.t-normal span');
                        const durationEl = item.querySelector('.t-14.t-normal.t-black--light span');
                        
                        experience.push({
                            title: titleEl ? titleEl.textContent.trim() : null,
                            company: companyEl ? companyEl.textContent.trim() : null,
                            duration: durationEl ? durationEl.textContent.trim() : null
                        });
                    });
                    data.experience = experience;
                    
                    // Education
                    const education = [];
                    document.querySelectorAll('#education ~ * .pvs-list__item--line-separated').forEach(item => {
                        const schoolEl = item.querySelector('.mr1.t-bold span');
                        const degreeEl = item.querySelector('.t-14.t-normal span');
                        
                        education.push({
                            school: schoolEl ? schoolEl.textContent.trim() : null,
                            degree: degreeEl ? degreeEl.textContent.trim() : null
                        });
                    });
                    data.education = education;
                    
                    // Skills
                    const skills = [];
                    document.querySelectorAll('#skills ~ * .mr1.t-bold span').forEach(el => {
                        skills.push(el.textContent.trim());
                    });
                    data.skills = skills;
                    
                    return data;
                }
            """)
            
            profile['url'] = profile_url
            
            # Rate limiting - wait between profiles
            time.sleep(random.uniform(10, 15))
            
            return profile
            
        except Exception as e:
            print(f"Error scraping profile: {e}")
            return None
    
    def _scroll_to_bottom(self):
        """Scroll to load all content"""
        previous_height = 0
        
        for _ in range(5):
            current_height = self.page.evaluate('document.body.scrollHeight')
            
            if current_height == previous_height:
                break
            
            self.page.evaluate('window.scrollTo(0, document.body.scrollHeight)')
            time.sleep(random.uniform(2, 3))
            
            previous_height = current_height

# Usage
with LinkedInScraper(email='your@email.com', password='yourpassword') as scraper:
    profile = scraper.get_profile('https://www.linkedin.com/in/username/')
    
    if profile:
        print(json.dumps(profile, indent=2))
```

## Twitter/X Data Collection

Twitter's API is the recommended approach, but scraping is still common.

### Challenges

1. **Login walls**: Many features require authentication
2. **Rate limits**: Strict limits on scrolling/loading
3. **Dynamic loading**: Infinite scroll for timelines
4. **API changes**: Frequent updates break scrapers

### Approach: API First, Scraper as Backup

```python
import tweepy
from typing import List, Dict
from datetime import datetime

class TwitterScraper:
    """Twitter scraper using official API"""
    
    def __init__(self, bearer_token: str):
        self.client = tweepy.Client(bearer_token=bearer_token)
    
    def search_tweets(self, query: str, max_results: int = 100) -> List[Dict]:
        """Search tweets using API v2"""
        tweets = []
        
        try:
            # Search recent tweets
            response = self.client.search_recent_tweets(
                query=query,
                max_results=min(max_results, 100),
                tweet_fields=['created_at', 'public_metrics', 'author_id'],
                expansions=['author_id'],
                user_fields=['username', 'name']
            )
            
            # Parse response
            if response.data:
                users = {user.id: user for user in response.includes['users']}
                
                for tweet in response.data:
                    author = users.get(tweet.author_id)
                    
                    tweets.append({
                        'id': tweet.id,
                        'text': tweet.text,
                        'created_at': tweet.created_at.isoformat(),
                        'author_id': tweet.author_id,
                        'author_username': author.username if author else None,
                        'author_name': author.name if author else None,
                        'likes': tweet.public_metrics['like_count'],
                        'retweets': tweet.public_metrics['retweet_count'],
                        'replies': tweet.public_metrics['reply_count']
                    })
            
            return tweets
            
        except Exception as e:
            print(f"Error searching tweets: {e}")
            return []
    
    def get_user_tweets(self, username: str, max_results: int = 100) -> List[Dict]:
        """Get tweets from specific user"""
        try:
            # Get user ID
            user = self.client.get_user(username=username)
            
            if not user.data:
                return []
            
            # Get user's tweets
            response = self.client.get_users_tweets(
                id=user.data.id,
                max_results=min(max_results, 100),
                tweet_fields=['created_at', 'public_metrics']
            )
            
            tweets = []
            if response.data:
                for tweet in response.data:
                    tweets.append({
                        'id': tweet.id,
                        'text': tweet.text,
                        'created_at': tweet.created_at.isoformat(),
                        'likes': tweet.public_metrics['like_count'],
                        'retweets': tweet.public_metrics['retweet_count'],
                        'replies': tweet.public_metrics['reply_count']
                    })
            
            return tweets
            
        except Exception as e:
            print(f"Error getting user tweets: {e}")
            return []

# Usage
scraper = TwitterScraper(bearer_token='your_bearer_token')

# Search tweets
tweets = scraper.search_tweets('python web scraping', max_results=50)
print(f"Found {len(tweets)} tweets")

# Get user's tweets
user_tweets = scraper.get_user_tweets('elonmusk', max_results=20)
```

## Instagram Scraping

Instagram is owned by Meta and has very strict anti-scraping measures.

### Challenges

1. **Login required**: Almost all content requires authentication
2. **Aggressive rate limiting**: Very strict
3. **Account bans**: Frequent for suspicious activity
4. **GraphQL API**: Complex API structure
5. **Legal issues**: Meta actively pursues scrapers

### Approach: Use Instaloader Library

```python
import instaloader
from typing import List, Dict
import time

class InstagramScraper:
    """Instagram scraper using Instaloader"""
    
    def __init__(self, username: str, password: str):
        self.L = instaloader.Instaloader()
        
        # Login
        try:
            self.L.login(username, password)
            print("Logged in successfully")
        except Exception as e:
            print(f"Login failed: {e}")
    
    def get_profile(self, username: str) -> Dict:
        """Get Instagram profile data"""
        try:
            profile = instaloader.Profile.from_username(self.L.context, username)
            
            return {
                'username': profile.username,
                'full_name': profile.full_name,
                'biography': profile.biography,
                'followers': profile.followers,
                'following': profile.followees,
                'posts': profile.mediacount,
                'is_verified': profile.is_verified,
                'is_private': profile.is_private,
                'profile_pic_url': profile.profile_pic_url
            }
        
        except Exception as e:
            print(f"Error getting profile: {e}")
            return {}
    
    def get_posts(self, username: str, max_posts: int = 12) -> List[Dict]:
        """Get posts from profile"""
        try:
            profile = instaloader.Profile.from_username(self.L.context, username)
            posts = []
            
            for post in profile.get_posts():
                if len(posts) >= max_posts:
                    break
                
                posts.append({
                    'shortcode': post.shortcode,
                    'url': f'https://www.instagram.com/p/{post.shortcode}/',
                    'caption': post.caption,
                    'likes': post.likes,
                    'comments': post.comments,
                    'date': post.date_utc.isoformat(),
                    'is_video': post.is_video,
                    'image_url': post.url
                })
                
                # Rate limiting
                time.sleep(2)
            
            return posts
            
        except Exception as e:
            print(f"Error getting posts: {e}")
            return []
    
    def get_hashtag_posts(self, hashtag: str, max_posts: int = 50) -> List[Dict]:
        """Get posts for hashtag"""
        try:
            hashtag_obj = instaloader.Hashtag.from_name(self.L.context, hashtag)
            posts = []
            
            for post in hashtag_obj.get_posts():
                if len(posts) >= max_posts:
                    break
                
                posts.append({
                    'shortcode': post.shortcode,
                    'owner': post.owner_username,
                    'caption': post.caption,
                    'likes': post.likes,
                    'comments': post.comments,
                    'date': post.date_utc.isoformat()
                })
                
                time.sleep(2)
            
            return posts
            
        except Exception as e:
            print(f"Error getting hashtag posts: {e}")
            return []

# Usage
scraper = InstagramScraper(username='your_username', password='your_password')

# Get profile
profile = scraper.get_profile('natgeo')
print(profile)

# Get posts
posts = scraper.get_posts('natgeo', max_posts=12)
```

## Reddit API + Scraping

Reddit has a good API but also scraping challenges.

### Approach: PRAW Library

```python
import praw
from typing import List, Dict
from datetime import datetime

class RedditScraper:
    """Reddit scraper using PRAW"""
    
    def __init__(self, client_id: str, client_secret: str, user_agent: str):
        self.reddit = praw.Reddit(
            client_id=client_id,
            client_secret=client_secret,
            user_agent=user_agent
        )
    
    def get_subreddit_posts(self, subreddit: str, sort: str = 'hot', 
                           limit: int = 100) -> List[Dict]:
        """Get posts from subreddit"""
        try:
            sub = self.reddit.subreddit(subreddit)
            
            # Choose sort method
            if sort == 'hot':
                posts = sub.hot(limit=limit)
            elif sort == 'new':
                posts = sub.new(limit=limit)
            elif sort == 'top':
                posts = sub.top(limit=limit, time_filter='week')
            else:
                posts = sub.hot(limit=limit)
            
            results = []
            for post in posts:
                results.append({
                    'id': post.id,
                    'title': post.title,
                    'author': post.author.name if post.author else '[deleted]',
                    'url': post.url,
                    'selftext': post.selftext,
                    'score': post.score,
                    'upvote_ratio': post.upvote_ratio,
                    'num_comments': post.num_comments,
                    'created_utc': datetime.fromtimestamp(post.created_utc).isoformat(),
                    'permalink': f'https://reddit.com{post.permalink}'
                })
            
            return results
            
        except Exception as e:
            print(f"Error getting posts: {e}")
            return []
    
    def get_post_comments(self, post_id: str, limit: int = 100) -> List[Dict]:
        """Get comments from post"""
        try:
            submission = self.reddit.submission(id=post_id)
            submission.comments.replace_more(limit=0)
            
            comments = []
            for comment in submission.comments.list()[:limit]:
                comments.append({
                    'id': comment.id,
                    'author': comment.author.name if comment.author else '[deleted]',
                    'body': comment.body,
                    'score': comment.score,
                    'created_utc': datetime.fromtimestamp(comment.created_utc).isoformat(),
                    'parent_id': comment.parent_id
                })
            
            return comments
            
        except Exception as e:
            print(f"Error getting comments: {e}")
            return []
    
    def search_posts(self, query: str, subreddit: str = 'all', 
                    limit: int = 100) -> List[Dict]:
        """Search Reddit posts"""
        try:
            sub = self.reddit.subreddit(subreddit)
            posts = sub.search(query, limit=limit, sort='relevance')
            
            results = []
            for post in posts:
                results.append({
                    'id': post.id,
                    'title': post.title,
                    'subreddit': post.subreddit.display_name,
                    'author': post.author.name if post.author else '[deleted]',
                    'url': post.url,
                    'score': post.score,
                    'num_comments': post.num_comments,
                    'created_utc': datetime.fromtimestamp(post.created_utc).isoformat()
                })
            
            return results
            
        except Exception as e:
            print(f"Error searching: {e}")
            return []

# Usage
scraper = RedditScraper(
    client_id='your_client_id',
    client_secret='your_client_secret',
    user_agent='scraper/1.0'
)

# Get hot posts
posts = scraper.get_subreddit_posts('python', sort='hot', limit=50)
print(f"Found {len(posts)} posts")

# Get comments
if posts:
    comments = scraper.get_post_comments(posts[0]['id'], limit=100)
    print(f"Found {len(comments)} comments")

# Search
search_results = scraper.search_posts('web scraping', subreddit='learnpython', limit=25)
```

## Real Estate Sites

Zillow, Realtor.com, and similar sites have specific challenges.

### Zillow Scraping

```python
from playwright.sync_api import sync_playwright
from typing import List, Dict
import time
import random

class ZillowScraper:
    """Zillow scraper with anti-detection"""
    
    def search_listings(self, location: str, max_pages: int = 3) -> List[Dict]:
        """Search Zillow listings"""
        with sync_playwright() as p:
            browser = p.chromium.launch(headless=True)
            context = browser.new_context(
                viewport={'width': 1920, 'height': 1080},
                user_agent='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
            )
            page = context.new_page()
            
            all_listings = []
            
            try:
                # Search
                search_url = f'https://www.zillow.com/homes/{location.replace(" ", "-")}_rb/'
                page.goto(search_url, wait_until='networkidle')
                
                time.sleep(random.uniform(3, 5))
                
                for page_num in range(max_pages):
                    # Extract listings
                    listings = page.evaluate("""
                        () => {
                            const results = [];
                            
                            document.querySelectorAll('article').forEach(listing => {
                                const priceEl = listing.querySelector('[data-test="property-card-price"]');
                                const addressEl = listing.querySelector('address');
                                const bedsEl = listing.querySelector('[data-test="property-card-beds"]');
                                const bathsEl = listing.querySelector('[data-test="property-card-baths"]');
                                const sqftEl = listing.querySelector('[data-test="property-card-sqft"]');
                                const linkEl = listing.querySelector('a');
                                
                                if (priceEl && addressEl) {
                                    results.push({
                                        price: priceEl.textContent,
                                        address: addressEl.textContent,
                                        beds: bedsEl ? bedsEl.textContent : null,
                                        baths: bathsEl ? bathsEl.textContent : null,
                                        sqft: sqftEl ? sqftEl.textContent : null,
                                        url: linkEl ? `https://www.zillow.com${linkEl.getAttribute('href')}` : null
                                    });
                                }
                            });
                            
                            return results;
                        }
                    """)
                    
                    all_listings.extend(listings)
                    print(f"Page {page_num + 1}: Found {len(listings)} listings")
                    
                    # Next page
                    if page_num < max_pages - 1:
                        try:
                            next_button = page.locator('[title="Next page"]')
                            if next_button.count() > 0:
                                next_button.click()
                                page.wait_for_load_state('networkidle')
                                time.sleep(random.uniform(3, 5))
                            else:
                                break
                        except:
                            break
                
                return all_listings
                
            finally:
                context.close()
                browser.close()

# Usage
scraper = ZillowScraper()
listings = scraper.search_listings('Seattle WA', max_pages=3)
print(f"Total listings: {len(listings)}")
```

## Job Boards

Indeed, LinkedIn Jobs, and other job boards.

### Indeed Scraper

```python
from playwright.sync_api import sync_playwright
import time
import random

class IndeedScraper:
    """Indeed job scraper"""
    
    def search_jobs(self, query: str, location: str, max_pages: int = 5) -> List[Dict]:
        """Search Indeed jobs"""
        with sync_playwright() as p:
            browser = p.chromium.launch(headless=True)
            page = browser.new_page()
            
            all_jobs = []
            
            try:
                # Search
                search_url = f'https://www.indeed.com/jobs?q={query}&l={location}'
                page.goto(search_url, wait_until='networkidle')
                
                time.sleep(random.uniform(2, 4))
                
                for page_num in range(max_pages):
                    # Extract jobs
                    jobs = page.evaluate("""
                        () => {
                            const results = [];
                            
                            document.querySelectorAll('.job_seen_beacon').forEach(job => {
                                const titleEl = job.querySelector('h2.jobTitle span');
                                const companyEl = job.querySelector('.companyName');
                                const locationEl = job.querySelector('.companyLocation');
                                const summaryEl = job.querySelector('.job-snippet');
                                const linkEl = job.querySelector('h2.jobTitle a');
                                
                                if (titleEl && companyEl) {
                                    results.push({
                                        title: titleEl.textContent,
                                        company: companyEl.textContent,
                                        location: locationEl ? locationEl.textContent : null,
                                        summary: summaryEl ? summaryEl.textContent : null,
                                        url: linkEl ? `https://www.indeed.com${linkEl.getAttribute('href')}` : null
                                    });
                                }
                            });
                            
                            return results;
                        }
                    """)
                    
                    all_jobs.extend(jobs)
                    print(f"Page {page_num + 1}: Found {len(jobs)} jobs")
                    
                    # Next page
                    if page_num < max_pages - 1:
                        try:
                            next_link = page.locator('[aria-label="Next Page"]')
                            if next_link.count() > 0:
                                next_link.click()
                                page.wait_for_load_state('networkidle')
                                time.sleep(random.uniform(2, 4))
                            else:
                                break
                        except:
                            break
                
                return all_jobs
                
            finally:
                browser.close()

# Usage
scraper = IndeedScraper()
jobs = scraper.search_jobs('python developer', 'New York', max_pages=5)
print(f"Total jobs: {len(jobs)}")
```

## Summary

Platform-specific scraping requires:

1. **Understanding anti-bot measures**: Each platform has unique detection methods
2. **Using official APIs when available**: Always prefer APIs over scraping
3. **Proper authentication**: Many platforms require login
4. **Rate limiting**: Respect limits to avoid bans
5. **Legal compliance**: Review ToS and legal restrictions
6. **Proxy rotation**: Essential for large-scale scraping
7. **Stealth techniques**: Browser fingerprinting, human-like behavior
8. **Data structures**: Platform-specific schemas for consistency

Always start with official APIs and use scraping only when necessary and legally permissible.