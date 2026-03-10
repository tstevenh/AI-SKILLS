# AI Data Processing & Entry

> Complete guide to automating data entry, extraction, and processing with AI.

---

## Table of Contents

1. [Data Processing Overview](#data-processing-overview)
2. [Document Extraction](#document-extraction)
3. [Form Processing](#form-processing)
4. [Data Normalization](#data-normalization)
5. [Spreadsheet Automation](#spreadsheet-automation)
6. [Data Quality & Validation](#data-quality--validation)
7. [Integration Patterns](#integration-patterns)

---

## Data Processing Overview

### The Data Entry Problem

Manual data entry is:
- **Expensive:** $20-40/hour for entry clerks
- **Error-prone:** 1-4% error rate typical
- **Slow:** 30-60 items/hour
- **Soul-crushing:** High turnover

### AI-Powered Data Processing

| Task | Manual | AI | Improvement |
|------|--------|-----|-------------|
| Invoice data extraction | 5 min | 10 sec | 30x faster |
| Resume parsing | 3 min | 5 sec | 36x faster |
| Form data entry | 2 min | Instant | ~100x faster |
| Data normalization | 1 min | Instant | ~60x faster |
| Error rate | 2-4% | <1% | 75% fewer errors |

### Data Processing Categories

```
┌─────────────────────────────────────────────────────────┐
│              DATA PROCESSING TYPES                       │
├─────────────────────────────────────────────────────────┤
│                                                          │
│  EXTRACTION (Unstructured → Structured)                 │
│  ├── Document OCR                                        │
│  ├── Invoice processing                                  │
│  ├── Receipt parsing                                     │
│  ├── Email data extraction                               │
│  └── Resume parsing                                      │
│                                                          │
│  TRANSFORMATION (Structured → Structured)               │
│  ├── Format conversion                                   │
│  ├── Data normalization                                  │
│  ├── Deduplication                                       │
│  ├── Enrichment                                          │
│  └── Aggregation                                         │
│                                                          │
│  VALIDATION (Quality Assurance)                         │
│  ├── Format validation                                   │
│  ├── Completeness check                                  │
│  ├── Cross-reference verification                        │
│  └── Anomaly detection                                   │
│                                                          │
└─────────────────────────────────────────────────────────┘
```

---

## Document Extraction

### Invoice Processing

**Vision-Based Extraction:**

```python
from anthropic import Anthropic
import base64

def extract_invoice_data(image_path: str) -> dict:
    client = Anthropic()
    
    with open(image_path, "rb") as f:
        image_data = base64.b64encode(f.read()).decode()
    
    response = client.messages.create(
        model="claude-3-5-sonnet-20241022",
        max_tokens=1024,
        messages=[{
            "role": "user",
            "content": [
                {
                    "type": "image",
                    "source": {
                        "type": "base64",
                        "media_type": "image/png",
                        "data": image_data
                    }
                },
                {
                    "type": "text",
                    "text": """
                    Extract all data from this invoice. Return JSON:
                    {
                        "vendor": {
                            "name": "",
                            "address": "",
                            "phone": "",
                            "email": ""
                        },
                        "invoice_number": "",
                        "invoice_date": "",
                        "due_date": "",
                        "purchase_order": "",
                        "line_items": [
                            {
                                "description": "",
                                "quantity": 0,
                                "unit_price": 0.00,
                                "total": 0.00
                            }
                        ],
                        "subtotal": 0.00,
                        "tax": 0.00,
                        "total": 0.00,
                        "payment_terms": "",
                        "notes": ""
                    }
                    """
                }
            ]
        }]
    )
    
    return json.loads(response.content[0].text)
```

**Invoice Processing Workflow:**

```yaml
workflow: Invoice Processor

trigger: 
  - Gmail: New attachment (subject contains "invoice")
  - Google Drive: New file in /Invoices

steps:
  - download_attachment
  
  - convert_to_image:
      if: pdf
      tool: pdf2image
      
  - extract_data:
      model: claude-3-5-sonnet (vision)
      prompt: [invoice extraction prompt]
      
  - validate_data:
      - check: total == sum(line_items) + tax
      - check: required_fields_present
      - check: vendor_exists_in_system
      
  - create_record:
      QuickBooks:
        action: Create Bill
      OR
      Google Sheets:
        action: Append Row
        
  - archive_original:
      Google Drive:
        folder: /Invoices/Processed/{{ year }}/{{ month }}
        
  - notify:
      Slack: Invoice processed: {{ vendor }} - ${{ total }}
```

### Receipt Processing

**Prompt:**
```
Extract data from this receipt image:

Return JSON:
{
  "merchant": {
    "name": "",
    "address": "",
    "phone": ""
  },
  "transaction": {
    "date": "",
    "time": "",
    "payment_method": "",
    "card_last_four": ""
  },
  "items": [
    {
      "name": "",
      "quantity": 1,
      "price": 0.00
    }
  ],
  "subtotal": 0.00,
  "tax": 0.00,
  "tip": 0.00,
  "total": 0.00,
  "category": "" // food, transport, supplies, etc.
}
```

### Contract Data Extraction

**Prompt:**
```
Extract key information from this contract:

{contract_text}

Return JSON:
{
  "parties": [
    {
      "name": "",
      "role": "party_a/party_b",
      "address": ""
    }
  ],
  "contract_type": "",
  "effective_date": "",
  "termination_date": "",
  "auto_renewal": true/false,
  "renewal_terms": "",
  "payment_terms": {
    "amount": 0.00,
    "frequency": "",
    "due_date": ""
  },
  "key_obligations": [
    {
      "party": "",
      "obligation": ""
    }
  ],
  "termination_clauses": [],
  "governing_law": "",
  "dispute_resolution": "",
  "confidentiality": true/false,
  "non_compete": true/false,
  "key_dates": [
    {
      "description": "",
      "date": ""
    }
  ],
  "summary": ""  // 2-3 sentence summary
}
```

### Resume Parsing

**Prompt:**
```
Parse this resume into structured data:

{resume_text}

Return JSON:
{
  "candidate": {
    "name": "",
    "email": "",
    "phone": "",
    "location": "",
    "linkedin": "",
    "portfolio": ""
  },
  "summary": "",  // 2-3 sentences
  "experience": [
    {
      "company": "",
      "title": "",
      "start_date": "",
      "end_date": "",
      "current": true/false,
      "description": "",
      "achievements": []
    }
  ],
  "education": [
    {
      "institution": "",
      "degree": "",
      "field": "",
      "graduation_date": "",
      "gpa": ""
    }
  ],
  "skills": {
    "technical": [],
    "soft": [],
    "languages": [],
    "certifications": []
  },
  "years_experience": 0,
  "most_recent_title": "",
  "key_strengths": []
}
```

---

## Form Processing

### Web Form to Database

**Workflow:**
```yaml
trigger: Typeform/HubSpot/Custom webhook

steps:
  - validate_fields:
      required: [email, name, company]
      format:
        email: valid_email
        phone: normalize_phone
        
  - enrich_if_needed:
      condition: company_data_missing
      action: clearbit_lookup
      
  - normalize_data:
      name: proper_case
      company: remove_suffixes
      phone: format_e164
      
  - check_duplicates:
      match_on: [email, phone, company+name]
      action: merge_or_create
      
  - create_record:
      database: CRM/Airtable/PostgreSQL
      
  - trigger_workflows:
      - assign_owner
      - send_welcome
      - add_to_sequence
```

### Paper Form Digitization

```python
class FormDigitizer:
    def __init__(self, form_template: dict):
        self.template = form_template
        self.llm = Anthropic()
    
    async def process_form(self, image_path: str) -> dict:
        # Extract raw text/data
        raw_data = await self.extract_from_image(image_path)
        
        # Map to template fields
        mapped_data = await self.map_to_template(raw_data)
        
        # Validate
        validated = self.validate(mapped_data)
        
        return validated
    
    async def extract_from_image(self, image_path: str) -> dict:
        prompt = f"""
        Extract all handwritten and printed text from this form.
        
        Form type: {self.template['name']}
        Expected fields: {self.template['fields']}
        
        Return JSON with field names as keys.
        For checkboxes, return true/false.
        For signatures, return "signed" or "unsigned".
        Mark unclear fields as "UNCLEAR: [best guess]"
        """
        
        return await self.llm.vision_extract(image_path, prompt)
    
    async def map_to_template(self, raw_data: dict) -> dict:
        prompt = f"""
        Map this extracted data to the template fields:
        
        Extracted: {raw_data}
        Template: {self.template}
        
        Handle:
        - Field name variations
        - Date format normalization
        - Phone number formatting
        - Address parsing
        """
        
        return await self.llm.generate(prompt)
```

### Email Data Extraction

**Prompt:**
```
Extract structured data from this email:

{email_content}

Determine the email type and extract relevant data:

If ORDER:
{
  "type": "order",
  "order_number": "",
  "customer_email": "",
  "items": [...],
  "total": 0.00,
  "shipping_address": {...}
}

If SUPPORT_REQUEST:
{
  "type": "support",
  "customer_email": "",
  "issue_category": "",
  "issue_description": "",
  "urgency": "",
  "product_mentioned": ""
}

If INQUIRY:
{
  "type": "inquiry",
  "sender_email": "",
  "company": "",
  "inquiry_type": "",
  "budget_mentioned": "",
  "timeline_mentioned": ""
}

If OTHER:
{
  "type": "other",
  "summary": "",
  "action_needed": true/false,
  "priority": ""
}
```

---

## Data Normalization

### Address Normalization

**Prompt:**
```
Normalize these addresses to a standard format:

Addresses:
{addresses_list}

For each address, return:
{
  "original": "",
  "normalized": {
    "street1": "",
    "street2": "",
    "city": "",
    "state": "",  // 2-letter code
    "zip": "",    // 5 or 9 digit
    "country": "" // ISO 2-letter
  },
  "valid": true/false,
  "issues": []  // any problems found
}

Handle:
- Abbreviations (St., Ave., Blvd.)
- Apartment/suite numbers
- Missing state/zip
- International formats
```

### Name Normalization

```python
def normalize_name(name: str) -> dict:
    prompt = f"""
    Parse and normalize this name: "{name}"
    
    Return:
    {{
      "original": "{name}",
      "first_name": "",
      "middle_name": "",
      "last_name": "",
      "suffix": "",  // Jr., III, etc.
      "prefix": "",  // Dr., Mr., etc.
      "display_name": "",  // First Last
      "formal_name": "",   // Mr. First Last Jr.
      "sortable_name": ""  // Last, First
    }}
    
    Handle edge cases:
    - Multiple last names
    - Asian name order
    - Single name only
    - Nicknames in quotes/parentheses
    """
    return llm.generate(prompt)
```

### Company Name Normalization

```python
def normalize_company(name: str) -> dict:
    prompt = f"""
    Normalize this company name: "{name}"
    
    Return:
    {{
      "original": "{name}",
      "cleaned": "",  // Remove Inc., LLC, etc.
      "legal_name": "",  // With Inc., LLC, etc.
      "display_name": "",
      "domain_guess": "",  // Best guess at website
      "parent_company": "",  // If subsidiary
      "variations": []  // Common alternate names
    }}
    
    Handle:
    - Legal suffixes (Inc., LLC, Corp., Ltd.)
    - "The" prefix
    - Punctuation (& vs and)
    - Subsidiaries/DBAs
    - Typos/misspellings
    """
    return llm.generate(prompt)
```

### Deduplication

```python
class SmartDeduplicator:
    def __init__(self, llm, embedding_model):
        self.llm = llm
        self.embedder = embedding_model
    
    async def find_duplicates(self, records: list) -> list:
        # Step 1: Blocking by obvious matches
        blocks = self.create_blocks(records)
        
        # Step 2: Embed for semantic matching
        embeddings = await self.embedder.batch_embed(records)
        
        # Step 3: Find candidate pairs
        candidates = self.find_similar_pairs(embeddings, threshold=0.85)
        
        # Step 4: AI verification
        verified_duplicates = []
        for pair in candidates:
            is_dup = await self.verify_duplicate(pair)
            if is_dup:
                verified_duplicates.append(pair)
        
        return verified_duplicates
    
    async def verify_duplicate(self, pair: tuple) -> bool:
        prompt = f"""
        Are these two records the same entity?
        
        Record 1:
        {pair[0]}
        
        Record 2:
        {pair[1]}
        
        Consider:
        - Name variations/typos
        - Address variations
        - Phone number formatting
        - Email variations
        
        Return:
        {{
          "is_duplicate": true/false,
          "confidence": 0-100,
          "reasoning": "",
          "merge_strategy": "keep_1|keep_2|merge"
        }}
        """
        result = await self.llm.generate(prompt)
        return result["is_duplicate"] and result["confidence"] > 80
```

---

## Spreadsheet Automation

### Data Cleaning

**Prompt:**
```
Clean this spreadsheet data:

{csv_data}

Tasks:
1. Standardize column names (snake_case)
2. Fix data types (dates, numbers, booleans)
3. Remove duplicates
4. Fill obvious missing values
5. Flag unclear/inconsistent data
6. Normalize formats (dates, phones, addresses)

Return:
{
  "cleaned_data": [...],
  "changes_made": [...],
  "rows_removed": 0,
  "issues_found": [...],
  "suggestions": [...]
}
```

### Report Generation

**Prompt:**
```
Analyze this data and generate a report:

{data}

REPORT TYPE: {weekly_sales / monthly_metrics / inventory}
AUDIENCE: {executives / operations / sales_team}

Generate:

# {Report Title}

## Executive Summary
[3-5 bullet points of key findings]

## Key Metrics
| Metric | Current | Previous | Change |
|--------|---------|----------|--------|
[Relevant metrics]

## Insights
[3-5 notable observations with explanations]

## Recommendations
[2-3 actionable recommendations]

## Appendix
[Supporting data tables]
```

### Pivot Table Generation

```python
async def generate_pivot_analysis(data: pd.DataFrame, question: str):
    prompt = f"""
    Given this data:
    Columns: {list(data.columns)}
    Sample rows: {data.head(5).to_dict()}
    Row count: {len(data)}
    
    Question: {question}
    
    Determine the best pivot table structure:
    {
      "rows": [],      // Fields to use as rows
      "columns": [],   // Fields to use as columns
      "values": [],    // Fields to aggregate
      "aggregations": [], // sum, count, avg, etc.
      "filters": [],   // Any filters to apply
      "explanation": ""
    }
    
    Then provide the SQL or pandas code to generate it.
    """
    
    config = await llm.generate(prompt)
    
    # Execute the analysis
    result = execute_pivot(data, config)
    
    return result
```

---

## Data Quality & Validation

### Validation Rules Engine

```python
class DataValidator:
    def __init__(self, schema: dict, llm):
        self.schema = schema
        self.llm = llm
    
    def validate_record(self, record: dict) -> dict:
        errors = []
        warnings = []
        
        for field, rules in self.schema.items():
            value = record.get(field)
            
            # Required check
            if rules.get("required") and not value:
                errors.append(f"Missing required field: {field}")
                continue
            
            # Type check
            if not self.check_type(value, rules.get("type")):
                errors.append(f"Invalid type for {field}")
            
            # Format check
            if rules.get("format"):
                if not self.check_format(value, rules["format"]):
                    errors.append(f"Invalid format for {field}")
            
            # Range check
            if rules.get("min") or rules.get("max"):
                if not self.check_range(value, rules):
                    warnings.append(f"Value out of range for {field}")
            
            # Custom validation
            if rules.get("custom"):
                result = self.custom_validate(value, rules["custom"])
                if not result.valid:
                    warnings.extend(result.warnings)
        
        return {
            "valid": len(errors) == 0,
            "errors": errors,
            "warnings": warnings,
            "record": record
        }
    
    async def ai_validate(self, record: dict) -> dict:
        """Use AI for complex validation"""
        prompt = f"""
        Validate this record against common sense and data quality rules:
        
        Record: {record}
        Context: {self.schema.get('context', '')}
        
        Check for:
        1. Logically inconsistent values
        2. Likely data entry errors
        3. Suspicious patterns
        4. Missing correlations
        5. Outlier values
        
        Return:
        {{
          "issues": [...],
          "suggestions": [...],
          "confidence": 0-100
        }}
        """
        return await self.llm.generate(prompt)
```

### Anomaly Detection

```python
async def detect_anomalies(data: list, context: str) -> list:
    prompt = f"""
    Analyze this data for anomalies:
    
    Data: {data}
    Context: {context}
    
    Look for:
    1. Outlier values (statistical)
    2. Pattern breaks
    3. Missing sequences
    4. Duplicate entries
    5. Impossible combinations
    6. Sudden changes
    
    Return:
    [
      {{
        "index": 0,
        "field": "",
        "issue": "",
        "severity": "high|medium|low",
        "suggested_value": "",
        "confidence": 0-100
      }}
    ]
    """
    return await llm.generate(prompt)
```

---

## Integration Patterns

### Database Sync

```yaml
workflow: Form to Database Sync

trigger: webhook

steps:
  - receive_data
  
  - validate:
      schema: form_schema
      
  - normalize:
      - names
      - addresses
      - phones
      
  - deduplicate:
      match_fields: [email, phone]
      action: update_or_create
      
  - sync_to_db:
      target: PostgreSQL
      table: customers
      upsert_on: email
      
  - sync_to_crm:
      target: HubSpot
      object: Contact
      
  - log:
      destination: audit_log
```

### ETL Pipeline

```python
class AIEnhancedETL:
    def extract(self, source):
        """Extract from various sources"""
        if source.type == "email":
            return self.extract_from_email(source)
        elif source.type == "document":
            return self.extract_from_document(source)
        elif source.type == "form":
            return self.extract_from_form(source)
    
    async def transform(self, data: dict) -> dict:
        """AI-powered transformation"""
        # Normalize
        data = await self.normalize(data)
        
        # Enrich
        data = await self.enrich(data)
        
        # Validate
        validation = await self.validate(data)
        
        if validation.has_errors:
            data = await self.auto_fix(data, validation.errors)
        
        return data
    
    def load(self, data: dict, target):
        """Load to destination"""
        if target.type == "database":
            self.load_to_db(data, target)
        elif target.type == "spreadsheet":
            self.load_to_sheet(data, target)
        elif target.type == "api":
            self.load_to_api(data, target)
```

---

## Summary

### Cost Savings

| Process | Manual Cost | AI Cost | Savings |
|---------|-------------|---------|---------|
| Invoice processing | $5/invoice | $0.10/invoice | 98% |
| Resume parsing | $3/resume | $0.05/resume | 98% |
| Data entry (100 records) | $50 | $2 | 96% |
| Data cleaning | $100/hour | $10/hour | 90% |

### Implementation Priority

1. **Week 1:** Invoice/receipt processing
2. **Week 2:** Form data automation
3. **Week 3:** Data normalization
4. **Week 4:** Quality validation

See [../workflows/n8n/templates.md](../workflows/n8n/templates.md) for data processing templates →
