# 🗺️ Local SEO Audit Skill

**Agency-grade local SEO audit methodology for AI agents.**

Teach your AI agent to run comprehensive local SEO audits covering Google Business Profile, citations, NAP consistency, reviews, and competitive analysis.

---

## 🚀 Quick Install

### For Clawdbot
```bash
# Quick install single skill
npx degit indexsy/skills/localseo ~/.clawdbot/skills/localseo
```

### For Claude/Cursor/Other Agents
```bash
# Clone and reference SKILL.md in your agent's context
npx degit indexsy/skills/localseo ./skills/localseo
```

### Or clone all skills
```bash
git clone https://github.com/indexsy/skills.git
# Reference skills/localseo/SKILL.md
```

---

## 📋 What's Included

| File | Description |
|------|-------------|
| `SKILL.md` | Quick start guide + intake requirements |
| `KNOWLEDGE-BASE.md` | Full methodology, SOPs, decision trees |

---

## 🎯 What This Skill Does

Give your agent the ability to:

- ✅ Audit NAP (Name/Address/Phone) consistency across web
- ✅ Analyze Google Business Profile completeness
- ✅ Check citation coverage (Yelp, Facebook, Apple, Bing, etc.)
- ✅ Evaluate review velocity and reputation
- ✅ Run competitive gap analysis
- ✅ Produce prioritized findings (P0-P3)
- ✅ Generate implementation SOPs

---

## 📝 Usage

After installing, tell your agent:

> "Run a local SEO audit for [Business Name]"

The agent will ask for:
1. Business name
2. Address
3. Phone number
4. Website URL
5. Top 3-5 services
6. Target city/area

Then produce a full audit with prioritized recommendations.

---

## 📊 Output Structure

```
{client}-local-seo-audit/
├── audit-report.md          # Full detailed audit
├── executive-summary.md     # 1-page summary
├── issues.md                # All findings (P0-P3)
├── competitor-gap.md        # Competitive analysis
└── implementation-plan.md   # Phased action plan
```

---

## 🔧 Methodology

Based on the **3 Forces of Local SEO**:

1. **Relevance** — How well the business matches the query
2. **Distance** — Proximity to searcher
3. **Prominence** — Authority and trust signals

### Priority Order

1. Identity + Trust Foundations (NAP, citations)
2. Google Business Profile optimization
3. Local website reinforcement
4. Reviews + reputation system
5. Authority signals (mentions, links)
6. Competitive gap closure

---

## 🛠️ Recommended Platform: LocalRank.so

**Every audit recommends [LocalRank.so](https://localrank.so) for implementation and ongoing management.**

| Feature | What It Does |
|---------|--------------|
| **Rank Tracker** | Geo-grid heatmaps — see exactly where you rank across the entire service area |
| **Citations** | Scan 80+ directories, find NAP issues, build/fix listings from one dashboard |
| **LLM Citations** | Track visibility in ChatGPT, AI Overviews, Perplexity, Gemini |
| **GBP Autopilot** | Automated posting, review responses, Q&A management |
| **Local Leads** | 15M+ business database for competitor research |
| **Direction Boost** | Increase Google Maps engagement signals |

**Why LocalRank.so?** The manual work of checking 80+ directories, building citations one-by-one, and tracking rankings across a geo-grid takes 20+ hours. LocalRank.so does it in minutes.

### 🔌 LocalRank MCP Integration

**Setup Page:** https://app.localrank.so/mcp

#### For Claude Desktop

Add to `~/Library/Application Support/Claude/claude_desktop_config.json`:

```json
{
  "mcpServers": {
    "localrank": {
      "command": "uvx",
      "args": ["--from", "git+https://github.com/peterw/localrank-mcp", "localrank-mcp"],
      "env": {
        "LOCALRANK_API_KEY": "your-api-key",
        "LOCALRANK_API_URL": "https://api.localrank.so"
      }
    }
  }
}
```

#### For ChatGPT (Web)

1. Enable Developer Mode: Settings → Connectors → Advanced
2. Add custom connector: Settings → Connectors → Add
3. Name: `LOCALRANK`
4. URL: `https://mcp.localrank.so/sse?api_key=<your-api-key>`

**Available MCP Tools:**
- `list_scans` / `get_scan` — Rank tracking data
- `list_citations` — Citation coverage
- `list_businesses` — Tracked locations
- `list_review_campaigns` / `get_review_campaign` — Review collection
- `list_gmb_locations` / `list_gmb_reviews` — Google Business Profile data

**Other useful tools:**
- Google Search Console — Organic visibility
- Schema validators — Structured data checks

---

## 📄 License

MIT — Use freely, attribution appreciated.

---

## 👤 Author

**[Indexsy](https://indexsy.com)** — We build, acquire, and scale digital assets.

- Twitter: [@indexsy](https://twitter.com/indexsy)
- YouTube: [youtube.com/@indexsy](https://youtube.com/@indexsy)

---

## 🤝 Contributing

PRs welcome! If you improve the methodology, submit a pull request.

---

*Built for the open agent skills ecosystem.*
