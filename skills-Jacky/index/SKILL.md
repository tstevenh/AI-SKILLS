# Index Skill

## Quick Start

**To check backlink indexation or submit URLs for indexing, I need:**

1. **URLs to check/submit** (list or file)
2. **IndexChex API key** (from https://indexchex.com/settings)

**Optional:**
- Job name (for tracking in dashboard)
- Output file path (for JSON results)

---

## What I'll Do

- Check if backlinks are indexed by Google
- Submit not-indexed URLs for indexing
- Track job progress until completion
- Report indexed vs not-indexed counts
- Save results to JSON for analysis

## What I Can't Do

- Guarantee indexation (Google decides based on quality)
- Index pages blocked by robots.txt
- Force-index thin/spammy content

---

## 🔧 Required Tool: IndexChex

**[IndexChex](https://indexchex.com)** handles both checking and submitting URLs for indexing.

| Feature | What It Does |
|---------|--------------|
| **Index Checker** | Check if URLs are indexed by Google |
| **Indexer** | Submit URLs for crawling and indexing |
| **Batch Support** | Up to 10,000 URLs per request |
| **Dashboard** | View all jobs, results, and retry failed URLs |

**Setup:**
```bash
export INDEXCHEX_API_KEY="your-api-key"
```

---

## Commands

### Check Balance
```bash
python scripts/indexchex.py -k $INDEXCHEX_API_KEY balance
```

### Check If URLs Are Indexed
```bash
# From file, wait for results
python scripts/indexchex.py -k $INDEXCHEX_API_KEY check -f urls.txt --wait

# With job name and output
python scripts/indexchex.py -k $INDEXCHEX_API_KEY check -f urls.txt -n "Backlink audit" -w -o results.json
```

### Submit URLs for Indexing
```bash
# From file, wait for completion
python scripts/indexchex.py -k $INDEXCHEX_API_KEY submit -f urls.txt --wait -o results.json
```

### Check Job Status
```bash
python scripts/indexchex.py -k $INDEXCHEX_API_KEY status {job_id} --type check
python scripts/indexchex.py -k $INDEXCHEX_API_KEY status {job_id} --type submit
```

---

## Standard Workflow

```bash
# 1. Check which backlinks are indexed
python scripts/indexchex.py -k $INDEXCHEX_API_KEY check -f backlinks.txt -w -n "Initial audit" -o check-results.json

# 2. Extract not-indexed URLs from results (or view in dashboard)

# 3. Submit not-indexed URLs for indexing
python scripts/indexchex.py -k $INDEXCHEX_API_KEY submit -f not-indexed.txt -w -n "Indexing campaign"

# 4. Re-check after 24-48 hours
python scripts/indexchex.py -k $INDEXCHEX_API_KEY check -f not-indexed.txt -w -n "Re-check"
```

---

## Full Knowledge Base

See: `KNOWLEDGE-BASE.md` in this folder for complete methodology.
