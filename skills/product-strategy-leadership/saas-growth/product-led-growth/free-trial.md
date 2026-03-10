# Free Trial Optimization

## Introduction

Free trials are the workhorse of PLG conversion. They let potential customers experience your product before committing, reducing risk and building confidence. But a free trial isn't just "give access for 14 days and hope they convert"—it's a carefully designed experience that guides users to value, demonstrates the product's worth, and creates compelling reasons to pay.

This guide covers everything you need to know about optimizing free trials: length, structure, onboarding, triggers, and benchmarks.

---

## 1. Trial Length Optimization

### The Trial Length Decision

Trial length is one of the most debated decisions in PLG. Too short and users don't have time to realize value. Too long and they lose urgency to convert.

**Common Trial Lengths:**

| Length | Best For | Examples |
|--------|----------|----------|
| 7 days | Quick time-to-value, urgency-driven | Simple tools, mobile apps |
| 14 days | Most B2B SaaS, standard choice | Slack, Notion, most SaaS |
| 30 days | Complex products, longer sales cycles | Enterprise tools, platforms |
| Usage-based | API products, infrastructure | Twilio, Stripe, AWS |

### Factors That Determine Optimal Length

**Product Complexity:**
- Simple tool (scheduling, forms): 7-14 days
- Medium complexity (CRM, project management): 14-21 days
- Complex platform (data warehouse, ERP): 30+ days

**Time to Value:**
- If value happens in first session: Shorter trial OK
- If value requires data/integration: Longer trial needed
- If value builds over time: Longer trial better

**Sales Cycle:**
- Self-serve SMB: 7-14 days
- Mid-market with sales: 14-30 days
- Enterprise: 30+ days or POC

**Decision Maker:**
- Individual user: Shorter trial
- Team evaluation: Longer trial (need to involve others)
- Committee decision: Longest trial (or sales involvement)

### Testing Trial Length

**A/B Test Approach:**

```
Hypothesis: 14-day trial will convert better than 7-day trial
Control: 7-day trial (current)
Variant: 14-day trial
Metric: Trial → Paid conversion rate
Secondary: Time to convert, revenue per trialer

Run until statistical significance (typically 1000+ trials per variant)
```

**What to Measure:**
- Conversion rate (primary)
- Average days to convert
- Activation rate within trial
- Revenue per trial (conversion × ACV)

**Common Findings:**
- Longer trials often have LOWER conversion rates
- But sometimes higher revenue (larger deals)
- Very short trials can feel pushy
- Very long trials lose urgency

### Trial Length Benchmarks

| Trial Length | Typical Conversion Rate |
|--------------|------------------------|
| 7-day | 12-20% |
| 14-day | 10-18% |
| 30-day | 8-15% |

**Note:** Shorter trials often convert higher % but may convert smaller deals.

### Extending Trials

**When to Offer Extension:**
- User requests it
- User is active but not converted
- High-potential account (PQL)
- Sales is engaged

**How to Offer:**
- Automatic extension for active users
- Manual extension via sales/success
- Extension in exchange for feedback
- Extension for completing setup steps

**Extension Strategy:**
```
Day 12 (of 14): 
"Need more time? Complete these 3 setup steps for 7 more days."

Day 14 (no extension):
"Trial ending. Ready to continue? Here's 20% off annual."

Day 14 (with extension):
"You've earned 7 more days! Make the most of it with these features."
```

---

## 2. Time-to-Value Reduction

### What is Time-to-Value (TTV)?

**Time-to-Value:** The time from signup to when a user experiences meaningful value from your product.

**Why TTV Matters:**
- Shorter TTV = higher activation rates
- Shorter TTV = higher trial conversion
- Shorter TTV = better retention
- Every hour of TTV adds friction

### Measuring Time-to-Value

**Define Your Value Moment:**

| Product | Value Moment | Typical TTV |
|---------|--------------|-------------|
| Calendly | First meeting scheduled | 10-30 minutes |
| Slack | First team conversation | 15-60 minutes |
| Mailchimp | First email sent | 1-2 hours |
| Salesforce | First deal tracked | 2-5 days |
| Snowflake | First query run | 1-3 days |

**Calculate TTV:**
```
TTV = Time of Value Moment - Time of Signup

Median TTV = Median of all users who reached value moment
% Reaching Value = Users reaching moment / Total signups
```

### Strategies to Reduce TTV

**1. Simplify Signup**

Every field adds friction:
- Email-only signup (verify later)
- Social login (Google, GitHub)
- Defer company info until needed
- No credit card required

**Before:** Name, email, company, company size, role, phone, password, confirm password
**After:** Email, password (or Google login)

**2. Smart Defaults**

Don't make users configure from scratch:
- Pre-populate settings based on common choices
- Use signup info to customize
- Default to most popular options
- Allow customization later

**Example:** 
Instead of: "What timezone?" (dropdown of 400 options)
Try: Detect from browser, show: "Your timezone: PT. Change?"

**3. Template Starting Points**

Don't start users with a blank slate:
- Pre-built templates
- Sample data
- Example projects
- Starter content

**Example (Notion):**
- Offer template: "Personal Wiki," "Team Wiki," "Project Tracker"
- User picks one, has something to customize immediately
- vs. blank page paralysis

**4. Progressive Onboarding**

Don't frontload all setup:
- Get to value first
- Add complexity later
- Teach features when needed
- Just-in-time guidance

**Example:**
```
Step 1: Create first project (value)
Step 2: Invite teammate (more value)
Step 3: Connect integration (extended value)
Step 4: Set up reporting (advanced value)

NOT: Set up company → Set up team → Configure integrations → Create project
```

**5. Quick Win First**

Design for immediate success:
- First action should succeed
- Celebrate small wins
- Build momentum
- Delay complex tasks

**Example (Email Marketing):**
```
Traditional: Import contacts → Create template → Write email → Send
Quick Win: Write a quick email → Send to yourself → See it work → Now import contacts
```

### TTV Benchmarks

| TTV | Rating | Action |
|-----|--------|--------|
| < 5 minutes | Excellent | Maintain and optimize |
| 5-30 minutes | Good | Look for quick wins |
| 30 min - 2 hours | Fair | Significant optimization needed |
| > 2 hours | Poor | Major onboarding overhaul |
| > 1 day | Critical | Product/process redesign |

---

## 3. Trial Onboarding

### The Trial Onboarding Framework

Trial onboarding should accomplish:
1. Get user to value moment ASAP
2. Build habit and engagement
3. Show product breadth
4. Create conversion context

### Onboarding Channels

**1. In-App Guidance**

- Product tours
- Tooltips
- Checklists
- Progress bars
- Empty state guidance
- Contextual help

**2. Email Sequences**

- Welcome email
- Getting started tips
- Feature highlights
- Use case inspiration
- Trial reminder
- Conversion nudge

**3. Human Touch (Scaled)**

- Chat support
- CS check-ins (for high-value)
- Webinars
- Office hours

### The Onboarding Checklist

**Why Checklists Work:**
- Clear progress indication
- Gamification (completion dopamine)
- Guides to key actions
- Shows what "done" looks like

**Checklist Best Practices:**

1. **5-7 items maximum**: More is overwhelming
2. **First item auto-completed**: Momentum from start
3. **Each item = value milestone**: Not arbitrary tasks
4. **Visual progress**: Progress bar, completion %
5. **Reward completion**: Unlock features, extended trial, badge

**Example Checklist (Project Management Tool):**

```
Getting Started (3/6 complete)
────────────────────────────────────────
✓ Create your account
✓ Create your first project
✓ Add a task
○ Invite a teammate
○ Set a due date
○ Complete a task
────────────────────────────────────────
Complete all steps for 7 extra trial days!
```

### Trial Email Sequences

**Day 0: Welcome Email**
```
Subject: Welcome to [Product]! Let's get you started

Hi [Name],

Welcome! You're one step away from [main benefit].

Here's how to get started in the next 5 minutes:
1. [First step with link]
2. [Second step with link]
3. [Third step with link]

Questions? Just reply to this email.

[CTA: Go to Dashboard]
```

**Day 1: First Value Check-in**
```
Subject: Did you [achieve value moment] yet?

Hi [Name],

Congrats on signing up! Most successful users [achieve X] in their first day.

Have you [value moment] yet?

If not, here's a 2-minute guide: [Link]

Already done it? Great! Here's what to do next: [Link]
```

**Day 3: Feature Highlight**
```
Subject: Have you tried [popular feature]?

Hi [Name],

Our most successful users love [Feature]. It helps them [benefit].

Here's how to use it: [Link/GIF]

[CTA: Try Feature Now]
```

**Day 7 (of 14): Mid-Trial Check-in**
```
Subject: One week down—how's it going?

Hi [Name],

You're halfway through your trial! Here's what you've accomplished:
- Created [X] projects
- Invited [Y] teammates
- [Other progress]

To get even more value, try:
- [Advanced feature]
- [Integration]

Questions? Book a quick call: [Link]
```

**Day 12: Trial Ending**
```
Subject: 2 days left in your trial

Hi [Name],

Your trial ends in 2 days. Here's what happens next:
- Your data stays safe
- Free tier: [what's included]
- Upgrade: [full access for $X/month]

Ready to continue? [Upgrade CTA]

Want more time? Reply and let us know why.
```

**Day 14: Trial Expired**
```
Subject: Your trial has ended—but your data is safe

Hi [Name],

Your trial ended today. Your [X projects and Y data] are still here.

You're now on our free plan with:
- [Limited feature]
- [Usage limit]

Ready for full access? [Upgrade for $X/month]

We'd love to have you as a customer!
```

### Onboarding Personalization

**Segment by Use Case:**
- Ask during signup: "What will you use this for?"
- Customize onboarding based on answer
- Show relevant templates/examples
- Adjust email content

**Segment by Role:**
- Technical vs. non-technical
- Individual vs. team admin
- Executive vs. practitioner
- Different guidance for each

**Segment by Behavior:**
- Active users: Feature education
- Inactive users: Re-engagement
- Power users: Advanced tips
- Struggling users: Basic help

---

## 4. Conversion Triggers

### Understanding Conversion Psychology

Users convert when:
1. They've experienced value (believe it works)
2. They anticipate future value (want to continue)
3. There's a reason to act now (urgency)
4. The risk feels low (trust/guarantee)

### Trigger Types

**1. Usage Limit Triggers**

Hit a limit → natural conversion point

Examples:
- Storage full (Dropbox)
- Meeting time up (Zoom 40-min)
- Contact limit reached (Mailchimp)
- Project limit hit

**Optimization:**
- Set limits that most active users hit
- Show limit approaching (warning)
- Make upgrade path obvious
- Don't cut off mid-action

**2. Feature Gate Triggers**

Need advanced feature → upgrade required

Examples:
- Need reporting → upgrade
- Need integrations → upgrade
- Need custom branding → upgrade

**Optimization:**
- Show locked features during trial
- Let them TRY the feature, then gate
- Highlight in-app when relevant

**3. Team Growth Triggers**

Adding more users → upgrade needed

Examples:
- Free tier for 1 user → paid for team
- Invite limit reached
- Admin features needed

**Optimization:**
- Make inviting easy during trial
- Show collaboration benefits
- Gate team features at right threshold

**4. Time Triggers**

Trial ending → decision required

Examples:
- X days left notifications
- Trial expiration
- Limited-time offer

**Optimization:**
- Multiple touchpoints (7 days, 3 days, 1 day)
- Clear communication of what happens
- Offer extension if engaged

**5. Value Triggers**

Realize value → willing to pay

Examples:
- "You saved 5 hours this month"
- "You tracked $50K in deals"
- "Your NPS improved by 20 points"

**Optimization:**
- Calculate and show value delivered
- Tie to their business metrics
- Compare to cost of product

### Conversion Trigger Timing

```
Trial Journey:
Day 1 ────────────────────────────────────── Day 14 → Expire

Value Triggers:    Feature Triggers:    Time Triggers:
   │                     │                    │
   ▼                     ▼                    ▼
[Celebrate     [Show upgrade      [7 days    [1 day
 quick wins]    when hit gate]     left]      left]
```

### Conversion CTAs

**In-App Upgrade Prompts:**

```
┌─────────────────────────────────────────────┐
│ ⚡ Upgrade to Pro                           │
│                                             │
│ You've used 8 of 10 projects.              │
│ Upgrade for unlimited projects +            │
│ advanced reporting.                         │
│                                             │
│ [Upgrade Now - $29/mo]    [Maybe Later]    │
└─────────────────────────────────────────────┘
```

**Pricing Page Design:**

Make the recommended plan obvious:
- Visual highlight (badge, color)
- "Most Popular" label
- Price anchor with higher tier
- Clear feature comparison

---

## 5. Trial-to-Paid Benchmarks

### Conversion Rate Benchmarks

**Overall Benchmarks:**

| Trial Type | Good | Great | Excellent |
|------------|------|-------|-----------|
| No credit card required | 3-5% | 5-10% | 10-15% |
| Credit card required | 25-40% | 40-50% | 50-60% |
| Freemium to paid | 2-5% | 5-8% | 8-12% |

**By Company Stage:**

| Stage | Typical | Target |
|-------|---------|--------|
| Pre-PMF | 2-5% | 5%+ to validate |
| Early | 5-10% | 10-15% |
| Growth | 10-15% | 15-20% |
| Mature | 15-25% | 20-30% |

**By Customer Segment:**

| Segment | Typical Conversion |
|---------|-------------------|
| Consumer | 2-5% |
| SMB | 5-15% |
| Mid-Market | 15-30% |
| Enterprise | 30-50%+ |

### Trial Metrics Dashboard

**Track These Weekly:**

| Metric | This Week | Last Week | Benchmark |
|--------|-----------|-----------|-----------|
| Trial Starts | 500 | 480 | - |
| Activated (reached value) | 250 (50%) | 240 (50%) | >40% |
| Active Day 7 | 150 (30%) | 140 (29%) | >25% |
| Converted | 50 (10%) | 48 (10%) | >8% |
| Revenue from Trials | $5,000 | $4,800 | - |

**Funnel Analysis:**

```
Trial Signups:        500 (100%)
      ↓
Completed Signup:     475 (95%)
      ↓
First Action:         400 (80%)
      ↓
Value Moment:         250 (50%)
      ↓
Active Week 2:        150 (30%)
      ↓
Converted:            50 (10%)
```

**Where to Focus:**
- Signup → First Action: Onboarding problem
- First Action → Value: TTV problem
- Value → Active: Engagement problem
- Active → Converted: Conversion problem

### Improving Trial Conversion

**Quick Wins:**

1. **Reduce signup friction**
   - Remove unnecessary fields
   - Add social login
   - Impact: 10-30% more signups

2. **Add onboarding checklist**
   - Guide to key actions
   - Show progress
   - Impact: 15-25% better activation

3. **Improve trial emails**
   - Send at right times
   - Clear CTAs
   - Impact: 10-20% better conversion

4. **Optimize pricing page**
   - Clear tier comparison
   - Highlight recommended
   - Impact: 5-15% better conversion

5. **Add in-app upgrade prompts**
   - Show at right moments
   - Clear value proposition
   - Impact: 10-20% better conversion

**Deeper Improvements:**

1. **Reduce time-to-value**
   - Simplify first experience
   - Add templates/defaults
   - Impact: 20-40% better activation

2. **Add feature gates**
   - Show premium features
   - Gate at right threshold
   - Impact: 10-20% better conversion

3. **Build PQL model**
   - Identify hot leads
   - Prioritize sales/success touch
   - Impact: 20-30% better enterprise conversion

4. **Personalize onboarding**
   - By use case
   - By segment
   - Impact: 15-25% better activation

---

## Summary: Trial Optimization Framework

### The Trial Success Equation

```
Trial Conversion = f(TTV, Activation, Engagement, Triggers, Trust)

Where:
- TTV: Time to Value (shorter = better)
- Activation: % reaching value moment
- Engagement: Sustained usage during trial
- Triggers: Reasons to convert now
- Trust: Confidence in the product/company
```

### Trial Optimization Checklist

**Setup:**
- [ ] Right trial length for product complexity
- [ ] No credit card required (or tested)
- [ ] Simple signup flow
- [ ] Clear expectations set

**Time-to-Value:**
- [ ] Value moment defined and measured
- [ ] TTV < 30 minutes for most users
- [ ] Templates/defaults available
- [ ] Progressive onboarding

**Activation:**
- [ ] Onboarding checklist
- [ ] Welcome email sequence
- [ ] In-app guidance
- [ ] Success milestones defined

**Engagement:**
- [ ] Day 3/7/10 email touchpoints
- [ ] Feature education in-app
- [ ] Re-engagement for inactive
- [ ] Personalization by segment

**Conversion:**
- [ ] Clear pricing page
- [ ] In-app upgrade prompts
- [ ] Usage limit triggers
- [ ] Trial ending reminders
- [ ] Easy checkout flow

### Key Metrics to Track

1. **Trial starts**: Volume entering funnel
2. **Activation rate**: % reaching value moment
3. **Day 7 retention**: % still active mid-trial
4. **Conversion rate**: % becoming paying
5. **Time to convert**: Days from start to paid
6. **Revenue per trial**: Conversion × Average ACV

---

*Next: [Freemium Strategy](./freemium.md)*
