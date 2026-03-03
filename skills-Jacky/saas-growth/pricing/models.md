# Pricing Models

## Introduction

Choosing the right pricing model is one of the most consequential decisions in SaaS. The model you choose affects everything: customer acquisition, expansion revenue, churn patterns, sales motions, and company valuation. There's no universally "best" model—the right choice depends on your product, market, and strategy.

This guide covers the major SaaS pricing models: per-seat, usage-based, flat-rate, tiered, and hybrid approaches, with guidance on when to use each.

---

## 1. Per-Seat Pricing

### How It Works

Charge based on number of users:
```
Monthly Cost = Number of Users × Per-Seat Price

Example: 10 users × $20/seat = $200/month
```

### Per-Seat Variations

**Pure Per-Seat:**
- Every user pays
- Simple calculation
- Linear scaling

**Tiered Per-Seat:**
- Price per seat decreases with volume
- 1-10 users: $30/seat
- 11-50 users: $25/seat
- 51+ users: $20/seat

**Minimum Seats:**
- Minimum payment regardless of users
- "$50/month for up to 5 users, $10/seat after"
- Ensures minimum revenue

**Named vs. Concurrent:**
- Named: Each user has account
- Concurrent: Licenses shared
- Concurrent is less common in modern SaaS

### When Per-Seat Works

**✓ Good Fit:**
- Collaboration tools (more users = more value)
- Communication platforms
- CRMs (each rep needs access)
- Project management
- HR systems

**✗ Poor Fit:**
- Individual productivity tools
- API/infrastructure products
- Products with varying usage intensity
- Products where one user serves many

### Per-Seat Advantages

**Predictable Revenue:**
- Easy to forecast
- Grows with customer team size
- Natural expansion as companies hire

**Simple to Understand:**
- Customers know the cost
- Easy budget planning
- No surprise bills

**Expansion Built-In:**
- Team growth = revenue growth
- Natural land and expand
- Aligned with customer success

### Per-Seat Challenges

**Seat Counting Games:**
- Customers minimize seats
- Shared logins
- Inactive seat bloat
- Procurement pushback

**Value Mismatch:**
- Power user vs. occasional user
- Same price, different value
- Can feel unfair

**Churn Correlation:**
- Layoffs = immediate revenue loss
- Economic sensitivity
- No usage buffer

### Per-Seat Examples

| Company | Per-Seat Price | Notes |
|---------|---------------|-------|
| Slack | $8.75-15/user/mo | Standard & Plus tiers |
| Salesforce | $25-300/user/mo | Many tiers |
| Asana | $11-25/user/mo | Premium & Business |
| Notion | $8-15/member/mo | Plus & Business |
| Figma | $12-45/editor/mo | Viewers free |

### Per-Seat Best Practices

**1. Free Viewers/Limited Roles**
- Charge for full users
- Free for view-only
- Expands adoption, captures value

**2. Activity-Based Definitions**
- "Active users" not "named users"
- Fair for occasional access
- Reduces seat-counting games

**3. Volume Discounts**
- Reward larger deployments
- Competitive at scale
- Simplify enterprise deals

**4. Bundle Minimums**
- Team minimum (5+ seats)
- Ensures viable deals
- Positions for teams

---

## 2. Usage-Based Pricing

### How It Works

Charge based on consumption:
```
Monthly Cost = Usage Volume × Per-Unit Price

Example: 50,000 API calls × $0.001 = $50/month
```

### Usage Metrics by Category

| Category | Common Metrics |
|----------|---------------|
| Infrastructure | Compute hours, storage GB, bandwidth |
| API | Requests, calls, transactions |
| Communication | Messages, minutes, contacts |
| Data | Events, rows, queries |
| Marketing | Emails sent, contacts, impressions |

### Usage Pricing Structures

**Linear Usage:**
```
Price = Units × Rate
10,000 events × $0.01 = $100
```

**Tiered Usage (Volume Discount):**
```
First 10,000: $0.01 each = $100
Next 50,000: $0.008 each = $400
Next 100,000: $0.005 each = $500
Total: 160,000 events = $1,000
```

**Step Function:**
```
0-10,000: $50/month (fixed)
10,001-50,000: $200/month (fixed)
50,001-200,000: $500/month (fixed)
```

**Committed Usage:**
```
Commit to $500/month usage → 20% discount
Overage: List price
```

### When Usage-Based Works

**✓ Good Fit:**
- API products (clear unit = call)
- Infrastructure (compute, storage)
- Transactional products (payments, messages)
- Data products (events, records)
- Products with highly variable usage

**✗ Poor Fit:**
- Collaboration tools
- Products with no clear usage metric
- Products where usage doesn't scale with value
- Customers needing predictable costs

### Usage-Based Advantages

**Perfect Value Alignment:**
- Pay for what you use
- Natural expansion
- Low barrier to start

**Expansion Revenue:**
- Revenue grows with customer growth
- No upsell conversation needed
- Strong NRR potential

**Lower Entry Barrier:**
- Start small, scale up
- Easier lands
- Good for SMB → Enterprise

### Usage-Based Challenges

**Revenue Unpredictability:**
- Seasonal variation
- Economic sensitivity
- Harder to forecast

**Bill Shock Risk:**
- Unexpected large bills
- Customer anger
- Churn from cost concerns

**Customer Budgeting:**
- Hard to forecast costs
- Procurement challenges
- May prefer fixed pricing

### Usage-Based Examples

| Company | Usage Metric | Pricing |
|---------|-------------|---------|
| Twilio | Messages/calls | ~$0.0075/SMS |
| Stripe | Transactions | 2.9% + $0.30 |
| Snowflake | Credits (compute) | ~$2-3/credit |
| AWS | Many metrics | Various |
| OpenAI | Tokens | $0.002-0.06/1K tokens |

### Usage-Based Best Practices

**1. Clear Unit Definition**
- Easy to understand
- Easy to measure
- Predictable

**2. Usage Dashboard**
- Real-time visibility
- Forecast tools
- No surprises

**3. Spending Alerts**
- 50%, 80%, 100% notifications
- Optional hard caps
- Customer control

**4. Committed-Use Options**
- Annual commitments for discount
- Predictability for customers
- Cash flow for you

---

## 3. Flat-Rate Pricing

### How It Works

Single price for the product:
```
Monthly Cost = Fixed Amount

Example: $99/month for everything
```

### Flat-Rate Variations

**Simple Flat:**
- One price, one product
- No tiers, no limits
- Take it or leave it

**Annual Flat:**
- Monthly equivalent price
- Annual payment required
- Volume discount implied

**Per-Product Flat:**
- Multiple products
- Each with flat price
- Bundle available

### When Flat-Rate Works

**✓ Good Fit:**
- Simple, focused products
- Individual users
- Clear value proposition
- Commodity markets

**✗ Poor Fit:**
- Variable value by customer
- Wide customer size range
- Complex products
- Enterprise sales needed

### Flat-Rate Advantages

**Ultimate Simplicity:**
- One price to remember
- No calculator needed
- No comparison complexity

**Easy to Sell:**
- No configuration needed
- Quick decision
- Self-serve friendly

**Predictable:**
- Customer knows exact cost
- Easy budgeting
- No surprises

### Flat-Rate Challenges

**Leaves Money on Table:**
- Enterprise pays same as startup
- Power users pay same as basic
- No value capture

**No Expansion Revenue:**
- Growth requires new customers
- No upsell path
- Lower LTV

**May Not Fit All:**
- Too expensive for small
- Too cheap for large
- One-size-fits-none risk

### Flat-Rate Examples

| Company | Flat Price | Notes |
|---------|-----------|-------|
| Basecamp | $99/mo flat | Unlimited users |
| Carrd | $19/year | Personal plan |
| Some indie SaaS | $X/month | Simplicity focused |

### Flat-Rate Best Practices

**1. Have "Flat" Not "Only"**
- Flat option for simplicity
- Usage option for scale
- Enterprise for large

**2. Generous Limits**
- Make flat feel abundant
- Don't nickel-and-dime
- Compete on simplicity

**3. Position as Anti-Complexity**
- Market against confusing pricing
- Attract decision-fatigued buyers
- Clear value proposition

---

## 4. Tiered Pricing

### How It Works

Multiple packages at different price points:
```
Starter: $29/month - Basic features
Pro: $99/month - More features
Enterprise: $299/month - All features
```

### Tiered Pricing Structures

**Good-Better-Best (3 Tiers):**
- Starter/Basic: Entry-level
- Pro/Growth: Target tier (most choose)
- Business/Enterprise: Full feature set

**Four-Tier:**
- Free: Limited functionality
- Starter: Paid entry point
- Pro: Full self-serve
- Enterprise: Custom

**Five+ Tiers:**
- Granular segmentation
- Multiple price points
- Complexity risk

### When Tiered Works

**✓ Good Fit:**
- Most B2B SaaS
- Wide customer range
- Clear feature differentiation
- Mix of self-serve and sales

**✗ Poor Fit:**
- Simple products
- Commodity offerings
- Pure usage products
- Very narrow market

### Tiered Advantages

**Capture Different Segments:**
- SMB on Starter
- Mid-Market on Pro
- Enterprise on custom
- Something for everyone

**Natural Upgrade Path:**
- Start small, grow up
- Clear next tier
- Expansion built-in

**Pricing Power:**
- Anchor with high tier
- Middle tier seems reasonable
- Psychological positioning

### Tiered Challenges

**Complexity:**
- Many options to compare
- Decision paralysis
- Harder to explain

**Cannibalization:**
- Lower tier too good
- Higher tier not compelling
- Wrong tier distribution

**Feature Allocation:**
- What goes where?
- Feature disputes
- Constant rebalancing

### Creating Effective Tiers

**The 40-40-20 Rule:**
```
Target distribution:
- Starter: 40% of customers
- Pro: 40% of customers  
- Enterprise: 20% of customers
```

If distribution is off:
- Too many in Starter → Starter too good or Pro too expensive
- Too few in Enterprise → Enterprise not differentiated

**Tier Differentiation:**

| Factor | Starter | Pro | Enterprise |
|--------|---------|-----|------------|
| Features | Core only | Core + Advanced | All |
| Limits | Low | Medium | High/Unlimited |
| Support | Self-serve | Email | Dedicated |
| Users | 1-3 | 10 | Unlimited |
| Price | $29 | $99 | $299+ |

### Tiered Examples

**Mailchimp:**
- Free: 500 contacts
- Essentials: $13/mo, 500+ contacts
- Standard: $20/mo, advanced automation
- Premium: $350/mo, enterprise features

**Slack:**
- Free: Limited history
- Pro: $8.75/user, unlimited
- Business+: $15/user, compliance
- Enterprise Grid: Custom

**Notion:**
- Free: Personal
- Plus: $8/member, team
- Business: $15/member, advanced
- Enterprise: Custom

### Tiered Best Practices

**1. Design for Middle Tier**
- Most customers should land here
- Best value perception
- Highest margin

**2. Make Tiers Distinct**
- Clear differences
- Not just "more of same"
- Compelling upgrade reasons

**3. Name Tiers Meaningfully**
- Reflect customer stage
- Not just "Tier 1, 2, 3"
- "Startup, Growth, Scale"

**4. Show Comparison**
- Easy feature comparison
- Highlight differences
- Guide decision

---

## 5. Hybrid Models

### Combining Pricing Elements

Most successful SaaS uses hybrid approaches:

**Base + Usage:**
```
$99/month base + $0.10 per action
```

**Per-Seat + Tiers:**
```
Pro: $20/user (features A, B)
Enterprise: $40/user (features A, B, C, D)
```

**Tier + Overage:**
```
Pro: $99/month includes 10,000 events
Overage: $0.01/event
```

### Hybrid Examples

**HubSpot:**
- Tiered products (Marketing, Sales, Service)
- Per-seat for Sales
- Contact-based for Marketing
- Platform bundles

**Intercom:**
- Seat-based core
- Usage components (MAU, resolutions)
- Tier features

**Datadog:**
- Host-based (infrastructure)
- Plus usage (logs, APM)
- Tier add-ons

### When to Go Hybrid

**Signals You Need Hybrid:**
- Single metric doesn't capture value
- Different segments need different models
- Usage is highly variable
- Base value + variable value

**Design Hybrid Carefully:**
- Don't over-complicate
- Keep primary metric clear
- Secondary metrics should be simple

### Hybrid Best Practices

**1. Primary + Secondary**
```
Primary: Per-seat ($X/user)
Secondary: Usage overage ($Y/event over limit)

Not: Per-seat + usage + features + support + storage + API
```

**2. Clear Base Value**
```
"$99/month includes 5 users and 10,000 events.
Additional users $15/each, additional events $0.01/each."
```

**3. Reasonable Defaults**
- Most customers should stay within base
- Overages for edge cases
- Not designed to trap

---

## 6. Choosing Your Model

### Decision Framework

| Question | If Yes → Model |
|----------|----------------|
| Value scales with users? | Per-seat |
| Value scales with usage? | Usage-based |
| Simple product, one use case? | Flat-rate |
| Variable customer sizes/needs? | Tiered |
| Multiple value dimensions? | Hybrid |

### Model by Product Type

| Product Type | Typical Model |
|--------------|---------------|
| Collaboration | Per-seat |
| Infrastructure/API | Usage |
| Simple tool | Flat or tiered |
| Platform/suite | Tiered + seat |
| Data/analytics | Usage or tiered |
| Marketing | Contacts + features |

### Model by Stage

**Early Stage (Finding PMF):**
- Keep it simple
- Easy to explain
- Easy to change

**Growth Stage (Scaling):**
- Add tiers for segments
- Introduce usage for expansion
- Optimize for retention

**Mature Stage (Efficiency):**
- Sophisticated hybrid
- Enterprise customization
- Usage for expansion revenue

### Transitioning Models

**When to Change:**
- Current model not capturing value
- Customer feedback indicates mismatch
- Competitive pressure
- New segment needs

**How to Transition:**
- Grandfather existing customers
- New customers on new model
- Offer migration path
- Communicate clearly

---

## Summary: Pricing Model Selection

### Model Comparison

| Model | Complexity | Expansion | Predictability | Best For |
|-------|-----------|-----------|----------------|----------|
| Per-Seat | Low | High | High | Collaboration |
| Usage | Medium | Very High | Low | Infrastructure |
| Flat | Very Low | None | Very High | Simple tools |
| Tiered | Medium | Medium | High | Most B2B SaaS |
| Hybrid | High | High | Medium | Complex platforms |

### Key Takeaways

1. **Match model to value**: How customers derive value determines model
2. **Start simple, add complexity**: Don't over-engineer early
3. **Plan for expansion**: Model should enable revenue growth
4. **Consider customer experience**: Predictability matters
5. **Review regularly**: Model should evolve with business

---

*Next: [Packaging](./packaging.md)*
