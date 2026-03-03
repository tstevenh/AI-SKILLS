# 26. Typography Deep Dive


Typography is fundamental to user experience—it affects readability, comprehension, accessibility, brand perception, and overall design quality. Typography testing ensures text is readable, accessible, performant, and beautifully rendered across all devices and contexts. This comprehensive section covers all aspects of typographic quality assurance.

### 26.1 Font Loading and Performance

How fonts load dramatically affects user experience and performance.

**Flash of Invisible Text (FOIT)**: FOIT occurs when text is hidden while web fonts load. Browser default behavior varies: Chrome and Firefox show invisible text for 3 seconds while loading web fonts (FOIT), then swap to fallback font if not loaded. Safari immediately shows fallback font (FOUT approach). Testing identifies if FOIT impacts user experience: measure font load time (should be <1-2 seconds), test with slow network (3G simulation), verify text becomes visible quickly, and check if important text is hidden during initial load.

**Flash of Unstyled Text (FOUT)**: FOUT occurs when fallback font briefly displays before web font loads. While less problematic than FOIT (text is visible immediately), FOUT can cause layout shift and visual jump when fonts swap. Testing measures: measure layout shift when fonts swap (Cumulative Layout Shift metric), test on slow networks where FOUT is more noticeable, verify fallback font sizing minimizes shift, and check that FOUT duration is brief.

**Font Loading Strategies**: CSS `font-display` controls loading behavior. `font-display: swap` shows fallback immediately, swaps to web font when loaded (FOUT approach, recommended for most cases). `font-display: block` hides text briefly (up to 3 seconds) waiting for web font (FOIT approach, use sparingly). `font-display: fallback` very brief block period (~100ms), then shows fallback, swaps if web font loads within ~3 seconds. `font-display: optional` allows browser to decide based on connection speed (may never load web font on slow connections). `font-display: auto` browser default behavior. Testing validates chosen strategy: test with slow networks, verify text is visible quickly, check layout shift is minimal, and validate strategy matches content priority (critical content should be visible immediately).

**Font Loading API**: JavaScript provides fine-grained control. Font Face Observer library simplifies font loading:

```javascript
const fontA = new FontFaceObserver('Open Sans');
const fontB = new FontFaceObserver('Open Sans', { weight: 700 });

Promise.all([fontA.load(), fontB.load()]).then(() => {
  document.documentElement.className += ' fonts-loaded';
});
```

CSS shows/hides content based on loading state:

```css
body {
  font-family: Arial, sans-serif; /* Fallback */
}

.fonts-loaded body {
  font-family: 'Open Sans', Arial, sans-serif; /* Web font */
}
```

Testing validates JavaScript loading works: verify fonts load correctly, check timeout handles very slow connections, test fallback experience is acceptable, and validate no JavaScript errors prevent font loading.

**Font Subsetting**: Reducing font file size improves load time. Subset fonts to only include needed characters (Latin characters only if not displaying other languages), remove unused glyphs (rarely-used special characters), use modern formats (WOFF2 is ~30% smaller than WOFF), and consider variable fonts (one file with multiple weights). Testing validates subsetting doesn't break display: test with actual content (ensure all needed characters are included), verify special characters display correctly, test numbers and punctuation, check accented characters for internationalization, and validate subset fonts load faster than full fonts.

**Preloading Fonts**: `<link rel="preload">` loads critical fonts early. Preload most critical fonts (typically body font and one heading font):

```html
<link rel="preload" href="/fonts/open-sans-regular.woff2" as="font" type="font/woff2" crossorigin>
<link rel="preload" href="/fonts/open-sans-bold.woff2" as="font" type="font/woff2" crossorigin>
```

Note: `crossorigin` attribute is required even for same-origin fonts. Testing validates preloading improves performance: measure font load timing with and without preload, verify preloaded fonts load before parsing CSS, test that preload doesn't delay other critical resources, and validate `crossorigin` attribute is present.

**System Fonts vs Web Fonts**: System fonts load instantly but vary across platforms. Use system font stack for optimal performance:

```css
body {
  font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
}
```

Testing validates system fonts: verify fonts render on macOS (San Francisco), Windows (Segoe UI), Android (Roboto), Linux (various), test font weights work (not all system fonts have all weights), check fallback chain works if preferred fonts unavailable, and validate performance (should be instant, no loading).

### 26.2 Variable Fonts

Variable fonts contain multiple weights and styles in a single file.

**Variable Font Benefits**: Variable fonts offer numerous advantages. Single file contains multiple weights (regular, semibold, bold, etc.) instead of separate files for each weight, smooth interpolation between weights (font-weight: 450 is possible, not just 400 or 500), reduced HTTP requests (one file vs 4-6 files for different weights), often smaller total file size than multiple individual fonts, optical sizing adjustments, and custom axes (width, slant, etc.). Testing measures benefits: compare variable font file size to multiple traditional fonts, test font-weight values work correctly (try intermediate weights like 450, 550), verify smooth weight transitions, and validate optical sizing improves readability at different sizes.

**Implementing Variable Fonts**: CSS syntax for variable fonts. Define variable font in @font-face:

```css
@font-face {
  font-family: 'Inter';
  src: url('/fonts/Inter-Variable.woff2') format('woff2');
  font-weight: 100 900; /* Range of weights in variable font */
  font-style: normal;
  font-display: swap;
}
```

Use any weight value:

```css
h1 {
  font-family: 'Inter', sans-serif;
  font-weight: 650; /* Custom weight */
}

p {
  font-family: 'Inter', sans-serif;
  font-weight: 425; /* Fine-tuned weight */
}
```

Use custom axes (if font supports):

```css
.heading {
  font-family: 'Inter', sans-serif;
  font-variation-settings: 'wght' 650, 'wdth' 110, 'slnt' -5;
}
```

Testing validates variable fonts work: test multiple font-weight values (100, 200, 300, ...900, and intermediate values), verify custom weights render correctly, test font-variation-settings custom axes, check variable fonts work across browsers (excellent support in modern browsers), and validate fallback for older browsers.

**Variable Font Axes**: Fonts can have multiple variation axes. Common axes: `wght` (weight, 100-900 typical), `wdth` (width, 75-125 typical), `ital` (italic, 0-1), `slnt` (slant, -15 to 0 typical), `opsz` (optical size, often 8-144). Custom axes font-specific. Testing validates axes: identify supported axes (check font documentation), test each axis at minimum, default, and maximum values, verify axis values between extremes, test axis combinations, and check optical sizing improves readability.

**Variable Font Performance**: While generally beneficial, variable fonts need performance testing. Measure variable font file size vs traditional fonts, test load time on slow connections, measure rendering performance (some GPUs struggle with variable fonts), test memory usage (variable fonts may use more memory), validate smooth animations using font-weight transitions, and check for any rendering glitches. Testing ensures variable fonts provide performance benefits without introducing problems.

**Variable Font Fallbacks**: Older browsers need fallbacks. Provide traditional fonts for browsers without variable font support:

```css
/* Traditional fonts for fallback */
@font-face {
  font-family: 'Inter';
  src: url('/fonts/Inter-Regular.woff2') format('woff2');
  font-weight: 400;
  font-style: normal;
}

@font-face {
  font-family: 'Inter';
  src: url('/fonts/Inter-Bold.woff2') format('woff2');
  font-weight: 700;
  font-style: normal;
}

/* Variable font for modern browsers */
@supports (font-variation-settings: normal) {
  @font-face {
    font-family: 'Inter';
    src: url('/fonts/Inter-Variable.woff2') format('woff2');
    font-weight: 100 900;
    font-style: normal;
  }
}
```

Testing validates fallbacks work: test in older browsers (IE11, old Safari), verify traditional fonts load when variable fonts aren't supported, check font weights display correctly in fallback, and validate progressive enhancement works.

### 26.3 Typography Scales and Hierarchy

Consistent typography scales create visual rhythm and hierarchy.

**Modular Scale**: Mathematical ratios create harmonious type scales. Common ratios: 1.125 (major second), 1.200 (minor third), 1.250 (major third), 1.333 (perfect fourth), 1.414 (augmented fourth), 1.500 (perfect fifth), 1.618 (golden ratio). Example scale using 1.250 ratio with 16px base:

```
16px × 1.250⁰ = 16px (base / body text)
16px × 1.250¹ = 20px (small heading)
16px × 1.250² = 25px (h4)
16px × 1.250³ = 31px (h3)
16px × 1.250⁴ = 39px (h2)
16px × 1.250⁵ = 49px (h1)
```

Testing validates scale: verify all text sizes use scale values (no arbitrary sizes), test hierarchy is clear visually, check scale works at mobile and desktop sizes, validate intermediate sizes exist for edge cases, and test scale creates rhythm without excessive jumps.

**Responsive Typography**: Font sizes should adapt to viewport. Use `clamp()` for fluid typography:

```css
h1 {
  font-size: clamp(28px, 5vw, 48px);
  /* Min 28px, scales with viewport, max 48px */
}

body {
  font-size: clamp(16px, 2.5vw, 18px);
}
```

Use media queries for breakpoint-based scaling:

```css
h1 {
  font-size: 32px;
}

@media (min-width: 768px) {
  h1 {
    font-size: 40px;
  }
}

@media (min-width: 1024px) {
  h1 {
    font-size: 48px;
  }
}
```

Testing validates responsive typography: test at mobile sizes (text should be readable, not too small), test at desktop sizes (text should be comfortable, not too large), test in-between sizes (fluid scaling should be smooth), verify text doesn't become unreadably small, check line lengths remain comfortable (45-75 characters), and validate heading hierarchy remains clear at all sizes.

**Line Height (Leading)**: Line height affects readability significantly. General guidelines: body text: 1.4-1.6 (1.5 is common), headings: 1.1-1.3 (tighter than body), small text (captions): 1.3-1.5, large text (displays): 1.0-1.2. Testing validates line height: verify text is readable (not cramped, not too loose), check multiple lines don't collide (descenders don't touch ascenders), test line height works with various content lengths, validate line height adapts responsively if needed, and verify line height creates visual rhythm.

**Letter Spacing (Tracking)**: Letter spacing affects readability and style. General guidelines: body text: 0 (default) to 0.02em (very subtle), headings: -0.02em to 0 (slightly tighter), all caps: 0.05em to 0.15em (looser), small text: 0 to 0.05em (slightly looser). Testing validates letter spacing: verify body text is readable (appropriate spacing), check headings look balanced, test all-caps text has adequate spacing, validate letter spacing at various sizes, and check letter spacing doesn't cause awkward word spacing.

**Word Spacing**: Word spacing is usually default but may need adjustment. Testing word spacing: verify words have appropriate separation (not cramped, not excessive), test justified text word spacing (can be irregular, requires testing), check word spacing with letter spacing adjustments (interaction), and validate word spacing in headings and body text.

**Line Length (Measure)**: Optimal line length improves readability. Guidelines: body text: 45-75 characters per line (50-65 ideal), narrow columns: 40-50 characters, wide columns: 75-85 characters max. Testing validates line length: count characters per line in body text paragraphs, verify line length at mobile, tablet, and desktop widths, check multi-column layouts have appropriate line lengths, test line length adapts responsively, and validate long lines aren't exhausting to read, short lines aren't choppy.

**Paragraph Spacing**: Space between paragraphs creates clear separation. Use margin-bottom on paragraphs (typically 1-1.5em, equivalent to one blank line) or use margin-top on subsequent paragraphs (creating space between but not after last paragraph), don't use both (creates double spacing). Testing validates paragraph spacing: verify paragraphs have clear separation, check spacing isn't excessive (too much white space), test paragraphs in various contexts (articles, forms, cards), and validate paragraph spacing creates comfortable reading rhythm.

### 26.4 Advanced Typography Properties

Modern CSS provides sophisticated typographic control.

**Font Feature Settings**: OpenType features enable advanced typography. Common features: `liga` (ligatures, e.g., fi → fi), `kern` (kerning, adjusts spacing between specific letter pairs), `onum` (oldstyle numbers, more readable in text), `pnum` (proportional numbers, variable width), `tnum` (tabular numbers, fixed width for tables), `smcp` (small caps), `swsh` (swashes, decorative flourishes), `frac` (automatic fractions, 1/2 → ½). Enable features:

```css
body {
  font-feature-settings: 'liga' 1, 'kern' 1;
}

.numbers-in-table {
  font-feature-settings: 'tnum' 1; /* Tabular numbers for alignment */
}

.small-caps {
  font-feature-settings: 'smcp' 1;
}
```

Testing validates font features: verify ligatures render correctly (fi, fl, ff ligatures), test kerning improves spacing between letters, check oldstyle vs lining numbers appearance, test tabular numbers align vertically in tables, validate small caps render (not just scaled down capitals), verify fractions render properly, and check font features work across browsers (modern browsers support, older may not).

**Text Rendering Optimization**: Control how text is rendered. Properties: `text-rendering: optimizeLegibility` (enables kerning and ligatures, can impact performance), `text-rendering: optimizeSpeed` (faster rendering, may reduce quality), `text-rendering: geometricPrecision` (precise rendering, slower). `-webkit-font-smoothing: antialiased` and `-moz-osx-font-smoothing: grayscale` reduce font weight on macOS (non-standard properties). Testing measures impact: compare rendering quality with different settings, measure rendering performance (optimizeLegibility can slow rendering of lots of text), test cross-browser consistency, verify readability isn't degraded, and validate font smoothing improves or degrades appearance.

**Hyphenation**: Automatic hyphenation improves text flow in narrow columns. Enable hyphenation:

```css
.narrow-column {
  hyphens: auto;
  hyphenate-limit-chars: 6 3 2; /* Minimum word length, min chars before break, min chars after break */
}
```

Set language for correct hyphenation rules:

```html
<p lang="en">This text will be hyphenated according to English rules.</p>
```

Testing validates hyphenation: verify hyphenation works (words break appropriately), test hyphenation with various content, check hyphenation respects language rules (set `lang` attribute), validate hyphenation improves readability in narrow columns, test hyphenation doesn't create excessive breaks (adjust limits), verify browser support (Safari, Firefox support, Chrome support is inconsistent), and check hyphenation in justified text.

**Text Wrapping and Overflow**: Control how text wraps and handles overflow. Properties: `word-wrap: break-word` (breaks long words to prevent overflow), `overflow-wrap: break-word` (same as word-wrap), `word-break: break-all` (breaks anywhere, even mid-word), `word-break: keep-all` (doesn't break between words in CJK text), `text-overflow: ellipsis` (truncates with ...), `white-space: nowrap` (prevents wrapping), `white-space: pre-wrap` (preserves whitespace and wraps). Testing validates wrapping behavior: test long words and URLs don't overflow containers, verify break-word doesn't break inappropriately, test CJK text wrapping respects word boundaries, validate ellipsis appears when text is truncated, check white-space settings preserve intended formatting, and test wrapping behavior responsively.

**Hanging Punctuation**: Punctuation can hang outside text block for optical alignment. Enable hanging punctuation:

```css
.quote {
  hanging-punctuation: first last;
}
```

Testing validates hanging punctuation (limited browser support—primarily Safari): verify opening quotes hang outside text block, check closing punctuation hangs, test fallback for unsupported browsers (graceful degradation), and validate optical alignment improves appearance.

**Orphans and Widows**: Control single lines at start/end of pages or columns. Properties: `orphans: 2` (minimum lines at bottom of page before break), `widows: 2` (minimum lines at top of page after break). Testing validates orphan/widow control: test multi-page printing (check if orphans/widows are controlled), verify single lines aren't stranded, check column breaks respect settings, and validate browser support (primarily effects printing and multi-column layouts).

### 26.5 Web Font Licensing and Legal Compliance

Font licensing is often overlooked but legally critical.

**Font License Types**: Different licenses allow different usage. Desktop licenses: for use in design software (Photoshop, Sketch, Figma), not for web embedding. Webfont licenses: allow @font-face embedding, usually have pageview limits or domains restrictions. App licenses: for mobile apps, separate from web licenses. Server licenses: for server-side rendering (PDFs, images). Testing validates licensing: confirm fonts have appropriate web licenses, verify usage complies with license terms (pageview limits, domain restrictions), check licenses cover all domains (production, staging, development if restricted), validate licenses are current (not expired), and document licenses and restrictions.

**Self-Hosted vs Font Services**: Each approach has licensing implications. Self-hosted fonts: must have web font license for each font, responsible for compliance, need to manage updates and optimization. Font services (Google Fonts, Adobe Fonts, Fonts.com): licensing handled by service (usually free or included in subscription), automatic updates and optimization, may have terms of service requirements. Testing validates: self-hosted fonts have valid licenses, font service usage complies with terms of service, appropriate fonts are used for intended purpose (free fonts for open-source projects, licensed fonts for commercial sites), and licenses are documented for team reference.

**Font Subsetting and Modification**: Licenses may restrict modification. Some licenses prohibit subsetting or modification (must use complete font file), other licenses allow subsetting for web performance, commercial fonts often have specific terms. Testing validates: subsetting complies with license, modifications (if any) are allowed, and license terms are respected.

### 26.6 Typography Accessibility

Typography must be accessible to all users, including those with low vision, dyslexia, and cognitive disabilities.

**Minimum Font Size**: Text must be large enough to read. WCAG doesn't specify minimum font size but requires text can be resized to 200% without loss of functionality (Success Criterion 1.4.4). Practical recommendations: body text minimum 16px (smaller than 16px triggers zoom on iOS), small text (captions, footnotes) minimum 14px, large headings can be larger than 24px. Testing validates: all body text is at least 16px, smaller text is at least 14px, text can be enlarged to 200% zoom without breaking layout, and text remains readable at 200% zoom.

**Font Choice for Readability**: Some fonts are more readable than others. Recommendations: sans-serif fonts generally more readable on screens (Helvetica, Arial, Open Sans, Roboto), serif fonts traditional for print but work on high-resolution screens (Georgia, Merriweather), avoid decorative or script fonts for body text, ensure adequate x-height (taller lowercase letters improve readability), and test fonts with actual users. Testing validates: chosen fonts are readable, fonts work at various sizes, font weights are distinct, and users with low vision find fonts readable.

**Dyslexia-Friendly Typography**: Some typographic choices help users with dyslexia. Recommendations: adequate letter spacing (0.12em recommended), adequate word spacing (0.16em recommended), adequate line height (1.5 minimum, 2.0 better for some users), sans-serif fonts often easier (avoid serif fonts with ambiguous letters like 'l' and 'I'), avoid fully justified text (uneven word spacing is challenging), use left-aligned text (ragged right edge helps track lines), adequate line length (40-60 characters for dyslexic readers), and use dyslexia-friendly fonts optionally (OpenDyslexic, Dyslexie, though research on effectiveness is mixed). Testing validates: text spacing meets WCAG 2.2 requirements (Success Criterion 1.4.12: Text Spacing), line height is adequate, text alignment supports readability, and line length is comfortable.

**Color Contrast in Typography**: Text must meet WCAG contrast requirements. Requirements: normal text (<24px) needs 4.5:1 contrast ratio minimum (AA), large text (24px+, or 19px+ bold) needs 3:1 contrast minimum (AA), for AAA compliance: 7:1 for normal text, 4.5:1 for large text. Testing validates: all text meets minimum contrast requirements (use contrast checkers), text over images has sufficient contrast (test at various image positions), colored text meets contrast requirements, light text on dark backgrounds meets requirements (dark mode), and placeholder text meets contrast requirements (4.5:1 like regular text).

**Responsive Typography for Accessibility**: Typography must work at all viewport sizes and zoom levels. Testing validates: text is readable without horizontal scrolling at 320px width (Success Criterion 1.4.10: Reflow), text is readable at 200% zoom (Success Criterion 1.4.4: Resize Text), text doesn't overlap at high zoom, text remains readable on mobile devices, line length remains comfortable at all sizes, and heading hierarchy remains clear at all sizes.

### 26.7 Typography Testing Checklist

Comprehensive typography testing checklist:

**Font Loading**:
☐ Web fonts load correctly
☐ Flash of invisible text (FOIT) is minimized or eliminated
☐ Flash of unstyled text (FOUT) is brief and non-disruptive
☐ font-display strategy is appropriate
☐ Critical fonts are preloaded
☐ Fallback fonts provide acceptable experience
☐ Font file sizes are optimized (compressed, subset if appropriate)
☐ Font loading doesn't block page render significantly

**Font Implementation**:
☐ All font families load correctly
☐ All font weights work correctly (check all weights used)
☐ Font styles (italic, oblique) work correctly
☐ Variable fonts work correctly (if used)
☐ Font axes work correctly (if using variable fonts)
☐ Font licensing is compliant (web licenses for all fonts)

**Typography Scale and Hierarchy**:
☐ Type scale is consistent (no arbitrary sizes)
☐ Heading hierarchy is clear (h1 largest, h6 smallest)
☐ Body text size is readable (16px minimum)
☐ Line height is appropriate (1.4-1.6 for body, 1.1-1.3 for headings)
☐ Letter spacing is appropriate
☐ Word spacing is appropriate
☐ Line length is comfortable (45-75 characters for body text)
☐ Paragraph spacing is clear

**Responsive Typography**:
☐ Typography scales appropriately at mobile sizes
☐ Typography scales appropriately at desktop sizes
☐ Line length remains comfortable at all viewport widths
☐ Heading hierarchy remains clear at all sizes
☐ Text is readable without horizontal scrolling at 320px

**Advanced Typography**:
☐ OpenType features work correctly (ligatures, kerning)
☐ Text rendering is optimized
☐ Hyphenation works appropriately (if used)
☐ Text wrapping handles long words and URLs
☐ Text overflow is handled gracefully
☐ Orphans and widows are controlled (for print)

**Accessibility**:
☐ All text meets contrast requirements (4.5:1 normal, 3:1 large)
☐ Text can be resized to 200% without breaking layout
☐ Text spacing can be adjusted per WCAG 2.2 (1.4.12)
☐ Font choice supports readability (no decorative fonts for body text)
☐ Line height supports readability (1.5 minimum)
☐ Text alignment supports readability (left-aligned or justified carefully)
☐ Line length supports readability (dyslexia considerations)

**Cross-Platform Testing**:
☐ Typography tested on Windows (ClearType rendering)
☐ Typography tested on macOS (sub-pixel rendering, Retina)
☐ Typography tested on iOS (mobile Safari)
☐ Typography tested on Android (various devices)
☐ Typography tested on Linux (various configurations)
☐ Typography renders acceptably across all platforms

---
