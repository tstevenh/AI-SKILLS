# AI API Integration Guide

> Complete technical guide to integrating AI APIs: authentication, best practices, error handling, and optimization.

---

## Table of Contents

1. [API Fundamentals](#api-fundamentals)
2. [Anthropic API (Claude)](#anthropic-api-claude)
3. [OpenAI API](#openai-api)
4. [Google AI APIs](#google-ai-apis)
5. [Open Source Model APIs](#open-source-model-apis)
6. [Integration Patterns](#integration-patterns)
7. [Error Handling](#error-handling)
8. [Performance Optimization](#performance-optimization)
9. [Security Best Practices](#security-best-practices)

---

## API Fundamentals

### Understanding AI APIs

AI APIs typically provide:
- Text generation (completions)
- Chat completions (multi-turn)
- Embeddings (vector representations)
- Image generation
- Speech-to-text
- Text-to-speech

### Common Concepts

**Tokens:**
- Basic unit of text processing
- ~4 characters per token (English)
- 100 words ≈ 130-150 tokens
- Affects cost and context limits

**Context Window:**
- Maximum tokens in a single request
- Includes input + output
- Varies by model (4K to 2M)

**Temperature:**
- Controls randomness (0.0-2.0)
- Lower = more deterministic
- Higher = more creative

**Max Tokens:**
- Limit on output length
- Always set appropriately

---

## Anthropic API (Claude)

### Authentication

```python
import anthropic

# Method 1: Direct API key
client = anthropic.Anthropic(api_key="your-api-key")

# Method 2: Environment variable (recommended)
# Set ANTHROPIC_API_KEY in environment
client = anthropic.Anthropic()
```

### Basic Usage

```python
import anthropic

client = anthropic.Anthropic()

# Simple message
message = client.messages.create(
    model="claude-3-5-sonnet-20241022",
    max_tokens=1024,
    messages=[
        {"role": "user", "content": "Hello, Claude!"}
    ]
)

print(message.content[0].text)
```

### Advanced Features

#### System Prompts
```python
message = client.messages.create(
    model="claude-3-5-sonnet-20241022",
    max_tokens=1024,
    system="You are a helpful assistant specializing in Python.",
    messages=[
        {"role": "user", "content": "How do I read a CSV file?"}
    ]
)
```

#### Multi-turn Conversations
```python
messages = [
    {"role": "user", "content": "What is Python?"},
    {"role": "assistant", "content": "Python is a programming language..."},
    {"role": "user", "content": "What are its main uses?"}
]

message = client.messages.create(
    model="claude-3-5-sonnet-20241022",
    max_tokens=1024,
    messages=messages
)
```

#### Streaming
```python
with client.messages.stream(
    model="claude-3-5-sonnet-20241022",
    max_tokens=1024,
    messages=[{"role": "user", "content": "Tell me a story."}]
) as stream:
    for text in stream.text_stream:
        print(text, end="", flush=True)
```

#### Tool Use (Function Calling)
```python
tools = [
    {
        "name": "get_weather",
        "description": "Get weather for a location",
        "input_schema": {
            "type": "object",
            "properties": {
                "location": {
                    "type": "string",
                    "description": "City name"
                },
                "unit": {
                    "type": "string",
                    "enum": ["celsius", "fahrenheit"]
                }
            },
            "required": ["location"]
        }
    }
]

message = client.messages.create(
    model="claude-3-5-sonnet-20241022",
    max_tokens=1024,
    tools=tools,
    messages=[
        {"role": "user", "content": "What's the weather in Paris?"}
    ]
)

# Handle tool use
if message.stop_reason == "tool_use":
    tool_use = message.content[0]
    # Call your actual function
    result = get_weather(**tool_use.input)
    
    # Continue conversation with result
    messages = [
        {"role": "user", "content": "What's the weather in Paris?"},
        {"role": "assistant", "content": message.content},
        {
            "role": "user",
            "content": [
                {
                    "type": "tool_result",
                    "tool_use_id": tool_use.id,
                    "content": str(result)
                }
            ]
        }
    ]
    
    final = client.messages.create(
        model="claude-3-5-sonnet-20241022",
        max_tokens=1024,
        tools=tools,
        messages=messages
    )
```

#### Vision (Image Input)
```python
import base64

# From file
with open("image.png", "rb") as f:
    image_data = base64.standard_b64encode(f.read()).decode()

# From URL (download first)
import httpx
image_data = base64.standard_b64encode(
    httpx.get("https://example.com/image.png").content
).decode()

message = client.messages.create(
    model="claude-3-5-sonnet-20241022",
    max_tokens=1024,
    messages=[
        {
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
                    "text": "What's in this image?"
                }
            ]
        }
    ]
)
```

#### Batch Processing
```python
# Create batch request
batch = client.beta.messages.batches.create(
    requests=[
        {
            "custom_id": f"request-{i}",
            "params": {
                "model": "claude-3-5-sonnet-20241022",
                "max_tokens": 1024,
                "messages": [{"role": "user", "content": prompt}]
            }
        }
        for i, prompt in enumerate(prompts)
    ]
)

# Poll for completion
import time
while batch.processing_status == "in_progress":
    time.sleep(60)
    batch = client.beta.messages.batches.retrieve(batch.id)

# Get results
results = client.beta.messages.batches.results(batch.id)
```

### Rate Limits

| Tier | Requests/min | Tokens/min | Tokens/day |
|------|-------------|------------|------------|
| 1 | 60 | 60,000 | 300,000 |
| 2 | 1,000 | 80,000 | 2,500,000 |
| 3 | 2,000 | 160,000 | 5,000,000 |
| 4 | 4,000 | 400,000 | 10,000,000 |

### Pricing (as of 2025)

| Model | Input/1M | Output/1M |
|-------|----------|-----------|
| Claude 3.5 Sonnet | $3.00 | $15.00 |
| Claude 3.5 Haiku | $0.25 | $1.25 |
| Claude 3 Opus | $15.00 | $75.00 |

---

## OpenAI API

### Authentication

```python
from openai import OpenAI

# Direct API key
client = OpenAI(api_key="your-api-key")

# Environment variable (recommended)
# Set OPENAI_API_KEY
client = OpenAI()
```

### Basic Usage

```python
from openai import OpenAI

client = OpenAI()

# Chat completion
response = client.chat.completions.create(
    model="gpt-4o",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Hello!"}
    ]
)

print(response.choices[0].message.content)
```

### Advanced Features

#### Streaming
```python
stream = client.chat.completions.create(
    model="gpt-4o",
    messages=[{"role": "user", "content": "Tell me a story."}],
    stream=True
)

for chunk in stream:
    if chunk.choices[0].delta.content:
        print(chunk.choices[0].delta.content, end="")
```

#### Function Calling
```python
tools = [
    {
        "type": "function",
        "function": {
            "name": "get_weather",
            "description": "Get weather for a location",
            "parameters": {
                "type": "object",
                "properties": {
                    "location": {"type": "string"},
                    "unit": {"type": "string", "enum": ["celsius", "fahrenheit"]}
                },
                "required": ["location"]
            }
        }
    }
]

response = client.chat.completions.create(
    model="gpt-4o",
    messages=[{"role": "user", "content": "What's the weather in NYC?"}],
    tools=tools,
    tool_choice="auto"
)

# Handle tool calls
if response.choices[0].message.tool_calls:
    for tool_call in response.choices[0].message.tool_calls:
        args = json.loads(tool_call.function.arguments)
        result = get_weather(**args)
        
        # Add tool result and continue
        messages.append(response.choices[0].message)
        messages.append({
            "role": "tool",
            "tool_call_id": tool_call.id,
            "content": str(result)
        })
```

#### JSON Mode
```python
response = client.chat.completions.create(
    model="gpt-4o",
    response_format={"type": "json_object"},
    messages=[
        {"role": "system", "content": "You output JSON."},
        {"role": "user", "content": "List 3 fruits with colors."}
    ]
)

data = json.loads(response.choices[0].message.content)
```

#### Vision
```python
response = client.chat.completions.create(
    model="gpt-4o",
    messages=[
        {
            "role": "user",
            "content": [
                {"type": "text", "text": "What's in this image?"},
                {
                    "type": "image_url",
                    "image_url": {
                        "url": "https://example.com/image.png",
                        # Or base64: "data:image/png;base64,..."
                    }
                }
            ]
        }
    ]
)
```

#### Embeddings
```python
response = client.embeddings.create(
    model="text-embedding-3-small",
    input="Hello, world!"
)

embedding = response.data[0].embedding  # 1536-dimensional vector
```

#### Image Generation (DALL-E)
```python
response = client.images.generate(
    model="dall-e-3",
    prompt="A white cat sitting on a windowsill",
    size="1024x1024",
    quality="hd",
    n=1
)

image_url = response.data[0].url
```

#### Text-to-Speech
```python
response = client.audio.speech.create(
    model="tts-1-hd",
    voice="nova",
    input="Hello, this is a test."
)

response.stream_to_file("output.mp3")
```

#### Speech-to-Text (Whisper)
```python
audio_file = open("audio.mp3", "rb")
transcript = client.audio.transcriptions.create(
    model="whisper-1",
    file=audio_file
)

print(transcript.text)
```

#### Batch API
```python
# Create batch file
batch_requests = [
    {
        "custom_id": f"request-{i}",
        "method": "POST",
        "url": "/v1/chat/completions",
        "body": {
            "model": "gpt-4o-mini",
            "messages": [{"role": "user", "content": prompt}]
        }
    }
    for i, prompt in enumerate(prompts)
]

# Upload file
file = client.files.create(
    file=io.BytesIO(json.dumps(batch_requests).encode()),
    purpose="batch"
)

# Create batch
batch = client.batches.create(
    input_file_id=file.id,
    endpoint="/v1/chat/completions",
    completion_window="24h"
)

# Poll and retrieve results
```

### Pricing (as of 2025)

| Model | Input/1M | Output/1M |
|-------|----------|-----------|
| GPT-4o | $2.50 | $10.00 |
| GPT-4o-mini | $0.15 | $0.60 |
| GPT-4 Turbo | $10.00 | $30.00 |
| o1-preview | $15.00 | $60.00 |

---

## Google AI APIs

### Gemini API

```python
import google.generativeai as genai

genai.configure(api_key="your-api-key")

model = genai.GenerativeModel("gemini-1.5-pro")

# Simple generation
response = model.generate_content("Tell me a joke")
print(response.text)

# Chat
chat = model.start_chat()
response = chat.send_message("Hello!")
print(response.text)

# With images
import PIL.Image
image = PIL.Image.open("image.png")
response = model.generate_content([image, "What's in this image?"])
```

### Vertex AI

```python
from google.cloud import aiplatform
from vertexai.generative_models import GenerativeModel

aiplatform.init(project="your-project", location="us-central1")

model = GenerativeModel("gemini-1.5-pro")
response = model.generate_content("Hello!")
```

---

## Open Source Model APIs

### Together.ai

```python
from together import Together

client = Together(api_key="your-api-key")

response = client.chat.completions.create(
    model="meta-llama/Meta-Llama-3.1-70B-Instruct-Turbo",
    messages=[{"role": "user", "content": "Hello!"}]
)
```

### Groq

```python
from groq import Groq

client = Groq(api_key="your-api-key")

response = client.chat.completions.create(
    model="llama3-70b-8192",
    messages=[{"role": "user", "content": "Hello!"}]
)
```

### Replicate

```python
import replicate

output = replicate.run(
    "meta/llama-2-70b-chat",
    input={"prompt": "Hello!"}
)

for item in output:
    print(item, end="")
```

### Ollama (Local)

```python
import ollama

response = ollama.chat(
    model="llama3.1",
    messages=[{"role": "user", "content": "Hello!"}]
)

print(response["message"]["content"])
```

---

## Integration Patterns

### Async Pattern

```python
import asyncio
from anthropic import AsyncAnthropic

async def process_batch(prompts: list[str]) -> list[str]:
    client = AsyncAnthropic()
    
    async def process_one(prompt: str) -> str:
        message = await client.messages.create(
            model="claude-3-5-sonnet-20241022",
            max_tokens=1024,
            messages=[{"role": "user", "content": prompt}]
        )
        return message.content[0].text
    
    tasks = [process_one(p) for p in prompts]
    return await asyncio.gather(*tasks)

# Usage
results = asyncio.run(process_batch(["Hello", "World"]))
```

### Retry Pattern

```python
import tenacity

@tenacity.retry(
    wait=tenacity.wait_exponential(multiplier=1, min=4, max=60),
    stop=tenacity.stop_after_attempt(5),
    retry=tenacity.retry_if_exception_type((
        anthropic.RateLimitError,
        anthropic.APIConnectionError,
        anthropic.APITimeoutError
    ))
)
async def call_api_with_retry(prompt: str) -> str:
    return await client.messages.create(...)
```

### Caching Pattern

```python
import hashlib
import redis

class LLMCache:
    def __init__(self):
        self.redis = redis.Redis()
        self.ttl = 86400 * 7  # 7 days
    
    def get_cache_key(self, model: str, prompt: str) -> str:
        content = f"{model}:{prompt}"
        return hashlib.sha256(content.encode()).hexdigest()
    
    async def get_or_generate(
        self, 
        model: str, 
        prompt: str, 
        generate_fn
    ) -> str:
        key = self.get_cache_key(model, prompt)
        
        # Check cache
        cached = self.redis.get(key)
        if cached:
            return cached.decode()
        
        # Generate
        result = await generate_fn(prompt)
        
        # Cache
        self.redis.setex(key, self.ttl, result)
        
        return result
```

### Fallback Pattern

```python
async def generate_with_fallback(prompt: str) -> str:
    models = [
        ("claude-3-5-sonnet", call_anthropic),
        ("gpt-4o", call_openai),
        ("llama-3.1-70b", call_together),
    ]
    
    for model_name, call_fn in models:
        try:
            return await call_fn(prompt)
        except Exception as e:
            logger.warning(f"{model_name} failed: {e}")
            continue
    
    raise Exception("All models failed")
```

---

## Error Handling

### Common Errors

```python
import anthropic

try:
    response = client.messages.create(...)
except anthropic.RateLimitError as e:
    # Too many requests - implement backoff
    logger.warning(f"Rate limited: {e}")
    await asyncio.sleep(60)
    
except anthropic.APIConnectionError as e:
    # Network issue - retry
    logger.error(f"Connection error: {e}")
    
except anthropic.APITimeoutError as e:
    # Request took too long - retry or reduce tokens
    logger.error(f"Timeout: {e}")
    
except anthropic.BadRequestError as e:
    # Invalid request - fix the request
    logger.error(f"Bad request: {e}")
    
except anthropic.AuthenticationError as e:
    # Invalid API key - check credentials
    logger.error(f"Auth error: {e}")
```

### Structured Error Handler

```python
class AIErrorHandler:
    def __init__(self, max_retries: int = 3):
        self.max_retries = max_retries
    
    async def execute(self, fn, *args, **kwargs):
        last_error = None
        
        for attempt in range(self.max_retries):
            try:
                return await fn(*args, **kwargs)
                
            except (RateLimitError, APIConnectionError, APITimeoutError) as e:
                last_error = e
                wait_time = self.calculate_backoff(attempt, e)
                logger.warning(f"Attempt {attempt + 1} failed: {e}. Retrying in {wait_time}s")
                await asyncio.sleep(wait_time)
                
            except BadRequestError as e:
                # Don't retry bad requests
                logger.error(f"Bad request: {e}")
                raise
                
            except AuthenticationError as e:
                # Don't retry auth errors
                logger.error(f"Auth error: {e}")
                raise
        
        raise last_error
    
    def calculate_backoff(self, attempt: int, error: Exception) -> float:
        # Check for Retry-After header
        if hasattr(error, 'response'):
            retry_after = error.response.headers.get('Retry-After')
            if retry_after:
                return float(retry_after)
        
        # Exponential backoff
        return min(4 ** attempt, 60)
```

---

## Performance Optimization

### Token Optimization

```python
def estimate_tokens(text: str) -> int:
    """Rough estimate: 4 chars per token"""
    return len(text) // 4

def optimize_prompt(prompt: str, max_tokens: int) -> str:
    """Reduce prompt size if needed"""
    current = estimate_tokens(prompt)
    
    if current <= max_tokens:
        return prompt
    
    # Truncate or summarize
    ratio = max_tokens / current
    truncated_length = int(len(prompt) * ratio * 0.9)  # Leave buffer
    return prompt[:truncated_length] + "..."
```

### Parallel Processing

```python
import asyncio
from typing import List

async def process_batch_parallel(
    items: List[str],
    max_concurrent: int = 10
) -> List[str]:
    semaphore = asyncio.Semaphore(max_concurrent)
    
    async def process_one(item: str) -> str:
        async with semaphore:
            return await call_api(item)
    
    tasks = [process_one(item) for item in items]
    return await asyncio.gather(*tasks)
```

### Response Streaming

```python
async def stream_response(prompt: str):
    """Stream response for faster time-to-first-token"""
    async with client.messages.stream(
        model="claude-3-5-sonnet-20241022",
        max_tokens=1024,
        messages=[{"role": "user", "content": prompt}]
    ) as stream:
        async for text in stream.text_stream:
            yield text
```

---

## Security Best Practices

### API Key Management

```python
import os
from dotenv import load_dotenv

# Load from .env file
load_dotenv()

# Never hardcode keys
api_key = os.getenv("ANTHROPIC_API_KEY")

# Validate key exists
if not api_key:
    raise ValueError("ANTHROPIC_API_KEY not set")

# Use secret managers in production
# AWS Secrets Manager, GCP Secret Manager, etc.
```

### Input Sanitization

```python
def sanitize_prompt(user_input: str) -> str:
    """Remove potential injection attempts"""
    # Remove prompt injection patterns
    patterns_to_remove = [
        "ignore previous instructions",
        "disregard above",
        "system prompt",
        "new instructions:"
    ]
    
    sanitized = user_input.lower()
    for pattern in patterns_to_remove:
        if pattern in sanitized:
            raise ValueError("Potential injection detected")
    
    return user_input

def validate_output(response: str) -> bool:
    """Validate AI response before using"""
    # Check for PII
    if contains_pii(response):
        return False
    
    # Check for harmful content
    if contains_harmful_content(response):
        return False
    
    return True
```

### Rate Limiting

```python
from datetime import datetime, timedelta
from collections import defaultdict

class RateLimiter:
    def __init__(self, requests_per_minute: int):
        self.limit = requests_per_minute
        self.requests = defaultdict(list)
    
    def can_make_request(self, key: str) -> bool:
        now = datetime.now()
        minute_ago = now - timedelta(minutes=1)
        
        # Clean old requests
        self.requests[key] = [
            t for t in self.requests[key] 
            if t > minute_ago
        ]
        
        return len(self.requests[key]) < self.limit
    
    def record_request(self, key: str):
        self.requests[key].append(datetime.now())
```

---

## Summary

### API Selection Guide

| Need | Recommended API |
|------|-----------------|
| Best reasoning | Claude 3.5 Sonnet |
| Best coding | Claude 3.5 Sonnet |
| High volume, simple | GPT-4o-mini |
| Vision tasks | GPT-4o or Claude |
| Long context | Gemini 1.5 Pro |
| Fastest inference | Groq (Llama) |
| Self-hosted | Ollama |
| Cost-sensitive | Together.ai |

### Integration Checklist

- [ ] API key securely stored
- [ ] Error handling implemented
- [ ] Rate limiting in place
- [ ] Retry logic configured
- [ ] Caching where appropriate
- [ ] Logging for debugging
- [ ] Cost monitoring
- [ ] Input validation
- [ ] Output validation

See [../cost-optimization/strategies.md](../cost-optimization/strategies.md) for cost optimization →
