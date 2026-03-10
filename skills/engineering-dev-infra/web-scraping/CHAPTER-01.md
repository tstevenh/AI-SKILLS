# Chapter 1: Anti-Detection and Stealth Scraping

## Introduction

Web scraping in the modern era is an arms race. Every major website deploys sophisticated bot detection systems that analyze dozens of browser signals, network characteristics, and behavioral patterns to distinguish human visitors from automated scrapers. This chapter provides a comprehensive technical deep-dive into anti-detection techniques that allow scrapers to operate undetected at scale.

The stakes are high: getting detected means IP bans, CAPTCHAs, fake data injection, or legal action. Understanding detection mechanisms is the first step toward building scrapers that blend seamlessly with legitimate traffic.

---

## 1.1 Browser Fingerprinting: The Detection Landscape

### What Is Browser Fingerprinting?

Browser fingerprinting is the process of collecting attributes from a user's browser to create a unique identifier. Unlike cookies, fingerprints don't require storage on the client side — they're computed server-side from observable characteristics. Detection systems like FingerprintJS, CreepJS, and proprietary solutions from Akamai, Cloudflare, and DataDome use fingerprinting extensively.

### Key Fingerprint Vectors

A modern fingerprint encompasses dozens of signals:

1. **Navigator properties**: `userAgent`, `platform`, `language`, `languages`, `hardwareConcurrency`, `deviceMemory`, `maxTouchPoints`
2. **Screen properties**: `screen.width`, `screen.height`, `screen.colorDepth`, `screen.pixelDepth`, `window.devicePixelRatio`
3. **Canvas fingerprint**: Rendered pixel data from HTML5 Canvas operations
4. **WebGL fingerprint**: GPU renderer string, supported extensions, shader precision
5. **Audio fingerprint**: AudioContext oscillator output variations
6. **Font enumeration**: Installed system fonts detected via rendering
7. **WebRTC**: Local IP address leakage
8. **Plugin/MIME type enumeration**: Browser plugins and supported MIME types
9. **CSS feature detection**: Supported CSS properties and values
10. **JavaScript engine quirks**: Error message formats, function serialization

### The Consistency Problem

The most common mistake in anti-detection is **inconsistency**. If your User-Agent says "Windows 10 Chrome 120" but your navigator.platform returns "Linux x86_64", detection is trivial. Every spoofed value must be internally consistent.

```python
# Example: Consistent browser profile generation
import random

class BrowserProfile:
    """Generate internally consistent browser fingerprint profiles."""
    
    PROFILES = {
        'windows_chrome': {
            'platform': 'Win32',
            'oscpu': None,  # Chrome doesn't expose this
            'app_version': '5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{version} Safari/537.36',
            'vendor': 'Google Inc.',
            'renderer_base': 'ANGLE (NVIDIA GeForce',
            'screen_resolutions': [(1920, 1080), (2560, 1440), (1366, 768), (1536, 864), (1440, 900)],
            'color_depth': 24,
            'pixel_ratio': [1, 1.25, 1.5, 2],
            'hardware_concurrency': [4, 8, 12, 16],
            'device_memory': [4, 8, 16, 32],
            'languages': [['en-US', 'en'], ['en-US']],
            'timezone': 'America/New_York',
            'max_touch_points': 0,
        },
        'mac_chrome': {
            'platform': 'MacIntel',
            'oscpu': None,
            'app_version': '5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{version} Safari/537.36',
            'vendor': 'Google Inc.',
            'renderer_base': 'ANGLE (Apple, ANGLE Metal Renderer: Apple M',
            'screen_resolutions': [(1440, 900), (1680, 1050), (2560, 1600), (1920, 1080)],
            'color_depth': 30,
            'pixel_ratio': [1, 2],
            'hardware_concurrency': [8, 10, 12],
            'device_memory': [8, 16, 32],
            'languages': [['en-US', 'en'], ['en-US']],
            'timezone': 'America/Los_Angeles',
            'max_touch_points': 0,
        },
        'mac_safari': {
            'platform': 'MacIntel',
            'oscpu': None,
            'app_version': '5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.2 Safari/605.1.15',
            'vendor': 'Apple Computer, Inc.',
            'renderer_base': 'Apple GPU',
            'screen_resolutions': [(1440, 900), (1680, 1050), (2560, 1600)],
            'color_depth': 30,
            'pixel_ratio': [2],
            'hardware_concurrency': [8, 10, 12],
            'device_memory': None,  # Safari doesn't expose this
            'languages': [['en-US', 'en'], ['en-US']],
            'timezone': 'America/Los_Angeles',
            'max_touch_points': 0,
        },
    }
    
    def __init__(self, profile_type='windows_chrome', chrome_version='120.0.0.0'):
        self.profile_type = profile_type
        self.config = self.PROFILES[profile_type]
        self.chrome_version = chrome_version
        self._generate()
    
    def _generate(self):
        """Generate a complete, consistent profile."""
        cfg = self.config
        res = random.choice(cfg['screen_resolutions'])
        
        self.screen_width = res[0]
        self.screen_height = res[1]
        self.avail_width = res[0]
        self.avail_height = res[1] - random.choice([0, 40, 48])  # taskbar
        self.color_depth = cfg['color_depth']
        self.pixel_depth = cfg['color_depth']
        self.pixel_ratio = random.choice(cfg['pixel_ratio'])
        self.hardware_concurrency = random.choice(cfg['hardware_concurrency'])
        self.device_memory = random.choice(cfg['device_memory']) if cfg['device_memory'] else None
        self.max_touch_points = cfg['max_touch_points']
        self.platform = cfg['platform']
        self.vendor = cfg['vendor']
        self.languages = random.choice(cfg['languages'])
        self.language = self.languages[0]
        self.timezone = cfg['timezone']
        self.user_agent = cfg['app_version'].format(version=self.chrome_version)
        
        # Inner/outer window dimensions should be plausible
        self.outer_width = self.screen_width
        self.outer_height = self.screen_height
        self.inner_width = self.screen_width - random.choice([0, 15])  # scrollbar
        self.inner_height = self.screen_height - random.randint(70, 140)  # chrome UI
    
    def to_playwright_args(self):
        """Convert profile to Playwright launch arguments."""
        return {
            'user_agent': self.user_agent,
            'viewport': {
                'width': self.inner_width,
                'height': self.inner_height,
            },
            'screen': {
                'width': self.screen_width,
                'height': self.screen_height,
            },
            'locale': self.language,
            'timezone_id': self.timezone,
            'device_scale_factor': self.pixel_ratio,
            'color_scheme': 'light',
        }
    
    def get_injection_script(self):
        """Generate JavaScript to inject consistent fingerprint values."""
        return f"""
        // Override navigator properties
        Object.defineProperty(navigator, 'hardwareConcurrency', {{
            get: () => {self.hardware_concurrency}
        }});
        {'Object.defineProperty(navigator, "deviceMemory", { get: () => ' + str(self.device_memory) + ' });' if self.device_memory else ''}
        Object.defineProperty(navigator, 'maxTouchPoints', {{
            get: () => {self.max_touch_points}
        }});
        Object.defineProperty(navigator, 'platform', {{
            get: () => '{self.platform}'
        }});
        Object.defineProperty(navigator, 'vendor', {{
            get: () => '{self.vendor}'
        }});
        Object.defineProperty(navigator, 'languages', {{
            get: () => {self.languages}
        }});
        Object.defineProperty(screen, 'width', {{ get: () => {self.screen_width} }});
        Object.defineProperty(screen, 'height', {{ get: () => {self.screen_height} }});
        Object.defineProperty(screen, 'availWidth', {{ get: () => {self.avail_width} }});
        Object.defineProperty(screen, 'availHeight', {{ get: () => {self.avail_height} }});
        Object.defineProperty(screen, 'colorDepth', {{ get: () => {self.color_depth} }});
        Object.defineProperty(screen, 'pixelDepth', {{ get: () => {self.pixel_depth} }});
        """


# Usage
profile = BrowserProfile('windows_chrome', '120.0.0.0')
playwright_opts = profile.to_playwright_args()
injection_js = profile.get_injection_script()
```

---

## 1.2 TLS Fingerprinting: JA3 and JA4 Signatures

### How TLS Fingerprinting Works

TLS fingerprinting is one of the most effective bot detection techniques because it operates at the network level — below the application layer where most spoofing occurs. When a client initiates a TLS handshake, the Client Hello message contains a specific set of:

- **TLS version**: The supported TLS versions
- **Cipher suites**: The list and order of cipher suites offered
- **Extensions**: TLS extensions and their order
- **Elliptic curves**: Supported curves and point formats
- **Signature algorithms**: Supported signature algorithms

These values create a fingerprint that's unique to each TLS implementation (browser, library, or tool).

### JA3 Fingerprinting

JA3 was created by John Althouse, Jeff Atkinson, and Josh Atkins at Salesforce. It creates an MD5 hash from five fields in the Client Hello:

```
JA3 = MD5(TLSVersion,Ciphers,Extensions,EllipticCurves,EllipticCurvePointFormats)
```

For example, a typical Chrome 120 JA3 hash looks like:
```
cd08e31494f9531f560d64c695473da9
```

While Python's `requests` library (using urllib3/OpenSSL) produces:
```
b32309a26951912be7dba376398abc3b
```

Detection systems maintain databases of known JA3 hashes. If your hash matches Python/curl/Go instead of Chrome/Firefox, you're flagged immediately.

### JA4 Fingerprinting

JA4 is the successor to JA3, created by John Althouse at FoxIO. It's more granular and readable:

```
JA4 = Protocol_Version + SNI + Cipher_Count + Extension_Count + ALPN_First_Last + Cipher_Hash + Extension_Hash
```

Example JA4 for Chrome: `t13d1516h2_8daaf6152771_b0da82dd1658`

JA4 is harder to spoof because it includes ALPN negotiation and separates cipher/extension ordering.

### Spoofing TLS Fingerprints in Python

The key library for TLS fingerprint spoofing is `curl_cffi`, which uses curl's SSL implementation and allows specifying a browser impersonation target:

```python
from curl_cffi import requests as curl_requests

# Impersonate Chrome 120 — matches its exact TLS fingerprint
response = curl_requests.get(
    'https://example.com',
    impersonate='chrome120',
    headers={
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8',
        'Accept-Language': 'en-US,en;q=0.9',
        'Accept-Encoding': 'gzip, deflate, br',
        'Cache-Control': 'max-age=0',
        'Sec-Ch-Ua': '"Not_A Brand";v="8", "Chromium";v="120", "Google Chrome";v="120"',
        'Sec-Ch-Ua-Mobile': '?0',
        'Sec-Ch-Ua-Platform': '"Windows"',
        'Sec-Fetch-Dest': 'document',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-Site': 'none',
        'Sec-Fetch-User': '?1',
        'Upgrade-Insecure-Requests': '1',
    },
    proxies={'https': 'http://user:pass@proxy:port'},
)

print(response.status_code)
print(response.text[:500])
```

### Advanced TLS Spoofing with tls-client

For more granular control, the `tls-client` library (Go-based with Python bindings) allows specifying exact cipher suites:

```python
import tls_client

# Create session with specific browser profile
session = tls_client.Session(
    client_identifier="chrome_120",
    random_tls_extension_order=True,
)

# These headers must match the TLS profile
session.headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.9',
    'Accept-Encoding': 'gzip, deflate, br',
    'Sec-Ch-Ua': '"Not_A Brand";v="8", "Chromium";v="120", "Google Chrome";v="120"',
    'Sec-Ch-Ua-Mobile': '?0',
    'Sec-Ch-Ua-Platform': '"Windows"',
}

response = session.get('https://www.example.com')
```

### HTTP/2 Fingerprinting (Akamai Fingerprint)

Beyond TLS, HTTP/2 settings also create fingerprints. The HTTP/2 SETTINGS frame, WINDOW_UPDATE frame, and HEADERS frame priority all vary between implementations:

```python
# HTTP/2 fingerprint components:
# 1. SETTINGS frame values (HEADER_TABLE_SIZE, ENABLE_PUSH, MAX_CONCURRENT_STREAMS, 
#    INITIAL_WINDOW_SIZE, MAX_FRAME_SIZE, MAX_HEADER_LIST_SIZE)
# 2. WINDOW_UPDATE increment
# 3. HEADERS frame pseudo-header order and priority

# Chrome 120 HTTP/2 settings:
# HEADER_TABLE_SIZE: 65536
# ENABLE_PUSH: 0 (disabled)  
# MAX_CONCURRENT_STREAMS: 1000
# INITIAL_WINDOW_SIZE: 6291456
# MAX_FRAME_SIZE: 16384
# MAX_HEADER_LIST_SIZE: 262144
# WINDOW_UPDATE: 15663105

# curl_cffi handles this automatically when impersonating
from curl_cffi import requests

session = requests.Session(impersonate='chrome120')
# This automatically sets correct HTTP/2 settings, TLS config, and header order
response = session.get('https://tls.browserleaks.com/json')
print(response.json())
```

### Verifying Your TLS Fingerprint

Always verify your fingerprint matches what you expect:

```python
import json
from curl_cffi import requests

def check_tls_fingerprint(session):
    """Check your TLS fingerprint against known databases."""
    
    # Check JA3
    r = session.get('https://tls.browserleaks.com/json')
    data = r.json()
    print(f"JA3 Hash: {data.get('ja3_hash')}")
    print(f"JA3 Text: {data.get('ja3_text')[:100]}...")
    
    # Check HTTP/2 fingerprint
    r2 = session.get('https://tls.peet.ws/api/all')
    data2 = r2.json()
    print(f"HTTP/2 Akamai FP: {data2.get('http2', {}).get('akamai_fingerprint')}")
    print(f"TLS Version: {data2.get('tls', {}).get('version')}")
    
    return data, data2

session = requests.Session(impersonate='chrome120')
ja3_data, h2_data = check_tls_fingerprint(session)
```

---

## 1.3 Canvas Fingerprint Spoofing

### How Canvas Fingerprinting Works

Canvas fingerprinting exploits the fact that different hardware, drivers, and OS configurations render identical drawing instructions slightly differently at the sub-pixel level. Detection scripts draw specific shapes, text, and gradients on an invisible canvas, then read back the pixel data via `toDataURL()` or `getImageData()`.

```javascript
// Typical canvas fingerprint collection (what detection scripts do)
function getCanvasFingerprint() {
    const canvas = document.createElement('canvas');
    canvas.width = 200;
    canvas.height = 50;
    const ctx = canvas.getContext('2d');
    
    // Draw text with specific font
    ctx.textBaseline = 'alphabetic';
    ctx.fillStyle = '#f60';
    ctx.fillRect(125, 1, 62, 20);
    ctx.fillStyle = '#069';
    ctx.font = '11pt no-real-font-123,Arial';
    ctx.fillText('Cwm fjordbank glyphs vext quiz, 😃', 2, 15);
    
    // Draw with blending
    ctx.fillStyle = 'rgba(102, 204, 0, 0.7)';
    ctx.fillRect(0, 0, 30, 30);
    
    return canvas.toDataURL();
}
```

### Spoofing Canvas in Playwright

There are two approaches: **noise injection** (adding subtle random noise to canvas output) and **consistent spoofing** (replacing the output with a pre-computed value).

```python
# Approach 1: Noise injection (recommended — more realistic)
CANVAS_NOISE_SCRIPT = """
(function() {
    const NOISE_SEED = %d;  // Unique per profile, consistent across sessions
    
    // Seeded PRNG for consistent noise
    function mulberry32(a) {
        return function() {
            a |= 0; a = a + 0x6D2B79F5 | 0;
            var t = Math.imul(a ^ a >>> 15, 1 | a);
            t = t + Math.imul(t ^ t >>> 7, 61 | t) ^ t;
            return ((t ^ t >>> 14) >>> 0) / 4294967296;
        }
    }
    
    const rng = mulberry32(NOISE_SEED);
    
    // Override toDataURL
    const originalToDataURL = HTMLCanvasElement.prototype.toDataURL;
    HTMLCanvasElement.prototype.toDataURL = function(type, quality) {
        const ctx = this.getContext('2d');
        if (ctx) {
            const imageData = ctx.getImageData(0, 0, this.width, this.height);
            const data = imageData.data;
            // Add very subtle noise (1-2 values per channel, imperceptible)
            for (let i = 0; i < data.length; i += 4) {
                // Only modify ~10%% of pixels
                if (rng() < 0.1) {
                    data[i] = Math.max(0, Math.min(255, data[i] + Math.floor((rng() - 0.5) * 3)));
                    data[i+1] = Math.max(0, Math.min(255, data[i+1] + Math.floor((rng() - 0.5) * 3)));
                    data[i+2] = Math.max(0, Math.min(255, data[i+2] + Math.floor((rng() - 0.5) * 3)));
                }
            }
            ctx.putImageData(imageData, 0, 0);
        }
        return originalToDataURL.call(this, type, quality);
    };
    
    // Override toBlob
    const originalToBlob = HTMLCanvasElement.prototype.toBlob;
    HTMLCanvasElement.prototype.toBlob = function(callback, type, quality) {
        const ctx = this.getContext('2d');
        if (ctx) {
            const imageData = ctx.getImageData(0, 0, this.width, this.height);
            const data = imageData.data;
            for (let i = 0; i < data.length; i += 4) {
                if (rng() < 0.1) {
                    data[i] = Math.max(0, Math.min(255, data[i] + Math.floor((rng() - 0.5) * 3)));
                    data[i+1] = Math.max(0, Math.min(255, data[i+1] + Math.floor((rng() - 0.5) * 3)));
                    data[i+2] = Math.max(0, Math.min(255, data[i+2] + Math.floor((rng() - 0.5) * 3)));
                }
            }
            ctx.putImageData(imageData, 0, 0);
        }
        return originalToBlob.call(this, callback, type, quality);
    };
    
    // Also override getImageData to be consistent
    const originalGetImageData = CanvasRenderingContext2D.prototype.getImageData;
    CanvasRenderingContext2D.prototype.getImageData = function(sx, sy, sw, sh) {
        const imageData = originalGetImageData.call(this, sx, sy, sw, sh);
        const data = imageData.data;
        for (let i = 0; i < data.length; i += 4) {
            if (rng() < 0.1) {
                data[i] = Math.max(0, Math.min(255, data[i] + Math.floor((rng() - 0.5) * 3)));
            }
        }
        return imageData;
    };
})();
"""

import random
from playwright.async_api import async_playwright

async def create_stealth_page(browser, profile):
    """Create a page with canvas fingerprint noise."""
    context = await browser.new_context(**profile.to_playwright_args())
    
    # Inject canvas noise before any page loads
    noise_seed = random.randint(1, 2**31)
    await context.add_init_script(CANVAS_NOISE_SCRIPT % noise_seed)
    
    page = await context.new_page()
    return page, context
```

### Canvas Fingerprint Consistency

A critical point: the canvas fingerprint must remain **consistent across page loads for the same "user"**. If the fingerprint changes on every request, that itself is a detection signal. Use a seeded PRNG tied to the browser profile:

```python
import hashlib

def get_canvas_seed(profile_id: str) -> int:
    """Generate a consistent canvas noise seed for a given profile."""
    hash_bytes = hashlib.sha256(f"canvas-seed-{profile_id}".encode()).digest()
    return int.from_bytes(hash_bytes[:4], 'big')

# Same profile always gets same seed = same fingerprint
seed = get_canvas_seed("profile-abc-123")  # Always returns same value
```

---

## 1.4 WebGL Fingerprinting

### WebGL Fingerprint Vectors

WebGL fingerprinting is even more revealing than canvas because it directly exposes GPU information:

1. **Renderer string**: `ANGLE (NVIDIA GeForce RTX 3080, D3D11)` or `Apple GPU`
2. **Vendor string**: `Google Inc. (NVIDIA)` or `Apple`
3. **Supported extensions**: List of WebGL extensions
4. **Shader precision**: `mediump`, `highp` precision formats
5. **Max parameters**: `MAX_TEXTURE_SIZE`, `MAX_RENDERBUFFER_SIZE`, etc.
6. **Unmasked renderer/vendor**: Via `WEBGL_debug_renderer_info` extension

```python
# WebGL spoofing injection script
WEBGL_SPOOF_SCRIPT = """
(function() {
    const config = %s;  // JSON config injected
    
    // Override WebGL getParameter
    const getParameterProxyHandler = {
        apply: function(target, thisArg, args) {
            const param = args[0];
            const gl = thisArg;
            
            // UNMASKED_VENDOR_WEBGL
            if (param === 0x9245) {
                return config.vendor;
            }
            // UNMASKED_RENDERER_WEBGL
            if (param === 0x9246) {
                return config.renderer;
            }
            // MAX_TEXTURE_SIZE
            if (param === 0x0D33) {
                return config.maxTextureSize || target.call(thisArg, param);
            }
            // MAX_RENDERBUFFER_SIZE
            if (param === 0x84E8) {
                return config.maxRenderbufferSize || target.call(thisArg, param);
            }
            
            return target.call(thisArg, ...args);
        }
    };
    
    // Override for WebGL1
    const originalGetParameter = WebGLRenderingContext.prototype.getParameter;
    WebGLRenderingContext.prototype.getParameter = new Proxy(originalGetParameter, getParameterProxyHandler);
    
    // Override for WebGL2
    if (typeof WebGL2RenderingContext !== 'undefined') {
        const originalGetParameter2 = WebGL2RenderingContext.prototype.getParameter;
        WebGL2RenderingContext.prototype.getParameter = new Proxy(originalGetParameter2, getParameterProxyHandler);
    }
    
    // Override getSupportedExtensions to return consistent list
    const originalGetExtensions = WebGLRenderingContext.prototype.getSupportedExtensions;
    WebGLRenderingContext.prototype.getSupportedExtensions = function() {
        if (config.extensions) {
            return config.extensions;
        }
        return originalGetExtensions.call(this);
    };
    
    // Override getShaderPrecisionFormat
    const originalGetShaderPrecision = WebGLRenderingContext.prototype.getShaderPrecisionFormat;
    WebGLRenderingContext.prototype.getShaderPrecisionFormat = function(shaderType, precisionType) {
        const result = originalGetShaderPrecision.call(this, shaderType, precisionType);
        if (config.shaderPrecision) {
            // Return spoofed precision values
            return {
                rangeMin: config.shaderPrecision.rangeMin || result.rangeMin,
                rangeMax: config.shaderPrecision.rangeMax || result.rangeMax,
                precision: config.shaderPrecision.precision || result.precision,
            };
        }
        return result;
    };
})();
"""

# WebGL configurations for common hardware
WEBGL_CONFIGS = {
    'nvidia_rtx_3080': {
        'vendor': 'Google Inc. (NVIDIA)',
        'renderer': 'ANGLE (NVIDIA, NVIDIA GeForce RTX 3080 Direct3D11 vs_5_0 ps_5_0, D3D11)',
        'maxTextureSize': 32768,
        'maxRenderbufferSize': 32768,
    },
    'nvidia_gtx_1660': {
        'vendor': 'Google Inc. (NVIDIA)',
        'renderer': 'ANGLE (NVIDIA, NVIDIA GeForce GTX 1660 SUPER Direct3D11 vs_5_0 ps_5_0, D3D11)',
        'maxTextureSize': 32768,
        'maxRenderbufferSize': 32768,
    },
    'apple_m1': {
        'vendor': 'Google Inc. (Apple)',
        'renderer': 'ANGLE (Apple, ANGLE Metal Renderer: Apple M1, Unspecified Version)',
        'maxTextureSize': 16384,
        'maxRenderbufferSize': 16384,
    },
    'apple_m2': {
        'vendor': 'Google Inc. (Apple)',
        'renderer': 'ANGLE (Apple, ANGLE Metal Renderer: Apple M2, Unspecified Version)',
        'maxTextureSize': 16384,
        'maxRenderbufferSize': 16384,
    },
    'intel_uhd_630': {
        'vendor': 'Google Inc. (Intel)',
        'renderer': 'ANGLE (Intel, Intel(R) UHD Graphics 630 Direct3D11 vs_5_0 ps_5_0, D3D11)',
        'maxTextureSize': 16384,
        'maxRenderbufferSize': 16384,
    },
}

import json

def get_webgl_injection(gpu_profile: str) -> str:
    """Get the WebGL spoofing script for a specific GPU profile."""
    config = WEBGL_CONFIGS.get(gpu_profile, WEBGL_CONFIGS['nvidia_gtx_1660'])
    return WEBGL_SPOOF_SCRIPT % json.dumps(config)
```

### WebGL Render Tests

Some advanced detection systems go beyond reading parameters — they actually render 3D scenes and hash the output. This is similar to canvas fingerprinting but in 3D. The noise injection approach works here too:

```python
WEBGL_RENDER_NOISE = """
(function() {
    const seed = %d;
    function rng(s) {
        s |= 0; s = s + 0x6D2B79F5 | 0;
        var t = Math.imul(s ^ s >>> 15, 1 | s);
        t = t + Math.imul(t ^ t >>> 7, 61 | t) ^ t;
        return ((t ^ t >>> 14) >>> 0) / 4294967296;
    }
    
    // Override readPixels for WebGL
    const origReadPixels = WebGLRenderingContext.prototype.readPixels;
    WebGLRenderingContext.prototype.readPixels = function() {
        origReadPixels.apply(this, arguments);
        const pixels = arguments[6];
        if (pixels && pixels.length) {
            let s = seed;
            for (let i = 0; i < pixels.length; i += 4) {
                s++;
                if (rng(s) < 0.05) {
                    pixels[i] = Math.max(0, Math.min(255, pixels[i] + (rng(s + 1) > 0.5 ? 1 : -1)));
                }
            }
        }
    };
})();
"""
```

---

## 1.5 Audio Fingerprinting

### AudioContext Fingerprinting

The AudioContext API creates another unique fingerprint. Detection scripts create an OscillatorNode, connect it through processing nodes, and analyze the output — which varies by audio hardware and driver:

```python
AUDIO_SPOOF_SCRIPT = """
(function() {
    const noise = %f;  // Small noise value, consistent per profile
    
    // Override AudioBuffer.getChannelData
    const originalGetChannelData = AudioBuffer.prototype.getChannelData;
    AudioBuffer.prototype.getChannelData = function(channel) {
        const data = originalGetChannelData.call(this, channel);
        // Only modify if this looks like a fingerprinting attempt (short buffer)
        if (this.length < 1000) {
            for (let i = 0; i < data.length; i++) {
                data[i] = data[i] + noise * 0.0001 * (i %% 2 === 0 ? 1 : -1);
            }
        }
        return data;
    };
    
    // Override AnalyserNode.getFloatFrequencyData
    const originalGetFloat = AnalyserNode.prototype.getFloatFrequencyData;
    AnalyserNode.prototype.getFloatFrequencyData = function(array) {
        originalGetFloat.call(this, array);
        for (let i = 0; i < array.length; i++) {
            array[i] = array[i] + noise * 0.1;
        }
    };
})();
"""

def get_audio_noise(profile_id: str) -> float:
    """Get consistent audio noise value for a profile."""
    import hashlib
    h = hashlib.sha256(f"audio-{profile_id}".encode()).digest()
    return (int.from_bytes(h[:2], 'big') / 65535.0) * 2 - 1  # Range [-1, 1]
```

---

## 1.6 Timezone and Language Consistency

### The Consistency Chain

Every element of the browser profile must tell the same story. If your IP address geolocates to Tokyo but your timezone is `America/New_York` and your language is `en-US`, that's a red flag. The consistency chain includes:

1. **IP geolocation** → determines expected timezone, language, and locale
2. **Timezone** (`Intl.DateTimeFormat().resolvedOptions().timeZone`)
3. **Language** (`navigator.language`, `navigator.languages`)
4. **Date formatting** (`new Date().toString()` includes timezone name)
5. **Intl API** (locale-dependent number/date/currency formatting)
6. **Accept-Language header**

```python
# Geo-consistent profile generation
import requests
from typing import Dict, Optional

# Mapping of common proxy locations to browser settings
GEO_PROFILES = {
    'US-NY': {
        'timezone': 'America/New_York',
        'languages': ['en-US', 'en'],
        'accept_language': 'en-US,en;q=0.9',
        'locale': 'en-US',
        'date_format': 'M/D/YYYY',
        'currency': 'USD',
    },
    'US-CA': {
        'timezone': 'America/Los_Angeles',
        'languages': ['en-US', 'en'],
        'accept_language': 'en-US,en;q=0.9',
        'locale': 'en-US',
        'date_format': 'M/D/YYYY',
        'currency': 'USD',
    },
    'UK': {
        'timezone': 'Europe/London',
        'languages': ['en-GB', 'en'],
        'accept_language': 'en-GB,en;q=0.9',
        'locale': 'en-GB',
        'date_format': 'DD/MM/YYYY',
        'currency': 'GBP',
    },
    'DE': {
        'timezone': 'Europe/Berlin',
        'languages': ['de-DE', 'de', 'en'],
        'accept_language': 'de-DE,de;q=0.9,en;q=0.8',
        'locale': 'de-DE',
        'date_format': 'DD.MM.YYYY',
        'currency': 'EUR',
    },
    'JP': {
        'timezone': 'Asia/Tokyo',
        'languages': ['ja-JP', 'ja', 'en'],
        'accept_language': 'ja-JP,ja;q=0.9,en;q=0.8',
        'locale': 'ja-JP',
        'date_format': 'YYYY/MM/DD',
        'currency': 'JPY',
    },
    'BR': {
        'timezone': 'America/Sao_Paulo',
        'languages': ['pt-BR', 'pt', 'en'],
        'accept_language': 'pt-BR,pt;q=0.9,en;q=0.8',
        'locale': 'pt-BR',
        'date_format': 'DD/MM/YYYY',
        'currency': 'BRL',
    },
}

def detect_geo_from_proxy(proxy_url: str) -> Optional[str]:
    """Detect the geographic location of a proxy."""
    try:
        resp = requests.get(
            'https://ipapi.co/json/',
            proxies={'http': proxy_url, 'https': proxy_url},
            timeout=10
        )
        data = resp.json()
        country = data.get('country_code')
        region = data.get('region_code')
        
        # Map to our geo profiles
        if country == 'US':
            east_states = ['NY', 'NJ', 'CT', 'MA', 'PA', 'VA', 'MD', 'FL', 'GA', 'NC']
            if region in east_states:
                return 'US-NY'
            return 'US-CA'
        elif country == 'GB':
            return 'UK'
        elif country == 'DE':
            return 'DE'
        elif country == 'JP':
            return 'JP'
        elif country == 'BR':
            return 'BR'
        
        return None
    except Exception:
        return None

def build_geo_consistent_profile(proxy_url: str) -> dict:
    """Build a browser profile that's consistent with proxy location."""
    geo = detect_geo_from_proxy(proxy_url)
    if not geo:
        geo = 'US-CA'  # Default fallback
    
    profile = GEO_PROFILES[geo]
    return {
        'proxy': proxy_url,
        'timezone_id': profile['timezone'],
        'locale': profile['locale'],
        'languages': profile['languages'],
        'accept_language': profile['accept_language'],
        'geolocation': None,  # Let it use IP-based
    }
```

### Deep Timezone Consistency

Detection scripts probe timezone beyond just `Intl.DateTimeFormat`:

```python
TIMEZONE_CONSISTENCY_SCRIPT = """
(function() {
    const targetTZ = '%s';
    const targetOffset = %d;  // minutes
    
    // Ensure Date.prototype.getTimezoneOffset returns correct value
    const originalGetTimezoneOffset = Date.prototype.getTimezoneOffset;
    Date.prototype.getTimezoneOffset = function() {
        return targetOffset;
    };
    
    // Ensure Date.prototype.toString includes correct timezone
    const originalToString = Date.prototype.toString;
    Date.prototype.toString = function() {
        // Let Intl handle formatting for consistency
        const formatter = new Intl.DateTimeFormat('en-US', {
            timeZone: targetTZ,
            weekday: 'short',
            year: 'numeric',
            month: 'short',
            day: '2-digit',
            hour: '2-digit',
            minute: '2-digit',
            second: '2-digit',
            hour12: false,
            timeZoneName: 'long'
        });
        return formatter.format(this);
    };
    
    // Ensure performance.timeOrigin is consistent
    // (some scripts check if time origin matches timezone)
})();
"""

# Timezone offsets (standard time, in minutes - note: negative for west of UTC)
TZ_OFFSETS = {
    'America/New_York': 300,     # UTC-5 (EST)
    'America/Los_Angeles': 480,  # UTC-8 (PST)
    'Europe/London': 0,          # UTC+0 (GMT)
    'Europe/Berlin': -60,        # UTC+1 (CET)
    'Asia/Tokyo': -540,          # UTC+9 (JST)
    'America/Sao_Paulo': 180,    # UTC-3 (BRT)
}
```

---

## 1.7 Residential Proxy Rotation

### Why Residential Proxies Matter

Datacenter IPs are cataloged in public databases (ASN lookups reveal hosting providers like AWS, DigitalOcean, Hetzner). Detection systems instantly flag datacenter traffic. Residential proxies use IP addresses assigned to real ISPs (Comcast, AT&T, BT) and are far harder to detect.

### Proxy Types Comparison

| Type | Detection Risk | Speed | Cost | Use Case |
|------|---------------|-------|------|----------|
| Datacenter | Very High | Very Fast | $1-5/GB | Low-value targets |
| Residential | Low | Medium | $5-15/GB | General scraping |
| ISP/Static Residential | Very Low | Fast | $2-5/IP/month | Account management |
| Mobile (4G/5G) | Lowest | Slow | $20-50/GB | Highest protection targets |

### Proxy Pool Management

```python
import time
import random
import asyncio
from dataclasses import dataclass, field
from typing import List, Optional, Dict
from collections import defaultdict
import aiohttp

@dataclass
class ProxyInfo:
    url: str
    provider: str
    geo: str
    proxy_type: str  # 'residential', 'datacenter', 'mobile'
    last_used: float = 0
    fail_count: int = 0
    success_count: int = 0
    banned_domains: set = field(default_factory=set)
    cooldown_until: float = 0

class ProxyPool:
    """Production proxy pool with rotation, cooldowns, and health tracking."""
    
    def __init__(self, proxies: List[ProxyInfo], min_delay: float = 2.0):
        self.proxies = proxies
        self.min_delay = min_delay
        self.domain_proxy_map: Dict[str, List[str]] = defaultdict(list)  # domain -> [proxy_urls used]
        self._lock = asyncio.Lock()
    
    async def get_proxy(self, domain: str, geo: Optional[str] = None) -> Optional[ProxyInfo]:
        """Get the best available proxy for a domain."""
        async with self._lock:
            now = time.time()
            candidates = []
            
            for proxy in self.proxies:
                # Skip if on cooldown
                if proxy.cooldown_until > now:
                    continue
                # Skip if banned for this domain
                if domain in proxy.banned_domains:
                    continue
                # Skip if geo doesn't match
                if geo and proxy.geo != geo:
                    continue
                # Skip if used too recently
                if now - proxy.last_used < self.min_delay:
                    continue
                
                # Calculate score (lower is better)
                score = 0
                score += proxy.fail_count * 10
                score -= proxy.success_count * 0.1
                # Prefer proxies not recently used for this domain
                if proxy.url in self.domain_proxy_map[domain]:
                    score += 5
                # Prefer residential/mobile over datacenter
                if proxy.proxy_type == 'mobile':
                    score -= 3
                elif proxy.proxy_type == 'residential':
                    score -= 1
                
                candidates.append((score, random.random(), proxy))  # random for tiebreaker
            
            if not candidates:
                return None
            
            candidates.sort(key=lambda x: (x[0], x[1]))
            best = candidates[0][2]
            best.last_used = now
            self.domain_proxy_map[domain].append(best.url)
            
            # Keep only last 10 proxies per domain
            if len(self.domain_proxy_map[domain]) > 10:
                self.domain_proxy_map[domain] = self.domain_proxy_map[domain][-10:]
            
            return best
    
    async def report_success(self, proxy: ProxyInfo):
        """Report a successful request."""
        async with self._lock:
            proxy.success_count += 1
            proxy.fail_count = max(0, proxy.fail_count - 1)
    
    async def report_failure(self, proxy: ProxyInfo, domain: str, is_ban: bool = False):
        """Report a failed request."""
        async with self._lock:
            proxy.fail_count += 1
            
            if is_ban:
                proxy.banned_domains.add(domain)
                proxy.cooldown_until = time.time() + 300  # 5 min cooldown
            elif proxy.fail_count >= 3:
                proxy.cooldown_until = time.time() + 60  # 1 min cooldown
    
    def stats(self) -> dict:
        """Get pool statistics."""
        now = time.time()
        return {
            'total': len(self.proxies),
            'available': sum(1 for p in self.proxies if p.cooldown_until <= now),
            'on_cooldown': sum(1 for p in self.proxies if p.cooldown_until > now),
            'total_successes': sum(p.success_count for p in self.proxies),
            'total_failures': sum(p.fail_count for p in self.proxies),
        }


# Initialize pool with multiple providers
def create_proxy_pool() -> ProxyPool:
    """Create a proxy pool from multiple providers."""
    proxies = []
    
    # BrightData residential proxies (rotating)
    for geo in ['US-NY', 'US-CA', 'UK', 'DE']:
        proxies.append(ProxyInfo(
            url=f'http://user-zone-residential-country-us:pass@brd.superproxy.io:22225',
            provider='brightdata',
            geo=geo,
            proxy_type='residential',
        ))
    
    # Oxylabs residential
    for i in range(5):
        proxies.append(ProxyInfo(
            url=f'http://user:pass@pr.oxylabs.io:7777',
            provider='oxylabs',
            geo='US-CA',
            proxy_type='residential',
        ))
    
    # SmartProxy mobile
    proxies.append(ProxyInfo(
        url='http://user:pass@gate.smartproxy.com:10001',
        provider='smartproxy',
        geo='US',
        proxy_type='mobile',
    ))
    
    return ProxyPool(proxies, min_delay=3.0)
```

### Sticky Sessions

For multi-page scraping (login flows, pagination), you need the same IP across requests:

```python
class StickySession:
    """Maintain the same proxy IP for a scraping session."""
    
    def __init__(self, pool: ProxyPool, domain: str, geo: Optional[str] = None):
        self.pool = pool
        self.domain = domain
        self.geo = geo
        self.proxy: Optional[ProxyInfo] = None
        self.session_id = f"session-{random.randint(100000, 999999)}"
    
    async def get_proxy(self) -> ProxyInfo:
        """Get the sticky proxy (same one each time)."""
        if self.proxy is None:
            self.proxy = await self.pool.get_proxy(self.domain, self.geo)
        return self.proxy
    
    async def rotate(self):
        """Force rotate to a new proxy (if current one fails)."""
        if self.proxy:
            await self.pool.report_failure(self.proxy, self.domain, is_ban=True)
        self.proxy = None
        return await self.get_proxy()
    
    def get_sticky_url(self) -> str:
        """Get proxy URL with session ID for provider-side stickiness."""
        # BrightData format: append session ID to username
        base = self.proxy.url
        if 'brd.superproxy.io' in base:
            return base.replace('user-zone', f'user-zone-session-{self.session_id}')
        # Oxylabs format
        if 'oxylabs.io' in base:
            return base.replace('user:', f'user-sessid-{self.session_id}:')
        return base
```

---

## 1.8 Request Pattern Randomization

### Why Patterns Matter

Even with perfect fingerprints and clean proxies, **behavioral patterns** can expose you. Humans don't make requests at precisely 2-second intervals. They don't visit pages in alphabetical order. They don't hit 1000 pages without ever scrolling.

### Realistic Delay Patterns

```python
import random
import time
import numpy as np
from typing import Callable

class HumanDelay:
    """Generate human-like delays between requests."""
    
    @staticmethod
    def between_pages() -> float:
        """Delay between navigating to different pages.
        Models human reading time + thinking + clicking.
        """
        # Log-normal distribution: most delays 3-8s, occasional long pauses
        base = np.random.lognormal(mean=1.5, sigma=0.5)
        # Clip to reasonable range
        delay = max(1.5, min(base, 30.0))
        # 10% chance of "distracted" pause (15-60s)
        if random.random() < 0.1:
            delay += random.uniform(15, 60)
        return delay
    
    @staticmethod
    def between_actions() -> float:
        """Delay between actions on the same page (clicking, scrolling)."""
        return max(0.3, np.random.lognormal(mean=0.5, sigma=0.4))
    
    @staticmethod
    def typing_delay() -> float:
        """Delay between keystrokes when typing."""
        # Average typing speed: 40-60 WPM = 100-150ms per character
        base = random.gauss(120, 30)
        # Occasional pause (thinking)
        if random.random() < 0.05:
            base += random.uniform(500, 2000)
        return max(50, base) / 1000  # Convert to seconds
    
    @staticmethod
    def session_pattern(num_pages: int) -> list:
        """Generate a realistic pattern of delays for a scraping session.
        
        Humans slow down over time (fatigue) and take occasional breaks.
        """
        delays = []
        for i in range(num_pages):
            base_delay = HumanDelay.between_pages()
            
            # Fatigue factor: delays increase slightly over time
            fatigue = 1.0 + (i / num_pages) * 0.3
            base_delay *= fatigue
            
            # Break every 15-30 pages
            if i > 0 and i % random.randint(15, 30) == 0:
                base_delay += random.uniform(30, 120)  # 30s-2min break
            
            delays.append(base_delay)
        
        return delays


class RequestPatternRandomizer:
    """Randomize request patterns to avoid detection."""
    
    def __init__(self):
        self.delay = HumanDelay()
    
    def randomize_header_order(self, headers: dict) -> dict:
        """Randomize non-critical header order.
        Note: Some headers must maintain order (Host, Connection).
        """
        # Headers that browsers send in consistent order
        ordered_keys = ['Host', 'Connection', 'Cache-Control', 'Upgrade-Insecure-Requests',
                       'User-Agent', 'Accept', 'Sec-Fetch-Site', 'Sec-Fetch-Mode', 
                       'Sec-Fetch-User', 'Sec-Fetch-Dest', 'Accept-Encoding', 'Accept-Language']
        
        result = {}
        for key in ordered_keys:
            if key in headers:
                result[key] = headers[key]
        
        # Add remaining headers
        for key, value in headers.items():
            if key not in result:
                result[key] = value
        
        return result
    
    def generate_referer_chain(self, target_url: str) -> list:
        """Generate a plausible referer chain to reach the target URL.
        
        Instead of directly hitting the target, simulate a natural navigation path:
        Google search -> landing page -> internal navigation -> target
        """
        from urllib.parse import urlparse
        parsed = urlparse(target_url)
        domain = parsed.netloc
        
        chain = [
            # Start with Google search
            {
                'url': f'https://www.google.com/search?q={domain.replace("www.", "")}',
                'referer': None,
            },
            # Click through to homepage
            {
                'url': f'https://{domain}/',
                'referer': 'https://www.google.com/',
            },
        ]
        
        # If target is deep, add intermediate steps
        path_parts = parsed.path.strip('/').split('/')
        if len(path_parts) > 1:
            for i in range(1, len(path_parts)):
                intermediate = '/'.join(path_parts[:i])
                chain.append({
                    'url': f'https://{domain}/{intermediate}/',
                    'referer': chain[-1]['url'],
                })
        
        # Final target
        chain.append({
            'url': target_url,
            'referer': chain[-1]['url'],
        })
        
        return chain
    
    def simulate_scroll_behavior(self) -> list:
        """Generate realistic scroll events to simulate on a page."""
        events = []
        current_y = 0
        page_height = random.randint(2000, 8000)
        
        while current_y < page_height:
            # Scroll amount varies
            scroll_amount = random.randint(100, 500)
            current_y += scroll_amount
            
            delay = random.uniform(0.5, 3.0)
            
            # Occasionally scroll up a bit (re-reading)
            if random.random() < 0.15 and current_y > 300:
                events.append({
                    'direction': 'up',
                    'amount': random.randint(50, 200),
                    'delay': delay,
                })
                current_y -= random.randint(50, 200)
            
            events.append({
                'direction': 'down',
                'amount': scroll_amount,
                'delay': delay,
            })
            
            # Pause to "read" content
            if random.random() < 0.3:
                events.append({
                    'direction': 'pause',
                    'amount': 0,
                    'delay': random.uniform(2.0, 8.0),
                })
        
        return events
    
    def simulate_mouse_movement(self, start: tuple, end: tuple, steps: int = None) -> list:
        """Generate realistic mouse movement from start to end point.
        
        Uses Bezier curves for natural-looking paths.
        """
        if steps is None:
            distance = ((end[0]-start[0])**2 + (end[1]-start[1])**2) ** 0.5
            steps = max(10, int(distance / 10))
        
        # Generate control points for Bezier curve
        cp1 = (
            start[0] + random.uniform(-50, 50) + (end[0] - start[0]) * 0.3,
            start[1] + random.uniform(-50, 50) + (end[1] - start[1]) * 0.3,
        )
        cp2 = (
            start[0] + (end[0] - start[0]) * 0.7 + random.uniform(-50, 50),
            start[1] + (end[1] - start[1]) * 0.7 + random.uniform(-50, 50),
        )
        
        points = []
        for i in range(steps + 1):
            t = i / steps
            # Cubic Bezier
            x = (1-t)**3 * start[0] + 3*(1-t)**2*t * cp1[0] + 3*(1-t)*t**2 * cp2[0] + t**3 * end[0]
            y = (1-t)**3 * start[1] + 3*(1-t)**2*t * cp1[1] + 3*(1-t)*t**2 * cp2[1] + t**3 * end[1]
            
            # Add tiny jitter (hand tremor)
            x += random.gauss(0, 1)
            y += random.gauss(0, 1)
            
            # Variable speed (slow at start and end, fast in middle)
            speed = 0.5 + 2.0 * (4 * t * (1 - t))  # Parabolic speed curve
            delay = (1.0 / speed) * (1.0 / steps) * random.uniform(0.8, 1.2)
            
            points.append({
                'x': int(x),
                'y': int(y),
                'delay': max(0.001, delay * 0.01),  # ~5-20ms between points
            })
        
        return points
```

### Implementing Mouse Movement in Playwright

```python
from playwright.async_api import Page
import asyncio

async def human_click(page: Page, selector: str):
    """Click an element with human-like mouse movement."""
    randomizer = RequestPatternRandomizer()
    
    # Get element position
    element = await page.query_selector(selector)
    box = await element.bounding_box()
    
    if not box:
        await page.click(selector)
        return
    
    # Target: random point within element (not dead center)
    target_x = box['x'] + random.uniform(box['width'] * 0.2, box['width'] * 0.8)
    target_y = box['y'] + random.uniform(box['height'] * 0.2, box['height'] * 0.8)
    
    # Current mouse position (approximate)
    viewport = page.viewport_size
    start_x = random.randint(0, viewport['width'])
    start_y = random.randint(0, viewport['height'])
    
    # Generate movement path
    path = randomizer.simulate_mouse_movement(
        (start_x, start_y),
        (target_x, target_y)
    )
    
    # Execute movement
    for point in path:
        await page.mouse.move(point['x'], point['y'])
        await asyncio.sleep(point['delay'])
    
    # Small pause before clicking (human reaction)
    await asyncio.sleep(random.uniform(0.05, 0.15))
    
    # Click with slight position jitter
    await page.mouse.click(
        target_x + random.gauss(0, 2),
        target_y + random.gauss(0, 2)
    )


async def human_type(page: Page, selector: str, text: str):
    """Type text with human-like timing."""
    delay = HumanDelay()
    
    await human_click(page, selector)
    await asyncio.sleep(random.uniform(0.3, 0.8))
    
    for char in text:
        await page.keyboard.type(char)
        await asyncio.sleep(delay.typing_delay())
        
        # Occasional typo and backspace (5% chance)
        if random.random() < 0.05:
            wrong_char = random.choice('abcdefghijklmnopqrstuvwxyz')
            await page.keyboard.type(wrong_char)
            await asyncio.sleep(random.uniform(0.1, 0.3))
            await page.keyboard.press('Backspace')
            await asyncio.sleep(random.uniform(0.1, 0.2))
```

---

## 1.9 Putting It All Together: Complete Stealth Scraper

Here's a production-ready stealth scraper that combines all the techniques:

```python
import asyncio
import json
import random
import logging
from pathlib import Path
from dataclasses import dataclass
from typing import Optional, List, Dict, Any

from playwright.async_api import async_playwright, Browser, BrowserContext, Page
from curl_cffi import requests as curl_requests

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger('stealth_scraper')


class StealthScraper:
    """Production stealth scraper combining all anti-detection techniques."""
    
    def __init__(self, proxy_pool: ProxyPool, headless: bool = True):
        self.proxy_pool = proxy_pool
        self.headless = headless
        self.browser: Optional[Browser] = None
        self.playwright = None
        self.delay = HumanDelay()
        self.randomizer = RequestPatternRandomizer()
    
    async def start(self):
        """Initialize the browser."""
        self.playwright = await async_playwright().start()
        self.browser = await self.playwright.chromium.launch(
            headless=self.headless,
            args=[
                '--disable-blink-features=AutomationControlled',
                '--disable-features=IsolateOrigins,site-per-process',
                '--disable-infobars',
                '--no-first-run',
                '--no-default-browser-check',
                '--disable-background-timer-throttling',
                '--disable-backgrounding-occluded-windows',
                '--disable-renderer-backgrounding',
                '--disable-hang-monitor',
                '--disable-prompt-on-repost',
            ],
        )
    
    async def create_session(self, domain: str, geo: Optional[str] = None) -> tuple:
        """Create a new stealth browsing session."""
        # Get a proxy
        proxy_info = await self.proxy_pool.get_proxy(domain, geo)
        if not proxy_info:
            raise Exception("No available proxies")
        
        # Build geo-consistent profile
        profile = BrowserProfile(
            'windows_chrome' if 'US' in (geo or 'US') else 'mac_chrome',
            '120.0.0.0'
        )
        
        # Get canvas/WebGL seeds
        profile_id = f"{proxy_info.url}-{domain}"
        canvas_seed = get_canvas_seed(profile_id)
        audio_noise = get_audio_noise(profile_id)
        
        # Create context with proxy
        context = await self.browser.new_context(
            **profile.to_playwright_args(),
            proxy={
                'server': proxy_info.url.split('@')[1] if '@' in proxy_info.url else proxy_info.url,
                'username': proxy_info.url.split('://')[1].split(':')[0] if '@' in proxy_info.url else None,
                'password': proxy_info.url.split(':')[2].split('@')[0] if '@' in proxy_info.url else None,
            },
        )
        
        # Inject all stealth scripts
        stealth_scripts = [
            profile.get_injection_script(),
            CANVAS_NOISE_SCRIPT % canvas_seed,
            get_webgl_injection('nvidia_gtx_1660' if 'windows' in profile.profile_type else 'apple_m1'),
            AUDIO_SPOOF_SCRIPT % audio_noise,
            self._get_webdriver_evasion_script(),
            self._get_permissions_evasion_script(),
            self._get_plugins_evasion_script(profile),
        ]
        
        for script in stealth_scripts:
            await context.add_init_script(script)
        
        page = await context.new_page()
        
        return page, context, proxy_info
    
    def _get_webdriver_evasion_script(self) -> str:
        """Evade navigator.webdriver detection."""
        return """
        // Remove webdriver flag
        Object.defineProperty(navigator, 'webdriver', {
            get: () => undefined
        });
        
        // Remove automation-related properties
        delete window.cdc_adoQpoasnfa76pfcZLmcfl_Array;
        delete window.cdc_adoQpoasnfa76pfcZLmcfl_Promise;
        delete window.cdc_adoQpoasnfa76pfcZLmcfl_Symbol;
        
        // Fix chrome object
        window.chrome = {
            runtime: {
                onMessage: { addListener: function() {} },
                sendMessage: function() {},
                connect: function() { return { onMessage: { addListener: function() {} } }; },
            },
            loadTimes: function() {
                return {
                    requestTime: Date.now() / 1000 - Math.random() * 100,
                    startLoadTime: Date.now() / 1000 - Math.random() * 50,
                    commitLoadTime: Date.now() / 1000 - Math.random() * 10,
                    finishDocumentLoadTime: Date.now() / 1000 - Math.random() * 5,
                    finishLoadTime: Date.now() / 1000 - Math.random() * 2,
                    firstPaintTime: Date.now() / 1000 - Math.random() * 8,
                    firstPaintAfterLoadTime: 0,
                    navigationType: 'Other',
                    wasFetchedViaSpdy: true,
                    wasNpnNegotiated: true,
                    npnNegotiatedProtocol: 'h2',
                    wasAlternateProtocolAvailable: false,
                    connectionInfo: 'h2',
                };
            },
            csi: function() { return { pageT: Date.now() }; },
            app: {
                isInstalled: false,
                InstallState: { DISABLED: 'disabled', INSTALLED: 'installed', NOT_INSTALLED: 'not_installed' },
                RunningState: { CANNOT_RUN: 'cannot_run', READY_TO_RUN: 'ready_to_run', RUNNING: 'running' },
                getDetails: function() { return null; },
                getIsInstalled: function() { return false; },
            },
        };
        
        // Fix Permissions API
        const originalQuery = window.Permissions.prototype.query;
        window.Permissions.prototype.query = function(parameters) {
            if (parameters.name === 'notifications') {
                return Promise.resolve({ state: Notification.permission });
            }
            return originalQuery.call(this, parameters);
        };
        """
    
    def _get_permissions_evasion_script(self) -> str:
        """Fix permission-related detection vectors."""
        return """
        // Override Notification.permission to return 'default' (not 'denied')
        Object.defineProperty(Notification, 'permission', {
            get: () => 'default'
        });
        """
    
    def _get_plugins_evasion_script(self, profile: BrowserProfile) -> str:
        """Add realistic browser plugins."""
        if 'chrome' in profile.profile_type:
            return """
            Object.defineProperty(navigator, 'plugins', {
                get: () => {
                    const plugins = [
                        { name: 'Chrome PDF Plugin', filename: 'internal-pdf-viewer', description: 'Portable Document Format' },
                        { name: 'Chrome PDF Viewer', filename: 'mhjfbmdgcfjbbpaeojofohoefgiehjai', description: '' },
                        { name: 'Native Client', filename: 'internal-nacl-plugin', description: '' },
                    ];
                    plugins.length = 3;
                    return plugins;
                }
            });
            
            Object.defineProperty(navigator, 'mimeTypes', {
                get: () => {
                    const mimeTypes = [
                        { type: 'application/pdf', suffixes: 'pdf', description: 'Portable Document Format' },
                        { type: 'application/x-google-chrome-pdf', suffixes: 'pdf', description: 'Portable Document Format' },
                    ];
                    mimeTypes.length = 2;
                    return mimeTypes;
                }
            });
            """
        return ""
    
    async def scrape_page(self, url: str, domain: str, 
                          geo: Optional[str] = None,
                          wait_selector: Optional[str] = None) -> dict:
        """Scrape a single page with full stealth measures."""
        page, context, proxy_info = await self.create_session(domain, geo)
        
        try:
            # Navigate with realistic referer
            chain = self.randomizer.generate_referer_chain(url)
            
            # Sometimes go through the full chain, sometimes shortcut
            if random.random() < 0.3:
                # Full chain (30% of time)
                for step in chain[:-1]:
                    try:
                        await page.goto(step['url'], 
                                       referer=step['referer'],
                                       wait_until='domcontentloaded',
                                       timeout=15000)
                        await asyncio.sleep(self.delay.between_pages() * 0.3)
                    except Exception:
                        pass  # Intermediate navigation failures are OK
            
            # Navigate to target
            response = await page.goto(
                url,
                referer=chain[-1].get('referer'),
                wait_until='networkidle',
                timeout=30000,
            )
            
            if not response or response.status >= 400:
                await self.proxy_pool.report_failure(proxy_info, domain, is_ban=(response and response.status == 403))
                raise Exception(f"HTTP {response.status if response else 'no response'}")
            
            # Wait for content
            if wait_selector:
                await page.wait_for_selector(wait_selector, timeout=10000)
            
            # Simulate human behavior
            scroll_events = self.randomizer.simulate_scroll_behavior()
            for event in scroll_events[:5]:  # Do a few scrolls
                if event['direction'] == 'down':
                    await page.mouse.wheel(0, event['amount'])
                elif event['direction'] == 'up':
                    await page.mouse.wheel(0, -event['amount'])
                await asyncio.sleep(event['delay'] * 0.3)
            
            # Extract content
            content = await page.content()
            title = await page.title()
            
            await self.proxy_pool.report_success(proxy_info)
            
            return {
                'url': url,
                'status': response.status,
                'title': title,
                'html': content,
                'proxy': proxy_info.url,
            }
            
        except Exception as e:
            logger.error(f"Error scraping {url}: {e}")
            raise
        finally:
            await context.close()
    
    async def scrape_with_curl(self, url: str, domain: str,
                                geo: Optional[str] = None) -> dict:
        """Lightweight scraping using curl_cffi (no browser overhead).
        Use for pages that don't require JavaScript rendering.
        """
        proxy_info = await self.proxy_pool.get_proxy(domain, geo)
        if not proxy_info:
            raise Exception("No available proxies")
        
        try:
            response = curl_requests.get(
                url,
                impersonate='chrome120',
                headers={
                    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8',
                    'Accept-Language': 'en-US,en;q=0.9',
                    'Accept-Encoding': 'gzip, deflate, br',
                    'Cache-Control': 'max-age=0',
                    'Sec-Ch-Ua': '"Not_A Brand";v="8", "Chromium";v="120", "Google Chrome";v="120"',
                    'Sec-Ch-Ua-Mobile': '?0',
                    'Sec-Ch-Ua-Platform': '"Windows"',
                    'Sec-Fetch-Dest': 'document',
                    'Sec-Fetch-Mode': 'navigate',
                    'Sec-Fetch-Site': 'none',
                    'Sec-Fetch-User': '?1',
                    'Upgrade-Insecure-Requests': '1',
                },
                proxies={'https': proxy_info.url, 'http': proxy_info.url},
                timeout=30,
            )
            
            if response.status_code >= 400:
                await self.proxy_pool.report_failure(proxy_info, domain, 
                                                      is_ban=(response.status_code == 403))
                raise Exception(f"HTTP {response.status_code}")
            
            await self.proxy_pool.report_success(proxy_info)
            
            return {
                'url': url,
                'status': response.status_code,
                'html': response.text,
                'headers': dict(response.headers),
            }
            
        except Exception as e:
            await self.proxy_pool.report_failure(proxy_info, domain)
            raise
    
    async def close(self):
        """Clean up resources."""
        if self.browser:
            await self.browser.close()
        if self.playwright:
            await self.playwright.stop()


# Usage example
async def main():
    pool = create_proxy_pool()
    scraper = StealthScraper(pool, headless=True)
    await scraper.start()
    
    try:
        # Browser-based scraping (for JS-heavy sites)
        result = await scraper.scrape_page(
            'https://www.example.com/products',
            domain='example.com',
            geo='US-CA',
            wait_selector='.product-list',
        )
        print(f"Got {len(result['html'])} bytes from {result['url']}")
        
        # Lightweight scraping (for static/SSR pages)
        result2 = await scraper.scrape_with_curl(
            'https://www.example.com/api/products?page=1',
            domain='example.com',
        )
        print(f"API returned {len(result2['html'])} bytes")
        
    finally:
        await scraper.close()

if __name__ == '__main__':
    asyncio.run(main())
```

---

## 1.10 Detection Testing and Validation

### Testing Your Stealth Setup

Before deploying against real targets, validate your anti-detection measures:

```python
DETECTION_TEST_SITES = [
    'https://bot.sannysoft.com/',           # Comprehensive bot detection test
    'https://abrahamjuliot.github.io/creepjs/',  # CreepJS fingerprint analysis
    'https://browserleaks.com/canvas',       # Canvas fingerprint
    'https://browserleaks.com/webgl',        # WebGL fingerprint
    'https://tls.browserleaks.com/',         # TLS/JA3 fingerprint
    'https://pixelscan.net/',                # Pixel-level detection
    'https://www.browserscan.net/',          # Comprehensive scanner
    'https://iphey.com/',                    # IP and browser checks
]

async def run_detection_tests(scraper: StealthScraper):
    """Run detection tests and report results."""
    results = {}
    
    for test_url in DETECTION_TEST_SITES:
        domain = test_url.split('/')[2]
        try:
            page, context, _ = await scraper.create_session(domain)
            await page.goto(test_url, wait_until='networkidle', timeout=30000)
            await asyncio.sleep(5)  # Wait for tests to complete
            
            # Screenshot for manual review
            await page.screenshot(path=f'detection_test_{domain}.png', full_page=True)
            
            # Try to extract test results
            content = await page.content()
            results[test_url] = {
                'status': 'loaded',
                'screenshot': f'detection_test_{domain}.png',
            }
            
            await context.close()
            
        except Exception as e:
            results[test_url] = {'status': 'error', 'error': str(e)}
    
    return results
```

### Common Detection Failures and Fixes

| Issue | Detection Signal | Fix |
|-------|-----------------|-----|
| `navigator.webdriver = true` | Automation detected | Inject webdriver override script |
| Wrong JA3 hash | Python/Node detected | Use curl_cffi or tls-client |
| Missing `chrome` object | Not a real Chrome | Inject chrome object |
| Canvas returns same hash | Fingerprint database match | Use noise injection with unique seed |
| `Permissions.query` rejects | Headless detected | Override Permissions API |
| No plugins/MIME types | Headless detected | Inject realistic plugins |
| WebGL vendor = "Brian Paul" | Mesa/software rendering | Use GPU or spoof WebGL params |
| Consistent timing between requests | Bot pattern | Use HumanDelay with lognormal distribution |
| IP from datacenter ASN | Non-residential | Use residential/mobile proxies |
| Timezone ≠ IP location | Geo mismatch | Use geo-consistent profiles |

---

## 1.11 Advanced Techniques

### Headless Browser Detection Evasion

Modern headless Chrome is much better than it used to be, but some detection still works:

```python
ADVANCED_HEADLESS_EVASION = """
(function() {
    // Override specific headless indicators
    
    // 1. Fix broken image dimensions (headless renders images with 0 dimensions)
    const originalImage = window.Image;
    window.Image = function(...args) {
        const img = new originalImage(...args);
        Object.defineProperty(img, 'naturalHeight', {
            get: function() {
                return this.getAttribute('data-natural-height') || 
                       originalImage.prototype.__lookupGetter__('naturalHeight').call(this) || 20;
            }
        });
        return img;
    };
    window.Image.prototype = originalImage.prototype;
    
    // 2. Fix missing connection info
    if (!navigator.connection) {
        Object.defineProperty(navigator, 'connection', {
            get: () => ({
                effectiveType: '4g',
                rtt: 50,
                downlink: 10,
                saveData: false,
                type: 'wifi',
                addEventListener: function() {},
                removeEventListener: function() {},
            })
        });
    }
    
    // 3. Fix Battery API
    if (!navigator.getBattery) {
        navigator.getBattery = () => Promise.resolve({
            charging: true,
            chargingTime: 0,
            dischargingTime: Infinity,
            level: 1.0,
            addEventListener: function() {},
            removeEventListener: function() {},
        });
    }
    
    // 4. Fix window.outerWidth/outerHeight (0 in headless)
    if (window.outerWidth === 0) {
        Object.defineProperty(window, 'outerWidth', { get: () => window.innerWidth + 15 });
        Object.defineProperty(window, 'outerHeight', { get: () => window.innerHeight + 85 });
    }
    
    // 5. Prevent iframe detection of automation
    const originalContentWindow = Object.getOwnPropertyDescriptor(HTMLIFrameElement.prototype, 'contentWindow');
    Object.defineProperty(HTMLIFrameElement.prototype, 'contentWindow', {
        get: function() {
            const win = originalContentWindow.get.call(this);
            if (win) {
                // Ensure iframes also don't leak webdriver
                try {
                    Object.defineProperty(win.navigator, 'webdriver', { get: () => undefined });
                } catch(e) {}
            }
            return win;
        }
    });
    
    // 6. Fix toString for overridden functions
    // Detection scripts call .toString() on native functions to check for "[native code]"
    const overrides = new Map();
    const originalToString = Function.prototype.toString;
    
    Function.prototype.toString = function() {
        if (overrides.has(this)) {
            return overrides.get(this);
        }
        return originalToString.call(this);
    };
    
    // Make our toString override look native too
    overrides.set(Function.prototype.toString, 'function toString() { [native code] }');
})();
"""
```

### Evading CDP (Chrome DevTools Protocol) Detection

Some sites detect the CDP connection used by Playwright/Puppeteer:

```python
CDP_EVASION = """
(function() {
    // Remove CDP-specific properties
    // Runtime.evaluate adds __proto__ differently
    
    // Fix stacktrace that reveals CDP
    const originalError = Error;
    Error = function(...args) {
        const err = new originalError(...args);
        // Clean stack traces that mention CDP/DevTools
        const originalStack = Object.getOwnPropertyDescriptor(err, 'stack');
        if (originalStack) {
            Object.defineProperty(err, 'stack', {
                get: function() {
                    let stack = originalStack.get ? originalStack.get.call(this) : originalStack.value;
                    if (typeof stack === 'string') {
                        stack = stack.split('\\n').filter(line => 
                            !line.includes('__puppeteer') && 
                            !line.includes('__playwright') &&
                            !line.includes('devtools')
                        ).join('\\n');
                    }
                    return stack;
                }
            });
        }
        return err;
    };
    Error.prototype = originalError.prototype;
    
    // Remove window.callPhantom (PhantomJS indicator sometimes checked)
    delete window.callPhantom;
    delete window._phantom;
    delete window.__nightmare;
})();
"""
```

### Font Fingerprint Spoofing

```python
FONT_SPOOF_SCRIPT = """
(function() {
    // Common Windows fonts to "support"
    const WINDOWS_FONTS = [
        'Arial', 'Arial Black', 'Calibri', 'Cambria', 'Cambria Math',
        'Comic Sans MS', 'Consolas', 'Constantia', 'Corbel', 'Courier New',
        'Georgia', 'Impact', 'Lucida Console', 'Lucida Sans Unicode',
        'Microsoft Sans Serif', 'Palatino Linotype', 'Segoe UI',
        'Segoe UI Symbol', 'Tahoma', 'Times New Roman', 'Trebuchet MS',
        'Verdana', 'Webdings', 'Wingdings',
    ];
    
    // Override font detection via CSS measurement technique
    // This is limited — most font detection uses canvas rendering
    // which our canvas noise handles
})();
"""
```

---

## 1.12 Performance Optimization

### When to Use Browser vs HTTP Client

Not every page needs a full browser. Use this decision tree:

```python
def should_use_browser(url: str, target_info: dict) -> bool:
    """Decide whether to use browser or HTTP client."""
    # Use browser if:
    # 1. JavaScript rendering required
    if target_info.get('requires_js', False):
        return True
    # 2. Complex bot protection (Cloudflare, DataDome)
    if target_info.get('protection') in ['cloudflare', 'datadome', 'perimeterx']:
        return True
    # 3. Need to interact (click, scroll, fill forms)
    if target_info.get('requires_interaction', False):
        return True
    # 4. Need full fingerprint consistency
    if target_info.get('fingerprint_check', False):
        return True
    
    # Use HTTP client (curl_cffi) for everything else
    return False


class AdaptiveScraper:
    """Automatically choose between browser and HTTP scraping."""
    
    def __init__(self, pool: ProxyPool):
        self.pool = pool
        self.stealth = StealthScraper(pool)
        self.domain_config: Dict[str, dict] = {}
    
    async def learn_domain(self, domain: str):
        """Probe a domain to determine what scraping approach to use."""
        # Try HTTP first
        try:
            proxy = await self.pool.get_proxy(domain)
            resp = curl_requests.get(
                f'https://{domain}/',
                impersonate='chrome120',
                proxies={'https': proxy.url},
                timeout=15,
            )
            
            html = resp.text.lower()
            
            config = {
                'requires_js': False,
                'protection': None,
                'requires_interaction': False,
            }
            
            # Check for JS rendering requirements
            if len(html) < 5000 and ('react' in html or 'angular' in html or 'vue' in html):
                config['requires_js'] = True
            
            # Check for bot protection
            if 'cloudflare' in html or '__cf_bm' in str(resp.headers):
                config['protection'] = 'cloudflare'
            elif 'datadome' in html:
                config['protection'] = 'datadome'
            elif 'perimeterx' in html or '_px' in html:
                config['protection'] = 'perimeterx'
            
            self.domain_config[domain] = config
            return config
            
        except Exception as e:
            # If HTTP fails, probably needs browser
            self.domain_config[domain] = {
                'requires_js': True,
                'protection': 'unknown',
                'requires_interaction': False,
            }
            return self.domain_config[domain]
    
    async def scrape(self, url: str) -> dict:
        """Scrape a URL using the optimal approach."""
        from urllib.parse import urlparse
        domain = urlparse(url).netloc
        
        if domain not in self.domain_config:
            await self.learn_domain(domain)
        
        config = self.domain_config[domain]
        
        if should_use_browser(url, config):
            return await self.stealth.scrape_page(url, domain)
        else:
            return await self.stealth.scrape_with_curl(url, domain)
```

---

## 1.13 Real-World Case Studies

### Case Study 1: Scraping an E-commerce Site with Akamai Bot Manager

Akamai Bot Manager uses a combination of TLS fingerprinting, JavaScript challenges, and behavioral analysis. Here's how to approach it:

```python
async def scrape_akamai_protected(url: str, pool: ProxyPool):
    """Strategy for Akamai-protected sites."""
    scraper = StealthScraper(pool, headless=False)  # Non-headless is safer for Akamai
    await scraper.start()
    
    domain = url.split('/')[2]
    page, context, proxy = await scraper.create_session(domain, geo='US-CA')
    
    # Step 1: Visit homepage first (sensor script needs to load)
    homepage = f"https://{domain}/"
    await page.goto(homepage, wait_until='networkidle')
    
    # Step 2: Wait for Akamai sensor to execute
    # Akamai's _abck cookie is generated by their sensor script
    await asyncio.sleep(3)
    
    # Step 3: Simulate human interaction
    # Akamai tracks mouse movements and keystrokes
    await page.mouse.move(random.randint(100, 500), random.randint(100, 400))
    await asyncio.sleep(random.uniform(0.5, 1.5))
    await page.mouse.move(random.randint(200, 600), random.randint(200, 500))
    
    # Step 4: Navigate to target (with valid referer from homepage)
    await page.goto(url, referer=homepage, wait_until='networkidle')
    
    # Step 5: Scroll and interact before extracting
    for _ in range(3):
        await page.mouse.wheel(0, random.randint(200, 500))
        await asyncio.sleep(random.uniform(1, 3))
    
    content = await page.content()
    
    await context.close()
    await scraper.close()
    
    return content
```

### Case Study 2: High-Volume Static Page Scraping

For sites with minimal protection that just need volume:

```python
import asyncio
from curl_cffi import requests as curl_requests

async def high_volume_scrape(urls: List[str], pool: ProxyPool, max_concurrent: int = 10):
    """High-volume scraping using curl_cffi with proxy rotation."""
    semaphore = asyncio.Semaphore(max_concurrent)
    results = []
    
    async def fetch_one(url: str):
        async with semaphore:
            domain = url.split('/')[2]
            proxy = await pool.get_proxy(domain)
            
            delay = HumanDelay.between_pages()
            await asyncio.sleep(delay * 0.3)  # Reduced delay for high volume
            
            try:
                response = curl_requests.get(
                    url,
                    impersonate='chrome120',
                    proxies={'https': proxy.url},
                    timeout=20,
                )
                
                if response.status_code == 200:
                    await pool.report_success(proxy)
                    return {'url': url, 'html': response.text, 'status': 200}
                else:
                    await pool.report_failure(proxy, domain, is_ban=(response.status_code == 403))
                    return {'url': url, 'html': None, 'status': response.status_code}
                    
            except Exception as e:
                await pool.report_failure(proxy, domain)
                return {'url': url, 'html': None, 'error': str(e)}
    
    tasks = [fetch_one(url) for url in urls]
    results = await asyncio.gather(*tasks, return_exceptions=True)
    
    success = sum(1 for r in results if isinstance(r, dict) and r.get('status') == 200)
    logger.info(f"Scraped {success}/{len(urls)} successfully")
    
    return results
```

---

## Summary

Anti-detection in web scraping requires a multi-layered approach:

1. **TLS fingerprinting** (JA3/JA4): Use `curl_cffi` or `tls-client` to match browser TLS signatures
2. **Browser fingerprinting**: Spoof canvas, WebGL, audio, fonts, and navigator properties consistently
3. **Geo-consistency**: Align timezone, language, and locale with proxy IP location
4. **Behavioral mimicry**: Randomize delays, mouse movements, and navigation patterns
5. **Proxy management**: Rotate residential/mobile proxies with smart cooldowns and health tracking
6. **Adaptive approach**: Use lightweight HTTP clients when possible, full browsers only when needed

The key principle is **consistency**: every signal your scraper emits must tell the same story — that of a real human using a real browser on a real computer. One inconsistency is all a detection system needs.

In the next chapter, we'll dive into CAPTCHA solving and bot detection bypass — what happens when despite your best stealth efforts, the site challenges you directly.
