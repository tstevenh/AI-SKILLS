# Keyword Research

Advanced keyword research with SERP clustering, weakness scoring, cannibalization detection, competitor gap analysis, and multi-platform expansion.

## What It Does

- **SERP Weakness Scoring** — KeywordScore (0-100) based on 17 weakness types across top 10 results
- **SERP Clustering** — 3 algorithms to group keywords by search intent (URL overlap)
- **Cannibalization Detection** — Identifies keywords with overlapping SERP results
- **Competitor Gap Analysis** — Find keywords competitors rank for that you don't
- **Multi-Platform Expansion** — Google, YouTube, Amazon, Bing, Reddit
- **Question Mining** — Answer The Public-style question keyword discovery
- **Webmaster Tools** — Real GSC + Bing click/impression data
- **Wildcard Patterns** — `"best * for dogs"` expands automatically

## Research Modes

| Mode | Purpose |
|------|---------|
| Keyword Expansion | Seed → related suggestions |
| Autocomplete | Long-tail via Google autocomplete |
| Question Mining | How/what/why question variations |
| Multi-Platform | YouTube, Amazon, Bing, Reddit |
| Competitor Research | What keywords does competitor X rank for? |
| Keyword Gap | What do they rank for that I don't? |
| Webmaster Tools | Real GSC + Bing performance data |
| SERP Clustering | Group by intent via URL overlap |

## KeywordScore (0-100)

Measures ranking opportunity based on SERP weaknesses:

| Score | Opportunity |
|-------|-------------|
| 90-100 | Exceptional |
| 70-89 | Strong |
| 50-69 | Moderate |
| 30-49 | Challenging |
| 0-29 | Very difficult |

**17 weakness types detected:** Low Domain Score, Low Page Score, No Backlinks, Slow Page Speed, High Spam Score, Non-HTTPS, Broken Page, Flash, Frames, Non-Canonical, Old Content, Title-Content Mismatch, Keyword Not in Headings, No Heading Tags, UGC-Heavy Results, Unmatched Intent.

## Clustering Algorithms

| Algorithm | Best For | Speed |
|-----------|----------|-------|
| DEFAULT | Large datasets (100K+) | Fastest |
| STRICT | Competitive niches | 2-3x slower |
| BALANCED STRICT | Most use cases (recommended) | Moderate |

## Usage

```
"Find keywords for organic coffee, minimum 100 searches/month"
"Keyword gap analysis: mydomain.com vs competitor.com"
"Cluster these keywords by SERP overlap, CPC-based primary"
"Score keyword opportunities for 'best CRM software'"
"Check cannibalization between 'best coffee' and 'top coffee'"
```

## Data Sources

- **DataForSEO** (primary) — volume, KD, CPC, SERP, backlinks, page speed
- **Serper** (alternative) — SERP data + autocomplete
- **Ahrefs** (optional) — DR/UR metrics
- **GSC + Bing Webmaster Tools** — real click/impression data

## Installation

```bash
npx degit indexsy/skills/keyword-research ./skills/keyword-research
```
