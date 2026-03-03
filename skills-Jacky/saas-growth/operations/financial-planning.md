# SaaS Financial Planning

## Introduction

Financial planning in SaaS differs significantly from traditional businesses. Revenue is recognized over time, growth requires upfront investment, and the interaction between acquisition, retention, and expansion creates complex dynamics. This guide covers SaaS financial modeling, forecasting, budgeting, and board reporting.

---

## 1. SaaS Financial Model

### Core Model Components

**Revenue Model:**
```
Monthly MRR Projection
───────────────────────────────────────────────────
Starting MRR             [Input]
+ New MRR               [Calculated from signups]
+ Expansion MRR          [% of starting MRR]
- Contraction MRR        [% of starting MRR]
- Churned MRR            [% of starting MRR]
= Ending MRR             [Calculated]
───────────────────────────────────────────────────
```

**Customer Model:**
```
Monthly Customer Count
───────────────────────────────────────────────────
Starting customers       [Input]
+ New customers          [From acquisition model]
- Churned customers      [Churn rate × starting]
= Ending customers       [Calculated]
───────────────────────────────────────────────────
```

**Expense Model:**
```
Monthly Expenses
───────────────────────────────────────────────────
COGS                    [% of revenue or headcount]
Sales & Marketing       [Headcount + programs]
Research & Development  [Headcount]
General & Administrative [Headcount + overhead]
───────────────────────────────────────────────────
Total Expenses          [Sum]
───────────────────────────────────────────────────
```

### Building the Financial Model

**Step 1: Revenue Drivers**

| Driver | Source | Assumption |
|--------|--------|------------|
| Website traffic | Marketing | X visitors/month |
| Trial rate | Conversion | Y% of visitors |
| Trial conversion | Product | Z% of trials |
| New customers | Calculated | Traffic × Trial × Conv |
| ARPA | Pricing | $X/customer/month |
| New MRR | Calculated | New customers × ARPA |

**Step 2: Retention Drivers**

| Driver | Source | Assumption |
|--------|--------|------------|
| Monthly churn | Historical | X% of MRR |
| Expansion rate | Historical | Y% of MRR |
| Net retention | Calculated | 100% - Churn + Expansion |

**Step 3: Cost Drivers**

| Driver | Source | Assumption |
|--------|--------|------------|
| Headcount | Hiring plan | X employees |
| Avg salary | Market | $Y/employee |
| Non-payroll | Historical | Z% of payroll |
| Marketing spend | Budget | $X/month |
| Hosting | Usage | Y% of revenue |

### Model Structure

**Tab 1: Assumptions**
All inputs in one place:
- Growth rates
- Conversion rates
- Churn rates
- Headcount plan
- Pricing

**Tab 2: Revenue**
Monthly/quarterly MRR build:
- New MRR
- Expansion MRR
- Churn MRR
- Net new MRR

**Tab 3: Customers**
Customer count over time:
- New customers
- Churned customers
- Net customers

**Tab 4: Expenses**
Cost by category:
- People costs
- Marketing costs
- Hosting/infrastructure
- General overhead

**Tab 5: P&L**
Summary view:
- Revenue
- Gross margin
- Operating expenses
- Net income/loss

**Tab 6: Cash Flow**
Cash management:
- Starting cash
- Cash from operations
- Cash from financing
- Ending cash/runway

### Model Validation

**Sanity Checks:**
| Metric | Reasonable Range |
|--------|-----------------|
| Month-over-month growth | 5-15% (early stage) |
| Gross margin | 70-85% |
| S&M % of revenue | 30-60% |
| R&D % of revenue | 15-30% |
| G&A % of revenue | 10-20% |
| CAC payback | 6-18 months |
| LTV:CAC | 3:1 to 5:1 |

---

## 2. Forecasting

### Types of Forecasts

**Top-Down Forecast:**
- Start with target (e.g., $10M ARR)
- Work backward to required inputs
- Useful for goal-setting

```
Target: $10M ARR
Current: $5M ARR
Gap: $5M = 100% growth needed
Required: X new customers, Y expansion, Z retention
```

**Bottom-Up Forecast:**
- Start with inputs (traffic, conversion, etc.)
- Calculate resulting output
- More realistic, detail-oriented

```
Traffic: 100,000 visits
× Trial rate: 5% = 5,000 trials
× Conversion: 10% = 500 customers
× ARPA: $200 = $100,000 new MRR
```

**Driver-Based Forecast:**
- Identify key drivers
- Model each driver
- Calculate outcomes

```
Key Drivers:
1. Sales headcount → Demos → Closed deals
2. Marketing spend → Leads → Trials → Conversions
3. Success team → Retention → Expansion
```

### Forecasting Best Practices

**Use Ranges:**
```
Scenario Analysis:
            Bear    Base    Bull
Growth      40%     60%     80%
Churn       5%      4%      3%
Expansion   20%     30%     40%
12-mo ARR   $7.5M   $9M     $11M
```

**Update Regularly:**
- Weekly: Short-term forecast
- Monthly: 12-month rolling forecast
- Quarterly: Annual forecast refresh

**Track Accuracy:**
```
Forecast Accuracy Report
────────────────────────────────────
Metric          Forecast    Actual    Variance
New MRR         $50,000     $48,000   -4%
Churn MRR       $15,000     $17,000   +13%
Net New MRR     $35,000     $31,000   -11%
────────────────────────────────────

Analysis: Churn higher than expected.
Investigate: [Specific accounts/causes]
```

### Cohort-Based Forecasting

**Revenue by Cohort:**

| Cohort | M1 | M3 | M6 | M12 | M24 |
|--------|-----|-----|-----|-----|-----|
| Existing | $100K | $102K | $105K | $110K | $115K |
| Q1 New | $20K | $21K | $22K | $24K | - |
| Q2 New | - | $25K | $26K | $28K | - |
| Q3 New | - | - | $30K | $32K | - |
| Q4 New | - | - | - | $35K | - |
| **Total** | **$120K** | **$148K** | **$183K** | **$229K** | **$115K+** |

**Why This Works:**
- Each cohort behaves predictably
- New cohorts added each period
- Apply retention curve to each
- More accurate than aggregate

---

## 3. Budgeting

### SaaS Budget Categories

**Revenue Budget:**
- New MRR targets
- Expansion targets
- Churn targets
- Net new MRR

**Cost of Goods Sold (COGS):**
- Hosting/infrastructure
- Support team
- Customer success (sometimes)
- Payment processing

**Sales & Marketing:**
- Marketing team
- Marketing programs
- Sales team
- Sales tools

**Research & Development:**
- Engineering team
- Product team
- Design team
- Development tools

**General & Administrative:**
- Finance
- HR/People
- Legal
- Office/facilities
- Insurance

### Budget Allocation

**By Stage:**

| Stage | S&M | R&D | G&A |
|-------|-----|-----|-----|
| Seed | 30% | 50% | 20% |
| Series A | 40% | 40% | 20% |
| Series B | 50% | 35% | 15% |
| Growth | 45% | 35% | 20% |

**Marketing Budget Breakdown:**

| Channel | Allocation |
|---------|-----------|
| Paid acquisition | 40% |
| Content/SEO | 20% |
| Events | 15% |
| Brand | 10% |
| Tools/tech | 10% |
| Other | 5% |

### Budget Process

**Timeline:**
```
Month 1: Planning kickoff
- Finance provides templates
- Leaders identify priorities
- Initial asks submitted

Month 2: First draft
- Consolidate submissions
- Identify gaps/conflicts
- Executive review

Month 3: Finalization
- Negotiations/adjustments
- Final approval
- Communication
```

**Budget vs. Actual Tracking:**
```
Budget vs. Actual - October
═══════════════════════════════════════════════════
Category         Budget     Actual    Variance
───────────────────────────────────────────────────
Revenue          $500,000   $485,000  -3% ⚠️
COGS             $75,000    $78,000   +4%
Gross Profit     $425,000   $407,000  -4%
───────────────────────────────────────────────────
S&M              $200,000   $195,000  -3% ✓
R&D              $150,000   $155,000  +3%
G&A              $75,000    $72,000   -4% ✓
───────────────────────────────────────────────────
Operating Exp    $425,000   $422,000  -1%
Net Income       $0         -$15,000  ⚠️
═══════════════════════════════════════════════════

Key Variances:
• Revenue below plan: 3 delayed deals
• R&D over: Contractor for urgent project
• Net: Below due to revenue shortfall
```

---

## 4. Board Reporting

### Board Deck Structure

**1. Executive Summary**
- Key highlights
- Performance vs. plan
- Strategic updates

**2. Financial Performance**
- Revenue metrics
- MRR waterfall
- P&L summary
- Cash position

**3. Customer Metrics**
- Customer count
- Acquisition metrics
- Retention metrics
- NPS

**4. Product Update**
- Key releases
- Roadmap status
- Technical health

**5. Go-to-Market**
- Sales performance
- Marketing performance
- Pipeline

**6. Team**
- Headcount
- Key hires
- Culture initiatives

**7. Strategic Discussion**
- Key decisions needed
- Upcoming milestones
- Risks and mitigation

### Key Board Metrics

**Must-Have Metrics:**

| Metric | Why |
|--------|-----|
| ARR/MRR | Size of business |
| MRR growth | Growth rate |
| Net Revenue Retention | Existing customer health |
| Gross Margin | Unit economics |
| Burn rate | Cash efficiency |
| Runway | Time to next milestone/raise |
| CAC Payback | Acquisition efficiency |
| Pipeline | Future revenue |

**Board Metrics Dashboard:**
```
BOARD METRICS - Q3 2024
═══════════════════════════════════════════════════

REVENUE
────────────────────────────────────
                    Q3 Actual   Q3 Plan   vs Plan
ARR                 $5.2M       $5.0M     +4%
QoQ Growth          18%         15%       +3pp
Net New MRR         $200K       $180K     +11%

UNIT ECONOMICS
────────────────────────────────────
                    Q3          Q2        Trend
NRR                 112%        108%      ↑
Gross Margin        78%         76%       ↑
CAC Payback         14 mo       16 mo     ↑
LTV:CAC             4.2:1       3.8:1     ↑

CASH
────────────────────────────────────
Cash Balance        $8.5M
Monthly Burn        $350K
Runway              24 months

CUSTOMERS
────────────────────────────────────
Total Customers     425
New (Q3)            75
Churned (Q3)        15
Logo Churn          3.5%

PIPELINE
────────────────────────────────────
Pipeline Value      $2.1M
Coverage            4.2x
Forecast (Q4)       $500K new MRR

═══════════════════════════════════════════════════
```

### Board Meeting Best Practices

**Before Meeting:**
- Send deck 48+ hours in advance
- Pre-read expectation
- Surface issues early
- No surprises

**During Meeting:**
- 60% discussion, 40% presentation
- Focus on decisions needed
- Address concerns directly
- Time for strategic discussion

**After Meeting:**
- Send meeting notes
- Document decisions
- Follow up on action items
- Prepare for next meeting

---

## Summary: Financial Planning Framework

### Financial Planning Checklist

**Model:**
- [ ] Revenue model built
- [ ] Cost model built
- [ ] Assumptions documented
- [ ] Validation checks passing
- [ ] Scenarios created

**Forecasting:**
- [ ] Monthly forecast process
- [ ] Accuracy tracking
- [ ] Cohort-based approach
- [ ] Range/scenario planning

**Budgeting:**
- [ ] Annual budget process
- [ ] Category allocations
- [ ] Monthly tracking
- [ ] Variance analysis

**Reporting:**
- [ ] Board deck template
- [ ] Key metrics defined
- [ ] Reporting cadence
- [ ] Decision tracking

---

*End of Operations Section*
