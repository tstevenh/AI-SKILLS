# AI Research Automation

> Complete guide to automating market research, competitor monitoring, and intelligence gathering with AI.

---

## Table of Contents

1. [Research Automation Overview](#research-automation-overview)
2. [Market Research](#market-research)
3. [Competitor Intelligence](#competitor-intelligence)
4. [Trend Analysis](#trend-analysis)
5. [Report Generation](#report-generation)
6. [Monitoring Systems](#monitoring-systems)
7. [Research Workflows](#research-workflows)

---

## Research Automation Overview

### The Research Challenge

Traditional research is:
- **Time-consuming:** Days to weeks for comprehensive research
- **Expensive:** Senior analysts at $100-200/hour
- **Quickly outdated:** Market changes faster than reports
- **Inconsistent:** Varies by researcher quality

### AI Research Benefits

| Task | Manual | AI-Assisted | Improvement |
|------|--------|-------------|-------------|
| Company research | 2 hours | 10 minutes | 12x faster |
| Competitor analysis | 1 day | 2 hours | 4x faster |
| Market sizing | 3 days | 4 hours | 6x faster |
| Trend report | 1 week | 1 day | 5x faster |

### Research Automation Types

```
┌─────────────────────────────────────────────────────────┐
│              RESEARCH AUTOMATION TYPES                   │
├─────────────────────────────────────────────────────────┤
│                                                          │
│  ONE-TIME RESEARCH                                       │
│  ├── Company deep dives                                  │
│  ├── Market sizing                                       │
│  ├── Industry analysis                                   │
│  └── Investment research                                 │
│                                                          │
│  CONTINUOUS MONITORING                                   │
│  ├── Competitor tracking                                 │
│  ├── News monitoring                                     │
│  ├── Social listening                                    │
│  └── Technology tracking                                 │
│                                                          │
│  PERIODIC REPORTS                                        │
│  ├── Weekly market updates                               │
│  ├── Monthly competitive analysis                        │
│  ├── Quarterly industry reports                          │
│  └── Annual strategic reviews                            │
│                                                          │
└─────────────────────────────────────────────────────────┘
```

---

## Market Research

### Industry Analysis

**Prompt:**
```
Conduct an industry analysis for: [INDUSTRY]

Research and provide:

## Industry Overview
- Market size (global and key regions)
- Growth rate (historical and projected)
- Key segments
- Industry lifecycle stage

## Market Drivers
- What's driving growth?
- Key trends shaping the industry
- Technology impacts
- Regulatory factors

## Competitive Landscape
- Market structure (fragmented/concentrated)
- Major players and market share
- Barriers to entry
- Competitive dynamics

## Value Chain
- Key activities in the value chain
- Where value is created
- Integration trends

## Challenges
- Industry headwinds
- Disruption risks
- Regulatory challenges

## Outlook
- 3-5 year projection
- Key uncertainties
- Opportunities for new entrants

Cite sources where possible. Focus on recent data (2023-2025).
```

### Market Sizing

**Prompt:**
```
Estimate the market size for: [PRODUCT/SERVICE]

Geography: [REGION]
Time frame: [YEAR]

Use multiple approaches:

## Top-Down Approach
1. Start with total addressable market
2. Apply relevant filters
3. Arrive at serviceable market

## Bottom-Up Approach
1. Identify potential customers
2. Estimate average spend
3. Calculate total market

## Competitor Analysis
1. Estimate competitor revenues
2. Infer market from shares

## Validation
- Cross-check approaches
- Identify discrepancies
- Best estimate with range

Provide:
- TAM (Total Addressable Market)
- SAM (Serviceable Addressable Market)
- SOM (Serviceable Obtainable Market)
- Growth rate (CAGR)
- Key assumptions
- Confidence level
```

### Customer Research

**Prompt:**
```
Research the typical customer for: [PRODUCT/COMPANY]

Provide:

## Demographics
- Company size (if B2B)
- Industry/sector
- Geography
- Budget range

## Psychographics
- Key pain points
- Priorities and goals
- Decision-making process
- Risk tolerance

## Buying Behavior
- How do they find solutions?
- What triggers a purchase?
- Who's involved in decisions?
- What are their alternatives?

## Customer Segments
- Primary segment
- Secondary segments
- Underserved segments

## Voice of Customer
- Common complaints about existing solutions
- What they wish existed
- Key features they value

Base this on publicly available information, reviews, forums, and industry knowledge.
```

### Research Workflow

```yaml
workflow: Market Research Report

trigger: manual or scheduled

input:
  - industry
  - focus_areas
  - depth_level

steps:
  - industry_overview:
      prompt: [industry_analysis_prompt]
      sources: perplexity, web_search
      
  - market_sizing:
      prompt: [market_sizing_prompt]
      validate: cross_reference_sources
      
  - competitive_analysis:
      prompt: [competitive_prompt]
      enrich: company_data_apis
      
  - trend_analysis:
      prompt: [trend_prompt]
      sources: news, social, patents
      
  - synthesis:
      prompt: "Synthesize these findings into a coherent report..."
      
  - format_report:
      template: market_research_template
      output: pdf, notion, google_docs
      
  - deliver:
      - email: requestor
      - slack: #research
      - notion: research_database
```

---

## Competitor Intelligence

### Company Deep Dive

**Prompt:**
```
Research [COMPETITOR] comprehensively:

## Company Overview
- Founded: 
- Headquarters:
- Employees:
- Funding/Public:
- Revenue (estimate):

## Product/Service
- Core offerings
- Recent launches
- Pricing model
- Key features

## Strategy
- Target market
- Go-to-market approach
- Positioning/messaging
- Partnerships

## Strengths
- Competitive advantages
- What they do well
- Customer praise

## Weaknesses
- Customer complaints
- Known limitations
- Gaps in offering

## Recent Activity
- News (last 6 months)
- Product updates
- Leadership changes
- Funding/acquisitions

## Threat Assessment
- How do they compete with us?
- Where are they winning?
- What can we learn?

Sources to check:
- Website, blog, press releases
- LinkedIn, Glassdoor
- G2, Capterra reviews
- News articles
- Job postings
- Social media
- SEC filings (if public)
```

### Competitive Matrix

**Prompt:**
```
Create a competitive comparison matrix:

Competitors: [LIST]
Our product: [PRODUCT]

Compare on:

## Features
| Feature | Us | Comp 1 | Comp 2 | Comp 3 |
|---------|-----|--------|--------|--------|
[Key features]

## Pricing
| Plan | Us | Comp 1 | Comp 2 | Comp 3 |
|------|-----|--------|--------|--------|
[Pricing tiers]

## Positioning
| Aspect | Us | Comp 1 | Comp 2 | Comp 3 |
|--------|-----|--------|--------|--------|
| Target market |||||
| Key message |||||
| Differentiation |||||

## Strengths/Weaknesses
For each competitor:
- Key strengths
- Key weaknesses
- Threat level (1-10)

## Recommendations
- Where we should compete
- Where we should differentiate
- Gaps to exploit
```

### Competitor Monitoring System

```yaml
workflow: Competitor Monitor

trigger: schedule - daily

competitors: [list from config]

for_each_competitor:
  steps:
    - check_website:
        detect: pricing_changes, new_pages, content_updates
        
    - check_news:
        sources: google_news, perplexity
        keywords: [company_name, product_name]
        
    - check_social:
        twitter: mentions, posts
        linkedin: posts, job_changes
        
    - check_jobs:
        linkedin: new_postings
        analyze: hiring_patterns
        
    - check_reviews:
        g2: new_reviews, rating_changes
        capterra: new_reviews
        
    - analyze_changes:
        prompt: |
          Analyze these changes for [competitor]:
          {{ changes }}
          
          Identify:
          - Significant changes
          - Strategic implications
          - Recommended actions
          
    - store_findings:
        database: competitor_intelligence
        
aggregate:
  - daily_digest: if significant_changes
  - weekly_summary: every_monday
  - monthly_report: first_of_month
```

### Job Posting Analysis

**Prompt:**
```
Analyze these job postings from [COMPETITOR]:

{job_listings}

Identify:

## Hiring Patterns
- Which departments are growing?
- Seniority levels being hired?
- Geographic expansion?

## Strategic Signals
- New product development hints
- Technology stack changes
- Market expansion plans
- Organizational changes

## Skill Requirements
- What skills are they prioritizing?
- What does this suggest about their direction?

## Competitive Implications
- What should we watch for?
- Any opportunities for us?
- Talent we should target?
```

---

## Trend Analysis

### Technology Trend Research

**Prompt:**
```
Research the current state of [TECHNOLOGY/TREND]:

## Overview
- What is it?
- Current adoption level
- Key players

## Evolution
- How has it evolved?
- Recent breakthroughs
- Adoption curve position

## Use Cases
- Primary applications
- Emerging use cases
- Industry-specific adoption

## Benefits
- Key advantages
- Proven outcomes
- ROI potential

## Challenges
- Barriers to adoption
- Limitations
- Risks

## Future Outlook
- Where is this heading?
- Timeline for mainstream adoption
- What will change?

## Implications for [OUR BUSINESS]
- Opportunities
- Threats
- Recommended actions

Focus on 2024-2026 timeframe with specific examples.
```

### Social Listening

```python
class SocialTrendAnalyzer:
    def __init__(self, llm, social_api):
        self.llm = llm
        self.social = social_api
    
    async def analyze_topic(self, topic: str, timeframe: str) -> dict:
        # Gather mentions
        mentions = await self.social.search(
            query=topic,
            timeframe=timeframe,
            platforms=["twitter", "reddit", "linkedin"]
        )
        
        # Analyze sentiment
        sentiment = await self.analyze_sentiment(mentions)
        
        # Extract themes
        themes = await self.extract_themes(mentions)
        
        # Identify influencers
        influencers = await self.identify_influencers(mentions)
        
        # Trend analysis
        trends = await self.analyze_trends(mentions)
        
        return {
            "summary": await self.summarize(mentions, sentiment, themes),
            "sentiment": sentiment,
            "themes": themes,
            "influencers": influencers,
            "trends": trends,
            "recommendations": await self.generate_recommendations()
        }
    
    async def analyze_sentiment(self, mentions: list) -> dict:
        prompt = f"""
        Analyze sentiment in these social media mentions:
        
        {mentions[:100]}  # Sample
        
        Provide:
        - Overall sentiment (positive/negative/neutral with %)
        - Sentiment by platform
        - Key drivers of positive sentiment
        - Key drivers of negative sentiment
        - Sentiment trend over time
        """
        return await self.llm.generate(prompt)
    
    async def extract_themes(self, mentions: list) -> list:
        prompt = f"""
        Extract main themes from these mentions:
        
        {mentions[:100]}
        
        For each theme:
        - Theme name
        - Description
        - Frequency
        - Example quotes
        - Sentiment for this theme
        """
        return await self.llm.generate(prompt)
```

### Patent Analysis

**Prompt:**
```
Analyze patent activity in [TECHNOLOGY AREA]:

Recent patents from: [COMPANIES]
Time period: Last 2 years

Analyze:

## Patent Volume
- Total patents filed
- Trend over time
- By company

## Technology Focus
- Main technology areas
- Emerging areas
- Cross-over areas

## Strategic Implications
- What are companies protecting?
- Where is innovation happening?
- Potential future products

## Gaps
- Under-patented areas
- Opportunities

## Key Patents
- Most significant recent patents
- Potential impact

Base analysis on publicly available patent data.
```

---

## Report Generation

### Executive Summary Template

**Prompt:**
```
Write an executive summary for this research:

{full_research}

Requirements:
- Maximum 1 page
- Lead with key findings
- Include critical numbers
- End with recommendations
- Use bullet points
- Appropriate for C-level

Structure:
## Key Findings
[3-5 bullets]

## Market Opportunity
[Size, growth, timing]

## Competitive Position
[Where we stand]

## Recommendations
[3 prioritized actions]

## Next Steps
[Immediate actions]
```

### Automated Report Builder

```python
class ResearchReportBuilder:
    def __init__(self, llm, template_engine):
        self.llm = llm
        self.templates = template_engine
    
    async def build_report(self, research_data: dict, report_type: str) -> str:
        # Select template
        template = self.templates.get(report_type)
        
        # Generate each section
        sections = {}
        for section in template.sections:
            sections[section.name] = await self.generate_section(
                section=section,
                data=research_data,
                context=sections  # Previous sections for context
            )
        
        # Generate executive summary
        sections["executive_summary"] = await self.generate_summary(
            sections=sections,
            audience=template.audience
        )
        
        # Format and compile
        report = self.templates.render(template, sections)
        
        return report
    
    async def generate_section(self, section, data, context) -> str:
        prompt = f"""
        Write the {section.name} section for a {section.report_type} report.
        
        Section requirements:
        {section.requirements}
        
        Data available:
        {data}
        
        Previous sections (for context):
        {context}
        
        Write in a {section.tone} tone for {section.audience}.
        Length: approximately {section.word_count} words.
        """
        
        return await self.llm.generate(prompt)
```

### Report Templates

**Market Report Structure:**
```markdown
# [Market] Market Report

## Executive Summary
[1 page max]

## Market Overview
- Definition and scope
- Market size and growth
- Key segments

## Industry Analysis
- Value chain
- Key players
- Competitive dynamics

## Trends and Drivers
- Growth drivers
- Key trends
- Headwinds

## Competitive Landscape
- Market share
- Competitor profiles
- Competitive positioning

## Opportunities and Threats
- Market opportunities
- Risks and challenges

## Outlook
- 5-year projections
- Scenarios

## Appendix
- Methodology
- Sources
- Detailed data
```

---

## Monitoring Systems

### News Monitoring

```yaml
workflow: News Monitor

trigger: schedule - every 4 hours

config:
  topics: [industry, competitors, technology]
  sources: [google_news, perplexity, rss_feeds]

steps:
  - gather_news:
      for_each: topic
      sources: configured_sources
      
  - deduplicate:
      similarity_threshold: 0.9
      
  - analyze:
      prompt: |
        Analyze these news items for [COMPANY]:
        
        {news_items}
        
        Identify:
        - Relevance to our business (1-10)
        - Sentiment
        - Key takeaways
        - Required action
        
  - filter:
      relevance: >= 7
      OR action_required: true
      
  - alert:
      if: high_relevance or urgent
      channel: slack
      
  - store:
      database: news_intelligence
      
  - daily_digest:
      time: 8am
      recipients: leadership
```

### Price Monitoring

```yaml
workflow: Competitor Price Monitor

trigger: schedule - daily

competitors:
  - name: Competitor A
    pricing_url: https://...
  - name: Competitor B
    pricing_url: https://...

steps:
  - for_each_competitor:
      - scrape_pricing:
          url: pricing_url
          
      - extract_prices:
          prompt: |
            Extract pricing information:
            {page_content}
            
            Return:
            - Plan names
            - Prices
            - Features per plan
            - Billing options
            
      - compare_to_previous:
          detect: changes
          
      - if_changed:
          - log_change
          - analyze_impact:
              prompt: "Analyze this pricing change..."
          - alert:
              channel: #pricing-intel
              
  - weekly_summary:
      compare: our_pricing vs competitors
      identify: positioning_opportunities
```

### Review Monitoring

```yaml
workflow: Review Monitor

trigger: schedule - twice daily

platforms:
  - G2
  - Capterra
  - TrustRadius
  - App stores (if applicable)

targets:
  - our_product
  - competitor_products

steps:
  - fetch_new_reviews:
      since: last_run
      
  - for_each_review:
      - analyze:
          prompt: |
            Analyze this review:
            {review}
            
            Extract:
            - Sentiment (1-5)
            - Key themes
            - Feature mentions
            - Competitor mentions
            - Specific issues
            - Actionable feedback
            
      - categorize:
          - product_feedback
          - support_issue
          - competitive_intel
          - feature_request
          
      - route:
          product_feedback: #product-feedback
          support_issue: create_ticket
          competitive: #competitive-intel
          
  - aggregate:
      daily: sentiment_trends
      weekly: theme_analysis
      monthly: competitive_comparison
```

---

## Research Workflows

### Company Research Workflow

```yaml
workflow: Company Deep Dive

input:
  - company_name
  - company_domain
  - research_depth: basic | standard | comprehensive

steps:
  - basic_info:
      - clearbit_lookup
      - linkedin_company
      - crunchbase
      
  - web_research:
      - fetch_website
      - analyze_positioning
      - extract_key_info
      
  - news_research:
      - recent_news
      - press_releases
      - industry_mentions
      
  - social_presence:
      - linkedin_activity
      - twitter_presence
      - content_analysis
      
  - if_comprehensive:
      - patent_analysis
      - job_posting_analysis
      - financial_analysis (if public)
      - customer_research (reviews, case studies)
      
  - synthesize:
      prompt: |
        Synthesize all research into a comprehensive company profile...
        
  - format:
      template: company_research_template
      
  - deliver:
      - notion_page
      - pdf_export
      - slack_notification
```

### Quarterly Market Review

```yaml
workflow: Quarterly Market Review

trigger: schedule - quarterly

scope:
  industry: [YOUR_INDUSTRY]
  competitors: [LIST]
  technology: [KEY_TECH]

sections:
  - market_update:
      research: market_size, growth, segments
      
  - competitive_landscape:
      for_each: competitor
      analyze: changes, strategy, wins/losses
      
  - technology_trends:
      research: emerging_tech, adoption
      
  - customer_insights:
      aggregate: reviews, feedback, churn_reasons
      
  - strategic_implications:
      synthesize: all_sections
      identify: opportunities, threats, actions
      
  - recommendations:
      prompt: |
        Based on all findings, provide strategic recommendations...
        
output:
  - executive_presentation (10 slides)
  - detailed_report (20-30 pages)
  - data_appendix
```

---

## Summary

### Research Automation ROI

| Research Type | Manual Time | AI Time | Savings |
|---------------|-------------|---------|---------|
| Company profile | 2 hours | 15 min | 87% |
| Competitive analysis | 8 hours | 2 hours | 75% |
| Market sizing | 24 hours | 4 hours | 83% |
| Quarterly review | 40 hours | 10 hours | 75% |

### Implementation Roadmap

1. **Week 1:** Set up news monitoring
2. **Week 2:** Build competitor tracker
3. **Week 3:** Create research templates
4. **Week 4:** Automate periodic reports

### Key Success Factors

1. **Quality sources** - Garbage in, garbage out
2. **Human review** - AI assists, humans verify
3. **Regular updates** - Stale data loses value
4. **Actionable output** - Research must inform decisions

See [../workflows/n8n/templates.md](../workflows/n8n/templates.md) for research automation templates →
