# SaaS Business Models

## Introduction to SaaS Business Models

Software as a Service (SaaS) has revolutionized how software is delivered, purchased, and consumed. Unlike traditional software with one-time license fees, SaaS operates on recurring revenue models where customers pay ongoing fees to access software hosted in the cloud. This fundamental shift has created entirely new business dynamics, metrics, and growth strategies.

Understanding SaaS business models isn't just academic—it directly impacts every decision you make from pricing to product development to go-to-market strategy. The model you choose shapes your unit economics, determines your growth constraints, and influences your competitive positioning.

This section provides a comprehensive exploration of SaaS business models, from foundational subscription models to emerging hybrid approaches.

---

## 1. Subscription Models Explained

### The Foundation of SaaS Revenue

Subscription models form the bedrock of SaaS businesses. Instead of a single large transaction, customers pay recurring fees—typically monthly or annually—to access the software. This creates predictable, recurring revenue (the holy grail of business models) while aligning vendor and customer incentives around ongoing value delivery.

### Monthly vs. Annual Subscriptions

**Monthly Subscriptions**

Monthly billing offers customers flexibility and lower upfront commitment:

- **Lower barrier to entry**: Customers can try your product without a large financial commitment
- **Faster feedback loops**: You learn quickly if customers don't find value (they cancel)
- **Cash flow challenges**: Revenue comes in smaller, spread-out increments
- **Higher churn risk**: Easy come, easy go—customers can leave at any time
- **Higher payment processing costs**: More transactions = more fees

Monthly subscriptions work best for:
- Products with quick time-to-value
- Lower price points ($50/month or less)
- Markets with price-sensitive customers
- Early-stage products still proving value
- Consumer or prosumer SaaS

**Annual Subscriptions**

Annual contracts provide upfront cash and increased commitment:

- **Improved cash flow**: Get 12 months of revenue immediately
- **Lower effective churn**: Customers commit for a full year
- **Reduced administrative overhead**: One invoice, one payment per year
- **Discount expectations**: Customers expect 15-35% off for annual commitment
- **Longer feedback cycles**: Takes a year to know if customers will renew

Annual subscriptions work best for:
- Products requiring implementation or onboarding
- Higher price points ($500/month and above)
- Enterprise customers with annual budgeting cycles
- Products where value compounds over time
- Businesses needing upfront capital

**The Hybrid Approach**

Most successful SaaS companies offer both monthly and annual options:

| Billing Cycle | Typical Discount | Best Customer Segment |
|--------------|------------------|----------------------|
| Monthly | 0% (full price) | SMB, trial converts, uncertain |
| Annual | 15-20% off | Committed SMB, confident users |
| Annual Prepaid | 25-35% off | Enterprise, budget-conscious |
| Multi-Year | 35-50% off | Enterprise, strategic accounts |

**Conversion Strategy**: Start customers on monthly, then use lifecycle emails and in-app prompts to encourage annual upgrades. Offer "exclusive" annual discounts to high-engagement monthly users.

### Subscription Billing Mechanics

**Billing Date Logic**

Two primary approaches:

1. **Anniversary Billing**: Charge on the same day each period (e.g., always the 15th)
   - Simpler to understand
   - Complications: What about February 30th?
   
2. **Calendar Billing**: Charge on the 1st of each month
   - Easier forecasting
   - Requires proration for mid-month starts

**Proration**

When customers upgrade, downgrade, or start mid-cycle:

```
Prorated Amount = (Days Remaining / Total Days in Period) × New Plan Price
Credit = (Days Remaining / Total Days in Period) × Old Plan Price
Net Charge = Prorated Amount - Credit
```

Example: Customer on $100/month plan upgrades to $200/month on day 15 of a 30-day period:
- Credit: (15/30) × $100 = $50
- New charge: (15/30) × $200 = $100
- Net charge: $100 - $50 = $50

**Billing Tools**

- **Stripe Billing**: Most popular for startups, excellent API
- **Chargebee**: More features, better for complex scenarios
- **Recurly**: Strong dunning and retention features
- **Paddle**: Merchant of record (handles taxes)
- **FastSpring**: Similar to Paddle, good for B2C
- **Zuora**: Enterprise-grade, complex pricing needs

### Subscription Tiers

Most SaaS products offer multiple subscription tiers (see Pricing section for deep dive). Common structures:

**Three-Tier Model (Most Common)**
1. **Starter/Basic**: Entry-level, core features
2. **Professional/Growth**: Most features, target segment
3. **Enterprise/Scale**: All features, premium support

**Four-Tier Model**
1. **Free**: Feature-limited or usage-limited
2. **Starter**: Paid entry point
3. **Professional**: Target tier
4. **Enterprise**: Custom pricing, maximum features

**Usage + Tier Hybrid**
- Base subscription tier
- Usage charges on top (API calls, storage, seats)

---

## 2. Usage-Based Pricing

### The Rise of Consumption Models

Usage-based pricing (UBP), also called consumption-based or pay-as-you-go pricing, charges customers based on actual product usage rather than a flat subscription fee. This model has grown dramatically, now representing 45%+ of SaaS companies in some form.

### Why Usage-Based Pricing Works

**For Customers:**
- **Fair pricing**: Pay only for what you use
- **Low barrier to entry**: Start small, scale as needed
- **No shelfware**: Unused licenses don't cost money
- **Budget flexibility**: Costs scale with business activity

**For SaaS Companies:**
- **Natural expansion revenue**: Revenue grows as customers grow
- **Lower acquisition barriers**: Easier to land new accounts
- **Better price-value alignment**: Price reflects value delivered
- **Reduced churn discussions**: Usage drops before cancellation (early warning)

### Usage-Based Pricing Models

**Pure Usage-Based**

100% of revenue comes from usage, no base fee:
- AWS (compute hours, storage)
- Twilio (per message, per minute)
- Stripe (percentage of transactions)

**Usage + Platform Fee**

Minimum monthly commitment plus usage charges:
- Snowflake (storage + compute)
- Datadog (host-based + features)
- MongoDB Atlas (base + usage)

**Tiered Usage**

Usage charges decrease at higher volumes:
- Tier 1: First 1,000 API calls at $0.01 each
- Tier 2: Next 10,000 calls at $0.008 each
- Tier 3: Beyond 11,000 at $0.005 each

**Usage Credits**

Pre-purchased credits that don't expire (or expire annually):
- OpenAI API credits
- Google Cloud credits
- Beneficial for cash flow, creates commitment

### Choosing the Right Usage Metric

The usage metric (or value metric) is arguably the most important pricing decision for usage-based companies. The ideal metric:

1. **Correlates with value**: More usage = more value for customer
2. **Scales with customer growth**: Enterprise pays more than startup
3. **Easy to understand**: Customers can predict/control costs
4. **Easy to measure**: Accurate, real-time tracking
5. **Hard to game**: Can't artificially reduce usage

**Common Usage Metrics by Category:**

| Category | Common Metrics |
|----------|---------------|
| Infrastructure | Compute hours, storage GB, bandwidth |
| API/Developer | API calls, requests, transactions |
| Communication | Messages sent, minutes, contacts reached |
| Data/Analytics | Rows synced, queries, events tracked |
| Sales/Marketing | Contacts, emails sent, leads scored |
| Collaboration | Seats, active users, storage |

**Testing Your Metric:**

Ask these questions:
1. Does the metric grow as customers get more value?
2. Can customers easily understand and predict their bill?
3. Is the metric stable enough for budgeting?
4. Does it create a land-and-expand motion?

### Usage-Based Pricing Challenges

**Revenue Predictability**

Usage revenue can be volatile:
- Seasonal businesses have seasonal usage
- Economic downturns reduce consumption
- Makes forecasting harder
- Investors may apply lower revenue multiples

**Mitigation strategies:**
- Minimum commitments (use-or-lose)
- Annual contracts with committed usage
- Hybrid models with base fee
- Building usage forecasts from customer data

**Bill Shock**

Customers can accidentally run up large bills:
- No spending limits by default
- Unexpected usage spikes
- Development environments left running

**Mitigation strategies:**
- Spending alerts at 50%, 80%, 100% of typical usage
- Hard spending caps (optional)
- Clear cost calculators
- Detailed usage dashboards
- Budget prediction tools

**Customer Budgeting**

Procurement teams prefer predictable costs:
- Annual budgets need fixed numbers
- Variable costs are harder to approve
- Finance teams may push back

**Mitigation strategies:**
- Committed-use discounts
- Annual contracts with overage rates
- Hybrid models with predictable base

### Implementing Usage-Based Pricing

**Technical Requirements:**

1. **Usage Tracking**: Accurate, real-time metering of the usage metric
2. **Rating Engine**: Converting raw usage into charges
3. **Billing Integration**: Invoicing based on usage
4. **Customer Dashboard**: Real-time usage visibility
5. **Alerts System**: Notifications for usage milestones

**Data Architecture:**

```
Usage Event → Event Store → Aggregation → Rating → Invoice
     ↓
Customer Dashboard ← Real-time Query
```

**Tooling:**
- Build vs. buy depends on complexity
- Metering: Segment, Snowplow, custom event tracking
- Billing: Stripe Usage, Metronome, Orb, Amberflo
- Enterprise: Zuora, Chargebee

---

## 3. Hybrid Models

### Combining the Best of Both Worlds

Hybrid models combine elements of subscription and usage-based pricing. This approach has become increasingly popular as companies seek the predictability of subscriptions with the expansion potential of usage.

### Types of Hybrid Models

**Base + Usage**

Fixed monthly fee plus variable usage charges:

```
Monthly Bill = Base Platform Fee + (Usage × Rate)
```

Example (HubSpot Marketing Hub):
- Base: $800/month for Professional tier
- Usage: $45/month per additional 1,000 contacts

Benefits:
- Predictable base revenue
- Expansion from usage growth
- Lower barrier (start with minimal usage)

**Tier + Overage**

Subscription tier includes usage allowance, overages billed separately:

```
Monthly Bill = Tier Fee + Max(0, Actual Usage - Included) × Overage Rate
```

Example (Mailchimp style):
- Standard Plan: $20/month includes 500 contacts
- Overage: $10 per additional 500 contacts

Benefits:
- Simple tier selection
- Natural upgrade path
- Customers understand their "bucket"

**Committed Usage**

Annual commitment to minimum usage, discounted rate:

```
Annual Contract = Committed Usage × Discounted Rate
Overage = (Actual - Committed) × List Rate
```

Example (Cloud providers):
- Commit to $10,000/month usage = 25% discount ($7,500/month)
- Overage above $10,000 at list price

Benefits:
- Revenue predictability for vendor
- Cost savings for customer
- Encourages higher commitments

**Seats + Usage**

Per-user pricing plus usage charges:

```
Monthly Bill = (Users × Seat Price) + (Usage × Rate)
```

Example (Developer tools):
- $10/user/month
- Plus $0.01 per build minute

Benefits:
- Revenue from both dimensions
- Team growth + product usage expansion

### Designing Hybrid Models

**Key Decisions:**

1. **What's in the base?**
   - Core functionality everyone needs
   - Should feel complete, not crippled
   - High enough to cover basic costs

2. **What's usage-based?**
   - Variable costs for the business
   - Correlates with customer value
   - Creates expansion revenue

3. **Where are the breakpoints?**
   - Usage included in base tier
   - Overage rates
   - Volume discounts

**Example Framework:**

```
Free Tier: 
  - 1,000 events/month
  - 1 user
  - 7-day retention

Starter ($49/month):
  - 10,000 events/month
  - 3 users
  - 30-day retention
  - Overage: $0.005/event

Growth ($199/month):
  - 100,000 events/month
  - 10 users
  - 90-day retention
  - Overage: $0.003/event

Enterprise (Custom):
  - Unlimited events
  - Unlimited users
  - Unlimited retention
  - Volume discounts available
```

### Hybrid Model Best Practices

1. **Make the base valuable**: Customers should feel they're getting real value from the subscription alone

2. **Usage should be a bonus**: Expansion revenue, not punishment for using the product

3. **Clear communication**: Customers must understand both components

4. **Predictable defaults**: Most customers should stay within tier limits most of the time

5. **Soft limits first**: Warn before hard cutoffs or overages

6. **Grandfathering**: Consider keeping existing customers on old model

---

## 4. Enterprise vs. SMB vs. Consumer

### Understanding Customer Segments

SaaS businesses typically serve three broad customer segments, each with distinct characteristics, requirements, and economics:

### Small and Medium Business (SMB)

**Definition:** Companies with 1-200 employees, typically spending $50-$2,000/month on a single SaaS product.

**Characteristics:**

| Attribute | SMB Pattern |
|-----------|-------------|
| Decision Speed | Fast (days to weeks) |
| Decision Makers | 1-3 people |
| Budget Authority | Often the user |
| Contract Length | Monthly to annual |
| Price Sensitivity | High |
| Feature Needs | Core functionality |
| Support Expectations | Self-serve, email |
| Churn | Higher (3-7% monthly) |
| Sales Motion | Product-led, low-touch |

**SMB SaaS Economics:**

```
Typical ACV: $600-$5,000
Target LTV: $2,000-$15,000
Target CAC: $500-$2,000
Sales Cycle: 1-14 days
Gross Margin: 75-85%
```

**What SMBs Value:**
- Easy setup (self-serve)
- Quick time-to-value
- Affordable pricing
- No annual commitment required
- Responsive support (when needed)
- Simple, intuitive UX

**SMB Go-to-Market:**
- Product-led growth dominant
- Content marketing for discovery
- Social proof (reviews, testimonials)
- Free trials or freemium
- In-app conversion
- Email-based customer success

**Challenges with SMB:**
- High churn: Small businesses fail, budgets get cut
- Low ACV: Need volume to build meaningful ARR
- Price pressure: Constant comparison shopping
- Feature requests: Want enterprise features at SMB prices

**When to Target SMB:**
- Product has broad horizontal appeal
- Self-serve onboarding is possible
- Unit economics work at lower price points
- Team can handle volume (automation)
- Market is large enough

### Mid-Market

**Definition:** Companies with 200-2,000 employees, typically spending $2,000-$20,000/month.

**Characteristics:**

| Attribute | Mid-Market Pattern |
|-----------|-------------------|
| Decision Speed | Moderate (weeks to months) |
| Decision Makers | 3-7 people |
| Budget Authority | Department head |
| Contract Length | Annual |
| Price Sensitivity | Moderate |
| Feature Needs | Advanced features |
| Support Expectations | Dedicated support |
| Churn | Moderate (1-3% monthly) |
| Sales Motion | Hybrid (PLG + sales) |

**Mid-Market SaaS Economics:**

```
Typical ACV: $24,000-$100,000
Target LTV: $72,000-$300,000
Target CAC: $10,000-$40,000
Sales Cycle: 30-90 days
Gross Margin: 70-80%
```

**What Mid-Market Values:**
- Proven ROI and case studies
- Security and compliance (SOC 2)
- Integrations with existing stack
- Customization options
- Account management
- Training and onboarding support
- Scalability for growth

**Mid-Market Go-to-Market:**
- PLG for initial land
- Sales for expansion and enterprise features
- Demo-driven conversion
- Customer success for retention
- Reference customers crucial

### Enterprise

**Definition:** Companies with 2,000+ employees, typically spending $50,000-$1,000,000+/year.

**Characteristics:**

| Attribute | Enterprise Pattern |
|-----------|-------------------|
| Decision Speed | Slow (months to year) |
| Decision Makers | 7-15+ people |
| Budget Authority | VP/C-level + procurement |
| Contract Length | Multi-year |
| Price Sensitivity | Lower (value focused) |
| Feature Needs | Full platform |
| Support Expectations | Premium, SLAs |
| Churn | Lower (5-15% annual) |
| Sales Motion | Sales-led |

**Enterprise SaaS Economics:**

```
Typical ACV: $100,000-$1,000,000+
Target LTV: $500,000-$5,000,000+
Target CAC: $50,000-$250,000
Sales Cycle: 90-365 days
Gross Margin: 60-75%
```

**What Enterprise Values:**
- Security (SOC 2, ISO 27001, HIPAA)
- Compliance and audit trails
- Custom integrations
- Single sign-on (SSO/SAML)
- Admin controls and permissions
- Dedicated support and SLAs
- Professional services
- Roadmap influence
- Custom terms
- Vendor stability

**Enterprise Go-to-Market:**
- Outbound sales
- Account-based marketing
- Executive relationships
- RFP responses
- Proof of concepts
- Custom pilots
- Professional services

**Challenges with Enterprise:**
- Long sales cycles: 6-18 months
- Implementation complexity: Professional services needed
- Customization demands: Product team burden
- Procurement processes: Legal, security reviews
- Revenue concentration: Single churn event = material impact

### Consumer SaaS (B2C)

**Definition:** Individual consumers, typically spending $5-$50/month.

**Characteristics:**

| Attribute | Consumer Pattern |
|-----------|-----------------|
| Decision Speed | Instant to days |
| Decision Makers | Individual |
| Budget Authority | Personal |
| Contract Length | Monthly |
| Price Sensitivity | Very high |
| Feature Needs | Simplicity |
| Support Expectations | Self-serve |
| Churn | Highest (5-15% monthly) |
| Sales Motion | Pure PLG |

**Consumer SaaS Economics:**

```
Typical ACV: $60-$300
Target LTV: $200-$1,000
Target CAC: $10-$100
Sales Cycle: Minutes
Gross Margin: 70-90%
```

**What Consumers Value:**
- Free tiers or cheap entry
- Instant gratification
- Beautiful, simple UX
- Mobile-first experience
- Social features
- No commitment required

**Consumer Go-to-Market:**
- Viral/word-of-mouth
- Social media
- App store optimization
- Influencer marketing
- Community building
- Content marketing

**Consumer Examples:**
- Spotify, Netflix (entertainment)
- Notion, Evernote (productivity)
- Grammarly (writing)
- 1Password, LastPass (security)
- Canva (design)

### Choosing Your Segment

**Factors to Consider:**

| Factor | Favors SMB | Favors Enterprise |
|--------|-----------|-------------------|
| Product complexity | Simple | Complex |
| Implementation | Self-serve | Services needed |
| Price point | <$500/month | >$2,000/month |
| Market size | Large, fragmented | Smaller, concentrated |
| Team experience | Limited sales | Sales experienced |
| Capital | Bootstrapped | Funded |
| Product maturity | Newer | Mature |

**The Dangerous Middle:**

Many SaaS companies fail by getting stuck in the "mid-market trap":
- Too expensive for self-serve SMB
- Too basic for enterprise requirements
- Not enough volume for efficiency
- Not enough ACV for sales economics

**Solutions:**
1. Pick a side and commit
2. Build separate tracks (SMB self-serve + enterprise sales)
3. Start SMB, expand up-market deliberately

---

## 5. Vertical vs. Horizontal SaaS

### Understanding Market Focus

**Horizontal SaaS** serves a function across all industries:
- CRM (Salesforce, HubSpot)
- Email marketing (Mailchimp, ConvertKit)
- Project management (Asana, Monday)
- Accounting (QuickBooks, Xero)
- HR (Gusto, Rippling)

**Vertical SaaS** serves a specific industry with tailored solutions:
- Healthcare: Epic, Athenahealth
- Construction: Procore, PlanGrid
- Real estate: AppFolio, Buildium
- Restaurants: Toast, Square for Restaurants
- Legal: Clio, MyCase
- Automotive: CDK Global, Dealertrack

### Horizontal SaaS Characteristics

**Advantages:**
- Larger total addressable market (TAM)
- More customers to sell to
- Diversified revenue base
- Flexibility in positioning
- Faster product development (generic features)

**Challenges:**
- Intense competition (many players)
- Commoditization pressure
- Feature parity expectations
- Harder differentiation
- Generic marketing (broad messaging)
- Lower switching costs

**Economics Typically:**
- Higher customer volume
- Lower ARPU (must work for all budgets)
- Higher marketing spend (broader reach)
- More price competition
- Winner-take-most dynamics

### Vertical SaaS Characteristics

**Advantages:**
- Deep industry expertise creates moats
- Less competition (smaller niches)
- Higher willingness to pay (specialized value)
- Stronger word-of-mouth (tight industries)
- Stickier customers (switching costs)
- Clear customer definition
- Focused product development
- Industry-specific data advantages

**Challenges:**
- Smaller total market
- Industry risk (regulatory, economic)
- Domain expertise required
- Slower sales cycles (need credibility)
- Industry-specific integrations needed
- Geographic limitations (some industries)

**Economics Typically:**
- Higher ARPU
- Lower customer volume
- Lower CAC (targeted marketing)
- Higher retention
- Expansion through industry workflow

### Vertical SaaS Playbook

**Building Credibility:**

1. **Hire from the industry**: Product, sales, and leadership should have domain experience
2. **Attend industry events**: Trade shows, conferences, local meetups
3. **Create industry content**: Blog posts, podcasts, reports with industry-specific insights
4. **Get flagship customers**: First 5-10 customers should be reference-able
5. **Speak the language**: Use industry terminology in product and marketing

**Go-to-Market Advantages:**

- **Concentrated marketing**: Industry publications, events, associations
- **Referral networks**: Industries are tight-knit, word spreads
- **Channel partners**: Industry consultants, integrators
- **Data network effects**: More customers = better industry benchmarks

**Expansion Strategies:**

1. **Own the workflow**: Expand from point solution to full platform
2. **Adjacent industries**: Move to related verticals (restaurants → hospitality)
3. **Vertical to horizontal**: Build industry-agnostic version of proven features

### Examples: Vertical Success Stories

**Toast (Restaurants)**
- Started with POS for restaurants
- Expanded to payments, payroll, inventory, online ordering
- Became the operating system for restaurants
- $1.1B ARR, $13B market cap (at peak)

**Procore (Construction)**
- Construction project management
- Expanded to financials, field productivity, preconstruction
- Strong in enterprise construction
- $900M+ ARR, public company

**Veeva (Life Sciences)**
- Started with CRM for pharma sales
- Expanded to clinical, regulatory, quality
- Deep pharma expertise
- $2.3B ARR, massive in the space

**ServiceTitan (Home Services)**
- HVAC, plumbing, electrical contractors
- Scheduling, dispatch, invoicing, payments
- Built entire operating system
- $500M+ ARR, $9.5B valuation

### Choosing Vertical vs. Horizontal

**Go Vertical If:**
- You have deep industry expertise
- Industry is large but underserved by software
- Industry-specific workflows exist
- Customers will pay premium for specialization
- You can build industry data moats
- Competition is generic horizontal players

**Go Horizontal If:**
- You're solving a universal problem
- The feature/function is commoditized
- You can compete on UX/price/distribution
- You have unique technology advantage
- Market dynamics favor aggregators
- You can achieve massive scale

**Hybrid Approach:**

Some companies start horizontal and verticalize:
- Shopify: E-commerce for all → industry-specific features
- HubSpot: Marketing automation → vertical solutions

Others start vertical and expand:
- Salesforce: Started in sales → became horizontal platform
- Square: Started in small retail → expanded everywhere

---

## 6. Emerging SaaS Models

### Vertical AI SaaS

Combining vertical SaaS with AI capabilities:
- Industry-specific training data
- Workflow automation
- Predictive features
- Outcome-based value

Examples:
- Harvey (legal AI)
- Hippocratic AI (healthcare)
- Jasper (marketing AI)

### Embedded SaaS

Software embedded into other platforms:
- Fintech infrastructure (Stripe, Plaid)
- Communications (Twilio, Sendgrid)
- Identity (Auth0, Okta)
- Payments (Square, Toast)

Characteristics:
- API-first products
- Developer-focused GTM
- Revenue scales with customer success
- Deep integrations

### Compound SaaS

Building multiple products under one umbrella:
- Rippling: HR + IT + Finance
- Gusto: Payroll + HR + Benefits
- Toast: POS + Payments + Operations

Strategy:
- Win one wedge
- Expand to adjacent problems
- Create switching costs through breadth

### Outcome-Based SaaS

Pricing based on results delivered:
- Demand-side platforms (ad spend percentage)
- Revenue share models
- Success fees

Examples:
- Performance marketing tools
- AI-driven revenue optimization
- Cost-saving automation

---

## Summary: Choosing Your Model

### Decision Framework

| Question | If Yes → |
|----------|----------|
| Does usage correlate with value? | Usage-based component |
| Is buyer experience important? | Subscription base |
| Enterprise buyers? | Annual contracts |
| SMB buyers? | Monthly option |
| Deep domain expertise? | Consider vertical |
| Universal problem? | Go horizontal |
| Need predictability? | Hybrid model |

### Key Takeaways

1. **Subscription is the default**: Start here, add complexity as needed

2. **Usage aligns incentives**: Consider usage components for expansion

3. **Hybrid wins often**: Predictable base + usage expansion

4. **Know your customer**: SMB/mid-market/enterprise have completely different needs

5. **Vertical can be powerful**: Smaller market but less competition, higher ARPU

6. **Model evolves**: Your model at $1M ARR won't be your model at $100M ARR

---

*Next: [SaaS Metrics](./metrics.md) - The numbers that matter*
