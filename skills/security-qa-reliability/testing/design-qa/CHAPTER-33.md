# 30. Design QA for Data Visualization


Data visualizations including charts, graphs, dashboards, and real-time displays require specialized testing to ensure accuracy, readability, accessibility, and performance. Visualizations must communicate data clearly while maintaining usability across devices and contexts.

### 30.1 Chart Accuracy and Data Integrity

The primary purpose of data visualization is accurate communication. Testing must verify that visualizations faithfully represent underlying data.

**Data Mapping Verification**: Test that all data points from source data appear in visualization, data values map correctly to visual properties (position, length, area, color), scales and axes represent data range accurately, data transformations (aggregations, calculations) are correct, null or missing data is handled appropriately (gaps, zero, or indicators), outliers display correctly without breaking visualization, and edge cases (very large numbers, very small numbers, negative values) work correctly.

**Scale and Axis Accuracy**: Axes are fundamental to chart interpretation. Verify that axis labels are accurate and appropriately formatted, axis range includes all data without unnecessary space, axis scales are linear unless explicitly logarithmic/other, zero baseline is included for bar charts (excluding zero can mislead), tick marks align with data points appropriately, gridlines (if present) help rather than clutter, axis titles clearly identify what's being measured, and axis inversions (if any) are intentionally designed and clear.

**Legend and Label Testing**: Labels and legends are critical for understanding. Test that legend items correspond correctly to data series, legend colors match visualization colors exactly, legend order is logical (matches data order or importance), legend is complete (all series represented), data labels display correctly at all sizes, labels don't overlap or become illegible, labels position appropriately (inside/outside elements), labels truncate or abbreviate gracefully if needed, and hover tooltips provide additional detail appropriately.

**Color and Visual Encoding**: Visual encoding must be accurate and accessible. Verify that color assignments are consistent across related charts, color intensity or saturation maps to data magnitude if used, color-blind safe palettes are used, color alone isn't the only means of differentiation (patterns, shapes, or labels also used), contrast is sufficient for readability, semantic colors match conventions (red for negative, green for positive, though consider color-blind implications), brand colors are used appropriately, and color changes based on thresholds work correctly.

**Responsive Data Visualization**: Visualizations must adapt to viewport size. Test that charts resize appropriately for different screens, axis labels remain readable when space is limited, legends reposition or transform for small screens (may move below chart or become abbreviated), tooltips work well on touch devices, data density adjusts for smaller displays (fewer ticks, simplified views), mobile-specific visualizations provide appropriate alternatives when needed, and landscape vs portrait orientations work well.

### 30.2 Chart Type-Specific Testing

Different chart types have unique testing requirements.

**Line Charts**: Line charts show trends over time or continuous data. Test that lines connect data points correctly, line styles differentiate multiple series (solid, dashed, dotted), line thickness is appropriate and accessible, data point markers are visible and clickable/hoverable, gaps in data are handled correctly (broken lines or interpolation), smooth curves (if used) don't misrepresent data, area under line (if filled) renders correctly, and animations along line paths work smoothly.

**Bar and Column Charts**: Bar charts compare discrete categories. Verify that bar widths are consistent within series, bars align with axis labels, bar spacing is appropriate (not too cramped or sparse), stacked bars sum to correct totals, grouped bars are clearly differentiated, horizontal vs vertical orientation works correctly, bars start at zero baseline (excluding zero is misleading), bars with negative values render correctly (below axis), and hover/click interactions work on each bar.

**Pie and Donut Charts**: Circular charts show proportions of a whole. Test that slice sizes accurately represent proportions (angles correct), slices sum to 100% (or appropriate total), slice order is logical (typically largest to smallest), slice colors are distinct and accessible, slice labels don't overlap, percentage labels are accurate, slice interactions (hover, click, explode) work correctly, donut center content (if present) displays correctly, and alternatives for many slices are considered (pies with >7 slices become hard to read).

**Scatter Plots**: Scatter plots show relationships between variables. Verify that points position correctly based on x and y values, point sizes reflect data if used (bubble charts), point colors/shapes differentiate series, overlapping points are handled (transparency, jittering, or clustering), axis scales accommodate all points, outliers don't cause scaling issues (consider separate treatment), hover shows data for specific points, selection and filtering work on points, and trend lines (if present) calculate correctly.

**Heat Maps**: Heat maps show data density or intensity across dimensions. Test that color scale accurately represents data range, color scale is accessible and distinguishable, color scale legend is clear (min/max indicated), cell sizes are appropriate for data granularity, cell borders help readability if cells are small, hover tooltips show exact values, missing data is visually distinct from zero, and responsive behavior maintains readability (may reduce granularity on small screens).

**Time Series and Real-Time Charts**: Charts showing data over time require special handling. Verify that time axis formatting is appropriate (seconds, minutes, hours, days, etc.), time zone handling is correct and indicated, time ranges can be adjusted (zoom, pan), real-time updates work smoothly (no jarring shifts), historical data loads efficiently, live data updates don't cause performance issues, time gaps (weekends, holidays) are handled appropriately, and animation of new data points is smooth.

### 30.3 Interactive Visualization Testing

Modern visualizations are highly interactive, requiring comprehensive interaction testing.

**Hover and Tooltip Interactions**: Hover tooltips provide detail on demand. Test that tooltips appear promptly on hover (not delayed too long), tooltips position correctly (don't go off-screen), tooltips don't obscure related data, tooltip content is formatted clearly (labels, values, units), tooltips work on touch devices (tap to show, tap outside to hide), tooltips can be dismissed easily, cursor changes indicate interactive elements, and tooltips perform well with many data points.

**Click and Selection**: Clicking often triggers drill-downs or filters. Verify that clicking elements triggers expected actions, selected state is visually clear, multiple selection works if designed, selection persists appropriately (or clears intentionally), selected items can be deselected, selection affects related visualizations if applicable, selection provides feedback (loading states, confirmations), and selection is keyboard accessible.

**Zoom and Pan**: Exploring large datasets requires zoom and pan. Test that scroll or pinch zoom works smoothly, zoom maintains aspect ratio and data accuracy, zoom controls (buttons, sliders) work correctly, pan drag works with mouse and touch, panning stays within data bounds (or allows appropriate overscroll), zoom/pan state can be reset, zoom/pan doesn't break labels or legends, and performance remains good while zooming/panning.

**Filter and Search**: Filtering enables focused analysis. Verify that filters apply correctly to visualization, filtered data updates visualization immediately, filter combinations work correctly (AND/OR logic), filters can be cleared easily, filtered state is visually indicated, filters are accessible and keyboard-operable, search within visualization data works, and filter performance is acceptable with large datasets.

**Cross-Chart Interactions**: Dashboards often link multiple visualizations. Test that selecting data in one chart filters others (if designed), hover in one chart highlights related data in others, interactions are performant with multiple charts, interaction timing is coordinated (not laggy or out of sync), clearing selections resets all linked charts, interaction direction is intuitive, and interactions work across chart types.

### 30.4 Dashboard and Multi-Visualization Testing

Dashboards combine multiple visualizations requiring system-level testing.

**Layout and Responsiveness**: Dashboard layouts must adapt to viewports. Test that dashboard grid system works correctly, visualizations resize proportionally, layout reflows appropriately on smaller screens, visualizations stack vertically on mobile if needed, visualization priority is maintained (important charts stay visible), scroll behavior is intuitive, dashboard navigation works on all devices, and layout doesn't break with different data ranges.

**Load Performance**: Dashboards can load substantial data. Verify that visualizations load efficiently (consider lazy loading), loading states are clear for each visualization, partial loading works (some charts load while others still loading), failed chart loads are handled gracefully (error states, retry), data fetching is optimized (batch requests if possible), caching is used appropriately, and dashboard remains usable while data loads.

**Data Consistency**: Multiple visualizations must show consistent data. Test that all visualizations reflect same data source and time range, time zones are consistent across dashboard, calculations are consistent (same formulas, aggregations), data updates propagate to all relevant visualizations, refresh behavior updates all visualizations, stale data is indicated if present, and data discrepancies are investigated and resolved.

**Drill-Down and Navigation**: Dashboards often enable hierarchical exploration. Verify that drill-down navigation works correctly, breadcrumbs or back navigation is clear, drilled-down views maintain context, URL reflects drill-down state (for sharing/bookmarking), drill-down performance is acceptable, drill-down transitions are smooth, and drill-down is keyboard accessible.

**Export and Sharing**: Users often need to export visualizations. Test that export to image works correctly (PNG, SVG, etc.), export includes all visible data and labels, exported images have appropriate resolution, export to data formats works (CSV, Excel, JSON), exported data is formatted correctly, sharing links work correctly, shared views reflect correct data and state, and export is accessible (keyboard, screen reader).

### 30.5 Accessibility in Data Visualization

Data visualizations present significant accessibility challenges requiring creative solutions.

**Screen Reader Accessibility**: Visualizations must be perceivable by screen readers. Verify that charts have descriptive text alternatives (alt text, aria-label), data tables are provided as alternatives or supplements, key insights are available as text (not only visual), ARIA roles describe chart structure (figure, img, etc.), ARIA live regions announce dynamic updates, screen readers can navigate to data points, data values are announced clearly, and descriptions include context (axes, scales, units).

**Keyboard Navigation**: Visual data exploration must work with keyboard. Test that visualizations can receive keyboard focus, Tab navigates through interactive elements, Arrow keys navigate data points within chart, Enter activates selections or drill-downs, Escape closes tooltips or overlays, keyboard shortcuts are documented and intuitive, focus indicator is always visible, and keyboard navigation is efficient (not requiring excessive tabbing).

**Color Contrast and Pattern**: Visual encoding must work for users with color blindness. Verify that color combinations meet WCAG AA contrast ratios, color isn't the only means of differentiation (patterns, shapes, labels also used), color-blind safe palettes are used, colorblind simulation testing is performed, high-contrast mode is supported, patterns/textures differentiate series, legends help interpretation without relying solely on color, and semantic colors are used thoughtfully (not all red/green).

**Zoom and Magnification**: Users may need to magnify visualizations. Test that browser zoom doesn't break visualizations (elements remain readable, positioned correctly), text labels remain readable at high zoom (don't overlap), SVG visualizations scale crisply, canvas visualizations maintain quality when zoomed, responsive breakpoints work with browser zoom, and magnification software works correctly with visualizations.

**Motion and Animation**: Animated visualizations can cause problems for some users. Verify that animations respect prefers-reduced-motion, essential animations remain in simplified form, decorative animations are disabled for reduced motion, animations don't flash or flicker excessively, auto-playing animations can be paused, animation speed is appropriate (not too fast), and animations don't convey critical information exclusively.

### 30.6 Real-Time Data Visualization Testing

Real-time visualizations updating with live data require specialized testing.

**Update Performance**: Live updates must be smooth and performant. Test that updates render smoothly without janking, update frequency is appropriate (not too fast, causing confusion), throttling/debouncing works correctly, performance remains good with continuous updates, CPU usage is reasonable, memory leaks don't occur over time, and updates work efficiently across device capabilities.

**Data Streaming**: Streaming data requires careful handling. Verify that streaming connection establishes correctly, connection failures are handled gracefully (retry, fallback), reconnection works after network disruption, buffering handles bursts of data, data queue doesn't grow unbounded (memory management), old data is removed appropriately (sliding windows), and streaming works across browsers and devices.

**Visual Stability**: Updates shouldn't disorient users. Test that axis scales adjust smoothly (not jumping erratically), new data transitions smoothly (not appearing abruptly), colors remain consistent as data changes, labels update without flickering, legends stay stable, chart focus remains stable (doesn't auto-scroll unless intended), and user interactions aren't interrupted by updates (can still hover, select during updates).

**Alert and Notification**: Real-time systems often include alerts. Verify that threshold alerts trigger correctly, alerts are visually distinct (color, icons, flashing), alerts are announced to screen readers (ARIA live regions), alert sounds respect user preferences, alerts can be acknowledged or dismissed, alert history is accessible, critical alerts have appropriate priority, and alert frequency is appropriate (not overwhelming).

**Historical vs Real-Time**: Many visualizations show both historical and real-time data. Test that transition from historical to real-time is clear, time axis handles both correctly, different update frequencies work (historical is static, real-time updates), switching between views works correctly, historical data loads efficiently, and real-time data doesn't cause performance issues.

### 30.7 Data Visualization Testing Checklist

Comprehensive data visualization testing checklist:

**Data Accuracy**:
☐ All data points are represented correctly
☐ Scales and axes are accurate
☐ Calculations (aggregations, percentages) are correct
☐ Null/missing data is handled appropriately
☐ Edge cases (very large/small values) work
☐ Data updates reflect in visualization
☐ Time zones are handled correctly

**Visual Design**:
☐ Colors are accessible (color-blind safe, sufficient contrast)
☐ Legends are accurate and complete
☐ Labels are readable and don't overlap
☐ Chart type is appropriate for data
☐ Visual encodings (size, color, position) are accurate
☐ Brand guidelines are followed
☐ Visual hierarchy is clear

**Responsiveness**:
☐ Charts resize appropriately for different screens
☐ Labels remain readable on small screens
☐ Mobile provides appropriate alternatives
☐ Touch interactions work correctly
☐ Landscape and portrait work well
☐ Extreme viewport sizes are handled

**Interactivity**:
☐ Hover tooltips work correctly
☐ Click interactions trigger expected actions
☐ Zoom and pan work smoothly
☐ Filters apply correctly
☐ Selection is visually clear
☐ Interactions are performant
☐ Touch gestures work on mobile

**Accessibility**:
☐ Screen reader alternatives are provided
☐ Keyboard navigation works throughout
☐ Color contrast meets WCAG standards
☐ Color isn't the only differentiator
☐ Focus indicators are visible
☐ ARIA attributes are correct
☐ Animations respect prefers-reduced-motion

**Performance**:
☐ Large datasets render efficiently
☐ Real-time updates are smooth
☐ No memory leaks over time
☐ Loading states are clear
☐ Failed loads are handled gracefully
☐ Export/download works correctly

---
