# 33. Design QA for Video and Rich Media


Video players, carousels, sliders, image galleries, and other rich media components require specialized testing to ensure visual quality, performance, accessibility, and cross-device compatibility.

### 33.1 Video Player Design QA

Video players are complex components with numerous states and controls requiring thorough testing.

**Player Controls and UI**: Video controls must be intuitive and accessible. Test that play/pause button is prominent and clearly labeled, play button placement is conventional (center overlay + bottom controls), volume control works correctly, volume slider is precise and responsive, mute button works and shows state clearly, progress bar shows current position accurately, progress bar is scrubbable (click or drag to seek), progress bar shows buffered ranges, time displays show current time and duration, playback speed control works if provided (0.5x, 0.75x, 1x, 1.25x, 1.5x, 2x), settings menu works correctly (quality, captions, speed), fullscreen button works across browsers and devices, picture-in-picture button works if supported, cast button appears if casting is available, and control bar auto-hides after inactivity.

**Player States**: Video players have many distinct states. Verify that loading state shows spinner or progress, buffering state indicates when video is loading more data, playing state is clear (pause button visible), paused state shows play button, ended state shows replay option and next video suggestion if applicable, error state shows clear message and recovery options, disabled state is visually distinct (if video unavailable), and state transitions are smooth and clear.

**Responsiveness and Sizing**: Video players must adapt to containers and viewports. Test that player maintains aspect ratio correctly (16:9, 4:3, 21:9, etc.), player resizes smoothly when container changes, player works in various layout contexts (full-width, sidebar, grid), player controls remain usable at small sizes, player controls adapt for touch on mobile (larger touch targets), player fullscreen works correctly (native fullscreen API), player fullscreen orientation works (landscape preferred for video), and player exits fullscreen correctly.

**Video Quality and Performance**: Video playback must be smooth and high-quality. Verify that video loads and starts promptly, adaptive bitrate works (switches quality based on bandwidth), quality settings work if manual control provided, video plays smoothly without stuttering, seeking is responsive (clicking progress bar), skip forward/backward controls work (10s increments typical), video performance is good on various devices, video doesn't cause excessive CPU usage, video doesn't drain battery excessively, and video works on slow connections (lower quality but still plays).

**Captions and Subtitles**: Captions are essential for accessibility. Test that captions can be enabled/disabled, caption selection works if multiple languages, captions display correctly (readable font, appropriate size), caption background provides sufficient contrast, captions don't obscure important video content, captions sync correctly with audio, caption position is appropriate (bottom-center typical), captions word-wrap correctly, captions work in fullscreen mode, and caption styling follows best practices (WCAG guidelines).

**Keyboard Controls**: Video players must be fully keyboard accessible. Verify that Space bar plays/pauses video, K key plays/pauses (YouTube convention), M key mutes/unmutes, F key toggles fullscreen, Arrow keys seek (left/right) and adjust volume (up/down), 0-9 keys jump to percentage points (5 key jumps to 50%), keyboard controls work when player is focused, focus indicator is visible on controls, Tab navigates through controls, and keyboard shortcuts are documented (help overlay).

**Accessibility**: Video content must be accessible. Test that player controls have proper ARIA labels, player state is announced to screen readers, captions/subtitles are available for all videos, audio descriptions are available for visual content (if appropriate), transcript is provided (linked or expandable), keyboard navigation works throughout, focus management is correct, player doesn't trap focus, color contrast meets WCAG standards, and player works with assistive technologies.

**Mobile and Touch Interactions**: Mobile video players have specific requirements. Verify that tap to play/pause works (single tap on video), double-tap to seek works (skip 10s forward/backward, YouTube-style), pinch-zoom works in fullscreen, swipe up/down adjusts brightness or volume (if implemented), tap shows/hides controls, controls auto-hide on mobile after inactivity, fullscreen works correctly on mobile (landscape orientation), inline playback works on iOS (playsinline attribute), autoplay works within platform restrictions (muted autoplay typically allowed), and mobile browser UI (address bar, etc.) doesn't interfere.

### 33.2 Image Gallery and Lightbox Testing

Image galleries and lightbox modals for viewing images require careful testing of navigation, zoom, and presentation.

**Gallery Layout**: Image galleries must present images attractively. Test that gallery grid layout is clean and organized, image aspect ratios are handled correctly (cropped consistently or varied heights work well), image thumbnails are sharp and high-quality, thumbnails lazy load as user scrolls, gallery is responsive (columns adjust for viewport), image captions or titles are readable, gallery performance is good with many images, and gallery works on mobile (appropriate thumbnail sizes, touch-friendly).

**Lightbox Opening**: Lightbox activation must be smooth. Verify that clicking thumbnail opens lightbox smoothly, lightbox animation is smooth (fade in, scale up, etc.), lightbox appears above all other content (z-index), lightbox backdrop darkens background, lightbox closes background scroll (body scroll lock), focus moves into lightbox, and keyboard users can activate lightbox (Enter on focused thumbnail).

**Image Navigation**: Users must be able to move through images easily. Test that previous/next buttons are prominent and accessible, clicking background image advances to next (if designed this way, though clicking backdrop more commonly closes), arrow key navigation works (left/right for prev/next), navigation wraps or stops at ends (depending on design), navigation works with keyboard, swipe gestures work on mobile/touch devices, navigation is announced to screen readers, and navigation indicators show current position (3 of 24, etc.).

**Image Zoom and Pan**: High-resolution images often need zoom functionality. Verify that zoom control is available and accessible, pinch-zoom works on touch devices, scroll-zoom works with mouse wheel, zoom in/out maintains center point (or focuses on cursor), max zoom is appropriate (can see details without excessive pixelation), panning works when zoomed (drag to pan), panning boundaries work (can't pan beyond image), zoom resets when navigating to different image, and zoom level indicator is visible.

**Image Loading and Quality**: Image quality must be optimized. Test that full-res images load quickly, loading indicator shows while image loads, progressive image loading provides quick preview (low-res, then high-res), images are sharp at all screen densities (srcset, 2x images), image optimization is good (file size vs quality balance), failed image loads are handled gracefully (retry, placeholder), and images work on slow connections.

**Captions and Metadata**: Image context enhances understanding. Verify that image captions are readable (white text on dark background typical), captions don't obscure image, caption can be toggled if lengthy, image metadata is available (EXIF info, location, etc., if relevant), image credit/attribution is shown if needed, caption is accessible (aria-describedby or within lightbox content), and caption works on mobile (may move below image).

**Lightbox Closing**: Users need clear ways to exit lightbox. Test that X close button is prominent and accessible, clicking backdrop closes lightbox (outside image), Escape key closes lightbox, closing returns focus to trigger thumbnail, closing animation is smooth, scroll is restored when lightbox closes, and mobile back button closes lightbox (browser history managed).

**Accessibility**: Lightbox must be fully accessible. Verify that lightbox has appropriate ARIA role (dialog), lightbox is labeled (aria-labelledby), focus trap works (Tab cycles through lightbox only), image alt text is provided, controls are keyboard accessible, screen readers announce image changes, navigation provides context (image X of Y), and close button is clearly labeled.

### 33.3 Carousel and Slider Testing

Carousels and sliders enable browsing multiple items, but require careful implementation to be usable and accessible.

**Carousel Navigation**: Users must be able to move through carousel items. Test that prev/next buttons are visible and clickable, buttons are disabled at ends if carousel doesn't loop, buttons are accessible (keyboard and screen reader), arrow keys navigate slides if carousel is focused, pagination dots indicate current slide and total slides, pagination dots are clickable to jump to slides, swiping works on touch devices, autoplay works if designed (with pause control), and autoplay stops on user interaction.

**Carousel Transitions**: Slide transitions significantly affect user experience. Verify that transitions are smooth and not jarring, transition duration is appropriate (300-500ms typical), transition easing feels natural, transition doesn't cause layout shift, transition respects prefers-reduced-motion, transition direction is clear (left-right, fade, etc.), transitions work well with images and text, and transition performance is good (60fps).

**Carousel Responsiveness**: Carousels must adapt to viewport sizes. Test that carousel items resize appropriately, number of visible items adjusts for viewport (3 on desktop, 1 on mobile, etc.), carousel controls remain usable on small screens, touch targets are appropriately sized on mobile, carousel scrolling works on all devices, carousel works in portrait and landscape, and carousel performance is good on mobile.

**Carousel Content**: Carousel items must be accessible and high-quality. Verify that images are high-quality and load correctly, image lazy loading works for off-screen slides, text is readable (sufficient contrast, appropriate size), content fits within carousel items (no cutoff), content is accessible (keyboard, screen reader), alt text is provided for images, links within carousel items work correctly, and items are keyboard focusable if interactive.

**Autoplay and Control**: Auto-advancing carousels must be controllable. Test that autoplay has pause/play control, autoplay pauses on hover, autoplay pauses on focus, autoplay stops on manual navigation, autoplay timing is appropriate (5-7 seconds per slide typical), autoplay resumes appropriately (or stays paused after user interaction), autoplay respects prefers-reduced-motion, and autoplay is announced to screen readers.

**Accessibility**: Carousels are often inaccessible and must be carefully implemented. Verify that carousel has appropriate ARIA roles (region, carousel, etc.), carousel is labeled (aria-label describing carousel), live region announces slide changes (aria-live), current slide is indicated (aria-current), keyboard navigation works (Tab through controls, arrows through slides if appropriate), carousel doesn't trap focus, carousel content is accessible, and alternatives are provided if carousel is complex (list of links below).

### 33.4 Audio Player Testing

Audio players share some video player concerns but have unique requirements.

**Audio Controls**: Audio controls must be clear and functional. Test that play/pause button works correctly, play button shows appropriate state (play vs pause icon), volume control works, mute button works, progress bar shows current position and duration, progress bar is scrubbable, playback speed control works if provided (podcasts often provide speed control), skip forward/backward buttons work (10-30 seconds typical for podcasts), and playlist navigation works if applicable.

**Audio Player Visuals**: Audio players need attractive UI without video. Verify that album art or podcast artwork displays, artwork is high-quality and sized correctly, audio waveform visualization works if provided, progress visualization is clear, player design is attractive and on-brand, player adapts to context (embedded, full-screen, mini-player), and player works in light and dark themes.

**Background Playback**: Audio often plays while user does other things. Test that audio continues when switching tabs, audio continues when minimizing browser, audio controls appear in OS media controls (Windows media overlay, macOS Touch Bar, etc.), browser media session API works (showing title, artist, artwork in OS), media notifications show correctly, media controls in notifications work (play/pause, skip), and audio stops appropriately when needed (navigating away, closing tab).

**Audio Accessibility**: Audio content must be accessible. Verify that transcripts are provided, speaker identification is clear in transcripts, important sound effects are noted in transcripts, player controls are keyboard accessible, player state is announced to screen readers, controls have proper ARIA labels, and audio doesn't autoplay without user consent (especially for users with hearing impairments who may find unexpected audio disorienting).

### 33.5 Animated GIF and Video Performance

Animated content can impact performance and must be optimized.

**GIF Optimization**: Animated GIFs are often large and inefficient. Test that GIFs are optimized (compressed, reduced colors if possible), GIFs are replaced with video where appropriate (MP4 is often much smaller for same visual quality), GIF loading is lazy (don't load off-screen GIFs immediately), GIF animation respects prefers-reduced-motion (show first frame only or smaller animation), and GIF performance is acceptable (doesn't cause jank or excessive CPU).

**Background Video**: Background videos can be attractive but are resource-intensive. Verify that background videos are optimized (compressed, appropriate resolution), videos are muted (unmuted background video is poor UX and may violate autoplay policies), videos loop seamlessly, videos don't obscure important content (ensure text contrast), videos have poster images (show immediately before video loads), videos pause or stop on slow connections (respect user's bandwidth), videos respect prefers-reduced-motion (show static image instead), and videos don't dramatically impact performance or battery.

**Lazy Loading**: Media should load only when needed. Test that images lazy load as user scrolls, videos lazy load, lazy loading works across browsers, loading placeholders are shown, lazy loading doesn't break scroll behavior (height reserved for content), and lazy loading improves performance (faster initial load).

### 33.6 Rich Media Accessibility

Rich media presents accessibility challenges requiring thoughtful solutions.

**Alternative Content**: Not all users can perceive rich media. Verify that images have meaningful alt text, decorative images have empty alt attributes, complex images have long descriptions, videos have captions and transcripts, audio has transcripts, charts and graphs have text descriptions or data tables, and animations have text alternatives describing their content.

**Media Controls**: All media controls must be accessible. Test that all controls are keyboard accessible, controls have visible focus indicators, controls have proper ARIA labels, controls work with assistive technologies, media state is announced to screen readers, and controls are touch-friendly on mobile.

**Motion and Animation**: Animations must respect user preferences. Verify that prefers-reduced-motion is respected, animations can be paused, auto-playing animations have controls, animations don't flash excessively (seizure risk), and animations don't convey critical information exclusively (provide alternatives).

### 33.7 Rich Media Testing Checklist

Comprehensive rich media testing checklist:

**Video Players**:
☐ Controls are visible, accessible, and functional
☐ Player states are clear (loading, playing, paused, ended, error)
☐ Player maintains aspect ratio correctly
☐ Video quality is good and adaptive
☐ Captions/subtitles are available and work correctly
☐ Keyboard controls work throughout
☐ Mobile/touch interactions work correctly
☐ Fullscreen works across browsers and devices
☐ Performance is good (smooth playback, no excessive CPU/battery drain)

**Image Galleries/Lightbox**:
☐ Gallery layout is attractive and functional
☐ Thumbnails are high-quality
☐ Lightbox opens and closes smoothly
☐ Image navigation works (prev/next, keyboard, swipe)
☐ Zoom and pan work correctly
☐ Images load quickly and are high-quality
☐ Captions are readable and accessible
☐ Lightbox is fully accessible (keyboard, screen reader)

**Carousels/Sliders**:
☐ Navigation works (buttons, dots, swipe, keyboard)
☐ Transitions are smooth and appropriate
☐ Carousel is responsive
☐ Content is accessible and high-quality
☐ Autoplay is controllable (pause, stops on interaction)
☐ Carousel is fully accessible (ARIA, keyboard, screen reader)

**Audio Players**:
☐ Controls are functional and accessible
☐ Visuals are attractive
☐ Background playback works
☐ OS media controls integration works
☐ Transcripts are provided

**General Rich Media**:
☐ GIFs are optimized or replaced with video
☐ Background video is optimized and doesn't harm UX
☐ Lazy loading works correctly
☐ Alternative content is provided (alt text, captions, transcripts)
☐ prefers-reduced-motion is respected
☐ Performance is acceptable

---
