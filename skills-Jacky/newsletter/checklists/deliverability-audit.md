# Deliverability Audit Checklist: Complete Technical Review

A comprehensive audit checklist to assess and optimize your email deliverability.

---

## Audit Overview

### When to Audit

**Regular schedule:**
- Quarterly full audit
- Monthly spot checks
- After any deliverability issues
- Before major campaigns
- After platform/provider changes

### Audit Scope

```
FULL DELIVERABILITY AUDIT

Duration: 2-4 hours
Frequency: Quarterly

Sections:
1. Authentication
2. Reputation
3. List Health
4. Content
5. Technical
6. Monitoring
```

---

## Section 1: Email Authentication

### SPF (Sender Policy Framework)

**Check:**
- [ ] SPF record exists
- [ ] Record is valid
- [ ] Includes all sending sources
- [ ] Under 10 DNS lookups
- [ ] No syntax errors

**How to check:**
```
nslookup -type=TXT yourdomain.com
OR
MXToolbox SPF checker
```

**Valid SPF example:**
```
v=spf1 include:_spf.google.com include:sendgrid.net ~all
```

**Issues to fix:**
- [ ] Record missing → Add record
- [ ] Too many lookups → Consolidate/flatten
- [ ] Missing senders → Add include statements
- [ ] Syntax error → Correct format

### DKIM (DomainKeys Identified Mail)

**Check:**
- [ ] DKIM record exists
- [ ] Signature validates
- [ ] Key length adequate (2048-bit preferred)
- [ ] Selector matches ESP configuration

**How to check:**
- Send test email
- View email headers
- Check for "dkim=pass"
- Or use Mail-tester.com

**Issues to fix:**
- [ ] Record missing → Add from ESP
- [ ] Signature fails → Regenerate key
- [ ] Wrong selector → Verify with ESP

### DMARC (Domain-based Message Authentication)

**Check:**
- [ ] DMARC record exists
- [ ] Policy is set (none/quarantine/reject)
- [ ] Reporting address configured
- [ ] Aligned with SPF and DKIM

**Recommended DMARC:**
```
v=DMARC1; p=quarantine; rua=mailto:dmarc@yourdomain.com
```

**DMARC progression:**
1. Start: `p=none` (monitoring)
2. After confidence: `p=quarantine`
3. Full enforcement: `p=reject`

**Issues to fix:**
- [ ] No record → Add DMARC record
- [ ] Policy too strict → Monitor first
- [ ] No reports → Add rua address

### Authentication Summary

**Complete this scorecard:**
```
AUTHENTICATION SCORECARD

| Check | Status | Notes |
|-------|--------|-------|
| SPF exists | ☐ Pass ☐ Fail | |
| SPF valid | ☐ Pass ☐ Fail | |
| DKIM exists | ☐ Pass ☐ Fail | |
| DKIM passes | ☐ Pass ☐ Fail | |
| DMARC exists | ☐ Pass ☐ Fail | |
| DMARC policy | ☐ Pass ☐ Fail | |

Overall: ___/6
```

---

## Section 2: Sender Reputation

### Google Postmaster Tools

**Check:**
- [ ] Account connected
- [ ] Domain verified
- [ ] Data flowing

**Review:**
- [ ] Domain reputation: [High/Medium/Low/Bad]
- [ ] IP reputation: [High/Medium/Low/Bad]
- [ ] Spam rate: [%]
- [ ] Delivery errors: [Any?]
- [ ] Feedback loop data: [Any?]

**Action thresholds:**
| Metric | Good | Warning | Critical |
|--------|------|---------|----------|
| Domain rep | High | Medium | Low/Bad |
| Spam rate | <0.1% | 0.1-0.3% | >0.3% |

### Microsoft SNDS

**Check:**
- [ ] Account registered
- [ ] IPs added

**Review:**
- [ ] Trap hits: [Yes/No]
- [ ] Complaint rate: [%]
- [ ] Sample messages: [Any issues?]

### Sender Score (Validity)

**Check:**
- [ ] Look up your sending IPs
- [ ] Score: [0-100]

**Score interpretation:**
| Score | Rating |
|-------|--------|
| 80-100 | Good |
| 70-79 | Fair |
| 60-69 | Poor |
| <60 | Critical |

### Blacklist Check

**Check against:**
- [ ] Spamhaus (ZEN)
- [ ] Barracuda
- [ ] SpamCop
- [ ] SORBS
- [ ] Composite lists

**Tools:**
- MXToolbox blacklist check
- MultiRBL.valli.org

**If blacklisted:**
- [ ] Identify which list
- [ ] Determine cause
- [ ] Fix underlying issue
- [ ] Request delisting

### Reputation Summary

```
REPUTATION SCORECARD

Google Postmaster:
- Domain Rep: ____________
- IP Rep: ____________
- Spam Rate: ____________

Microsoft SNDS:
- Status: ____________
- Trap Hits: ____________

Sender Score: ____________

Blacklists:
- Spamhaus: ☐ Clear ☐ Listed
- Barracuda: ☐ Clear ☐ Listed
- SpamCop: ☐ Clear ☐ Listed
- Others: ____________
```

---

## Section 3: List Health

### Subscriber Quality

**Analyze:**
- [ ] Total subscribers: _____
- [ ] Active (opened in 90 days): _____
- [ ] Inactive (no opens 90+ days): _____
- [ ] Activity rate: _____%

**Targets:**
| Metric | Good | Warning | Critical |
|--------|------|---------|----------|
| 90-day active | >70% | 50-70% | <50% |

### Bounce Analysis

**Check recent bounce rates:**
- [ ] Hard bounce rate: _____%
- [ ] Soft bounce rate: _____%
- [ ] Total bounce rate: _____%

**Targets:**
| Bounce Type | Good | Warning | Critical |
|-------------|------|---------|----------|
| Hard | <0.5% | 0.5-2% | >2% |
| Soft | <2% | 2-5% | >5% |
| Total | <3% | 3-5% | >5% |

### Complaint Analysis

**Check:**
- [ ] Spam complaint rate: _____%
- [ ] Recent trend: [Up/Down/Stable]

**Targets:**
| Metric | Good | Warning | Critical |
|--------|------|---------|----------|
| Complaints | <0.05% | 0.05-0.1% | >0.1% |

### Source Analysis

**Review subscriber sources:**
- [ ] Organic: _____%
- [ ] Referral: _____%
- [ ] Paid: _____%
- [ ] Co-reg: _____%
- [ ] Other: _____%

**Check quality by source:**
| Source | 30-day Open Rate | Quality |
|--------|------------------|---------|
| Organic | _____% | |
| Referral | _____% | |
| Paid | _____% | |
| Co-reg | _____% | |

### List Health Actions

- [ ] Remove all hard bounces
- [ ] Clean 90+ day inactive
- [ ] Review low-quality sources
- [ ] Plan re-engagement campaign

---

## Section 4: Content Analysis

### Spam Score Check

**Send test email to Mail-tester.com:**
- [ ] Score: _____/10

**Target:** 9/10 or higher

**Issues flagged:**
- [ ] Spam trigger words
- [ ] HTML issues
- [ ] Link problems
- [ ] Image ratio
- [ ] Authentication

### Content Review

**Check recent emails for:**
- [ ] Spam trigger words (FREE, ACT NOW, etc.)
- [ ] Excessive caps/punctuation
- [ ] Too many links
- [ ] Broken HTML
- [ ] Large images
- [ ] Heavy formatting

### HTML Quality

**Verify:**
- [ ] Valid HTML structure
- [ ] All tags closed
- [ ] Inline CSS (not external)
- [ ] Alt text on images
- [ ] Plain text version exists

### Link Audit

**Check all links for:**
- [ ] Broken links
- [ ] Redirect chains
- [ ] Blacklisted domains
- [ ] Suspicious shorteners

---

## Section 5: Technical Configuration

### Sending Domain

**Check:**
- [ ] Custom sending domain configured
- [ ] Domain age (older is better)
- [ ] Domain not on any blacklists
- [ ] Consistent sending address

### IP Configuration

**Shared IP (most newsletters):**
- [ ] ESP reputation monitored
- [ ] ESP has good practices

**Dedicated IP (if applicable):**
- [ ] Properly warmed up
- [ ] Consistent volume
- [ ] Monitored reputation

### ESP Settings

**Review:**
- [ ] Feedback loops registered
- [ ] Bounce handling enabled
- [ ] Complaint handling automatic
- [ ] Unsubscribe processing
- [ ] List-unsubscribe header

### Technical Summary

```
TECHNICAL SCORECARD

Sending Domain: ____________
Domain Age: ____________
IP Type: ☐ Shared ☐ Dedicated

ESP Configuration:
- Feedback loops: ☐ Yes ☐ No
- Bounce handling: ☐ Yes ☐ No
- Complaint handling: ☐ Yes ☐ No
- List-unsubscribe: ☐ Yes ☐ No
```

---

## Section 6: Monitoring Setup

### Current Monitoring

**Confirm active monitoring:**
- [ ] Google Postmaster connected
- [ ] Microsoft SNDS registered
- [ ] Alerts configured
- [ ] Regular review scheduled

### Alert Thresholds

**Set alerts for:**
| Metric | Alert Threshold |
|--------|-----------------|
| Open rate drop | >20% decline |
| Bounce spike | >5% |
| Complaints | >0.1% |
| Reputation drop | Medium or lower |

### Documentation

**Maintain:**
- [ ] Deliverability log
- [ ] Issue history
- [ ] Fix documentation
- [ ] Regular audit schedule

---

## Audit Summary and Action Plan

### Complete Summary

```
DELIVERABILITY AUDIT SUMMARY

Date: ____________
Auditor: ____________

SCORES:
Authentication: ___/6
Reputation: [Good/Fair/Poor]
List Health: [Good/Fair/Poor]
Content: ___/10
Technical: [Complete/Partial/Needs Work]
Monitoring: [Active/Partial/Missing]

OVERALL STATUS: [Green/Yellow/Red]
```

### Priority Actions

**Complete action plan:**

```
IMMEDIATE (This Week):
1. ________________________
2. ________________________
3. ________________________

SHORT-TERM (This Month):
1. ________________________
2. ________________________
3. ________________________

ONGOING:
1. ________________________
2. ________________________
```

### Next Audit

- [ ] Scheduled for: ____________
- [ ] Added to calendar
- [ ] Set reminder

---

## Quick Audit (15 Minutes)

For regular spot checks:

- [ ] Check Google Postmaster reputation
- [ ] Review last week's bounce rate
- [ ] Check spam complaint rate
- [ ] Verify no new blacklistings
- [ ] Confirm authentication passing
- [ ] Note any issues for investigation
