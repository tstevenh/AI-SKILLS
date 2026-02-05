#!/usr/bin/env python3
"""
Gym Data Enrichment Script - Batch 7 (Rows 81-100)
"""

import csv
import json
import re
from pathlib import Path

# Configuration
INPUT_CSV = "/Users/tsth/Coding/rockclimbing/new_gyms_to_add.csv"
OUTPUT_DIR = "/Users/tsth/Coding/rockclimbing/zGym"
START_ROW = 81
BATCH_SIZE = 20
STATE_MAP = {
    "Washington": "WA", "California": "CA", "Texas": "TX", "Colorado": "CO",
    "New York": "NY", "Oregon": "OR", "Utah": "UT", "Nevada": "NV",
    "Arizona": "AZ", "Florida": "FL", "Illinois": "IL", "Georgia": "GA",
    "North Carolina": "NC", "Tennessee": "TN", "Virginia": "VA", "Kentucky": "KY",
    "Michigan": "MI", "Indiana": "IN", "Ohio": "OH", "Pennsylvania": "PA",
    "Massachusetts": "MA", "Wisconsin": "WI", "Missouri": "MO"
}

def clean_decimal(value):
    """Fix decimal formatting"""
    if not value:
        return None
    cleaned = str(value).replace(',', '.').replace(';', '')
    try:
        num = float(cleaned)
        if abs(num) > 1000:
            num = num / 100
        return round(num, 6)
    except:
        return None

def clean_phone(phone):
    """Format phone: +1XXXXXXXXXX"""
    if not phone:
        return None
    digits = re.sub(r'[^\d]', '', str(phone))
    if len(digits) == 10:
        return f"+1{digits}"
    elif len(digits) == 11 and digits.startswith('1'):
        return f"+{digits}"
    return phone

def parse_hours(csv_hours):
    """Parse working hours from CSV format to pipe-separated format"""
    if not csv_hours:
        return None

    day_map = {
        "Monday": "mon", "Tuesday": "tue", "Wednesday": "wed",
        "Thursday": "thu", "Friday": "fri", "Saturday": "sat", "Sunday": "sun"
    }

    try:
        result = []
        for day_entry in csv_hours.split('|'):
            parts = day_entry.split(',')
            if len(parts) == 3:
                day, open_time, close_time = parts
                if day in day_map:
                    def time_to_24hr(t_str):
                        t_str = t_str.strip().replace('AM', '').replace('PM', '')
                        parts = t_str.split(':')
                        hour = int(parts[0])
                        minute = int(parts[1]) if len(parts) > 1 else 0
                        if 'PM' in t_str and hour != 12:
                            hour += 12
                        if 'AM' in t_str and hour == 12:
                            hour = 0
                        return f"{hour:02d}:{minute:02d}"

                    result.append(f"{day_map[day]}:{time_to_24hr(open_time)}-{time_to_24hr(close_time)}")

        return '|'.join(result) if result else None
    except Exception as e:
        print(f"    Warning: Could not parse hours: {e}")
        return None

def slugify(name):
    """Convert name to kebab-case"""
    name = name.lower()
    name = re.sub(r'[^\w\s-]', '', name)
    name = re.sub(r'[-\s]+', '-', name)
    return name.strip('-')

def get_safe_filename(base_path, name, counter=0):
    """Get unique filename, appending counter if needed"""
    slug = slugify(name)
    if counter > 0:
        slug = f"{slug}-{counter}"
    filepath = base_path / f"{slug}.json"
    if filepath.exists():
        return get_safe_filename(base_path, name, counter + 1)
    return filepath

def process_gym_row(row):
    """Process a single CSV row into enriched gym object"""
    name = row.get('name', '')
    website = row.get('website', '')
    latitude = clean_decimal(row.get('latitude'))
    longitude = clean_decimal(row.get('longitude'))
    state_name = row.get('state', '')

    gym = {
        "name": name,
        "slug": slugify(name),
        "address": row.get('address', ''),
        "city": row.get('city', ''),
        "region": STATE_MAP.get(state_name, row.get('state_code', '')),
        "country": row.get('country_code', 'US'),
        "latitude": latitude,
        "longitude": longitude,
        "phone": clean_phone(row.get('phone', '')),
        "website": website if website else None,
        "hero_image": row.get('photo', ''),
        "google_maps_url": row.get('location_link', ''),
        "google_rating": clean_decimal(row.get('rating', '')),
        "google_reviews_count": int(row.get('reviews', 0)) if row.get('reviews') else None,
        "reviews_link": row.get('reviews_link', ''),
        "working_hour": parse_hours(row.get('other_hours', row.get('working_hours_csv_compatible', ''))),
        "place_id": row.get('place_id', '')
    }

    about_json = row.get('about', '')
    if about_json:
        try:
            about_data = json.loads(about_json.replace('""', '"'))
            gym['about_raw'] = about_data
        except:
            pass

    return gym

def main():
    """Main processing function"""
    Path(OUTPUT_DIR).mkdir(parents=True, exist_ok=True)

    print(f"Reading {INPUT_CSV}...")
    print(f"Starting from row {START_ROW}, processing {BATCH_SIZE} gyms (rows {START_ROW}-{START_ROW+BATCH_SIZE-1})\n")
    gyms_processed = 0
    gyms_saved = 0
    gyms_flagged = 0
    current_row = 0

    with open(INPUT_CSV, 'r', encoding='utf-8-sig') as f:
        reader = csv.DictReader(f, delimiter=';')

        for row in reader:
            current_row += 1

            if current_row < START_ROW:
                continue

            if gyms_processed >= BATCH_SIZE:
                print(f"\nBatch complete: Processed {BATCH_SIZE} gyms (rows {START_ROW}-{current_row-1})")
                break

            gym_name = row.get('name', f'Gym_{current_row}')
            print(f"[{gyms_processed+1}/{BATCH_SIZE}] Processing row {current_row}: {gym_name}")

            try:
                gym = process_gym_row(row)

                subtypes = row.get('subtypes', '').lower()
                if any(x in subtypes for x in ['trampoline', 'playground', 'amusement', 'arcade']):
                    print(f"  ⚠️  FLAGGED: Non-climbing subtype: {subtypes}")
                    status = 'flagged'
                    gyms_flagged += 1
                elif not gym.get('website'):
                    print(f"  ⚠️  FLAGGED: No website")
                    status = 'flagged'
                    gyms_flagged += 1
                else:
                    print(f"  ✓ Basic data extracted, ready for full enrichment")
                    status = 'enriching'
                    gyms_saved += 1

                    filepath = get_safe_filename(Path(OUTPUT_DIR), gym_name)
                    with open(filepath, 'w', encoding='utf-8') as out:
                        json.dump(gym, out, indent=2, ensure_ascii=False)
                    print(f"  💾 Saved: {filepath.name}")

            except Exception as e:
                print(f"  ❌ Error: {e}")
                status = 'error'

            gyms_processed += 1

    print(f"\n{'='*60}")
    print(f"Processing Summary:")
    print(f"  Processed: {gyms_processed}")
    print(f"  Saved:     {gyms_saved}")
    print(f"  Flagged:   {gyms_flagged}")
    print(f"  Output:    {OUTPUT_DIR}")
    print(f"{'='*60}")

if __name__ == "__main__":
    main()
