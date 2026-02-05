---
name: gym-data-enrichment-hybrid
description: Enrich climbing gym data from Outscraper Google Maps exports using Crawl4AI + LLM hybrid approach. Use when processing batches of gym listings to extract climbing-specific data (pricing, amenities, climbing types), generate editorial content (about, FAQ, highlights), and calculate detailed ratings. Triggers on requests to enrich gym data, process Outscraper exports, or prepare gym listings for database import. Uses Python/Crawl4AI for fast web crawling, LLM for content synthesis.
---

# Gym Data Enrichment (Hybrid: Crawl4AI + LLM)

Enrich raw Outscraper Google Maps data into complete climbing gym listings ready for database import.

**Hybrid Approach:**
- **Crawl4AI**: Fast, parallel web crawling with JavaScript rendering and CSS extraction
- **LLM**: Editorial content synthesis (about, FAQ, ratings) from extracted data

This hybrid approach is **10-100x faster** and **significantly cheaper** than pure LLM-based extraction.

## Workflow

```
INPUT: CSV batch (50 rows) from Outscraper
  ↓
PHASE 1: Clean & transform Outscraper fields
  ↓
PHASE 2: Crawl4AI deep crawl → extract structured data
  ↓
PHASE 3: Crawl4AI scrape reviews → analyze for ratings
  ↓
PHASE 4: LLM generate editorial content from extracted data
  ↓
PHASE 5: LLM calculate ratings from review analysis
  ↓
OUTPUT: JSON array of enriched gym objects
```

## Quick Start

1. **Install dependencies** (one-time):
   ```bash
   pip3 install 'crawl4ai<0.5' beautifulsoup4 pandas
   /Users/tsth/Library/Python/3.9/bin/crawl4ai-setup
   ```

2. **Run enrichment script**:
   ```bash
   python3 enrich_gyms_hybrid.py --csv gyms_batch.csv --output zGym/
   ```

## Phase 1: Clean Outscraper Data

Transform raw Outscraper columns:

| Outscraper Column | Transform | Output Field |
|-------------------|-----------|--------------|
| `name` | Direct | `name` |
| `full_address` | Direct | `address` |
| `city` | Direct | `city` |
| `state` | Map to 2-letter: "Texas" → "TX" | `region` |
| `latitude` | Fix decimal: `2,977,124` → `29.77124` | `latitude` |
| `longitude` | Fix decimal: `-953,776` → `-95.3776` | `longitude` |
| `site` | Direct | `website` |
| `photo` | Direct | `hero_image` |
| `location_link` | Direct | `google_maps_url` |
| `phone` | Format: +1XXXXXXXXXX (no dashes) | `phone` |

**Decimal fix logic:** If value > 1000 or < -1000, divide by 100000.

**Phone format:** Strip all non-digits, prepend +1 if US.

## Phase 2: Crawl4AI Deep Crawl (Primary Data Source)

**What makes this different:**
- **Single request** crawls entire website (pricing, about, facilities pages)
- **JavaScript rendering** handles dynamic/React sites
- **CSS extraction** is 100x faster than LLM
- **Parallel processing** for multiple gyms

### Using the Python Script

The `enrich_gyms_hybrid.py` script handles everything:

```python
import asyncio
from crawl4ai import AsyncWebCrawler

async def crawl_gym_website(url):
    async with AsyncWebCrawler(verbose=True) as crawler:
        result = await crawler.arun(
            url=url,
            # Deep crawl with max 5 pages
            deep_crawl_strategy="bfs",
            max_pages=5,
            # Extract CSS-based structured data
            css_selector=".pricing, .hours, .amenities, .contact",
            # Bypass bot detection
            bypass_cache=True,
            headless=True
        )
        return result.markdown, result.extracted_content
```

### What Gets Extracted

| Field | CSS/XPath Pattern | Fallback |
|-------|-------------------|----------|
| `email` | `a[href^="mailto:"]` | contact@ patterns in text |
| `phone` | `a[href^="tel:"]` | \(\d{3}\)\s*\d{3}-\d{4} patterns |
| `climbing_types` | Keywords: bouldering, top rope, lead, speed | - |
| `amenities` | Keywords: showers, lockers, cafe, wifi, parking | - |
| `custom_amenities` | Keywords: yoga, sauna, tension board, kilter board | - |
| `day_pass_price_local` | `$XX` near "day pass" or "drop-in" | - |
| `membership_from_local` | `$XX` near "month" or "membership" | - |
| `working_hour` | Hours table patterns | - |
| `difficulty_grades` | V0-V10, 5.6-5.13 patterns | - |

### Deep Crawl Strategy

The script automatically discovers and crawls:
1. Homepage (main URL)
2. `/pricing` or `/rates` or `/membership`
3. `/about` or `/facilities`
4. `/contact` or `/visit`
5. `/classes` or `/programs`

### CSS Selectors by Gym Site Type

**Climbing-specific patterns:**
```css
/* Pricing sections */
.pricing, .rates, .membership, .day-pass, .drop-in

/* Hours */
.hours, .schedule, .opening-hours, table[class*="hour"]

/* Amenities */
.amenities, .facilities, .features, .offerings

/* Contact */
.contact, .footer-contact, .contact-info

/* Climbing types */
[class*="boulder"], [class*="rope"], [class*="lead"]
```

## Phase 3: Review Scraping (Crawl4AI + LLM Analysis)

**Google Maps Reviews:**
- Use Crawl4AI with stealth mode for Maps pages
- Extract review text elements
- LLM analyzes sentiment for 5 rating dimensions

**Alternative review sources:**
- Yelp (if available)
- Facebook reviews
- Reddit (/r/climbing gym discussions)

### Review Analysis with LLM

Once Crawl4AI extracts review text, use LLM to score:

```python
review_analysis_prompt = """
Analyze these climbing gym reviews and rate 5 dimensions (1.0-5.0):

Reviews:
{review_text}

Output JSON:
{
  "rating_route_quality": 4.5,
  "rating_cleanliness": 4.8,
  "rating_staff_friendliness": 4.9,
  "rating_facilities": 4.7,
  "rating_value_for_money": 4.5,
  "why_climbers_like_it": ["quote 1", "quote 2", "quote 3"]
}
"""
```

## Phase 4: LLM Editorial Content Generation

Using **extracted data** (not web browsing), generate:

### `about` (2-3 paragraphs, max 5000 chars)
```python
about_prompt = """
Write a 3-paragraph editorial overview of {gym_name} in {city}, {state}.

Use ONLY this factual data:
- Climbing types: {climbing_types}
- Amenities: {amenities}, {custom_amenities}
- Training facilities: {training_facilities}
- Notable features: {notable_features}

Tone: Friendly local guide. Cover climbing style, community vibe, notable features, ideal visitors.
Do NOT invent facts not in the data.
"""
```

### `faq` (5-8 Q&A pairs)
```python
faq_prompt = """
Generate 5-8 FAQ pairs for {gym_name} based ONLY on this data:

Data:
- Hours: {working_hour}
- Pricing: day pass ${day_pass}, membership ${membership}/month
- Rentals: {rental_equipment}
- Classes: {class_info}

Output JSON: [{"question": "...", "answer": "..."}, ...]
"""
```

### `why_climbers_like_it` (3-5 bullets)
Extract directly from positive review themes found in Phase 3.

## Phase 5: Rating Calculation

**Rating scale:** 1.0-5.0 (one decimal)

**Fallback chain:**
1. Extract from review analysis (Phase 3)
2. If insufficient reviews, estimate based on:
   - Overall Google rating as baseline
   - Gym chain reputation (Momentum, BP = typically 4.3-4.7)
   - Price point correlation
   - Facility age/type

**Calculate `rating_overall`:**
```python
rating_overall = mean([
    rating_route_quality,
    rating_cleanliness,
    rating_staff_friendliness,
    rating_facilities,
    rating_value_for_money
])
```

## Output Schema

**CRITICAL:** All output must follow the exact 32-field schema defined in [OUTPUT_SCHEMA.md](OUTPUT_SCHEMA.md).

```json
{
  "name": "string",
  "address": "string",
  "city": "string",
  "region": "TX",
  "country": "US",
  "latitude": 29.6612,
  "longitude": -98.4485,
  "phone": "+12105551234",
  "email": "info@gym.com",
  "website": "https://...",
  "hero_image": "https://...",
  "google_maps_url": "https://...",
  "amenities": "showers|wifi|parking",
  "custom_amenities": "tension_board|yoga_studio",
  "climbing_types": "bouldering|top_rope|lead",
  "route_reset_frequency": "weekly",
  "total_routes": 120,
  "wall_height_meters": 4.8,
  "training_facilities": "hangboard|campus_board|spray_wall",
  "rental_equipment": "shoes|harness|chalk_bag",
  "beginner_friendly": true,
  "day_pass_price_local": 25,
  "student_discount": true,
  "membership_from_local": 89,
  "difficulty_grades": "V0-V10",
  "working_hour": "mon:08:00-22:00|tue:08:00-22:00|...",
  "about": "2-3 paragraphs...",
  "faq": [{"question": "...", "answer": "..."}],
  "why_climbers_like_it": ["bullet 1", "bullet 2"],
  "rating_route_quality": 4.5,
  "rating_cleanliness": 4.8,
  "rating_staff_friendliness": 4.9,
  "rating_facilities": 4.7,
  "rating_value_for_money": 4.5,
  "rating_overall": 4.68
}
```

## Quality Flags

Flag gyms for manual review if:
- `subtypes` contains: trampoline, playground, amusement, arcade
- Website returned 404 after Crawl4AI retry
- No pricing found from any source
- Name doesn't contain climbing-related words

## Batch Processing

### Parallel Processing with Crawl4AI

The script processes gyms in parallel (configurable concurrency):

```python
# Default: 5 concurrent crawls
CONCURRENCY = 5

async def process_batch(gym_list):
    tasks = [crawl_gym(gym) for gym in gym_list]
    results = await asyncio.gather(*tasks, return_exceptions=True)
    return results
```

### Progress Tracking

1. Log each gym: `"Processing 1/50: Momentum Indoor Climbing..."`
2. Crawl4AI crawls website (deep crawl, 5 pages max)
3. Extract structured data via CSS
4. Save enriched JSON immediately
5. Update CSV with `enrichment_status = done`

## Output File Saving

**Output directory:** `/Users/tsth/Coding/rockclimbing/zGym/`

**Filename format:** `{gym-name}.json`
- Convert name to kebab-case: "Momentum Indoor Climbing Sandy" → `momentum-indoor-climbing-sandy.json`

**After each gym:** Save immediately (don't wait for batch completion)

## CSV Progress Tracking

**IMPORTANT:** Mark each gym as done in source CSV.

**Add column:** `enrichment_status`

**After each gym:**
1. Find row by `name`
2. Set `enrichment_status` to `done` or `flagged`
3. Save CSV immediately

**Before batch:**
1. Read CSV
2. Filter rows where `enrichment_status` is empty
3. Process only those rows

## Advantages Over Pure LLM Approach

| Metric | Pure LLM | Hybrid (Crawl4AI + LLM) |
|--------|----------|-------------------------|
| **Speed** | ~30s/gym | ~3-5s/gym (6-10x faster) |
| **Cost** | High (API tokens) | Low (CSS = free) |
| **JS Support** | Limited | Full Playwright browser |
| **Parallel** | No | Yes (async/concurrent) |
| **Accuracy** | Good (hallucination risk) | Excellent (raw data) |

## Troubleshooting

### Crawl4AI Issues

```bash
# Reinstall browser
/Users/tsth/Library/Python/3.9/bin/crawl4ai-setup

# Check installation
/Users/tsth/Library/Python/3.9/bin/crawl4ai-doctor

# Manual browser install
python3 -m playwright install chromium
```

### Common Errors

| Error | Solution |
|-------|----------|
| `Browser not found` | Run `crawl4ai-setup` |
| `SSL error` | Python 3.9 LibreSSL warning (safe to ignore) |
| `Timeout` | Increase `page_timeout` in script |
| `Empty result` | Check URL validity, try `bypass_cache=True` |

## Resources

- [references/example-output.json](references/example-output.json) - Perfect output example
- [references/full-schema-prompts.json](references/full-schema-prompts.json) - Complete field schema with prompts
- [references/output-schema.json](references/output-schema.json) - Field type definitions
- [references/extraction-prompts.md](references/extraction-prompts.md) - Quick reference patterns
- [enrich_gyms_hybrid.py](enrich_gyms_hybrid.py) - Main enrichment script

## Version Notes

- **Crawl4AI version:** 0.4.248 (Python 3.9 compatible)
- **For Python 3.10+:** Can use 0.7.x with newer features
- **Browser:** Chromium via Playwright
