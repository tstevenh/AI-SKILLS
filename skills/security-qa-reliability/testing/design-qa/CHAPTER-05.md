# 5. Typography Consistency


Typography is fundamental to user interface design, affecting readability, visual hierarchy, brand identity, and overall user experience. Consistent typography implementation requires meticulous attention to font families, sizes, weights, line heights, letter spacing, and other typographic properties. Typography QA ensures that text appears exactly as designed across all contexts, devices, and browsers, maintaining both aesthetic quality and functional readability.

### 5.1 Typography Fundamentals for QA

Understanding typography fundamentals provides the foundation for effective testing.

**Font Families and Fallbacks**: Web typography relies on font stacks—ordered lists of font families where browsers use the first available font. Testing must verify that preferred fonts load correctly, fallback fonts activate when primary fonts unavailable, font loading doesn't cause layout shifts (FOUT - Flash of Unstyled Text or FOIT - Flash of Invisible Text), web fonts deliver at correct weights and styles, and variable fonts (if used) render properly across their full range.

**Font Weights**: Modern interfaces use multiple font weights to establish hierarchy. Common weights include Thin (100), Extra Light (200), Light (300), Regular (400), Medium (500), Semi-Bold (600), Bold (700), Extra Bold (800), and Black (900). Testing validates that all used weights load correctly, weights match design specifications exactly, faux bold (browser-synthesized bold) isn't used when real weights are available, and weight variations render distinctly enough to be meaningful.

**Font Sizes**: Font sizes create visual hierarchy and ensure readability. Testing checks that heading sizes create clear hierarchy (h1 > h2 > h3, etc.), body text meets minimum readability standards (16px minimum for body text), sizes scale appropriately across responsive breakpoints, relative sizing (em, rem) behaves correctly, and size relationships match design system ratios.

**Line Height (Leading)**: Line height affects readability and visual density. Testing validates that line heights are appropriate for font sizes (typically 1.4-1.6 for body text), headings use tighter line height than body (often 1.1-1.3), sufficient vertical spacing exists between text blocks, multi-line text remains readable, and line height doesn't cause text clipping or overlap.

**Letter Spacing (Tracking)**: Letter spacing affects text density and readability. Testing checks that letter spacing matches design specifications, all-caps text has appropriate positive tracking, negative tracking (if used) doesn't compromise legibility, letter spacing adjusts appropriately at responsive breakpoints, and letter spacing doesn't cause text overflow.

**Word Spacing**: Less commonly adjusted than letter spacing, word spacing can significantly impact readability when modified. Testing validates that word spacing modifications are intentional, justified text has appropriate word spacing, word spacing doesn't create rivers of whitespace, and custom word spacing doesn't break text layout.

**Text Alignment**: Text alignment affects readability and aesthetics. Testing validates that body text uses left alignment (or right for RTL languages), centered text is used appropriately (not for long passages), right alignment is intentional and purposeful, justified text has acceptable spacing, and alignment changes appropriately across breakpoints.

### 5.2 Font Loading and Performance

Font loading impacts both performance and visual consistency, requiring careful testing.

**Font Loading Strategies**: Modern web fonts use various loading strategies. Testing should verify behavior of different strategies: `font-display: swap` (show fallback immediately, swap to web font when loaded), `font-display: block` (brief invisible period, then show web font), `font-display: fallback` (very brief invisible period, swap to web font if quick, otherwise stick with fallback), `font-display: optional` (use web font only if immediately available), and custom loading logic. Each strategy has different visual implications.

**FOUT and FOIT Detection**: Flash of Unstyled Text (FOUT) shows fallback font briefly before web font loads. Flash of Invisible Text (FOIT) renders text invisibly while web font loads. Both create poor experiences. Testing identifies FOUT/FOIT occurrences, measures duration of flashes, validates mitigation strategies, and checks for layout shifts when fonts swap. Ideally, fallback fonts closely match web font metrics to minimize shifts.

**Font Preloading**: Critical fonts can be preloaded with `<link rel="preload" as="font">` to improve performance. Testing validates that preloaded fonts actually load faster, preloading doesn't delay other critical resources, preloaded fonts match fonts actually used, and preload doesn't cause unnecessary downloads.

**Font Subsetting**: Subsetting reduces font file sizes by including only needed characters. Testing ensures that subsets include all necessary characters, no missing glyphs cause fallback to other fonts, subset definitions match actual content needs, and different language versions load appropriate subsets.

**Variable Font Loading**: Variable fonts pack multiple weights and styles into one file. Testing validates that variable fonts load correctly, all weight and style variations render properly, browser support is adequate or fallbacks exist, and file size benefits materialize in practice.

**Font Loading Performance**: Performance testing for fonts includes measuring time to first text render, checking total font download size, validating caching headers, testing behavior on slow connections, and confirming font loading doesn't block page interaction.

### 5.3 Typography in Responsive Design

Typography must adapt across viewport sizes to maintain readability and hierarchy.

**Responsive Font Sizes**: Font sizes often scale with viewport size. Testing validates that font sizes increase/decrease appropriately, maintain readability at smallest viewports (minimum 16px for body text on mobile), preserve hierarchy at all viewport sizes, use appropriate scaling methods (media queries, clamp(), vw units), and transitions between sizes are smooth (with fluid typography).

**Fluid Typography**: CSS clamp() enables fluid typography that scales smoothly between viewport sizes. Testing fluid typography includes validating minimum and maximum sizes are appropriate, scaling rate is neither too fast nor too slow, hierarchy is maintained throughout range, and formula calculations produce expected results. For example: `font-size: clamp(1rem, 0.5rem + 2vw, 2rem)` scales between 1rem and 2rem based on viewport width.

**Breakpoint-Specific Typography**: Typography often changes at breakpoints. Testing checks that font sizes adjust at appropriate breakpoints, weight changes (if any) enhance mobile readability, line heights adapt for viewport size, heading hierarchy adjusts if needed, and changes are consistent across similar components.

**Mobile Typography Considerations**: Small screens require specific typography considerations. Testing validates that text is large enough to read without zooming (16px minimum), line lengths aren't too long or too short (45-75 characters ideal), tap targets in text (links) meet minimum sizes, and density is appropriate for touch interaction.

**Reading Width Control**: Optimal line length enhances readability. Testing ensures that content width is constrained for readability (66-75 characters per line for optimal reading), constraints scale appropriately across viewports, narrow viewports don't create excessively short lines, and wide viewports don't create excessively long lines.

### 5.4 Typography Accessibility

Accessible typography ensures content is readable by everyone, including users with visual impairments.

**Minimum Font Sizes**: WCAG doesn't specify minimum font sizes, but best practices recommend 16px for body text, minimum 14px for any text except fine print, proportionally larger sizes for headings, and caution with small text (should only be used sparingly). Testing validates these minimums are met.

**Contrast Ratios**: Text must have sufficient contrast against backgrounds. WCAG requirements include 4.5:1 for normal text (AA), 3:1 for large text (18pt or 14pt bold) (AA), 7:1 for normal text (AAA), and 4.5:1 for large text (AAA). Testing must validate contrast ratios for all text against all possible backgrounds, including hover states, overlays, and dynamic backgrounds.

**Font Weight and Contrast**: Very thin font weights can compromise readability even with adequate color contrast. Testing checks that thin weights (100, 200, 300) have higher color contrast or are used only for large text, regular weights (400, 500) are used for body text, and bold weights enhance legibility where needed.

**Line Height for Readability**: WCAG 1.4.12 requires line height of at least 1.5 for paragraphs, space between paragraphs at least 2x font size, letter spacing at least 0.12x font size, and word spacing at least 0.16x font size. Testing validates these minimums are met and can be overridden by users.

**Text Resizing**: Users must be able to resize text up to 200% without loss of functionality or content. Testing validates that text can be resized in browser settings, layouts don't break when text is enlarged, no text is clipped or truncated, all functionality remains accessible, and horizontal scrolling is not required.

**Fonts and Dyslexia**: While no font is universally better for dyslexia, certain characteristics help. Consider testing with clear, distinct letter shapes, adequate spacing between letters and words, generous line height, and avoiding overly decorative fonts for body text. OpenDyslexic and similar fonts are options but not required.

### 5.5 Typography Consistency Testing

Ensuring consistent typography across an application requires systematic testing.

**Design System Typography Audit**: Auditing design system typography establishes baseline expectations. Audit should document all defined type styles (heading levels, body variants, labels, captions), specify exact properties for each style (family, size, weight, line-height, letter-spacing), identify where each style should be used, document responsive variations, and establish acceptable variation tolerances.

**Heading Hierarchy Validation**: Proper heading hierarchy is both a design and accessibility concern. Testing validates that heading levels are used semantically (h1 for page title, h2 for sections, etc.), no heading levels are skipped, visual hierarchy matches semantic hierarchy, heading styles are consistent across application, and headings create clear content structure.

**Automated Typography Testing**: Automated tests can validate typography programmatically. Tests might query computed font properties, compare against design specifications, validate that correct CSS classes are applied, check for unintended inline styles overriding system styles, and flag use of non-standard font sizes or weights. Tools like Playwright and Cypress enable automated property checking.

**Visual Regression for Typography**: Visual regression testing catches unintended typography changes. This includes capturing baselines of typography specimens, comparing implementations against baselines, flagging unexpected font changes, detecting size or spacing variations, and validating web font loading doesn't cause regressions.

**Cross-Browser Typography Rendering**: Typography renders differently across browsers and operating systems. Testing should capture screenshots across major browsers (Chrome, Firefox, Safari, Edge), compare rendering across platforms (Windows, macOS, iOS, Android), document acceptable variations, flag problematic differences, and ensure readability is maintained everywhere.

**Component Typography Consistency**: Components using similar contexts should have consistent typography. Testing validates that all buttons use same typography, form labels are consistent, error messages match styling, navigation items are uniform, and card titles, lists, and other repeated patterns maintain consistency.

### 5.6 Special Typography Scenarios

Certain scenarios present unique typography testing challenges.

**Truncation and Ellipsis**: Text truncation prevents overflow but must be tested carefully. Validation includes ensuring truncation occurs only when necessary, ellipsis ("...") indicate truncation clearly, full text is accessible (tooltip, expansion, etc.), truncation doesn't hide critical information, and truncation breakpoints are appropriate for different viewports.

**Multi-line Heading Handling**: Long headings may wrap across multiple lines. Testing checks that line breaks occur at appropriate points, line height is appropriate for multi-line, multi-line headings maintain hierarchy, excessive line breaks are avoided (through width constraints), and manual line breaks (if used) are positioned semantically.

**Internationalization and Localization**: Different languages have different typography needs. Testing should validate adequate space for text expansion (German, Finnish), support for non-Latin scripts (Arabic, Chinese, Japanese, Korean), correct handling of RTL languages, appropriate fonts for each language, and preserved hierarchy in all translations.

**Special Characters and Symbols**: Special characters must render correctly. Testing validates that common symbols render in chosen fonts (©, ®, ™, •), proper quotes are used (" " rather than " "), dashes are correct type (en-dash, em-dash), mathematical symbols appear correctly, and currency symbols display properly.

**Code Typography**: Code snippets require monospace fonts and special handling. Testing ensures monospace fonts load correctly, code blocks are clearly distinguished from body text, inline code is visually distinct, syntax highlighting (if used) is legible, and code wrapping or scrolling is appropriate.

**Fine Print and Legal Text**: Small legal text must balance compactness with legibility. Testing validates that minimum font sizes are respected, contrast is sufficient even for small text, line length is appropriate, and users can zoom or enlarge if needed.

### 5.7 Typography Tools and APIs

Various tools assist with typography testing and validation.

**Typography Bookmarklets**: Browser bookmarklets can reveal typography information. Examples include Type Sample (displays font family, size, line-height for selected text), WhatFont (identifies fonts on hover), and Fontalyzer (analyzes typography across page).

**Browser DevTools**: DevTools provide detailed typography information. Chrome and Firefox DevTools show computed font properties, visualize line height and spacing, highlight text nodes, identify loaded font files, and simulate font loading states.

**Type Scale Calculators**: Tools like typescale.com and type-scale.com help validate type scales. They generate proportional type scales based on ratios, visualize size relationships, export CSS, and help identify whether implementation matches design system ratios.

**Font Testing Services**: Online services validate font loading and rendering. FontFace Ninja, Fount, and Typecast help identify fonts, test fallback behavior, preview web fonts, and analyze font loading performance.

**Accessibility Checking Tools**: Automated accessibility tools check typography-related issues. axe DevTools checks contrast ratios, validates text resizing, identifies heading hierarchy issues, and flags typography-related WCAG violations.

**Font Analytics**: Understanding font usage helps prioritize testing. Font analytics track which fonts are actually used, measure loading performance, identify unused font weights or styles, and detect inconsistent font usage.

**Programmatic Font Checking**: Libraries like opentype.js and fontkit enable programmatic font analysis. They can parse font files, extract glyph data, measure character widths, validate font subsetting, and check font format support.

### 5.8 Typography Testing Best Practices

Established best practices improve typography QA effectiveness.

**Establish a Type System**: Before testing, establish a clear type system defining all text styles, their properties, and usage contexts. This provides a specification to test against and ensures consistency.

**Test with Real Content**: Lorem ipsum doesn't reveal how typography handles real content. Test with actual headlines, body copy, varying content lengths, special characters users will encounter, and translations in target languages.

**Check Fallback Scenarios**: Don't just test happy path font loading. Validate fallback fonts when web fonts fail, behavior on slow connections, appearances before web fonts load, and layouts when fallback metrics differ from web fonts.

**Validate Across Platforms**: Typography rendering varies significantly across operating systems. Test on Windows, macOS, iOS, and Android to ensure acceptable rendering everywhere. Pay particular attention to Windows font rendering differences.

**Include Performance in QA**: Typography performance impacts user experience. Monitor font loading times, track layout shifts from font swapping, measure total font download size, and validate caching is effective.

**Document Typography Bugs Clearly**: Typography bugs can be subtle. Document bugs with screenshots, exact specifications (expected vs actual), viewport and browser information, and steps to reproduce. Include font loading timeline if relevant.

**Automate Where Possible, Inspect Manually**: Automated tests catch regressions and property deviations. Manual review evaluates readability, hierarchy effectiveness, and aesthetic quality. Combine both approaches for comprehensive coverage.

---
