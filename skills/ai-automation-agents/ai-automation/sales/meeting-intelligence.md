# AI Meeting Intelligence

> Complete guide to automating meeting preparation, note-taking, follow-ups, and CRM updates using AI.

---

## Table of Contents

1. [Meeting Intelligence Overview](#meeting-intelligence-overview)
2. [Pre-Meeting Preparation](#pre-meeting-preparation)
3. [During Meeting: AI Notes](#during-meeting-ai-notes)
4. [Post-Meeting Automation](#post-meeting-automation)
5. [CRM Integration](#crm-integration)
6. [Conversation Analytics](#conversation-analytics)
7. [Tools and Implementation](#tools-and-implementation)

---

## Meeting Intelligence Overview

### The Meeting Productivity Problem

Average sales rep spends:
- 30 minutes preparing for each meeting
- 15 minutes taking notes
- 20 minutes writing follow-ups
- 15 minutes updating CRM

**Total: 80 minutes per meeting on admin**

With 20 meetings/week = 26 hours/week on meeting admin

### AI Meeting Intelligence Benefits

| Task | Manual Time | AI Time | Savings |
|------|-------------|---------|---------|
| Prep research | 30 min | 5 min review | 83% |
| Note-taking | 15 min | 0 (automated) | 100% |
| Follow-up draft | 20 min | 2 min review | 90% |
| CRM update | 15 min | 1 min verify | 93% |
| **Total** | **80 min** | **8 min** | **90%** |

### The AI Meeting Stack

```
┌─────────────────────────────────────────────────────────┐
│                 AI MEETING STACK                         │
├─────────────────────────────────────────────────────────┤
│                                                          │
│  PRE-MEETING                                             │
│  ├── Calendar sync                                       │
│  ├── Attendee research                                   │
│  ├── Company intelligence                                │
│  └── Prep document generation                            │
│                                                          │
│  DURING MEETING                                          │
│  ├── Real-time transcription                             │
│  ├── Speaker identification                              │
│  └── Key point detection                                 │
│                                                          │
│  POST-MEETING                                            │
│  ├── Summary generation                                  │
│  ├── Action item extraction                              │
│  ├── Follow-up drafting                                  │
│  └── CRM updates                                         │
│                                                          │
│  ANALYTICS                                               │
│  ├── Talk ratio analysis                                 │
│  ├── Sentiment tracking                                  │
│  ├── Topic frequency                                     │
│  └── Coaching insights                                   │
│                                                          │
└─────────────────────────────────────────────────────────┘
```

---

## Pre-Meeting Preparation

### Automated Research

**Trigger:** New calendar event with external attendee

**Workflow:**
```yaml
trigger: calendar.event.created
filter: has_external_attendees

steps:
  - extract_attendees:
      get: email, name, company
      
  - for_each_attendee:
      - linkedin_research:
          get: title, experience, posts
      - company_research:
          get: industry, size, funding, news
      - crm_lookup:
          get: history, notes, deals
          
  - generate_prep_doc:
      prompt: |
        Create a meeting prep document for:
        
        Meeting: {{ meeting.title }}
        Attendees: {{ attendees_data }}
        
        Include:
        1. One-liner on each attendee
        2. Company overview
        3. Recent news/triggers
        4. Suggested talking points
        5. Potential objections
        6. Questions to ask
        7. Deal context (if existing relationship)
        
  - deliver:
      - email: 30 min before
      - slack: notification
      - notion: create meeting page
```

### Prep Document Template

```markdown
# Meeting Prep: {{ meeting_title }}

**Date:** {{ date }}
**Time:** {{ time }}
**Duration:** {{ duration }}

## Attendees

### {{ attendee_1.name }}
- **Title:** {{ title }}
- **Background:** {{ 2-3 sentence summary }}
- **LinkedIn:** {{ url }}
- **Recent Activity:** {{ recent_post_or_activity }}

### {{ company_name }}
- **Industry:** {{ industry }}
- **Size:** {{ employee_count }}
- **Recent News:** {{ news_item }}
- **Tech Stack:** {{ relevant_tech }}

## Your Relationship
- **First contact:** {{ date }} via {{ channel }}
- **Previous meetings:** {{ count }}
- **Key discussions:** {{ summary }}
- **Open items:** {{ list }}

## Suggested Agenda
1. {{ item_1 }}
2. {{ item_2 }}
3. {{ item_3 }}

## Talking Points
- {{ point_1 }}
- {{ point_2 }}
- {{ point_3 }}

## Questions to Ask
- {{ question_1 }}
- {{ question_2 }}
- {{ question_3 }}

## Potential Objections
| Objection | Response |
|-----------|----------|
| {{ objection_1 }} | {{ response_1 }} |
| {{ objection_2 }} | {{ response_2 }} |

## Goal for This Meeting
{{ specific_outcome }}
```

### Research Prompts

**Attendee Research:**
```
Based on this LinkedIn profile data:
{{ linkedin_data }}

Create a brief for a sales meeting:
1. One-liner summary of this person
2. Their likely priorities based on role
3. Communication style hints
4. How our product ([product]) relates to their role
5. Icebreaker suggestion
```

**Company Research:**
```
Based on this company information:
{{ company_data }}

Analyze for a sales conversation:
1. Company summary (2 sentences)
2. Business model
3. Likely pain points we can address
4. Competitors they might use
5. Recent events that affect our pitch
6. Decision-making process estimate
```

---

## During Meeting: AI Notes

### Real-Time Transcription Tools

**Fathom:**
- Free for individuals
- Real-time transcription
- Auto-highlights key moments
- Integrates with CRM

**Otter.ai:**
- Team collaboration
- Speaker identification
- Keyword search
- API available

**Fireflies.ai:**
- Meeting bot joins calls
- CRM integrations
- Topic tracking
- Action item detection

**Grain:**
- Clip key moments
- Share highlights
- Team collaboration
- Sales-focused

### Key Moment Detection

AI identifies and highlights:
- Questions asked
- Objections raised
- Pricing discussion
- Competition mentioned
- Next steps agreed
- Pain points expressed
- Decision timeline mentioned

### Live Assistance (Emerging)

Real-time AI suggestions:
- Objection handling tips
- Relevant case studies to mention
- Questions to ask
- Information from your CRM

---

## Post-Meeting Automation

### Summary Generation

**Prompt:**
```
Generate a meeting summary from this transcript:

{{ transcript }}

MEETING CONTEXT:
- Our company: {{ company }}
- Our product: {{ product }}
- Meeting type: {{ sales_call / demo / negotiation }}
- Stage: {{ pipeline_stage }}

Generate:

## Meeting Summary
[3-5 sentence overview of what was discussed]

## Key Discussion Points
- [Point 1]
- [Point 2]
- [Point 3]

## Action Items
- [ ] [Task] - [Owner] - [Due date if mentioned]
- [ ] [Task] - [Owner] - [Due date if mentioned]

## Customer Pain Points/Needs
- [Need 1]
- [Need 2]

## Objections/Concerns Raised
- [Objection 1] - [How it was addressed or if open]

## Competitive Mentions
- [Competitor and context]

## Next Steps
- [Agreed next step 1]
- [Agreed next step 2]

## Deal Impact
- [How this meeting affects the deal]
- [New information learned]
- [Risk factors identified]

## Follow-Up Required
- [What needs to happen next]
```

### Action Item Extraction

**Prompt:**
```
Extract action items from this meeting transcript:

{{ transcript }}

ATTENDEES:
- Our team: {{ our_attendees }}
- Customer team: {{ their_attendees }}

For each action item, provide:
1. Task description
2. Owner (who said they would do it)
3. Due date (if mentioned, otherwise estimate)
4. Priority (based on context)
5. Related deal stage

Format as JSON:
[
  {
    "task": "",
    "owner": "",
    "owner_type": "internal|customer",
    "due_date": "",
    "priority": "high|medium|low",
    "context": ""
  }
]
```

### Follow-Up Email Generation

**Prompt:**
```
Write a follow-up email after this meeting:

MEETING SUMMARY:
{{ summary }}

ACTION ITEMS:
{{ action_items }}

RECIPIENT: {{ name }}, {{ title }}
RELATIONSHIP: {{ new_contact / existing_relationship }}
TONE: {{ professional / friendly / formal }}

Write an email that:
1. Thanks them for their time
2. Summarizes key points discussed
3. Confirms action items and owners
4. Proposes next step
5. Offers additional value (resource, introduction)

Keep under 200 words. Be specific, not generic.
```

### Automated Workflow

```yaml
workflow: Post-Meeting Automation

trigger: meeting.ended (via Fathom/Otter webhook)

steps:
  - get_transcript:
      source: fathom_api
      meeting_id: {{ meeting_id }}
      
  - get_meeting_context:
      source: calendar + crm
      
  - generate_summary:
      model: claude-3-5-sonnet
      prompt: [summary_prompt]
      
  - extract_action_items:
      model: claude-3-5-sonnet
      prompt: [action_item_prompt]
      
  - draft_follow_up:
      model: claude-3-5-sonnet
      prompt: [follow_up_prompt]
      
  - update_crm:
      - create_note: {{ summary }}
      - update_deal_stage: if_applicable
      - log_activity: meeting
      
  - create_tasks:
      for_each: action_item
      in: asana / hubspot / salesforce
      
  - send_to_rep:
      slack:
        message: |
          Meeting with {{ attendee }} complete!
          
          📋 Summary ready
          ✅ {{ action_count }} action items created
          📧 Follow-up draft ready
          
          <Review in CRM>
```

---

## CRM Integration

### Automatic CRM Updates

**What to update:**

```python
def update_crm_from_meeting(meeting, summary, action_items):
    # Log activity
    crm.activities.create({
        "type": "meeting",
        "contact_ids": meeting.attendee_ids,
        "deal_id": meeting.deal_id,
        "date": meeting.date,
        "duration": meeting.duration,
        "notes": summary.full_text,
        "outcome": summary.outcome
    })
    
    # Update contact
    for attendee in meeting.external_attendees:
        crm.contacts.update(attendee.id, {
            "last_activity": meeting.date,
            "last_meeting": meeting.date,
            "notes": append(summary.key_points)
        })
    
    # Update deal
    if meeting.deal_id:
        crm.deals.update(meeting.deal_id, {
            "last_activity": meeting.date,
            "next_step": summary.next_steps[0] if summary.next_steps else None,
            "close_date": summary.timeline if mentioned else None,
            "amount": summary.budget if mentioned else None,
            "stage": suggest_stage(summary)
        })
    
    # Create tasks
    for item in action_items:
        if item.owner_type == "internal":
            crm.tasks.create({
                "title": item.task,
                "owner": map_to_crm_user(item.owner),
                "due_date": item.due_date,
                "deal_id": meeting.deal_id,
                "priority": item.priority
            })
```

### Deal Stage Suggestions

**Prompt:**
```
Based on this meeting summary, suggest the appropriate deal stage:

MEETING SUMMARY:
{{ summary }}

CURRENT STAGE: {{ current_stage }}

OUR STAGES:
1. Prospecting - Initial outreach
2. Qualification - Confirming fit
3. Discovery - Understanding needs
4. Demo - Showing product
5. Proposal - Sent pricing
6. Negotiation - Discussing terms
7. Closed Won - Deal done
8. Closed Lost - No deal

Based on the meeting content, should the stage:
- Stay the same: [reason]
- Move forward to [stage]: [reason]
- Move backward to [stage]: [reason]

Also note any red flags that suggest risk.
```

---

## Conversation Analytics

### Talk Ratio Analysis

Track for each meeting:
- Rep talk time vs prospect talk time
- Ideal: 40-60% rep / 40-60% prospect
- Monologue length (should be <2 minutes)

**Coaching insight:**
```
Meetings where rep talked >70%:
- Won rate: 23%
- Avg deal size: $8,000

Meetings where rep talked 40-60%:
- Won rate: 42%
- Avg deal size: $15,000

Recommendation: Ask more questions, talk less.
```

### Topic Analysis

Track frequency of:
- Pricing discussion
- Competitor mentions
- Feature requests
- Objections
- Decision maker references
- Timeline discussion

**Trend analysis:**
```
Q4 Trend: 45% increase in "budget freeze" mentions
Action: Update talk track to address economic concerns
```

### Sentiment Tracking

Analyze meeting tone:
- Prospect engagement level
- Positive/negative signals
- Interest indicators
- Hesitation patterns

### Team Performance

Aggregate metrics:
- Average meetings per rep
- Meeting-to-opportunity ratio
- Topics that correlate with wins
- Objections that kill deals
- Optimal meeting length

---

## Tools and Implementation

### Tool Comparison

| Tool | Best For | Price | Key Feature |
|------|----------|-------|-------------|
| Fathom | Individual reps | Free-$32/mo | Auto-summary |
| Otter.ai | Team collab | $8-30/user/mo | Speaker ID |
| Fireflies | Automation | $10-19/user/mo | CRM integration |
| Gong | Enterprise | Custom | Full analytics |
| Chorus | Enterprise | Custom | Revenue intelligence |
| Grain | Clips/sharing | $15-29/user/mo | Highlight clips |

### Implementation Workflow

**Week 1: Tool Setup**
```
- Select and deploy meeting recording tool
- Connect to calendar
- Configure CRM integration
- Set up team accounts
```

**Week 2: Workflow Creation**
```
- Build prep automation
- Create summary templates
- Set up follow-up drafts
- Configure task creation
```

**Week 3: Team Training**
```
- Train on tool usage
- Review sample outputs
- Gather feedback
- Adjust prompts
```

**Week 4: Optimization**
```
- Review meeting analytics
- Identify coaching opportunities
- Refine automation
- Document best practices
```

### n8n Meeting Workflow

```yaml
workflow: Complete Meeting Intelligence

# PRE-MEETING
pre_meeting:
  trigger: calendar.event (1 hour before)
  steps:
    - research_attendees
    - generate_prep_doc
    - send_prep_email

# POST-MEETING  
post_meeting:
  trigger: webhook (from recording tool)
  steps:
    - get_transcript
    - generate_summary
    - extract_actions
    - draft_follow_up
    - update_crm
    - create_tasks
    - notify_rep
```

---

## Summary

### Impact Metrics

| Metric | Before | After | Change |
|--------|--------|-------|--------|
| Prep time | 30 min | 5 min | -83% |
| Admin per meeting | 80 min | 8 min | -90% |
| CRM data quality | 40% | 95% | +138% |
| Follow-up within 24h | 60% | 95% | +58% |
| Rep selling time | 35% | 60% | +71% |

### Getting Started

1. **Day 1:** Set up Fathom (free)
2. **Day 2:** Build prep automation
3. **Day 3:** Create post-meeting workflow
4. **Day 4:** Connect to CRM
5. **Day 5:** Train team and launch

See [../workflows/n8n/templates.md](../workflows/n8n/templates.md) for workflow templates →
