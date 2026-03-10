# 31. Design QA for E-commerce Interfaces


E-commerce interfaces require meticulous design QA as visual quality directly impacts conversion rates, trust, and revenue. Product pages, shopping carts, checkout flows, and payment interfaces demand pixel-perfect execution combined with flawless functionality and accessibility.

### 31.1 Product Page Design QA

Product pages are the critical conversion point in e-commerce, requiring comprehensive visual and functional testing.

**Product Image Quality and Gallery**: Product images are the primary selling tool in online retail. Test that main product image loads at high resolution, image zoom functionality works correctly (hover zoom, click to expand, pinch zoom on mobile), image zoom level is appropriate (can see fine details), zoomed image quality remains sharp (using higher-res source), product gallery thumbnails display correctly, thumbnail active state is clear, clicking thumbnails updates main image instantly, gallery navigation works (arrows, swipe), gallery supports keyboard navigation, alt text describes products accurately, image loading is optimized (lazy loading, responsive images), images have appropriate aspect ratio (not distorted), placeholder images show while loading, and failed image loads are handled gracefully (broken image indicators, retry options).

**Product Variants and Options**: Many products have multiple options requiring complex state management. Verify that variant selectors (color, size, material, etc.) display correctly, selected variant is visually clear, unavailable variants are disabled and visually distinct, selecting variants updates product image appropriately, variant thumbnails (if used) are accurate, variant selection updates price if prices differ, variant selection updates SKU and product details, dropdown variant selectors work correctly (for many options), swatch variant selectors are accessible (tooltips, labels), variant changes are smooth (no flickering or layout shift), variant state persists when navigating back, and variant URLs enable direct linking to specific options.

**Pricing Display**: Price is critical information requiring absolute accuracy. Test that price displays in correct currency and format, sale prices show alongside original price (with visual distinction), discounts calculate correctly and display percentage/amount saved, strikethrough pricing is clear, price updates correctly when variants change, quantity-based pricing works if applicable (bulk discounts), tax indication is clear (inclusive/exclusive of tax), shipping cost indication is appropriate (free shipping highlighted), price remains visible while scrolling (sticky positioning if designed), price formatting respects locale (decimal separators, currency symbols), and price accessibility is maintained (not just color to show discount).

**Product Information Layout**: Product details must be scannable and comprehensive. Verify that product title is prominent and descriptive, key features are highlighted (bullets, tags, badges), product description is readable and formatted appropriately, technical specifications are clear and organized, detailed information is accessible but not overwhelming (tabs, accordions, "Read more" links work correctly), badges (new, sale, limited, bestseller) display correctly, trust indicators (certifications, guarantees) are visible, size guides link correctly, care instructions are clear, inventory status is accurate (in stock, low stock, out of stock), availability information is current, and delivery estimates are accurate and clearly displayed.

**Add to Cart Functionality**: The add-to-cart action is the primary conversion goal. Test that "Add to Cart" button is prominent and accessible, button is clearly labeled (not ambiguous), button disabled state works (when required selections not made), button loading state shows while processing, button success state provides feedback (checkmark, "Added"), success feedback is clear but not disruptive (toast notification, modal, inline message), cart icon updates to reflect new item count, mini-cart preview works correctly (if designed), add-to-cart animation is smooth (item flying to cart icon, etc.), add-to-cart fails gracefully (out of stock, error conditions), and add-to-cart works with keyboard (Enter on focused button).

**Reviews and Social Proof**: Reviews and ratings significantly impact purchasing decisions. Verify that star ratings display accurately (match review scores), star ratings are accessible (text alternative, aria-label), aggregate review count is accurate, individual reviews display correctly, review sorting and filtering work (most helpful, recent, rating), review pagination works correctly, review images/videos display appropriately, verified purchase badges are clear, review helpfulness voting works (thumbs up/down), review reporting works (flag inappropriate content), and "No reviews yet" state is handled gracefully (call-to-action to write first review).

**Responsive Product Page**: Product pages must work flawlessly on mobile. Test that image gallery works well on mobile (swipeable, pinch-zoom), product info is readable without excessive scrolling, sticky add-to-cart appears appropriately on mobile (typically at bottom), variant selectors work well on touch, price remains visible, critical information is above fold or easily accessible, mobile layout prioritizes conversion path, accordions work smoothly for collapsed content, and mobile performance is good (images optimized, fast load).

### 31.2 Shopping Cart Design QA

Shopping carts must provide clear overview of selections while enabling easy modifications.

**Cart Item Display**: Each cart item needs complete, clear information. Verify that product images display correctly in cart, product names/titles are clearly readable, variant selections are displayed (size, color, etc.), price per item is accurate, quantity selector works correctly, quantity updates price dynamically, quantity limits work (min/max quantity, inventory limits), quantity input validates (no negative, no decimals unless appropriate), quantity buttons are accessible (keyboard, screen reader), item removal works clearly (trash icon, remove link), removal confirmation if appropriate, removed item provides feedback (fade out, slide out), item subtotal calculates correctly, and item subtotal updates when quantity changes.

**Cart Summary and Totals**: Cart totals must be accurate and clearly presented. Test that subtotal sums individual items correctly, shipping cost calculates accurately (may be estimate based on location), tax calculates correctly (if applicable at this stage), discounts apply correctly (promo codes, automatic discounts), coupon codes can be entered and validated, invalid coupon code shows clear error, applied discounts are itemized clearly, total is visually prominent, currency and formatting are correct, calculations update immediately when cart changes, and estimated vs final pricing is clearly indicated.

**Empty Cart State**: Empty cart needs appropriate messaging and guidance. Verify that empty cart message is clear and friendly, "Continue Shopping" or similar CTA is prominent, recently viewed or recommended products show (if designed), empty cart animation is pleasant (if used), cart icon reflects empty state (no count badge), and empty cart is accessible (screen reader friendly, keyboard navigable).

**Cart Modifications**: Users frequently modify cart contents. Test that quantity changes save immediately or on explicit "Update" action (be consistent), quantity changes don't lose items accidentally, "Save for Later" works if offered (items move to separate section), saved items can be moved back to cart, removing all items transitions to empty state gracefully, bulk actions work if offered (remove all, move all to wishlist), undo functionality works if offered (after item removal), and modifications provide clear feedback (loading states, confirmation).

**Cart Persistence**: Cart contents should persist across sessions. Verify that cart contents save when user navigates away, cart persists after browser close/reopen (reasonable timeframe), cart persists across devices when logged in, expired cart items are handled gracefully (show notification, remove or mark unavailable), price changes are indicated if product price changed since added, inventory changes are handled (item now out of stock), and cart merges correctly when logging in (guest cart + user account cart).

**Mini Cart and Cart Preview**: Many sites offer cart preview without full page. Test that mini cart shows accurate item count, mini cart preview displays on hover/click, mini cart shows key info (items, quantities, thumbnail images, subtotal), mini cart links to full cart page, mini cart "Checkout" button works, mini cart scrolls if many items, mini cart updates in real-time when items added, mini cart doesn't block important page content, mini cart dismisses appropriately, and mini cart is accessible.

### 31.3 Checkout Flow Design QA

Checkout is the most critical conversion flow requiring flawless execution.

**Checkout Progress Indicator**: Multi-step checkouts need clear progress indication. Verify that progress indicator shows all checkout steps clearly, current step is visually highlighted, completed steps are distinguished, future steps are indicated, step labels are descriptive (Shipping, Payment, Review, etc.), clicking completed steps navigates back (if allowed), progress indicator adapts to mobile (may become dropdown or simpler), progress indicator is accessible (keyboard navigation, screen reader support), and progress indicator doesn't distract from form completion.

**Form Field Layout and Design**: Checkout forms must be optimized for conversion. Test that form fields are appropriately sized and spaced, field labels are clear and positioned consistently (typically above fields), required fields are clearly indicated (asterisk, "required" label), placeholder text is helpful but not relied upon exclusively, input types are correct (email, tel, etc. for better mobile keyboards), autofill works correctly (name, address, payment, etc.), field grouping is logical (shipping address fields together), field order follows conventions (first name before last name, etc.), multi-column layouts work on desktop, single-column layouts on mobile, field focus states are clear, and field error states are visually distinct.

**Address Entry and Validation**: Address entry significantly impacts checkout success. Verify that address fields match user's country format, address autocomplete works (Google Places API or similar), apartment/suite field is available, ZIP/postal code format validates correctly for country, country selection is easy (dropdown, typeahead), country selection updates address format, shipping country restrictions are enforced, address validation provides helpful feedback (correcting typos, confirming unusual addresses), international addresses are supported properly, and "Ship to different address" works correctly.

**Payment Method Selection**: Payment method selection must be clear and trustworthy. Test that available payment methods display clearly with logos, payment method selection is obvious (radio buttons, tiles), selected payment method is visually distinct, payment method specific fields show/hide appropriately (credit card fields when card selected, PayPal buttons when PayPal selected), payment card logos are standard and recognizable, secure payment indicators are visible (padlock icons, security badges), CVV field has helpful tooltips, expiration date format is clear, card number formats with spaces (easier to verify), credit card validation provides immediate feedback, and alternative payment methods (Apple Pay, Google Pay, PayPal, etc.) work correctly.

**Order Review**: Final review step prevents errors. Verify that all order details are visible (items, quantities, prices, totals), shipping address is displayed clearly, billing address is shown (and editable), payment method is indicated (card ending in xxxx), shipping method is confirmed, estimated delivery is shown, order subtotal, taxes, shipping, discounts, and total are itemized, edit links work for each section (go back to relevant step), terms and conditions checkbox is clear, "Place Order" button is prominent, button label is clear ("Place Order", "Complete Purchase", etc., with price if designed), button loading state works during processing, and button is disabled during processing (prevent double-submission).

**Guest Checkout**: Guest checkout reduces friction. Test that guest checkout option is prominent, account creation isn't forced (unless business rule), guest email field works correctly, guest info is clearly communicated (order confirmation will go to email), optional account creation at end works (after successful order), guest checkout supports all payment methods, guest order tracking works, and guest checkout conversion rate is monitored (forcing account creation typically hurts conversion).

**Checkout Error Handling**: Errors must be handled gracefully. Verify that validation errors are clear and specific, errors appear inline near relevant fields (not just at top of page), error summary at top if multiple errors, errors prevent form submission (not submit and show errors after page reload), payment errors (declined cards, etc.) are clear and actionable, errors don't lose entered data (form remains populated), error recovery is obvious (what user needs to do), error messages are accessible (screen readers announce), and error messages are friendly and blame-free.

**Checkout Loading and Performance**: Checkout must be fast and responsive. Test that checkout pages load quickly (critical for conversion), loading states are clear during processing, asynchronous validation doesn't slow form completion, payment processing shows clear loading indicator, checkout doesn't block UI unnecessarily (use async where possible), checkout works on slower connections, checkout is optimized for mobile performance, images are optimized, and third-party scripts don't slow checkout.

### 31.4 Order Confirmation Design QA

Order confirmation reassures customers and provides critical information.

**Confirmation Message**: Clear confirmation is essential. Verify that confirmation message is prominent ("Order Confirmed", "Thank You", etc.), confirmation is immediate (no unnecessary delay after placing order), order number is clearly displayed and formatted, confirmation provides next steps (what happens next, when to expect delivery), confirmation tone is friendly and reassuring, confirmation page is bookmarkable, and confirmation is accessible (screen readers announce confirmation clearly).

**Order Details Summary**: Complete order details enable customer verification. Test that all purchased items are listed (images, names, quantities, prices), shipping address is displayed, billing address is shown, payment method is indicated (last 4 digits of card), order totals are itemized, estimated delivery is shown, tracking information is provided (or indication of when it will be available), invoice/receipt can be printed or downloaded, and order details are formatted for printing (print stylesheet).

**Email Confirmation**: Email confirmation is critical documentation. Verify that confirmation email sends immediately (within seconds of order completion), email contains complete order details (items, quantities, prices, totals, addresses), email is well-formatted (responsive email design), email includes relevant links (order tracking, customer service, product pages), email is accessible (semantic HTML, alt text for images), email passes spam filters (proper authentication, reasonable content), email subject is clear ("Your Order Confirmation - Order #12345"), and email includes PDF invoice attachment if designed.

**Next Steps and CTAs**: Guide customers to relevant next actions. Test that account creation CTA is shown if guest checkout was used, "Continue Shopping" link is available, "Track Order" link works (or indicates when tracking will be available), support/help links are clear, social media or review prompts are appropriately timed (not too pushy immediately), promotional content is tastefully integrated (related products, newsletter signup), and download mobile app prompt is shown if relevant.

### 31.5 Product Filtering and Search

Helping customers find products quickly is critical for conversion.

**Filter Interface Design**: Filters must be usable and accessible. Verify that available filters are relevant to product category, filters are logically organized (priority order), filter groups can be expanded/collapsed (accordions typically), selected filters are clearly indicated (checkboxes checked, pills shown), applied filters display above products (as removable tags/pills), filter counts show number of products per option, filter options update as filters applied (show only applicable remaining filters), "Clear All Filters" works correctly, filters work on mobile (often in drawer/overlay), and filters are keyboard accessible.

**Search Functionality**: Product search must be fast and relevant. Test that search bar is prominent in navigation, search provides autocomplete suggestions, suggestions include products, categories, and brands, search handles misspellings (did you mean...?, fuzzy matching), search provides instant results (as you type) or is very fast, search results are relevant (good ranking algorithm), search results can be sorted and filtered, "No results" page is helpful (suggestions, related searches, popular products), search tracks recent searches if designed, and search works on mobile (prominent, easy to access).

**Sort Functionality**: Sort options enable different discovery patterns. Verify that standard sort options are available (Featured, Price Low-High, Price High-Low, Newest, Best Selling, Highest Rated), sort order is clearly indicated (selected option highlighted), sort applies immediately or on explicit action (be consistent), sort maintains applied filters, sort works with pagination, sort options are accessible (keyboard, screen reader), and sort default makes sense for context (Featured for main category pages, Relevance for search results).

**Faceted Search**: Combining search with filters creates powerful discovery. Test that search query persists when applying filters, filters are relevant to search results, search refinement works (refining initial search), breadcrumbs show search + filters, URL reflects search query and filters (for sharing/bookmarking), and search + filter combination performs well.

### 31.6 E-commerce Accessibility

E-commerce accessibility is legally required and ethically important.

**Keyboard Navigation**: Entire shopping experience must be keyboard accessible. Verify that all interactive elements are keyboard accessible (products, filters, cart, checkout), Tab order is logical throughout, Enter activates buttons and links, Space selects checkboxes and radio buttons, Arrow keys navigate where appropriate (carousels, galleries), focus indicators are always visible and clear, keyboard shortcuts don't conflict with assistive tech, focus doesn't get trapped anywhere, and keyboard navigation is efficient (skip links, landmark navigation).

**Screen Reader Compatibility**: Content must be perceivable by screen readers. Test that all images have meaningful alt text (products, icons, badges), decorative images have empty alt attributes, dynamic content updates are announced (ARIA live regions for cart updates, price changes, etc.), form labels are programmatically associated, error messages are announced when they appear, status messages are announced (added to cart, order confirmed, etc.), ARIA attributes enhance understanding (aria-label, aria-labelledby, aria-describedby), and page structure uses semantic HTML (headings, landmarks, lists).

**Color and Contrast**: Visual information must be perceivable. Verify that text meets WCAG AA contrast ratios (4.5:1 for normal text, 3:1 for large text), links are distinguishable from surrounding text (not just by color), prices and discounts are distinguishable without color, product variants aren't indicated by color alone (labels, patterns, shapes also), form errors aren't indicated only by red color, and interactive states don't rely solely on color change.

**Touch Target Sizes**: Mobile commerce requires appropriate touch targets. Test that all interactive elements meet minimum 44x44px touch target size, closely spaced links/buttons have sufficient spacing, touch targets work reliably (tap registers consistently), and swipe gestures work smoothly on touch devices.

### 31.7 E-commerce Design QA Checklist

Comprehensive e-commerce testing checklist:

**Product Pages**:
☐ Product images are high-quality and load correctly
☐ Image zoom works correctly
☐ Image gallery navigation works (thumbnails, arrows, swipe)
☐ Variant selection works and updates appropriately
☐ Price is accurate and prominently displayed
☐ Add to cart is prominent and works correctly
☐ Inventory status is accurate (in stock, out of stock)
☐ Product information is comprehensive and scannable
☐ Reviews display correctly
☐ Responsive design works on all devices

**Shopping Cart**:
☐ Cart items display correctly (images, names, variants, prices)
☐ Quantity updates work correctly
☐ Cart totals calculate accurately
☐ Item removal works and provides feedback
☐ Empty cart state is clear
☐ Cart persistence works
☐ Mini cart preview works correctly

**Checkout**:
☐ Checkout flow is clear and logical
☐ Progress indicator shows current step
☐ Form fields are clearly labeled
☐ Required fields are indicated
☐ Address autocomplete works
☐ Payment methods display correctly
☐ Order review shows complete information
☐ Guest checkout is available
☐ Error handling is clear and helpful
☐ Loading states work correctly
☐ Checkout performs well (fast load, responsive)

**Order Confirmation**:
☐ Confirmation message is clear and immediate
☐ Order number is displayed prominently
☐ Order details are complete
☐ Confirmation email sends promptly
☐ Email contains all order information
☐ Next steps are clear

**Search and Filters**:
☐ Search is prominent and works correctly
☐ Autocomplete provides relevant suggestions
☐ Search results are relevant
☐ Filters are logical and usable
☐ Applied filters are clearly shown
☐ Sort options work correctly
☐ Mobile filtering works well

**Accessibility**:
☐ Entire flow is keyboard accessible
☐ Screen readers can navigate successfully
☐ Color contrast meets WCAG standards
☐ Touch targets are appropriately sized
☐ Alt text is provided for all images
☐ Form labels are programmatically associated
☐ Error messages are announced to screen readers

---
