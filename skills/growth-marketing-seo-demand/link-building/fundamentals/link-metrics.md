# Link Metrics Explained

## The Language of Link Building

Before you can evaluate a link opportunity, prospect for targets, or report to clients, you need to speak the language of link metrics. These third-party measurements attempt to quantify what Google keeps secret: how authoritative and trustworthy is a given website or page?

No metric perfectly represents Google's internal scores. But used correctly, these tools provide invaluable shortcuts for evaluating thousands of potential link opportunities without manual review of each one.

This chapter covers every major metric you'll encounter, how they're calculated, their strengths and limitations, and how to use them in practice.

## Domain Rating (DR) / Domain Authority (DA)

### What They Measure

Domain Rating (Ahrefs) and Domain Authority (Moz) are attempts to predict how well an entire domain will rank in search engines. They're composite scores from 0-100 that aggregate multiple link-related signals into a single number.

**Key distinction:** These measure the *domain* (entire website), not individual pages.

### Ahrefs Domain Rating (DR)

**How it's calculated:**
1. Count the number of unique domains linking to the target
2. Assess the DR of those linking domains
3. Account for how many sites each linking domain links to
4. Apply a logarithmic scale (harder to go from 90→91 than 10→11)

**What it includes:**
- Referring domains count
- Authority of referring domains  
- Distribution of that authority

**What it doesn't include:**
- Content quality
- On-page factors
- User behavior
- Link relevance
- Spam signals

**DR ranges and their meaning:**

| DR Range | Interpretation | Examples |
|----------|---------------|----------|
| 0-20 | Very low authority | New sites, personal blogs |
| 21-40 | Low-medium authority | Established blogs, small businesses |
| 41-60 | Medium-high authority | Popular blogs, regional news |
| 61-80 | High authority | Major publications, large brands |
| 81-100 | Elite authority | Wikipedia, NYT, Google |

### Moz Domain Authority (DA)

**How it's calculated:**
Moz uses machine learning to predict how likely a domain is to rank. It considers:
- Linking root domains
- Total number of links
- MozRank and MozTrust scores
- 40+ other factors

**Key differences from Ahrefs DR:**
- Different crawl index (Moz's is smaller)
- Different algorithm methodology
- Tends to fluctuate more with index updates
- Generally considered less reliable than DR since 2020

**DA ranges are similar to DR but often differ by 5-15 points for the same domain.**

### Practical Usage of DR/DA

**For prospecting:**
- Set minimum thresholds based on your link building tier
- Filter out obvious low-quality sites quickly
- Identify relative value within a niche

**Our recommended minimums (Indexsy standards):**

| Campaign Type | Minimum DR/DA |
|---------------|---------------|
| High-end client | 50+ |
| Standard campaign | 30+ |
| Budget campaign | 20+ |
| Never accept | Below 15 |

**Important caveats:**
1. DR/DA can be artificially inflated through link schemes
2. A DR40 site in your exact niche often beats a DR60 general site
3. DR doesn't account for traffic—a DR50 site with 0 traffic is suspect
4. Always verify DR with other signals (traffic, content quality, spam)

### DR Manipulation and Red Flags

**How DR gets artificially inflated:**
- PBN links from high-DR expired domains
- Link exchanges with high-DR sites
- Parasite links from high-DR platforms (Medium, LinkedIn)
- Buying links from sites that sell to everyone

**Red flags indicating inflated DR:**
- High DR but low organic traffic
- High DR but thin/low-quality content
- Recently expired and restarted domain
- Suspicious link profile (same linking sites as known PBNs)
- Accepting any paid post regardless of relevance

**Verification checklist:**
✓ Check organic traffic (should correlate with DR)
✓ Review recent content quality
✓ Check domain age and history
✓ Look at referring domains for patterns
✓ Verify the site has editorial standards

## URL Rating (UR) / Page Authority (PA)

### What They Measure

While DR/DA measure entire domains, URL Rating (Ahrefs) and Page Authority (Moz) measure individual pages. This is crucial because:

1. Your link comes from a specific page, not the domain
2. New pages on high-DR sites often have low page authority
3. A link from a DR70 site's homepage differs vastly from a deep blog post

### Ahrefs URL Rating (UR)

**How it's calculated:**
- Similar to original PageRank concept
- Considers links pointing to that specific URL
- Internal links count (so well-linked internal pages have higher UR)
- Logarithmic scale like DR

**UR vs DR relationship:**
- Homepage typically has highest UR
- Category pages have moderate UR
- New blog posts start with very low UR
- UR can exceed DR if page has strong direct links

**What to look for:**
| UR | Interpretation |
|----|---------------|
| 0-10 | New or poorly linked page |
| 11-25 | Established page with some links |
| 26-40 | Well-linked page |
| 41-60 | Strong page with significant links |
| 61+ | Exceptional page authority |

### Practical Usage of UR/PA

**For link placement decisions:**
- Links from high-UR pages pass more value
- A link from a DR70 site's UR5 page may underperform a DR50 site's UR30 page
- Consider asking for link placement on specific high-UR pages

**For outreach targeting:**
- Target resource pages with existing links (higher UR)
- Guest posts on sites with strong internal linking (helps your post gain UR)
- Avoid sites where every page has UR0-5 (poor internal structure)

**For opportunity evaluation:**
- UR shows actual page strength, not just domain strength
- Helps compare opportunities on the same domain
- Indicates how much the site invests in that content type

## Trust Flow and Citation Flow (Majestic)

### The Majestic Approach

Majestic takes a different approach from Ahrefs and Moz, splitting authority into two components:

**Citation Flow (CF):** How many links point to a site/page (quantity)
**Trust Flow (TF):** How trustworthy those links are (quality)

### How They're Calculated

**Citation Flow:**
- Essentially a measure of link quantity
- More links = higher CF
- Link spam can inflate CF easily

**Trust Flow:**
- Based on distance from trusted seed sites
- Majestic manually curates a set of "trusted" domains (universities, gov sites, major brands)
- Sites closely connected to trusted seeds have higher TF
- Links from high-TF sites pass trust

### The TF/CF Ratio

The relationship between Trust Flow and Citation Flow is often more useful than either number alone:

**TF:CF Ratio Interpretation:**

| Ratio | Meaning |
|-------|---------|
| TF ≈ CF | Balanced, natural profile |
| TF > CF | Very high quality links (rare) |
| CF >> TF | Many links but low trust (spam signal) |

**Rule of thumb:** Look for TF/CF ratio of at least 0.5 (TF is at least half of CF)

**Examples:**
- TF 45, CF 50 → Ratio 0.9 → Excellent
- TF 20, CF 60 → Ratio 0.33 → Concerning
- TF 5, CF 70 → Ratio 0.07 → Major red flag

### Topical Trust Flow

Majestic categorizes links by topic, showing which subjects a domain has authority in:

**Why this matters:**
- A site might have high overall TF but no authority in your niche
- Topical TF shows relevance signals
- Helps identify sites that *actually* cover your industry

**Using topical TF:**
1. Check if your target niche appears in their top topics
2. Higher topical TF in your category = more relevant link
3. Sites with scattered topical TF may be less valuable than focused sites

### Practical Usage of Majestic Metrics

**For quality assessment:**
- Use TF/CF ratio as a spam filter
- Check topical TF for relevance
- Compare against DR/DA for consistency

**Red flags:**
- CF 60+ but TF under 10
- No topical relevance to your niche
- TF dropped significantly recently (may indicate link cleanup)

**Integration with other metrics:**
- Sites with high DR, high traffic, AND good TF/CF ratio are strong candidates
- Discrepancies between tools often indicate manipulation
- Use Majestic as a secondary verification, not primary filter

## Referring Domains vs. Backlinks

### Understanding the Difference

**Backlinks:** Total count of individual links pointing to a site/page
**Referring Domains:** Count of unique domains those links come from

**Example:**
- Site A has 3 links from nytimes.com, 2 from forbes.com, 1 from techcrunch.com
- Backlinks = 6
- Referring Domains = 3

### Why Referring Domains Matter More

Google likely values link diversity over raw link count. The rationale:

1. **Manipulation resistance:** Getting 100 links from one site is easier than from 100 sites
2. **Broader endorsement:** 50 different sites linking to you is a stronger signal than 50 links from your own PBN
3. **Natural patterns:** Organically popular content earns links from many sources

**Indexsy's rule:** We count referring domains, not total backlinks, when reporting to clients.

### Analyzing Referring Domain Patterns

**What to look for in a link profile:**

**Healthy patterns:**
- Referring domains grow over time
- Mix of high and low authority domains
- Diverse geographic and topical sources
- Natural anchor text distribution

**Unhealthy patterns:**
- Sudden spikes followed by plateaus
- All referring domains from same country (if site is English/global)
- Many referring domains but all low authority
- Same referring domains appear across multiple unrelated sites

### Domain-Level vs. Page-Level Referring Domains

**Domain RDs:** Unique domains linking anywhere on your site
**Page RDs:** Unique domains linking to a specific URL

**Why both matter:**

For overall site authority, domain-level RDs show your total endorsement count.

For ranking specific pages, page-level RDs often correlate more directly with rankings. A page with 50 referring domains will typically outrank a page with 5, assuming other factors equal.

**Our benchmarks:**
| Keyword Difficulty | Page RDs Typically Needed |
|--------------------|--------------------------|
| KD 0-20 | 5-20 |
| KD 21-40 | 20-50 |
| KD 41-60 | 50-100 |
| KD 61-80 | 100-300 |
| KD 81-100 | 300+ |

*These are rough guidelines; actual requirements vary by niche and content quality.*

## Dofollow vs. Nofollow vs. Sponsored vs. UGC

### The Link Attribute Ecosystem

Link attributes tell Google about the nature of a link. Understanding them is essential for both building links and analyzing competitors.

### Dofollow Links (No Attribute)

**Technical definition:** A link with no rel attribute, or with rel="dofollow" (though the latter is redundant)

**SEO implications:**
- Passes full link equity (PageRank)
- Counts as an editorial endorsement
- The primary target for most link building

**Example HTML:**
```html
<a href="https://example.com">Anchor Text</a>
```

### Nofollow Links

**Technical definition:** `rel="nofollow"` attribute

**Original purpose:** Tell search engines not to follow or count this link for ranking purposes.

**Current Google stance:** A "hint" rather than directive. Google may choose to follow and value nofollow links.

**SEO implications:**
- Traditionally passed no link equity
- Since 2019, Google may use for discovery and potentially rankings
- Still less valuable than dofollow
- Natural link profiles include nofollow links

**Example HTML:**
```html
<a href="https://example.com" rel="nofollow">Anchor Text</a>
```

**Common nofollow scenarios:**
- Blog comments
- Forum signatures
- Untrusted user-generated content
- Affiliate links
- Press releases
- Some guest post links

### Sponsored Links

**Technical definition:** `rel="sponsored"` attribute (introduced 2019)

**Purpose:** Identify paid or sponsored placements

**SEO implications:**
- Should not pass link equity
- Complies with Google's link scheme guidelines
- Required for paid placements to avoid penalties
- Safer than dofollow for paid links

**Example HTML:**
```html
<a href="https://example.com" rel="sponsored">Anchor Text</a>
```

**When to expect/request sponsored:**
- Clearly paid advertorial content
- Sponsored content on major publications
- Affiliate links (alternative to nofollow)

### UGC (User-Generated Content) Links

**Technical definition:** `rel="ugc"` attribute (introduced 2019)

**Purpose:** Identify links in user-generated content (comments, forums)

**SEO implications:**
- Similar to nofollow—limited equity transfer
- Helps Google understand link context
- Can be combined with nofollow: `rel="nofollow ugc"`

**Example HTML:**
```html
<a href="https://example.com" rel="ugc">Anchor Text</a>
```

### Combining Attributes

Attributes can be combined:
- `rel="nofollow sponsored"` - Paid link, don't follow
- `rel="nofollow ugc"` - User content, don't follow
- `rel="sponsored ugc"` - Paid user content

### The Practical Link Builder's Perspective

**Priority order for link building:**
1. Dofollow (full value)
2. Nofollow from high-authority sites (still valuable)
3. Sponsored from relevant sites (visibility value)
4. UGC (limited value, usually not worth targeting)

**Don't ignore nofollow links from:**
- Major publications (TechCrunch, Forbes, NYT)
- Wikipedia
- High-traffic sites (referral traffic value)
- Industry resources (credibility value)

**Analyzing competitor profiles:**
- Healthy profiles have 60-80% dofollow
- 100% dofollow is suspicious (manipulated)
- 100% nofollow means minimal SEO benefit from those links

## Link Velocity

### What Is Link Velocity?

Link velocity measures how quickly a site or page acquires new backlinks over time. It's expressed as:
- Links per day
- Links per week
- Links per month

### Why Link Velocity Matters

**For analysis:**
- Sudden spikes may indicate manipulation or viral content
- Steady growth suggests sustainable link building
- Decline may indicate aging content or lost links

**For strategy:**
- Building links too fast can trigger algorithmic scrutiny
- Building too slow may not move rankings
- Matching or slightly exceeding competitor velocity is often ideal

### Calculating Link Velocity

**Simple calculation:**
New referring domains in period ÷ Number of days = Daily velocity

**Example:**
- 30 new referring domains in the last month
- 30 ÷ 30 = 1 new RD per day

### Natural vs. Unnatural Velocity Patterns

**Natural patterns:**
- Gradual increase after content publication
- Spikes around newsworthy events (then return to baseline)
- Seasonal variations matching industry trends
- Growth proportional to content output

**Unnatural patterns:**
- Sudden spike from zero to hundreds
- Perfect consistency (exactly 10 links per week forever)
- Spikes with no corresponding content or news
- Burst followed by complete silence

### Safe Link Building Velocity

**General guidelines:**

For a new site:
- Start with 5-10 links per month
- Gradually increase over 6-12 months
- Match velocity to content production

For an established site:
- Match historical velocity patterns
- Increase 20-30% per quarter maximum
- Accelerate around content launches

**Red lines:**
- Doubling links overnight (looks purchased)
- Going from 0 to 100 links in a week
- Dramatically different velocity than competitors

**For Indexsy campaigns:**
We typically deliver links over 30-90 days rather than all at once, maintaining natural velocity patterns.

### Monitoring Link Velocity

**Tools:**
- Ahrefs: New referring domains over time chart
- SEMrush: Backlink analytics timeline
- Majestic: Referring domains history

**What to track:**
- Your own velocity trends
- Competitor velocity (to benchmark)
- Unusual spikes or drops (investigate causes)

## Anchor Text Distribution

### What Is Anchor Text?

Anchor text is the visible, clickable text of a hyperlink. It signals to Google what the linked page is about.

**Example:**
`<a href="https://example.com/shoes">best running shoes</a>`
Anchor text = "best running shoes"

### Why Anchor Text Distribution Matters

Google uses anchor text as a relevance signal. The anchors pointing to your page tell Google what terms you should rank for.

**The danger:** Too many exact-match anchors looks manipulative. Before Penguin, SEOs would build thousands of links with exact anchor matches like "buy cheap shoes." This no longer works and actively hurts rankings.

### Types of Anchor Text

**1. Exact Match**
The anchor exactly matches your target keyword.
- Target keyword: "best email marketing software"
- Anchor: "best email marketing software"

**2. Partial Match**
The anchor includes your keyword plus other words.
- Target keyword: "email marketing software"
- Anchor: "this email marketing software comparison"

**3. Branded**
The anchor is your brand name.
- Brand: Mailchimp
- Anchor: "Mailchimp"

**4. Branded + Keyword**
Combines brand with keywords.
- Anchor: "Mailchimp email marketing"

**5. Naked URL**
The anchor is the URL itself.
- Anchor: "https://mailchimp.com"
- Anchor: "mailchimp.com"

**6. Generic**
Non-descriptive call-to-action anchors.
- "click here"
- "learn more"
- "read this"
- "visit website"
- "this article"

**7. Image (No Text)**
When an image links to your page, Google uses the alt text.
- Alt text becomes the effective anchor

### Safe Anchor Text Distribution

**Our recommended ratios (Indexsy standard):**

| Anchor Type | Percentage |
|-------------|------------|
| Branded | 40-50% |
| Naked URL | 20-25% |
| Generic | 15-20% |
| Exact Match | 5-10% |
| Partial Match | 10-15% |

**Why these ratios?**
- Natural link patterns are dominated by branded and URL anchors
- People linking organically rarely use exact keyword anchors
- Exact match should be rare and contextually natural
- Diversity signals organic acquisition

### Anchor Text Strategy by Page Type

**Homepage:**
- Heavily branded (70%+)
- Naked URLs
- Minimal keyword anchors

**Product/Service pages:**
- Mix of branded + keyword
- More partial match acceptable
- Still limit exact match to <10%

**Blog posts/content:**
- Title variations
- Partial matches common
- Topic-descriptive anchors

**Local businesses:**
- Brand + location
- Service + location
- Business name variations

### Analyzing Competitor Anchor Distribution

Before building links, analyze competitors ranking for your terms:

1. Export their anchor text profile from Ahrefs/SEMrush
2. Categorize anchors by type
3. Calculate percentages
4. Note over-optimized competitors (you can beat them with cleaner profile)
5. Model your distribution on top-ranking, established competitors

### Fixing Over-Optimized Anchor Profiles

**Signs of over-optimization:**
- More than 20% exact match
- Very few branded anchors
- Many anchors with commercial modifiers ("buy," "cheap," "best")

**Solutions:**
1. Build more branded and generic anchor links
2. Request anchor text changes on existing links (if relationships allow)
3. Create diverse new content to attract varied anchors
4. Disavow obviously spam links with manipulative anchors

### Anchor Text Best Practices

**Do:**
- Vary anchors with every new link
- Use natural language variations
- Include surrounding context that's relevant
- Let some anchors be editor's choice

**Don't:**
- Use the same exact anchor repeatedly
- Over-optimize for commercial terms
- Create anchors that don't fit the content context
- Ignore anchor distribution in reporting

## Putting Metrics Together: Holistic Evaluation

### The Multi-Metric Assessment Framework

No single metric tells the whole story. Here's how we evaluate link opportunities at Indexsy:

**Tier 1: Quick Filters**
- DR/DA: Meets minimum threshold?
- Traffic: Has real organic visitors?
- Language/Geo: Appropriate for target audience?

**Tier 2: Quality Verification**
- TF/CF ratio: Above 0.5?
- Content review: Quality editorial standards?
- Link profile: Clean or spammy linking patterns?

**Tier 3: Opportunity Assessment**
- UR/PA of linking page: How strong is it?
- Relevance: Topically aligned?
- Link placement: Where would link appear?

**Tier 4: Value Calculation**
- Estimated PageRank transfer
- Referral traffic potential
- Brand association value
- Cost vs. benefit

### Metric Red Flags Summary

| Red Flag | What It Means | Action |
|----------|---------------|--------|
| High DR, low traffic | Inflated/manipulated | Verify or skip |
| Low TF/CF ratio | Spammy link profile | Skip |
| New domain, high DR | PBN or purchased domain | Skip |
| Traffic from wrong country | Irrelevant audience | Usually skip |
| Accepts any content | Low editorial standards | Lower value |
| DR dropped recently | Lost links or penalty | Investigate |

### Creating Your Evaluation Scorecard

Build a systematic approach for your team:

| Metric | Minimum | Ideal | Weight |
|--------|---------|-------|--------|
| DR | 30 | 50+ | 25% |
| Organic Traffic | 1,000 | 10,000+ | 25% |
| TF/CF Ratio | 0.4 | 0.7+ | 15% |
| UR of Linking Page | 10 | 25+ | 15% |
| Topical Relevance | Some | High | 20% |

Score each opportunity and compare systematically rather than relying on gut feel alone.

## Summary

Understanding link metrics is foundational to effective link building. Key takeaways:

1. **DR/DA** measures domain authority but can be manipulated—verify with traffic
2. **UR/PA** measures page authority—often more relevant than domain metrics
3. **TF/CF ratio** helps identify spam—look for at least 0.5
4. **Referring domains** matter more than total backlinks—diversity is key
5. **Link attributes** (dofollow, nofollow, sponsored) affect value transfer
6. **Link velocity** should appear natural—avoid sudden spikes
7. **Anchor text distribution** must look organic—limit exact match to 5-10%

Use multiple metrics together, never in isolation. The best link opportunities score well across all dimensions while representing good value for the investment required.
