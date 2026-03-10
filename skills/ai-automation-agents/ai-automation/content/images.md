# AI Image Generation Deep Dive

> Complete guide to AI image generation for business: tools, workflows, prompts, and production systems.

---

## Table of Contents

1. [AI Image Strategy](#ai-image-strategy)
2. [Tools Deep Dive](#tools-deep-dive)
3. [Prompt Engineering](#prompt-engineering)
4. [Use Case Workflows](#use-case-workflows)
5. [Brand Consistency](#brand-consistency)
6. [Production Pipelines](#production-pipelines)
7. [Quality Control](#quality-control)
8. [Legal Considerations](#legal-considerations)

---

## AI Image Strategy

### When to Use AI Images

**Best for:**
- Blog hero images
- Social media graphics
- Ad creative testing
- Presentation visuals
- Concept mockups
- Internal documents
- Placeholder content

**Not ideal for:**
- Product photography (real products)
- Testimonial photos (use real people)
- Team photos (use real team)
- News/journalism
- Legal/medical contexts

### The Image Generation Decision

```
Need an image?
    │
    ├─ Is it of your real product/team?
    │   └─ YES → Use photography
    │
    ├─ Need exact specifications?
    │   └─ YES → Consider stock + editing
    │
    ├─ Need unique/creative visual?
    │   └─ YES → AI generation
    │
    └─ Need many variations quickly?
        └─ YES → AI generation
```

### Cost Comparison

| Source | Cost/Image | Speed | Uniqueness | Control |
|--------|-----------|-------|------------|---------|
| Photographer | $200-2000 | Days | High | High |
| Stock photo | $5-50 | Minutes | Low | Low |
| Freelance design | $50-500 | Hours | High | Medium |
| Midjourney | $0.02-0.10 | Seconds | High | Medium |
| DALL-E 3 | $0.04-0.12 | Seconds | High | High |
| Flux Pro | $0.05 | Seconds | High | Medium |
| Stable Diffusion | $0.002-0.02 | Seconds | High | High |

---

## Tools Deep Dive

### Midjourney

**Best for:** Marketing visuals, creative exploration, aesthetic content

**Access:** Discord bot or web interface (alpha)

**Pricing:**
- Basic: $10/month (~200 images)
- Standard: $30/month (~900 images)  
- Pro: $60/month (~1800 images)
- Mega: $120/month (~3600 images)

**Key Commands:**
```
/imagine [prompt] - Generate image
/blend - Combine images
/describe - Get prompt from image
/settings - Adjust preferences
```

**Parameters:**
```
--ar 16:9        # Aspect ratio
--v 6.1          # Version
--style raw      # Less Midjourney styling
--stylize 50     # Stylization level (0-1000)
--chaos 20       # Variation (0-100)
--no [element]   # Exclude elements
--seed [number]  # Reproducibility
--sref [url]     # Style reference
--cref [url]     # Character reference
```

**Workflow for Automation:**
Midjourney lacks a direct API, but you can automate via:
1. Discord bot automation (ToS gray area)
2. Third-party services (costs more)
3. Manual batch generation

### DALL-E 3

**Best for:** Images with text, precise compositions, API automation

**Access:** API (OpenAI) or ChatGPT Plus

**Pricing:**
| Quality | Size | Cost |
|---------|------|------|
| Standard | 1024×1024 | $0.040 |
| Standard | 1024×1792 | $0.080 |
| HD | 1024×1024 | $0.080 |
| HD | 1024×1792 | $0.120 |

**API Example:**
```python
from openai import OpenAI

client = OpenAI()

response = client.images.generate(
    model="dall-e-3",
    prompt="A professional infographic showing...",
    size="1024x1024",
    quality="hd",
    n=1
)

image_url = response.data[0].url
revised_prompt = response.data[0].revised_prompt
```

**Key Features:**
- Excellent text rendering
- Prompt rewriting (enhances your prompt)
- Consistent API access
- Vision API for editing context

**Limitations:**
- Cannot generate multiple images per call
- No style references
- Less artistic than Midjourney

### Flux (Black Forest Labs)

**Best for:** Photorealism, speed, API automation

**Models:**
- **Flux Pro:** Best quality ($0.05/image)
- **Flux Dev:** Good quality, open weights
- **Flux Schnell:** Fastest, open weights

**API via Replicate:**
```python
import replicate

output = replicate.run(
    "black-forest-labs/flux-pro",
    input={
        "prompt": "Professional headshot...",
        "aspect_ratio": "1:1",
        "output_format": "png",
        "safety_tolerance": 2
    }
)
```

**API via Together.ai:**
```python
import together

response = together.Images.generate(
    model="black-forest-labs/FLUX.1-schnell",
    prompt="Your prompt here",
    width=1024,
    height=1024,
    n=1
)
```

**Strengths:**
- Exceptional photorealism
- Good at hands/anatomy
- Fast generation
- Multiple API providers
- Open weights for self-hosting

### Stable Diffusion

**Best for:** Custom training, high volume, self-hosting

**Versions:**
- SDXL 1.0 (current recommended)
- SD 3.0 (newest)
- SD 1.5 (legacy, most LoRAs)

**Self-hosting:**
```bash
# Using AUTOMATIC1111
git clone https://github.com/AUTOMATIC1111/stable-diffusion-webui
cd stable-diffusion-webui
./webui.sh
```

**API via Stability.ai:**
```python
import requests

response = requests.post(
    "https://api.stability.ai/v1/generation/stable-diffusion-xl-1024-v1-0/text-to-image",
    headers={
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json",
    },
    json={
        "text_prompts": [{"text": "Your prompt"}],
        "cfg_scale": 7,
        "steps": 30,
        "width": 1024,
        "height": 1024,
    }
)
```

**Customization:**
- **LoRAs:** Style/subject fine-tunes
- **ControlNet:** Pose/depth control
- **Inpainting:** Edit parts of images
- **Upscaling:** Increase resolution

---

## Prompt Engineering

### The Universal Prompt Structure

```
[Subject] + [Action/State] + [Setting] + [Style] + [Technical] + [Mood]
```

**Example:**
```
A professional businesswoman | presenting to a team | 
in a modern glass conference room | corporate photography | 
shot with 50mm lens, soft natural lighting | confident, engaging
```

### Subject Descriptions

**People:**
```
# Basic
A young professional man in his 30s

# Detailed
A confident young professional man in his early 30s, 
wearing a tailored navy suit, short dark hair neatly styled, 
warm smile, Mediterranean features
```

**Products:**
```
# Basic
A smartphone on a desk

# Detailed
A sleek modern smartphone with edge-to-edge display, 
placed at a 45-degree angle on a white marble desk, 
showing a colorful app interface
```

**Scenes:**
```
# Basic
An office

# Detailed
A bright open-plan startup office with floor-to-ceiling 
windows overlooking a city skyline, exposed brick walls, 
modern furniture, plants, collaborative workspace
```

### Style Modifiers

**Photography Styles:**
```
corporate photography
editorial photography
lifestyle photography
product photography
candid photography
portrait photography
documentary style
```

**Art Styles:**
```
digital illustration
minimalist flat design
3D render
isometric illustration
watercolor
line art
pop art
```

**Technical Specs:**
```
shot with Canon EOS R5, 50mm lens
f/1.8 aperture, shallow depth of field
studio lighting, three-point lighting
natural window light
golden hour lighting
soft diffused lighting
high contrast dramatic lighting
8k, ultra detailed
```

**Mood/Atmosphere:**
```
warm and inviting
professional and clean
energetic and dynamic
calm and serene
bold and confident
friendly and approachable
```

### Prompt Templates by Use Case

#### Blog Hero Image
```
[Topic] concept visualization, 
modern minimalist style, 
[primary color] and [secondary color] color scheme, 
abstract geometric elements, 
clean professional look, 
suitable for tech blog header
```

**Example:**
```
AI and automation concept visualization, 
modern minimalist style, 
deep blue and electric purple color scheme, 
abstract geometric elements representing data flow, 
clean professional look, 
suitable for tech blog header,
16:9 aspect ratio
```

#### Social Media Post
```
[Action/Scene] for [topic], 
vibrant engaging style, 
[platform] optimized composition, 
eye-catching colors, 
space for text overlay on [position]
```

#### Product Mockup
```
[Product description] displayed on 
[surface/setting], 
product photography style, 
[lighting type], 
[background description], 
high-end commercial look,
sharp focus on product
```

#### Team/Culture Photo
```
A diverse group of [number] professionals 
[action] in [setting], 
authentic candid moment, 
natural lighting, 
modern office environment, 
inclusive and collaborative atmosphere,
lifestyle photography style
```

### Negative Prompts

For Stable Diffusion and some other models, negative prompts help avoid issues:

```
Standard negative prompt:
blurry, low quality, distorted, deformed, ugly, 
bad anatomy, bad proportions, extra limbs, 
cloned face, disfigured, gross proportions, 
malformed limbs, missing arms, missing legs, 
extra arms, extra legs, fused fingers, 
too many fingers, long neck, watermark, 
signature, text, logo
```

**Specific additions by content type:**

| Content Type | Add to Negative |
|--------------|-----------------|
| People | extra fingers, crossed eyes, weird hands |
| Products | scratches, dust, reflections, artifacts |
| Interiors | cluttered, messy, asymmetrical |
| Food | unappetizing, raw, burnt |

---

## Use Case Workflows

### Blog Featured Images

**Volume:** 4-20 per month
**Style consistency:** High
**Model:** Midjourney or DALL-E 3

**Workflow:**
```
1. BRIEF
   Topic: [Topic]
   Keywords: [SEO keywords]
   Mood: [Desired feeling]
   Colors: [Brand colors if applicable]

2. GENERATE
   Create 4-6 variations
   Test different styles

3. SELECT
   Choose best 1-2 options
   Consider:
   - Readability with text overlay
   - Thumbnail appearance
   - Brand fit

4. POST-PROCESS
   - Resize to blog dimensions
   - Add any text overlays
   - Optimize file size
   - Create thumbnail version

5. STORE
   Save prompt for future reference
   Tag with topic/keywords
```

**Prompt Template:**
```
Create a blog header image for an article about [TOPIC].

Style: Modern, professional, [industry] aesthetic
Colors: [primary] and [accent] with [neutral] backgrounds
Mood: [Informative/Inspiring/Action-oriented]
Elements: [Abstract concepts to visualize]
Avoid: [What not to include]
Aspect ratio: 16:9 (1200x630 for social sharing)
```

### Social Media Graphics

**Volume:** 20-100 per month
**Style consistency:** Very high
**Model:** Midjourney or DALL-E 3

**Batch Generation Workflow:**
```
1. CREATE STYLE GUIDE
   - Define 3-5 recurring visual themes
   - Set color palette
   - Choose consistent elements

2. TEMPLATE PROMPTS
   Theme 1: [Prompt template with {{topic}} variable]
   Theme 2: [Prompt template with {{topic}} variable]
   Theme 3: [Prompt template with {{topic}} variable]

3. BATCH GENERATE
   - Input week's content topics
   - Generate 2-3 per post
   - Rotate through themes

4. POST-PROCESS
   - Add text overlays
   - Add branding elements
   - Resize per platform

5. SCHEDULE
   - Load to scheduling tool
   - Assign to content calendar
```

**Platform Dimensions:**
| Platform | Post | Story | Header |
|----------|------|-------|--------|
| Instagram | 1080x1080 | 1080x1920 | - |
| Facebook | 1200x630 | 1080x1920 | 820x312 |
| Twitter | 1200x675 | - | 1500x500 |
| LinkedIn | 1200x627 | 1080x1920 | 1128x191 |
| Pinterest | 1000x1500 | 1080x1920 | - |

### Ad Creatives

**Volume:** 20-50 per campaign
**Style consistency:** Medium (testing variations)
**Model:** Midjourney, DALL-E 3, or Flux

**Creative Testing Workflow:**
```
1. DEFINE ANGLES
   Angle 1: [Problem-focused]
   Angle 2: [Benefit-focused]
   Angle 3: [Social proof]
   Angle 4: [Lifestyle]

2. GENERATE PER ANGLE
   For each angle:
   - 3-5 image variations
   - Different visual approaches
   - Various compositions

3. PAIR WITH COPY
   - Match images to copy angles
   - Ensure visual-text harmony
   - Check text readability

4. CREATE AD SETS
   - Square (1:1)
   - Portrait (4:5)
   - Story (9:16)

5. LOAD TO ADS MANAGER
   - A/B test images
   - Track performance
   - Kill losers, scale winners
```

### E-commerce Product Images

**Volume:** 10-1000+ per catalog
**Style consistency:** Very high
**Model:** Flux Pro or DALL-E 3

**Note:** Only for products you don't have photos of, mockups, or lifestyle contexts.

**Mockup Workflow:**
```
1. PRODUCT INFO
   - Name
   - Description
   - Target customer
   - Use context

2. SCENE TYPES
   - White background (main)
   - Lifestyle context
   - In-use demonstration
   - Detail shots

3. GENERATE SERIES
   Each product:
   - Main product shot
   - 2-3 lifestyle images
   - Detail/texture shot

4. POST-PROCESS
   - Background removal
   - Color correction
   - Consistency check
   - Add shadows/reflections
```

### Presentation Slides

**Volume:** 10-50 per presentation
**Style consistency:** Very high
**Model:** Midjourney or DALL-E 3

**Workflow:**
```
1. DEFINE VISUAL THEME
   Based on:
   - Company branding
   - Topic/mood
   - Audience

2. CREATE SLIDE TEMPLATES
   - Title slide image
   - Section dividers
   - Concept illustrations
   - Background patterns

3. GENERATE KEY VISUALS
   For each main point:
   - Metaphor/concept visualization
   - Leave space for text
   - Consistent style

4. ASSEMBLE
   - Place in slide deck
   - Add text and data
   - Check visual flow
```

---

## Brand Consistency

### Creating a Visual Identity with AI

**Step 1: Define Brand Elements**
```
BRAND VISUAL BRIEF

Colors:
- Primary: [hex code]
- Secondary: [hex code]
- Accent: [hex code]
- Neutrals: [hex codes]

Style keywords:
- [Modern/Classic/Playful/etc.]
- [Minimal/Detailed/Bold/etc.]
- [Warm/Cool/Neutral/etc.]

Recurring elements:
- [Geometric shapes/Organic forms/etc.]
- [Specific objects/symbols]
- [Lighting preferences]

Avoid:
- [Styles that don't fit]
- [Colors to avoid]
- [Imagery that conflicts]
```

**Step 2: Create Style Reference Library**
```
Collect 10-20 images that represent your brand:
- Existing brand photos
- Aspirational examples
- Mood references
- Texture/pattern samples
```

**Step 3: Develop Master Prompts**

Create reusable prompt templates:

```
Base style prompt (append to all):
", [brand style keywords], [color scheme description], 
[lighting style], consistent with modern tech brand aesthetic"
```

**Step 4: Use Style References**

Midjourney:
```
/imagine [prompt] --sref [URL of brand image]
```

Consistent character:
```
/imagine [prompt] --cref [URL of character reference]
```

### Maintaining Consistency at Scale

**1. Prompt Library**

Maintain a library of working prompts:

```yaml
# prompts.yaml
blog_headers:
  tech:
    base: "Abstract technology concept, flowing data visualization..."
    variations:
      - "with neural network patterns"
      - "with cloud computing elements"
      - "with AI/machine learning symbolism"
  
  business:
    base: "Professional business concept, clean minimal style..."
    variations:
      - "with growth chart elements"
      - "with collaboration symbolism"
      - "with strategy/chess metaphor"

social:
  instagram:
    base: "Vibrant [topic] visualization, Instagram-worthy..."
  linkedin:
    base: "Professional [topic] concept, LinkedIn appropriate..."
```

**2. Seed Management**

For reproducibility (Midjourney/SD):
```
Keep record of:
- Prompt
- Seed number
- Parameters used
- Result rating
```

**3. Quality Checklist**

Before publishing:
- [ ] Colors match brand palette
- [ ] Style consistent with recent posts
- [ ] No off-brand elements
- [ ] Resolution appropriate
- [ ] File size optimized

---

## Production Pipelines

### Automated Image Pipeline

**n8n Workflow:**
```
Webhook (content request)
  → Extract requirements
  → Select prompt template
  → Call image API (DALL-E/Flux)
  → Save to cloud storage
  → Resize to needed dimensions
  → Optimize file size
  → Deliver to destination (CMS/social scheduler)
  → Log metadata
```

**Code Example (Python):**
```python
import openai
from PIL import Image
import requests
from io import BytesIO

class ImagePipeline:
    def __init__(self, api_key):
        self.client = openai.OpenAI(api_key=api_key)
    
    def generate(self, topic, style="blog_header"):
        prompt = self.build_prompt(topic, style)
        
        response = self.client.images.generate(
            model="dall-e-3",
            prompt=prompt,
            size="1792x1024",
            quality="hd",
            n=1
        )
        
        image_url = response.data[0].url
        return self.process_image(image_url, style)
    
    def build_prompt(self, topic, style):
        templates = {
            "blog_header": f"""
                Professional blog header image for an article about {topic}.
                Modern minimal design, subtle tech aesthetic,
                blue and white color scheme with accent colors,
                clean composition with space for text overlay,
                16:9 aspect ratio, high-end editorial look.
            """,
            "social_post": f"""
                Eye-catching social media image about {topic}.
                Vibrant colors, engaging composition,
                square format, Instagram-worthy aesthetic,
                bold and clear visual concept.
            """
        }
        return templates.get(style, templates["blog_header"])
    
    def process_image(self, url, style):
        # Download
        response = requests.get(url)
        img = Image.open(BytesIO(response.content))
        
        # Resize based on style
        sizes = {
            "blog_header": (1200, 630),
            "social_post": (1080, 1080),
        }
        
        target = sizes.get(style, (1200, 630))
        img = img.resize(target, Image.LANCZOS)
        
        # Save optimized
        output = BytesIO()
        img.save(output, format='JPEG', quality=85, optimize=True)
        
        return output.getvalue()
```

### Batch Generation System

For high-volume needs:

```python
import asyncio
from concurrent.futures import ThreadPoolExecutor

async def batch_generate(topics, max_concurrent=5):
    """Generate images for multiple topics concurrently."""
    semaphore = asyncio.Semaphore(max_concurrent)
    pipeline = ImagePipeline(api_key)
    
    async def generate_one(topic):
        async with semaphore:
            loop = asyncio.get_event_loop()
            with ThreadPoolExecutor() as executor:
                return await loop.run_in_executor(
                    executor,
                    pipeline.generate,
                    topic
                )
    
    tasks = [generate_one(topic) for topic in topics]
    return await asyncio.gather(*tasks)

# Usage
topics = [
    "AI automation",
    "Remote work productivity",
    "SaaS metrics",
    # ... more topics
]

images = asyncio.run(batch_generate(topics))
```

---

## Quality Control

### Automated Quality Checks

```python
def quality_check(image_path):
    """Run automated quality checks on generated image."""
    img = Image.open(image_path)
    
    checks = {
        "resolution": check_resolution(img),
        "aspect_ratio": check_aspect_ratio(img),
        "file_size": check_file_size(image_path),
        "color_profile": check_color_profile(img),
        "sharpness": check_sharpness(img),
    }
    
    passed = all(checks.values())
    return {"passed": passed, "details": checks}

def check_resolution(img, min_width=1200, min_height=630):
    w, h = img.size
    return w >= min_width and h >= min_height

def check_aspect_ratio(img, target=16/9, tolerance=0.1):
    w, h = img.size
    ratio = w / h
    return abs(ratio - target) / target <= tolerance

def check_file_size(path, max_mb=2):
    import os
    size_mb = os.path.getsize(path) / (1024 * 1024)
    return size_mb <= max_mb
```

### Human Review Queue

For important content, add human review:

```yaml
# n8n workflow
Generate Image
  → Quality Check (automated)
  → Pass?
    → Yes: Add to Approval Queue (Slack/email)
    → No: Regenerate or flag
  → Human Approves
    → Yes: Move to Publishing
    → No: Add feedback, regenerate
```

### Common Issues and Fixes

| Issue | Detection | Fix |
|-------|-----------|-----|
| Distorted faces | Manual review | Regenerate with different seed |
| Wrong hands | Manual review | Use inpainting or regenerate |
| Text errors | Automated OCR | Use DALL-E 3 for text |
| Off-brand colors | Color analysis | Post-process color correction |
| Low detail | Visual inspection | Upscale with AI upscaler |
| Artifacts | Edge detection | Inpaint or regenerate |

---

## Legal Considerations

### Usage Rights

**Most AI generators (Midjourney, DALL-E, Flux):**
- You own the output
- Commercial use allowed
- Cannot claim copyright (in most jurisdictions)
- Check specific terms for each platform

**Stable Diffusion (self-hosted):**
- Full ownership of outputs
- No platform restrictions
- Your responsibility for content

### Avoiding IP Issues

**Do NOT generate:**
- Copyrighted characters (Disney, Marvel, etc.)
- Celebrity likenesses without permission
- Trademarked logos or products
- Style that too closely mimics specific artist

**Safe practices:**
```
# Instead of:
"Mickey Mouse in a business suit"

# Use:
"A friendly cartoon mouse character in a business suit,
original design, not resembling any existing characters"
```

### Disclosure Recommendations

| Use Case | Disclosure |
|----------|-----------|
| Marketing images | Not required (most cases) |
| News/journalism | Required |
| Social media | Recommended |
| Product mockups | Clarify "mockup/concept" |
| Art/creative | Consider transparency |

### Stock Photo Replacement

AI images can replace stock photos, but consider:
- Model releases not needed (no real people)
- Can't claim "real" if synthetic
- May need disclosure in some contexts

---

## Summary

### Model Selection Quick Guide

| Need | Best Model |
|------|------------|
| Marketing visuals | Midjourney |
| Images with text | DALL-E 3 |
| Photorealistic | Flux Pro |
| High volume/budget | Stable Diffusion |
| API automation | DALL-E 3 or Flux |
| Consistency/training | Stable Diffusion |

### Cost Optimization

1. **Start with cheapest** - SDXL via API ($0.002)
2. **Upgrade if quality needs** - Flux ($0.05)
3. **Premium for hero content** - Midjourney
4. **Batch similar requests** - Save API calls
5. **Cache and reuse** - Don't regenerate same images

### Next Steps

1. Set up your image generation API
2. Create brand prompt templates
3. Build your production pipeline
4. Establish quality control process
5. Train team on prompt engineering

See [video.md](video.md) for AI video creation →
