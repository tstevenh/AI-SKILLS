# Backlink Indexation Knowledge Base (for LLMs)

**Purpose:** Provide a repeatable process for checking backlink indexation status and submitting URLs for indexing, with best practices, troubleshooting, and expected outcomes.

**Voice guidelines:** Clear, practical, non-hype. No guarantees on indexation. Focus on diagnosis → action → measurement.

---

## 1) Why Backlink Indexation Matters

A backlink only passes SEO value if Google has indexed the page containing the link.

**The Problem:**
- 20-40% of backlinks are never indexed by Google
- Unindexed links = wasted link building budget
- Most teams never check indexation status

**The Solution:**
- Audit indexation status monthly
- Submit not-indexed URLs for crawling
- Track indexation rates by link type
- Focus future efforts on sources that get indexed

---

## 2) How Google Indexation Works

### Discovery → Crawl → Index

1. **Discovery:** Google finds the URL (via links, sitemap, or submission)
2. **Crawl:** Googlebot fetches the page content
3. **Index:** Google adds the page to search results (if quality threshold met)

### Why Pages Don't Get Indexed

| Reason | Fix |
|--------|-----|
| Page not discovered | Submit URL, add internal links |
| Blocked by robots.txt | Contact site owner |
| Noindex meta tag | Contact site owner |
| Low-quality content | Nothing (Google's decision) |
| Duplicate content | Nothing (Google's decision) |
| New domain / low authority | Wait + submit |
| Crawl budget exhausted | Submit URL directly |

---

## 3) IndexChex: How It Works

IndexChex provides two services:

### Index Checker

Checks if URLs appear in Google's index by querying Google search.

**Process:**
1. Submit list of URLs
2. IndexChex queries Google for each URL
3. Returns: indexed / not indexed / error

**Accuracy:** ~90-95% accurate. May under-report by 5-10% for homepage/root URLs.

### Indexer (Submission)

Submits URLs to Google for crawling via multiple methods:
- Google Indexing API
- Google Search Console pings
- Sitemap submission signals
- Web mention signals

**Success rate:** 60-80% for quality pages. Low-quality pages may still not index.

---

## 4) Standard Operating Procedure

### A) Monthly Indexation Audit

**Goal:** Know what percentage of your backlinks are indexed.

**Process:**

1. Export backlinks from Ahrefs, SEMrush, or tracker
2. Clean the list (remove duplicates, invalid URLs)
3. Submit to IndexChex checker
4. Record baseline metrics

**Command:**
```bash
python scripts/indexchex.py -k $INDEXCHEX_API_KEY check -f backlinks.txt --wait -n "Monthly audit $(date +%Y-%m)" -o audit-$(date +%Y%m).json
```

**Metrics to Track:**
- Total backlinks
- Indexed count / percentage
- Not-indexed count / percentage
- Change from last month

---

### B) Index Submission Campaign

**Goal:** Get not-indexed backlinks crawled and indexed.

**Process:**

1. Filter not-indexed URLs from audit
2. Remove URLs that won't index (blocked, noindex, thin content)
3. Submit remaining URLs to IndexChex indexer
4. Wait 24-48 hours
5. Re-check indexation status

**Command:**
```bash
# Submit
python scripts/indexchex.py -k $INDEXCHEX_API_KEY submit -f not-indexed.txt --wait -n "Index campaign $(date +%Y-%m)"

# Re-check after 48 hours
python scripts/indexchex.py -k $INDEXCHEX_API_KEY check -f not-indexed.txt --wait -n "Re-check $(date +%Y-%m)"
```

**Expected Results:**
- 60-80% of quality pages will index within 48 hours
- 10-20% may take 1-2 weeks
- 10-20% may never index (low quality)

---

### C) Link Source Analysis

**Goal:** Identify which link sources have best indexation rates.

**Process:**

1. Tag backlinks by source type (guest post, niche edit, directory, etc.)
2. Run separate audits per source type
3. Compare indexation rates
4. Adjust link building strategy

**Example Analysis:**

| Source | Total | Indexed | Rate |
|--------|-------|---------|------|
| Guest posts | 100 | 85 | 85% |
| Niche edits | 50 | 40 | 80% |
| HARO | 30 | 28 | 93% |
| Directories | 200 | 140 | 70% |
| Forum profiles | 50 | 15 | 30% |

**Action:** Reduce forum profile building, increase HARO outreach.

---

## 5) Troubleshooting

### URLs Show "Not Indexed" But Actually Are

**Cause:** Google's index is eventually consistent. Recent pages may not show immediately.

**Fix:** 
- Wait 24 hours and re-check
- Manually verify with `site:url.com/page` search

### Submitted URLs Still Not Indexed After 1 Week

**Causes:**
- Page blocked by robots.txt
- Noindex meta tag
- Low domain authority
- Thin/duplicate content
- Google chose not to index

**Fixes:**
- Check robots.txt and meta tags
- Verify page has unique, valuable content
- Build more links to the linking page
- Accept that some pages won't index

### Job Stuck in "Processing"

**Cause:** Large batches take time. 10,000 URLs = 30-60 minutes.

**Fix:** 
- Check job status periodically
- View progress in IndexChex dashboard

---

## 6) Best Practices

### Do

- ✅ Audit indexation monthly
- ✅ Submit new backlinks within 1 week of going live
- ✅ Track indexation rates by link source
- ✅ Re-check submitted URLs after 48 hours
- ✅ Focus link building on sources with high index rates

### Don't

- ❌ Submit the same URL repeatedly (wastes credits)
- ❌ Expect 100% indexation (unrealistic)
- ❌ Submit URLs blocked by robots.txt
- ❌ Submit thin/spammy pages
- ❌ Panic if homepage shows "not indexed" (check manually)

---

## 7) API Reference

### Endpoints

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/v1/balance` | GET | Check credit balance |
| `/v1/index-check/jobs` | POST | Create index check job |
| `/v1/index-check/jobs/{id}` | GET | Get check job status |
| `/v1/index-submit/jobs` | POST | Create index submit job |
| `/v1/index-submit/jobs/{id}` | GET | Get submit job status |

### Request Format

```json
{
  "urls": ["https://example.com/page1", "https://example.com/page2"],
  "name": "Job name (optional)"
}
```

### Response Format (Check)

```json
{
  "job_id": 42,
  "status": "completed",
  "total_urls": 100,
  "indexed_count": 75,
  "not_indexed_count": 25,
  "progress_percent": 100
}
```

### Limits

- **Batch size:** 10,000 URLs per request
- **Credits:** 1 per URL (check or submit)
- **Rate limit:** None specified (be reasonable)

---

## 8) Integration with Link Building Workflow

### Recommended Process

```
Build Links → Export URLs → Check Indexation → Submit Not-Indexed → Re-check → Report
     ↑                                                                           |
     └───────────────────── Adjust Strategy Based on Data ───────────────────────┘
```

### Automation Opportunities

1. **Weekly export** from Ahrefs/SEMrush to `backlinks.txt`
2. **Automated check** via cron job
3. **Auto-submit** not-indexed URLs
4. **Slack/email alert** if indexation rate drops below threshold

---

## 9) Metrics & KPIs

### Primary Metrics

| Metric | Target | Frequency |
|--------|--------|-----------|
| Overall indexation rate | >70% | Monthly |
| New link indexation (30 days) | >60% | Monthly |
| Submission success rate | >50% | Per campaign |

### Warning Signs

- Indexation rate below 50% → Review link sources
- New links not indexing → Check for site-wide issues
- Submission success below 30% → Links may be low quality

---

## 10) Glossary

| Term | Definition |
|------|------------|
| **Indexed** | Page appears in Google search results |
| **Not Indexed** | Page not found in Google search results |
| **Crawled** | Googlebot has fetched the page |
| **Index Check** | Verify if URL is in Google's index |
| **Index Submit** | Request Google to crawl/index a URL |
| **Backlink** | Link from external site to your site |
| **Referring Page** | The page containing the backlink |
