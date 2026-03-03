# AI Support Chatbots

> Complete guide to implementing AI chatbots for customer support: deflecting tickets, improving response time, and maintaining quality.

---

## Table of Contents

1. [Support Chatbot Strategy](#support-chatbot-strategy)
2. [Platform Options](#platform-options)
3. [Building Support Bots](#building-support-bots)
4. [Knowledge Base Integration](#knowledge-base-integration)
5. [Human Handoff](#human-handoff)
6. [Quality Assurance](#quality-assurance)
7. [Metrics and Optimization](#metrics-and-optimization)

---

## Support Chatbot Strategy

### The Support Automation Spectrum

```
Level 1: FAQ Bot
- Answers predefined questions
- Keyword matching
- Limited flexibility
- 20-30% deflection

Level 2: Knowledge Base Bot
- Searches documentation
- Returns relevant articles
- Some understanding of intent
- 30-50% deflection

Level 3: AI Conversational Bot
- Natural language understanding
- Contextual responses
- Handles variations
- 50-70% deflection

Level 4: AI Agent Bot
- Takes actions (refunds, changes)
- Accesses customer data
- Resolves complex issues
- 60-80% deflection
```

### ROI of Support Bots

```
Support team of 5 agents
- 5,000 tickets/month
- $15/ticket cost (agent time)
- Monthly cost: $75,000

With AI bot (60% deflection):
- 3,000 tickets deflected
- 2,000 tickets to agents
- Agent cost: $30,000
- Bot cost: $2,000/month
- Monthly cost: $32,000

Savings: $43,000/month (57%)
```

### What Can Support Bots Handle?

**Perfect for AI:**
- Password resets
- Order status inquiries
- Return/refund requests (simple)
- How-to questions
- Account information
- Shipping inquiries
- Feature explanations
- Billing questions (basic)

**Need human:**
- Complex technical issues
- Emotional customers
- Escalated complaints
- Legal/compliance matters
- Custom enterprise requests
- Edge cases

---

## Platform Options

### All-in-One Support Platforms

#### Intercom Fin

**The leading AI support agent.**

**Capabilities:**
- Trained on your help center
- Natural conversations
- Takes actions (Fin Actions)
- Learns from corrections
- Multilingual

**Pricing:** Included in Intercom plans + usage fees

**Strengths:**
- Best AI quality
- Deep integration
- Continuous learning
- Great reporting

#### Zendesk AI

**Enterprise-grade AI support.**

**Capabilities:**
- Intent detection
- Suggested articles
- Automated resolution
- Agent assist
- Sentiment analysis

**Pricing:** Add-on to Zendesk plans

**Strengths:**
- Enterprise scale
- Deep analytics
- Workflow automation
- Mature platform

#### Freshdesk Freddy

**Mid-market AI support.**

**Capabilities:**
- Canned response suggestions
- Ticket categorization
- Resolution bot
- Email management

**Pricing:** Part of Freshdesk plans

**Strengths:**
- Affordable
- Easy setup
- Good for growing teams

### Specialized AI Support Tools

#### Ada

**Purpose-built AI support automation.**

**Capabilities:**
- Natural language understanding
- Custom actions
- Handoff management
- Analytics

**Pricing:** Custom, typically $10k+/year

**Strengths:**
- Enterprise-focused
- High customization
- Multi-channel

#### Forethought

**AI for support operations.**

**Capabilities:**
- Intelligent triage
- Suggested responses
- Knowledge assist
- Workflow automation

**Pricing:** Custom

**Strengths:**
- Agent augmentation
- Predictive routing
- Strong analytics

### Custom Solutions

#### Build with LLMs

For unique needs, build custom:

```python
from anthropic import Anthropic

class SupportBot:
    def __init__(self, knowledge_base, customer_data_api):
        self.client = Anthropic()
        self.kb = knowledge_base
        self.customer_api = customer_data_api
    
    async def handle_message(self, message, customer_id):
        # Get customer context
        customer = await self.customer_api.get(customer_id)
        
        # Search knowledge base
        relevant_docs = self.kb.search(message)
        
        # Generate response
        response = await self.client.messages.create(
            model="claude-3-5-sonnet-20241022",
            system=self.build_system_prompt(customer, relevant_docs),
            messages=[{"role": "user", "content": message}]
        )
        
        return response.content
```

### Platform Comparison

| Platform | Best For | Starting Price | AI Quality |
|----------|----------|----------------|------------|
| Intercom Fin | All-in-one | $89/mo + usage | ★★★★★ |
| Zendesk AI | Enterprise | Custom | ★★★★☆ |
| Freshdesk | Mid-market | $79/mo | ★★★☆☆ |
| Ada | Large scale | $10k+/year | ★★★★☆ |
| Custom build | Unique needs | Dev time | Variable |

---

## Building Support Bots

### Conversation Design Principles

1. **Set expectations immediately**
   ```
   "Hi! I'm an AI assistant. I can help with common questions 
   and connect you with a human if needed."
   ```

2. **Understand intent first**
   ```
   "What can I help you with?"
   - Order/shipping question
   - Technical support
   - Billing issue
   - Account help
   - Something else
   ```

3. **Gather context before answering**
   ```
   "Let me pull up your account. Can you share the email 
   address associated with your order?"
   ```

4. **Confirm understanding**
   ```
   "Just to confirm, you'd like to track order #12345?"
   ```

5. **Provide clear resolution**
   ```
   "Your order is currently in transit. Here's the tracking: 
   [link]. Expected delivery: Friday, Jan 15."
   ```

6. **Offer escalation**
   ```
   "Did that answer your question? If you need more help, 
   I can connect you with a team member."
   ```

### Common Support Flows

#### Order Status Flow

```
User: "Where is my order?"
  │
  ▼
Bot: "I can help! What's your order number or email?"
  │
  ▼
User: [provides info]
  │
  ▼
Bot: [looks up order]
  │
  ├── Order found
  │   └── "Your order #12345 is [status]. 
  │       Tracking: [link]. ETA: [date]."
  │
  └── Order not found
      └── "I couldn't find that order. Can you double-check 
          the number? Or I can connect you with support."
```

#### Password Reset Flow

```
User: "I forgot my password"
  │
  ▼
Bot: "I can help reset it. What's your email address?"
  │
  ▼
User: [provides email]
  │
  ▼
Bot: [trigger password reset]
  │
  └── "Done! Check your email at j***@email.com for 
      the reset link. It'll expire in 30 minutes."
```

#### Refund Request Flow

```
User: "I want a refund"
  │
  ▼
Bot: "I can help. What's your order number?"
  │
  ▼
User: [provides order number]
  │
  ▼
Bot: [checks order status and policy]
  │
  ├── Within policy, simple case
  │   └── [Process refund] "Refund processed! $X will 
  │       return to your card in 5-10 days."
  │
  ├── Within policy, needs confirmation
  │   └── "Your order qualifies for a refund. Should I 
  │       process it now? The $X will return in 5-10 days."
  │
  └── Outside policy
      └── "This order is outside our standard return window.
          Let me connect you with someone who can review 
          your situation."
```

### System Prompt for Support Bot

```
You are a helpful customer support AI for [Company Name].

ABOUT [COMPANY]:
[Brief company/product description]
[Key policies: refund, shipping, etc.]

YOUR CAPABILITIES:
- Answer questions using the knowledge base
- Look up order status (use order_lookup function)
- Process simple refunds (use process_refund function)
- Reset passwords (use password_reset function)
- Connect to human support when needed

RESPONSE GUIDELINES:
- Be friendly, helpful, and concise
- Use simple language, avoid jargon
- One question at a time
- Confirm actions before taking them
- Always offer human escalation option
- Don't make promises you can't keep
- If unsure, escalate to human

ESCALATE WHEN:
- Customer is frustrated or angry
- Issue requires policy exception
- Technical problem beyond documentation
- Customer specifically requests human
- You're not confident in the answer
- Issue involves legal/compliance

TONE:
- Friendly but professional
- Empathetic with frustrated customers
- Efficient with simple queries
- Patient with confused customers
```

---

## Knowledge Base Integration

### RAG (Retrieval-Augmented Generation)

The standard pattern for support bots:

```python
class RAGSupportBot:
    def __init__(self):
        self.vectorstore = initialize_vectorstore()
        self.llm = initialize_llm()
    
    async def answer(self, question, conversation_history):
        # 1. Search knowledge base
        relevant_docs = self.vectorstore.similarity_search(
            question,
            k=5
        )
        
        # 2. Build context
        context = "\n\n".join([doc.content for doc in relevant_docs])
        
        # 3. Generate response
        prompt = f"""
        Answer the customer question using only the information below.
        If the answer isn't in the documentation, say so.
        
        Documentation:
        {context}
        
        Conversation:
        {conversation_history}
        
        Customer question: {question}
        """
        
        response = await self.llm.generate(prompt)
        
        # 4. Add source citations
        response.sources = [doc.source for doc in relevant_docs[:3]]
        
        return response
```

### Knowledge Base Best Practices

**1. Structure content for AI:**
```markdown
# How to Reset Your Password

## When to use this
- Forgot password
- Password not working
- Want to change password

## Steps
1. Go to [login page](https://...)
2. Click "Forgot Password"
3. Enter your email
4. Check inbox for reset link
5. Click link (expires in 30 min)
6. Enter new password

## Common issues
- **No email received:** Check spam, try again in 5 min
- **Link expired:** Request new reset link
- **Still can't login:** Contact support
```

**2. Cover variations:**
```markdown
# Shipping Information

## Keywords
shipping, delivery, when arrive, how long, tracking, where's my order

## Answer
Orders typically ship within 1-2 business days...
```

**3. Include edge cases:**
```markdown
## Exceptions
- Orders over $500: May require signature
- PO Boxes: USPS only, add 1-2 days
- International: 7-21 days, customs may add time
```

**4. Keep updated:**
- Review weekly for accuracy
- Add new questions from tickets
- Remove outdated information
- Test with real queries

---

## Human Handoff

### When to Escalate

```python
ESCALATION_TRIGGERS = {
    "explicit_request": [
        "speak to human",
        "talk to person",
        "real person",
        "agent please"
    ],
    "frustration_signals": [
        "this is ridiculous",
        "not helpful",
        "don't understand",
        "wrong answer"
    ],
    "complex_issues": [
        "legal",
        "lawsuit",
        "discrimination",
        "security breach"
    ],
    "confidence_threshold": 0.6,  # Below this, escalate
    "max_turns": 5  # Escalate if not resolved
}
```

### Handoff Flow

```
Bot detects escalation trigger
  │
  ▼
"I want to make sure you get the best help. Let me 
connect you with a team member."
  │
  ▼
[Check agent availability]
  │
  ├── Agent available
  │   └── "I'm connecting you with [Name] now. 
  │       They'll be with you in a moment."
  │       [Transfer with context summary]
  │
  └── No agent available
      └── "Our team is currently busy. I can:
          1. Have someone call you back
          2. Send this to email and respond within 24h
          3. You can wait (est. 15 min)
          
          What works best?"
```

### Context Handoff

Always pass context to the human agent:

```json
{
  "customer": {
    "email": "customer@email.com",
    "name": "John Doe",
    "account_status": "premium",
    "lifetime_value": "$5,000",
    "previous_tickets": 3
  },
  "conversation_summary": "Customer asking about refund for order #12345. Order is outside return window (45 days old). Customer claims product was defective. Bot could not resolve automatically.",
  "escalation_reason": "Policy exception needed",
  "sentiment": "frustrated",
  "full_transcript": "[conversation history]"
}
```

---

## Quality Assurance

### Accuracy Monitoring

```python
class QualityMonitor:
    def evaluate_response(self, query, bot_response, knowledge_base):
        # Check for hallucination
        facts_in_response = extract_facts(bot_response)
        verified = all(
            fact in knowledge_base 
            for fact in facts_in_response
        )
        
        # Check response relevance
        relevance_score = calculate_relevance(query, bot_response)
        
        # Check tone
        tone_appropriate = check_tone(bot_response)
        
        return {
            "factually_accurate": verified,
            "relevance_score": relevance_score,
            "appropriate_tone": tone_appropriate,
            "needs_review": not verified or relevance_score < 0.7
        }
```

### Human Review Workflow

```
All responses flagged for review:
  │
  ▼
Daily review queue
  │
  ▼
Reviewer checks:
- Was answer correct?
- Was tone appropriate?
- Should escalation have happened?
  │
  ▼
If incorrect:
- Add correct answer to training data
- Update knowledge base if needed
- Reach out to customer to correct
```

### Customer Feedback Loop

```
After bot resolves:
  "Did this answer your question?"
  [Yes] [No] [Sort of]
  
If "No" or "Sort of":
  "Would you like to:"
  [Try rephrasing] [Talk to human] [Submit feedback]
  
Track:
- Resolution rate
- Feedback scores
- Common "No" patterns
```

---

## Metrics and Optimization

### Key Metrics

| Metric | Formula | Target |
|--------|---------|--------|
| Deflection rate | Bot resolved / Total conversations | 60-80% |
| CSAT | Satisfied ratings / Total ratings | >85% |
| Resolution time | Time to close | <5 min |
| Escalation rate | Escalated / Total | <30% |
| First contact resolution | Resolved in one session | >70% |
| Containment rate | Stayed with bot / Started with bot | >80% |

### Optimization Strategies

**1. Analyze failed conversations**
```sql
SELECT 
  query,
  bot_response,
  escalation_reason,
  customer_feedback
FROM conversations
WHERE 
  escalated = true 
  OR feedback_score < 3
ORDER BY created_at DESC
LIMIT 100
```

**2. Identify knowledge gaps**
```sql
SELECT 
  intent_category,
  COUNT(*) as volume,
  AVG(resolution_score) as avg_resolution
FROM conversations
GROUP BY intent_category
HAVING avg_resolution < 0.6
ORDER BY volume DESC
```

**3. Improve low-performing intents**
- Add missing documentation
- Create specific flows
- Add training examples
- Consider human handling

**4. A/B test responses**
- Try different phrasings
- Test proactive vs reactive
- Compare short vs detailed answers

### Continuous Improvement Loop

```
Monitor metrics
  │
  ▼
Identify issues
  │
  ▼
Analyze root cause
  │
  ▼
Implement fix (knowledge, prompt, flow)
  │
  ▼
Measure impact
  │
  └── Loop back
```

---

## Summary

### Implementation Checklist

- [ ] Audit current support volume and types
- [ ] Choose platform based on needs
- [ ] Prepare knowledge base for AI
- [ ] Design conversation flows
- [ ] Set up human handoff
- [ ] Configure escalation triggers
- [ ] Implement monitoring
- [ ] Train support team
- [ ] Launch with subset of queries
- [ ] Expand based on performance

### Expected Timeline

| Phase | Duration | Goal |
|-------|----------|------|
| Setup | 1-2 weeks | Platform configured |
| Content | 2-4 weeks | Knowledge base ready |
| Testing | 1-2 weeks | Internal testing |
| Soft launch | 2-4 weeks | 20% of traffic |
| Full launch | Ongoing | 100% of traffic |

### Success Criteria

- 60%+ deflection rate
- 85%+ CSAT
- <30% escalation rate
- Cost savings achieved
- Agent satisfaction improved

See [voice.md](voice.md) for AI voice support →
