# AI Content Strategy

> Strategic framework for AI-powered content: planning, governance, quality standards, and scaling content operations.

---

## Table of Contents

1. [Strategic Framework](#strategic-framework)
2. [Content Governance](#content-governance)
3. [Brand Voice with AI](#brand-voice-with-ai)
4. [Content Quality Standards](#content-quality-standards)
5. [Editorial Workflow](#editorial-workflow)
6. [Content Performance](#content-performance)
7. [Scaling Content Operations](#scaling-content-operations)
8. [Ethics and Disclosure](#ethics-and-disclosure)

---

## Strategic Framework

### The AI Content Spectrum

```
                 HUMAN INVOLVEMENT
         Low ◄──────────────────────► High
         
    ┌─────────────────────────────────────┐
    │  100% AI        Hybrid      Human   │
    │                                      │
    │  Data-driven    Blog       Thought  │
    │  reports        posts      leadership│
    │                                      │
    │  Product        Landing    Research │
    │  descriptions   pages      reports  │
    │                                      │
    │  Social         Email      Expert   │
    │  snippets       sequences  interviews│
    └─────────────────────────────────────┘
```

### Content Type Decision Matrix

| Content Type | Volume | Stakes | AI Role | Human Role |
|--------------|--------|--------|---------|------------|
| Blog (informational) | High | Medium | Draft + SEO | Edit + fact-check |
| Blog (thought leadership) | Low | High | Research | Write + voice |
| Landing pages | Medium | High | Draft variants | Strategy + copy |
| Email (marketing) | High | Medium | Generate variations | Select + approve |
| Email (transactional) | High | Low | Template generation | Setup + monitor |
| Social media | Very High | Low | Full generation | Schedule + engage |
| Product descriptions | Very High | Medium | Full generation | QA sample |
| Documentation | Medium | High | Draft + structure | Verify + maintain |
| Press releases | Low | Very High | Draft only | Heavy editing |
| Legal/compliance | Low | Critical | Never | Full human |

### AI Content Goals

**Primary goals:**
1. **Scale** - Produce more content without proportional headcount
2. **Speed** - Reduce time from idea to published
3. **Consistency** - Maintain quality across high volume
4. **Personalization** - Tailor content at scale
5. **Cost efficiency** - Lower cost per content piece

**Secondary goals:**
1. SEO coverage expansion
2. Content freshness maintenance
3. Multi-language/market expansion
4. A/B testing capacity
5. Content repurposing efficiency

### Strategic Content Planning

```yaml
content_strategy:
  
  audience_segments:
    - segment: Technical decision makers
      content_needs: Deep technical content, comparisons
      ai_role: Research, draft technical sections
      
    - segment: Business buyers
      content_needs: ROI content, case studies
      ai_role: Draft structure, generate variations
      
    - segment: End users
      content_needs: How-to guides, FAQs
      ai_role: High automation potential
  
  content_pillars:
    - pillar: Product education
      volume: 20 pieces/month
      ai_automation: 70%
      
    - pillar: Industry insights
      volume: 4 pieces/month
      ai_automation: 40%
      
    - pillar: Customer success
      volume: 2 pieces/month
      ai_automation: 20%
  
  channels:
    - blog: 16 posts/month
    - email: 8 campaigns/month
    - social: 60 posts/month
    - documentation: As needed
```

---

## Content Governance

### AI Content Policies

```markdown
# AI Content Policy

## Scope
This policy covers all content created with AI assistance published under [Company] name.

## Permitted Uses
- Draft generation for human review
- Content optimization and enhancement
- Idea generation and research
- Data analysis and summarization
- SEO optimization
- Social media post generation
- Email personalization

## Prohibited Uses
- Publishing AI content without human review for:
  - Customer-facing product documentation
  - Legal or compliance content
  - Medical or financial advice
  - News or factual reporting
- Generating content that:
  - Impersonates real individuals
  - Makes claims we cannot verify
  - Violates copyright
  - Contains misinformation

## Required Disclosures
- Internal: All AI-assisted content tagged in CMS
- External: [Company policy on disclosure]

## Quality Requirements
- All AI content must score 75+ on quality checklist
- Fact-checking required for all claims
- Brand voice audit for public content
- Legal review for sensitive topics

## Accountability
- Content owner responsible for final accuracy
- AI-generated content treated same as human content for liability
```

### Review and Approval Workflow

```yaml
workflow: Content Approval

levels:
  
  level_1_auto_approve:
    content_types:
      - Internal social posts
      - Email subject line tests
      - Meta description variations
    requirements:
      - AI quality score >= 85
      - No flagged content
      - Within brand guidelines
    
  level_2_single_review:
    content_types:
      - Blog posts (informational)
      - Marketing emails
      - Product descriptions
    requirements:
      - AI draft review
      - One editor approval
      - Quality checklist complete
    
  level_3_double_review:
    content_types:
      - Landing pages
      - Case studies
      - PR content
    requirements:
      - AI draft review
      - Editor approval
      - Subject matter expert review
    
  level_4_full_review:
    content_types:
      - Thought leadership
      - Legal mentions
      - Competitive claims
    requirements:
      - AI draft review
      - Editor approval
      - SME review
      - Legal/compliance review
```

### Content Audit Trail

```python
class ContentAudit:
    def log_content_creation(
        self,
        content_id: str,
        content_type: str,
        ai_involvement: dict,
        reviews: list,
        published_version: str
    ):
        return {
            "content_id": content_id,
            "created_at": datetime.utcnow(),
            "content_type": content_type,
            "ai_involvement": {
                "percentage": ai_involvement["percentage"],
                "models_used": ai_involvement["models"],
                "prompts_used": ai_involvement["prompt_ids"],
                "generations": ai_involvement["generation_count"],
                "human_edits": ai_involvement["edit_percentage"]
            },
            "review_chain": [
                {
                    "reviewer": r["reviewer"],
                    "role": r["role"],
                    "timestamp": r["timestamp"],
                    "action": r["action"],
                    "changes": r["changes"]
                }
                for r in reviews
            ],
            "final_version_hash": hash(published_version),
            "compliance_checks": self.run_compliance_checks(published_version)
        }
```

---

## Brand Voice with AI

### Voice Profile Creation

```
Analyze these writing samples to create a brand voice profile:

SAMPLES:
[Include 5-10 representative content pieces]

Create a detailed voice profile:

## TONE ATTRIBUTES

### Formality Spectrum
[1-10 scale, where 1 is casual, 10 is formal]
Score: _
Description: _

### Warmth Spectrum  
[1-10 scale, where 1 is distant, 10 is warm]
Score: _
Description: _

### Authority Spectrum
[1-10 scale, where 1 is humble, 10 is authoritative]
Score: _
Description: _

### Energy Spectrum
[1-10 scale, where 1 is calm, 10 is energetic]
Score: _
Description: _

## LANGUAGE PATTERNS

### Words We Use
[List of preferred words and phrases]

### Words We Avoid
[List of words/phrases to never use]

### Sentence Style
- Average length: _
- Complexity: _
- Active vs passive: _

### Punctuation Style
- Exclamation marks: _
- Em dashes: _
- Oxford comma: _

## STRUCTURAL PATTERNS

### Opening Style
How we typically start content: _

### Closing Style
How we typically end content: _

### Transition Phrases
Common transitions we use: _

## VOICE EXAMPLES

### How we say "Our product is good":
[Rewrite in our voice]

### How we say "Sign up now":
[Rewrite in our voice]

### How we handle bad news:
[Example in our voice]

## ANTI-EXAMPLES

### This sounds like us:
[Good example]

### This does NOT sound like us:
[Bad example - too formal/casual/etc.]
```

### Voice Application in Prompts

```
[System prompt for content generation]

VOICE GUIDELINES:

Tone:
- Conversational but knowledgeable
- Warm but not overly familiar
- Confident but not arrogant
- 7/10 on formality spectrum

Language:
- Use "you" and "your" frequently
- Contractions are good (you're, we'll, it's)
- Active voice whenever possible
- Short sentences, clear language

Words we USE:
- Simple, clear, straightforward, practical, powerful
- "Here's how", "Let's", "You can"

Words we AVOID:
- Leverage, synergy, utilize, revolutionary, game-changing
- Corporate jargon
- Superlatives without evidence

Structure:
- Lead with the benefit
- Use bullet points for lists
- Include examples
- End with clear action

Voice check: Read it aloud. Would a smart friend say this?
```

### Voice Consistency Scoring

```python
class VoiceScorer:
    def __init__(self, voice_profile):
        self.profile = voice_profile
        
    async def score_content(self, content: str) -> dict:
        prompt = f"""
        Score this content against the brand voice profile:
        
        CONTENT:
        {content}
        
        VOICE PROFILE:
        {self.profile}
        
        Score each dimension (0-100):
        
        1. Formality match: Does it match target formality?
        2. Warmth match: Does it match target warmth?
        3. Authority match: Does it match target authority?
        4. Vocabulary match: Uses preferred words, avoids forbidden?
        5. Structure match: Follows structural patterns?
        6. Overall voice: Does it "sound like us"?
        
        Return:
        {{
            "scores": {{
                "formality": 0,
                "warmth": 0,
                "authority": 0,
                "vocabulary": 0,
                "structure": 0,
                "overall": 0
            }},
            "average": 0,
            "issues": [],
            "suggestions": []
        }}
        """
        
        return await self.llm.generate(prompt)
```

---

## Content Quality Standards

### Quality Checklist

```markdown
## Content Quality Checklist

### ACCURACY (Must pass all)
- [ ] All facts verified with source
- [ ] Statistics include date and source
- [ ] Claims can be substantiated
- [ ] No contradictions with existing content
- [ ] Technical accuracy verified by SME (if applicable)

### COMPLETENESS (Score 4/5 minimum)
- [ ] Topic fully addressed
- [ ] Reader questions anticipated and answered
- [ ] Appropriate depth for audience
- [ ] Logical flow and structure
- [ ] Clear conclusion or next step

### BRAND ALIGNMENT (Score 4/5 minimum)
- [ ] Voice matches brand guidelines
- [ ] Tone appropriate for content type
- [ ] Visual style consistent (if applicable)
- [ ] Messaging aligns with positioning
- [ ] No competitor mentions (unless intentional)

### SEO (For applicable content)
- [ ] Target keyword included naturally
- [ ] Title optimized (keyword + compelling)
- [ ] Meta description optimized
- [ ] Headers use keywords where natural
- [ ] Internal links included
- [ ] Image alt text optimized

### READABILITY (All required)
- [ ] Flesch-Kincaid grade level appropriate
- [ ] Paragraphs ≤ 4 sentences
- [ ] Sentences average < 20 words
- [ ] Technical terms explained
- [ ] Scannable format (headers, bullets, etc.)

### LEGAL/COMPLIANCE (Must pass all)
- [ ] No trademark issues
- [ ] No copyright infringement
- [ ] Claims are defensible
- [ ] Disclosures included if required
- [ ] Approved for publication
```

### Quality Gates

```yaml
quality_gates:

  gate_1_automated:
    checks:
      - Spelling and grammar
      - Readability score
      - Keyword presence (SEO content)
      - Length requirements
      - Formatting validation
    action: Block if fails

  gate_2_ai_review:
    checks:
      - Voice score
      - Accuracy check against KB
      - Claim verification
      - Brand alignment
    action: Flag for human if score < 80

  gate_3_human_review:
    checks:
      - Editorial review
      - Fact verification
      - Final approval
    action: Required for all public content

  gate_4_compliance:
    triggers:
      - Legal terms mentioned
      - Competitive claims
      - Financial/medical content
    checks:
      - Legal review
      - Compliance approval
    action: Required before publish
```

---

## Editorial Workflow

### Content Pipeline

```yaml
pipeline:
  
  stage_1_ideation:
    duration: 1-2 days
    activities:
      - Keyword research
      - Topic selection
      - Content brief creation
    ai_role:
      - Generate topic ideas
      - Create initial briefs
    human_role:
      - Approve topics
      - Refine briefs
      - Assign priority
  
  stage_2_creation:
    duration: 2-3 days
    activities:
      - Research
      - Outline
      - Draft writing
    ai_role:
      - Research compilation
      - Outline generation
      - First draft
    human_role:
      - Guide research
      - Review outline
      - Edit draft
  
  stage_3_review:
    duration: 1-2 days
    activities:
      - Editorial review
      - SME review (if needed)
      - Revisions
    ai_role:
      - Revision suggestions
      - Grammar/style check
    human_role:
      - Quality review
      - Expert verification
      - Final edits
  
  stage_4_publish:
    duration: 1 day
    activities:
      - Final formatting
      - Asset preparation
      - Scheduling
    ai_role:
      - Meta generation
      - Social snippets
    human_role:
      - Final approval
      - Publish
```

### Editorial Calendar Automation

```yaml
workflow: Content Calendar Management

monthly:
  - Generate topic recommendations based on:
      - Keyword opportunities
      - Competitor content gaps
      - Trending topics
      - Business priorities
  - Create content briefs for approved topics
  - Assign to writers/AI pipeline

weekly:
  - Review content in pipeline
  - Generate missing briefs
  - Update calendar status
  - Send team digest

daily:
  - Check for publishing deadlines
  - Generate social promotion posts
  - Monitor published content performance
```

### Collaboration Model

```
ROLES AND RESPONSIBILITIES

Content Strategist:
- Define content pillars
- Approve topics
- Review performance
- Manage AI guidelines

Editor:
- Review AI drafts
- Maintain voice consistency
- Final quality approval
- Train AI on improvements

Writer (Human):
- Thought leadership content
- SME interviews
- Complex narratives
- AI prompt refinement

AI (Assistant):
- Research and data gathering
- First draft generation
- SEO optimization
- Variation generation
- Content repurposing
```

---

## Content Performance

### Performance Metrics

```yaml
metrics:

  production_metrics:
    - Content velocity: Pieces/month
    - Time to publish: Idea to live
    - Cost per piece: Total cost / pieces
    - AI efficiency: AI draft acceptance rate
    
  quality_metrics:
    - Quality score: Average content score
    - Edit rate: % of AI content edited
    - Rewrite rate: % requiring full rewrite
    - Voice score: Brand voice alignment
    
  engagement_metrics:
    - Page views: Traffic to content
    - Time on page: Engagement depth
    - Bounce rate: Content relevance
    - Social shares: Amplification
    - Comments: Community engagement
    
  business_metrics:
    - Conversion rate: Content to action
    - Lead generation: Leads from content
    - SEO ranking: Keyword positions
    - Revenue attribution: Revenue from content
```

### Performance Dashboard

```markdown
## Content Performance Dashboard

### Production This Month
- Published: 24 pieces
- AI-assisted: 20 (83%)
- Fully AI-generated: 8 (33%)
- Avg time to publish: 4.2 days
- Cost per piece: $47

### Quality Metrics
- Avg quality score: 82/100
- AI draft acceptance: 76%
- Voice score: 85/100
- Fact-check pass rate: 98%

### Engagement
- Total page views: 45,000
- Avg time on page: 3:24
- Social shares: 892
- Top performer: "AI Automation Guide" (8.5k views)

### Business Impact
- Leads generated: 156
- Conversion rate: 2.8%
- Revenue attributed: $23,400

### Trends
[Chart: Performance over time]

### Recommendations
1. Top topics to expand
2. Underperforming content to refresh
3. Optimization opportunities
```

### AI Content Attribution

```python
class ContentAttributionTracker:
    def track_content(self, content_id: str):
        return {
            "production": {
                "ai_draft_percentage": self.calculate_ai_percentage(content_id),
                "human_edit_percentage": self.calculate_edit_percentage(content_id),
                "time_saved": self.estimate_time_saved(content_id),
                "cost_savings": self.estimate_cost_savings(content_id)
            },
            "performance": {
                "quality_score": self.get_quality_score(content_id),
                "engagement_score": self.get_engagement_score(content_id),
                "seo_score": self.get_seo_score(content_id),
                "business_value": self.calculate_business_value(content_id)
            },
            "comparison": {
                "vs_human_average": self.compare_to_human_content(content_id),
                "vs_category_average": self.compare_to_category(content_id)
            }
        }
```

---

## Scaling Content Operations

### Scaling Stages

```
Stage 1: Pilot (0-10 pieces/month)
├── Test AI capabilities
├── Develop prompts
├── Establish quality baseline
└── Build team confidence

Stage 2: Growth (10-50 pieces/month)
├── Standardize workflows
├── Expand content types
├── Train team broadly
└── Refine quality gates

Stage 3: Scale (50-200 pieces/month)
├── Fully automated pipelines
├── Multi-market/language
├── Advanced personalization
└── Continuous optimization

Stage 4: Enterprise (200+ pieces/month)
├── Decentralized creation
├── Global content ops
├── AI content factory
└── Real-time content
```

### Automation Roadmap

```yaml
phase_1_quick_wins:
  duration: Month 1
  automate:
    - Social media post generation
    - Email subject line variations
    - Meta description generation
    - Content repurposing (blog → social)
  expected_impact:
    - 20 hours/month saved
    - 3x social content volume

phase_2_core_content:
  duration: Months 2-3
  automate:
    - Blog post first drafts
    - Product description generation
    - Email sequence drafts
    - SEO optimization
  expected_impact:
    - 60 hours/month saved
    - 2x blog content volume

phase_3_advanced:
  duration: Months 4-6
  automate:
    - Personalized content at scale
    - Multi-language content
    - Content performance optimization
    - Predictive content planning
  expected_impact:
    - 100 hours/month saved
    - New market entry enabled
```

### Team Structure at Scale

```
Content Operations Team

Head of Content
├── Content Strategy (Human)
│   ├── Content planning
│   ├── AI governance
│   └── Performance analysis
│
├── Editorial (Human)
│   ├── Quality control
│   ├── Voice guardians
│   └── Final approval
│
├── AI Operations (Technical)
│   ├── Prompt engineering
│   ├── Pipeline maintenance
│   └── Model optimization
│
└── AI Content Engine (Automated)
    ├── Draft generation
    ├── Optimization
    └── Repurposing
```

---

## Ethics and Disclosure

### Disclosure Guidelines

```markdown
## AI Content Disclosure Policy

### When to Disclose (Required)
- Journalistic content
- Research or academic content
- Content where human authorship is claimed
- Regulated industries (finance, healthcare)
- Where legally required

### When Disclosure is Optional
- Marketing content
- Product descriptions
- Social media posts
- Internal communications

### How to Disclose
Acceptable formats:
- "This article was written with AI assistance and edited by [human editor]"
- "AI-generated content, reviewed by our team"
- Byline: "Company Team, with AI assistance"

### Internal Tracking
- All AI-assisted content tagged in CMS
- AI involvement percentage recorded
- Audit trail maintained
```

### Ethical Guidelines

```markdown
## AI Content Ethics Guidelines

### Authenticity
- AI content must be factually accurate
- No fabricated quotes, sources, or data
- Clear distinction between facts and opinions
- No impersonation of real people

### Transparency
- Honest about AI use when asked
- No deceptive practices
- Clear about limitations

### Responsibility
- Human oversight required for public content
- Human accountable for published content
- Corrections process same as human content
- Feedback mechanisms for errors

### Harm Prevention
- No content that could cause harm
- Bias review for sensitive topics
- Cultural sensitivity review
- Avoid reinforcing stereotypes

### Intellectual Property
- No unauthorized use of copyrighted material
- Respect for training data sources
- Clear ownership of AI-generated content
- Proper attribution practices
```

### Compliance Checklist

```markdown
## AI Content Compliance Checklist

### Before Publishing

Legal:
- [ ] No trademark infringement
- [ ] No copyright issues
- [ ] Claims can be substantiated
- [ ] Appropriate disclosures included

Ethical:
- [ ] Factually accurate
- [ ] No harmful content
- [ ] Bias review complete
- [ ] Sensitivity review (if applicable)

Regulatory:
- [ ] Industry-specific compliance checked
- [ ] Required disclaimers included
- [ ] Geographic restrictions reviewed

### Record Keeping
- [ ] AI involvement documented
- [ ] Review chain recorded
- [ ] Version history maintained
- [ ] Compliance sign-off logged
```

---

## Summary

### Content Strategy Checklist

- [ ] Content types and AI roles defined
- [ ] Brand voice profile created
- [ ] Quality standards documented
- [ ] Editorial workflow established
- [ ] Performance metrics defined
- [ ] Scaling roadmap planned
- [ ] Ethics and disclosure policy in place
- [ ] Team trained on AI content

### Key Success Factors

1. **Clear governance** - Know what AI can/can't do
2. **Quality obsession** - Don't sacrifice quality for speed
3. **Human oversight** - AI assists, humans decide
4. **Continuous improvement** - Learn from every piece
5. **Ethical standards** - Build trust with transparency

See [writing.md](writing.md) for tactical AI writing guidance →
