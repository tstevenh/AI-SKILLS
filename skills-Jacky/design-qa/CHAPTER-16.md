# 16. Error States


Error states occur when operations fail, input is invalid, or systems malfunction. Effective error state design helps users understand problems, provides clear guidance for resolution, maintains system trust, and enables recovery. This comprehensive section covers all aspects of error state testing in design QA.

### 16.1 Error State Fundamentals

Understanding error state principles enables effective testing.

**Purpose of Error States**: Error states serve critical functions. They communicate that something went wrong (user must be aware), explain what failed and why (understanding the problem), provide guidance on resolution (actionable next steps), maintain user trust (transparent, helpful, apologetic tone), prevent data loss (preserve user input), and enable recovery (clear path forward). Testing validates error states fulfill these purposes, are helpful not frustrating, and enable users to successfully complete tasks despite errors.

**Error Types**: Different errors require different approaches. Validation errors result from invalid user input (empty required field, incorrect format), system errors occur due to server or application issues (500 error, database unavailable), network errors stem from connectivity problems (timeout, no connection), authorization errors indicate insufficient permissions (401, 403), not found errors occur when resources don't exist (404), conflict errors happen when operations conflict (409, duplicate record), and business logic errors enforce rules (insufficient funds, invalid operation). Testing validates appropriate error type is identified, error messaging matches error type, and handling is appropriate for each type.

**Error State Components**: Complete error states include multiple elements. Error indication shows something is wrong (icon, color, styling), error message explains what happened, guidance provides resolution steps, retry mechanism enables another attempt, fallback offers alternative path, contact support link for help when stuck, error code or reference for support inquiries, and error logging for debugging and monitoring. Testing validates all appropriate components are present, components work together cohesively, and user experience is comprehensive.

**Error Severity**: Errors have different severity levels. Critical errors completely block user progress (payment failure, authentication loss), high-severity errors significantly impair functionality (feature unavailable, data save failure), medium-severity errors cause inconvenience (failed preference save, non-critical feature broken), low-severity errors are minor issues (analytics not loaded, non-essential asset missing), and warnings indicate potential problems (unsaved changes, weak password). Testing validates severity is appropriately communicated, critical errors demand immediate attention, and lower-severity issues don't inappropriately alarm users.

**Error Placement**: Location affects noticeability and context. Inline errors appear next to relevant field or component (form validation), toast/snackbar errors show brief notification (non-critical, transient errors), modal errors demand attention (critical errors blocking progress), banner errors appear at top of page (persistent, page-level errors), and page-level errors replace content entirely (fatal errors like 404, 500). Testing validates error placement is appropriate for severity and context, errors are noticeable, and placement doesn't confuse users.

### 16.2 Error Messages

Clear, helpful error messages are crucial for usability.

**Error Message Principles**: Effective error messages follow key principles. Be clear and specific (explain exactly what's wrong), use plain language (avoid technical jargon unless targeting technical users), be concise but complete (don't be terse at expense of clarity), be respectful and apologetic (errors are frustrating; acknowledge that), provide actionable guidance (tell user what to do next), avoid blame (don't say "You entered an invalid..." say "The email format is invalid..."), and be consistent (similar errors have similar messages). Testing validates messages are clear, helpful, appropriately apologetic, actionable, and consistent across application.

**What to Include**: Complete error messages contain several elements. Explanation of what went wrong ("The payment could not be processed"), reason if known and helpful ("Your card was declined"), guidance on resolution ("Please check your card details and try again"), specific field or data if applicable ("Email address is required"), error code or reference if helpful for support ("Error code: PAY_DECLINED"), and contact information if user needs help ("Contact support if problem persists"). Testing validates messages include appropriate elements, information is helpful not overwhelming, and technical details are appropriate for audience.

**What to Avoid**: Certain error message anti-patterns should be eliminated. Don't use overly technical language ("SQLException: Connection refused"), don't blame the user ("You failed to..."), don't be vague ("An error occurred"), don't be humorous about serious problems (payment failures aren't funny), don't expose sensitive information (stack traces in production, internal paths), don't overwhelm with information (keep it concise), and don't dead-end users (always provide next steps). Testing validates these anti-patterns are absent, messages are appropriate, and user experience is respectful.

**Error Message Tone**: Tone affects user emotional response. Use apologetic tone for system errors ("We're sorry, something went wrong"), use neutral, instructive tone for validation errors ("Email address is required"), use urgent tone for critical errors ("Your session has expired. Please log in again"), use reassuring tone when data is safe ("Your progress was saved"), and maintain brand voice while being appropriate to situation. Testing validates tone matches error severity, brand voice is maintained appropriately, and tone doesn't worsen user frustration.

**Internationalization**: Error messages must work across languages. Design message system for localization (externalize all strings, avoid hardcoded text), provide context to translators (explain error scenario), test with much longer text (German, Finnish can be 30-40% longer), validate right-to-left languages (Arabic, Hebrew), ensure error codes or references are locale-independent, and test cultural appropriateness (humor, directness varies by culture). Testing validates all error messages are localized, translations are accurate and helpful, UI handles text length variations, and RTL works correctly.

### 16.3 Inline Validation Errors

Form field errors require special attention.

**Field-Level Error Display**: Individual field errors need clear presentation. Display error message below field (most common, follows visual flow), use error color (typically red), show error icon next to field, add error border or background to field, associate message with field (aria-describedby), mark field as invalid (aria-invalid="true"), and maintain adequate contrast (WCAG compliance). Testing validates field errors are obvious, association is clear, accessibility attributes are correct, contrast is sufficient, and styling is consistent.

**Validation Timing**: When errors show affects UX. Show required field errors on blur (after user leaves field) or form submit, show format errors after user finishes typing (brief delay to avoid annoying mid-typing errors), show real-time validation for complex requirements (password strength, username availability), clear errors as soon as field becomes valid, and avoid showing errors before user has chance to enter valid data. Testing validates timing feels helpful not intrusive, errors appear at appropriate moments, errors clear when fixed, and timing is consistent.

**Multiple Field Errors**: When multiple fields have errors. Show all errors simultaneously (don't make user fix one to see next), prioritize visibility (scroll to first error on submit, focus first error field), show error count if many errors ("3 errors prevent submission"), highlight all error fields, and provide error summary at top if errors aren't all visible. Testing validates all errors are shown, navigation to errors is easy, error count is accurate, and summary is helpful.

**Error Recovery**: Help users fix errors easily. Keep form data when validation fails (don't clear fields), focus first error field on submit, clear error as soon as field becomes valid, provide positive feedback when fixed (optional: green checkmark), allow resubmission easily, and maintain error history (don't hide errors user hasn't seen). Testing validates data is preserved, focus management works, errors clear appropriately, resubmission works, and UX facilitates correction.

**Field-Specific Error Types**: Different fields have specific error patterns. Email field: "Email address is required", "Email format is invalid", "This email is already registered". Password field: "Password is required", "Password must be at least 8 characters", "Password is too common". Phone field: "Phone number is required", "Phone format is invalid", "Phone number must be 10 digits". URL field: "URL is required", "URL must start with http:// or https://". Testing validates messages are specific and helpful, format requirements are clear, and guidance enables correction.

### 16.4 System and Network Errors

Errors beyond user control require different handling.

**500 Internal Server Errors**: Server-side errors need graceful handling. Show apologetic, reassuring message ("We're sorry, something went wrong on our end"), avoid exposing technical details (no stack traces), provide error reference ("Error ID: ABC123" for support), offer retry mechanism, suggest when to retry ("Please try again in a few moments"), provide alternative contact method if critical, and log error thoroughly server-side. Testing validates message is helpful, technical details aren't exposed, retry works, error reference is provided, and logging captures details.

**Network Errors**: Connectivity issues require special handling. Detect network availability (navigator.onLine), show clear network error message ("No internet connection"), distinguish between timeout vs no connection, provide retry mechanism, queue operations for when connection restored if appropriate, show offline indicator persistently, and provide guidance on troubleshooting. Testing validates network errors are detected, messages are clear, retry works, offline experience is graceful, and reconnection transitions smoothly.

**Timeout Errors**: Operations that take too long must timeout gracefully. Set reasonable timeout thresholds (typically 30-60s), show timeout-specific message ("Request timed out"), explain what happened and why, provide retry option, consider allowing longer wait ("Keep waiting" button), preserve user data, and log timeout for monitoring. Testing validates timeouts occur at appropriate thresholds, messages are clear, retry works, data is preserved, and logging captures details.

**Authorization Errors**: Permission issues need clear communication. Distinguish 401 (unauthenticated) from 403 (unauthorized), for 401 show login prompt (preserve intended action for after login), for 403 explain what permission is needed, provide path to gain permission if possible (contact admin, upgrade plan), be respectful (don't say "You are not allowed"), and log authorization failures (security monitoring). Testing validates authorization errors are handled distinctly, messages are clear and respectful, login flow works, and security is maintained.

**Rate Limiting Errors**: Throttling requires specific messaging. Explain rate limiting clearly ("Too many requests"), indicate when user can try again ("Please wait 1 minute"), show countdown timer if appropriate, don't penalize user unfairly (reasonable limits), provide alternative if available (contact support), and log rate limit hits (might indicate abuse or UX issue). Testing validates rate limiting is explained clearly, retry timing is accurate, countdown updates correctly, and logging captures details.

### 16.5 Page-Level Errors

Certain errors affect entire pages.

**404 Not Found**: Missing resources need helpful error pages. Clearly state page wasn't found ("Page not found"), avoid generic "404" alone (explain what that means), acknowledge user's frustration, provide search functionality, suggest related or popular pages, maintain site navigation (header, footer), use consistent branding and styling, avoid humor unless brand-appropriate (lost users aren't amused), and log 404s (might indicate broken links). Testing validates 404 page is helpful, navigation is maintained, suggested alternatives are relevant, and user can recover.

**500 Server Error**: Server failures need apologetic, helpful pages. Clearly state server error occurred ("Something went wrong"), apologize sincerely ("We're sorry"), avoid technical jargon (no stack traces), provide error reference for support, estimate when service might be restored if known, maintain site navigation, use consistent branding, and log errors thoroughly. Testing validates 500 page is helpful and apologetic, technical details aren't exposed, navigation works, and errors are logged.

**Maintenance Pages**: Planned downtime needs proactive communication. Clearly state maintenance is in progress, indicate expected duration ("Back in approximately 30 minutes" or "Back on January 15 at 2:00 PM PST"), explain why maintenance is happening ("Upgrading servers"), provide status page link if available, show progress if possible, use consistent branding, and update estimate if duration changes. Testing validates maintenance page is clear, timing is communicated well, updates work, and branding is maintained.

**Access Denied Pages**: Permission errors need clear explanation. State clearly that access is denied ("Access Denied"), explain why ("This content requires a premium subscription"), provide path to gain access (upgrade link, contact admin), be respectful (not punitive), maintain navigation, allow return to accessible content, and log access denials (security and product analytics). Testing validates denied access is explained clearly, path to access is provided, tone is respectful, and logging captures details.

**Error Page SEO**: Error pages need appropriate SEO treatment. Return correct HTTP status code (404, 500, etc. - not 200), set appropriate meta tags (noindex for error pages), maintain site structure (header, footer, navigation), provide search functionality or sitemap, link to home page and key pages, avoid redirect loops (404 page returning 302 redirect), and test that search engines don't index error pages. Testing validates status codes are correct, SEO tags are appropriate, search engines handle correctly, and error pages don't appear in search results.

### 16.6 Error State Accessibility

Error states must be perceivable and understandable by all users.

**Screen Reader Announcements**: Errors must be announced. Use aria-live="polite" for non-critical errors (form validation), use aria-live="assertive" for critical errors (session expiration, payment failure), use role="alert" for important messages, associate error messages with fields (aria-describedby), mark fields as invalid (aria-invalid="true"), announce error count if multiple errors, and test with screen readers (NVDA, JAWS, VoiceOver, TalkBack). Testing validates screen readers announce errors appropriately, associations are correct, critical errors demand attention, and announcements are helpful not overwhelming.

**Error Identification**: Errors must be perceivable. Don't rely on color alone (use icon, text, and position), ensure sufficient contrast (4.5:1 for error text), make error icons understandable (internationally recognized symbols), associate errors with fields clearly (visual proximity, aria-describedby), use consistent error styling across application, and work in high contrast mode. Testing validates errors are perceivable without color, contrast is sufficient, identification works across modes, and consistency is maintained.

**Focus Management**: Error states should guide keyboard users. Focus first error field on form submission error, maintain logical tab order, don't lose focus when errors appear, provide skip link to error summary if many errors, allow easy navigation between errors, and ensure focus indicators remain visible. Testing validates focus moves appropriately, tab order is logical, focus isn't lost, navigation is efficient, and focus indicators are visible.

**Error Text**: Message text must be accessible. Write in plain language (reading level appropriate), avoid relying only on icons (provide text), keep messages concise but complete, use proper semantic HTML (paragraphs, lists), associate with appropriate elements (aria-describedby), and provide adequate information for comprehension. Testing validates error text is clear, works without visual elements, length is appropriate, HTML semantics are correct, and associations are proper.

**Keyboard Interaction**: Error recovery must work without mouse. Allow dismissing errors with keyboard (Escape, focus and Enter), enable retry with keyboard, allow navigation to help/support links, ensure error modals trap focus appropriately, and provide keyboard shortcuts if beneficial. Testing validates all error interactions work with keyboard, dismissal works, retry works, navigation works, and focus trapping is appropriate.

### 16.7 Error State Testing

Comprehensive testing ensures effective error handling.

**Test All Error Scenarios**: Cover complete error space. Test validation errors (required fields, format errors, business logic), system errors (500, database errors, service unavailable), network errors (timeout, no connection, DNS failure), authorization errors (401, 403), not found errors (404), conflict errors (409, duplicate), rate limiting, payment failures, file upload errors, and any domain-specific errors. Testing validates all error types are handled, messages are appropriate, and recovery mechanisms work.

**Test Error Timing**: When errors appear affects UX. Validate errors appear at appropriate times (form submit, field blur, real-time), errors don't appear prematurely (before user has chance to enter valid data), errors clear when fixed, error persistence is appropriate (don't disappear too quickly), and timing is consistent across similar errors.

**Test Error Recovery**: Users must be able to recover from errors. Validate retry mechanisms work, form data is preserved on validation errors, users can correct errors easily, alternative paths are available when appropriate, and contact/support options function correctly.

**Test with Screen Readers**: Accessibility is critical. Test with NVDA (Windows), JAWS (Windows), VoiceOver (macOS/iOS), and TalkBack (Android). Validate errors are announced, associations are correct, recovery is possible with audio only, and navigation is efficient.

**Test Error Messages**: Message quality affects recovery success. Validate messages are clear and helpful, technical jargon is absent or explained, guidance is actionable, tone is appropriate, translations are accurate, and messages work in all contexts.

**Test Edge Cases**: Unusual error scenarios need handling. Test multiple simultaneous errors, rapid error-retry cycles, errors during error handling (meta-errors), network failure during error display, and any domain-specific edge cases. Validate graceful handling throughout.

**Visual Regression Testing**: Automated testing catches error state regressions. Capture baselines of all error states, compare implementations against baselines, test error states in all themes, validate error styling consistency, and integrate error state testing in CI/CD.

**Monitor Error Rates**: Production error monitoring informs improvements. Track error frequency, identify common errors, monitor recovery success rates, analyze error journeys (where users go after errors), and use data to prioritize improvements. Testing validates monitoring captures errors correctly.

---

*Continuing with additional comprehensive sections to reach the target word count...*

