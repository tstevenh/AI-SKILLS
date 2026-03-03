# Customer Health Scores

## Introduction

Customer health scores are predictive metrics that help you identify at-risk customers before they churn and spot expansion opportunities. A well-designed health score system enables proactive customer success, efficient resource allocation, and data-driven retention strategies. This comprehensive guide covers how to build, implement, and operationalize customer health scores.

---

## 1. Understanding Health Scores

### What is a Customer Health Score?

**Definition:** A composite metric that indicates the likelihood a customer will renew, expand, or churn.

**Purpose:**
- Predict churn before it happens
- Identify expansion opportunities
- Prioritize CSM attention
- Trigger automated interventions
- Measure CS effectiveness

### Health Score vs. Other Metrics

| Metric | Focus | Timeframe | Action |
|--------|-------|-----------|--------|
| NPS | Sentiment | Point in time | Feedback |
| CSAT | Satisfaction | Transaction | Support quality |
| Health Score | Likelihood | Ongoing | Intervention |
| Engagement | Usage | Current | Product |

### Health Score Categories

```
┌─────────────────────────────────────────────────────────┐
│                  CUSTOMER HEALTH                        │
├─────────────────────────────────────────────────────────┤
│ HEALTHY (70-100)                                        │
│ ████████████████████████████████████████                │
│ Active, engaged, expanding, advocates                   │
│ Action: Identify expansion, get referrals              │
├─────────────────────────────────────────────────────────┤
│ NEUTRAL (40-69)                                         │
│ ████████████████████████                                │
│ Using product, not growing, no red flags               │
│ Action: Increase engagement, find champions            │
├─────────────────────────────────────────────────────────┤
│ AT RISK (0-39)                                          │
│ █████████████                                           │
│ Declining usage, support issues, no engagement         │
│ Action: Immediate intervention, save plan              │
└─────────────────────────────────────────────────────────┘
```

---

## 2. Building a Health Score

### Health Score Components

**1. Product Usage**
- Feature adoption
- Usage frequency
- Usage depth
- Active users

**2. Engagement**
- Login frequency
- Session duration
- Feature exploration
- Community participation

**3. Support**
- Ticket volume
- Ticket severity
- Resolution satisfaction
- Escalations

**4. Relationship**
- Executive sponsor
- Champion engagement
- CSM interactions
- QBR participation

**5. Commercial**
- Contract value
- Renewal date
- Payment history
- Expansion history

### Weighting Components

**Example Weight Distribution:**

| Component | Weight | Rationale |
|-----------|--------|-----------|
| Product Usage | 35% | Strongest churn predictor |
| Engagement | 25% | Leading indicator |
| Support | 15% | Risk indicator |
| Relationship | 15% | Qualitative balance |
| Commercial | 10% | Lag indicator |

### Component Scoring

**Product Usage Score (0-100):**
```
Usage Score = 
  (DAU/Total Users × 30) +
  (Features Used / Key Features × 35) +
  (Usage vs. Benchmark × 35)

Example:
DAU/Users: 60% → 18 points
Features: 5/7 → 25 points
Usage: 120% of benchmark → 42 points (capped at 35)
Total: 18 + 25 + 35 = 78
```

**Engagement Score (0-100):**
```
Engagement Score =
  (Sessions/Week vs. Healthy × 40) +
  (Time in Product vs. Healthy × 30) +
  (Feature Discovery × 30)

Example:
Sessions: 8/10 healthy → 32 points
Time: 5h/4h healthy → 40 points (capped at 30)
Discovery: Low → 10 points
Total: 32 + 30 + 10 = 72
```

**Support Score (0-100):**
```
Support Score = 
  100 - 
  (Tickets × 5) - 
  (Critical Tickets × 20) -
  (Unsatisfied Responses × 15)

Example:
3 tickets: -15
0 critical: -0
1 unsatisfied: -15
Total: 100 - 15 - 0 - 15 = 70
```

**Relationship Score (0-100):**
```
Relationship Score =
  (Has Champion × 25) +
  (Executive Sponsor × 25) +
  (QBR Attended × 20) +
  (CSM Sentiment × 30)

Example:
Champion: Yes → 25
Sponsor: No → 0
QBR: Yes → 20
CSM Sentiment: Good → 24
Total: 25 + 0 + 20 + 24 = 69
```

**Commercial Score (0-100):**
```
Commercial Score =
  (Payment On-Time × 30) +
  (Contract Growing × 35) +
  (Renewal Likelihood × 35)

Example:
Payment: Yes → 30
Growing: Flat → 17
Renewal: Likely → 28
Total: 30 + 17 + 28 = 75
```

### Calculating Overall Health

**Weighted Average:**
```
Health Score = 
  (Usage × 0.35) +
  (Engagement × 0.25) +
  (Support × 0.15) +
  (Relationship × 0.15) +
  (Commercial × 0.10)

Example:
(78 × 0.35) + (72 × 0.25) + (70 × 0.15) + (69 × 0.15) + (75 × 0.10)
= 27.3 + 18 + 10.5 + 10.35 + 7.5
= 73.65 → Healthy
```

---

## 3. Health Score Models

### Simple Model (Starter)

**For early-stage or limited data:**

| Metric | Healthy | Neutral | At Risk |
|--------|---------|---------|---------|
| WAU/Total | >50% | 25-50% | <25% |
| Key Feature Used | Yes | Sometimes | No |
| Recent Support Issue | No | Resolved | Open |

**Score:**
- All Healthy = 85
- Mixed = 50
- All At Risk = 20

### Standard Model

**Balanced approach:**

```
Health Score = 
  Usage Score (40%) +
  Engagement Score (30%) +
  Sentiment Score (30%)

Where:
Usage = (DAU Rate × 50) + (Feature Adoption × 50)
Engagement = (Login Frequency × 50) + (Actions × 50)
Sentiment = (NPS × 50) + (Support Score × 50)
```

### Advanced Model (ML-Based)

**Predictive model using machine learning:**

**Inputs:**
- All usage metrics
- All engagement metrics
- Support ticket data
- NPS/CSAT scores
- Commercial data
- Demographic data

**Output:**
- Churn probability (0-100%)
- Health score = 100 - Churn probability

**Benefits:**
- More accurate
- Identifies non-obvious patterns
- Continuously improves

**Challenges:**
- Requires data science
- Needs training data
- Black box concerns

---

## 4. Implementing Health Scores

### Data Requirements

**Data Sources:**

| Data Type | Source | Freshness |
|-----------|--------|-----------|
| Product Usage | Analytics (Amplitude, Mixpanel) | Daily |
| Logins/Sessions | Auth system | Daily |
| Support Tickets | Helpdesk (Zendesk, Intercom) | Daily |
| NPS/CSAT | Survey tool | Monthly |
| Commercial | CRM/Billing | Weekly |
| CSM Notes | CS Platform | Ongoing |

### Technical Architecture

```
┌────────────────┐
│ Data Sources   │
├────────────────┤
│ Analytics      │──┐
│ Helpdesk       │──│
│ CRM            │──│
│ Billing        │──┼──▶ ┌────────────┐
│ Auth/Sessions  │──│    │ Data       │
│ Surveys        │──│    │ Warehouse  │
│ CS Platform    │──┘    └─────┬──────┘
                               │
                               ▼
                    ┌──────────────────┐
                    │ Health Score     │
                    │ Calculation      │
                    └────────┬─────────┘
                             │
              ┌──────────────┼──────────────┐
              ▼              ▼              ▼
        ┌─────────┐   ┌─────────┐   ┌─────────┐
        │ CS      │   │ Alert   │   │ Auto    │
        │ Platform│   │ System  │   │ Actions │
        └─────────┘   └─────────┘   └─────────┘
```

### Calculation Frequency

| Score Type | Frequency | Use Case |
|------------|-----------|----------|
| Overall Health | Daily | Dashboard, reporting |
| Risk Alerts | Real-time | Immediate intervention |
| Trend Analysis | Weekly | Strategic review |
| Predictive | Daily | Proactive outreach |

---

## 5. Operationalizing Health Scores

### Thresholds and Actions

**Healthy (70-100):**
```
Actions:
- Identify expansion opportunities
- Request referrals/testimonials
- Invite to community/advocacy
- Lighter touch engagement
- Celebrate milestones
```

**Neutral (40-69):**
```
Actions:
- Increase engagement touchpoints
- Identify and develop champions
- Feature education campaigns
- Usage goal setting
- Regular check-ins
```

**At Risk (0-39):**
```
Actions:
- Immediate CSM outreach
- Executive sponsor engagement
- Custom save plan
- Product/support escalation
- Renewal risk flagged
```

### Alert System

**Trigger Alerts When:**

| Trigger | Priority | Action |
|---------|----------|--------|
| Score drops >15 points | High | CSM immediate follow-up |
| Score enters At Risk | Critical | Save playbook triggered |
| Score enters Healthy | Info | Expansion review |
| Usage drops >50% | High | Engagement campaign |
| Support escalation | High | CS + Support sync |

### CSM Workflow Integration

**Daily CSM View:**
```
CSM HEALTH DASHBOARD - Sarah
═══════════════════════════════════════════════════

AT RISK (Action Required)
────────────────────────────────────────────────
Company A     Score: 28 ↓ (-15)   ARR: $50K
  Issue: Usage dropped 60%, no logins 7 days
  Next: Call today, exec escalation

Company B     Score: 35 ↓ (-8)    ARR: $25K
  Issue: 3 critical tickets, frustration
  Next: Support sync, check-in call

NEUTRAL (Monitor)
────────────────────────────────────────────────
Company C     Score: 52 → (stable) ARR: $30K
  Note: Steady usage, no champion identified
  Next: Schedule adoption review

HEALTHY (Expansion)
────────────────────────────────────────────────
Company D     Score: 85 ↑ (+5)    ARR: $40K
  Note: Growing usage, added 5 users
  Next: Expansion conversation, case study

SUMMARY
────────────────────────────────────────────────
Total Accounts: 45
At Risk: 4 (9%)
Neutral: 18 (40%)
Healthy: 23 (51%)
ARR At Risk: $125K
═══════════════════════════════════════════════════
```

---

## 6. Health Score Best Practices

### Dos

**1. Start Simple**
- Begin with 3-5 factors
- Add complexity over time
- Validate before expanding

**2. Include Leading Indicators**
- Usage trends (not just current)
- Engagement patterns
- Feature adoption velocity

**3. Calibrate Regularly**
- Compare scores to actual churn
- Adjust weights based on data
- Validate with CSM feedback

**4. Make It Actionable**
- Clear thresholds
- Defined playbooks
- Automated alerts

**5. Combine Quantitative + Qualitative**
- Data-driven scores
- CSM sentiment overlay
- Customer feedback input

### Don'ts

**1. Don't Over-Complicate**
- Too many factors = noise
- Unclear = unused
- Perfect enemy of good

**2. Don't Ignore Outliers**
- High usage ≠ always healthy
- Low usage ≠ always at risk
- Context matters

**3. Don't Set and Forget**
- Models decay
- Business changes
- Regular review needed

**4. Don't Hide from Customers**
- Share what drives health
- Make it a partnership
- Transparency builds trust

---

## 7. Measuring Health Score Effectiveness

### Validation Metrics

**Churn Prediction Accuracy:**
```
For customers who churned:
% that were At Risk: 70%+
% that were Neutral: 20-25%
% that were Healthy: <10%
```

**Intervention Success:**
```
At Risk accounts saved: Target 30-50%
Save rate by intervention type:
- CSM outreach: 35%
- Exec engagement: 50%
- Custom plan: 45%
```

### Continuous Improvement

**Monthly Review:**
- Score distribution changes
- Churn by health segment
- False positives/negatives
- Weight adjustments

**Quarterly Review:**
- Model performance
- Factor effectiveness
- New data sources
- Benchmark updates

---

## 8. Health Score Dashboard

### Executive Dashboard

```
CUSTOMER HEALTH OVERVIEW - October 2024
═══════════════════════════════════════════════════

PORTFOLIO HEALTH
────────────────────────────────────────────────
Average Score:         67 (+2 from Sept)
Score Distribution:
  Healthy:    45% ($2.5M ARR)
  Neutral:    40% ($2.0M ARR)
  At Risk:    15% ($750K ARR)

TRENDS
────────────────────────────────────────────────
Improving:            35 accounts (+$400K ARR)
Stable:               100 accounts ($2.8M ARR)
Declining:            25 accounts (-$300K ARR)

INTERVENTIONS
────────────────────────────────────────────────
Save Playbooks Active: 12
Saved This Month:      4 ($180K ARR)
Churned This Month:    3 ($95K ARR)
Save Rate:             57%

FORECAST IMPACT
────────────────────────────────────────────────
ARR At Risk (next 90 days):    $750K
Projected Save Rate:            50%
Projected Churn:                $375K
NRR Impact:                     -2.5%
═══════════════════════════════════════════════════
```

---

## Summary: Health Score Framework

### Building Health Scores

1. **Define components**: Usage, engagement, support, relationship, commercial
2. **Assign weights**: Based on churn correlation
3. **Set thresholds**: Healthy, neutral, at-risk
4. **Create playbooks**: Actions per segment
5. **Implement alerts**: Proactive triggers
6. **Measure effectiveness**: Validate and improve

### Health Score Checklist

- [ ] Components defined
- [ ] Weights assigned
- [ ] Data sources connected
- [ ] Calculation automated
- [ ] Thresholds set
- [ ] Playbooks created
- [ ] Alerts configured
- [ ] CSM workflow integrated
- [ ] Dashboard built
- [ ] Validation process established

---

*End of Customer Health Scores Section*
