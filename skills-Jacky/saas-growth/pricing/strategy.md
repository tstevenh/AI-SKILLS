# Pricing Strategy

## Introduction

Pricing is one of the most powerful levers in SaaS, yet most founders underprice and underinvest in pricing strategy. A 1% improvement in pricing has a bigger impact on profits than a 1% improvement in customer acquisition or retention. Yet companies often spend months on product features and minutes on pricing.

This guide covers the fundamental approaches to SaaS pricing strategy: value-based pricing, competitor-based pricing, cost-plus pricing, willingness-to-pay research, and pricing experiments.

---

## 1. Value-Based Pricing

### The Foundation of SaaS Pricing

**Value-Based Pricing:** Setting prices based on the value delivered to customers, not based on costs or competitors.

**Core Principle:**
```
Price = f(Customer Value) 

Not: Price = Cost + Margin
Not: Price = Competitor Price - 10%
```

### Why Value-Based Pricing Works

**1. Captures More Value**

If your product saves a customer $10,000/month, charging $100/month leaves $9,900 on the table. Charging $1,000/month captures 10% of value—still a great deal for the customer.

**2. Aligns with Customer Success**

When price correlates with value:
- Customers who get more value, pay more
- Customers who get less value, pay less
- Natural alignment of incentives

**3. Creates Pricing Power**

Differentiated value justifies premium pricing:
- Less price comparison shopping
- Customers buy value, not features
- Sustainable pricing position

### Implementing Value-Based Pricing

**Step 1: Understand Customer Value**

Quantify the value your product creates:

**Economic Value:**
- Revenue increased
- Costs reduced
- Time saved
- Risk mitigated

**Example Calculation:**
```
Marketing Automation Tool:

Without tool:
- Marketer salary: $80,000/year
- Time on manual tasks: 40%
- Cost of manual time: $32,000/year

With tool:
- Time on manual tasks: 10%
- Cost of manual time: $8,000/year
- Time savings: $24,000/year

Additional value:
- Better targeting → 15% more conversions
- Revenue impact: $50,000/year

Total value: $74,000/year
10% value capture: $7,400/year ($617/month)
```

**Step 2: Segment by Value**

Different customers get different value:

| Segment | Value Delivered | Willingness to Pay |
|---------|-----------------|-------------------|
| Startup | Saves 5 hrs/month | $50-100/month |
| SMB | Saves 20 hrs/month | $200-500/month |
| Enterprise | Saves 100 hrs/month | $1,000-3,000/month |

**Step 3: Create Pricing Tiers Aligned to Value**

```
Starter: $49/month
- For small teams
- Basic features
- Saves 5+ hours/month

Growth: $199/month  
- For growing companies
- Advanced features
- Saves 20+ hours/month

Enterprise: $999/month
- For large organizations
- Full platform
- Saves 100+ hours/month
```

### Value Metrics

**What's a Value Metric?**

The unit of measurement that scales with customer value:
- Users/seats (value scales with team)
- Contacts/records (value scales with data)
- Revenue processed (value scales with volume)
- Actions/API calls (value scales with usage)

**Good Value Metrics:**

| Product | Value Metric | Why It Works |
|---------|--------------|--------------|
| Slack | Users | More users = more collaboration value |
| Mailchimp | Contacts | More contacts = more marketing reach |
| Stripe | Revenue processed | More revenue = more payment value |
| Twilio | Messages/calls | More communication = more value |
| Segment | Events tracked | More data = more insights |

**Choosing Your Value Metric:**

| Criteria | Question |
|----------|----------|
| Aligned | Does more of this = more value? |
| Understandable | Can customers easily explain it? |
| Predictable | Can customers forecast usage? |
| Growable | Does it naturally grow over time? |
| Measurable | Can you accurately track it? |

---

## 2. Competitor-Based Pricing

### Understanding Competitive Positioning

**Competitor-Based Pricing:** Setting prices relative to competing alternatives.

**When It Makes Sense:**
- Commodity markets with many alternatives
- Clear substitute products exist
- Buyers actively compare
- New entrants needing market reference

### Competitive Positioning Options

**1. Premium Pricing (Above Market)**

Price higher than competitors:
```
Competitor A: $100/month
Competitor B: $80/month
Your Price: $150/month

Positioning: Better quality, more features, superior support
```

**Requirements:**
- Clear differentiation
- Demonstrated superior value
- Strong brand/reputation
- Customers willing to pay more

**Examples:**
- Salesforce vs. cheaper CRMs
- Zoom vs. free alternatives
- HubSpot vs. basic tools

**2. Market Rate Pricing (At Market)**

Price similar to competitors:
```
Competitor A: $100/month
Competitor B: $80/month
Your Price: $90/month

Positioning: Comparable value, different strengths
```

**Requirements:**
- Some differentiation
- Competitive features
- Viable unit economics

**3. Penetration Pricing (Below Market)**

Price lower than competitors:
```
Competitor A: $100/month
Competitor B: $80/month
Your Price: $40/month

Positioning: Same value, lower cost
```

**Requirements:**
- Lower cost structure
- Scale advantages
- Plan to raise prices later
- Or freemium/usage-based model

**Risks:**
- Race to bottom
- Attracts price-sensitive customers
- Hard to raise prices
- May signal lower quality

### Competitive Pricing Analysis

**Step 1: Map Competitors**

| Competitor | Pricing Model | Price Range | Key Features |
|------------|---------------|-------------|--------------|
| Competitor A | Per seat | $10-30/user/mo | Feature X, Y |
| Competitor B | Tiered | $49-299/mo | Feature Y, Z |
| Competitor C | Usage | $0.01/action | Feature X, Z |

**Step 2: Analyze Positioning**

```
                    Price
                      ↑
                      │     Premium
           High │     │  ● Enterprise Tools
                │     │
                │     ● Your target position?
                │     │
                │  ● You today
                │     │
            Low │  ●  │  Budget Tools
                └─────┴─────────────────→
                   Low          High
                        Features/Value
```

**Step 3: Find Your Position**

Questions to ask:
- Where are we differentiated?
- Who competes for our customers?
- What justifies premium/discount?
- Where is whitespace?

### Competitive Pricing Pitfalls

**❌ Copying Without Context**

Just because competitor charges $99 doesn't mean you should:
- Their costs differ
- Their value proposition differs
- Their target customer differs

**❌ Race to Bottom**

Competing only on price:
- Erodes margins
- Attracts worst customers
- Creates commoditization
- Rarely sustainable

**❌ Ignoring Alternatives**

Competitors aren't just similar products:
- Spreadsheets
- Manual processes
- In-house tools
- Different solution categories

---

## 3. Cost-Plus Pricing

### The Traditional Approach

**Cost-Plus Pricing:** Price = Costs + Desired Margin

```
Cost per customer: $20/month
Desired margin: 80%
Price: $20 / (1 - 0.80) = $100/month
```

### Why Cost-Plus Is Problematic for SaaS

**1. Costs Are Often Low**

Software marginal costs are near zero:
- Hosting: Pennies per user
- Support: Minimal for self-serve
- No COGS like physical products

**2. Ignores Value**

A $1 cost product might deliver $1,000 value:
- Cost-plus: $5 (5x markup)
- Value-based: $100 (10% value capture)
- Leaving $95 on the table

**3. Doesn't Differentiate**

All competitors have similar costs:
- SaaS infrastructure commoditized
- Costs converge
- No pricing differentiation

### When Cost-Plus Has a Role

**Infrastructure Products:**
- Usage-based infrastructure
- Clear marginal costs
- Customer cost expectations

**Floor Setting:**
```
Minimum price = Costs / (1 - Minimum Margin)

If costs = $10 and minimum margin = 60%:
Floor price = $10 / 0.40 = $25

Price can't go below $25 without losing money.
```

**Internal Budgeting:**
- Understanding cost structure
- Setting profitability targets
- Capacity planning

---

## 4. Willingness-to-Pay Research

### Why Research Willingness to Pay

**The Problem:**
- You think product is worth $100
- Customers might pay $300
- Or they might only pay $50
- Without research, you're guessing

**The Solution:**
Research what customers will actually pay.

### Research Methods

**1. Van Westendorp Price Sensitivity Meter**

Ask four questions:
1. At what price would this be **too cheap** (quality concerns)?
2. At what price is this a **bargain** (great deal)?
3. At what price is this **getting expensive** (but still consider)?
4. At what price is this **too expensive** (wouldn't buy)?

**Analysis:**
Plot cumulative distributions of each answer:
- "Too cheap" and "Too expensive" intersect at **optimal price point**
- "Bargain" and "Expensive" create **acceptable range**

```
100% ┼─────────────────────────────────
     │╲   Too Cheap        Too Expensive╱│
     │ ╲                              ╱  │
 50% │  ╲      ●───Optimal Price───●╱   │
     │   ╲    ╱                   ╱      │
     │    ╲  ╱                   ╱       │
  0% │     ╲╱___________________╱        │
     └───────────────────────────────────┘
         $25   $50   $75   $100  $125
```

**2. Gabor-Granger Method**

Ask directly about purchase intent at prices:
1. Would you buy at $50/month? [Yes/No]
2. (If yes) Would you buy at $75/month? [Yes/No]
3. (If no to 1) Would you buy at $25/month? [Yes/No]

**Analysis:**
Create demand curve from responses.

```
Purchase Intent:
100% │████
     │████████
 50% │████████████
     │████████████████
  0% │████████████████████
     └────────────────────────
        $25  $50  $75  $100  $125
```

**3. Conjoint Analysis**

Show product configurations with prices, ask preferences:

```
Option A:                 Option B:
- Feature X               - Feature X
- Feature Y               - Feature Z  
- 10 users                - 25 users
- $99/month               - $149/month

Which would you choose? [A] [B]
```

**Analysis:**
Statistical analysis reveals:
- Relative value of features
- Price sensitivity
- Optimal bundle configurations

**4. Direct Questions (With Caution)**

Simple but unreliable:
- "What would you pay for this?"
- "Is $X a fair price?"

**Problems:**
- Hypothetical ≠ actual behavior
- Anchoring effects
- Social desirability bias

**Better Framing:**
- "Compared to [alternative], how much more/less would you pay?"
- "What would you pay for [specific outcome]?"
- "What's your budget for solving [problem]?"

### Conducting WTP Research

**Sample Size:**
- Van Westendorp: 100-200 responses
- Gabor-Granger: 200-400 responses
- Conjoint: 300-500 responses

**Segmentation:**
Run analysis by segment:
- Company size
- Use case
- Industry
- Geography

Different segments have different WTP.

**Timing:**
- Before major pricing changes
- Before new product launch
- Annually for pricing review
- When entering new segments

### Research to Pricing

**Example Output:**

Van Westendorp results:
- Optimal price: $79/month
- Acceptable range: $49-129/month
- Segment A: Optimal $99
- Segment B: Optimal $59

**Pricing Decision:**
- Set standard price at $79
- Create "Starter" tier at $49 for Segment B
- Create "Pro" tier at $99 for Segment A
- Test $129 for premium/enterprise

---

## 5. Pricing Experiments

### Why Run Pricing Experiments

**The Truth:** You don't know the optimal price. Test to find out.

**What You Can Test:**
- Price points
- Tier structures
- Feature allocation
- Billing frequency discounts
- Value metrics

### Types of Pricing Experiments

**1. A/B Testing Prices**

Show different prices to different users:
- Control: $99/month
- Variant: $129/month

**Measurement:**
- Conversion rate
- Revenue per visitor
- Downstream metrics (retention, LTV)

**Considerations:**
- Ethical concerns (fairness)
- Legal concerns (some jurisdictions)
- Can cause backlash if discovered

**Best Practice:**
- Test on new visitors only
- Consider geographic segmentation
- Be transparent about testing
- Grandfather existing customers

**2. Sequential Testing**

Change price, measure, iterate:
- Week 1-4: $99/month
- Week 5-8: $129/month
- Week 9-12: $109/month

**Challenges:**
- External factors confound
- Takes longer
- Seasonality effects

**3. Geographic Price Testing**

Different prices by region:
- US: $129/month
- EU: €99/month
- LATAM: $49/month

**Benefits:**
- Natural segmentation
- PPP considerations
- Different competitive landscapes

**4. Tier/Package Testing**

Test different packaging:
- Control: 3 tiers (Free, Pro, Enterprise)
- Variant: 4 tiers (Free, Basic, Pro, Enterprise)

**Measure:**
- Overall conversion
- Tier distribution
- Revenue per customer

**5. Feature Allocation Testing**

Test which features in which tier:
- Control: Feature X in Pro tier
- Variant: Feature X in Free tier

**Measure:**
- Free → Paid conversion
- Feature adoption
- Overall revenue impact

### Pricing Experiment Best Practices

**1. Define Success Metrics**

```
Primary: Revenue per visitor
Secondary: Conversion rate, LTV, Churn
Guardrails: Customer satisfaction, support tickets
```

**2. Calculate Sample Size**

```
Need statistical significance:
- Current conversion: 5%
- Minimum detectable effect: 20% relative change
- Significance: 95%
- Power: 80%

Sample needed: ~2,000 per variant
```

**3. Run Long Enough**

- Minimum 2 weeks (weekly cycles)
- Account for decision time
- Include renewal periods for retention impact

**4. Segment Analysis**

Price changes affect segments differently:
- SMB might be more price sensitive
- Enterprise might not care
- Analyze by segment

**5. Consider Long-Term**

Higher price might:
- Reduce conversion but increase quality
- Increase initial churn but improve long-term retention
- Look beyond immediate metrics

### Interpreting Results

**Scenario Analysis:**

| Metric | $99 | $129 | Winner |
|--------|-----|------|--------|
| Conversion | 5% | 4% | $99 |
| Revenue/visitor | $4.95 | $5.16 | $129 |
| 90-day LTV | $250 | $290 | $129 |
| Customer satisfaction | 4.5 | 4.3 | $99 |

**Decision:** $129 wins on revenue metrics, but satisfaction is lower. Investigate why and whether it's acceptable.

---

## Summary: Pricing Strategy Framework

### The Strategic Pricing Process

```
1. Understand Value Delivered
   └→ Quantify customer ROI
   └→ Identify value metric

2. Research Willingness to Pay
   └→ Van Westendorp / Conjoint
   └→ Segment analysis

3. Analyze Competition
   └→ Map competitive landscape
   └→ Define positioning

4. Design Pricing Structure
   └→ Tiers and packaging
   └→ Price points

5. Test and Iterate
   └→ A/B tests
   └→ Continuous optimization
```

### Pricing Strategy Checklist

**Value Understanding:**
- [ ] Customer ROI quantified
- [ ] Value metric identified
- [ ] Segments defined by value

**Research:**
- [ ] WTP research conducted
- [ ] Segment-level insights
- [ ] Competitive analysis complete

**Pricing Design:**
- [ ] Tiers aligned to value
- [ ] Price points tested
- [ ] Model matches customer needs

**Execution:**
- [ ] Pricing page optimized
- [ ] Sales team trained
- [ ] Metrics tracking in place

### Key Principles

1. **Price to value, not cost**: Capture portion of value delivered
2. **Segment thoughtfully**: Different customers, different prices
3. **Test continuously**: Pricing is never "done"
4. **Communicate value**: Price is only half—articulating value is the other half
5. **Review regularly**: Annual pricing review minimum

---

*Next: [Pricing Models](./models.md)*
