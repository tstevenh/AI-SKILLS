# Pattern Library

Detailed component patterns organized by type, with real examples from analyzed sites.

---

## Table of Contents

1. [Hero Patterns](#hero-patterns)
2. [Navigation Patterns](#navigation-patterns)
3. [Content Section Patterns](#content-section-patterns)
4. [Card & Grid Patterns](#card--grid-patterns)
5. [Form Patterns](#form-patterns)
6. [Footer Patterns](#footer-patterns)
7. [Specialized Patterns](#specialized-patterns)

---

## Hero Patterns

### Pattern 1: Full-Height Centered

**Best for:** Portfolios, agencies, emotional products, landing pages

**Real Example:** Bajgart Office

**Structure:**
```
┌─────────────────────────────────────┐
│  [Sticky Navigation]                │
├─────────────────────────────────────┤
│                                     │
│         [Headline]                  │
│         H1 - 72px, Bold             │
│                                     │
│    [Subheadline - 20px]             │
│    Brief value proposition          │
│                                     │
│       [Primary CTA Button]          │
│                                     │
│    [Supporting visual/video]        │
│                                     │
│                                     │
└─────────────────────────────────────┘
       100vh minimum height
```

**Design Specs:**
- Height: 100vh (min-height: 600px)
- Content: Vertically and horizontally centered
- Headline: Max 10 words, communicates core value
- Background: Image/video with overlay (rgba(0,0,0,0.4)) or solid color
- CTA: High contrast, action-oriented text

**Code Template:**
```html
<section class="hero">
  <nav class="sticky-nav">...</nav>
  <div class="hero-content">
    <h1>Headline that communicates value</h1>
    <p class="subtitle">Supporting description that clarifies the value proposition</p>
    <button class="cta-primary">Get Started</button>
  </div>
</section>
```

```css
.hero {
  min-height: 100vh;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  text-align: center;
  padding: 2rem;
  background: linear-gradient(rgba(0,0,0,0.5), rgba(0,0,0,0.5)), url('hero-bg.jpg');
  background-size: cover;
  background-position: center;
}

.hero h1 {
  font-size: clamp(2.5rem, 5vw, 4.5rem);
  font-weight: 700;
  line-height: 1.1;
  max-width: 12ch;
  margin-bottom: 1.5rem;
}

.hero .subtitle {
  font-size: clamp(1rem, 2vw, 1.25rem);
  max-width: 50ch;
  margin-bottom: 2rem;
  opacity: 0.9;
}
```

---

### Pattern 2: Split Hero (50/50)

**Best for:** SaaS, products with visual appeal, B2B

**Real Example:** VOID (centrally-divided layout)

**Structure:**
```
┌─────────────────────────────────────┐
│  [Sticky Navigation]                │
├──────────────────┬──────────────────┤
│                  │                  │
│   [Headline]     │   [Product       │
│   H1 - 56px      │    Image/        │
│                  │    Animation]    │
│   [Description]  │                  │
│                  │   Often 3D or    │
│   [CTA Button]   │   interactive    │
│                  │                  │
│   [Trust Logos]  │                  │
│                  │                  │
└──────────────────┴──────────────────┘
```

**Design Specs:**
- Layout: CSS Grid or Flexbox, 50/50 split
- Mobile: Stack vertically (image on top or bottom)
- Visual side: Can overflow container for effect
- Content side: Max 600px width for readability

**Code Template:**
```html
<section class="hero-split">
  <div class="hero-content">
    <h1>Your headline here</h1>
    <p class="description">Detailed explanation of your product</p>
    <button class="cta-primary">Start Free Trial</button>
    <div class="trust-logos">...</div>
  </div>
  <div class="hero-visual">
    <img src="product-screenshot.png" alt="Product">
  </div>
</section>
```

```css
.hero-split {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 4rem;
  align-items: center;
  min-height: 90vh;
  padding: 4rem;
}

@media (max-width: 768px) {
  .hero-split {
    grid-template-columns: 1fr;
    gap: 2rem;
  }
}

.hero-visual img {
  max-width: 120%;
  transform: perspective(1000px) rotateY(-5deg);
  box-shadow: 0 25px 50px rgba(0,0,0,0.2);
}
```

---

### Pattern 3: Asymmetric Split

**Best for:** Creative portfolios, agencies, unique brands

**Real Example:** App&Flow (narrow layout with 3D hero)

**Structure:**
```
┌─────────────────────────────────────┐
│  [Minimal Nav]                      │
├─────────────────────────────────────┤
│                                     │
│     [Large Typography]              │
│     H1 spanning full width          │
│                                     │
│  ┌────────┐                         │
│  │ Text   │  [Large visual element] │
│  │ column │  positioned right       │
│  │ 30%    │  or overlapping         │
│  └────────┘                         │
│                                     │
└─────────────────────────────────────┘
```

**Design Specs:**
- Unconventional layout breaks expectations
- Typography is often oversized
- Visual element may overlap text area
- Requires careful balance

---

### Pattern 4: Minimal Text Hero

**Best for:** Luxury brands, portfolios, artistic projects

**Real Example:** Luciano Pereira (résumé)

**Structure:**
```
┌─────────────────────────────────────┐
│                                     │
│                                     │
│      [Name/Brand]                   │
│      Massive typography             │
│      120px+                         │
│                                     │
│      [One line descriptor]          │
│                                     │
│           [↓]                       │
│      Scroll indicator               │
│                                     │
└─────────────────────────────────────┘
```

**Design Specs:**
- Typography IS the design
- Often monochromatic or duotone
- Extreme minimalism
- Negative space is crucial

---

## Navigation Patterns

### Pattern 1: Sticky Minimal Nav

**Best for:** Most websites - the standard pattern

**Real Examples:** Bajgart Office, Forma, Joi Planner

**Structure:**
```
┌─────────────────────────────────────┐
│ [Logo]    [Link] [Link] [Link] [CTA]│
└─────────────────────────────────────┘
```

**States:**

**Initial (top):**
- Background: Transparent
- Padding: 24px vertical
- Logo: Full size

**Scrolled:**
- Background: White/blur with shadow
- Padding: 16px vertical
- Logo: Slightly smaller
- Transition: 300ms ease

**Code Template:**
```html
<nav class="nav-sticky">
  <a href="/" class="logo">Brand</a>
  <ul class="nav-links">
    <li><a href="#features">Features</a></li>
    <li><a href="#pricing">Pricing</a></li>
    <li><a href="#about">About</a></li>
  </ul>
  <button class="nav-cta">Get Started</button>
</nav>
```

```css
.nav-sticky {
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 1.5rem 2rem;
  z-index: 1000;
  transition: all 0.3s ease;
}

.nav-sticky.scrolled {
  background: rgba(255,255,255,0.95);
  backdrop-filter: blur(10px);
  box-shadow: 0 1px 3px rgba(0,0,0,0.1);
  padding: 1rem 2rem;
}
```

**JavaScript:**
```javascript
window.addEventListener('scroll', () => {
  const nav = document.querySelector('.nav-sticky');
  if (window.scrollY > 50) {
    nav.classList.add('scrolled');
  } else {
    nav.classList.remove('scrolled');
  }
});
```

---

### Pattern 2: Hidden/Reveal Nav

**Best for:** Immersive experiences, portfolios, experimental sites

**Real Example:** VOID

**Structure:**
```
┌─────────────────────────────────────┐
│         [☰ Hamburger]               │
│              Top right              │
├─────────────────────────────────────┤
│                                     │
│         [Full content               │
│          without nav                │
│          distraction]               │
│                                     │
└─────────────────────────────────────┘

[When clicked:]
┌─────────────────────────────────────┐
│ [Close X]                           │
├─────────────────────────────────────┤
│                                     │
│         [HOME]                      │
│         [ABOUT]                     │
│         [WORK]                      │
│         [CONTACT]                   │
│                                     │
│    Large, centered, fullscreen      │
│                                     │
└─────────────────────────────────────┘
```

**Design Specs:**
- Hamburger always visible or appears on scroll
- Full-screen overlay when opened
- Large, tappable links
- Often includes animation

---

### Pattern 3: Bottom Navigation (Mobile)

**Best for:** Mobile apps, progressive web apps

**Structure:**
```
┌─────────────────────────────────────┐
│                                     │
│                                     │
│         [Content Area]              │
│                                     │
│                                     │
├─────────────────────────────────────┤
│  [🏠]    [🔍]    [+]    [♥]    [👤] │
│ Home   Search  Add   Fav    Profile │
└─────────────────────────────────────┘
```

**Design Specs:**
- Fixed to bottom
- 3-5 primary actions
- Current page highlighted
- Thumb-friendly tap targets (44px+)

---

## Content Section Patterns

### Pattern 1: Feature Grid (Bento Box)

**Best for:** Feature showcases, capabilities, services

**Real Example:** App&Flow

**Structure:**
```
[Section Header]
┌─────────────────────────────────────┐
│  [Icon]              [Large Card    │
│  Feature One         spanning 2x1   │
│  Description         with image]    │
├──────────┬──────────────────────────┤
│ [Icon]   │  [Icon]      [Icon]      │
│ Feature  │  Feature     Feature     │
│ Two      │  Three       Four        │
├──────────┴──────────┬───────────────┤
│  [Large Card        │  [Icon]       │
│   with stats]       │  Feature Five │
└─────────────────────┴───────────────┘
```

**Design Specs:**
- Mix of card sizes creates visual interest
- Consistent internal padding (24px)
- Icons or illustrations in each card
- Hover states reveal more info

**Code Template:**
```html
<section class="features">
  <h2>Features</h2>
  <div class="bento-grid">
    <div class="card card-large">
      <h3>Main Feature</h3>
      <p>Description</p>
    </div>
    <div class="card">
      <icon></icon>
      <h3>Feature 2</h3>
    </div>
    <!-- More cards -->
  </div>
</section>
```

```css
.bento-grid {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 1.5rem;
}

.card {
  background: #f9fafb;
  border-radius: 16px;
  padding: 2rem;
}

.card-large {
  grid-column: span 2;
}
```

---

### Pattern 2: Alternating Content Blocks

**Best for:** Process explanations, storytelling, case studies

**Structure:**
```
[Section Header]

┌─────────────────────────────────────┐
│  [Image]        │  [Text Content]   │
│  Screenshot or  │  - Headline       │
│  illustration   │  - Description    │
│                 │  - Link/CTA       │
└─────────────────────────────────────┘

┌─────────────────────────────────────┐
│  [Text Content] │  [Image]          │
│  - Headline     │  Screenshot or    │
│  - Description  │  illustration     │
│  - Link/CTA     │                   │
└─────────────────────────────────────┘

[Repeat...]
```

**Design Specs:**
- Alternating sides break monotony
- Image: 50-60% width
- Text: Well-aligned, consistent padding
- Subtle connector or timeline optional

---

### Pattern 3: Sticky Side Navigation

**Best for:** Documentation, long-form content, case studies

**Real Example:** Eat Real Food (long-form journalism)

**Structure:**
```
┌──────────┬──────────────────────────┐
│ [Sticky  │  [Content Header]        │
│  Side    │                          │
│  Nav]    │  Content paragraph...    │
│          │                          │
│ • Intro  │  [Image]                 │
│ • Part 1 │                          │
│ • Part 2 │  More content...         │
│ • Part 3 │                          │
│          │  [Subsection]            │
│ (Highlights│                        │
│  current)│  Content continues...    │
│          │                          │
└──────────┴──────────────────────────┘
```

**Design Specs:**
- Left column: 240px fixed, sticky
- Right column: Flexible, max 70ch
- Active section highlighted
- Smooth scroll to anchors

---

## Card & Grid Patterns

### Pattern 1: Testimonial Cards

**Structure:**
```
┌─────────────────────────────────────┐
│ "Quote text that is specific and    │
│  provides real value insight..."    │
│                                     │
│ ┌────┐  John Doe                    │
│ │ 👤 │  CEO, Company Name           │
│ └────┘                              │
└─────────────────────────────────────┘
```

**Variants:**
- **Single Featured:** Large, centered, with photo
- **Grid:** 2-3 columns, consistent cards
- **Carousel:** Auto-advancing, dots navigation

**Design Specs:**
- Quote: Large, italic or distinct style
- Photo: 48-64px, circular or rounded
- Name: Bold
- Title: Muted, smaller
- Company logo: Optional but adds credibility

---

### Pattern 2: Pricing Cards

**Structure:**
```
        Basic       Pro ★        Enterprise
        ─────       ─────        ───────────
        $9/mo       $29/mo         Custom

        ✓ Feature   ✓ Feature    ✓ Feature
        ✓ Feature   ✓ Feature    ✓ Feature
        ✗ Feature   ✓ Feature    ✓ Feature
                    ✓ Feature    ✓ Feature
                                 ✓ Feature

       [Button]   [Button]      [Button]

      (★ Most Popular badge on Pro)
```

**Design Specs:**
- Middle/recommended tier should visually pop
- Use checkmarks for included, subtle styling for excluded
- Annual discount clearly shown
- "Most Popular" or "Best Value" badge
- Button hierarchy matches tier hierarchy

---

### Pattern 3: Portfolio/Project Cards

**Structure:**
```
┌─────────────────────────────────────┐
│                                     │
│  [Image/Thumbnail]                  │
│  Hover: Show project details        │
│                                     │
├─────────────────────────────────────┤
│ Project Name                        │
│ Category • Year                     │
└─────────────────────────────────────┘
```

**Hover States:**
- Overlay with project title
- Slight zoom on image
- Reveal "View Project" button
- Color shift

---

## Form Patterns

### Pattern 1: Single-Field CTA

**Best for:** Email capture, newsletter signup

**Structure:**
```
[Headline: Stay Updated]
[Subhead: Get weekly design tips]

┌────────────────────────┬────────────┐
│  email@example.com     │  Subscribe │
└────────────────────────┴────────────┘
```

**Design Specs:**
- Input: Large (48px height), clear placeholder
- Button: Same height, attached or separate
- Success: Clear confirmation message
- Error: Inline, specific feedback

---

### Pattern 2: Multi-Step Form

**Best for:** Complex forms, onboarding, checkout

**Structure:**
```
[Progress Bar: Step 1 of 3]

[Section Header]

[Field Label]
[Input field                    ]
[Helper text]

[Field Label]
[Input field                    ]

        [Continue →]
```

**Design Specs:**
- Show progress clearly
- Group related fields
- Primary action at bottom
- Allow going back
- Save progress if possible

---

### Pattern 3: Floating Labels

**Structure:**
```
Focus:  ┌─────────────────────┐
        │ Name                │
        │ John Doe            │
        └─────────────────────┘

Empty:  ┌─────────────────────┐
        │ Name                │
        └─────────────────────┘
```

**Design Specs:**
- Label floats up on focus/content
- Smooth transition (200ms)
- Saves space while maintaining clarity
- Good for mobile

---

## Footer Patterns

### Pattern 1: Big Footer (Multi-Column)

**Real Example:** Bajgart Office

**Structure:**
```
┌─────────────────────────────────────────────────┐
│                                                 │
│  [Logo]     Product    Company    Resources    │
│  Tagline    - Feature  - About    - Blog       │
│             - Pricing  - Careers  - Help       │
│             - Docs     - Contact  - API        │
│                                                 │
│  [Social Icons]        [Newsletter Signup]     │
│                        [Email        ][Sub]    │
│                                                 │
├─────────────────────────────────────────────────┤
│  © 2024 Company    Privacy • Terms • Cookies   │
└─────────────────────────────────────────────────┘
```

**Design Specs:**
- Background: Dark or contrasting color
- 4-5 columns on desktop
- Logo + tagline in first column
- Newsletter signup prominent
- Legal links at very bottom

---

### Pattern 2: Minimal Footer

**Best for:** Simple sites, portfolios

**Structure:**
```
┌─────────────────────────────────────┐
│                                     │
│   © 2024 Name    [Social Icons]    │
│                                     │
└─────────────────────────────────────┘
```

---

## Specialized Patterns

### Pattern 1: Launching Soon / Waitlist

**Real Examples:** Droplist, Luffu, Control Tower

**Structure:**
```
┌─────────────────────────────────────┐
│                                     │
│         [Logo/Mark]                 │
│                                     │
│    Something great is coming        │
│                                     │
│    Brief description of what        │
│    you're building...               │
│                                     │
│    [Email input    ] [Notify Me]    │
│                                     │
│    [Social proof: 1,234+ joined]    │
│                                     │
│    [Twitter] [LinkedIn] [Insta]     │
│                                     │
└─────────────────────────────────────┘
```

**Design Specs:**
- Single focus: Email capture
- Countdown timer optional
- Social proof builds urgency
- Simple, minimal distractions

---

### Pattern 2: Comparison Table

**Structure:**
```
┌──────────┬──────────┬──────────┬──────────┐
│ Feature  │  Basic   │   Pro    │ Business │
├──────────┼──────────┼──────────┼──────────┤
│ Feature A│    ✓     │    ✓     │    ✓     │
│ Feature B│    ✗     │    ✓     │    ✓     │
│ Feature C│    ✗     │    ✓     │    ✓     │
│ Feature D│    ✗     │    ✗     │    ✓     │
├──────────┼──────────┼──────────┼──────────┤
│          │  $9/mo   │  $29/mo  │  $99/mo  │
│          │ [Select] │ [Select] │ [Select] │
└──────────┴──────────┴──────────┴──────────┘
```

**Design Specs:**
- Highlight recommended column
- Sticky header on scroll
- Checkmarks vs dashes for clarity
- Zebra striping optional

---

### Pattern 3: FAQ Accordion

**Structure:**
```
[Section: Frequently Asked Questions]

┌─────────────────────────────────────┐
│ Question text here?            [+]  │
└─────────────────────────────────────┘
┌─────────────────────────────────────┐
│ Another question that might be      │
│ asked by users?                [-]  │
│                                     │
│ Answer text that provides the       │
│ detailed information...             │
└─────────────────────────────────────┘
┌─────────────────────────────────────┐
│ Third question here?             [+]│
└─────────────────────────────────────┘
```

**Design Specs:**
- Clear expand/collapse icons
- Smooth animation (300ms)
- Only one open at a time (optional)
- Padding around answer text

---

*All patterns derived from analysis of 120+ real websites on One Page Love.*
