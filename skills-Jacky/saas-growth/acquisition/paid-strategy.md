# Paid Acquisition Strategy

## Introduction

Paid acquisition can be a powerful growth accelerator when done right, or an expensive way to burn cash when done wrong. The key is unit economics—your paid acquisition only works if LTV exceeds CAC by a healthy margin. This comprehensive guide covers building, optimizing, and scaling paid acquisition for SaaS companies.

---

## 1. Paid Acquisition Fundamentals

### When to Invest in Paid

**Ready for Paid:**
- Product-market fit validated
- Trial-to-paid conversion working
- Retention is stable
- Unit economics are favorable
- Budget available to test

**Not Ready for Paid:**
- Still finding PMF
- High churn rate
- Conversion rate unknown
- No budget to sustain testing
- CAC payback > 24 months

### Paid Acquisition Economics

**The Math:**
```
LTV = $3,000
Target LTV:CAC = 3:1
Maximum CAC = $1,000

If paid CAC = $800 → Profitable
If paid CAC = $1,200 → Unprofitable
```

**Calculating Target CAC:**
```
Target CAC = LTV / Target LTV:CAC Ratio

Example:
LTV = $2,400
Target ratio = 4:1
Target CAC = $2,400 / 4 = $600
```

### Channel Economics

**Typical CAC by Channel (B2B SaaS):**

| Channel | SMB CAC | Mid-Market CAC |
|---------|---------|----------------|
| Google Search | $200-800 | $800-3,000 |
| Google Display | $100-400 | $500-1,500 |
| Facebook | $150-500 | $600-2,000 |
| LinkedIn | $400-1,000 | $1,500-5,000 |
| Retargeting | $50-200 | $200-800 |

---

## 2. Campaign Architecture

### Account Structure

**Google Ads Structure:**
```
Account
├── Campaign: Brand
│   └── Ad Group: Brand Terms
├── Campaign: Competitor
│   ├── Ad Group: Competitor A Terms
│   └── Ad Group: Competitor B Terms
├── Campaign: Category
│   ├── Ad Group: Category - Exact
│   └── Ad Group: Category - Phrase
├── Campaign: Problem
│   ├── Ad Group: Problem A
│   └── Ad Group: Problem B
└── Campaign: Retargeting
    ├── Ad Group: All Visitors
    └── Ad Group: Pricing Page Visitors
```

**Facebook Ads Structure:**
```
Account
├── Campaign: Prospecting
│   ├── Ad Set: Lookalike - 1%
│   ├── Ad Set: Lookalike - 3%
│   ├── Ad Set: Interest - Tech
│   └── Ad Set: Interest - Job Title
├── Campaign: Retargeting
│   ├── Ad Set: Website Visitors 7d
│   ├── Ad Set: Website Visitors 30d
│   └── Ad Set: Engaged (video, page)
└── Campaign: Creative Testing
    ├── Ad Set: Test A
    ├── Ad Set: Test B
    └── Ad Set: Test C
```

### Campaign Types

**1. Brand Campaigns**
- Protect your brand keywords
- Low CPC, high conversion
- Essential—competitors bid on your name

**2. Competitor Campaigns**
- Bid on competitor names
- "[Competitor] alternative"
- High intent, medium-high CPC

**3. Category Campaigns**
- "CRM software," "project management tool"
- High volume, high competition
- Expensive but scalable

**4. Problem/Solution Campaigns**
- "how to manage leads"
- Lower intent but cheaper
- Good for awareness

**5. Retargeting Campaigns**
- Previous visitors
- Highest conversion rate
- Limited scale

---

## 3. Google Ads for SaaS

### Campaign Setup

**Search Campaign Best Practices:**

**Keywords:**
- Start with exact match
- Add phrase match for discovery
- Use negative keywords extensively
- Organize by tight themes

**Ad Copy:**
```
Headline 1: [Primary Keyword] + [Benefit]
Headline 2: [Social Proof or CTA]
Headline 3: [Secondary Benefit]
Description 1: [Value proposition, include keyword]
Description 2: [Call to action, create urgency]

Example:
Headline 1: Best CRM for Startups
Headline 2: 10,000+ Teams Trust Us
Headline 3: Start Free Today
Description 1: The CRM built for fast-growing startups. 
              Manage contacts, close deals, grow revenue.
Description 2: Sign up free. No credit card required. 
              See results in 5 minutes.
```

**Bidding Strategies:**

| Stage | Strategy | Why |
|-------|----------|-----|
| Launch | Manual CPC | Control while learning |
| Data gathering | Maximize Clicks | Build conversion data |
| Optimization | Target CPA | Optimize for conversions |
| Scale | Target ROAS | Optimize for revenue |

### Google Ads Optimization

**Weekly Optimization:**
- Review search terms report
- Add negative keywords
- Pause low performers
- Adjust bids

**Monthly Optimization:**
- Ad copy testing
- Landing page testing
- Audience adjustments
- Budget reallocation

**Key Metrics:**

| Metric | Target |
|--------|--------|
| CTR | >3% |
| Quality Score | >7 |
| Conversion Rate | >3% |
| Cost per Trial | <$100 (SMB) |

---

## 4. Facebook/Meta Ads for SaaS

### Audience Building

**1. Custom Audiences**
- Website visitors (install pixel)
- Customer email list
- Engaged users
- Video viewers

**2. Lookalike Audiences**
- 1% lookalike of customers
- 1% lookalike of high-value customers
- 1% lookalike of engaged users

**3. Interest Targeting**
- Business software interests
- Job title targeting
- Industry targeting
- Competitor fans

### Creative Strategy

**Creative Types:**

| Type | Best For | Tips |
|------|----------|------|
| Image | Quick tests | Clear product shot |
| Video | Explanation | 15-30 seconds |
| Carousel | Features | One feature per card |
| UGC | Authenticity | Customer testimonials |

**Creative Framework:**
```
Hook (0-3 seconds): Grab attention
- Question about pain point
- Surprising statistic
- Bold statement

Problem (3-8 seconds): Establish relevance
- Describe the pain
- Show consequences
- Create desire for solution

Solution (8-20 seconds): Introduce product
- Show product
- Highlight benefits
- Social proof

CTA (20-30 seconds): Drive action
- Clear call to action
- Urgency if appropriate
- Risk reducer
```

### Facebook Optimization

**Testing Framework:**
```
Week 1: Test audiences (same creative)
Week 2: Test creative (winning audience)
Week 3: Test copy (winning creative)
Week 4: Scale winners
```

**Metrics:**

| Metric | Target |
|--------|--------|
| CTR | >1% |
| CPM | <$30 |
| CPC | <$3 |
| Cost per Lead | <$75 |

---

## 5. LinkedIn Ads for SaaS

### When to Use LinkedIn

**Good fit:**
- Enterprise/mid-market target
- High ACV (>$5K)
- B2B with specific buyer personas
- Account-based marketing

**Bad fit:**
- SMB/prosumer target
- Low ACV (<$2K)
- Volume-based acquisition
- Limited budget

### LinkedIn Targeting

**Best Targeting Options:**

| Option | Precision | Availability |
|--------|-----------|--------------|
| Job Title | High | Limited |
| Job Function | Medium | Good |
| Seniority | High | Good |
| Company Size | High | Good |
| Industry | Medium | Good |
| Company Name | Very High | ABM only |

**Example Targeting:**
```
Job Function: Marketing
Seniority: Director, VP, C-Suite
Company Size: 51-200, 201-500
Industry: Computer Software, Technology
Geography: United States
```

### LinkedIn Ad Types

| Type | Best For | Cost |
|------|----------|------|
| Sponsored Content | Awareness | Medium |
| Message Ads | Direct outreach | Higher |
| Text Ads | Budget | Lowest |
| Conversation Ads | Engagement | Higher |

### LinkedIn Optimization

**Best Practices:**
- Use Lead Gen Forms (pre-filled)
- Keep copy professional but human
- Test image vs. no image
- Promote valuable content

**Metrics:**

| Metric | Target |
|--------|--------|
| CTR | >0.5% |
| Cost per Lead | <$150 |
| Lead quality | Higher than other channels |

---

## 6. Retargeting Strategy

### Retargeting Segments

**Segment by Behavior:**

| Segment | Timing | Intent | Priority |
|---------|--------|--------|----------|
| Pricing visitors | 7 days | Very High | 1 |
| Feature visitors | 14 days | High | 2 |
| Blog visitors | 30 days | Medium | 3 |
| All visitors | 30 days | Low | 4 |
| Abandoned trial | 14 days | Very High | 1 |
| Engaged non-convert | 21 days | High | 2 |

**Creative by Segment:**

| Segment | Creative |
|---------|----------|
| Pricing visitors | "Ready to start?" + discount |
| Feature visitors | Feature benefits + demo |
| Blog visitors | More content + light CTA |
| Abandoned trial | "Continue where you left off" |

### Retargeting Best Practices

**Frequency Caps:**
- 3-5 impressions per day
- Rotate creative weekly
- Burn pixels after 60-90 days

**Sequential Messaging:**
```
Days 1-7: Product benefits
Days 8-14: Social proof/case studies
Days 15-21: Offer/urgency
Days 22-30: Last chance
```

**Exclusions:**
- Exclude customers
- Exclude recent converters
- Exclude bounced visitors (<10 seconds)

---

## 7. Landing Page Optimization

### Landing Page Framework

**Above the Fold:**
```
┌─────────────────────────────────────────────────────────┐
│ Logo                              [CTA Button]          │
├─────────────────────────────────────────────────────────┤
│                                                         │
│     [Headline - Clear Value Proposition]               │
│                                                         │
│     [Subheadline - Supporting Detail]                  │
│                                                         │
│     [Primary CTA Button]                               │
│                                                         │
│     [Trust Signals: Logos, Reviews, Security]          │
│                                                         │
│     [Hero Image or Product Screenshot]                 │
│                                                         │
└─────────────────────────────────────────────────────────┘
```

**Full Page Structure:**
1. Hero with value prop + CTA
2. Social proof (logos, testimonials)
3. Problem agitation
4. Solution (your product)
5. Key benefits (3-5)
6. How it works (3 steps)
7. More social proof
8. FAQ (objection handling)
9. Final CTA

### Landing Page Testing

**Elements to Test:**

| Element | Impact | Difficulty |
|---------|--------|------------|
| Headline | High | Easy |
| CTA copy | High | Easy |
| CTA color | Medium | Easy |
| Hero image | Medium | Medium |
| Form fields | High | Medium |
| Social proof | Medium | Easy |
| Page length | Medium | Medium |

**Testing Process:**
1. Identify lowest-converting element
2. Create hypothesis
3. Build variant
4. Run test (95% confidence)
5. Implement winner
6. Repeat

---

## 8. Scaling Paid Acquisition

### When to Scale

**Ready to Scale:**
- CAC is within target
- Conversion rate stable
- Creative performing
- Budget available

**Not Ready:**
- CAC too high
- Conversion dropping
- Creative fatigue
- No budget headroom

### Scaling Strategies

**Horizontal Scaling:**
- Add new audiences
- Add new keywords
- Add new creative
- Add new channels

**Vertical Scaling:**
- Increase budget on winners
- Broader targeting
- Higher bids
- New markets

### Avoiding Scaling Pitfalls

**Common Mistakes:**
1. Scaling too fast (CPA rises)
2. Ignoring creative fatigue
3. Not refreshing audiences
4. Chasing vanity metrics

**Healthy Scaling:**
- 20-30% budget increase at a time
- Wait 3-4 days for data
- Monitor CAC closely
- Refresh creative every 2-4 weeks

---

## 9. Paid Acquisition Dashboard

```
PAID ACQUISITION DASHBOARD - October 2024
═══════════════════════════════════════════════════

OVERVIEW
────────────────────────────────────────────────
Total Spend:        $50,000
Total Trials:       625
Cost per Trial:     $80
Trial-to-Paid:      20%
New Customers:      125
CAC:                $400
Target CAC:         $500 ✓

BY CHANNEL
────────────────────────────────────────────────
Channel      Spend    Trials   CPA    Conv   CAC
Google       $25K     350      $71    22%    $324
Facebook     $15K     175      $86    18%    $476
LinkedIn     $8K      80       $100   20%    $500
Retargeting  $2K      20       $100   25%    $400

TOP CAMPAIGNS
────────────────────────────────────────────────
1. Google - Competitor    $6K    120 trials  $50
2. Google - Brand         $4K    100 trials  $40
3. Facebook - LLA 1%      $5K    80 trials   $63
4. Google - Category      $8K    70 trials   $114

TRENDS
────────────────────────────────────────────────
CAC Trend: ↓ 5% MoM (improving)
Volume Trend: ↑ 15% MoM (scaling)
Efficiency: Holding at 3.5:1 LTV:CAC
═══════════════════════════════════════════════════
```

---

## Summary: Paid Acquisition Framework

### Paid Acquisition Checklist

**Foundation:**
- [ ] Unit economics calculated
- [ ] Target CAC defined
- [ ] Tracking implemented
- [ ] Landing pages ready

**Campaigns:**
- [ ] Brand campaigns protecting
- [ ] Competitor campaigns running
- [ ] Category campaigns testing
- [ ] Retargeting active

**Optimization:**
- [ ] Weekly review cadence
- [ ] Creative testing process
- [ ] Landing page testing
- [ ] Audience refinement

**Scale:**
- [ ] Winners identified
- [ ] Budget allocation optimized
- [ ] Scaling plan defined
- [ ] Reporting automated

---

*End of Paid Strategy Section*
