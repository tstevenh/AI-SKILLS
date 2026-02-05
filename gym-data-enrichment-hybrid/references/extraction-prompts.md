# Field Extraction Prompts

Use these prompts when extracting data from gym websites and reviews.

## Contact Information

### email
Extract primary contact email. Look for mailto: links, contact pages, footer.
```
Return single email (e.g., info@example.com). If multiple, choose main/general contact.
```

### phone
Extract phone number. Look for tel: links, contact sections.
```
Return in +1XXXXXXXXXX format (no dashes, spaces, or parentheses).
```

## Climbing Data

### climbing_types
Identify disciplines. Allowed: bouldering|top_rope|lead|speed
```
Keywords: "bouldering", "boulder", "top rope", "toprope", "lead climbing",
"sport climbing", "speed wall", "speed climbing"
Output: pipe-delimited (e.g., "bouldering|top_rope|lead")
```

### difficulty_grades
Extract grade range displayed.
```
Look for: "V0-V10", "VB to V12", "5.6-5.13", "all levels"
Output: Range text (e.g., "V0-V10" or "5.6-5.13a")
```

### total_routes
Extract approximate route/problem count.
```
Look for: "200+ problems", "over 150 routes", "100 boulder problems"
Output: Integer only
```

### wall_height_meters
Extract maximum wall height, convert to meters.
```
Look for: "50 foot walls", "15 meters", "40ft"
Conversion: feet × 0.3048 = meters
Output: Decimal (e.g., 15.24)
```

### route_reset_frequency
Determine reset cadence. Allowed: weekly|biweekly|monthly|quarterly|varies
```
Look for: "weekly resets", "reset every Monday", "monthly route setting"
```

## Amenities & Facilities

### amenities
Standard amenities only. Allowed: showers|lockers|cafe|wifi|parking|sauna|kids_zone|pro_shop
```
Keywords:
- showers: "showers", "shower facilities"
- lockers: "lockers", "locker room"
- cafe: "cafe", "coffee bar", "snack bar"
- wifi: "wifi", "wi-fi", "free internet"
- parking: "parking", "free parking", "parking lot"
- sauna: "sauna", "steam room"
- kids_zone: "kids area", "children's", "youth climbing"
- pro_shop: "pro shop", "gear shop", "retail"
Output: pipe-delimited
```

### custom_amenities
Non-standard amenities not in the above list.
```
Examples: yoga_studio, fitness_area, coworking, tension_board, kilter_board,
moon_board, spray_wall, coffee_on_tap, youth_programs, physical_therapy
Use underscores for spaces. Output: pipe-delimited
```

### training_facilities
Training equipment. Allowed: hangboard|campus_board|treadwall|weights|spray_wall
```
Keywords:
- hangboard: "hangboard", "fingerboard"
- campus_board: "campus board", "campus rungs"
- treadwall: "treadwall", "climbing treadmill"
- weights: "weight room", "free weights", "fitness area"
- spray_wall: "spray wall", "systems wall"
```

### rental_equipment
Rental gear. Allowed: shoes|harness|belay_device|chalk_bag
```
Look for: "shoe rental", "harness rental", "gear rental", "equipment rental"
```

## Pricing

### day_pass_price_local
Adult single visit price.
```
Look for: "day pass", "drop-in", "single visit", "walk-in"
Patterns: "$25", "$20/day", "Day Pass: $22"
Output: Numeric only (e.g., 25)
```

### membership_from_local
Lowest monthly membership.
```
Look for: "monthly membership", "membership starting at", "from $XX/month"
Output: Numeric only (e.g., 89)
```

### student_discount
Whether student discount exists.
```
Look for: "student discount", "student rate", "student pricing", "college discount"
Output: true/false
```

## Operations

### beginner_friendly
Suitability for beginners.
```
Look for: "beginner classes", "intro to climbing", "first-time climbers",
"learn to climb", "beginner-friendly"
Also TRUE if rental equipment available.
Output: true/false
```

### working_hour
Operating hours in pipe-delimited format.
```
Format: mon:HH:MM-HH:MM|tue:HH:MM-HH:MM|wed:HH:MM-HH:MM|thu:HH:MM-HH:MM|fri:HH:MM-HH:MM|sat:HH:MM-HH:MM|sun:HH:MM-HH:MM
Use 24-hour time. Convert: 6am=06:00, 10pm=22:00, 11:30pm=23:30
Example: mon:06:00-22:00|tue:06:00-22:00|wed:06:00-22:00|thu:06:00-22:00|fri:06:00-22:00|sat:09:00-20:00|sun:09:00-20:00
```

## Editorial Content

### about
Generate 2-3 paragraph overview (max 5000 chars).
```
Tone: Friendly local guide
Cover: Climbing style, community vibe, notable features, ideal visitors
Use ONLY factual data found - don't invent details.
```

### faq
Generate 5-8 Q&A pairs as JSON array.
```
Focus on practical visitor questions:
- Hours and pricing
- Rental gear availability
- Beginner programs
- Age requirements
- Booking requirements
- Parking
Only include Q&A you can answer from collected data.
Format: [{"question": "...", "answer": "..."}, ...]
```

### why_climbers_like_it
Extract 3-5 standout positives as JSON array.
```
Source from reviews and website highlights.
Be specific and quote-worthy, not generic.
Format: ["specific point 1", "specific point 2", ...]
```

## Ratings

### Rating Scale
All ratings: 1.0-5.0 with one decimal place.

**Never return null.** Use this fallback chain:
1. Extract from review text
2. Web search for more reviews
3. LLM estimation based on Google rating + gym type

### rating_route_quality
```
Positive: "great routes", "creative setting", "fresh problems", "variety"
Negative: "stale routes", "boring", "same old problems"
Scale:
- 4.5-5.0: Exceptional (world-class, highly praised)
- 4.0-4.4: Very good (creative, regular resets)
- 3.5-3.9: Good (decent variety)
- 3.0-3.4: Adequate (basic, mixed reviews)
- <3.0: Poor (complaints about staleness)
```

### rating_cleanliness
```
Positive: "clean", "well maintained", "spotless"
Negative: "dusty", "dirty", "chalk everywhere", "grimy"
```

### rating_staff_friendliness
```
Positive: "friendly staff", "helpful", "welcoming", "great service"
Negative: "rude", "unhelpful", "ignored"
```

### rating_facilities
```
Positive: "nice showers", "good training area", "great amenities"
Negative: "cramped", "outdated", "lacking"
```

### rating_value_for_money
```
Positive: "worth it", "good deal", "fair prices", "great value"
Negative: "overpriced", "expensive", "not worth it"
```

### rating_overall
```
Calculated: average of the 5 ratings above
Round to 2 decimal places
```
