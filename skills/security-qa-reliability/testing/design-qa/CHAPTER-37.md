# 34. Design QA for Internationalization (i18n)


Internationalization (i18n) and localization (l10n) present unique design QA challenges. Text expansion, layout reflows, different writing directions, cultural conventions, and regional differences all require careful testing to ensure interfaces work seamlessly for global audiences.

### 34.1 Text Expansion and Layout Reflow

Different languages take different amounts of space to express the same concept. English text, typically a baseline, can expand significantly when translated.

**Text Expansion Guidelines**: Text expansion varies by language. Test expansion scenarios where German text expands 25-40% compared to English, French expands 15-25%, Spanish expands 15-25%, Italian expands 15-25%, Portuguese expands 20-30%, Russian expands 15-25%, Asian languages (Chinese, Japanese, Korean) often contract 15-20% but may expand vertically for text wrapping, and Arabic/Hebrew expand 15-25% but also have right-to-left considerations. UI elements must accommodate these variations gracefully.

**Button and Label Testing**: Short labels are especially vulnerable. Test that primary action buttons don't wrap awkwardly (buy, submit, continue), tab labels remain visible and readable, navigation items don't overlap or truncate excessively, form labels don't break layouts, menu items fit within containers, error messages display fully (may expand significantly in translation), and success messages remain visible.

**Text Overflow Handling**: Overflow must be handled gracefully. Verify that ellipsis truncation works correctly (text-overflow: ellipsis), truncation includes title attributes for hover reveal, important text is never truncated (critical error messages, prices), containers expand vertically when text wraps (flexbox behavior), min-height allows content expansion, max-width constraints prevent excessive expansion, text scaling maintains readability at small sizes, and overlapping text is prevented with proper spacing.

**Component Width Flexibility**: Components must be width-flexible. Test that fixed-width buttons accommodate translations (min-width vs fixed-width), input fields don't break when labels expand, select dropdowns widen appropriately, table columns resize gracefully, card components expand vertically as needed, sidebar navigation handles longer items, tabs overflow or wrap correctly, and badges/pills expand or truncate gracefully.

**Font Sizing Across Scripts**: Different scripts have different readability needs. Verify that font sizes are appropriate for each script, line-height adjusts for script needs (CJK characters often need less line-height), font-weight changes don't harm readability (some scripts become illegible at bold weights), custom fonts support all target languages, fallback fonts are appropriate and match metrics, and text remains readable when mixed scripts appear together.

### 34.2 Right-to-Left (RTL) Language Support

RTL languages (Arabic, Hebrew, Persian, Urdu) require complete layout inversion and specific text handling.

**Layout Mirroring**: RTL requires fundamental layout changes. Test that entire layout flips horizontally (main content on right, sidebar on left), navigation flows right-to-left, menu items align right, breadcrumbs read right-to-left, form labels align appropriately (may flip or stay same depending on design), buttons in button groups reverse order, pagination controls reverse, timeline or process steps reverse direction, and card layouts adjust (images may move positions).

**Text Direction and Alignment**: Text must flow correctly. Verify that RTL text starts from right and flows left, text alignment is right for RTL (text-align: right), block-level elements align correctly, mixed RTL and LTR text flows correctly (bidirectional algorithm), numbers within RTL text flow correctly, punctuation at sentence boundaries positions correctly, lists (bullets, numbers) align appropriately, and quotes and parentheses face correct directions.

**Icon and Symbol Directionality**: Icons may need adjustment for RTL. Test that directional icons flip (arrows, chevrons, navigation), progress indicators reverse direction, play buttons may stay same (universal) or flip, checkmarks typically stay same (universal), sorting indicators flip (ascending/descending), back/forward arrows reverse, undo/redo icons reverse, and icon placement adjusts (may need margin/padding changes).

**Form Input Considerations**: Forms require special attention for RTL. Verify that text input fields accept RTL text correctly, cursor positioning works correctly in mixed text, placeholders align appropriately (often based on field type), input masks work for RTL locales, date pickers adapt to local format (Hijri, Hebrew calendar), currency input handles RTL currency symbols, phone number formats adapt to local conventions, and validation messages display correctly.

**CSS Logical Properties**: Modern CSS supports bidirectional layouts. Test that logical properties work correctly (margin-inline-start instead of margin-left), logical values work (text-align: start instead of text-align: left), border-radius logical properties work, inset shorthand works, flexbox row-reverse adapts appropriately, grid logical values work, and fallback CSS works in older browsers.

### 34.3 Date, Time, and Number Formatting

Different locales have different conventions for displaying temporal and numerical data.

**Date Formats**: Date formats vary dramatically by locale. Test that date formats match locale expectations (US: MM/DD/YYYY, UK: DD/MM/YYYY, Japan: YYYY/MM/DD), month names are translated, day names are translated, relative dates work (today, yesterday, in 3 days), date pickers match local calendar (Gregorian, Hijri, Hebrew, Buddhist, etc.), date ranges format correctly, and date parsing accepts local formats.

**Time Formats**: Time display varies by region. Verify that 12-hour vs 24-hour format matches locale (US typically 12-hour with AM/PM, most of Europe 24-hour), time zone handling is clear, time zone names are localized, relative time is accurate across time zones, and countdown timers format appropriately for locale.

**Number Formats**: Numbers format differently worldwide. Test that decimal separators match locale (comma vs period), thousands separators match locale (period vs comma vs space), currency symbols position correctly (before or after number), negative numbers display correctly (minus sign, parentheses), percentages format correctly, phone numbers format for local conventions, and large numbers use appropriate abbreviations (1K, 1万, etc.).

**Currency Display**: Currency requires precise formatting. Verify that currency symbol displays correctly ($, €, ¥, £, etc.), currency symbol position is correct for locale, decimal places match currency (JPY has no decimals, most others have 2), currency codes display when needed (USD, EUR), multiple currencies display correctly together, and currency conversion is clearly indicated.

**Address Formats**: Address structure varies globally. Test that address fields match local format (different countries have different field requirements), address display formats correctly, postal code field accepts local format (ZIP vs postcode), state/province field adapts to country (some have states, some don't), address validation is appropriate for locale, and address autocomplete works with local services.

### 34.4 Cultural and Regional Considerations

Beyond language, cultural differences affect design.

**Color Symbolism**: Colors have different meanings across cultures. Test that green (positive in West, sometimes negative in China), red (warning/danger in West, good fortune in China), white (purity in West, mourning in East Asia), and black (sophistication in West, mourning in West, evil in some cultures) are used appropriately. Consider color adaptations for regional versions if needed.

**Image Content**: Images may need cultural adaptation. Verify that people in images represent target demographics appropriately, gestures in images are culturally appropriate (thumbs up is offensive in some regions), clothing in images is culturally appropriate, symbols and icons are culturally neutral or adapted, and product images may need regional variations.

**Content Density**: Different cultures have different preferences for information density. Test that high-density layouts work for cultures expecting lots of information (East Asian markets often prefer), low-density layouts work for cultures preferring whitespace (Western markets typically), and appropriate defaults are set by region.

**Social Proof**: Social proof elements may need regional adaptation. Verify that testimonials match regional demographics, case studies feature regional customers, review counts display appropriately, trust badges match regional expectations, and payment method icons match regional preferences.

**Legal and Regulatory**: Regional legal requirements affect design. Test that privacy policy links are present and accessible, cookie consent appears where required, terms of service are accessible, age verification appears where required, accessibility statements are present where required, and regional disclaimers are visible.

### 34.5 i18n Testing Checklist

Comprehensive internationalization testing checklist:

**Text Expansion**:
☐ UI accommodates 25-40% text expansion for German
☐ Buttons don't truncate critical text
☐ Navigation remains readable when expanded
☐ Forms accommodate longer labels
☐ Error messages display fully
☐ Text overflow is handled gracefully (ellipsis, wrapping)
☐ Components expand vertically appropriately

**RTL Languages**:
☐ Layout flips correctly for RTL locales
☐ Text direction is correct (right-to-left)
☐ Directional icons flip appropriately
☐ Navigation flows right-to-left
☐ Forms work correctly in RTL
☐ CSS logical properties are used
☐ Mixed LTR/RTL text flows correctly

**Date, Time, Numbers**:
☐ Date formats match locale conventions
☐ Time formats match locale (12/24 hour)
☐ Number formatting matches locale (decimal/thousands separators)
☐ Currency displays correctly with proper symbol position
☐ Phone numbers format for local conventions
☐ Address fields match local format

**Cultural Considerations**:
☐ Colors are culturally appropriate
☐ Images represent target demographics
☐ Content density matches regional preferences
☐ Social proof is locally relevant
☐ Legal/regulatory requirements are met
☐ Content is culturally sensitive

**Technical Implementation**:
☐ Locale detection works correctly
☐ Language switching works smoothly
☐ URL structure handles locales appropriately
☐ SEO meta tags are localized
☐ Font loading supports all character sets
☐ Right-to-left CSS is applied correctly
☐ Content is translatable (no hardcoded strings)

---
