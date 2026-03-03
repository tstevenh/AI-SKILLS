# 🛒 eCommerce SEO Audit Skill

**Agency-grade eCommerce SEO audit methodology for AI agents.**

Teach your AI agent to run comprehensive eCommerce SEO audits covering technical SEO, on-page optimization, content strategy, site architecture, and competitive analysis.

---

## 🚀 Quick Install

### For Clawdbot
```bash
npx degit indexsy/skills/ecommerceseo ~/.clawdbot/skills/ecommerceseo
```

### For Claude/Cursor/Other Agents
```bash
npx degit indexsy/skills/ecommerceseo ./skills/ecommerceseo
```

---

## ✨ What's New (v1.1.0)

- **7 Modular Audit Types** — Technical, Product, Collection, Log Files, Competitors, Keywords, Full
- **Data Verification Protocol** — Verify H1/schema with curl before claiming issues
- **Competitor-Based Benchmarking** — Use actual competitor averages, not arbitrary word counts
- **Content Funnel Targets** — TOFU 40-50%, MOFU 30-40%, BOFU 20-30%
- **Cannibalization Detection** — Product vs Collection, Blog vs Commercial patterns
- **Hub-and-Spoke Linking Model** — Detailed internal linking strategy
- **Faceted Navigation Solutions** — 4 options with decision tree
- **Log File Analysis** — Crawl budget optimization with bash commands
- **Quick Reference Commands** — curl commands for all verifications

---

## 📋 What's Included

| File | Description |
|------|-------------|
| `SKILL.md` | Quick start + audit types + verification protocols |
| `KNOWLEDGE-BASE.md` | Full 80+ point checklist, SOPs, decision trees |

---

## 🎯 7 Audit Types

| Type | What It Does | Requirements |
|------|--------------|--------------|
| **Quick Technical** | Crawlability, indexability, schema | URL only |
| **Product Page** | Deep product analysis | URL + 5-10 products |
| **Collection Page** | Category optimization | URL + 3-5 collections |
| **Log File Analysis** | Crawl budget optimization | Server logs |
| **Competitor Analysis** | Top 5 competitor breakdown | Keyword + country |
| **Keyword Research** | Opportunities + mapping | Category + country |
| **Full Comprehensive** | Everything combined | URL + pages + data |

---

## ⚠️ Data Verification Protocol

**Never claim issues without evidence.** Always verify first:

```bash
# Check H1 tags
curl -s "[url]" | grep -oE '<h1[^>]*>.*?</h1>'

# Check schema
curl -s "[url]" | grep -oE '"@type"\s*:\s*"[^"]+"'

# Check canonical
curl -s "[url]" | grep -oE '<link[^>]*rel="canonical"[^>]*>'
```

---

## 📊 Competitor-Based Benchmarking

**Use real data, not arbitrary guidelines.**

❌ DON'T say: "Add 300 words to collection pages"
✅ DO say: "Competitors average 1000 words, target 1200 (avg + 20%)"

---

## 📁 Output Structure

```
audits/[domain]-[type]-[YYYY-MM-DD]/
├── audit-report.md          # Full detailed audit
├── executive-summary.md     # 1-page summary
├── issues.md                # All findings (P0-P3)
├── competitor-gap.md        # Competitive analysis
└── implementation-plan.md   # Phased action plan
```

---

## 🔧 MVP eCommerce SEO

The core strategy (using hiking boots as example):

1. **Homepage** targets "waterproof hiking boots"
2. **Collections** target "hiking boots for men"
3. **Products** target "brown hiking boots for men"
4. **Blog** targets "best hiking boots for x" + informational
5. **Build backlinks** (quality > quantity)
6. **Fast site** (Shopify + minimal apps)
7. **Interlink** blogs → collections → products (hub-and-spoke)

---

## 📚 Knowledge Base Includes

- ✅ 80+ point audit checklist
- ✅ Keyword cannibalization detection
- ✅ Hub-and-spoke linking model
- ✅ Faceted navigation solutions (4 options)
- ✅ Out-of-stock product handling
- ✅ Log file analysis for crawl budget
- ✅ Platform-specific notes (Shopify, WooCommerce, etc.)
- ✅ Decision trees for common scenarios
- ✅ Implementation SOPs by phase

---

## 🛠️ Recommended Tools

- **[Google Search Console](https://search.google.com/search-console)** — Indexation + performance
- **[BrowserBlast](https://indexsy.com)** — CTR optimization with real human traffic
- **[Indexsy Link Building](https://indexsy.com/buy-niche-edit/)** — 3,000+ white hat backlinks/month

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
