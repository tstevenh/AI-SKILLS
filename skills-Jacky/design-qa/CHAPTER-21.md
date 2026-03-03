# 21. Accessibility Visual QA - WCAG 2.2 AA/AAA


Accessibility visual QA ensures that designs are perceivable, operable, understandable, and robust for all users, including those with disabilities. Accessibility isn't optional—it's a legal requirement in many jurisdictions (ADA in US, EAA in EU, AODA in Canada) and a moral imperative for inclusive design. This comprehensive section covers WCAG 2.2 Level AA and AAA criteria with specific focus on visual and design QA aspects.

### 21.1 WCAG 2.2 Overview and Principles

WCAG (Web Content Accessibility Guidelines) 2.2, published October 2023, is the current standard for web accessibility.

**Four Principles (POUR)**: WCAG is organized around four principles. **Perceivable**: Information and user interface components must be presentable to users in ways they can perceive. This means providing text alternatives for non-text content, providing captions and alternatives for multimedia, creating content that can be presented in different ways without losing meaning, and making it easier for users to see and hear content. **Operable**: User interface components and navigation must be operable. This means making all functionality available from a keyboard, giving users enough time to read and use content, not designing content in a way that causes seizures, and providing ways to help users navigate and find content. **Understandable**: Information and the operation of user interface must be understandable. This means making text readable and understandable, making content appear and operate in predictable ways, and helping users avoid and correct mistakes. **Robust**: Content must be robust enough that it can be interpreted reliably by a wide variety of user agents, including assistive technologies. This means maximizing compatibility with current and future user tools.

**Conformance Levels**: WCAG defines three levels. **Level A**: Minimum level of accessibility; if not met, some users will be unable to access content. **Level AA**: Deals with the biggest and most common barriers; legally required in many jurisdictions. **Level AAA**: Highest level of accessibility; not required to conform to all AAA criteria, but encouraged to meet where possible. Most organizations target Level AA conformance with selective AAA criteria.

**WCAG 2.2 New Success Criteria**: WCAG 2.2 adds nine new success criteria to 2.1: 2.4.11 Focus Not Obscured (Minimum) - Level AA, 2.4.12 Focus Not Obscured (Enhanced) - Level AAA, 2.4.13 Focus Appearance - Level AAA, 2.5.7 Dragging Movements - Level AA, 2.5.8 Target Size (Minimum) - Level AA, 3.2.6 Consistent Help - Level A, 3.3.7 Redundant Entry - Level A, 3.3.8 Accessible Authentication (Minimum) - Level AA, and 3.3.9 Accessible Authentication (Enhanced) - Level AAA. Design QA must address all applicable criteria.

### 21.2 Color Contrast - Success Criterion 1.4.3 (AA) and 1.4.6 (AAA)

Color contrast ensures text is readable for users with low vision or color blindness.

**Level AA Requirements (1.4.3)**: Text and images of text must have contrast ratio of at least: 4.5:1 for normal text (below 24px or below 19px bold), 3:1 for large text (24px+ or 19px+ bold), and 3:1 for UI components and graphical objects. Exceptions: incidental text (text in inactive UI components, pure decoration, invisible, part of logo), and no requirement for logotypes.

**Level AAA Requirements (1.4.6)**: Enhanced contrast: 7:1 for normal text, 4.5:1 for large text. These ratios are harder to achieve but provide better accessibility.

**Testing Color Contrast**: Multiple tools and methods exist. Browser DevTools: Chrome, Firefox, Edge show contrast ratios in color picker. Tools: WebAIM Contrast Checker (online), Colour Contrast Analyser (desktop app), accessible color palette generator tools, browser extensions (WAVE, axe DevTools), and automated testing (pa11y, axe-core). Manual testing process: 1) Identify all text on page. 2) For each text element, determine foreground color and background color. 3) Calculate contrast ratio (tools do this automatically). 4) Verify ratio meets requirements (4.5:1 for normal text, 3:1 for large text, 3:1 for UI components). 5) Document failures. 6) Recommend compliant color alternatives.

**Common Contrast Issues**: Certain design patterns consistently cause contrast problems. Light gray text on white backgrounds (very common, often fails). Colored text on colored backgrounds (decorative but often low contrast). Text over images (background varies, making consistent contrast difficult). Placeholder text (often too light, fails contrast requirements—placeholders need 4.5:1 like regular text). Disabled form controls (historically gray, but WCAG 2.2 requires contrast for disabled controls to identify them). Link text that relies only on color (must have 3:1 contrast vs surrounding text or non-color differentiation). Transparent or translucent overlays (background bleeds through, reducing contrast).

**Solutions for Contrast Issues**: Darken light text or lighten dark backgrounds to meet ratios. For text over images: add solid background color behind text, use semi-transparent overlay to darken image behind text, add text stroke or shadow (subtle, maintain readability), or use images with predictable tone (dark images with light text, light images with dark text). For placeholder text: use darker placeholder color, or avoid relying on placeholder text (use labels outside inputs). For disabled controls: maintain sufficient contrast or visually hide disabled controls with screen reader announcement.

**Testing Edge Cases**: Some scenarios require careful testing. Gradient backgrounds: test contrast at each point text overlaps gradient (worst-case contrast must meet requirements). Animated backgrounds: contrast must meet requirements throughout animation. User-generated content: if users can set colors (themes, customization), test that all combinations meet contrast requirements or prevent inaccessible combinations. Dark mode: requires separate contrast testing (light text on dark backgrounds). Text over video: extremely challenging; provide alternatives like solid background option or captions.

**Contrast for UI Components (WCAG 2.2)**: Non-text contrast 1.4.11 requires 3:1 contrast ratio for: user interface components (buttons, form controls, focus indicators), graphical objects conveying information (icons, charts, graphs). Testing validates all buttons and form controls have 3:1 contrast with adjacent colors, focus indicators have 3:1 contrast with focused element and surrounding content, icons that convey information have 3:1 contrast, and chart elements are distinguishable with 3:1 contrast.

**Color Contrast Testing Checklist**:
☐ All normal text (<24px) has 4.5:1 contrast (AA) or 7:1 (AAA)
☐ All large text (24px+) has 3:1 contrast (AA) or 4.5:1 (AAA)
☐ All UI components have 3:1 contrast
☐ All meaningful graphics have 3:1 contrast
☐ Placeholder text has sufficient contrast
☐ Disabled elements are distinguishable
☐ Link text has contrast vs surrounding text
☐ Text over images maintains contrast
☐ Focus indicators have 3:1 contrast
☐ Contrast is tested in all modes (light/dark)
☐ Gradient and animated backgrounds maintain contrast
☐ All color combinations in themes/customization meet requirements

### 21.3 Use of Color - Success Criterion 1.4.1 (A)

Color must not be the only means of conveying information.

**Requirement**: Color is not used as the only visual means of conveying information, indicating an action, prompting a response, or distinguishing a visual element. This means if information is conveyed with color, another visual indicator must also be present (text, icon, pattern, underline, etc.).

**Common Violations**: Links identified only by color (blue text without underline or icon). Form validation errors shown only with red border. Charts with color-coded legend and no other differentiation (patterns, labels). Status indicators using only color (green for success, red for error). Required fields marked only with red asterisk (red alone isn't sufficient). Calendar events differentiated only by color.

**Solutions**: Links: underline links or use icon/chevron to indicate clickability. Form errors: add icon (X, warning triangle), add error text explaining issue, add aria-invalid attribute, and use visual indicator beyond color (icon, border style change). Charts: add patterns to differentiate data series, add direct labels to chart elements, use different line styles (solid, dashed, dotted), and provide data table alternative. Status indicators: add text label ("Success", "Error"), add icon (checkmark, X), and use shape differences (circle, square, triangle). Required fields: use text label ("Required"), use asterisk with text legend explaining asterisk meaning, and ensure visual indicator beyond color.

**Testing Use of Color**: Testing requires identifying information conveyed by color and verifying alternative indicators exist. Process: 1) Review page and identify all information conveyed with color (links, errors, status, charts, etc.). 2) For each instance, verify whether non-color indicator exists. 3) Test by viewing page in grayscale (simulates color blindness)—can you still distinguish all information? 4) Test with color blindness simulators (simulate various types of color blindness). 5) Document violations where color is sole indicator. 6) Recommend adding non-color indicators.

**Color Blindness Types**: Understanding color blindness guides design. Protanopia (red-blind, ~1% males): red appears dark gray. Deuteranopia (green-blind, ~1% males): green appears beige/tan. Tritanopia (blue-blind, ~0.01% people): blue appears greenish. Achromatopsia (complete color blindness, rare): sees only grayscale. Design should work for all types, which generally means ensuring information isn't conveyed solely by color.

**Use of Color Checklist**:
☐ Links have non-color indicator (underline, icon, or 3:1 contrast + indicator on hover/focus)
☐ Form errors use icon or text, not color alone
☐ Required fields indicated by text or icon, not color alone
☐ Charts use patterns or labels in addition to color
☐ Status indicators use icon or text, not color alone
☐ Calendar events use icon or pattern, not color alone
☐ Information conveyed by color has non-color alternative
☐ Page is usable in grayscale
☐ Page is usable with color blindness simulation

### 21.4 Focus Visible - Success Criterion 2.4.7 (AA) and Focus Appearance 2.4.13 (AAA)

Keyboard users must be able to see which element has focus.

**Level AA Requirements (2.4.7 Focus Visible)**: Any keyboard operable user interface has a mode of operation where the keyboard focus indicator is visible. This means when users tab through the page, they must be able to see which element is focused. Focus indicators can be browser default or custom, but must be clearly visible.

**Level AAA Requirements (2.4.13 Focus Appearance)**: Focus indicator meets: minimum area of at least 2px thick perimeter or equivalent, minimum contrast of 3:1 between focused and unfocused states, and minimum contrast of 3:1 against adjacent colors. Additionally, WCAG 2.2 adds 2.4.11 Focus Not Obscured (Minimum) - AA: when element receives focus, it must not be entirely hidden by author-created content, and 2.4.12 Focus Not Obscured (Enhanced) - AAA: when element receives focus, no part of it is hidden by author-created content.

**Custom Focus Indicators**: Browsers provide default focus indicators (typically blue outline), but custom indicators often improve design integration. Best practices: maintain or exceed default visibility, ensure consistent focus indicators across site, use outline or box-shadow (not border, which affects layout), ensure 3:1 contrast with focused element and adjacent content, make indicator at least 2px thick (AAA requirement), and test with actual keyboard users. Example custom focus indicator:

```css
/* Basic custom focus indicator */
:focus {
  outline: 2px solid #4A90E2;
  outline-offset: 2px;
}

/* Use :focus-visible to show focus only for keyboard navigation */
:focus:not(:focus-visible) {
  outline: none;
}

:focus-visible {
  outline: 2px solid #4A90E2;
  outline-offset: 2px;
}

/* Focus indicator with contrast consideration */
button:focus-visible {
  outline: 2px solid #000;
  outline-offset: 2px;
}

.light-background button:focus-visible {
  outline: 2px solid #000;
}

.dark-background button:focus-visible {
  outline: 2px solid #FFF;
}
```

**Testing Focus Indicators**: Focus testing requires keyboard navigation. Process: 1) Navigate page using only keyboard (Tab, Shift+Tab, Enter, Space, Arrow keys). 2) As you tab through, verify visible focus indicator appears on each focusable element. 3) Check that focus indicator has sufficient contrast (3:1 with element and adjacent content). 4) Verify focus indicator is at least 2px thick (measure in DevTools or screenshots). 5) Test that focus isn't obscured by sticky headers, modals, or other overlays. 6) Test focus trap behavior in modals/dialogs. 7) Test skip links provide focus on activation. 8) Document any missing or insufficient focus indicators.

**Common Focus Issues**: Removing focus indicators without replacement (outline: none without alternative). Focus indicator too subtle (thin 1px outline, low contrast). Focus indicator obscured by content (sticky headers covering focused element, modals hiding focused element behind overlay). Focus order doesn't match visual order (CSS positioning creating confusing focus order). Focus lost or trapped inappropriately (focus sent nowhere on action, focus trapped outside modal). Custom components without focus management (custom dropdowns, date pickers without focus indicators).

**Focus Not Obscured**: WCAG 2.2 requires focused elements not be completely hidden. Scenarios requiring testing: sticky headers that might cover focused elements (ensure focused elements scroll into unobscured position). Fixed footers covering focused elements. Modals or overlays obscuring previously focused content. Expandable sections pushing focused elements outside viewport. Testing validates when element receives focus, at least part of it is visible (AA requirement), and ideally all of it is visible (AAA requirement). Implement by ensuring scroll behavior brings focused elements into view, implementing skip links to avoid covered content, managing focus within modals (don't leave focus on obscured element), and ensuring fixed headers/footers have transparent or push-content behavior.

**Focus Indicator Checklist**:
☐ All interactive elements have visible focus indicator
☐ Focus indicator has 3:1 contrast with element
☐ Focus indicator has 3:1 contrast with adjacent content
☐ Focus indicator is at least 2px thick (AAA)
☐ Focus indicator is consistent across site
☐ Focus order matches visual order
☐ Focus isn't lost during interaction
☐ Focus isn't trapped inappropriately
☐ Modals trap focus appropriately (within modal)
☐ Skip links work and receive focus
☐ Focused elements aren't obscured by sticky/fixed elements (AA)
☐ Focused elements are fully visible (AAA)
☐ Custom components have focus indicators

### 21.5 Target Size - Success Criterion 2.5.5 (AAA) and 2.5.8 (AA)

Touch and click targets must be large enough for easy interaction.

**Level AAA (2.5.5 Target Size)**: The size of the target for pointer inputs is at least 44×44 CSS pixels. Exceptions: equivalent (another control on same page providing same function meets size requirement), inline (target is in a sentence or block of text), user agent control (size controlled by user agent, not author), and essential (particular size is essential to the information being conveyed).

**Level AA (2.5.8 Target Size - Minimum)**: New in WCAG 2.2. The size of the target for pointer inputs is at least 24×24 CSS pixels, except: spacing (undersized targets have at least 24px spacing to next target), equivalent, inline, user agent control, and essential. This lower threshold makes compliance easier while still significantly improving usability.

**Measuring Target Sizes**: Target size is the area users can click/tap to activate, not necessarily visible size. For buttons and links, it's the entire clickable area including padding. For icons and icon buttons, it's the clickable area, which should be larger than the icon itself. Measurement in DevTools: inspect element, check computed box size including padding, verify width and height both meet requirement (44×44 or 24×24). Common issue: icon buttons with small clickable area—icon might be 20×20 with no padding, creating 20×20 target (fails). Solution: add padding to increase clickable area to 44×44 or 24×24.

**Implementing Adequate Target Sizes**: CSS techniques to ensure compliant targets:

```css
/* Button with adequate target size */
.button {
  min-width: 44px;
  min-height: 44px;
  padding: 12px 20px;
  /* Even if text is small, button is at least 44×44 */
}

/* Icon button with invisible padding for larger target */
.icon-button {
  width: 44px;
  height: 44px;
  padding: 12px;
  border: none;
  background: transparent;
}

.icon-button svg {
  width: 20px;
  height: 20px;
}

/* Small target with adequate spacing (meets 2.5.8) */
.small-target {
  width: 24px;
  height: 24px;
  margin: 12px; /* 24px target + 24px spacing = compliant */
}

/* Link with adequate target size */
a {
  display: inline-block;
  min-height: 44px;
  padding: 12px 8px;
  line-height: 1.5;
}
```

**Touch Target Spacing**: When targets don't meet size requirements, spacing can compensate (for WCAG 2.2 Level AA only). If target is 24×24 or larger but smaller than 44×44, ensure at least 24px spacing to the next target. Spacing is measured as the minimum distance from the edge of one target to the edge of the next. This prevents accidental taps on adjacent targets.

**Common Target Size Issues**: Small icon buttons (icon is 20×20, clickable area is 20×20). Close buttons on modals (often small X icon with minimal target). Dropdown arrows (small chevron with no padding). Pagination controls (small page numbers, previous/next links). Social media icons (small icons without adequate padding). Inline text links (height is just line-height, might be less than 44px). Mobile form controls (checkboxes and radio buttons sometimes too small). Small tags or chips (category tags, filters with small tap areas).

**Testing Target Sizes**: Manual testing is most reliable for target sizes. Process: 1) Identify all interactive elements (buttons, links, form controls, icons). 2) For each element, inspect in DevTools to check computed size including padding. 3) Verify width and height meet 44×44 (AAA) or 24×24 (AA). 4) If targets are 24-44px, measure spacing to adjacent targets (needs 24px minimum for AA). 5) Test on actual touch devices—do targets feel comfortably tappable? 6) Document failures and recommend size or spacing adjustments. Automated tools (axe DevTools, WAVE) can detect some target size issues but manual verification is necessary.

**Target Size Checklist**:
☐ All interactive elements are at least 44×44px (AAA) or 24×24px (AA)
☐ Targets smaller than 44×44 but at least 24×24 have 24px spacing (AA)
☐ Icon buttons have adequate padding to reach target size
☐ Close buttons are large enough
☐ Form controls (checkboxes, radios) are large enough
☐ Dropdown arrows are tappable
☐ Pagination controls are adequately sized
☐ Mobile touch targets are tested on actual devices
☐ Spacing between adjacent targets is adequate
☐ Small targets have exceptions documented (inline, essential, etc.)

### 21.6 Text Spacing - Success Criterion 1.4.12 (AA)

Content must be readable when users adjust text spacing.

**Requirement**: No loss of content or functionality occurs when users set: line height (line spacing) to at least 1.5 times the font size, spacing following paragraphs to at least 2 times the font size, letter spacing (tracking) to at least 0.12 times the font size, and word spacing to at least 0.16 times the font size. This allows users with reading or cognitive disabilities to adjust spacing for better readability.

**Testing Text Spacing**: Text spacing issues arise when designs rely on specific spacing and break when users override. Testing methods: 1) Use text spacing bookmarklet (official WCAG bookmarklet available) that applies required spacing. 2) Use browser extension that allows custom CSS injection. 3) Manually apply CSS:

```css
* {
  line-height: 1.5 !important;
  letter-spacing: 0.12em !important;
  word-spacing: 0.16em !important;
}

p {
  margin-bottom: 2em !important;
}
```

4) After applying spacing, navigate entire site checking for broken layouts, cut-off text, overlapping content, or missing functionality. 5) Document any issues.

**Common Text Spacing Issues**: Fixed height containers that clip content when spacing increases. Overlapping text when letter spacing increases. Broken layouts when line height increases. Buttons or navigation items that clip when word spacing increases. Modals or tooltips that become too tall and extend offscreen. Form labels or validation messages that overlap form controls. Text in SVG or canvas that doesn't respect CSS spacing (difficult to fix—may need alternative presentation).

**Solutions for Text Spacing Issues**: Use min-height instead of fixed height (allows containers to grow). Ensure adequate padding (prevents clipping when spacing increases). Use flexbox or grid layouts that adapt to content size. Avoid absolute positioning for text elements. Test with increased spacing during development. Use overflow: auto on containers to allow scrolling if content exceeds container. Avoid cramming too much text in fixed-size areas.

**Text Spacing Checklist**:
☐ No content is clipped when text spacing is increased
☐ No functionality is lost when text spacing is increased
☐ Layouts adapt gracefully to increased spacing
☐ Containers use min-height, not fixed height
☐ Text doesn't overlap when spacing increases
☐ Buttons and navigation remain functional
☐ Modals and tooltips remain on-screen
☐ Form layouts remain functional
☐ SVG/canvas text has alternatives if spacing doesn't apply

### 21.7 Reflow - Success Criterion 1.4.10 (AA)

Content must reflow for small viewports and zoomed views without requiring two-dimensional scrolling.

**Requirement**: Content can be presented without loss of information or functionality, and without requiring scrolling in two dimensions for: vertical scrolling content at a width equivalent to 320 CSS pixels, and horizontal scrolling content at a height equivalent to 256 CSS pixels. Exceptions: parts of content that require two-dimensional layout for usage or meaning (data tables, maps, diagrams, presentations, games).

**What This Means in Practice**: Users must be able to zoom to 400% (or use viewport of 320px width) without horizontal scrolling on vertical content. This helps users with low vision who need to zoom. It also ensures mobile responsive design works at narrow widths. Testing: 1) Set browser viewport to 1280×1024. 2) Zoom to 400% (which results in effective 320px width). 3) Navigate site—should be able to view all content without horizontal scrolling. 4) Or test directly at 320px viewport width. 5) Document any content requiring horizontal scrolling.

**Common Reflow Issues**: Fixed-width containers (width: 1000px doesn't scale to 320px). Horizontal scroll layouts not marked as exceptions. Large images without max-width. Fixed-width form elements. Tables without responsive handling. Layout breaking at narrow widths. Elements positioned outside viewport.

**Solutions for Reflow**: Use responsive design with mobile-first approach. Avoid fixed widths—use max-width, percentages, or flexible units. Ensure images are responsive (max-width: 100%). Make tables responsive (stacked layout, horizontal scroll for tables, or card-based layout). Test at 320px width during development. Use CSS Grid or Flexbox for adaptive layouts. Provide skip links to avoid long navigation at zoomed levels.

**Reflow Checklist**:
☐ No horizontal scrolling required at 320px width (or 400% zoom)
☐ All content is accessible without two-dimensional scrolling
☐ Images scale appropriately
☐ Tables are responsive or marked as exceptions
☐ Forms work at narrow widths
☐ No fixed-width containers break layout
☐ Navigation is accessible at zoomed levels
☐ Exceptions (data tables, maps) are documented

### 21.8 Non-Text Contrast - Success Criterion 1.4.11 (AA)

User interface components and meaningful graphics must have sufficient contrast.

**Requirement**: Visual presentation of UI components and graphical objects has contrast ratio of at least 3:1 against adjacent colors. This applies to: user interface components (borders of form controls, visual indicators of state), parts of graphics needed to understand content (icons conveying meaning, chart elements), and focus indicators (covered earlier). Exceptions: inactive controls, purely decorative, logos, and cases where the component's appearance is controlled by user agent (browser defaults).

**Testing Non-Text Contrast**: Testing requires identifying UI elements and measuring contrast. Process: 1) Identify all UI components (buttons, form controls, icons). 2) For each component, identify the part that conveys information (button border, checkbox border, icon shape). 3) Measure contrast between component and adjacent background (use color picker and contrast calculator). 4) Verify 3:1 contrast is met. 5) Test different states (default, hover, focus, disabled). 6) Document failures.

**Common Non-Text Contrast Issues**: Light gray borders on form inputs on white background (common failure). Icon buttons with low contrast icons. Disabled controls that are too faint to identify. Focus indicators with insufficient contrast (covered earlier). Chart legends or graph elements with low contrast. Toggle switches with indistinct states. Checkboxes and radio buttons with low contrast borders.

**Solutions**: Darken borders on form controls to meet 3:1 contrast. Use icons with sufficient contrast or add backgrounds. Maintain contrast even on disabled controls (or use aria-disabled with visual hiding). Ensure focus indicators meet 3:1 contrast. Use high-contrast colors in charts and graphics. Design toggle switches with clear visual distinction. Test all states of components.

**Non-Text Contrast Checklist**:
☐ All form control borders have 3:1 contrast
☐ All meaningful icons have 3:1 contrast
☐ All graphic elements conveying information have 3:1 contrast
☐ Focus indicators have 3:1 contrast (covered in 2.4.7)
☐ Toggle switches have clear visual states with sufficient contrast
☐ Checkboxes and radio buttons have sufficient contrast
☐ Disabled controls are distinguishable
☐ Chart and graph elements have sufficient contrast
☐ All interactive component states (hover, active) maintain contrast

### 21.9 Label in Name - Success Criterion 2.5.3 (A)

For UI components with labels that include text, the accessible name must contain the visible text label.

**Requirement**: For UI components with labels that include text or images of text, the accessible name must contain the text presented visually. This allows voice input users to activate controls by speaking the visible label. For example, if a button is visually labeled "Submit", the accessible name should be "Submit" or "Submit Form", not something completely different like "Send".

**Testing Label in Name**: Testing requires comparing visible labels with accessible names. Process: 1) Identify all interactive elements with visible text labels. 2) Inspect each element in DevTools Accessibility panel to see computed accessible name. 3) Verify accessible name contains the visible label text. 4) If mismatch, adjust ARIA labels or visible text to align. 5) Test with voice control (if available) to verify controls can be activated by speaking visible label.

**Common Label in Name Issues**: Button with visible text "Submit" but aria-label="Send form" (voice users can't say "Submit" to activate). Icon button with tooltip "Delete" but aria-label="Remove item" (mismatch). Link text "Read more" but aria-label completely different. Form label text doesn't match input's accessible name. Custom components with visible labels not reflected in accessible names.

**Solutions**: Ensure aria-label, aria-labelledby match or include visible text. If adding context for screen readers, append to visible label rather than replacing: visible text "Submit", accessible name "Submit form" (acceptable). Avoid overriding visible labels completely. Use aria-labelledby to reference visible labels when possible. Test with voice control to ensure activation by visible label works.

**Label in Name Checklist**:
☐ All button accessible names include visible button text
☐ All link accessible names include visible link text
☐ Form control accessible names match or include visible labels
☐ Icon button tooltips match accessible names
☐ Custom components' accessible names include visible labels
☐ ARIA labels don't contradict visible labels
☐ Voice control can activate controls by visible label

### 21.10 Orientation - Success Criterion 1.3.4 (AA)

Content must not restrict view and operation to a single display orientation unless essential.

**Requirement**: Content does not restrict its view and operation to a single display orientation (portrait or landscape) unless a specific display orientation is essential. This means users must be able to use content in portrait or landscape orientation. Exceptions: bank check (requires landscape for proper display), piano app (requires landscape for keys), slides or presentations.

**Testing Orientation**: Testing requires rotating device or simulating orientation changes. Process: 1) Access site on mobile device or using DevTools device emulation. 2) Test in portrait orientation—verify all content is accessible and functional. 3) Rotate to landscape orientation—verify all content remains accessible and functional. 4) Check that content adapts appropriately to orientation (layout may change, but functionality must remain). 5) Test any modals, dropdowns, or overlays in both orientations. 6) Document any restrictions.

**Common Orientation Issues**: Content displays message "Please rotate device to portrait" (fails unless essential). Layout breaks in landscape orientation (content clipped, horizontal scroll required). Modals extend offscreen in landscape. Video players restrict to landscape without user option. Games or applications lock to one orientation without necessity.

**Solutions**: Use responsive design that works in both orientations. Test both orientations during development. Don't use orientation detection to force specific orientation. Use @media (orientation: portrait/landscape) to adapt layouts, not restrict. Provide orientation-appropriate layouts but allow both. For truly essential cases (rare), clearly communicate why orientation is required.

**Orientation Checklist**:
☐ Content works in portrait orientation
☐ Content works in landscape orientation
☐ Layouts adapt appropriately to orientation changes
☐ No forced orientation lock (unless essential with justification)
☐ Modals and overlays work in both orientations
☐ Navigation is accessible in both orientations
☐ Forms are usable in both orientations

### 21.11 Motion and Animation - Success Criteria 2.2.2 (A), 2.3.3 (AAA), 2.3.1 (A)

Motion and animation must be pausable, and users must be able to disable motion.

**Pause, Stop, Hide (2.2.2 - Level A)**: For any moving, blinking, or scrolling information that: starts automatically, lasts more than 5 seconds, and is presented in parallel with other content, there must be a mechanism to pause, stop, or hide it. Exceptions: if the movement is essential. This applies to carousels, scrolling tickers, animated content.

**Animation from Interactions (2.3.3 - Level AAA)**: Motion animation triggered by interaction can be disabled, unless the animation is essential to the functionality or information being conveyed. This means users should be able to turn off animations triggered by scrolling, hovering, clicking, etc.

**Three Flashes or Below Threshold (2.3.1 - Level A)**: Web pages do not contain anything that flashes more than three times in any one second period, or the flash is below general flash and red flash thresholds. This prevents seizures in users with photosensitive epilepsy.

**Respecting prefers-reduced-motion**: The prefers-reduced-motion CSS media query allows users to request reduced motion. Implementations must respect this setting:

```css
/* Default animations */
.element {
  transition: transform 0.3s ease;
  animation: slideIn 0.5s ease;
}

/* Reduce or remove animations for users who prefer reduced motion */
@media (prefers-reduced-motion: reduce) {
  .element {
    transition: none;
    animation: none;
  }
  
  /* Or significantly reduce duration */
  .element {
    transition-duration: 0.01ms;
    animation-duration: 0.01ms;
  }
}

/* Maintain essential motion (loading indicators) */
@media (prefers-reduced-motion: reduce) {
  .loader {
    /* Simplified animation instead of spinning */
    animation: pulse 2s infinite;
  }
}

@keyframes pulse {
  0%, 100% { opacity: 1; }
  50% { opacity: 0.5; }
}
```

**Testing Motion and Animation**: Testing requires enabling prefers-reduced-motion and testing animation controls. Process: 1) Identify all animations (transitions, CSS animations, JavaScript animations, autoplay videos). 2) Enable prefers-reduced-motion in OS settings (macOS: System Preferences > Accessibility > Display > Reduce Motion, Windows: Settings > Ease of Access > Display > Show animations). 3) Reload page and verify animations are significantly reduced or eliminated. 4) For autoplay content (carousels, tickers), verify pause/stop controls exist and work. 5) Test that essential animations (loading indicators) remain functional. 6) Check for flashing content—if any exists, verify it's below three flashes per second. 7) Document any failures.

**Common Motion/Animation Issues**: Animations don't respect prefers-reduced-motion. Carousels autoplay without pause controls. Parallax scrolling effects can't be disabled. Infinite scrolling or auto-updating content without stop mechanism. Flashing advertisements or banners. Animated backgrounds that can't be disabled. Hover effects with motion that can't be reduced.

**Solutions**: Implement prefers-reduced-motion media query for all animations. Provide pause buttons on carousels and autoplay content. Make parallax scrolling opt-in or disable for prefers-reduced-motion. Provide mechanism to stop auto-updating content. Avoid flashing content or ensure it's below threshold (three flashes per second). Provide user setting to disable animations. Test with OS-level reduced motion settings.

**Motion and Animation Checklist**:
☐ All animations respect prefers-reduced-motion
☐ Carousels and autoplay content have pause/stop controls
☐ Parallax scrolling can be disabled
☐ Auto-updating content can be paused
☐ No flashing content above three flashes per second
☐ Essential animations remain functional with reduced motion
☐ Motion animation from interactions can be disabled (AAA)
☐ User settings or controls exist for disabling animations
☐ OS-level reduced motion settings are respected
☐ Documentation explains how to disable motion

### 21.12 Cognitive Accessibility

Cognitive accessibility ensures content is understandable for users with cognitive and learning disabilities.

**Reading Level (3.1.5 - AAA)**: When text requires reading ability more advanced than lower secondary education level (roughly 9th grade in US) after removing proper names and titles, supplemental content or a version understandable to users with lower secondary education reading ability is available. This is AAA level, not required for most sites, but encouraged for content meant for general audiences.

**Clear Language**: Beyond WCAG requirements, cognitive accessibility benefits from: short sentences and paragraphs, simple words (avoid jargon), clear headings and structure, bullet points and lists instead of long paragraphs, consistent terminology, definitions for technical terms, and visual aids (images, diagrams, icons).

**Consistent Navigation (3.2.3 - AA)**: Navigational mechanisms repeated on multiple pages occur in the same relative order each time, unless a change is initiated by the user. This means navigation menus, search boxes, and other repeated elements appear in consistent locations.

**Consistent Identification (3.2.4 - AA)**: Components that have the same functionality are identified consistently. For example, all search icons should look the same, all "delete" actions should use the same icon/label, all "expand" controls should be consistent.

**Testing Cognitive Accessibility**: Testing involves reviewing content and design for clarity. Process: 1) Review text content for readability (use readability tools like Hemingway Editor, check reading level with Flesch-Kincaid or similar). 2) Verify navigation is consistent across pages (same order, same labels). 3) Check that icons and controls are used consistently (search always uses same icon, delete always uses same action). 4) Verify headings create clear structure (use accessibility tree to check heading hierarchy). 5) Test forms for clear instructions and error messages. 6) Check that complex processes are broken into clear steps. 7) Verify timeout warnings exist if session timeouts are used. 8) Document cognitive barriers.

**Cognitive Accessibility Checklist**:
☐ Text is written clearly at appropriate reading level (or alternatives exist - AAA)
☐ Sentences and paragraphs are short
☐ Jargon is avoided or defined
☐ Headings create clear content structure
☐ Navigation is consistent across pages
☐ Icons and controls are used consistently
☐ Forms have clear instructions and labels
☐ Error messages are clear and helpful
☐ Complex processes are broken into steps
☐ Timeout warnings are provided if applicable
☐ Visual aids support understanding
☐ Consistent terminology is used throughout

### 21.13 Accessible Authentication (WCAG 2.2)

New in WCAG 2.2, accessible authentication ensures users with cognitive disabilities can authenticate.

**Success Criterion 3.3.8 - Accessible Authentication (Minimum) - Level AA**: Cognitive function test (memory or puzzle-solving test) is not required for any step in authentication unless: alternative authentication method that doesn't rely on cognitive function test, mechanism to assist in completing cognitive function test, or cognitive function test is to recognize objects, personal content, or non-text content provided by user.

**Success Criterion 3.3.9 - Accessible Authentication (Enhanced) - Level AAA**: Cognitive function test is not required, with same exceptions as 3.3.8.

**What This Means**: Traditional CAPTCHA (distorted text), mathematical problems, or memory tests in authentication fail WCAG 2.2 unless alternatives exist. Acceptable alternatives include: password managers (allow users to paste passwords), biometric authentication (Face ID, Touch ID, fingerprint), security keys (hardware tokens), magic links (email link authentication), OAuth social login, and image recognition of personal content (user-selected images).

**Testing Accessible Authentication**: Process: 1) Identify all authentication flows (login, registration, password reset). 2) Check for CAPTCHA or cognitive tests. 3) If present, verify alternatives exist (can user paste password? Is there alternative auth method?). 4) Test with password manager to ensure passwords can be pasted. 5) Test any CAPTCHA alternatives (reCAPTCHA v3, hCaptcha accessibility options). 6) Document any problematic authentication steps.

**Accessible Authentication Checklist**:
☐ Authentication doesn't require memory tests (or has alternatives)
☐ Authentication doesn't require puzzle-solving (or has alternatives)
☐ Users can paste passwords (password managers work)
☐ Alternative authentication methods exist (biometric, magic link, OAuth)
☐ CAPTCHA has accessible alternatives or isn't used
☐ Users aren't required to transcribe distorted text
☐ Security measures don't exclude users with cognitive disabilities

### 21.14 Redundant Entry (WCAG 2.2)

Success Criterion 3.3.7 - Redundant Entry - Level A (new in WCAG 2.2).

**Requirement**: Information previously entered by or provided to the user that is required to be entered again in the same process is either auto-populated or available for the user to select. Exceptions: re-entering is essential (confirming password, security reasons), previously entered information is invalid, or information is from previous session.

**What This Means**: In multi-step forms or processes, users shouldn't have to re-enter information they've already provided. For example: shipping address shouldn't need to be re-entered for billing address (provide "same as shipping" option or auto-populate). Email address entered in step 1 shouldn't need to be entered again in step 3. Username entered on previous page shouldn't need to be re-typed.

**Testing Redundant Entry**: Process: 1) Identify multi-step processes (checkout, registration, account setup). 2) Track what information is requested at each step. 3) Verify information isn't requested multiple times without reason. 4) Check for auto-population or "same as above" options. 5) Document any redundant entry requirements.

**Redundant Entry Checklist**:
☐ Multi-step forms don't request same information multiple times
☐ "Same as above" options exist where appropriate
☐ Auto-population is used to carry information forward
☐ Password confirmation is only redundant entry (exception)
☐ Users aren't required to re-type previously entered data

### 21.15 Comprehensive Accessibility Testing Checklist

**Perceivable**:
☐ 1.1.1 All images have alt text (A)
☐ 1.2.1 Audio-only and video-only have alternatives (A)
☐ 1.2.2 Captions for videos (A)
☐ 1.2.3 Audio description or media alternative for videos (A)
☐ 1.2.5 Audio description for videos (AA)
☐ 1.3.1 Info and relationships marked up semantically (A)
☐ 1.3.2 Meaningful sequence maintained (A)
☐ 1.3.3 Instructions don't rely on sensory characteristics alone (A)
☐ 1.3.4 Content works in portrait and landscape (AA)
☐ 1.3.5 Identify input purpose where applicable (AA)
☐ 1.4.1 Color is not the only means of conveying information (A)
☐ 1.4.2 Audio control for autoplay audio (A)
☐ 1.4.3 Text has 4.5:1 contrast (AA)
☐ 1.4.4 Text can be resized 200% without loss of content or functionality (AA)
☐ 1.4.5 Images of text avoided where possible (AA)
☐ 1.4.6 Text has 7:1 contrast (AAA)
☐ 1.4.10 Content reflows without two-dimensional scrolling at 320px width (AA)
☐ 1.4.11 UI components and graphics have 3:1 contrast (AA)
☐ 1.4.12 Text spacing can be adjusted without loss of content (AA)
☐ 1.4.13 Content on hover/focus is dismissible, hoverable, persistent (AA)

**Operable**:
☐ 2.1.1 All functionality available from keyboard (A)
☐ 2.1.2 No keyboard trap (A)
☐ 2.1.4 Keyboard shortcuts can be remapped or turned off (A)
☐ 2.2.1 Timing adjustable where time limits exist (A)
☐ 2.2.2 Moving/blinking/scrolling content can be paused (A)
☐ 2.3.1 No flashing more than 3 times per second (A)
☐ 2.4.1 Skip links provided (A)
☐ 2.4.2 Page has descriptive title (A)
☐ 2.4.3 Focus order is logical (A)
☐ 2.4.4 Link purpose clear from link text or context (A)
☐ 2.4.5 Multiple ways to find pages (AA)
☐ 2


