# SaaS Analytics and Reporting

## Introduction

Data-driven decision making is essential for SaaS success. This comprehensive guide covers the analytics infrastructure, metrics tracking, reporting cadences, and dashboards needed to run a successful SaaS business. From product analytics to financial reporting, you'll learn how to build a complete analytics system.

---

## 1. Analytics Infrastructure

### The SaaS Analytics Stack

```
┌─────────────────────────────────────────────────────────┐
│                   DATA COLLECTION                       │
├─────────────────────────────────────────────────────────┤
│ Product      │ Marketing   │ Sales     │ Finance       │
│ Analytics    │ Analytics   │ CRM       │ Billing       │
│ (Amplitude,  │ (GA, Ads)   │(Salesforce│ (Stripe,      │
│  Mixpanel)   │             │ HubSpot)  │  Chargebee)   │
└──────┬───────┴──────┬──────┴─────┬─────┴───────┬───────┘
       │              │            │             │
       ▼              ▼            ▼             ▼
┌─────────────────────────────────────────────────────────┐
│                   DATA WAREHOUSE                        │
│              (Snowflake, BigQuery, Redshift)           │
└─────────────────────────┬───────────────────────────────┘
                          │
                          ▼
┌─────────────────────────────────────────────────────────┐
│                 TRANSFORMATION LAYER                    │
│                       (dbt)                             │
└─────────────────────────┬───────────────────────────────┘
                          │
                          ▼
┌─────────────────────────────────────────────────────────┐
│                   BI & REPORTING                        │
│           (Looker, Metabase, Tableau, Mode)            │
└─────────────────────────────────────────────────────────┘
```

### Data Sources

| Source | Data Type | Tools |
|--------|-----------|-------|
| Product | Events, features, usage | Segment, Amplitude, Mixpanel |
| Marketing | Traffic, campaigns, attribution | GA4, UTM, ad platforms |
| Sales | Pipeline, deals, activities | Salesforce, HubSpot |
| Support | Tickets, satisfaction, time | Zendesk, Intercom |
| Finance | Revenue, billing, churn | Stripe, Chargebee, ChartMogul |
| Customer Success | Health, NPS, engagement | Gainsight, ChurnZero |

### Event Tracking Architecture

**Standard Event Structure:**
```json
{
  "event": "feature_used",
  "userId": "user_123",
  "accountId": "account_456",
  "timestamp": "2024-10-15T14:30:00Z",
  "properties": {
    "feature_name": "report_created",
    "feature_category": "analytics",
    "plan_type": "professional",
    "session_id": "sess_789"
  },
  "context": {
    "page_url": "/reports/new",
    "device_type": "desktop",
    "browser": "chrome"
  }
}
```

**Essential Events to Track:**

| Event | When | Why |
|-------|------|-----|
| signed_up | Account created | Funnel start |
| activation_completed | Activation milestone | Activation rate |
| feature_used | Any feature usage | Adoption tracking |
| upgrade_started | Started upgrade flow | Conversion funnel |
| upgraded | Paid conversion | Revenue |
| invited_user | Sent invite | Virality |
| support_ticket_created | Ticket opened | Health |

---

## 2. Key SaaS Metrics

### Financial Metrics

**Monthly Recurring Revenue (MRR):**
```
MRR = Sum of all monthly subscription revenue

Components:
- New MRR: First-time customers
- Expansion MRR: Upgrades, add-ons
- Contraction MRR: Downgrades
- Churn MRR: Cancellations

Net New MRR = New + Expansion - Contraction - Churn
```

**Annual Recurring Revenue (ARR):**
```
ARR = MRR × 12

Note: Only for businesses with annual contracts
or as a projection metric
```

**Average Revenue Per User (ARPU):**
```
ARPU = MRR / Active Customers

Also useful:
- ARPU by segment
- ARPU trend over time
- ARPU by cohort
```

### Customer Metrics

**Customer Acquisition Cost (CAC):**
```
CAC = (Sales + Marketing Spend) / New Customers

Segment by:
- Channel CAC
- Segment CAC
- Blended CAC
```

**Lifetime Value (LTV):**
```
Simple: LTV = ARPU × Avg Customer Lifetime

More accurate:
LTV = ARPU × Gross Margin % / Monthly Churn Rate
```

**LTV:CAC Ratio:**
```
LTV:CAC = LTV / CAC

Benchmarks:
<1 = Losing money
1-3 = Improving
3-5 = Healthy
>5 = Underinvesting in growth
```

### Retention Metrics

**Logo Churn:**
```
Logo Churn Rate = Customers Lost / Starting Customers × 100

Monthly benchmark:
SMB: 3-5%
Mid-market: 1-2%
Enterprise: <1%
```

**Revenue Churn:**
```
Gross Revenue Churn = Churned MRR / Starting MRR × 100

Net Revenue Churn = (Churned - Expansion) / Starting MRR × 100
```

**Net Revenue Retention (NRR):**
```
NRR = (Starting MRR - Churn + Expansion) / Starting MRR × 100

Benchmarks:
<90% = Problem
90-100% = Okay
100-120% = Good
>120% = Excellent
```

---

## 3. Reporting Cadences

### Daily Metrics

**What to Track:**
- Signups
- Activations
- Revenue
- Major alerts

**Daily Dashboard:**
```
DAILY PULSE - October 15, 2024
═══════════════════════════════════════

TODAY vs YESTERDAY vs AVG
────────────────────────────────────────
Signups:        125 vs 118 vs 105 (+19%)
Activations:    65 vs 62 vs 55 (+18%)
Trials Started: 48 vs 44 vs 40 (+20%)
Revenue:        $4,200 vs $3,800 vs $3,500

ALERTS
────────────────────────────────────────
⚠️ Signup rate below target (need 150)
✓ Activation rate strong
✓ Trial starts tracking
═══════════════════════════════════════
```

### Weekly Metrics

**What to Track:**
- Funnel metrics
- Pipeline changes
- Team activities
- Trend analysis

**Weekly Report:**
```
WEEKLY REPORT - Week 42, 2024
═══════════════════════════════════════

ACQUISITION
────────────────────────────────────────
Website Visitors:    25,000 (+8% WoW)
Signups:            625 (+12% WoW)
Trial Starts:       225 (+5% WoW)

CONVERSION
────────────────────────────────────────
Visitor→Signup:     2.5% (+0.2%)
Signup→Trial:       36% (-2%)
Trial→Paid:         22% (+1%)

REVENUE
────────────────────────────────────────
New MRR:            $18,500
Expansion MRR:      $5,200
Churn MRR:          ($4,800)
Net New MRR:        $18,900

PIPELINE
────────────────────────────────────────
Added:              $180K
Closed Won:         $85K
Closed Lost:        $45K
Net:                +$50K
═══════════════════════════════════════
```

### Monthly Metrics

**What to Track:**
- Full financial picture
- Cohort analysis
- Strategic metrics
- Board-level data

**Monthly Report:**
```
MONTHLY REPORT - October 2024
═══════════════════════════════════════════════════

REVENUE
────────────────────────────────────────────────
MRR:                $850,000 (+4.5% MoM)
ARR:                $10.2M
New MRR:            $75,000
Expansion MRR:      $22,000
Contraction MRR:    ($8,000)
Churn MRR:          ($25,000)
Net New MRR:        $64,000

CUSTOMERS
────────────────────────────────────────────────
Total Customers:    2,500 (+80 net)
New Customers:      120
Churned:            40
Logo Churn:         1.6%
Net Revenue Retention: 105%

ACQUISITION
────────────────────────────────────────────────
Total Signups:      2,500
Activated:          1,250 (50%)
Converted:          120 (4.8% of signup)
CAC:                $800
LTV:CAC:            4.2

ENGAGEMENT
────────────────────────────────────────────────
MAU:                5,000
DAU/MAU:            32%
Feature Adoption:   65% using core features
NPS:                45 (+3 from Sept)

EFFICIENCY
────────────────────────────────────────────────
Burn Multiple:      1.2
Rule of 40:         42% (profitable + growth)
Revenue per FTE:    $180K ARR
═══════════════════════════════════════════════════
```

### Quarterly Business Review

**What to Track:**
- Strategic progress
- Annual plan status
- Competitive position
- Resource allocation

---

## 4. Dashboard Design

### Executive Dashboard

**Purpose:** High-level business health for leadership

**Metrics:**
- ARR and growth rate
- Net new MRR
- Logo and revenue churn
- LTV:CAC
- Cash runway

```
┌─────────────────────────────────────────────────────────┐
│ EXECUTIVE DASHBOARD                     October 2024   │
├─────────────────────────────────────────────────────────┤
│                                                         │
│  ARR              Growth           Churn               │
│  $10.2M           +54% YoY        2.5% monthly         │
│  ████████████     ▲▲▲▲▲▲▲▲▲       Target: <3% ✓       │
│                                                         │
│  ─────────────────────────────────────────────────     │
│                                                         │
│  Net New MRR      LTV:CAC         Cash Runway          │
│  $64K             4.2:1           18 months            │
│  vs $55K target   Target: >3 ✓    $2.1M balance        │
│                                                         │
│  ─────────────────────────────────────────────────     │
│                                                         │
│  [MRR Trend Chart]                [ARR Bridge Chart]   │
│                                                         │
└─────────────────────────────────────────────────────────┘
```

### Marketing Dashboard

**Purpose:** Marketing performance and attribution

**Metrics:**
- Traffic by source
- Lead generation
- CAC by channel
- Pipeline contribution

### Sales Dashboard

**Purpose:** Pipeline and revenue performance

**Metrics:**
- Pipeline value
- Win rate
- Sales cycle
- Quota attainment
- Activity metrics

### Product Dashboard

**Purpose:** Product usage and adoption

**Metrics:**
- MAU/DAU
- Feature adoption
- Activation rate
- Retention curves

### Customer Success Dashboard

**Purpose:** Customer health and retention

**Metrics:**
- Health score distribution
- NPS trends
- Churn risk
- Expansion pipeline

---

## 5. Cohort Analysis

### What is Cohort Analysis?

**Definition:** Analyzing groups of users who share a common characteristic over time.

**Types:**
- Acquisition cohorts (signup month)
- Behavioral cohorts (feature usage)
- Revenue cohorts (starting ARR)

### Retention Cohort

**Format:**
```
         Month 0  Month 1  Month 2  Month 3  Month 4
Jan '24    100%     85%      78%      72%      68%
Feb '24    100%     87%      80%      74%      70%
Mar '24    100%     88%      82%      76%      -
Apr '24    100%     90%      84%      -        -
May '24    100%     91%      -        -        -
```

**What to Look For:**
- Retention curve shape
- Cohort-over-cohort improvement
- Inflection points
- Segment differences

### Revenue Cohort

**Format:**
```
         Month 0  Month 3  Month 6  Month 9  Month 12
Jan '24   $100K    $98K     $102K    $108K    $115K
Feb '24   $120K    $118K    $125K    $132K    -
Mar '24   $110K    $108K    $116K    -        -
```

**NRR by Cohort:**
- Month 12 / Month 0 = Cohort NRR
- Example: $115K / $100K = 115%

### LTV Cohort

**Format:**
```
Cohort    Month 0  Cumulative LTV at Month 12
Jan '24   $500     $5,200
Feb '24   $480     $5,100
Mar '24   $520     $5,400
Apr '24   $550     $5,800
```

---

## 6. Segmentation

### Why Segment?

**Aggregates can be misleading:**
```
Overall churn: 3%

But segmented:
- SMB churn: 5%
- Mid-market churn: 2%
- Enterprise churn: 0.5%

Different problems, different solutions.
```

### Common Segments

| Segment Type | Options |
|--------------|---------|
| Company Size | SMB, Mid-market, Enterprise |
| Plan | Free, Pro, Enterprise |
| Industry | Tech, Finance, Healthcare |
| Geography | NA, EMEA, APAC |
| Acquisition | Organic, Paid, Referral |
| Behavior | Power users, Casual, At-risk |

### Segment Analysis

**Template:**
```
SEGMENT ANALYSIS - October 2024
═══════════════════════════════════════════════════

BY COMPANY SIZE
────────────────────────────────────────────────
            Customers  ARR       ARPU    Churn   NRR
SMB         1,800      $4.5M    $208    4.2%    92%
Mid-Market  550        $4.2M    $636    1.8%    108%
Enterprise  150        $1.5M    $833    0.8%    125%

INSIGHTS:
- SMB is volume, not value
- Mid-market is the sweet spot
- Enterprise has best retention

BY ACQUISITION
────────────────────────────────────────────────
            Customers  CAC      LTV     LTV:CAC
Organic     1,000      $200     $3,200  16:1
Paid        800        $600     $2,800  4.7:1
Referral    500        $150     $3,500  23:1
Outbound    200        $1,500   $5,000  3.3:1

INSIGHTS:
- Referral best unit economics
- Outbound gets bigger customers
- Organic needs more investment
═══════════════════════════════════════════════════
```

---

## 7. Attribution Modeling

### Attribution Types

**First Touch:**
- Credit to first interaction
- Good for: Awareness channels
- Bad for: Ignores nurturing

**Last Touch:**
- Credit to last interaction before conversion
- Good for: Closing channels
- Bad for: Ignores discovery

**Linear:**
- Equal credit to all touches
- Good for: Simple fairness
- Bad for: Not all touches equal

**Time Decay:**
- More credit to recent touches
- Good for: Values recency
- Bad for: Undervalues discovery

**Position Based (U-Shaped):**
- 40% first, 40% last, 20% middle
- Good for: Balances discovery and closing
- Bad for: Arbitrary weights

### Multi-Touch Attribution

**Example Customer Journey:**
```
1. Google Ad (Paid)         → Landed on blog
2. Blog post (Organic)      → Downloaded ebook
3. Email nurture (Email)    → Clicked to pricing
4. Retargeting (Paid)       → Signed up for trial
5. Demo (Sales)             → Converted to paid

Attribution Models:
First Touch:     100% to Google Ad
Last Touch:      100% to Demo
Linear:          20% each
Position Based:  40% Google, 40% Demo, 6.67% each middle
```

---

## 8. Analytics Implementation

### Implementation Checklist

- [ ] Event tracking implemented
- [ ] Data warehouse set up
- [ ] Data pipelines running
- [ ] Metrics defined
- [ ] Dashboards built
- [ ] Reporting cadence established
- [ ] Team trained on tools
- [ ] Data quality monitoring

### Common Mistakes

**1. Vanity Metrics Focus**
- Tracking what looks good, not what matters
- Fix: Focus on actionable metrics

**2. No Segmentation**
- Treating all customers the same
- Fix: Always segment analysis

**3. Ignoring Data Quality**
- Garbage in, garbage out
- Fix: Monitor and validate data

**4. Dashboard Overload**
- Too many dashboards, no focus
- Fix: Fewer, better dashboards

**5. No Action from Insights**
- Analytics without action is waste
- Fix: Tie metrics to decisions

---

## Summary: Analytics Framework

### Essential SaaS Analytics

1. **Infrastructure**: Collection → Warehouse → BI
2. **Metrics**: Financial, customer, retention, efficiency
3. **Cadences**: Daily, weekly, monthly, quarterly
4. **Dashboards**: By function and audience
5. **Analysis**: Cohorts, segments, attribution

### Analytics Checklist

- [ ] Core metrics defined
- [ ] Tracking implemented
- [ ] Data warehouse ready
- [ ] Dashboards built
- [ ] Reporting cadence set
- [ ] Team using data
- [ ] Regular reviews scheduled

---

*End of SaaS Analytics Section*
