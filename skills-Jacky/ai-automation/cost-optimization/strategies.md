# AI Automation Cost Optimization

> Comprehensive strategies for reducing AI and automation costs while maintaining quality.

---

## Table of Contents

1. [API Cost Management](#api-cost-management)
2. [Platform Cost Optimization](#platform-cost-optimization)
3. [Infrastructure Decisions](#infrastructure-decisions)
4. [ROI Tracking](#roi-tracking)
5. [Cost Benchmarks](#cost-benchmarks)

---

## API Cost Management

### Understanding AI Costs

**Cost components:**
- Input tokens (what you send)
- Output tokens (what AI generates)
- API calls (some models charge per call)
- Storage (embeddings, files)

**Token estimation:**
- ~4 characters = 1 token (English)
- 100 words ≈ 130-150 tokens
- A typical email ≈ 200-500 tokens
- A blog post ≈ 1,500-3,000 tokens

### Model Selection Strategy

**Tiered Model Approach:**

```python
def select_model(task_type, complexity):
    """Route to appropriate model based on task."""
    
    # Tier 1: Cheapest (GPT-4o-mini, Claude Haiku)
    # $0.15-0.25 per 1M input tokens
    tier_1_tasks = [
        "classification",
        "simple_extraction",
        "summarization_short",
        "format_conversion",
    ]
    
    # Tier 2: Mid-range (GPT-4o, Claude Sonnet)
    # $2.50-3.00 per 1M input tokens
    tier_2_tasks = [
        "content_generation",
        "analysis",
        "complex_extraction",
        "code_generation",
    ]
    
    # Tier 3: Premium (Claude Opus, o1)
    # $15+ per 1M input tokens
    tier_3_tasks = [
        "complex_reasoning",
        "research_synthesis",
        "critical_decisions",
    ]
    
    if task_type in tier_1_tasks or complexity == "simple":
        return "gpt-4o-mini"
    elif task_type in tier_2_tasks or complexity == "medium":
        return "claude-3-5-sonnet"
    else:
        return "claude-3-opus"
```

**Cost comparison example (1,000 emails classified):**

| Model | Input (1M) | Output | Total |
|-------|------------|--------|-------|
| GPT-4o-mini | $0.15 | $0.12 | $0.27 |
| GPT-4o | $2.50 | $2.00 | $4.50 |
| Claude Sonnet | $3.00 | $3.00 | $6.00 |

**Savings: 95% by using mini for simple tasks**

### Prompt Optimization

**Before (847 tokens):**
```
I would like you to analyze the following customer support 
email and determine the appropriate category. The categories 
are: billing, technical, shipping, account, and general. 
Please also determine the priority level which can be low, 
medium, high, or urgent. Additionally, please identify the 
customer's sentiment and provide a brief summary of the issue.

Here is the email:
[email content]
```

**After (234 tokens):**
```
Classify this email. Output JSON only:
{
  "category": "billing|technical|shipping|account|general",
  "priority": "low|medium|high|urgent",
  "sentiment": "positive|neutral|negative",
  "issue_summary": "<20 words>"
}

Email:
[email content]
```

**Savings: 72% fewer input tokens**

### Caching Strategies

**1. Exact Match Cache**
```python
import hashlib
import redis

class LLMCache:
    def __init__(self):
        self.redis = redis.Redis()
        self.ttl = 86400 * 7  # 7 days
    
    def get_or_generate(self, prompt, model, generate_fn):
        # Create cache key
        key = hashlib.sha256(
            f"{model}:{prompt}".encode()
        ).hexdigest()
        
        # Check cache
        cached = self.redis.get(key)
        if cached:
            return cached.decode()
        
        # Generate and cache
        result = generate_fn(prompt, model)
        self.redis.setex(key, self.ttl, result)
        return result
```

**2. Semantic Cache**
```python
# Cache similar queries using embeddings
def get_cached_similar(query, threshold=0.95):
    query_embedding = embed(query)
    similar = vector_db.search(query_embedding, top_k=1)
    
    if similar.score > threshold:
        return similar.cached_response
    return None
```

**Cache hit rates by use case:**

| Use Case | Expected Hit Rate | Savings |
|----------|-------------------|---------|
| FAQ responses | 60-80% | 60-80% |
| Classification | 30-50% | 30-50% |
| Content generation | 5-15% | 5-15% |
| Personalized content | <5% | <5% |

### Batch Processing

**OpenAI Batch API:**
```python
# 50% discount, 24-hour window
batch = client.batches.create(
    input_file_id=file.id,
    endpoint="/v1/chat/completions",
    completion_window="24h"
)
```

**When to batch:**
- Non-time-sensitive tasks
- Large volume processing
- Report generation
- Data enrichment

### Output Control

```python
# Limit output length
response = client.chat.completions.create(
    model="gpt-4o-mini",
    max_tokens=100,  # Hard limit
    messages=[{
        "role": "user",
        "content": "Summarize in 2 sentences max: ..."
    }]
)
```

**Output tokens are 3-4x more expensive than input!**

---

## Platform Cost Optimization

### Automation Platform Costs

**n8n:**
| Scenario | Cloud Cost | Self-Hosted |
|----------|-----------|-------------|
| 5,000 exec/mo | $20 | $10-20 server |
| 50,000 exec/mo | $50 | $20-50 server |
| 500,000 exec/mo | Custom | $50-100 server |

**Make:**
| Operations/mo | Cost |
|---------------|------|
| 10,000 | $21 |
| 40,000 | $54 |
| 150,000 | $166 |

**Zapier:**
| Tasks/mo | Cost |
|----------|------|
| 750 | $30 |
| 2,000 | $74 |
| 50,000 | $299 |

### Reducing Operation Counts

**1. Filter early**
```
# Bad: Process then filter
Trigger → Action → Action → Filter → Action

# Good: Filter first
Trigger → Filter → Action → Action
```

**2. Aggregate calls**
```
# Bad: 100 API calls
For each item → API call

# Good: 1 batch call
Aggregate items → Batch API call
```

**3. Use polling wisely**
```
# Expensive: Check every minute
Check → No new data → Waste

# Better: Use webhooks when available
Webhook trigger → Process only when data exists
```

### Free Tier Maximization

**Tools with generous free tiers:**

| Tool | Free Tier |
|------|-----------|
| Apollo | 10k contacts/month |
| Hunter | 25 searches/month |
| Notion | Unlimited pages |
| Airtable | 1,000 records/base |
| n8n | Unlimited (self-hosted) |
| Google Sheets | Generous limits |

---

## Infrastructure Decisions

### Self-Hosting vs Cloud

**Self-host when:**
- Volume > 50,000 executions/month
- Data sensitivity requirements
- Need for customization
- Technical team available
- Predictable workloads

**Cloud when:**
- Quick start needed
- < 50,000 executions/month
- No ops team
- Variable workloads
- Need managed reliability

### Self-Hosting Cost Breakdown

**n8n on DigitalOcean:**
```
Server: $48/month (4GB RAM Droplet)
Managed PostgreSQL: $15/month
Backup: $5/month
Total: $68/month

Equivalent cloud cost at scale: $200-500/month
Savings: 60-85%
```

### When to Upgrade

**Signs you need more resources:**
- Execution timeouts increasing
- Queue backing up
- Memory errors
- API rate limits hit

**Scaling options:**
1. Vertical: Bigger server
2. Horizontal: Worker nodes
3. Queue mode: Redis + workers

---

## ROI Tracking

### Tracking Framework

```python
class AutomationROI:
    def calculate_monthly_savings(self, automation):
        # Time savings
        time_saved = (
            automation.runs_per_month * 
            automation.minutes_saved_per_run / 60
        )
        time_value = time_saved * automation.hourly_rate
        
        # Quality improvements
        error_reduction = (
            automation.errors_prevented * 
            automation.error_cost
        )
        
        # Revenue impact
        revenue = automation.leads_influenced * automation.conversion_rate * automation.deal_value
        
        # Costs
        api_cost = automation.api_cost_per_run * automation.runs_per_month
        platform_cost = automation.platform_cost_per_month
        maintenance = automation.maintenance_hours * automation.hourly_rate
        
        total_benefit = time_value + error_reduction + revenue
        total_cost = api_cost + platform_cost + maintenance
        
        return {
            "gross_savings": total_benefit,
            "costs": total_cost,
            "net_savings": total_benefit - total_cost,
            "roi_percent": (total_benefit - total_cost) / total_cost * 100
        }
```

### Dashboard Metrics

**Track weekly:**
- Total API spend by provider
- Cost per automation run
- Cost per successful outcome
- Model usage breakdown
- Cache hit rate

### Cost Alerts

```python
# Set up budget alerts
alerts = [
    {"provider": "openai", "monthly_budget": 500, "alert_at": [50, 80, 100]},
    {"provider": "anthropic", "monthly_budget": 300, "alert_at": [50, 80, 100]},
    {"provider": "make", "monthly_budget": 50, "alert_at": [80, 100]},
]
```

---

## Cost Benchmarks

### Cost Per Task Benchmarks

| Task | Optimal Cost | Model |
|------|-------------|-------|
| Email classification | $0.001 | GPT-4o-mini |
| Email draft | $0.005 | GPT-4o-mini |
| Blog post (2000 words) | $0.10-0.30 | Claude Sonnet |
| Lead enrichment | $0.15-0.50 | APIs + mini |
| Support ticket response | $0.02-0.05 | Claude Sonnet |
| Image generation | $0.04-0.10 | DALL-E/Flux |
| Voice (1 min) | $0.30 | ElevenLabs |
| Transcription (1 min) | $0.006 | Whisper |

### Monthly Budget Examples

**Startup (5 employees):**
```
AI APIs: $100
Automation platform: $50 (n8n cloud)
Data enrichment: $100
Total: $250/month
```

**Growth company (25 employees):**
```
AI APIs: $500
Automation platform: $100 (n8n self-hosted)
Data enrichment: $300
Support tools: $200
Total: $1,100/month
```

**Mid-market (100 employees):**
```
AI APIs: $2,000
Automation platform: $500
Data enrichment: $800
Support tools: $500
Sales tools: $500
Total: $4,300/month
```

### Cost Reduction Checklist

- [ ] Using cheapest appropriate model for each task
- [ ] Prompts optimized for token efficiency
- [ ] Caching implemented where applicable
- [ ] Batch processing for non-urgent tasks
- [ ] Output length controlled
- [ ] Free tiers maximized
- [ ] Self-hosting evaluated for high volume
- [ ] Monitoring and alerts active
- [ ] Regular usage review scheduled

---

## Summary

### Key Strategies

1. **Model tiering** - Use cheap models for simple tasks
2. **Prompt optimization** - Fewer tokens = lower cost
3. **Caching** - Don't regenerate identical content
4. **Batching** - 50% savings with batch APIs
5. **Output control** - Limit expensive output tokens
6. **Self-hosting** - 60-85% savings at scale
7. **Monitor actively** - Catch waste early

### Expected Savings

Implementing all strategies:
- **30-50%** reduction in API costs
- **60-85%** reduction with self-hosting
- **10-20%** reduction in platform costs

### Next Steps

1. Audit current spending
2. Implement model tiering
3. Set up caching
4. Configure budget alerts
5. Schedule monthly reviews

See [../implementation/roadmap.md](../implementation/roadmap.md) for implementation guidance.
