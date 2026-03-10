# Reducing Voluntary Churn

## Introduction

Voluntary churn—customers actively choosing to leave—is the most challenging type of churn to address because it reflects a conscious decision that your product no longer delivers sufficient value. This guide provides comprehensive strategies for predicting, preventing, and recovering from voluntary churn.

---

## 1. Customer Health Scores

### What is a Customer Health Score?

A customer health score is a composite metric that predicts the likelihood of a customer renewing or churning. It combines multiple signals into a single, actionable number.

### Building a Health Score Model

**Step 1: Identify Signals**

| Category | Signals |
|----------|---------|
| Usage | Login frequency, feature usage, time in app |
| Adoption | % of features used, depth of usage |
| Engagement | Email opens, support tickets, NPS |
| Relationship | Executive sponsor engaged, champion active |
| Commercial | Payment history, expansion history |

**Step 2: Weight Signals**

Based on correlation with churn/retention:

| Signal | Weight | Churn Correlation |
|--------|--------|-------------------|
| Login frequency | 25% | Strong negative |
| Core feature usage | 30% | Strong negative |
| Support ticket sentiment | 15% | Medium |
| NPS score | 15% | Medium |
| Contract value trend | 15% | Medium |

**Step 3: Calculate Score**

```
Health Score = Σ (Signal Value × Signal Weight)

Score ranges:
0-40: Critical (high churn risk)
40-60: At risk (monitor closely)
60-80: Healthy (normal)
80-100: Strong (expansion opportunity)
```

### Example Health Score Calculation

```
Customer: Acme Corp

Signals:
- Login frequency: 8/10 (logged in 20/30 days)
- Feature usage: 7/10 (using 70% of features)
- Support sentiment: 6/10 (neutral tickets)
- NPS: 8/10 (NPS score of 8)
- Contract trend: 9/10 (expanded last quarter)

Health Score:
= (8 × 0.25) + (7 × 0.30) + (6 × 0.15) + (8 × 0.15) + (9 × 0.15)
= 2.0 + 2.1 + 0.9 + 1.2 + 1.35
= 7.55/10 or 75.5%

Status: Healthy
```

### Health Score Actions

| Score | Status | Action |
|-------|--------|--------|
| 80-100 | Strong | Expansion outreach, case study request |
| 60-80 | Healthy | Standard success activities |
| 40-60 | At Risk | Proactive check-in, usage review |
| 0-40 | Critical | Immediate intervention, exec engagement |

---

## 2. Proactive Outreach

### Timing Proactive Engagement

**Trigger-Based Outreach:**

| Trigger | Timing | Action |
|---------|--------|--------|
| Health drops below 60 | Within 24 hours | CSM check-in call |
| No login in 14 days | Day 14 | Automated email + CSM alert |
| Support ticket negative | Same day | Manager review, outreach |
| Usage down 30% MoM | Monthly review | Success review meeting |
| Champion leaves company | Within 48 hours | New champion cultivation |

### Proactive Check-In Templates

**Health Score Drop:**
```
Subject: Quick check-in from [Product]

Hi [Name],

I noticed your team's usage of [Product] has dropped recently. 
Just wanted to reach out and see if everything's okay.

Are there any blockers or concerns I can help with?

If helpful, I'd love to schedule a quick 15-minute call to:
• Understand what's changed
• Share some tips for [specific use case]
• Make sure you're getting maximum value

[Calendar Link]

Here for you,
[CSM Name]
```

**No Login Alert:**
```
Subject: Missing you at [Product]

Hi [Name],

It's been a couple weeks since you logged into [Product]. 
I wanted to check in and make sure everything's alright.

If you're stuck or need help getting back on track, 
I'm here. Here are some quick resources:

• [Getting started guide]
• [Popular feature tutorial]
• [Book time with me]

Is there anything specific I can help with?

[CSM Name]
```

**Champion Departure:**
```
Subject: Changes at [Company] — how can I help?

Hi [New Contact],

I understand [Previous Champion] has moved on from [Company]. 
I wanted to reach out and introduce myself as your 
[Product] Customer Success Manager.

[Previous Champion] and I worked on [initiatives/projects]. 
I'd love to continue supporting your team's success.

Would you have 30 minutes to connect? I can bring you up 
to speed on your account and learn about your priorities.

[Calendar Link]

Looking forward to working together,
[CSM Name]
```

---

## 3. Success Milestones

### Defining Success Milestones

Success milestones are achievable outcomes that demonstrate value and build commitment.

**Example Milestones (Project Management Tool):**

| Milestone | Target | Timeframe |
|-----------|--------|-----------|
| First project created | 1 | Day 1 |
| Task completed | 5 | Week 1 |
| Teammate invited | 1 | Week 1 |
| First sprint completed | 1 | Month 1 |
| First report generated | 1 | Month 1 |
| Integration connected | 1 | Month 2 |
| Team adoption | 80% of seats | Month 3 |

### Milestone-Based Communication

**Milestone Achieved:**
```
Subject: 🎉 Congratulations on [Milestone]!

Hi [Name],

You just [achieved milestone]! 

Here's what that means:
• [Impact 1]
• [Impact 2]

What's next? Try:
• [Next recommended action]
• [Advanced feature to explore]

Keep up the great work!
[CSM Name]
```

**Milestone Overdue:**
```
Subject: How can I help you [achieve milestone]?

Hi [Name],

I noticed your team hasn't [completed milestone] yet. 
Most teams like yours do this by [timeframe].

Common blockers I see:
• [Issue 1] — [Quick solution]
• [Issue 2] — [Quick solution]

Would a quick 15-minute walkthrough help?
[Calendar Link]

[CSM Name]
```

---

## 4. Engagement Triggers

### Automated Engagement System

**Positive Triggers (Celebrate):**

| Trigger | Response |
|---------|----------|
| Heavy usage week | In-app celebration + tips |
| Feature milestone | Achievement email |
| Team growth | Welcome new members |
| Success metric hit | ROI summary email |

**Negative Triggers (Intervene):**

| Trigger | Response |
|---------|----------|
| Usage decline | Check-in email |
| Feature abandonment | Re-education email |
| Support issue | Follow-up satisfaction |
| Inactivity | Re-engagement sequence |

### Engagement Automation Examples

**Usage Spike Response:**
```
Trigger: User has 2x normal usage this week

Subject: You've been busy! 🚀

Hi [Name],

Noticed you've been putting [Product] to work this week:
• [X] [actions] completed
• [Y]% more than last week

You're clearly getting things done! 

Pro tip: Try [feature] to be even more efficient.
[Link to feature]

Keep crushing it,
[Product] Team
```

**Feature Abandonment Response:**
```
Trigger: User tried feature but hasn't returned in 7 days

Subject: Quick tip for [Feature]

Hi [Name],

I noticed you explored [Feature] last week but haven't 
been back. Totally normal—it can take a minute to click.

Here's a 2-minute video that shows the power of [Feature]:
[Video link]

Or if [Feature] isn't what you need, let me know what 
you're trying to accomplish. I might have suggestions.

[CSM Name]
```

---

## 5. NPS and Feedback Loops

### NPS Implementation

**When to Survey:**
- After key milestones (activation, 30 days, 90 days)
- Before renewal (60-90 days out)
- After major interactions (support, onboarding)
- Regular cadence (quarterly)

**NPS Survey Format:**
```
On a scale of 0-10, how likely are you to recommend 
[Product] to a colleague?

[0] [1] [2] [3] [4] [5] [6] [7] [8] [9] [10]

What's the primary reason for your score?
[Text field]
```

### NPS Follow-Up Actions

| Score | Category | Action |
|-------|----------|--------|
| 9-10 | Promoter | Thank, request case study/review |
| 7-8 | Passive | Understand gaps, improve experience |
| 0-6 | Detractor | Immediate outreach, escalate |

**Promoter Response:**
```
Subject: Thank you! One small favor?

Hi [Name],

Thank you for the kind score! It means a lot to hear 
you'd recommend us.

If you have 2 minutes, would you share your experience 
on G2? It helps others find us.

[Review Link]

Thank you for being an amazing customer!
[CSM Name]
```

**Detractor Response:**
```
Subject: We want to make this right

Hi [Name],

Thank you for your honest feedback. I'm sorry we're 
not meeting your expectations.

I'd really like to understand what's not working and 
see if we can fix it. Do you have 15 minutes this week?

[Calendar Link]

Your feedback is valuable—even when it's hard to hear.

[CSM Name]
```

### Closing the Feedback Loop

**Key Principle:** Always respond to feedback, and show action.

**Feedback Closed Loop:**
```
Subject: You asked, we listened

Hi [Name],

Remember when you mentioned [feedback]?

We heard you. Here's what we did:
• [Action 1]
• [Action 2]

This is now live in [Product]. Check it out!

Thank you for helping us improve.
[Product] Team
```

---

## 6. Win-Back After Churn

### Win-Back Timeline

| Day | Action | Goal |
|-----|--------|------|
| 0 | Exit survey | Understand reason |
| 1 | Personalized goodbye | Leave door open |
| 7 | First win-back | Immediate return |
| 30 | What's new | Feature updates |
| 60 | Incentive | Return offer |
| 90 | Final | Last direct attempt |
| Ongoing | Newsletter | Stay in touch |

### Win-Back by Churn Reason

**Reason: Too Expensive**
```
Offer: Lower tier or discount
Message: "We have a plan that might fit your budget"
```

**Reason: Missing Features**
```
Trigger: When feature ships
Message: "Remember that feature you wanted? It's here!"
```

**Reason: Switched to Competitor**
```
Message: Share differentiation or improvements
Timing: Wait for potential dissatisfaction (90 days)
```

**Reason: No Longer Needed**
```
Message: New use cases or features
Timing: Quarterly check-ins on business changes
```

### Win-Back Metrics

| Metric | Target |
|--------|--------|
| Win-back attempt rate | 100% |
| Win-back response rate | >20% |
| Win-back success rate | 5-15% |
| Time to win-back | <90 days |

---

## Summary: Voluntary Churn Reduction Framework

### Key Strategies

1. **Predict with Health Scores**: Know who's at risk
2. **Prevent with Proactive Outreach**: Intervene early
3. **Prove with Success Milestones**: Demonstrate value
4. **Engage with Automation**: Scale personal touch
5. **Listen with NPS**: Capture feedback
6. **Recover with Win-Back**: Second chances work

### Voluntary Churn Checklist

- [ ] Health score model built
- [ ] Triggers defined and automated
- [ ] Proactive outreach templates
- [ ] Success milestones mapped
- [ ] NPS implemented
- [ ] Feedback loop closed
- [ ] Win-back sequence created
- [ ] Churn reasons tracked

---

*Next: [Involuntary Churn](./involuntary-churn.md)*
