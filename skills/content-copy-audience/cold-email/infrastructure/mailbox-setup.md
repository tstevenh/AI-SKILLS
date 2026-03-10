# Mailbox Setup for Cold Email

Your mailboxes are the engines of your cold email operation. This guide covers everything from provider selection to warming protocols to rotation strategies.

## Table of Contents

1. [Email Provider Selection](#email-provider-selection)
2. [Google Workspace Setup](#google-workspace-setup)
3. [Microsoft 365 Setup](#microsoft-365-setup)
4. [Alternative Providers](#alternative-providers)
5. [Mailbox Creation Best Practices](#mailbox-creation-best-practices)
6. [Mailbox Warming Explained](#mailbox-warming-explained)
7. [Manual Warming Process](#manual-warming-process)
8. [Warmup Tools Compared](#warmup-tools-compared)
9. [Sending Limits by Provider](#sending-limits-by-provider)
10. [Mailbox Rotation Strategies](#mailbox-rotation-strategies)
11. [When to Retire a Mailbox](#when-to-retire-a-mailbox)
12. [Mailbox Management at Scale](#mailbox-management-at-scale)
13. [Mailbox Checklist](#mailbox-checklist)

---

## Email Provider Selection

### Key Selection Criteria

**Deliverability**: How well does mail from this provider reach inboxes?

**Cost**: Monthly/annual cost per mailbox.

**Features**: Aliases, forwarding, admin controls, API access.

**Sending Limits**: Daily/hourly sending caps.

**Reputation**: Provider's overall standing with receiving servers.

**Ease of Setup**: How simple is configuration?

**Integration**: Works with your cold email tools?

### Provider Comparison Overview

| Provider | Deliverability | Cost/User/Mo | Best For |
|----------|---------------|--------------|----------|
| Google Workspace | Excellent | $6-18 | Most use cases |
| Microsoft 365 | Excellent | $6-12.50 | Enterprise, Outlook targets |
| Zoho Mail | Good | $1-4 | Budget operations |
| Amazon WorkMail | Good | $4 | AWS-integrated stacks |
| Rackspace Email | Good | $2.99 | Budget with support |
| SMTP.com | Varies | $25+ | High volume |
| Custom SMTP | Varies | Varies | Advanced users |

### Recommendation

**For most cold email operations**: Google Workspace

Google Workspace has the best overall deliverability, is widely trusted, and integrates with virtually every cold email tool. The premium cost is worth it.

**For targeting Microsoft domains**: Microsoft 365

If your targets are primarily on Outlook/Microsoft, Microsoft 365 may have slight advantages for inbox placement.

**For budget operations**: Zoho Mail

Zoho provides decent deliverability at a fraction of the cost, good for testing or tight budgets.

---

## Google Workspace Setup

### Why Google Workspace

**Deliverability**: Gmail's sending reputation is excellent. Emails from Google Workspace are less likely to be filtered.

**Trust**: Recipients trust @gmail.com-connected domains more than unknown providers.

**Features**: Excellent admin controls, alias support, API access.

**Integration**: Works with every cold email tool.

### Google Workspace Plans

| Plan | Price/User/Month | Storage | Features |
|------|------------------|---------|----------|
| Business Starter | $6 | 30 GB | Basic email |
| Business Standard | $12 | 2 TB | + Meet, recording |
| Business Plus | $18 | 5 TB | + Vault, advanced controls |
| Enterprise | Custom | Unlimited | Full features |

**For cold email**: Business Starter is sufficient.

### Setup Process

**Step 1: Sign Up**
- Go to workspace.google.com
- Enter your domain
- Create admin account
- Choose plan

**Step 2: Verify Domain**
- Add verification TXT record to DNS
- Or upload verification file to website
- Wait for verification (usually minutes)

**Step 3: Configure DNS Records**

**MX Records** (Replace existing):
```
ASPMX.L.GOOGLE.COM          Priority 1
ALT1.ASPMX.L.GOOGLE.COM     Priority 5
ALT2.ASPMX.L.GOOGLE.COM     Priority 5
ALT3.ASPMX.L.GOOGLE.COM     Priority 10
ALT4.ASPMX.L.GOOGLE.COM     Priority 10
```

**SPF Record**:
```
v=spf1 include:_spf.google.com ~all
```

**DKIM** (Get from Google Admin):
- Admin Console → Apps → Google Workspace → Gmail → Authenticate Email
- Generate DKIM key
- Add TXT record with provided value

**DMARC Record**:
```
v=DMARC1; p=none; rua=mailto:dmarc@yourdomain.com
```

**Step 4: Create Mailboxes**
- Admin Console → Users → Add new user
- Enter first name, last name, email
- Set initial password

**Step 5: Configure Mailbox Settings**
For each mailbox:
- Complete profile (name, photo optional)
- Set up signature
- Configure sending name
- Add recovery email

### Google Workspace Cold Email Considerations

**Sending Limits**:
- Business Starter: 2,000 emails/day per user
- Business Standard+: 2,000 emails/day per user
- For cold email: Stay under 50/day for safety

**Account Maturation**:
- New accounts are flagged for 2-4 weeks
- Start with very low volume
- Gradually increase

**Multi-send Risk**:
- Google monitors for automated sending
- Patterns that look "robotic" trigger review
- Use varied sending times
- Mix automated sends with manual activity

### Google Workspace Troubleshooting

**"Suspicious activity" alerts**: Slow down sending, add manual activity.

**Temporary blocks**: Wait 24-48 hours, reduce volume.

**Account suspension**: Contact support, review activities.

---

## Microsoft 365 Setup

### Why Microsoft 365

**Outlook Targeting**: Better inbox placement to Outlook.com, Hotmail, corporate O365.

**Trust**: Widely recognized, professional perception.

**Features**: Good admin controls, familiar interface.

**Stability**: More lenient on cold email patterns than Google (sometimes).

### Microsoft 365 Plans

| Plan | Price/User/Month | Features |
|------|------------------|----------|
| Exchange Online Plan 1 | $4 | Email only |
| Microsoft 365 Business Basic | $6 | Email + Teams |
| Microsoft 365 Business Standard | $12.50 | + Desktop apps |
| Microsoft 365 Business Premium | $22 | + Security |

**For cold email**: Exchange Online Plan 1 is sufficient and most cost-effective.

### Setup Process

**Step 1: Sign Up**
- Go to microsoft.com/microsoft-365/business
- Choose plan
- Enter domain

**Step 2: Verify Domain**
- Add TXT record to DNS
- Wait for verification

**Step 3: Configure DNS Records**

**MX Record**:
```
yourdomain-com.mail.protection.outlook.com    Priority 0
```

**SPF Record**:
```
v=spf1 include:spf.protection.outlook.com -all
```

**DKIM**:
- Admin Center → Settings → Domains → Select domain → DNS records
- Enable DKIM signing
- Add CNAME records as instructed

**DMARC Record**:
```
v=DMARC1; p=none; rua=mailto:dmarc@yourdomain.com
```

**Autodiscover CNAME** (for Outlook client):
```
autodiscover.yourdomain.com → autodiscover.outlook.com
```

**Step 4: Create Mailboxes**
- Admin Center → Users → Active users → Add user
- Enter details
- Assign license

**Step 5: Configure Mailbox Settings**
- Set display name
- Configure signature
- Add profile photo (optional)

### Microsoft 365 Cold Email Considerations

**Sending Limits**:
- 10,000 recipients/day
- 30 messages/minute
- For cold email: Stay under 50/day

**Reputation Management**:
- Microsoft takes longer to build reputation
- Also takes longer to tank it
- More forgiving of initial low engagement

**Throttling**:
- Less aggressive than Google
- Still monitor for unusual patterns

### Microsoft 365 vs. Google Workspace

| Factor | Google Workspace | Microsoft 365 |
|--------|-----------------|---------------|
| Overall deliverability | Excellent | Very Good |
| Gmail inbox placement | Best | Good |
| Outlook inbox placement | Good | Best |
| Admin interface | Cleaner | More complex |
| Cold email tools support | Universal | Universal |
| Price (basic) | $6/user | $4/user |
| Account suspension risk | Higher | Lower |

---

## Alternative Providers

### Zoho Mail

**Best for**: Budget operations, testing

**Pricing**: 
- Free: Up to 5 users (not for professional use)
- Mail Lite: $1/user/month (5GB)
- Mail Premium: $4/user/month (50GB)

**Pros**:
- Very affordable
- Decent deliverability
- Good features

**Cons**:
- Less recognized than Google/Microsoft
- Deliverability not as strong
- Some tool integration issues

**Setup**: Similar to Google, domain verification + DNS records

### Amazon WorkMail

**Best for**: AWS-integrated businesses

**Pricing**: $4/user/month

**Pros**:
- Good for AWS users
- Solid deliverability
- Integrates with AWS services

**Cons**:
- Less known
- Smaller ecosystem
- Limited integrations

### Rackspace Email

**Best for**: Budget with support needs

**Pricing**: $2.99/user/month

**Pros**:
- Affordable
- Good support
- Reasonable deliverability

**Cons**:
- Less modern interface
- Limited features
- Mixed cold email results

### Custom SMTP

**Best for**: Advanced users, high volume

**Options**:
- SendGrid
- Mailgun
- Amazon SES
- Postmark

**Pros**:
- High volume capacity
- Full control
- Cost-effective at scale

**Cons**:
- More complex setup
- Reputation management is all on you
- Need technical expertise
- Deliverability varies greatly

**Note**: Raw SMTP is generally not recommended for cold email without significant expertise.

---

## Mailbox Creation Best Practices

### Naming Conventions

**Use Real Human Names**:
- john.smith@domain.com ✓
- jane.doe@domain.com ✓
- sales@domain.com ✗
- info@domain.com ✗
- support@domain.com ✗

**Format Options**:
- firstname.lastname@domain.com (most common)
- firstnamelastname@domain.com
- firstname@domain.com (for common names)
- flastname@domain.com (for privacy)

**Consistency**: Use the same format across all mailboxes in your operation.

### Profile Setup

**Display Name**:
- Use full name matching the email
- john.smith@domain.com → "John Smith"
- Don't use company name in display name

**Profile Photo**:
- Optional but recommended
- Use professional headshot
- Increases trust
- Some use AI-generated faces (controversial)

**Signature**:
```
John Smith
Account Executive | Acme Software
Phone: (555) 123-4567
acme.com
```

Keep signatures minimal. Avoid:
- Banner images
- Social media icons
- Marketing messages
- Too many links

### Technical Configuration

**Reply-to Address**:
- Default: Same as from address
- Option: Different address for consolidating replies
- For most cases, keep the same

**Time Zone**:
- Set to your business timezone
- Or to target recipient timezone
- Affects timestamp perception

**Out of Office**:
- Don't enable during campaigns
- Can use for vacation coverage

### Multiple Mailboxes Per Domain

**Ratio**: 2-3 mailboxes per domain is optimal

**Why**:
- More capacity per domain
- Rotation options
- Backup if one has issues

**Example**:
- john.smith@tryacme.com
- sarah.jones@tryacme.com
- mike.chen@tryacme.com

**Caution**: Too many mailboxes per domain (5+) can look like a spam operation.

---

## Mailbox Warming Explained

### What Is Mailbox Warming?

Mailbox warming is the process of building sender reputation for a new email account through gradual, positive email activity.

### Why Warming Is Necessary

**New Account Problem**:
- No sending history
- No engagement data
- Mailbox providers are suspicious
- Early emails likely filtered

**What Warming Accomplishes**:
- Establishes sending patterns
- Generates positive engagement signals
- Builds reputation with major providers
- Prepares account for cold email volume

### Warming Signals That Help

**Outbound**:
- Consistent sending
- Varied recipients
- Mix of individual and business addresses
- Normal sending hours

**Inbound**:
- Receiving replies
- Getting emails opened
- Having emails marked "not spam"
- Being added to contacts

**Engagement**:
- Two-way conversations
- Thread replies
- Reading/interacting with received emails

### Warming Timeline

**Week 1**: 5-10 emails/day
- Mix of test accounts and real contacts
- Ensure replies and engagement
- Monitor for any issues

**Week 2**: 10-20 emails/day
- Expand to more recipients
- Maintain engagement rates
- Begin light outreach

**Week 3**: 20-30 emails/day
- Approaching campaign volume
- Mix of warm and cold contacts
- Watch metrics closely

**Week 4**: 30-50 emails/day
- Near target volume
- Mostly cold contacts acceptable
- Continued monitoring

**Post-Warming**: Maintain
- Don't jump to high volume
- Continue engagement-positive activity
- Keep some warm sends in mix

---

## Manual Warming Process

Manual warming involves personally building reputation without automated tools.

### Manual Warming Steps

**Step 1: Personal Email Activity (Days 1-7)**
- Sign up for newsletters (reputable ones)
- Email friends/colleagues
- Respond to confirmations
- Keep inbox organized

**Step 2: Business Communication (Days 8-14)**
- Email existing customers
- Respond to inquiries
- Light networking emails
- Ensure replies happen

**Step 3: Gradual Outreach (Days 15-21)**
- Begin very light cold email (5-10/day)
- Focus on highest-quality prospects
- Personalize heavily
- Prioritize engagement over volume

**Step 4: Scaling (Days 22-30)**
- Increase volume gradually
- Monitor engagement rates
- Adjust based on metrics
- Continue some warm activity

### Manual Warming Best Practices

**Variety in Recipients**:
- Gmail addresses
- Outlook addresses
- Corporate domains
- Various industries

**Conversation Depth**:
- Multiple back-and-forth exchanges
- Reading and replying
- Adding context to threads

**Timing Patterns**:
- Vary send times
- Don't send exactly every X minutes
- Mix morning, afternoon, evening

**Content Variety**:
- Short messages
- Longer emails
- Questions
- Responses
- Forwarded content (occasionally)

### Manual vs. Automated Warming

| Aspect | Manual | Automated |
|--------|--------|-----------|
| Time investment | High | Low |
| Cost | Time only | Tool subscription |
| Control | Full | Limited |
| Natural patterns | Very natural | Somewhat artificial |
| Scalability | Low | High |
| Reliability | Varies | Consistent |

**Recommendation**: Use automated tools for scale, supplement with manual activity.

---

## Warmup Tools Compared

### How Warmup Tools Work

Warmup tools connect your mailbox to a network of other mailboxes. They:
1. Send emails from your account to network accounts
2. Network accounts open, reply, mark as important
3. This generates positive engagement signals
4. Your mailbox builds reputation

### Major Warmup Tools

#### Instantly Warmup

**Overview**: Built into Instantly cold email platform

**Pricing**: Included with Instantly subscription ($30-$97/month)

**Features**:
- Large network of real mailboxes
- Automatic daily warmup
- Reply generation
- Reputation tracking

**Pros**:
- Convenient if using Instantly
- Large network
- Good reputation building

**Cons**:
- Tied to Instantly subscription
- Less standalone flexibility

**Best for**: Instantly users

#### Lemwarm

**Overview**: Dedicated warmup tool from Lemlist

**Pricing**: $29/mailbox/month

**Features**:
- Smart email conversations
- Human-like replies
- Domain health monitoring
- Works with any email provider

**Pros**:
- High-quality conversations
- Good reputation building
- Works standalone

**Cons**:
- Relatively expensive per mailbox
- Separate from sending tool

**Best for**: Premium warming needs

#### Warmbox

**Overview**: Dedicated email warmup service

**Pricing**: 
- $15/mailbox/month (Solo)
- $49/month for 3 mailboxes (Startup)
- $99/month for 10 mailboxes (Growth)

**Features**:
- AI-powered conversations
- Inbox placement monitoring
- Reply optimization
- Multi-provider support

**Pros**:
- Affordable
- Good features
- Works independently

**Cons**:
- Smaller network than some
- Separate tool to manage

**Best for**: Cost-conscious warming

#### Mailwarm

**Overview**: Simple warmup service

**Pricing**: 
- $69/month for 1 mailbox
- $159/month for 3 mailboxes
- $479/month for 10 mailboxes

**Features**:
- Automated sending/receiving
- Reply generation
- Reputation tracking

**Pros**:
- Simple to use
- Reliable

**Cons**:
- Expensive per mailbox
- Basic features

**Best for**: Simplicity

#### Smartlead Warmup

**Overview**: Built into Smartlead cold email platform

**Pricing**: Included with Smartlead ($39-$79/month)

**Features**:
- Network-based warming
- Automatic engagement
- Reputation scoring
- Integrated with sending

**Pros**:
- Convenient if using Smartlead
- Included in platform price
- Good network

**Cons**:
- Tied to Smartlead
- Less standalone control

**Best for**: Smartlead users

### Warmup Tool Comparison

| Tool | Cost/Mailbox/Mo | Network Size | Standalone | Integration |
|------|-----------------|--------------|------------|-------------|
| Instantly | ~$10-15* | 200K+ | No | Instantly |
| Lemwarm | $29 | Large | Yes | Any |
| Warmbox | $15-33 | Medium | Yes | Any |
| Mailwarm | $69 | Medium | Yes | Any |
| Smartlead | ~$13-26* | Large | No | Smartlead |

*Estimated based on plan pricing

### Warmup Best Practices

**Do**:
- Start warming 2-4 weeks before campaigns
- Continue warming during campaigns (reduced)
- Monitor warmup metrics
- Combine with some manual activity

**Don't**:
- Rely solely on warmup tools
- Skip warming due to impatience
- Stop warming entirely during campaigns
- Ignore warmup analytics

---

## Sending Limits by Provider

### Provider Sending Limits

#### Google Workspace

**Official Limits**:
- 2,000 emails/day (external recipients)
- 500 emails/day (trial accounts)
- 10,000 emails/day (internal + external)

**Practical Cold Email Limits**:
- Recommended: 30-50/day per mailbox
- Maximum safe: 100/day (established accounts)
- Risky: 150+/day

**Why Lower Than Official**:
- Cold email has higher complaint rates
- Low engagement triggers review
- Staying conservative protects reputation

#### Microsoft 365

**Official Limits**:
- 10,000 recipients/day
- 30 messages/minute

**Practical Cold Email Limits**:
- Recommended: 30-50/day per mailbox
- Maximum safe: 100/day (established accounts)
- Risky: 150+/day

#### Zoho Mail

**Official Limits**:
- 500-1,500/day depending on plan

**Practical Cold Email Limits**:
- Recommended: 25-40/day
- Maximum safe: 75/day

#### Other Providers

Most email providers have limits around:
- 500-2,000 emails/day officially
- 30-50/day recommended for cold email

### Volume Scaling Strategy

**Month 1**: Conservative
- 25-30 emails/day per mailbox
- Focus on quality over volume
- Monitor metrics closely

**Month 2**: Moderate
- 40-50 emails/day per mailbox
- Verify metrics remain healthy
- Add mailboxes for more volume

**Month 3+**: Optimized
- Up to 50-75/day for healthy mailboxes
- Scale through more mailboxes, not more per-mailbox volume
- Continuous monitoring

### Sending Patterns

**Time Distribution**:
- Don't send all emails at once
- Spread across business hours
- Randomize slightly

**Day Distribution**:
- Tuesday-Thursday: Full volume
- Monday: Moderate (inbox backlog)
- Friday: Lighter (weekend mode)
- Weekend: Minimal or none

**Hourly Pattern**:
- 8-10 AM: Good opens
- 11 AM-12 PM: Moderate
- 1-3 PM: Lower
- 3-5 PM: Good

---

## Mailbox Rotation Strategies

### Why Rotate Mailboxes

**Risk Distribution**: Problems with one mailbox don't stop everything.

**Reputation Protection**: No single mailbox gets overworked.

**Engagement Balance**: Different mailboxes may resonate differently.

### Rotation Approaches

**Even Rotation**:
All mailboxes send equal daily volume.

10 mailboxes, 500 emails/day → 50 each

**Performance-Based Rotation**:
Higher-performing mailboxes get more volume.

Mailbox A (60% open rate): 75 emails
Mailbox B (50% open rate): 50 emails
Mailbox C (40% open rate): 25 emails

**Prospect-Segment Rotation**:
Different mailboxes for different segments.

Mailbox A: Enterprise prospects
Mailbox B: Mid-market prospects
Mailbox C: SMB prospects

**A/B Test Rotation**:
Different mailboxes test different approaches.

Mailbox A: Approach 1
Mailbox B: Approach 2

### Implementing Rotation

**Tool-Based Rotation**:
Most cold email tools handle rotation automatically.

Settings typically include:
- Rotate evenly
- Rotate by time
- Rotate by performance
- Custom rules

**Manual Rotation**:
For simple setups, manually assign campaigns to mailboxes.

### Rotation Best Practices

- Keep sequences within same mailbox (avoid switching mid-sequence)
- Match sender to content (different people for different offers)
- Balance warm and cold activity per mailbox
- Review rotation effectiveness monthly

---

## When to Retire a Mailbox

### Warning Signs

**Declining Metrics**:
- Open rates dropping below 30%
- Bounce rates above 3%
- Reply rates declining
- Increasing spam complaints

**Provider Warnings**:
- "Suspicious activity" alerts
- Temporary sending blocks
- Security challenges

**Deliverability Issues**:
- Landing in spam consistently
- Failed seed tests
- Postmaster reputation "Low" or "Bad"

### Retirement Decision Framework

**Minor Issues**: Rest and recover
- Pause for 1-2 weeks
- Continue warming activity
- Resume at lower volume

**Moderate Issues**: Extended recovery
- Pause for 2-4 weeks
- Reset warming from scratch
- Investigate root cause

**Severe Issues**: Retire
- Persistent problems after recovery attempts
- Account suspended
- Blacklist that won't clear

### Retirement Process

1. **Stop all cold email** from the mailbox
2. **Complete existing sequences** if possible (or notify recipients)
3. **Export any needed data**
4. **Remove from tools**
5. **Keep the account** (don't delete immediately)
6. **Re-evaluate in 3-6 months**

### Replacement Planning

Always have backup mailboxes ready:

**Reserve mailboxes**: 10-20% of active count
**State**: Warmed and ready
**Volume**: Minimal maintenance volume

When retiring a mailbox, promote a reserve to active status.

---

## Mailbox Management at Scale

### Scaling Challenges

**Organization**: Tracking many mailboxes becomes complex.

**Consistency**: Maintaining quality across all mailboxes.

**Monitoring**: Can't manually check each mailbox daily.

**Cost**: Provider fees multiply.

### Organization System

**Mailbox Database**:
Track all mailboxes in a central system (spreadsheet, Notion, Airtable).

| Email | Domain | Provider | Status | Created | Last Audit | Daily Vol | Notes |
|-------|--------|----------|--------|---------|------------|-----------|-------|
| john@tryacme.com | tryacme.com | Google | Active | 2025-01-15 | 2026-01-01 | 50 | Primary |
| sarah@tryacme.com | tryacme.com | Google | Active | 2025-01-15 | 2026-01-01 | 50 | |
| mike@acme.io | acme.io | Google | Warming | 2026-01-20 | - | 10 | Reserve |

### Monitoring at Scale

**Automated Monitoring**:
- Use cold email tool dashboards
- Set up alerts for metric thresholds
- Regular export/review of performance data

**Regular Audits**:
- Weekly: Quick metric review
- Monthly: Deep dive per mailbox
- Quarterly: Full audit and cleanup

### Cost Management

**Optimize Provider Mix**:
- Core mailboxes: Google Workspace
- Backup/reserve: Cheaper providers
- Test mailboxes: Free tiers if available

**Consolidate Domains**:
- 2-3 mailboxes per domain (not 1)
- Reduces per-mailbox domain cost

**Remove Unused**:
- Audit for inactive mailboxes
- Retire genuinely unused accounts
- Don't pay for mailboxes not in rotation

### Team Management

**For teams sending cold email**:

**Dedicated Mailboxes**: Each sender has their own mailbox(es)
- Clear ownership
- Personal brand building
- Individual metrics

**Shared Mailboxes**: Pool of mailboxes used by team
- Flexibility
- Cover absences
- Harder to track individual performance

**Hybrid**: Primary personal + shared backup
- Best of both worlds
- More complex management

---

## Mailbox Checklist

### New Mailbox Setup Checklist

- [ ] Created with human name format
- [ ] Display name configured
- [ ] Profile photo added (optional)
- [ ] Signature set up
- [ ] Connected to warmup tool
- [ ] Added to sending tool
- [ ] SPF/DKIM verified for domain
- [ ] Test email sent successfully
- [ ] Added to tracking system

### Weekly Maintenance Checklist

- [ ] Check warmup metrics
- [ ] Review bounce rates
- [ ] Check for provider warnings
- [ ] Verify sending volume appropriate
- [ ] Review reply handling

### Monthly Audit Checklist

- [ ] Full metric review per mailbox
- [ ] Provider dashboard check
- [ ] Postmaster Tools review
- [ ] Update tracking database
- [ ] Identify underperformers
- [ ] Plan rotation adjustments
- [ ] Check warmup tool effectiveness

### Quarterly Review Checklist

- [ ] Cost analysis
- [ ] Performance comparison
- [ ] Retirement decisions
- [ ] Reserve mailbox status
- [ ] Provider evaluation
- [ ] Process improvements

---

## Summary: Mailbox Success Principles

**Quality Providers**: Google Workspace or Microsoft 365 for primary sending.

**Proper Warming**: Never skip or rush the warming process.

**Conservative Limits**: Stay well under provider maximums.

**Active Rotation**: Don't overwork any single mailbox.

**Constant Monitoring**: Catch issues before they become crises.

**Strategic Scaling**: Add mailboxes before hitting limits.

**Documentation**: Track everything in a central system.

---

*Mailboxes are your sending engines. Treat them with care, and they'll deliver results consistently.*
