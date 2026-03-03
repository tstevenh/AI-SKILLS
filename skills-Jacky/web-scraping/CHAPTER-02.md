# Chapter 2: CAPTCHA Solving and Bot Detection Bypass

## Introduction

CAPTCHAs represent the last line of defense for websites against automated access. When fingerprinting and behavioral analysis aren't enough, sites present challenges that are (theoretically) easy for humans but hard for machines. This chapter covers every major CAPTCHA system, bot detection platform, and the techniques to bypass them programmatically.

We'll cover the technical internals of each system, integration with third-party solving services, and browser automation techniques that avoid triggering challenges in the first place.

---

## 2.1 Understanding CAPTCHA Systems

### The CAPTCHA Ecosystem

Modern CAPTCHAs fall into three categories:

1. **Interactive CAPTCHAs**: Require explicit user action (image selection, puzzle solving)
2. **Score-based CAPTCHAs**: Assign a bot probability score based on behavior (reCAPTCHA v3)
3. **Transparent challenges**: Run entirely in the background with no user interaction (Cloudflare Turnstile, managed challenges)

### How CAPTCHAs Actually Work (Internally)

Every CAPTCHA system collects telemetry before, during, and after the challenge:

- **Pre-challenge**: Mouse movements, scroll patterns, time on page, browser fingerprint, IP reputation
- **During challenge**: Solve time, mouse trajectory to answer, click precision, hesitation patterns
- **Post-challenge**: Token validation, subsequent request patterns

This telemetry is why simply "solving" the challenge isn't enough — you need to generate realistic telemetry around the solve.

---

## 2.2 Google reCAPTCHA v2 (Checkbox and Image)

### How reCAPTCHA v2 Works

reCAPTCHA v2 has two modes:
- **Checkbox ("I'm not a robot")**: May pass with just a click if Google's risk score is low
- **Image challenge**: Presented when the risk score is medium-high

The checkbox collects extensive behavioral data:
- Mouse movement trajectory to the checkbox
- Click timing and position
- Page interaction history (scrolls, clicks, keypresses)
- Browser fingerprint and cookies
- Google account status (if logged into Chrome)

### Solving reCAPTCHA v2 with Third-Party Services

```python
import asyncio
import aiohttp
import time
from typing import Optional

class CaptchaSolver:
    """Multi-provider CAPTCHA solving with failover."""
    
    def __init__(self, providers: dict):
        """
        providers = {
            '2captcha': {'api_key': 'xxx', 'priority': 1},
            'anticaptcha': {'api_key': 'yyy', 'priority': 2},
            'capsolver': {'api_key': 'zzz', 'priority': 3},
        }
        """
        self.providers = providers
        self.stats = {name: {'success': 0, 'fail': 0, 'avg_time': 0} for name in providers}
    
    async def solve_recaptcha_v2(self, site_url: str, site_key: str, 
                                  invisible: bool = False,
                                  timeout: int = 120) -> Optional[str]:
        """Solve reCAPTCHA v2 using the best available provider."""
        
        # Try providers in priority order
        sorted_providers = sorted(self.providers.items(), key=lambda x: x[1]['priority'])
        
        for name, config in sorted_providers:
            try:
                if name == '2captcha':
                    token = await self._solve_2captcha_recaptcha(
                        config['api_key'], site_url, site_key, invisible, timeout
                    )
                elif name == 'anticaptcha':
                    token = await self._solve_anticaptcha_recaptcha(
                        config['api_key'], site_url, site_key, invisible, timeout
                    )
                elif name == 'capsolver':
                    token = await self._solve_capsolver_recaptcha(
                        config['api_key'], site_url, site_key, invisible, timeout
                    )
                else:
                    continue
                
                if token:
                    self.stats[name]['success'] += 1
                    return token
                    
            except Exception as e:
                self.stats[name]['fail'] += 1
                print(f"Provider {name} failed: {e}")
                continue
        
        return None
    
    async def _solve_2captcha_recaptcha(self, api_key: str, site_url: str, 
                                         site_key: str, invisible: bool,
                                         timeout: int) -> Optional[str]:
        """Solve reCAPTCHA v2 using 2Captcha API."""
        async with aiohttp.ClientSession() as session:
            # Step 1: Submit task
            payload = {
                'key': api_key,
                'method': 'userrecaptcha',
                'googlekey': site_key,
                'pageurl': site_url,
                'json': 1,
            }
            if invisible:
                payload['invisible'] = 1
            
            async with session.post('http://2captcha.com/in.php', data=payload) as resp:
                result = await resp.json()
                if result.get('status') != 1:
                    raise Exception(f"2Captcha submit error: {result}")
                task_id = result['request']
            
            # Step 2: Poll for result
            start_time = time.time()
            while time.time() - start_time < timeout:
                await asyncio.sleep(5)
                
                params = {
                    'key': api_key,
                    'action': 'get',
                    'id': task_id,
                    'json': 1,
                }
                async with session.get('http://2captcha.com/res.php', params=params) as resp:
                    result = await resp.json()
                    if result.get('status') == 1:
                        return result['request']
                    elif result.get('request') == 'CAPCHA_NOT_READY':
                        continue
                    else:
                        raise Exception(f"2Captcha error: {result}")
            
            raise Exception("2Captcha timeout")
    
    async def _solve_anticaptcha_recaptcha(self, api_key: str, site_url: str,
                                            site_key: str, invisible: bool,
                                            timeout: int) -> Optional[str]:
        """Solve reCAPTCHA v2 using Anti-Captcha API."""
        async with aiohttp.ClientSession() as session:
            # Step 1: Create task
            task_payload = {
                'clientKey': api_key,
                'task': {
                    'type': 'RecaptchaV2TaskProxyless',
                    'websiteURL': site_url,
                    'websiteKey': site_key,
                    'isInvisible': invisible,
                },
            }
            
            async with session.post('https://api.anti-captcha.com/createTask', json=task_payload) as resp:
                result = await resp.json()
                if result.get('errorId') != 0:
                    raise Exception(f"Anti-Captcha error: {result}")
                task_id = result['taskId']
            
            # Step 2: Poll for result
            start_time = time.time()
            while time.time() - start_time < timeout:
                await asyncio.sleep(5)
                
                poll_payload = {
                    'clientKey': api_key,
                    'taskId': task_id,
                }
                async with session.post('https://api.anti-captcha.com/getTaskResult', json=poll_payload) as resp:
                    result = await resp.json()
                    if result.get('status') == 'ready':
                        return result['solution']['gRecaptchaResponse']
                    elif result.get('status') == 'processing':
                        continue
                    else:
                        raise Exception(f"Anti-Captcha error: {result}")
            
            raise Exception("Anti-Captcha timeout")
    
    async def _solve_capsolver_recaptcha(self, api_key: str, site_url: str,
                                          site_key: str, invisible: bool,
                                          timeout: int) -> Optional[str]:
        """Solve reCAPTCHA v2 using CapSolver API."""
        async with aiohttp.ClientSession() as session:
            task_payload = {
                'clientKey': api_key,
                'task': {
                    'type': 'ReCaptchaV2TaskProxyLess',
                    'websiteURL': site_url,
                    'websiteKey': site_key,
                    'isInvisible': invisible,
                },
            }
            
            async with session.post('https://api.capsolver.com/createTask', json=task_payload) as resp:
                result = await resp.json()
                if result.get('errorId') != 0:
                    raise Exception(f"CapSolver error: {result}")
                task_id = result['taskId']
            
            start_time = time.time()
            while time.time() - start_time < timeout:
                await asyncio.sleep(3)
                
                poll_payload = {
                    'clientKey': api_key,
                    'taskId': task_id,
                }
                async with session.post('https://api.capsolver.com/getTaskResult', json=poll_payload) as resp:
                    result = await resp.json()
                    if result.get('status') == 'ready':
                        return result['solution']['gRecaptchaResponse']
                    elif result.get('status') == 'processing':
                        continue
            
            raise Exception("CapSolver timeout")
```

### Injecting Solved reCAPTCHA Tokens

Once you have the token, inject it into the page:

```python
from playwright.async_api import Page

async def inject_recaptcha_token(page: Page, token: str):
    """Inject a solved reCAPTCHA v2 token into the page."""
    await page.evaluate(f"""
        // Set the response in the textarea
        document.getElementById('g-recaptcha-response').value = '{token}';
        
        // Make the textarea visible (some sites check this)
        const textarea = document.getElementById('g-recaptcha-response');
        if (textarea) {{
            textarea.style.display = 'block';
            textarea.style.visibility = 'visible';
            textarea.style.opacity = '1';
            textarea.style.height = '100px';
        }}
        
        // Trigger the callback function
        // The callback name is in the reCAPTCHA widget config
        if (typeof ___grecaptcha_cfg !== 'undefined') {{
            const clients = ___grecaptcha_cfg.clients;
            for (const key in clients) {{
                const client = clients[key];
                // Find the callback
                function findCallback(obj) {{
                    for (const k in obj) {{
                        if (typeof obj[k] === 'function') {{
                            try {{ obj[k]('{token}'); return true; }} catch(e) {{}}
                        }} else if (typeof obj[k] === 'object' && obj[k] !== null) {{
                            if (findCallback(obj[k])) return true;
                        }}
                    }}
                    return false;
                }}
                findCallback(client);
            }}
        }}
    """)
    
    # Alternative: if there's a known callback function
    await page.evaluate(f"""
        if (typeof onCaptchaSuccess === 'function') {{
            onCaptchaSuccess('{token}');
        }}
        if (typeof captchaCallback === 'function') {{
            captchaCallback('{token}');
        }}
    """)
```

---

## 2.3 Google reCAPTCHA v3 (Score-Based)

### How reCAPTCHA v3 Works

reCAPTCHA v3 never shows a visual challenge. Instead, it runs continuously in the background and assigns a score from 0.0 (bot) to 1.0 (human). The site owner decides the threshold.

Factors that influence the score:
- **Browser environment**: Fingerprint consistency, headless indicators
- **Behavioral signals**: Mouse movements, scroll patterns, keyboard usage
- **Google account status**: Logged-in users get higher scores
- **IP reputation**: Known VPN/proxy/datacenter IPs get lower scores
- **Historical behavior**: Previous interactions with reCAPTCHA across the web
- **Page interaction time**: How long before the token is requested

### Achieving High reCAPTCHA v3 Scores

```python
async def warm_recaptcha_v3(page: Page, site_key: str, action: str = 'submit'):
    """Warm up reCAPTCHA v3 by generating legitimate-looking behavior."""
    
    # Step 1: Load the page and let reCAPTCHA observe
    # The script starts monitoring immediately on load
    await asyncio.sleep(random.uniform(2, 5))
    
    # Step 2: Generate mouse movements (reCAPTCHA v3 watches these)
    for _ in range(random.randint(5, 15)):
        x = random.randint(100, 800)
        y = random.randint(100, 600)
        await page.mouse.move(x, y, steps=random.randint(5, 20))
        await asyncio.sleep(random.uniform(0.1, 0.5))
    
    # Step 3: Scroll (natural reading behavior)
    for _ in range(random.randint(2, 5)):
        await page.mouse.wheel(0, random.randint(100, 400))
        await asyncio.sleep(random.uniform(1, 3))
    
    # Step 4: Some random clicks on safe areas
    for _ in range(random.randint(1, 3)):
        await page.mouse.click(
            random.randint(200, 700),
            random.randint(200, 500)
        )
        await asyncio.sleep(random.uniform(0.5, 2))
    
    # Step 5: Wait total at least 10 seconds (v3 penalizes quick submissions)
    await asyncio.sleep(random.uniform(3, 8))
    
    # Step 6: Execute the reCAPTCHA v3 challenge
    token = await page.evaluate(f"""
        new Promise((resolve, reject) => {{
            grecaptcha.ready(function() {{
                grecaptcha.execute('{site_key}', {{action: '{action}'}})
                    .then(function(token) {{
                        resolve(token);
                    }})
                    .catch(function(error) {{
                        reject(error);
                    }});
            }});
        }})
    """)
    
    return token


async def solve_recaptcha_v3_via_service(solver: CaptchaSolver, site_url: str,
                                          site_key: str, action: str = 'submit',
                                          min_score: float = 0.7) -> Optional[str]:
    """Solve reCAPTCHA v3 using a solving service.
    
    Note: v3 tokens from services often have lower scores (0.3-0.7).
    For high-score requirements, browser-based warming is better.
    """
    async with aiohttp.ClientSession() as session:
        # Using 2Captcha's v3 endpoint
        payload = {
            'key': solver.providers['2captcha']['api_key'],
            'method': 'userrecaptcha',
            'version': 'v3',
            'googlekey': site_key,
            'pageurl': site_url,
            'action': action,
            'min_score': min_score,
            'json': 1,
        }
        
        async with session.post('http://2captcha.com/in.php', data=payload) as resp:
            result = await resp.json()
            if result.get('status') != 1:
                raise Exception(f"Submit error: {result}")
            task_id = result['request']
        
        for _ in range(24):  # 2 minutes max
            await asyncio.sleep(5)
            params = {
                'key': solver.providers['2captcha']['api_key'],
                'action': 'get',
                'id': task_id,
                'json': 1,
            }
            async with session.get('http://2captcha.com/res.php', params=params) as resp:
                result = await resp.json()
                if result.get('status') == 1:
                    return result['request']
                elif result.get('request') != 'CAPCHA_NOT_READY':
                    raise Exception(f"Error: {result}")
    
    return None
```

### reCAPTCHA v3 Token Lifecycle

reCAPTCHA v3 tokens expire after 2 minutes. Plan your scraping flow accordingly:

```python
class RecaptchaV3Manager:
    """Manage reCAPTCHA v3 token generation and lifecycle."""
    
    def __init__(self, site_key: str, site_url: str, solver: CaptchaSolver):
        self.site_key = site_key
        self.site_url = site_url
        self.solver = solver
        self.token_cache = []
        self.token_ttl = 110  # Use within 110 seconds (tokens expire at 120)
    
    async def get_fresh_token(self, action: str = 'submit') -> str:
        """Get a fresh, valid token."""
        # Check cache for valid tokens
        now = time.time()
        self.token_cache = [(t, ts) for t, ts in self.token_cache if now - ts < self.token_ttl]
        
        if self.token_cache:
            return self.token_cache.pop(0)[0]
        
        # Generate new token
        token = await solve_recaptcha_v3_via_service(
            self.solver, self.site_url, self.site_key, action
        )
        return token
    
    async def prefetch_tokens(self, count: int = 3, action: str = 'submit'):
        """Pre-fetch tokens for upcoming requests."""
        tasks = [
            solve_recaptcha_v3_via_service(
                self.solver, self.site_url, self.site_key, action
            )
            for _ in range(count)
        ]
        tokens = await asyncio.gather(*tasks, return_exceptions=True)
        
        now = time.time()
        for token in tokens:
            if isinstance(token, str):
                self.token_cache.append((token, now))
```

---

## 2.4 hCaptcha

### How hCaptcha Differs from reCAPTCHA

hCaptcha is the primary alternative to reCAPTCHA, used by Cloudflare and many other sites. Key differences:
- Privacy-focused (doesn't track across sites like Google)
- Image labeling challenges contribute to ML training datasets
- Generally considered harder to solve programmatically
- Uses its own behavioral analysis separate from Google's

### Solving hCaptcha

```python
async def solve_hcaptcha(solver: CaptchaSolver, site_url: str, 
                          site_key: str, timeout: int = 180) -> Optional[str]:
    """Solve hCaptcha using solving service."""
    async with aiohttp.ClientSession() as session:
        # 2Captcha supports hCaptcha
        payload = {
            'key': solver.providers['2captcha']['api_key'],
            'method': 'hcaptcha',
            'sitekey': site_key,
            'pageurl': site_url,
            'json': 1,
        }
        
        async with session.post('http://2captcha.com/in.php', data=payload) as resp:
            result = await resp.json()
            if result.get('status') != 1:
                raise Exception(f"hCaptcha submit error: {result}")
            task_id = result['request']
        
        start = time.time()
        while time.time() - start < timeout:
            await asyncio.sleep(5)
            params = {
                'key': solver.providers['2captcha']['api_key'],
                'action': 'get',
                'id': task_id,
                'json': 1,
            }
            async with session.get('http://2captcha.com/res.php', params=params) as resp:
                result = await resp.json()
                if result.get('status') == 1:
                    return result['request']
                elif result.get('request') != 'CAPCHA_NOT_READY':
                    raise Exception(f"hCaptcha error: {result}")
        
        return None


async def inject_hcaptcha_token(page: Page, token: str):
    """Inject solved hCaptcha token into page."""
    await page.evaluate(f"""
        // Set the response
        const responseInputs = document.querySelectorAll('[name="h-captcha-response"], [name="g-recaptcha-response"]');
        responseInputs.forEach(input => {{
            input.value = '{token}';
        }});
        
        // Find and trigger the hCaptcha callback
        const iframes = document.querySelectorAll('iframe[src*="hcaptcha"]');
        if (iframes.length > 0) {{
            // hCaptcha stores callbacks on the hcaptcha object
            if (typeof hcaptcha !== 'undefined') {{
                // Try to find the widget ID and trigger callback
                const widgetIds = Object.keys(hcaptcha._widgetMap || {{}});
                widgetIds.forEach(id => {{
                    const widget = hcaptcha._widgetMap[id];
                    if (widget && widget.callback) {{
                        widget.callback('{token}');
                    }}
                }});
            }}
        }}
    """)
```

### hCaptcha Enterprise Challenges

hCaptcha Enterprise includes additional challenges like:
- **Proof of Work**: Browser must compute a hash challenge
- **Accessibility challenges**: Audio-based alternatives
- **Risk scoring**: Similar to reCAPTCHA v3

```python
async def handle_hcaptcha_enterprise(page: Page, solver: CaptchaSolver):
    """Handle hCaptcha Enterprise with proof-of-work."""
    # Wait for hCaptcha to load
    await page.wait_for_selector('iframe[src*="hcaptcha"]', timeout=10000)
    
    # Extract sitekey from the page
    site_key = await page.evaluate("""
        (() => {
            // Try data attribute
            const div = document.querySelector('[data-sitekey]');
            if (div) return div.getAttribute('data-sitekey');
            
            // Try iframe URL
            const iframe = document.querySelector('iframe[src*="hcaptcha"]');
            if (iframe) {
                const url = new URL(iframe.src);
                return url.searchParams.get('sitekey');
            }
            
            // Try hcaptcha config
            if (typeof hcaptcha !== 'undefined') {
                const widgets = Object.values(hcaptcha._widgetMap || {});
                if (widgets.length > 0) return widgets[0].sitekey;
            }
            
            return null;
        })()
    """)
    
    if not site_key:
        raise Exception("Could not find hCaptcha sitekey")
    
    site_url = page.url
    token = await solve_hcaptcha(solver, site_url, site_key)
    
    if token:
        await inject_hcaptcha_token(page, token)
        return True
    
    return False
```

---

## 2.5 Cloudflare Bot Protection

### Cloudflare's Multi-Layer Defense

Cloudflare offers several levels of bot protection:

1. **Browser Integrity Check**: Checks HTTP headers for known bot patterns
2. **JS Challenge (5-second page)**: Forces browser to execute JavaScript
3. **Managed Challenge (Turnstile)**: Invisible or interactive challenge
4. **Under Attack Mode**: All visitors get a challenge page
5. **Bot Fight Mode**: ML-based bot detection with automatic blocking

### Bypassing Cloudflare JS Challenge

The classic "Checking your browser" page runs JavaScript that:
1. Computes a proof-of-work (hash computation)
2. Collects browser fingerprint data
3. Sets the `cf_clearance` cookie on success
4. Redirects to the original page

```python
from curl_cffi import requests as curl_requests
import re
import time

class CloudflareBypasser:
    """Bypass Cloudflare protection using browser automation."""
    
    def __init__(self, proxy_pool):
        self.proxy_pool = proxy_pool
    
    async def bypass_with_browser(self, url: str, page: Page, max_wait: int = 30) -> bool:
        """Wait for Cloudflare challenge to resolve in browser."""
        await page.goto(url, wait_until='domcontentloaded')
        
        start = time.time()
        while time.time() - start < max_wait:
            # Check if we're past the challenge
            content = await page.content()
            title = await page.title()
            
            # Cloudflare challenge page indicators
            cf_indicators = [
                'Just a moment',
                'Checking your browser',
                'cf-browser-verification',
                'challenge-platform',
                'ray ID',
            ]
            
            is_challenge = any(ind.lower() in content.lower() or ind.lower() in title.lower() 
                             for ind in cf_indicators)
            
            if not is_challenge:
                # Challenge passed! Extract cookies
                cookies = await page.context.cookies()
                cf_clearance = next((c for c in cookies if c['name'] == 'cf_clearance'), None)
                
                if cf_clearance:
                    return True
            
            # Wait and check Turnstile iframe
            turnstile = await page.query_selector('iframe[src*="challenges.cloudflare.com"]')
            if turnstile:
                # Turnstile might need a click
                box = await turnstile.bounding_box()
                if box:
                    # Click in the center of the Turnstile checkbox
                    await page.mouse.click(
                        box['x'] + box['width'] / 2,
                        box['y'] + box['height'] / 2
                    )
            
            await asyncio.sleep(2)
        
        return False
    
    async def get_cf_cookies(self, url: str, browser) -> dict:
        """Get cf_clearance cookies by solving Cloudflare challenge."""
        from urllib.parse import urlparse
        domain = urlparse(url).netloc
        
        proxy = await self.proxy_pool.get_proxy(domain)
        
        context = await browser.new_context(
            user_agent='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
            viewport={'width': 1920, 'height': 1080},
        )
        
        # Add stealth scripts
        await context.add_init_script("""
            Object.defineProperty(navigator, 'webdriver', { get: () => undefined });
            // ... (other evasion scripts from Chapter 1)
        """)
        
        page = await context.new_page()
        
        success = await self.bypass_with_browser(url, page)
        
        if success:
            cookies = await context.cookies()
            cookie_dict = {c['name']: c['value'] for c in cookies}
            await context.close()
            return cookie_dict
        
        await context.close()
        raise Exception("Failed to bypass Cloudflare")
    
    async def scrape_with_cf_cookies(self, url: str, cookies: dict) -> str:
        """Use obtained CF cookies with curl_cffi for subsequent requests."""
        response = curl_requests.get(
            url,
            impersonate='chrome120',
            cookies=cookies,
            headers={
                'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
                'Accept-Language': 'en-US,en;q=0.9',
            },
        )
        return response.text
```

### Cloudflare Turnstile

Turnstile is Cloudflare's CAPTCHA alternative. It's designed to be invisible most of the time:

```python
async def solve_cloudflare_turnstile(page: Page, solver: CaptchaSolver) -> Optional[str]:
    """Solve Cloudflare Turnstile challenge."""
    
    # Find the Turnstile sitekey
    site_key = await page.evaluate("""
        (() => {
            // Method 1: From data attribute
            const div = document.querySelector('[data-sitekey]');
            if (div) return div.getAttribute('data-sitekey');
            
            // Method 2: From Turnstile render call
            const scripts = document.querySelectorAll('script');
            for (const script of scripts) {
                const match = script.textContent.match(/sitekey['"\\s:]+['"]([0-9a-zA-Z_-]+)['"]/);
                if (match) return match[1];
            }
            
            // Method 3: From iframe
            const iframe = document.querySelector('iframe[src*="challenges.cloudflare.com"]');
            if (iframe) {
                const url = new URL(iframe.src);
                return url.searchParams.get('sitekey') || url.searchParams.get('k');
            }
            
            return null;
        })()
    """)
    
    if not site_key:
        raise Exception("Could not find Turnstile sitekey")
    
    # Solve via service
    async with aiohttp.ClientSession() as session:
        payload = {
            'key': solver.providers['2captcha']['api_key'],
            'method': 'turnstile',
            'sitekey': site_key,
            'pageurl': page.url,
            'json': 1,
        }
        
        async with session.post('http://2captcha.com/in.php', data=payload) as resp:
            result = await resp.json()
            task_id = result['request']
        
        for _ in range(60):
            await asyncio.sleep(3)
            params = {
                'key': solver.providers['2captcha']['api_key'],
                'action': 'get',
                'id': task_id,
                'json': 1,
            }
            async with session.get('http://2captcha.com/res.php', params=params) as resp:
                result = await resp.json()
                if result.get('status') == 1:
                    return result['request']
                elif result.get('request') != 'CAPCHA_NOT_READY':
                    break
    
    return None


async def inject_turnstile_token(page: Page, token: str):
    """Inject Turnstile token into the page."""
    await page.evaluate(f"""
        // Find the response input
        const inputs = document.querySelectorAll(
            'input[name="cf-turnstile-response"], ' +
            'input[name="cf_turnstile_response"], ' +
            '[name="turnstile-response"]'
        );
        inputs.forEach(input => {{ input.value = '{token}'; }});
        
        // Trigger Turnstile callback
        if (typeof turnstile !== 'undefined') {{
            const widgets = document.querySelectorAll('.cf-turnstile');
            widgets.forEach(widget => {{
                const widgetId = widget.getAttribute('data-widget-id');
                if (widgetId && turnstile._widgets && turnstile._widgets[widgetId]) {{
                    const callback = turnstile._widgets[widgetId].callback;
                    if (typeof callback === 'function') {{
                        callback('{token}');
                    }}
                }}
            }});
        }}
    """)
```

---

## 2.6 DataDome Bot Protection

### How DataDome Works

DataDome is a sophisticated bot detection system used by many e-commerce sites. It works by:

1. **JavaScript SDK**: Injects a script that collects 200+ browser signals
2. **Cookie validation**: Sets and validates `datadome` cookie
3. **API endpoint**: Sends telemetry to `api-js.datadome.co`
4. **Challenge pages**: Serves CAPTCHAs when suspicious activity is detected
5. **Real-time ML**: Uses machine learning to detect bots in real-time

### DataDome Detection Vectors

DataDome checks:
- Navigator properties (webdriver, plugins, languages)
- Canvas and WebGL fingerprints
- Mouse movements and click patterns
- Keyboard event timing
- Touch events on mobile
- Screen orientation and device motion
- WebRTC local IP
- Battery API
- CSS computed styles
- Performance timing APIs
- Error handling behavior

### Bypassing DataDome

```python
class DataDomeBypasser:
    """Techniques for bypassing DataDome bot protection."""
    
    DATADOME_JS_ENDPOINT = 'https://api-js.datadome.co/js/'
    
    async def handle_datadome(self, page: Page, max_retries: int = 3) -> bool:
        """Handle DataDome protection on a page."""
        
        for attempt in range(max_retries):
            # Check if DataDome is blocking
            content = await page.content()
            
            # DataDome CAPTCHA page indicators
            if 'datadome' in content.lower() and ('captcha' in content.lower() or 'geo.captcha' in content.lower()):
                # DataDome is showing a CAPTCHA
                return await self._solve_datadome_captcha(page)
            
            # Check for DataDome cookie
            cookies = await page.context.cookies()
            dd_cookie = next((c for c in cookies if c['name'] == 'datadome'), None)
            
            if dd_cookie:
                # Cookie exists, check if it's valid
                response = await page.reload(wait_until='networkidle')
                if response and response.status == 200:
                    return True
            
            # Wait for DataDome JS to execute and set cookie
            await asyncio.sleep(3)
            
            # Generate behavioral signals
            await self._generate_human_signals(page)
            
            await asyncio.sleep(2)
        
        return False
    
    async def _generate_human_signals(self, page: Page):
        """Generate mouse/keyboard signals that DataDome expects."""
        # DataDome specifically tracks these events
        
        # Mouse movements
        for _ in range(random.randint(10, 25)):
            x = random.randint(50, 1200)
            y = random.randint(50, 700)
            await page.mouse.move(x, y, steps=random.randint(3, 10))
            await asyncio.sleep(random.uniform(0.05, 0.2))
        
        # Mouse clicks
        for _ in range(random.randint(1, 3)):
            await page.mouse.click(
                random.randint(100, 800),
                random.randint(100, 600)
            )
            await asyncio.sleep(random.uniform(0.3, 1.0))
        
        # Scroll
        for _ in range(random.randint(2, 5)):
            await page.mouse.wheel(0, random.randint(50, 300))
            await asyncio.sleep(random.uniform(0.5, 2.0))
        
        # Keyboard events (not typing into any field, just generating events)
        await page.evaluate("""
            document.dispatchEvent(new KeyboardEvent('keydown', {key: 'ArrowDown', bubbles: true}));
            document.dispatchEvent(new KeyboardEvent('keyup', {key: 'ArrowDown', bubbles: true}));
        """)
    
    async def _solve_datadome_captcha(self, page: Page) -> bool:
        """Solve DataDome's CAPTCHA challenge."""
        # DataDome uses either GeeTest or its own CAPTCHA
        
        # Check for GeeTest (sliding puzzle)
        geetest = await page.query_selector('.geetest_holder')
        if geetest:
            return await self._solve_geetest(page)
        
        # Check for DataDome's own CAPTCHA (usually audio/image)
        dd_captcha = await page.query_selector('#captcha-container, .dd-captcha')
        if dd_captcha:
            # Use solving service
            # DataDome CAPTCHAs often have a specific URL format
            captcha_url = page.url
            
            # Extract the captcha parameters
            captcha_params = await page.evaluate("""
                (() => {
                    const urlParams = new URLSearchParams(window.location.search);
                    return {
                        initialCid: urlParams.get('initialCid'),
                        cid: urlParams.get('cid'),
                        t: urlParams.get('t'),
                        referer: urlParams.get('referer'),
                    };
                })()
            """)
            
            return False  # DataDome CAPTCHAs require specialized handling
        
        return False
    
    async def _solve_geetest(self, page: Page) -> bool:
        """Solve GeeTest sliding CAPTCHA used by DataDome."""
        # GeeTest requires sliding a puzzle piece to the correct position
        
        # Wait for GeeTest to fully load
        await page.wait_for_selector('.geetest_canvas_img', timeout=10000)
        await asyncio.sleep(1)
        
        # Get the slider button
        slider = await page.query_selector('.geetest_slider_button')
        if not slider:
            return False
        
        slider_box = await slider.bounding_box()
        
        # Determine slide distance (this requires image analysis)
        # For now, use a solving service for GeeTest
        # GeeTest parameters can be sent to 2Captcha/CapSolver
        
        gt = await page.evaluate("typeof geetest_params !== 'undefined' ? geetest_params.gt : null")
        challenge = await page.evaluate("typeof geetest_params !== 'undefined' ? geetest_params.challenge : null")
        
        if gt and challenge:
            # Send to solving service
            pass
        
        return False
    
    async def extract_datadome_cookie_via_browser(self, url: str, browser) -> dict:
        """Get a valid DataDome cookie by browsing naturally."""
        context = await browser.new_context(
            user_agent='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
            viewport={'width': 1920, 'height': 1080},
        )
        
        page = await context.new_page()
        
        # Navigate to a low-protection page first (homepage, about page)
        from urllib.parse import urlparse
        domain = urlparse(url).netloc
        
        await page.goto(f'https://{domain}/', wait_until='networkidle')
        await asyncio.sleep(3)
        
        # Generate signals
        await self._generate_human_signals(page)
        
        # Check if cookie was set
        cookies = await context.cookies()
        dd_cookie = next((c for c in cookies if c['name'] == 'datadome'), None)
        
        if dd_cookie:
            cookie_dict = {c['name']: c['value'] for c in cookies}
            await context.close()
            return cookie_dict
        
        await context.close()
        raise Exception("Failed to obtain DataDome cookie")
```

---

## 2.7 PerimeterX (HUMAN Security)

### How PerimeterX Works

PerimeterX (now HUMAN Security) is another major bot detection platform. Key features:

1. **Sensor script**: Collects browser environment, behavioral, and network signals
2. **Cookie-based**: Sets `_px`, `_pxvid`, `_pxhd` cookies
3. **Challenge types**: CAPTCHA, block page, or transparent pass
4. **Device fingerprinting**: Creates a persistent device ID across sessions
5. **Behavioral analysis**: ML model trained on human interaction patterns

### PerimeterX Cookie Flow

```
1. First visit → PX sensor script loads
2. Sensor collects data → Sends to PX cloud
3. PX evaluates risk → Returns cookie
4. Cookie validated on each subsequent request
5. If suspicious → CAPTCHA or block
```

### Bypassing PerimeterX

```python
class PerimeterXBypasser:
    """Bypass PerimeterX bot detection."""
    
    async def get_px_cookies(self, url: str, browser) -> dict:
        """Obtain valid PerimeterX cookies through browser automation."""
        context = await browser.new_context(
            user_agent='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
            viewport={'width': 1920, 'height': 1080},
        )
        
        # Inject stealth scripts
        await context.add_init_script("""
            Object.defineProperty(navigator, 'webdriver', { get: () => undefined });
            // ... comprehensive stealth from Chapter 1
        """)
        
        page = await context.new_page()
        
        # Monitor PX requests
        px_requests = []
        page.on('request', lambda req: px_requests.append(req.url) if '/api/v2/collector' in req.url or 'captcha' in req.url else None)
        
        # Navigate
        await page.goto(url, wait_until='networkidle')
        
        # Generate behavioral signals (PX is very sensitive to these)
        await self._px_behavioral_signals(page)
        
        # Wait for PX to process
        await asyncio.sleep(5)
        
        # Extract cookies
        cookies = await context.cookies()
        px_cookies = {c['name']: c['value'] for c in cookies 
                     if c['name'].startswith('_px') or c['name'] in ['datadome', 'cf_clearance']}
        
        await context.close()
        return px_cookies
    
    async def _px_behavioral_signals(self, page: Page):
        """Generate signals that PerimeterX expects from human users."""
        
        # PerimeterX tracks:
        # 1. Mouse movement entropy
        # 2. Click patterns
        # 3. Scroll behavior
        # 4. Focus/blur events
        # 5. Touch events (mobile)
        # 6. Keyboard timing
        
        # Mouse movements with realistic entropy
        prev_x, prev_y = 500, 400
        for _ in range(random.randint(15, 30)):
            # Don't move in straight lines
            angle = random.uniform(0, 2 * 3.14159)
            distance = random.uniform(30, 200)
            new_x = max(0, min(1920, prev_x + int(distance * __import__('math').cos(angle))))
            new_y = max(0, min(1080, prev_y + int(distance * __import__('math').sin(angle))))
            
            await page.mouse.move(new_x, new_y, steps=random.randint(5, 15))
            prev_x, prev_y = new_x, new_y
            await asyncio.sleep(random.uniform(0.05, 0.3))
        
        # Scroll with variable speed
        for _ in range(random.randint(3, 7)):
            scroll_amount = random.choice([100, 150, 200, 250, 300, 350])
            await page.mouse.wheel(0, scroll_amount)
            await asyncio.sleep(random.uniform(0.5, 3.0))
        
        # Focus/blur simulation
        await page.evaluate("""
            window.dispatchEvent(new Event('blur'));
            setTimeout(() => window.dispatchEvent(new Event('focus')), 1000 + Math.random() * 3000);
        """)
        
        await asyncio.sleep(random.uniform(2, 5))
    
    async def handle_px_captcha(self, page: Page, solver: CaptchaSolver) -> bool:
        """Handle PerimeterX CAPTCHA challenge."""
        # PX often uses its own press-and-hold CAPTCHA
        
        # Check for PX block page
        px_block = await page.query_selector('#px-captcha, .px-captcha-container')
        if not px_block:
            return False
        
        # PX "press and hold" CAPTCHA
        press_hold = await page.query_selector('#px-captcha[data-cmd="hold"]')
        if press_hold:
            return await self._solve_press_hold(page, press_hold)
        
        # PX with reCAPTCHA fallback
        recaptcha = await page.query_selector('.g-recaptcha, [data-sitekey]')
        if recaptcha:
            site_key = await recaptcha.get_attribute('data-sitekey')
            token = await solver.solve_recaptcha_v2(page.url, site_key)
            if token:
                await inject_recaptcha_token(page, token)
                return True
        
        return False
    
    async def _solve_press_hold(self, page: Page, element) -> bool:
        """Solve PerimeterX press-and-hold CAPTCHA."""
        box = await element.bounding_box()
        if not box:
            return False
        
        center_x = box['x'] + box['width'] / 2
        center_y = box['y'] + box['height'] / 2
        
        # Move to element naturally
        await page.mouse.move(center_x - 100, center_y - 50, steps=10)
        await asyncio.sleep(random.uniform(0.2, 0.5))
        await page.mouse.move(center_x, center_y, steps=15)
        await asyncio.sleep(random.uniform(0.1, 0.3))
        
        # Press and hold (typically needs 5-10 seconds)
        await page.mouse.down()
        hold_time = random.uniform(6, 10)
        await asyncio.sleep(hold_time)
        await page.mouse.up()
        
        # Wait for verification
        await asyncio.sleep(3)
        
        # Check if we passed
        content = await page.content()
        return 'px-captcha' not in content.lower()
```

---

## 2.8 Browser Automation Detection Evasion

### undetected-chromedriver

`undetected-chromedriver` patches Selenium's ChromeDriver to avoid detection:

```python
import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def create_undetected_browser(proxy: str = None, headless: bool = False):
    """Create an undetected Chrome browser instance."""
    options = uc.ChromeOptions()
    
    if headless:
        options.add_argument('--headless=new')  # New headless mode (Chrome 109+)
    
    if proxy:
        options.add_argument(f'--proxy-server={proxy}')
    
    # Additional stealth options
    options.add_argument('--disable-blink-features=AutomationControlled')
    options.add_argument('--no-first-run')
    options.add_argument('--no-service-autorun')
    options.add_argument('--password-store=basic')
    options.add_argument('--disable-infobars')
    options.add_argument('--lang=en-US')
    
    # Set window size (not viewport — this affects outer dimensions too)
    options.add_argument('--window-size=1920,1080')
    
    # Create driver
    driver = uc.Chrome(
        options=options,
        version_main=120,  # Match your Chrome version
        use_subprocess=True,
    )
    
    return driver


def scrape_with_undetected(url: str, proxy: str = None):
    """Scrape a page using undetected-chromedriver."""
    driver = create_undetected_browser(proxy)
    
    try:
        driver.get(url)
        
        # Wait for page to load
        WebDriverWait(driver, 30).until(
            EC.presence_of_element_located((By.TAG_NAME, 'body'))
        )
        
        # Optional: wait for specific content
        # WebDriverWait(driver, 10).until(
        #     EC.presence_of_element_located((By.CSS_SELECTOR, '.content'))
        # )
        
        html = driver.page_source
        cookies = {c['name']: c['value'] for c in driver.get_cookies()}
        
        return {
            'html': html,
            'cookies': cookies,
            'url': driver.current_url,
        }
        
    finally:
        driver.quit()
```

### Playwright Stealth

`playwright-stealth` is a port of `puppeteer-extra-plugin-stealth`:

```python
from playwright.async_api import async_playwright
from playwright_stealth import stealth_async

async def create_stealth_playwright(proxy: str = None, headless: bool = True):
    """Create a stealth Playwright browser."""
    playwright = await async_playwright().start()
    
    launch_args = [
        '--disable-blink-features=AutomationControlled',
        '--disable-features=IsolateOrigins,site-per-process',
        '--disable-infobars',
    ]
    
    browser = await playwright.chromium.launch(
        headless=headless,
        args=launch_args,
    )
    
    context_options = {
        'viewport': {'width': 1920, 'height': 1080},
        'user_agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
        'locale': 'en-US',
        'timezone_id': 'America/New_York',
    }
    
    if proxy:
        context_options['proxy'] = {'server': proxy}
    
    context = await browser.new_context(**context_options)
    page = await context.new_page()
    
    # Apply stealth
    await stealth_async(page)
    
    return playwright, browser, context, page


async def advanced_stealth_playwright():
    """Create Playwright with maximum stealth (manual patches)."""
    playwright = await async_playwright().start()
    
    browser = await playwright.chromium.launch(
        headless=True,
        args=[
            '--disable-blink-features=AutomationControlled',
            '--disable-features=IsolateOrigins,site-per-process',
            '--disable-dev-shm-usage',
            '--disable-accelerated-2d-canvas',
            '--no-first-run',
            '--no-zygote',
            '--disable-gpu',
            '--hide-scrollbars',
            '--mute-audio',
        ],
    )
    
    context = await browser.new_context(
        viewport={'width': 1920, 'height': 1080},
        user_agent='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
        locale='en-US',
        timezone_id='America/New_York',
        device_scale_factor=1,
        color_scheme='light',
        extra_http_headers={
            'Accept-Language': 'en-US,en;q=0.9',
        },
    )
    
    # Comprehensive stealth script
    await context.add_init_script("""
        // === Navigator Patches ===
        Object.defineProperty(navigator, 'webdriver', { get: () => undefined });
        Object.defineProperty(navigator, 'plugins', {
            get: () => [
                { name: 'Chrome PDF Plugin', filename: 'internal-pdf-viewer' },
                { name: 'Chrome PDF Viewer', filename: 'mhjfbmdgcfjbbpaeojofohoefgiehjai' },
                { name: 'Native Client', filename: 'internal-nacl-plugin' },
            ]
        });
        Object.defineProperty(navigator, 'languages', { get: () => ['en-US', 'en'] });
        Object.defineProperty(navigator, 'hardwareConcurrency', { get: () => 8 });
        Object.defineProperty(navigator, 'deviceMemory', { get: () => 8 });
        Object.defineProperty(navigator, 'maxTouchPoints', { get: () => 0 });
        
        // === Chrome Object ===
        window.chrome = {
            runtime: { onMessage: { addListener: () => {} }, sendMessage: () => {} },
            loadTimes: () => ({ requestTime: Date.now()/1000 - 1, startLoadTime: Date.now()/1000 - 0.5 }),
            csi: () => ({ pageT: Date.now() }),
            app: { isInstalled: false, getDetails: () => null, getIsInstalled: () => false,
                   InstallState: { DISABLED: 'disabled', INSTALLED: 'installed', NOT_INSTALLED: 'not_installed' },
                   RunningState: { CANNOT_RUN: 'cannot_run', READY_TO_RUN: 'ready_to_run', RUNNING: 'running' } },
        };
        
        // === Permissions ===
        const origQuery = Permissions.prototype.query;
        Permissions.prototype.query = (params) => {
            if (params.name === 'notifications') return Promise.resolve({ state: 'default' });
            return origQuery(params);
        };
        
        // === Window Dimensions ===
        Object.defineProperty(window, 'outerWidth', { get: () => 1920 });
        Object.defineProperty(window, 'outerHeight', { get: () => 1080 });
        
        // === Connection ===
        Object.defineProperty(navigator, 'connection', {
            get: () => ({ effectiveType: '4g', rtt: 50, downlink: 10, saveData: false })
        });
        
        // === Iframe protection ===
        const origContentWindow = Object.getOwnPropertyDescriptor(HTMLIFrameElement.prototype, 'contentWindow');
        Object.defineProperty(HTMLIFrameElement.prototype, 'contentWindow', {
            get: function() {
                const w = origContentWindow.get.call(this);
                try { Object.defineProperty(w.navigator, 'webdriver', { get: () => undefined }); } catch(e) {}
                return w;
            }
        });
        
        // === toString protection ===
        const nativeToString = Function.prototype.toString;
        const overrides = new WeakMap();
        Function.prototype.toString = function() {
            return overrides.get(this) || nativeToString.call(this);
        };
        overrides.set(Function.prototype.toString, 'function toString() { [native code] }');
    """)
    
    page = await context.new_page()
    return playwright, browser, context, page
```

---

## 2.9 Camoufox: Firefox-Based Stealth Browser

Camoufox is a modified Firefox build designed specifically for web scraping with anti-detection:

```python
# Installation: pip install camoufox && python -m camoufox fetch
from camoufox.async_api import AsyncCamoufox

async def scrape_with_camoufox(url: str, proxy: str = None):
    """Use Camoufox for maximum stealth."""
    config = {}
    
    if proxy:
        config['proxy'] = {'server': proxy}
    
    async with AsyncCamoufox(
        headless=True,
        humanize=True,  # Adds realistic mouse/keyboard behavior
        geoip=True,  # Auto-match locale to IP location
        **config
    ) as browser:
        page = await browser.new_page()
        await page.goto(url, wait_until='networkidle')
        
        content = await page.content()
        return content
```

### Why Firefox-Based Solutions Can Be Better

Chrome-based automation (Playwright Chromium, undetected-chromedriver) shares common detection vectors because they all use the same browser engine. Firefox-based solutions like Camoufox have:

1. Different TLS fingerprint (Firefox, not Chrome)
2. Different JavaScript engine (SpiderMonkey, not V8)
3. Different rendering engine (Gecko, not Blink)
4. Less common in bot detection training data
5. Native canvas randomization (Firefox has built-in fingerprint resistance)

---

## 2.10 CAPTCHA Solving Cost Optimization

### Provider Pricing Comparison (as of 2024)

| Provider | reCAPTCHA v2 | reCAPTCHA v3 | hCaptcha | Turnstile | Speed |
|----------|-------------|-------------|----------|-----------|-------|
| 2Captcha | $2.99/1K | $2.99/1K | $2.99/1K | $2.99/1K | 15-45s |
| Anti-Captcha | $2.00/1K | $2.00/1K | $2.00/1K | $2.00/1K | 10-30s |
| CapSolver | $1.50/1K | $2.00/1K | $0.80/1K | $1.50/1K | 5-20s |
| Capsolver | $1.50/1K | N/A | $0.80/1K | $1.00/1K | 5-15s |
| NopeCHA | Free tier | Free tier | Free tier | - | 10-30s |

### Cost Optimization Strategies

```python
class CaptchaCostOptimizer:
    """Minimize CAPTCHA solving costs."""
    
    def __init__(self, solver: CaptchaSolver):
        self.solver = solver
        self.domain_stats = {}  # Track CAPTCHA rates per domain
    
    def should_solve_or_rotate(self, domain: str) -> str:
        """Decide whether to solve CAPTCHA or rotate proxy.
        
        If solving costs more than proxy rotation, rotate instead.
        """
        stats = self.domain_stats.get(domain, {})
        captcha_rate = stats.get('captcha_rate', 0)
        
        # If >50% of requests hit CAPTCHAs, proxy quality is the issue
        if captcha_rate > 0.5:
            return 'rotate_proxy'
        
        # If solving costs < $0.005/request average, solve
        avg_cost_per_request = captcha_rate * 0.003  # $3/1K CAPTCHAs
        if avg_cost_per_request < 0.005:
            return 'solve'
        
        return 'rotate_proxy'
    
    async def solve_or_bypass(self, page: Page, domain: str) -> bool:
        """Intelligently handle CAPTCHA encounters."""
        action = self.should_solve_or_rotate(domain)
        
        if action == 'rotate_proxy':
            # Don't waste money solving — get a better proxy
            return False  # Caller should rotate proxy and retry
        
        # Try to bypass without solving first
        bypassed = await self._try_cookie_bypass(page, domain)
        if bypassed:
            return True
        
        # Solve as last resort
        return await self._solve_captcha(page, domain)
    
    async def _try_cookie_bypass(self, page: Page, domain: str) -> bool:
        """Try to bypass using cached cookies from a previous solve."""
        # Check if we have valid cookies from a recent solve
        cached = self._get_cached_cookies(domain)
        if cached:
            await page.context.add_cookies(cached)
            await page.reload(wait_until='networkidle')
            
            # Check if bypass worked
            content = await page.content()
            if 'captcha' not in content.lower():
                return True
        
        return False
    
    def _get_cached_cookies(self, domain: str) -> list:
        """Get cached authentication cookies for a domain."""
        # Implementation depends on your cookie storage
        return []
    
    async def _solve_captcha(self, page: Page, domain: str) -> bool:
        """Solve whatever CAPTCHA is on the page."""
        content = await page.content()
        
        # Detect CAPTCHA type
        if 'recaptcha' in content.lower() or 'g-recaptcha' in content.lower():
            site_key = await page.evaluate("""
                document.querySelector('[data-sitekey]')?.getAttribute('data-sitekey') ||
                document.querySelector('.g-recaptcha')?.getAttribute('data-sitekey')
            """)
            if site_key:
                token = await self.solver.solve_recaptcha_v2(page.url, site_key)
                if token:
                    await inject_recaptcha_token(page, token)
                    return True
        
        elif 'hcaptcha' in content.lower() or 'h-captcha' in content.lower():
            site_key = await page.evaluate("""
                document.querySelector('[data-sitekey]')?.getAttribute('data-sitekey') ||
                document.querySelector('.h-captcha')?.getAttribute('data-sitekey')
            """)
            if site_key:
                token = await solve_hcaptcha(self.solver, page.url, site_key)
                if token:
                    await inject_hcaptcha_token(page, token)
                    return True
        
        elif 'turnstile' in content.lower() or 'challenges.cloudflare.com' in content.lower():
            token = await solve_cloudflare_turnstile(page, self.solver)
            if token:
                await inject_turnstile_token(page, token)
                return True
        
        return False
```

---

## 2.11 Token Harvesting Architecture

For high-volume scraping, pre-solve CAPTCHAs and maintain a token pool:

```python
import asyncio
from collections import deque

class TokenHarvester:
    """Pre-solve CAPTCHAs and maintain a ready-to-use token pool."""
    
    def __init__(self, solver: CaptchaSolver, site_url: str, site_key: str,
                 captcha_type: str = 'recaptcha_v2', pool_size: int = 5,
                 token_ttl: int = 110):
        self.solver = solver
        self.site_url = site_url
        self.site_key = site_key
        self.captcha_type = captcha_type
        self.pool_size = pool_size
        self.token_ttl = token_ttl
        self.tokens = deque()  # (token, timestamp) pairs
        self._running = False
        self._lock = asyncio.Lock()
    
    async def start(self):
        """Start the token harvesting loop."""
        self._running = True
        asyncio.create_task(self._harvest_loop())
    
    async def stop(self):
        """Stop harvesting."""
        self._running = False
    
    async def _harvest_loop(self):
        """Continuously harvest tokens to maintain pool size."""
        while self._running:
            # Clean expired tokens
            now = time.time()
            async with self._lock:
                while self.tokens and now - self.tokens[0][1] > self.token_ttl:
                    self.tokens.popleft()
            
            # Refill pool
            current_size = len(self.tokens)
            if current_size < self.pool_size:
                tasks = []
                for _ in range(self.pool_size - current_size):
                    tasks.append(self._solve_one())
                
                results = await asyncio.gather(*tasks, return_exceptions=True)
                
                async with self._lock:
                    now = time.time()
                    for result in results:
                        if isinstance(result, str):
                            self.tokens.append((result, now))
            
            await asyncio.sleep(5)
    
    async def _solve_one(self) -> str:
        """Solve a single CAPTCHA."""
        if self.captcha_type == 'recaptcha_v2':
            return await self.solver.solve_recaptcha_v2(self.site_url, self.site_key)
        elif self.captcha_type == 'hcaptcha':
            return await solve_hcaptcha(self.solver, self.site_url, self.site_key)
        raise ValueError(f"Unknown CAPTCHA type: {self.captcha_type}")
    
    async def get_token(self, timeout: int = 60) -> str:
        """Get a fresh token from the pool."""
        start = time.time()
        while time.time() - start < timeout:
            async with self._lock:
                now = time.time()
                # Find a valid token
                while self.tokens:
                    token, ts = self.tokens.popleft()
                    if now - ts < self.token_ttl:
                        return token
            
            await asyncio.sleep(1)
        
        raise Exception("Token harvest timeout")
    
    @property
    def available(self) -> int:
        """Number of valid tokens in pool."""
        now = time.time()
        return sum(1 for _, ts in self.tokens if now - ts < self.token_ttl)


# Usage
async def main():
    solver = CaptchaSolver({
        '2captcha': {'api_key': 'YOUR_KEY', 'priority': 1},
    })
    
    harvester = TokenHarvester(
        solver=solver,
        site_url='https://example.com',
        site_key='6Lc...',
        captcha_type='recaptcha_v2',
        pool_size=5,
    )
    
    await harvester.start()
    
    # Now tokens are always ready
    for url in urls_to_scrape:
        token = await harvester.get_token()
        # Use token in request...
    
    await harvester.stop()
```

---

## 2.12 Integrated CAPTCHA Handling Pipeline

Here's a complete pipeline that detects, classifies, and solves CAPTCHAs automatically:

```python
class CaptchaPipeline:
    """Automatic CAPTCHA detection and solving pipeline."""
    
    def __init__(self, solver: CaptchaSolver, proxy_pool=None):
        self.solver = solver
        self.proxy_pool = proxy_pool
        self.cost_optimizer = CaptchaCostOptimizer(solver)
        self.harvesters = {}  # domain -> TokenHarvester
    
    async def handle_page(self, page: Page, expected_content_selector: str = None) -> bool:
        """Check if page has CAPTCHA and handle it.
        
        Returns True if page is now accessible, False if handling failed.
        """
        # Step 1: Detect CAPTCHA type
        captcha_info = await self._detect_captcha(page)
        
        if not captcha_info:
            return True  # No CAPTCHA
        
        captcha_type = captcha_info['type']
        print(f"Detected CAPTCHA: {captcha_type}")
        
        # Step 2: Check if we have a pre-harvested token
        domain = page.url.split('/')[2]
        if domain in self.harvesters:
            try:
                token = await self.harvesters[domain].get_token(timeout=5)
                await self._inject_token(page, captcha_info, token)
                await asyncio.sleep(2)
                
                # Verify
                if await self._verify_solved(page, expected_content_selector):
                    return True
            except Exception:
                pass
        
        # Step 3: Solve fresh
        token = await self._solve(page, captcha_info)
        if not token:
            return False
        
        await self._inject_token(page, captcha_info, token)
        await asyncio.sleep(2)
        
        return await self._verify_solved(page, expected_content_selector)
    
    async def _detect_captcha(self, page: Page) -> Optional[dict]:
        """Detect what type of CAPTCHA is on the page."""
        return await page.evaluate("""
            (() => {
                // reCAPTCHA v2
                const recaptchaV2 = document.querySelector('.g-recaptcha, [data-sitekey][data-callback]');
                if (recaptchaV2) {
                    return {
                        type: 'recaptcha_v2',
                        sitekey: recaptchaV2.getAttribute('data-sitekey'),
                        invisible: recaptchaV2.getAttribute('data-size') === 'invisible',
                    };
                }
                
                // reCAPTCHA v3 (detected via script src)
                const v3Script = document.querySelector('script[src*="recaptcha/api.js?render="]');
                if (v3Script) {
                    const src = v3Script.src;
                    const key = src.match(/render=([^&]+)/)?.[1];
                    if (key && key !== 'explicit') {
                        return { type: 'recaptcha_v3', sitekey: key };
                    }
                }
                
                // hCaptcha
                const hcaptcha = document.querySelector('.h-captcha, [data-sitekey][class*="hcaptcha"]');
                if (hcaptcha) {
                    return {
                        type: 'hcaptcha',
                        sitekey: hcaptcha.getAttribute('data-sitekey'),
                    };
                }
                
                // Cloudflare Turnstile
                const turnstile = document.querySelector('.cf-turnstile, [data-sitekey]');
                const turnstileIframe = document.querySelector('iframe[src*="challenges.cloudflare.com"]');
                if (turnstile || turnstileIframe) {
                    return {
                        type: 'turnstile',
                        sitekey: turnstile?.getAttribute('data-sitekey') || null,
                    };
                }
                
                // Cloudflare challenge page
                if (document.title.includes('Just a moment') || 
                    document.querySelector('#challenge-form, .challenge-running')) {
                    return { type: 'cloudflare_challenge' };
                }
                
                // DataDome
                if (document.querySelector('[class*="datadome"], #datadome-captcha') ||
                    document.cookie.includes('datadome')) {
                    return { type: 'datadome' };
                }
                
                // PerimeterX
                if (document.querySelector('#px-captcha, .px-captcha-container')) {
                    return { type: 'perimeterx' };
                }
                
                // GeeTest
                if (document.querySelector('.geetest_holder, .geetest_panel')) {
                    return { type: 'geetest' };
                }
                
                return null;
            })()
        """)
    
    async def _solve(self, page: Page, captcha_info: dict) -> Optional[str]:
        """Route to appropriate solver."""
        ct = captcha_info['type']
        
        if ct == 'recaptcha_v2':
            return await self.solver.solve_recaptcha_v2(
                page.url, captcha_info['sitekey'],
                invisible=captcha_info.get('invisible', False)
            )
        
        elif ct == 'recaptcha_v3':
            return await solve_recaptcha_v3_via_service(
                self.solver, page.url, captcha_info['sitekey']
            )
        
        elif ct == 'hcaptcha':
            return await solve_hcaptcha(
                self.solver, page.url, captcha_info['sitekey']
            )
        
        elif ct == 'turnstile':
            return await solve_cloudflare_turnstile(page, self.solver)
        
        elif ct == 'cloudflare_challenge':
            # Wait for auto-solve
            cf = CloudflareBypasser(self.proxy_pool)
            success = await cf.bypass_with_browser(page.url, page)
            return 'cloudflare_passed' if success else None
        
        return None
    
    async def _inject_token(self, page: Page, captcha_info: dict, token: str):
        """Inject token based on CAPTCHA type."""
        ct = captcha_info['type']
        
        if ct in ('recaptcha_v2', 'recaptcha_v3'):
            await inject_recaptcha_token(page, token)
        elif ct == 'hcaptcha':
            await inject_hcaptcha_token(page, token)
        elif ct == 'turnstile':
            await inject_turnstile_token(page, token)
    
    async def _verify_solved(self, page: Page, 
                              expected_selector: Optional[str]) -> bool:
        """Verify CAPTCHA was solved successfully."""
        await asyncio.sleep(2)
        
        # Check if CAPTCHA is still present
        captcha = await self._detect_captcha(page)
        if captcha:
            return False
        
        # Check for expected content
        if expected_selector:
            try:
                await page.wait_for_selector(expected_selector, timeout=5000)
                return True
            except Exception:
                return False
        
        return True
```

---

## 2.13 Advanced Techniques for Specific Platforms

### Amazon Bot Detection

Amazon uses a combination of custom detection plus CAPTCHA:

```python
async def handle_amazon_captcha(page: Page, solver: CaptchaSolver) -> bool:
    """Handle Amazon's image CAPTCHA."""
    # Amazon shows a text CAPTCHA with an image
    captcha_img = await page.query_selector('#captchacharacters ~ img, img[src*="captcha"]')
    
    if not captcha_img:
        return False
    
    # Get the image URL
    img_src = await captcha_img.get_attribute('src')
    
    # Download the image
    import base64
    img_element = await page.evaluate(f"""
        fetch('{img_src}')
            .then(r => r.blob())
            .then(blob => new Promise((resolve) => {{
                const reader = new FileReader();
                reader.onloadend = () => resolve(reader.result);
                reader.readAsDataURL(blob);
            }}))
    """)
    
    # Send to solver
    img_base64 = img_element.split(',')[1]
    
    async with aiohttp.ClientSession() as session:
        payload = {
            'key': solver.providers['2captcha']['api_key'],
            'method': 'base64',
            'body': img_base64,
            'json': 1,
        }
        
        async with session.post('http://2captcha.com/in.php', data=payload) as resp:
            result = await resp.json()
            task_id = result['request']
        
        for _ in range(30):
            await asyncio.sleep(3)
            params = {
                'key': solver.providers['2captcha']['api_key'],
                'action': 'get',
                'id': task_id,
                'json': 1,
            }
            async with session.get('http://2captcha.com/res.php', params=params) as resp:
                result = await resp.json()
                if result.get('status') == 1:
                    solution = result['request']
                    
                    # Type the solution
                    captcha_input = await page.query_selector('#captchacharacters')
                    if captcha_input:
                        await captcha_input.fill(solution)
                        submit = await page.query_selector('button[type="submit"]')
                        if submit:
                            await submit.click()
                        return True
                elif result.get('request') != 'CAPCHA_NOT_READY':
                    break
    
    return False
```

### LinkedIn Challenge Handling

```python
async def handle_linkedin_challenge(page: Page):
    """Handle LinkedIn's security verification."""
    # LinkedIn uses a multi-step verification:
    # 1. Email/phone verification
    # 2. CAPTCHA (reCAPTCHA or Arkose Labs)
    # 3. Identity verification
    
    # Check for Arkose Labs (FunCaptcha)
    arkose = await page.query_selector('#FunCaptcha, iframe[src*="arkoselabs"]')
    if arkose:
        # Arkose Labs requires specialized solving
        # Services like CapSolver support FunCaptcha
        pass
    
    # Check for reCAPTCHA
    recaptcha = await page.query_selector('.g-recaptcha')
    if recaptcha:
        # Standard reCAPTCHA solve
        pass
```

---

## 2.14 Monitoring and Alerting

```python
import json
from datetime import datetime

class CaptchaMonitor:
    """Monitor CAPTCHA encounter rates and solving performance."""
    
    def __init__(self):
        self.events = []
    
    def record_encounter(self, domain: str, captcha_type: str, solved: bool, 
                         solve_time: float, cost: float = 0):
        """Record a CAPTCHA encounter."""
        self.events.append({
            'timestamp': datetime.utcnow().isoformat(),
            'domain': domain,
            'captcha_type': captcha_type,
            'solved': solved,
            'solve_time': solve_time,
            'cost': cost,
        })
    
    def get_stats(self, domain: str = None, hours: int = 24) -> dict:
        """Get CAPTCHA statistics."""
        cutoff = datetime.utcnow().timestamp() - hours * 3600
        
        filtered = [e for e in self.events 
                    if datetime.fromisoformat(e['timestamp']).timestamp() > cutoff]
        if domain:
            filtered = [e for e in filtered if e['domain'] == domain]
        
        if not filtered:
            return {'total': 0}
        
        total = len(filtered)
        solved = sum(1 for e in filtered if e['solved'])
        total_cost = sum(e['cost'] for e in filtered)
        avg_time = sum(e['solve_time'] for e in filtered) / total
        
        by_type = {}
        for e in filtered:
            ct = e['captcha_type']
            if ct not in by_type:
                by_type[ct] = {'total': 0, 'solved': 0}
            by_type[ct]['total'] += 1
            if e['solved']:
                by_type[ct]['solved'] += 1
        
        return {
            'total': total,
            'solved': solved,
            'solve_rate': solved / total if total else 0,
            'total_cost': total_cost,
            'avg_solve_time': avg_time,
            'by_type': by_type,
        }
    
    def should_alert(self, domain: str) -> Optional[str]:
        """Check if CAPTCHA rate is abnormally high."""
        stats = self.get_stats(domain, hours=1)
        
        if stats['total'] > 10 and stats['solve_rate'] < 0.5:
            return f"High CAPTCHA failure rate for {domain}: {stats['solve_rate']:.1%} ({stats['solved']}/{stats['total']})"
        
        if stats['total'] > 50:
            return f"Excessive CAPTCHAs for {domain}: {stats['total']} in last hour. Consider proxy rotation."
        
        return None
```

---

## Summary

CAPTCHA solving and bot detection bypass requires a layered approach:

1. **Prevention first**: Use stealth techniques from Chapter 1 to avoid triggering CAPTCHAs
2. **Detection**: Automatically identify CAPTCHA type on any page
3. **Solving**: Route to the most cost-effective solving method
4. **Token management**: Pre-harvest tokens for high-volume operations
5. **Optimization**: Track costs and adjust strategy based on encounter rates
6. **Monitoring**: Alert on abnormal CAPTCHA rates that indicate detection

Key principles:
- **Browser-first**: Many challenges can be solved by simply having a well-configured browser wait
- **Cost awareness**: At $3/1K solves, CAPTCHAs add up fast. Prevent them when possible.
- **Provider diversity**: Don't rely on a single solving service
- **Token freshness**: reCAPTCHA tokens expire in 2 minutes. Plan accordingly.
- **Behavioral realism**: The challenge itself is often less important than the behavior around it

The next chapter covers scaling these techniques across distributed infrastructure for enterprise-level scraping operations.
