# Troubleshooting

When cold email isn't working, systematic troubleshooting finds the problem. This chapter covers the most common issues and how to fix them.

## Diagnostic Framework

### The Funnel Diagnosis
Identify where the funnel is breaking:

**Low Open Rates**: Subject line, deliverability, or list problem
**Opens But No Replies**: Body copy, CTA, or relevance problem
**Replies But No Meetings**: Follow-up or qualification problem
**Meetings But No Deals**: Product-market fit or sales problem

---

## Low Open Rates

### Symptoms
- Open rate below 30%
- Declining opens over time
- Opens much lower than industry benchmark

### Possible Causes

**1. Deliverability Issues**
- Emails landing in spam
- Domain reputation declining
- IP reputation issues

**Diagnosis**: 
- Check Google Postmaster Tools
- Send test emails to seed accounts
- Check blacklist status

**Fixes**:
- Pause sending from affected domains
- Review authentication (SPF/DKIM/DMARC)
- Clean list aggressively
- Warm new infrastructure

**2. Subject Line Problems**
- Generic subject lines
- Spam trigger words
- Not relevant to recipient

**Diagnosis**: 
- Review subject lines for spam words
- Check if subject relates to recipient
- Compare to previous high-performing subjects

**Fixes**:
- A/B test new subject line approaches
- Increase personalization
- Remove spam triggers
- Try different formulas (question, observation, etc.)

**3. List Quality Issues**
- Old/stale data
- Wrong audience
- Invalid emails

**Diagnosis**:
- Check bounce rate (if high, list is bad)
- Review list source
- Verify sample of emails

**Fixes**:
- Re-verify entire list
- Remove old data
- Improve targeting criteria
- Find better data sources

**4. Sender Reputation**
- Unknown sender
- Suspicious-looking address
- No profile/presence

**Diagnosis**:
- Check if sender has LinkedIn presence
- Review sender name format
- Test with different sender

**Fixes**:
- Use real human names
- Build out sender's online presence
- Establish sender through warm-up

---

## Low Reply Rates

### Symptoms
- Opens are good (45%+) but replies below 3%
- Replies declining over time
- No engagement despite opens

### Possible Causes

**1. Irrelevant Message**
- Value prop doesn't resonate
- Wrong pain point
- Misaligned with their needs

**Diagnosis**:
- Review if message matches ICP
- Check if referenced challenges are real
- Survey non-responders if possible

**Fixes**:
- Interview customers about their real challenges
- Refine ICP based on who actually responds
- Test different value propositions
- Increase relevance in copy

**2. Weak CTA**
- Too demanding
- Not clear what to do
- No reason to respond

**Diagnosis**:
- Review CTA for clarity
- Check if CTA matches relationship stage
- Compare to CTAs that worked

**Fixes**:
- Lower friction (interest vs. commitment)
- Make action clearer
- Add reason to respond
- Test different CTA approaches

**3. Trust Issues**
- No credibility established
- Sounds too salesy
- Skeptical audience

**Diagnosis**:
- Review for trust signals
- Check tone and language
- Look for salesy phrases

**Fixes**:
- Add social proof
- Reduce sales language
- Include credibility markers
- Sound more human

**4. Wrong Person**
- Contacting non-decision makers
- Wrong department
- Too senior or too junior

**Diagnosis**:
- Review titles of those responding
- Compare ICP to response patterns
- Check if referrals are common

**Fixes**:
- Adjust targeting criteria
- Test different titles/roles
- Add "who should I talk to?" follow-up

---

## High Bounce Rates

### Symptoms
- Bounce rate above 2%
- Many hard bounces
- Increasing bounces over time

### Causes and Fixes

**1. Invalid Email Addresses**
- Data is old
- Emails were scraped/purchased
- Poor verification

**Fixes**:
- Verify all emails before sending
- Remove bounced addresses immediately
- Improve data sources
- Re-verify old lists

**2. Technical Issues**
- Authentication failures
- Server problems
- Blocked by providers

**Fixes**:
- Check SPF/DKIM/DMARC
- Review server configuration
- Check blacklist status
- Contact blocked providers

**3. List Quality**
- Purchased lists
- Old data
- Wrong sources

**Fixes**:
- Stop using purchased lists
- Refresh data regularly
- Use verified sources only

---

## Spam Folder Issues

### Symptoms
- Emails confirmed going to spam
- Good list but terrible engagement
- Seed tests show spam placement

### Causes and Fixes

**1. Content Triggers**
- Spam words in copy
- Too many links
- Suspicious formatting

**Fixes**:
- Review and remove spam trigger words
- Reduce links (1-2 max)
- Simplify HTML/formatting
- Use plain text

**2. Reputation Issues**
- New/untrusted domain
- Bad IP reputation
- Previous spam history

**Fixes**:
- Check domain and IP reputation
- Warm new infrastructure properly
- Request removal from blacklists
- Improve sending practices

**3. Engagement Signals**
- Recipients not engaging
- High delete without open rate
- Previous complaints

**Fixes**:
- Improve targeting
- Better subject lines
- More relevant content
- Smaller, more engaged lists

---

## Deliverability Recovery

### Emergency Steps
1. **Stop all sending immediately**
2. **Diagnose the issue** (blacklist, reputation, content)
3. **Fix root cause** (clean list, fix authentication, etc.)
4. **Request blacklist removal** if applicable
5. **Rest the affected infrastructure** (2-4 weeks)
6. **Re-warm gradually** before resuming

### Recovery Timeline
- Minor issues: 1-2 weeks
- Moderate issues: 2-4 weeks  
- Severe issues: 4-8 weeks or new infrastructure

### Prevention
- Monitor metrics daily
- Clean lists continuously
- Maintain conservative sending volumes
- Keep authentication current
- Build reputation gradually

---

## Quick Diagnosis Checklist

**Opens Low (<30%)**
- [ ] Check deliverability (Postmaster, seed tests)
- [ ] Review subject lines for spam/relevance
- [ ] Verify list quality and recency
- [ ] Check sender reputation and presence

**Replies Low (<3%)**
- [ ] Verify opens are legitimate (not just privacy pixels)
- [ ] Review message relevance to ICP
- [ ] Check CTA for clarity and friction
- [ ] Assess trust and credibility signals

**Bounces High (>2%)**
- [ ] Verify email list before sending
- [ ] Check data source quality
- [ ] Review technical configuration
- [ ] Remove bounced addresses immediately

**Spam Placement**
- [ ] Run spam content checker
- [ ] Check authentication (SPF/DKIM/DMARC)
- [ ] Review sender reputation
- [ ] Check blacklist status

---

## Summary: Troubleshooting Principles

**Diagnose Before Fixing**: Identify the actual problem.

**Check the Basics First**: Authentication, list quality, deliverability.

**One Fix at a Time**: Don't change everything at once.

**Monitor After Changes**: Verify the fix worked.

**Prevent Future Issues**: Build systems to catch problems early.
