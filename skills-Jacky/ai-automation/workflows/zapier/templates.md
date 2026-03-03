# Zapier Automation Templates

> 15+ production-ready Zapier automations for AI workflows, optimized for simplicity and reliability.

---

## Content Automation

### 1. Blog Post to Social Media

```
Trigger: WordPress - New Post
    │
    ▼
Action 1: ChatGPT - Conversation
    Prompt: "Write 3 tweet-sized summaries of: {{post_content}}"
    │
    ▼
Action 2: Twitter - Create Tweet
    Text: "{{chatgpt_response_1}}"
    │
    ▼
Action 3: LinkedIn - Create Share Update
    Text: "{{chatgpt_response_2}}"
    │
    ▼
Action 4: Slack - Send Message
    Message: "New blog published and shared!"
```

### 2. Content Idea Generator

```
Trigger: Schedule - Weekly
    │
    ▼
Action 1: Google Sheets - Get Rows
    Spreadsheet: Content Calendar
    Filter: Status = "Needs Topic"
    │
    ▼
Action 2: ChatGPT - Conversation
    Prompt: "Generate 5 blog topics for {{industry}} audience"
    │
    ▼
Action 3: Google Sheets - Create Row
    Values: {{generated_topics}}
    │
    ▼
Action 4: Slack - Send Message
    Channel: #content
```

### 3. Newsletter Draft Builder

```
Trigger: RSS by Zapier - New Item in Feed
    │
    ▼
Filter: Must contain {{keyword}}
    │
    ▼
Action 1: ChatGPT - Conversation
    Prompt: "Summarize in 2 sentences: {{item_content}}"
    │
    ▼
Action 2: Notion - Create Database Item
    Database: Newsletter Queue
    Properties: title, summary, url
```

---

## Lead Generation

### 4. Form to Enriched CRM Contact

```
Trigger: Typeform - New Entry
    │
    ▼
Action 1: Webhooks by Zapier - POST
    URL: Apollo API (enrich)
    │
    ▼
Action 2: ChatGPT - Conversation
    Prompt: "Score this lead 1-100: {{enriched_data}}"
    │
    ▼
Action 3: HubSpot - Create Contact
    Properties: name, email, score, company
    │
    ▼
Paths:
    Path A (Score ≥ 70):
        → Slack - Send Message to #sales
    Path B (Score < 70):
        → Mailchimp - Add Subscriber
```

### 5. LinkedIn Lead Processor

```
Trigger: Google Sheets - New Row
    (LinkedIn profile URLs)
    │
    ▼
Action 1: Webhooks by Zapier - POST
    URL: Phantombuster API
    │
    ▼
Action 2: Webhooks by Zapier - POST
    URL: Hunter API (find email)
    │
    ▼
Action 3: ChatGPT - Conversation
    Prompt: "Write personalized first line for {{name}} at {{company}}"
    │
    ▼
Action 4: Google Sheets - Update Row
    Fields: email, first_line, status
```

### 6. Demo Request Handler

```
Trigger: Calendly - Invitee Created
    │
    ▼
Action 1: Webhooks by Zapier - GET
    URL: Clearbit API (company info)
    │
    ▼
Action 2: ChatGPT - Conversation
    Prompt: "Create 3 talking points for {{company}}"
    │
    ▼
Action 3: Salesforce - Create Lead
    │
    ▼
Action 4: Gmail - Send Email
    Template: Pre-meeting prep to sales rep
    │
    ▼
Action 5: Slack - Send Message
    Channel: #demos
```

---

## Customer Support

### 7. Ticket Auto-Tagger

```
Trigger: Zendesk - New Ticket
    │
    ▼
Action 1: ChatGPT - Conversation
    Prompt: "Classify into: billing, technical, shipping, account. 
             Priority: low, medium, high. Return JSON."
    │
    ▼
Action 2: Formatter by Zapier - Text
    Extract: category from JSON
    │
    ▼
Action 3: Zendesk - Update Ticket
    Tags: {{category}}
    Priority: {{priority}}
```

### 8. Support Response Drafter

```
Trigger: Zendesk - Ticket Assigned to Agent
    │
    ▼
Action 1: ChatGPT - Conversation
    Prompt: "Draft a helpful response for: {{ticket_description}}"
    │
    ▼
Action 2: Zendesk - Create Ticket Comment
    Body: "🤖 AI Draft: {{response}}"
    Private: Yes
    │
    ▼
Action 3: Slack - Send Direct Message
    User: {{assigned_agent}}
    Message: "AI draft ready for ticket #{{id}}"
```

### 9. CSAT Follow-Up Automation

```
Trigger: Zendesk - Ticket Closed
    │
    ▼
Delay: 24 hours
    │
    ▼
Action 1: Gmail - Send Email
    Template: CSAT survey
    │
    ▼
Action 2: Typeform - New Response (separate Zap)
    │
    ▼
Paths:
    Path A (Rating < 3):
        → Zendesk - Create Ticket (follow-up)
        → Slack - Alert manager
    Path B (Rating ≥ 4):
        → Google Sheets - Log positive feedback
```

---

## Data Processing

### 10. Email Attachment Processor

```
Trigger: Gmail - New Attachment
    Search: has:attachment filename:pdf
    │
    ▼
Action 1: Google Drive - Upload File
    │
    ▼
Action 2: ChatGPT - Conversation
    Prompt: "Extract key data: vendor, date, amount, items"
    (Using GPT-4 Vision when available)
    │
    ▼
Action 3: Google Sheets - Create Row
    │
    ▼
Action 4: Slack - Send Message
    "New invoice processed: {{vendor}} - ${{amount}}"
```

### 11. Review Monitor

```
Trigger: Schedule - Daily
    │
    ▼
Action 1: Webhooks by Zapier - GET
    URL: G2 reviews API
    │
    ▼
Action 2: ChatGPT - Conversation
    Prompt: "Analyze sentiment. Flag any negative (<3 stars)."
    │
    ▼
Paths:
    Path A (Has negative):
        → Slack - Send Message to #product
        → Airtable - Create Record
    Path B (All positive):
        → Google Sheets - Log summary
```

---

## Reporting

### 12. Weekly Metrics Email

```
Trigger: Schedule - Monday 8am
    │
    ▼
Action 1: Webhooks by Zapier - GET
    URL: Stripe API (revenue)
    │
    ▼
Action 2: Webhooks by Zapier - GET
    URL: HubSpot API (deals)
    │
    ▼
Action 3: ChatGPT - Conversation
    Prompt: "Generate executive summary from: {{metrics}}"
    │
    ▼
Action 4: Gmail - Send Email
    To: leadership@company.com
    Subject: "Weekly Metrics - {{date}}"
```

### 13. Anomaly Alerter

```
Trigger: Schedule - Every 6 hours
    │
    ▼
Action 1: Google Sheets - Get Row
    (Previous metrics)
    │
    ▼
Action 2: Webhooks by Zapier - GET
    URL: Analytics API (current metrics)
    │
    ▼
Action 3: ChatGPT - Conversation
    Prompt: "Compare and flag any anomalies (>20% change)"
    │
    ▼
Filter: Has anomalies = true
    │
    ▼
Action 4: Slack - Send Message
    Channel: #alerts
```

---

## Operations

### 14. Meeting Notes to Tasks

```
Trigger: Otter.ai - New Transcript
    │
    ▼
Action 1: ChatGPT - Conversation
    Prompt: "Extract: summary, decisions, action items with owners"
    │
    ▼
Action 2: Notion - Create Page
    Database: Meetings
    │
    ▼
Action 3: Formatter - Split Text
    Delimiter: newline (for action items)
    │
    ▼
Action 4: Asana - Create Task (for each)
    Project: {{relevant_project}}
```

### 15. New Hire Onboarding

```
Trigger: BambooHR - New Employee
    │
    ▼
Action 1: Google Workspace - Create User
    │
    ▼
Action 2: Slack - Invite User
    │
    ▼
Action 3: Notion - Create Page
    Template: Onboarding Checklist
    │
    ▼
Action 4: Gmail - Send Email
    Template: Welcome email
    │
    ▼
Action 5: Slack - Send Channel Message
    Channel: #general
    "Welcome {{name}} to the team! 🎉"
```

---

## Zapier-Specific Tips

### Using Paths

Paths let you branch logic:
```
Trigger
    │
    ▼
Paths
    ├─► Path A: Condition 1
    │   └─► Actions for condition 1
    │
    └─► Path B: Condition 2
        └─► Actions for condition 2
```

### Using Formatter

Transform data between steps:
- Split text into arrays
- Extract patterns with regex
- Format dates
- Convert case

### Using Webhooks

For APIs without native integration:
```
Webhooks by Zapier - GET/POST
    URL: API endpoint
    Headers: Authorization, Content-Type
    Body: JSON payload
```

### Using Delay

Space out actions:
```
Trigger
    │
    ▼
Delay by Zapier
    For: 1 hour
    │
    ▼
Action (runs after delay)
```

### Task Optimization

Reduce task usage:
1. Use Filters early (don't charge for filtered items)
2. Combine related actions
3. Use Paths instead of multiple Zaps
4. Batch with Schedule triggers

---

## Zapier Tables Integration

Store and manage data within Zapier:

```
Trigger: Form submission
    │
    ▼
Action 1: Zapier Tables - Create Record
    │
    ▼
Later...
    │
    ▼
Trigger: Zapier Tables - Record Updated
    │
    ▼
Action: Process based on status
```

---

## Limitations & Workarounds

| Limitation | Workaround |
|------------|------------|
| No loops | Use Paths or separate Zaps |
| 2-min timeout | Break into smaller Zaps |
| 100 steps max | Chain Zaps via webhooks |
| Limited transforms | Use Code by Zapier (premium) |

See [n8n templates](../n8n/templates.md) and [Make templates](../make/templates.md) →
