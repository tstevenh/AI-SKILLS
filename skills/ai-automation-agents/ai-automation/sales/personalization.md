# AI Personalization at Scale

> Complete guide to personalizing sales outreach using AI: emails, LinkedIn, and multi-channel campaigns.

---

## Table of Contents

1. [The Personalization Spectrum](#the-personalization-spectrum)
2. [AI Personalization Strategies](#ai-personalization-strategies)
3. [Email Personalization](#email-personalization)
4. [LinkedIn Personalization](#linkedin-personalization)
5. [Outreach Tools Integration](#outreach-tools-integration)
6. [Quality Control](#quality-control)
7. [Templates and Prompts](#templates-and-prompts)

---

## The Personalization Spectrum

### Levels of Personalization

```
Level 0: No personalization
"Hi,
We help companies like yours improve sales..."

Level 1: Basic merge fields
"Hi {first_name},
I noticed {company} is in the {industry} space..."

Level 2: Segment-based
"Hi {first_name},
As a {title} at a {company_size} {industry} company, 
you're probably dealing with {pain_point}..."

Level 3: Individual research
"Hi {first_name},
I saw your recent post about {specific_topic}. 
Given {company}'s focus on {specific_initiative}..."

Level 4: AI-powered deep personalization
"Hi {first_name},
Congrats on {recent_achievement}. Your approach to 
{specific_thing_they_said} resonated with me. At 
{company}, with your {tech_stack} setup and focus on 
{business_priority}, I think {specific_value_prop}..."
```

### Personalization ROI

| Level | Effort/Email | Reply Rate | Best For |
|-------|--------------|------------|----------|
| 0 | 0 sec | 0.5% | Nobody |
| 1 | 0 sec | 1-2% | High volume |
| 2 | 0 sec | 3-5% | Segmented campaigns |
| 3 | 5-10 min | 10-15% | High-value targets |
| 4 (AI) | 30 sec | 8-12% | Scale + quality |

**The AI advantage:** Level 4 quality at Level 1-2 effort

---

## AI Personalization Strategies

### Data-Driven Personalization

What you can personalize based on:

| Data Point | Personalization |
|------------|-----------------|
| Company news | Congrats on [achievement] |
| Funding | Growth-focused messaging |
| Job postings | Address hiring challenges |
| Tech stack | Integration-specific value |
| LinkedIn posts | Reference their thoughts |
| Competitors | Competitive positioning |
| Industry trends | Relevant insights |
| Role/title | Pain point specific |

### The Personalization Stack

```
┌─────────────────────────────────────────────────────┐
│              PERSONALIZATION STACK                   │
├─────────────────────────────────────────────────────┤
│                                                      │
│  1. DATA COLLECTION                                  │
│     ├── Enrichment (Apollo, Clearbit)               │
│     ├── LinkedIn activity (Phantombuster)           │
│     └── News/triggers (Google Alerts, Clay)         │
│                                                      │
│  2. AI PROCESSING                                    │
│     ├── Summarize company                           │
│     ├── Identify pain points                        │
│     └── Generate personalization                    │
│                                                      │
│  3. MESSAGE GENERATION                               │
│     ├── First line                                  │
│     ├── Relevant problem                            │
│     ├── Specific value prop                         │
│     └── Call to action                              │
│                                                      │
│  4. DELIVERY                                         │
│     └── Outreach tool (Instantly, Apollo, etc.)    │
│                                                      │
└─────────────────────────────────────────────────────┘
```

---

## Email Personalization

### The Anatomy of a Personalized Email

```
Subject: {personalized_subject}

Hi {first_name},

{personalized_first_line} ← AI generated

{transition_to_problem}

{value_proposition} ← Tailored to their situation

{soft_cta}

{signature}
```

### First Line Generation

#### The Best First Lines Reference:

1. **Achievement/News**
   - "Congrats on [specific achievement]"
   - "Saw the news about [funding/acquisition/launch]"
   - "Your [award/recognition] caught my attention"

2. **Content/Thought Leadership**
   - "Your post about [topic] resonated with me"
   - "I appreciated your take on [specific point]"
   - "Your article on [topic] was spot-on"

3. **Company Observation**
   - "I noticed [company] recently [specific action]"
   - "Your job posts suggest [growth area]"
   - "The way you've [specific thing] is impressive"

4. **Shared Connection**
   - "I was talking to [mutual connection] about..."
   - "Fellow [school/company/community] member here"
   - "We both [shared interest/experience]"

5. **Industry Insight**
   - "With [industry trend], I imagine [challenge]"
   - "Given what's happening in [industry]..."
   - "Companies like [peer companies] are [doing X]"

### First Line Prompts

#### Prompt 1: News-Based
```
Write a personalized email opening line based on this company news:

Recipient: {name}, {title}
Company: {company}
Recent News: {news_headline}
News Summary: {news_summary}

Requirements:
- Reference the specific news
- Be congratulatory but not over-the-top
- Naturally transition to a business context
- Under 20 words
- Sound like a real person, not a template

Return only the first line.
```

#### Prompt 2: LinkedIn Activity
```
Write a personalized email opening based on this LinkedIn activity:

Recipient: {name}, {title} at {company}
Recent Post: "{post_excerpt}"
Post Topic: {topic}

Requirements:
- Reference something specific from their post
- Show you actually read and understood it
- Add a brief genuine reaction
- Under 25 words
- Don't be sycophantic

Return only the first line.
```

#### Prompt 3: Tech Stack Based
```
Write a personalized email opening based on their tech stack:

Recipient: {name}, {title}
Company: {company}
Their Tech Stack: {tools_list}
Our Product: {product_description}
Integration: We integrate with {relevant_tool}

Requirements:
- Reference their specific stack
- Hint at relevant integration
- Show you understand their workflow
- Under 25 words

Return only the first line.
```

#### Prompt 4: Role-Based
```
Write a personalized email opening based on their role:

Recipient: {name}
Title: {title}
Department: {department}
Company Type: {company_type} with {employee_count} employees
Industry: {industry}

Requirements:
- Acknowledge a challenge specific to their role
- Be empathetic, not presumptuous
- Show understanding of their priorities
- Under 25 words

Return only the first line.
```

### Full Email Generation

#### Email Template with AI Variables
```
Subject: {personalized_subject}

Hi {first_name},

{ai_first_line}

{role_based_problem_statement}

At [Company], we help {similar_companies} {achieve_result} 
by {how_we_do_it}.

{specific_value_for_their_situation}

Would you be open to a 15-minute call to see if this 
might help {company}?

Best,
[Name]
```

#### Full Email Prompt
```
Write a cold outreach email for:

RECIPIENT:
- Name: {name}
- Title: {title}
- Company: {company}

CONTEXT:
- Company size: {employees}
- Industry: {industry}
- Recent news: {news}
- Tech stack: {tech_stack}

OUR PRODUCT:
- We help: {target_customer}
- To achieve: {main_benefit}
- By: {how_we_do_it}

REQUIREMENTS:
- Personalized first line referencing their situation
- Identify a problem relevant to their role
- Connect our solution to their specific context
- Soft CTA (15-min call)
- Under 150 words
- Natural, conversational tone
- No hype or marketing speak

Return the complete email.
```

### Subject Line Generation

```
Generate 5 email subject lines for this cold email:

Recipient: {name}, {title} at {company}
Email purpose: {purpose}
Key hook: {main_personalization_point}

Requirements:
- Under 50 characters
- Create curiosity or relevance
- Include personalization where natural
- Avoid spam triggers
- Mix approaches: question, observation, intrigue

Return 5 subject lines, one per line.
```

---

## LinkedIn Personalization

### Connection Request Messages

**Character limit:** 300 characters

```
Prompt:
Write a LinkedIn connection request message:

Target: {name}, {title} at {company}
Reason for connecting: {reason}
Common ground: {shared_interest_or_connection}

Requirements:
- Under 280 characters (leave room)
- Specific reason for connecting
- No sales pitch
- Genuine and professional
- Include a small compliment or observation

Return only the message.
```

**Examples:**

```
Good:
"Hi {name}, your post on {topic} really resonated. 
I'm exploring similar approaches at {my_company}. 
Would love to connect and exchange ideas."

Bad:
"Hi {name}, I help companies like {company} increase 
revenue. Let's connect to discuss how we can help!"
```

### LinkedIn Message Sequences

**Message 1: Soft opener (Day 1)**
```
Hi {name},

{reference_to_something_specific}

I've been following {company}'s approach to {topic} - 
really interesting work.

{genuine_question_or_observation}

Curious to hear your thoughts.

{your_name}
```

**Message 2: Value add (Day 4)**
```
Hi {name},

Came across this {resource_type} that reminded me of 
your work on {topic}: {link}

Thought you might find it useful.

{your_name}
```

**Message 3: Soft pitch (Day 7)**
```
Hi {name},

I've been thinking about the challenges {titles like yours} 
face with {specific_challenge}.

We've been helping companies like {similar_company} 
{achieve_specific_result}.

Would you be open to a quick chat to see if we might 
be able to help {company} with {specific_thing}?

{your_name}
```

### LinkedIn Prompt Templates

#### InMail Template
```
Write a LinkedIn InMail for:

Target: {name}, {title} at {company}
Goal: {book_meeting / start_conversation / share_resource}
Hook: {personalization_point}
Our value prop: {what_we_offer}

Requirements:
- Personalized opening
- Clear but soft ask
- Under 200 words
- Professional but human
- One clear CTA

Return the complete InMail.
```

---

## Outreach Tools Integration

### Popular Tools

| Tool | Best For | Personalization Features |
|------|----------|-------------------------|
| Instantly | Email at scale | Custom variables, AI warmup |
| Smartlead | Advanced sequences | AI-generated emails |
| Apollo | All-in-one | Built-in AI assist |
| Outreach.io | Enterprise | Sentiment analysis |
| Salesloft | Enterprise | Cadence optimization |
| Lemlist | Creative emails | Image personalization |

### Integration Patterns

#### Clay → Instantly

```
Clay workflow:
1. Enrich leads
2. AI generate personalization
3. Export CSV with custom columns

Instantly:
1. Import CSV
2. Map columns to variables
3. Use {{custom_field}} in templates
```

#### n8n → Email Tool

```yaml
# n8n workflow
trigger: new_lead

steps:
  - enrich_lead
  - generate_personalization:
      prompt: "Write first line..."
      model: claude-3-5-sonnet
  - add_to_outreach:
      tool: instantly
      custom_variables:
        first_line: "{{ $json.ai_first_line }}"
        company_context: "{{ $json.ai_company_summary }}"
```

### CSV Structure for Import

```csv
email,first_name,company,title,ai_first_line,ai_subject,ai_value_prop
john@co.com,John,Acme,VP Marketing,"Congrats on the Series B...","Quick thought on Acme's growth","Given your focus on PLG..."
```

---

## Quality Control

### Common AI Personalization Failures

| Failure | Example | Fix |
|---------|---------|-----|
| Over-familiarity | "John! Buddy!" | Set professional tone |
| Generic | "Love what you're doing" | Require specifics |
| Factual errors | Wrong company name | Validate data first |
| Awkward phrasing | "I couldn't help but notice..." | Test and refine prompts |
| Sycophantic | "Your incredible work..." | Tone down compliments |
| Too long | 300 word first line | Set length limits |

### Quality Checklist

```markdown
## Personalization Quality Check

Before sending, verify:

### Accuracy
- [ ] Name spelled correctly
- [ ] Company name correct
- [ ] Title accurate
- [ ] Referenced news/post is real
- [ ] No competitor company mentioned accidentally

### Relevance
- [ ] First line references something specific
- [ ] Problem statement fits their role
- [ ] Value prop relevant to their situation
- [ ] CTA appropriate for relationship stage

### Tone
- [ ] Professional but human
- [ ] Not overly salesy
- [ ] Compliments are genuine, not excessive
- [ ] Length appropriate (under 150 words)

### Technical
- [ ] No broken variables ({{name}})
- [ ] Links work
- [ ] Signature correct
```

### Review Workflow

```
AI generates → Automated checks → Sample human review → Send

Automated checks:
- Length limits
- No broken variables
- No banned words (guarantee, limited time, etc.)
- Company name in email matches recipient

Human review:
- Spot check 5% of emails
- Review any flagged by automated system
- Weekly calibration on AI quality
```

---

## Templates and Prompts

### Master Personalization Prompt

```
You are an expert cold email writer. Generate personalized 
outreach copy for:

RECIPIENT INFO:
Name: {name}
Title: {title}
Company: {company}
Industry: {industry}
Company size: {employees} employees
Recent news: {news}
LinkedIn activity: {recent_posts}
Tech stack: {tech_stack}

MY COMPANY:
Product: {product}
Target customer: {icp}
Main benefit: {value_prop}
Social proof: {proof}

GENERATE:
1. subject_line: Under 50 chars, creates curiosity
2. first_line: Under 25 words, references specific detail
3. problem: 1-2 sentences about their likely challenge
4. value_prop: How we specifically help companies like theirs
5. cta: Soft ask for 15-min call

FORMAT as JSON:
{
  "subject_line": "",
  "first_line": "",
  "problem": "",
  "value_prop": "",
  "cta": ""
}

STYLE:
- Natural and human
- Professional but not corporate
- Specific, not generic
- Confident but not arrogant
- Focus on them, not us
```

### Batch Personalization Prompt

```
Generate personalized first lines for these leads:

Context: We sell {product} to {target_customer}

Leads:
{lead_data_array}

For each lead, generate:
- first_line: Specific, genuine opener
- angle: What hook you used (news/tech/role/etc)

Return as JSON array.
```

### Follow-Up Personalization

```
Write a follow-up email to someone who didn't respond:

Original email sent: {days_ago} days ago
Original subject: {subject}
Original first line: {first_line}

Requirements:
- Acknowledge the first email
- Add new value (insight, resource, case study)
- Don't be pushy
- Different angle than first email
- Under 100 words

Return the complete follow-up email.
```

---

## Summary

### Personalization Playbook

1. **Collect data** - Enrichment + social signals
2. **Identify hooks** - News, posts, tech, role
3. **Generate first line** - AI with specific prompts
4. **Build full message** - Template + AI variables
5. **Quality check** - Automated + human
6. **Deliver** - Outreach tool integration
7. **Iterate** - Track what works, improve prompts

### Cost Analysis

| Component | Monthly Cost | Per Email |
|-----------|--------------|-----------|
| Enrichment (Clay) | $300 | $0.15 |
| AI (Claude/GPT) | $50 | $0.02 |
| Email tool | $100 | $0.05 |
| **Total** | **$450** | **$0.22** |

For 2,000 emails/month: $0.22/email vs $5+ for human-written

### Next Steps

1. Set up enrichment pipeline
2. Create prompt library
3. Test with small batch
4. Measure response rates
5. Iterate on prompts
6. Scale up

See [chatbots.md](chatbots.md) for AI sales chatbots →
