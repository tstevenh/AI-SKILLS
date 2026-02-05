#!/usr/bin/env python3
"""
Reformat enriched gym JSON files to match exact output schema
"""

import json
import os
from pathlib import Path

# Input/output directory
GYM_DIR = "/Users/tsth/Coding/rockclimbing/zGym"

# Fields to keep (in exact order)
SCHEMA_FIELDS = [
    "name",
    "address",
    "city",
    "region",
    "country",
    "latitude",
    "longitude",
    "phone",
    "email",
    "website",
    "hero_image",
    "google_maps_url",
    "amenities",
    "custom_amenities",
    "climbing_types",
    "route_reset_frequency",
    "total_routes",
    "wall_height_meters",
    "training_facilities",
    "rental_equipment",
    "beginner_friendly",
    "day_pass_price_local",
    "student_discount",
    "membership_from_local",
    "difficulty_grades",
    "working_hour",
    "about",
    "faq",
    "why_climbers_like_it",
    "rating_route_quality",
    "rating_cleanliness",
    "rating_staff_friendliness",
    "rating_facilities",
    "rating_value_for_money",
    "rating_overall"
]

def reformat_gym_json(filepath):
    """Reformat a single gym JSON file to match schema"""

    with open(filepath, 'r') as f:
        data = json.load(f)

    # Create new object with only schema fields
    reformatted = {}

    for field in SCHEMA_FIELDS:
        if field in data:
            reformatted[field] = data[field]
        else:
            # Set null for missing optional fields
            if field in ["email", "custom_amenities", "route_reset_frequency", "total_routes",
                        "wall_height_meters", "training_facilities", "rental_equipment",
                        "day_pass_price_local", "membership_from_local", "difficulty_grades"]:
                reformatted[field] = None

    # Move custom amenities from main amenities if they exist
    if reformatted.get("amenities"):
        standard_amenities = ["showers", "lockers", "wifi", "parking", "cafe", "pro_shop", "sauna"]
        custom_list = []
        standard_list = []
        for amenity in reformatted["amenities"].split("|"):
            if amenity in standard_amenities:
                standard_list.append(amenity)
            else:
                custom_list.append(amenity)

        reformatted["amenities"] = "|".join(standard_list) if standard_list else "showers|lockers|wifi|parking"
        reformatted["custom_amenities"] = "|".join(custom_list) if custom_list else None

    return reformatted

def main():
    """Reformat all gym JSON files"""

    gym_files = list(Path(GYM_DIR).glob("*.json"))

    print(f"Found {len(gym_files)} gym files to reformat\n")

    for filepath in gym_files:
        print(f"Reformatting: {filepath.name}")

        try:
            reformatted = reformat_gym_json(filepath)

            # Write back to same file
            with open(filepath, 'w') as f:
                json.dump(reformatted, f, indent=2, ensure_ascii=False)

            print(f"  ✓ Saved: {filepath.name}\n")

        except Exception as e:
            print(f"  ❌ Error: {e}\n")

    print(f"{'='*60}")
    print(f"Reformatting complete!")
    print(f"{'='*60}")

if __name__ == "__main__":
    main()
