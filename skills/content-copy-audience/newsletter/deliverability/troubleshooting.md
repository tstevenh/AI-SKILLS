# Deliverability Troubleshooting: Diagnosis and Recovery Guide

When deliverability problems hit, you need to act fast. This guide helps you diagnose issues and execute recovery.

---

## Recognizing Deliverability Problems

### Warning Signs

**Immediate Red Flags:**
- Open rates drop suddenly (20%+ decline)
- Spam complaints spike (>0.1%)
- Bounce rate jumps (>5%)
- Subscribers report not receiving
- Gmail Postmaster shows "Low" or "Bad"

**Gradual Decline Signals:**
- Open rates trending down over weeks
- Engagement slowly decreasing
- Unsubscribe rate climbing
- Click rates declining

### Is It Really Deliverability?

**Before assuming deliverability, check:**

| Symptom | Could Also Be |
|---------|---------------|
| Low opens | Bad subject lines, send time |
| Low clicks | Poor content, irrelevant |
| Rising unsubs | Content quality, frequency |
| Complaints | Unexpected content, forgot subscribing |

**True Deliverability Indicators:**
- Opens drop but engagement among openers is normal
- Subscribers actively report not receiving
- Postmaster/SNDS shows reputation decline
- Authentication failures in headers

---

## Diagnostic Process

### Step 1: Check Authentication

**Tools:**
- MXToolbox.com
- Mail-tester.com (send test email)
- Google Admin Toolbox

**What to Check:**
```
SPF: PASS/FAIL
DKIM: PASS/FAIL
DMARC: PASS/FAIL
```

**If Any Fail:**
- Fix immediately
- Contact ESP support
- Update DNS records
- Re-verify setup

### Step 2: Check Reputation

**Google Postmaster Tools:**
- Domain reputation: High/Medium/Low/Bad
- IP reputation
- Spam rate
- Feedback loop data

**Microsoft SNDS:**
- IP status
- Complaint rate
- Trap hits

**Sender Score (Validity):**
- Score out of 100
- Below 80 = investigate

### Step 3: Analyze Recent Changes

**Ask yourself:**
- Changed email service provider?
- Changed sending domain?
- Significant list growth recently?
- Changed content type?
- Imported new subscribers?
- Changed frequency?

### Step 4: Examine List Health

**Check:**
- Bounce rate by recent sends
- Spam trap indicators
- List hygiene status
- Subscriber quality by source

### Step 5: Review Content

**Scan for:**
- Spam trigger words
- Excessive links
- Spammy formatting
- Broken HTML
- Image-heavy emails

---

## Common Problems and Fixes

### Problem 1: Authentication Failure

**Symptoms:**
- Sudden delivery drop
- "No authentication" in headers
- ESP warning

**Causes:**
- DNS changes
- Domain verification lost
- ESP configuration issue

**Fix:**
1. Check DNS records immediately
2. Re-verify SPF, DKIM, DMARC
3. Contact ESP support
4. Re-add records if missing
5. Wait 24-48 hours for propagation

### Problem 2: IP Reputation Damage

**Symptoms:**
- Gradual delivery decline
- Low IP score
- Specific provider blocking

**Causes:**
- High spam complaints
- Spam trap hits
- List quality issues
- Sending pattern changes

**Fix:**
1. Reduce sending volume
2. Send only to engaged subscribers
3. Clean list aggressively
4. Monitor improvement
5. Consider dedicated IP (at scale)

### Problem 3: Domain Reputation Damage

**Symptoms:**
- All sends affected
- Domain blacklisted
- Google Postmaster shows "Low/Bad"

**Causes:**
- Prolonged poor practices
- Major spam event
- Compromised account
- Similar domain to spammer

**Fix:**
1. Stop sending (temporary)
2. Identify root cause
3. Clean entire list
4. Start fresh with engaged only
5. Gradually rebuild volume
6. Consider new subdomain (last resort)

### Problem 4: Spam Trap Hits

**Symptoms:**
- Sudden blacklisting
- Reputation crash
- ISP blocks

**Causes:**
- Old, never-cleaned list
- Purchased/scraped emails
- Recycled addresses

**Fix:**
1. Remove all subscribers 6+ months inactive
2. Re-confirm list via re-engagement
3. Implement strict hygiene going forward
4. Never buy lists again

### Problem 5: Provider-Specific Blocking

**Symptoms:**
- One ISP (Gmail, Outlook) blocks
- Others fine
- Provider-specific low engagement

**Fix for Gmail:**
1. Check Google Postmaster Tools
2. Review guidelines compliance
3. Improve Gmail-specific engagement
4. Use re-engagement campaigns
5. Register feedback loop

**Fix for Microsoft:**
1. Check SNDS
2. Apply for JMRP
3. Review Microsoft requirements
4. Reduce volume to Microsoft domains
5. Request delisting if blacklisted

### Problem 6: Content Triggering Filters

**Symptoms:**
- Specific emails blocked
- Pattern when certain content sent
- Works when simplified

**Causes:**
- Spam trigger words
- Suspicious URLs
- Bad HTML
- Too many images

**Fix:**
1. Review content against spam filters
2. Remove/replace trigger words
3. Simplify HTML
4. Reduce image-to-text ratio
5. Test with Mail-tester before sending

---

## Recovery Playbook

### Emergency Response (Day 1)

**If Open Rates Crash:**

1. **Stop scheduled sends** (if severe)
2. **Diagnose immediately**
   - Check authentication
   - Check Postmaster
   - Review recent changes
3. **Identify scope**
   - All sends or specific?
   - All providers or specific?
4. **Quick fixes if found**
   - Authentication: Fix immediately
   - Content: Adjust and resend
5. **Communicate if needed**
   - Social media notice
   - Alternative channel notification

### Short-Term Recovery (Week 1-2)

**Stabilization:**
1. Send only to most engaged (opened last 30 days)
2. Reduce frequency temporarily
3. Use best-performing content
4. Monitor metrics closely
5. Document everything

**List Cleaning:**
1. Remove hard bounces
2. Remove 90-day inactive
3. Remove spam complainers
4. Quarantine suspicious segments

### Medium-Term Recovery (Week 2-4)

**Gradual Expansion:**
1. Slowly add back 60-day segment
2. Monitor engagement
3. Continue if metrics hold
4. Pull back if drops

**Reputation Rebuilding:**
1. Focus on high-engagement content
2. Encourage replies and clicks
3. Avoid promotional content
4. Build positive signals

### Long-Term Recovery (Month 1-3)

**Full Restoration:**
1. Continue gradual expansion
2. Implement prevention measures
3. Regular hygiene schedule
4. Ongoing monitoring

---

## Prevention Framework

### Daily Monitoring

**Check:**
- Delivery rate
- Bounce rate
- Complaint rate (if visible)

**Alert if:**
- Delivery <95%
- Bounces >5%
- Complaints >0.1%

### Weekly Review

**Check:**
- Open rate trends
- Engagement patterns
- Growth source quality
- Any provider-specific issues

### Monthly Maintenance

**Execute:**
- Full list hygiene
- Re-engagement campaigns
- Inactive sunset
- Authentication verification

### Quarterly Audit

**Review:**
- Full deliverability health
- Reputation status
- List quality by cohort
- Prevention effectiveness

---

## Tool Reference

### Diagnostic Tools

| Tool | What It Checks | Cost |
|------|---------------|------|
| MXToolbox | DNS, blacklists | Free |
| Mail-tester.com | Spam score | Free/Paid |
| Google Postmaster | Gmail reputation | Free |
| Microsoft SNDS | Outlook reputation | Free |
| Sender Score | IP reputation | Free |
| GlockApps | Seed testing | Paid |

### Blacklist Checking

**Check against:**
- Spamhaus
- Barracuda
- SpamCop
- SORBS
- Composite blacklists

**If Blacklisted:**
1. Identify which list
2. Review their removal process
3. Fix underlying issue first
4. Request removal
5. Document for future

### Seed Testing

**What It Does:**
Send to test addresses across providers, see where it lands.

**Tools:**
- GlockApps
- 250ok (now Validity)
- Mail Monitor

**When to Use:**
- Before major campaigns
- After changes
- During recovery
- Regular monitoring (monthly)

---

## Provider-Specific Guides

### Gmail

**Reputation Tool:** Google Postmaster Tools

**Key Metrics:**
- Domain reputation
- IP reputation
- Spam rate
- Delivery errors

**Best Practices:**
- Keep spam rate <0.1%
- Use one-click unsubscribe
- Authenticate properly
- Maintain engagement

**If Blocked:**
1. Review Postmaster data
2. Reduce volume
3. Clean list
4. Improve engagement
5. Wait for reputation recovery

### Microsoft (Outlook/Hotmail)

**Reputation Tool:** SNDS (Smart Network Data Services)

**Key Metrics:**
- Complaint rate
- Trap hits
- Sending volume

**Best Practices:**
- Register with SNDS
- Join JMRP (Junk Mail Reporting Program)
- Maintain consistent sending
- Avoid sudden volume spikes

**If Blocked:**
1. Check SNDS for issues
2. Review sending patterns
3. Apply for mitigation if needed
4. Reduce volume and rebuild

### Yahoo/AOL

**Reputation Tool:** Feedback loop registration

**Best Practices:**
- Register for feedback loops
- Process complaints immediately
- Maintain list quality
- Consistent sending patterns

---

## Deliverability Incident Log

**Document every incident:**

```
DELIVERABILITY INCIDENT LOG

Date: [Date]
Severity: [Critical/High/Medium/Low]
Discovery: [How noticed]

SYMPTOMS:
- [Symptom 1]
- [Symptom 2]

DIAGNOSIS:
- [What was found]

ROOT CAUSE:
- [Underlying issue]

ACTIONS TAKEN:
1. [Action 1]
2. [Action 2]

RESULT:
- [Outcome]

RECOVERY TIME:
- [Duration]

PREVENTION:
- [Future steps]

LESSONS:
- [What learned]
```

---

## Quick Reference: Recovery Checklist

### Immediate Response

- [ ] Identify symptom (opens, bounces, blocks)
- [ ] Check authentication
- [ ] Check reputation (Postmaster, SNDS)
- [ ] Review recent changes
- [ ] Assess severity

### Short-Term

- [ ] Pause problematic sends
- [ ] Send only to engaged
- [ ] Clean list
- [ ] Fix identified issues
- [ ] Monitor closely

### Medium-Term

- [ ] Gradual volume increase
- [ ] Segment testing
- [ ] Reputation monitoring
- [ ] Documentation

### Prevention

- [ ] Regular hygiene schedule
- [ ] Monitoring dashboard
- [ ] Alert thresholds
- [ ] Documentation of practices
