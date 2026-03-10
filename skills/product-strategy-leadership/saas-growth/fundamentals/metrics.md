# SaaS Metrics: The Numbers That Matter

## Introduction

SaaS metrics are the vital signs of your business. Unlike traditional businesses where revenue and profit tell most of the story, SaaS economics are complex—revenue is recognized over time, customer relationships compound, and the interaction between acquisition, retention, and expansion creates intricate dynamics.

This guide provides a comprehensive understanding of SaaS metrics: how to calculate them, what benchmarks to target, how they interact, and how to use them for decision-making.

---

## 1. Revenue Metrics

### Monthly Recurring Revenue (MRR)

**Definition:** The predictable, recurring revenue normalized to a monthly amount.

**Calculation:**
```
MRR = Sum of all active subscription revenue per month
```

**Components of MRR:**
- **New MRR**: Revenue from new customers acquired this month
- **Expansion MRR**: Revenue increase from existing customers (upgrades, add-ons)
- **Contraction MRR**: Revenue decrease from existing customers (downgrades)
- **Churn MRR**: Revenue lost from cancelled customers
- **Reactivation MRR**: Revenue from previously churned customers returning

**Net New MRR Formula:**
```
Net New MRR = New MRR + Expansion MRR + Reactivation MRR - Contraction MRR - Churn MRR
```

**MRR Waterfall Example:**

| Component | Amount | Description |
|-----------|--------|-------------|
| Starting MRR | $100,000 | Beginning of month |
| + New MRR | $15,000 | 30 new customers @ $500 avg |
| + Expansion MRR | $8,000 | Upgrades and add-ons |
| + Reactivation MRR | $2,000 | Returned customers |
| - Contraction MRR | $3,000 | Downgrades |
| - Churn MRR | $7,000 | Cancellations |
| = Ending MRR | $115,000 | End of month |
| = Net New MRR | $15,000 | Growth |

**MRR Best Practices:**

1. **Normalize annual contracts**: Divide annual payments by 12
2. **Exclude one-time fees**: Setup fees, professional services don't count
3. **Handle mid-month changes**: Use the recurring amount, not what was actually billed
4. **Track components separately**: Understanding the mix is crucial

**MRR vs. Cash:**

MRR is not the same as cash collected:
- Annual prepayment: Collect $12,000 → MRR is $1,000
- Monthly payment: Collect $1,000 → MRR is $1,000
- Failed payment: Collect $0 → MRR might still be counted (until cancellation)

### Annual Recurring Revenue (ARR)

**Definition:** MRR × 12, representing the annualized run rate of recurring revenue.

**Calculation:**
```
ARR = MRR × 12
```

**When to Use ARR vs. MRR:**

| Use ARR When | Use MRR When |
|--------------|--------------|
| Talking to investors | Operational decisions |
| Annual planning | Month-over-month analysis |
| Comparing to enterprise companies | Cash flow planning |
| Calculating valuations | Forecasting |

**ARR is a projection**, not actual revenue. A company with $12M ARR hasn't earned $12M—they're on pace to earn that over the next 12 months if nothing changes.

### Committed ARR (CARR)

**Definition:** ARR including signed contracts not yet live.

```
CARR = Live ARR + Contracted ARR (pending implementation)
```

Useful for:
- Enterprise SaaS with long implementations
- Understanding true pipeline
- Forecasting future ARR

### Annual Contract Value (ACV)

**Definition:** The average annualized revenue per contract.

**Calculation:**
```
ACV = Total Contract Value / Contract Length in Years
```

**Or more commonly:**
```
ACV = ARR / Number of Customers
```

**ACV Benchmarks by Segment:**

| Segment | Typical ACV Range |
|---------|-------------------|
| Consumer | $60-$300 |
| SMB | $600-$5,000 |
| Mid-Market | $5,000-$50,000 |
| Enterprise | $50,000-$500,000+ |

**Why ACV Matters:**
- Determines viable sales motions
- Indicates customer segment
- Impacts CAC payback calculations
- Guides team structure decisions

### Total Contract Value (TCV)

**Definition:** Total value of a contract including all years and one-time fees.

```
TCV = (Annual Value × Contract Years) + One-time Fees
```

**Example:**
- 3-year deal at $100K/year = $300K TCV
- Plus $50K implementation = $350K TCV

### Revenue Recognition

**Deferred Revenue:**

When you collect cash upfront but recognize revenue over time:
- Collect $12,000 annual payment
- Recognize $1,000/month as revenue
- $11,000 sits in deferred revenue (liability)

**Why It Matters:**
- Cash ≠ Revenue in GAAP/IFRS
- Deferred revenue is money you "owe" in service
- Important for financial statements

---

## 2. Customer Metrics

### Customer Count

**Active Customers:** Those currently paying for the product.

**Calculating Customer Count:**
- Count unique paying entities (not users)
- Free tier users are not customers
- Paused accounts: depends on your policy

**Segmentation:**

Track customer count by:
- Plan tier (Free, Starter, Pro, Enterprise)
- Contract type (monthly, annual)
- Size (SMB, mid-market, enterprise)
- Industry/vertical
- Acquisition source

### Average Revenue Per Account (ARPA)

**Definition:** Average revenue per customer, usually monthly.

**Calculation:**
```
ARPA = MRR / Number of Active Customers
```

**Or annually:**
```
Annual ARPA = ARR / Number of Active Customers = ACV
```

**ARPA Trends to Watch:**

- **Rising ARPA**: Moving upmarket, successful expansion
- **Falling ARPA**: More SMB, pricing pressure, downgrades
- **Flat ARPA**: Balance of forces, or stagnation

**ARPA by Cohort:**

Tracking ARPA by signup cohort reveals:
- Are newer customers paying more or less?
- Is pricing strategy working?
- Are you attracting the right customers?

### Logo Churn vs. Revenue Churn

**Logo Churn:** Percentage of customers who cancel.
**Revenue Churn:** Percentage of MRR lost to cancellations.

These often differ significantly:

**Example:**
- Lose 10 customers paying $100/month each = $1,000 MRR
- Lose 1 customer paying $10,000/month = $10,000 MRR
- Same logo churn (if 100 customers), vastly different revenue churn

**Implications:**
- If revenue churn > logo churn: Losing big customers
- If logo churn > revenue churn: Losing small customers
- Enterprise SaaS should obsess over revenue churn
- SMB SaaS watches both closely

---

## 3. Churn Metrics

### Gross Revenue Churn

**Definition:** MRR lost from cancellations and downgrades as a percentage of starting MRR.

**Calculation:**
```
Gross Revenue Churn Rate = (Churn MRR + Contraction MRR) / Starting MRR
```

**Monthly Calculation:**
```
Gross Revenue Churn (Monthly) = MRR Lost This Month / MRR at Start of Month
```

**Example:**
- Starting MRR: $100,000
- Churn MRR: $5,000
- Contraction MRR: $2,000
- Gross Churn: ($5,000 + $2,000) / $100,000 = 7%

**Why Gross Churn Matters:**
- Shows the "leaky bucket" problem
- Indicates customer satisfaction
- Determines how much you need to grow just to stay flat

**Gross Churn Benchmarks:**

| Company Type | Good | Great | Elite |
|--------------|------|-------|-------|
| SMB Monthly | <7% | <5% | <3% |
| SMB Annual | <15% | <10% | <7% |
| Enterprise | <10% annual | <7% annual | <5% annual |

### Net Revenue Churn / Net Revenue Retention (NRR)

**Definition:** Net change in revenue from existing customers, accounting for expansion.

**Net Revenue Churn Calculation:**
```
Net Revenue Churn = (Churn MRR + Contraction MRR - Expansion MRR) / Starting MRR
```

**Net Revenue Retention (NRR) Calculation:**
```
NRR = (Starting MRR - Churn MRR - Contraction MRR + Expansion MRR) / Starting MRR

Or simply:
NRR = 1 - Net Revenue Churn
```

**Example:**
- Starting MRR: $100,000
- Churn MRR: $5,000
- Contraction MRR: $2,000
- Expansion MRR: $10,000
- Net Churn: ($5,000 + $2,000 - $10,000) / $100,000 = -3% (negative = growth!)
- NRR: 103%

**Interpreting NRR:**
- **NRR < 100%**: Shrinking from existing customers (bad)
- **NRR = 100%**: Staying flat (okay)
- **NRR > 100%**: Growing from existing customers (good)
- **NRR > 120%**: Strong expansion (great)

**Why NRR is the Most Important SaaS Metric:**

High NRR means:
- Customers are getting more value over time
- You can grow even without new customers
- LTV is higher than initial calculations
- Product-market fit for existing customers

Low NRR means:
- Product value isn't compounding
- Heavy reliance on new customer acquisition
- Fighting against churn headwinds
- Harder path to profitability

**NRR Benchmarks:**

| Company Type | Target NRR |
|--------------|-----------|
| SMB SaaS | 90-100% |
| Mid-Market SaaS | 100-110% |
| Enterprise SaaS | 110-130% |
| Best-in-Class | 130-150%+ |

**Top Companies NRR Examples:**
- Snowflake: ~160%+ (usage-based, massive expansion)
- Twilio: ~140% (usage growth)
- Slack: ~130% (seat expansion)
- Zoom: ~125% (seat + usage)
- HubSpot: ~110% (upsells)

### Customer (Logo) Churn Rate

**Definition:** Percentage of customers who cancel their subscription.

**Calculation:**
```
Logo Churn Rate = Customers Lost / Starting Customers
```

**Monthly vs. Annual:**
```
Monthly Logo Churn → Annual: 1 - (1 - monthly_rate)^12

Example: 3% monthly → 1 - (1 - 0.03)^12 = 30.6% annual
```

**Logo Churn Benchmarks:**

| Segment | Monthly | Annual |
|---------|---------|--------|
| Consumer B2C | 5-15% | 45-80% |
| SMB | 3-7% | 30-60% |
| Mid-Market | 1-3% | 12-30% |
| Enterprise | 0.5-1.5% | 6-17% |

### Cohort Retention Analysis

**Why Cohorts Matter:**

Overall churn metrics can hide important patterns:
- Different acquisition channels have different retention
- Product changes affect new vs. old customers differently
- Seasonal cohorts may behave differently
- Pricing changes impact cohort behavior

**Building Cohort Tables:**

Rows: Signup month
Columns: Months since signup
Values: % of cohort still active (or % of MRR retained)

**Example Cohort Table (Logo Retention):**

| Cohort | M0 | M1 | M2 | M3 | M6 | M12 |
|--------|-----|-----|-----|-----|-----|-----|
| Jan | 100% | 85% | 78% | 74% | 65% | 52% |
| Feb | 100% | 82% | 75% | 70% | 60% | 48% |
| Mar | 100% | 88% | 82% | 79% | 72% | 61% |
| Apr | 100% | 87% | 81% | 77% | 70% | - |

**Reading the Table:**
- Jan cohort: 85% still active after 1 month, 52% after 12 months
- Mar cohort performing better: 88% M1, 61% M12 (improving!)
- Product/process change in March may have helped

**Revenue Cohort Analysis:**

Same structure, but tracking MRR retained (can exceed 100% with expansion):

| Cohort | M0 | M1 | M2 | M3 | M6 | M12 |
|--------|-----|-----|-----|-----|-----|-----|
| Jan | 100% | 95% | 98% | 102% | 110% | 118% |
| Feb | 100% | 93% | 96% | 98% | 105% | 112% |

Cohort from Jan grew from expansion: started at 100%, now at 118% = 118% NRR for that cohort.

---

## 4. Lifetime Value (LTV)

### Basic LTV Calculation

**Definition:** The total revenue expected from a customer over their entire relationship.

**Simple Formula:**
```
LTV = ARPA / Monthly Churn Rate

Or:
LTV = ARPA × Average Customer Lifetime (in months)
```

**Example:**
- ARPA: $100/month
- Monthly churn: 5%
- LTV = $100 / 0.05 = $2,000

**Alternative (Lifetime in Months):**
```
Average Lifetime = 1 / Monthly Churn Rate

Example: 1 / 0.05 = 20 months
LTV = $100 × 20 = $2,000
```

### Gross Margin-Adjusted LTV

More accurate for comparing across businesses:

```
LTV (Gross Margin) = (ARPA × Gross Margin) / Monthly Churn Rate
```

**Example:**
- ARPA: $100/month
- Gross Margin: 80%
- Monthly Churn: 5%
- LTV (GM) = ($100 × 0.80) / 0.05 = $1,600

### LTV with Expansion Revenue

When customers expand over time:

```
LTV with Expansion = ARPA / (Monthly Churn - Monthly Expansion Rate)
```

**Example:**
- ARPA: $100/month
- Monthly Churn: 5%
- Monthly Expansion Rate: 2%
- Effective Churn = 5% - 2% = 3%
- LTV = $100 / 0.03 = $3,333

**This is why NRR matters so much**—high expansion dramatically increases LTV.

### LTV Calculation Methods

**1. Historic LTV (Simple)**
```
Historic LTV = Total Revenue from Churned Customers / Number of Churned Customers
```

Pros: Based on actual data
Cons: Backward-looking, slow to reflect changes

**2. Predictive LTV (Subscription)**
```
Predictive LTV = ARPA × Predicted Lifetime
```

Use survival analysis or cohort data for lifetime prediction.

**3. DCF-Adjusted LTV**

For more sophisticated analysis, discount future cash flows:

```
LTV = Σ (Monthly Margin × Survival Probability) / (1 + Monthly Discount Rate)^month
```

This accounts for time value of money (a dollar today > dollar tomorrow).

### LTV Benchmarks

| Segment | Typical LTV Range |
|---------|-------------------|
| Consumer B2C | $100-$500 |
| SMB | $1,000-$5,000 |
| Mid-Market | $10,000-$50,000 |
| Enterprise | $100,000-$1,000,000+ |

---

## 5. Customer Acquisition Cost (CAC)

### Basic CAC Calculation

**Definition:** The cost to acquire a new customer.

**Simple Formula:**
```
CAC = Total Sales & Marketing Spend / New Customers Acquired
```

**Example:**
- Marketing spend: $50,000
- Sales spend: $75,000
- New customers: 100
- CAC = $125,000 / 100 = $1,250

### Blended vs. Segmented CAC

**Blended CAC:** Overall CAC across all channels and segments.

**Segmented CAC:** CAC broken down by:
- **Channel**: Organic vs. paid vs. outbound
- **Segment**: SMB vs. mid-market vs. enterprise
- **Product**: If multiple products

**Example Segmented CAC:**

| Segment | Customers | Spend | CAC |
|---------|-----------|-------|-----|
| SMB (self-serve) | 80 | $40,000 | $500 |
| Mid-Market (sales) | 15 | $60,000 | $4,000 |
| Enterprise (sales) | 5 | $25,000 | $5,000 |
| **Blended** | **100** | **$125,000** | **$1,250** |

**Why This Matters:**

Blended CAC of $1,250 hides that:
- SMB is efficient ($500 CAC)
- Enterprise is less efficient but higher value

### Fully-Loaded CAC

Include ALL costs of acquisition:

```
Fully-Loaded CAC = (Salaries + Commissions + Tools + Ads + Content + Events + Overhead) / New Customers
```

**What to Include:**
- Marketing team salaries
- Sales team salaries
- Sales commissions
- Advertising spend
- Marketing software (HubSpot, etc.)
- Content creation costs
- Events and sponsorships
- PR and analyst relations
- Allocated overhead

**What NOT to Include:**
- Customer success (that's retention, not acquisition)
- Product development
- General company overhead (unless allocated)

### CAC by Channel

Track CAC for each acquisition channel:

| Channel | CAC | Notes |
|---------|-----|-------|
| Organic/SEO | $200 | Long-term investment |
| Paid Search | $800 | Scalable but competitive |
| Paid Social | $1,200 | Varies by platform |
| Outbound Sales | $3,000 | Enterprise focus |
| Partnerships | $600 | Revenue share often |
| Referrals | $150 | Lowest CAC |
| Events | $5,000 | Enterprise, high-touch |

### CAC Payback Period

**Definition:** How long until a customer pays back their acquisition cost.

**Calculation:**
```
CAC Payback (months) = CAC / (ARPA × Gross Margin)
```

**Example:**
- CAC: $1,200
- ARPA: $100/month
- Gross Margin: 80%
- Payback = $1,200 / ($100 × 0.80) = 15 months

**Payback Benchmarks:**

| Quality | Payback Period |
|---------|---------------|
| Excellent | < 6 months |
| Good | 6-12 months |
| Acceptable | 12-18 months |
| Concerning | 18-24 months |
| Dangerous | > 24 months |

**Why Payback Matters:**
- Shorter payback = faster reinvestment
- Long payback = cash flow pressure
- Affects growth rate sustainability
- Key metric for investors

### CAC Benchmarks

| Segment | Typical CAC Range |
|---------|-------------------|
| Consumer B2C | $10-$100 |
| SMB Self-Serve | $100-$500 |
| SMB Sales-Assisted | $500-$2,000 |
| Mid-Market | $2,000-$20,000 |
| Enterprise | $20,000-$100,000+ |

---

## 6. LTV:CAC Ratio

### The Golden Ratio

**Definition:** Lifetime value divided by customer acquisition cost.

**Calculation:**
```
LTV:CAC = LTV / CAC
```

**Example:**
- LTV: $5,000
- CAC: $1,250
- LTV:CAC = 4.0 (or 4:1)

### Interpreting LTV:CAC

| Ratio | Interpretation | Action |
|-------|---------------|--------|
| < 1:1 | Losing money on each customer | Crisis mode |
| 1:1 to 2:1 | Barely viable | Reduce CAC or improve retention |
| 3:1 | Healthy | Good baseline |
| 4:1 to 5:1 | Strong | Room to invest in growth |
| > 5:1 | Very efficient | Consider investing more in acquisition |

**The "3x Rule":** LTV:CAC of 3:1 is often cited as the minimum for a healthy SaaS business.

**Too High Can Be Bad:**

LTV:CAC > 5:1 might mean:
- Underinvesting in growth
- Missing market opportunity
- Competitors will outspend you
- Not enough channel diversification

### LTV:CAC Benchmarks

| Company Stage | Target LTV:CAC |
|---------------|---------------|
| Pre-PMF | Focus on retention first |
| Early Stage | > 3:1 |
| Growth Stage | 3:1 to 5:1 |
| Mature | 3:1 to 4:1 |

**By Segment:**

| Segment | Typical LTV:CAC |
|---------|-----------------|
| SMB Self-Serve | 4:1 to 8:1 |
| Mid-Market | 3:1 to 5:1 |
| Enterprise | 2:1 to 4:1 |

Enterprise tolerates lower ratios because:
- Higher revenue per customer
- More predictable (lower churn)
- Strategic value beyond revenue

### LTV:CAC Improvement Levers

**To Increase LTV:**
- Reduce churn (biggest impact)
- Increase expansion revenue
- Raise prices (carefully)
- Add upsell products
- Improve gross margin

**To Decrease CAC:**
- Improve conversion rates
- Optimize paid channels
- Invest in organic/content
- Build referral programs
- Shorten sales cycles
- Improve targeting

---

## 7. Quick Ratio (SaaS)

### Definition

**SaaS Quick Ratio:** Measures growth efficiency by comparing revenue inflows to outflows.

**Calculation:**
```
Quick Ratio = (New MRR + Expansion MRR) / (Churned MRR + Contraction MRR)
```

**Example:**
- New MRR: $15,000
- Expansion MRR: $8,000
- Churned MRR: $7,000
- Contraction MRR: $3,000
- Quick Ratio = ($15,000 + $8,000) / ($7,000 + $3,000) = 2.3

### Interpreting Quick Ratio

| Quick Ratio | Interpretation |
|-------------|---------------|
| < 1 | Shrinking (losing more than gaining) |
| 1-2 | Slow growth, leaky bucket |
| 2-3 | Healthy growth |
| 3-4 | Strong growth |
| > 4 | Excellent (efficient growth) |

**Mamoon Hamid (Kleiner Perkins) Rule:**
- "Good" SaaS companies have Quick Ratio > 4
- But this is very hard to sustain at scale

**More Realistic Targets:**
- Early stage: > 4 (growing fast, churn not yet showing)
- Growth stage: 2-4 (sustainable)
- Scale stage: 1.5-2.5 (natural slowing)

### Quick Ratio by Stage

| ARR Stage | Target Quick Ratio |
|-----------|-------------------|
| $0-1M | > 4 |
| $1-5M | > 3 |
| $5-20M | > 2.5 |
| $20-50M | > 2 |
| $50M+ | > 1.5 |

---

## 8. Gross Margin

### Definition

**Gross Margin:** Revenue minus cost of goods sold, as a percentage.

**Calculation:**
```
Gross Margin = (Revenue - COGS) / Revenue × 100
```

**SaaS COGS Includes:**
- Hosting/infrastructure costs
- Customer support salaries
- Customer success salaries (sometimes)
- Third-party software fees (per-customer)
- Payment processing fees
- Professional services costs (if included in revenue)

**Example:**
- Revenue: $100,000
- Hosting: $5,000
- Support: $10,000
- Payment fees: $3,000
- COGS: $18,000
- Gross Margin = ($100,000 - $18,000) / $100,000 = 82%

### SaaS Gross Margin Benchmarks

| Type | Typical Range | Target |
|------|---------------|--------|
| Pure SaaS | 70-90% | > 75% |
| SaaS + Services | 50-70% | > 60% |
| Infrastructure SaaS | 50-70% | > 60% |
| Usage-Based | 60-80% | > 65% |

**What Good Looks Like:**
- Slack: ~87%
- Zoom: ~75%
- Salesforce: ~75%
- Snowflake: ~68%
- Twilio: ~52%

### Why Gross Margin Matters

1. **LTV Calculation:** Affects true customer profitability
2. **Valuation:** Higher margin = higher multiple
3. **Investment Capacity:** More margin = more to reinvest
4. **Operating Leverage:** Margin improvement drops to bottom line

### Improving Gross Margin

**Infrastructure Optimization:**
- Negotiate cloud contracts
- Optimize resource usage
- Right-size infrastructure
- Multi-cloud arbitrage

**Support Efficiency:**
- Self-serve documentation
- Chatbots and automation
- Community support
- Tiered support (paid premium)

**Payment Optimization:**
- Negotiate processing rates
- ACH for annual contracts
- Annual vs. monthly (fewer transactions)

---

## 9. The Rule of 40

### Definition

**Rule of 40:** Growth rate + profit margin should exceed 40%.

**Calculation:**
```
Rule of 40 Score = Revenue Growth Rate (%) + EBITDA Margin (%)

Or for earlier stage:
Rule of 40 Score = Revenue Growth Rate (%) + Free Cash Flow Margin (%)
```

**Examples:**

| Company | Growth | Margin | Rule of 40 |
|---------|--------|--------|-----------|
| A | 50% | -10% | 40% ✓ |
| B | 30% | 15% | 45% ✓ |
| C | 20% | 25% | 45% ✓ |
| D | 15% | 10% | 25% ✗ |

### Interpreting Rule of 40

| Score | Interpretation |
|-------|---------------|
| > 60% | Exceptional |
| 40-60% | Strong |
| 25-40% | Acceptable |
| < 25% | Needs improvement |

**The Trade-off:**
- High growth companies can burn cash (negative margin)
- Slower growth companies need profitability
- Balance shifts as company matures

### Rule of 40 by Stage

| ARR | Typical Target |
|-----|----------------|
| < $10M | Growth > 100%, margin less relevant |
| $10-50M | > 40% combined |
| $50-100M | > 40% with margin > 0% |
| $100M+ | > 40% with positive margin |

---

## 10. Metrics Hierarchy and Dashboards

### Primary Metrics (Track Daily/Weekly)

1. **MRR/ARR**: The foundation
2. **Net New MRR**: Growth engine
3. **Churn Rate**: Health indicator
4. **New Customers**: Volume metric

### Secondary Metrics (Track Weekly/Monthly)

1. **NRR**: Expansion health
2. **ARPA**: Customer value
3. **LTV:CAC**: Unit economics
4. **CAC Payback**: Efficiency
5. **Quick Ratio**: Growth quality

### Strategic Metrics (Track Monthly/Quarterly)

1. **Gross Margin**: Profitability
2. **Rule of 40**: Overall health
3. **Cohort Analysis**: Deep understanding
4. **Customer Concentration**: Risk assessment

### Sample Executive Dashboard

```
┌─────────────────────────────────────────────────────────┐
│                    SaaS METRICS DASHBOARD               │
├─────────────────────────────────────────────────────────┤
│ ARR: $2.4M        MRR: $200K       Customers: 400       │
│ MoM Growth: 8%    Net New MRR: $15K                     │
├─────────────────────────────────────────────────────────┤
│ MRR Breakdown:                                          │
│ ├─ New: $12K (80 customers @ $150 avg)                 │
│ ├─ Expansion: $6K                                       │
│ ├─ Contraction: -$1.5K                                  │
│ └─ Churn: -$1.5K                                        │
├─────────────────────────────────────────────────────────┤
│ Retention:                                              │
│ ├─ Gross Revenue Churn: 0.75%                          │
│ ├─ Net Revenue Retention: 102.25%                       │
│ └─ Logo Churn: 2%                                       │
├─────────────────────────────────────────────────────────┤
│ Unit Economics:                                         │
│ ├─ ARPA: $500/mo                                        │
│ ├─ CAC: $1,500                                          │
│ ├─ LTV: $8,000 (GM-adjusted)                           │
│ ├─ LTV:CAC: 5.3:1                                       │
│ └─ Payback: 4 months                                    │
├─────────────────────────────────────────────────────────┤
│ Efficiency:                                             │
│ ├─ Gross Margin: 80%                                    │
│ ├─ Quick Ratio: 4.0                                     │
│ └─ Rule of 40: 58% (96% growth + -38% margin)          │
└─────────────────────────────────────────────────────────┘
```

### Metrics by Company Stage

**$0-$1M ARR (Finding PMF)**

Primary Focus:
- Retention (are people staying?)
- Activation (are people getting value?)
- Customer feedback (qualitative)

Secondary:
- New customer count
- Time to value
- Feature usage

**$1M-$10M ARR (Finding Repeatability)**

Primary Focus:
- Net New MRR (growth engine)
- CAC by channel
- NRR (expansion working?)

Secondary:
- LTV:CAC
- Payback period
- Cohort retention curves

**$10M+ ARR (Scaling Efficiently)**

Primary Focus:
- Efficiency metrics (Rule of 40)
- Gross margin
- CAC payback

Secondary:
- Customer concentration
- Enterprise metrics
- Sales productivity

---

## 11. Metric Mistakes to Avoid

### Vanity Metrics

**Don't Celebrate:**
- Total signups (without activation)
- Page views (without conversion)
- Downloads (without usage)
- "Users" (vs. paying customers)
- Gross bookings (vs. recognized revenue)

**Do Track:**
- Activated users
- Paying customers
- Net revenue
- Active usage

### Calculation Errors

**Common Mistakes:**

1. **Including one-time revenue in MRR**
   - Setup fees, professional services aren't recurring

2. **Not normalizing annual contracts**
   - $12K annual = $1K MRR, not $12K MRR

3. **Wrong churn denominator**
   - Use STARTING customers/MRR, not ending

4. **Mixing time periods**
   - Monthly CAC with annual LTV

5. **Ignoring gross margin in LTV**
   - Revenue ≠ profit

6. **Survivorship bias in cohorts**
   - Only tracking active customers hides churn

### Over-Optimization Traps

1. **Optimizing churn too early**
   - Focus on activation first

2. **Reducing CAC at expense of quality**
   - Cheap customers often churn faster

3. **Chasing vanity NRR**
   - Forced upgrades backfire

4. **Ignoring leading indicators**
   - By the time churn shows, it's too late

---

## Summary: The Metrics That Matter Most

### If You Track Only 5 Metrics:

1. **ARR/MRR**: How big is the business?
2. **Net New MRR**: Is it growing?
3. **Gross Revenue Churn**: Is it retaining?
4. **LTV:CAC**: Is it efficient?
5. **Cash**: Can it survive?

### The Ultimate Questions Metrics Answer:

| Question | Metric |
|----------|--------|
| How big? | ARR |
| How fast? | MRR growth rate |
| How sticky? | Churn, NRR |
| How efficient? | LTV:CAC, CAC Payback |
| How profitable? | Gross margin, Rule of 40 |
| How healthy? | Quick Ratio |

---

*Next: [SaaS Economics](./economics.md) - Unit economics, cohort analysis, and financial planning*
