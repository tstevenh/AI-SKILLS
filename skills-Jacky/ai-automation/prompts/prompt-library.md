# AI Prompt Library

> Comprehensive collection of tested, production-ready prompts organized by use case.

---

## Table of Contents

1. [Content Generation](#content-generation)
2. [Data Processing](#data-processing)
3. [Sales & Marketing](#sales--marketing)
4. [Customer Support](#customer-support)
5. [Research & Analysis](#research--analysis)
6. [Operations](#operations)
7. [Code & Technical](#code--technical)
8. [Prompt Engineering Tips](#prompt-engineering-tips)

---

## Content Generation

### Blog Post Writing

#### Full Article Generator
```
Write a comprehensive blog post on [TOPIC].

TARGET KEYWORD: [keyword]
WORD COUNT: [number]
AUDIENCE: [description]
TONE: [professional/casual/authoritative]
GOAL: [educate/convert/engage]

STRUCTURE:
- Hook opening that addresses reader's pain point
- Clear thesis in first paragraph
- H2 sections with H3 subsections
- Include specific examples and data
- FAQ section with 5 questions
- Strong conclusion with CTA

REQUIREMENTS:
- Keyword in first 100 words
- Keyword in 2-3 H2 headings naturally
- Include 3-5 internal linking opportunities (mark as [LINK: topic])
- Include 2-3 external reference suggestions
- Write for featured snippet for main question
- Avoid: clichés, passive voice, filler phrases
- Include: specific numbers, real examples, actionable advice

OUTPUT FORMAT:
## [Title with keyword]

[Article content with markdown formatting]

---
META TITLE: [under 60 chars]
META DESCRIPTION: [150-160 chars]
SLUG: [url-friendly]
TAGS: [comma-separated]
```

#### Content Repurposing
```
Transform this content into multiple formats:

ORIGINAL CONTENT:
[paste content]

CREATE:

1. TWITTER THREAD (7-10 tweets)
- Hook in first tweet
- One key point per tweet
- End with CTA
- Under 280 chars each

2. LINKEDIN POST
- Professional tone
- Use line breaks
- Under 1300 chars
- End with question

3. EMAIL NEWSLETTER SECTION
- Casual, friendly tone
- 150-200 words
- Include link to full content

4. INSTAGRAM CAROUSEL OUTLINE
- 7-10 slides
- Headline + key point per slide
- Visual suggestions

5. YOUTUBE VIDEO SCRIPT OUTLINE
- Hook (first 10 seconds)
- Main points
- CTA
- Estimated length

For each, maintain the core message but adapt to platform conventions.
```

#### Email Copy Generator
```
Write a [TYPE] email:

TYPE: [welcome/nurture/sales/re-engagement/announcement]
RECIPIENT: [description]
RELATIONSHIP: [new subscriber/lead/customer/churned]
GOAL: [open/click/reply/convert]
TONE: [professional/friendly/urgent]

CONTEXT:
[Any relevant context]

REQUIREMENTS:
- Subject line options (5)
- Preview text
- Body under [X] words
- One clear CTA
- PS line for important emails

OUTPUT:
SUBJECT: [5 options with char counts]
PREVIEW: [under 90 chars]

[Email body]

PS: [if applicable]
```

### Social Media Content

#### LinkedIn Post Generator
```
Write a LinkedIn post about [TOPIC]:

AUTHOR: [name, title]
GOAL: [thought leadership/engagement/leads/awareness]
AUDIENCE: [who follows this person]
INCLUDE: [specific points to make]

REQUIREMENTS:
- Strong hook in first line (shows before "see more")
- Use line breaks for readability
- Personal perspective/story
- Actionable insight or takeaway
- End with engagement question or CTA
- Under 1300 characters
- 3 hashtags (mix popular and niche)
- Suggest image/graphic idea

AVOID:
- Starting with "I"
- Corporate speak
- Being preachy
- Humble bragging
```

#### Twitter/X Thread Generator
```
Create a Twitter thread about [TOPIC]:

GOAL: [educate/entertain/promote/engage]
AUDIENCE: [who will read this]
EXPERTISE LEVEL: [beginner/intermediate/expert]

STRUCTURE:
Tweet 1: HOOK
- Bold claim, question, or intriguing statement
- Must stop the scroll
- Under 200 chars (leave room for engagement)

Tweets 2-8: CONTENT
- One key point per tweet
- Use numbers and specifics
- Include examples
- Add visual suggestions where helpful

Tweet 9: SUMMARY
- Recap key points
- Restate main benefit

Tweet 10: CTA
- Ask for retweet/follow
- Link to resource
- Engagement question

RULES:
- Each tweet under 280 chars
- Can use threads well on their own
- No excessive emojis
- No hashtags mid-thread (only end if any)
```

---

## Data Processing

### Data Extraction

#### Invoice Extraction
```
Extract all data from this invoice:

[Invoice image or text]

Return JSON with this exact structure:
{
  "vendor": {
    "name": "",
    "address": "",
    "city": "",
    "state": "",
    "zip": "",
    "phone": "",
    "email": "",
    "website": "",
    "tax_id": ""
  },
  "customer": {
    "name": "",
    "address": "",
    "account_number": ""
  },
  "invoice_details": {
    "invoice_number": "",
    "invoice_date": "",
    "due_date": "",
    "po_number": "",
    "terms": ""
  },
  "line_items": [
    {
      "description": "",
      "quantity": 0,
      "unit": "",
      "unit_price": 0.00,
      "discount": 0.00,
      "tax": 0.00,
      "total": 0.00
    }
  ],
  "totals": {
    "subtotal": 0.00,
    "discount": 0.00,
    "tax_rate": "",
    "tax_amount": 0.00,
    "shipping": 0.00,
    "total": 0.00,
    "amount_paid": 0.00,
    "balance_due": 0.00
  },
  "payment_info": {
    "methods_accepted": [],
    "bank_details": "",
    "payment_instructions": ""
  },
  "notes": "",
  "confidence_score": 0-100,
  "unclear_fields": []
}

Rules:
- Use null for missing fields, not empty strings
- Dates in YYYY-MM-DD format
- Amounts as numbers, not strings
- Flag any unclear or ambiguous data
```

#### Email Parsing
```
Parse this email and extract structured data:

EMAIL:
From: [from]
To: [to]
Subject: [subject]
Date: [date]
Body:
[body]

Return JSON:
{
  "email_type": "order|inquiry|support|notification|newsletter|personal|spam|other",
  "priority": "high|medium|low",
  "sentiment": "positive|neutral|negative",
  "action_required": true|false,
  "action_type": "",
  
  "extracted_data": {
    // Depends on email_type
    // For orders:
    "order_number": "",
    "items": [],
    "total": 0,
    
    // For inquiries:
    "question": "",
    "topic": "",
    "deadline": "",
    
    // For support:
    "issue": "",
    "product": "",
    "urgency": ""
  },
  
  "entities": {
    "people": [],
    "companies": [],
    "dates": [],
    "amounts": [],
    "phone_numbers": [],
    "addresses": []
  },
  
  "summary": "",
  "suggested_response": ""
}
```

### Data Transformation

#### Address Normalization
```
Normalize this address to USPS standard format:

INPUT: "[address string]"

Return JSON:
{
  "original": "",
  "parsed": {
    "street_number": "",
    "street_name": "",
    "street_type": "",  // ST, AVE, BLVD, etc.
    "unit_type": "",    // APT, STE, UNIT, etc.
    "unit_number": "",
    "city": "",
    "state": "",        // 2-letter code
    "zip": "",          // 5-digit
    "zip4": "",         // 4-digit extension
    "country": "US"
  },
  "normalized": {
    "line1": "",
    "line2": "",
    "city_state_zip": ""
  },
  "formatted": "",      // Single line
  "is_valid": true|false,
  "validation_issues": [],
  "suggestions": []
}

Rules:
- Expand abbreviations (ST → STREET, AVE → AVENUE)
- Uppercase everything
- Standard formatting
- Flag potential issues
```

#### Name Parsing
```
Parse this name into components:

INPUT: "[full name]"

Return JSON:
{
  "original": "",
  "parsed": {
    "prefix": "",       // Dr., Mr., Mrs., etc.
    "first_name": "",
    "middle_name": "",
    "last_name": "",
    "suffix": "",       // Jr., III, PhD, etc.
    "nickname": ""      // If in quotes or parentheses
  },
  "formatted": {
    "full_name": "",
    "formal": "",       // Mr. John Smith Jr.
    "casual": "",       // John
    "professional": "", // J. Smith
    "sortable": ""      // Smith, John
  },
  "gender_guess": "",
  "confidence": 0-100,
  "notes": ""
}

Handle edge cases:
- Multiple last names (hyphenated, Spanish style)
- East Asian name order
- Single names (mononyms)
- Nicknames in quotes or parentheses
- Titles and credentials
```

---

## Sales & Marketing

### Lead Qualification

#### Lead Scoring Prompt
```
Score this lead based on our ICP:

OUR ICP:
- Company size: [range] employees
- Industry: [industries]
- Revenue: [range]
- Technology: Uses [tools]
- Role: [titles]
- Location: [regions]

LEAD DATA:
[lead information]

Score (1-100) based on:

COMPANY FIT (0-35 points):
- Size match: 0-15
- Industry match: 0-10
- Revenue match: 0-10

CONTACT FIT (0-35 points):
- Title/seniority: 0-15
- Department: 0-10
- Decision authority: 0-10

TIMING/INTENT (0-30 points):
- Urgency signals: 0-10
- Budget indicators: 0-10
- Technology fit: 0-10

Return JSON:
{
  "total_score": 0,
  "grade": "A|B|C|D|F",
  "breakdown": {
    "company_fit": 0,
    "contact_fit": 0,
    "timing_intent": 0
  },
  "reasoning": "",
  "red_flags": [],
  "green_flags": [],
  "recommended_action": "hot_pursuit|nurture|disqualify",
  "personalization_hooks": []
}
```

### Email Personalization

#### First Line Generator
```
Write a personalized email first line for:

RECIPIENT:
- Name: [name]
- Title: [title]
- Company: [company]
- Industry: [industry]

CONTEXT (use one):
- Recent news: [news item]
- LinkedIn post: [post summary]
- Company announcement: [announcement]
- Job posting: [posting]
- Mutual connection: [connection]
- Shared interest: [interest]

REQUIREMENTS:
- Reference something specific
- Be genuine, not sycophantic
- Natural transition to email purpose
- Under 25 words
- No "I noticed" or "I came across"

OUR PRODUCT: [brief description]

Generate 3 options with different angles.
```

#### Sales Email Generator
```
Write a cold sales email:

RECIPIENT:
[Lead data]

OUR PRODUCT:
[Product description]

EMAIL TYPE: [first touch/follow-up/breakup]
GOAL: [meeting/demo/reply]

PERSONALIZATION HOOK:
[Specific detail to reference]

STRUCTURE:
1. Personalized first line (reference hook)
2. Problem statement (their likely pain)
3. Solution teaser (how we help)
4. Social proof (brief)
5. Soft CTA

REQUIREMENTS:
- Under 125 words
- No links in first email
- Conversational tone
- Clear but soft ask
- PS line with additional hook

Generate email + 3 subject line options.
```

### Ad Copy

#### Facebook Ad Generator
```
Generate Facebook ad copy variations:

PRODUCT: [product/service]
TARGET AUDIENCE: [detailed audience]
CAMPAIGN GOAL: [awareness/traffic/conversions]
OFFER: [if any]

Generate 5 variations with different angles:

1. PAIN-FOCUSED
Primary text: [under 125 chars above fold]
Headline: [under 40 chars]
Description: [under 30 chars]
Angle explanation:

2. BENEFIT-FOCUSED
[Same structure]

3. SOCIAL PROOF-FOCUSED
[Same structure]

4. CURIOSITY-DRIVEN
[Same structure]

5. DIRECT/CLEAR
[Same structure]

For each, include:
- Suggested image direction
- Audience this works best for
- A/B testing suggestions
```

---

## Customer Support

### Ticket Classification

#### Support Ticket Classifier
```
Classify this support ticket:

TICKET:
Subject: [subject]
Body: [body]
Customer: [customer info if available]

Return JSON:
{
  "category": "billing|technical|shipping|account|product|general",
  "subcategory": "",
  "priority": "urgent|high|medium|low",
  "sentiment": "positive|neutral|negative|frustrated",
  "complexity": "simple|moderate|complex",
  
  "requires_action": true|false,
  "action_type": "refund|replacement|investigation|information|escalation",
  
  "auto_resolvable": true|false,
  "auto_resolve_reason": "",
  
  "entities": {
    "order_number": "",
    "product": "",
    "date_mentioned": "",
    "amount": ""
  },
  
  "key_issues": [],
  "customer_ask": "",
  "suggested_response_type": "template|personalized|escalate",
  "routing": "team_name"
}
```

### Response Generation

#### Support Response Generator
```
Draft a support response for this ticket:

TICKET:
[ticket content]

CLASSIFICATION:
Category: [category]
Sentiment: [sentiment]
Customer type: [new/existing/vip]

RELEVANT KNOWLEDGE:
[Knowledge base excerpts or policies]

RESPONSE REQUIREMENTS:
- Acknowledge their issue
- Apologize if frustrated
- Provide clear solution/next steps
- Offer additional help
- Match their tone (formal if they're formal, casual if they're casual)
- Under [X] words

COMPANY GUIDELINES:
[Any specific requirements]

Generate:
1. The response
2. Confidence score (0-100) for auto-send
3. Flag any escalation needs
4. Internal notes for agent
```

---

## Research & Analysis

### Company Research

#### Company Deep Dive
```
Research [COMPANY] and provide comprehensive analysis:

Known information:
- Website: [url]
- Industry: [industry]
- Founded: [year]

RESEARCH:

## Company Overview
- Business model
- Products/services
- Revenue model
- Size and scale

## Market Position
- Target market
- Competitive advantages
- Market share estimate
- Key competitors

## Recent Developments
- News (last 12 months)
- Product launches
- Leadership changes
- Funding/acquisitions

## Strategic Direction
- Based on job postings
- Based on recent moves
- Based on leadership comments

## SWOT Analysis
- Strengths
- Weaknesses
- Opportunities
- Threats

## Implications for [OUR COMPANY]
- How they compete with us
- Partnership opportunities
- Lessons to learn

Format as detailed report. Cite sources where possible.
```

### Market Analysis

#### Market Sizing
```
Estimate the market size for [PRODUCT/SERVICE]:

GEOGRAPHY: [region]
YEAR: [year]

APPROACH:

1. TOP-DOWN
- Start with: [broader market]
- Apply filters: [relevant segments]
- Calculate: [TAM → SAM → SOM]

2. BOTTOM-UP
- Number of potential customers: 
- Average spend per customer:
- Total market calculation:

3. COMPETITOR-BASED
- Known competitor revenues:
- Estimated market shares:
- Implied market size:

OUTPUT:
{
  "tam": {
    "value": "$X",
    "description": "",
    "methodology": ""
  },
  "sam": {
    "value": "$X",
    "description": "",
    "methodology": ""
  },
  "som": {
    "value": "$X",
    "description": "",
    "methodology": ""
  },
  "growth_rate": "X% CAGR",
  "key_assumptions": [],
  "data_sources": [],
  "confidence_level": "high|medium|low",
  "sensitivity_analysis": ""
}
```

---

## Operations

### Meeting Processing

#### Meeting Summary Generator
```
Generate a meeting summary from this transcript:

TRANSCRIPT:
[transcript]

MEETING CONTEXT:
- Type: [type]
- Attendees: [list]
- Purpose: [purpose]

OUTPUT:

## Meeting Summary

**Date:** [extract from transcript]
**Duration:** [extract]
**Attendees:** [list]

### Executive Summary
[3-5 sentence overview]

### Key Discussion Points
1. [Point 1]
   - [Detail]
   - [Decision if any]

2. [Point 2]
   - [Detail]
   - [Decision if any]

### Decisions Made
- [Decision 1]
- [Decision 2]

### Action Items
| Action | Owner | Due Date | Notes |
|--------|-------|----------|-------|
| [Action] | [Who] | [When] | [Context] |

### Follow-Up Required
- [Item 1]
- [Item 2]

### Open Questions
- [Question 1]
- [Question 2]

### Next Steps
- [Step 1]
- [Step 2]

---
**Next Meeting:** [if mentioned]
**Notes compiled by:** AI Assistant
```

### Process Documentation

#### SOP Generator
```
Create a Standard Operating Procedure for: [PROCESS]

CONTEXT:
- Department: [department]
- Frequency: [how often]
- Current issues: [problems to address]

OUTPUT:

# [Process Name] SOP

**Version:** 1.0
**Effective Date:** [date]
**Owner:** [role]
**Reviewers:** [roles]

## Purpose
[Why this process exists]

## Scope
[What this covers and doesn't cover]

## Prerequisites
- [ ] [Requirement 1]
- [ ] [Requirement 2]

## Tools/Systems Required
- [Tool 1] - [purpose]
- [Tool 2] - [purpose]

## Step-by-Step Procedure

### Step 1: [Name]
**Owner:** [role]
**Time:** [estimate]

1. [Sub-step 1]
2. [Sub-step 2]

**Expected output:** [what success looks like]
**Common issues:** [what could go wrong]

### Step 2: [Name]
[Continue pattern]

## Exceptions
- **If [condition]:** [what to do]
- **If [condition]:** [what to do]

## Escalation
- **Level 1:** [who to contact]
- **Level 2:** [who to contact]

## Quality Checklist
- [ ] [Check 1]
- [ ] [Check 2]

## Metrics
- [Metric 1] - Target: [target]
- [Metric 2] - Target: [target]

## Revision History
| Date | Version | Changes | Author |
|------|---------|---------|--------|
```

---

## Code & Technical

### Code Generation

#### Function Generator
```
Generate a [LANGUAGE] function for:

TASK: [description]
INPUTS: [list with types]
OUTPUT: [expected output]

REQUIREMENTS:
- Error handling
- Input validation
- Logging (optional)
- Tests (optional)
- Documentation

STYLE:
- Follow [style guide]
- Use [patterns]

Generate:
1. The function with docstring
2. Example usage
3. Edge cases to consider
4. Unit tests
```

### Documentation

#### API Documentation
```
Generate API documentation for this endpoint:

ENDPOINT: [method] [path]
DESCRIPTION: [what it does]

CODE/SPEC:
[code or OpenAPI spec]

Generate:

# [Endpoint Name]

[Brief description]

## Request

### URL
```
[METHOD] [path]
```

### Headers
| Header | Required | Description |
|--------|----------|-------------|

### Parameters
| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|

### Request Body
```json
[Example request]
```

## Response

### Success Response (200)
```json
[Example response]
```

### Error Responses
| Status | Description | Body |
|--------|-------------|------|

## Examples

### cURL
```bash
[Example]
```

### Python
```python
[Example]
```

### JavaScript
```javascript
[Example]
```

## Notes
- [Important note 1]
- [Important note 2]
```

---

## Prompt Engineering Tips

### Structure Your Prompts

```
1. ROLE/CONTEXT
   "You are a [role] with expertise in [domain]"

2. TASK
   "Your task is to [specific action]"

3. INPUT SPECIFICATION
   "Given the following: [format of input]"

4. OUTPUT SPECIFICATION
   "Return [format] with the following structure:"

5. CONSTRAINTS
   "Requirements: [list]"
   "Avoid: [list]"

6. EXAMPLES (if helpful)
   "Example input: [example]"
   "Example output: [example]"
```

### Key Principles

1. **Be specific** - Vague prompts get vague results
2. **Show, don't tell** - Examples beat descriptions
3. **Constrain appropriately** - Limits improve output
4. **Iterate** - First prompt is rarely optimal
5. **Test with variations** - Edge cases reveal issues

### Common Patterns

**Chain of Thought:**
```
Think through this step by step:
1. First, consider...
2. Then, analyze...
3. Finally, conclude...
```

**Role Playing:**
```
You are an expert [role] with 20 years of experience in [domain].
Respond as this expert would.
```

**Few-Shot Learning:**
```
Here are examples of the task:

Input: [example 1]
Output: [example 1]

Input: [example 2]
Output: [example 2]

Now complete:
Input: [actual input]
Output:
```

**Self-Consistency:**
```
Generate 3 different approaches to this problem.
Then evaluate each and select the best one with reasoning.
```

---

## Summary

This prompt library provides templates for common automation tasks. Customize based on your specific needs and iterate based on results.

### Usage Tips

1. **Start with templates** - Modify rather than create from scratch
2. **Version control** - Track what works
3. **Test systematically** - Validate with real data
4. **Document learnings** - Note what works for future reference

See [../workflows/](../workflows/) for how to use these prompts in automation workflows.
