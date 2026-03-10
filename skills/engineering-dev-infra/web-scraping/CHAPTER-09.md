# CHAPTER 09: Data Cleaning and Quality Assurance

## Introduction

Scraping data is only half the battle. Raw scraped data is messy, inconsistent, and often contains errors, duplicates, and irrelevant information. Data cleaning and quality assurance transforms this raw data into reliable, structured information suitable for analysis and business use.

This chapter covers the complete data cleaning pipeline: regex parsing, NLP entity extraction, deduplication strategies, normalization techniques, schema validation, enrichment, and quality monitoring. We'll build production-ready systems that ensure scraped data meets quality standards.

## The Data Cleaning Pipeline

A robust data cleaning pipeline consists of several stages:

1. **Raw Data Validation**: Check if scraping succeeded
2. **Parsing**: Extract structured data from text
3. **Normalization**: Standardize formats
4. **Deduplication**: Remove duplicates
5. **Enrichment**: Add missing data
6. **Validation**: Verify against schema
7. **Quality Scoring**: Assess data quality
8. **Monitoring**: Track quality over time

## Regex Parsing Patterns

Regular expressions are essential for extracting structured data from text.

### Common Patterns Library

```python
import re
from typing import Optional, List, Dict
from dataclasses import dataclass

@dataclass
class ExtractedData:
    """Container for extracted data"""
    emails: List[str]
    phones: List[str]
    urls: List[str]
    prices: List[Dict[str, any]]
    dates: List[str]
    zipcodes: List[str]
    
class RegexParser:
    """Production-ready regex patterns for common data types"""
    
    # Email pattern (RFC 5322 compliant)
    EMAIL_PATTERN = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    
    # Phone patterns (US and international)
    PHONE_US_PATTERN = r'(?:\+?1[-.\s]?)?\(?([0-9]{3})\)?[-.\s]?([0-9]{3})[-.\s]?([0-9]{4})'
    PHONE_INTL_PATTERN = r'\+?[1-9]\d{1,14}'
    
    # URL pattern
    URL_PATTERN = r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+'
    
    # Price patterns
    PRICE_USD_PATTERN = r'\$\s*(\d{1,3}(?:,\d{3})*(?:\.\d{2})?)'
    PRICE_GENERIC_PATTERN = r'([£€¥₹])\s*(\d{1,3}(?:,\d{3})*(?:\.\d{2})?)'
    
    # Date patterns
    DATE_MDY_PATTERN = r'\b(\d{1,2})[/-](\d{1,2})[/-](\d{2,4})\b'
    DATE_FULL_PATTERN = r'\b(?:Jan(?:uary)?|Feb(?:ruary)?|Mar(?:ch)?|Apr(?:il)?|May|Jun(?:e)?|Jul(?:y)?|Aug(?:ust)?|Sep(?:tember)?|Oct(?:ober)?|Nov(?:ember)?|Dec(?:ember)?)\s+\d{1,2},?\s+\d{4}\b'
    
    # ZIP code
    ZIP_US_PATTERN = r'\b\d{5}(?:-\d{4})?\b'
    
    # Social Security Number
    SSN_PATTERN = r'\b\d{3}-\d{2}-\d{4}\b'
    
    # Credit Card
    CC_PATTERN = r'\b(?:\d{4}[-\s]?){3}\d{4}\b'
    
    @classmethod
    def extract_emails(cls, text: str) -> List[str]:
        """Extract email addresses"""
        return list(set(re.findall(cls.EMAIL_PATTERN, text, re.IGNORECASE)))
    
    @classmethod
    def extract_phones(cls, text: str, country: str = 'US') -> List[str]:
        """Extract phone numbers"""
        if country == 'US':
            matches = re.findall(cls.PHONE_US_PATTERN, text)
            # Format as (XXX) XXX-XXXX
            return [f"({m[0]}) {m[1]}-{m[2]}" for m in matches]
        else:
            return list(set(re.findall(cls.PHONE_INTL_PATTERN, text)))
    
    @classmethod
    def extract_urls(cls, text: str) -> List[str]:
        """Extract URLs"""
        return list(set(re.findall(cls.URL_PATTERN, text)))
    
    @classmethod
    def extract_prices(cls, text: str) -> List[Dict[str, any]]:
        """Extract prices with currency"""
        prices = []
        
        # USD prices
        for match in re.finditer(cls.PRICE_USD_PATTERN, text):
            amount = match.group(1).replace(',', '')
            prices.append({
                'currency': 'USD',
                'amount': float(amount),
                'formatted': f"${amount}"
            })
        
        # Other currencies
        for match in re.finditer(cls.PRICE_GENERIC_PATTERN, text):
            symbol = match.group(1)
            amount = match.group(2).replace(',', '')
            
            currency_map = {'£': 'GBP', '€': 'EUR', '¥': 'JPY', '₹': 'INR'}
            
            prices.append({
                'currency': currency_map.get(symbol, 'UNKNOWN'),
                'amount': float(amount),
                'formatted': f"{symbol}{amount}"
            })
        
        return prices
    
    @classmethod
    def extract_dates(cls, text: str) -> List[str]:
        """Extract dates"""
        dates = []
        
        # MM/DD/YYYY format
        dates.extend(re.findall(cls.DATE_MDY_PATTERN, text))
        
        # Full text format
        dates.extend(re.findall(cls.DATE_FULL_PATTERN, text, re.IGNORECASE))
        
        return dates
    
    @classmethod
    def extract_zipcodes(cls, text: str) -> List[str]:
        """Extract US ZIP codes"""
        return list(set(re.findall(cls.ZIP_US_PATTERN, text)))
    
    @classmethod
    def extract_all(cls, text: str) -> ExtractedData:
        """Extract all common data types"""
        return ExtractedData(
            emails=cls.extract_emails(text),
            phones=cls.extract_phones(text),
            urls=cls.extract_urls(text),
            prices=cls.extract_prices(text),
            dates=cls.extract_dates(text),
            zipcodes=cls.extract_zipcodes(text)
        )

# Usage
text = """
Contact us at support@example.com or call (555) 123-4567.
Visit our website at https://example.com
Prices start at $1,299.99
Event date: January 15, 2024
Office: 12345 or 12345-6789
"""

parser = RegexParser()
data = parser.extract_all(text)

print(f"Emails: {data.emails}")
print(f"Phones: {data.phones}")
print(f"URLs: {data.urls}")
print(f"Prices: {data.prices}")
print(f"Dates: {data.dates}")
print(f"ZIPs: {data.zipcodes}")
```

### Advanced Regex Patterns for Web Scraping

```python
class AdvancedPatterns:
    """Advanced patterns for specific scraping scenarios"""
    
    # Product codes
    SKU_PATTERN = r'\b[A-Z0-9]{2,}-[A-Z0-9]{2,}\b'
    UPC_PATTERN = r'\b\d{12}\b'
    
    # Social media handles
    TWITTER_HANDLE = r'@[A-Za-z0-9_]{1,15}\b'
    INSTAGRAM_HANDLE = r'@[A-Za-z0-9_.]{1,30}\b'
    
    # HTML/XML tags
    HTML_TAG_PATTERN = r'<[^>]+>'
    
    # IPv4 address
    IPV4_PATTERN = r'\b(?:\d{1,3}\.){3}\d{1,3}\b'
    
    # File extensions
    IMAGE_FILE_PATTERN = r'\b\w+\.(jpg|jpeg|png|gif|webp|svg)\b'
    
    @staticmethod
    def clean_html(text: str) -> str:
        """Remove HTML tags"""
        return re.sub(AdvancedPatterns.HTML_TAG_PATTERN, '', text)
    
    @staticmethod
    def extract_hashtags(text: str) -> List[str]:
        """Extract hashtags"""
        return re.findall(r'#(\w+)', text)
    
    @staticmethod
    def extract_mentions(text: str) -> List[str]:
        """Extract @mentions"""
        return re.findall(r'@(\w+)', text)
    
    @staticmethod
    def normalize_whitespace(text: str) -> str:
        """Normalize whitespace"""
        # Replace multiple spaces with single space
        text = re.sub(r'\s+', ' ', text)
        # Remove leading/trailing whitespace
        return text.strip()
    
    @staticmethod
    def extract_numbers(text: str) -> List[float]:
        """Extract all numbers"""
        # Match integers and decimals
        matches = re.findall(r'-?\d+\.?\d*', text)
        return [float(m) for m in matches]
```

## NLP Entity Extraction

Natural Language Processing helps extract structured information from unstructured text.

### Using spaCy for Entity Extraction

```python
import spacy
from typing import List, Dict, Optional
from collections import defaultdict

class NLPExtractor:
    """Extract entities using spaCy"""
    
    def __init__(self, model: str = 'en_core_web_sm'):
        """Initialize spaCy model"""
        try:
            self.nlp = spacy.load(model)
        except OSError:
            print(f"Downloading {model}...")
            import subprocess
            subprocess.run(['python', '-m', 'spacy', 'download', model])
            self.nlp = spacy.load(model)
    
    def extract_entities(self, text: str) -> Dict[str, List[str]]:
        """Extract named entities"""
        doc = self.nlp(text)
        
        entities = defaultdict(list)
        
        for ent in doc.ents:
            entities[ent.label_].append(ent.text)
        
        # Return unique entities per type
        return {
            entity_type: list(set(entity_list))
            for entity_type, entity_list in entities.items()
        }
    
    def extract_persons(self, text: str) -> List[str]:
        """Extract person names"""
        entities = self.extract_entities(text)
        return entities.get('PERSON', [])
    
    def extract_organizations(self, text: str) -> List[str]:
        """Extract organization names"""
        entities = self.extract_entities(text)
        return entities.get('ORG', [])
    
    def extract_locations(self, text: str) -> List[str]:
        """Extract locations"""
        entities = self.extract_entities(text)
        return entities.get('GPE', []) + entities.get('LOC', [])
    
    def extract_dates(self, text: str) -> List[str]:
        """Extract dates using NLP"""
        entities = self.extract_entities(text)
        return entities.get('DATE', [])
    
    def extract_money(self, text: str) -> List[str]:
        """Extract money values"""
        entities = self.extract_entities(text)
        return entities.get('MONEY', [])

# Usage
extractor = NLPExtractor()

text = """
Apple Inc. announced that Tim Cook will speak at a conference in San Francisco on March 15, 2024.
The company's revenue reached $394.3 billion last year.
"""

entities = extractor.extract_entities(text)
print(f"All entities: {entities}")

persons = extractor.extract_persons(text)
print(f"Persons: {persons}")

orgs = extractor.extract_organizations(text)
print(f"Organizations: {orgs}")

locations = extractor.extract_locations(text)
print(f"Locations: {locations}")
```

### Custom Entity Extraction Patterns

```python
from spacy.matcher import Matcher

class CustomEntityExtractor:
    """Extract custom entities using patterns"""
    
    def __init__(self):
        self.nlp = spacy.load('en_core_web_sm')
        self.matcher = Matcher(self.nlp.vocab)
        self._setup_patterns()
    
    def _setup_patterns(self):
        """Setup custom patterns"""
        
        # Product code pattern: XXX-NNNN
        product_code_pattern = [
            {'IS_ALPHA': True, 'LENGTH': 3},
            {'TEXT': '-'},
            {'IS_DIGIT': True, 'LENGTH': 4}
        ]
        self.matcher.add('PRODUCT_CODE', [product_code_pattern])
        
        # Email with capture
        email_pattern = [
            {'LIKE_EMAIL': True}
        ]
        self.matcher.add('EMAIL', [email_pattern])
        
        # Price pattern: $ followed by number
        price_pattern = [
            {'TEXT': '$'},
            {'LIKE_NUM': True}
        ]
        self.matcher.add('PRICE', [price_pattern])
    
    def extract(self, text: str) -> Dict[str, List[str]]:
        """Extract custom entities"""
        doc = self.nlp(text)
        matches = self.matcher(doc)
        
        results = defaultdict(list)
        
        for match_id, start, end in matches:
            span = doc[start:end]
            label = self.nlp.vocab.strings[match_id]
            results[label].append(span.text)
        
        return dict(results)

# Usage
extractor = CustomEntityExtractor()
text = "Product ABC-1234 costs $599.99. Email: support@example.com"
entities = extractor.extract(text)
print(entities)
```

## Deduplication Algorithms

Removing duplicates is critical for data quality.

### Exact Deduplication

```python
from typing import List, Dict, Set
import hashlib
import json

class ExactDeduplicator:
    """Remove exact duplicates"""
    
    @staticmethod
    def deduplicate_by_field(items: List[Dict], field: str) -> List[Dict]:
        """Deduplicate by specific field"""
        seen = set()
        unique_items = []
        
        for item in items:
            value = item.get(field)
            if value and value not in seen:
                seen.add(value)
                unique_items.append(item)
        
        return unique_items
    
    @staticmethod
    def deduplicate_by_hash(items: List[Dict]) -> List[Dict]:
        """Deduplicate by content hash"""
        seen = set()
        unique_items = []
        
        for item in items:
            # Create hash of entire item
            item_json = json.dumps(item, sort_keys=True)
            item_hash = hashlib.md5(item_json.encode()).hexdigest()
            
            if item_hash not in seen:
                seen.add(item_hash)
                unique_items.append(item)
        
        return unique_items
    
    @staticmethod
    def deduplicate_by_fields(items: List[Dict], fields: List[str]) -> List[Dict]:
        """Deduplicate by multiple fields"""
        seen = set()
        unique_items = []
        
        for item in items:
            # Create tuple of field values
            key = tuple(item.get(field) for field in fields)
            
            if key not in seen:
                seen.add(key)
                unique_items.append(item)
        
        return unique_items

# Usage
products = [
    {'id': '1', 'name': 'iPhone 13', 'price': 799},
    {'id': '2', 'name': 'iPhone 13', 'price': 799},  # Duplicate
    {'id': '3', 'name': 'iPhone 14', 'price': 899}
]

dedup = ExactDeduplicator()

# By ID
unique = dedup.deduplicate_by_field(products, 'id')
print(f"Unique by ID: {len(unique)}")

# By name and price
unique = dedup.deduplicate_by_fields(products, ['name', 'price'])
print(f"Unique by name+price: {len(unique)}")
```

### Fuzzy Deduplication

```python
from fuzzywuzzy import fuzz
from typing import List, Dict, Tuple
import Levenshtein

class FuzzyDeduplicator:
    """Remove fuzzy duplicates"""
    
    def __init__(self, threshold: int = 85):
        self.threshold = threshold
    
    def deduplicate_by_field(self, items: List[Dict], field: str) -> List[Dict]:
        """Fuzzy deduplicate by field"""
        if not items:
            return []
        
        unique_items = [items[0]]
        
        for item in items[1:]:
            current_value = str(item.get(field, ''))
            
            is_duplicate = False
            for unique_item in unique_items:
                unique_value = str(unique_item.get(field, ''))
                
                # Calculate similarity
                similarity = fuzz.ratio(current_value, unique_value)
                
                if similarity >= self.threshold:
                    is_duplicate = True
                    break
            
            if not is_duplicate:
                unique_items.append(item)
        
        return unique_items
    
    def find_duplicates(self, items: List[Dict], field: str) -> List[Tuple[int, int, int]]:
        """Find pairs of fuzzy duplicates with similarity scores"""
        duplicates = []
        
        for i, item1 in enumerate(items):
            for j, item2 in enumerate(items[i+1:], start=i+1):
                value1 = str(item1.get(field, ''))
                value2 = str(item2.get(field, ''))
                
                similarity = fuzz.ratio(value1, value2)
                
                if similarity >= self.threshold:
                    duplicates.append((i, j, similarity))
        
        return duplicates

# Usage
products = [
    {'name': 'iPhone 13 Pro', 'price': 999},
    {'name': 'iPhone 13Pro', 'price': 999},  # Fuzzy duplicate (missing space)
    {'name': 'iPhone 14', 'price': 899}
]

dedup = FuzzyDeduplicator(threshold=90)
unique = dedup.deduplicate_by_field(products, 'name')
print(f"Unique products: {len(unique)}")

duplicates = dedup.find_duplicates(products, 'name')
print(f"Duplicate pairs: {duplicates}")
```

### LSH (Locality-Sensitive Hashing) for Large Datasets

```python
from datasketch import MinHash, MinHashLSH
from typing import List, Dict, Set

class LSHDeduplicator:
    """Efficient deduplication for large datasets using LSH"""
    
    def __init__(self, threshold: float = 0.85, num_perm: int = 128):
        self.threshold = threshold
        self.num_perm = num_perm
    
    def _text_to_minhash(self, text: str) -> MinHash:
        """Convert text to MinHash"""
        m = MinHash(num_perm=self.num_perm)
        
        # Shingle the text (create n-grams)
        words = text.lower().split()
        for i in range(len(words) - 1):
            shingle = ' '.join(words[i:i+2])
            m.update(shingle.encode('utf-8'))
        
        return m
    
    def deduplicate(self, items: List[Dict], text_field: str, 
                   id_field: str = 'id') -> List[Dict]:
        """Deduplicate using LSH"""
        # Create LSH index
        lsh = MinHashLSH(threshold=self.threshold, num_perm=self.num_perm)
        
        # Store minhashes
        minhashes = {}
        
        for item in items:
            item_id = item.get(id_field) or str(hash(str(item)))
            text = str(item.get(text_field, ''))
            
            minhash = self._text_to_minhash(text)
            minhashes[item_id] = minhash
            
            # Check for duplicates
            similar = lsh.query(minhash)
            
            if not similar:
                # No duplicates found, add to index
                lsh.insert(item_id, minhash)
        
        # Return only items in LSH index
        indexed_ids = set(lsh.keys)
        unique_items = [
            item for item in items 
            if (item.get(id_field) or str(hash(str(item)))) in indexed_ids
        ]
        
        return unique_items
    
    def find_duplicates_groups(self, items: List[Dict], text_field: str,
                              id_field: str = 'id') -> Dict[str, List[str]]:
        """Find groups of duplicates"""
        lsh = MinHashLSH(threshold=self.threshold, num_perm=self.num_perm)
        
        # Build index and track groups
        item_map = {}
        duplicate_groups = {}
        
        for item in items:
            item_id = item.get(id_field) or str(hash(str(item)))
            text = str(item.get(text_field, ''))
            
            minhash = self._text_to_minhash(text)
            item_map[item_id] = item
            
            # Check for similar items
            similar = lsh.query(minhash)
            
            if similar:
                # Add to existing group
                group_id = similar[0]
                if group_id not in duplicate_groups:
                    duplicate_groups[group_id] = [group_id]
                duplicate_groups[group_id].append(item_id)
            else:
                # Create new group
                duplicate_groups[item_id] = [item_id]
            
            lsh.insert(item_id, minhash)
        
        return duplicate_groups

# Usage
documents = [
    {'id': '1', 'text': 'Python is a great programming language'},
    {'id': '2', 'text': 'Python is a great programming language.'},  # Near duplicate
    {'id': '3', 'text': 'JavaScript is also a programming language'},
    {'id': '4', 'text': 'Python is an excellent programming language'}  # Similar
]

dedup = LSHDeduplicator(threshold=0.8)
unique = dedup.deduplicate(documents, text_field='text')
print(f"Unique documents: {len(unique)}")

groups = dedup.find_duplicates_groups(documents, text_field='text')
print(f"Duplicate groups: {groups}")
```

## Data Normalization

Standardizing data formats ensures consistency.

### Text Normalization

```python
import unicodedata
import re

class TextNormalizer:
    """Normalize text data"""
    
    @staticmethod
    def normalize_unicode(text: str) -> str:
        """Normalize unicode characters"""
        # Convert to NFKD form (compatibility decomposition)
        return unicodedata.normalize('NFKD', text)
    
    @staticmethod
    def remove_accents(text: str) -> str:
        """Remove accents from characters"""
        nfkd = unicodedata.normalize('NFKD', text)
        return ''.join([c for c in nfkd if not unicodedata.combining(c)])
    
    @staticmethod
    def normalize_whitespace(text: str) -> str:
        """Normalize whitespace"""
        # Replace multiple spaces/tabs/newlines with single space
        text = re.sub(r'\s+', ' ', text)
        return text.strip()
    
    @staticmethod
    def normalize_case(text: str, mode: str = 'lower') -> str:
        """Normalize case"""
        if mode == 'lower':
            return text.lower()
        elif mode == 'upper':
            return text.upper()
        elif mode == 'title':
            return text.title()
        return text
    
    @staticmethod
    def remove_special_chars(text: str, keep: str = '') -> str:
        """Remove special characters"""
        pattern = f'[^a-zA-Z0-9\\s{re.escape(keep)}]'
        return re.sub(pattern, '', text)
    
    @staticmethod
    def normalize_all(text: str) -> str:
        """Apply all normalizations"""
        text = TextNormalizer.normalize_unicode(text)
        text = TextNormalizer.remove_accents(text)
        text = TextNormalizer.normalize_whitespace(text)
        text = TextNormalizer.normalize_case(text)
        text = TextNormalizer.remove_special_chars(text)
        return text

# Usage
text = "  Héllo   Wørld!  This  is  a   TEST  "
normalized = TextNormalizer.normalize_all(text)
print(f"Normalized: '{normalized}'")
```

### Date Normalization

```python
from datetime import datetime
from dateutil import parser
from typing import Optional

class DateNormalizer:
    """Normalize date formats"""
    
    @staticmethod
    def parse_date(date_str: str) -> Optional[datetime]:
        """Parse date string to datetime"""
        try:
            return parser.parse(date_str)
        except:
            return None
    
    @staticmethod
    def normalize_date(date_str: str, format: str = '%Y-%m-%d') -> Optional[str]:
        """Normalize date to standard format"""
        dt = DateNormalizer.parse_date(date_str)
        if dt:
            return dt.strftime(format)
        return None
    
    @staticmethod
    def normalize_datetime(date_str: str) -> Optional[str]:
        """Normalize to ISO 8601 format"""
        dt = DateNormalizer.parse_date(date_str)
        if dt:
            return dt.isoformat()
        return None

# Usage
dates = [
    "Jan 15, 2024",
    "2024-01-15",
    "15/01/2024",
    "January 15, 2024"
]

for date_str in dates:
    normalized = DateNormalizer.normalize_date(date_str)
    print(f"{date_str} -> {normalized}")
```

### Price Normalization

```python
class PriceNormalizer:
    """Normalize price data"""
    
    @staticmethod
    def parse_price(price_str: str) -> Optional[float]:
        """Parse price string to float"""
        # Remove currency symbols and whitespace
        cleaned = re.sub(r'[$£€¥₹,\s]', '', price_str)
        
        try:
            return float(cleaned)
        except:
            return None
    
    @staticmethod
    def normalize_price(price_str: str, decimals: int = 2) -> Optional[float]:
        """Normalize price to float with fixed decimals"""
        price = PriceNormalizer.parse_price(price_str)
        if price is not None:
            return round(price, decimals)
        return None
    
    @staticmethod
    def format_price(amount: float, currency: str = 'USD') -> str:
        """Format price with currency"""
        symbols = {
            'USD': '$',
            'EUR': '€',
            'GBP': '£',
            'JPY': '¥'
        }
        
        symbol = symbols.get(currency, currency)
        return f"{symbol}{amount:,.2f}"

# Usage
prices = ["$1,299.99", "€ 1299.99", "1299", "$1299"]

for price_str in prices:
    normalized = PriceNormalizer.normalize_price(price_str)
    formatted = PriceNormalizer.format_price(normalized, 'USD')
    print(f"{price_str} -> {normalized} -> {formatted}")
```

## Schema Validation with JSON Schema

Validate scraped data against predefined schemas.

```python
import jsonschema
from jsonschema import validate, ValidationError
from typing import Dict, List, Optional

class SchemaValidator:
    """Validate data against JSON schemas"""
    
    # Product schema example
    PRODUCT_SCHEMA = {
        "type": "object",
        "required": ["id", "name", "price"],
        "properties": {
            "id": {"type": "string"},
            "name": {"type": "string", "minLength": 1},
            "price": {"type": "number", "minimum": 0},
            "description": {"type": "string"},
            "category": {"type": "string"},
            "in_stock": {"type": "boolean"},
            "rating": {"type": "number", "minimum": 0, "maximum": 5},
            "reviews": {"type": "integer", "minimum": 0},
            "images": {
                "type": "array",
                "items": {"type": "string", "format": "uri"}
            },
            "attributes": {"type": "object"}
        }
    }
    
    def __init__(self, schema: Dict):
        self.schema = schema
    
    def validate_item(self, item: Dict) -> tuple[bool, Optional[str]]:
        """Validate single item"""
        try:
            validate(instance=item, schema=self.schema)
            return True, None
        except ValidationError as e:
            return False, str(e)
    
    def validate_batch(self, items: List[Dict]) -> Dict[str, any]:
        """Validate batch of items"""
        results = {
            'valid': [],
            'invalid': [],
            'total': len(items),
            'valid_count': 0,
            'invalid_count': 0
        }
        
        for item in items:
            is_valid, error = self.validate_item(item)
            
            if is_valid:
                results['valid'].append(item)
                results['valid_count'] += 1
            else:
                results['invalid'].append({
                    'item': item,
                    'error': error
                })
                results['invalid_count'] += 1
        
        return results
    
    def get_validation_report(self, items: List[Dict]) -> str:
        """Generate validation report"""
        results = self.validate_batch(items)
        
        report = f"""
Validation Report
=================
Total items: {results['total']}
Valid: {results['valid_count']} ({results['valid_count']/results['total']*100:.1f}%)
Invalid: {results['invalid_count']} ({results['invalid_count']/results['total']*100:.1f}%)

Invalid Items:
"""
        
        for i, invalid in enumerate(results['invalid'][:10], 1):
            report += f"\n{i}. Error: {invalid['error']}\n"
            report += f"   Item: {invalid['item']}\n"
        
        if results['invalid_count'] > 10:
            report += f"\n... and {results['invalid_count'] - 10} more"
        
        return report

# Usage
products = [
    {'id': '1', 'name': 'iPhone 13', 'price': 799},
    {'id': '2', 'name': 'MacBook Pro', 'price': 1999, 'in_stock': True},
    {'id': '3', 'name': '', 'price': -100},  # Invalid: empty name, negative price
    {'name': 'iPad', 'price': 499}  # Invalid: missing id
]

validator = SchemaValidator(SchemaValidator.PRODUCT_SCHEMA)
results = validator.validate_batch(products)

print(f"Valid: {results['valid_count']}")
print(f"Invalid: {results['invalid_count']}")

print("\n" + validator.get_validation_report(products))
```

## Data Enrichment

Add missing data from external sources.

```python
import requests
from typing import Dict, Optional, List

class DataEnricher:
    """Enrich scraped data with external sources"""
    
    def __init__(self, api_keys: Dict[str, str]):
        self.api_keys = api_keys
    
    def enrich_location(self, address: str) -> Optional[Dict]:
        """Enrich with geocoding data"""
        # Example using Nominatim (OpenStreetMap)
        url = 'https://nominatim.openstreetmap.org/search'
        
        params = {
            'q': address,
            'format': 'json',
            'limit': 1
        }
        
        headers = {
            'User-Agent': 'DataEnricher/1.0'
        }
        
        try:
            response = requests.get(url, params=params, headers=headers)
            data = response.json()
            
            if data:
                result = data[0]
                return {
                    'latitude': float(result['lat']),
                    'longitude': float(result['lon']),
                    'display_name': result['display_name']
                }
        except:
            pass
        
        return None
    
    def enrich_company(self, company_name: str) -> Optional[Dict]:
        """Enrich with company data (mock example)"""
        # In production, use APIs like Clearbit, FullContact, etc.
        
        # Mock enrichment
        return {
            'industry': 'Technology',
            'employee_count': '1000-5000',
            'founded_year': 2010
        }
    
    def enrich_product(self, product_name: str) -> Optional[Dict]:
        """Enrich product data (mock example)"""
        # In production, use product databases, APIs
        
        return {
            'category': 'Electronics',
            'brand': 'Apple',
            'specifications': {}
        }
    
    def enrich_batch(self, items: List[Dict], 
                    enrich_fields: Dict[str, str]) -> List[Dict]:
        """Enrich batch of items
        
        Args:
            items: List of items to enrich
            enrich_fields: Dict mapping field name to enrichment type
                          e.g. {'address': 'location', 'company': 'company'}
        """
        enriched_items = []
        
        for item in items:
            enriched_item = item.copy()
            
            for field, enrich_type in enrich_fields.items():
                value = item.get(field)
                
                if value:
                    if enrich_type == 'location':
                        enriched_data = self.enrich_location(value)
                    elif enrich_type == 'company':
                        enriched_data = self.enrich_company(value)
                    elif enrich_type == 'product':
                        enriched_data = self.enrich_product(value)
                    else:
                        enriched_data = None
                    
                    if enriched_data:
                        enriched_item[f'{field}_enriched'] = enriched_data
            
            enriched_items.append(enriched_item)
        
        return enriched_items

# Usage
items = [
    {'company': 'Apple Inc', 'address': '1 Apple Park Way, Cupertino, CA'},
    {'company': 'Google', 'address': '1600 Amphitheatre Parkway, Mountain View, CA'}
]

enricher = DataEnricher(api_keys={})
enriched = enricher.enrich_batch(items, {
    'address': 'location',
    'company': 'company'
})

print(enriched[0])
```

## Quality Monitoring Pipeline

Monitor data quality over time.

```python
from dataclasses import dataclass
from datetime import datetime
from typing import List, Dict, Optional
import statistics

@dataclass
class QualityMetrics:
    """Quality metrics for scraped data"""
    timestamp: datetime
    total_items: int
    valid_items: int
    invalid_items: int
    completeness: float  # % of fields filled
    accuracy_score: float  # Based on validation
    duplicate_rate: float
    error_rate: float
    
class QualityMonitor:
    """Monitor data quality over time"""
    
    def __init__(self):
        self.metrics_history: List[QualityMetrics] = []
    
    def calculate_completeness(self, items: List[Dict], 
                              required_fields: List[str]) -> float:
        """Calculate data completeness"""
        if not items:
            return 0.0
        
        total_fields = len(items) * len(required_fields)
        filled_fields = 0
        
        for item in items:
            for field in required_fields:
                if item.get(field) not in [None, '', [], {}]:
                    filled_fields += 1
        
        return (filled_fields / total_fields) * 100
    
    def calculate_quality_score(self, items: List[Dict],
                               schema: Dict,
                               required_fields: List[str]) -> QualityMetrics:
        """Calculate comprehensive quality score"""
        
        # Validate against schema
        validator = SchemaValidator(schema)
        validation_results = validator.validate_batch(items)
        
        # Calculate completeness
        completeness = self.calculate_completeness(items, required_fields)
        
        # Calculate accuracy (validation pass rate)
        accuracy = (validation_results['valid_count'] / 
                   validation_results['total'] * 100)
        
        # Detect duplicates
        dedup = ExactDeduplicator()
        unique = dedup.deduplicate_by_hash(items)
        duplicate_rate = ((len(items) - len(unique)) / len(items) * 100)
        
        # Error rate (inverse of accuracy)
        error_rate = 100 - accuracy
        
        metrics = QualityMetrics(
            timestamp=datetime.now(),
            total_items=len(items),
            valid_items=validation_results['valid_count'],
            invalid_items=validation_results['invalid_count'],
            completeness=completeness,
            accuracy_score=accuracy,
            duplicate_rate=duplicate_rate,
            error_rate=error_rate
        )
        
        self.metrics_history.append(metrics)
        
        return metrics
    
    def get_quality_report(self, metrics: QualityMetrics) -> str:
        """Generate quality report"""
        report = f"""
Data Quality Report
===================
Timestamp: {metrics.timestamp.isoformat()}

Volume:
  Total items: {metrics.total_items}
  Valid items: {metrics.valid_items}
  Invalid items: {metrics.invalid_items}

Quality Scores:
  Completeness: {metrics.completeness:.1f}%
  Accuracy: {metrics.accuracy_score:.1f}%
  Duplicate rate: {metrics.duplicate_rate:.1f}%
  Error rate: {metrics.error_rate:.1f}%

Overall Quality: {self._calculate_overall_quality(metrics):.1f}%
Quality Grade: {self._get_quality_grade(metrics)}
"""
        return report
    
    def _calculate_overall_quality(self, metrics: QualityMetrics) -> float:
        """Calculate overall quality score"""
        # Weighted average
        return (
            metrics.completeness * 0.3 +
            metrics.accuracy_score * 0.4 +
            (100 - metrics.duplicate_rate) * 0.2 +
            (100 - metrics.error_rate) * 0.1
        )
    
    def _get_quality_grade(self, metrics: QualityMetrics) -> str:
        """Get letter grade for quality"""
        score = self._calculate_overall_quality(metrics)
        
        if score >= 90:
            return 'A (Excellent)'
        elif score >= 80:
            return 'B (Good)'
        elif score >= 70:
            return 'C (Fair)'
        elif score >= 60:
            return 'D (Poor)'
        else:
            return 'F (Fail)'
    
    def get_trend_report(self, last_n: int = 10) -> str:
        """Generate trend report from history"""
        if len(self.metrics_history) < 2:
            return "Not enough data for trend analysis"
        
        recent = self.metrics_history[-last_n:]
        
        # Calculate trends
        completeness_trend = [m.completeness for m in recent]
        accuracy_trend = [m.accuracy_score for m in recent]
        
        report = f"""
Quality Trend Report (Last {len(recent)} runs)
============================================

Completeness:
  Average: {statistics.mean(completeness_trend):.1f}%
  Std Dev: {statistics.stdev(completeness_trend) if len(completeness_trend) > 1 else 0:.1f}
  Min: {min(completeness_trend):.1f}%
  Max: {max(completeness_trend):.1f}%

Accuracy:
  Average: {statistics.mean(accuracy_trend):.1f}%
  Std Dev: {statistics.stdev(accuracy_trend) if len(accuracy_trend) > 1 else 0:.1f}
  Min: {min(accuracy_trend):.1f}%
  Max: {max(accuracy_trend):.1f}%
"""
        
        return report

# Usage
monitor = QualityMonitor()

products = [
    {'id': '1', 'name': 'iPhone 13', 'price': 799, 'category': 'Electronics'},
    {'id': '2', 'name': 'MacBook Pro', 'price': 1999},
    {'id': '3', 'name': '', 'price': -100},  # Invalid
]

metrics = monitor.calculate_quality_score(
    items=products,
    schema=SchemaValidator.PRODUCT_SCHEMA,
    required_fields=['id', 'name', 'price', 'category']
)

print(monitor.get_quality_report(metrics))
```

## Summary

Data cleaning and quality assurance transforms raw scraped data into reliable, structured information:

1. **Regex Parsing**: Extract structured data from text using pattern matching
2. **NLP Extraction**: Use natural language processing for entity recognition
3. **Deduplication**: Remove exact and fuzzy duplicates efficiently
4. **Normalization**: Standardize formats for consistency
5. **Schema Validation**: Enforce data structure requirements
6. **Enrichment**: Add missing data from external sources
7. **Quality Monitoring**: Track and improve data quality over time
8. **Trend Analysis**: Monitor quality metrics to catch regressions

A robust data cleaning pipeline ensures that scraped data is accurate, complete, and ready for analysis or business use.