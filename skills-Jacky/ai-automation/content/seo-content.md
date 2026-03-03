# AI for SEO Content at Scale

> Complete guide to using AI for SEO content production: keyword research, content briefs, optimization, and programmatic SEO.

---

## Table of Contents

1. [AI SEO Strategy](#ai-seo-strategy)
2. [Keyword Research with AI](#keyword-research-with-ai)
3. [Content Brief Generation](#content-brief-generation)
4. [SEO Writing Workflows](#seo-writing-workflows)
5. [On-Page Optimization](#on-page-optimization)
6. [Programmatic SEO](#programmatic-seo)
7. [Internal Linking Automation](#internal-linking-automation)
8. [Quality Control for SEO](#quality-control-for-seo)

---

## AI SEO Strategy

### The SEO Content Challenge

Traditional SEO content production faces:
- High cost per article ($150-500)
- Long production time (1-4 weeks)
- Limited scalability
- Quality inconsistency
- Difficult to iterate

### AI-Powered SEO Benefits

| Metric | Traditional | AI-Assisted | AI-Primary |
|--------|-------------|-------------|------------|
| Time to publish | 2 weeks | 3 days | 1 day |
| Cost per 2000 words | $300 | $75 | $25 |
| Articles per month | 4 | 20 | 50+ |
| Quality consistency | Variable | High | Medium-High |
| Scalability | Low | Medium | High |

### When to Use Each Approach

**AI-Primary (minimal human input):**
- Informational content
- Product descriptions
- FAQ pages
- Directory listings
- Data-driven content

**AI-Assisted (significant human input):**
- Thought leadership
- Original research
- Expert roundups
- Case studies
- Brand content

**Human-Primary (AI assistance only):**
- News commentary
- Opinion pieces
- Personal stories
- Sensitive topics
- Legal/medical advice

---

## Keyword Research with AI

### Expanding Seed Keywords

**Prompt:**
```
I'm doing keyword research for [NICHE]. 

Starting keyword: "[SEED KEYWORD]"

Generate:
1. 20 related long-tail keywords (3-5 words)
2. 10 question-based keywords (what, how, why, when)
3. 10 comparison keywords ([X] vs [Y])
4. 10 "best" keywords (best [X] for [Y])
5. 5 commercial intent keywords (buy, price, review)

For each keyword, estimate:
- Search intent (informational/commercial/transactional)
- Difficulty (low/medium/high)
- Priority for a new site (1-5)

Format as a table.
```

### Keyword Clustering

**Prompt:**
```
Cluster these keywords by topic and search intent:

[LIST OF KEYWORDS]

Group into clusters where:
- Keywords in same cluster target same page
- Each cluster has 1 primary keyword, multiple secondary
- Note the search intent for each cluster

Output as:
Cluster Name: [Name]
Primary: [keyword]
Secondary: [list]
Intent: [intent]
Suggested URL: [/path]
```

### Content Gap Analysis

**Prompt:**
```
I'm creating content for [MY SITE] competing with [COMPETITOR].

Their top pages are:
[LIST OF COMPETITOR PAGES]

Based on these topics, identify:
1. Topics they cover that I should also cover
2. Angle they're missing that I could own
3. Long-tail opportunities they've ignored
4. Content types they haven't created (guides, tools, etc.)

For each opportunity, rate priority (1-5) and explain why.
```

### Keyword Difficulty Assessment

**Prompt:**
```
For this keyword: "[KEYWORD]"

Based on your knowledge of typical search results:

1. What type of pages typically rank? (commercial, informational, etc.)
2. What authority level is needed? (new site can compete / need authority)
3. What content format ranks? (listicle, guide, tool, etc.)
4. Estimated content length needed
5. Key topics to cover
6. Featured snippet opportunity? (yes/no, type)
```

---

## Content Brief Generation

### Comprehensive Brief Prompt

```
Create an SEO content brief for:

TARGET KEYWORD: [keyword]
SECONDARY KEYWORDS: [list]
SEARCH INTENT: [informational/commercial/transactional]
WORD COUNT TARGET: [number]
COMPETITOR URLS: [top 3 ranking]

Analyze the keyword and generate:

## TITLE OPTIONS (5)
- Include keyword naturally
- Under 60 characters
- Click-worthy

## META DESCRIPTION
- 150-160 characters
- Include keyword
- Clear value proposition
- Call to action

## CONTENT STRUCTURE

### H1
[Title with keyword]

### H2 Sections
For each section:
- H2 heading
- Key points to cover (3-5 bullets)
- Word count target
- Keywords to include
- Questions to answer

### FAQ Section
[5 questions from "People Also Ask"]

## KEYWORD USAGE
- Primary keyword: [X] times naturally
- Secondary keywords: [list with frequency]
- LSI keywords: [list]

## INTERNAL LINKING
- Link to: [existing relevant pages]
- Anchor text suggestions

## EXTERNAL SOURCES
- Stats to cite
- Authoritative sources to reference

## FEATURED SNIPPET OPTIMIZATION
- Target type: [paragraph/list/table]
- Content format for snippet

## VISUAL ASSETS
- Images needed
- Suggested alt text with keywords
```

### Brief Automation Workflow

```yaml
workflow: SEO Brief Generator

nodes:
  - Trigger: Airtable new keyword record
  
  - HTTP: Fetch SERP data
      url: SerpAPI or similar
      query: {{ keyword }}
      
  - HTTP: Fetch competitor content
      for each: top 3 results
      extract: headings, word count, topics
      
  - Anthropic: Generate brief
      prompt: [comprehensive brief prompt]
      inputs: keyword, serp_data, competitor_data
      
  - Anthropic: Extract People Also Ask
      prompt: "List common questions for: {{ keyword }}"
      
  - Merge: Combine all data
  
  - Notion: Create brief page
      database: Content Briefs
      properties: title, keyword, brief_content
      
  - Slack: Notify content team
```

### Brief Quality Checklist

```markdown
## Brief Quality Check

### Keyword Analysis
- [ ] Primary keyword clearly identified
- [ ] Secondary keywords listed with frequency
- [ ] Search intent correctly identified
- [ ] Difficulty assessment included

### Structure
- [ ] H1 includes primary keyword
- [ ] H2s cover all major subtopics
- [ ] Logical flow of information
- [ ] FAQ section with real questions

### Optimization
- [ ] Meta title under 60 chars
- [ ] Meta description 150-160 chars
- [ ] Internal linking opportunities identified
- [ ] External sources suggested

### Differentiation
- [ ] Unique angle identified
- [ ] Content gaps addressed
- [ ] Better than competition in [specific way]
```

---

## SEO Writing Workflows

### Full Article Generation

**Step 1: Section-by-Section Writing**

```
Write the [SECTION NAME] section for this article:

ARTICLE TOPIC: [topic]
TARGET KEYWORD: [keyword]
SECTION OUTLINE:
[paste outline for this section]

PREVIOUS SECTIONS SUMMARY:
[brief summary for context]

REQUIREMENTS:
- Length: [X] words
- Include keywords: [list]
- Answer: [specific questions]
- Tone: [describe tone]
- Include: [examples, stats, etc.]

Write naturally, not like AI. Use specific examples.
Avoid clichés and filler phrases.
```

**Step 2: Assembly and Transitions**

```
Review these sections and:
1. Ensure smooth transitions between sections
2. Remove any redundancy
3. Add transitional phrases where needed
4. Verify keyword placement is natural
5. Check that all key points are covered

Sections:
[paste all sections]

Return the improved, unified article.
```

**Step 3: SEO Optimization Pass**

```
Optimize this article for SEO:

ARTICLE:
[paste article]

PRIMARY KEYWORD: [keyword]
SECONDARY KEYWORDS: [list]

Tasks:
1. Ensure keyword in first 100 words
2. Verify keyword density (1-2%)
3. Add secondary keywords naturally
4. Optimize headings for keywords
5. Add internal linking placeholder text
6. Suggest image alt text
7. Write meta description

Return the optimized article with changes noted.
```

### Bulk Content Production

```python
class SEOContentPipeline:
    def __init__(self, llm, brief_db, content_db):
        self.llm = llm
        self.briefs = brief_db
        self.content = content_db
    
    async def produce_article(self, brief_id: str):
        # Get brief
        brief = await self.briefs.get(brief_id)
        
        # Generate sections
        sections = []
        for section in brief.outline:
            content = await self.write_section(
                section=section,
                context=sections,  # Previous sections for context
                keyword=brief.primary_keyword
            )
            sections.append(content)
        
        # Assemble article
        article = await self.assemble(sections)
        
        # Optimize
        optimized = await self.optimize(article, brief)
        
        # Quality check
        quality = await self.quality_check(optimized, brief)
        
        # Store
        await self.content.create({
            "brief_id": brief_id,
            "content": optimized,
            "quality_score": quality.score,
            "status": "draft" if quality.needs_review else "ready"
        })
        
        return optimized
    
    async def write_section(self, section, context, keyword):
        prompt = f"""
        Write the section: {section.title}
        
        Outline: {section.points}
        Target length: {section.word_count} words
        Keyword: {keyword}
        
        Previous context: {summarize(context)}
        """
        
        return await self.llm.generate(prompt)
```

---

## On-Page Optimization

### Title Tag Optimization

**Prompt:**
```
Generate 10 SEO title tag options for:

KEYWORD: [keyword]
TOPIC: [topic]
BRAND: [brand name]
CURRENT TITLE: [if optimizing existing]

Requirements:
- Under 60 characters (include count)
- Keyword near the beginning
- Compelling for clicks
- Match search intent

Include variety:
- Question format
- List/number format
- How-to format
- Benefit-focused
- Curiosity-driven

Format: Title (XX chars)
```

### Meta Description Optimization

**Prompt:**
```
Write 5 meta description options for:

KEYWORD: [keyword]
PAGE CONTENT: [summary]
GOAL: [traffic/clicks/conversions]
COMPETITOR META: [what competitors use]

Requirements:
- 150-160 characters exactly
- Include keyword naturally
- Clear value proposition
- Include call to action
- Unique from competitors

Format: Description (XXX chars)
```

### Header Optimization

**Prompt:**
```
Optimize these headings for SEO:

CURRENT HEADINGS:
[list of H2s/H3s]

TARGET KEYWORD: [keyword]
SECONDARY KEYWORDS: [list]

For each heading:
1. Include keyword or variation where natural
2. Keep descriptive and useful
3. Maintain logical hierarchy
4. Make scannable

Return optimized headings with explanations.
```

### Content Optimization Workflow

```yaml
workflow: Content Optimizer

input: article_url, target_keyword

steps:
  - fetch: Get page content
  
  - analyze: 
      - Current keyword density
      - Heading structure
      - Word count
      - Internal/external links
      
  - compare:
      - Get top 3 ranking pages
      - Extract their structure
      - Identify gaps
      
  - optimize:
      - Generate improved title
      - Generate improved meta
      - Suggest heading changes
      - Identify keyword opportunities
      - Suggest internal links
      
  - output: Optimization report with before/after
```

---

## Programmatic SEO

### What is Programmatic SEO?

Creating large numbers of pages from data and templates:
- City + Service pages (e.g., "Plumbers in [City]")
- Comparison pages (e.g., "[Tool A] vs [Tool B]")
- Definition pages (e.g., "What is [Term]")
- Stats pages (e.g., "[Topic] Statistics 2024")

### Template-Based Generation

**Template:**
```
Create content for a [SERVICE] in [CITY] page.

DATA:
Service: {{ service_name }}
City: {{ city_name }}
State: {{ state }}
Population: {{ population }}
Local data: {{ local_stats }}

TEMPLATE STRUCTURE:

# [SERVICE] in [CITY], [STATE]

## Introduction
[2-3 sentences about the service in this city]

## Why Choose [SERVICE] in [CITY]
[3-4 local reasons]

## Our [SERVICE] Services
[List services with descriptions]

## [CITY] [SERVICE] Statistics
[Use local_stats data]

## Service Areas in [CITY]
[List neighborhoods/areas]

## FAQ
[5 city-specific questions]

Generate unique, valuable content for this combination.
Avoid generic filler. Include specific local details.
```

### Programmatic SEO Pipeline

```python
class ProgrammaticSEO:
    def __init__(self, data_source, template_engine, llm):
        self.data = data_source
        self.templates = template_engine
        self.llm = llm
    
    async def generate_pages(self, page_type: str):
        # Get combinations
        combos = await self.data.get_combinations(page_type)
        
        # Generate each page
        pages = []
        for combo in combos:
            # Get template
            template = self.templates.get(page_type)
            
            # Fill template with data
            base_content = template.fill(combo)
            
            # Enhance with AI
            enhanced = await self.llm.generate(f"""
                Enhance this content to be unique and valuable:
                
                Base content:
                {base_content}
                
                Make it:
                - Locally relevant
                - Naturally written
                - Unique from other pages
                - Valuable to readers
            """)
            
            pages.append({
                "url": self.generate_url(combo),
                "content": enhanced,
                "meta": await self.generate_meta(combo),
                "data": combo
            })
        
        return pages
    
    async def generate_at_scale(self, page_type: str, batch_size: int = 50):
        combos = await self.data.get_combinations(page_type)
        
        for batch in chunks(combos, batch_size):
            pages = await asyncio.gather(*[
                self.generate_page(combo) for combo in batch
            ])
            
            await self.publish(pages)
            await asyncio.sleep(1)  # Rate limiting
```

### Programmatic SEO Best Practices

**Do:**
- Add genuine value on each page
- Include unique data/insights
- Create logical URL structure
- Interlink related pages
- Monitor for thin content penalties

**Don't:**
- Generate pure template content
- Create pages without search volume
- Ignore page quality
- Build too fast (looks spammy)
- Neglect mobile experience

---

## Internal Linking Automation

### Link Opportunity Detection

**Prompt:**
```
Find internal linking opportunities in this article:

ARTICLE:
[paste article content]

EXISTING PAGES ON OUR SITE:
[list of page titles and URLs]

For each opportunity, provide:
1. Anchor text (from the article)
2. Target URL
3. Context (sentence containing anchor)
4. Relevance score (1-10)

Only suggest highly relevant links. Quality over quantity.
```

### Automatic Link Insertion

```python
class InternalLinker:
    def __init__(self, site_pages, llm):
        self.pages = site_pages
        self.llm = llm
        self.embeddings = self.build_embeddings()
    
    def build_embeddings(self):
        """Create embeddings for all site pages"""
        embeddings = {}
        for page in self.pages:
            embeddings[page.url] = embed(page.title + " " + page.summary)
        return embeddings
    
    async def find_opportunities(self, content: str) -> list:
        # Extract potential anchor texts
        sentences = content.split(".")
        
        opportunities = []
        for sentence in sentences:
            # Find relevant pages
            sentence_embedding = embed(sentence)
            matches = self.find_similar(sentence_embedding, top_k=3)
            
            for match in matches:
                if match.score > 0.8:
                    # Use AI to find best anchor text
                    anchor = await self.find_anchor(sentence, match.page)
                    if anchor:
                        opportunities.append({
                            "anchor": anchor,
                            "url": match.page.url,
                            "context": sentence,
                            "score": match.score
                        })
        
        return opportunities
    
    async def find_anchor(self, sentence: str, target_page) -> str:
        prompt = f"""
        Find a natural anchor text in this sentence to link to "{target_page.title}":
        
        Sentence: {sentence}
        Target page topic: {target_page.summary}
        
        Requirements:
        - Must be exact text from the sentence
        - Must be 2-5 words
        - Must be relevant to target page
        
        Return just the anchor text, or "NONE" if no good fit.
        """
        
        result = await self.llm.generate(prompt)
        return None if result == "NONE" else result
```

### Link Building at Scale

```yaml
workflow: Internal Link Builder

trigger: Schedule - Weekly

steps:
  - Get all published content
  
  - Get all potential link targets
  
  - For each piece of content:
      - Find linking opportunities (AI)
      - Score by relevance
      - Filter: only high relevance
      
  - Deduplicate across content
  
  - Generate report:
      - Orphan pages (no links to them)
      - Over-linked pages
      - Missing opportunities
      
  - Create tasks for implementation
  
  - Send weekly report to SEO team
```

---

## Quality Control for SEO

### SEO Quality Scoring

```python
def score_seo_content(article, keyword, brief):
    scores = {}
    
    # Keyword presence
    scores["keyword_in_title"] = keyword.lower() in article.title.lower()
    scores["keyword_in_h1"] = keyword.lower() in article.h1.lower()
    scores["keyword_in_first_100"] = keyword.lower() in article.content[:500].lower()
    scores["keyword_density"] = calculate_density(article.content, keyword)
    
    # Structure
    scores["has_h2s"] = len(article.h2s) >= 3
    scores["has_faq"] = "faq" in article.content.lower() or "?" in article.content
    scores["word_count"] = len(article.content.split()) >= brief.target_word_count * 0.9
    
    # Optimization
    scores["meta_title_length"] = 50 <= len(article.meta_title) <= 60
    scores["meta_desc_length"] = 150 <= len(article.meta_description) <= 160
    scores["has_internal_links"] = article.internal_links >= 3
    scores["has_external_links"] = article.external_links >= 2
    
    # Quality
    scores["readability"] = calculate_readability(article.content) > 60
    scores["unique_content"] = check_plagiarism(article.content) < 5
    
    # Calculate overall
    total = sum(1 for v in scores.values() if v) / len(scores) * 100
    
    return {
        "score": total,
        "details": scores,
        "needs_improvement": [k for k, v in scores.items() if not v]
    }
```

### Pre-Publish Checklist

```markdown
## SEO Content Pre-Publish Check

### Technical SEO
- [ ] URL is SEO-friendly (short, with keyword)
- [ ] Title tag optimized (under 60 chars, keyword present)
- [ ] Meta description optimized (150-160 chars)
- [ ] H1 contains primary keyword
- [ ] Image alt text includes keywords
- [ ] Schema markup added (if applicable)

### Content Quality
- [ ] Meets word count target
- [ ] Answers search intent
- [ ] Better than ranking competitors
- [ ] Includes unique value/data
- [ ] No factual errors
- [ ] Proper grammar and spelling

### On-Page Optimization
- [ ] Keyword in first 100 words
- [ ] Keyword density 1-2%
- [ ] Secondary keywords included
- [ ] Headers include keywords naturally
- [ ] Content is scannable

### Linking
- [ ] 3+ internal links added
- [ ] 2+ external links to authorities
- [ ] Anchor text is descriptive
- [ ] No broken links

### User Experience
- [ ] Content is scannable
- [ ] Has clear structure
- [ ] Mobile-friendly formatting
- [ ] Fast loading (optimize images)
```

---

## Summary

### SEO Content Production Metrics

| Metric | Manual | AI-Assisted | Improvement |
|--------|--------|-------------|-------------|
| Time per 2000 words | 8 hours | 2 hours | 75% faster |
| Cost per article | $300 | $50 | 83% cheaper |
| Articles per month | 4 | 20 | 5x more |
| SEO score average | 70 | 85 | 21% better |

### Recommended Workflow

1. **Keyword research:** Weekly AI-assisted research session
2. **Brief generation:** Automated from keyword list
3. **Content production:** Section-by-section AI generation
4. **Optimization:** AI optimization pass
5. **Human review:** Quality check and unique additions
6. **Publishing:** Automated formatting and scheduling
7. **Linking:** Monthly internal linking audit

See [../workflows/n8n/templates.md](../workflows/n8n/templates.md) for automation templates →
