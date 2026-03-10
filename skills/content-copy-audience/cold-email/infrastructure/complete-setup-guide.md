# Complete Infrastructure Setup Guide

A step-by-step guide to setting up cold email infrastructure from scratch.

---

## Phase 1: Planning (Week 1)

### Step 1.1: Define Your Goals

Before buying anything, define:

**Volume Goals**:
- How many emails per day/month?
- What's your target over 6-12 months?

**Budget**:
- Tools: $100-500/month typical starting point
- Domains: $100-200/year
- Email accounts: $200-500/year

**Timeline**:
- When do you need to be sending?
- Account for 4-6 weeks of setup and warming

### Step 1.2: Calculate Infrastructure Needs

**Formula**:
```
Daily emails ÷ 50 = Number of mailboxes needed
Number of mailboxes ÷ 2-3 = Number of domains needed
```

**Examples**:

| Daily Volume | Mailboxes | Domains |
|--------------|-----------|---------|
| 100 | 2-3 | 1-2 |
| 250 | 5-6 | 2-3 |
| 500 | 10-12 | 4-5 |
| 1,000 | 20-25 | 8-10 |

### Step 1.3: Create Infrastructure Plan

Document your plan:
- Number of domains to purchase
- Domain naming convention
- Email provider choice
- Tool selection
- Timeline with milestones

---

## Phase 2: Domain Setup (Week 1-2)

### Step 2.1: Purchase Domains

**Where to Buy**:
- Namecheap (recommended)
- Cloudflare Registrar
- Porkbun
- Google Domains

**Naming Convention**:
Choose a consistent approach:
- tryacme.com, getacme.com, heyacme.com
- acme.io, acme.co, acme.tech
- acmehq.com, acmeteam.com, acmeinc.com

**Registration Settings**:
- Enable WHOIS privacy
- Register for 2+ years
- Enable auto-renewal
- Set up 2FA on registrar account

### Step 2.2: Configure DNS

For each domain, add these records:

**Basic Records**:
```
A Record: @ → [IP of redirect target] or CNAME to main site
```

**If Redirecting to Main Site** (Recommended):
Set up 301 redirect from secondary domain to primary website.

### Step 2.3: Set Up SSL/TLS

All domains need HTTPS:

**Option 1: Cloudflare** (Recommended)
- Move DNS to Cloudflare
- Enable "Always HTTPS"
- Free SSL certificate

**Option 2: Let's Encrypt**
- Install certbot
- Configure auto-renewal

### Step 2.4: Create Basic Website

Even for secondary domains:

**Minimum**:
- Company name and logo
- Brief description
- Link to main website
- Contact information

**Example HTML**:
```html
<!DOCTYPE html>
<html>
<head>
    <title>Acme Software</title>
    <meta http-equiv="refresh" content="5;url=https://acme.com">
</head>
<body>
    <h1>Acme Software</h1>
    <p>You will be redirected to our main site.</p>
    <p><a href="https://acme.com">Click here if not redirected</a></p>
</body>
</html>
```

---

## Phase 3: Email Provider Setup (Week 2)

### Step 3.1: Choose Provider

**Google Workspace** (Recommended for most):
- Best deliverability
- Universal tool compatibility
- $6/user/month

**Microsoft 365**:
- Good for targeting Outlook users
- $4-6/user/month

### Step 3.2: Set Up Google Workspace

**Account Creation**:
1. Go to workspace.google.com
2. Enter your domain
3. Create admin account
4. Choose plan (Business Starter is fine)
5. Complete payment

**Domain Verification**:
1. Access Admin Console
2. Go to Domains
3. Add verification TXT record to DNS
4. Wait for verification (usually minutes)

### Step 3.3: Configure MX Records

Replace existing MX records with:

```
Priority 1:  ASPMX.L.GOOGLE.COM
Priority 5:  ALT1.ASPMX.L.GOOGLE.COM
Priority 5:  ALT2.ASPMX.L.GOOGLE.COM
Priority 10: ALT3.ASPMX.L.GOOGLE.COM
Priority 10: ALT4.ASPMX.L.GOOGLE.COM
```

### Step 3.4: Configure SPF Record

Add TXT record:
```
v=spf1 include:_spf.google.com ~all
```

### Step 3.5: Configure DKIM

1. Admin Console → Apps → Google Workspace → Gmail
2. Authenticate email
3. Generate DKIM key
4. Add TXT record with provided value
5. Start authentication

### Step 3.6: Configure DMARC

Add TXT record at `_dmarc.yourdomain.com`:
```
v=DMARC1; p=none; rua=mailto:dmarc@yourdomain.com; ruf=mailto:dmarc@yourdomain.com; fo=1
```

Start with `p=none` (monitoring only).

### Step 3.7: Create Mailboxes

For each mailbox:
1. Admin Console → Users → Add new user
2. Enter real-sounding name
3. Create email (firstname.lastname@domain.com)
4. Set temporary password
5. Repeat for all planned mailboxes

### Step 3.8: Configure Each Mailbox

Log into each mailbox and:
1. Set display name (Full Name)
2. Add profile photo (optional but recommended)
3. Create email signature
4. Set timezone
5. Configure recovery email

**Signature Template**:
```
John Smith
Account Executive | Acme Software
(555) 123-4567
www.acme.com
```

---

## Phase 4: Authentication Verification (Week 2)

### Step 4.1: Test Authentication

Use mail-tester.com:
1. Get unique email address
2. Send test email from new mailbox
3. Check results
4. Verify SPF, DKIM, DMARC all pass

### Step 4.2: Verify Google Postmaster Setup

1. Go to postmaster.google.com
2. Add your domain
3. Verify ownership
4. Access reputation data once sending starts

### Step 4.3: Check Blacklist Status

Use MXToolbox or similar:
1. Check domain blacklist status
2. Check IP blacklist status
3. Address any issues before proceeding

---

## Phase 5: Warming (Weeks 3-6)

### Step 5.1: Choose Warming Approach

**Option 1: Automated Warmup Tool** (Recommended)
- Instantly (built-in)
- Smartlead (built-in)
- Lemwarm
- Warmbox

**Option 2: Manual Warming**
- More work but more control
- Use real contacts

### Step 5.2: Start Automated Warmup

If using Instantly or Smartlead:
1. Connect mailboxes
2. Enable warmup
3. Set warmup settings:
   - Start: 5-10 emails/day
   - Increase: 2-3 per day
   - Target: 30-50/day
4. Let run for 2-4 weeks minimum

### Step 5.3: Manual Warming Activities (Supplement)

In parallel with automated warmup:
1. Sign up for newsletters
2. Email colleagues and friends
3. Respond to confirmations
4. Have conversations (back-and-forth)
5. Mix of Gmail, Outlook, corporate addresses

### Step 5.4: Monitor Warming Progress

Track daily:
- Emails sent via warmup
- Emails received
- Reputation indicators
- Any issues or flags

---

## Phase 6: Tool Setup (Weeks 3-4)

### Step 6.1: Choose Sending Tool

**For most users**: Instantly or Smartlead

**Factors**:
- Budget
- Features needed
- Integration requirements
- Volume goals

### Step 6.2: Set Up Sending Tool

**Instantly Setup Example**:
1. Create account
2. Connect email accounts (OAuth or SMTP)
3. Enable warmup on all accounts
4. Configure sending settings:
   - Daily limit per account (30-50)
   - Sending hours (8 AM - 6 PM)
   - Timezone (recipient's)
5. Create test campaign

### Step 6.3: Connect CRM

If using HubSpot, Pipedrive, Salesforce, etc.:
1. Set up integration (native or via Zapier)
2. Configure what syncs:
   - New contacts
   - Email activity
   - Replies
   - Meeting bookings
3. Test integration

### Step 6.4: Set Up Tracking and Analytics

1. Connect Google Postmaster
2. Configure tool dashboards
3. Set up alerts for:
   - Bounce rate spikes
   - Reputation changes
   - Complaint increases

---

## Phase 7: List Preparation (Week 4-5)

### Step 7.1: Define ICP

Document clearly:
- Industry/vertical
- Company size
- Geography
- Job titles
- Technologies
- Exclusions

### Step 7.2: Build Initial List

**Sources**:
- Apollo.io (recommended starting point)
- LinkedIn Sales Navigator
- Your existing contacts

**Volume**: Start with 500-1,000 prospects for initial testing.

### Step 7.3: Verify Emails

Before importing:
1. Export prospect list
2. Run through verification (ZeroBounce, NeverBounce)
3. Remove invalid/risky addresses
4. Target <2% expected bounce rate

### Step 7.4: Import to Tool

1. Import verified list
2. Segment appropriately
3. Map fields correctly
4. Verify import accuracy

---

## Phase 8: Copy Preparation (Week 5)

### Step 8.1: Write Initial Sequence

Create 5-7 email sequence:
- Email 1: Introduction
- Email 2: Follow-up bump
- Email 3: New angle
- Email 4: Value add
- Email 5: Social proof
- Email 6: Different approach
- Email 7: Breakup

### Step 8.2: Create Subject Line Variations

For A/B testing:
- 2-3 subject lines per email
- Different approaches (question, observation, direct)

### Step 8.3: Review for Spam Triggers

Check all emails for:
- Spam words
- Excessive links
- HTML issues
- Merge field errors

### Step 8.4: Test Emails

Send test emails to:
- Your personal accounts
- Colleague accounts
- Seed accounts across providers
- Verify inbox placement

---

## Phase 9: Launch (Week 6)

### Step 9.1: Pre-Launch Checklist

Verify:
- [ ] Warmup has run 3-4 weeks
- [ ] All authentication passing
- [ ] No blacklist issues
- [ ] List verified
- [ ] Copy tested
- [ ] Tracking configured
- [ ] Team trained on reply handling

### Step 9.2: Start Slowly

**Day 1**: 10-25 emails per mailbox
**Day 2-3**: Monitor closely
**Day 4-7**: Gradually increase if metrics look good
**Week 2+**: Reach target volume if healthy

### Step 9.3: Monitor Metrics

**Daily**:
- Bounce rate (should be <2%)
- Delivery rate (should be >97%)
- Open rates (directional check)
- Reply rates
- Spam complaints

**Red Flags to Watch**:
- Bounce rate spike
- Delivery rate drop
- Sudden drop in opens
- Spam complaints

### Step 9.4: Iterate and Optimize

Based on initial data:
- Adjust subject lines
- Modify copy
- Refine targeting
- Optimize sending times

---

## Ongoing Maintenance

### Daily Tasks
- Check for replies
- Process bounces
- Monitor metrics

### Weekly Tasks
- Review campaign performance
- A/B test analysis
- List hygiene
- Adjust sequences

### Monthly Tasks
- Full metrics review
- Infrastructure health check
- Authentication audit
- Suppression list update

### Quarterly Tasks
- Domain assessment
- Tool evaluation
- Strategy review
- List source audit

---

## Common Setup Mistakes

### Mistake 1: Skipping Warmup
**Problem**: Sending too soon tanks deliverability
**Solution**: Always warm 3-4 weeks minimum

### Mistake 2: Incorrect Authentication
**Problem**: SPF/DKIM/DMARC failures = spam
**Solution**: Test thoroughly before sending

### Mistake 3: Poor List Quality
**Problem**: High bounces damage reputation
**Solution**: Verify all emails before sending

### Mistake 4: Too Much Volume Too Fast
**Problem**: Volume spikes look suspicious
**Solution**: Ramp gradually, never spike

### Mistake 5: Using Primary Domain
**Problem**: Risk to main business email
**Solution**: Always use secondary domains

---

## Setup Timeline Summary

| Week | Phase | Key Activities |
|------|-------|----------------|
| 1 | Planning + Domains | Define goals, buy domains, basic DNS |
| 2 | Email Setup | Provider setup, authentication, mailboxes |
| 3-4 | Warming + Tools | Begin warmup, set up sending tool |
| 5 | List + Copy | Build list, write sequences |
| 6 | Launch | Start sending, monitor, iterate |

---

## Cost Breakdown Example

**For 500 emails/day operation**:

| Item | Monthly Cost |
|------|-------------|
| Domains (10 × $15/year) | $12.50 |
| Google Workspace (20 × $6) | $120 |
| Sending Tool (Instantly Hypergrowth) | $77 |
| Data (Apollo Professional) | $99 |
| Verification | $30 |
| **Total** | **~$340/month** |

---

*Proper setup takes time but pays dividends. Rushing leads to problems that take longer to fix than doing it right the first time.*
