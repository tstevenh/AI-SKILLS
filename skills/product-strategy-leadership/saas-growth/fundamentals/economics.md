# SaaS Economics

## Introduction

Understanding SaaS economics is the difference between building a sustainable business and running on a treadmill. Unlike traditional businesses where profit = revenue - costs, SaaS economics involve complex relationships between acquisition costs paid today, revenue recognized over years, and the compounding effects of retention and expansion.

This section dives deep into unit economics, cohort analysis, revenue forecasting, cash flow management, and the eternal question: should you bootstrap or raise capital?

---

## 1. Unit Economics Explained

### What Are Unit Economics?

Unit economics measure the profitability of a single "unit" of your business—typically one customer. They answer the fundamental question: **Do we make money on each customer we acquire?**

### The Unit Economics Equation

**Basic Profitability:**
```
Unit Profit = LTV - CAC

If LTV > CAC → Profitable unit
If LTV < CAC → Unprofitable unit
```

**Time-Adjusted View:**
```
Cumulative Profit at Month N = Σ(Monthly Margin × Survival Rate) - CAC
```

### Visualizing Unit Economics

**Customer Economics Over Time:**

```
Month    Revenue    Margin(80%)   Cumulative    CAC      Net
  0      $0         $0            $0            $1,200   -$1,200
  1      $100       $80           $80           $1,200   -$1,120
  3      $100       $80           $240          $1,200   -$960
  6      $100       $80           $480          $1,200   -$720
 12      $100       $80           $960          $1,200   -$240
 15      $100       $80           $1,200        $1,200   $0 ← Payback
 24      $100       $80           $1,920        $1,200   +$720
 36      $100       $80           $2,880        $1,200   +$1,680
```

**With Churn (5% monthly):**

```
Month    Survival    Revenue    Margin    Cumulative    Net
  0      100%        $0         $0        $0            -$1,200
  1      95%         $95        $76       $76           -$1,124
  3      86%         $86        $69       $217          -$983
  6      74%         $74        $59       $404          -$796
 12      54%         $54        $43       $644          -$556
 18      40%         $40        $32       $816          -$384
 24      29%         $29        $23       $932          -$268
 36      16%         $16        $13       $1,042        -$158
```

**Key Insight:** With 5% monthly churn, this customer may never reach payback at the $100 ARPA level. Need higher ARPA, lower CAC, or better retention.

### Unit Economics by Segment

Different customer segments have radically different unit economics:

| Segment | ACV | CAC | LTV | LTV:CAC | Payback |
|---------|-----|-----|-----|---------|---------|
| Self-Serve SMB | $600 | $200 | $1,200 | 6:1 | 4 mo |
| Sales-Assisted SMB | $1,200 | $800 | $2,400 | 3:1 | 8 mo |
| Mid-Market | $12,000 | $6,000 | $36,000 | 6:1 | 6 mo |
| Enterprise | $60,000 | $40,000 | $180,000 | 4.5:1 | 8 mo |

### Marginal Unit Economics

**The Key Question:** What does the NEXT customer cost?

**Fixed vs. Variable Costs:**

Fixed Costs (don't change with one more customer):
- Marketing team salaries
- Content already created
- Events already sponsored
- Tools already purchased

Variable Costs (change with each customer):
- Paid ads (cost per click)
- Sales commission
- Hosting (if usage-based)
- Support time

**Marginal CAC:**
```
Marginal CAC = Variable Cost per Acquisition

Often much lower than Blended CAC
```

**Example:**
- Total marketing spend: $100,000
- New customers: 100
- Blended CAC: $1,000

But if 50 came from organic (variable cost: $0) and 50 from ads ($500 each):
- Marginal CAC for organic: $0
- Marginal CAC for paid: $500

**Why This Matters:**

You might think CAC is $1,000, but:
- Organic customers: Actually $0 marginal CAC
- Paid customers: $500 marginal CAC
- The next $10K spent on paid = 20 more customers

### Unit Economics Levers

**To Improve LTV:**

| Lever | Impact | Difficulty |
|-------|--------|-----------|
| Reduce churn | Very High | Medium |
| Increase expansion | High | Medium |
| Raise prices | Medium | Low |
| Improve gross margin | Medium | Medium |
| Add products | High | High |

**To Reduce CAC:**

| Lever | Impact | Difficulty |
|-------|--------|-----------|
| Improve conversion rate | High | Medium |
| Optimize paid channels | Medium | Ongoing |
| Invest in content/SEO | High | Long-term |
| Build referral program | Medium | Medium |
| Shorten sales cycle | Medium | Medium |
| Reduce sales cost | Medium | Careful |

---

## 2. Cohort Analysis

### Why Cohorts Matter

Aggregate metrics hide important patterns. Cohort analysis reveals:
- How different groups of customers behave
- Whether you're improving over time
- Early warning signs of problems
- True customer lifetime patterns

### Types of Cohorts

**Time-Based Cohorts:**
- Signup month/quarter
- First purchase date
- Campaign date

**Attribute-Based Cohorts:**
- Acquisition channel
- Plan tier
- Company size
- Geography
- Use case

### Building Retention Cohorts

**Logo Retention Cohort Table:**

| Signup | M0 | M1 | M2 | M3 | M6 | M12 | M24 |
|--------|-----|-----|-----|-----|-----|-----|-----|
| Jan'24 | 100 | 85 | 78 | 74 | 65 | 52 | 42 |
| Feb'24 | 100 | 82 | 75 | 70 | 60 | 48 | - |
| Mar'24 | 100 | 88 | 82 | 79 | 72 | 61 | - |
| Apr'24 | 100 | 87 | 81 | 77 | 70 | - | - |
| May'24 | 100 | 90 | 85 | 82 | - | - | - |

**Reading This Table:**
- January cohort: Started with 100%, 52% remain at month 12
- Improvement visible: March cohort at 61% vs January at 52%
- May cohort showing best early retention (90% M1)

**Revenue Retention Cohort Table:**

| Signup | M0 | M3 | M6 | M12 | M24 |
|--------|-----|-----|-----|-----|-----|
| Jan'24 | 100% | 102% | 108% | 118% | 125% |
| Feb'24 | 100% | 98% | 104% | 112% | - |
| Mar'24 | 100% | 105% | 115% | 128% | - |
| Apr'24 | 100% | 103% | 112% | - | - |

**Key Insight:** Revenue exceeds 100% due to expansion. January cohort at 118% month 12 = NRR of 118% for that cohort.

### Cohort Analysis Techniques

**1. Retention Curve Shape**

Healthy retention curves flatten out over time:

```
100% ─┐
      │╲
 80%  │ ╲
      │  ╲____
 60%  │       ╲____
      │             ─────────── ← Flatten = stable
 40%  │
      └───────────────────────────
       M1  M3  M6  M12  M24  M36
```

Bad retention curves keep declining:

```
100% ─┐
      │╲
 80%  │ ╲
      │  ╲
 60%  │   ╲
      │    ╲
 40%  │     ╲
      │      ╲                  ← Never flattens = problem
 20%  │       ╲
      └─────────╲───────────────
       M1  M3  M6  M12  M24  M36
```

**2. Cohort Comparison**

Compare cohorts to identify:
- Seasonal patterns (Q1 cohorts worse? Better?)
- Product improvements (newer cohorts better?)
- Channel quality (paid vs organic cohorts)
- Pricing impact (post-price change cohorts)

**3. Triangular Cohort Matrix**

Full matrix shows pattern evolution:

```
      M0    M1    M2    M3    M4    M5
Jan   100%  85%   78%   74%   70%   67%
Feb   100%  82%   75%   70%   66%   
Mar   100%  88%   82%   79%   
Apr   100%  87%   81%   
May   100%  90%   
Jun   100%  
```

Look diagonally: Each diagonal represents the same calendar month. If a diagonal shows weakness, something happened that month.

### Advanced Cohort Metrics

**Average Revenue Per User (ARPU) by Cohort:**

| Signup | M0 | M3 | M6 | M12 |
|--------|-----|-----|-----|-----|
| Jan'24 | $80 | $95 | $110 | $140 |
| Apr'24 | $100 | $120 | $145 | - |

April cohort starts higher and expands faster—pricing change or better customers?

**Feature Adoption by Cohort:**

| Signup | Feature A | Feature B | Feature C |
|--------|-----------|-----------|-----------|
| Pre-launch | 45% | 60% | - |
| Post-launch | 62% | 58% | 73% |

New feature (C) driving engagement in newer cohorts.

**Activation by Cohort:**

| Signup | Day 1 | Day 7 | Day 30 |
|--------|-------|-------|--------|
| Jan | 45% | 52% | 55% |
| Feb | 48% | 55% | 58% |
| Mar | 55% | 62% | 65% |

Onboarding improvements showing in activation rates.

### Cohort Analysis Tools

**Spreadsheet Method:**
- Export customer data with signup date, MRR by month
- Pivot table: Rows = signup month, Columns = months since signup
- Calculate % of starting value for each cell

**Analytics Tools:**
- Amplitude: Built-in retention analysis
- Mixpanel: Cohort analysis
- ChartMogul: Revenue cohorts
- ProfitWell: Retention cohorts
- Baremetrics: Financial cohorts

**SQL Pattern:**

```sql
SELECT 
  DATE_TRUNC('month', signup_date) as cohort,
  DATE_DIFF('month', signup_date, activity_date) as month_number,
  COUNT(DISTINCT user_id) as active_users
FROM user_activity
GROUP BY 1, 2
ORDER BY 1, 2
```

---

## 3. Revenue Forecasting

### Bottom-Up Forecasting

Build forecast from individual components:

**MRR Forecasting Model:**

```
Next Month MRR = 
  Current MRR
  + Expected New MRR
  + Expected Expansion MRR
  - Expected Churn MRR
  - Expected Contraction MRR
```

**Forecasting Each Component:**

**New MRR Forecast:**
```
New MRR = Signups × Conversion Rate × Average Starting MRR

Example:
- Expected signups: 500
- Trial-to-paid: 20%
- Average starting plan: $100
- New MRR = 500 × 0.20 × $100 = $10,000
```

**Expansion MRR Forecast:**
```
Expansion MRR = Current MRR × Historical Expansion Rate

Example:
- Current MRR: $200,000
- Historical expansion: 3%/month
- Expansion MRR = $200,000 × 0.03 = $6,000
```

**Churn MRR Forecast:**
```
Churn MRR = Current MRR × Historical Churn Rate

Example:
- Current MRR: $200,000
- Historical churn: 3%/month
- Churn MRR = $200,000 × 0.03 = $6,000
```

### Top-Down Forecasting

Start with target and work backward:

**Goal-Based Model:**
```
To reach $5M ARR in 12 months from $2M ARR:
- Required growth: 150% or ~8% monthly
- Current Net New MRR needed: $167K/month by end of year
- If churn = $60K, need $227K gross new + expansion
```

### Driver-Based Forecasting

Forecast the inputs, derive the outputs:

**Key Drivers:**
- Website traffic → Signups → Trials → Conversions
- Sales pipeline → Demos → Opportunities → Closed
- Existing customers → Expansion eligible → Expansion rate
- At-risk customers → Churn probability → Churned

**Example Driver Model:**

```
Traffic: 50,000 visits
→ Signup rate: 2%
→ Signups: 1,000
→ Trial start rate: 80%
→ Trials: 800
→ Conversion rate: 15%
→ New customers: 120
→ Average ACV: $1,200
→ New ARR: $144,000/month
```

### Scenario Planning

Build multiple scenarios:

| Scenario | Growth | Churn | NRR | 12-Month ARR |
|----------|--------|-------|-----|--------------|
| Bear | 5%/mo | 5% | 95% | $3.2M |
| Base | 8%/mo | 3% | 105% | $4.8M |
| Bull | 12%/mo | 2% | 115% | $6.5M |

**Key Variables to Stress Test:**
- Conversion rate changes
- Churn rate changes
- Average deal size
- Sales cycle length
- Expansion rate

### Forecasting Best Practices

1. **Use cohort data**: Retention curves predict future churn
2. **Segment forecasts**: SMB and Enterprise behave differently
3. **Validate assumptions**: Compare forecast to actual monthly
4. **Update regularly**: Re-forecast monthly with new data
5. **Build ranges**: Point estimates are always wrong; ranges capture uncertainty

---

## 4. Cash Flow Considerations

### The SaaS Cash Flow Challenge

SaaS businesses often lose money on customers upfront:

```
Month 0: Spend $1,200 CAC
Month 1: Collect $100
Month 2: Collect $100
...
Month 15: Break even on this customer
Month 16+: Start making profit
```

**The Problem:** You need cash TODAY to acquire customers who pay you LATER.

### Cash vs. Revenue vs. Profit

**Three Different Numbers:**

| Metric | When Counted | Example |
|--------|--------------|---------|
| Cash | When received | Collect $1,200 annual upfront |
| Revenue | When earned | Recognize $100/month |
| Profit | Revenue - Costs | $100 - $80 = $20 |

**Annual Prepay Impact:**
- Better cash flow (get money now)
- Deferred revenue on balance sheet
- Cash > Revenue in growth mode

### Working Capital Requirements

**Growth Requires Cash:**

To grow MRR by $100K:
- If CAC = $1,200 and ARPA = $100
- Need 1,000 new customers
- CAC investment: $1,200,000 (spent upfront)
- Revenue: $100,000/month (received over time)

**Cash Gap Calculation:**
```
Cash needed = Growth Target × CAC / ARPA
Cash Gap = Cash needed - Cash from operations
```

### Funding Growth

**Self-Funded Growth:**
```
Maximum Growth Rate = Net Cash Flow / CAC per New Customer
```

If you generate $50K cash/month and CAC is $500:
- Can afford 100 new customers/month
- At $100 ARPA = $10K new MRR/month
- = 5% monthly growth on $200K MRR base

**Venture-Funded Growth:**
- Raise capital to fund CAC gap
- Grow faster than cash flow allows
- Trade equity for growth rate

### Cash Flow Levers

**Improve Cash Position:**

| Lever | Impact | Notes |
|-------|--------|-------|
| Annual prepay | High | Offer 20%+ discount |
| Reduce CAC | Medium | Takes time |
| Shorten payback | Medium | Pricing, retention |
| Reduce COGS | Low | Hosting optimization |
| Delay vendor payments | Low | Net 30/60 terms |

**Annual Contract Benefits:**
- Collect cash upfront
- Lower churn (commitment)
- Better forecasting
- Typically worth 15-25% discount

### Cash Flow Forecasting

**13-Week Cash Flow Model:**

```
Week    Starting    Inflows    Outflows    Ending
  1     $500,000    $75,000    $60,000     $515,000
  2     $515,000    $70,000    $65,000     $520,000
  3     $520,000    $80,000    $70,000     $530,000
...
```

**Key Inflows:**
- Monthly subscription payments
- Annual renewals
- New customer first payments
- Professional services

**Key Outflows:**
- Payroll (typically 50-70% of spend)
- Marketing/advertising
- Hosting/infrastructure
- Software subscriptions
- Office/facilities

### The Rule of 40 and Cash

Companies above Rule of 40 often generate cash:
- High growth + moderate burn = fine
- Moderate growth + profitability = generating cash
- Low growth + burning cash = problem

---

## 5. When to Raise vs. Bootstrap

### The Fundamental Trade-off

**Raising Capital:**
- Pro: Faster growth potential
- Pro: Longer runway for experimentation
- Pro: Access to expertise/network
- Con: Dilution (give up ownership)
- Con: Pressure for specific outcomes
- Con: Loss of control

**Bootstrapping:**
- Pro: Full ownership retained
- Pro: Control over decisions
- Pro: Profitable from earlier
- Con: Slower growth
- Con: Limited resources
- Con: Competitive disadvantage in winner-take-all markets

### When to Bootstrap

**Bootstrap if:**

1. **Market allows it**: Not winner-take-all, room for multiple players
2. **CAC payback is short**: Self-fund growth from revenue
3. **No network effects**: First mover advantage isn't decisive
4. **Lifestyle fit**: Prefer control over maximum outcome
5. **Proven playbook**: Know how to acquire customers efficiently

**Good Bootstrap Fit:**
- Niche vertical SaaS
- Services + software hybrid
- Geographic focus
- Agency/productized service
- Passion project / lifestyle business

**Bootstrap Benchmarks:**
- Achieve profitability within 18-24 months
- Target 30-50% growth annually
- Own 100% of equity

### When to Raise Capital

**Raise if:**

1. **Winner-take-all market**: Speed is existential
2. **Network effects**: First to scale wins
3. **Long sales cycles**: Need capital for enterprise sales
4. **High CAC**: Can't self-fund customer acquisition
5. **Competitive pressure**: Well-funded competitors

**Good VC Fit:**
- Platform plays (marketplaces, networks)
- Infrastructure/developer tools
- Enterprise with long sales cycles
- Markets with clear #1 winner dynamics
- Breakthrough technology

**VC Expectations:**
- 10x+ return potential
- $100M+ ARR path
- 100%+ annual growth (early stage)
- Eventual IPO or large acquisition

### The Funding Spectrum

```
┌─────────────────────────────────────────────────────────┐
│                                                         │
│  Bootstrap    Revenue-Based    Angel    Seed    Series  │
│     ▼             ▼             ▼        ▼         ▼   │
│   No             Debt-like     Equity   Equity   Equity│
│   Dilution       Minimal       5-15%    15-25%   20-30%│
│                                                         │
│  Full    ←─────────────────────────────────→    Less   │
│  Control                                        Control │
└─────────────────────────────────────────────────────────┘
```

### Alternative Funding Options

**Revenue-Based Financing:**
- Borrow against MRR (typically 3-6x monthly)
- Pay back as percentage of revenue
- No dilution, but has cost
- Providers: Pipe, Capchase, Clearco

**Venture Debt:**
- Debt for VC-backed companies
- Extends runway between rounds
- Interest + warrants (small dilution)
- Providers: SVB, Hercules, Western Technology

**Angel/Indie Funding:**
- Smaller checks, less pressure
- Often founder-friendly terms
- Good for getting to $1M ARR
- Platforms: Calm Fund, TinySeed, Earnest Capital

### Decision Framework

**Step 1: Define Your Goal**
- Build a $1B company? Likely need VC.
- Build a $10M/year lifestyle business? Bootstrap.
- Build a $50M company? Either could work.

**Step 2: Assess Market Dynamics**
- Is speed critical? (VC favored)
- Is there room for niche players? (Bootstrap OK)

**Step 3: Evaluate Unit Economics**
- Can you self-fund growth? (Bootstrap possible)
- Is CAC payback > 12 months? (Funding helps)

**Step 4: Personal Preference**
- Do you want maximum ownership?
- Can you handle investor pressure?
- Do you need strategic help?

### Hybrid Approaches

**Bootstrap First, Raise Later:**
- Prove model bootstrapped
- Raise from position of strength
- Better terms, less dilution

**Small Raise, Efficient Growth:**
- Raise modest seed ($500K-$2M)
- Grow efficiently (not hyper-growth)
- May not need more funding

**Raise, Then Become Profitable:**
- Use funding to reach scale
- Then focus on profitability
- "Default alive" mindset

---

## 6. Financial Modeling for SaaS

### Core Model Components

**Revenue Model:**
- Starting MRR/ARR
- New customer acquisition
- Expansion revenue
- Churn and contraction
- Output: MRR/ARR forecast

**Cost Model:**
- People (headcount × salary)
- Marketing spend
- Sales spend
- Hosting/infrastructure
- Software/tools
- Office/overhead
- Output: Monthly burn

**Cash Model:**
- Starting cash
- Revenue collected
- Expenses paid
- Output: Cash runway

### Building a SaaS Financial Model

**Revenue Sheet:**

| Month | Starting MRR | New | Expansion | Churn | Ending MRR |
|-------|-------------|-----|-----------|-------|------------|
| M1 | $100,000 | $10,000 | $5,000 | $5,000 | $110,000 |
| M2 | $110,000 | $11,000 | $5,500 | $5,500 | $121,000 |
| M3 | $121,000 | $12,100 | $6,050 | $6,050 | $133,100 |

**Assumptions:**
- New MRR grows at 10%/month
- Expansion = 5% of starting MRR
- Churn = 5% of starting MRR

**Expense Sheet:**

| Category | M1 | M2 | M3 | Notes |
|----------|-----|-----|-----|-------|
| People | $80,000 | $80,000 | $85,000 | +1 hire M3 |
| Marketing | $20,000 | $22,000 | $25,000 | Scaling |
| Sales | $15,000 | $16,000 | $18,000 | Commission |
| Hosting | $5,000 | $5,500 | $6,000 | Scales with customers |
| Tools | $3,000 | $3,000 | $3,500 | Added tool |
| Other | $7,000 | $7,000 | $7,500 | Overhead |
| **Total** | **$130,000** | **$133,500** | **$145,000** | |

**P&L Summary:**

| | M1 | M2 | M3 |
|--|-----|-----|-----|
| Revenue | $100,000 | $110,000 | $121,000 |
| Gross Margin (80%) | $80,000 | $88,000 | $96,800 |
| Operating Expenses | $130,000 | $133,500 | $145,000 |
| Net Income | -$50,000 | -$45,500 | -$48,200 |

### Key Model Ratios

**Burn Rate:**
```
Net Burn = Cash Out - Cash In
Gross Burn = Total Cash Out (ignore revenue)
```

**Runway:**
```
Runway (months) = Cash Balance / Monthly Net Burn
```

**Efficiency:**
```
Burn Multiple = Net Burn / Net New ARR

Example: $150K burn / $50K Net New ARR = 3x burn multiple

< 1x = Excellent
1-2x = Good
2-3x = Acceptable (early stage)
> 3x = Concerning
```

### Scenario Modeling

Build three scenarios:

**Conservative (Bear):**
- Lower conversion rates
- Higher churn
- Slower hiring

**Base Case:**
- Expected performance
- Realistic assumptions
- Most likely outcome

**Aggressive (Bull):**
- Everything works
- Faster growth
- Expand team quickly

**Present All Three:**
- Investors expect base case
- Board wants to know downside
- Team should know upside potential

---

## Summary: SaaS Economics Mastery

### The Essential Economics Framework

1. **Unit Economics Must Work**: LTV > 3x CAC minimum

2. **Cohorts Reveal Truth**: Aggregate metrics hide problems

3. **Cash ≠ Revenue**: Manage both separately

4. **Forecasting is Iterative**: Update monthly, learn from variance

5. **Funding Fits Strategy**: Bootstrap or raise based on market and goals

### Key Formulas Reference

```
LTV = ARPA × Gross Margin / Monthly Churn Rate
CAC = Sales & Marketing Spend / New Customers
LTV:CAC = LTV / CAC (target: >3:1)
Payback = CAC / (ARPA × Gross Margin) in months
NRR = (Starting - Churn - Contraction + Expansion) / Starting
Quick Ratio = (New + Expansion) / (Churn + Contraction)
Burn Multiple = Net Burn / Net New ARR
Runway = Cash / Monthly Net Burn
```

### Red Flags to Watch

- LTV:CAC < 3:1 without clear path to improvement
- Payback > 18 months
- NRR < 90%
- Cohorts getting worse over time
- Burn multiple > 3x consistently
- Runway < 6 months without funding plan

---

*Next: [Product-Led Growth Fundamentals](../product-led-growth/plg-fundamentals.md)*
