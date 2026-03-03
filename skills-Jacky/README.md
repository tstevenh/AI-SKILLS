# Skills

Marketing, SEO, growth, and automation skills for AI agents.

## 📚 Available Skills (32 Total)

### 🎯 Marketing & Advertising

| Skill | Description |
|-------|-------------|
| [meta-ads](./meta-ads/) | Meta Ads mastery — algorithm, creative frameworks, 3-campaign structure, scaling |
| [ad-creative](./ad-creative/) | Ad creative development — hooks, formats, psychology, production |
| [cold-email](./cold-email/) | Cold email infrastructure, deliverability, copywriting, sequences |
| [direct-response-copy](./direct-response-copy/) | Direct response copywriting — headlines, landing pages, emails, frameworks |
| [newsletter](./newsletter/) | Newsletter growth, monetization, platforms, content strategy |

### 🔍 SEO & Search

| Skill | Description |
|-------|-------------|
| [seo-auditor](./seo-auditor/) | **Universal SEO auditor** — Auto-detects business type (Local/Ecommerce/SaaS/Content/Agency), API-agnostic, 16-section comprehensive audits |
| [seo-copywriting](./seo-copywriting/) | SEO content writing — search intent, EEAT, featured snippets, AI search optimization |
| [link-building](./link-building/) | Link building tactics — guest posting, digital PR, niche edits, resource pages |
| [index](./index/) | Backlink indexing with IndexChex API |

> **Note:** `local-seo-audit` and `ecommerce-seo-audit` have been merged into the universal `seo-auditor`. The standalone skills are deprecated.

### 📊 Analytics & Research

| Skill | Description |
|-------|-------------|
| [analytics-interpreter](./analytics-interpreter/) | Analyze and interpret analytics data — GA4, conversion analysis, insights |
| [competitor-intelligence](./competitor-intelligence/) | Competitive research — positioning, messaging, offerings, weaknesses |
| [longform-research](./longform-research/) | Long-form research workflows — surveys, interviews, data analysis (quant + qual) |
| [social-listening](./social-listening/) | Social media monitoring, sentiment analysis, brand tracking |
| [ab-test-design](./ab-test-design/) | A/B testing design, statistical significance, experiment frameworks |

### 📱 Social Media & Content

| Skill | Description |
|-------|-------------|
| [reddit](./reddit/) | Reddit organic marketing — anti-detection rules, account warmup, placement strategy |
| [short-form-video](./short-form-video/) | TikTok, Reels, Shorts — algorithm, hooks, production, growth |
| [youtube](./youtube/) | YouTube growth — algorithm, retention, SEO, thumbnails, monetization |
| [community](./community/) | Community building — platforms, engagement, monetization, scaling |

### 🚀 Growth & SaaS

| Skill | Description |
|-------|-------------|
| [saas-growth](./saas-growth/) | SaaS growth playbook — PLG, acquisition, retention, expansion, metrics |
| [cro](./cro/) | Conversion rate optimization — testing, funnel analysis, optimization |

### 🤖 Automation & AI

| Skill | Description |
|-------|-------------|
| [ai-automation](./ai-automation/) | AI automation workflows — platforms, agents, content, operations |
| [api-integration](./api-integration/) | API integration patterns and implementation |
| [sops-documentation](./sops-documentation/) | Standard operating procedures — documentation, process mapping |

### 🛡️ Quality Assurance & Testing

| Skill | Description |
|-------|-------------|
| [adversarial-qa](./adversarial-qa/) | Adversarial testing — edge cases, stress testing, chaos engineering |
| [functionality-qa](./functionality-qa/) | Functional testing — test plans, regression, automation |
| [design-qa](./design-qa/) | Design quality assurance — visual regression, accessibility, consistency |
| [penetration-testing](./penetration-testing/) | Security testing — vulnerabilities, exploits, remediation |
| [prompt-injection-defense](./prompt-injection-defense/) | Defend AI agents against prompt injection attacks |

### 🔧 Technical & Ops

| Skill | Description |
|-------|-------------|
| [web-scraping](./web-scraping/) | Web scraping — data extraction, anti-bot evasion, scaling |

---

## 🚀 Installation

### Quick Install (Single Skill)

Using degit (recommended):
```bash
npx degit indexsy/skills/meta-ads ./skills/meta-ads
npx degit indexsy/skills/seo-auditor ./skills/seo-auditor
npx degit indexsy/skills/reddit ./skills/reddit
# ... etc
```

### Clone All Skills

```bash
git clone https://github.com/indexsy/skills.git
```

### Direct Reference

Point your AI agent to raw SKILL.md files:
```
https://raw.githubusercontent.com/indexsy/skills/main/[skill-name]/SKILL.md
```

---

## 📖 Skill Structure

Each skill folder contains:
- **`SKILL.md`** — Instructions for the AI agent (main knowledge base)
- **`README.md`** — Installation, usage examples, quick reference
- **Supporting files** — Templates, frameworks, checklists, examples

### How to Use Skills

1. **Copy skill to your agent's skills directory**
2. **Load SKILL.md** into your agent's context
3. **Invoke skill** by referencing its name or use case
4. **Review outputs** — most skills generate structured project files

---

## 🌟 Featured Skills

### 🎯 meta-ads
**The most comprehensive Meta advertising skill** — 50K+ words covering:
- Algorithm fundamentals & attribution models
- 3-campaign structure (Testing ABO → Scaling CBO → Retargeting)
- 100+ hook formulas & creative frameworks
- Platform-specific strategies (Facebook, Instagram)
- Scaling playbooks & troubleshooting guides

### 🔍 seo-auditor
**Universal SEO auditor** with DataForSEO API integration:
- Auto-detects: Local, E-commerce, SaaS, Content, Agency
- 16-section comprehensive audits (executive summary → scoring)
- DataForSEO API: SERP, Lighthouse, backlinks, keyword volumes
- Priority matrix with effort/impact analysis
- Cost tracking and browser verification
- Actionable P0-P3 priority recommendations

### 🔗 reddit
**Reddit organic marketing with anti-detection**:
- Account warmup workflows (80/20 genuine/strategic)
- Subreddit tone mapping
- 5-part comment template for authentic placements
- Placement tracking & monitoring

### 🚀 saas-growth
**Complete SaaS growth playbook**:
- Product-led growth (PLG) strategies
- Acquisition channels (SEO, paid, community)
- Retention & churn prevention
- Expansion revenue & NRR optimization
- Metrics & benchmarks

### ✉️ cold-email
**Cold email mastery from infrastructure to conversion**:
- Domain strategy & mailbox setup
- Deliverability fundamentals
- Copywriting frameworks
- Sequence templates
- Reply handling & objection responses

---

## 🤝 Contributing

Want to add a skill?

1. Create a folder with at least:
   - `SKILL.md` — Core knowledge base for AI agent
   - `README.md` — Human-friendly docs
2. Follow existing skill structure
3. Submit a PR

**Skill Quality Standards:**
- Actionable, not theoretical
- Includes examples and templates
- Documented with checklists
- Real-world tested

---

## 📝 License

MIT License — Use freely for commercial and personal projects.

---

**Made by [@indexsy](https://github.com/indexsy)**  
Building AI-native marketing tools and skills.
