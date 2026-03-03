---
name: keyword-research
description: Advanced keyword research with SERP clustering, cannibalization detection, SERP weakness scoring, competitor gap analysis, and multi-platform expansion. Use when researching keywords for SEO content strategy, finding untapped keyword opportunities, building topic clusters, detecting keyword cannibalization, analyzing competitor keywords, or scoring keyword difficulty by SERP weaknesses. Triggers on "find keywords", "keyword research", "keyword gap", "competitor keywords", "cluster keywords", "check cannibalization", "keyword score", or "SERP weakness".
---

# Keyword Research Skill

## Overview

Full-stack keyword research: expansion → filtering → SERP intent validation → SERP weakness scoring → clustering → cannibalization detection → competitor gap analysis.

**Keywords must be:**
- Tangentially relevant (semantically related, not just exact matches)
- Have search volume (minimum 50/month by default)
- SERP-clustered (grouped by search intent via URL overlap)
- Opportunity-scored (KeywordScore based on SERP weaknesses)

## Research Modes

| Mode | Purpose |
|------|---------|
| **Keyword Expansion** | Expand seed keywords with related suggestions |
| **Autocomplete** | Google autocomplete long-tail expansion |
| **Question Mining** | Answer The Public-style question variations |
| **Multi-Platform** | YouTube, Amazon, Bing, Reddit suggestions |
| **Domain Research** | Keywords associated with a domain's niche |
| **Competitor Research** | Exact keywords a competitor ranks for |
| **Keyword Gap** | Keywords competitor ranks for that you don't |
| **Webmaster Tools** | Real click/impression data from GSC + Bing |
| **SERP Clustering** | Group keywords by intent using URL overlap |

## Workflow

### 1. Gather Inputs

Required:
- **Seed keywords/topic/brand**
- **Target geography** (default: US)

Optional:
- Minimum volume (default: 50/month)
- Maximum difficulty
- Existing keywords (for cannibalization check)
- Competitor domain(s) (for gap analysis)
- Your domain (for GSC data + gap analysis)
- Primary selection method: volume (default) or CPC

### 2. Expand Keywords

#### 2.1 Google Sources
- **Autocomplete** — type-ahead suggestions
- **People Also Ask** — question variations
- **Related searches** — bottom of SERP
- **Wildcard patterns** — `"best * for dogs"` returns "best food for dogs", "best toys for dogs", etc.

#### 2.2 Question Mining (Answer The Public Style)
Generate variations with modifiers:
- **How/What/Why/When/Where/Who/Which**
- **Can/Should/Does/Is/Are/Will**
- **Comparison** — vs, versus, or, alternative, compared to

#### 2.3 Multi-Platform Expansion
- **YouTube** — video search suggestions
- **Amazon** — buyer intent keywords
- **Bing** — different autocomplete corpus
- **Reddit** — discussion-based queries

#### 2.4 Semantic Adjacencies
- Adjacent problems (what else do they search?)
- Upstream/downstream topics (buyer journey)
- Comparisons (vs, alternatives, best)
- Alternatives (substitute products/services)

#### 2.5 Competitor & Gap Research

**Competitor keywords:** Pull exact keywords a competitor ranks for with position + estimated traffic + ranking URL.

**Keyword gap:** Compare your domain vs competitor — find keywords they rank for that you don't.

**Domain research:** Find keywords associated with a domain's niche.

#### 2.6 Webmaster Tools (For Owned Sites)
Pull real performance data from Google Search Console + Bing Webmaster Tools:
- Clicks, Impressions, CTR, Position
- Enrich with volume/KD/CPC from DataForSEO
- Find high-impression low-CTR keywords to optimize

### 3. Filter

Remove keywords below thresholds:
- `--min-volume N` (default: 50)
- `--max-difficulty N`
- `--intent informational|commercial|transactional|navigational`
- `--contains "term"` / `--excludes "term"`

### 4. SERP Intent Validation

Before scoring keywords, validate that the SERP intent matches your target content type (default: blog/article). This prevents wasting resources on keywords dominated by product pages.

**Process:**
1. Pull top 10 organic results via SERP API
2. Classify each result by type:
   - **Product Page**: URL has /product/, /p/, /shop/item; title is single product
   - **Category/Collection**: URL has /collections/, /category/, /c/; title is "[Brand] [Category]"
   - **Blog/Article**: URL has /blog/, /articles/, /guide/; title has "How to", "Best", "Tips", numbered lists
   - **Listicle/Review**: "best X", "top X", "X vs Y", comparison/review sites
   - **Other**: Homepage, social, forums, e-commerce aggregators
3. **Decision Rule:**
   - **KEEP** if 3+ of top 10 match target content type
   - **REMOVE** if fewer than 3 (SERP intent is product/transactional)

**Shortcut Rules (to save API costs):**
- Obviously informational ("how to X", "what is X", "X tips", "X guide") → auto-keep for blog
- Obviously transactional ("buy X", "X price", "X discount", "X coupon", brand-specific products like "prada slip on") → auto-remove for blog
- Only SERP-check ambiguous keywords

**Cost Note:** SERP API ~$0.004/keyword. Use shortcut rules to minimize checks.

### 5. SERP Weakness Scoring (KeywordScore)

For each keyword, analyze the top 10 SERP results and score the opportunity.

#### 17 SERP Weakness Types

**Domain & Authority (3)**

| Weakness | Threshold |
|----------|-----------|
| Low Domain Score | DS ≤ 10 |
| Low Page Score | PS ≤ 0 |
| No Backlinks | 0 backlinks to ranking page |

**Technical SEO (7)**

| Weakness | Threshold |
|----------|-----------|
| Slow Page Speed | > 3000ms load time |
| High Spam Score | ≥ 50 |
| Non-HTTPS | HTTP only |
| Broken Page | 4xx/5xx status |
| Flash Code | Present |
| Frames | Present |
| Non-Canonical | Missing canonical tag |

**Content Quality (4)**

| Weakness | Threshold |
|----------|-----------|
| Old Content | > 2 years since update |
| Title-Content Mismatch | Title doesn't match query |
| Keyword Not in Headings | Missing from H1-H3 |
| No Heading Tags | Zero H tags |

**SERP Composition (2)**

| Weakness | Threshold |
|----------|-----------|
| UGC-Heavy Results | 3+ Reddit/Quora/forums in top 10 |
| Unmatched Intent | Titles missing 1+ query words (+4 for 1 word, +7 for 2+) |

#### KeywordScore Algorithm (0-100)

| Component | Points |
|-----------|--------|
| Each standard weakness found | +1 |
| Unmatched Intent (1 word) | +4 |
| Unmatched Intent (2+ words) | +7 |
| Volume 101-1,000 | +1 |
| Volume 1,001-5,000 | +2 |
| Volume 5,000+ | +3 |
| KD = 0 | +3 |
| KD 1-15 | +2 |
| KD 16-30 | +1 |
| Low avg Domain Score | Variable |
| Individual low DS (position-weighted) | Variable |
| SERP features (non-organic) | -1 each (max -3) |

**Score Interpretation:**

| Score | Opportunity |
|-------|-------------|
| 90-100 | Exceptional — multiple significant weaknesses |
| 70-89 | Strong — several exploitable weaknesses |
| 50-69 | Moderate — some weaknesses |
| 30-49 | Challenging — few weaknesses |
| 0-29 | Very difficult — highly competitive |

### 6. SERP Clustering

Group keywords by search intent using SERP URL overlap.

#### Three Algorithms

**DEFAULT (Fast & Broad)**
- Keyword joins cluster if it shares X URLs with **primary keyword only**
- Best for: Large datasets (100K+), content hubs
- Speed: Fastest

**STRICT (Tight & Precise)**
- Keyword must share X URLs with **ALL existing cluster members**
- Best for: Competitive niches, precise targeting
- Speed: 2-3x slower
- Note: May create many single-keyword clusters ("first-mover advantage")

**BALANCED STRICT (Recommended)**
- Progressive thresholds by cluster size:
  - 2-5 keywords: 100% match
  - 6-10: 80% match
  - 11+: 60% match
- Best for: Most use cases

#### Similarity Threshold
- Range: 3-7 shared URLs in top 10 results
- Default: 4
- Higher = stricter relevance

#### Primary Keyword Selection
- **Volume-based** (default): Highest search volume in cluster
- **CPC-based**: Highest CPC — better for commercial/transactional keywords

### 7. Cannibalization Detection

Check if keywords have overlapping SERP intent:

1. Get top 10 results for Keyword A and Keyword B
2. Calculate: `(shared URLs / total unique URLs) × 100`
3. If overlap > 70% → **CANNIBALIZING**
4. Group cannibalizing keywords — user targets ONE per group

### 8. Re-Clustering

When adding new keywords to existing research:
- Reuse saved SERP data (configurable age: 1-30 days)
- Distribute new keywords into existing clusters
- Mark additions with "New" badge and run number
- No full rebuild needed

### 9. Output Format

```
## Keyword Research: [Topic]

### Summary
- Keywords analyzed: X | Clusters: Y | Cannibalization alerts: Z
- Top opportunity: [keyword] (KS: 85, Vol: 2,400)

### Top Clusters (by volume)

#### Cluster 1: [Primary Keyword] (Vol: 2,400 | KS: 72)
| Keyword | Vol | KD | KS | CPC | Intent | Weaknesses |
|---------|-----|----|----|-----|--------|------------|
| primary kw | 2,400 | 32 | 72 | $2.50 | Commercial | Old Content, Low DS ×3, No Backlinks |
| related kw | 1,200 | 28 | 68 | $1.80 | Commercial | Slow Page, UGC-Heavy |
Target all with ONE page.

### Cannibalization Alerts
- **Group A**: "kw1" vs "kw2" — 85% overlap — Pick one

### Competitor Gap (if requested)
| Keyword | Vol | KD | Their Pos | Their URL |
|---------|-----|----|-----------|-----------|
| gap kw 1 | 3,200 | 41 | 5 | competitor.com/page |

### Tangential Opportunities (High KS, Low KD)
| Keyword | Vol | KD | KS | Source |
|---------|-----|----|-----|--------|
| question kw | 320 | 12 | 81 | People Also Ask |
| youtube kw | 580 | 18 | 74 | YouTube |

### Recommendations
1. Target Cluster 1 first (highest volume, KS 72)
2. Create FAQ content for question opportunities (KS 80+)
3. Avoid Group A — cannibalizing with existing content
4. Competitor gap: 12 keywords they rank for that you don't
```

### CSV Export

Export with `--csv` to `~/Downloads/keyword-research-YYYYMMDD-HHMMSS.csv`:

**Basic:** `Keyword,Volume,CPC,Difficulty,Intent`
**Extended:** `Keyword,Volume,CPC,Difficulty,Intent,KeywordScore,DomainScore,PageScore,WeaknessCount,Weaknesses`
**Competitor/Gap:** `Keyword,Volume,CPC,Difficulty,Intent,Position,EstTraffic,RankingURL`

## Tools & APIs

**Primary (recommended):**
- **DataForSEO** — keyword suggestions, competitor keywords, domain intersection, backlink scores, SERP analysis, page speed (~$0.60/1000 keywords for SERP)
  - Endpoints: `keyword_suggestions/live`, `ranked_keywords/live`, `domain_intersection/live`, `backlinks/summary/live`, `serp/google/organic/live`, `onpage/instant_pages`

**Alternative:**
- **Serper** — faster/simpler for basic SERP data + autocomplete
- **SerpAPI** — SERP scraping for clustering

**Optional enrichment:**
- **Ahrefs API** — DR/UR metrics
- **Google Search Console API** — real click/impression data
- **Bing Webmaster Tools API** — Bing performance data

**For large-scale clustering (1M+ keywords):**
- Proxies + custom scraper ($80-100/mo rotating residential vs $600/mo API)

## Best Practices

| Scenario | Algorithm | Primary | Threshold |
|----------|-----------|---------|-----------|
| Content hub planning | DEFAULT | Volume | 3-4 |
| Competitive niche | STRICT | Volume | 5-6 |
| E-commerce categories | BALANCED STRICT | CPC | 4 |
| PPC campaign planning | BALANCED STRICT | CPC | 4-5 |
| Blog content calendar | BALANCED STRICT | Volume | 4 |
| 100K+ keyword datasets | DEFAULT | Volume | 3-4 |
