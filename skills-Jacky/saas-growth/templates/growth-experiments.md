# Growth Experiment Templates

## Introduction

Systematic experimentation is the key to sustainable SaaS growth. This comprehensive collection of growth experiment templates provides ready-to-use frameworks for testing hypotheses across acquisition, activation, retention, referral, and revenue. Each template includes the hypothesis, implementation steps, metrics to track, and expected results.

---

## 1. Experimentation Framework

### The Growth Experiment Process

```
┌─────────────────────────────────────────────────────────┐
│                 GROWTH EXPERIMENT CYCLE                 │
├─────────────────────────────────────────────────────────┤
│                                                         │
│    1. IDEATE                                           │
│    Generate hypotheses from data and insights          │
│                          ↓                             │
│    2. PRIORITIZE                                       │
│    Score by impact, confidence, ease (ICE)            │
│                          ↓                             │
│    3. DESIGN                                           │
│    Define test, metrics, success criteria             │
│                          ↓                             │
│    4. IMPLEMENT                                        │
│    Build experiment, launch test                      │
│                          ↓                             │
│    5. ANALYZE                                          │
│    Review results, statistical significance           │
│                          ↓                             │
│    6. DECIDE                                           │
│    Ship, iterate, or kill                             │
│                          ↓                             │
│    7. DOCUMENT                                         │
│    Record learnings for future reference              │
│                          │                             │
│                          └──────→ Back to 1.           │
│                                                         │
└─────────────────────────────────────────────────────────┘
```

### Experiment Template Structure

```
EXPERIMENT: [Name]
═══════════════════════════════════════════════════

HYPOTHESIS
────────────────────────────────────────────────
If we [do this change]
Then [this metric] will [improve by X%]
Because [reasoning]

DETAILS
────────────────────────────────────────────────
Area: [Acquisition/Activation/Retention/Referral/Revenue]
Metric: [Primary metric]
Baseline: [Current performance]
Goal: [Target improvement]
Duration: [Test length]
Sample: [Required sample size]

IMPLEMENTATION
────────────────────────────────────────────────
Control: [Current experience]
Variant: [New experience]
Traffic: [% to each variant]
Targeting: [Who sees this]

RESULTS
────────────────────────────────────────────────
Status: [Running/Complete]
Winner: [Control/Variant/Inconclusive]
Lift: [+X% / -X%]
Confidence: [XX%]
Learning: [Key insight]

NEXT STEPS
────────────────────────────────────────────────
[Ship/Iterate/Kill]
═══════════════════════════════════════════════════
```

---

## 2. Acquisition Experiments

### Experiment: Homepage Headline Test

```
EXPERIMENT: Homepage Headline Optimization
═══════════════════════════════════════════════════

HYPOTHESIS
────────────────────────────────────────────────
If we change the homepage headline from feature-focused 
to benefit-focused, then signup rate will increase by 15%
because visitors care more about outcomes than features.

DETAILS
────────────────────────────────────────────────
Area: Acquisition
Metric: Visitor-to-signup rate
Baseline: 2.5%
Goal: 2.9%
Duration: 2 weeks
Sample: 10,000 visitors per variant

IMPLEMENTATION
────────────────────────────────────────────────
Control: "The All-in-One CRM Platform"
Variant A: "Close More Deals in Less Time"
Variant B: "The CRM 10,000 Sales Teams Trust"
Traffic: 33% each
Targeting: All homepage visitors

METRICS TO TRACK
────────────────────────────────────────────────
- Signup rate (primary)
- Scroll depth
- CTA clicks
- Bounce rate
═══════════════════════════════════════════════════
```

### Experiment: Social Proof Placement

```
EXPERIMENT: Logo Bar Above Fold
═══════════════════════════════════════════════════

HYPOTHESIS
────────────────────────────────────────────────
If we add customer logos above the fold on the homepage,
then signup rate will increase by 10% because social 
proof builds immediate trust.

DETAILS
────────────────────────────────────────────────
Area: Acquisition
Metric: Visitor-to-signup rate
Baseline: 2.5%
Goal: 2.75%
Duration: 2 weeks
Sample: 8,000 visitors per variant

IMPLEMENTATION
────────────────────────────────────────────────
Control: Logos below fold
Variant: Logos above fold, under headline
Traffic: 50/50
Targeting: All homepage visitors

VARIANTS
────────────────────────────────────────────────
Control:
[Headline]
[Subheadline]
[CTA]
---scroll---
[Logos]

Variant:
[Headline]
[Logo bar: "Trusted by"]
[Subheadline]
[CTA]
═══════════════════════════════════════════════════
```

### Experiment: Pricing Page CTA

```
EXPERIMENT: Pricing Page CTA Copy Test
═══════════════════════════════════════════════════

HYPOTHESIS
────────────────────────────────────────────────
If we change the CTA from "Start Free Trial" to 
"Start Building Free" then click rate will increase 
by 20% because it emphasizes immediate value.

DETAILS
────────────────────────────────────────────────
Area: Acquisition
Metric: CTA click rate
Baseline: 8%
Goal: 9.6%
Duration: 2 weeks
Sample: 5,000 pricing page visitors per variant

IMPLEMENTATION
────────────────────────────────────────────────
Control: "Start Free Trial"
Variant A: "Start Building Free"
Variant B: "Get Started — It's Free"
Variant C: "Try [Product] Free"
Traffic: 25% each
Targeting: All pricing page visitors
═══════════════════════════════════════════════════
```

---

## 3. Activation Experiments

### Experiment: Onboarding Checklist

```
EXPERIMENT: Onboarding Checklist Implementation
═══════════════════════════════════════════════════

HYPOTHESIS
────────────────────────────────────────────────
If we add a progress checklist to onboarding,
then activation rate will increase by 25% because
users will have clear guidance on next steps.

DETAILS
────────────────────────────────────────────────
Area: Activation
Metric: Activation rate (Day 7)
Baseline: 40%
Goal: 50%
Duration: 4 weeks
Sample: 1,000 new signups per variant

IMPLEMENTATION
────────────────────────────────────────────────
Control: No checklist, standard dashboard
Variant: Sidebar checklist with 5 steps:
  □ Complete profile
  □ Create first project
  □ Invite a teammate
  □ Connect an integration
  □ Run first report

Traffic: 50/50
Targeting: New signups only

METRICS TO TRACK
────────────────────────────────────────────────
- Activation rate (primary)
- Time to activation
- Checklist completion rate
- Day 7 retention
- Feature adoption
═══════════════════════════════════════════════════
```

### Experiment: Welcome Email Sequence

```
EXPERIMENT: Welcome Email Optimization
═══════════════════════════════════════════════════

HYPOTHESIS
────────────────────────────────────────────────
If we send a 5-email welcome sequence instead of 
a single welcome email, then activation will increase
by 20% because multiple touchpoints reinforce activation.

DETAILS
────────────────────────────────────────────────
Area: Activation
Metric: Email-attributed activation rate
Baseline: 25%
Goal: 30%
Duration: 4 weeks
Sample: 2,000 new signups per variant

IMPLEMENTATION
────────────────────────────────────────────────
Control: 
- Day 0: Welcome email only

Variant:
- Day 0: Welcome + quick win
- Day 1: Feature highlight
- Day 3: Success story
- Day 5: Tips from power users
- Day 7: Check-in + offer help

Traffic: 50/50
Targeting: All new signups
═══════════════════════════════════════════════════
```

### Experiment: First Run Experience

```
EXPERIMENT: Interactive Product Tour
═══════════════════════════════════════════════════

HYPOTHESIS
────────────────────────────────────────────────
If we add an interactive product tour on first login,
then time to first value will decrease by 40% because
users will understand core features faster.

DETAILS
────────────────────────────────────────────────
Area: Activation
Metric: Time to first value action
Baseline: 45 minutes
Goal: 27 minutes
Duration: 3 weeks
Sample: 800 new users per variant

IMPLEMENTATION
────────────────────────────────────────────────
Control: Static help docs link
Variant: Step-by-step tour with:
  1. Welcome modal explaining value
  2. Highlight #1: Create workspace
  3. Highlight #2: Key feature
  4. Highlight #3: Invite team
  5. Completion celebration

Traffic: 50/50
Targeting: First-time logins
═══════════════════════════════════════════════════
```

---

## 4. Retention Experiments

### Experiment: Engagement Email Triggers

```
EXPERIMENT: Inactivity Re-engagement Emails
═══════════════════════════════════════════════════

HYPOTHESIS
────────────────────────────────────────────────
If we send personalized re-engagement emails after 
7 days of inactivity, then Day 30 retention will 
increase by 15% because we'll recover lapsing users.

DETAILS
────────────────────────────────────────────────
Area: Retention
Metric: Day 30 retention rate
Baseline: 35%
Goal: 40%
Duration: 6 weeks
Sample: 1,500 inactive users per variant

IMPLEMENTATION
────────────────────────────────────────────────
Control: No inactivity email
Variant: 3-email sequence:
  - Day 7: "We miss you" + one quick action
  - Day 10: New feature announcement
  - Day 14: Final "how can we help?"

Traffic: 50/50
Targeting: Users inactive 7+ days

METRICS TO TRACK
────────────────────────────────────────────────
- Day 30 retention (primary)
- Email open rate
- Click rate
- Re-engagement rate (logged in after email)
═══════════════════════════════════════════════════
```

### Experiment: In-App Notifications

```
EXPERIMENT: Achievement Notifications
═══════════════════════════════════════════════════

HYPOTHESIS
────────────────────────────────────────────────
If we add achievement notifications for milestones,
then weekly retention will increase by 10% because
users feel progress and accomplishment.

DETAILS
────────────────────────────────────────────────
Area: Retention
Metric: Week 4 retention rate
Baseline: 50%
Goal: 55%
Duration: 4 weeks
Sample: 1,000 active users per variant

IMPLEMENTATION
────────────────────────────────────────────────
Control: No achievement notifications
Variant: Notifications for:
  - First project completed
  - 10 tasks completed
  - First team collaboration
  - 7-day streak
  - Power user milestone

Traffic: 50/50
Targeting: All active users
═══════════════════════════════════════════════════
```

---

## 5. Referral Experiments

### Experiment: Referral Program Launch

```
EXPERIMENT: Two-Sided Referral Incentive
═══════════════════════════════════════════════════

HYPOTHESIS
────────────────────────────────────────────────
If we launch a referral program giving both parties
1 month free, then referred signups will increase by
50% because users have financial incentive to share.

DETAILS
────────────────────────────────────────────────
Area: Referral
Metric: Referral signup rate
Baseline: 5% of signups from referral
Goal: 7.5% of signups from referral
Duration: 8 weeks
Sample: Full user base

IMPLEMENTATION
────────────────────────────────────────────────
Control: No referral program
Variant: 
  - Referrer gets 1 month free
  - Referred gets 1 month free
  - Promotion in settings, email, in-app

Traffic: Staged rollout (25% → 50% → 100%)
Targeting: All paying customers

METRICS TO TRACK
────────────────────────────────────────────────
- Referral rate (primary)
- Shares per user
- Referral conversion rate
- LTV of referred users
- Program cost (free months given)
═══════════════════════════════════════════════════
```

### Experiment: Share Flow Optimization

```
EXPERIMENT: One-Click Share Options
═══════════════════════════════════════════════════

HYPOTHESIS
────────────────────────────────────────────────
If we add one-click social share buttons to the 
referral page, then share rate will increase by 35%
because friction to share will be reduced.

DETAILS
────────────────────────────────────────────────
Area: Referral
Metric: Shares per referral page visit
Baseline: 15%
Goal: 20%
Duration: 4 weeks
Sample: 2,000 referral page visitors per variant

IMPLEMENTATION
────────────────────────────────────────────────
Control: Copy link only
Variant: 
  - Copy link (default)
  - Share to Twitter (pre-filled)
  - Share to LinkedIn (pre-filled)
  - Share via Email (pre-filled)
  - Share via Slack (if connected)

Traffic: 50/50
Targeting: Referral page visitors
═══════════════════════════════════════════════════
```

---

## 6. Revenue Experiments

### Experiment: Pricing Page Optimization

```
EXPERIMENT: Plan Comparison Layout
═══════════════════════════════════════════════════

HYPOTHESIS
────────────────────────────────────────────────
If we highlight the middle tier as "Most Popular"
then middle tier selection will increase by 20%
because anchoring guides decision-making.

DETAILS
────────────────────────────────────────────────
Area: Revenue
Metric: Middle tier conversion rate
Baseline: 45% select middle
Goal: 54% select middle
Duration: 4 weeks
Sample: 3,000 pricing page visitors per variant

IMPLEMENTATION
────────────────────────────────────────────────
Control: Equal presentation of all tiers
Variant: Middle tier:
  - "Most Popular" badge
  - Slightly larger card
  - Different border color
  - Recommended checkmark

Traffic: 50/50
Targeting: All pricing page visitors
═══════════════════════════════════════════════════
```

### Experiment: Upgrade Prompt Timing

```
EXPERIMENT: Usage-Based Upgrade Prompts
═══════════════════════════════════════════════════

HYPOTHESIS
────────────────────────────────────────────────
If we show upgrade prompts at 80% usage limit
instead of 100%, then upgrade rate will increase
by 25% because users have time to decide.

DETAILS
────────────────────────────────────────────────
Area: Revenue
Metric: Free-to-paid conversion rate
Baseline: 5%
Goal: 6.25%
Duration: 6 weeks
Sample: 1,500 free users approaching limit per variant

IMPLEMENTATION
────────────────────────────────────────────────
Control: Prompt at 100% limit (hard stop)
Variant: 
  - Soft prompt at 80% (dismissible)
  - Reminder at 95% (more urgent)
  - Prompt at 100% (with trial offer)

Traffic: 50/50
Targeting: Free users at 75%+ usage
═══════════════════════════════════════════════════
```

### Experiment: Annual Plan Discount

```
EXPERIMENT: Annual Plan Discount Level
═══════════════════════════════════════════════════

HYPOTHESIS
────────────────────────────────────────────────
If we increase annual discount from 20% to 33%
(2 months free), then annual plan selection will
increase by 40% because the savings are clearer.

DETAILS
────────────────────────────────────────────────
Area: Revenue
Metric: % choosing annual vs monthly
Baseline: 30% annual
Goal: 42% annual
Duration: 8 weeks
Sample: 500 new paying customers per variant

IMPLEMENTATION
────────────────────────────────────────────────
Control: 20% off annual (Save 20%)
Variant: 33% off annual (Get 2 months free!)

Traffic: 50/50
Targeting: All new paying customers

ANALYSIS NOTES
────────────────────────────────────────────────
Consider:
- Short-term revenue impact
- Long-term retention of annual vs monthly
- Cash flow implications
═══════════════════════════════════════════════════
```

---

## 7. Experiment Prioritization

### ICE Scoring Template

```
EXPERIMENT BACKLOG - ICE PRIORITIZATION
═══════════════════════════════════════════════════

ID   Experiment               Impact  Confidence  Ease   ICE
────────────────────────────────────────────────────────────
E01  Homepage headline         8       7          9      8.0
E02  Onboarding checklist      9       8          6      7.7
E03  Referral program          7       6          5      6.0
E04  Annual discount           6       8          9      7.7
E05  Welcome email sequence    7       7          8      7.3
E06  Achievement notifs        5       5          7      5.7
E07  Interactive tour          8       6          4      6.0
E08  Pricing highlight         6       7          9      7.3
E09  Usage-based prompts       7       6          7      6.7
E10  Share flow optimize       5       7          8      6.7

PRIORITIZED ORDER:
1. E01 - Homepage headline (ICE: 8.0)
2. E02 - Onboarding checklist (ICE: 7.7)
3. E04 - Annual discount (ICE: 7.7)
4. E05 - Welcome emails (ICE: 7.3)
5. E08 - Pricing highlight (ICE: 7.3)
═══════════════════════════════════════════════════
```

### Weekly Experiment Review

```
WEEKLY EXPERIMENT REVIEW - Week 42
═══════════════════════════════════════════════════

RUNNING EXPERIMENTS
────────────────────────────────────────────────
E01 - Homepage headline
  Status: Day 8 of 14
  Sample: 6,200 / 10,000 target
  Early signal: Variant A +12% (not significant yet)

E05 - Welcome email sequence
  Status: Day 5 of 28
  Sample: 450 / 2,000 target
  Early signal: Too early

COMPLETED THIS WEEK
────────────────────────────────────────────────
E08 - Pricing highlight
  Result: WINNER - Variant
  Lift: +18% middle tier selection
  Confidence: 95%
  Action: Shipped to 100%
  
NEXT UP
────────────────────────────────────────────────
E02 - Onboarding checklist (starting Monday)
E04 - Annual discount (starting Wednesday)
═══════════════════════════════════════════════════
```

---

## Summary: Experiment Framework

### Running Effective Experiments

1. **Hypothesize**: Clear "if/then/because"
2. **Prioritize**: ICE score all ideas
3. **Design**: One variable, clear metrics
4. **Calculate**: Sample size for significance
5. **Run**: Don't peek, wait for full data
6. **Analyze**: Statistical significance check
7. **Decide**: Ship, iterate, or kill
8. **Document**: Record all learnings

### Experiment Velocity Targets

| Stage | Experiments/Month |
|-------|-------------------|
| Early | 4-6 |
| Growth | 8-12 |
| Scale | 15-20 |

---

*End of Growth Experiments Templates*
