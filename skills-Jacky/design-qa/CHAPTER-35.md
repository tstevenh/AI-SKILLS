# 32. Design QA for Progressive Web Apps (PWAs)


Progressive Web Apps blur the line between web and native applications, requiring specialized design QA to ensure app-like experiences, offline functionality, and platform integration work flawlessly.

### 32.1 App Shell and Loading Experience

The app shell architecture provides instant loading for repeat visits, requiring careful testing of the initial experience.

**App Shell Design**: The app shell is the minimal HTML, CSS, and JavaScript needed for the UI skeleton. Test that app shell loads instantly on repeat visits (cached by service worker), app shell provides meaningful layout (not just blank screen), app shell includes navigation structure, app shell includes loading indicators for dynamic content, app shell visual design matches full application, app shell is lightweight (minimal bytes), app shell works offline (fully cached), and app shell doesn't cause layout shift when content loads.

**Splash Screens**: PWAs installed to home screens can show splash screens. Verify that splash screen appears when launching app from home screen (iOS, Android), splash screen uses theme colors appropriately, splash screen shows app icon and name, splash screen duration is appropriate (not too long), splash screen transitions smoothly to app, splash screen works on both iOS and Android, and splash screen design matches brand and app design.

**First Paint and First Contentful Paint**: Initial perceived performance is critical. Test that first paint happens within 1 second (ideally), first contentful paint shows meaningful content quickly, loading strategies optimize perceived performance (show skeleton, then content), critical CSS is inlined or loaded immediately, render-blocking resources are minimized, fonts load efficiently (font-display: swap or fallback), and performance budget is maintained across updates.

**Loading Indicators and Skeleton Screens**: While content loads, users need feedback. Verify that skeleton screens match layout of loaded content, skeleton screens don't cause layout shift when content appears, loading spinners appear for slow operations, loading indicators are accessible (announced to screen readers), loading indicators don't block UI unnecessarily, loading states handle errors gracefully (transition to error state), and progressive loading works (show partial content as it becomes available).

### 32.2 Offline Functionality

PWAs must provide graceful offline experiences.

**Offline Page**: When content isn't cached, offline page provides fallback. Test that offline page appears when network unavailable and content not cached, offline page clearly communicates offline status, offline page provides helpful information (what's available offline, when to retry), offline page design matches app shell, offline page includes navigation to cached pages, offline page is fully cached (always available), offline page is accessible, and offline page includes sync status if background sync is used.

**Cached Content**: Previously viewed content should work offline. Verify that pages work offline after being visited once, images are cached and appear offline, styles and scripts are cached, cached content is up-to-date (cache invalidation strategy works), cached content indicates it may be stale if appropriate, users can identify what's available offline, and cache size is managed appropriately (doesn't fill storage).

**Offline Actions**: Some actions should queue for later sync. Test that forms can be filled offline (data stored locally), "Submit" indicates action will complete when online, background sync queues actions, sync status is visible (pending actions indicated), actions complete when connectivity returns, users receive feedback when synced actions complete, failed syncs are indicated and can be retried, and conflicting changes are handled gracefully.

**Network Status Indicators**: Users need visibility into network state. Verify that network status indicator shows when offline (banner, icon, etc.), indicator updates when connectivity changes, indicator is non-intrusive but visible, indicator provides context (limited functionality offline), indicator offers retry option, indicator is accessible (announced to screen readers), and indicator design fits app aesthetic.

### 32.3 Installation and Home Screen

PWAs can be installed like native apps, requiring specific testing.

**Install Prompt**: PWAs can prompt users to install. Test that install prompt appears at appropriate time (after engagement, not immediately), install prompt is dismissible, install prompt can be triggered manually (install button in menu), custom install UI works if designed, install prompt works on both Android and iOS, install prompt doesn't appear if already installed, install prompt respects user's previous dismissal (doesn't immediately re-prompt), and install prompt is accessible.

**App Icons**: Installed PWAs need icons at multiple resolutions. Verify that icons at all required sizes are provided (manifest.json icons array), icon sizes match requirements (typically 192x192, 512x512, others), icons are high-quality and sharp at all sizes, icon design works on various backgrounds (light, dark), maskable icons are provided (Android adaptive icons), icon formats are supported (PNG, SVG), icons display correctly when installed, and icons follow platform guidelines (rounded squares on Android, rounded corners on iOS).

**App Manifest**: Web app manifest defines app metadata. Test that manifest.json is valid and accessible, app name and short_name are appropriate (short_name for home screen where space is limited), start_url is correct (where app opens when launched), display mode is appropriate (standalone, fullscreen, minimal-ui, browser), theme_color matches app design, background_color is appropriate (used for splash screen), icons array is complete, manifest is referenced in HTML (<link rel="manifest">), and manifest validates (using PWA testing tools).

**Home Screen Experience**: Installed PWAs should feel app-like. Verify that app opens in standalone mode (no browser UI), app uses defined theme color, app opens to correct start_url, app handles deep links correctly, app works when offline (if content cached), app icon and name appear correctly on home screen, app appears in app drawer/launcher (Android), app appears in home screen (iOS), and app can be uninstalled (standard platform uninstall process).

### 32.4 Push Notifications

Push notifications enable re-engagement, requiring careful testing.

**Notification Permission**: Apps must request notification permission appropriately. Test that permission prompt appears at appropriate time (after user action, not immediately), permission prompt explains value proposition (why notifications are useful), permission prompt is dismissible, permission can be requested again if initially denied (with explanation), permission state is checked before attempting to send notifications, denied permission is handled gracefully (doesn't break app), and permission prompt is accessible.

**Notification Content**: Notifications must be relevant and well-formatted. Verify that notification title is clear and concise, notification body provides helpful context, notification icon displays correctly (manifest icons used), notification badge displays on app icon (Android), notification actions work if provided (buttons like "Reply", "Dismiss"), notification click opens relevant page in app, notification respects user preferences (frequency, types), notifications are timely and relevant, and notifications aren't spammy (don't send too many).

**Notification Display**: Notifications should appear correctly across platforms. Test notifications on Android, notifications on iOS (if using compatible service), notification grouping works (related notifications group together), notification sounds work if designed (and respect system preferences), notification vibration works if designed, notification appearance is acceptable (different platforms style differently), and notifications can be dismissed.

**Notification Delivery**: Ensure reliable notification delivery. Verify that push service registration works, service worker receives push messages, push encryption works correctly (VAPID keys), notification triggers work (scheduled, server-push, etc.), notification delivery is timely (not significant delays), notifications work when app is closed, notifications work on all target platforms, and notification failures are logged and handled.

### 32.5 App-Like Interactions and Gestures

PWAs should provide interactions users expect from native apps.

**Swipe Gestures**: Common mobile gestures should work naturally. Test that swipe to go back works if designed (careful with browser back), swipe to refresh works (pull-down to refresh), swipe gestures don't conflict with browser gestures, horizontal swipes for navigation work (carousels, etc.), swipe gestures provide visual feedback, swipe gestures have appropriate thresholds (how far to swipe), and swipe gestures work smoothly and responsively.

**Touch Interactions**: Touch interactions should feel responsive and native. Verify that tap targets are appropriately sized (44x44px minimum), tap response is immediate (visual feedback on touch), long-press gestures work if designed, multi-touch gestures work (pinch-zoom, etc.), touch ripple effects feel natural, touch interactions don't conflict with scrolling, and touch interactions work across devices.

**Smooth Scrolling**: Scrolling should feel fluid and native. Test that scroll is smooth and doesn't jank, scroll momentum feels natural (native-like inertia), scroll-triggered effects perform well (parallax, lazy loading, etc.), fixed/sticky elements don't cause scroll issues, overscroll behavior is appropriate (bounce on iOS, glow on Android), scroll position restores when navigating back, and scroll performance is good on lower-end devices.

**Animations and Transitions**: App-like animations enhance perceived quality. Verify that page transitions are smooth (not instant or janky), navigation animations match platform conventions, animated interactions feel responsive (minimal delay), animations perform at 60fps, animations respect prefers-reduced-motion, transition timing feels natural (ease curves), and animations don't interfere with interactions.

### 32.6 Platform Integration

PWAs can integrate with platform features requiring testing.

**Share API**: Web Share API enables native sharing. Test that share button triggers native share sheet, share sheet includes text, URL, and title, share sheet includes image if sharing image, share sheet works on both Android and iOS, share fallback works on unsupported browsers (copy link, etc.), share content is appropriate, and share is accessible (keyboard, screen reader).

**Media APIs**: Camera and microphone access enables rich features. Verify that getUserMedia permission requests work, camera access works correctly, microphone access works, file upload works (especially for images), captured media displays correctly, media upload shows progress, media errors are handled gracefully, and permissions are requested at appropriate time (when needed, not immediately).

**File System Access**: Some PWAs can read/write files. Test that file picker works correctly, file reading works for supported types, file saving works (downloads), file system permissions work, file operations show progress, file errors are handled gracefully (permission denied, unsupported type), and file operations are accessible.

**Clipboard API**: Modern clipboard APIs enable better copy/paste. Verify that copy to clipboard works, copied content is correct (text, HTML, etc.), copy provides user feedback ("Copied!"), clipboard permission works if required, paste from clipboard works if used, paste permission works, and clipboard operations are accessible.

### 32.7 PWA Performance and Optimization

PWAs must be optimized for app-like performance.

**Service Worker Efficiency**: Service worker is core to PWA functionality. Test that service worker installs correctly, service worker updates appropriately (versioning strategy), service worker caching strategy is effective (cache-first, network-first, etc. as appropriate), service worker doesn't cache too much (storage management), service worker cleanup works (removing old caches), service worker errors are logged, and service worker doesn't cause performance issues.

**Bundle Size Optimization**: Fast loading requires small bundles. Verify that JavaScript bundles are optimized (minified, tree-shaken), code splitting reduces initial bundle size, lazy loading works for routes and components, images are optimized (compressed, responsive), fonts are optimized (subset, woff2), unused code is eliminated, bundle sizes are within budget, and bundle analysis identifies opportunities.

**Runtime Performance**: App must perform well during use. Test that interactions are responsive (<100ms response), animations run at 60fps, scrolling is smooth, memory usage is reasonable (no leaks), CPU usage is reasonable, battery drain is acceptable, performance is good on lower-end devices, and performance profiling identifies bottlenecks.

### 32.8 PWA Testing Checklist

Comprehensive PWA testing checklist:

**App Shell and Loading**:
☐ App shell loads instantly on repeat visits
☐ App shell provides meaningful layout
☐ Splash screen appears correctly when installed
☐ First paint is within 1 second
☐ Loading indicators are clear and accessible
☐ Skeleton screens match final layout

**Offline Functionality**:
☐ Offline page appears when appropriate
☐ Previously viewed content works offline
☐ Offline actions queue for later sync
☐ Network status is clearly indicated
☐ Cache strategy is effective
☐ Cache size is managed

**Installation**:
☐ Install prompt appears at appropriate time
☐ App icons are provided at all required sizes
☐ Manifest.json is valid and complete
☐ App opens in standalone mode when installed
☐ App icon and name appear correctly on home screen
☐ Deep links work correctly

**Push Notifications**:
☐ Permission is requested appropriately
☐ Notification content is clear and relevant
☐ Notifications display correctly across platforms
☐ Notification clicks open relevant content
☐ Notification delivery is reliable
☐ Users can manage notification preferences

**App-Like Experience**:
☐ Swipe gestures work naturally
☐ Touch interactions feel responsive
☐ Scrolling is smooth and native-feeling
☐ Animations and transitions are smooth
☐ Platform integrations work (share, camera, etc.)

**Performance**:
☐ Service worker installs and updates correctly
☐ Bundle sizes are optimized
☐ Initial load is fast
☐ Runtime performance is good
☐ App works well on lower-end devices
☐ Performance budgets are maintained

---
