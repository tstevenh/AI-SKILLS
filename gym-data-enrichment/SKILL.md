---
name: gym-data-enrichment
description: Enrich climbing gym data from Outscraper Google Maps exports. Use when processing batches of gym listings to extract climbing-specific data (pricing, amenities, climbing types), generate editorial content (about, FAQ, highlights), and calculate detailed ratings. Triggers on requests to enrich gym data, process Outscraper exports, or prepare gym listings for database import.
---

# Gym Data Enrichment

Enrich raw Outscraper Google Maps data into complete climbing gym listings ready for database import.

## Workflow

```
INPUT: CSV batch (50 rows) from Outscraper
  ↓
PHASE 1: Clean & transform Outscraper fields
  ↓
PHASE 2: Fetch official website → extract data
  ↓
PHASE 3: Fetch Google reviews → analyze for ratings
  ↓
PHASE 4: Fetch Google Maps listing (if needed)
  ↓
PHASE 5: Web search (if data still missing)
  ↓
PHASE 6: Generate editorial content with LLM
  ↓
PHASE 7: Calculate ratings & finalize
  ↓
OUTPUT: JSON array of enriched gym objects
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

## Phase 2: Fetch Official Website

**Source:** `site` column

**2-Tier Fetching Strategy:**

**Tier 1 - WebFetch (Primary):**
```
WebFetch(url: "{website_url}", prompt: "Extract gym info: email, phone, pricing, hours, amenities, climbing types")
```

**Tier 2 - WebSearch (If WebFetch fails or insufficient data):**
```
WebSearch("{gym_name} {city} climbing gym pricing hours amenities")
```

**When to escalate:**
- WebFetch returns error or empty → Try WebSearch
- WebSearch doesn't find critical fields → Flag for manual review

**Extract these fields:**

```
email           → mailto: links, contact@domain patterns
phone           → tel: links, (xxx) xxx-xxxx patterns
climbing_types  → "bouldering", "top rope", "lead", "speed"
amenities       → showers|lockers|cafe|wifi|parking|sauna|kids_zone|pro_shop
custom_amenities → yoga_studio|fitness_area|coworking|tension_board|kilter_board|moon_board
training_facilities → hangboard|campus_board|treadwall|weights|spray_wall
rental_equipment → shoes|harness|belay_device|chalk_bag
day_pass_price_local → "day pass $XX", "drop-in $XX"
membership_from_local → "monthly $XX", "membership from $XX"
working_hour    → Hours table → mon:HH:MM-HH:MM|tue:...|...
difficulty_grades → "V0-V10", "5.6-5.13a"
total_routes    → "XX+ problems", "XX routes"
wall_height_meters → "XX feet" × 0.3048, or "XX meters"
beginner_friendly → "beginner", "intro class", "first time"
student_discount → "student discount", "student rate"
route_reset_frequency → weekly|biweekly|monthly|quarterly|varies
```

## Phase 3: Fetch Google Reviews

**Source:** `reviews_link` column

**Analyze review text for ratings:**

| Rating Field | Look For |
|--------------|----------|
| `rating_route_quality` | "great routes", "creative setting", "fresh problems", "stale" |
| `rating_cleanliness` | "clean", "dusty", "well maintained", "dirty" |
| `rating_staff_friendliness` | "friendly staff", "helpful", "welcoming", "rude" |
| `rating_facilities` | "nice showers", "good training area", "cramped" |
| `rating_value_for_money` | "worth it", "expensive", "good deal", "overpriced" |

**Also extract:** Positive themes for `why_climbers_like_it`

## Phase 4: Google Maps Listing (Fallback)

**Source:** `location_link` column OR `about` JSON column

**Use only if website didn't provide amenities.**

Map Google `about` JSON:
- "Wi-Fi" → wifi
- "Lockers available" → lockers
- "Free parking lot" → parking
- "Good for kids" → kids_zone
- "Sauna" → sauna

## Phase 5: Web Search (If Data Missing)

Use WebSearch for any missing critical fields:
- Pricing (day pass, membership)
- Hours
- Climbing types
- Additional reviews for ratings

Search query: `"{gym name}" {city} climbing gym {field}` (e.g., "day pass price")

## Phase 6: Generate Editorial Content

Using collected data, generate:

**`about`** (2-3 paragraphs, max 5000 chars)
- Friendly local-guide tone
- Cover: climbing style, community vibe, notable features, ideal visitors
- Use only factual data found - don't invent

**`faq`** (5-8 Q&A pairs as JSON array)
- Practical visitor questions: hours, rentals, pricing, classes, parking
- Only include Q&A answerable from collected data

**`why_climbers_like_it`** (3-5 bullets as JSON array)
- Specific standout positives from reviews
- Quote-worthy, not generic

## Phase 7: Calculate Ratings

**Rating scale:** 1.0-5.0 (one decimal)

**Never return null.** Fallback chain:
1. Extract from review text
2. Web search for more reviews
3. LLM estimation based on:
   - Overall Google rating as baseline
   - Gym chain reputation (Momentum, Bouldering Project = typically 4.3-4.7)
   - Price point correlation
   - Facility age/type

**Calculate `rating_overall`:**
```
rating_overall = average(rating_route_quality, rating_cleanliness,
                         rating_staff_friendliness, rating_facilities,
                         rating_value_for_money)
```

## Output Schema

**CRITICAL:** All output must follow the exact 32-field schema defined in [OUTPUT_SCHEMA.md](OUTPUT_SCHEMA.md).

**DO NOT include internal fields:** `slug`, `google_rating`, `google_reviews_count`, `reviews_link`, `place_id`, `about_raw`

**Amenities separation logic:**
- Standard amenities (in `amenities` field): showers, lockers, wifi, parking, cafe, pro_shop, sauna
- Custom amenities (in `custom_amenities` field): yoga_studio, cold_plunge, coworking_space, tension_board, kilter_board, etc.

See [references/output-schema.json](references/output-schema.json) for additional reference.

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
- Website returned 404
- No pricing found from any source
- Name doesn't contain climbing-related words

## Batch Processing

Process 50 gyms per batch. For each gym:
1. Log progress: "Processing 1/50: Momentum Indoor Climbing..."
2. Fetch all sources (website, reviews, maps listing)
3. Extract and generate all fields
4. Save enriched JSON to file

## Output File Saving

**Output directory:** `/Users/tsth/Coding/rockclimbing/zGym/`

**Filename format:** `{gym-name}.json`
- Convert name to kebab-case: "Momentum Indoor Climbing Sandy" → `momentum-indoor-climbing-sandy.json`
- If file already exists, append number: `momentum-indoor-climbing-sandy-2.json`

**Example:**
```
/Users/tsth/Coding/rockclimbing/zGym/
├── armadillo-boulders-stone-oak.json
├── momentum-indoor-climbing-sandy.json
├── momentum-indoor-climbing-katy.json
├── bouldering-project-springdale.json
└── ...
```

**After each gym:** Save immediately (don't wait for batch completion)

**Batch summary:** After all gyms processed, output summary:
```
Batch complete: 50 gyms processed
- Saved: 48 files to /Users/tsth/Coding/rockclimbing/zGym/
- Flagged for review: 2
```

## Progress Tracking in CSV

**IMPORTANT:** After enriching each gym, mark it as done in the source CSV file.

**Add column:** `enrichment_status`

**After each gym is processed:**
1. Find the row by matching `name` column
2. Set `enrichment_status` to `done` (or `flagged` if needs review)
3. Save the CSV immediately

**This ensures:**
- You know which gyms are already processed
- You can resume from where you left off
- No duplicate processing

**Before starting a batch:**
1. Read the CSV
2. Filter to rows where `enrichment_status` is empty or missing
3. Process only those rows

**CSV update example:**
```
name,site,...,enrichment_status
Momentum Indoor Climbing Sandy,https://...,done
Bouldering Project Springdale,https://...,done
Sky Zone Trampoline Park,https://...,flagged
Next Gym To Process,https://...,(empty - process this one)
```

## Resources

- [references/example-output.json](references/example-output.json) - **Perfect output example** (Armadillo Boulders) - match this format exactly
- [references/full-schema-prompts.json](references/full-schema-prompts.json) - **Complete field schema with extraction prompts** - use these prompts for each field
- [references/output-schema.json](references/output-schema.json) - Field type definitions and allowed values
- [references/extraction-prompts.md](references/extraction-prompts.md) - Quick reference for extraction patterns
