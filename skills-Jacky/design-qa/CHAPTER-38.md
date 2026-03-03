# 35. Design QA for Marketing and Landing Pages


Marketing and landing pages have unique objectives and constraints. They must maximize conversion while maintaining brand consistency, load quickly to prevent bounce, and work across all acquisition channels and devices.

### 35.1 Hero Section Testing

The hero section is the first impression and primary conversion driver.

**Hero Layout and Composition**: Hero sections must be visually compelling. Test that headline is prominent and readable, headline doesn't wrap awkwardly (test various lengths), subheadline complements headline, call-to-action (CTA) button is prominent, CTA button text is clear and action-oriented, hero image or video is high-quality, hero image doesn't compete with text (contrast maintained), hero layout works at various viewport sizes, and hero maintains visual hierarchy.

**Hero Responsiveness**: Hero sections must adapt to all devices. Verify that mobile hero is optimized (often simplified), text size remains readable on mobile, CTA remains prominent on mobile, hero image crops appropriately on mobile, load performance is good on mobile, portrait orientation works well, landscape orientation on mobile works, and tablet layout is appropriate.

**Hero Loading Performance**: Hero content often blocks initial render. Test that hero image loads quickly (optimized, correct format), LCP (Largest Contentful Paint) target is met for hero, hero doesn't cause layout shift (aspect ratio specified), critical CSS includes hero styles, above-fold hero renders immediately, lazy loading doesn't delay hero image, placeholder/skeleton shown while loading, and hero video doesn't auto-play with sound.

**Hero Accessibility**: Hero sections must be accessible. Verify that text contrast meets WCAG AA (4.5:1 for normal text), text contrast meets AAA if possible (7:1), background image has overlay or sufficient contrast, CTA is keyboard accessible, focus indicator is visible on CTA, hero content is screen reader friendly, video has pause control, and reduced motion preferences are respected.

### 35.2 Conversion Elements Testing

Conversion elements drive the primary action.

**Call-to-Action Buttons**: CTAs must be optimized for conversion. Test that primary CTA is visually dominant, CTA color contrasts with background, CTA is appropriately sized (large enough to notice, not overwhelming), CTA placement is prominent (above fold, repeated if long page), CTA text is action-oriented (Start Free Trial, not Submit), CTA hover state is clear, CTA click feedback is immediate, CTA loading state shows during action, and multiple CTAs have clear hierarchy if present.

**Form Optimization**: Forms on landing pages must minimize friction. Verify that form fields are minimal (only essential fields), form labels are clear, placeholder text is helpful (not duplicative of label), inline validation provides immediate feedback, error messages are specific and actionable, success state is clear, form submission is fast, form works on mobile (appropriate keyboard types), and privacy assurance is visible near form.

**Trust Indicators**: Trust elements reduce friction. Test that trust badges/logos display correctly, customer count or social proof is visible, testimonials or reviews are prominent, security indicators are visible (SSL, secure payment), guarantee messaging is clear, privacy policy link is present, and social proof doesn't slow page load.

**Urgency and Scarcity**: Urgency elements must be credible and accessible. Verify that countdown timers work correctly, countdown timers don't reset on refresh (unless designed), limited quantity indicators are accurate, urgency messaging is clear, urgency colors don't cause accessibility issues (don't use red alone), and urgency is genuine (not fake scarcity).

### 35.3 Landing Page Performance

Landing pages must load instantly to prevent bounce.

**Core Web Vitals**: Landing pages must meet Core Web Vitals thresholds. Test that LCP (Largest Contentful Paint) is under 2.5 seconds, FID (First Input Delay) is under 100 milliseconds, CLS (Cumulative Layout Shift) is under 0.1, TTFB (Time to First Byte) is fast, FCP (First Contentful Paint) is fast, and performance is tested on real devices and slow connections.

**Image Optimization**: Images often dominate landing page weight. Verify that images are appropriately sized (not loading 4000px images for 800px display), images use modern formats (WebP with fallbacks), images are compressed appropriately, responsive images provide correct sizes (srcset), lazy loading is used for below-fold images, above-fold images are preloaded, and LCP image is prioritized.

**Third-Party Scripts**: Marketing pages often include many scripts. Test that scripts are loaded asynchronously where possible, non-critical scripts are deferred, tracking scripts don't block rendering, A/B testing tools don't cause layout shift, chat widgets don't block content, social widgets load efficiently, and script loading failures don't break page.

**Mobile Performance**: Mobile performance is especially critical. Verify that mobile page weight is reasonable, mobile images are optimized, touch targets are appropriately sized, mobile layout doesn't require excessive scrolling, mobile CTA is easily reachable, mobile form inputs work correctly, and mobile page doesn't freeze or jank.

### 35.4 Cross-Channel Consistency

Landing pages often receive traffic from multiple channels.

**Ad-to-Landing Page Continuity**: Users expect consistency from ad to landing page. Test that headline matches ad copy, imagery matches ad creative, offer matches ad promise, CTA matches ad CTA, color scheme matches ad branding, messaging tone matches ad tone, and users immediately recognize they're in the right place.

**UTM and Tracking Parameters**: Landing pages must handle tracking correctly. Verify that UTM parameters persist through page navigation, UTM parameters pass through to conversion events, tracking pixels fire correctly, tracking doesn't slow page load, tracking works with ad blockers (graceful degradation), and conversion attribution is accurate.

**Social Media Previews**: Landing pages should share well. Test that Open Graph tags are correct, Twitter Card tags are correct, share preview image is appropriate, share title is compelling, share description is appropriate, and share URL is canonical.

### 35.5 Landing Page Testing Checklist

Comprehensive landing page testing checklist:

**Hero Section**:
☐ Headline is prominent and readable
☐ Subheadline complements headline
☐ CTA is prominent and clear
☐ Hero image/video is high-quality
☐ Hero works on all device sizes
☐ Hero loads quickly (LCP target met)
☐ Text contrast meets accessibility standards

**Conversion Elements**:
☐ Primary CTA is visually dominant
☐ Form is minimized (only essential fields)
☐ Trust indicators are visible
☐ Social proof is prominent
☐ Urgency elements work correctly
☐ All CTAs are keyboard accessible
☐ Form validation works correctly

**Performance**:
☐ Core Web Vitals meet thresholds
☐ Images are optimized
☐ Third-party scripts don't block rendering
☐ Mobile performance is excellent
☐ Page weight is reasonable
☐ Loading states are clear

**Cross-Channel**:
☐ Ad-to-landing continuity is maintained
☐ UTM parameters work correctly
☐ Tracking fires accurately
☐ Social previews display correctly
☐ Messaging is consistent across channels

---
