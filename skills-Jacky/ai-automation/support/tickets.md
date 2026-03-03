# AI Ticket Automation

> Complete guide to automating support ticket handling: classification, routing, suggested responses, and auto-resolution.

---

## Table of Contents

1. [Ticket Automation Overview](#ticket-automation-overview)
2. [Classification and Routing](#classification-and-routing)
3. [Suggested Responses](#suggested-responses)
4. [Auto-Resolution](#auto-resolution)
5. [Priority and SLA](#priority-and-sla)
6. [Workflow Automation](#workflow-automation)
7. [Implementation](#implementation)

---

## Ticket Automation Overview

### The Ticket Lifecycle

```
Ticket Created
      │
      ▼
Classification (AI)
      │
      ▼
Priority Scoring (AI)
      │
      ▼
Routing (Rules + AI)
      │
      ▼
Response (AI Draft or Auto-Resolve)
      │
      ▼
Resolution
      │
      ▼
Quality Check (AI)
      │
      ▼
Closed + Learned
```

### Automation Opportunities

| Stage | AI Capability | Effort Saved |
|-------|---------------|--------------|
| Classification | Auto-tag 95%+ accurately | 2-3 min/ticket |
| Routing | Smart assignment | 1-2 min/ticket |
| First response | Draft suggestion | 5-10 min/ticket |
| Resolution | Auto-resolve simple | 15-30 min/ticket |
| Quality | Auto-review | 2-5 min/ticket |

### ROI of Ticket Automation

```
Before automation:
- 500 tickets/day
- 15 min average handle time
- 125 agent hours/day
- Cost: $3,750/day ($30/hr)

After automation:
- 200 auto-resolved (40%)
- 300 with AI assistance (60% faster)
- 50 agent hours/day
- Cost: $1,500/day

Savings: $2,250/day = $67,500/month
```

---

## Classification and Routing

### Intent Classification

#### Multi-Label Classification
```python
TICKET_CATEGORIES = {
    "billing": {
        "subcategories": ["refund", "charge_dispute", "invoice", "payment_method"],
        "keywords": ["charged", "refund", "invoice", "bill", "payment"],
    },
    "technical": {
        "subcategories": ["bug", "how_to", "integration", "performance"],
        "keywords": ["error", "not working", "bug", "how do I", "slow"],
    },
    "account": {
        "subcategories": ["access", "password", "settings", "deletion"],
        "keywords": ["login", "password", "access", "delete", "account"],
    },
    "shipping": {
        "subcategories": ["tracking", "delay", "lost", "address"],
        "keywords": ["where", "ship", "delivery", "tracking", "arrive"],
    },
    "product": {
        "subcategories": ["feature_request", "feedback", "question"],
        "keywords": ["feature", "suggestion", "why can't", "wish"],
    }
}
```

#### AI Classification Prompt
```
Classify this support ticket:

Subject: {subject}
Body: {body}
Customer: {customer_info}

Provide:
1. primary_category: One of [billing, technical, account, shipping, product, other]
2. subcategory: Specific type within category
3. sentiment: positive/neutral/negative/urgent
4. complexity: simple/medium/complex
5. requires_action: boolean (does agent need to DO something vs just answer)

Output as JSON.
```

#### Classification Implementation
```python
async def classify_ticket(ticket):
    prompt = f"""
    Classify this support ticket:
    
    Subject: {ticket.subject}
    Body: {ticket.body}
    Customer tier: {ticket.customer.tier}
    Previous tickets: {len(ticket.customer.tickets)}
    
    Categories: {list(TICKET_CATEGORIES.keys())}
    
    Return JSON: {{
        "category": "",
        "subcategory": "",
        "sentiment": "",
        "complexity": "",
        "requires_action": boolean,
        "confidence": 0-1
    }}
    """
    
    response = await llm.generate(prompt)
    classification = json.loads(response)
    
    # If low confidence, flag for human review
    if classification["confidence"] < 0.8:
        classification["needs_review"] = True
    
    return classification
```

### Smart Routing

#### Routing Rules
```python
def route_ticket(ticket, classification):
    # VIP customers → Senior agents
    if ticket.customer.tier == "enterprise":
        return assign_to_team("enterprise_support")
    
    # Urgent + negative → Immediate attention
    if classification.sentiment == "urgent":
        return assign_to_team("escalations")
    
    # By category
    routing = {
        "billing": "billing_team",
        "technical": "technical_support",
        "account": "account_team",
        "shipping": "fulfillment_team",
        "product": "product_feedback"
    }
    
    team = routing.get(classification.category, "general_support")
    
    # Load balance within team
    return assign_to_least_loaded(team)
```

#### AI-Assisted Routing
```
Based on this ticket, who should handle it?

Ticket: {ticket_summary}
Category: {classification.category}
Complexity: {classification.complexity}

Available teams:
- general_support: Basic questions, simple issues
- technical_support: Bugs, integrations, API questions
- billing_team: Refunds, charges, invoices
- enterprise_support: Enterprise customer issues
- escalations: Urgent or angry customers

Consider:
- Customer tier: {customer.tier}
- Issue complexity: {classification.complexity}
- Sentiment: {classification.sentiment}
- Required skills

Return: team_name and reason
```

---

## Suggested Responses

### Response Generation

#### Knowledge-Grounded Response
```python
async def generate_suggested_response(ticket, classification):
    # Search knowledge base
    relevant_docs = await kb.search(
        query=f"{ticket.subject} {ticket.body}",
        category=classification.category,
        k=5
    )
    
    # Get similar resolved tickets
    similar_tickets = await tickets_db.find_similar(
        ticket_text=ticket.body,
        resolved=True,
        limit=3
    )
    
    # Generate response
    prompt = f"""
    Write a support response for this ticket:
    
    TICKET:
    Subject: {ticket.subject}
    Body: {ticket.body}
    Category: {classification.category}
    
    RELEVANT DOCUMENTATION:
    {format_docs(relevant_docs)}
    
    SIMILAR RESOLVED TICKETS:
    {format_similar(similar_tickets)}
    
    CUSTOMER CONTEXT:
    - Name: {ticket.customer.name}
    - Account type: {ticket.customer.tier}
    - Previous tickets: {ticket.customer.ticket_count}
    
    GUIDELINES:
    - Be friendly and professional
    - Address their specific issue
    - Provide clear steps if applicable
    - Offer additional help
    - Match the customer's formality level
    - Include relevant links to documentation
    
    Write the response:
    """
    
    response = await llm.generate(prompt)
    return response
```

### Response Templates + AI

Combine templates with AI personalization:

```python
TEMPLATES = {
    "refund_approved": """
Hi {name},

I've processed your refund for order #{order_id}. 

Here's what to expect:
- Amount: ${amount}
- Method: Original payment method
- Timeline: 5-10 business days

{personalized_note}

{closing}

Best,
{agent_name}
    """,
    
    "technical_steps": """
Hi {name},

I understand you're experiencing {issue_summary}. Here's how to resolve it:

{numbered_steps}

{additional_context}

Let me know if you have any questions!

{closing}

Best,
{agent_name}
    """
}

async def personalize_template(template_name, ticket, data):
    template = TEMPLATES[template_name]
    
    # Generate personalized note
    personalized_note = await llm.generate(f"""
    Write a brief personalized note (1-2 sentences) for this customer:
    - Issue: {ticket.subject}
    - Customer context: {ticket.customer.history_summary}
    - Tone: friendly, empathetic
    """)
    
    data["personalized_note"] = personalized_note
    
    return template.format(**data)
```

### Response Quality Scoring

```python
async def score_response_quality(response, ticket, classification):
    prompt = f"""
    Score this support response on these criteria (1-10 each):
    
    RESPONSE:
    {response}
    
    FOR TICKET:
    {ticket.subject}: {ticket.body}
    
    CRITERIA:
    1. addresses_issue: Does it directly address the customer's question?
    2. accuracy: Is the information accurate? (based on classification)
    3. tone: Is the tone appropriate for the sentiment ({classification.sentiment})?
    4. completeness: Are all parts of the question answered?
    5. clarity: Is it easy to understand and follow?
    6. actionable: Are next steps clear?
    
    Return JSON with scores and brief explanation for any score under 7.
    """
    
    scores = await llm.generate(prompt)
    return json.loads(scores)
```

---

## Auto-Resolution

### When to Auto-Resolve

```python
AUTO_RESOLVE_CRITERIA = {
    "required": {
        "classification_confidence": 0.9,
        "response_confidence": 0.85,
        "category_allowed": True,
        "customer_tier_allowed": True
    },
    "categories_allowed": [
        "order_status",
        "tracking_info",
        "password_reset",
        "faq_question",
        "documentation_link"
    ],
    "customer_tiers_allowed": [
        "free",
        "starter",
        "professional"
    ],
    "excluded_keywords": [
        "refund",
        "angry",
        "lawsuit",
        "urgent",
        "frustrated",
        "cancel"
    ]
}

def should_auto_resolve(ticket, classification, response_confidence):
    # Check classification confidence
    if classification.confidence < AUTO_RESOLVE_CRITERIA["required"]["classification_confidence"]:
        return False
    
    # Check response confidence
    if response_confidence < AUTO_RESOLVE_CRITERIA["required"]["response_confidence"]:
        return False
    
    # Check category
    if classification.subcategory not in AUTO_RESOLVE_CRITERIA["categories_allowed"]:
        return False
    
    # Check customer tier
    if ticket.customer.tier not in AUTO_RESOLVE_CRITERIA["customer_tiers_allowed"]:
        return False
    
    # Check for excluded keywords
    ticket_text = f"{ticket.subject} {ticket.body}".lower()
    for keyword in AUTO_RESOLVE_CRITERIA["excluded_keywords"]:
        if keyword in ticket_text:
            return False
    
    return True
```

### Auto-Resolution Flows

#### Order Status
```
Ticket: "Where is my order #12345?"
      │
      ▼
Classify: shipping/tracking
      │
      ▼
Action: lookup_order(12345)
      │
      ▼
Generate response with status
      │
      ▼
Auto-send + close
```

#### Password Reset
```
Ticket: "I forgot my password"
      │
      ▼
Classify: account/password
      │
      ▼
Action: trigger_password_reset(email)
      │
      ▼
Send confirmation response
      │
      ▼
Auto-send + close
```

#### FAQ Question
```
Ticket: "How do I export my data?"
      │
      ▼
Classify: product/how_to
      │
      ▼
Search KB → high confidence match
      │
      ▼
Generate response with steps + link
      │
      ▼
Auto-send + close
```

### Safe Auto-Resolution Implementation

```python
async def process_ticket_for_auto_resolution(ticket):
    # Classify
    classification = await classify_ticket(ticket)
    
    # Generate response
    response = await generate_response(ticket, classification)
    
    # Score response
    quality = await score_response_quality(response, ticket, classification)
    
    # Determine if auto-resolve is safe
    if should_auto_resolve(ticket, classification, quality.overall_score):
        # Send response
        await ticket.reply(response)
        
        # Mark as resolved
        await ticket.resolve(
            method="auto_resolved",
            confidence=quality.overall_score
        )
        
        # Log for review
        await log_auto_resolution(ticket, classification, response, quality)
        
        return {"auto_resolved": True}
    else:
        # Add suggested response as draft
        await ticket.add_draft(response)
        
        # Route to appropriate agent
        await route_ticket(ticket, classification)
        
        return {"auto_resolved": False, "draft_added": True}
```

---

## Priority and SLA

### AI Priority Scoring

```python
async def calculate_priority(ticket, classification, customer):
    prompt = f"""
    Calculate priority score (1-100) for this ticket:
    
    TICKET:
    Subject: {ticket.subject}
    Sentiment: {classification.sentiment}
    Category: {classification.category}
    Age: {ticket.age_hours} hours old
    
    CUSTOMER:
    Tier: {customer.tier}
    ARR: ${customer.arr}
    Lifetime: {customer.months_as_customer} months
    Open tickets: {customer.open_ticket_count}
    Previous CSAT: {customer.avg_csat}
    
    FACTORS TO CONSIDER:
    - Business impact (is their work blocked?)
    - Customer value (higher tier = higher priority)
    - Sentiment (urgent/frustrated = higher priority)
    - Time waiting (older = higher priority)
    - Complexity (simpler issues can wait if others are urgent)
    
    Return JSON: {{
        "score": 1-100,
        "factors": {{
            "business_impact": 1-25,
            "customer_value": 1-25,
            "urgency_signals": 1-25,
            "time_waiting": 1-25
        }},
        "reasoning": "brief explanation"
    }}
    """
    
    result = await llm.generate(prompt)
    return json.loads(result)
```

### SLA Management

```python
SLA_RULES = {
    "enterprise": {
        "first_response": 1,  # hours
        "resolution": 24,
        "escalation_after": 2
    },
    "professional": {
        "first_response": 4,
        "resolution": 48,
        "escalation_after": 8
    },
    "starter": {
        "first_response": 8,
        "resolution": 72,
        "escalation_after": 24
    }
}

async def check_sla_status(ticket):
    sla = SLA_RULES[ticket.customer.tier]
    
    # Check first response SLA
    if not ticket.first_response_at:
        hours_waiting = ticket.age_hours
        if hours_waiting > sla["first_response"]:
            return {
                "breached": True,
                "type": "first_response",
                "hours_over": hours_waiting - sla["first_response"]
            }
    
    # Check resolution SLA
    if not ticket.resolved_at:
        hours_open = ticket.age_hours
        if hours_open > sla["resolution"]:
            return {
                "breached": True,
                "type": "resolution",
                "hours_over": hours_open - sla["resolution"]
            }
    
    return {"breached": False}

# Automated SLA monitoring
async def sla_monitor():
    """Run every 15 minutes"""
    tickets = await get_open_tickets()
    
    for ticket in tickets:
        sla_status = await check_sla_status(ticket)
        
        if sla_status["breached"]:
            # Alert team
            await notify_sla_breach(ticket, sla_status)
            
            # Auto-escalate if configured
            if ticket.age_hours > SLA_RULES[ticket.customer.tier]["escalation_after"]:
                await escalate_ticket(ticket)
```

---

## Workflow Automation

### n8n Ticket Workflow

```yaml
# Trigger: New ticket created
trigger:
  type: webhook
  event: ticket.created

steps:
  # 1. Classify ticket
  - classify:
      action: anthropic
      prompt: "Classify this ticket: {ticket}"
      
  # 2. Enrich with customer data
  - enrich:
      action: http
      url: "{{ crm_api }}/customers/{{ ticket.customer_id }}"
      
  # 3. Calculate priority
  - priority:
      action: anthropic
      prompt: "Calculate priority based on: {classification}, {customer}"
      
  # 4. Check for auto-resolution
  - check_auto:
      action: code
      code: |
        const autoResolve = checkAutoResolveCriteria(
          $json.classification,
          $json.customer
        );
        return { autoResolve };
        
  # 5. Branch based on auto-resolve
  - branch:
      condition: "{{ $json.autoResolve }}"
      true:
        - generate_response
        - send_response
        - close_ticket
      false:
        - generate_draft
        - route_ticket
        - notify_agent
```

### Make Ticket Scenario

```
Zendesk - New Ticket
      │
      ▼
OpenAI - Classify Ticket
      │
      ▼
HTTP - Get Customer Data
      │
      ▼
OpenAI - Generate Response
      │
      ▼
Router (by classification confidence)
      ├── High confidence → Zendesk: Send Reply + Close
      └── Low confidence → Zendesk: Add Internal Note + Assign
```

### Slack Integration

```python
async def notify_team_of_urgent_ticket(ticket, classification, priority):
    blocks = [
        {
            "type": "header",
            "text": f"🚨 Urgent Ticket #{ticket.id}"
        },
        {
            "type": "section",
            "fields": [
                {"type": "mrkdwn", "text": f"*Customer:*\n{ticket.customer.name}"},
                {"type": "mrkdwn", "text": f"*Tier:*\n{ticket.customer.tier}"},
                {"type": "mrkdwn", "text": f"*Category:*\n{classification.category}"},
                {"type": "mrkdwn", "text": f"*Priority:*\n{priority.score}/100"}
            ]
        },
        {
            "type": "section",
            "text": f"*Subject:* {ticket.subject}\n\n{ticket.body[:500]}..."
        },
        {
            "type": "actions",
            "elements": [
                {
                    "type": "button",
                    "text": "View Ticket",
                    "url": ticket.url
                },
                {
                    "type": "button",
                    "text": "Claim",
                    "action_id": "claim_ticket",
                    "value": str(ticket.id)
                }
            ]
        }
    ]
    
    await slack.post(channel="#urgent-tickets", blocks=blocks)
```

---

## Implementation

### Implementation Roadmap

**Phase 1: Classification (Week 1-2)**
- Set up classification categories
- Train/prompt-engineer classifier
- Test accuracy on historical tickets
- Implement auto-tagging

**Phase 2: Routing (Week 3)**
- Define routing rules
- Implement skill-based routing
- Add priority scoring
- Test with live tickets

**Phase 3: Response Suggestions (Week 4-5)**
- Integrate knowledge base
- Build response generation
- Implement quality scoring
- Deploy as agent assistant

**Phase 4: Auto-Resolution (Week 6-8)**
- Define safe categories
- Build resolution workflows
- Implement confidence thresholds
- Gradual rollout with monitoring

### Metrics to Track

| Metric | Before | Target | How to Measure |
|--------|--------|--------|----------------|
| Classification accuracy | - | >95% | Manual audit sample |
| Auto-resolution rate | 0% | 30-40% | Tickets auto-closed |
| First response time | 4 hrs | 30 min | Average across tickets |
| Agent handle time | 15 min | 8 min | Time from assign to close |
| CSAT | 85% | 90% | Post-resolution survey |

### Quality Assurance

```python
async def qa_audit_sample():
    """Daily QA of auto-resolved tickets"""
    
    # Get sample of yesterday's auto-resolved tickets
    tickets = await get_auto_resolved_tickets(
        date=yesterday,
        sample_size=50
    )
    
    issues = []
    
    for ticket in tickets:
        # Check if response was appropriate
        review = await llm.evaluate(f"""
        Review this auto-resolved ticket:
        
        Question: {ticket.body}
        Response: {ticket.response}
        Customer reply (if any): {ticket.customer_reply}
        
        Evaluate:
        1. Was the response accurate?
        2. Did it fully address the question?
        3. Was auto-resolution appropriate?
        4. Did customer seem satisfied?
        
        Return: {{
            "accurate": bool,
            "complete": bool,
            "appropriate": bool,
            "issues": "description if any"
        }}
        """)
        
        if not review["appropriate"]:
            issues.append({
                "ticket_id": ticket.id,
                "issues": review["issues"]
            })
    
    # Report
    if issues:
        await send_qa_report(issues)
```

---

## Summary

### Automation Checklist

- [ ] Define ticket categories and subcategories
- [ ] Build classification system
- [ ] Set up routing rules
- [ ] Integrate knowledge base
- [ ] Build response generation
- [ ] Implement quality scoring
- [ ] Define auto-resolution criteria
- [ ] Set up monitoring and alerts
- [ ] Train team on new workflow
- [ ] Gradual rollout with QA

### Expected Results

| Metric | Improvement |
|--------|-------------|
| First response time | 70-80% faster |
| Handle time | 40-60% reduction |
| Auto-resolution | 30-50% of tickets |
| Agent productivity | 2-3x increase |
| Cost per ticket | 40-60% reduction |

### Next Steps

1. Audit current ticket categories
2. Choose implementation approach
3. Build classification system
4. Test with historical tickets
5. Deploy response suggestions
6. Gradually enable auto-resolution

See [../workflows/n8n/templates.md](../workflows/n8n/templates.md) for ticket automation templates →
