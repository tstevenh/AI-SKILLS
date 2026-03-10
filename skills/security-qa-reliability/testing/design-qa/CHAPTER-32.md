# 29. Design QA for Complex UI Patterns


Modern web applications employ increasingly sophisticated UI patterns that present unique testing challenges. Complex components like modals, dropdowns, tooltips, popovers, mega menus, and overlays require thorough testing across multiple dimensions including positioning, behavior, accessibility, interaction patterns, and edge cases. This section provides comprehensive guidance for testing these intricate UI patterns.

### 29.1 Modal Dialog Testing

Modal dialogs interrupt the user's workflow to present critical information or gather input. Their disruptive nature demands flawless implementation across all aspects of design and behavior.

**Visual Positioning and Layout**: Modals must appear correctly positioned and sized across all viewports. Test that modals are centered horizontally and vertically in the viewport, remain centered when content changes dynamically, handle very long content appropriately (scrollable content area with fixed header/footer, or full-screen modal on small devices), maintain appropriate margins from viewport edges on all screen sizes, and scale responsively without breaking layout. On mobile devices, many designs switch from centered modals to full-screen sheets—verify this transition happens at appropriate breakpoints and animations are smooth.

**Backdrop and Focus Management**: The modal backdrop serves visual and functional purposes. Verify that backdrop appears immediately when modal opens, has appropriate opacity and color (typically semi-transparent dark overlay), prevents interaction with underlying content (clicks on backdrop don't reach content below), closes modal when clicked (unless this behavior is intentionally disabled), and doesn't flicker or flash during opening animation. Focus management is critical for accessibility—when modal opens, focus should move to the first focusable element (typically close button or first form input), focus remains trapped within modal (Tab and Shift+Tab cycle through modal elements only), Escape key closes modal and returns focus to trigger element, and when modal closes, focus returns to the element that opened it.

**Stacking and Nesting**: Applications sometimes require multiple modals or modals opened from modals. Test scenarios where modal is opened from a page, second modal is opened from first modal, third-level nesting if your application supports it, verify proper z-index ordering (later modals appear above earlier ones), ensure backdrop opacity is appropriate for stacked modals (doesn't become too dark), confirm focus management works correctly through nesting levels (Escape closes top modal, focus remains in second modal), and validate that closing all modals returns focus to original trigger element.

**Animation and Transitions**: Modal open and close animations significantly impact perceived quality. Test that opening animation is smooth and performant (typically fade-in combined with scale or slide), closing animation is slightly faster than opening (feels more responsive), animations respect prefers-reduced-motion (instant or minimal animation for users who request reduced motion), modal content doesn't render partially during animation (wait for animation to complete before showing interactive elements, or ensure all elements animate together), and backdrop fade timing coordinates with modal animation.

**Responsive Behavior**: Modal responsiveness goes beyond simple resizing. Test on desktop viewports (typical centered modal), tablet sizes (modal may become wider relative to viewport), mobile phones (modal often becomes full-screen or bottom sheet), very small screens (content remains accessible and usable), landscape vs portrait orientation (layout adapts appropriately), and viewport height considerations (very short viewports require scrollable content).

**Content Handling**: Modals must gracefully handle content variations. Test with minimal content (modal doesn't become awkwardly small), typical content amount, maximum expected content (appropriate scrolling), unexpectedly long content (defensive design prevents breaking), images and media (load properly and don't overflow), forms with validation errors (errors display within modal without breaking layout), and dynamic content updates (modal adjusts size/scroll as content changes).

**Accessibility Compliance**: Modal accessibility is non-negotiable. Verify that modal has role="dialog" or role="alertdialog", aria-modal="true" prevents screen readers from reading background content, aria-labelledby references modal title, aria-describedby references modal description if present, focus trap works correctly with assistive technologies, modal can be closed via Escape key, modal close button is clearly labeled (not just an "×" with no text alternative), all interactive elements are keyboard accessible, and color contrast meets WCAG requirements for all text.

**Edge Cases and Error Conditions**: Robust modals handle edge cases gracefully. Test modal opening while previous modal is still closing, rapid opening and closing (click open then immediately close), opening modal with slow network (content loads asynchronously), modal trigger element being removed from DOM while modal is open, modal containing forms with autofocus, modal containing iframes or embedded content, modal in pages with existing scroll position (should scroll to top or handle elegantly), and modal behavior when browser zoom is used.

**Mobile-Specific Considerations**: Mobile presents unique challenges. Test touch scrolling within modal (only modal content scrolls, not page behind), pinch-zoom behavior (modal content can be zoomed if needed), iOS Safari bottom bar appearing and disappearing (modal position adjusts appropriately), Android keyboard appearance (modal resizes or scrolls to keep inputs visible), pull-to-refresh gesture doesn't trigger while modal is open, swipe gestures for closing (if supported), and safe area insets on notched devices (content avoids notch area).

### 29.2 Dropdown Menu Testing

Dropdown menus, including select inputs and custom action menus, require precise positioning and interaction testing.

**Opening and Closing Behavior**: Dropdowns must open and close predictably. Test that dropdown opens on click/tap of trigger, opens on Enter or Space key when trigger is focused, closes when option is selected, closes when clicking outside dropdown, closes when pressing Escape key, closes when tabbing away from dropdown, and maintains proper z-index (appears above other content).

**Positioning and Boundary Detection**: Dropdown positioning is crucial for usability. Verify that dropdown appears below trigger by default, flips above trigger when insufficient space below, aligns left edge with trigger (or right edge for RTL), adjusts horizontal position to fit within viewport, maintains appropriate margin from viewport edges, repositions correctly when window resizes, and updates position if page is scrolled while open.

**Content and Scrolling**: Dropdown content must be accessible regardless of size. Test dropdowns with few options (2-3 items), typical number of options (5-20 items), many options requiring scroll (50+ items), very long option text (wraps or truncates appropriately), options with icons or rich content, grouped options with section headers, disabled options (visually distinct, not selectable), and search/filter functionality if present.

**Keyboard Navigation**: Keyboard support is essential for accessibility. Verify that Arrow Down opens dropdown and moves to first option, subsequent Arrow Down/Up navigate options, Home key jumps to first option, End key jumps to last option, typing filters or selects matching options (typeahead), Enter selects focused option and closes dropdown, Escape closes dropdown without selection, and focus remains visible throughout navigation.

**Visual States**: All dropdown states require distinct visual treatment. Test default closed state, open state, each option's default state, option hover state (mouse only), option focused state (keyboard navigation), option active state (mouse down), selected option state (different from focused), disabled option state, and loading state if options load asynchronously.

**Mobile Adaptations**: Dropdowns often work differently on mobile. Test that mobile OS native select is used when appropriate (better UX for simple selects), custom dropdowns work well with touch (large enough touch targets), dropdown size is appropriate for mobile viewport (may become full-screen), scrolling works smoothly with touch, keyboard appearance doesn't obscure dropdown, and dropdown closes when scrolling page content.

**Search and Filter**: Many dropdowns include search functionality. Verify that search input appears prominently, typing focuses search input automatically, search filters options in real-time, filtered list shows "no results" message appropriately, clearing search restores full list, search maintains keyboard navigation, and search performance is good with large option lists.

### 29.3 Tooltip and Popover Testing

Tooltips and popovers provide contextual information without cluttering interfaces, but require careful testing of positioning, timing, and accessibility.

**Tooltip Appearance Timing**: Timing significantly affects tooltip UX. Test that tooltip appears after appropriate hover delay (typically 300-500ms), appears immediately if user recently triggered another tooltip (no delay for subsequent tooltips), disappears when mouse leaves trigger, disappears after delay when mouse enters tooltip then leaves, doesn't appear if user is quickly mousing across trigger (cursor must dwell), keyboard focus shows tooltip immediately (no delay), and mobile tap shows tooltip (with appropriate dismiss mechanism).

**Positioning and Arrow Indicators**: Tooltips must point clearly to their triggers. Verify that tooltip appears above trigger by default (or as specified in design), flips to below if insufficient space above, tries right/left sides if no room above or below, arrow points directly to trigger center, tooltip edge aligns with trigger when possible (doesn't extend far beyond trigger width), tooltip remains fully within viewport, repositions dynamically if page is scrolled while visible, and handles edge-of-screen positioning gracefully.

**Content and Sizing**: Tooltip content must be readable and appropriately sized. Test with short text (1-5 words), medium text (1-2 lines), long text (multiple lines, has reasonable max-width), formatted content if supported (bold, links, etc.), tooltips on small triggers (tooltip is substantially wider than trigger), tooltips on wide triggers (tooltip relates clearly to trigger), and multilingual content (text length varies).

**Accessibility Considerations**: Tooltip accessibility is often overlooked. Verify that tooltips are keyboard accessible (show on focus), tooltip content is programmatically associated with trigger (aria-describedby), critical information isn't only in tooltips (some users can't access tooltips), tooltip content is readable by screen readers, tooltips don't trap focus, tooltip content meets color contrast requirements, and tooltips work with screen magnification.

**Hover vs Focus vs Mobile**: Different input methods need different tooltip behavior. Test that mouse hover shows tooltip, keyboard focus shows tooltip, touch on mobile shows tooltip (and provides dismiss method), second touch dismisses or activates trigger (context-dependent), tooltip doesn't interfere with clicking trigger, tooltip doesn't appear for disabled elements (unless design requires explanation), and tooltip timing is appropriate for each input method.

**Popover Extended Content**: Popovers differ from tooltips by containing richer, interactive content. Test that popover can contain links, buttons, and interactive elements, focus moves into popover when it contains interactive content, Tab key navigates through popover content, popover stays open while interacting with its content, clicking outside popover closes it, Escape key closes popover, popover closes when trigger is activated again (toggle behavior), and popover doesn't close when clicking inside it (unless explicitly dismissed).

**Multiple Simultaneous Tooltips**: Handle scenarios where multiple tooltips might appear. Test that hovering a second trigger closes first tooltip (typically only one tooltip visible at a time), exceptions for multi-touch scenarios, tooltip showing doesn't interfere with hover states of other elements, and tooltips don't trigger infinite loops or cascading behaviors.

### 29.4 Mega Menu Testing

Mega menus display complex, multi-column navigation structures. Their size and complexity require comprehensive testing.

**Opening and Closing**: Mega menus typically open on hover but require careful timing. Verify that mega menu opens after appropriate hover delay (prevents accidental opening), remains open while cursor is over trigger or menu, closes when cursor leaves trigger and menu area, hover "safety triangle" prevents premature closing (cursor can move diagonally toward menu without closing), keyboard activation opens menu (Enter or Arrow Down), menu closes when selecting an item, Escape closes menu and returns focus to trigger, and clicking outside menu closes it.

**Layout and Responsiveness**: Mega menus contain complex layouts requiring responsive testing. Test that menu columns layout correctly at various viewport widths, menu adjusts number of columns on smaller screens, menu becomes stacked mobile menu below appropriate breakpoint, menu stays within viewport horizontally, menu handles viewport height appropriately (scrollable if needed), menu orientation adjusts based on trigger position (left vs right edge), and menu appearance is smooth and glitch-free.

**Content Organization**: Content within mega menus must be well-organized. Verify that sections are clearly separated, headings are distinct from links, category labels aren't clickable (if design intends), subcategory structure is clear, featured items or images display correctly, promotional content integrates cleanly, and content hierarchy is maintained at all sizes.

**Keyboard Navigation**: Keyboard support for mega menus is complex. Test that Tab moves through trigger items in main navigation, Arrow keys open menu and navigate within it, Down Arrow from trigger enters first menu item, Arrow keys navigate within columns, Tab moves between menu sections (or through all items sequentially), Home/End jump to first/last menu item, typing filters or jumps to matching items, Enter activates focused link, and Escape closes menu and returns focus.

**Focus Management**: Large menus require sophisticated focus handling. Verify that focus indicator is always visible, focus doesn't get trapped in menu, focus returns to trigger when menu closes, focus moves logically through complex layouts, focus skip-link patterns work if implemented, and focus order makes sense with screen readers.

**Touch and Mobile**: Mega menus often become accordion or drill-down patterns on mobile. Test that mobile transformation happens at appropriate breakpoint, mobile pattern is intuitive and accessible, touch targets are appropriately sized, touch scrolling works within menu sections, nested navigation works on touch devices, back buttons return to previous level, and mobile menu closing returns to expected state.

**Performance**: Large mega menus can impact performance. Verify that menu renders quickly when opened, images lazy-load appropriately, menu content doesn't cause layout shift, animations are smooth and performant, menu doesn't block main thread, menu content is cached if appropriate, and menu works well on slower connections/devices.

### 29.5 Overlay and Sheet Testing

Overlays and bottom sheets provide contextual interfaces without full page transitions.

**Bottom Sheet Behavior**: Bottom sheets slide up from screen bottom, popular in mobile interfaces. Test that sheet slides up smoothly from bottom, sheet header remains visible (typically fixed), sheet content scrolls independently, dragging header dismisses sheet, swipe down gesture closes sheet, sheet backdrop works correctly, sheet height adapts to content, sheet can be full-height when needed, sheet handle/gripper is visible and functional, and sheet respects safe areas (notches, home indicators).

**Drawer/Side Panel Testing**: Side drawers slide in from screen edge. Verify that drawer slides from correct edge (left/right based on design), drawer has appropriate width (typically 300-400px on desktop), drawer width responds to viewport size, drawer backdrop covers main content, clicking backdrop closes drawer, drawer can be dismissed by swipe (mobile), drawer content is scrollable, drawer push vs overlay mode works correctly, drawer position works with app header, and drawer animation is smooth and performant.

**Overlay Content Management**: Overlays displaying rich content need special attention. Test that content loads efficiently (lazy loading if appropriate), content updates don't cause layout shift, scrolling behavior is intuitive, nested scrollable areas work correctly, embedded content (videos, maps) functions properly, form within overlay works correctly, validation errors display appropriately, and loading states are clear.

**Stacking and Layer Management**: Multiple overlays may be needed simultaneously. Test that appropriate z-index ordering is maintained, newer overlays appear above older ones, each overlay has its own backdrop (if designed that way), closing top overlay reveals previous overlay correctly, focus management works through overlay stack, and system handles maximum overlay depth gracefully.

**Accessibility for Overlays**: Overlays must be fully accessible. Verify that overlays use appropriate ARIA roles (dialog, complementary, etc.), overlays are labeled correctly, focus moves to overlay when opened, focus stays within overlay (if modal), focus returns to trigger when overlay closes, screen readers announce overlay opening, overlay content is navigable with assistive tech, and keyboard shortcuts work as expected.

### 29.6 Complex UI Pattern Checklist

Comprehensive checklist for complex UI patterns:

**Modals**:
☐ Modal centers correctly at all viewport sizes
☐ Backdrop prevents interaction with page content
☐ Focus moves to modal when opened
☐ Focus trap works correctly (Tab cycles through modal only)
☐ Escape closes modal and returns focus
☐ Closing button is accessible and clearly labeled
☐ Modal is keyboard-navigable throughout
☐ Nested modals work correctly if supported
☐ Animations are smooth and respect prefers-reduced-motion
☐ Mobile displays full-screen or appropriately sized sheet
☐ Scrolling works correctly for long content
☐ Form validation works within modal

**Dropdowns**:
☐ Dropdown opens on click/tap and keyboard activation
☐ Dropdown positions correctly (flips when near viewport edge)
☐ Dropdown options are keyboard-navigable
☐ Arrow keys navigate, Enter selects, Escape closes
☐ Selected state is visually clear
☐ Disabled options are visually distinct
☐ Scroll works for long option lists
☐ Typeahead/search works if implemented
☐ Mobile uses appropriate pattern (native select or custom)
☐ Touch targets are appropriately sized
☐ Focus indicator is always visible

**Tooltips/Popovers**:
☐ Tooltip appears with appropriate delay on hover
☐ Tooltip appears immediately on keyboard focus
☐ Tooltip positions correctly and flips when needed
☐ Tooltip arrow points to trigger
☐ Tooltip content is readable (appropriate size, contrast)
☐ Tooltip is accessible (aria-describedby, screen reader compatible)
☐ Tooltip dismisses appropriately
☐ Mobile tap shows tooltip with dismiss mechanism
☐ Popover focus management works for interactive content
☐ Popover closes correctly (outside click, Escape)

**Mega Menus**:
☐ Menu opens with appropriate hover delay
☐ Menu stays open while cursor moves toward it
☐ Menu layout is correct at all viewport sizes
☐ Menu becomes mobile navigation below breakpoint
☐ Keyboard navigation works through entire menu
☐ Focus indicator is always visible
☐ Touch targets are appropriately sized
☐ Menu performance is acceptable
☐ Menu stays within viewport bounds
☐ Menu close behavior is predictable

**Overlays/Sheets**:
☐ Sheet/drawer animates smoothly
☐ Backdrop works correctly
☐ Swipe to dismiss works on mobile
☐ Content scrolls appropriately
☐ Overlay respects safe areas
☐ Focus management is correct
☐ Stacking works if multiple overlays possible
☐ Accessibility attributes are correct
☐ Performance is acceptable

---
