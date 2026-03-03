# Design Review Checklist

A comprehensive checklist for evaluating any web design before launch. Use this for quality assurance, client reviews, or self-assessment.

---

## Quick Navigation

- [Visual Design](#visual-design)
- [User Experience (UX)](#user-experience-ux)
- [Responsive Design](#responsive-design)
- [Performance](#performance)
- [Accessibility](#accessibility)
- [Content](#content)
- [SEO](#seo)
- [Pre-Launch](#pre-launch)

---

## Visual Design

### Color & Contrast

- [ ] **Primary color represents brand** - Color aligns with brand guidelines
- [ ] **60-30-10 rule followed** - 60% dominant, 30% secondary, 10% accent
- [ ] **Text contrast 4.5:1 minimum** - Passes WCAG AA for body text
- [ ] **Large text contrast 3:1 minimum** - Passes WCAG AA for headings
- [ ] **Interactive elements visible** - Buttons and links stand out
- [ ] **Dark mode implemented (if applicable)** - Colors adjusted for dark theme
- [ ] **No color alone conveys meaning** - Icons/text accompany color coding

### Typography

- [ ] **Maximum 2 font families** - Clean, consistent typographic system
- [ ] **Readable font sizes** - Body text 16px minimum
- [ ] **Proper line height** - 1.5 for body, 1.2 for headlines
- [ ] **Line length optimal** - 45-75 characters per line
- [ ] **Hierarchy clear** - H1, H2, H3 visually distinct
- [ ] **Font weights appropriate** - No ultra-thin text for body
- [ ] **Text readable on all backgrounds** - Sufficient contrast everywhere

### Spacing & Layout

- [ ] **Consistent spacing scale** - Uses 4px, 8px, 16px, 24px, 32px, 48px, 64px
- [ ] **Adequate white space** - Elements can breathe
- [ ] **Alignment consistent** - Grid system followed
- [ ] **Content centered properly** - Not too wide on large screens (max 1200px)
- [ ] **Mobile padding sufficient** - 16px minimum on sides
- [ ] **No awkward breaks** - Images, buttons not cut off

### Visual Elements

- [ ] **Images high quality** - No pixelation, proper resolution
- [ ] **Images optimized** - WebP format, lazy loaded
- [ ] **Icons consistent** - Same style throughout (outline vs filled)
- [ ] **No generic stock photos** - Real, purposeful imagery
- [ ] **Decorative elements minimal** - Everything serves a purpose
- [ ] **Shadows subtle and consistent** - Same direction, opacity, blur

---

## User Experience (UX)

### Navigation

- [ ] **Navigation sticky or easily accessible** - Always within reach
- [ ] **Current page indicated** - Users know where they are
- [ ] **Mobile menu works** - Hamburger opens/closes properly
- [ ] **Navigation labels clear** - Users understand where links go
- [ ] **No more than 7 nav items** - Prevents decision paralysis
- [ ] **Logo links to home** - Standard behavior

### Interactions

- [ ] **All clickable elements have hover states** - Clear feedback
- [ ] **Hover states visible** - Color change, shadow, or scale
- [ ] **Focus states defined** - Keyboard navigation visible
- [ ] **Active states defined** - Click feedback
- [ ] **Loading states present** - Users know something is happening
- [ ] **Error states designed** - Form errors don't break layout
- [ ] **Success states designed** - Confirmations are clear

### Forms

- [ ] **Labels present** - Every input has a label
- [ ] **Placeholder text helpful** - Shows expected format
- [ ] **Required fields marked** - Users know what's mandatory
- [ ] **Error messages specific** - "Enter a valid email" not "Error"
- [ ] **Input types correct** - email, tel, number where appropriate
- [ ] **Form validation works** - Client-side before server
- [ ] **Submit button prominent** - Clear primary action

### Calls to Action (CTAs)

- [ ] **Primary CTA obvious** - Highest contrast, prominent position
- [ ] **CTA text action-oriented** - "Get Started" not "Submit"
- [ ] **One primary CTA per section** - Clear focus
- [ ] **CTA above the fold** - Hero section has clear action
- [ ] **CTA repeated at bottom** - Final conversion opportunity

### Feedback & Trust

- [ ] **404 page designed** - On-brand, helpful navigation
- [ ] **Success messages clear** - Users know actions worked
- [ ] **Error messages helpful** - Users know what to fix
- [ ] **Social proof present** - Testimonials, logos, ratings
- [ ] **Contact info accessible** - Users can reach you

---

## Responsive Design

### Breakpoints

- [ ] **Mobile (< 640px) tested** - Layout works on small screens
- [ ] **Tablet (640px - 1024px) tested** - Layout adapts properly
- [ ] **Desktop (1024px+) tested** - Full layout displays correctly
- [ ] **Large screens (> 1440px) tested** - Content doesn't stretch too wide

### Mobile-Specific

- [ ] **Touch targets 44px minimum** - Easy to tap
- [ ] **No horizontal scroll** - Content fits viewport
- [ ] **Text readable without zoom** - No tiny text
- [ ] **Images scale properly** - No overflow
- [ ] **Navigation accessible** - Hamburger or thumb-friendly
- [ ] **Forms usable** - Inputs large enough to tap

### Layout Adaptations

- [ ] **Grids collapse properly** - 4-col → 2-col → 1-col
- [ ] **Hero text readable** - Font sizes reduce appropriately
- [ ] **Images resize** - Maintain aspect ratios
- [ ] **Spacing reduces** - Less padding on mobile
- [ ] **Navigation adapts** - Desktop nav → mobile nav
- [ ] **Tables scroll horizontally** - Or stack gracefully

---

## Performance

### Loading

- [ ] **Page loads under 3 seconds** - On 3G connection
- [ ] **Largest Contentful Paint < 2.5s** - Core Web Vital
- [ ] **First Input Delay < 100ms** - Core Web Vital
- [ ] **Cumulative Layout Shift < 0.1** - Core Web Vital

### Images

- [ ] **Images compressed** - Without visible quality loss
- [ ] **WebP format used** - With fallbacks
- [ ] **Lazy loading implemented** - Images load as needed
- [ ] **Proper dimensions set** - Prevents layout shift
- [ ] **Responsive images** - srcset for different sizes

### Code

- [ ] **CSS minified** - Production build optimized
- [ ] **JavaScript minified** - Production build optimized
- [ ] **Unused CSS removed** - PurgeCSS or similar
- [ ] **Critical CSS inlined** - Above-fold styles loaded first
- [ ] **Render-blocking resources minimized** - Async/defer scripts

### Fonts

- [ ] **Font files subset** - Only needed characters
- [ ] **Fonts preloaded** - Critical fonts load first
- [ ] **Font-display: swap** - Text visible immediately
- [ ] **Maximum 3 font weights** - Reduces file size

---

## Accessibility

### Structure

- [ ] **Semantic HTML used** - header, nav, main, section, footer
- [ ] **Heading hierarchy correct** - H1 → H2 → H3, no skips
- [ ] **Landmarks present** - ARIA landmarks or semantic elements
- [ ] **Skip link included** - Bypass navigation

### Screen Readers

- [ ] **Alt text on images** - Descriptive, purposeful
- [ ] **ARIA labels where needed** - Icons, complex interactions
- [ ] **Form inputs labeled** - Explicit labels or aria-label
- [ ] **Status messages announced** - aria-live regions
- [ ] **Focus order logical** - Tab through in expected order

### Keyboard Navigation

- [ ] **All functionality keyboard accessible** - No mouse-only features
- [ ] **Focus visible** - Clear focus indicator
- [ ] **No keyboard traps** - Can tab through entire page
- [ ] **Shortcuts don't conflict** - Avoid single-key shortcuts

### Visual Accessibility

- [ ] **Zoom works to 200%** - Content still usable
- [ ] **Color not sole indicator** - Icons/text with color
- [ ] **Animations can be disabled** - prefers-reduced-motion
- [ ] **Flashing content avoided** - No seizures risk

---

## Content

### Copy

- [ ] **No lorem ipsum** - Real content throughout
- [ ] **Grammar checked** - No spelling errors
- [ ] **Tone consistent** - Matches brand voice
- [ ] **Jargon minimized** - Audience-appropriate language
- [ ] **Active voice preferred** - "We deliver" not "Delivery is made"
- [ ] **Headlines scannable** - Users get gist quickly

### Information Architecture

- [ ] **Value proposition clear** - Above the fold
- [ ] **Navigation labels clear** - Users understand options
- [ ] **Content hierarchy logical** - Most important first
- [ ] **Related content grouped** - Clear sections
- [ ] **Search present (if needed)** - For content-heavy sites

### Legal

- [ ] **Privacy policy linked** - Required in many jurisdictions
- [ ] **Terms of service linked** - If applicable
- [ ] **Cookie consent (if EU)** - GDPR compliance
- [ ] **Copyright notice** - Current year

---

## SEO

### Technical

- [ ] **Title tags unique** - Every page has specific title
- [ ] **Meta descriptions present** - Compelling summaries
- [ ] **Canonical URLs set** - Prevents duplicate content
- [ ] **Robots.txt configured** - Search engines know what to crawl
- [ ] **Sitemap submitted** - To Google Search Console
- [ ] **SSL certificate installed** - HTTPS throughout

### Content

- [ ] **One H1 per page** - Contains primary keyword
- [ ] **Images have alt text** - Descriptive, keyword-appropriate
- [ ] **URLs are readable** - /about-us not /p=123
- [ ] **Internal links present** - Connects related content
- [ ] **Schema markup added** - Rich snippets where applicable

### Mobile

- [ ] **Mobile-friendly test passed** - Google Mobile-Friendly Test
- [ ] **Viewport meta tag set** - width=device-width
- [ ] **No intrusive interstitials** - Doesn't block content

---

## Pre-Launch

### Functionality

- [ ] **All links work** - No 404s
- [ ] **Forms submit correctly** - Data received where expected
- [ ] **Emails send** - Contact forms, notifications work
- [ ] **E-commerce functions** - Cart, checkout, payments work
- [ ] **Search works** - Returns relevant results
- [ ] **Social sharing works** - OG tags, proper previews

### Cross-Browser

- [ ] **Chrome tested** - Latest version
- [ ] **Firefox tested** - Latest version
- [ ] **Safari tested** - Latest version
- [ ] **Edge tested** - Latest version
- [ ] **Mobile Safari tested** - iOS
- [ ] **Chrome Mobile tested** - Android

### Devices

- [ ] **iPhone tested** - iOS Safari
- [ ] **Android tested** - Chrome Mobile
- [ ] **iPad tested** - Tablet experience
- [ ] **Desktop tested** - Windows and Mac

### Analytics & Tracking

- [ ] **Analytics installed** - Google Analytics 4 or similar
- [ ] **Goals configured** - Conversion tracking set up
- [ ] **Privacy compliant** - GDPR/CCPA settings
- [ ] **Search Console connected** - Google Search Console

### Final Checks

- [ ] **Favicon present** - All sizes for devices
- [ ] **Touch icon present** - iOS home screen icon
- [ ] **Social images set** - OG image, Twitter card
- [ ] **Loading states work** - No broken experiences
- [ ] **Error pages styled** - 404, 500 pages on-brand
- [ ] **Print stylesheets** - Pages print reasonably

---

## Severity Levels

### 🔴 Critical (Must Fix Before Launch)

- Broken functionality (forms, links, checkout)
- Security issues (no HTTPS, exposed credentials)
- Legal compliance missing (privacy policy, cookie consent)
- Severe accessibility blockers (no keyboard access)
- Major performance issues (> 10s load time)

### 🟠 High Priority (Fix Soon After Launch)

- Mobile usability issues
- Poor contrast ratios
- Missing alt text on important images
- Slow loading images
- Broken social sharing

### 🟡 Medium Priority (Address in Next Iteration)

- Minor spacing inconsistencies
- Suboptimal image formats
- Missing schema markup
- Non-critical accessibility improvements

### 🟢 Low Priority (Nice to Have)

- Animation refinements
- Additional breakpoints
- Enhanced micro-interactions
- Advanced SEO optimizations

---

## Using This Checklist

### For Self-Review:
1. Go through each section systematically
2. Mark items as you verify them
3. Note issues for fixing
4. Prioritize by severity

### For Client Review:
1. Share checklist before review
2. Walk through together
3. Document decisions
4. Set expectations for iterations

### For Team Handoff:
1. Use as acceptance criteria
2. QA tests against checklist
3. Sign-off required before launch
4. Reference for future updates

---

## Tools for Validation

### Performance
- **PageSpeed Insights** - Core Web Vitals
- **GTmetrix** - Detailed performance analysis
- **WebPageTest** - Multi-location testing

### Accessibility
- **Lighthouse** - Built into Chrome DevTools
- **WAVE** - Web accessibility evaluation
- **axe DevTools** - Browser extension

### Responsiveness
- **Chrome DevTools Device Mode** - Multiple viewports
- **BrowserStack** - Real device testing
- **Responsively App** - Side-by-side viewports

### SEO
- **Screaming Frog** - Technical SEO audit
- **Google Search Console** - Indexing status
- **Rich Results Test** - Schema validation

---

*Checklist compiled from WCAG guidelines, Core Web Vitals, and industry best practices.*
