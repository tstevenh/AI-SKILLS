# AI Writing Deep Dive

> Complete guide to AI-powered content creation: strategies, workflows, prompts, and quality control.

---

## Table of Contents

1. [AI Content Strategy](#ai-content-strategy)
2. [The AI Writing Spectrum](#the-ai-writing-spectrum)
3. [Blog Post Generation](#blog-post-generation)
4. [Landing Page Copy](#landing-page-copy)
5. [Email Copy](#email-copy)
6. [Ad Copy](#ad-copy)
7. [Social Media Content](#social-media-content)
8. [Product Descriptions](#product-descriptions)
9. [SEO Content at Scale](#seo-content-at-scale)
10. [Quality Control Systems](#quality-control-systems)
11. [Voice and Brand Consistency](#voice-and-brand-consistency)
12. [Ethical Considerations](#ethical-considerations)
13. [Workflow Templates](#workflow-templates)

---

## AI Content Strategy

### The Strategic Question

Before automating content, answer:

1. **What is the goal?** Traffic, conversions, brand awareness?
2. **What is the quality bar?** Can AI meet it alone?
3. **What is the volume need?** 5 posts/month or 100?
4. **What is the audience expectation?** Expert analysis or helpful info?
5. **What are the risks?** Brand damage, legal, accuracy?

### The Content Matrix

| Content Type | Volume Need | Quality Sensitivity | AI Role |
|--------------|-------------|---------------------|---------|
| Blog posts (informational) | High | Medium | Primary drafter |
| Blog posts (thought leadership) | Low | Very High | Assistant only |
| Landing pages | Medium | High | Draft + heavy edit |
| Email sequences | High | Medium | Primary drafter |
| Sales emails (1:1) | Medium | High | Personalization layer |
| Ad copy | Very High | High | Generate variations |
| Social posts | Very High | Medium | Primary creator |
| Product descriptions | Very High | Medium | Primary creator |
| Support docs | Medium | Medium-High | Draft + review |
| Legal/compliance | Low | Very High | Never |

### AI-Assisted vs AI-Generated

#### AI-Assisted (Human Primary)
- Human writes core content
- AI helps with research, outlines, editing
- Human voice dominates
- Best for: Thought leadership, sensitive topics

#### AI-Generated (AI Primary)
- AI creates first draft
- Human reviews and edits
- AI voice with human polish
- Best for: High-volume, informational content

#### Fully Automated
- AI handles end-to-end
- Minimal human oversight
- Best for: Internal docs, data-driven content

### The Quality-Volume Tradeoff

```
                    ┌─────────────────┐
           High    │ Thought         │
                   │ Leadership      │
                   │ (Human + AI)    │
  Quality          ├─────────────────┤
                   │ Standard Blog   │
                   │ (AI + Human)    │
                   ├─────────────────┤
           Low     │ Scale Content   │
                   │ (AI primary)    │
                   └─────────────────┘
                   Low ──────────► High
                        Volume
```

---

## The AI Writing Spectrum

### Level 1: Research Assistant

AI helps gather information:

```
Prompt: "Research the top 10 competitors for [product]. 
For each, list: key features, pricing, target market, 
main differentiators. Output as a table."
```

**Human does:** All writing
**AI does:** Research, organization

### Level 2: Outline Generator

AI structures the content:

```
Prompt: "Create a detailed outline for a blog post titled 
'[Title]'. Include main sections, subsections, key points 
to cover, and suggested data/examples to include."
```

**Human does:** Writing, voice, examples
**AI does:** Structure, research, initial points

### Level 3: Draft Creator

AI writes the first draft:

```
Prompt: "Write a comprehensive blog post following this 
outline: [outline]. Use a professional but approachable 
tone. Include specific examples and data points."
```

**Human does:** Editing, fact-checking, voice refinement
**AI does:** Full draft

### Level 4: Polished Content

AI creates near-final content:

```
Prompt: "Write a polished, publish-ready blog post about 
[topic]. Follow these brand guidelines: [guidelines]. 
Include SEO optimization for [keyword]."
```

**Human does:** Final review, fact-check, publish
**AI does:** Complete content creation

### Level 5: Full Automation

AI handles everything:

```
Workflow: 
Trigger → Research → Draft → SEO Optimize → 
Format → Schedule → Publish
```

**Human does:** Set up system, monitor quality
**AI does:** Everything operational

---

## Blog Post Generation

### The Blog Post Workflow

```
┌─────────────────────────────────────────────────────────────┐
│                    BLOG POST WORKFLOW                        │
├─────────────────────────────────────────────────────────────┤
│                                                              │
│  1. TOPIC SELECTION                                          │
│     ├── Keyword research (Ahrefs/SEMrush)                   │
│     ├── AI expansion: "Related topics to [keyword]"         │
│     └── Human approval                                       │
│                                                              │
│  2. RESEARCH                                                 │
│     ├── AI: Gather top 10 ranking articles                  │
│     ├── AI: Extract key points, stats, gaps                 │
│     └── AI: Compile research brief                          │
│                                                              │
│  3. OUTLINE                                                  │
│     ├── AI: Generate detailed outline                       │
│     ├── Human: Review and adjust structure                  │
│     └── Include SEO requirements                            │
│                                                              │
│  4. FIRST DRAFT                                              │
│     ├── AI: Write section by section                        │
│     ├── Include examples, data points                       │
│     └── Follow outline precisely                            │
│                                                              │
│  5. ENHANCEMENT                                              │
│     ├── AI: Add internal links                              │
│     ├── AI: Optimize for target keyword                     │
│     └── AI: Generate meta description, title options        │
│                                                              │
│  6. REVIEW                                                   │
│     ├── Human: Fact-check claims                            │
│     ├── Human: Add unique insights                          │
│     ├── Human: Verify tone and voice                        │
│     └── Editor review (optional)                            │
│                                                              │
│  7. PUBLISH                                                  │
│     ├── Format for CMS                                      │
│     ├── Add images (see images.md)                          │
│     ├── Schedule or publish                                 │
│     └── Promote (social, email)                             │
│                                                              │
└─────────────────────────────────────────────────────────────┘
```

### Blog Post Prompts

#### Research Prompt
```
I'm writing a blog post about [TOPIC] targeting the keyword [KEYWORD].

Research this topic and provide:

1. KEY STATISTICS: 5-10 recent statistics I should cite (with sources)

2. COMMON QUESTIONS: What questions do people commonly ask about this topic?

3. EXPERT OPINIONS: What are the main schools of thought or expert perspectives?

4. COMPETITOR ANALYSIS: What are the top-ranking articles missing? What angle could I take?

5. EXAMPLES: What case studies or examples would strengthen this article?

Format as a research brief I can reference while writing.
```

#### Outline Prompt
```
Create a comprehensive outline for a blog post:

TOPIC: [Topic]
TARGET KEYWORD: [Keyword]
TARGET LENGTH: [X] words
AUDIENCE: [Description]
GOAL: [What should readers do/learn?]

Include:
- H1 title (with keyword)
- Introduction hook
- H2 sections with H3 subsections
- Key points for each section
- Where to include examples/data
- CTA placement
- Internal linking opportunities to: [URLs]

Make the outline detailed enough that a writer could follow it exactly.
```

#### Section Writing Prompt
```
Write the [Section Name] section of a blog post.

CONTEXT:
- Overall topic: [Topic]
- Target keyword: [Keyword]  
- Audience: [Description]
- Tone: [Describe]

OUTLINE FOR THIS SECTION:
[Paste section outline]

REQUIREMENTS:
- Length: ~[X] words
- Include [specific requirement]
- Transition smoothly from previous section about [topic]
- End with transition to next section about [topic]

Write naturally, not like AI. Use specific examples. Avoid clichés.
```

#### Editing Prompt
```
Edit this blog post section for:

1. CLARITY: Simplify complex sentences, remove jargon
2. ENGAGEMENT: Add hooks, improve flow
3. SEO: Naturally incorporate [keyword] 2-3 times
4. SPECIFICITY: Replace vague claims with specifics
5. VOICE: Match this style: [example paragraph]

Original text:
[Paste text]

Return the edited version with a brief note on major changes.
```

### Blog Post Quality Checklist

```markdown
## Pre-Publish Checklist

### Content Quality
- [ ] Thesis is clear in introduction
- [ ] Each section advances the main argument
- [ ] Claims are supported with evidence
- [ ] Examples are specific and relevant
- [ ] Conclusion provides actionable takeaway

### SEO
- [ ] Target keyword in H1
- [ ] Keyword in first 100 words
- [ ] Keyword in 2-3 H2s naturally
- [ ] Meta description includes keyword
- [ ] Internal links added (3-5 minimum)
- [ ] External links to authoritative sources

### Readability
- [ ] Sentences under 25 words average
- [ ] Paragraphs under 4 sentences
- [ ] Subheadings every 300 words
- [ ] Bullet points for lists
- [ ] No walls of text

### Accuracy
- [ ] All statistics verified
- [ ] Links work
- [ ] No outdated information
- [ ] Legal review if needed

### Brand
- [ ] Tone matches brand voice
- [ ] No competitor mentions (unless intentional)
- [ ] CTA aligns with business goals
```

---

## Landing Page Copy

### Landing Page Framework

The classic structure:

1. **Hero** - Headline + subheadline + CTA
2. **Problem** - Agitate the pain
3. **Solution** - Introduce your offering
4. **Features/Benefits** - What they get
5. **Social Proof** - Testimonials, logos, numbers
6. **Objections** - Handle concerns
7. **CTA** - Clear next step
8. **FAQ** - Common questions

### Hero Section Prompts

#### Headline Generation
```
Generate 10 headlines for a landing page:

PRODUCT: [Product name and description]
TARGET AUDIENCE: [Who is this for?]
MAIN BENEFIT: [Primary value proposition]
TONE: [Professional/Playful/Urgent/etc.]

Requirements:
- Under 10 words
- Benefit-focused (not feature-focused)
- Creates curiosity or urgency
- Avoids clichés and hype words

Format: Just the headlines, numbered 1-10.
```

#### Subheadline Generation
```
Write 5 subheadlines to pair with this headline: "[HEADLINE]"

PRODUCT: [Description]
AUDIENCE: [Description]

Requirements:
- 15-25 words
- Expands on headline benefit
- Adds specificity or credibility
- Includes one of: timeframe, number, or differentiator
```

### Problem Section Prompt
```
Write the "problem" section for a landing page:

PRODUCT: [Product]
TARGET AUDIENCE: [Audience]
MAIN PAIN POINTS:
1. [Pain 1]
2. [Pain 2]
3. [Pain 3]

Requirements:
- 150-200 words
- Make the reader feel understood
- Use "you" language
- Be specific about consequences of the problem
- Don't mention the solution yet
- End with transition to solution

Tone: Empathetic but not melodramatic.
```

### Features/Benefits Prompt
```
Write feature-benefit pairs for a landing page:

PRODUCT: [Product]
FEATURES:
1. [Feature 1]
2. [Feature 2]
3. [Feature 3]
4. [Feature 4]

For each feature, write:
- A compelling 3-5 word headline
- A 20-30 word description focusing on the benefit
- Use "you" language

Format:
### [Feature Headline]
[Benefit description]
```

### Testimonial Enhancement Prompt
```
Enhance this customer testimonial for a landing page:

ORIGINAL: "[Raw testimonial]"
CUSTOMER: [Name, title, company]

Requirements:
- Keep the authentic voice
- Highlight specific results
- Add credibility markers
- Keep under 50 words
- Do not fabricate details - only clarify and tighten

Return the enhanced version.
```

### Landing Page Complete Prompt
```
Write complete landing page copy for:

PRODUCT: [Name] - [One sentence description]
PRICE: [Price point]
TARGET: [Ideal customer]
MAIN BENEFIT: [Primary value proposition]
KEY FEATURES:
1. [Feature 1]
2. [Feature 2]
3. [Feature 3]
COMPETITORS: [Main alternatives]
DIFFERENTIATOR: [Why choose us]
SOCIAL PROOF: [What we have: testimonials/logos/numbers]
GOAL: [Desired action]

Write these sections:
1. Hero (headline, subheadline, CTA button text)
2. Problem (150 words)
3. Solution (100 words)
4. Features (3 feature blocks)
5. Social proof section (how to present it)
6. Objection handling (3 common objections with responses)
7. Final CTA (headline + button text)
8. FAQ (5 questions with answers)

Tone: [Specify tone]
```

---

## Email Copy

### Email Types and Frameworks

#### 1. Welcome Sequence

**Email 1: Welcome**
```
Subject: Welcome to [Brand] 🎉

Structure:
- Thank them for signing up
- Set expectations (what they'll receive)
- Quick win or valuable resource
- One CTA
```

**Email 2: Value (Day 2)**
```
Subject: [Solve immediate problem]

Structure:
- Address their main pain point
- Provide immediate value
- Show you understand them
- Soft mention of product
```

**Email 3: Story (Day 4)**
```
Subject: Why I created [Product]

Structure:
- Founder/brand story
- Relatable struggle
- The "aha" moment
- How product solves it
```

**Email 4: Social Proof (Day 6)**
```
Subject: [Customer name] increased [result] by [X]%

Structure:
- Customer story
- Specific results
- How they did it
- CTA to try
```

**Email 5: Offer (Day 8)**
```
Subject: Special offer for new members

Structure:
- Exclusive offer
- Deadline/urgency
- What they get
- Clear CTA
```

### Email Prompt Templates

#### Welcome Email
```
Write a welcome email for:

COMPANY: [Name]
PRODUCT: [What it is]
SUBSCRIBER SOURCE: [How they signed up]
IMMEDIATE VALUE: [What to give them]
TONE: [Friendly/Professional/Playful]

Requirements:
- Subject line (under 50 chars)
- Preview text (under 100 chars)
- Body under 200 words
- One clear CTA
- Set expectations for future emails
- Make them feel they made a good decision
```

#### Nurture Email
```
Write a nurture email for:

CONTEXT: This is email [X] of [Y] in a sequence
PREVIOUS EMAIL: [What was covered]
THIS EMAIL'S GOAL: [Specific goal]
AUDIENCE SEGMENT: [Who they are]
VALUE TO PROVIDE: [What insight/tip/resource]

Requirements:
- Subject line that creates curiosity
- Open with connection to previous email or their situation
- Provide genuine value (not just teaser)
- Soft CTA or breadcrumb
- Under 250 words

Avoid: Being salesy, vague promises, "checking in" openers
```

#### Sales Email
```
Write a sales email for:

PRODUCT: [Product]
OFFER: [What you're offering]
AUDIENCE: [Who is receiving this]
URGENCY: [Deadline or scarcity element]
PRICE: [If relevant]
PREVIOUS RELATIONSHIP: [What do they already know?]

Requirements:
- Subject line that gets opens (under 50 chars)
- Benefit-focused opening
- Clear value proposition
- Handle main objection
- Strong CTA
- PS line with additional hook
- Under 300 words
```

#### Re-Engagement Email
```
Write a re-engagement email for subscribers who haven't 
opened an email in 60+ days:

COMPANY: [Name]
LAST INTERACTION: [What they last engaged with]
GOAL: [Get them back or clean list]

Include:
- Attention-grabbing subject line
- Acknowledge the absence
- Remind them of value
- Offer something special
- Clear choice: stay or unsubscribe
- Under 150 words
```

### Email Subject Line Generation
```
Generate 20 email subject lines for:

EMAIL TYPE: [Welcome/Nurture/Sales/Newsletter]
MAIN TOPIC: [What the email is about]
TONE: [Specify]
AUDIENCE: [Who]

Requirements:
- Under 50 characters
- Mix of approaches: curiosity, benefit, urgency, personalization
- No spam trigger words (free, guarantee, etc.)
- Would work in B2B context

Format: Just the subject lines, one per line.
```

### Cold Email Personalization

```
Write a personalized cold email opening for:

RECIPIENT: [Name]
TITLE: [Their title]
COMPANY: [Their company]
RECENT NEWS: [Something they did/announced]
MY PRODUCT: [What I'm selling]
CONNECTION: [Why I'm reaching out to them specifically]

Requirements:
- First line references something specific about them (not generic)
- Natural transition to reason for email
- Under 50 words for the opening
- Genuine, not sycophantic

Do NOT:
- Mention you "came across" their profile
- Compliment generically ("love what you're doing")
- Start with "I"
```

---

## Ad Copy

### Ad Copy Frameworks

#### Facebook/Instagram Ads

**Format Options:**
1. **Single image/video:** Headline + Primary text + Description
2. **Carousel:** Headline per card + Primary text + Description
3. **Stories:** Text overlays + CTA

**Character Limits:**
- Primary text: 125 chars (above fold)
- Headline: 40 chars
- Description: 30 chars

#### Google Ads

**Responsive Search Ads:**
- Headlines: 15 (up to 30 chars each)
- Descriptions: 4 (up to 90 chars each)

**Best practice:** Provide variations for Google to test

### Ad Copy Prompts

#### Facebook Ad Copy Generation
```
Generate Facebook ad copy for:

PRODUCT: [Product]
TARGET AUDIENCE: [Detailed audience]
CAMPAIGN GOAL: [Conversions/Traffic/Awareness]
OFFER: [What you're offering]
LANDING PAGE: [Where they go]

Create 5 variations with different angles:
1. Pain point focused
2. Benefit focused  
3. Social proof focused
4. Curiosity/intrigue
5. Direct/clear

For each variation, provide:
- Primary text (under 125 chars for above fold)
- Headline (under 40 chars)
- Description (under 30 chars)
- Suggested image/video direction
```

#### Google Ads Headlines
```
Generate Google Ads headlines for:

KEYWORD: [Target keyword]
PRODUCT: [Product/Service]
UNIQUE SELLING POINTS:
1. [USP 1]
2. [USP 2]
3. [USP 3]
OFFERS: [Any current offers]

Generate 15 headlines (max 30 characters each):
- 5 with keyword included
- 5 benefit-focused
- 3 with numbers/specifics
- 2 with urgency/scarcity

Format: Just the headlines, one per line, with character count.
```

#### Google Ads Descriptions
```
Generate Google Ads descriptions for:

KEYWORD: [Keyword]
PRODUCT: [Product]
HEADLINES BEING USED: [List them]
CTA: [Desired action]

Generate 4 descriptions (max 90 characters each):
- Include keyword naturally in 2
- Include CTA in all
- Expand on headlines without repeating
- Include credibility markers if possible

Format: Description with character count.
```

#### Video Ad Script
```
Write a 30-second video ad script for:

PRODUCT: [Product]
AUDIENCE: [Target audience]
PLATFORM: [TikTok/Instagram/YouTube]
HOOK: [First 3 seconds must...]
CTA: [What to do]

Structure:
- Hook (0-3s): Grab attention
- Problem (3-10s): Relate to their struggle
- Solution (10-20s): Show the product
- Proof (20-25s): Quick result/testimonial
- CTA (25-30s): Clear next step

Include:
- Script text
- Visual directions
- Text overlay suggestions
- Music mood
```

### Ad Copy Testing Framework

```
For each ad set, create variations testing:

1. HOOK VARIATION
   - Question hook: "Tired of [problem]?"
   - Statement hook: "[Bold claim]"
   - Story hook: "I was [relatable situation]..."
   - Curiosity hook: "The secret to [result]..."

2. BENEFIT ANGLE
   - Time saved
   - Money saved
   - Status/identity
   - Avoiding pain

3. SOCIAL PROOF TYPE
   - Numbers: "10,000+ customers"
   - Testimonial: "Changed my life - Sarah"
   - Authority: "Featured in Forbes"
   - Comparison: "Better than [alternative]"

4. CTA VARIATION
   - Direct: "Buy Now"
   - Soft: "Learn More"
   - Curious: "See How"
   - Urgent: "Get Yours Before [deadline]"
```

---

## Social Media Content

### Platform-Specific Strategies

#### Twitter/X

**Character limit:** 280 (images reduce to 257)

**Content types:**
- Threads (educational)
- Single tweets (hot takes, quotes)
- Quote tweets (commentary)
- Polls
- Images/memes

**Tweet Generation Prompt:**
```
Generate 10 tweets about [TOPIC] for a [AUDIENCE] audience.

Tone: [Professional/Witty/Educational]
Brand voice: [Describe]

Requirements:
- Under 280 characters
- Mix of formats: statements, questions, lists
- Include 2-3 with hooks for threads
- No hashtags unless specifically relevant
- Engaging, not generic

Format: Numbered list with character counts.
```

**Thread Generation Prompt:**
```
Write a Twitter thread about [TOPIC]:

TARGET AUDIENCE: [Who]
GOAL: [Educate/Entertain/Persuade]
LENGTH: [7-15 tweets]
CTA: [What to do at end]

Requirements:
- Tweet 1: Hook that stops the scroll
- Each tweet standalone but flows
- Include specific examples/data
- End with CTA + engagement question
- Under 280 chars per tweet

Format each tweet on its own line with number.
```

#### LinkedIn

**Character limits:**
- Posts: 3,000
- Article headlines: 150

**LinkedIn Post Prompt:**
```
Write a LinkedIn post about [TOPIC]:

AUTHOR: [Name, title]
AUDIENCE: [Target connections]
GOAL: [Thought leadership/Engagement/Leads]
TONE: [Professional but human]

Structure:
- Hook (first line visible before "see more")
- Story or insight (main content)
- Takeaway (what they learn)
- Engagement question (optional)

Requirements:
- Under 1,500 characters
- Use line breaks for readability
- First line must hook
- No excessive hashtags (3 max)
- Professional but not corporate speak

Include 3 hashtag suggestions at the end.
```

#### Instagram

**Caption limit:** 2,200 characters

**Instagram Caption Prompt:**
```
Write an Instagram caption for:

IMAGE/VIDEO: [Describe what's shown]
ACCOUNT TYPE: [Brand/Personal/Creator]
TOPIC: [What the post is about]
GOAL: [Engagement/Traffic/Sales]
TONE: [Casual/Inspiring/Educational]

Requirements:
- Hook in first 125 characters (visible before "more")
- Include emoji naturally
- CTA or question for engagement
- 5 relevant hashtags (mix of popular and niche)
- Under 1,000 characters for optimal engagement
```

### Content Calendar Generation

```
Create a 2-week social media calendar for:

BRAND: [Name]
PLATFORMS: [Twitter, LinkedIn, Instagram]
TOPICS/PILLARS:
1. [Topic 1]
2. [Topic 2]
3. [Topic 3]
4. [Topic 4 - promotional]
POSTING FREQUENCY: [X posts per platform per week]
UPCOMING: [Events, launches, holidays]

For each post, include:
- Platform
- Date/time
- Content type (text, image, video, carousel)
- Topic
- Brief description or actual copy
- CTA

Format as a table.
```

### Content Repurposing

```
Repurpose this blog post into social content:

BLOG POST: [Title and URL]
MAIN POINTS:
1. [Key point 1]
2. [Key point 2]
3. [Key point 3]
PLATFORMS: [Where to post]

Create:
1. Twitter thread (7-10 tweets)
2. 3 standalone tweets
3. LinkedIn post
4. Instagram carousel (5-7 slides outline)
5. 2 Facebook posts

For each, adapt the content for the platform's style and audience.
```

---

## Product Descriptions

### E-commerce Product Descriptions

#### Product Description Framework
```
PRODUCT: [Name]
CATEGORY: [Type]
KEY FEATURES:
1. [Feature 1]
2. [Feature 2]
3. [Feature 3]
BENEFITS:
1. [Benefit 1]
2. [Benefit 2]
TARGET CUSTOMER: [Who buys this]
PRICE POINT: [Budget/Mid/Premium]
DIFFERENTIATOR: [Why this over competitors]
```

#### Product Description Prompt
```
Write a product description for:

[Product Framework filled out]

Requirements:
- 150-200 words
- Lead with benefits, follow with features
- Use sensory language for physical products
- Include one customer pain point it solves
- End with subtle urgency or CTA
- Optimize for keyword: [keyword]

Avoid: Generic adjectives (high-quality, premium), clichés
```

#### Bulk Product Description Prompt
```
Write descriptions for these products in a consistent style:

BRAND VOICE: [Describe]
CATEGORY: [Product category]
TARGET CUSTOMER: [Who]
DESCRIPTION LENGTH: [100/150/200 words]

Products:
1. [Product 1 details]
2. [Product 2 details]
3. [Product 3 details]
[...]

For each, provide:
- SEO-friendly title
- Short description (50 words)
- Full description ([length] words)
- 5 bullet points
- Meta description (155 chars)
```

### SaaS Feature Descriptions

#### Feature Page Copy
```
Write feature page copy for:

PRODUCT: [SaaS product]
FEATURE: [Feature name]
WHAT IT DOES: [Functional description]
USER BENEFIT: [Why they care]
COMPETITIVE ADVANTAGE: [What's different]
USE CASE: [Example scenario]

Include:
1. H1 headline (benefit-focused)
2. Subheadline (what + for whom)
3. Overview paragraph (100 words)
4. 3 sub-features with descriptions
5. Use case scenario (150 words)
6. CTA

Tone: [Specify]
```

---

## SEO Content at Scale

### The SEO Content System

For high-volume SEO content, you need a system:

```
┌─────────────────────────────────────────────────────┐
│              SEO CONTENT SYSTEM                      │
├─────────────────────────────────────────────────────┤
│                                                      │
│  1. KEYWORD RESEARCH                                 │
│     └── Tool: Ahrefs, SEMrush, or AI-assisted       │
│                                                      │
│  2. KEYWORD CLUSTERING                               │
│     └── Group by intent and topic                   │
│                                                      │
│  3. CONTENT BRIEF GENERATION                         │
│     └── AI generates briefs from top results        │
│                                                      │
│  4. DRAFT CREATION                                   │
│     └── AI writes based on brief                    │
│                                                      │
│  5. OPTIMIZATION                                     │
│     └── AI adds keywords, links, structure          │
│                                                      │
│  6. REVIEW                                           │
│     └── Human editor checks quality                 │
│                                                      │
│  7. PUBLISH + MONITOR                                │
│     └── Track rankings, iterate                     │
│                                                      │
└─────────────────────────────────────────────────────┘
```

### Content Brief Prompt
```
Create an SEO content brief for:

TARGET KEYWORD: [Keyword]
SEARCH VOLUME: [Volume]
KEYWORD DIFFICULTY: [Score]
SEARCH INTENT: [Informational/Transactional/etc.]
COMPETITOR URLS: [Top 3 ranking URLs]

Include:
1. RECOMMENDED TITLE (with keyword)
2. META DESCRIPTION (155 chars, with keyword)
3. TARGET WORD COUNT (based on competitors)
4. OUTLINE
   - H1
   - H2s with H3s
   - Key points for each section
5. KEYWORDS TO INCLUDE
   - Primary (X times)
   - Secondary keywords (list)
   - LSI keywords (list)
6. QUESTIONS TO ANSWER (from People Also Ask)
7. INTERNAL LINKING OPPORTUNITIES
8. EXTERNAL SOURCES TO CITE
9. IMAGE SUGGESTIONS
10. FEATURED SNIPPET OPPORTUNITY (if any)
```

### Keyword Research with AI
```
Act as an SEO specialist. Research keywords for:

WEBSITE: [URL]
NICHE: [Industry]
CURRENT RANKINGS: [Brief overview]
BUSINESS GOAL: [Traffic/Leads/Sales]

Provide:
1. 20 primary keywords (medium difficulty, good volume)
2. 30 long-tail keywords (low difficulty, lower volume)
3. 10 question keywords (featured snippet opportunities)
4. 5 comparison keywords ([product] vs [competitor])
5. 10 "best" keywords ([best product for X])

For each keyword, estimate:
- Search intent
- Difficulty level
- Priority (1-3)

Format as a table.
```

### Meta Description Generation at Scale
```
Generate meta descriptions for these pages:

BRAND: [Brand name]
PAGES:
1. [Page title + target keyword]
2. [Page title + target keyword]
3. [Page title + target keyword]
[...]

Requirements:
- 150-155 characters exactly
- Include target keyword naturally
- Include brand name
- Action-oriented
- Unique to each page

Format: Page number + meta description + character count
```

---

## Quality Control Systems

### The Review Workflow

```
┌─────────────────────────────────────────────────────┐
│               QUALITY CONTROL FLOW                   │
├─────────────────────────────────────────────────────┤
│                                                      │
│  AI DRAFT                                            │
│     │                                                │
│     ▼                                                │
│  AUTOMATED CHECKS                                    │
│  ├── Grammar (Grammarly API)                        │
│  ├── Readability (Hemingway)                        │
│  ├── SEO score (Surfer/Clearscope)                  │
│  ├── Plagiarism (Copyscape)                         │
│  └── Brand voice (custom classifier)                │
│     │                                                │
│     ▼                                                │
│  PASS/FAIL                                           │
│  ├── Pass → Human Review Queue                      │
│  └── Fail → AI Revision → Re-check                  │
│     │                                                │
│     ▼                                                │
│  HUMAN REVIEW                                        │
│  ├── Fact-checking                                  │
│  ├── Voice/tone check                               │
│  ├── Add unique insights                            │
│  └── Final approval                                 │
│     │                                                │
│     ▼                                                │
│  PUBLISH                                             │
│                                                      │
└─────────────────────────────────────────────────────┘
```

### AI Self-Review Prompt
```
Review this draft for quality issues:

CONTENT: [Paste content]
TYPE: [Blog/Email/Ad/etc.]
GUIDELINES: [Any specific rules]

Check for:
1. FACTUAL ACCURACY: Flag any claims that need verification
2. CLARITY: Identify confusing or unclear sentences
3. ENGAGEMENT: Rate hook strength (1-10) and suggest improvements
4. STRUCTURE: Is the flow logical?
5. REDUNDANCY: Identify repetitive points
6. TONE: Does it match [brand voice description]?
7. SEO: For keyword [X], suggest optimizations
8. CTA: Is the call to action clear?

Provide specific line-by-line feedback, then an overall score (1-10).
```

### Plagiarism Prevention
```
Rewrite this content to be completely original:

ORIGINAL: [Content that needs rewriting]
TOPIC: [Same topic, fresh angle]
VOICE: [Your brand voice]

Requirements:
- Same key information
- Completely different phrasing
- Add new examples not in original
- Different structure
- Your unique perspective

Do not retain any consecutive phrases of 5+ words from the original.
```

---

## Voice and Brand Consistency

### Creating a Voice Profile

```
Analyze these writing samples to create a brand voice profile:

SAMPLES:
1. [Sample 1]
2. [Sample 2]
3. [Sample 3]

Create a voice profile including:

1. TONE ATTRIBUTES
   - Formality (1-10 scale)
   - Warmth (1-10 scale)
   - Humor (1-10 scale)
   - Authority (1-10 scale)

2. VOCABULARY
   - Words we USE: [list]
   - Words we AVOID: [list]
   - Industry jargon level

3. SENTENCE STYLE
   - Average length
   - Simple vs complex
   - Active vs passive

4. PERSPECTIVE
   - First person (we/I) vs second person (you)
   - Direct vs indirect

5. SIGNATURE ELEMENTS
   - Phrases we repeat
   - Unique stylistic choices
   - Punctuation habits

6. EXAMPLE REWRITES
   - Generic: "Our product is the best"
   - Our voice: [how we'd say it]
```

### Applying Voice to AI Drafts
```
Rewrite this content in our brand voice:

VOICE PROFILE: [Paste or reference voice profile]

ORIGINAL CONTENT:
[Paste AI draft]

Requirements:
- Maintain all key information
- Transform to match voice profile exactly
- Add examples in our style
- Adjust formality/tone
- Use our vocabulary preferences
```

---

## Ethical Considerations

### Disclosure Guidelines

**When to disclose AI use:**
- Academic content: Always
- Journalism: Always
- Product reviews: Always
- Bylined content: Recommended
- Marketing content: Generally not required
- Internal docs: Not required

### Avoiding Misinformation

```
After generating any factual content, verify:

1. Are statistics accurate and sourced?
2. Are quotes real and attributed correctly?
3. Are claims about competitors accurate?
4. Are technical details correct?
5. Are dates and events accurate?

Never publish AI-generated:
- Medical advice without review
- Legal advice without review
- Financial advice without review
- News without verification
```

### Copyright Considerations

- AI cannot create copyrighted works (current legal understanding)
- You own the output (in most jurisdictions)
- Don't train custom models on copyrighted content without license
- Be cautious with style copying (may infringe on voice)

---

## Workflow Templates

### Template 1: Weekly Blog Post

```yaml
trigger: every Monday 9am
steps:
  - get_keyword_from_calendar
  - generate_research_brief
  - generate_outline
  - human_approve_outline
  - generate_draft_section_by_section
  - run_quality_checks
  - human_review
  - optimize_for_seo
  - format_for_cms
  - schedule_publish
```

### Template 2: Daily Social Content

```yaml
trigger: daily 6am
steps:
  - get_content_calendar
  - for_each_scheduled_post:
    - expand_brief_to_full_post
    - generate_hashtags
    - create_image_prompt
  - add_to_scheduling_tool
  - slack_notify_for_review
```

### Template 3: Email Sequence Creation

```yaml
trigger: manual (new product launch)
input: product_brief
steps:
  - generate_customer_avatar
  - generate_email_sequence_outline
  - for_each_email:
    - generate_subject_lines (5 options)
    - generate_email_body
    - generate_preview_text
  - human_review_all
  - load_to_email_platform
```

### Template 4: Ad Copy Testing

```yaml
trigger: new_campaign_request
input: campaign_brief
steps:
  - generate_audience_angles (5)
  - for_each_angle:
    - generate_ad_copy_variations (3)
    - generate_image_briefs
  - review_and_select_best
  - create_in_ads_manager
  - set_up_ab_tests
```

---

## Summary

### Key Takeaways

1. **Match AI involvement to content type** - Not everything needs heavy automation
2. **Quality systems are non-negotiable** - Always have human review for public content
3. **Prompts are your leverage** - Invest in prompt engineering
4. **Voice consistency matters** - Create and enforce brand voice profiles
5. **Fact-check everything** - AI hallucinates; verify before publishing

### Cost Estimates

| Content Type | AI Model | Human Time | Total Cost |
|--------------|----------|------------|------------|
| Blog post (2000 words) | $0.50 | 30 min edit | ~$30 |
| Email sequence (5 emails) | $0.20 | 20 min review | ~$20 |
| Social posts (10) | $0.10 | 10 min review | ~$10 |
| Ad copy set (15 variations) | $0.15 | 15 min selection | ~$15 |
| Product descriptions (10) | $0.20 | 15 min review | ~$15 |

### Next Steps

1. Set up your content workflow in [n8n](../workflows/n8n/templates.md)
2. Create your brand voice profile
3. Build your prompt library
4. Establish your quality control process
5. Start with one content type, then expand
