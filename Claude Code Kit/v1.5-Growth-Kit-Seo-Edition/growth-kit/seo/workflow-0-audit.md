# Workflow 0: SEO Audit & Opportunity Analysis

**Purpose:** Evaluate existing content, competitive positioning, and content gaps BEFORE keyword research  
**Platform:** Claude Desktop (or Claude Code) with web_search  
**Input:** Website URL + Google Search Console data (optional) + business context  
**Output:** Single comprehensive Markdown artifact with audit findings and prioritized opportunities  
**Capacity:** 1 domain per execution  
**Status:** ✅ Production-ready

---

## Why Workflow 0 Exists

Most SEO workflows start with keyword research. This is backwards.

**The Problem:**
- Keyword research without context produces generic recommendations
- You may already have content assets that need optimization, not replacement
- Competitor gaps are invisible without systematic analysis
- Without positioning evaluation, you're "ranking in a vacuum"

**The Solution:**
Workflow 0 audits what exists BEFORE discovering new keywords. It answers:
1. What content do we already have, and what should we do with it?
2. Where do we stand vs. competitors in search results?
3. What gaps exist—both vs. competitors AND in the market overall?
4. What should we prioritize first?

**Pipeline Position:**
```
Workflow 0 (Audit) → Workflow 1 (Keyword Discovery) → Workflow 2 (Organization) → Workflow 3 (Content Generation)
                  ↘ Workflow 4 (Rank Enhancement) ← existing content optimization loop
```

---

## The Three Pillars Framework

Workflow 0 is structured around three audit dimensions:

| Pillar | Focus | Key Question |
|--------|-------|--------------|
| **Positioning Evaluation** | Competitive landscape | Where do we stand vs. competitors? |
| **Content Gap Analysis** | Missing opportunities | What topics are we missing? |
| **Content Inventory** | Existing assets | What should we do with current content? |

**Critical Insight (Lidia Infante, Wix):**
> "There is a ceiling to how much optimizing one aspect of your SEO can improve your rankings. Be it content, technical SEO, or links, the returns on your SEO activities diminish as you become better and better at one particular area."

This means: if your content is excellent but not ranking, more content improvement yields diminishing returns. Focus shifts to technical SEO or link building instead.

---

## Execution Mode: Autonomous + Single Artifact Output

**Process Flow:**
1. Receive website URL and business context
2. Gather GSC data if available (or use web_search for competitive intelligence)
3. Execute all audit stages sequentially
4. Output complete audit as single Markdown artifact

**Dependencies:**
- web_search tool for SERP analysis and competitor research
- Optional: Google Search Console data export (CSV or manual input)
- Optional: SEO tool exports (Ahrefs, Semrush) for deeper analysis

**Execution Principles:**
- Audit existing state before recommending new content
- Apply Three Pillars framework systematically
- Use decision trees for consistent recommendations
- Produce actionable output that feeds into Workflow 1 or Workflow 4
- Prioritize by Impact × Effort

---

## Input Requirements

### Required Information

```
Website URL: [full domain, e.g., https://example.com]
Business Description: [1-2 sentences on what the business does]
Primary Topic/Niche: [main subject area for SEO]
Target Audience: [who you're trying to reach]
Business Goals: [what success looks like - traffic, leads, sales, authority]
```

### Optional (Enhances Analysis)

```
Google Search Console Export: [CSV with queries, pages, clicks, impressions, position]
Top 3-5 Competitors: [domains of main SEO competitors]
Existing Content List: [URLs of current blog/content pages]
Current Rankings: [any known keyword positions]
Previous SEO Work: [what's been tried before]
```

### Minimal Viable Input

At minimum, provide:
- Website URL
- Primary topic/niche
- Target audience

All other information can be inferred through web_search analysis.

---

## Processing Stages (Autonomous Execution)

### STAGE 1: Context Gathering & Competitor Identification

**Step 1.1: Parse Input**
1. Extract website URL and strip to root domain
2. Note business description and goals
3. Identify primary topic/niche for SERP analysis
4. Record target audience for intent matching

**Step 1.2: Identify SEO Competitors**

Execute web_search for 3-5 core topic queries:
```
web_search("[primary topic] guide")
web_search("[primary topic] best practices")
web_search("[primary topic] for [target audience]")
```

**From search results, identify:**
- Which domains consistently appear in top 10
- Note: SEO competitors may differ from business competitors
- Select 3-5 domains that compete for same keywords

**Output: Competitor List**
| Competitor | Domain | Appears in X/5 Searches | Notes |
|------------|--------|------------------------|-------|

**Step 1.3: Baseline Assessment**

If GSC data available:
- Total organic clicks (last 3 months)
- Total impressions
- Average position
- Number of ranking queries
- Top 10 pages by traffic

If no GSC data:
- Use web_search to check if site appears for core queries
- Note approximate visibility level (strong/moderate/weak/invisible)

---

### STAGE 2: Positioning Evaluation

**Purpose:** Understand where you stand relative to competitors in search results.

**Step 2.1: SERP Landscape Analysis**

For 10-15 core keywords in your niche, execute web_search and document:

| Keyword | Your Position | Top Competitor | SERP Features | Content Type Winning |
|---------|---------------|----------------|---------------|---------------------|

**SERP Features to Note:**
- Featured snippets (present/absent, who owns it)
- People Also Ask boxes
- AI Overviews (and which sources cited)
- Video carousels
- Local pack
- Knowledge panels
- Image packs

**Content Types Winning:**
- Ultimate guides (3000+ words)
- Listicles
- How-to tutorials
- Comparison pages
- Tools/calculators
- Video content

**Step 2.2: Competitive Scorecard**

For each competitor (3-5), assess:

| Metric | Competitor A | Competitor B | Competitor C | Your Site |
|--------|--------------|--------------|--------------|-----------|
| Estimated organic traffic | | | | |
| Content volume (approx pages) | | | | |
| Domain authority (if known) | | | | |
| Content quality (1-5) | | | | |
| SERP feature ownership | | | | |

**Quality Assessment Criteria:**
- 5: Comprehensive, well-structured, unique insights, strong E-E-A-T signals
- 4: Thorough coverage, good structure, some unique value
- 3: Adequate coverage, standard approach, no differentiation
- 2: Thin content, missing key subtopics, outdated
- 1: Poor quality, keyword-stuffed, unhelpful

**Step 2.3: Position Gap Identification**

Categorize your keyword positions:

| Position Range | Count | Strategic Implication |
|----------------|-------|----------------------|
| 1-3 | | Defend and maintain |
| 4-10 | | Optimize for quick wins (Workflow 4) |
| 11-20 | | Striking distance—priority optimization |
| 21-50 | | Requires significant investment |
| Not ranking | | Net new content opportunities (Workflow 1-3) |

**Step 2.4: Competitive Advantage Assessment**

Based on analysis, identify:

**Your Advantages:**
- Topics where you outrank competitors
- Unique angles or expertise you have
- Content formats you do better
- E-E-A-T signals (credentials, experience, authority)

**Your Disadvantages:**
- Topics where competitors dominate
- Content depth gaps
- Technical or UX weaknesses
- Authority/backlink gaps

---

### STAGE 3: Content Gap Analysis

**Purpose:** Identify missing topic opportunities—both vs. competitors and in the market overall.

**Step 3.1: Competitor Content Mapping**

For each competitor, categorize their content:

```
web_search("site:competitor.com [primary topic]")
```

**Document:**
- Main topic categories covered
- Estimated number of pieces per category
- Notable content series or hubs
- Content you have vs. don't have

**Output: Content Coverage Matrix**

| Topic Category | Competitor A | Competitor B | Competitor C | Your Site | Gap? |
|----------------|--------------|--------------|--------------|-----------|------|
| [Topic 1] | ✅ 12 pieces | ✅ 8 pieces | ✅ 5 pieces | ❌ 0 | YES |
| [Topic 2] | ✅ 6 pieces | ❌ 0 | ✅ 3 pieces | ✅ 2 pieces | Partial |

**Step 3.2: Standard Content Gap (vs. Competitors)**

Identify topics where:
- **All competitors rank, you don't** = Critical gap
- **Multiple competitors rank, you don't** = Important gap
- **One competitor ranks, you don't** = Opportunity gap

**Classification:**

| Gap Type | Definition | Priority |
|----------|------------|----------|
| Missing | Competitors cover extensively, you have nothing | High |
| Weak | You have content but competitors significantly outrank | Medium |
| Partial | You cover some subtopics but not comprehensively | Medium |
| Format | Competitors use different format (video, tool, etc.) | Varies |

**Step 3.3: Double Content Gap (Blue Ocean Analysis)**

**Critical Addition:** Find topics that BOTH you AND competitors are missing.

**Discovery Methods:**

1. **People Also Ask Mining**
   - Search core topics and expand PAA boxes
   - Note questions without satisfying answers in results
   - These are untapped demand signals

2. **Related Searches Analysis**
   - Bottom of SERP "Related searches"
   - Check if any lead to weak/thin content

3. **Pain Point Indicators**
   - If you have access: customer support tickets, sales call notes
   - Community mining: Reddit, forums, Discord for unanswered questions
   - Comment sections on competitor content

4. **SERP Quality Assessment**
   - For potential topics, analyze top 3 results
   - If results are outdated, thin, or off-topic = opportunity

**Blue Ocean Criteria:**
- Real pain point (heard from multiple sources)
- SERP shows unsatisfying results
- You can provide genuinely better/different value
- Aligns with your expertise and product
- Serves users who could become customers

**Output: Double Content Gap Opportunities**

| Topic/Question | Evidence of Demand | Current SERP Quality | Our Advantage | Priority |
|----------------|-------------------|---------------------|---------------|----------|

**Step 3.4: Intent Gap Analysis**

Check if you're missing entire intent categories:

| Intent Type | Your Coverage | Competitor Coverage | Gap? |
|-------------|---------------|--------------------|----- |
| Informational (how/what/why) | | | |
| Commercial (best/compare/review) | | | |
| Transactional (buy/pricing/get) | | | |
| Navigational (brand + keyword) | | | |

---

### STAGE 4: Content Inventory Assessment

**Purpose:** Evaluate existing content and determine action for each piece.

**Step 4.1: Content Collection**

If site has existing content, list all content pages:
- URL
- Title
- Publish date (if visible)
- Topic/category
- Estimated word count

**Step 4.2: Performance Classification**

If GSC data available, classify each page:

| Performance Tier | Criteria | Typical Action |
|------------------|----------|----------------|
| Top Performers | Position 1-3, consistent traffic | KEEP (monitor) |
| Near Winners | Position 4-10, good impressions | IMPROVE (Workflow 4) |
| Striking Distance | Position 11-20, moderate impressions | IMPROVE (priority) |
| Underperformers | Position 21-50, low traffic | EVALUATE (improve or remove) |
| Zero Traffic | No impressions for 6+ months | EVALUATE (consolidate or remove) |

**Step 4.3: KICP Decision Tree**

Apply this decision tree to each piece of content:

```
START: Is the content still relevant to our business?
│
├─ NO → Is there a redirect target? 
│        ├─ YES → REMOVE + 301 redirect
│        └─ NO → REMOVE (410 or soft 404)
│
└─ YES → Is it performing adequately?
         │
         ├─ YES → KEEP (monitor annually)
         │
         └─ NO → Is the core topic still relevant?
                  │
                  ├─ NO → Is there similar content to combine?
                  │        ├─ YES → CONSOLIDATE into stronger piece
                  │        └─ NO → REMOVE + redirect
                  │
                  └─ YES → Can it be meaningfully improved?
                           ├─ YES → IMPROVE (refresh content)
                           └─ NO → REMOVE + redirect
```

**Step 4.4: Content Actions Summary**

| Action | Count | Description |
|--------|-------|-------------|
| KEEP | | Pages performing well, monitor only |
| IMPROVE | | Pages with optimization potential (→ Workflow 4) |
| CONSOLIDATE | | Multiple weak pages to merge into one strong page |
| PRUNE | | Pages to remove or redirect |

**For IMPROVE pages, note specific opportunities:**
- Title/meta optimization needed
- Content expansion needed
- Internal linking gaps
- Outdated information
- Missing SERP feature optimization

**For CONSOLIDATE pages, identify:**
- Target page (the "winner" to merge into)
- Pages to merge
- Redirect mapping

---

### STAGE 5: Opportunity Prioritization

**Purpose:** Rank all opportunities by Impact × Effort to create actionable roadmap.

**Step 5.1: Compile All Opportunities**

Gather opportunities from all stages:

| Source | Opportunity Type | Count |
|--------|-----------------|-------|
| Positioning (Stage 2) | Striking distance optimizations | |
| Content Gap (Stage 3) | Competitor gaps to fill | |
| Content Gap (Stage 3) | Blue ocean opportunities | |
| Content Inventory (Stage 4) | Content improvements | |
| Content Inventory (Stage 4) | Consolidations | |

**Step 5.2: Score Each Opportunity**

**Impact Score (1-5):**
- 5: High traffic potential + high conversion relevance
- 4: Good traffic potential + good relevance
- 3: Moderate traffic + moderate relevance
- 2: Low traffic but strategic value
- 1: Minimal expected impact

**Effort Score (1-5):**
- 5: Minimal effort (quick optimization, <1 day)
- 4: Low effort (minor content update, 1-2 days)
- 3: Moderate effort (significant update, 3-5 days)
- 2: High effort (new content piece, 1-2 weeks)
- 1: Major effort (pillar content, multiple weeks)

**Priority Score = Impact × Effort**

| Priority | Score Range | Action |
|----------|-------------|--------|
| Tier 1 | 15-25 | Execute immediately |
| Tier 2 | 10-14 | Schedule for next sprint |
| Tier 3 | 5-9 | Plan for future |
| Tier 4 | 1-4 | Deprioritize or eliminate |

**Step 5.3: Create Prioritized Roadmap**

**Tier 1: Quick Wins (This Week)**
- Striking distance optimizations (→ Workflow 4)
- Meta title/description updates
- Internal linking fixes
- Content consolidations

**Tier 2: Short-Term (This Month)**
- Content improvements requiring moderate effort
- Blue ocean content opportunities
- Key competitor gap content

**Tier 3: Medium-Term (This Quarter)**
- New content pillars
- Topic cluster buildout
- Authority building content

**Tier 4: Long-Term (Next Quarter+)**
- Major site restructuring
- Comprehensive link building
- New content formats (tools, videos)

---

### STAGE 6: Output Generation

**Purpose:** Compile all findings into actionable audit report.

Generate the complete audit artifact following the Output Format Template below.

---

## Output Format: Markdown Artifact Template

```markdown
# SEO Audit Report: [Website Domain]

**Audit Date:** [current date]
**Primary Topic/Niche:** [from input]
**Target Audience:** [from input]

---

## Executive Summary

[2-3 paragraph summary of key findings, including:]
- Current positioning status (strong/moderate/weak)
- Most critical gaps identified
- Biggest quick win opportunities
- Recommended priority focus

---

## Part 1: Positioning Evaluation

### SEO Competitor Landscape

| Competitor | Domain | Estimated Traffic | Content Volume | Strengths |
|------------|--------|-------------------|----------------|-----------|
[competitor data]

### SERP Landscape Analysis

| Keyword | Your Position | Top Competitor | SERP Features | Content Type Winning |
|---------|---------------|----------------|---------------|---------------------|
[keyword position data]

### Position Distribution

| Range | Count | Implication |
|-------|-------|-------------|
| 1-3 | | Defend |
| 4-10 | | Quick win candidates |
| 11-20 | | Striking distance (priority) |
| 21-50 | | Requires investment |
| Not ranking | | New content needed |

### Competitive Advantages & Disadvantages

**Advantages:**
- [list advantages]

**Disadvantages:**
- [list disadvantages]

---

## Part 2: Content Gap Analysis

### Content Coverage Matrix

| Topic Category | Comp A | Comp B | Comp C | You | Gap Status |
|----------------|--------|--------|--------|-----|------------|
[coverage data]

### Standard Content Gaps (vs. Competitors)

**Critical Gaps (all competitors have, you don't):**
1. [gap 1]
2. [gap 2]

**Important Gaps (most competitors have, you don't):**
1. [gap 1]
2. [gap 2]

### Blue Ocean Opportunities (Market Gaps)

| Topic/Question | Demand Evidence | SERP Quality | Priority |
|----------------|-----------------|--------------|----------|
[blue ocean opportunities]

### Intent Coverage Gaps

| Intent Type | Your Coverage | Gap? |
|-------------|---------------|------|
| Informational | | |
| Commercial | | |
| Transactional | | |

---

## Part 3: Content Inventory Assessment

### Current Content Overview

- **Total content pages:** [X]
- **Estimated total words:** [X]
- **Average publish age:** [X months]

### Performance Distribution

| Status | Count | Percentage |
|--------|-------|------------|
| Top Performers (pos 1-3) | | |
| Near Winners (pos 4-10) | | |
| Striking Distance (pos 11-20) | | |
| Underperformers (pos 21-50) | | |
| Zero Traffic | | |

### Content Actions Required

| Action | Count | Priority |
|--------|-------|----------|
| KEEP | | Low (monitor) |
| IMPROVE | | High |
| CONSOLIDATE | | Medium |
| PRUNE | | Medium |

### Pages to Improve (Workflow 4 Candidates)

| URL | Current Position | Issue | Recommended Action |
|-----|------------------|-------|-------------------|
[improvement candidates]

### Pages to Consolidate

| Target Page | Pages to Merge | Redirect Plan |
|-------------|----------------|---------------|
[consolidation plan]

### Pages to Prune

| URL | Reason | Action |
|-----|--------|--------|
[prune list]

---

## Part 4: Prioritized Opportunity Roadmap

### Tier 1: Quick Wins (Execute This Week)

| Opportunity | Type | Impact | Effort | Score | Action |
|-------------|------|--------|--------|-------|--------|
[tier 1 items]

**Recommended First Action:** [specific actionable recommendation]

### Tier 2: Short-Term (This Month)

| Opportunity | Type | Impact | Effort | Score | Action |
|-------------|------|--------|--------|-------|--------|
[tier 2 items]

### Tier 3: Medium-Term (This Quarter)

| Opportunity | Type | Impact | Effort | Score |
|-------------|------|--------|--------|-------|
[tier 3 items]

### Tier 4: Long-Term (Next Quarter+)

| Opportunity | Type | Impact | Effort | Score |
|-------------|------|--------|--------|-------|
[tier 4 items]

---

## Part 5: Next Steps

### Immediate Actions

1. **[Action 1]** - [specific instruction]
2. **[Action 2]** - [specific instruction]
3. **[Action 3]** - [specific instruction]

### Workflow Routing

**For Existing Content Optimization:**
→ Take "Pages to Improve" list to **Workflow 4: Rank Enhancement**

**For New Content Creation:**
→ Take "Content Gap" topics to **Workflow 1: Keyword Discovery**
→ Research [specific topic] as primary keyword

**For Content Consolidation:**
→ Execute consolidation plan, then route merged pages to Workflow 4

### Recommended Workflow 1 Primary Keywords

Based on gap analysis, research these keywords first:

1. **[keyword 1]** - [rationale]
2. **[keyword 2]** - [rationale]
3. **[keyword 3]** - [rationale]

---

## Audit Metadata

- **Audit Type:** Comprehensive SEO Audit
- **Methodology:** Three Pillars Framework + KICP Decision Tree
- **Data Sources:** [list sources used]
- **Limitations:** [note any data gaps]

---

*Generated by Workflow 0: SEO Audit & Opportunity Analysis*
```

---

## Integration with Other Workflows

### Feeding Workflow 1 (Keyword Discovery)

The audit identifies primary keywords for research:

**From Content Gaps:**
- Topics competitors cover that you don't → research as primary keywords
- Blue ocean opportunities → research to validate demand

**From Positioning:**
- Topic clusters where you're weakest → research for expansion

**Handoff Format:**
```
Primary Keyword: [from audit gap analysis]
Rationale: [why this keyword matters based on audit]
Priority: [Tier 1/2/3 from prioritization]
```

### Feeding Workflow 4 (Rank Enhancement)

The audit identifies pages for optimization:

**From Content Inventory:**
- Pages marked IMPROVE → direct candidates for Workflow 4
- Striking distance pages (position 11-20) → priority optimization
- Near winners (position 4-10) → quick win optimization

**Handoff Format:**
```
URL: [page URL]
Current Position: [from GSC or estimate]
Target Keyword: [primary keyword for page]
Issues Identified: [from audit]
Priority: [Tier 1/2/3]
```

### Audit Cadence

| Audit Type | Frequency | Scope |
|------------|-----------|-------|
| Full Audit | Annually | Complete 6-stage process |
| Quarterly Check | Every 3 months | Stages 2 + 4 only (positioning + inventory) |
| Monthly Monitor | Monthly | GSC trends + top performers check |

---

## Execution Checklist

Before generating the audit artifact, ensure:

- [ ] Website URL and business context captured
- [ ] 3-5 SEO competitors identified
- [ ] SERP landscape analyzed for 10-15 core keywords
- [ ] Competitive scorecard completed
- [ ] Position distribution mapped
- [ ] Content coverage matrix created
- [ ] Standard content gaps identified
- [ ] Blue ocean opportunities explored
- [ ] Intent coverage assessed
- [ ] Content inventory collected (if applicable)
- [ ] KICP decision tree applied to all content
- [ ] All opportunities scored (Impact × Effort)
- [ ] Prioritized roadmap created with 4 tiers
- [ ] Workflow routing recommendations provided
- [ ] Primary keywords for Workflow 1 identified

---

## Example Execution

### User Input
```
Website: https://example-saas.com
Business: Project management software for remote teams
Primary Topic: Remote team productivity
Target Audience: Team leads and managers at companies with 10-100 remote employees
Goals: Increase organic signups, establish thought leadership
Competitors: monday.com, asana.com, notion.so
```

### Claude Response
```
I'll conduct a comprehensive SEO audit for example-saas.com focusing on remote team productivity.

[Executes web_search for core topic queries]
[Identifies SERP landscape and competitor positions]
[Maps content coverage across competitors]
[Identifies content gaps and blue ocean opportunities]
[Assesses existing content with KICP framework]
[Scores and prioritizes all opportunities]

[Generates complete audit artifact]

**Key Findings:**
- You're invisible for 80% of core keywords (competitors dominate)
- Biggest gap: No comparison/alternative content (competitors have 10+ pieces each)
- Blue ocean opportunity: "Async communication for remote teams" has weak SERP
- 15 existing pages identified; 8 need improvement, 3 should consolidate

**Recommended First Action:**
Run Workflow 4 on your "Remote Team Guide" page (position 12 → potential top 5)

**Recommended Workflow 1 Keywords:**
1. "project management for remote teams" (competitor gap)
2. "async communication tools" (blue ocean)
3. "remote team productivity tips" (intent gap - informational)
```

---

## Summary

Workflow 0 is the **strategic foundation** of the SEO system. It:

✅ Precedes keyword research with strategic audit  
✅ Evaluates competitive positioning systematically  
✅ Identifies both competitor gaps AND market gaps (Blue Ocean)  
✅ Assesses existing content with KICP decision tree  
✅ Prioritizes opportunities by Impact × Effort  
✅ Routes findings to appropriate downstream workflow (W1 or W4)  
✅ Uses Three Pillars framework (Content, Technical, Backlinks)  
✅ Produces actionable roadmap with 4 priority tiers  
✅ Execution time: 15-30 minutes depending on site complexity  
✅ Recommended cadence: Full audit annually, quarterly checks  

**Key Innovation:** Transforms SEO from "keyword-first" to "strategy-first" by auditing what exists before researching what to create.

**Philosophical Shift:**
> "You're not ranking in a vacuum. Ranking is actually about outranking your search competitors." — Lidia Infante

Workflow 0 ensures you understand the battlefield before deploying resources.

---

*End of Workflow 0 Documentation*
*Version 1.0 — December 2025*
