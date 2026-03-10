# Email Deliverability Science

Deliverability is the technical foundation of cold email success. You can write the perfect email, but if it doesn't reach the inbox, it doesn't matter. This comprehensive guide covers everything you need to know about getting your emails delivered.

## Table of Contents

1. [Understanding Deliverability](#understanding-deliverability)
2. [How Spam Filters Work in 2026](#how-spam-filters-work-in-2026)
3. [Sender Reputation Explained](#sender-reputation-explained)
4. [IP Warming Protocols](#ip-warming-protocols)
5. [Domain Reputation](#domain-reputation)
6. [Email Authentication (SPF, DKIM, DMARC)](#email-authentication-spf-dkim-dmarc)
7. [Blacklists and How to Avoid Them](#blacklists-and-how-to-avoid-them)
8. [Inbox Placement vs. Delivery Rate](#inbox-placement-vs-delivery-rate)
9. [Advanced Deliverability Factors](#advanced-deliverability-factors)
10. [Monitoring and Testing](#monitoring-and-testing)
11. [Deliverability Recovery](#deliverability-recovery)
12. [Deliverability Checklist](#deliverability-checklist)

---

## Understanding Deliverability

### What Is Deliverability?

Deliverability is the ability of an email to reach the recipient's inbox. It's distinct from delivery:

**Delivery**: The email was accepted by the recipient's mail server
**Deliverability**: The email reached the inbox (not spam folder)

An email can be delivered but not deliverable—it arrived at the server but landed in spam.

### Why Deliverability Matters

Consider two campaigns:

**Campaign A**: 1,000 emails sent, 90% deliverability
- 900 reach inbox
- 50% open rate = 450 opens
- 10% reply rate = 45 replies

**Campaign B**: 1,000 emails sent, 50% deliverability
- 500 reach inbox
- 50% open rate = 250 opens
- 10% reply rate = 25 replies

Same email, same list, 44% fewer results just from deliverability difference.

### The Deliverability Ecosystem

Multiple parties influence deliverability:

**Mailbox Providers (MBPs)**: Gmail, Outlook, Yahoo, etc. They decide what reaches the inbox.

**Internet Service Providers (ISPs)**: Network-level providers that can block IP addresses.

**Reputation Services**: Third-party services that track sender reputation.

**Your Infrastructure**: Domains, IPs, authentication, and technical setup.

**Your Practices**: How you build lists, write emails, and handle responses.

### The Deliverability Goal

The goal isn't just reaching the inbox—it's sustainable inbox placement:

- Primary inbox, not promotions tab
- Consistent delivery over time
- Across all major providers
- At your desired sending volume

---

## How Spam Filters Work in 2026

Spam filters have evolved dramatically. Understanding modern filtering helps you avoid triggering them.

### The Three Filtering Stages

#### Stage 1: Gateway Filtering

When your email arrives at the recipient's mail server, gateway filters perform initial checks:

**Connection-Level Checks**:
- Is the sending IP blacklisted?
- Does the sending IP have proper DNS configuration?
- Is the sender authenticated (SPF/DKIM/DMARC)?
- Is the sending server behavior suspicious?

**Envelope Checks**:
- Is the sender domain legitimate?
- Does the "From" address match authentication?
- Are there suspicious header anomalies?

**Volume Checks**:
- Is this IP sending unusual volume?
- Are there patterns suggesting automation?

If the email fails gateway filtering, it's rejected (bounced) or silently dropped before reaching any folder.

#### Stage 2: Content Filtering

Emails that pass gateway filters are analyzed for content signals:

**Textual Analysis**:
- Spam keywords and phrases
- Urgency language patterns
- Promotional indicators
- Link/text ratio
- Image/text ratio
- HTML complexity

**Link Analysis**:
- Are links pointing to suspicious domains?
- Are links using URL shorteners?
- Are redirects involved?
- Is the link domain reputation good?
- Are links tracking pixels or spammy?

**Attachment Analysis**:
- File types and sizes
- Macro presence
- Known malware signatures

**Template Detection**:
- Does this email match known spam templates?
- Is the structure formulaic?
- Does it resemble other spam?

#### Stage 3: Machine Learning Filtering

Modern spam filters use ML models that consider:

**Behavioral Signals**:
- How do recipients interact with emails from this sender?
- Do they open, reply, delete, mark as spam?
- Do they move emails out of spam?
- Do they add the sender to contacts?

**Network Analysis**:
- Are other senders from this IP/domain being flagged?
- Are recipients across the network complaining?
- What's the sender's historical pattern?

**Content Modeling**:
- Does this email match patterns of wanted mail?
- Is the language consistent with legitimate communication?
- Are there anomalies in writing style?

### Gmail's Filtering Approach

Gmail is the most sophisticated and most important MBP to understand:

**User Engagement Priority**: Gmail heavily weights recipient behavior. If your emails are opened, replied to, and starred, future emails are prioritized. If they're deleted unopened or marked spam, you're in trouble.

**Sender Reputation System**: Gmail maintains detailed reputation scores based on:
- Domain reputation
- IP reputation
- Authentication compliance
- Complaint rates
- Engagement metrics

**Promotions Tab Filtering**: Gmail categorizes promotional content to the Promotions tab, not spam—but this still reduces visibility. Factors include:
- Promotional language
- Marketing design elements
- Unsubscribe headers
- Bulk sending patterns
- Tracking pixels

**AI-Based Filtering**: Gmail uses advanced ML models trained on billions of emails. These models can detect spam patterns humans might miss.

### Microsoft's Filtering Approach

Outlook/Hotmail/Office 365 has its own approach:

**SmartScreen Filtering**: Microsoft's reputation system that analyzes sender history, content, and recipient behavior.

**Junk Email Filter Levels**: Recipients can set filtering aggressiveness, affecting how much email is filtered.

**Safe Senders List**: If a recipient adds you to their safe senders, your emails bypass most filtering.

**Authentication Emphasis**: Microsoft is strict about SPF/DKIM/DMARC compliance.

**Slow to Warm, Slow to Cool**: Microsoft takes longer to build positive reputation, but also takes longer to tank reputation.

### Yahoo/AOL Filtering

Now under the same corporate umbrella, Yahoo and AOL share filtering:

**Complaint-Based Filtering**: Heavily influenced by spam complaint rates. Low tolerance for complaints.

**IP Reputation Focus**: Strong emphasis on sending IP reputation.

**Engagement Tracking**: Engagement signals influence filtering decisions.

### Corporate Email Filtering

Enterprise email systems add layers:

**Security Gateways**: Proofpoint, Mimecast, Barracuda, etc. These enterprise security systems have their own filters.

**Sandboxing**: Links and attachments may be analyzed in sandboxed environments.

**Policy-Based Filtering**: IT departments set policies that can block categories of email.

**Custom Blocklists**: Organizations maintain their own blocklists.

**Impersonation Detection**: Systems looking for business email compromise attempts.

### Content Filtering Signals

#### High-Risk Content (Avoid)

**Subject Line Red Flags**:
- ALL CAPS
- Excessive punctuation (!!!, ???)
- "Free," "Act now," "Limited time"
- "Re:" or "Fwd:" when not actually replying
- Dollar amounts ($$$)
- Percentage promises (100%, 50% off)

**Body Copy Red Flags**:
- Excessive links
- URL shorteners (bit.ly, etc.)
- Invisible text or tiny fonts
- Color discrepancies (white text on white background)
- Suspicious image URLs
- JavaScript or embedded forms
- Excessive HTML formatting
- Attachments from unknown senders

**Technical Red Flags**:
- Missing or failed authentication
- Mismatched "From" and reply-to domains
- Unusual character encoding
- Inconsistent headers
- Broken HTML

#### Lower-Risk Content

**Positive Signals**:
- Plain text or minimal HTML
- Few links (1-2 maximum)
- Links to reputable domains
- Personalization that appears genuine
- Conversational tone
- Questions that invite replies
- Proper grammar and spelling

### Engagement-Based Filtering

The most important modern filter factor is engagement:

**Positive Engagement Signals**:
- Opens (especially quick opens)
- Replies
- Clicks on links
- Adding to contacts
- Moving from spam to inbox
- Starring or flagging
- Forwarding

**Negative Engagement Signals**:
- Marking as spam
- Deleting without opening
- Ignoring repeatedly
- Unsubscribing
- Bouncing

**The Engagement Feedback Loop**: Good engagement improves reputation, which improves deliverability, which enables more good engagement. Bad engagement creates a downward spiral.

---

## Sender Reputation Explained

Sender reputation is the aggregate measure of your email trustworthiness. It's the single most important factor in deliverability.

### What Contributes to Reputation

#### IP Reputation

Your sending IP address carries reputation based on:

**Sending History**: Volume and consistency of sending from this IP.

**Complaint Rates**: Percentage of emails marked as spam by recipients.

**Bounce Rates**: Percentage of emails that hard bounce (invalid addresses).

**Spam Trap Hits**: Emails sent to known spam trap addresses.

**Blacklist Presence**: Whether the IP appears on any blacklists.

**Authentication Compliance**: Whether emails from this IP pass SPF/DKIM/DMARC.

**Content Quality**: Historical quality of content sent from this IP.

**Engagement Rates**: How recipients interact with mail from this IP.

#### Domain Reputation

Independent of IP, your domain has reputation:

**Domain Age**: Older domains generally have better baseline reputation.

**Domain Sending History**: What's been sent from this domain before?

**Associated IPs**: What IPs have sent email for this domain?

**Blacklist Status**: Is the domain on any blacklists?

**Website Content**: Some systems check the associated website for spamminess.

**WHOIS Information**: Is registration private? Recently changed?

**Authentication Setup**: Does the domain have proper SPF/DKIM/DMARC?

### How Reputation Is Scored

Different MBPs have different scoring systems:

**Gmail Postmaster Tools** provides:
- Domain reputation (Bad, Low, Medium, High)
- IP reputation (Bad, Low, Medium, High)
- Spam rate
- Authentication success rate

**Microsoft SNDS** (Smart Network Data Services) provides:
- IP status
- Sample messages
- Complaint data

**Yahoo Complaint Feedback Loop** provides:
- Complaint rates
- Affected email addresses

### Reputation Thresholds

While exact thresholds are proprietary, general guidelines:

**Complaint Rate**:
- Excellent: < 0.1%
- Good: 0.1% - 0.3%
- Concerning: 0.3% - 0.5%
- Dangerous: > 0.5%

**Bounce Rate**:
- Excellent: < 1%
- Good: 1% - 2%
- Concerning: 2% - 5%
- Dangerous: > 5%

**Spam Trap Hits**:
- Acceptable: 0
- Any spam trap hits indicate list problems

### Building Reputation from Scratch

New domains and IPs have no reputation, which isn't the same as good reputation—it's closer to suspicious.

**The Cold Start Problem**: With no history, MBPs are cautious. Your first emails are likely filtered more aggressively.

**Solutions**:
1. **Gradual ramp-up**: Start with very low volume and increase slowly
2. **Warm-up activities**: Send to engaged recipients first
3. **Authentication from day one**: Have all authentication perfect before sending
4. **Quality over quantity**: Early emails should have exceptional engagement

### Protecting Reputation

**Proactive Protection**:
- Clean lists before sending
- Verify email addresses
- Remove unengaged contacts
- Honor opt-outs immediately
- Monitor complaint rates
- Track bounce rates
- Check blacklist status regularly

**Reactive Protection**:
- Pause sending if metrics deteriorate
- Investigate spikes in complaints or bounces
- Remove problematic list segments
- Review recent changes to practices

---

## IP Warming Protocols

IP warming is the process of gradually increasing sending volume from a new IP to establish positive reputation.

### Why IP Warming Is Necessary

New IPs have no reputation history. When MBPs see sudden high volume from an unknown IP, they assume spam and filter aggressively.

Warming builds trust incrementally:
1. Send small volumes
2. Get positive engagement
3. MBPs learn to trust the IP
4. Gradually increase volume
5. Maintain positive metrics throughout

### IP Warming Schedule

#### Week 1: Foundation (Days 1-7)

| Day | Daily Volume | Target Recipients |
|-----|--------------|-------------------|
| 1   | 20           | Most engaged contacts |
| 2   | 30           | Most engaged contacts |
| 3   | 50           | Most engaged contacts |
| 4   | 75           | Engaged contacts |
| 5   | 100          | Engaged contacts |
| 6   | 150          | Engaged contacts |
| 7   | 200          | Engaged contacts |

**Week 1 Focus**:
- Send only to contacts who know you (existing customers, newsletter subscribers)
- Prioritize contacts who have opened/clicked recently
- Split across major MBPs (Gmail, Outlook, etc.)
- Monitor deliverability closely

#### Week 2: Building (Days 8-14)

| Day | Daily Volume | Target Recipients |
|-----|--------------|-------------------|
| 8   | 300          | Engaged + warm contacts |
| 9   | 400          | Engaged + warm contacts |
| 10  | 500          | Mixed engagement levels |
| 11  | 650          | Mixed engagement levels |
| 12  | 800          | General list |
| 13  | 1,000        | General list |
| 14  | 1,200        | General list |

**Week 2 Focus**:
- Expand to less engaged contacts
- Continue monitoring metrics
- Pause if bounce rates or complaints spike
- Maintain authentication compliance

#### Weeks 3-4: Scaling (Days 15-28)

| Day Range | Daily Volume |
|-----------|--------------|
| 15-17     | 1,500        |
| 18-20     | 2,000        |
| 21-23     | 3,000        |
| 24-26     | 4,000        |
| 27-28     | 5,000+       |

**Weeks 3-4 Focus**:
- Gradual increase toward target volume
- Monitor reputation tools
- Introduce cold contacts slowly
- Adjust pace based on metrics

#### Week 5+: Maintenance

- Reach target volume
- Maintain consistent sending
- Continue monitoring
- Avoid sudden volume spikes

### Warming Best Practices

**Start with Your Best List**:
Send first to contacts most likely to engage—existing customers, recent inquiries, active subscribers. Their positive engagement builds reputation.

**Diversify Recipients**:
Don't send all emails to one MBP. Spread across Gmail, Outlook, Yahoo, corporate domains proportionally.

**Send at Normal Times**:
Warm during your intended sending windows. Sending at 3 AM then switching to 9 AM changes behavior patterns.

**Maintain Consistency**:
Daily sending is better than large batches. Consistent patterns build predictable reputation.

**Watch the Metrics**:
- Bounce rate > 2%? Pause and clean list
- Complaint rate > 0.3%? Review content/targeting
- Delivery rate dropping? Investigate immediately

**Don't Rush**:
Impatience is the biggest warming failure. Skipping ahead because "everything looks fine" can permanently damage reputation.

### Warming with Cold Email Tools

Many cold email platforms have built-in warming features:

**Instantly**: Auto-warming with network of real inboxes
**Smartlead**: Warmup with email interactions
**Lemwarm**: Automated warmup conversations
**Warmbox**: Dedicated warming service

These tools send emails between real accounts, generating opens and replies that build reputation.

**Using warmup tools effectively**:
1. Start warming 2-4 weeks before cold campaigns
2. Continue warming during campaigns (reduced volume)
3. Use tool analytics to monitor warming progress
4. Don't rely solely on tool—also send to engaged real contacts

### Shared IP vs. Dedicated IP

**Shared IP**:
- Multiple senders share the same IP
- Reputation is collective
- Other senders' behavior affects you
- Lower cost
- Suitable for low volume

**Dedicated IP**:
- IP is exclusively yours
- Full control over reputation
- Requires warming
- Higher cost
- Necessary for high volume

**When to Use Each**:
- < 5,000 emails/month: Shared IP is fine
- 5,000-50,000/month: Consider dedicated
- > 50,000/month: Dedicated IP strongly recommended

---

## Domain Reputation

Domain reputation exists independently of IP reputation and can be equally important—sometimes more so.

### Domain Reputation Factors

**Age**: Older domains have more history. Brand new domains are suspicious.

**Sending History**: Has this domain sent spam before? Has it sent high-engagement mail?

**Associated IPs**: What IPs have sent for this domain? Are any problematic?

**Blacklist Status**: Is the domain on any blacklists?

**Website Content**: Some systems check the domain's website for spam signals.

**Authentication Configuration**: Does the domain have proper SPF, DKIM, DMARC?

### Domain Age Strategies

**Aging New Domains**:
If buying new domains for cold email:
1. Purchase domains 2-4 weeks before using
2. Set up website with basic content
3. Configure authentication immediately
4. Send light email traffic (personal use)
5. Begin warming process

**Purchasing Aged Domains**:
Some buy expired domains with history. Risks:
- Previous owner's spam history may persist
- Domain may be blacklisted
- MBPs track domain changes
- Not recommended unless you can fully verify history

### Multiple Domain Strategy

Using multiple domains protects your primary domain:

**Primary Domain**: Your main business domain. Use for customers, marketing, important communications.

**Secondary Domains**: Separate domains for cold outreach. If reputation suffers, your primary domain is protected.

**Domain Naming Conventions**:
- tryacme.com (add prefix)
- getacme.com (add prefix)
- acme.io (different TLD)
- acmehq.com (add suffix)
- acme-mail.com (descriptive suffix)

**Best Practices**:
- Keep secondary domains professional
- Forward secondary domains to main website
- Use consistent branding
- Have 2-5 secondary domains per 1,000 daily emails

### Domain Warming

Domains need warming too, especially new ones:

**Week 1-2**: Personal email activity
- Set up basic email accounts
- Send/receive personal emails
- Sign up for newsletters
- Respond to confirmations

**Week 2-3**: Light business activity
- Email existing contacts
- Respond to inquiries
- Very light outreach

**Week 3-4**: Gradual cold outreach
- Begin cold campaigns at low volume
- Follow IP warming schedule
- Monitor metrics closely

---

## Email Authentication (SPF, DKIM, DMARC)

Email authentication proves your emails actually come from you. Without proper authentication, deliverability suffers severely.

### SPF (Sender Policy Framework)

SPF tells receiving servers which IP addresses can send email for your domain.

**How SPF Works**:
1. You publish an SPF record in your DNS
2. Record lists authorized sending IPs/servers
3. Receiving server checks if sending IP is authorized
4. If not authorized, email may be rejected or flagged

**SPF Record Example**:
```
v=spf1 include:_spf.google.com include:sendgrid.net ip4:192.168.1.1 -all
```

This says:
- `v=spf1`: SPF version 1
- `include:_spf.google.com`: Google Workspace IPs are authorized
- `include:sendgrid.net`: SendGrid IPs are authorized
- `ip4:192.168.1.1`: This specific IP is authorized
- `-all`: Reject (hard fail) anything else

**SPF Mechanisms**:
- `include`: Include another domain's SPF
- `ip4`: Authorize IPv4 address/range
- `ip6`: Authorize IPv6 address/range
- `a`: Authorize domain's A record IP
- `mx`: Authorize domain's mail server IPs

**SPF Qualifiers**:
- `+`: Pass (default)
- `-`: Hard fail (reject)
- `~`: Soft fail (mark suspicious)
- `?`: Neutral (no policy)

**SPF Best Practices**:
- Use `-all` (hard fail) once confident in configuration
- Include all legitimate senders
- Avoid too many DNS lookups (limit of 10)
- Test before implementing
- Update when adding new sending services

### DKIM (DomainKeys Identified Mail)

DKIM adds a digital signature to your emails, proving they haven't been tampered with.

**How DKIM Works**:
1. Sending server signs email with private key
2. Signature is added to email headers
3. Public key is published in DNS
4. Receiving server retrieves public key
5. Receiving server verifies signature
6. If verified, email passes DKIM check

**DKIM Record Example**:
```
selector._domainkey.yourdomain.com IN TXT "v=DKIM1; k=rsa; p=MIIBIjANBgkqh..."
```

This publishes your public key at the selector location.

**DKIM Components**:
- **Private Key**: Kept secret on your sending server
- **Public Key**: Published in DNS for verification
- **Selector**: Identifier for this key pair (allows rotation)
- **Signature**: Added to email header

**DKIM Best Practices**:
- Use 2048-bit keys minimum
- Rotate keys periodically
- Sign all outgoing email
- Ensure signing works for all sending services
- Test DKIM before launching

### DMARC (Domain-based Message Authentication, Reporting & Conformance)

DMARC builds on SPF and DKIM, telling receivers what to do when authentication fails.

**How DMARC Works**:
1. You publish a DMARC record specifying your policy
2. Receiving server checks SPF and DKIM
3. If both fail, DMARC policy determines action
4. Receiving server sends reports to you

**DMARC Record Example**:
```
_dmarc.yourdomain.com IN TXT "v=DMARC1; p=quarantine; rua=mailto:dmarc@yourdomain.com; pct=100"
```

This says:
- `v=DMARC1`: DMARC version 1
- `p=quarantine`: Quarantine (spam folder) failures
- `rua=mailto:dmarc@yourdomain.com`: Send aggregate reports here
- `pct=100`: Apply to 100% of email

**DMARC Policies**:
- `p=none`: Monitor only (no action on failures)
- `p=quarantine`: Send failures to spam/junk
- `p=reject`: Reject failures entirely

**DMARC Implementation Path**:
1. Start with `p=none` to monitor
2. Review reports for legitimate failures
3. Fix authentication issues
4. Move to `p=quarantine`
5. Monitor for issues
6. Eventually move to `p=reject`

**DMARC Best Practices**:
- Start with monitoring (`p=none`)
- Use aggregate reports to identify issues
- Gradually strengthen policy
- Align SPF and DKIM (same domain)
- Monitor ongoing

### Implementing Authentication

**Step 1: Audit Current State**
Check existing SPF, DKIM, DMARC records:
- Use tools like MXToolbox, dmarcian, or Google Admin Toolbox
- Identify what's missing or misconfigured

**Step 2: SPF Setup**
1. List all services that send email for your domain
2. Create SPF record including all services
3. Add to DNS as TXT record
4. Verify with checking tools

**Step 3: DKIM Setup**
1. Generate key pair (usually through email provider)
2. Add public key to DNS as TXT record
3. Configure sending server to sign emails
4. Verify signatures with checking tools

**Step 4: DMARC Setup**
1. Start with monitoring policy
2. Add DMARC record to DNS
3. Monitor reports for 2-4 weeks
4. Fix any authentication failures
5. Strengthen policy gradually

**Step 5: Ongoing Monitoring**
- Check authentication regularly
- Review DMARC reports weekly
- Update records when adding new sending services
- Periodically audit all authentication

### Authentication Troubleshooting

**SPF Failures**:
- Sending IP not included in SPF record
- Too many DNS lookups (limit 10)
- Record syntax errors
- Forwarding breaking SPF

**DKIM Failures**:
- Public key not found in DNS
- Key mismatch (wrong key published)
- Email modified in transit
- Selector mismatch

**DMARC Failures**:
- Both SPF and DKIM fail
- Alignment issues (different domains)
- Record syntax errors

---

## Blacklists and How to Avoid Them

Blacklists are databases of IPs and domains known to send spam. Being listed severely impacts deliverability.

### Major Blacklists

**Spamhaus**: Most influential blacklist. Being listed here significantly impacts delivery.
- SBL: Spamhaus Block List (spam sources)
- XBL: Exploits Block List (compromised systems)
- DBL: Domain Block List (spam domains)

**Barracuda**: Used by many corporate email systems.

**SpamCop**: Based on user spam reports.

**SORBS**: Multiple lists for various spam types.

**URIBL/SURBL**: Lists of domains found in spam messages.

### How to Check Blacklist Status

**Manual Checking**:
- MXToolbox Blacklist Check
- MultiRBL.valli.org
- WhatIsMyIPAddress Blacklist Check

**Automated Monitoring**:
- Set up monitoring through your ESP
- Use deliverability tools with blacklist monitoring
- Get alerts when listed

### How Blacklisting Happens

**Spam Complaints**: Too many recipients mark your email as spam.

**Spam Traps**: Sending to email addresses that exist only to catch spammers.

**High Bounce Rates**: Sending to many invalid addresses suggests purchased/scraped lists.

**Content Triggers**: Sending content that matches spam patterns.

**Volume Spikes**: Sudden massive volume increase looks like compromised account.

**Association**: Your IP shared with spammers, or your ESP has reputation issues.

### Spam Traps Explained

Spam traps are email addresses designed to catch spammers:

**Pristine Traps**: Email addresses that have never belonged to real people. They're published in hidden places. If you email them, you got the address by scraping, which means spam.

**Recycled Traps**: Old email addresses that have been abandoned. After bouncing for a period, they're converted to traps. If you email them, your list isn't maintained.

**Typo Traps**: Common typo domains (gmial.com instead of gmail.com). Catching poorly verified lists.

**Avoiding Spam Traps**:
- Never buy or scrape email lists
- Verify all email addresses before sending
- Remove bouncing addresses immediately
- Re-verify old lists
- Use double opt-in for subscriptions
- Monitor bounce rates closely

### Blacklist Removal

If blacklisted:

**Step 1: Identify the Cause**
- What triggered the listing?
- Spam trap hit?
- Complaint spike?
- Compromised account?

**Step 2: Fix the Problem**
- Clean your list
- Fix any security issues
- Review sending practices
- Remove problematic segments

**Step 3: Request Removal**
Most blacklists have delisting procedures:
- Spamhaus: Automated for some listings, manual for severe
- Barracuda: Request form
- SpamCop: Usually auto-expires after fixing

**Step 4: Prevent Recurrence**
- Implement better list hygiene
- Add verification steps
- Monitor metrics more closely

**Delisting Timelines**:
- SpamCop: Usually 24-48 hours after complaints stop
- Spamhaus: Days to weeks depending on severity
- Barracuda: 24-72 hours after request
- Some lists: May take weeks or require multiple requests

---

## Inbox Placement vs. Delivery Rate

Understanding the difference between delivery and inbox placement is crucial for measuring deliverability.

### Definitions

**Delivery Rate**: Percentage of emails accepted by receiving servers.
```
Delivery Rate = (Sent - Bounced) / Sent × 100%
```

**Inbox Placement Rate**: Percentage of delivered emails that reach the inbox (not spam).
```
Inbox Placement Rate = Inbox Arrivals / Delivered Emails × 100%
```

### Why Both Matter

High delivery rate with low inbox placement means emails are accepted but filtered to spam. This is often worse than bouncing because:
- You don't know they went to spam
- Metrics look artificially good
- You keep sending to people who never see you
- Your reputation degrades silently

### Measuring Inbox Placement

**Seed Testing**: Send emails to accounts you control across different MBPs. Check where they land.

**Deliverability Tools**:
- GlockApps
- Mail-Tester
- Inbox Placement tools from major ESPs
- Google Postmaster Tools

**Indirect Indicators**:
- Open rates by domain (Gmail opens vs. Outlook)
- Engagement pattern differences
- Reply rates by domain

### Inbox vs. Tabs

Even reaching the inbox, emails may land in tabs:

**Primary**: Main inbox, highest visibility
**Promotions**: Marketing emails, lower visibility
**Updates**: Notifications, moderate visibility
**Social**: Social network notifications
**Forums**: Mailing lists, group emails

For cold email, Primary is the goal. Promotions significantly reduces engagement.

**Avoiding Promotions Tab**:
- Reduce promotional language
- Minimize HTML formatting
- Avoid images
- Keep it conversational
- Remove tracking pixels
- Limit links
- Write like a human, not a marketer

---

## Advanced Deliverability Factors

Beyond the basics, several advanced factors affect deliverability.

### Sending Patterns

**Time of Day**: Sending at normal business hours looks legitimate.

**Day of Week**: Weekend sending can look suspicious for B2B.

**Volume Patterns**: Consistent volume is better than spikes.

**Geographic Patterns**: Sudden sending to new regions looks suspicious.

### Technical Factors

**Reverse DNS (PTR Record)**: Your sending IP should have a PTR record pointing to a valid domain.

**HELO/EHLO Identity**: Server greeting should match your domain.

**MX Records**: Domain should have valid mail exchange records.

**TLS Encryption**: Send over encrypted connections (TLS).

### Content Factors

**Text-to-HTML Ratio**: Heavy HTML with little text is suspicious.

**Image-to-Text Ratio**: Too many images with little text triggers filters.

**Link Quality**: Links to reputable domains help; suspicious links hurt.

**Personalization Tokens**: Well-implemented personalization helps; broken tokens hurt.

### List Quality Factors

**List Age**: Old, unengaged lists hurt reputation.

**Engagement History**: Sending to non-engagers damages reputation.

**Acquisition Method**: Purchased lists almost always cause problems.

**Verification Status**: Unverified lists have higher bounce rates.

### Infrastructure Factors

**Email Service Provider**: Your ESP's overall reputation affects you.

**IP Pool**: Shared IPs carry collective reputation.

**Server Configuration**: Misconfigured servers cause deliverability issues.

---

## Monitoring and Testing

Continuous monitoring and testing are essential for maintaining deliverability.

### Key Metrics to Monitor

**Daily Monitoring**:
- Delivery rate
- Bounce rate (hard and soft)
- Open rate (by domain)
- Click rate
- Spam complaint rate
- Unsubscribe rate

**Weekly Monitoring**:
- Inbox placement (via seed testing)
- Blacklist status
- Domain reputation (Postmaster tools)
- IP reputation
- DMARC reports

**Monthly Analysis**:
- Trend analysis of all metrics
- List health assessment
- Authentication audit
- Competitor deliverability comparison

### Testing Framework

**Pre-Send Testing**:
1. Send to seed accounts
2. Check inbox/spam placement
3. Verify authentication passes
4. Review with spam scoring tools
5. Check links and images load

**In-Flight Testing**:
1. Monitor real-time bounce rates
2. Watch for spam complaints
3. Track opens by domain
4. Check Postmaster tools

**Post-Send Analysis**:
1. Compare results to benchmarks
2. Identify problem domains
3. Investigate anomalies
4. Document learnings

### Tools for Monitoring

**Google Postmaster Tools** (Free):
- Domain reputation
- IP reputation
- Spam rate
- Authentication success

**Microsoft SNDS** (Free):
- IP status
- Complaint data
- Sample messages

**Deliverability Testing Tools**:
- GlockApps
- Mail-Tester
- Inbox Placement by Validity

**ESP Dashboard**:
- Most ESPs provide delivery metrics
- Use their built-in monitoring

**DMARC Reporting Services**:
- Dmarcian
- Postmark DMARC
- Valimail

---

## Deliverability Recovery

When deliverability tanks, here's how to recover.

### Diagnosing the Problem

**Step 1: Identify the Scope**
- Which MBPs are affected?
- Which sending domains/IPs?
- When did it start?
- What changed around that time?

**Step 2: Check the Obvious**
- Blacklist status
- Authentication failures
- Bounce rate spikes
- Complaint rate spikes

**Step 3: Investigate Deeper**
- Review sent content for spam triggers
- Audit list sources
- Check for compromised accounts
- Review ESP status

### Recovery Strategies

**Minor Deliverability Decline**:
1. Pause new cold outreach
2. Clean list aggressively
3. Focus on engaged recipients
4. Reduce volume
5. Improve content quality
6. Monitor for improvement

**Moderate Deliverability Problems**:
1. Stop sending from affected domain/IP
2. Request blacklist removal
3. Review and fix authentication
4. Clean list thoroughly
5. Investigate root cause
6. Develop new domain/IP
7. Warm new infrastructure
8. Resume gradually

**Severe Deliverability Crisis**:
1. Stop all sending immediately
2. Assume domain/IP is burned
3. Prepare new infrastructure
4. Completely rebuild lists
5. Review all practices
6. Implement stronger safeguards
7. Start fresh with warming

### Blacklist-Specific Recovery

**Spamhaus Recovery**:
1. Identify the specific list (SBL, XBL, DBL)
2. Determine the cause
3. Fix the underlying issue
4. Submit removal request
5. Wait for review (can take days)
6. If denied, appeal with evidence of fixes

**Other Blacklist Recovery**:
1. Follow blacklist-specific procedures
2. Document remediation steps
3. Request removal
4. Monitor for recurrence

### Reputation Rebuilding

After fixing issues, rebuild reputation:

1. **Start with transactional email**: Send to existing customers who engage
2. **Gradually add marketing**: Introduce promotional content slowly
3. **Last add cold outreach**: Only after reputation stabilizes
4. **Monitor closely**: Watch metrics at every stage
5. **Move slowly**: Impatience re-damages reputation

---

## Deliverability Checklist

### Infrastructure Setup Checklist

**Domain Configuration**:
- [ ] Domain purchased and aged (2+ weeks)
- [ ] SPF record configured
- [ ] DKIM keys generated and published
- [ ] DMARC policy implemented (start with p=none)
- [ ] MX records configured
- [ ] PTR (reverse DNS) configured
- [ ] Website exists on domain

**Mailbox Configuration**:
- [ ] Mailboxes created with proper naming
- [ ] Signature configured
- [ ] Reply-to address set
- [ ] Profile picture/avatar added
- [ ] Connected to sending tool

**Authentication Verification**:
- [ ] SPF passing (test with mail-tester.com)
- [ ] DKIM passing
- [ ] DMARC passing
- [ ] No authentication warnings

### Pre-Campaign Checklist

**List Quality**:
- [ ] List source is documented
- [ ] Emails verified with validation service
- [ ] Bounce rate expected < 2%
- [ ] No purchased/scraped emails without verification
- [ ] List segmented by engagement level

**Content Quality**:
- [ ] Subject line tested for spam triggers
- [ ] Body copy reviewed for spam language
- [ ] Links tested and working
- [ ] No URL shorteners
- [ ] Unsubscribe mechanism works
- [ ] Physical address included
- [ ] Plain text version available

**Technical Setup**:
- [ ] Sending limits configured correctly
- [ ] Sending schedule set (appropriate hours)
- [ ] Suppression list synced
- [ ] Tracking configured correctly
- [ ] Test email sent to seed accounts

### Ongoing Monitoring Checklist

**Daily**:
- [ ] Check bounce rates
- [ ] Review complaint rates
- [ ] Monitor open rates by domain
- [ ] Process opt-outs

**Weekly**:
- [ ] Check blacklist status
- [ ] Review Postmaster Tools
- [ ] Analyze engagement trends
- [ ] Send test to seed accounts

**Monthly**:
- [ ] Full deliverability audit
- [ ] Review DMARC reports
- [ ] Clean inactive contacts
- [ ] Authentication audit

### Recovery Checklist

**When Metrics Drop**:
- [ ] Identify affected scope
- [ ] Check blacklist status
- [ ] Review authentication
- [ ] Audit recent list additions
- [ ] Review content changes
- [ ] Reduce volume
- [ ] Focus on engaged recipients
- [ ] Monitor for improvement

---

## Summary: The Deliverability Mindset

Deliverability isn't a one-time setup—it's an ongoing practice. Maintain the mindset that:

**Everything Affects Reputation**: Every email sent, every list choice, every content decision impacts your ability to reach the inbox.

**Prevention Beats Recovery**: It's much easier to maintain good deliverability than to recover from bad deliverability.

**Metrics Are Early Warnings**: Don't ignore declining metrics. Small problems become big problems.

**Quality Over Quantity**: A smaller, engaged list with good deliverability outperforms a large list landing in spam.

**Stay Current**: Email filtering evolves constantly. Keep learning and adapting.

---

*Deliverability is the foundation. Master these technical elements before focusing on copy and strategy.*
