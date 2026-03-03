# Quality Assurance SOP

## Purpose

This SOP defines the quality assurance process for verifying link placements and maintaining link building standards.

## Scope

Applies to: QA specialists and anyone verifying link placements.

## QA Process Overview

```
1. Receive Notification → 2. Verify Placement → 3. Check Quality → 4. Document → 5. Address Issues
```

## Step 1: Receive Placement Notification

### Trigger Points

QA process begins when:
- Outreach reports placement complete
- Site owner confirms link is live
- Scheduled verification date arrives
- Client requests verification

### Required Information

Before starting QA, have:
- Target URL (your page that should receive link)
- Linking page URL (where link should appear)
- Agreed anchor text
- Agreed link attributes (dofollow, etc.)
- Placement type (contextual, bio, resource)

## Step 2: Verify Placement

### Link Existence Check

1. Open linking page URL
2. Search page for your URL (Ctrl/Cmd+F)
3. Verify link is present
4. Click link to confirm it works
5. Check destination URL is correct

### Link Attribute Check

1. Right-click the link
2. Select "Inspect" or "Inspect Element"
3. Examine the `<a>` tag
4. Verify attributes:

**Expected for dofollow:**
```html
<a href="https://yoursite.com/page">anchor text</a>
```
OR
```html
<a href="https://yoursite.com/page" target="_blank">anchor text</a>
```

**Red flags (not dofollow):**
```html
<a href="..." rel="nofollow">
<a href="..." rel="sponsored">
<a href="..." rel="ugc">
<a href="..." rel="nofollow sponsored">
```

### Anchor Text Verification

1. Check visible anchor text
2. Compare to agreed anchor
3. Document any variations
4. Flag significant deviations

### Placement Quality Check

Verify placement location:
- [ ] Contextual (within content) - Best
- [ ] Resource section - Acceptable
- [ ] Author bio - Acceptable for guest posts
- [ ] Footer/sidebar - Flag for review
- [ ] Hidden/obscured - Reject

## Step 3: Check Quality

### Page Quality Check

Verify the linking page:
- [ ] Page is indexed (site:url returns result)
- [ ] Page has content around link
- [ ] No new spam/low-quality content added
- [ ] Page still meets original quality standards

### Site Quality Check

Verify the site hasn't degraded:
- [ ] Site is still active
- [ ] No obvious quality decline
- [ ] No spam signals
- [ ] DR hasn't dropped significantly

## Step 4: Document Results

### QA Record Template

```
QA VERIFICATION RECORD

Date: [Date]
Campaign/Client: [Name]
Verifier: [Your name]

PLACEMENT DETAILS
Target URL: [URL receiving the link]
Linking Page: [URL of page with link]
Expected Anchor: [What was agreed]
Actual Anchor: [What appears on page]

VERIFICATION RESULTS
Link Present: [Yes/No]
Link Works: [Yes/No]
Correct URL: [Yes/No]
Anchor Correct: [Yes/No/Variation - details]
Dofollow: [Yes/No/Partial]
Placement Type: [Contextual/Bio/Resource/Other]

QUALITY CHECKS
Page Indexed: [Yes/No]
Page Quality: [Good/Acceptable/Concerning]
Site Quality: [Good/Acceptable/Concerning]

OVERALL STATUS: [Approved/Issues/Rejected]

NOTES:
[Any relevant observations]
```

### Database Updates

Update tracking systems with:
- Verification date
- QA status
- Any issues found
- Screenshots (if required)

## Step 5: Address Issues

### Issue Categories and Actions

**Link Missing:**
1. Double-check URL
2. Contact site owner immediately
3. Document outreach
4. Escalate if no response in 48 hours

**Wrong Anchor Text:**
1. Document deviation
2. Assess impact on anchor distribution
3. Request correction if significant
4. Accept if minor variation

**Nofollow Added:**
1. Document the issue
2. Contact site owner
3. Request correction per agreement
4. Negotiate price reduction if uncorrectable

**Wrong URL:**
1. Contact site owner immediately
2. Request correction
3. Provide correct URL

**Poor Placement:**
1. Document placement type
2. Request improvement if below standard
3. Negotiate if they refuse

**Quality Decline:**
1. Document concerns
2. Escalate to manager
3. Consider requesting link removal
4. Blacklist site for future

### Escalation Path

**Level 1 (QA Specialist handles):**
- Minor anchor variations
- Simple corrections needed
- Routine follow-ups

**Level 2 (Manager review):**
- Significant quality issues
- Site owner disputes
- Pricing/refund discussions

**Level 3 (Director/Client involvement):**
- Major disputes
- Potential penalties
- Client-facing issues

## Ongoing Monitoring

### Monthly Link Check

For all live links:
1. Verify still present
2. Check attributes unchanged
3. Note any page changes
4. Flag any issues

### Monitoring Schedule

| Link Type | Check Frequency |
|-----------|-----------------|
| Paid placements | Monthly for 3 months, then quarterly |
| Guest posts | Quarterly |
| Earned links | Semi-annually |

### Lost Link Process

If link is found missing:
1. Verify (tool error vs. actually gone)
2. Check if page still exists
3. Attempt recovery outreach
4. Document outcome
5. Report in metrics

## Quality Standards

### Acceptance Criteria

Link is approved when:
- Link exists and works
- Pointing to correct URL
- Dofollow (unless otherwise agreed)
- Acceptable anchor text
- Appropriate placement
- Page/site quality maintained

### Rejection Criteria

Link is rejected when:
- Link missing
- Wrong URL
- Nofollow when dofollow agreed
- Hidden or manipulative placement
- Significant quality degradation

### Quality Metrics

Track:
- First-pass acceptance rate
- Issue types and frequency
- Resolution success rate
- Average time to resolve issues

## Tools

**Required:**
- Browser developer tools
- Ahrefs (site metrics)
- Screaming Frog (bulk checks)
- Screenshot tool
- Spreadsheet/CRM

**Optional:**
- Automated monitoring tools
- Link checking extensions

## Reporting

### Weekly QA Report

- Links verified this week
- Pass/fail breakdown
- Issues found and status
- Trends and concerns

### Monthly QA Summary

- Total verifications
- Acceptance rate
- Common issues
- Recommendations

## Process Updates

Review this SOP:
- Monthly (during high volume)
- When issues arise
- When tools change
- Quarterly (routine)

Last updated: [Date]
Version: [X.X]
