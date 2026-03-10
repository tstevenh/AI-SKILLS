# Personalization Templates

Ready-to-use personalization snippets and structures for different scenarios.

---

## First Line Generators

### LinkedIn Post Reference
```
Your recent post about [topic] resonated—especially your point about [specific insight].

Saw your LinkedIn post on [topic]. [Your reaction/observation].

Your take on [topic] was different from what I usually see—in a good way.
```

### Company News Reference
```
Congrats on [news]—that's a big milestone for [Company].

Saw the announcement about [news]. [Observation about what it means].

[Company]'s [news] caught my attention because [specific reason].
```

### Hiring Activity Reference
```
Noticed you're building out the [department] team—[X] new roles is ambitious.

Saw you're hiring [roles]. [Inference about their priorities].

Your job posting for [role] caught my eye—particularly [specific requirement].
```

### Content/Podcast Reference
```
Your [podcast/talk] at [venue] was excellent—especially [specific point].

Been following your [newsletter/blog]. The piece on [topic] was [reaction].

Your interview on [podcast] was great—your story about [moment] stood out.
```

### Achievement Reference
```
[Achievement] is impressive—not many companies hit that milestone.

Congrats on [recognition/award]. Well deserved based on [observation].

[Company]'s [metric/growth] caught my attention.
```

---

## PS Line Personalization

### Education Connection
```
PS - Fellow [school] alum here. Go [mascot]!
```

### Previous Company
```
PS - Saw you came from [Company]. [Relevant observation about their experience there].
```

### Shared Interest
```
PS - Noticed you're into [hobby/interest]. [Brief relevant comment].
```

### Mutual Connection
```
PS - Just realized we're both connected to [Name]. Small world.
```

### Recent Event
```
PS - Were you at [event]? Would have loved to connect in person.
```

---

## Industry-Specific Personalization

### SaaS
```
Your product's approach to [specific feature] is clever—most competitors [what they do differently].

Noticed you're on a [funding stage] path—the next 12 months are critical for [specific SaaS challenge].

Your PLG motion is working—[evidence from their site/reviews].
```

### Agency
```
Your work for [client] was impressive—especially [specific element].

[Agency]'s positioning in [specialty] is clear. How's demand for that?

Noticed you're growing the team. Capacity or new capability?
```

### E-commerce
```
Your [product category] selection is unique—especially [specific product/approach].

[Brand]'s customer reviews mention [specific positive pattern]—that's rare.

Your site's [specific element] is really well optimized.
```

### Healthcare
```
Your approach to [specific healthcare challenge] is different from typical [provider type].

[Company]'s patient satisfaction scores are impressive—clearly something's working.

Given [regulation/change], I imagine [relevant implication] is top of mind.
```

---

## AI Prompt Templates for Personalization

### First Line Generation Prompt
```
Write a personalized first line for a cold email.

Recipient: [Name], [Title] at [Company]

Context:
- Their recent LinkedIn post: "[Post content]"
- Company industry: [Industry]
- Company size: [Size]
- What we sell: [Brief description]

Requirements:
- 1-2 sentences maximum
- Reference their specific content or situation
- Natural and conversational tone
- Should connect to why we're relevant to them
- Avoid generic compliments like "love what you're doing"
```

### Company-Specific Value Prop Prompt
```
Customize this generic value proposition for the specific company.

Generic value prop: "[Your standard value prop]"

Company context:
- Company: [Name]
- Industry: [Industry]
- Size: [Size]
- Recent news: [News]
- Likely challenges: [Challenges]
- Current tools they use: [Technologies]

Requirements:
- Keep the core message but make it specific to this company
- Reference their situation
- 1-2 sentences
```

### Case Study Match Prompt
```
Select and customize the most relevant case study reference.

Available case studies:
1. [Company A]: [Brief description and result]
2. [Company B]: [Brief description and result]
3. [Company C]: [Brief description and result]

Target prospect:
- Company: [Name]
- Industry: [Industry]
- Size: [Size]
- Likely challenge: [Challenge]

Requirements:
- Select the most similar case study
- Explain why it's relevant to them
- 2-3 sentences maximum
```

---

## Personalization Variables

### Standard Variables
```
{{first_name}} - Recipient's first name
{{last_name}} - Recipient's last name
{{company}} - Company name
{{title}} - Job title
{{industry}} - Industry
{{city}} - Location
```

### Advanced Variables
```
{{recent_news}} - Recent company news or announcement
{{linkedin_post}} - Summary of recent LinkedIn activity
{{company_size}} - Employee count
{{tech_stack}} - Technologies they use
{{funding_stage}} - Funding status
{{competitor}} - Key competitor name
{{mutual_connection}} - Shared connection name
{{recent_hire}} - Recent notable hire
{{case_study_company}} - Relevant case study company name
{{case_study_result}} - Relevant case study result
{{personalized_first_line}} - AI-generated opening
```

---

## Personalization Workflows

### Manual Personalization (High Quality)
```
1. Open prospect's LinkedIn profile
2. Read recent posts and about section
3. Check company news (press releases, announcements)
4. Identify 1-2 specific personalization points
5. Write custom first line referencing findings
6. Connect personalization to value proposition
7. Write remainder of email
8. Review for natural flow
```

### Semi-Automated (Balanced)
```
1. Pull prospect data from tool (Clay, Apollo)
2. Auto-generate first line candidates using AI
3. Human reviews and selects/edits best option
4. Merge into email template
5. Human reviews final email
6. Send
```

### Automated (Scale)
```
1. Import prospects to enrichment tool
2. Run automated enrichment (LinkedIn, news, tech)
3. AI generates personalized elements
4. Auto-merge into sequence
5. Spot-check sample emails
6. Launch campaign
7. Monitor and adjust
```

---

## Quality Control

### Before Scaling Personalization
- [ ] Test AI outputs manually (review 50+ examples)
- [ ] Verify data accuracy (check 20+ profiles)
- [ ] Confirm personalization connects to pitch
- [ ] Check for common errors (dates, names, relevance)
- [ ] Test merge fields work correctly
- [ ] Have human review sample before launch

### Ongoing Quality Checks
- [ ] Spot-check 5-10% of personalized emails
- [ ] Monitor reply rate by personalization type
- [ ] Track "this doesn't apply to me" responses
- [ ] Update AI prompts based on failures
- [ ] Refresh case studies and examples regularly

---

## Summary: Personalization Templates

**Specificity Wins**: Generic personalization ("love what you're doing") is worse than none.

**Connection to Pitch**: Personalization should bridge to why you're reaching out.

**Quality Over Volume**: Better to send fewer, well-personalized emails than many poorly personalized ones.

**Test and Iterate**: What works varies by audience. Test different approaches.

**Human Review**: Always have humans review AI-generated content before sending.
