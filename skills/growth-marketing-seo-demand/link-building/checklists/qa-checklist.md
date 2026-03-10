# QA Checklist

## Pre-Verification Setup

### Information Required
- [ ] Target URL (your page receiving link)
- [ ] Linking page URL (where link appears)
- [ ] Agreed anchor text
- [ ] Expected link attributes (dofollow, etc.)
- [ ] Placement type (contextual, bio, etc.)

---

## Link Verification

### Link Existence
- [ ] Opened linking page URL
- [ ] Found link to target URL (Ctrl+F search)
- [ ] Link is clickable
- [ ] Link navigates to correct destination
- [ ] Destination URL is exact (no redirects to wrong page)

### Link Attributes
- [ ] Right-click → Inspect Element
- [ ] Check `<a>` tag attributes

**Expected dofollow:**
```html
<a href="https://yoursite.com/page">anchor text</a>
```

**Red flags:**
- [ ] ~~rel="nofollow"~~ - NOT present (unless agreed)
- [ ] ~~rel="sponsored"~~ - NOT present (unless agreed)
- [ ] ~~rel="ugc"~~ - NOT present (unless agreed)

### Anchor Text
- [ ] Visible anchor text matches agreed
- [ ] Document actual anchor: _____________
- [ ] Variation acceptable? Yes / No

### Placement Quality
- [ ] **Contextual** (within paragraph content) ✓ Best
- [ ] **Resource section** ✓ Acceptable
- [ ] **Author bio** ✓ Acceptable for guest posts
- [ ] **Footer/sidebar** ⚠️ Flag for review
- [ ] **Hidden/obscured** ✗ Reject

---

## Page Quality Check

### Page Status
- [ ] Page loads correctly
- [ ] Page is indexed: `site:[page URL]` returns result
- [ ] Page has substantial content
- [ ] Content around link is relevant

### Page Changes
- [ ] No new spam content added
- [ ] No excessive ads added
- [ ] Link neighborhood remains clean
- [ ] Overall page quality maintained

---

## Site Quality Check

### Site Status
- [ ] Site is active
- [ ] No obvious quality degradation
- [ ] No spam signals
- [ ] DR hasn't dropped significantly

---

## Issue Documentation

### If Issues Found

**Issue type:** _____________________
**Details:** _______________________
**Screenshot taken:** Yes / No
**Escalation needed:** Yes / No

### Issue Resolution

| Issue | Action | Status |
|-------|--------|--------|
| Link missing | Contact site owner | _____ |
| Wrong anchor | Request correction | _____ |
| Nofollow added | Request fix | _____ |
| Wrong URL | Request correction | _____ |
| Poor placement | Request improvement | _____ |

---

## QA Result

### Verification Outcome

- [ ] **APPROVED** - All checks pass
- [ ] **APPROVED WITH NOTES** - Minor variations acceptable
- [ ] **ISSUES** - Action required (see documentation)
- [ ] **REJECTED** - Does not meet standards

### Record

**Verified by:** ________________
**Date:** ________________
**Status:** ________________

---

## Ongoing Monitoring

### Add to Monitoring List
- [ ] Added to link tracking spreadsheet
- [ ] Monitoring alert set (if applicable)
- [ ] Next check date scheduled

### Monitoring Schedule

| Check | Date | Status |
|-------|------|--------|
| 30 days | _____ | _____ |
| 60 days | _____ | _____ |
| 90 days | _____ | _____ |
| 6 months | _____ | _____ |
| 1 year | _____ | _____ |

---

## Lost Link Response

### If Link Disappears

1. [ ] Verified link is actually gone (not tool error)
2. [ ] Checked if page still exists
3. [ ] Investigated cause if possible
4. [ ] Sent recovery outreach
5. [ ] Documented outcome
6. [ ] Reported in metrics

### Recovery Outreach Template

```
Hi [Name],

I noticed the link we placed in [article title] is no longer showing.

Was this intentional? If there was an issue, I'd love to understand so we can resolve it.

If it can be restored, we'd greatly appreciate it.

Thanks,
[Your Name]
```

---

## QA Summary Report

### Weekly QA Summary

| Metric | Count |
|--------|-------|
| Links verified | ___ |
| Passed | ___ |
| Issues found | ___ |
| Resolved | ___ |
| Pending | ___ |

### Issue Types This Week

| Issue | Count |
|-------|-------|
| Link missing | ___ |
| Wrong anchor | ___ |
| Nofollow added | ___ |
| Wrong URL | ___ |
| Poor placement | ___ |
| Page quality | ___ |

### Action Items
1. _______________________
2. _______________________
3. _______________________

---

## Quick Reference: HTML Attributes

**Dofollow (good):**
```html
<a href="...">text</a>
<a href="..." target="_blank">text</a>
```

**Nofollow (bad unless agreed):**
```html
<a href="..." rel="nofollow">text</a>
```

**Sponsored (bad unless agreed):**
```html
<a href="..." rel="sponsored">text</a>
```

**UGC (bad unless agreed):**
```html
<a href="..." rel="ugc">text</a>
```

**Combined (bad):**
```html
<a href="..." rel="nofollow sponsored">text</a>
```
