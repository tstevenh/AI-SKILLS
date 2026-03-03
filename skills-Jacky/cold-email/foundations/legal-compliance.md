# Legal & Compliance for Cold Email

Cold email operates in a complex legal landscape. Understanding and complying with regulations isn't just about avoiding fines—it's about building sustainable practices that protect your business and respect recipients. This comprehensive guide covers every major regulation and how to stay compliant.

## Table of Contents

1. [Why Compliance Matters](#why-compliance-matters)
2. [CAN-SPAM Act (United States)](#can-spam-act-united-states)
3. [GDPR (European Union)](#gdpr-european-union)
4. [CASL (Canada)](#casl-canada)
5. [PECR (United Kingdom)](#pecr-united-kingdom)
6. [Australia's Spam Act](#australias-spam-act)
7. [Other Country Regulations](#other-country-regulations)
8. [Industry-Specific Regulations](#industry-specific-regulations)
9. [Penalties and Enforcement](#penalties-and-enforcement)
10. [Safe Harbor Practices](#safe-harbor-practices)
11. [Building a Compliance Framework](#building-a-compliance-framework)
12. [Compliance Checklist](#compliance-checklist)

---

## Why Compliance Matters

### Beyond Legal Risk

Compliance isn't just about avoiding lawsuits and fines. It impacts:

**Deliverability**: Email providers track spam complaints and compliance violations. Non-compliant practices tank your sender reputation, meaning even compliant emails stop reaching inboxes.

**Brand Reputation**: One viral complaint about spammy practices can damage your brand more than any fine. In B2B, your prospects talk to each other.

**Sustainable Results**: Compliant practices are sustainable. Spammy practices work until they don't—then you've burned your domains, your lists, and your reputation.

**Ethical Obligation**: Beyond business considerations, recipients deserve respect. Compliance frameworks codify that respect.

### The Compliance Hierarchy

Think of compliance as a hierarchy:

1. **Legal Minimum**: What the law requires
2. **Best Practice**: What industry standards suggest
3. **Excellence**: What builds trust and long-term relationships

This guide covers all three levels for each regulation.

---

## CAN-SPAM Act (United States)

The Controlling the Assault of Non-Solicited Pornography And Marketing Act of 2003 (CAN-SPAM) is the primary US regulation governing commercial email.

### Who It Applies To

CAN-SPAM applies to "commercial electronic mail messages"—any email whose primary purpose is promoting or advertising a commercial product or service.

**Important**: CAN-SPAM applies based on the recipient's location. If you're sending from anywhere in the world to US recipients, CAN-SPAM applies.

### What CAN-SPAM Requires

#### 1. Accurate Header Information

Your "From," "To," "Reply-To," and routing information must be accurate and identify the person or business who initiated the message.

**What this means**:
- The "From" name and address must accurately identify who sent the email
- You can't spoof sender information
- Domain names and email addresses must identify who you actually are

**Example of violation**:
- From: "Support Team" <support@their-company.com> (impersonating another company)

**Compliant example**:
- From: "John Smith - Acme Corp" <john@acmecorp.com>

#### 2. Accurate Subject Lines

Subject lines cannot be deceptive. They must accurately reflect the content of the message.

**What this means**:
- Subject lines must not mislead recipients about the email's contents
- "Re:" or "Fwd:" is deceptive if the email isn't actually a reply or forward
- "Urgent" or "Important" is deceptive if the content isn't urgent/important to the recipient

**Example of violation**:
- Subject: "Your order has shipped" (when there's no order)
- Subject: "Re: Our meeting tomorrow" (when there was no prior conversation)

**Compliant example**:
- Subject: "Question about your content strategy"

#### 3. Identification as Advertisement

The message must include clear and conspicuous identification that it's an advertisement.

**What this means**:
- You must disclose that your email is promotional
- The disclosure must be clear, not hidden in fine print
- There's flexibility in how you disclose

**Practical application**:
Many B2B cold emails are clearly promotional in nature, making explicit disclosure less critical. However, best practice is to include language like "This is a promotional message from [Company]" in your email footer.

**Note**: The FTC has stated that if the commercial nature of the email is obvious, additional disclosure may not be required. Most B2B cold emails fall into this category.

#### 4. Physical Postal Address

Every commercial email must include a valid physical postal address.

**What counts**:
- Current street address
- PO Box registered with USPS
- Private mailbox registered with a commercial mail receiving agency

**What doesn't count**:
- Fake addresses
- Addresses that can't receive mail
- Email-only contact information

**Practical application**:
Include your physical address in every email footer. This is typically:
```
Acme Corp
123 Main Street, Suite 100
San Francisco, CA 94105
```

#### 5. Opt-Out Mechanism

Every email must include a clear and conspicuous explanation of how recipients can opt out of future messages.

**Requirements**:
- Opt-out must be clear (visible, understandable)
- Must be easy to execute (can't require excessive steps)
- Must be free (no charges to unsubscribe)
- Must work for at least 30 days after sending
- Can't require personal information beyond email address to opt out
- Can't make them log in to unsubscribe

**Standard approach**:
Include an unsubscribe link in your email footer:
```
Don't want to receive these emails? Click here to unsubscribe.
```

**For cold email specifically**:
Some cold email tools don't have traditional unsubscribe links (since prospects aren't on a "list"). In this case, include clear language like:
"If you'd prefer I don't reach out again, just reply and let me know."

#### 6. Honor Opt-Out Requests

You must honor opt-out requests within 10 business days.

**Requirements**:
- Process opt-outs within 10 business days
- Cannot send any promotional email to that address after opting out
- Cannot sell or transfer the email address to anyone else
- Cannot require them to provide any information beyond email address
- Cannot charge any fee

**Practical application**:
- Set up systems to automatically process unsubscribes
- Maintain a suppression list that's checked before every send
- If someone replies "unsubscribe," treat it as an opt-out request

#### 7. Monitor Third Parties

If you hire another company to handle email marketing, you can't contract away your legal responsibility.

**What this means**:
- You're responsible for your contractors' compliance
- "I hired an agency" is not a legal defense
- Both the company whose product is promoted AND the company that sends the message can be held liable

### What CAN-SPAM Does NOT Require

Understanding what CAN-SPAM doesn't require is equally important:

**Prior consent is NOT required**: Unlike GDPR and CASL, CAN-SPAM does not require opt-in consent before sending commercial email. You can legally send cold email to US recipients.

**Prior relationship is NOT required**: You don't need an existing relationship to send commercial email.

**Double opt-in is NOT required**: Single opt-out (unsubscribe) mechanism is sufficient.

### CAN-SPAM Best Practices (Beyond Legal Minimum)

While CAN-SPAM sets a relatively low bar, best practices go further:

**Best Practice 1: Easy Opt-Out**
Don't just meet the legal requirement—make opting out trivial. A simple reply should suffice, no link-clicking required.

**Best Practice 2: Immediate Honor**
Process opt-outs within hours, not 10 days. The 10-day window is a maximum, not a goal.

**Best Practice 3: List Hygiene**
Proactively remove bounces and complainers, not just opt-outs.

**Best Practice 4: Respectful Volume**
Just because you can legally email someone doesn't mean you should. Limit sequence length and respect non-response.

---

## GDPR (European Union)

The General Data Protection Regulation is the EU's comprehensive data protection law, with significant implications for cold email.

### Who It Applies To

GDPR applies to:
- Organizations established in the EU, regardless of where processing occurs
- Organizations outside the EU that offer goods/services to EU residents
- Organizations outside the EU that monitor the behavior of EU residents

**For cold email**: If you're sending email to people located in the EU (even if you're based elsewhere), GDPR likely applies to your activities.

### Core GDPR Principles for Email

#### 1. Lawful Basis for Processing

Under GDPR, you need a "lawful basis" to process personal data (which includes email addresses). For cold email, the relevant bases are:

**Consent**: The individual has given clear consent for you to process their data for a specific purpose.

**Legitimate Interest**: Processing is necessary for your legitimate business interests, unless outweighed by the individual's interests, rights, or freedoms.

#### The Legitimate Interest Path for B2B Cold Email

B2B cold email can be lawful under GDPR's legitimate interest basis, but it requires careful assessment:

**The Three-Part Test**:

1. **Purpose Test**: Is there a legitimate interest?
   - Yes, promoting products/services to businesses is a legitimate commercial interest

2. **Necessity Test**: Is the processing necessary for that purpose?
   - Is email the only/best way to reach these prospects?
   - Could you achieve the same goal with less data processing?

3. **Balancing Test**: Do individual rights override your interest?
   - What's the nature of your relationship (if any)?
   - What data are you processing, and is it sensitive?
   - What are reasonable expectations of the individual?
   - What's the impact on the individual?
   - Are safeguards in place?

**When Legitimate Interest Likely Applies**:
- B2B emails to corporate addresses
- Emails relevant to the recipient's professional role
- Appropriate safeguards (easy opt-out, data minimization)
- Data obtained from legitimate sources
- Reasonable privacy expectations were considered

**When Legitimate Interest Likely Doesn't Apply**:
- Emails to personal addresses without consent
- Mass emails with no personalization/relevance
- No easy opt-out mechanism
- Excessive data collection beyond what's needed
- Data obtained through questionable means

#### 2. Transparency Requirements

Even with legitimate interest, you must be transparent:

**What you must communicate**:
- Who you are (identity of data controller)
- How you obtained their data
- What you're using their data for
- Their rights under GDPR
- How they can object to processing

**Practical implementation**:
Include a privacy-related footer or link in cold emails explaining:
- Your company and contact details
- Where you found their information
- Link to your privacy policy
- How to opt out

**Example footer for GDPR compliance**:
```
You're receiving this because we found your contact info on [source] and believe our service may be relevant to your role at [Company]. 

Read our privacy policy: [link]
To stop receiving emails: [unsubscribe] or simply reply "unsubscribe"
```

#### 3. Right to Object

Individuals have the right to object to processing based on legitimate interest at any time.

**What this means**:
- You must honor objections immediately
- You must make objecting easy
- You can't challenge their reason for objecting

**Practical implementation**:
- Include clear opt-out in every email
- Process objections within 24-48 hours
- Maintain robust suppression lists

#### 4. Data Subject Rights

GDPR grants individuals several rights you must be prepared to handle:

**Right of Access**: Individuals can request all personal data you hold about them.

**Right to Rectification**: Individuals can request correction of inaccurate data.

**Right to Erasure** ("Right to be Forgotten"): Individuals can request deletion of their data.

**Right to Restrict Processing**: Individuals can request you stop using their data.

**Right to Data Portability**: Individuals can request their data in a portable format.

**Practical implementation**:
- Have processes to handle data subject requests
- Be prepared to provide, correct, or delete data within 30 days
- Train your team on recognizing and routing these requests

### GDPR Documentation Requirements

GDPR requires documentation of your compliance efforts:

**Legitimate Interest Assessment (LIA)**: Document your analysis of why legitimate interest applies to your cold email activities.

**Records of Processing**: Maintain records of what personal data you process, for what purpose, and with what safeguards.

**Data Protection Impact Assessment**: For high-risk processing, conduct formal risk assessments.

### Consent vs. Legitimate Interest: A Comparison

| Aspect | Consent | Legitimate Interest |
|--------|---------|---------------------|
| Prior action required | Yes, explicit opt-in | No |
| Can be withdrawn | Yes, easily | Yes, through objection |
| Documentation required | Proof of consent | LIA documentation |
| Scope | Specific purpose stated | Stated legitimate purpose |
| Best for | B2C, newsletters | B2B cold outreach |
| Risk level | Lower (if valid consent) | Higher (if poorly documented) |

### ePrivacy Directive Considerations

The ePrivacy Directive (soon to be replaced by the ePrivacy Regulation) adds another layer for electronic communications:

**Article 13**: Member states may restrict unsolicited electronic communications to those who have given prior consent, OR may require opt-out mechanisms.

**In practice**: Different EU countries have implemented this differently. Some allow B2B cold email with opt-out (like the UK pre-Brexit), while others require prior consent (like Germany).

**Recommendation**: For EU-wide campaigns, obtain consent when possible, and at minimum ensure robust legitimate interest documentation and easy opt-out.

### GDPR Penalties

GDPR enforcement is serious:

**Administrative Fines**:
- Up to €20 million, or 4% of annual global turnover (whichever is higher)
- Lower tier: Up to €10 million or 2% of turnover

**Individual Lawsuits**: Individuals can sue for damages from GDPR violations.

**Reputational Damage**: GDPR violations become public and can damage brand significantly.

---

## CASL (Canada)

Canada's Anti-Spam Legislation is one of the strictest email regulations globally, with significant requirements for consent.

### Who It Applies To

CASL applies to "commercial electronic messages" (CEMs) sent to, from, or within Canada. If either the sender OR the recipient is in Canada, CASL likely applies.

### The Consent Requirement

CASL's fundamental requirement is **consent before sending**. Unlike CAN-SPAM, you cannot simply send cold email and provide opt-out—you need consent first.

#### Express Consent

The gold standard under CASL. Express consent requires:

1. **Clear request**: You asked clearly for permission to send emails
2. **Specific purpose**: You stated what kind of emails you'd send
3. **Affirmative action**: They took action to consent (not just failed to opt-out)
4. **Your identity disclosed**: You identified yourself and provided contact info
5. **Withdrawal information**: You explained how they could unsubscribe

**How to get express consent**:
- Website signup forms
- Trade show lead capture (with clear disclosure)
- Verbal consent (documented)
- Written consent

**Important**: Express consent does not expire (unless you stop sending for 2+ years or they withdraw consent).

#### Implied Consent

CASL recognizes limited circumstances where consent can be implied:

**Existing Business Relationship**: Consent is implied for 2 years after:
- Purchase of products/services
- Written contract between parties
- Inquiry or application (6 months only)

**Existing Non-Business Relationship**: Consent is implied for 2 years after:
- Donation to registered charity
- Volunteer work
- Membership in organization

**Conspicuously Published Address**: Consent MAY be implied if:
- Email address is conspicuously published (website, business card)
- No statement prohibiting unsolicited email
- Message is relevant to recipient's role or function
- Recipient is in Canada

**Referral**: Consent is implied for a single message if:
- You're referred by someone with consent relationship
- You name the referrer in the message
- Referrer has actual relationship with recipient

### CASL Requirements for All CEMs

Regardless of consent type, every CEM must include:

#### 1. Identification

- Your name (individual or business)
- Name of person on whose behalf you're sending (if applicable)
- Physical mailing address
- Website address, email address, or phone number

#### 2. Unsubscribe Mechanism

- Clear and prominently displayed
- Functional for at least 60 days after sending
- Free to use
- Quick to execute
- Honored within 10 business days

### Cold Email Under CASL

Given CASL's consent requirements, pure cold email to Canadian recipients is challenging but not impossible:

**Scenario 1: Conspicuously Published Address**
If their business email is on their company website with no prohibition on unsolicited email, AND your message is relevant to their professional role, you may have implied consent.

This is the most common path for B2B cold email under CASL, but it requires:
- The email address is clearly displayed on a website/directory
- There's no "do not email" statement
- Your message relates to their business function

**Scenario 2: Referral**
If someone with a relationship to the prospect refers you, you can send ONE message that names the referrer.

**Scenario 3: Express Consent First**
Some senders request consent before sending commercial content:
"Hi [Name], I'm reaching out to ask if you'd be interested in receiving information about [topic]. If yes, please reply and I'll share some resources that might be relevant to your work at [Company]."

This approach is safer but less effective for pure cold outreach.

### CASL Penalties

CASL has among the highest penalties for email violations:

**Administrative Monetary Penalties (AMPs)**:
- Up to $10 million per violation for businesses
- Up to $1 million per violation for individuals

**Private Right of Action** (currently not in force):
- Individuals can sue for damages
- Up to $200 per violation (max $1 million per day)

**Note**: The private right of action has been suspended indefinitely, but AMPs remain in effect.

### CASL Best Practices

**Best Practice 1: Get Express Consent When Possible**
Express consent provides the most protection. Build consent into your lead generation processes.

**Best Practice 2: Document Everything**
Keep records of:
- How you obtained each email address
- What consent exists (express or implied)
- When implied consent relationships started
- When express consent was granted

**Best Practice 3: Be Conservative with Implied Consent**
The "conspicuously published" exception is narrower than many assume. When in doubt, don't send.

**Best Practice 4: Check the Source of Data**
If you bought or scraped a list, you likely don't have valid consent for Canadian addresses.

---

## PECR (United Kingdom)

The Privacy and Electronic Communications Regulations govern electronic marketing in the UK, working alongside UK GDPR post-Brexit.

### Who It Applies To

PECR applies to electronic marketing sent to or from the UK, including:
- Email marketing
- SMS marketing
- Phone marketing
- Fax marketing
- Cookies and tracking

### B2B Email Rules Under PECR

PECR makes an important distinction between B2C and B2B email:

**B2C Email**: Requires prior consent (opt-in)

**B2B Email**: Can be sent without prior consent IF:
- Sent to corporate email addresses (not personal addresses)
- Identifies the sender
- Includes valid opt-out mechanism

This makes the UK relatively favorable for B2B cold email compared to stricter jurisdictions.

### What Constitutes a Corporate vs. Personal Address

**Corporate address examples**:
- john.smith@company.com
- sales@company.com
- info@acme.co.uk

**Personal address examples**:
- johnsmith@gmail.com
- john.smith@btinternet.com

**Edge cases** (treat as personal to be safe):
- john@smith.com (personal domain)
- john@johnsmithconsulting.com (sole trader)

### PECR Requirements for B2B Email

1. **Sender Identification**: Clearly identify who you are
2. **Opt-Out Mechanism**: Provide easy way to refuse future emails
3. **No Disguise**: Don't disguise or conceal your identity

### UK GDPR Interaction

PECR works alongside UK GDPR. Even if PECR allows sending without consent, you still need:
- Valid lawful basis under UK GDPR (typically legitimate interest for B2B)
- Compliance with transparency requirements
- Honor data subject rights

### Post-Brexit Considerations

Since Brexit, the UK has maintained substantially similar rules to EU GDPR through UK GDPR. However, the UK is reviewing its data protection framework, and changes may emerge. Monitor developments and maintain practices compliant with both EU and UK standards.

---

## Australia's Spam Act

The Spam Act 2003 regulates commercial electronic messages in Australia.

### Who It Applies To

The Spam Act applies to commercial electronic messages with an "Australian link":
- Sent from Australia
- Sent to an address accessed in Australia
- Sent by an organization with Australian connection

### Key Requirements

#### 1. Consent

Like CASL, Australia requires consent before sending commercial email:

**Express consent**: Recipient clearly agreed to receive emails

**Inferred consent**: Consent can be inferred from:
- Existing business relationship (no time limit specified)
- Conspicuously published address (if message relevant to business)
- Reasonable expectation they would consent

The "conspicuously published" exception works similarly to CASL, enabling some B2B cold outreach.

#### 2. Identification

Messages must include:
- Accurate sender information
- Contact details (physical address, phone, or email)

#### 3. Functional Unsubscribe

Messages must include:
- Clear unsubscribe facility
- Functional for at least 30 days
- Honored within 5 business days

### Australian Penalties

The Australian Communications and Media Authority (ACMA) can impose:
- Formal warnings
- Infringement notices
- Civil penalties up to $2.22 million per day for businesses
- Injunctions

---

## Other Country Regulations

### Germany (Gesetz gegen den unlauteren Wettbewerb - UWG)

Germany has strict rules beyond GDPR:
- Generally requires prior consent for advertising emails
- B2B exception exists but is narrow
- High enforcement risk from competitors (not just regulators)

**Recommendation**: Obtain express consent for German contacts when possible.

### France (LCEN)

French law requires prior consent for commercial email marketing, with limited exceptions for existing customers.

**Recommendation**: Treat France as consent-required for cold outreach.

### Italy

Italian law requires consent for marketing emails, with B2B exceptions for:
- Emails to publicly available business addresses
- Content relevant to recipient's professional activity

**Recommendation**: Similar to CASL "conspicuously published" standard.

### Spain (LSSI)

Spain requires consent for commercial communications, with narrow exceptions.

**Recommendation**: Obtain consent when possible.

### Netherlands

The Netherlands follows EU framework with GDPR + ePrivacy. Some B2B leeway exists but requires legitimate interest documentation.

### Brazil (LGPD)

Brazil's General Data Protection Law (LGPD) is modeled on GDPR:
- Requires lawful basis for processing
- Legitimate interest can apply to B2B
- Strong consent requirements for certain data

**Recommendation**: Apply GDPR-like practices.

### Japan (Act on Regulation of Transmission of Specified Electronic Mail)

Japan requires:
- Prior consent or existing relationship
- Sender identification
- Unsubscribe mechanism

Cold email is restricted without consent.

### Singapore (Spam Control Act)

Singapore requires:
- Valid consent or existing relationship
- Sender identification
- Functional unsubscribe

Similar framework to other consent-based jurisdictions.

### South Korea (Act on Promotion of Information and Communications Network Utilization and Information Protection)

Korea requires:
- Express consent before sending commercial email
- Clear identification
- Easy opt-out

One of the stricter regimes globally.

### India

India's Information Technology Act contains provisions on spam, but enforcement is limited. New data protection legislation (Digital Personal Data Protection Act) is evolving.

**Recommendation**: Follow global best practices.

### Summary by Region

| Region | Cold Email Allowed | Key Requirement |
|--------|-------------------|-----------------|
| United States | Yes | Opt-out mechanism |
| Canada | Limited | Consent or conspicuously published exception |
| United Kingdom | B2B Yes | Legitimate interest + opt-out |
| EU (General) | Limited | GDPR legitimate interest + country rules |
| Germany | Restricted | Generally requires consent |
| France | Restricted | Generally requires consent |
| Australia | Limited | Consent or business relationship/published address |
| Japan | Restricted | Requires consent |
| South Korea | Restricted | Requires express consent |
| Brazil | Limited | LGPD legitimate interest |

---

## Industry-Specific Regulations

### HIPAA (Healthcare - US)

The Health Insurance Portability and Accountability Act restricts use of protected health information (PHI).

**Impact on cold email**:
- Cannot reference individual health conditions in outreach
- Cannot use patient lists for marketing without authorization
- Healthcare organizations must follow PHI rules in all communications

### FINRA (Financial Services - US)

Financial Industry Regulatory Authority rules affect financial services email:
- Recordkeeping requirements for all communications
- Supervision requirements
- Fair and balanced communications
- No misleading statements

### TCPA (Telecommunications - US)

The Telephone Consumer Protection Act primarily covers calls/texts but has email implications when emails include offers to call.

### PCI DSS (Payment Card Industry)

If handling payment card data, PCI DSS requirements affect data security in email systems.

### SOC 2

For SaaS companies, SOC 2 compliance may affect how customer data (including prospect data) is handled.

---

## Penalties and Enforcement

### Enforcement Patterns

Understanding how regulations are enforced helps prioritize compliance:

**US (CAN-SPAM)**:
- FTC enforcement for major violations
- Primarily targets egregious spammers
- Class action lawsuits possible
- ISP lawsuits (rare but possible)

**EU (GDPR)**:
- Data Protection Authorities in each country
- Increasing enforcement activity
- Large fines for major violations
- Individual complaints can trigger investigation

**Canada (CASL)**:
- CRTC enforcement
- Primarily focused on major violators
- Significant fines when enforced
- Private right of action suspended

**UK (PECR/UK GDPR)**:
- ICO enforcement
- Focus on repeat offenders and complaints
- Fines possible but smaller than GDPR

**Australia**:
- ACMA enforcement
- Active investigation of complaints
- Significant penalties possible

### Fine Examples

**GDPR Notable Fines**:
- Amazon: €746 million (2021) - data processing violations
- WhatsApp: €225 million (2021) - transparency violations
- Google: €50 million (2019) - consent/transparency
- H&M: €35 million (2020) - employee data processing

**CAN-SPAM**:
- Odyssey Tech: $1.5 million - deceptive practices
- World Patent Marketing: $26 million - multiple violations
- ValueClick: $2.9 million - deceptive headers

**CASL**:
- Compu-Finder: $1.1 million - sending without consent
- Porter Airlines: $150,000 - inadequate consent
- Rogers Media: $200,000 - consent violations

### Individual Liability

In most jurisdictions, individuals involved in violations can be personally liable:
- Directors and officers can face personal fines
- Employees who knowingly violate can be prosecuted
- "I was just following orders" is not a defense

### Reputation Damage

Beyond fines, compliance violations cause:
- Public relations disasters
- Loss of customer trust
- Difficulty in future marketing
- Challenges with email deliverability
- Insurance and partnership complications

---

## Safe Harbor Practices

Safe harbor practices protect you even when regulations are ambiguous or evolving.

### Universal Safe Harbor Practices

These practices provide protection regardless of jurisdiction:

**1. Maintain Consent Records**
Document how, when, and what consent was obtained for every contact.

**2. Provide Easy Opt-Out**
Make unsubscribing trivial—one click, one reply, no barriers.

**3. Honor Opt-Outs Immediately**
Process opt-outs within 24 hours, not the legal maximum.

**4. Include Physical Address**
Every email includes a valid physical address.

**5. Identify Yourself Clearly**
No deceptive sender names or subject lines.

**6. Match Message to Consent**
Only send what you said you'd send when obtaining consent.

**7. Maintain Suppression Lists**
Robust suppression lists checked before every send.

**8. Verify List Sources**
Know where your data comes from and ensure it was collected properly.

**9. Conduct Regular Audits**
Review practices, suppression lists, and procedures regularly.

**10. Train Your Team**
Everyone involved in email understands compliance requirements.

### Documentation Practices

**Consent Documentation**:
For each contact, record:
- Email address
- Consent type (express or implied)
- Source of consent/relationship
- Date consent obtained
- What was consented to
- Evidence of consent (form snapshot, recording, etc.)

**Processing Documentation** (GDPR):
- Lawful basis for processing
- Legitimate interest assessment (if applicable)
- Data minimization rationale
- Retention schedule

**Opt-Out Documentation**:
- Date of opt-out request
- Channel of request (reply, unsubscribe link, etc.)
- Date processed
- Confirmation sent (if applicable)

### List Source Verification

Before using any email list, verify:

**If purchased**:
- How was consent obtained?
- What were recipients told about data sharing?
- Is consent transferable?
- Documentation available?

**If scraped**:
- Was the source public and conspicuous?
- Is the email relevant to their public role?
- Is there any prohibition on contact?

**If from partners**:
- What consent exists?
- Does consent cover sharing?
- Is the partner reputable?

**General rule**: If you can't verify consent/source, don't use the list.

### Jurisdiction-Specific Safe Harbor

**For US recipients**:
- CAN-SPAM compliance is sufficient legal minimum
- Add privacy notice for California residents (CCPA)

**For EU recipients**:
- Document legitimate interest thoroughly
- Include GDPR-compliant transparency
- Be prepared for data subject requests

**For Canadian recipients**:
- Verify consent exists (express or implied)
- Use conspicuously published exception carefully
- Document basis for each contact

**For UK recipients**:
- Confirm corporate (not personal) email
- Document legitimate interest
- Provide clear opt-out

**For uncertain jurisdiction**:
- Apply the strictest applicable standard
- When in doubt, obtain express consent

---

## Building a Compliance Framework

### Compliance Infrastructure

**1. Data Governance**
- Define data retention policies
- Implement data minimization
- Create data subject request procedures
- Establish data security measures

**2. Technical Implementation**
- Automated suppression list management
- Consent tracking systems
- Unsubscribe processing automation
- Audit logging for all email activities

**3. Process Documentation**
- Documented procedures for all email activities
- Training materials for team members
- Audit schedules and checklists
- Incident response procedures

**4. Legal Review**
- Regular review by legal counsel
- Updates when regulations change
- Contract review for vendors/partners
- DPA (Data Processing Agreement) management

### Compliance Workflow

**Before Campaign**:
1. Verify list source and consent
2. Confirm jurisdiction requirements
3. Review email content for compliance
4. Check suppression lists
5. Document campaign details

**During Campaign**:
1. Monitor bounce and complaint rates
2. Process opt-outs immediately
3. Log all send activity
4. Watch for legal notices/complaints

**After Campaign**:
1. Update consent/suppression records
2. Document results
3. Review any complaints
4. Archive campaign records

### Vendor Compliance

When using third-party tools:

**Data Processing Agreements**:
Ensure DPAs are in place with all vendors handling personal data.

**Sub-processor Lists**:
Know who your vendors share data with.

**Security Measures**:
Verify vendors have appropriate security certifications.

**Data Location**:
Understand where data is processed and stored.

**Deletion Capabilities**:
Confirm vendors can delete data when required.

---

## Compliance Checklist

### Pre-Send Checklist

**List Compliance**:
- [ ] Source of each contact is documented
- [ ] Consent type is verified (express/implied/relationship)
- [ ] Jurisdiction requirements are met for each contact
- [ ] Suppression list has been checked
- [ ] List is recent (not stale data)

**Email Compliance**:
- [ ] Sender name and address are accurate
- [ ] Subject line is not deceptive
- [ ] Physical address is included
- [ ] Unsubscribe mechanism works
- [ ] Privacy/transparency notice included (if required)
- [ ] No prohibited content (health info, misleading claims)

**Technical Compliance**:
- [ ] Email authentication is configured (SPF, DKIM, DMARC)
- [ ] Unsubscribe processing is automated
- [ ] Suppression list sync is current
- [ ] Logging is enabled

### Post-Send Checklist

- [ ] Opt-out requests processed within 24 hours
- [ ] Bounce addresses removed from list
- [ ] Complaint addresses added to suppression
- [ ] Campaign documented for records
- [ ] Any data subject requests handled

### Quarterly Audit Checklist

- [ ] Suppression lists reviewed for completeness
- [ ] Consent records audited for documentation
- [ ] List sources verified for continued validity
- [ ] Vendor DPAs reviewed
- [ ] Team training completed/updated
- [ ] Regulatory changes reviewed
- [ ] Procedures updated as needed
- [ ] Incident log reviewed

### Annual Compliance Review

- [ ] Full legitimate interest assessment review
- [ ] Privacy policy update
- [ ] Data processing records update
- [ ] Vendor security review
- [ ] Legal consultation on regulatory changes
- [ ] Penetration testing / security audit
- [ ] Insurance coverage review
- [ ] Board/leadership compliance briefing

---

## Summary: The Compliance Mindset

Compliance isn't a checkbox exercise—it's a mindset that should inform every cold email decision:

**Ask**: Would I be comfortable if regulators reviewed this campaign?

**Ask**: Would I be comfortable if this recipient posted my email publicly?

**Ask**: Is this how I would want to be contacted?

**Ask**: Am I treating personal data with appropriate respect?

**Ask**: Do I have documentation to defend my practices?

If you can answer "yes" to all five questions, you're likely operating ethically and compliantly. If any answer is uncertain, pause and reconsider.

---

*Compliance protects your business, your reputation, and the people you contact. It's not overhead—it's foundation.*
