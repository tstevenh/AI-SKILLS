# n8n Workflow Templates

> 25+ production-ready n8n workflows for AI automation across marketing, sales, support, and operations.

---

## Table of Contents

1. [Content Automation](#content-automation)
2. [Lead Generation](#lead-generation)
3. [Customer Support](#customer-support)
4. [Data Processing](#data-processing)
5. [Reporting & Analytics](#reporting--analytics)
6. [Operations](#operations)

---

## Content Automation

### 1. AI Blog Post Generator

**Purpose:** Generate blog post drafts from topics
**Trigger:** Webhook or Schedule
**Complexity:** Medium

```yaml
workflow: AI Blog Post Generator

nodes:
  - Webhook:
      name: Receive topic
      path: /generate-blog
      
  - HTTP Request:
      name: Research with Perplexity
      url: https://api.perplexity.ai/chat/completions
      method: POST
      body:
        model: pplx-7b-online
        messages:
          - role: user
            content: "Research: {{ $json.topic }}. Provide key facts and statistics."
            
  - Anthropic:
      name: Generate outline
      model: claude-3-5-sonnet
      prompt: |
        Create a detailed blog outline for: {{ $json.topic }}
        
        Research: {{ $node["Research"].json.content }}
        
        Include H2 sections, H3 subsections, and key points.
        
  - Loop Over Items:
      name: Generate each section
      items: "{{ $json.sections }}"
      
      - Anthropic:
          name: Write section
          prompt: |
            Write the section: {{ $json.section_title }}
            
            Outline:
            {{ $json.section_outline }}
            
            Previous sections for context:
            {{ $json.previous_content }}
            
  - Merge:
      name: Combine sections
      
  - Anthropic:
      name: Generate meta
      prompt: |
        For this blog post, generate:
        1. SEO title (under 60 chars)
        2. Meta description (150-160 chars)
        3. 5 relevant tags
        
        Post: {{ $json.content }}
        
  - Google Sheets:
      name: Save to content database
      operation: Append Row
      values:
        - title: "{{ $json.title }}"
        - content: "{{ $json.full_content }}"
        - meta: "{{ $json.meta_description }}"
        - status: draft
        
  - Slack:
      name: Notify team
      channel: "#content"
      message: |
        📝 New blog draft ready!
        Topic: {{ $json.topic }}
        <{{ $json.sheets_link }}|View in Sheets>
```

### 2. Social Media Repurposer

**Purpose:** Convert blog posts to social content
**Trigger:** New blog published
**Complexity:** Low

```yaml
workflow: Social Media Repurposer

nodes:
  - Webhook:
      name: New blog trigger
      path: /new-blog
      
  - HTTP Request:
      name: Fetch blog content
      url: "{{ $json.blog_url }}"
      
  - Anthropic:
      name: Generate social posts
      prompt: |
        Convert this blog post into social media content:
        
        {{ $json.content }}
        
        Generate:
        1. 3 tweets (under 280 chars each)
        2. 1 LinkedIn post (1000 chars max)
        3. 1 Facebook post (500 chars)
        4. 5 relevant hashtags
        
        Output as JSON.
        
  - Split In Batches:
      name: Process each platform
      
  - Switch:
      name: Route by platform
      conditions:
        - Twitter: schedule to Buffer
        - LinkedIn: schedule to Buffer
        - Facebook: schedule to Buffer
        
  - Buffer:
      name: Schedule posts
      profile: "{{ $json.profile_id }}"
      text: "{{ $json.post_content }}"
      scheduled_at: "{{ $json.schedule_time }}"
```

### 3. AI Newsletter Generator

**Purpose:** Curate and write weekly newsletter
**Trigger:** Weekly schedule
**Complexity:** Medium

```yaml
workflow: Weekly Newsletter Generator

nodes:
  - Schedule:
      name: Every Monday 6am
      cron: "0 6 * * 1"
      
  - HTTP Request:
      name: Fetch RSS feeds
      url: "{{ $json.feed_urls }}"
      
  - Anthropic:
      name: Curate top stories
      prompt: |
        From these articles, select the 5 most interesting for a 
        {{ $json.newsletter_topic }} newsletter:
        
        {{ $json.articles }}
        
        For each, provide:
        - Headline
        - Key insight (2 sentences)
        - Why it matters
        
  - Anthropic:
      name: Write intro
      prompt: |
        Write a friendly, engaging intro for this week's newsletter.
        Main topics: {{ $json.topics }}
        
  - Anthropic:
      name: Write outro
      prompt: |
        Write a brief outro with a call to action to reply with thoughts.
        
  - Code:
      name: Assemble newsletter
      code: |
        const sections = [
          $json.intro,
          ...items.map(i => formatStory(i)),
          $json.outro
        ];
        return { html: buildNewsletterHTML(sections) };
        
  - Beehiiv:
      name: Create draft
      action: Create Post
      content: "{{ $json.html }}"
      status: draft
      
  - Slack:
      name: Notify for review
      message: "📬 Newsletter draft ready for review"
```

### 4. Content Calendar Automation

**Purpose:** Auto-generate content briefs from calendar
**Trigger:** Daily check
**Complexity:** Low

```yaml
workflow: Content Brief Generator

nodes:
  - Schedule:
      name: Daily 9am
      cron: "0 9 * * *"
      
  - Airtable:
      name: Get upcoming content
      base: content_calendar
      table: Posts
      filter: "AND({Status}='Scheduled', {Brief}='')"
      
  - Loop Over Items:
      - Anthropic:
          name: Generate brief
          prompt: |
            Create a content brief for:
            
            Topic: {{ $json.Topic }}
            Format: {{ $json.Format }}
            Target keyword: {{ $json.Keyword }}
            Due date: {{ $json.Due_Date }}
            
            Include:
            - Working title
            - Target audience
            - Key points to cover
            - Suggested sources
            - Word count recommendation
            
      - Airtable:
          name: Update with brief
          operation: Update Record
          record_id: "{{ $json.id }}"
          fields:
            Brief: "{{ $json.brief }}"
            Status: Brief Ready
```

---

## Lead Generation

### 5. Inbound Lead Enrichment

**Purpose:** Enrich and score new leads
**Trigger:** New form submission
**Complexity:** Medium

```yaml
workflow: Lead Enrichment Pipeline

nodes:
  - Webhook:
      name: HubSpot form trigger
      path: /new-lead
      
  - Code:
      name: Extract domain
      code: |
        const email = $json.email;
        const domain = email.split('@')[1];
        return { email, domain };
        
  - HTTP Request:
      name: Apollo enrichment
      url: https://api.apollo.io/v1/people/match
      method: POST
      body:
        email: "{{ $json.email }}"
        
  - HTTP Request:
      name: Clearbit company
      url: https://company.clearbit.com/v2/companies/find
      query:
        domain: "{{ $json.domain }}"
        
  - Merge:
      name: Combine data
      
  - Anthropic:
      name: Score lead
      prompt: |
        Score this lead from 1-100 based on ICP fit:
        
        ICP: B2B SaaS, 50-500 employees, using Salesforce
        
        Lead data:
        {{ $json }}
        
        Return: { score: number, reasoning: string }
        
  - HubSpot:
      name: Update contact
      operation: Update Contact
      properties:
        lead_score: "{{ $json.score }}"
        company_size: "{{ $json.employee_count }}"
        industry: "{{ $json.industry }}"
        enriched: true
        
  - IF:
      name: Check score
      condition: "{{ $json.score >= 70 }}"
      
      true:
        - Slack:
            name: Hot lead alert
            channel: "#sales"
            message: "🔥 Hot lead: {{ $json.name }} - Score: {{ $json.score }}"
            
        - HubSpot:
            name: Create task
            operation: Create Task
            subject: "Follow up with {{ $json.name }}"
```

### 6. LinkedIn Lead Scraper → Outreach

**Purpose:** Import LinkedIn leads and add to sequence
**Trigger:** New LinkedIn export
**Complexity:** High

```yaml
workflow: LinkedIn to Outreach

nodes:
  - Google Drive:
      name: Watch for CSV
      folder: LinkedIn Exports
      
  - Spreadsheet File:
      name: Parse CSV
      operation: Read
      
  - Split In Batches:
      name: Process leads
      batch_size: 10
      
  - Loop Over Items:
      - HTTP Request:
          name: Find email
          url: https://api.apollo.io/v1/people/match
          body:
            first_name: "{{ $json.First Name }}"
            last_name: "{{ $json.Last Name }}"
            organization_name: "{{ $json.Company }}"
            
      - IF:
          name: Email found?
          condition: "{{ $json.email != null }}"
          
          true:
            - HTTP Request:
                name: Verify email
                url: https://api.hunter.io/v2/email-verifier
                
            - IF:
                name: Valid?
                condition: "{{ $json.status == 'valid' }}"
                
                true:
                  - Anthropic:
                      name: Generate personalization
                      prompt: |
                        Write a personalized first line for:
                        Name: {{ $json.name }}
                        Company: {{ $json.company }}
                        Title: {{ $json.title }}
                        
                  - HTTP Request:
                      name: Add to Instantly
                      url: https://api.instantly.ai/v1/leads
                      body:
                        email: "{{ $json.email }}"
                        campaign_id: "{{ $env.CAMPAIGN_ID }}"
                        variables:
                          first_line: "{{ $json.personalization }}"
```

### 7. Website Visitor Identification

**Purpose:** Identify and enrich website visitors
**Trigger:** Clearbit Reveal webhook
**Complexity:** Medium

```yaml
workflow: Visitor Intelligence

nodes:
  - Webhook:
      name: Clearbit Reveal
      path: /visitor
      
  - IF:
      name: Target company?
      condition: "{{ $json.company.employees >= 50 }}"
      
      true:
        - HTTP Request:
            name: Get decision makers
            url: https://api.apollo.io/v1/people/search
            body:
              organization_domain: "{{ $json.company.domain }}"
              titles: ["VP", "Director", "Head"]
              
        - Anthropic:
            name: Prioritize contacts
            prompt: |
              From these contacts, rank top 3 for outreach:
              {{ $json.people }}
              
              Our product: [description]
              
        - HubSpot:
            name: Create company
            operation: Create Company
            
        - HubSpot:
            name: Create contacts
            operation: Create Contacts
            
        - Slack:
            name: Notify team
            message: |
              🏢 Target company visiting!
              {{ $json.company.name }}
              Page: {{ $json.page_url }}
```

---

## Customer Support

### 8. Ticket Classification & Routing

**Purpose:** Auto-classify and route support tickets
**Trigger:** New ticket created
**Complexity:** Low

```yaml
workflow: Ticket Auto-Router

nodes:
  - Zendesk:
      name: New ticket trigger
      
  - Anthropic:
      name: Classify ticket
      prompt: |
        Classify this support ticket:
        
        Subject: {{ $json.subject }}
        Body: {{ $json.description }}
        
        Categories: billing, technical, shipping, account, general
        Priority: low, medium, high, urgent
        
        Return JSON: { category, priority, sentiment }
        
  - Switch:
      name: Route by category
      conditions:
        - billing: assign to billing_team
        - technical: assign to tech_team
        - urgent: assign to escalations
        
  - Zendesk:
      name: Update ticket
      operation: Update
      fields:
        group_id: "{{ $json.team_id }}"
        tags: ["{{ $json.category }}", "ai-routed"]
        priority: "{{ $json.priority }}"
```

### 9. AI Support Response Drafter

**Purpose:** Draft responses for support tickets
**Trigger:** Ticket assigned
**Complexity:** Medium

```yaml
workflow: Support Response Drafter

nodes:
  - Zendesk:
      name: Ticket assigned
      trigger: ticket.assigned
      
  - HTTP Request:
      name: Search knowledge base
      url: "{{ $env.KB_API }}/search"
      query:
        q: "{{ $json.subject }} {{ $json.description }}"
        
  - Anthropic:
      name: Generate response
      prompt: |
        Draft a support response for:
        
        Ticket: {{ $json.subject }}
        {{ $json.description }}
        
        Relevant KB articles:
        {{ $json.kb_results }}
        
        Customer name: {{ $json.requester.name }}
        
        Guidelines:
        - Friendly and helpful
        - Address all points
        - Include relevant links
        
  - Anthropic:
      name: Quality check
      prompt: |
        Review this response for accuracy and tone.
        Flag any issues.
        
        Response: {{ $json.draft }}
        
  - Zendesk:
      name: Add internal note
      operation: Create Comment
      body: |
        🤖 AI Draft:
        
        {{ $json.draft }}
        
        Quality: {{ $json.quality_score }}
        
      public: false
      
  - Slack:
      name: Notify agent
      message: "AI draft ready for ticket #{{ $json.id }}"
```

### 10. Auto-Response for Simple Tickets

**Purpose:** Auto-resolve simple, high-confidence tickets
**Trigger:** New ticket
**Complexity:** High

```yaml
workflow: Auto-Resolution Engine

nodes:
  - Zendesk:
      name: New ticket
      
  - Anthropic:
      name: Analyze ticket
      prompt: |
        Analyze this ticket for auto-resolution:
        
        {{ $json }}
        
        Return:
        - intent: specific intent
        - confidence: 0-1
        - suggested_response: if confidence > 0.9
        - needs_action: boolean
        - action_type: if applicable
        
  - IF:
      name: Auto-resolvable?
      conditions:
        - confidence > 0.9
        - intent in allowed_intents
        - customer.tier not in vip
        
      true:
        - IF:
            name: Needs action?
            condition: "{{ $json.needs_action }}"
            
            true:
              - Switch:
                  name: Execute action
                  cases:
                    - order_status: lookup order
                    - password_reset: trigger reset
                    
        - Zendesk:
            name: Send response
            operation: Create Comment
            body: "{{ $json.suggested_response }}"
            public: true
            
        - Zendesk:
            name: Close ticket
            operation: Update
            status: solved
            tags: ["auto-resolved"]
            
      false:
        - workflow.8  # Route normally
```

---

## Data Processing

### 11. Invoice Data Extraction

**Purpose:** Extract data from invoice PDFs
**Trigger:** New email attachment
**Complexity:** Medium

```yaml
workflow: Invoice Processor

nodes:
  - Gmail:
      name: Watch for invoices
      filter: "has:attachment filename:pdf subject:invoice"
      
  - Gmail:
      name: Get attachment
      operation: Get Attachment
      
  - Anthropic:
      name: Extract invoice data
      model: claude-3-5-sonnet
      vision: true
      prompt: |
        Extract from this invoice:
        - Vendor name
        - Invoice number
        - Invoice date
        - Due date
        - Line items (description, quantity, unit price, total)
        - Subtotal
        - Tax
        - Total
        
        Return as JSON.
        
  - QuickBooks:
      name: Create bill
      operation: Create Bill
      vendor: "{{ $json.vendor }}"
      lines: "{{ $json.line_items }}"
      
  - Google Sheets:
      name: Log to tracker
      operation: Append Row
```

### 12. Form Response Processor

**Purpose:** Process and analyze form submissions
**Trigger:** New form response
**Complexity:** Low

```yaml
workflow: Form Response Analyzer

nodes:
  - Typeform:
      name: New response
      
  - Anthropic:
      name: Analyze response
      prompt: |
        Analyze this form submission:
        
        {{ $json.answers }}
        
        Determine:
        - Lead quality: hot/warm/cold
        - Key pain points
        - Recommended follow-up
        - Summary (2 sentences)
        
  - Airtable:
      name: Store response
      operation: Create Record
      fields:
        Email: "{{ $json.email }}"
        Responses: "{{ $json.answers_json }}"
        Quality: "{{ $json.quality }}"
        Summary: "{{ $json.summary }}"
        
  - IF:
      name: Hot lead?
      condition: "{{ $json.quality == 'hot' }}"
      true:
        - HubSpot:
            name: Create contact
        - Slack:
            name: Alert sales
```

### 13. Review Aggregator & Analyzer

**Purpose:** Collect and analyze product reviews
**Trigger:** Daily schedule
**Complexity:** Medium

```yaml
workflow: Review Intelligence

nodes:
  - Schedule:
      name: Daily 8am
      cron: "0 8 * * *"
      
  - HTTP Request:
      name: Fetch G2 reviews
      url: "{{ $env.G2_API }}/reviews"
      
  - HTTP Request:
      name: Fetch Capterra reviews
      url: "{{ $env.CAPTERRA_API }}/reviews"
      
  - Merge:
      name: Combine reviews
      
  - Anthropic:
      name: Analyze reviews
      prompt: |
        Analyze these product reviews:
        
        {{ $json.reviews }}
        
        Provide:
        1. Overall sentiment score (1-10)
        2. Top 5 praised features
        3. Top 5 requested improvements
        4. Competitor mentions
        5. Notable quotes (positive and negative)
        6. Week-over-week trend
        
  - Notion:
      name: Update report
      operation: Create Page
      database: Reviews
      
  - Slack:
      name: Weekly summary
      condition: "{{ $today.dayOfWeek == 1 }}"  # Mondays
```

---

## Reporting & Analytics

### 14. Automated Weekly Report

**Purpose:** Generate and send weekly business reports
**Trigger:** Weekly schedule
**Complexity:** Medium

```yaml
workflow: Weekly Report Generator

nodes:
  - Schedule:
      name: Every Monday 7am
      cron: "0 7 * * 1"
      
  - HTTP Request:
      name: Get Stripe metrics
      url: https://api.stripe.com/v1/balance/history
      
  - HTTP Request:
      name: Get HubSpot metrics
      url: https://api.hubspot.com/analytics/v2
      
  - HTTP Request:
      name: Get support metrics
      url: "{{ $env.ZENDESK_API }}/tickets/stats"
      
  - Merge:
      name: Combine metrics
      
  - Anthropic:
      name: Generate insights
      prompt: |
        Generate a weekly business report from this data:
        
        Revenue: {{ $json.stripe }}
        Sales: {{ $json.hubspot }}
        Support: {{ $json.zendesk }}
        
        Include:
        - Executive summary (3 sentences)
        - Key wins
        - Areas of concern
        - Recommendations
        - Week-over-week comparisons
        
  - Code:
      name: Build HTML report
      
  - Gmail:
      name: Send to team
      to: team@company.com
      subject: "Weekly Report - {{ $today.format('MMM D') }}"
      
  - Slack:
      name: Post to #general
```

### 15. Ad Performance Monitor

**Purpose:** Monitor ad campaigns and alert on issues
**Trigger:** Hourly check
**Complexity:** Medium

```yaml
workflow: Ad Performance Monitor

nodes:
  - Schedule:
      name: Every hour
      cron: "0 * * * *"
      
  - HTTP Request:
      name: Get Facebook Ads
      url: https://graph.facebook.com/v18.0/act_xxx/insights
      
  - HTTP Request:
      name: Get Google Ads
      url: https://googleads.googleapis.com/v14/customers/xxx
      
  - Anthropic:
      name: Analyze performance
      prompt: |
        Analyze ad performance and flag issues:
        
        {{ $json.campaigns }}
        
        Alert if:
        - ROAS < 2
        - CPA increased >20%
        - Spend >120% of daily budget
        - CTR dropped >30%
        
        Return: { alerts: [...], summary: string }
        
  - IF:
      name: Has alerts?
      condition: "{{ $json.alerts.length > 0 }}"
      
      true:
        - Slack:
            name: Alert marketing
            channel: "#marketing"
            message: |
              🚨 Ad Alert:
              {{ $json.alerts.join('\n') }}
```

### 16. Churn Prediction Alerts

**Purpose:** Identify and alert on at-risk customers
**Trigger:** Daily analysis
**Complexity:** High

```yaml
workflow: Churn Risk Monitor

nodes:
  - Schedule:
      name: Daily 6am
      
  - Postgres:
      name: Get customer health data
      query: |
        SELECT 
          c.id, c.name, c.email,
          u.last_login,
          u.usage_30d,
          s.tickets_30d,
          s.nps_score
        FROM customers c
        JOIN usage u ON c.id = u.customer_id
        JOIN support s ON c.id = s.customer_id
        WHERE c.status = 'active'
        
  - Loop Over Items:
      - Anthropic:
          name: Calculate risk
          prompt: |
            Calculate churn risk for this customer:
            
            {{ $json }}
            
            Risk factors:
            - No login in 14+ days
            - Usage down >50%
            - Multiple support tickets
            - Low NPS
            
            Return: { risk: high/medium/low, score: 1-100, factors: [...] }
            
  - Filter:
      name: High risk only
      condition: "{{ $json.risk == 'high' }}"
      
  - Google Sheets:
      name: Update risk tracker
      
  - HubSpot:
      name: Create tasks
      subject: "Reach out to at-risk: {{ $json.name }}"
      
  - Slack:
      name: Alert CS team
```

---

## Operations

### 17. Meeting Notes & Follow-ups

**Purpose:** Process meeting recordings into notes and tasks
**Trigger:** New recording
**Complexity:** Medium

```yaml
workflow: Meeting Intelligence

nodes:
  - Fireflies.ai:
      name: New transcript
      trigger: transcript.ready
      
  - Anthropic:
      name: Process transcript
      prompt: |
        Process this meeting transcript:
        
        {{ $json.transcript }}
        
        Generate:
        1. Executive summary (3-5 sentences)
        2. Key decisions made
        3. Action items with owners
        4. Follow-up questions
        5. Topics for next meeting
        
  - Notion:
      name: Create meeting note
      database: Meetings
      properties:
        Title: "{{ $json.meeting_title }}"
        Date: "{{ $json.date }}"
        Attendees: "{{ $json.participants }}"
        Summary: "{{ $json.summary }}"
        
  - Loop Over Items:
      items: "{{ $json.action_items }}"
      
      - Asana:
          name: Create task
          project: "{{ $env.PROJECT_ID }}"
          name: "{{ $json.action }}"
          assignee: "{{ $json.owner }}"
          due_date: "{{ $json.due_date }}"
          
  - Gmail:
      name: Send summary
      to: "{{ $json.participants }}"
      subject: "Notes: {{ $json.meeting_title }}"
```

### 18. Competitor Monitoring

**Purpose:** Track competitor changes and news
**Trigger:** Daily check
**Complexity:** Medium

```yaml
workflow: Competitor Intelligence

nodes:
  - Schedule:
      name: Daily 7am
      
  - Loop Over Items:
      items: "{{ $env.COMPETITORS }}"
      
      - HTTP Request:
          name: Check website changes
          url: "{{ $json.website }}"
          
      - HTTP Request:
          name: Search news
          url: https://api.perplexity.ai/chat/completions
          body:
            model: pplx-7b-online
            messages:
              - role: user
                content: "Recent news about {{ $json.name }}"
                
      - HTTP Request:
          name: Check job postings
          url: https://api.linkedin.com/v2/jobs/search
          query:
            company: "{{ $json.linkedin_id }}"
            
  - Anthropic:
      name: Analyze changes
      prompt: |
        Analyze competitor activity:
        
        {{ $json }}
        
        Identify:
        - Significant website changes
        - News and announcements
        - Hiring patterns (what roles?)
        - Potential product launches
        - Strategic moves
        
  - Notion:
      name: Update competitor page
      
  - IF:
      name: Significant news?
      condition: "{{ $json.significance == 'high' }}"
      
      true:
        - Slack:
            name: Alert team
```

### 19. Document Processor

**Purpose:** Process and organize uploaded documents
**Trigger:** New file upload
**Complexity:** Medium

```yaml
workflow: Document Processor

nodes:
  - Google Drive:
      name: New file in folder
      folder: Inbox
      
  - Switch:
      name: By file type
      conditions:
        - "*.pdf": Process PDF
        - "*.docx": Process Word
        - "*.csv": Process CSV
        
  - Anthropic:
      name: Analyze document
      vision: true
      prompt: |
        Analyze this document and extract:
        
        1. Document type (invoice, contract, report, etc.)
        2. Key information (dates, parties, amounts)
        3. Summary
        4. Suggested folder/category
        5. Action items if any
        
  - Google Drive:
      name: Move to folder
      destination: "{{ $json.suggested_folder }}"
      
  - Notion:
      name: Create record
      database: Documents
      
  - IF:
      name: Has action items?
      true:
        - Asana:
            name: Create tasks
```

### 20. Employee Onboarding Automation

**Purpose:** Automate new hire onboarding tasks
**Trigger:** New hire in HRIS
**Complexity:** High

```yaml
workflow: Onboarding Automation

nodes:
  - BambooHR:
      name: New employee
      trigger: employee.created
      
  - Parallel:
      - Google Workspace:
          name: Create account
          email: "{{ $json.first_name.lower() }}@company.com"
          
      - Slack:
          name: Create account
          email: "{{ $json.email }}"
          
      - GitHub:
          name: Add to org
          username: "{{ $json.github }}"
          
  - Notion:
      name: Create onboarding page
      database: Employees
      template: Onboarding Checklist
      
  - Gmail:
      name: Send welcome email
      to: "{{ $json.email }}"
      template: new_hire_welcome
      
  - Slack:
      name: Notify team
      channel: "#general"
      message: "Welcome {{ $json.first_name }} to the team! 🎉"
      
  - Schedule Tasks:
      - Day 1: IT setup
      - Day 1: Manager intro
      - Day 3: Tools training
      - Week 1: 1:1 with CEO
      - Week 2: Team lunch
```

---

## Additional Templates

### 21. PR/Media Monitoring
### 22. Customer Feedback Loop
### 23. Inventory Alert System
### 24. Contract Renewal Reminders
### 25. Knowledge Base Auto-Update

*(Detailed implementations available in full skill)*

---

## Implementation Notes

### Error Handling

Add error handling to every workflow:

```yaml
- Error Trigger:
    name: Catch errors
    
    - Code:
        name: Format error
        
    - Slack:
        name: Alert team
        channel: "#errors"
        
    - Google Sheets:
        name: Log error
```

### Testing

Before production:
1. Test with sample data
2. Verify API credentials
3. Check rate limits
4. Test error paths
5. Document workflows

### Monitoring

Track workflow health:
- Execution success rate
- Average runtime
- Error frequency
- API costs

See [Make templates](../make/templates.md) and [Zapier templates](../zapier/templates.md) →
