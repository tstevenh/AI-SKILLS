# AI Voice Support

> Complete guide to AI-powered phone support: voice agents, IVR replacement, and call automation.

---

## Table of Contents

1. [Voice AI Overview](#voice-ai-overview)
2. [Platform Options](#platform-options)
3. [Building Voice Agents](#building-voice-agents)
4. [Use Cases](#use-cases)
5. [Integration Patterns](#integration-patterns)
6. [Quality and Compliance](#quality-and-compliance)

---

## Voice AI Overview

### The Voice AI Revolution

Phone support is being transformed by AI that can:

- **Understand** natural speech
- **Respond** in natural voice
- **Handle** complete conversations
- **Take actions** (look up orders, process requests)
- **Escalate** intelligently to humans

### Current Capabilities

**What works well:**
- Order status inquiries
- Appointment scheduling
- Basic troubleshooting
- Account balance/info
- FAQ-style questions
- Routing and triage
- Callback scheduling

**What still needs humans:**
- Complex troubleshooting
- Emotional situations
- Negotiations
- Legal/compliance issues
- Edge cases

### Voice AI vs Traditional IVR

| Feature | Traditional IVR | AI Voice Agent |
|---------|-----------------|----------------|
| Input | Button press | Natural speech |
| Understanding | Keywords only | Full sentences |
| Flexibility | Rigid tree | Dynamic conversation |
| Resolution | Route only | Can resolve |
| Experience | Frustrating | Natural |
| Maintenance | Constant updates | Self-learning |

---

## Platform Options

### Leading Voice AI Platforms

#### Bland.ai

**Best for:** Developers, custom solutions

**Capabilities:**
- Natural conversations
- Custom voices
- API-first
- Integrations
- Analytics

**Pricing:**
- Pay per minute (~$0.09/min)
- Enterprise custom pricing

**Strengths:**
- Developer friendly
- Fast to deploy
- Good voice quality
- Flexible

**Example Code:**
```python
from bland import BlandClient

client = BlandClient(api_key="your_key")

call = client.calls.create(
    phone_number="+1234567890",
    pathway_id="support-flow",
    voice_id="professional_female",
    transfer_phone_number="+1987654321",
    webhook_url="https://your-app.com/call-complete"
)
```

#### Vapi

**Best for:** Complex workflows, enterprise

**Capabilities:**
- Voice assistants
- Phone calls
- Web calls
- Custom LLM integration
- Tool calling

**Pricing:**
- Free tier: 10 minutes/month
- Pay-as-you-go: ~$0.05-0.10/min
- Enterprise: Custom

**Strengths:**
- Flexible LLM support
- Good for complex flows
- Strong integrations

**Example Code:**
```python
import vapi

assistant = vapi.Assistant.create(
    name="Support Agent",
    model={
        "provider": "openai",
        "model": "gpt-4o",
        "temperature": 0.7
    },
    voice={
        "provider": "11labs",
        "voiceId": "voice_id"
    },
    system_prompt="You are a helpful support agent..."
)

call = vapi.Call.create(
    assistant_id=assistant.id,
    phone_number="+1234567890"
)
```

#### Retell AI

**Best for:** Enterprise, compliance-focused

**Capabilities:**
- Inbound and outbound
- LLM integration
- Custom voices
- Call recording
- Analytics

**Pricing:** Custom, enterprise-focused

**Strengths:**
- Enterprise features
- Compliance focus
- Good quality

#### Poly.ai

**Best for:** Large contact centers

**Capabilities:**
- Full conversation handling
- Deep integrations
- Analytics
- Compliance

**Pricing:** Enterprise only

**Strengths:**
- Proven at scale
- Deep analytics
- Professional grade

### Platform Comparison

| Feature | Bland | Vapi | Retell | Poly.ai |
|---------|-------|------|--------|---------|
| Pricing | $0.09/min | $0.05-0.10/min | Custom | Enterprise |
| Setup ease | ★★★★★ | ★★★★☆ | ★★★☆☆ | ★★☆☆☆ |
| Voice quality | ★★★★☆ | ★★★★☆ | ★★★★★ | ★★★★★ |
| Customization | ★★★★☆ | ★★★★★ | ★★★★☆ | ★★★☆☆ |
| Enterprise | ★★★☆☆ | ★★★★☆ | ★★★★★ | ★★★★★ |
| Best for | Startups | Mid-market | Enterprise | Large centers |

---

## Building Voice Agents

### Voice Agent Architecture

```
┌─────────────────────────────────────────────────────────┐
│                   VOICE AI STACK                         │
├─────────────────────────────────────────────────────────┤
│                                                          │
│  TELEPHONY LAYER                                         │
│  └── Twilio / Provider's telephony                      │
│                                                          │
│  SPEECH-TO-TEXT                                          │
│  └── Deepgram / Whisper / Google STT                    │
│                                                          │
│  LANGUAGE MODEL                                          │
│  └── GPT-4 / Claude / Custom                            │
│                                                          │
│  TEXT-TO-SPEECH                                          │
│  └── ElevenLabs / Play.ht / Provider TTS               │
│                                                          │
│  INTEGRATIONS                                            │
│  └── CRM / Order system / Knowledge base                │
│                                                          │
└─────────────────────────────────────────────────────────┘
```

### Conversation Design for Voice

**Key differences from chat:**
- No visual cues
- Can't skim/scroll back
- More forgiving of AI
- Needs clearer confirmations
- Silences are awkward

#### Opening
```
Agent: "Thanks for calling [Company]. This is Amy, your 
virtual assistant. I can help with order status, returns, 
and general questions. What can I help you with today?"
```

#### Gathering Information
```
Agent: "I can look that up for you. Can you give me your 
order number? It starts with the letters O-R-D."

[Customer gives number]

Agent: "Let me repeat that back: O-R-D-1-2-3-4-5. Is that 
correct?"
```

#### Providing Information
```
Agent: "I found your order. It shipped yesterday via FedEx 
and should arrive by Friday, January 15th. Would you like 
me to text you the tracking link?"
```

#### Escalation
```
Agent: "I want to make sure you get the best help with this. 
Let me connect you with a specialist. You'll be with someone 
in about 2 minutes. Is that okay, or would you prefer a 
callback?"
```

### System Prompt for Voice Agent

```
You are Amy, a voice support agent for [Company].

CONTEXT:
You are on a phone call with a customer. They cannot see 
anything, so describe things clearly.

VOICE GUIDELINES:
- Keep responses under 30 words when possible
- Use natural, conversational language
- Confirm important information by repeating it back
- Use clear transitions: "Let me check that for you"
- Fill silence: "I'm looking that up now, one moment"
- Spell out unusual words: "That's S-M-I-T-H"

CAPABILITIES:
You can:
- Look up order status (use lookup_order function)
- Check account balance
- Process simple returns
- Answer product questions
- Schedule callbacks
- Transfer to human agent

ESCALATION:
Transfer to human if:
- Customer asks for human
- Technical issue beyond your knowledge
- Customer is upset
- Issue requires exception to policy
- You're unsure how to help

ACTIONS:
When taking an action, confirm first:
"I can process that return for you. You'll receive $49.99 
back to your card in 5-10 days. Should I go ahead?"
```

### Handling Voice-Specific Challenges

#### Background Noise
```python
if transcription_confidence < 0.7:
    return "I had trouble hearing that. Could you repeat 
    what you said?"
```

#### Spelling/Numbers
```
"Can you spell that for me?"
"Let me confirm: that's 1-2-3-4-5, correct?"
"Is that B as in boy, or D as in dog?"
```

#### Long Silences
```python
if silence_duration > 5_seconds:
    return "Are you still there? I'm here whenever you're ready."
```

#### Interruptions
Handle barge-in gracefully:
```
[Customer interrupts]
Agent: [Stops speaking] "Sorry, go ahead."
```

---

## Use Cases

### Inbound Support

**Order Status:**
```
Flow:
1. Greet customer
2. Ask for order number or email
3. Look up order
4. Provide status
5. Offer tracking link via text
6. Ask if anything else needed
```

**Appointment Scheduling:**
```
Flow:
1. Identify type of appointment
2. Check calendar availability
3. Offer options: "I have Tuesday at 2pm or Thursday at 10am"
4. Confirm selection
5. Send confirmation via text/email
6. Provide rescheduling info
```

**Technical Support (Tier 1):**
```
Flow:
1. Identify the issue category
2. Walk through basic troubleshooting
3. If resolved, close
4. If not resolved, escalate with context
```

### Outbound Calls

**Appointment Reminders:**
```
Agent: "Hi, this is a reminder from [Company] about your 
appointment tomorrow at 2pm with Dr. Smith. Press 1 to 
confirm, 2 to reschedule, or stay on the line to speak 
with someone."
```

**Payment Reminders:**
```
Agent: "Hi, this is [Company] calling about invoice #1234 
for $500, due in 3 days. Would you like to pay now over 
the phone, or should I send a payment link to your email?"
```

**Surveys:**
```
Agent: "Hi, this is [Company]. We'd love to hear about your 
recent experience. It'll take about 2 minutes. On a scale 
of 1-10, how likely are you to recommend us to a friend?"
```

### IVR Replacement

Transform traditional IVR:

**Before (Traditional IVR):**
```
"Press 1 for billing, press 2 for support, press 3 for 
sales, press 4 for..."
[Customer presses 2]
"For password reset, press 1, for order status, press 2..."
```

**After (AI Voice Agent):**
```
"Thanks for calling. What can I help you with?"
[Customer: "I want to know where my order is"]
"Sure, I can help with that. What's your order number?"
```

---

## Integration Patterns

### CRM Integration

```python
async def handle_call(call_data):
    # Look up customer
    customer = await crm.find_customer(call_data.phone_number)
    
    # Get context
    recent_tickets = await crm.get_recent_tickets(customer.id)
    recent_orders = await crm.get_recent_orders(customer.id)
    
    # Pass context to agent
    agent_context = {
        "customer_name": customer.name,
        "account_status": customer.status,
        "recent_issues": recent_tickets,
        "recent_orders": recent_orders
    }
    
    return agent_context
```

### Order System Integration

```python
# Function for AI to call
def lookup_order(order_id: str) -> dict:
    """Look up order status"""
    order = orders_api.get(order_id)
    return {
        "status": order.status,
        "shipped_date": order.shipped_date,
        "tracking_number": order.tracking,
        "estimated_delivery": order.eta,
        "items": order.items
    }

# Register with voice agent
agent.register_function(
    name="lookup_order",
    description="Look up order status by order ID",
    function=lookup_order
)
```

### Knowledge Base Integration

```python
async def search_knowledge_base(query: str) -> str:
    """Search KB for relevant answer"""
    results = await kb.semantic_search(query, k=3)
    
    if results:
        # Combine top results
        context = "\n".join([r.content for r in results])
        return context
    else:
        return "No relevant information found."
```

### Post-Call Automation

```python
@webhook("/call-complete")
async def handle_call_complete(data):
    # Log to CRM
    await crm.create_activity(
        contact_id=data.customer_id,
        type="phone_call",
        duration=data.duration,
        summary=data.ai_summary,
        transcript=data.transcript
    )
    
    # Create ticket if needed
    if data.escalation_needed:
        await crm.create_ticket(
            contact_id=data.customer_id,
            subject=data.issue_summary,
            description=data.transcript
        )
    
    # Send follow-up if promised
    if data.follow_up_required:
        await email.send(
            to=data.customer_email,
            template="call_follow_up",
            data=data.follow_up_content
        )
```

---

## Quality and Compliance

### Call Quality Monitoring

**Metrics to track:**
- Call completion rate
- Average handle time
- Resolution rate (vs escalation)
- Customer satisfaction (post-call survey)
- Transcript accuracy
- Response latency

**Quality scoring:**
```python
def score_call(transcript, outcome, duration):
    score = 0
    
    # Was issue resolved?
    if outcome == "resolved":
        score += 40
    elif outcome == "escalated_appropriately":
        score += 30
    
    # Appropriate duration?
    if duration < 300:  # Under 5 min
        score += 20
    elif duration < 600:  # Under 10 min
        score += 10
    
    # Followed script/guidelines?
    if confirmed_information(transcript):
        score += 20
    
    # Professional tone?
    if appropriate_tone(transcript):
        score += 20
    
    return score
```

### Compliance Considerations

**Disclosures required:**
- "This call may be recorded for quality purposes"
- Disclose if AI (depending on jurisdiction)
- PCI compliance for payments
- HIPAA for healthcare

**Data handling:**
```python
# Mask sensitive data in transcripts
def sanitize_transcript(transcript):
    # Remove credit card numbers
    transcript = re.sub(r'\b\d{4}[-\s]?\d{4}[-\s]?\d{4}[-\s]?\d{4}\b', 
                        '[CARD MASKED]', transcript)
    
    # Remove SSNs
    transcript = re.sub(r'\b\d{3}[-\s]?\d{2}[-\s]?\d{4}\b', 
                        '[SSN MASKED]', transcript)
    
    return transcript
```

**Escalation requirements:**
```
Always transfer to human:
- Customer requests human
- Legal matters mentioned
- Discrimination claims
- Security concerns
- Medical emergencies
```

### AI Disclosure Best Practices

```
Option 1 (Transparent):
"Thanks for calling. You'll be speaking with our AI 
assistant today, but I can transfer you to a person 
anytime. How can I help?"

Option 2 (Subtle):
"Thanks for calling. This is Amy, your virtual assistant. 
What can I help you with?"

Check local regulations - some jurisdictions require 
explicit AI disclosure.
```

---

## Summary

### Implementation Checklist

- [ ] Choose platform based on scale and needs
- [ ] Define use cases and flows
- [ ] Set up integrations (CRM, orders, KB)
- [ ] Train on common scenarios
- [ ] Implement escalation logic
- [ ] Set up monitoring and analytics
- [ ] Plan compliance requirements
- [ ] Test extensively
- [ ] Launch with limited hours/queue
- [ ] Scale based on performance

### Cost Analysis

| Cost Type | Traditional | AI Voice |
|-----------|------------|----------|
| Agent cost | $20-30/hr | $0.10-0.20/min |
| Per call (5 min) | $2-3 | $0.50-1.00 |
| Available hours | Business hours | 24/7 |
| Scale | Linear cost | Marginal cost |

### Expected Results

- 40-60% of calls handled without human
- 80%+ satisfaction for handled calls
- 50%+ cost reduction
- 24/7 availability

See [tickets.md](tickets.md) for AI ticket automation →
