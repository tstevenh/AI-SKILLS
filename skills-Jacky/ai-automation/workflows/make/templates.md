# Make (Integromat) Scenario Templates

> 15+ production-ready Make scenarios for AI automation across business functions.

---

## Content Automation

### 1. Blog to Social Media Pipeline

```
Trigger: WordPress - New Post Published
    │
    ▼
HTTP - Fetch full post content
    │
    ▼
OpenAI - Generate social posts
    Prompt: "Convert to: 3 tweets, 1 LinkedIn, 1 Facebook"
    │
    ▼
Iterator - Loop through posts
    │
    ├─► Twitter - Create Tweet (scheduled)
    ├─► LinkedIn - Create Post (scheduled)
    └─► Facebook - Create Post (scheduled)
    │
    ▼
Airtable - Log posts
    │
    ▼
Slack - Notify team
```

### 2. AI Image Generation Pipeline

```
Trigger: Airtable - New Record (Image Requests)
    │
    ▼
OpenAI - Generate DALL-E image
    Prompt: {{ImagePrompt}}
    │
    ▼
HTTP - Download image
    │
    ▼
Google Drive - Upload to folder
    │
    ▼
Airtable - Update record with URL
    │
    ▼
Slack - Share in channel
```

### 3. Newsletter Curation

```
Trigger: Schedule - Every Monday 6am
    │
    ▼
RSS - Aggregate feeds (multiple)
    │
    ▼
Array Aggregator - Combine articles
    │
    ▼
OpenAI - Curate top 5
    Prompt: "Select most relevant for {{Audience}}"
    │
    ▼
OpenAI - Write summaries
    │
    ▼
Mailchimp - Create campaign draft
    │
    ▼
Slack - Notify for review
```

---

## Lead Generation

### 4. Form Lead Enrichment

```
Trigger: Typeform - New Response
    │
    ▼
HTTP - Apollo enrichment
    POST /v1/people/match
    │
    ▼
HTTP - Clearbit company
    GET /v2/companies/find?domain={{Domain}}
    │
    ▼
OpenAI - Score lead
    Prompt: "Score 1-100 based on ICP: {{ICP_Description}}"
    │
    ▼
Router
    │
    ├─► Score ≥ 70: 
    │   ├─► HubSpot - Create Contact (Hot)
    │   └─► Slack - Alert sales
    │
    └─► Score < 70:
        └─► HubSpot - Create Contact (Nurture)
```

### 5. LinkedIn to Email Finder

```
Trigger: Google Sheets - New Row (LinkedIn URLs)
    │
    ▼
HTTP - Phantombuster - Scrape profile
    │
    ▼
HTTP - Apollo - Find email
    │
    ▼
HTTP - Hunter - Verify email
    │
    ▼
Filter - Valid emails only
    │
    ▼
OpenAI - Generate first line
    Prompt: "Personalize for {{Name}} at {{Company}}"
    │
    ▼
Google Sheets - Update with results
    │
    ▼
HTTP - Add to Instantly campaign
```

### 6. Website Visitor Follow-up

```
Trigger: Webhook - Clearbit Reveal
    │
    ▼
Filter - Company size ≥ 50
    │
    ▼
HTTP - Apollo - Get decision makers
    │
    ▼
OpenAI - Rank contacts
    │
    ▼
HubSpot - Create company + contacts
    │
    ▼
HubSpot - Create task
    "Research and reach out"
    │
    ▼
Slack - Notify sales
```

---

## Customer Support

### 7. Ticket Classifier & Router

```
Trigger: Zendesk - New Ticket
    │
    ▼
OpenAI - Classify ticket
    Output: {category, priority, sentiment}
    │
    ▼
Router
    │
    ├─► Billing: Zendesk - Assign to billing_group
    ├─► Technical: Zendesk - Assign to tech_group
    ├─► Urgent: 
    │   ├─► Zendesk - Assign to escalations
    │   └─► Slack - Alert team
    └─► General: Zendesk - Assign to general_queue
    │
    ▼
Zendesk - Add tags
```

### 8. Support Response Suggester

```
Trigger: Zendesk - Ticket Assigned
    │
    ▼
HTTP - Search knowledge base
    │
    ▼
OpenAI - Generate draft response
    Prompt: Include KB context, match tone
    │
    ▼
OpenAI - Quality check
    Score accuracy and tone
    │
    ▼
Zendesk - Add internal comment
    "🤖 AI Suggestion: {{Draft}}"
    │
    ▼
Slack - Notify agent
```

### 9. Auto-Resolution for FAQs

```
Trigger: Zendesk - New Ticket
    │
    ▼
OpenAI - Analyze for auto-resolution
    Output: {intent, confidence, response}
    │
    ▼
Filter - Confidence > 0.9
    │
    ▼
Filter - Intent in allowed_list
    │
    ▼
Zendesk - Send response (public)
    │
    ▼
Zendesk - Set status: Solved
    │
    ▼
Data Store - Log auto-resolution
```

---

## Data Processing

### 10. Invoice Data Extraction

```
Trigger: Gmail - New email with attachment
    Filter: Subject contains "invoice"
    │
    ▼
Gmail - Download attachment
    │
    ▼
OpenAI - Extract invoice data (Vision)
    Output: {vendor, number, date, items, total}
    │
    ▼
QuickBooks - Create bill
    │
    ▼
Google Sheets - Log to tracker
    │
    ▼
Slack - Notify accounting
```

### 11. Review Sentiment Analysis

```
Trigger: Schedule - Daily
    │
    ▼
HTTP - Fetch reviews (G2, Capterra)
    │
    ▼
Iterator - Process each review
    │
    ▼
OpenAI - Analyze sentiment
    Output: {score, themes, quotes}
    │
    ▼
Array Aggregator - Combine results
    │
    ▼
OpenAI - Generate daily summary
    │
    ▼
Notion - Create report page
    │
    ▼
Slack - Post summary
```

---

## Reporting

### 12. Weekly KPI Report

```
Trigger: Schedule - Monday 7am
    │
    ▼
HTTP - Stripe API (revenue)
    │
    ▼
HTTP - HubSpot API (pipeline)
    │
    ▼
HTTP - Zendesk API (support metrics)
    │
    ▼
OpenAI - Generate insights
    Prompt: "Analyze week-over-week trends"
    │
    ▼
HTML - Build report template
    │
    ▼
Gmail - Send to leadership
    │
    ▼
Slack - Post to #metrics
```

### 13. Ad Performance Alerts

```
Trigger: Schedule - Hourly
    │
    ▼
Facebook Ads - Get campaign insights
    │
    ▼
Google Ads - Get campaign performance
    │
    ▼
OpenAI - Analyze for anomalies
    Alert if: ROAS < 2, CPA spike, CTR drop
    │
    ▼
Filter - Has alerts
    │
    ▼
Slack - Alert marketing team
    │
    ▼
Airtable - Log alert history
```

---

## Operations

### 14. Meeting Notes Processor

```
Trigger: Otter.ai - New Transcript
    │
    ▼
OpenAI - Process transcript
    Output: {summary, decisions, action_items}
    │
    ▼
Notion - Create meeting note
    │
    ▼
Iterator - Action items
    │
    ▼
Asana - Create task per item
    │
    ▼
Gmail - Send summary to attendees
```

### 15. Competitor Monitor

```
Trigger: Schedule - Daily
    │
    ▼
HTTP - Check competitor websites
    │
    ▼
HTTP - Search news (Perplexity)
    │
    ▼
HTTP - Check job postings
    │
    ▼
OpenAI - Analyze changes
    Identify: launches, hiring, strategy
    │
    ▼
Notion - Update competitor pages
    │
    ▼
Filter - Significant news
    │
    ▼
Slack - Alert team
```

---

## Make-Specific Features

### Data Stores

Use Data Stores for:
- Caching API responses
- Tracking processed items
- Storing configuration
- Rate limiting

```
Scenario: Check if processed
    │
    ▼
Data Store - Search Records
    │
    ▼
Router
    ├─► Found: Skip
    └─► Not found: Process
                    │
                    ▼
        Data Store - Add Record
```

### Error Handling

```
Main Scenario
    │
    ▼
Error Handler (Break)
    │
    ▼
Slack - Send error alert
    │
    ▼
Google Sheets - Log error
    │
    ▼
(Optional) Retry logic
```

### Webhooks with Response

```
Trigger: Custom Webhook
    │
    ▼
Process data
    │
    ▼
Webhook Response
    Status: 200
    Body: { "success": true, "result": {{data}} }
```

---

## Implementation Tips

### Operation Limits
- Watch operation counts on each plan
- Use aggregators to reduce operations
- Filter early in scenarios

### Scheduling
- Spread schedules to avoid rate limits
- Use off-peak times for heavy jobs
- Consider time zones

### Testing
- Use scenario history to debug
- Test with small batches first
- Save test data in Data Stores

See [n8n templates](../n8n/templates.md) and [Zapier templates](../zapier/templates.md) →
