# 20. Mobile Design QA


Mobile design quality assurance ensures that applications provide excellent experiences on smartphones and tablets. Mobile devices dominate web traffic—over 60% globally—making mobile QA critical, not optional. Mobile QA goes far beyond testing at small viewports; it encompasses touch interactions, device-specific constraints, platform differences between iOS and Android, network variability, hardware limitations, and unique usage contexts. This comprehensive section covers every aspect of mobile design QA.

### 20.1 Mobile Device Landscape

Understanding the diversity of mobile devices guides testing strategy.

**Device Fragmentation**: Mobile devices vary dramatically in screen size, resolution, processor, memory, operating system version, browser version, and capabilities. Screen sizes range from compact phones (iPhone SE at 4.7" / 375×667px) to phablets (iPhone 15 Pro Max at 6.7" / 430×932px) to tablets (iPad Pro at 12.9" / 1024×1366px). Pixel density varies from ~300 PPI on older devices to ~460 PPI on flagships. Processors range from powerful (Apple A17 Pro, Snapdragon 8 Gen 3) to budget (Snapdragon 4-series, older chips). Memory varies from 2GB on budget phones to 12GB+ on flagships. Testing must cover representative devices across this spectrum.

**iOS Device Considerations**: Apple's controlled ecosystem provides consistency but still has variation. Current iPhone sizes: iPhone SE (4.7", 375×667 @2x), iPhone 13/14 Mini (5.4", 375×812 @3x, discontinued but still in use), iPhone 13/14/15 (6.1", 390×844 @3x), iPhone 13/14/15 Pro (6.1", 393×852 @3x), and iPhone 13/14/15 Pro Max (6.7", 430×932 @3x). iPad sizes: iPad Mini (8.3", 744×1133 @2x), iPad / iPad Air (10.9", 820×1180 @2x), iPad Pro 11" (11", 834×1194 @2x), and iPad Pro 12.9" (12.9", 1024×1366 @2x). iOS version adoption is high—within months, 70%+ of users update to latest iOS. Safari is the only real browser engine on iOS (even "Chrome" and "Firefox" use WebKit). Testing priorities: test across different iPhone sizes (particularly notched vs non-notched, different safe areas), test iPad separately (tablet layout triggers, different interactions), test current iOS and one version back (covers ~90%+ users), and test Safari exclusively (other browsers are WebKit-based).

**Android Device Considerations**: Android's open ecosystem creates massive fragmentation. Screen sizes range from compact (~5") to extra-large (7"+). Resolutions vary: HD (720×1280), Full HD (1080×1920), Quad HD (1440×2560), and various aspect ratios (16:9, 18:9, 19.5:9, 20:9, 21:9). Manufacturers customize Android: Samsung One UI, Xiaomi MIUI, OnePlus OxygenOS, each with visual and functional differences. Android version fragmentation is significant—even years after release, older versions remain popular. Browser options include Chrome (most common), Samsung Internet (prevalent on Samsung devices), Firefox, Opera, and others. Testing priorities: test on multiple manufacturers (Samsung, Google Pixel, OnePlus, Xiaomi), test flagship and budget devices (performance varies dramatically), test Android versions based on analytics (typically Android 10+), test Chrome primarily but spot-check Samsung Internet, and test various screen sizes and aspect ratios.

**Tablet-Specific Considerations**: Tablets are neither phones nor desktops. iPad users expect tablet-optimized layouts, not blown-up phone layouts or squished desktop layouts. Android tablets are less common but still represent significant usage. Tablet considerations: larger screen enables multi-column layouts, touch targets remain necessary (no mouse unless external accessory), landscape orientation is more common than on phones, split-screen multitasking (iPad Split View, Android split-screen) requires responsive adaptation, and desktop features might be expected (file upload, complex interactions). Testing validates tablet-specific layouts exist and work well, touch interactions function properly, landscape and portrait both work, split-screen scenarios are handled, and tablets don't just receive phone or desktop layouts inappropriately.

**Foldable Device Considerations**: Foldable phones (Samsung Galaxy Z Fold, Google Pixel Fold, others) introduce new challenges. Foldables have multiple screen configurations: closed (cover screen, phone-sized), unfolded (tablet-sized square-ish screen), and flex mode (partially folded, split interface). Screen aspect ratios are unusual (particularly square-ish unfolded screens). Apps must adapt as device unfolds/refolds during use. Testing foldables validates layouts work on cover screen, layouts adapt when unfolded (often triggering tablet layout), layout transitions smoothly during folding, flex mode is handled (if supported), and no content is lost during transitions.

### 20.2 Mobile Viewports and Breakpoints

Mobile viewports are more complex than simple width checks.

**Common Mobile Viewport Sizes**: Understanding prevalent sizes guides breakpoint decisions. Common portrait widths: 375px (iPhone SE, iPhone X/11/12/13 Mini), 390px (iPhone 13/14/15), 393px (iPhone 13/14/15 Pro), 412px (Google Pixel, many Android phones), 360px (Samsung Galaxy, common Android), 414px (iPhone Plus models), 430px (iPhone 14/15 Pro Max), and 768px (iPad portrait). Testing should cover at least 360px (common Android), 375-390px (common iPhone), 414-430px (larger phones), and 768px (tablet). Testing at only one or two sizes misses many devices.

**Viewport Meta Tag**: The viewport meta tag is essential for mobile-optimized sites. Proper viewport tag:

```html
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
```

`width=device-width`: sets viewport width to device width (enables responsive design). `initial-scale=1`: sets initial zoom level to 100% (no default zoom). `viewport-fit=cover`: extends content into safe areas on notched devices. Avoid: `user-scalable=no` (prevents zooming, accessibility issue), `maximum-scale=1` (prevents zooming, accessibility issue), and `minimum-scale` (rarely needed). Testing validates viewport tag is present and correct, viewport width matches device width, initial zoom is correct (no inadvertent zoom), users can zoom (accessibility requirement), and safe area handling works on notched devices.

**Breakpoint Strategy for Mobile**: Effective breakpoints adapt to content, not specific devices. Common breakpoint structure: mobile (<600px or <768px), tablet (600-900px or 768-1024px), desktop (>900px or >1024px), and large desktop (>1400px or >1920px). However, content-driven breakpoints are better—set breakpoints where layout breaks, not at arbitrary device widths. Consider: mobile-first approach (base styles for mobile, enhance for larger screens), major layout shifts at breakpoints (single column → two column → three column), minor adjustments between breakpoints (fluid typography, flexible spacing), and avoiding too many breakpoints (3-5 is usually sufficient). Testing validates layouts work at all breakpoints, transitions between breakpoints are smooth, layouts work between breakpoints (not just at exact breakpoint values), content remains readable and accessible at all sizes, and breakpoints are appropriate for content (not just device sizes).

**Safe Area Insets for Notched Devices**: iPhone X and newer have notches/Dynamic Island requiring safe area consideration. CSS environment variables provide safe area insets:

```css
/* Support notched devices */
.header {
  padding-top: env(safe-area-inset-top);
  padding-left: env(safe-area-inset-left);
  padding-right: env(safe-area-inset-right);
}

.footer {
  padding-bottom: env(safe-area-inset-bottom);
}

/* Fallback for non-notched devices */
.header {
  padding-top: 20px;
  padding-top: env(safe-area-inset-top);
}
```

Safe area insets are non-zero only on notched devices in landscape orientation (horizontal insets) or with home indicator (bottom inset). Testing validates content isn't hidden behind notches/Dynamic Island, safe area insets are applied correctly, fallback padding works on non-notched devices, landscape orientation is handled correctly (horizontal insets), and footer buttons aren't obscured by home indicator area.

**Responsive Typography on Mobile**: Text must be readable without zooming. Minimum font sizes: body text should be 16px minimum (smaller triggers zoom on iOS), small text (captions, labels) 14px minimum, large headings can scale responsively, and line height should be 1.4-1.6 for readability. Responsive typography techniques:

```css
/* Fluid typography using clamp() */
body {
  font-size: clamp(16px, 4vw, 18px);
  line-height: 1.5;
}

h1 {
  font-size: clamp(28px, 8vw, 48px);
}

/* Viewport-based scaling */
h2 {
  font-size: calc(20px + 1vw);
}

/* Media query adjustments */
@media (max-width: 600px) {
  p {
    font-size: 16px;
    line-height: 1.6;
  }
}
```

Testing validates text is readable without zooming, font sizes are appropriate at all viewport widths, line heights provide good readability, line lengths are comfortable (45-75 characters), and users can zoom text if needed (accessibility requirement).

**Responsive Images**: Images must adapt to viewport and bandwidth. Responsive image techniques:

```html
<!-- Responsive image with srcset -->
<img 
  src="image-800.jpg"
  srcset="image-400.jpg 400w,
          image-800.jpg 800w,
          image-1200.jpg 1200w,
          image-1600.jpg 1600w"
  sizes="(max-width: 600px) 100vw,
         (max-width: 1200px) 50vw,
         800px"
  alt="Description"
/>

<!-- Art direction with picture -->
<picture>
  <source media="(max-width: 600px)" srcset="image-mobile.jpg">
  <source media="(max-width: 1200px)" srcset="image-tablet.jpg">
  <img src="image-desktop.jpg" alt="Description">
</picture>

<!-- WebP with fallback -->
<picture>
  <source srcset="image.webp" type="image/webp">
  <img src="image.jpg" alt="Description">
</picture>
```

Testing validates images load correctly on mobile, appropriate image size loads (not desktop-sized images on mobile), art direction works (different crops for mobile vs desktop), modern formats (WebP, AVIF) load with fallbacks, lazy loading works (intersection observer or native loading="lazy"), and image quality is good (not over-compressed).

### 20.3 Touch Interactions and Gestures

Mobile relies on touch; interactions must be designed for fingers, not mouse pointers.

**Touch Target Sizes**: Touch targets must be large enough to tap accurately. WCAG 2.2 Level AA requires 24×24px minimum (CSS pixels), Apple HIG recommends 44×44pt minimum (~44×44px), Android Material Design recommends 48×48dp minimum (~48×48px), and practical recommendation is 44×44px minimum for small targets, 48×48px or larger for primary actions. Testing validates all interactive elements meet minimum size, touch targets have adequate spacing (8px minimum between targets), small text links are enlarged for mobile (either larger tap area or converted to buttons), icon buttons are adequately sized, and form controls are large enough (inputs, checkboxes, radio buttons).

**Tap vs Click Events**: Touch events differ from mouse events. Event sequence: touch starts with touchstart, moves with touchmove, ends with touchend, click event fires ~300ms after touchend (historical delay, mostly eliminated in modern browsers). Use pointer events for unified handling:

```javascript
// Pointer events work for mouse and touch
element.addEventListener('pointerdown', handleDown);
element.addEventListener('pointermove', handleMove);
element.addEventListener('pointerup', handleUp);

// Or use click for simple interactions (works for both)
button.addEventListener('click', handleClick);

// Avoid mouse-specific events on mobile
// mouseenter, mouseleave, mouseover don't work with touch
```

Testing validates click events fire correctly on touch, touch interactions don't have 300ms delay (modern browsers eliminate this), pointer events work for both mouse and touch, hover-dependent interactions have touch alternatives, and long-press interactions work appropriately.

**Hover States on Mobile**: Hover doesn't exist on touch devices. Strategies: provide touch alternatives to hover (tap to reveal, explicit toggle button), use :active state for touch feedback, use focus styles for focused elements, avoid critical functionality in hover-only interactions, and accept that some hover effects simply won't work on touch. CSS for touch-appropriate hover:

```css
/* Hover only on devices that support hover */
@media (hover: hover) and (pointer: fine) {
  .button:hover {
    background: #blue;
  }
}

/* Touch feedback with :active */
.button:active {
  transform: scale(0.98);
  opacity: 0.8;
}

/* Focus styles for keyboard and touch focus */
.button:focus-visible {
  outline: 2px solid blue;
}
```

Testing validates hover effects work on desktop/mouse, hover effects don't create issues on touch (sticky hover states), touch feedback is provided (:active states), focus styles work on mobile when navigating with external keyboard, and critical functionality doesn't require hover.

**Gestures and Swipe Interactions**: Mobile users expect gesture support. Common gestures: swipe (horizontal or vertical scrolling, dismiss actions, carousel navigation), pinch-to-zoom (expected for images, maps, allowed for accessibility), pull-to-refresh (common pattern, but can conflict with scrolling), long-press (context menus, reordering), two-finger scroll (within scrollable areas), and double-tap (zoom, less common in web). Implementing swipe gestures:

```javascript
// Basic swipe detection
let touchStartX = 0;
let touchEndX = 0;

element.addEventListener('touchstart', (e) => {
  touchStartX = e.changedTouches[0].screenX;
});

element.addEventListener('touchend', (e) => {
  touchEndX = e.changedTouches[0].screenX;
  handleSwipe();
});

function handleSwipe() {
  if (touchEndX < touchStartX - 50) {
    // Swipe left
  }
  if (touchEndX > touchStartX + 50) {
    // Swipe right
  }
}

// Or use a library like Hammer.js
const hammer = new Hammer(element);
hammer.on('swipeleft', () => {
  // Handle swipe left
});
```

Testing validates swipe gestures work smoothly, gestures don't conflict with scrolling, pinch-to-zoom works on images/maps and is allowed generally (accessibility), pull-to-refresh doesn't interfere with normal scrolling, long-press actions are discoverable, and gestures work consistently across iOS and Android.

**Preventing Unwanted Zoom**: Some interactions should prevent zoom. Form inputs with font-size <16px trigger zoom on iOS (solution: use 16px font-size). Pinch-to-zoom should generally be allowed (accessibility requirement). Prevent zoom only in specific interactions:

```javascript
// Prevent zoom during map interaction
map.addEventListener('touchmove', (e) => {
  if (e.touches.length > 1) {
    e.preventDefault(); // Prevents pinch-zoom during map pan
  }
}, { passive: false });

// Prevent double-tap zoom on specific elements
button.addEventListener('touchend', (e) => {
  e.preventDefault();
  // Handle button action
});
```

Testing validates zoom is allowed generally (don't disable in viewport meta), form input zoom is prevented by using 16px font-size, specific interactions can prevent zoom where appropriate (maps, games), double-tap zoom is prevented on buttons and interactive elements, and users can still zoom when needed (accessibility).

### 20.4 Mobile-Specific Layout Issues

Mobile layouts face unique challenges beyond simply scaling desktop layouts.

**Fixed Positioning on Mobile**: Fixed elements behave differently on mobile. Address bar shows/hides on scroll, affecting viewport height and fixed element positioning. Safari iOS address bar causes significant viewport height changes. Solutions:

```css
/* Fixed header accounting for safe area */
.header {
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  padding-top: env(safe-area-inset-top);
  height: 60px;
  height: calc(60px + env(safe-area-inset-top));
}

/* Fixed footer with safe area */
.footer {
  position: fixed;
  bottom: 0;
  left: 0;
  right: 0;
  padding-bottom: env(safe-area-inset-bottom);
  height: 60px;
  height: calc(60px + env(safe-area-inset-bottom));
}

/* Full-height content with fixed header/footer */
.content {
  padding-top: calc(60px + env(safe-area-inset-top));
  padding-bottom: calc(60px + env(safe-area-inset-bottom));
  min-height: 100vh;
}
```

Testing validates fixed headers stay at top when scrolling, fixed footers stay at bottom, fixed elements don't overlap content, safe areas are respected on notched devices, address bar appearance/disappearance doesn't break layout, and fixed elements don't cause scrolling issues.

**100vh Height Issues**: 100vh is problematic on mobile because it includes address bar area. When address bar hides, content extends beyond viewport. Solutions:

```css
/* Use dvh (dynamic viewport height) in modern browsers */
.full-height {
  height: 100dvh;
}

/* Fallback for older browsers */
.full-height {
  height: 100vh;
  height: 100dvh;
}

/* Or use JavaScript to calculate actual viewport height */
.full-height {
  height: 100vh;
}
```

```javascript
// JavaScript solution for older browsers
function setVH() {
  let vh = window.innerHeight * 0.01;
  document.documentElement.style.setProperty('--vh', `${vh}px`);
}

window.addEventListener('resize', setVH);
setVH();
```

```css
/* Use custom property */
.full-height {
  height: calc(var(--vh, 1vh) * 100);
}
```

Testing validates 100vh doesn't cause scrolling issues, content fits within visible viewport, dvh is used with vh fallback, JavaScript solution works if used, and layout handles address bar show/hide gracefully.

**Horizontal Scrolling Prevention**: Unwanted horizontal scroll is common mobile issue. Causes include elements wider than viewport, fixed-width elements, negative margins pushing content outside viewport, absolutely positioned elements positioned outside viewport, images without max-width, tables without responsive handling, and unbroken long strings. Prevention:

```css
/* Prevent horizontal scroll */
body {
  overflow-x: hidden;
}

/* Ensure all content fits */
* {
  max-width: 100%;
  box-sizing: border-box;
}

/* Responsive images */
img {
  max-width: 100%;
  height: auto;
}

/* Word breaking for long strings */
.text {
  word-wrap: break-word;
  overflow-wrap: break-word;
}

/* Responsive tables */
.table-container {
  overflow-x: auto;
  -webkit-overflow-scrolling: touch;
}
```

Testing validates no horizontal scrolling occurs (swipe left/right shouldn't scroll), all content fits within viewport, images don't cause overflow, tables are scrollable or responsive, long strings break appropriately, and fixed-width elements adapt to viewport.

**Content Reflow at Mobile Sizes**: Desktop layouts must reflow appropriately for mobile. Common reflow patterns: multi-column → single column, horizontal navigation → hamburger menu, side-by-side → stacked, grid layouts → fewer columns or single column, and large images → smaller/different crop. Testing validates all content reflows appropriately, no content is hidden or inaccessible, reading order remains logical, images are appropriately sized/cropped, and navigation is accessible (hamburger menu works, all items are accessible).

**Modals and Overlays on Mobile**: Modals must work well on small screens. Mobile modal considerations: modals should be full-screen or nearly full-screen, provide clear close action (X button, back gesture), trap focus within modal, prevent body scroll when open, work in landscape orientation, stack properly if multiple modals, and handle keyboard appearance (iOS keyboard reduces viewport). Mobile modal CSS:

```css
.modal {
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background: white;
  z-index: 1000;
  overflow-y: auto;
  -webkit-overflow-scrolling: touch;
}

@media (min-width: 768px) {
  .modal {
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
    width: 600px;
    max-height: 90vh;
    border-radius: 8px;
  }
}
```

Testing validates modals are sized appropriately for mobile, close actions are obvious and work, focus is trapped in modal, body scroll is prevented, landscape orientation works, keyboard doesn't break layout, and modals work well on small screens.

### 20.5 iOS vs Android Differences

Platform differences require platform-specific testing and sometimes platform-specific solutions.

**System UI Differences**: iOS and Android have different system UI conventions. iOS uses bottom tab bars, Android uses bottom navigation or top tabs. iOS uses top navigation bars with back button on left, Android uses top app bars with hamburger or back on left. iOS uses action sheets (bottom sheet), Android uses dialogs or bottom sheets. iOS uses SF Symbols, Android uses Material Icons. iOS scroll bounces by default, Android scroll doesn't bounce. Respecting platform conventions improves UX, but web apps often choose one consistent approach. Testing validates chosen navigation pattern works on both platforms, back navigation works appropriately, UI doesn't look broken on either platform, icons are clear on both platforms, and scroll behavior is acceptable.

**Font Rendering Differences**: Fonts render differently on iOS vs Android. iOS typically renders fonts slightly lighter/thinner. Android font rendering varies by manufacturer and Android version. System fonts differ: iOS uses San Francisco, Android uses Roboto. Using system font stack ensures native appearance:

```css
body {
  font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
}
```

Testing validates fonts are readable on both platforms, font weights work well on both (not too thin on iOS, not too heavy on Android), system fonts provide native feel, and custom web fonts render acceptably on both.

**Browser Differences**: iOS only allows WebKit (Safari engine). Android allows multiple browser engines. iOS Safari quirks: 100vh includes address bar, fixed positioning has quirks, date inputs are limited, backdrop-filter requires prefix, and some CSS features lag. Android Chrome: supports most modern CSS, PWA features are more robust, form controls are different, and performance can vary on budget devices. Testing validates features work in both Safari iOS and Chrome Android, fallbacks exist for Safari limitations, Android Chrome features are leveraged where beneficial, and budget Android device performance is acceptable.

**Form Control Styling**: Form controls look very different on iOS vs Android. iOS uses rounded corners, specific colors, distinct styles. Android Material Design uses underlines, different colors, animation effects. Native controls are hard to style consistently. Options: accept platform differences (native controls look native), custom-style all controls (requires significant CSS, accessibility considerations), or use third-party component library (provides consistency but increases bundle size). Testing validates form controls are usable on both platforms, custom styling works on both or native controls are accepted, accessibility is maintained (labels, ARIA), focus states are clear, and validation errors are obvious.

**Keyboard Differences**: Mobile keyboards differ significantly. iOS keyboards: keyboard type changes based on input type (numeric, email, tel, URL), keyboard has autocorrect and suggestions, Return key label changes based on context (Go, Search, Done), and keyboard appearance is animated. Android keyboards: keyboard type changes based on input type, keyboards vary by manufacturer and user-installed keyboards (Gboard, SwiftKey, etc.), Return key often shows search icon for search inputs, and keyboard appearance is animated. Proper input types trigger appropriate keyboards:

```html
<input type="text" inputmode="text">
<input type="email" inputmode="email">
<input type="tel" inputmode="tel">
<input type="number" inputmode="numeric">
<input type="url" inputmode="url">
<input type="search" inputmode="search">
```

Testing validates appropriate keyboards appear for input types (email keyboard for email, numeric for phone numbers), keyboards don't break layout, keyboard appearance doesn't hide focused input (viewport adjusts or page scrolls), Return key behavior is appropriate, and autocorrect/autocomplete work reasonably.

**Notification Differences**: Platform notification systems differ. iOS notifications: appear at top, require user permission, have specific format, support actions (buttons), and appear in Notification Center. Android notifications: appear as cards, require user permission (Android 13+), have flexible format, support actions and expanded content, and appear in notification shade. Web notifications:

```javascript
// Request notification permission
if ('Notification' in window) {
  Notification.requestPermission().then(permission => {
    if (permission === 'granted') {
      new Notification('Title', {
        body: 'Message',
        icon: '/icon.png',
      });
    }
  });
}
```

Testing validates notification permission requests work on both platforms, notifications appear correctly on both, notification content is appropriate, actions work if implemented, and notifications aren't over-used (user experience, not technical issue).

### 20.6 Mobile Performance Optimization

Mobile devices have limited resources; performance optimization is critical for mobile QA.

**Network Performance**: Mobile networks are slower and less reliable than Wi-Fi. Network conditions: 4G LTE provides good speeds (15-30 Mbps typically) but variable latency. 3G is much slower (1-5 Mbps) and still used in some areas. Poor signal dramatically degrades speeds. Testing validates site loads reasonably on 3G (use Chrome DevTools throttling to simulate), critical content loads first (above-fold content prioritized), images are compressed appropriately (serve modern formats like WebP/AVIF), lazy loading is implemented for below-fold images, JavaScript bundles are optimized (code-splitting, tree-shaking), and offline/poor network conditions are handled gracefully.

**Reducing Page Weight**: Every byte matters on mobile. Optimization strategies: compress images (WebP, AVIF, proper JPEG/PNG compression), use responsive images (serve smaller images to mobile), lazy load images and iframes, minify CSS and JavaScript, remove unused CSS and JS (PurgeCSS, tree-shaking), use code-splitting (load only needed code), compress text resources (gzip, Brotli), limit web fonts (use system fonts or minimal font weights), and defer non-critical resources. Testing validates total page weight is reasonable (<1MB for initial load ideally, <3MB acceptable), images are optimized (measure individual image sizes), JavaScript bundle size is reasonable (track with Bundle Analyzer), CSS is minified and unused CSS is removed, and compression is enabled (check response headers).

**JavaScript Performance on Mobile**: Mobile CPUs are less powerful than desktop. JavaScript optimization: minimize main thread work (offload to Web Workers where possible), debounce/throttle scroll and resize handlers, use requestAnimationFrame for animations, avoid layout thrashing (batch DOM reads and writes), lazy load non-critical JavaScript, use efficient selectors and DOM queries, avoid blocking long tasks (break into smaller chunks), and minimize third-party scripts. Testing validates JavaScript execution doesn't cause jank, interactions are responsive (measure Time to Interactive), animations run smoothly (60fps), scroll performance is smooth, and budget devices perform acceptably (test on lower-end Android devices).

**Rendering Performance**: Painting and layout can be expensive on mobile. Optimization strategies: use CSS transforms for animations (GPU-accelerated), avoid animating layout properties (width, height, top, left), use will-change sparingly for elements that will animate, minimize layout recalculations (avoid force layout/reflow), reduce number of DOM elements, simplify CSS selectors, use contain property to limit layout scope, and avoid expensive visual effects on mobile (shadows, filters, blurs). Testing validates rendering performance is smooth (use DevTools Performance panel), Layout Shift is minimal (CLS metric), paint times are reasonable, animations hit 60fps, and budget devices don't have severe performance degradation.

**Battery Consumption**: Mobile users care about battery life. Battery-draining factors: constant animations, background JavaScript execution, frequent network requests, GPS/geolocation tracking, Web Workers running continuously, and camera/media usage. Optimization: pause animations when page is hidden (Page Visibility API), throttle or stop background processes, cache data to reduce network requests, use geolocation sparingly, clean up resources when not needed, and respect low-power mode preferences. Testing validates battery drain is reasonable (subjective, requires real device testing), animations pause when page is hidden, background processes are minimal, and app respects battery-saving settings.

**Memory Limitations**: Mobile devices have limited memory. Memory optimization: clean up event listeners when elements are removed, avoid memory leaks (detach observers, cancel requests), limit cached data, optimize images (reduce memory usage), avoid creating excessive DOM elements, use lazy loading to defer loading, and monitor memory usage. Testing validates memory usage is reasonable (use DevTools Memory profiler), memory leaks don't exist (test repeated navigation), app doesn't crash on memory-constrained devices, and memory usage doesn't grow unbounded during use.

### 20.7 PWA Design Considerations

Progressive Web Apps provide app-like experiences on mobile.

**Installability and App Icons**: PWAs can be installed to home screen. Requirements: HTTPS (required for PWA), valid manifest.json, service worker registered, sufficient app icons. Manifest.json:

```json
{
  "name": "My App",
  "short_name": "App",
  "start_url": "/",
  "display": "standalone",
  "background_color": "#ffffff",
  "theme_color": "#000000",
  "icons": [
    {
      "src": "/icon-192.png",
      "sizes": "192x192",
      "type": "image/png"
    },
    {
      "src": "/icon-512.png",
      "sizes": "512x512",
      "type": "image/png"
    }
  ]
}
```

Testing validates manifest is valid (use Chrome DevTools Application panel), icons are provided in required sizes, install prompt appears appropriately, app installs successfully on iOS and Android, app launches correctly after install, and splash screen appears on launch (Android).

**Standalone Display Mode**: PWAs can run without browser UI. Display modes: standalone (no browser UI, looks like native app), fullscreen (no system UI), minimal-ui (minimal browser UI), and browser (normal browser). CSS for standalone:

```css
/* Styles specific to standalone mode */
@media (display-mode: standalone) {
  .install-button {
    display: none;
  }
  
  .app-header {
    padding-top: env(safe-area-inset-top);
  }
}
```

JavaScript detection:

```javascript
if (window.matchMedia('(display-mode: standalone)').matches || window.navigator.standalone) {
  // Running as PWA
}
```

Testing validates standalone mode works correctly, safe areas are respected in standalone, navigation works without browser back button, and UI adapts appropriately to standalone context.

**Offline Functionality**: Service workers enable offline operation. Offline strategies: cache-first (serve from cache, fallback to network), network-first (try network, fallback to cache), stale-while-revalidate (serve cache immediately, update in background), and offline page (show custom offline page when network unavailable). Testing validates offline functionality works (test with DevTools offline mode), critical content is cached, offline page appears when appropriate, cache updates correctly, and cache doesn't grow unbounded (implement cache expiration).

**App-Like Navigation**: PWAs should feel like native apps. Considerations: provide in-app navigation (don't rely on browser back button in standalone mode), implement gesture navigation where appropriate (swipe back), handle deep linking correctly (direct navigation to specific screens), maintain navigation state, implement loading states and transitions, and provide clear back navigation. Testing validates navigation works in standalone mode, deep links open correctly, back navigation functions properly, navigation state persists appropriately, and transitions feel smooth and app-like.

**Push Notifications**: PWAs can send push notifications. Implementation requires user permission, push subscription, server implementation to send pushes, and service worker to handle pushes. Testing validates permission requests are timely and contextual, subscriptions work on iOS and Android, notifications appear correctly, notification actions work, and notifications aren't overly aggressive (user experience).

### 20.8 Mobile Accessibility

Mobile accessibility ensures users with disabilities can use mobile applications effectively.

**Touch Target Sizes**: As discussed earlier, minimum 44×44px or 48×48px touch targets. Testing validates all interactive elements meet minimum sizes, spacing between targets is adequate, targets don't overlap, and small links are made tappable (padding, converted to buttons).

**Screen Reader Support**: Mobile screen readers work differently than desktop. iOS VoiceOver: activated with triple-click home button or side button, uses gestures (swipe right to move forward, swipe left to move back, double-tap to activate), speaks element roles and states, and respects ARIA attributes. Android TalkBack: activated in accessibility settings, uses gestures (similar to VoiceOver), speaks element roles and states, and respects ARIA attributes. Testing validates content is announced correctly on VoiceOver and TalkBack, navigation works with swipe gestures, interactive elements are activatable with double-tap, forms are usable, ARIA attributes function correctly, dynamic content updates are announced, and images have alt text.

**Zoom and Text Resizing**: Users must be able to zoom and resize text. Requirements: allow pinch-to-zoom (don't use user-scalable=no), support text-only zoom (iOS Settings > Display & Brightness > Text Size), layouts don't break at 200% zoom (WCAG requirement), and text remains readable when enlarged. Testing validates pinch-to-zoom works, text resizing in iOS settings affects app text, layouts remain functional at 200% zoom, and no content is lost when zoomed/enlarged.

**Color Contrast**: Same requirements as desktop—4.5:1 for normal text, 3:1 for large text. Testing validates contrast meets requirements on mobile screens (can differ from desktop due to screen quality, brightness), contrast is tested in various lighting conditions (bright sunlight, low light), and reduced transparency settings are respected (iOS Reduce Transparency setting).

**Motion and Animation**: Respect prefers-reduced-motion. Users with vestibular disorders or motion sensitivity need reduced motion. CSS:

```css
@media (prefers-reduced-motion: reduce) {
  * {
    animation-duration: 0.01ms !important;
    animation-iteration-count: 1 !important;
    transition-duration: 0.01ms !important;
  }
}
```

Testing validates prefers-reduced-motion is respected, animations are disabled or significantly reduced, essential motion is maintained (loading indicators), and functionality doesn't depend on motion.

**Keyboard and External Input Devices**: Mobile devices can use external keyboards, mice, and trackpads. Testing validates keyboard navigation works on mobile (tab order, focus indicators), external mouse/trackpad interactions work (hover, click), focus indicators are visible with external keyboard, and keyboard shortcuts don't conflict with system shortcuts.

### 20.9 Mobile-Specific Testing Checklists

Comprehensive checklists ensure thorough mobile QA.

**Essential Mobile Device Testing**:
☐ Test on actual iOS devices (iPhone with notch, iPhone SE without notch, iPad)
☐ Test on actual Android devices (Samsung, Google Pixel, budget device)
☐ Test on various screen sizes (small phone 360px, standard 390px, large 430px, tablet 768px)
☐ Test in portrait and landscape orientations
☐ Test with slow network (3G simulation)
☐ Test with poor network (flaky connection)
☐ Test completely offline
☐ Test on low-end/budget devices
☐ Test with external keyboard
☐ Test with VoiceOver (iOS) and TalkBack (Android)

**Touch Interaction Testing**:
☐ All interactive elements meet minimum 44×44px touch target size
☐ Touch targets have adequate spacing (8px minimum)
☐ Tap events work correctly
☐ No 300ms delay on taps
☐ Active states provide touch feedback
☐ Swipe gestures work smoothly
☐ Pinch-to-zoom works where appropriate
☐ Long-press actions work
☐ Gestures don't conflict with system gestures
☐ Hover-dependent features have touch alternatives

**Layout and Visual Testing**:
☐ No horizontal scrolling
☐ Content reflows appropriately at mobile sizes
☐ Fixed headers/footers work correctly
☐ Safe areas respected on notched devices
☐ 100vh doesn't cause issues
☐ Modals/overlays work well on small screens
☐ Images are appropriately sized
☐ Text is readable (16px minimum body text)
☐ Line lengths are comfortable
☐ Spacing is appropriate for mobile

**Performance Testing**:
☐ Page load time is reasonable on 3G
☐ Time to Interactive is acceptable
☐ Animations run at 60fps
☐ Scrolling is smooth
☐ No significant battery drain
☐ Memory usage is reasonable
☐ Budget devices perform acceptably
☐ Total page weight is reasonable

**PWA Testing** (if applicable):
☐ Manifest.json is valid
☐ App installs successfully
☐ App launches correctly
☐ Standalone mode works properly
☐ Offline functionality works
☐ Service worker registers correctly
☐ Push notifications work
☐ App icon displays correctly

**Accessibility Testing**:
☐ VoiceOver announces content correctly
☐ TalkBack announces content correctly
☐ Pinch-to-zoom is enabled
☐ Text resizing works (iOS)
☐ Color contrast meets requirements
☐ Prefers-reduced-motion is respected
☐ External keyboard navigation works
☐ Focus indicators are visible

---
