# PLG Metrics Deep Dive

## Introduction

Product-Led Growth requires a different set of metrics than traditional sales-led businesses. While sales-led companies focus on pipeline and deal metrics, PLG companies track product usage, activation, and self-serve conversion. This comprehensive guide covers the essential PLG metrics, how to calculate them, benchmarks, and how to use them for decision-making.

---

## 1. The PLG Metrics Framework

### PLG Metric Categories

**Acquisition Metrics:**
- Signups
- Visitor-to-signup rate
- Signup sources
- Signup quality

**Activation Metrics:**
- Activation rate
- Time to activation
- Activation by cohort
- Activation by source

**Engagement Metrics:**
- Daily/Weekly/Monthly Active Users
- Feature adoption
- Usage depth
- Session metrics

**Conversion Metrics:**
- Free-to-paid rate
- Trial conversion rate
- Time to conversion
- PQL conversion

**Retention Metrics:**
- Day 1/7/30 retention
- Weekly retention
- Logo retention
- Revenue retention

**Expansion Metrics:**
- Seat expansion rate
- Tier upgrade rate
- Usage expansion
- Viral coefficient

### The PLG Funnel

```
VISITORS
    │ Visitor-to-Signup Rate
    ▼
SIGNUPS
    │ Signup-to-Activation Rate
    ▼
ACTIVATED USERS
    │ Activation-to-Engaged Rate
    ▼
ENGAGED USERS (WAU)
    │ PQL Rate
    ▼
PRODUCT QUALIFIED LEADS (PQLs)
    │ PQL-to-Paid Rate
    ▼
PAYING CUSTOMERS
    │ Retention & Expansion
    ▼
RETAINED & EXPANDED CUSTOMERS
```

---

## 2. Acquisition Metrics

### Signups

**Definition:** Total new accounts created

**Calculation:**
```
Signups = Count of new accounts created in period
```

**Segment By:**
- Source (organic, paid, referral)
- Plan (free, trial, direct paid)
- Type (individual, team, enterprise)

### Visitor-to-Signup Rate

**Definition:** Percentage of website visitors who sign up

**Calculation:**
```
Visitor-to-Signup Rate = Signups / Unique Visitors × 100

Example:
2,500 signups / 100,000 visitors = 2.5%
```

**Benchmarks:**

| Site Type | Poor | Average | Good | Great |
|-----------|------|---------|------|-------|
| Homepage | <1% | 1-2% | 2-4% | >4% |
| Landing Page | <3% | 3-6% | 6-10% | >10% |
| Pricing Page | <5% | 5-10% | 10-15% | >15% |

### Signup Quality

**Measure signup quality by:**
- Company domain (business vs. personal email)
- Company size (from clearbit/enrichment)
- Role (from signup questions)
- Activation likelihood (predictive)

**Quality Score:**
```
Signup Quality Score = Σ (Quality Factor × Weight)

Factors:
- Business email: +30
- Company size match: +20
- Target role: +25
- Target industry: +15
- Referral source: +10
```

---

## 3. Activation Metrics

### Activation Rate

**Definition:** Percentage of signups who complete the activation milestone

**Calculation:**
```
Activation Rate = Activated Users / Total Signups × 100

Example:
1,250 activated / 2,500 signups = 50%
```

**Benchmarks:**

| Product Type | Poor | Average | Good | Great |
|--------------|------|---------|------|-------|
| Simple Tool | <30% | 30-50% | 50-70% | >70% |
| Medium Complexity | <20% | 20-40% | 40-60% | >60% |
| Complex Platform | <15% | 15-30% | 30-45% | >45% |

### Time to Activation

**Definition:** How long from signup until activation

**Calculation:**
```
Time to Activation = Median(Activation Time - Signup Time)

Measure in minutes, hours, or days depending on product
```

**Benchmarks:**

| Product Type | Target |
|--------------|--------|
| Consumer App | <5 minutes |
| Simple B2B Tool | <1 hour |
| Medium B2B | <24 hours |
| Complex B2B | <7 days |

### Activation by Cohort

**Track activation rate by signup cohort:**

| Signup Month | D7 Activated | D14 Activated | D30 Activated |
|--------------|--------------|---------------|---------------|
| Jan | 35% | 42% | 48% |
| Feb | 38% | 45% | 50% |
| Mar | 42% | 50% | 55% |
| Apr | 45% | 52% | 57% |

Improving cohorts indicate onboarding improvements working.

---

## 4. Engagement Metrics

### Daily/Weekly/Monthly Active Users

**Definitions:**
- **DAU**: Unique users active in last 24 hours
- **WAU**: Unique users active in last 7 days
- **MAU**: Unique users active in last 30 days

**Define "Active":**
- Logged in (weak)
- Performed core action (better)
- Completed value-generating action (best)

### DAU/WAU/MAU Ratios

**Stickiness Metrics:**
```
DAU/MAU = Daily engagement intensity
WAU/MAU = Weekly engagement intensity

Examples:
Social app: 60% DAU/MAU (very sticky)
B2B tool: 25% DAU/MAU (weekly use)
Monthly tool: 10% DAU/MAU (monthly use)
```

**Benchmarks:**

| Product Type | DAU/WAU | WAU/MAU |
|--------------|---------|---------|
| Consumer social | 70%+ | 85%+ |
| Consumer app | 40-60% | 60-80% |
| B2B daily use | 50-70% | 70-85% |
| B2B weekly use | 25-40% | 50-70% |
| B2B monthly use | 10-25% | 30-50% |

### Feature Adoption

**Track which features users adopt:**

| Feature | Users Using | % of Active | Trend |
|---------|-------------|-------------|-------|
| Core Feature A | 8,500 | 85% | → |
| Core Feature B | 7,200 | 72% | ↑ |
| Feature C | 3,500 | 35% | → |
| Feature D | 2,000 | 20% | ↓ |

**Feature Adoption Rate:**
```
Feature Adoption = Users who used feature / Total active users × 100
```

### Usage Depth

**Measure how deeply users engage:**

| Depth Metric | Calculation |
|--------------|-------------|
| Actions per session | Total actions / Sessions |
| Time per session | Total time / Sessions |
| Features per user | Unique features used / Users |
| Sessions per week | Total sessions / Active users / 4 |

---

## 5. Conversion Metrics

### Free-to-Paid Conversion Rate

**Definition:** Percentage of free users who become paying

**Calculation:**
```
Free-to-Paid Rate = Converted to Paid / Total Free Users × 100

Note: Use cohort-based calculation for accuracy
```

**Cohort-Based Calculation:**
```
Jan cohort: 1000 free signups
→ 50 converted by March (5%)
→ 75 converted by June (7.5%)
→ 90 converted by December (9%)
```

**Benchmarks:**

| Model | Poor | Average | Good | Great |
|-------|------|---------|------|-------|
| Freemium | <2% | 2-4% | 4-7% | >7% |
| Free Trial | <10% | 10-20% | 20-30% | >30% |
| Free Trial (CC required) | <30% | 30-50% | 50-65% | >65% |

### Trial Conversion Rate

**Definition:** Percentage of trial users who convert to paid

**Calculation:**
```
Trial Conversion = Converted / Completed Trials × 100
```

**By Trial Length:**

| Trial Length | Typical Conversion |
|--------------|-------------------|
| 7-day | 15-25% |
| 14-day | 12-20% |
| 30-day | 10-18% |

### Time to Conversion

**Definition:** Days from signup to paid conversion

**Calculation:**
```
Time to Conversion = Median(Conversion Date - Signup Date)
```

**Distribution Analysis:**
```
Days to Convert | % of Conversions
0-7             | 35%
8-14            | 25%
15-30           | 20%
31-60           | 12%
61+             | 8%
```

### PQL Conversion

**PQL (Product Qualified Lead):** User meeting criteria indicating readiness to buy

**PQL Conversion Rate:**
```
PQL Conversion = PQLs Converted / Total PQLs × 100
```

**Typical PQL Conversion: 25-50%** (much higher than MQL)

---

## 6. Product Qualified Leads (PQLs)

### Defining PQLs

**PQL Criteria Examples:**

| Criteria Type | Example |
|---------------|---------|
| Usage threshold | >50 actions in 7 days |
| Feature adoption | Used 3+ features |
| Team activity | 3+ users active |
| Limit approaching | 80%+ of free limit |
| Time-based | Active 14+ days |
| Behavior | Viewed pricing page |

### PQL Scoring

**Build a PQL Score:**
```
PQL Score = Σ (Signal × Weight)

Signals:
- Daily active last 7 days: +5 per day (max 35)
- Team members: +10 per member (max 50)
- Core features used: +5 per feature (max 25)
- Pricing page viewed: +15
- Limit >80%: +20

PQL Threshold: Score > 75
```

### PQL Dashboard

```
PQL DASHBOARD - October 2024
═══════════════════════════════════════════════════

VOLUME
────────────────────────────────────────────────
Total PQLs:           150
New PQLs this week:   35
PQL Rate:             6% of active users

QUALITY
────────────────────────────────────────────────
Avg PQL Score:        82
High Score (>90):     45 (30%)
Medium (75-90):       75 (50%)
Threshold (75):       30 (20%)

CONVERSION
────────────────────────────────────────────────
PQLs Converted:       52
Conversion Rate:      35%
Avg Time to Convert:  8 days
Revenue from PQLs:    $52,000

TOP PQL SIGNALS
────────────────────────────────────────────────
1. Pricing page + 3 users    → 55% conversion
2. 7-day streak + features   → 45% conversion
3. Limit reached             → 40% conversion
4. Team growth               → 38% conversion
═══════════════════════════════════════════════════
```

---

## 7. Retention Metrics

### User Retention

**Day N Retention:**
```
Day N Retention = Users active on day N / Users who signed up × 100

Common intervals: Day 1, Day 7, Day 14, Day 30
```

**Retention Curve:**
```
100% │━━━
     │   ╲
 75% │    ╲
     │     ╲___
 50% │         ╲___
     │              ╲___________
 25% │                          ────────
     │
  0% └──────────────────────────────────────
      D1  D7  D14  D30  D60  D90  D180  D365
```

**Healthy Curve:** Flattens out (loyal users remain)
**Unhealthy Curve:** Keeps declining (no loyal base)

### Retention Benchmarks

| Product Type | D1 | D7 | D30 |
|--------------|-----|-----|-----|
| Consumer Social | 40%+ | 30%+ | 20%+ |
| Consumer App | 30%+ | 20%+ | 10%+ |
| B2B SaaS | 60%+ | 40%+ | 30%+ |
| Enterprise | 80%+ | 70%+ | 60%+ |

### Cohort Retention Analysis

**Retention Cohort Table:**

| Cohort | W1 | W2 | W3 | W4 | W8 | W12 |
|--------|-----|-----|-----|-----|-----|-----|
| Jan | 100% | 65% | 55% | 50% | 42% | 38% |
| Feb | 100% | 68% | 58% | 52% | 45% | 40% |
| Mar | 100% | 72% | 62% | 56% | 48% | - |
| Apr | 100% | 75% | 65% | 58% | - | - |

---

## 8. Viral & Expansion Metrics

### Viral Coefficient (K Factor)

**Definition:** How many new users each existing user brings

**Calculation:**
```
K = i × c

Where:
i = invites sent per user
c = conversion rate of invites

Example:
i = 4 invites per user
c = 15% conversion
K = 4 × 0.15 = 0.6
```

**Interpretation:**
- K < 1: Viral assists growth but doesn't drive it
- K = 1: Each user replaces themselves
- K > 1: Exponential growth (rare, usually temporary)

### Seat Expansion Rate

**Definition:** Rate at which existing accounts add seats

**Calculation:**
```
Seat Expansion Rate = (New Seats Added / Starting Seats) × 100

Monthly example:
Starting seats: 1,000
New seats added: 50
Rate: 5% monthly
```

### Net Seat Retention

**Definition:** Like NRR but for seats instead of revenue

**Calculation:**
```
Net Seat Retention = 
(Starting Seats - Removed Seats + Added Seats) / Starting Seats × 100
```

---

## 9. PLG Dashboard

### Complete PLG Metrics Dashboard

```
PLG METRICS DASHBOARD - October 2024
═══════════════════════════════════════════════════

ACQUISITION
────────────────────────────────────────────────
Visitors:             100,000
Signups:              2,500 (2.5% visitor rate)
Signup Quality:       72% ICP match
WoW Change:           +8%

ACTIVATION
────────────────────────────────────────────────
Activated:            1,250 (50% of signups)
Time to Activation:   45 minutes median
Activation Trend:     ↑ +5% vs last month

ENGAGEMENT
────────────────────────────────────────────────
DAU:                  5,000
WAU:                  12,000
MAU:                  25,000
DAU/MAU:              20%
Stickiness Trend:     → Stable

CONVERSION
────────────────────────────────────────────────
PQLs:                 500 (4% of MAU)
PQL Conversion:       35%
Free-to-Paid:         7% (lifetime)
Trial Conversion:     22%
Time to Convert:      18 days median

RETENTION
────────────────────────────────────────────────
D7 Retention:         65%
D30 Retention:        45%
Monthly Logo Churn:   3%
Net Revenue Retention: 108%

EXPANSION
────────────────────────────────────────────────
Viral K Factor:       0.4
Seat Expansion:       5% monthly
Tier Upgrades:        8% of customers

REVENUE
────────────────────────────────────────────────
New MRR from PLG:     $25,000
Expansion MRR:        $8,000
PLG % of New Revenue: 65%
═══════════════════════════════════════════════════
```

---

## Summary: PLG Metrics Framework

### Key PLG Metrics

| Category | Primary Metric | Target |
|----------|---------------|--------|
| Acquisition | Signup Rate | >2% |
| Activation | Activation Rate | >40% |
| Engagement | DAU/MAU | Depends on type |
| Conversion | Free-to-Paid | >5% |
| Retention | D30 Retention | >30% |
| Expansion | Viral K | >0.3 |

### PLG Metrics Checklist

- [ ] Activation metric defined
- [ ] Engagement metrics tracked
- [ ] PQL criteria established
- [ ] Retention cohorts built
- [ ] Conversion funnel measured
- [ ] Viral metrics tracked
- [ ] Dashboard implemented
- [ ] Regular review cadence

### Optimization Priority

1. **Activation**: The biggest lever—optimize first
2. **Retention**: Retaining users matters more than acquiring
3. **Conversion**: Turn engaged users into revenue
4. **Acquisition**: Scale once funnel is working

---

*End of PLG Metrics Section*
