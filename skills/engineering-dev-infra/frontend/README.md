# Web Design Skill for OpenClaw

A comprehensive design intelligence system for building beautiful, professional websites based on analysis of 120+ real-world examples from One Page Love combined with industry best practices.

---

## Overview

This skill provides actionable guidance for web design across all aspects:

- **Design Principles** - Core rules derived from real sites
- **Layout Patterns** - Proven structures for common sections
- **Color & Typography** - Industry-specific guidance
- **Component Patterns** - Detailed anatomy of common UI elements
- **Responsive Design** - Mobile-first approach
- **Animation Guidelines** - Timing, easing, and accessibility
- **Common Mistakes** - What to avoid

---

## File Structure

```
~/clawd/skills/web-design/
├── README.md           # This file - overview and usage
├── SKILL.md            # Main skill file - comprehensive design guide
├── patterns.md         # Detailed pattern library with code examples
├── inspiration.md      # 120+ curated sites from One Page Love
├── checklist.md        # Pre-launch design review checklist
└── data/
    └── sites_complete.json  # Raw data of analyzed sites
```

---

## Quick Start

### When Starting a New Project:

1. **Open `inspiration.md`** - Find 3-5 sites in your category
2. **Reference `SKILL.md`** - Review relevant design principles
3. **Use `patterns.md`** - Copy code templates for components
4. **Before launch** - Run through `checklist.md`

### Key Sections by Need:

| If you need... | Reference |
|----------------|-----------|
| Hero section ideas | SKILL.md → Layout Patterns → Hero Patterns |
| Color palette guidance | SKILL.md → Color Theory & Palettes |
| Typography rules | SKILL.md → Typography Rules |
| Component code | patterns.md |
| Site examples | inspiration.md |
| Pre-launch QA | checklist.md |

---

## Design Principles Summary

### The 5 Core Principles:

1. **Clarity First** - Every element serves understanding
2. **Consistency Creates Trust** - Same patterns, predictable behavior
3. **Mobile-First Thinking** - Design for constraints first
4. **Purposeful Motion** - Animation guides, doesn't distract
5. **Content-Driven Design** - Design amplifies content

### Key Rules:

- **Colors:** 60-30-10 rule, 4.5:1 contrast minimum
- **Typography:** Max 2 fonts, 16px body minimum, 1.5 line-height
- **Spacing:** 4px base scale (4, 8, 16, 24, 32, 48, 64)
- **Animation:** 200-300ms micro, 400-600ms large, always respect `prefers-reduced-motion`
- **Mobile:** 44px touch targets, 16px side padding

---

## Pattern Categories

### Hero Patterns
- Full-Height Centered (Bajgart Office style)
- Split Hero (VOID style)
- Asymmetric Split (App&Flow style)
- Minimal Text (Luciano Pereira style)

### Navigation Patterns
- Sticky Minimal (Standard)
- Hidden/Reveal (Experimental)
- Bottom Navigation (Mobile apps)

### Content Patterns
- Feature Grid (Bento Box)
- Alternating Content Blocks
- Sticky Side Navigation
- Timeline/Story Layout

### Component Patterns
- Testimonial Cards (3 variants)
- Pricing Tables (3-tier structure)
- Portfolio Cards
- Forms (3 patterns)
- Footers (Big and Minimal)

---

## Site Categories in Inspiration Gallery

| Category | Count | Example Sites |
|----------|-------|---------------|
| Portfolios | 15+ | Bajgart Office, App&Flow, Dann Petty |
| SaaS & Apps | 20+ | Joi Planner, Forma, Control Tower |
| Agencies & Services | 10+ | Shapeshyft, Everline Studio, Studio Nika |
| Landing Pages | 8+ | Magnet Lover, ISO Meet, Katja Wolfinger |
| Experimental | 15+ | VOID, The Spark, Shopify Editions |
| Products | 15+ | Porsche Cayenne, Paper, EyeDrop |
| Personal | 8+ | René Coignard, Luciano Pereira |
| Specialized | 20+ | Database School, HealthFlex, Today in Design |

**Total: 120+ sites analyzed**

---

## Design System Quick Reference

### Color Palette (CSS Variables)

```css
:root {
  --color-primary: #2563EB;
  --color-primary-dark: #1D4ED8;
  --color-background: #FFFFFF;
  --color-surface: #F9FAFB;
  --color-border: #E5E7EB;
  --color-text-primary: #111827;
  --color-text-secondary: #6B7280;
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

### Typography Scale

```
Display:     72px+      (hero headlines)
H1:          48-56px    (page titles)
H2:          36-42px    (section headers)
H3:          24-28px    (subsections)
H4:          18-20px    (card titles)
Body Large:  18px       (lead paragraphs)
Body:        16px       (standard text)
Small:       14px       (captions)
Tiny:        12px       (footnotes)
```

### Breakpoints

```
Mobile:      < 640px
Tablet:      640px - 1024px
Desktop:     1024px - 1440px
Large:       > 1440px
```

---

## Anti-Patterns to Avoid

### Visual
- ❌ Low contrast text
- ❌ Too many fonts (> 2)
- ❌ Inconsistent spacing
- ❌ Generic stock photos
- ❌ Decorative without purpose

### UX
- ❌ No hover states
- ❌ Missing focus states
- ❌ Wall of text
- ❌ Confusing navigation
- ❌ Too many CTAs

### Technical
- ❌ Ignoring reduced motion
- ❌ Non-responsive images
- ❌ Touch targets too small
- ❌ No loading states
- ❌ Broken mobile navigation

---

## Real Site References by Pattern

| Pattern | Reference Site | URL |
|---------|---------------|-----|
| Video in hero | Bajgart Office | onepagelove.com/bajgart-office |
| 3D interactive hero | App&Flow | onepagelove.com/app-flow |
| Split layout | VOID | onepagelove.com/void |
| Dark mode toggle | App&Flow | onepagelove.com/app-flow |
| Sticky side nav | Eat Real Food | onepagelove.com/eat-real-food |
| Coming soon page | Droplist | onepagelove.com/droplist |
| Experimental portfolio | MA Studio | onepagelove.com/ma-studio-speculative-software |
| Minimal personal | Luciano Pereira | onepagelove.com/luciano-pereira |
| Product landing | Magnet Lover | onepagelove.com/magnet-lover |
| Healthcare | HealthFlex | onepagelove.com/healthflex |

---

## Usage Examples

### Example 1: SaaS Landing Page

1. **Reference sites:** Joi Planner, Forma, Control Tower
2. **Hero pattern:** Split Hero (50/50)
3. **Color palette:** SaaS - Blues, clean grays
4. **Typography:** Inter or similar sans-serif
5. **Components:** Feature grid, pricing table, testimonial cards

### Example 2: Portfolio Site

1. **Reference sites:** Bajgart Office, Dann Petty, Franz Wiebe
2. **Hero pattern:** Full-height centered or minimal text
3. **Color palette:** Depends on brand, often monochromatic
4. **Typography:** 1-2 fonts, expressive headline
5. **Components:** Project cards, about section, contact form

### Example 3: Product Launch

1. **Reference sites:** Magnet Lover, ISO Meet, Beanstalk
2. **Hero pattern:** Full-height with email capture
3. **Color palette:** Product-aligned, high energy
4. **Typography:** Bold headlines, clear CTAs
5. **Components:** Waitlist form, social proof, feature highlights

---

## Data Source

### One Page Love Analysis

This skill is built on analysis of 120+ real websites from [One Page Love](https://onepagelove.com/), including:

- Site metadata (name, URL, categories)
- Design features (typefaces, platforms, features)
- Descriptions of what makes each site great
- Identified design patterns
- Categorization by type

### Enhanced with Industry Best Practices

Combined with:
- WCAG accessibility guidelines
- Core Web Vitals performance standards
- Current design trends (2024-2026)
- UX research findings
- Typography and color theory principles

---

## Checklist Summary

The included checklist covers:

- ✅ Visual Design (color, typography, spacing, imagery)
- ✅ User Experience (navigation, interactions, forms, CTAs)
- ✅ Responsive Design (breakpoints, mobile, layout)
- ✅ Performance (loading, images, code, fonts)
- ✅ Accessibility (structure, screen readers, keyboard, visual)
- ✅ Content (copy, IA, legal)
- ✅ SEO (technical, content, mobile)
- ✅ Pre-Launch (functionality, cross-browser, devices, analytics)

**150+ individual checkpoints**

---

## Comparison to UI/UX Pro Max

This skill significantly improves upon the UI/UX Pro Max skill by:

1. **More practical examples** - 120+ real sites vs theoretical patterns
2. **Better organization** - Logical flow from principles to patterns to examples
3. **Code templates** - Ready-to-use CSS/HTML for common patterns
4. **Comprehensive checklist** - Pre-launch QA system
5. **Real descriptions** - What makes each site great, not just categories
6. **Actionable guidance** - Specific when-to-reference guidance
7. **Better structure** - SKILL.md for principles, patterns.md for code, inspiration.md for examples

---

## Version

**Version:** 1.0.0  
**Created:** February 2026  
**Sites Analyzed:** 120+  
**Source:** One Page Love + Industry Best Practices

---

## Credits

- **Data Source:** [One Page Love](https://onepagelove.com/) by Rob Hope
- **Accessibility:** WCAG 2.1 Guidelines
- **Performance:** Google Core Web Vitals
- **Typography:** Industry standards + Google Fonts
- **Color:** WCAG contrast guidelines + color theory

---

*This skill helps AI agents build beautiful websites based on real-world examples, not just theory.*
