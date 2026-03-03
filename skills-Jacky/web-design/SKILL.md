# Web Design Skill

A comprehensive design intelligence system for building beautiful, professional websites based on analysis of 100+ real-world examples from One Page Love and industry best practices.

---

## Table of Contents

1. [Design Principles](#design-principles)
2. [Layout Patterns](#layout-patterns)
3. [Color Theory & Palettes](#color-theory--palettes)
4. [Typography Rules](#typography-rules)
5. [Component Patterns](#component-patterns)
6. [Responsive Design](#responsive-design)
7. [Animation & Interactions](#animation--interactions)
8. [Common Mistakes to Avoid](#common-mistakes-to-avoid)

---

## Design Principles

### 1. Clarity First
Every design decision should serve the user's understanding. If it doesn't add clarity, remove it.

**Key Rules:**
- One primary action per section
- Visual hierarchy must be immediately obvious
- White space is not empty space—it's breathing room
- Every element must earn its place

**From Real Sites:**
- Bajgart Office uses "strong copywriting" and "upfront availability" to build instant trust
- App&Flow uses 3D elements purposefully—not for decoration, but to demonstrate capability

### 2. Consistency Creates Trust
Users should feel they're in the same experience throughout their journey.

**Key Rules:**
- Limit to 2-3 colors for primary UI
- Use consistent spacing (4px, 8px, 16px, 24px, 32px, 48px, 64px scale)
- Maintain typographic rhythm throughout
- Interactive elements should behave predictably

### 3. Mobile-First Thinking
Design for constraints first, then enhance for larger screens.

**Key Rules:**
- Start with 375px viewport
- Thumb-friendly tap targets (44px minimum)
- Content hierarchy must work without hover states
- Performance matters most on mobile

### 4. Purposeful Motion
Animation should guide, not distract.

**Key Rules:**
- 200-300ms for micro-interactions
- 400-600ms for larger transitions
- Use `prefers-reduced-motion` always
- Movement should follow user gaze

### 5. Content-Driven Design
Design amplifies content; it doesn't replace it.

**Key Rules:**
- Start with real content, never lorem ipsum
- Typography choices should enhance readability
- Images must be high-quality and purposeful
- Copy and design should reinforce each other

---

## Layout Patterns

### Hero Patterns

#### 1. Full-Height Centered Hero
**Best for:** Portfolios, agencies, emotional products
**Example:** Bajgart Office
**Structure:**
```
[Sticky Nav]
[Full-height hero with centered content]
  - Headline (large, bold)
  - Subheadline
  - Primary CTA
  - Supporting visual/video
```
**Key Characteristics:**
- 100vh height
- Content vertically and horizontally centered
- Background: Image, video, or solid color
- Single, clear CTA above the fold

#### 2. Split Hero (Text + Visual)
**Best for:** SaaS, products with visual appeal
**Example:** VOID (centrally-divided)
**Structure:**
```
[Sticky Nav]
[Split layout: 50% text | 50% visual]
  Left: Headline, subhead, CTA
  Right: Product image, illustration, or animation
```
**Key Characteristics:**
- Clear visual separation
- Visual side should be compelling
- Text side has clear hierarchy
- Often uses asymmetric balance

#### 3. Minimal Text Hero
**Best for:** Studios, luxury brands, artistic projects
**Example:** Luciano Pereira (résumé)
**Structure:**
```
[Minimal nav]
[Large typographic treatment]
[Subtle background or pure color]
```
**Key Characteristics:**
- Typography as the main visual element
- Extreme minimalism
- High contrast
- Often single-page scroll

### Content Section Patterns

#### 1. Sticky Side Navigation
**Best for:** Long-form content, documentation, case studies
**Features:**
- Navigation stays visible while scrolling
- Shows reading progress
- Links to section anchors

#### 2. Bento Grid
**Best for:** Feature showcases, portfolios, dashboards
**Example:** App&Flow feature sections
**Structure:**
```
[Grid layout with varying card sizes]
[2x2, 3x3, or asymmetric arrangements]
[Cards contain: icon, title, description]
```
**Key Characteristics:**
- Visual variety within structure
- Cards can span multiple cells
- Consistent internal padding
- Hover states reveal more

#### 3. Timeline/Story Layout
**Best for:** Case studies, about pages, process explanations
**Structure:**
```
[Vertical line or connector]
[Alternating left/right content blocks]
[Dates or milestones as anchors]
```

### Navigation Patterns

#### 1. Sticky Minimal Nav
- Logo left, links right (or hamburger on mobile)
- Background blur on scroll
- Height reduces slightly on scroll
- Most common pattern across all sites

#### 2. Hidden/Minimal Nav
- No visible nav on hero
- Hamburger or scroll-reveal
- Used for immersive experiences
- Example: Experimental sites like VOID

#### 3. Bottom Navigation
- Rare but effective for mobile apps
- Thumb-friendly positioning
- 3-5 primary actions

---

## Color Theory & Palettes

### Industry-Appropriate Palettes

#### SaaS/Tech
- **Primary:** Deep blues (#2563EB, #3B82F6)
- **Secondary:** Clean grays (#F3F4F6, #1F2937)
- **Accent:** Bright accent for CTAs (#10B981, #F59E0B)
- **Reference:** Joi Planner, Control Tower

#### Creative/Agency
- **Primary:** Bold, distinctive (varies by brand)
- **Secondary:** Neutral backgrounds
- **Accent:** High-contrast for actions
- **Reference:** App&Flow, Shapeshyft

#### Portfolio/Personal
- **Primary:** Often monochromatic or duotone
- **Secondary:** White or near-white
- **Accent:** Single accent color for CTAs
- **Reference:** Franz Wiebe, Dann Petty

#### Product/Physical
- **Primary:** Product color or complementary
- **Secondary:** Neutral backgrounds
- **Accent:** High contrast for buy/CTA
- **Reference:** Magnet Lover, Porsche Cayenne

#### Healthcare/Wellness
- **Primary:** Calming blues, greens, soft tones
- **Secondary:** Warm whites
- **Accent:** Trust-building colors
- **Reference:** HealthFlex, LAVA dental

### Color Rules

1. **60-30-10 Rule**
   - 60% dominant (backgrounds)
   - 30% secondary (sections, cards)
   - 10% accent (CTAs, highlights)

2. **Contrast Requirements**
   - Body text: 4.5:1 minimum (WCAG AA)
   - Large text: 3:1 minimum
   - Interactive elements: 3:1 against adjacent colors

3. **Dark Mode Considerations**
   - Don't just invert colors
   - Reduce brightness of primary colors
   - Use desaturated backgrounds (#121212 not pure black)
   - Adjust shadows to glows

---

## Typography Rules

### Typeface Selection by Category

#### Modern SaaS/Startups
- **Sans-serif:** Inter, DM Sans, Plus Jakarta Sans
- **Monospace (accents):** DM Mono, JetBrains Mono
- **Reference:** App&Flow (DM Mono + Inter)

#### Elegant/Luxury
- **Serif:** Cormorant Garamond, Playfair Display
- **Sans (pairing):** Montserrat, Inter
- **Reference:** Bajgart Office (Rhymes)

#### Experimental/Artistic
- **Display:** Advercase, Custom fonts
- **Body:** IBM Plex, system fonts
- **Reference:** VOID (Advercase + IBM Plex)

#### Editorial/Blog
- **Serif:** Source Serif Pro, Merriweather
- **Sans:** Source Sans Pro, Open Sans
- **Reference:** Today in Design

### Typography Scale

```
Display:     72px+ (hero headlines)
H1:          48-56px (page titles)
H2:          36-42px (section headers)
H3:          24-28px (subsections)
H4:          18-20px (card titles)
Body Large:  18px (lead paragraphs)
Body:        16px (standard text)
Small:       14px (captions, metadata)
Tiny:        12px (footnotes)
```

### Typography Rules

1. **Line Height**
   - Headlines: 1.1-1.2
   - Body: 1.5-1.7
   - Small text: 1.4-1.5

2. **Line Length**
   - Optimal: 45-75 characters
   - Maximum: 90 characters

3. **Font Weights**
   - Headlines: 600-800
   - Body: 400
   - Emphasis: 500-600
   - Don't use font-weight below 400 for body

4. **Type Pairing**
   - Maximum 2 font families
   - Contrast serif/sans or weights
   - Establish clear hierarchy

---

## Component Patterns

### Hero Section

**Anatomy:**
```
[Navigation - sticky or static]
[Hero Container - full height or large]
  [Background - image/video/color]
  [Content Layer]
    [Eyebrow text - optional]
    [Headline - H1, max 10 words]
    [Subheadline - 1-2 sentences]
    [CTA Button - primary action]
    [Social proof - optional: logos, ratings]
```

**Design Guidelines:**
- Headline should communicate value in 5 seconds
- CTA button: High contrast, clear action verb
- Background shouldn't compete with text (use overlays)
- Mobile: Stack vertically, reduce text size

### Call-to-Action (CTA)

**Button Best Practices:**
- Minimum height: 44px (mobile), 48px (desktop)
- Padding: 16px horizontal minimum
- Border radius: Match brand (4px for sharp, 8-12px for friendly, pill for modern)
- Text: Action verb + benefit ("Start Free Trial")
- Hover: Clear visual change (color shift, shadow, scale)

**CTA Placement:**
- Hero: Primary action
- After benefits: Reinforce
- Sticky footer (mobile): Always accessible
- End of page: Final conversion opportunity

### Navigation

**Standard Pattern:**
```
[Logo - left aligned]
[Nav Links - center or right]
  - Products/Services
  - About
  - Resources
  - Pricing
[CTA Button - right]
[Mobile: Hamburger menu]
```

**Sticky Nav Behavior:**
- Add background blur or solid color on scroll
- Reduce height slightly (64px → 56px)
- Show shadow for depth
- Transition: 200-300ms ease

### Testimonials

**Effective Patterns:**
1. **Single Featured:** Large quote, prominent photo, company logo
2. **Grid:** 2-3 columns, consistent card design
3. **Carousel:** For many testimonials, auto-advance with pause

**Elements:**
- Quote text (short, specific)
- Photo (professional, consistent style)
- Name and title
- Company logo (adds credibility)
- Star rating (if applicable)

### Pricing Tables

**Structure:**
```
[3-tier layout: Basic | Recommended | Enterprise]
[Recommended tier: Highlighted visually]
[Each tier:]
  - Plan name
  - Price (monthly/annual toggle)
  - Feature list (checkmarks)
  - CTA button
  - "Most Popular" badge (on recommended)
```

**Design Guidelines:**
- Recommended plan should visually pop
- Use checkmarks for included, subtle X for excluded
- Annual pricing: Show savings percentage
- Enterprise: "Contact Us" CTA

### Footer

**Big Footer Pattern (from Bajgart Office):**
```
[Multi-column layout]
  - Brand column (logo, tagline, social)
  - Link columns (Product, Company, Resources)
  - Newsletter signup
[Bottom bar]
  - Copyright
  - Legal links
  - Privacy/Terms
```

**Minimal Footer:**
```
[Single row]
  - Copyright
  - Social links
  - Essential links only
```

---

## Responsive Design

### Breakpoints

**Standard Breakpoints:**
```
Mobile:      < 640px
Tablet:      640px - 1024px
Desktop:     1024px - 1440px
Large:       > 1440px
```

**Content Widths:**
```
Mobile:      100% - 32px padding
Tablet:      100% - 48px padding
Desktop:     100% - 64px padding, max 1200px
Large:       Centered, max 1400px
```

### Responsive Patterns

#### Navigation
- Desktop: Horizontal links
- Tablet: May collapse to hamburger
- Mobile: Always hamburger

#### Hero
- Desktop: Side-by-side or centered with large type
- Tablet: May reduce image size
- Mobile: Stacked, reduced headline size

#### Grids
- Desktop: 3-4 columns
- Tablet: 2 columns
- Mobile: 1 column

#### Typography Scale
- Desktop: Base 16px, scale up
- Mobile: Base 16px, smaller headlines (reduce by ~20%)

---

## Animation & Interactions

### Timing Guidelines

| Animation Type | Duration | Easing |
|---------------|----------|--------|
| Micro-interaction (hover) | 150-200ms | ease-out |
| Button state change | 200ms | ease-in-out |
| Modal/dialog | 250-300ms | cubic-bezier(0.4, 0, 0.2, 1) |
| Page transition | 300-400ms | ease-in-out |
| Scroll reveal | 400-600ms | cubic-bezier(0, 0, 0.2, 1) |
| Hero entrance | 600-800ms | cubic-bezier(0.22, 1, 0.36, 1) |

### Common Animations

#### Scroll Reveal
```css
/* Fade up on scroll */
.reveal {
  opacity: 0;
  transform: translateY(24px);
  transition: opacity 0.4s ease-out, transform 0.4s ease-out;
}
.reveal.visible {
  opacity: 1;
  transform: translateY(0);
}
```

#### Hover States
```css
/* Button hover */
.button {
  transition: transform 0.2s ease, box-shadow 0.2s ease;
}
.button:hover {
  transform: translateY(-2px);
  box-shadow: 0 4px 12px rgba(0,0,0,0.15);
}
```

#### Stagger Animation
```css
/* Stagger children */
.stagger-children > * {
  animation: fadeInUp 0.4s ease-out forwards;
}
.stagger-children > *:nth-child(1) { animation-delay: 0ms; }
.stagger-children > *:nth-child(2) { animation-delay: 100ms; }
.stagger-children > *:nth-child(3) { animation-delay: 200ms; }
```

### Accessibility

**Always include:**
```css
@media (prefers-reduced-motion: reduce) {
  *, *::before, *::after {
    animation-duration: 0.01ms !important;
    animation-iteration-count: 1 !important;
    transition-duration: 0.01ms !important;
  }
}
```

### Interactive Elements

#### Hover Requirements
- All clickable elements must have hover states
- Feedback should be immediate (cursor change, visual shift)
- Don't rely on hover for essential information (mobile!)

#### Focus States
- Must be visible for keyboard navigation
- Often same as hover or stronger
- Use `outline` or `box-shadow`

#### Loading States
- Buttons: Show spinner, disable interaction
- Images: Skeleton or blur-up placeholder
- Content: Skeleton screens preferred over spinners

---

## Common Mistakes to Avoid

### 1. Visual Mistakes

❌ **Low contrast text** - Always check 4.5:1 ratio  
❌ **Too many fonts** - Max 2 font families  
❌ **Inconsistent spacing** - Use a scale system  
❌ **Generic stock photos** - Use real, purposeful imagery  
❌ **Decorative without purpose** - Every element must earn its place  

### 2. UX Mistakes

❌ **No hover states** - Users need feedback  
❌ **Missing focus states** - Accessibility failure  
❌ **Wall of text** - Break into scannable chunks  
❌ **Confusing navigation** - Labels should be clear  
❌ **Too many CTAs** - One primary action per section  

### 3. Technical Mistakes

❌ **Ignoring reduced motion** - Respect user preferences  
❌ **Non-responsive images** - Always set max-width: 100%  
❌ **Touch targets too small** - 44px minimum  
❌ **No loading states** - Users need feedback  
❌ **Broken mobile navigation** - Test on real devices  

### 4. Content Mistakes

❌ **Lorem ipsum** - Design with real content  
❌ **Jargon-heavy copy** - Write for your audience  
❌ **Missing alt text** - Accessibility requirement  
❌ **Generic testimonials** - Specific beats generic  
❌ **Unclear value proposition** - Answer "why" immediately  

### 5. Performance Mistakes

❌ **Unoptimized images** - Compress, use WebP  
❌ **Too many fonts** - Subset, preload critical  
❌ **Heavy animations** - Test on low-end devices  
❌ **Render-blocking resources** - Defer non-critical  

---

## Quick Reference

### When to Reference Specific Sites

| Pattern Needed | Reference Site |
|---------------|----------------|
| Portfolio with explainer video | Bajgart Office |
| 3D interactive hero | App&Flow |
| Experimental/retro aesthetic | VOID |
| Product landing page | Magnet Lover |
| SaaS app landing | Joi Planner, Forma |
| Minimal personal site | Luciano Pereira |
| Experimental portfolio | MA Studio Speculative Software |
| Photography portfolio | Everline Studio |
| Healthcare landing | HealthFlex |
| Automotive product | Porsche Cayenne |
| Educational platform | Database School |
| Newsletter/content | Today in Design |

### Color Palette Quick Start

```css
:root {
  /* Primary - Your brand color */
  --color-primary: #2563EB;
  --color-primary-dark: #1D4ED8;
  
  /* Neutrals */
  --color-background: #FFFFFF;
  --color-surface: #F9FAFB;
  --color-border: #E5E7EB;
  
  /* Text */
  --color-text-primary: #111827;
  --color-text-secondary: #6B7280;
  --color-text-tertiary: #9CA3AF;
  
  /* Semantic */
  --color-success: #10B981;
  --color-warning: #F59E0B;
  --color-error: #EF4444;
}
```

### Spacing Scale

```css
:root {
  --space-1: 4px;
  --space-2: 8px;
  --space-3: 12px;
  --space-4: 16px;
  --space-5: 24px;
  --space-6: 32px;
  --space-7: 48px;
  --space-8: 64px;
  --space-9: 96px;
  --space-10: 128px;
}
```

---

*Based on analysis of 120+ real websites from One Page Love and enhanced with industry best practices.*
