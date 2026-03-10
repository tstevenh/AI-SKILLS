# AI Sales Chatbots

> Complete guide to implementing AI chatbots for sales: qualifying visitors, booking meetings, and driving conversions.

---

## Table of Contents

1. [Sales Chatbot Strategy](#sales-chatbot-strategy)
2. [Platform Comparison](#platform-comparison)
3. [Building Sales Chatbots](#building-sales-chatbots)
4. [Qualification Flows](#qualification-flows)
5. [Meeting Booking](#meeting-booking)
6. [Integration Patterns](#integration-patterns)
7. [Optimization](#optimization)

---

## Sales Chatbot Strategy

### What Sales Chatbots Do

1. **Engage visitors** - Proactive outreach
2. **Qualify leads** - Ask qualifying questions
3. **Answer questions** - Product/pricing info
4. **Book meetings** - Calendar integration
5. **Route to sales** - Connect with humans
6. **Capture information** - Email, company, needs

### The Sales Chatbot Funnel

```
Website Visitor (100%)
       │
       ▼
Engages with Bot (10-30%)
       │
       ▼
Completes Qualification (5-15%)
       │
       ▼
Books Meeting (2-8%)
       │
       ▼
Shows Up (70-80% of booked)
```

### ROI Calculation

```
Without chatbot:
- 10,000 visitors/month
- 100 form submissions (1%)
- 20 qualified (20%)
- 10 meetings booked (50%)
- 7 show up (70%)
- 1.4 deals closed (20%)
- Revenue: $14,000 ($10k ACV)

With AI chatbot:
- 10,000 visitors/month
- 300 engaged (3%)
- 90 qualified (30%)
- 45 meetings booked (50%)
- 35 show up (78%)
- 7 deals closed (20%)
- Revenue: $70,000

ROI: 5x improvement
```

### When to Use Sales Chatbots

✅ **Good fit:**
- High-traffic website
- Complex product requiring explanation
- Multiple buyer personas
- Long sales cycle
- Sales team capacity constrained

❌ **Less suitable:**
- Very low traffic (<1000/month)
- Simple product, self-serve purchase
- Price-sensitive buyers who dislike bots
- Highly technical audience

---

## Platform Comparison

### Major Platforms

#### Intercom

**Best for:** Full customer lifecycle (marketing, sales, support)

**Features:**
- AI (Fin) for conversations
- Custom bots with visual builder
- Meeting scheduling
- CRM integrations
- Product tours

**Pricing:**
| Plan | Starting At | Key Features |
|------|------------|--------------|
| Essential | $39/seat/mo | Basic bots |
| Advanced | $99/seat/mo | Custom bots, AI |
| Expert | $139/seat/mo | Full AI, analytics |

**Strengths:**
- Unified platform
- Strong AI capabilities
- Rich integrations
- Good UX

#### Drift

**Best for:** Enterprise, account-based sales

**Features:**
- AI chatbots
- Revenue acceleration
- ABM targeting
- Meeting booking
- Video chat

**Pricing:** Custom, typically $2,500+/month

**Strengths:**
- ABM-focused
- Enterprise features
- Strong routing

#### Qualified

**Best for:** B2B, Salesforce native

**Features:**
- Real-time conversations
- AI agent
- Salesforce native
- Intent signals
- Meeting booking

**Pricing:** Starting $3,500/month

**Strengths:**
- Salesforce integration
- Enterprise focus
- Sophisticated routing

#### Crisp

**Best for:** SMB, cost-effective

**Features:**
- Live chat + chatbot
- Knowledge base
- Campaigns
- CRM

**Pricing:**
| Plan | Price | Features |
|------|-------|----------|
| Basic | Free | 2 seats |
| Pro | $25/seat/mo | Chatbot |
| Unlimited | $95/mo | Unlimited seats |

**Strengths:**
- Affordable
- Easy setup
- Good for SMB

#### Tidio

**Best for:** E-commerce, small business

**Features:**
- AI chatbots
- Live chat
- Email marketing
- Visitor tracking

**Pricing:**
| Plan | Price | Conversations |
|------|-------|---------------|
| Free | $0 | 50/mo |
| Starter | $29/mo | 100/mo |
| Growth | $59/mo | 2,000/mo |

**Strengths:**
- Easy setup
- E-commerce focus
- Good templates

### Platform Selection Matrix

| Factor | Intercom | Drift | Qualified | Crisp | Tidio |
|--------|----------|-------|-----------|-------|-------|
| Price | $$$ | $$$$ | $$$$ | $ | $ |
| AI Quality | ★★★★★ | ★★★★☆ | ★★★★☆ | ★★★☆☆ | ★★★☆☆ |
| Ease of Use | ★★★★☆ | ★★★☆☆ | ★★★☆☆ | ★★★★★ | ★★★★★ |
| Enterprise | ★★★★☆ | ★★★★★ | ★★★★★ | ★★☆☆☆ | ★★☆☆☆ |
| Salesforce | ★★★☆☆ | ★★★★☆ | ★★★★★ | ★★☆☆☆ | ★★☆☆☆ |
| SMB | ★★★★☆ | ★★☆☆☆ | ★★☆☆☆ | ★★★★★ | ★★★★★ |

---

## Building Sales Chatbots

### Conversation Design

#### Opening Strategy

**Proactive (trigger-based):**
```
IF visitor on pricing page > 30 seconds:
  "Have questions about pricing? I can help."

IF visitor viewed 3+ pages:
  "Looking for something specific? Let me know."

IF visitor from target account:
  "Welcome from {company}! Want a personalized demo?"
```

**Reactive (visitor initiates):**
```
"Hi! How can I help you today?"
  - "I have questions about your product"
  - "I want to see pricing"
  - "I'd like to talk to sales"
  - "Just browsing"
```

#### Qualification Conversation Flow

```
┌─────────────────────────────────────────────────────────┐
│              QUALIFICATION FLOW                          │
├─────────────────────────────────────────────────────────┤
│                                                          │
│  GREETING                                                │
│  "Hi! Looking for [product category]?"                  │
│     │                                                    │
│     ▼                                                    │
│  ROLE                                                    │
│  "What's your role?"                                    │
│  [Decision maker / Team member / Individual]            │
│     │                                                    │
│     ▼                                                    │
│  COMPANY SIZE                                            │
│  "How large is your company?"                           │
│  [1-10 / 11-50 / 51-200 / 201-1000 / 1000+]           │
│     │                                                    │
│     ▼                                                    │
│  USE CASE                                                │
│  "What are you hoping to accomplish?"                   │
│  [Free text or options]                                 │
│     │                                                    │
│     ▼                                                    │
│  TIMELINE                                                │
│  "When are you looking to implement?"                   │
│  [ASAP / 1-3 months / 3-6 months / Just exploring]     │
│     │                                                    │
│     ▼                                                    │
│  ROUTE                                                   │
│  Based on answers:                                       │
│  - High fit + ASAP → Book with AE                       │
│  - High fit + Later → Book with SDR                     │
│  - Medium fit → Nurture sequence                        │
│  - Low fit → Self-serve resources                       │
│                                                          │
└─────────────────────────────────────────────────────────┘
```

### AI-Powered Conversations

#### Using LLMs in Chatbots

Most platforms now support LLM-based conversations:

**Intercom Fin:**
- Trained on your help docs
- Answers product questions
- Qualifies with natural conversation
- Hands off to humans

**Custom AI Integration:**
```python
# Webhook handler for chatbot
async def handle_message(user_message, context):
    # Get conversation history
    history = get_conversation_history(context.conversation_id)
    
    # Call LLM
    response = await openai.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": SALES_BOT_PROMPT},
            *history,
            {"role": "user", "content": user_message}
        ],
        functions=[QUALIFY_FUNCTION, BOOK_MEETING_FUNCTION],
    )
    
    # Handle function calls
    if response.function_call:
        return handle_function(response.function_call)
    
    return response.content
```

#### Sales Bot System Prompt

```
You are a friendly sales assistant for [Company Name]. 

YOUR ROLE:
- Greet visitors warmly
- Answer questions about our product
- Qualify leads by understanding their needs
- Help them book a meeting with our team

PRODUCT INFO:
[Brief product description]
[Key features]
[Pricing overview]

QUALIFICATION CRITERIA:
We're best fit for:
- Companies with 50-500 employees
- In SaaS, E-commerce, or Professional Services
- Looking to solve [specific problem]

CONVERSATION STYLE:
- Friendly and helpful, not pushy
- Ask one question at a time
- Use natural language
- Keep responses under 50 words
- If they seem frustrated, offer to connect with human

WHEN TO ESCALATE:
- Specific pricing questions beyond basic
- Technical integration questions
- Complaints or issues
- Request to speak with human

GOAL:
Understand their needs and either:
1. Book a meeting if qualified
2. Point to self-serve resources if not ideal fit
3. Escalate to human if needed
```

### Handling Common Scenarios

#### "What's the pricing?"

```
Bot: "Great question! Our pricing depends on your team size 
and needs. Can I ask a few quick questions to give you 
relevant info?

Quick overview:
- Starter: $49/mo for small teams
- Professional: $149/mo for growing teams
- Enterprise: Custom for large orgs

What size is your team?"
```

#### "Can I see a demo?"

```
Bot: "Absolutely! We'd love to show you around.

To make sure we cover what matters to you, quick question: 
What's the main thing you're hoping to solve?

[Options or free text]"
```

#### "Just browsing"

```
Bot: "No problem! Feel free to look around.

If you have any questions, I'm here. Or you can check out:
- [Product overview video]
- [Customer stories]
- [Documentation]

Happy to help whenever you're ready!"
```

#### Objection Handling

```
"Too expensive":
Bot: "I understand budget is important. Many of our customers 
found that the time savings paid for themselves within a month.

Would it help to see a quick calculation of potential ROI 
for your situation? What's your team size?"

"Need to talk to boss":
Bot: "Of course! Want me to send you a summary you can share 
with them? I can include relevant case studies.

What's your email? I'll also CC you when we send it."

"Using competitor":
Bot: "Got it! Many of our customers switched from [competitor]. 
They usually mention [key differentiator] as the main reason.

Would you be open to a quick comparison call? No pressure, 
just want to see if there's something we could offer."
```

---

## Qualification Flows

### BANT Qualification

```
BUDGET:
"What's your budget range for this solution?"
- Under $500/mo
- $500-2000/mo
- $2000-5000/mo
- Over $5000/mo
- Don't know yet

AUTHORITY:
"Who else would be involved in this decision?"
- Just me
- My manager
- A committee
- IT/Security team

NEED:
"What's driving your search for a solution?"
- Current tool isn't working
- New initiative
- Growing pains
- Exploring options

TIMELINE:
"When do you need a solution in place?"
- This month
- This quarter
- Next quarter
- No specific timeline
```

### Scoring-Based Qualification

```python
def calculate_lead_score(answers):
    score = 0
    
    # Company size
    size_scores = {
        "1-10": 5,
        "11-50": 15,
        "51-200": 25,
        "201-1000": 20,
        "1000+": 10
    }
    score += size_scores.get(answers.company_size, 0)
    
    # Role
    role_scores = {
        "C-level": 30,
        "VP": 25,
        "Director": 20,
        "Manager": 15,
        "Individual": 5
    }
    score += role_scores.get(answers.role, 0)
    
    # Timeline
    timeline_scores = {
        "ASAP": 30,
        "1-3 months": 25,
        "3-6 months": 15,
        "Just exploring": 5
    }
    score += timeline_scores.get(answers.timeline, 0)
    
    # Budget
    if answers.budget and answers.budget >= 1000:
        score += 15
    
    return score

# Routing based on score
def route_lead(score):
    if score >= 70:
        return "book_ae_meeting"
    elif score >= 50:
        return "book_sdr_meeting"
    elif score >= 30:
        return "email_sequence"
    else:
        return "self_serve"
```

---

## Meeting Booking

### Calendar Integration

Most chatbot platforms integrate with:
- Calendly
- HubSpot Meetings
- Chili Piper
- Cal.com
- Google Calendar direct

### Booking Flow Best Practices

```
1. Qualify first (don't let unqualified book)

2. Explain the meeting
   "Great! Let me book you a 15-minute intro call with [Name]. 
   They'll show you [specific thing] based on your [use case]."

3. Show calendar
   [Embedded calendar widget]

4. Confirm details
   "Perfect! You're booked with [Name] on [date] at [time].
   You'll receive a calendar invite at [email].
   
   Anything specific you'd like to cover?"

5. Set expectations
   "Before the call, you might want to check out [resource].
   [Name] will send a quick agenda the day before.
   
   See you soon!"
```

### Smart Routing

```
# Route to appropriate rep based on lead attributes
def route_to_rep(lead):
    if lead.company_size >= 500:
        return ENTERPRISE_TEAM
    elif lead.vertical == "Healthcare":
        return HEALTHCARE_SPECIALIST
    elif lead.location == "EMEA":
        return EMEA_TEAM
    else:
        return GENERAL_POOL
    
# Round robin within team
def get_next_rep(team):
    reps = get_available_reps(team)
    return reps.sort_by("last_assigned").first()
```

---

## Integration Patterns

### CRM Integration

```yaml
# On qualification complete
trigger: bot_qualification_complete

actions:
  - hubspot:
      action: create_contact
      properties:
        email: "{{ conversation.email }}"
        company: "{{ conversation.company }}"
        lead_score: "{{ conversation.score }}"
        lead_source: "chatbot"
        qualification_answers: "{{ conversation.answers_json }}"
        
  - hubspot:
      action: create_deal
      condition: "{{ conversation.score >= 70 }}"
      properties:
        deal_name: "{{ conversation.company }} - Inbound"
        stage: "qualified"
        amount: "{{ estimated_deal_size }}"
```

### Slack Notifications

```python
def notify_sales_team(conversation):
    message = f"""
🔥 *New Qualified Lead!*

*Contact:* {conversation.name} ({conversation.email})
*Company:* {conversation.company}
*Size:* {conversation.company_size}
*Score:* {conversation.score}/100

*Key Answers:*
- Use case: {conversation.use_case}
- Timeline: {conversation.timeline}
- Budget: {conversation.budget}

*Meeting:* {conversation.meeting_time or 'Not booked'}

<{crm_link}|View in CRM>
    """
    
    slack.post_message(
        channel="#sales-leads",
        text=message,
        thread_ts=None
    )
```

### Email Sequences

```yaml
# For leads who don't book
trigger: qualification_complete
condition: score >= 50 AND meeting_booked == false

sequence:
  - delay: 1_hour
    email:
      template: "followup_after_chat"
      variables:
        conversation_summary: "{{ ai_summary }}"
        
  - delay: 2_days
    email:
      template: "resource_share"
      variables:
        resource: "{{ relevant_case_study }}"
        
  - delay: 5_days
    email:
      template: "meeting_offer"
```

---

## Optimization

### Key Metrics

| Metric | Benchmark | What It Tells You |
|--------|-----------|-------------------|
| Engagement rate | 5-15% | Bot visibility/relevance |
| Qualification completion | 30-50% | Flow quality |
| Meeting book rate | 10-25% | Offer relevance |
| Show rate | 70-85% | Confirmation quality |
| Qualified rate | 60-80% | Targeting accuracy |

### A/B Testing

**Test these elements:**
- Opening message timing
- Opening message copy
- Number of qualification questions
- Question order
- Button vs text responses
- Proactive vs reactive triggers

### Common Optimizations

**1. Reduce friction**
```
Before: 7 questions before meeting
After: 3 questions, rest asked in meeting
Result: 2x booking rate
```

**2. Better targeting**
```
Before: Show bot to all visitors
After: Show only to visitors from target companies
Result: Higher qualified %
```

**3. Faster response**
```
Before: AI takes 3-5 seconds to respond
After: Streaming responses
Result: Lower abandonment
```

**4. Human handoff**
```
Before: Bot handles everything
After: Quick handoff to human for high-value leads
Result: Higher conversion for enterprise
```

---

## Summary

### Implementation Checklist

- [ ] Choose platform based on needs/budget
- [ ] Define qualification criteria
- [ ] Design conversation flows
- [ ] Set up calendar integration
- [ ] Configure CRM integration
- [ ] Set up notifications
- [ ] Train team on handoffs
- [ ] Launch with A/B test
- [ ] Monitor and optimize

### Recommended Stack

| Business Size | Platform | Cost |
|---------------|----------|------|
| SMB | Crisp or Tidio | $30-100/mo |
| Mid-market | Intercom | $300-500/mo |
| Enterprise | Drift or Qualified | $2,500+/mo |

### Next Steps

1. Audit current website conversion
2. Select platform
3. Design qualification flow
4. Build and test
5. Train sales team
6. Launch and iterate

See [../support/chatbots.md](../support/chatbots.md) for support-focused chatbots →
