# 25. Dark Mode Testing


Dark mode has evolved from niche preference to mainstream expectation. Users demand dark mode for eye strain reduction, battery savings on OLED screens, personal preference, and accessibility needs. Thorough dark mode testing ensures excellent experiences in both light and dark themes without compromising readability, accessibility, or visual quality.

### 25.1 Dark Mode Fundamentals

Understanding dark mode principles guides effective implementation and testing.

**Dark Mode Purpose**: Dark mode serves multiple user needs. Reduced eye strain in low-light environments (white backgrounds can be harsh in dark rooms), improved battery life on OLED/AMOLED screens (black pixels are off, consuming no power), personal aesthetic preference (many users simply prefer dark interfaces), accessibility for light-sensitive users (migraine sufferers, photophobia), better focus on content (less overall screen brightness), and professional contexts (developers, designers, creative professionals often prefer dark interfaces). Testing validates dark mode serves these purposes without introducing new problems.

**Dark Mode Approaches**: Several implementation strategies exist. System preference detection: respect OS-level dark mode setting (prefers-color-scheme CSS media query), user toggle: allow explicit light/dark/auto selection regardless of system setting, automatic time-based switching: dark mode at night, light during day (less common), per-component dark variants: some components support dark mode, others don't (avoid this inconsistency), and universal dark mode: entire application supports dark mode comprehensively (best practice). Testing validates chosen approach works consistently and respects user preferences.

**Color Scheme Principles**: Dark mode isn't just inverted colors. True dark mode uses dark grays rather than pure black (reduces eye strain, prevents OLED burn-in, provides better contrast hierarchy), maintains sufficient contrast (same WCAG requirements apply), adjusts colors for dark backgrounds (vibrant colors need desaturation or dimming, overlays need adjustment), maintains brand colors appropriately (may need slight adjustments), preserves semantic meaning (success still green-ish, error still red-ish, warning still amber-ish), and inverts elevation (shadows become highlights, depth inverted). Testing validates dark mode color choices are intentional and effective, not just inverted light mode.

**Implementing Dark Mode with CSS**: CSS provides multiple approaches. CSS Custom Properties with color-scheme:

```css
:root {
  color-scheme: light;
  --bg-primary: #ffffff;
  --text-primary: #000000;
  --color-primary: #0066cc;
}

@media (prefers-color-scheme: dark) {
  :root {
    color-scheme: dark;
    --bg-primary: #1a1a1a;
    --text-primary: #ffffff;
    --color-primary: #4da6ff;
  }
}
```

Data attribute approach with user preference:

```css
[data-theme="light"] {
  --bg-primary: #ffffff;
  --text-primary: #000000;
}

[data-theme="dark"] {
  --bg-primary: #1a1a1a;
  --text-primary: #ffffff;
}
```

Testing validates CSS approach works correctly, color variables switch appropriately, and transitions are smooth.

**JavaScript Theme Management**: JavaScript handles user preferences. Detect system preference:

```javascript
const prefersDark = window.matchMedia('(prefers-color-scheme: dark)').matches;

// Listen for changes
window.matchMedia('(prefers-color-scheme: dark)').addEventListener('change', (e) => {
  const newTheme = e.matches ? 'dark' : 'light';
  applyTheme(newTheme);
});
```

Store user preference:

```javascript
// Save preference
localStorage.setItem('theme', 'dark');

// Load preference
const savedTheme = localStorage.getItem('theme');
const systemTheme = prefersDark ? 'dark' : 'light';
const activeTheme = savedTheme || systemTheme;

// Apply theme
document.documentElement.setAttribute('data-theme', activeTheme);
```

Testing validates JavaScript correctly detects system preference, stores user preference, applies theme on load without flash, handles system preference changes, and allows user override of system preference.

### 25.2 Dark Mode Color Testing

Colors must be carefully adjusted for dark mode.

**Background Colors**: Dark mode backgrounds require nuance. Use dark grays (e.g., #1a1a1a, #2d2d2d) rather than pure black (#000000) for reduced eye strain and better hierarchy, create background color hierarchy (surface elevations: base #1a1a1a, elevated #2d2d2d, overlays #3d3d3d), test backgrounds on actual OLED screens (pure black can cause smearing on some OLED displays), verify background doesn't cause text to vibrate or be hard to read, test gradients in dark mode (may need adjustment), and validate transparent backgrounds work over dark base. Testing ensures dark backgrounds are comfortable and provide clear hierarchy.

**Text Colors**: Text must remain readable in dark mode. Use off-white colors (e.g., #e0e0e0, #f5f5f5) rather than pure white (#ffffff) to reduce harsh contrast and eye strain, maintain text color hierarchy (primary text #f5f5f5, secondary text #b0b0b0, disabled text #6b6b6b), test text contrast ratios meet WCAG (4.5:1 for normal text, 3:1 for large text, on dark backgrounds), verify text doesn't appear to glow or bloom (overly bright text on dark backgrounds can create halos), test colored text (links, semantic colors) on dark backgrounds, and validate text over images or gradients maintains contrast. Testing ensures text remains readable and comfortable in dark mode.

**Brand Colors in Dark Mode**: Brand colors often need adjustment. Test brand colors on dark backgrounds (may be too vibrant or oversaturated), desaturate or dim overly bright brand colors for dark mode (vibrant blues, greens can be harsh), maintain brand recognition while improving readability, test brand colors meet contrast requirements, verify logo colors work on dark backgrounds (may need dark mode logo variant), and test brand color consistency across components. Testing validates brand identity is preserved while adapting to dark mode.

**Semantic Colors in Dark Mode**: Success, error, warning, info colors need dark mode variants. Test semantic colors on dark backgrounds (standard semantic colors often too bright), adjust semantic colors for dark mode (e.g., success: light green #4caf50 becomes darker green #81c784, error: bright red #f44336 becomes slightly less saturated #e57373), maintain semantic meaning (colors still communicate intent clearly), verify semantic color contrast meets requirements, test semantic colors in all contexts (buttons, alerts, badges, icons), and validate semantic colors work with text and backgrounds. Testing ensures semantic meaning is preserved in dark mode.

**Color Inversion Issues**: Some elements shouldn't be inverted. Identify elements that should maintain light appearance (photos, product images, user avatars, logos typically stay original), test that images don't get incorrectly inverted, verify syntax highlighting in code blocks works well in dark mode (may need specific dark theme), check that charts and data visualizations work in dark mode (may need dark-specific color palettes), test emoji and icons (ensure sufficient contrast), validate video thumbnails and embedded media, and ensure third-party content (ads, widgets) integrates reasonably. Testing catches elements incorrectly inverted or inadequately adapted.

**Color Contrast Measurements in Dark Mode**: WCAG applies equally. Test all text meets 4.5:1 contrast ratio minimum (normal text) and 3:1 for large text (24px+), verify UI components have 3:1 contrast with backgrounds, check focus indicators meet contrast requirements (3:1 with focused element and adjacent colors), test disabled elements are distinguishable (even if lower contrast), validate semantic color contrast, measure actual rendered colors (browser DevTools color picker), and test contrast at various brightness levels (users may have dim screens). Testing validates all contrast requirements are met in dark mode.

### 25.3 Dark Mode Shadow and Elevation

Shadows must be reimagined for dark interfaces.

**Traditional Shadows Don't Work**: Dark mode shadows require different approaches. Traditional shadows darken surfaces (shadow = darker color), but dark mode surfaces are already dark, shadows cast on dark surfaces are barely visible (darker on dark is subtle), pure black shadows on dark gray are ineffective, and traditional elevation hierarchy breaks down. Testing reveals this limitation quickly.

**Dark Mode Elevation Strategies**: Several alternatives effectively communicate depth. Lighten elevated surfaces (instead of shadows, raised surfaces are lighter: base #1a1a1a, card #2d2d2d, modal #3d3d3d), use subtle light borders on elevated surfaces (1px border in light gray #404040 defines edges), combine lighter surface with subtle border (layered approach), use backlighting effect (glow instead of shadow, subtle light-colored shadow), reduce reliance on elevation (flatter design works well in dark mode), and use color/opacity changes to distinguish surfaces. Testing validates elevation hierarchy is clear in dark mode.

**Adapting Shadow Tokens**: Shadow design tokens need dark mode variants. Define dark mode shadow tokens separately (may be light-colored or eliminated), test shadows with light backgrounds (light mode: dark shadows) and dark backgrounds (dark mode: lighter "shadows" or borders), adjust shadow opacity for dark mode (if keeping shadows, make them subtle), consider removing some shadows entirely in dark mode (not all elevations need explicit shadows), verify shadow tokens are used consistently, and test shadow appearance on various dark background shades. Testing ensures shadow system works across themes.

**Border and Outline Adjustments**: Borders replace some shadow functions in dark mode. Use subtle borders to define component edges (1px solid #404040 on #2d2d2d background), test border contrast (must meet 3:1 ratio for UI component contrast), lighten borders compared to light mode (darker borders don't show well on dark surfaces), use borders to create visual hierarchy (heavier borders for more important elements), verify borders don't make interface feel heavy or boxy, and test border appearance across all background shades. Testing validates borders effectively communicate structure in dark mode.

**Focus Indicators in Dark Mode**: Focus indicators need adequate contrast in dark mode. Test focus indicators have 3:1 contrast with focused element (lighter or more saturated colors needed for dark mode), verify focus indicators have 3:1 contrast with adjacent backgrounds, use bright colors for focus indicators in dark mode (blue or cyan show well), test focus indicators are visible on all background shades, ensure focus indicators don't blend with elevated surfaces, validate focus indicators work with light-colored text, and test focus indicators are consistent across components. Testing ensures keyboard navigation is always clear in dark mode.

### 25.4 Image Handling in Dark Mode

Images and graphics require special consideration in dark mode.

**Photos and User Content**: Realistic images generally shouldn't be altered. Don't invert photos (people look like aliens, unnatural), don't desaturate photos (loses richness and information), keep user-generated images in original form (photos, avatars, uploaded content), optionally reduce image brightness slightly (can make bright images less jarring on dark backgrounds), use transparent overlays with caution (can muddy images), test that images have adequate borders or backgrounds (distinguish from UI), and ensure images load and display correctly in both modes. Testing validates photos remain natural and recognizable in dark mode.

**Icons in Dark Mode**: Icons must adapt to dark backgrounds. Invert icon colors (light mode icons often dark, need to be light in dark mode), use CSS filters to adjust icon colors (filter: invert(1) or specific color filters), maintain icon contrast (icons must have 3:1 contrast with backgrounds), test icon legibility on various dark surfaces, verify icon states change appropriately (hover, active, disabled), use SVG icons with CSS color control (fill: currentColor inherits text color), and test third-party icon libraries (Font Awesome, Material Icons) in dark mode. Testing ensures icons remain clear and functional in dark mode.

**Logos in Dark Mode**: Brand logos may need variants. Provide light logo variant for dark backgrounds (if logo is primarily dark), test logo contrast on dark backgrounds, consider using logo with transparent background (allows background to show through), maintain brand identity (logo should remain recognizable), verify logo sizing and placement work in dark mode, test logo in navigation, headers, footers, and authentication screens, and document logo usage guidelines for dark mode. Testing validates brand presence is maintained in dark mode.

**Charts and Data Visualizations**: Data viz requires dark mode adaptations. Create dark mode color palettes for charts (lighter, more saturated colors on dark backgrounds), test chart colors have adequate contrast and distinction (color + pattern for accessibility), adjust chart backgrounds (may need dark chart background), adapt grid lines and axes (lighter colors on dark backgrounds), test labels and annotations are readable, verify legends work on dark backgrounds, ensure interactive elements (tooltips, highlights) are visible, and test chart libraries support dark mode (Chart.js, D3, Recharts, etc.). Testing validates data remains clear and beautiful in dark mode.

**Syntax Highlighting in Code Blocks**: Code requires special color schemes. Use dedicated dark syntax theme (Dracula, Nord, One Dark, Monokai, etc.), test code colors have adequate contrast on dark code block backgrounds, verify keywords, strings, comments, functions use distinct colors, test line numbers and gutters are readable, ensure selection and highlighting work well, test diff highlighting (git diffs, code review), and validate code block UI (copy button, language label) works in dark mode. Testing ensures code remains readable and syntax is clear in dark mode.

### 25.5 Dark Mode Component Testing

Every component must be tested in dark mode.

**Button States in Dark Mode**: Buttons need full state testing. Test default button appearance on dark backgrounds, verify hover states have adequate visual change, check active/pressed states are obvious, validate focus states meet contrast requirements, test disabled buttons are distinguishable but clearly disabled, verify loading states (spinner visibility, button opacity), test button variants (primary, secondary, tertiary, ghost) in dark mode, check destructive buttons (delete, remove) communicate danger, and validate icon buttons work in dark mode. Testing ensures buttons are usable and clear in dark mode.

**Form Inputs in Dark Mode**: Form components are critical. Test input backgrounds work on dark page backgrounds (slightly lighter than page for depth), verify input borders have adequate contrast, check placeholder text is visible but not too bright, test input text is readable, validate focus states are clear, verify error states communicate problems effectively, test success states and validation, check disabled inputs are distinguishable, validate autocomplete dropdowns work in dark mode, test date pickers and selects, and ensure form labels are readable. Testing validates forms remain usable and accessible in dark mode.

**Navigation in Dark Mode**: Navigation must remain clear. Test navigation backgrounds (may be darkest surface or elevated), verify navigation text/icons are readable, check active/selected navigation items are obvious, test hover states on navigation items, validate mobile navigation (hamburger menu, drawer) in dark mode, test breadcrumbs in dark mode, verify pagination in dark mode, and check footer links and text. Testing ensures users can navigate effectively in dark mode.

**Cards and Surfaces in Dark Mode**: Card components use elevation. Test card backgrounds are distinct from page background (lighter surface), verify card borders if used (subtle light borders), check card shadows or elevation treatment, test card content is readable, validate card interactive states (clickable cards), test card hierarchies (multiple elevation levels), and verify cards work at various sizes and contexts. Testing ensures card-based layouts work well in dark mode.

**Modals and Overlays in Dark Mode**: Overlays need special attention. Test modal backgrounds (should be elevated surface, lighter than page), verify modal overlay (scrim) on page (semi-transparent dark overlay), check modal content is readable, test modal borders and shadows, validate modal close button is visible, test modal focus trap works, verify modal content scrolling, and check modal animations don't create jarring transitions. Testing validates modals remain functional and clear in dark mode.

**Tables in Dark Mode**: Tables need careful color management. Test table backgrounds (base or slightly elevated), verify table borders have adequate contrast (subtle light borders), check header styling is distinct, test alternating row colors (zebra stripes) if used (subtle on dark backgrounds), verify selected row highlighting, test hover states on rows, validate table text is readable, and check table scrolling and sticky headers. Testing ensures tables remain usable and scannable in dark mode.

**Notification and Toasts in Dark Mode**: Temporary messages need visibility. Test notification backgrounds (should be distinct, possibly using semantic colors), verify notification text is readable, check notification borders or shadows, test notification icons are visible, validate close buttons work, test stacking (multiple notifications), and verify animations don't cause jarring flashes. Testing ensures notifications effectively communicate in dark mode.

### 25.6 Dark Mode Transition Testing

Theme switching must be smooth and non-disruptive.

**Transition Animation**: Smooth theme switching improves perceived quality. Implement fade transition between themes (200-300ms transition on root element colors), use CSS transitions on all color properties:

```css
* {
  transition: background-color 0.3s ease, color 0.3s ease, border-color 0.3s ease;
}

@media (prefers-reduced-motion: reduce) {
  * {
    transition: none;
  }
}
```

Test transition is smooth and pleasant, verify all elements transition (no jarring color snaps), test transition doesn't cause layout shifts, validate transition respects prefers-reduced-motion, and ensure transition isn't too slow (feels sluggish) or too fast (feels jarring). Testing validates theme switching feels polished.

**Flash of Unstyled Content (FOUC)**: Prevent incorrect theme from flashing. Load theme preference before page render (inline script in HTML head), apply theme class/attribute immediately:

```html
<script>
(function() {
  const theme = localStorage.getItem('theme') || 
                (window.matchMedia('(prefers-color-scheme: dark)').matches ? 'dark' : 'light');
  document.documentElement.setAttribute('data-theme', theme);
})();
</script>
```

Test page loads with correct theme (no flash of wrong theme), verify theme is applied before first paint, test with slow network (FOUC more likely), and validate server-side rendering applies correct theme. Testing ensures users never see wrong theme flash.

**Persistence Across Sessions**: Theme preference should persist. Save user preference to localStorage or cookie, load preference on page load, respect explicit user choice over system preference, sync preference across tabs (storage event), test preference persists after browser restart, verify preference syncs across devices (if account-based), and test clearing browser data resets to system preference. Testing validates theme preference is reliably remembered.

**Respecting System Changes**: Respond to system theme changes. Listen for prefers-color-scheme changes:

```javascript
window.matchMedia('(prefers-color-scheme: dark)').addEventListener('change', (e) => {
  if (!localStorage.getItem('theme')) { // Only if user hasn't explicitly set preference
    const newTheme = e.matches ? 'dark' : 'light';
    applyTheme(newTheme);
  }
});
```

Test app updates when OS theme changes (if user hasn't explicitly set preference), verify user explicit choice overrides system changes, and test transition is smooth when system changes. Testing ensures system integration feels seamless.

### 25.7 Dark Mode Accessibility Testing

Dark mode must maintain accessibility standards.

**Contrast Testing in Dark Mode**: All WCAG requirements apply. Test all text meets 4.5:1 contrast (normal text) or 3:1 (large text 24px+), verify UI components meet 3:1 contrast, check focus indicators meet 3:1 contrast, test semantic colors (success, error, warning) meet requirements, validate disabled elements are distinguishable, use color contrast analyzers for dark mode colors, and test on various actual screens (contrast can appear different on different displays). Testing ensures dark mode is accessible to users with low vision.

**High Contrast Mode Compatibility**: Windows High Contrast Mode interaction. Test that dark mode works with Windows High Contrast Mode enabled, verify forced colors mode doesn't break layout (use forced-colors media query to adapt), test that semantic HTML ensures structure is maintained, check that custom colors are overridden appropriately, and validate that high contrast mode styling is acceptable. Testing ensures compatibility with system accessibility features.

**Screen Reader Testing in Dark Mode**: Visual changes shouldn't affect screen readers, but test anyway. Verify screen reader announces content correctly in both themes, test theme toggle is announced (e.g., "Switched to dark mode"), ensure theme preference is communicated if relevant, validate content hierarchy is maintained in dark mode (headings, landmarks work identically), and test with NVDA, JAWS, VoiceOver, and TalkBack. Testing confirms dark mode doesn't inadvertently affect screen reader experience.

**Motion Sensitivity in Dark Mode**: Theme switching can trigger motion sensitivity. Test theme transition respects prefers-reduced-motion (instant switch vs animated transition), verify auto-switching doesn't cause unexpected motion, check that theme changes at appropriate times (not while user is mid-task), and test that rapid theme switching doesn't cause discomfort. Testing ensures theme changes don't cause accessibility issues.

### 25.8 Dark Mode Testing Checklist

Comprehensive checklist ensures complete dark mode testing:

**Color Testing**:
☐ All backgrounds use appropriate dark colors (dark grays, not pure black)
☐ All text colors provide sufficient contrast (4.5:1 minimum)
☐ All UI components have 3:1 contrast
☐ Brand colors are adapted appropriately for dark mode
☐ Semantic colors (success, error, warning) are adjusted and meet contrast
☐ Images remain natural and visible
☐ Icons have sufficient contrast
☐ Logos work on dark backgrounds
☐ Charts and visualizations use dark-appropriate palettes

**Component Testing**:
☐ Buttons: all variants and states work in dark mode
☐ Form inputs: backgrounds, borders, text, placeholders, focus, errors all work
☐ Navigation: backgrounds, text, icons, active states work
☐ Cards: backgrounds, elevation, content all work
☐ Modals: backgrounds, overlays, content all work
☐ Tables: backgrounds, borders, text, rows all work
☐ Notifications: backgrounds, text, icons all visible

**Technical Testing**:
☐ Theme switching works (toggle button, system preference detection)
☐ Theme preference persists across sessions
☐ No flash of unstyled content (FOUC) on page load
☐ Transition between themes is smooth
☐ prefers-reduced-motion is respected
☐ Theme syncs across tabs
☐ CSS variables or theming approach works correctly

**Accessibility Testing**:
☐ All text meets WCAG contrast requirements in dark mode
☐ Focus indicators are clearly visible and meet 3:1 contrast
☐ Screen readers work correctly in dark mode
☐ High contrast mode compatibility works
☐ Theme changes don't cause motion accessibility issues

**Cross-Browser Testing**:
☐ Dark mode works in Chrome
☐ Dark mode works in Firefox
☐ Dark mode works in Safari
☐ Dark mode works in Edge
☐ Dark mode works on iOS Safari
☐ Dark mode works on Android Chrome

**Device Testing**:
☐ Dark mode tested on OLED screens (check for pure black vs dark gray)
☐ Dark mode tested at various brightness levels
☐ Dark mode tested in actual dark environments
☐ Dark mode tested on various screen qualities

---
