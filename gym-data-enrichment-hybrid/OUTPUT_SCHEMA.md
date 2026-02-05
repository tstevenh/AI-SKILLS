# Gym Data Enrichment - Exact Output Schema

**CRITICAL:** All enriched gym JSON files must follow this exact structure with NO additional fields.

## Complete Schema (32 fields)

```json
{
  "name": "string",
  "address": "string",
  "city": "string",
  "region": "string",
  "country": "string",
  "latitude": number,
  "longitude": number,
  "phone": "string",
  "email": "string | null",
  "website": "string",
  "hero_image": "string",
  "google_maps_url": "string",
  "amenities": "string",
  "custom_amenities": "string | null",
  "climbing_types": "string",
  "route_reset_frequency": "string | null",
  "total_routes": "number | null",
  "wall_height_meters": "number | null",
  "training_facilities": "string | null",
  "rental_equipment": "string | null",
  "beginner_friendly": "boolean",
  "day_pass_price_local": "number | null",
  "student_discount": "boolean",
  "membership_from_local": "number | null",
  "difficulty_grades": "string | null",
  "working_hour": "string",
  "about": "string",
  "faq": [
    {
      "question": "string",
      "answer": "string"
    }
  ],
  "why_climbers_like_it": [
    "string"
  ],
  "rating_route_quality": "number",
  "rating_cleanliness": "number",
  "rating_staff_friendliness": "number",
  "rating_facilities": "number",
  "rating_value_for_money": "number",
  "rating_overall": "number"
}
```

## Field Definitions

### Location & Contact (11 fields)

- `name`: Full gym name
- `address`: Full street address
- `city`: City name
- `region`: 2-letter state code (TX, WA, CA, etc.)
- `country`: 2-letter country code (US)
- `latitude`: Decimal degrees (29.6612)
- `longitude`: Decimal degrees (-98.4485)
- `phone`: Format: +12105551234
- `email`: Contact email or null
- `website`: Full URL
- `hero_image`: Google Maps photo URL
- `google_maps_url`: Full Google Maps place URL

### Amenities & Features (10 fields)

- `amenities`: Pipe-separated standard amenities only
  - Allowed: showers, lockers, wifi, parking, cafe, pro_shop, sauna
  - Example: "showers|lockers|wifi|parking|sauna"
- `custom_amenities`: Pipe-separated custom amenities or null
  - Examples: yoga_studio|cold_plunge|coworking_space|tension_board|kilter_board
- `climbing_types`: Pipe-separated
  - Allowed: bouldering, top_rope, lead, auto_belay
  - Example: "bouldering|top_rope|lead"
- `route_reset_frequency`: weekly|biweekly|monthly|quarterly|varies|null
- `total_routes`: Number of routes or null
- `wall_height_meters`: Height in meters or null
- `training_facilities`: Pipe-separated or null
  - Examples: weights|hangboard|campus_board|spray_wall|yoga_room
- `rental_equipment`: Pipe-separated or null
  - Examples: shoes|harness|chalk_bag|belay_device
- `beginner_friendly`: true|false

### Pricing (4 fields)

- `day_pass_price_local`: Number (no currency symbol) or null
- `student_discount`: true|false
- `membership_from_local`: Monthly price (no currency symbol) or null
- `difficulty_grades`: String or null
  - Examples: "V0-V10", "5.6-5.13", "V0-V10|5.6-5.12"

### Operations (1 field)

- `working_hour`: Pipe-separated format
  - Format: day:HH:MM-HH:MM|day:HH:MM-HH:MM|...
  - Days: mon, tue, wed, thu, fri, sat, sun
  - Example: "mon:08:00-22:00|tue:08:00-22:00|wed:08:00-22:00|thu:08:00-22:00|fri:08:00-22:00|sat:08:00-22:00|sun:08:00-22:00"

### Editorial Content (3 fields)

- `about`: 2-3 paragraphs, max 5000 characters
- `faq`: Array of Q&A objects (5-8 questions)
  ```json
  [
    {"question": "...", "answer": "..."},
    {"question": "...", "answer": "..."}
  ]
  ```
- `why_climbers_like_it`: Array of 3-7 bullet strings
  ```json
  ["bullet 1", "bullet 2", "bullet 3"]
  ```

### Ratings (6 fields)

All ratings are 1.0-5.0 scale, one decimal place.

- `rating_route_quality`: number
- `rating_cleanliness`: number
- `rating_staff_friendliness`: number
- `rating_facilities`: number
- `rating_value_for_money`: number
- `rating_overall`: number (average of above 5)

## IMPORTANT: Do NOT Include These Fields

❌ `slug` - Not needed in final output
❌ `google_rating` - Use rating_overall instead
❌ `google_reviews_count` - Internal use only
❌ `reviews_link` - Internal use only
❌ `place_id` - Internal use only
❌ `about_raw` - Internal use only
❌ `currency` - Not needed (USD assumed)

## Amenities Separation Logic

**Standard amenities** (go in `amenities` field):
- showers
- lockers
- wifi
- parking
- cafe
- pro_shop
- sauna

**Custom amenities** (go in `custom_amenities` field):
- yoga_studio
- cold_plunge
- coworking_space
- tension_board
- kilter_board
- moon_board
- fitness_area
- yoga_classes
- youth_programs
- coffee_on_tap
- Anything else not in standard list

## Example: Complete Output

```json
{
  "name": "Armadillo Boulders - Stone Oak",
  "address": "23132 US-281, San Antonio, TX 78258",
  "city": "San Antonio",
  "region": "TX",
  "country": "US",
  "latitude": 29.6612,
  "longitude": -98.4485,
  "phone": "+12102514029",
  "email": "stoneoak@armadilloboulders.com",
  "website": "https://www.armadilloboulders.com/",
  "hero_image": "https://lh3.googleusercontent.com/gps-cs-s/...",
  "google_maps_url": "https://www.google.com/maps/search/?api=1&query=...",
  "amenities": "showers|wifi|parking|cafe|pro_shop",
  "custom_amenities": "tension_board|kilter_board|fitness_area|yoga_classes|youth_programs|coffee_on_tap",
  "climbing_types": "bouldering",
  "route_reset_frequency": "varies",
  "total_routes": 120,
  "wall_height_meters": 4.8,
  "training_facilities": "tension_board|kilter_board|weights|spray_wall|campus_board",
  "rental_equipment": "shoes|chalk_bag",
  "beginner_friendly": true,
  "day_pass_price_local": 19,
  "student_discount": true,
  "membership_from_local": 78,
  "difficulty_grades": "V-scale",
  "working_hour": "mon:08:00-22:00|tue:08:00-22:00|wed:08:00-22:00|thu:08:00-22:00|fri:08:00-22:00|sat:08:00-22:00|sun:08:00-22:00",
  "about": "2-3 paragraphs describing the gym...",
  "faq": [
    {"question": "...", "answer": "..."}
  ],
  "why_climbers_like_it": [
    "Access to premium training boards",
    "Spacious fitness area",
    "Consistent route setting"
  ],
  "rating_route_quality": 4.5,
  "rating_cleanliness": 4.8,
  "rating_staff_friendliness": 4.9,
  "rating_facilities": 4.7,
  "rating_value_for_money": 4.5,
  "rating_overall": 4.7
}
```

## Validation Checklist

Before saving, verify:
- ✅ Exactly 32 fields (no more, no less)
- ✅ No internal fields (slug, google_rating, etc.)
- ✅ Standard amenities in `amenities` field only
- ✅ Custom amenities in `custom_amenities` field only
- ✅ Phone format: +1XXXXXXXXXX
- ✅ Region is 2-letter state code
- ✅ Coordinates are decimal degrees
- ✅ Working hours use pipe-separated format
- ✅ All ratings are present and 1.0-5.0 scale
- ✅ `about`, `faq`, and `why_climbers_like_it` are populated
