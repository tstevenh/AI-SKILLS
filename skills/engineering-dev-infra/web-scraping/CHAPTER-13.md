# Chapter 13: Data Cleaning and Normalization

## Table of Contents
1. [Introduction to Data Cleaning](#introduction)
2. [Text Normalization Techniques](#text-normalization)
3. [Price and Currency Handling](#price-handling)
4. [Date and Time Parsing](#date-parsing)
5. [Category and Taxonomy Mapping](#taxonomy)
6. [Image URL Processing](#image-processing)
7. [Deduplication Strategies](#deduplication)
8. [Quality Scoring](#quality-scoring)

---

## Introduction to Data Cleaning

Raw scraped data is rarely usable without cleaning. Websites present information in inconsistent formats, with varying encodings, mixed currencies, and irregular date formats. This chapter covers comprehensive techniques for transforming messy scraped data into clean, structured datasets ready for analysis or storage.

### The Data Cleaning Pipeline

Data cleaning follows a logical sequence:

1. **Decode and Normalize Encoding** - Ensure consistent character encoding
2. **Strip Whitespace and Control Characters** - Remove invisible formatting
3. **Standardize Case** - Consistent capitalization for comparison
4. **Parse and Normalize Values** - Convert strings to typed values
5. **Validate and Flag** - Mark problematic records
6. **Enrich and Augment** - Add computed fields

---

## Text Normalization Techniques

### Whitespace Handling

```python
import re
import unicodedata

class TextNormalizer:
    """Comprehensive text normalization for scraped data"""
    
    # Unicode whitespace characters beyond regular space
    WHITESPACE_CHARS = [
        '\\t', '\\n', '\\r', '\\f', '\\v',           # Control chars
        '\\u00A0', '\\u2000', '\\u2001', '\\u2002',  # Various spaces
        '\\u2003', '\\u2004', '\\u2005', '\\u2006',
        '\\u2007', '\\u2008', '\\u2009', '\\u200A',
        '\\u202F', '\\u205F', '\\u3000',
    ]
    
    @classmethod
    def normalize_whitespace(cls, text):
        """Collapse all whitespace to single spaces"""
        if not text:
            return ''
        
        # Replace all whitespace chars with regular space
        pattern = '[' + ''.join(cls.WHITESPACE_CHARS) + ']'
        text = re.sub(pattern, ' ', text)
        
        # Collapse multiple spaces
        text = re.sub(r' +', ' ', text)
        
        return text.strip()
    
    @classmethod
    def remove_control_chars(cls, text):
        """Remove non-printable control characters"""
        if not text:
            return ''
        
        # Keep tabs, newlines, spaces; remove other control chars
        return ''.join(
            char for char in text
            if unicodedata.category(char)[0] != 'C' or char in '\\t\\n\\r '
        )
    
    @classmethod
    def normalize_unicode(cls, text, form='NFKC'):
        """Normalize unicode characters to canonical form"""
        if not text:
            return ''
        return unicodedata.normalize(form, text)
    
    @classmethod
    def clean_html_entities(cls, text):
        """Decode HTML entities"""
        import html
        if not text:
            return ''
        return html.unescape(text)
    
    @classmethod
    def full_clean(cls, text):
        """Apply all cleaning steps"""
        text = cls.clean_html_entities(text)
        text = cls.normalize_unicode(text)
        text = cls.remove_control_chars(text)
        text = cls.normalize_whitespace(text)
        return text


# Usage examples
test_cases = [
    "  Multiple   spaces  and\\ttabs\\n\\nnewlines  ",
    "Price:&#160;$100&#x20;USD",  # HTML entities
    "Caf\\u00e9",  # Unicode
    "\\xa0\\u2002\\u3000weird spaces\\xa0",  # Various spaces
]

for test in test_cases:
    print(f"Before: {repr(test)}")
    print(f"After:  {repr(TextNormalizer.full_clean(test))}")
    print()
```

### Case Normalization

```python
class CaseNormalizer:
    """Handle text case consistently"""
    
    @staticmethod
    def title_case(text):
        """Smart title case that handles small words"""
        if not text:
            return text
        
        small_words = {'a', 'an', 'the', 'and', 'but', 'or', 'for', 'nor',
                       'on', 'at', 'to', 'from', 'by', 'in', 'of'}
        
        words = text.lower().split()
        result = []
        
        for i, word in enumerate(words):
            if i == 0 or i == len(words) - 1 or word not in small_words:
                result.append(word.capitalize())
            else:
                result.append(word)
        
        return ' '.join(result)
    
    @staticmethod
    def normalize_brand_name(name):
        """Normalize brand names to canonical form"""
        brand_mapping = {
            'apple': 'Apple',
            'APPLE': 'Apple',
            'samsung': 'Samsung',
            'SAMSUNG': 'Samsung',
            'sony': 'Sony',
            'SONY': 'Sony',
        }
        
        normalized = name.lower().strip()
        return brand_mapping.get(normalized, name)
```

---

## Price and Currency Handling

### Comprehensive Price Parser

```python
from decimal import Decimal, InvalidOperation
from dataclasses import dataclass
from typing import Optional, Tuple
import re


@dataclass
class ParsedPrice:
    """Structured price data"""
    amount: Optional[Decimal]
    currency_code: Optional[str]
    original_string: str
    is_range: bool = False
    min_amount: Optional[Decimal] = None
    max_amount: Optional[Decimal] = None
    per_unit: Optional[str] = None
    
    @property
    def is_valid(self):
        return self.amount is not None


class PriceParser:
    """Parse prices from various string formats"""
    
    # Currency symbols and codes
    CURRENCY_MAP = {
        '$': 'USD', 'USD': 'USD',
        '€': 'EUR', 'EUR': 'EUR',
        '£': 'GBP', 'GBP': 'GBP',
        '¥': 'JPY', 'JPY': 'JPY', 'CN¥': 'CNY',
        '₹': 'INR', 'INR': 'INR',
        'A$': 'AUD', 'AU$': 'AUD', 'AUD': 'AUD',
        'C$': 'CAD', 'CA$': 'CAD', 'CAD': 'CAD',
        'CHF': 'CHF', 'Fr.': 'CHF',
    }
    
    # Price patterns
    PRICE_PATTERN = re.compile(
        r'(?P<currency>[$€£¥]|USD|EUR|GBP|AUD|CAD|CHF)?'
        r'\\s*'
        r'(?P<amount>[\d,]+(?:\.\d{2})?)'
        r'(?P<suffix>\\s*(?:USD|EUR|GBP|each|per|/))?
    ', re.IGNORECASE)
    
    RANGE_PATTERNS = [
        re.compile(r'\$?([\d,]+(?:\.\d{2})?)\s*-\s*\$?([\d,]+(?:\.\d{2})?)'),
        re.compile(r'\$?([\d,]+(?:\.\d{2})?)\s*to\s*\$?([\d,]+(?:\.\d{2})?)'),
    ]
    
    def parse(self, price_string: str) -> ParsedPrice:
        """Parse a price string into structured data"""
        if not price_string:
            return ParsedPrice(None, None, price_string)
        
        # Try range patterns first
        for pattern in self.RANGE_PATTERNS:
            match = pattern.search(price_string)
            if match:
                min_str, max_str = match.groups()
                return ParsedPrice(
                    amount=None,
                    currency_code=self._detect_currency(price_string),
                    original_string=price_string,
                    is_range=True,
                    min_amount=self._parse_amount(min_str),
                    max_amount=self._parse_amount(max_str),
                )
        
        # Try single price pattern
        match = self.PRICE_PATTERN.search(price_string)
        if match:
            amount = self._parse_amount(match.group('amount'))
            currency = self._detect_currency(price_string)
            
            return ParsedPrice(
                amount=amount,
                currency_code=currency,
                original_string=price_string,
            )
        
        # Fallback: just extract numbers
        numbers = re.findall(r'[\d,]+(?:\.\d{2})?', price_string)
        if numbers:
            return ParsedPrice(
                amount=self._parse_amount(numbers[0]),
                currency_code=None,
                original_string=price_string,
            )
        
        return ParsedPrice(None, None, price_string)
    
    def _parse_amount(self, amount_str: str) -> Optional[Decimal]:
        """Parse numeric amount string"""
        if not amount_str:
            return None
        
        # Remove thousands separators
        clean = amount_str.replace(',', '')
        
        try:
            return Decimal(clean)
        except InvalidOperation:
            return None
    
    def _detect_currency(self, text: str) -> Optional[str]:
        """Detect currency from text"""
        text_upper = text.upper()
        
        for symbol, code in self.CURRENCY_MAP.items():
            if symbol in text or code in text_upper:
                return code
        
        return None
    
    @staticmethod
    def normalize_currency_code(code: str) -> str:
        """Normalize currency code to ISO 4217"""
        mapping = {
            'US': 'USD', 'USA': 'USD', 'DOLLAR': 'USD', 'DOLLARS': 'USD',
            'EURO': 'EUR', 'EUROS': 'EUR',
            'POUND': 'GBP', 'POUNDS': 'GBP', 'STERLING': 'GBP',
        }
        return mapping.get(code.upper(), code.upper())


class PriceConverter:
    """Convert prices between currencies"""
    
    def __init__(self, rates: dict = None):
        # Default rates (would normally fetch from API)
        self.rates = rates or {
            'USD': 1.0,
            'EUR': 0.92,
            'GBP': 0.79,
            'JPY': 149.50,
            'AUD': 1.53,
            'CAD': 1.35,
        }
    
    def convert(self, amount: Decimal, from_currency: str, to_currency: str) -> Decimal:
        """Convert amount between currencies"""
        if from_currency == to_currency:
            return amount
        
        # Convert to USD first, then to target
        usd_amount = amount / Decimal(str(self.rates[from_currency]))
        return usd_amount * Decimal(str(self.rates[to_currency]))


# Usage
parser = PriceParser()
test_prices = [
    "$99.99",
    "€150,00",
    "$50 - $100",
    "£45.50 GBP",
    "Was $200, Now $150",
    "¥12,800",
]

for price in test_prices:
    result = parser.parse(price)
    print(f"{price} -> {result}")
```

---

## Date and Time Parsing

### Flexible Date Parser

```python
from datetime import datetime, date
from dateutil import parser as date_parser
import pytz


class DateParser:
    """Parse dates from various string formats"""
    
    DATE_FORMATS = [
        '%Y-%m-%d',           # ISO format: 2024-01-15
        '%m/%d/%Y',           # US format: 01/15/2024
        '%d/%m/%Y',           # European: 15/01/2024
        '%B %d, %Y',          # January 15, 2024
        '%b %d, %Y',          # Jan 15, 2024
        '%d %B %Y',           # 15 January 2024
        '%Y%m%d',             # Compact: 20240115
        '%d-%b-%Y',           # 15-Jan-2024
    ]
    
    RELATIVE_TERMS = {
        'today': 0,
        'yesterday': -1,
        'tomorrow': 1,
    }
    
    @classmethod
    def parse(cls, date_string: str, default_timezone='UTC') -> Optional[datetime]:
        """Parse date from string with multiple strategies"""
        if not date_string:
            return None
        
        # Clean the input
        date_string = date_string.strip().lower()
        
        # Handle relative terms
        if date_string in cls.RELATIVE_TERMS:
            days = cls.RELATIVE_TERMS[date_string]
            return datetime.now(pytz.timezone(default_timezone)) + timedelta(days=days)
        
        # Try each format
        for fmt in cls.DATE_FORMATS:
            try:
                parsed = datetime.strptime(date_string, fmt)
                return pytz.timezone(default_timezone).localize(parsed)
            except ValueError:
                continue
        
        # Fallback to dateutil parser
        try:
            parsed = date_parser.parse(date_string, fuzzy=True)
            if parsed.tzinfo is None:
                parsed = pytz.timezone(default_timezone).localize(parsed)
            return parsed
        except (ValueError, TypeError):
            return None
    
    @classmethod
    def normalize_to_iso(cls, date_string: str) -> Optional[str]:
        """Parse and return ISO format string"""
        parsed = cls.parse(date_string)
        return parsed.isoformat() if parsed else None


from datetime import timedelta


class DateRangeParser:
    """Parse date ranges from strings"""
    
    RANGE_PATTERNS = [
        (re.compile(r'(\w+\s+\d{1,2},?\s+\d{4})\s*-\s*(\w+\s+\d{1,2},?\s+\d{4})'), 'explicit'),
        (re.compile(r'(\d{1,2}/\d{1,2}/\d{4})\s*-\s*(\d{1,2}/\d{1,2}/\d{4})'), 'us_date'),
        (re.compile(r'(\d{4}-\d{2}-\d{2})\s*to\s*(\d{4}-\d{2}-\d{2})'), 'iso_range'),
    ]
    
    def parse(self, range_string: str) -> Tuple[Optional[datetime], Optional[datetime]]:
        """Parse a date range string"""
        if not range_string:
            return None, None
        
        for pattern, fmt in self.RANGE_PATTERNS:
            match = pattern.search(range_string)
            if match:
                start_str, end_str = match.groups()
                start = DateParser.parse(start_str)
                end = DateParser.parse(end_str)
                return start, end
        
        # Single date - treat as range of one day
        single = DateParser.parse(range_string)
        if single:
            end = single + timedelta(days=1)
            return single, end
        
        return None, None
```

---

## Category and Taxonomy Mapping

### Hierarchical Category System

```python
class CategoryMapper:
    """Map scraped categories to canonical taxonomy"""
    
    def __init__(self, taxonomy_file=None):
        self.taxonomy = self._load_taxonomy(taxonomy_file)
        self.aliases = self._build_alias_map()
    
    def _load_taxonomy(self, filepath):
        """Load category taxonomy"""
        default_taxonomy = {
            'Electronics': {
                'id': 'elec',
                'children': {
                    'Computers': {
                        'id': 'elec.comp',
                        'children': {
                            'Laptops': {'id': 'elec.comp.lap'},
                            'Desktops': {'id': 'elec.comp.desk'},
                            'Tablets': {'id': 'elec.comp.tab'},
                        }
                    },
                    'Phones': {
                        'id': 'elec.phon',
                        'children': {
                            'Smartphones': {'id': 'elec.phon.smart'},
                            'Accessories': {'id': 'elec.phon.acc'},
                        }
                    },
                }
            },
            'Clothing': {
                'id': 'cloth',
                'children': {
                    'Men': {
                        'id': 'cloth.men',
                        'children': {
                            'Shirts': {'id': 'cloth.men.shirt'},
                            'Pants': {'id': 'cloth.men.pant'},
                        }
                    },
                    'Women': {
                        'id': 'cloth.women',
                        'children': {
                            'Dresses': {'id': 'cloth.women.dress'},
                            'Tops': {'id': 'cloth.women.top'},
                        }
                    },
                }
            },
        }
        
        if filepath:
            with open(filepath, 'r') as f:
                import json
                return json.load(f)
        
        return default_taxonomy
    
    def _build_alias_map(self):
        """Build map of common aliases"""
        return {
            'laptop': 'Laptops',
            'notebook': 'Laptops',
            'cell phone': 'Smartphones',
            'mobile phone': 'Smartphones',
            'cellphone': 'Smartphones',
            'smart phone': 'Smartphones',
        }
    
    def map_category(self, scraped_name: str) -> Optional[dict]:
        """Map scraped category name to canonical category"""
        normalized = scraped_name.lower().strip()
        
        # Check aliases first
        if normalized in self.aliases:
            normalized = self.aliases[normalized].lower()
        
        # Search taxonomy
        return self._find_in_taxonomy(self.taxonomy, normalized)
    
    def _find_in_taxonomy(self, taxonomy, search_name):
        """Recursively search taxonomy"""
        for name, data in taxonomy.items():
            if name.lower() == search_name:
                return {
                    'name': name,
                    'id': data.get('id'),
                    'path': self._build_path(taxonomy, name),
                }
            
            if 'children' in data:
                result = self._find_in_taxonomy(data['children'], search_name)
                if result:
                    return result
        
        return None
    
    def _build_path(self, taxonomy, target_name, path=None):
        """Build full path to category"""
        if path is None:
            path = []
        
        for name, data in taxonomy.items():
            current_path = path + [name]
            if name == target_name:
                return current_path
            
            if 'children' in data:
                result = self._build_path(data['children'], target_name, current_path)
                if result:
                    return result
        
        return None
```

---

## Image URL Processing

### Image URL Cleaner

```python
from urllib.parse import urlparse, parse_qs, urlencode, urlunparse


class ImageURLProcessor:
    """Process and normalize image URLs"""
    
    # Common URL parameters to remove (tracking, resizing)
    DIRTY_PARAMS = [
        'utm_source', 'utm_medium', 'utm_campaign',
        'ref', 'referrer', 'source',
        'w', 'width', 'h', 'height',  # Often want to keep these
        'fit', 'crop', 'quality',
    ]
    
    # Known image CDN patterns
    CDN_PATTERNS = {
        'cloudinary': r'res.cloudinary.com',
        'imgix': r'.*\.imgix\.net',
        'cloudfront': r'.*\.cloudfront\.net',
        'akamai': r'.*\.akamaihd\.net',
    }
    
    @classmethod
    def normalize(cls, url: str) -> str:
        """Clean and normalize image URL"""
        if not url:
            return url
        
        # Ensure HTTPS
        if url.startswith('http://'):
            url = 'https://' + url[7:]
        
        # Parse URL
        parsed = urlparse(url)
        
        # Remove tracking parameters (optional - keep size params)
        # query_params = parse_qs(parsed.query)
        # clean_params = {k: v for k, v in query_params.items() 
        #                 if k not in cls.DIRTY_PARAMS}
        # clean_query = urlencode(clean_params, doseq=True)
        
        # Rebuild URL
        # normalized = urlunparse((
        #     parsed.scheme,
        #     parsed.netloc,
        #     parsed.path,
        #     parsed.params,
        #     clean_query,
        #     parsed.fragment
        # ))
        
        return url
    
    @classmethod
    def get_high_res(cls, url: str) -> str:
        """Try to get high-resolution version of image"""
        # Common patterns for high-res images
        replacements = [
            ('_thumb.', '_large.'),
            ('_small.', '_full.'),
            ('/thumbnail/', '/full/'),
            ('?w=200&', '?w=1200&'),
            ('?w=300', '?w=1200'),
        ]
        
        for old, new in replacements:
            if old in url:
                return url.replace(old, new)
        
        return url
    
    @classmethod
    def validate_url(cls, url: str) -> bool:
        """Check if URL appears to be valid image"""
        if not url:
            return False
        
        # Check for image extensions
        image_extensions = ('.jpg', '.jpeg', '.png', '.gif', '.webp', '.svg')
        parsed = urlparse(url.lower())
        
        has_image_ext = any(parsed.path.endswith(ext) for ext in image_extensions)
        is_data_uri = url.startswith('data:image/')
        
        return has_image_ext or is_data_uri


# Usage
urls = [
    "http://example.com/image.jpg?w=200&utm_source=scraper",
    "//cdn.example.com/product_thumb.png",
]

for url in urls:
    print(f"Original: {url}")
    print(f"Normalized: {ImageURLProcessor.normalize(url)}")
    print(f"High-res: {ImageURLProcessor.get_high_res(url)}")
    print(f"Valid: {ImageURLProcessor.validate_url(url)}")
    print()
```

---

## Deduplication Strategies

### Content-Based Deduplication

```python
import hashlib
from dataclasses import dataclass
from typing import List, Set


@dataclass
class DedupConfig:
    """Configuration for deduplication"""
    fields: List[str]              # Fields to consider
    fuzzy_threshold: float = 0.9   # For fuzzy matching
    use_content_hash: bool = True  # Hash full content


class Deduplicator:
    """Remove duplicate items from datasets"""
    
    def __init__(self, config: DedupConfig):
        self.config = config
        self.seen_hashes: Set[str] = set()
        self.seen_signatures: Set[str] = set()
    
    def deduplicate(self, items: List[dict]) -> List[dict]:
        """Remove duplicates from item list"""
        unique_items = []
        
        for item in items:
            if not self._is_duplicate(item):
                unique_items.append(item)
                self._mark_seen(item)
        
        return unique_items
    
    def _is_duplicate(self, item: dict) -> bool:
        """Check if item is a duplicate"""
        # Check content hash
        if self.config.use_content_hash:
            content_hash = self._compute_hash(item)
            if content_hash in self.seen_hashes:
                return True
        
        # Check signature (selected fields)
        signature = self._compute_signature(item)
        if signature in self.seen_signatures:
            return True
        
        return False
    
    def _compute_hash(self, item: dict) -> str:
        """Compute hash of full item"""
        import json
        content = json.dumps(item, sort_keys=True)
        return hashlib.md5(content.encode()).hexdigest()
    
    def _compute_signature(self, item: dict) -> str:
        """Compute signature from key fields"""
        values = []
        for field in self.config.fields:
            value = item.get(field, '')
            values.append(str(value).lower().strip())
        
        signature = '|'.join(values)
        return hashlib.md5(signature.encode()).hexdigest()
    
    def _mark_seen(self, item: dict):
        """Mark item as seen"""
        if self.config.use_content_hash:
            self.seen_hashes.add(self._compute_hash(item))
        
        self.seen_signatures.add(self._compute_signature(item))


# Fuzzy deduplication using similarity
class FuzzyDeduplicator:
    """Deduplicate using string similarity"""
    
    def __init__(self, threshold=0.9):
        self.threshold = threshold
        self.seen_items = []
    
    def deduplicate(self, items: List[dict], key_field='name') -> List[dict]:
        """Remove fuzzy duplicates"""
        from difflib import SequenceMatcher
        
        unique = []
        
        for item in items:
            text = str(item.get(key_field, ''))
            is_duplicate = False
            
            for seen in self.seen_items:
                similarity = SequenceMatcher(None, text.lower(), 
                                            seen.lower()).ratio()
                if similarity >= self.threshold:
                    is_duplicate = True
                    break
            
            if not is_duplicate:
                unique.append(item)
                self.seen_items.append(text)
        
        return unique
```

---

## Quality Scoring

### Data Quality Assessment

```python
from dataclasses import dataclass
from typing import Dict, List


@dataclass
class QualityReport:
    """Report on data quality"""
    total_items: int
    valid_items: int
    invalid_items: int
    completeness: float
    field_coverage: Dict[str, float]
    common_errors: List[str]
    score: float


class QualityScorer:
    """Score and report on data quality"""
    
    def __init__(self, required_fields=None, field_weights=None):
        self.required_fields = required_fields or []
        self.field_weights = field_weights or {}
    
    def score_items(self, items: List[dict]) -> QualityReport:
        """Score a batch of items"""
        total = len(items)
        valid = 0
        field_counts = {field: 0 for field in self.required_fields}
        errors = []
        
        for item in items:
            is_valid = True
            
            for field in self.required_fields:
                value = item.get(field)
                if value:
                    field_counts[field] += 1
                else:
                    is_valid = False
                    errors.append(f"Missing {field}")
            
            if is_valid:
                valid += 1
        
        # Calculate metrics
        completeness = valid / total if total > 0 else 0
        
        field_coverage = {
            field: count / total if total > 0 else 0
            for field, count in field_counts.items()
        }
        
        # Calculate overall score
        score = completeness * 100
        if field_coverage:
            avg_coverage = sum(field_coverage.values()) / len(field_coverage)
            score = (completeness * 0.6 + avg_coverage * 0.4) * 100
        
        # Get most common errors
        from collections import Counter
        error_counts = Counter(errors)
        common_errors = [f"{err} ({count}x)" for err, count in error_counts.most_common(5)]
        
        return QualityReport(
            total_items=total,
            valid_items=valid,
            invalid_items=total - valid,
            completeness=completeness,
            field_coverage=field_coverage,
            common_errors=common_errors,
            score=score,
        )
    
    def generate_report(self, report: QualityReport) -> str:
        """Generate human-readable report"""
        lines = [
            "=" * 50,
            "DATA QUALITY REPORT",
            "=" * 50,
            f"",
            f"Total Items:     {report.total_items}",
            f"Valid Items:     {report.valid_items} ({report.completeness:.1%})",
            f"Invalid Items:   {report.invalid_items}",
            f"",
            f"Overall Score:   {report.score:.1f}/100",
            f"",
            "Field Coverage:",
        ]
        
        for field, coverage in report.field_coverage.items():
            bar = "█" * int(coverage * 20) + "░" * (20 - int(coverage * 20))
            lines.append(f"  {field:20} {bar} {coverage:.1%}")
        
        if report.common_errors:
            lines.extend([
                f"",
                "Common Issues:",
            ])
            for error in report.common_errors:
                lines.append(f"  • {error}")
        
        lines.append("=" * 50)
        
        return "\\n".join(lines)


# Example usage
def example_quality_check():
    items = [
        {'name': 'Product A', 'price': 99.99, 'brand': 'Brand X'},
        {'name': 'Product B', 'price': None, 'brand': 'Brand Y'},
        {'name': 'Product C', 'price': 149.99, 'brand': None},
        {'name': 'Product D', 'price': 49.99, 'brand': 'Brand Z'},
    ]
    
    scorer = QualityScorer(required_fields=['name', 'price', 'brand'])
    report = scorer.score_items(items)
    print(scorer.generate_report(report))


# example_quality_check()
```

This chapter provides comprehensive tools for cleaning and normalizing scraped data. These techniques transform raw, messy web data into clean, structured datasets ready for analysis, storage, or downstream processing. The modular design allows you to use only the components you need for your specific data cleaning requirements.
