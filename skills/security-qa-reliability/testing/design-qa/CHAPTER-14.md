# 14. Button States and Interactive Elements


Buttons and interactive elements are fundamental to user interfaces, enabling actions, navigation, and communication. Button QA ensures interactive elements are visually consistent, provide appropriate feedback, communicate purpose clearly, maintain accessibility, and enable efficient interaction across devices. This comprehensive section covers all aspects of button and interactive element testing.

### 14.1 Button Fundamentals

Understanding button design principles enables effective testing.

**Button Types**: Buttons serve different purposes requiring distinct styling. Primary buttons indicate main actions (often filled with brand color), secondary buttons indicate alternative actions (often outlined or subtly filled), tertiary buttons indicate less important actions (often text-only), destructive buttons indicate dangerous actions like delete (often red), and ghost buttons are minimal, often over images or backgrounds. Testing validates appropriate button type is used for action importance, visual hierarchy is clear, styling is consistent, and differentiation is maintained across themes.

**Button Anatomy**: Buttons have multiple components. Label text communicates action, icon (optional) provides visual reinforcement, background color establishes hierarchy, border defines edge, padding creates touchable area, and cursor change indicates interactivity. Testing validates all components are present and appropriate, sizing is adequate for touch, padding is consistent, and composition is harmonious.

**Button Sizing**: Size affects usability and hierarchy. Large buttons emphasize importance and improve touch targeting, medium buttons are standard for most interfaces, small buttons save space but risk poor mobile usability, and minimum size on mobile should be 44×44px (iOS) or 48×48px (Android). Testing validates sizing supports hierarchy, touch targets meet minimums, sizing is consistent across similar buttons, and mobile usability is maintained.

**Button Copy**: Button text should be action-oriented and clear. Use verbs to start button labels (Submit, Continue, Delete, Cancel), be specific about action result (Place Order vs Submit), keep labels concise but not too abbreviated, match user's language and expectations, and maintain consistency across similar actions. Testing validates labels are clear and specific, text isn't too long or too short, language matches user expectations, and consistency is maintained.

**Icon Buttons**: Buttons with only icons save space but risk clarity. Use only universally understood icons (hamburger menu, close X, trash for delete), provide accessible label (aria-label or visually hidden text), ensure icon meaning is clear in context, make touch target adequate (even if icon is small), and consider tooltip on hover for desktop. Testing validates icons are understandable, accessible labels are present, touch targets meet minimums, and tooltips (if present) are helpful.

**Button Groups**: Related buttons often appear together. Primary action should be rightmost in LTR languages (placement varies by context), secondary/tertiary follow to left, destructive actions might be separated or confirmed, spacing between buttons should be adequate (8px minimum), and group should work at all viewport sizes. Testing validates grouping is logical, ordering makes sense, spacing is appropriate, and responsive behavior is good.

### 14.2 Button State Testing

Buttons have multiple states requiring thorough testing for each.

**Default State**: Initial button appearance should be clear and inviting. Buttons should stand out as interactive elements, communicate hierarchy through styling, have adequate contrast against background, display label text clearly, and be obviously buttons (affordance). Testing validates default state is obvious, hierarchy is clear, contrast is sufficient, and button purpose is clear.

**Hover State**: Provides feedback on mouse interfaces. Hover should provide subtle visual feedback (color change, elevation increase), use appropriate cursor (pointer), be quick to respond (immediate or very brief transition), be consistent across all buttons of similar type, and not be relied upon for essential information (touch devices don't hover). Testing validates hover feedback is appropriate, cursor changes to pointer, response is immediate, consistency is maintained, and essential info isn't hover-only.

**Focus State**: Critical for keyboard navigation. Focus indicator should be highly visible (often blue border or outline), meet 3:1 contrast against button and background, be consistent across all interactive elements, not be removed without replacement (outline: none is almost always bad), and clearly distinguish from hover state. Testing validates focus indicator is obvious, contrast is sufficient, consistency is maintained, keyboard users can identify focus, and state is distinct from hover.

**Active/Pressed State**: Indicates button is being clicked. Active state should provide immediate visual feedback (typically slight scale down or color darken), be brief (only during click), be distinct from hover and focus, feel responsive, and work for both mouse and touch. Testing validates active feedback is immediate, duration is appropriate, state is distinguishable, feedback feels responsive, and works for all input methods.

**Loading State**: Indicates processing after click. Loading button should show spinner or progress indicator, disable further clicks (prevent double submission), maintain button dimensions (avoid layout shift), communicate progress to screen readers (aria-busy, aria-live), and feel responsive. Testing validates loading state is obvious, duplicate submissions prevented, layout is maintained, screen readers announce loading, and UX feels responsive even during wait.

**Disabled State**: Indicates button cannot currently be used. Disabled button should be visually distinct (typically grayed/faded), have cursor: not-allowed or cursor: default, be removed from tab order (disabled attribute or tabindex="-1"), be announced as disabled by screen readers (disabled or aria-disabled), and ideally communicate why disabled. Testing validates disabled state is obvious, keyboard navigation skips disabled buttons, cursor indicates non-interactive, screen readers announce disabled, and reason is clear if possible.

**Success State**: Confirms action completion (not always present). Success state might show checkmark icon, change to green color, display "Saved" or "Complete" text, briefly persist then revert or stay changed, and be announced to screen readers. Testing validates success state is clear, confirmation is provided, timing is appropriate, and communication is accessible.

**Error State**: Indicates action failure. Error state should show error color (often red), display error icon, present helpful error message, maintain opportunity to retry, and announce error to screen readers. Testing validates error state is obvious, message is helpful, retry mechanism exists, and error is announced to assistive tech.

### 14.3 Button Accessibility

Accessible buttons enable all users to take actions independently.

**Semantic HTML**: Use proper button elements. Use `<button>` for actions that don't navigate (submit, toggle, trigger), use `<a>` for navigation, never use `<div>` or `<span>` with onclick (poor accessibility), use type attribute (type="button" for non-submit, type="submit" for form submission), and maintain semantic meaning. Testing validates correct element is used, semantics match purpose, type attribute is appropriate, and assistive tech understands element correctly.

**Accessible Labels**: All buttons need perceivable labels. Use visible text label for most buttons, use aria-label for icon-only buttons, use aria-labelledby to reference visible text if needed, never rely only on placeholder or title, and ensure label text is meaningful. Testing validates all buttons have accessible names, labels are clear and specific, icon-only buttons have aria-label, and screen readers announce labels correctly.

**Keyboard Accessibility**: Buttons must be fully keyboard-accessible. Button is reachable via Tab key, Enter or Space activates button, button maintains visible focus indicator, button is in logical tab order, disabled buttons are skipped in tab order, and no keyboard traps are created. Testing validates keyboard navigation works correctly, activation works with both Enter and Space, focus indicators are visible, tab order is logical, and no traps exist.

**Touch Targets**: Mobile buttons must meet size minimums. Buttons should be minimum 44×44px (iOS guideline) or 48×48px (Android guideline), adequate spacing between adjacent buttons (minimum 8px), entire button area is tappable, and small icons have larger touch targets. Testing validates touch targets meet minimums, spacing prevents accidental activation, entire button is tappable, and mobile usability is good.

**Focus Management**: Proper focus behavior enhances usability. Focus should move logically after button activation, focus shouldn't be lost unexpectedly, focus should return appropriately after modal close, button triggering modal should receive focus on close, and focus shouldn't be trapped unintentionally. Testing validates focus behavior is appropriate, focus isn't lost, focus returns correctly, and no traps exist.

**Color and Contrast**: Visual indicators must be perceivable. Button text must meet 4.5:1 contrast against background (normal text) or 3:1 (large text ≥24px or ≥18.5px bold), button border/outline must meet 3:1 contrast against adjacent colors, don't rely on color alone to convey meaning (use text or icons too), ensure sufficient contrast in all states, and validate contrast in both light and dark modes. Testing validates contrast meets WCAG, color isn't sole indicator, all states have sufficient contrast, and both themes are compliant.

**Screen Reader Announcements**: Screen readers must understand buttons. Buttons should be announced as "button" not "link" or "group", label/name is announced, disabled state is announced, loading state is announced (aria-busy), and state changes are announced (aria-live for dynamic content). Testing validates screen reader announcements are correct, role is appropriate, states are communicated, and dynamic changes are announced.

### 14.4 Other Interactive Elements

Beyond buttons, many elements enable interaction.

**Links**: Links navigate to other pages or sections. Use `<a>` element with href, style links distinctly from buttons, underline text links in body content, provide focus indicators, indicate external links (icon or text), and ensure link purpose is clear from text. Testing validates links use correct element, styling is distinct from buttons, links are keyboard-accessible, external links are indicated, and purpose is clear.

**Toggle Switches**: Alternative to checkboxes for binary settings. Use role="switch" for accessibility, clearly label on/off states, provide immediate visual feedback when toggled, use aria-checked to communicate state, make switch large enough for touch (44px minimum height), and communicate that effect is immediate. Testing validates switch toggles correctly, states are clear, accessibility attributes are correct, touch target is adequate, and immediate effect is clear.

**Tabs**: Navigate between related content sections. Use appropriate ARIA (role="tablist", "tab", "tabpanel"), ensure tabs are keyboard-navigable (arrow keys to switch tabs), show active tab clearly, maintain tab focus when switching, lazy-load tab content when appropriate, and maintain tab state in URL if appropriate. Testing validates ARIA implementation is correct, keyboard navigation works (Tab key to tablist, arrow keys between tabs), active tab is obvious, and content loads correctly.

**Accordions**: Expand/collapse sections of content. Use button for accordion trigger, use aria-expanded to indicate state, use aria-controls to associate trigger with content, animate expand/collapse smoothly, allow multiple accordions open (or restrict to one), and maintain state appropriately. Testing validates ARIA is correct, keyboard navigation works, expand/collapse animations are smooth, multiple/single open behavior is correct, and state is maintained.

**Dropdown Menus**: Reveal options on interaction. Use button to trigger dropdown, use role="menu" and role="menuitem" if keyboard navigation is implemented, ensure keyboard navigation works (arrow keys), close on outside click, close on Escape key, manage focus appropriately (focus first item on open, return focus to trigger on close), and position dropdown appropriately (don't go off-screen). Testing validates trigger works, keyboard navigation functions correctly, closing behavior works, focus management is correct, and positioning is appropriate.

**Modals and Dialogs**: Overlay content requiring attention. Use role="dialog" or role="alertdialog", trap focus within modal, provide accessible close mechanism, close on Escape key, close on background click (usually), return focus to trigger on close, prevent background scroll, and ensure content is accessible. Testing validates ARIA role is correct, focus trap works, all close mechanisms function, focus returns correctly, scrolling is prevented, and content is accessible.

**Tooltips**: Provide supplemental information on hover or focus. Show tooltip on both hover and focus (keyboard accessible), use role="tooltip", use aria-describedby to associate with element, position tooltips to avoid covering related content, dismiss tooltip on Escape or when focus/hover is removed, and keep tooltip content concise. Testing validates tooltips appear on both hover and focus, ARIA association is correct, positioning is appropriate, dismissal works, and content is helpful.

### 14.5 Interactive Element Performance

Interaction responsiveness affects perceived quality.

**Tap Delay Elimination**: Remove 300ms tap delay on mobile. Use viewport meta tag with width=device-width, use touch-action CSS property where appropriate, and test that taps feel immediate. Testing validates no perceivable delay exists between tap and response.

**Animation Performance**: Interactive animations should be smooth. Use GPU-accelerated properties (transform, opacity), avoid animating layout properties, maintain 60fps during animations, use will-change sparingly for elements that will animate, and test on low-end devices. Testing validates animations are smooth, frame rates are good, animations don't cause jank, and performance is acceptable on low-end devices.

**Debouncing and Throttling**: Control rapid interactions. Debounce search input to avoid excessive queries, throttle scroll listeners to maintain performance, prevent double clicks on submit buttons, and provide feedback during processing. Testing validates debouncing works correctly, throttling doesn't degrade UX, double submissions are prevented, and feedback is provided.

**Perceived Performance**: Make interactions feel fast. Provide immediate visual feedback on click, show loading states quickly, use optimistic updates where appropriate, preload likely next actions, and communicate progress for long operations. Testing validates feedback is immediate, loading states appear promptly, optimistic updates work correctly, and UX feels fast.

### 14.6 Interactive Element Testing Tools

Various tools assist interactive element testing.

**Accessibility Checkers**: Automated tools catch many issues. axe DevTools checks button accessibility, Pa11y validates interactive elements, Lighthouse audits buttons and links, and WAVE evaluates interactive element semantics. Testing integrates these tools into workflows.

**Keyboard Testing**: Keyboard navigation must be tested manually. Tab through interface verifying focus indicators are visible, test activation with Enter and Space, test Escape to dismiss, verify arrow key navigation in compound widgets, and ensure no keyboard traps. Manual keyboard testing is essential.

**Screen Reader Testing**: Test with actual screen readers. Use NVDA (Windows), JAWS (Windows), VoiceOver (macOS/iOS), and TalkBack (Android). Verify buttons are announced correctly, states are communicated, labels are clear, and interaction is possible with audio-only output.

**Touch Testing**: Test on actual touch devices. Verify touch targets are adequate, no accidental activations occur, touch feedback is clear, and touch interactions feel responsive. Real device testing is essential as simulators don't perfectly replicate touch.

**Visual Regression**: Automated visual testing catches state regressions. Tools like Percy, Chromatic, and Applitools capture screenshots of all button states and interactive elements, compare against baselines, and flag changes. Integration into CI prevents regressions.

### 14.7 Interactive Element Best Practices

Industry best practices guide effective interactive element implementation.

**Use Semantic HTML**: Proper elements provide accessibility for free. Use `<button>` for actions, `<a>` for navigation, appropriate ARIA when needed, and semantic structure throughout.

**Make Interactive Elements Obvious**: Users should recognize interactive elements. Provide clear visual affordance, use appropriate cursor, ensure adequate contrast, and maintain consistency across similar elements.

**Provide Clear Feedback**: Users need to know their actions registered. Provide immediate visual feedback on interaction, show loading states for processing, communicate success and errors clearly, and ensure feedback is accessible.

**Support All Input Methods**: Users interact in various ways. Support mouse, keyboard, touch, and assistive technology, ensure functionality works with each method, and test with actual devices and input methods.

**Test Thoroughly**: Comprehensive testing ensures quality. Test all states of all interactive elements, test keyboard navigation extensively, test with assistive technology, test on actual devices, and test with real users.

---

*Continuing with more sections...*
