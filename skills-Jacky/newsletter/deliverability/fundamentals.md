# Email Deliverability Fundamentals: Complete Guide

Deliverability determines whether your emails reach the inbox or disappear into spam. A 90% deliverability rate means you're losing 10% of your audience on every send. This guide covers everything you need to protect your sender reputation.

---

## Deliverability 101

### What Is Deliverability?

**Deliverability** = The ability of your emails to reach the inbox (not spam, promotions, or blocked).

**Deliverability Rate** = Emails delivered to inbox / Emails sent

### The Email Journey

```
You hit send
    ↓
Your ESP sends email
    ↓
Receiving server (Gmail, Outlook) checks:
    - Is sender authenticated?
    - Is sender reputation good?
    - Does content look spammy?
    - Do recipients engage?
    ↓
Decision: Inbox, Promotions, Spam, or Blocked
```

### Why Deliverability Matters

| Deliverability | Impact |
|----------------|--------|
| 95%+ | Healthy list, good engagement |
| 85-95% | Some issues, investigate |
| 75-85% | Serious problems, act now |
| <75% | Emergency, stop and fix |

**The Math:**
- 50,000 subscribers
- 85% deliverability
- = 7,500 emails never seen
- = Lost revenue, lost engagement

---

## Email Authentication

### The Three Pillars

Email authentication proves you are who you say you are. Three protocols work together:

**1. SPF (Sender Policy Framework)**
- Lists servers authorized to send on your behalf
- DNS record specifying allowed IPs
- Prevents spoofing from unauthorized servers

**2. DKIM (DomainKeys Identified Mail)**
- Cryptographic signature on emails
- Proves email wasn't modified in transit
- Verifies sending domain ownership

**3. DMARC (Domain-based Message Authentication)**
- Policy combining SPF and DKIM
- Tells receivers what to do with failing emails
- Provides reporting on authentication

### Authentication Status Check

**How to Check:**
1. Send email to yourself (Gmail)
2. Open email → Three dots → "Show original"
3. Look for SPF, DKIM, DMARC: PASS

**Or use tools:**
- MXToolbox.com
- Mail-tester.com
- Google Postmaster Tools

### Setting Up Authentication

**SPF Record:**
```
v=spf1 include:_spf.google.com include:sendgrid.net ~all
```
*(Adjust for your ESP)*

**DKIM:**
Usually handled by your ESP. Add their DKIM record to your DNS.

**DMARC:**
```
v=DMARC1; p=quarantine; rua=mailto:dmarc@yourdomain.com
```

**Setup Checklist:**
- [ ] SPF record added
- [ ] DKIM configured
- [ ] DMARC policy set
- [ ] Custom sending domain (not ESP's domain)
- [ ] All records pass verification

---

## Sender Reputation

### What Is Sender Reputation?

Every domain and IP address has a reputation score used by email providers to decide if you're trustworthy.

**Reputation Factors:**
| Factor | Impact |
|--------|--------|
| Bounce rate | High impact |
| Spam complaints | Very high impact |
| Engagement (opens/clicks) | High impact |
| Spam trap hits | Very high impact |
| List age and quality | Medium impact |
| Sending volume/consistency | Medium impact |

### Checking Your Reputation

**Tools:**
- Google Postmaster Tools (for Gmail)
- Microsoft SNDS (for Outlook/Hotmail)
- Sender Score (from Validity)
- Talos Intelligence (IP reputation)

**Google Postmaster Setup:**
1. Go to postmaster.tools.google.com
2. Add and verify your domain
3. Monitor domain reputation dashboard

### Reputation Levels

**Google Postmaster Ratings:**
| Rating | Meaning |
|--------|---------|
| High | Excellent, inbox delivery |
| Medium | Good, some filtering |
| Low | Problems, more spam filtering |
| Bad | Critical, mostly spam |

### Building Good Reputation

**Do:**
- Maintain high engagement
- Clean list regularly
- Authenticate properly
- Send consistently
- Use double opt-in

**Don't:**
- Buy email lists
- Send to cold emails
- Ignore bounces
- Trigger spam complaints
- Blast after long inactivity

---

## Engagement and Deliverability

### The Engagement Loop

Gmail and others track how recipients interact with your emails:

**Positive Signals:**
- Opens
- Clicks
- Replies
- Moving to primary
- Adding to contacts

**Negative Signals:**
- No opens
- Deleting without opening
- Marking as spam
- Unsubscribes (less negative)

### How Engagement Affects Deliverability

```
High engagement
    ↓
Provider sees value
    ↓
More emails to inbox
    ↓
More engagement
    ↓
(Positive spiral)
```

```
Low engagement
    ↓
Provider sees no value
    ↓
More emails to spam
    ↓
Even lower engagement
    ↓
(Death spiral)
```

### Improving Engagement

**Content Quality:**
- Write compelling subject lines
- Deliver on promises
- Provide genuine value
- Match audience expectations

**List Quality:**
- Remove inactive subscribers
- Segment by engagement
- Re-engage or sunset cold subscribers
- Maintain only interested readers

---

## List Hygiene

### Why Hygiene Matters

Dead emails hurt you:
- Bounces damage reputation
- Inactive subscribers lower engagement
- Spam traps can be fatal

### Types of Bad Emails

**Hard Bounces:**
- Invalid email addresses
- Domain doesn't exist
- Mailbox doesn't exist
- REMOVE IMMEDIATELY

**Soft Bounces:**
- Temporary issues
- Full mailbox
- Server problems
- Monitor and remove if persistent

**Inactive Subscribers:**
- Haven't opened in 60-90+ days
- Dragging down engagement
- Candidates for re-engagement or removal

**Spam Traps:**
- Addresses used to catch spammers
- Often old, abandoned emails
- Catastrophic for reputation

### Hygiene Practices

**Regular Cleaning:**
| Frequency | Action |
|-----------|--------|
| Every send | Remove hard bounces |
| Weekly | Review soft bounces |
| Monthly | Identify 60-day inactive |
| Quarterly | Clean 90-day inactive |

**Cleaning Process:**
1. Export inactive subscribers (90+ days no open)
2. Run re-engagement campaign
3. Give 2-4 weeks to respond
4. Remove non-responders
5. Document and track

---

## Spam Complaints

### The Spam Complaint Threshold

**Industry Standard:** < 0.1% spam complaints

**Calculation:**
```
Spam Complaint Rate = Spam Complaints / Emails Delivered
```

**Example:**
- 50,000 emails sent
- 25 spam complaints
- Rate: 25/50,000 = 0.05% ✓

### What Triggers Complaints

**Common Reasons:**
1. Didn't remember subscribing
2. Content not as expected
3. Too many emails
4. Hard to unsubscribe
5. Email looks spammy

### Reducing Complaints

**Preventive:**
- Clear signup expectations
- Consistent from name/address
- Easy unsubscribe link
- Deliver promised content
- Respect sending frequency

**Reactive:**
- One-click unsubscribe (required by Gmail)
- Preference center
- Immediate removal on complaint
- Process feedback loops

---

## Bounce Management

### Understanding Bounces

**Hard Bounces (Permanent):**
- Email doesn't exist
- Domain invalid
- Blocked sender
- ACTION: Remove immediately

**Soft Bounces (Temporary):**
- Mailbox full
- Server temporarily unavailable
- Message too large
- ACTION: Retry, then remove after 3-5 attempts

### Bounce Rate Targets

| Bounce Rate | Assessment |
|-------------|------------|
| <2% | Healthy |
| 2-5% | Monitor |
| 5-10% | Investigate |
| >10% | Serious problem |

### Managing Bounces

**Automatic:**
Most ESPs handle bounce processing automatically:
- Hard bounces removed immediately
- Soft bounces retried then removed

**Manual Checks:**
- Review bounces weekly
- Look for patterns (domain issues, etc.)
- Clean any missed bounces

---

## Deliverability Monitoring

### Key Metrics to Track

| Metric | Target | Warning |
|--------|--------|---------|
| Delivery rate | >98% | <95% |
| Bounce rate | <2% | >5% |
| Spam complaints | <0.1% | >0.1% |
| Open rate | >30% | <20% |
| Gmail Postmaster | High | Low |

### Monitoring Tools

**Built-in (ESP):**
- Delivery reports
- Bounce reports
- Complaint data

**External:**
- Google Postmaster Tools
- Microsoft SNDS
- GlockApps (seed testing)
- Mail-tester.com

### Weekly Deliverability Review

**Check:**
1. Delivery rate trend
2. Bounce rate
3. Spam complaints
4. Open rate trend
5. Postmaster reputation
6. Any provider-specific issues

---

## Provider-Specific Considerations

### Gmail

**Dominance:** 30-40% of most lists

**Gmail-Specific:**
- Uses Postmaster Tools
- Heavy engagement weighting
- Tabs (Primary vs. Promotions)
- AI-powered filtering

**Gmail Best Practices:**
- High engagement critical
- Authentication required
- Watch Postmaster Tools
- Avoid heavy HTML/images

### Microsoft (Outlook, Hotmail)

**Considerations:**
- Strict spam filtering
- SNDS for monitoring
- IP reputation matters more
- Slower reputation recovery

**Microsoft Best Practices:**
- Watch SNDS data
- Maintain IP reputation
- Consistent sending patterns

### Apple Mail/iCloud

**Privacy Challenges:**
- Mail Privacy Protection (MPP)
- Opens may not be reliable
- Focus on clicks and engagement

### Yahoo/AOL

**Combined Infrastructure:**
- Uses Verizon Media
- Complaint feedback loop
- Watch engagement metrics

---

## Recovery from Deliverability Issues

### Signs of Trouble

- Open rates suddenly drop
- Gmail Postmaster shows "Low" or "Bad"
- Increased bounces
- Spam complaints spike
- Subscriber reports not receiving

### Diagnosis Steps

1. Check authentication (SPF, DKIM, DMARC)
2. Review Google Postmaster
3. Analyze recent sends for issues
4. Check for spam trap hits
5. Review list quality
6. Examine content changes

### Recovery Plan

**Week 1: Stop the Bleeding**
- Pause or reduce sending
- Clean list aggressively
- Fix authentication issues
- Remove known bad segments

**Week 2-4: Rebuild**
- Send only to engaged subscribers
- Smaller, more frequent sends
- Monitor metrics closely
- Gradually expand audience

**Week 5+: Stabilize**
- Slowly increase volume
- Continue monitoring
- Implement prevention measures
- Document learnings

---

## Deliverability Checklist

### Setup (One-Time)

- [ ] Custom sending domain configured
- [ ] SPF record set up correctly
- [ ] DKIM enabled and verified
- [ ] DMARC policy implemented
- [ ] Google Postmaster Tools connected
- [ ] Feedback loops registered

### Ongoing (Weekly)

- [ ] Review delivery rates
- [ ] Check bounce rates
- [ ] Monitor spam complaints
- [ ] Review engagement metrics
- [ ] Check Postmaster reputation
- [ ] Clean bounces from list

### Monthly

- [ ] Deep list hygiene
- [ ] Re-engagement campaigns
- [ ] Sunset inactive subscribers
- [ ] Review sending patterns
- [ ] Update authentication if needed

---

## Key Takeaways

1. **Authentication is table stakes** - Set up SPF, DKIM, DMARC properly
2. **Reputation is everything** - Protect it relentlessly
3. **Engagement drives deliverability** - Quality content = inbox placement
4. **Clean your list** - Dead subscribers hurt you
5. **Monitor constantly** - Catch issues early
6. **React quickly** - Deliverability problems compound fast
