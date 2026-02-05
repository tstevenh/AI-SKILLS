#!/usr/bin/env python3
"""
Gym Data Enrichment Script - Hybrid Approach
Uses Crawl4AI for fast web crawling + LLM for content synthesis

Requirements:
    pip3 install 'crawl4ai<0.5' beautifulsoup4 pandas

Usage:
    python3 enrich_gyms_hybrid.py --csv gyms.csv --output zGym/ --concurrency 5
"""

import argparse
import asyncio
import csv
import json
import os
import re
import sys
from pathlib import Path
from typing import Dict, List, Optional, Any
from urllib.parse import urljoin, urlparse

# Crawl4AI imports
try:
    from crawl4ai import AsyncWebCrawler
    from bs4 import BeautifulSoup
except ImportError:
    print("Error: Required packages not installed.")
    print("Run: pip3 install 'crawl4ai<0.5' beautifulsoup4 pandas")
    sys.exit(1)

# =============================================================================
# CONFIGURATION
# =============================================================================

STATE_MAP = {
    "Washington": "WA", "California": "CA", "Texas": "TX", "Colorado": "CO",
    "New York": "NY", "Oregon": "OR", "Utah": "UT", "Nevada": "NV",
    "Arizona": "AZ", "Florida": "FL", "Illinois": "IL", "Georgia": "GA",
    "North Carolina": "NC", "Tennessee": "TN", "Virginia": "VA",
    "Ohio": "OH", "Pennsylvania": "PA", "Massachusetts": "MA", "Michigan": "MI"
}

# CSS selectors for climbing gym websites
CSS_SELECTORS = {
    "pricing": [
        ".pricing", ".rates", ".membership", ".day-pass", ".drop-in",
        "[class*='pricing']", "[class*='rates']", "[class*='membership']",
        "#pricing", "#rates", "#membership"
    ],
    "hours": [
        ".hours", ".schedule", ".opening-hours", "table[class*='hour']",
        "[class*='hours']", "[class*='schedule']",
        "#hours", "#schedule"
    ],
    "amenities": [
        ".amenities", ".facilities", ".features", ".offerings",
        "[class*='amenit']", "[class*='facilit']",
        "#amenities", "#facilities"
    ],
    "contact": [
        ".contact", ".footer-contact", ".contact-info",
        "[class*='contact']", "#contact"
    ]
}

# Keywords for extraction
CLIMBING_TYPE_KEYWORDS = ["bouldering", "top rope", "top-rope", "lead", "speed", "sport", "trad"]

STANDARD_AMENITIES = [
    "showers", "lockers", "cafe", "wifi", "parking", "sauna", "kids zone", "kids_zone",
    "pro shop", "pro_shop", "yoga studio", "fitness area", "weight room"
]

CUSTOM_AMENITIES_KEYWORDS = [
    "tension board", "tension_board", "kilter board", "kilter_board", "moon board",
    "moon_board", "spray wall", "spray_wall", "campus board", "campus_board",
    "hangboard", "hang board", "treadwall", "coworking", "cold plunge", "pilates"
]

TRAINING_FACILITIES = [
    "hangboard", "campus board", "treadwall", "weights", "spray wall",
    "training board", "system wall"
]

RENTAL_EQUIPMENT = ["shoes", "harness", "belay device", "chalk bag", "chalk"]

# =============================================================================
# UTILITY FUNCTIONS
# =============================================================================

def clean_decimal(value: Any) -> Optional[float]:
    """Fix decimal formatting from Outscraper exports"""
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


def clean_phone(phone: str) -> Optional[str]:
    """Format phone to +1XXXXXXXXXX format"""
    if not phone:
        return None
    digits = re.sub(r'[^\d]', '', str(phone))
    if len(digits) == 10:
        return f"+1{digits}"
    elif len(digits) == 11 and digits.startswith('1'):
        return f"+{digits}"
    return phone


def slugify(name: str) -> str:
    """Convert name to kebab-case"""
    name = name.lower()
    name = re.sub(r'[^\w\s-]', '', name)
    name = re.sub(r'[-\s]+', '-', name)
    return name.strip('-')


def get_safe_filename(base_path: Path, name: str, counter: int = 0) -> Path:
    """Get unique filename, appending counter if needed"""
    slug = slugify(name)
    if counter > 0:
        slug = f"{slug}-{counter}"
    filepath = base_path / f"{slug}.json"
    if filepath.exists():
        return get_safe_filename(base_path, name, counter + 1)
    return filepath


def extract_price_from_text(text: str) -> Optional[float]:
    """Extract price like $25, 25.00, $25.00 from text"""
    if not text:
        return None
    # Find patterns like $25, $25.00, 25.00
    patterns = [
        r'\$(\d+\.?\d*)',
        r'(\d+\.\d{2})',
        r'(\d+)\s*dollars?',
    ]
    for pattern in patterns:
        match = re.search(pattern, text)
        if match:
            try:
                price = float(match.group(1))
                if 0 < price < 500:  # Sanity check
                    return price
            except:
                pass
    return None


def parse_hours_from_html(html: str) -> Optional[str]:
    """Parse operating hours from HTML content"""
    if not html:
        return None

    day_map = {
        "monday": "mon", "tuesday": "tue", "wednesday": "wed",
        "thursday": "thu", "friday": "fri", "saturday": "sat", "sunday": "sun",
        "mon": "mon", "tue": "tue", "wed": "wed", "thu": "thu",
        "fri": "fri", "sat": "sat", "sun": "sun"
    }

    # Look for time patterns like 9:00 AM - 10:00 PM
    time_pattern = r'(\d{1,2}):?(\d{2})?\s*(AM|PM|am|pm)'

    results = []
    soup = BeautifulSoup(html, 'html.parser')

    # Common hour section selectors
    hour_sections = soup.select('.hours, .schedule, .opening-hours, [class*="hour"]')

    for section in hour_sections:
        text = section.get_text()
        lines = text.split('\n')

        for line in lines:
            line = line.strip().lower()
            for full_day, short_day in day_map.items():
                if full_day in line:
                    times = re.findall(time_pattern, line)
                    if times and len(times[0]) >= 3:
                        hour, minute, ampm = times[0]
                        hour = int(hour)
                        if ampm.upper() == 'PM' and hour != 12:
                            hour += 12
                        elif ampm.upper() == 'AM' and hour == 12:
                            hour = 0
                        open_time = f"{hour:02d}:{int(times[0][1]) if times[0][1] else '00':02d}"
                        # Look for closing time
                        if len(times) > 1:
                            hour2, minute2, ampm2 = times[1]
                            hour2 = int(hour2)
                            if ampm2.upper() == 'PM' and hour2 != 12:
                                hour2 += 12
                            elif ampm2.upper() == 'AM' and hour2 == 12:
                                hour2 = 0
                            close_time = f"{hour2:02d}:{int(minute2) if minute2 else '00':02d}"
                        else:
                            close_time = "22:00"  # Default close

                        results.append(f"{short_day}:{open_time}-{close_time}")
                        break

    return '|'.join(results) if len(results) == 7 else None


# =============================================================================
# CRAWL4AI EXTRACTION FUNCTIONS
# =============================================================================

async def crawl_gym_website(url: str, max_pages: int = 3) -> Dict[str, Any]:
    """
    Deep crawl a gym website using Crawl4AI

    Returns:
        {
            'markdown': str,  # Clean markdown content
            'email': Optional[str],
            'phone': Optional[str],
            'climbing_types': List[str],
            'amenities': List[str],
            'custom_amenities': List[str],
            'day_pass_price': Optional[float],
            'membership_price': Optional[float],
            'hours': Optional[str],
            'content_sections': Dict[str, str],  # Separate sections by type
            'all_links': List[str]
        }
    """
    result = {
        'markdown': '',
        'email': None,
        'phone': None,
        'climbing_types': [],
        'amenities': [],
        'custom_amenities': [],
        'day_pass_price': None,
        'membership_price': None,
        'hours': None,
        'content_sections': {},
        'all_links': []
    }

    try:
        async with AsyncWebCrawler(
            verbose=False,
            headless=True,
            bypass_cache=True
        ) as crawler:
            # Main crawl
            crawl_result = await crawler.arun(
                url=url,
                word_count_threshold=10,
                exclude_tags=['nav', 'footer', 'header', 'script', 'style'],
                # Deep crawl settings
                deep_crawl_strategy="bfs",
                max_pages=max_pages,
            )

            if crawl_result.markdown:
                result['markdown'] = crawl_result.markdown

                # Extract email
                email_match = re.search(r'[\w.+-]+@[\w-]+\.[\w.-]+', crawl_result.markdown)
                if email_match:
                    result['email'] = email_match.group(0)

                # Extract phone
                phone_match = re.search(r'\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}', crawl_result.markdown)
                if phone_match:
                    result['phone'] = clean_phone(phone_match.group(0))

                # Extract climbing types
                markdown_lower = crawl_result.markdown.lower()
                for ct in CLIMBING_TYPE_KEYWORDS:
                    if ct in markdown_lower:
                        normalized = ct.replace('-', '_').replace(' ', '_')
                        if normalized not in result['climbing_types']:
                            result['climbing_types'].append(normalized)

                # Extract standard amenities
                for amenity in STANDARD_AMENITIES:
                    if amenity.replace('_', ' ') in markdown_lower or amenity in markdown_lower:
                        normalized = amenity.replace(' ', '_')
                        if normalized not in result['amenities']:
                            result['amenities'].append(normalized)

                # Extract custom amenities
                for custom in CUSTOM_AMENITIES_KEYWORDS:
                    if custom in markdown_lower:
                        normalized = custom.replace(' ', '_')
                        if normalized not in result['custom_amenities']:
                            result['custom_amenities'].append(normalized)

                # Extract pricing
                # Look for day pass pricing
                for pattern in [
                    r'day pass[:\s*$]?(\d+\.?\d*)',
                    r'drop-?in[:\s*$]?(\d+\.?\d*)',
                    r'admission[:\s*$]?(\d+\.?\d*)'
                ]:
                    match = re.search(pattern, markdown_lower)
                    if match:
                        try:
                            result['day_pass_price'] = float(match.group(1))
                            break
                        except:
                            pass

                # Look for membership pricing
                for pattern in [
                    r'monthly[:\s*$]?(\d+\.?\d*)',
                    r'membership[:\s*$]?(\d+\.?\d*)',
                    r'unlimited[:\s*$]?(\d+\.?\d*)'
                ]:
                    match = re.search(pattern, markdown_lower)
                    if match:
                        try:
                            result['membership_price'] = float(match.group(1))
                            break
                        except:
                            pass

                # Extract hours using parse function
                result['hours'] = parse_hours_from_html(crawl_result.html)

                # Store all links found
                if crawl_result.links:
                    result['all_links'] = [link.get('href', '') for link in crawl_result.links if link.get('href')]

    except Exception as e:
        print(f"    ⚠️  Crawl4AI error: {e}")

    return result


# =============================================================================
# DATA ENRICHMENT FUNCTIONS
# =============================================================================

def clean_outscraper_data(row: Dict[str, Any]) -> Dict[str, Any]:
    """Phase 1: Clean and transform Outscraper data"""

    state_name = row.get('state', '')
    gym = {
        'name': row.get('name', ''),
        'address': row.get('full_address', row.get('address', '')),
        'city': row.get('city', ''),
        'region': STATE_MAP.get(state_name, row.get('state_code', '')),
        'country': row.get('country_code', 'US'),
        'latitude': clean_decimal(row.get('latitude')),
        'longitude': clean_decimal(row.get('longitude')),
        'phone': clean_phone(row.get('phone', '')),
        'website': row.get('site', row.get('website', '')),
        'hero_image': row.get('photo', ''),
        'google_maps_url': row.get('location_link', ''),
    }

    # Parse about JSON if available
    about_json = row.get('about', '')
    if about_json:
        try:
            about_data = json.loads(about_json.replace('""', '"'))
            gym['about_raw'] = about_data
        except:
            pass

    return gym


async def enrich_single_gym(
    row: Dict[str, Any],
    idx: int,
    total: int
) -> Dict[str, Any]:
    """
    Enrich a single gym with Crawl4AI crawling

    This is a READY-TO-USE function that returns the gym object with
    all fields extracted. LLM content generation (about, FAQ, ratings)
    should be done separately using the extracted data.
    """

    gym_name = row.get('name', f'Gym_{idx}')
    print(f"[{idx}/{total}] Processing: {gym_name}")

    # Phase 1: Clean Outscraper data
    gym = clean_outscraper_data(row)
    website = gym.get('website')

    # Phase 2: Crawl website with Crawl4AI
    if website:
        try:
            print(f"    🌐 Crawling {website}...")
            crawl_data = await crawl_gym_website(website, max_pages=3)

            # Merge crawled data
            if crawl_data['email']:
                gym['email'] = crawl_data['email']
            if crawl_data['phone'] and not gym.get('phone'):
                gym['phone'] = crawl_data['phone']

            gym['climbing_types'] = '|'.join(crawl_data['climbing_types']) if crawl_data['climbing_types'] else None
            gym['amenities'] = '|'.join(crawl_data['amenities']) if crawl_data['amenities'] else None
            gym['custom_amenities'] = '|'.join(crawl_data['custom_amenities']) if crawl_data['custom_amenities'] else None
            gym['day_pass_price_local'] = crawl_data['day_pass_price']
            gym['membership_from_local'] = crawl_data['membership_price']
            gym['working_hour'] = crawl_data['hours']

            # Store markdown for LLM processing
            gym['_raw_markdown'] = crawl_data['markdown']
            gym['_crawl_data'] = crawl_data

            print(f"    ✓ Extracted: types={gym.get('climbing_types')}, "
                  f"amenities={len(crawl_data['amenities'])}, "
                  f"custom={len(crawl_data['custom_amenities'])}")

        except Exception as e:
            print(f"    ❌ Crawl error: {e}")

    # Phase 3-5: These would need review scraping and LLM generation
    # For now, set placeholder values that should be filled by LLM
    if not gym.get('about'):
        gym['about'] = None  # To be generated by LLM
    if not gym.get('faq'):
        gym['faq'] = []  # To be generated by LLM
    if not gym.get('why_climbers_like_it'):
        gym['why_climbers_like_it'] = []  # To be generated by LLM

    # Default ratings (to be improved by LLM analysis)
    for rating_field in ['rating_route_quality', 'rating_cleanliness',
                         'rating_staff_friendliness', 'rating_facilities',
                         'rating_value_for_money']:
        if rating_field not in gym:
            gym[rating_field] = 4.0  # Default baseline

    gym['rating_overall'] = 4.0  # Will be calculated

    return gym


async def process_batch(
    rows: List[Dict[str, Any]],
    output_dir: Path,
    concurrency: int = 5
) -> Dict[str, int]:
    """Process a batch of gyms with parallel crawling"""

    stats = {'processed': 0, 'saved': 0, 'flagged': 0, 'errors': 0}
    output_dir.mkdir(parents=True, exist_ok=True)

    # Process in chunks for concurrency control
    for i in range(0, len(rows), concurrency):
        chunk = rows[i:i + concurrency]
        tasks = [
            enrich_single_gym(row, i + j + 1, len(rows))
            for j, row in enumerate(chunk)
        ]

        results = await asyncio.gather(*tasks, return_exceptions=True)

        for result in results:
            if isinstance(result, Exception):
                print(f"    ❌ Error: {result}")
                stats['errors'] += 1
                continue

            stats['processed'] += 1

            # Check for flagging conditions
            subtypes = result.get('_raw_outscraper', {}).get('subtypes', '').lower()
            if any(x in subtypes for x in ['trampoline', 'playground', 'amusement', 'arcade']):
                print(f"    ⚠️  FLAGGED: Non-climbing subtype")
                stats['flagged'] += 1
                result['_status'] = 'flagged'
            elif not result.get('website'):
                print(f"    ⚠️  FLAGGED: No website")
                stats['flagged'] += 1
                result['_status'] = 'flagged'
            else:
                # Save enriched gym
                filepath = get_safe_filename(output_dir, result['name'])
                with open(filepath, 'w', encoding='utf-8') as f:
                    json.dump(result, f, indent=2, ensure_ascii=False)
                print(f"    💾 Saved: {filepath.name}")
                stats['saved'] += 1
                result['_status'] = 'done'

    return stats


# =============================================================================
# MAIN
# =============================================================================

async def main_async(args):
    """Async main function"""

    input_csv = Path(args.csv)
    output_dir = Path(args.output)

    if not input_csv.exists():
        print(f"Error: CSV file not found: {input_csv}")
        sys.exit(1)

    print(f"📂 Reading: {input_csv}")
    print(f"📁 Output: {output_dir}")
    print(f"🔄 Concurrency: {args.concurrency}")
    print(f"🌐 Using: Crawl4AI for web crawling")
    print()

    # Read CSV
    rows = []
    with open(input_csv, 'r', encoding='utf-8-sig') as f:
        reader = csv.DictReader(f, delimiter=';' if ';' in f.read(1000) else ',')
        f.seek(0)
        reader = csv.DictReader(f, delimiter=';')
        rows = list(reader)

    # Filter already processed if enrichment_status column exists
    has_status = any('enrichment_status' in row for row in rows)
    if has_status:
        rows = [r for r in rows if not r.get('enrichment_status')]

    print(f"📊 Processing {len(rows)} gyms...")
    print("=" * 60)

    # Process batch
    stats = await process_batch(
        rows,
        output_dir,
        concurrency=args.concurrency
    )

    print()
    print("=" * 60)
    print("✅ Batch Complete!")
    print(f"  Processed: {stats['processed']}")
    print(f"  Saved:     {stats['saved']}")
    print(f"  Flagged:   {stats['flagged']}")
    print(f"  Errors:    {stats['errors']}")
    print(f"  Output:    {output_dir}")
    print("=" * 60)


def main():
    """CLI entry point"""
    parser = argparse.ArgumentParser(
        description='Enrich climbing gym data using Crawl4AI + LLM hybrid approach'
    )
    parser.add_argument('--csv', required=True, help='Input CSV file from Outscraper')
    parser.add_argument('--output', default='zGym', help='Output directory for JSON files')
    parser.add_argument('--concurrency', type=int, default=5, help='Parallel crawl concurrency')
    parser.add_argument('--max-pages', type=int, default=3, help='Max pages to crawl per gym')

    args = parser.parse_args()

    # Run async main
    asyncio.run(main_async(args))


if __name__ == "__main__":
    main()
