# AI Lead Enrichment Deep Dive

> Complete guide to automating lead enrichment: finding data, qualifying prospects, and building enrichment workflows.

---

## Table of Contents

1. [Lead Enrichment Fundamentals](#lead-enrichment-fundamentals)
2. [Data Sources and Providers](#data-sources-and-providers)
3. [Clay Workflows](#clay-workflows)
4. [Building Enrichment Pipelines](#building-enrichment-pipelines)
5. [AI-Powered Qualification](#ai-powered-qualification)
6. [Automation Templates](#automation-templates)
7. [Cost Optimization](#cost-optimization)

---

## Lead Enrichment Fundamentals

### What is Lead Enrichment?

Lead enrichment is the process of augmenting basic lead data (email, name) with additional information to:

1. **Qualify leads** - Determine if they're worth pursuing
2. **Personalize outreach** - Craft relevant messages
3. **Route appropriately** - Send to right sales rep/segment
4. **Score leads** - Prioritize follow-up

### The Enrichment Spectrum

```
Basic Lead              →              Fully Enriched Lead
────────────────────────────────────────────────────────────
email@company.com          email@company.com
                           Name: John Smith
                           Title: VP of Marketing
                           Company: Acme Corp
                           Company Size: 50-200
                           Industry: SaaS
                           Revenue: $10M-50M
                           Tech Stack: Salesforce, HubSpot
                           LinkedIn: linkedin.com/in/johnsmith
                           Recent News: Series B funding
                           Mobile: +1 555-123-4567
                           Score: 85/100
                           Personalization: "Congrats on Series B!"
```

### ROI of Enrichment

**Without enrichment:**
- Send generic emails
- 1% response rate
- Waste time on bad-fit leads
- No personalization

**With enrichment:**
- Targeted, personalized outreach
- 5-15% response rate
- Focus on qualified leads
- Relevant conversations

**Math:**
- 1,000 leads/month
- Without: 10 responses → 2 meetings → 1 deal ($5k)
- With: 80 responses → 20 meetings → 5 deals ($25k)
- Enrichment cost: $500
- ROI: 40x

---

## Data Sources and Providers

### Data Categories

| Category | What It Includes | Primary Sources |
|----------|------------------|-----------------|
| Contact | Name, email, phone, LinkedIn | Apollo, Hunter, Lusha |
| Company | Size, revenue, industry | Clearbit, ZoomInfo, Apollo |
| Technographic | Tools/stack used | BuiltWith, Wappalyzer, Slintel |
| Intent | Buying signals | Bombora, G2, 6sense |
| Social | Posts, activity, engagement | Phantombuster, LinkedIn |
| News | Funding, hires, announcements | Crunchbase, Google News |

### Provider Deep Dive

#### Apollo.io

**Best for:** Contact data, all-in-one

**Data Coverage:**
- 265M+ contacts
- 60M+ companies
- Email verification included
- Phone numbers
- LinkedIn profiles

**Pricing:**
| Plan | Monthly | Email Credits |
|------|---------|---------------|
| Free | $0 | 10,000 |
| Basic | $59 | 120,000/year |
| Professional | $99 | 240,000/year |
| Organization | $149 | 480,000/year |

**API Example:**
```python
import requests

response = requests.post(
    "https://api.apollo.io/v1/people/match",
    headers={"X-Api-Key": api_key},
    json={
        "email": "john@company.com"
    }
)

person = response.json()["person"]
# Returns: name, title, company, linkedin, phone, etc.
```

#### Clearbit

**Best for:** Company data, real-time enrichment

**Data Coverage:**
- Company firmographics
- Employee count
- Revenue estimates
- Tech stack (partial)
- Social profiles

**Pricing:** Credit-based, starts ~$99/month

**API Example:**
```python
import clearbit

clearbit.key = api_key

# Enrich from email
person = clearbit.Enrichment.find(email="john@company.com")

# Company lookup
company = clearbit.Company.find(domain="company.com")
```

#### Hunter.io

**Best for:** Email finding and verification

**Pricing:**
| Plan | Monthly | Searches | Verifications |
|------|---------|----------|---------------|
| Free | $0 | 25 | 50 |
| Starter | $49 | 500 | 1,000 |
| Growth | $149 | 5,000 | 10,000 |
| Business | $499 | 50,000 | 100,000 |

**API Example:**
```python
import requests

# Find email
response = requests.get(
    "https://api.hunter.io/v2/email-finder",
    params={
        "domain": "company.com",
        "first_name": "John",
        "last_name": "Smith",
        "api_key": api_key
    }
)

# Verify email
response = requests.get(
    "https://api.hunter.io/v2/email-verifier",
    params={
        "email": "john@company.com",
        "api_key": api_key
    }
)
```

#### BuiltWith

**Best for:** Technology stack identification

**What it detects:**
- CMS (WordPress, Shopify, etc.)
- Analytics (GA, Mixpanel)
- Marketing tools (HubSpot, Marketo)
- Hosting infrastructure
- Payment processors

**Pricing:** Starts ~$295/month for API

#### ZoomInfo

**Best for:** Enterprise, most comprehensive

**Data Coverage:**
- Most extensive database
- Direct dials
- Org charts
- Intent data
- Technographics

**Pricing:** Enterprise only (~$15k+/year)

### Provider Selection Matrix

| Need | Budget | Recommended |
|------|--------|-------------|
| Contact finding | Low | Apollo (free tier) |
| Contact finding | Medium | Apollo or Hunter |
| Company data | Low | Clearbit Reveal |
| Company data | Medium | Clearbit or Apollo |
| Tech stack | Any | BuiltWith or Wappalyzer |
| Enterprise | High | ZoomInfo |
| All-in-one | Any | Clay (aggregates all) |

---

## Clay Workflows

### Why Clay?

Clay is the most powerful tool for lead enrichment because it:

1. **Aggregates 100+ data sources** - Query multiple providers
2. **Waterfall logic** - Try cheap sources first
3. **AI columns** - Transform data with AI
4. **Visual workflow** - Easy to build
5. **Automation** - Trigger on new leads

### Clay Fundamentals

#### Tables
A table is a list of leads/contacts with columns for each data point.

#### Enrichment Columns
Click "Enrich" to add data:
- Find email
- Get company info
- Get LinkedIn profile
- Find phone number
- And 100+ more options

#### Waterfall Enrichment
Set up fallback logic:
```
Try Apollo (cheapest)
  → Found? Done
  → Not found? Try Clearbit
    → Found? Done
    → Not found? Try ZoomInfo
```

#### AI Columns
Use GPT-4/Claude to:
- Write personalized first lines
- Summarize company descriptions
- Categorize leads
- Generate talking points

### Clay Workflow Examples

#### Workflow 1: Inbound Lead Enrichment

**Trigger:** New form submission

```
1. Import lead (email, name)

2. Find company
   - Extract domain from email
   - Clearbit company lookup
   - Get: size, industry, revenue

3. Enrich contact
   - Apollo person search
   - Get: title, LinkedIn, phone

4. Find tech stack
   - BuiltWith lookup
   - Get: tools they use

5. Qualify with AI
   - Prompt: "Score this lead 1-100 based on: 
     [criteria]. Return score and reasoning."
   - Inputs: company size, industry, title

6. Generate personalization
   - Prompt: "Write a personalized first line..."
   - Use company news, tech stack, title

7. Export
   - Push to CRM (HubSpot/Salesforce)
   - Alert Slack if score > 80
```

#### Workflow 2: LinkedIn Sales Nav → Outreach

**Trigger:** Import from LinkedIn Sales Navigator

```
1. Import LinkedIn profiles

2. Find emails (waterfall)
   - Try Apollo
   - Try Hunter
   - Try Snov.io
   - Try GetProspect

3. Verify email
   - Hunter verification
   - Remove invalid

4. Company enrichment
   - Clearbit or Apollo
   - Get company details

5. Recent activity
   - LinkedIn posts (via Phantombuster)
   - Company news (Google News API)

6. AI personalization
   - Reference recent post/news
   - Connect to value prop

7. Export to sequence
   - Push to Instantly/Smartlead
   - With personalized fields
```

#### Workflow 3: Account-Based Enrichment

**Goal:** Enrich target account list with decision makers

```
1. Import target companies (domain list)

2. Company enrichment
   - Clearbit company data
   - BuiltWith tech stack
   - Crunchbase funding data

3. Find decision makers
   - Apollo people search
   - Filter: VP+, Marketing/Sales/Ops
   - Get 3-5 contacts per company

4. Enrich contacts
   - Full Apollo data
   - LinkedIn profiles
   - Email verification

5. AI account brief
   - Summarize company
   - Identify pain points
   - Map to your solution

6. Export
   - Per-account spreadsheets
   - CRM account records
```

### Clay AI Prompts

#### Lead Qualification
```
Score this lead from 1-100 based on fit with our ICP:

Our ICP:
- Company size: 50-500 employees
- Industry: SaaS, E-commerce, or Professional Services
- Revenue: $5M-100M
- Uses: Salesforce or HubSpot
- Role: VP or Director of Marketing/Growth

Lead Information:
- Company: {company}
- Employees: {employee_count}
- Industry: {industry}
- Revenue: {revenue}
- Tech Stack: {tech_stack}
- Title: {title}

Return ONLY a JSON object:
{"score": [number], "reason": "[brief explanation]", "priority": "high/medium/low"}
```

#### First Line Generation
```
Write a personalized email opening line for:

Recipient: {name}
Title: {title}
Company: {company}
Recent News: {news}
Their Tech Stack: {tech_stack}

Requirements:
- Reference something specific (news, tech, role)
- Be genuine, not sycophantic
- Under 20 words
- Natural, like a real person wrote it
- Connect to why they might care about [your product]

Return only the first line.
```

#### Company Summary
```
Based on this information, write a 2-sentence company summary 
for a sales rep to quickly understand this prospect:

Company: {company}
Website: {website}
Industry: {industry}
Size: {size}
Description: {description}
Funding: {funding}

Focus on: What they do, who they serve, current stage/momentum.
```

---

## Building Enrichment Pipelines

### n8n Enrichment Workflow

```yaml
# Trigger: Webhook from form/CRM
webhook:
  path: /enrich-lead
  method: POST
  response: 202

# Extract email domain
code:
  const email = $input.first().json.email;
  const domain = email.split('@')[1];
  return { email, domain };

# Parallel enrichment
parallel:
  - apollo_person:
      email: "{{ $json.email }}"
  - clearbit_company:
      domain: "{{ $json.domain }}"
  - builtwith:
      domain: "{{ $json.domain }}"

# Merge results
merge:
  mode: combine
  
# AI qualification
anthropic:
  model: claude-3-5-sonnet
  prompt: |
    Score this lead...
    {{ $json }}

# Route based on score
switch:
  - condition: "{{ $json.score >= 80 }}"
    output: hot_leads
  - condition: "{{ $json.score >= 50 }}"
    output: warm_leads
  - default:
    output: nurture

# Hot leads path
hot_leads:
  - slack:
      channel: "#hot-leads"
      message: "🔥 New hot lead: {{ $json.name }}"
  - hubspot:
      action: create_contact
      properties:
        lead_score: "{{ $json.score }}"
        lead_status: "hot"
```

### Make Enrichment Scenario

```
Trigger: HubSpot - New Contact
  │
  ▼
HTTP - Apollo Enrichment
  │
  ▼
HTTP - Clearbit Company
  │
  ▼
OpenAI - Score Lead
  │
  ▼
Router
  ├── Score > 80 → Slack + HubSpot (Hot)
  ├── Score > 50 → HubSpot (Warm)
  └── Score < 50 → HubSpot (Nurture)
```

### Real-Time vs Batch Processing

| Approach | When to Use | Tools |
|----------|-------------|-------|
| Real-time | High-value inbound, low volume | Webhooks + n8n |
| Near real-time | Medium volume, quick needed | Queue + workers |
| Batch | High volume, cost-sensitive | Scheduled jobs |

**Real-time pattern:**
```
Form submit → Webhook → Enrich → CRM → Alert
(Seconds)
```

**Batch pattern:**
```
Collect leads → Nightly job → Enrich batch → Update CRM
(Hours)
```

---

## AI-Powered Qualification

### Lead Scoring Models

#### Rule-Based Scoring
```python
def score_lead(lead):
    score = 0
    
    # Company fit
    if lead.employees >= 50 and lead.employees <= 500:
        score += 20
    if lead.industry in ['SaaS', 'E-commerce']:
        score += 15
    if lead.revenue and lead.revenue >= 5_000_000:
        score += 15
        
    # Contact fit
    if 'VP' in lead.title or 'Director' in lead.title:
        score += 20
    if 'Marketing' in lead.title or 'Growth' in lead.title:
        score += 10
        
    # Engagement signals
    if lead.visited_pricing_page:
        score += 10
    if lead.downloaded_content:
        score += 10
        
    return min(score, 100)
```

#### AI Scoring
```
Prompt: Score this lead based on:

1. COMPANY FIT (0-30)
   - Right size? (50-500 employees ideal)
   - Right industry? (SaaS, E-commerce, Services)
   - Revenue range? ($5M-100M ideal)

2. CONTACT FIT (0-30)
   - Decision maker? (VP+)
   - Right department? (Marketing, Growth, Sales)
   - LinkedIn active?

3. TIMING/INTENT (0-20)
   - Recent funding/growth?
   - Job postings in relevant areas?
   - Using competitor tools?

4. ENGAGEMENT (0-20)
   - Visited key pages?
   - Downloaded content?
   - Multiple touchpoints?

Lead data:
{lead_json}

Return: {score: number, breakdown: {company_fit, contact_fit, timing, engagement}, reasoning: string}
```

### Qualification Questions AI Can Answer

1. **Is this the right company size?** → Compare employee count to ICP
2. **Is this the right industry?** → Classify from company description
3. **Is this a decision maker?** → Analyze title seniority
4. **Is there budget?** → Infer from revenue/funding
5. **Is there urgency?** → Check for job posts, news
6. **Is there fit?** → Match tech stack to your integrations

---

## Automation Templates

### Template 1: Form Lead Enrichment

**Trigger:** Typeform/HubSpot form submission

```yaml
steps:
  - extract_email_and_domain
  - enrich_person:
      provider: apollo
  - enrich_company:
      provider: clearbit
  - score_lead:
      method: ai
  - route:
      hot: slack_alert + instant_assignment
      warm: nurture_sequence
      cold: low_priority_queue
  - update_crm
```

### Template 2: LinkedIn Import Enrichment

**Trigger:** CSV import from Sales Navigator

```yaml
steps:
  - import_csv
  - for_each_row:
    - find_email:
        waterfall: [apollo, hunter, snov]
    - verify_email:
        provider: hunter
    - enrich_company
    - generate_personalization:
        method: ai
  - export_to_outreach_tool
```

### Template 3: Website Visitor Enrichment

**Trigger:** Clearbit Reveal identifies visitor

```yaml
steps:
  - receive_webhook  # Clearbit visitor data
  - check_existing  # Already in CRM?
  - enrich_company:
      provider: builtwith  # Tech stack
  - find_contacts:
      provider: apollo
      filter: decision_makers
  - score_account
  - if_score_high:
    - create_crm_records
    - alert_sales_rep
    - add_to_target_list
```

---

## Cost Optimization

### Waterfall Strategy

Always query cheapest sources first:

```
1. Apollo (often included in subscription)
2. Hunter ($0.05 per search)
3. Clearbit ($0.20+ per enrichment)
4. ZoomInfo (most expensive)
```

### Credit Optimization

**1. Deduplicate first**
```python
# Don't enrich same email twice
if email in already_enriched:
    return cached_data
```

**2. Only enrich what you need**
```python
# Don't enrich if basic disqualifier
if company_employee_count < 10:
    return  # Skip enrichment, not ICP
```

**3. Batch for discounts**
```python
# Many providers offer batch discounts
# Collect leads, process in batches
```

**4. Cache aggressively**
```python
# Company data changes slowly
# Cache for 30-90 days
cache.set(f"company:{domain}", data, ttl=86400*30)
```

### Cost per Lead Estimates

| Enrichment Level | Data Points | Est. Cost |
|------------------|-------------|-----------|
| Basic | Email verification only | $0.01-0.05 |
| Standard | Email + company | $0.10-0.30 |
| Full | Email + company + tech + social | $0.30-1.00 |
| Premium | All above + phone + intent | $1.00-3.00 |

### ROI Calculation

```
Lead enrichment ROI = 
  (Additional deals × Average deal value) / 
  (Enrichment cost + Implementation time)

Example:
- 1,000 leads/month × $0.50 = $500 enrichment cost
- Implementation: $500 one-time
- Additional deals from better targeting: 3/month
- Average deal value: $5,000

Year 1 ROI:
Revenue: 3 × 12 × $5,000 = $180,000
Cost: ($500 × 12) + $500 = $6,500
ROI: 27x
```

---

## Summary

### Key Takeaways

1. **Enrichment pays for itself** - Better data = better conversion
2. **Use waterfall logic** - Don't overpay for data
3. **AI supercharges enrichment** - Scoring and personalization
4. **Automate the full flow** - Form → Enrichment → CRM → Alert
5. **Cache and dedupe** - Don't waste credits

### Recommended Stack

| Component | Tool | Cost |
|-----------|------|------|
| All-in-one | Clay | $149-800/mo |
| Contact data | Apollo | $59-149/mo |
| Company data | Clearbit | $99+/mo |
| Email verification | Hunter | $49-149/mo |
| Tech stack | BuiltWith | $295/mo |
| Orchestration | n8n | Free (self-host) |

### Next Steps

1. Audit current enrichment (what's manual?)
2. Choose primary data provider
3. Set up Clay or n8n workflow
4. Create AI qualification prompt
5. Connect to CRM/outreach tools

See [personalization.md](personalization.md) for using enriched data in outreach →
