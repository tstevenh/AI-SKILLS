# Niche Edit Quality Control

## Why QC Matters for Niche Edits

Quality control is even more important for niche edits than guest posts because:

1. **You don't control the content** - The site owner makes the changes
2. **Variations are common** - Anchor text, placement, and context can differ from what you requested
3. **Links can disappear** - Easier to remove a link than an entire article
4. **Page changes happen** - The page may change in ways that affect your link

A robust QC process protects your investment and ensures deliverables match expectations.

## Verifying Placements

### Verification Checklist

When a placement is reported as live, verify:

**Link exists:**
✓ Link is actually on the page
✓ Link points to correct URL
✓ Link is not redirected

**Link attributes:**
✓ Dofollow (unless agreed otherwise)
✓ No rel="sponsored" or "ugc" (unless agreed)
✓ Opens in appropriate way

**Anchor text:**
✓ Matches agreed anchor
✓ Natural in context
✓ Not over-optimized

**Placement quality:**
✓ Contextual (within paragraph)
✓ Not hidden or footer
✓ Relevant surrounding content
✓ Reasonable position on page

**Page status:**
✓ Page is indexed
✓ Page has traffic (verify hasn't tanked)
✓ No new spam on page
✓ No noindex added to page

### Using Browser Tools for Verification

**Check link attributes:**
1. Right-click the link
2. Inspect element
3. Look at the `<a>` tag
4. Check for rel attributes

**What to look for:**
```html
<!-- Good - clean dofollow link -->
<a href="https://yoursite.com">anchor text</a>

<!-- Acceptable - standard link -->
<a href="https://yoursite.com" target="_blank">anchor text</a>

<!-- Problem - nofollow added -->
<a href="https://yoursite.com" rel="nofollow">anchor text</a>

<!-- Problem - sponsored tag -->
<a href="https://yoursite.com" rel="sponsored">anchor text</a>
```

### Automated Verification Tools

**For single link checks:**
- Browser inspector (manual but thorough)
- Link analysis extensions

**For bulk verification:**
- Screaming Frog (crawl pages, export link data)
- Ahrefs (check if link is detected)
- Custom scripts (for large-scale operations)

### What to Do If Verification Fails

**Link missing:**
Contact immediately: "Hi [Name], I'm not seeing the link live on [URL]. Could you confirm it was added?"

**Wrong anchor text:**
Request correction: "The link is live but shows [actual anchor] instead of [agreed anchor]. Could this be updated?"

**Nofollow added:**
Address per agreement: "I noticed the link has a nofollow attribute. Our agreement was for a dofollow link—can this be corrected?"

**Wrong URL:**
Request fix: "The link points to [wrong URL] instead of [correct URL]. Could you update this?"

## Anchor Text Optimization

### Balancing What You Request vs. What They Allow

Many site owners have opinions about anchor text. Navigate this by:

**Before agreement:**
"We'd like the anchor text to be [preferred]. Is that okay, or do you have preferences?"

**If they want changes:**
Evaluate if their suggestion is acceptable for your anchor profile. Often it is.

**Non-negotiables:**
- Don't accept random anchors that hurt your profile
- Don't push for exact match if they resist
- Do maintain natural language

### Anchor Text for Niche Edits

Since you're inserting into existing content, anchors must:

1. **Fit the context** - Make sense in the paragraph
2. **Sound natural** - Like original author wrote it
3. **Support your strategy** - Align with anchor distribution

**Good anchor text approaches:**

**Blend with existing style:**
If article says "tools like Trello and Asana," your addition might be "tools like Trello, Asana, and [Your Product Name]"

**Descriptive without keyword stuffing:**
"You can also check out [Brand Name]'s guide to email automation" vs. "best email automation software platform"

**Author voice:**
Match how the author naturally writes. Formal author = formal anchor language.

### Tracking Anchor Distribution

Maintain an anchor text tracker:

| Link # | Domain | Anchor Used | Category | Date |
|--------|--------|-------------|----------|------|
| 1 | site1.com | Your Brand | Branded | 2026-01-15 |
| 2 | site2.com | yoursite.com | Naked URL | 2026-01-18 |
| 3 | site3.com | this helpful guide | Generic | 2026-01-22 |
| 4 | site4.com | project management tips | Partial | 2026-02-01 |

**Monitor distribution:**
- Branded: 40-50%
- Naked URL: 20-25%
- Generic: 15-20%
- Partial match: 10-15%
- Exact match: 5-10%

## Link Monitoring

### Why Monitor After Placement

Links can disappear because:
- Site owner removes them
- Page gets deleted
- Content gets overhauled
- Technical issues
- Site changes ownership

### Monitoring Approach

**Monthly checks:**
- Visit each placement URL
- Verify link still exists
- Check link attributes haven't changed
- Note any page changes

**Automated monitoring:**
- Ahrefs backlink alerts
- Semrush monitoring
- Linkody or similar tools
- Custom scripts for bulk checking

### Setting Up Ahrefs Alerts

1. Go to Alerts → Backlinks
2. Enter your domain
3. Set to alert on "Lost" backlinks
4. Review lost links monthly

### What to Do When Links Disappear

**Step 1: Verify**
Confirm the link is actually gone (not just a tool error).

**Step 2: Contact**
Reach out to the site owner:

"Hi [Name], I noticed the link we placed in [article title] is no longer showing. Was this intentional? If there was an issue, I'd love to understand so we can resolve it."

**Step 3: Negotiate**
Depending on response:
- If accidental: Request restoration
- If intentional: Understand why, negotiate if possible
- If unreasonable: Request refund if paid

**Step 4: Document**
Track lost links, reasons, and recovery rates. This informs future site selection.

### Lost Link Recovery Rates

**Industry benchmarks:**
- Recovery rate from outreach: 30-50%
- Links lost within 90 days: 5-10%
- Links lost within 1 year: 10-20%

**Factors affecting retention:**
- Site owner relationship
- Quality of link placement
- Site stability
- Whether link truly adds value

## Building a QC System

### QC Workflow

**Stage 1: Pre-placement verification**
- Confirm page metrics (DR, UR, traffic)
- Verify page is indexed
- Check page content quality
- Document baseline state

**Stage 2: Placement confirmation**
- Request screenshot from site owner
- Verify link is live
- Check all attributes
- Document placement

**Stage 3: Post-placement monitoring**
- Add to monitoring list
- Set calendar for monthly check
- Watch for alerts
- Track in spreadsheet

### QC Documentation Template

For each niche edit, record:

```
NICHE EDIT QC RECORD

Domain: _______________
Page URL: _______________
Date Placed: _______________
Cost: $_______________ 

PLACEMENT DETAILS
Target URL: _______________
Agreed Anchor: _______________
Actual Anchor: _______________
Placement Type: [ ] Contextual [ ] Resource section [ ] Other

VERIFICATION
Link Present: [ ] Yes [ ] No
Dofollow: [ ] Yes [ ] No
Anchor Correct: [ ] Yes [ ] No
Placement Acceptable: [ ] Yes [ ] No
Page Indexed: [ ] Yes [ ] No

QC Notes:
_________________________________

MONITORING LOG
Check 1 (30 days): [ ] Present [ ] Missing - Date: ______
Check 2 (60 days): [ ] Present [ ] Missing - Date: ______
Check 3 (90 days): [ ] Present [ ] Missing - Date: ______
Check 4 (6 months): [ ] Present [ ] Missing - Date: ______
Check 5 (1 year): [ ] Present [ ] Missing - Date: ______

Issues & Resolutions:
_________________________________
```

### Team QC Standards

If running a team, document:

**Verification SOP:**
1. Check within 24 hours of reported placement
2. Document with screenshots
3. Report issues immediately
4. Track in central spreadsheet

**Escalation path:**
- Minor issues (anchor variation): Note and proceed
- Moderate issues (nofollow added): Contact site, escalate if unresolved
- Major issues (link missing): Immediate escalation, contact site urgently

**Quality thresholds:**
- Acceptable variation: Slight anchor text changes
- Unacceptable: Missing link, wrong URL, nofollow when agreed dofollow

## Common QC Issues and Solutions

### Issue: Anchor Text Changed

**Situation:** Site owner used different anchor than agreed.

**Solution:**
If minor variation: Accept and document
If significantly different: Request correction
If damages your profile: Insist on fix or removal

**Prevention:**
Provide exact suggested text upfront
Confirm anchor in writing before payment
Build relationship to ensure compliance

### Issue: Link Placed in "Resources" Section

**Situation:** Agreed on contextual placement, link ended up in footer resources list.

**Solution:**
Request move to contextual placement
If refused: Negotiate price reduction or accept lower value

**Prevention:**
Specify placement location in agreement
Request to see placement location before finalizing

### Issue: Page Got Noindexed

**Situation:** Page now has noindex tag—link has no value.

**Solution:**
Contact site owner to understand why
Request move to different (indexed) page
If recent and accidental: Request fix

**Prevention:**
Monitor page status monthly
Include page status in monitoring checklist

### Issue: Surrounding Content Changed to Spam

**Situation:** Page now has gambling/pharma content alongside your link.

**Solution:**
Request immediate link removal
Document for future site avoidance

**Prevention:**
Monitor page content, not just link existence
Avoid sites with low editorial standards

## Summary

Niche edit QC protects your investment:

1. **Verify every placement** - Don't trust, verify
2. **Check all attributes** - Dofollow, anchor, placement
3. **Monitor ongoing** - Links disappear
4. **Document everything** - Track for patterns
5. **Act on issues** - Don't let problems slide
6. **Build systems** - Consistent process beats ad hoc checking

With QC processes in place, your niche edit campaigns deliver reliable, lasting value.
