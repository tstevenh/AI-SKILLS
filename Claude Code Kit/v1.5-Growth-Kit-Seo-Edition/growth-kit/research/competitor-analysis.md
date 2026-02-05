# Competitive Intelligence Framework

A structured approach for analyzing competitors and maintaining ongoing competitive awareness.

---

## Quick Reference: Competitor Tracking

### Primary Competitors (Direct)

| Competitor     | Product Type | Price | Target Audience | Threat Level      |
| -------------- | ------------ | ----- | --------------- | ----------------- |
| [Competitor A] | [Type]       | $[X]  | [Audience]      | [HIGH/MEDIUM/LOW] |
| [Competitor B] | [Type]       | $[X]  | [Audience]      | [Level]           |
| [Competitor C] | [Type]       | $[X]  | [Audience]      | [Level]           |

### Adjacent Competitors (Indirect)

| Competitor   | Product Type       | Overlap Area       | Notes                  |
| ------------ | ------------------ | ------------------ | ---------------------- |
| [Company]    | Free documentation | Tool education     | Not direct competition |
| [Platform]   | Free content       | Beginner education | Funnel, not competitor |
| [Competitor] | [Type]             | [Overlap]          | [Notes]                |

---

## Competitor Brief Template

Use this structure when analyzing a new competitor:

### [Competitor Name] Brief

**Last Updated:** [Date]
**URL:** [Website]
**Threat Level:** HIGH | MEDIUM | LOW

#### Overview

| Attribute       | Value                                   |
| --------------- | --------------------------------------- |
| Product Type    | [Course / Framework / SaaS / Community] |
| Price           | $[X]                                    |
| Target Audience | [Description]                           |
| Platform/Tools  | [What they teach/use]                   |
| Customers       | [X]                                     |
| Launch Date     | [Date]                                  |

#### Product Structure

- **Format:** [Video / Text / Code / Mixed]
- **Length:** [X hours / X modules]
- **Delivery:** [Self-paced / Cohort / Live]
- **Support:** [Community / 1:1 / AI assistant / None]
- **Guarantee:** [X days / Outcome-based / None]

#### Pricing Model

| Tier         | Price | Includes   |
| ------------ | ----- | ---------- |
| [Base]       | $[X]  | [Features] |
| [Premium]    | $[X]  | [Features] |
| [Enterprise] | $[X]  | [Features] |

#### Target Audience (Verbatim from their marketing)

**Who it's for:**

- [Bullet 1]
- [Bullet 2]

**Who it's NOT for:**

- [Bullet 1]
- [Bullet 2]

#### Key Messaging

**Headline:** "[Their main headline]"

**Pain Points Addressed:**

- [Pain 1]
- [Pain 2]

**Promise/Outcome:**

- [Promise 1]
- [Promise 2]

#### Strengths (What they do well)

1. [Strength 1]
2. [Strength 2]
3. [Strength 3]

#### Weaknesses (Gaps we can exploit)

1. [Weakness 1] - Our opportunity: [How we win]
2. [Weakness 2] - Our opportunity: [How we win]
3. [Weakness 3] - Our opportunity: [How we win]

#### Your Positioning Against Them

**They are:** [One-line description]
**We are:** [One-line differentiation]

**Win on:**

- [Advantage 1]
- [Advantage 2]

**Don't compete on:**

- [Their strength 1]
- [Their strength 2]

---

## Competitor Monitoring Checklist

### Monthly Review Tasks

- [ ] Check competitor pricing changes
- [ ] Review new content/features launched
- [ ] Monitor social media for positioning changes
- [ ] Search for new reviews/testimonials
- [ ] Check job postings (indicates growth areas)

### Quarterly Deep Dive

- [ ] Full landing page analysis
- [ ] Customer sentiment review (Reddit, Twitter, reviews)
- [ ] Feature comparison update
- [ ] Market positioning reassessment

---

## Battle Card Template

Quick reference for positioning conversations:

### vs [Competitor Name]

**30-Second Pitch:**

> "Unlike [Competitor] which [weakness], [Your Product] [strength]. This means you [concrete benefit]."

**Key Differentiators:**

| They                | We                |
| ------------------- | ----------------- |
| [Their approach]    | [Our approach]    |
| [Their limitation]  | [Our advantage]   |
| [Their price/model] | [Our price/model] |

**Handle Common Objections:**

"But [Competitor] teaches a process I can reuse"

- [Your response about instant capability vs learning curve]

"But [Competitor] has more content/hours"

- [Your response about results vs content volume]

"But [Competitor] is more established"

- [Your response about innovation/specialization]

---

## Competitive Response Triggers

### When to Update Analysis

| Trigger                                  | Action                     |
| ---------------------------------------- | -------------------------- |
| Competitor launches new product          | Full brief update          |
| Competitor changes pricing               | Pricing section update     |
| Competitor gets major press/visibility   | Assess threat level change |
| Customer mentions competitor in feedback | Note positioning gap       |
| Competitor targets your keywords         | SEO response planning      |

### Response Playbook

**If competitor copies your feature:**

- Document the copy (screenshots, dates)
- Emphasize your innovation and depth of implementation
- Continue improving faster than they can copy

**If competitor undercuts your price:**

- Don't race to the bottom
- Emphasize value and results over cost
- Consider targeted offers for specific segments

**If competitor targets your customers directly:**

- Strengthen customer relationships
- Highlight switching costs and unique value
- Create comparison content

---

## Integration with Other Skills

**After completing competitive intelligence:**

1. **hook-finder** - Use gaps identified for differentiation
2. **direct-response-copy** - Update messaging based on competitive landscape
3. **seo-content** - Create comparison content for organic traffic
4. **gtm-playbook** - Adjust launch positioning based on competitors

---

## Competitor Analysis Prompt Template

Use this prompt to analyze a new competitor:

```
Analyze [COMPETITOR URL] as a competitor. Research thoroughly and provide:

1. **Product Overview:** What they sell, pricing, target audience
2. **Messaging Analysis:** Key headlines, pain points addressed, promises made
3. **Strengths:** What they do well (be objective)
4. **Weaknesses:** Gaps and limitations
5. **Positioning Comparison:** How we differ and win
6. **Threat Assessment:** High/Medium/Low and why

Use web search to gather current information from their website, social media, and reviews.

Format as a competitor brief following the standard template.
```

---

## Market Landscape Mapping

### Category Mapping

Plot competitors on these dimensions:

**Price vs Depth:**

```
        HIGH PRICE
            |
            |    [Enterprise Tools]
            |
            |
LOW DEPTH --+------------------ HIGH DEPTH
            |
            |    [Your Position?]
            |
        LOW PRICE
```

**Audience Sophistication:**

```
        BEGINNERS
            |
            |
            |
BROAD ------+------------- NARROW
TARGET      |               NICHE
            |
            |
        EXPERTS
```

### Positioning Gaps

Identify white space in the market:

| Gap Identified        | Competitor Coverage             | Our Opportunity     |
| --------------------- | ------------------------------- | ------------------- |
| [Underserved segment] | [How competitors miss it]       | [How we can own it] |
| [Unmet need]          | [Why competitors don't address] | [How we can solve]  |

---

## Ongoing Intelligence Gathering

### Web Crawling with crawl-cli

Use the `crawl-cli` skill to systematically extract and archive competitor content:

```bash
# Full competitor site crawl
crawl-cli https://competitor.com --discover -m 100 -O "./research/competitors/competitor-name/"

# Targeted extraction
crawl-cli https://competitor.com/pricing -o "./research/competitors/competitor-pricing.md"
crawl-cli https://competitor.com/blog -d 2 -m 50 -O "./research/competitors/competitor-blog/"
```

**Recommended crawl schedule:**

- **Monthly:** Pricing pages, feature pages, homepage messaging
- **Quarterly:** Full site crawl, blog content, documentation

### Information Sources

**Primary:**

- Competitor websites and pricing pages
- Customer reviews (G2, Capterra, Reddit, Twitter)
- Social media accounts
- Email newsletters (sign up for all competitors)
- Product changelogs

**Secondary:**

- Industry publications and blogs
- Conference presentations
- Podcast appearances
- Job postings
- Press releases

### Weekly Scan Checklist

- [ ] Check competitor social accounts for announcements
- [ ] Review relevant subreddits for competitor mentions
- [ ] Scan industry Twitter for trends
- [ ] Check competitor email inbox for updates

---

## The Test

Good competitive intelligence answers:

1. **Who are we actually competing against?** (Named competitors with specifics)
2. **Where do we win?** (Concrete advantages we can claim)
3. **Where do we lose?** (Honest assessment of competitor strengths)
4. **What gaps exist?** (White space we can own)
5. **How should we respond?** (Actionable positioning decisions)

If you can't answer these clearly, dig deeper.
