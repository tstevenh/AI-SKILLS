# Schema Markup for SEO Content

> Schema markup helps search engines understand your content and can earn you rich results that stand out in SERPs.

## What is Schema Markup?

Schema markup (structured data) is code you add to your pages that explicitly tells search engines what your content is about. It's a standardized vocabulary from Schema.org that Google, Bing, and other search engines understand.

**Example**: Instead of Google guessing your page is a recipe, schema tells it:
- This is a recipe
- It takes 30 minutes to cook
- It has 4.5 stars from 200 reviews
- It yields 4 servings

---

## Why Schema Matters

### Rich Results

Schema can earn you enhanced search listings:

| Rich Result Type | Schema Type | Visual Enhancement |
|-----------------|-------------|-------------------|
| Review stars | Review, AggregateRating | ⭐⭐⭐⭐⭐ (4.5) |
| FAQ dropdowns | FAQPage | Expandable Q&A |
| How-to steps | HowTo | Step-by-step cards |
| Recipe cards | Recipe | Image, time, rating |
| Product info | Product | Price, availability |
| Event listings | Event | Date, location |
| Article info | Article | Publish date, author |

### Performance Impact

Google case studies show:
- **Rotten Tomatoes**: 25% higher CTR with schema
- **Food Network**: 35% increase in visits
- **Nestlé**: 82% higher CTR on rich result pages

### Better Understanding

Even without rich results, schema helps Google understand:
- Content type and structure
- Entity relationships
- Author and publisher information
- Date and freshness signals

---

## Schema Format: JSON-LD

Google recommends **JSON-LD** format. It goes in a `<script>` tag, usually in the `<head>`.

**Basic structure**:
```html
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "Your Article Title",
  "author": {
    "@type": "Person",
    "name": "Author Name"
  }
}
</script>
```

---

## Schema Types for Content

### Article Schema

**Use for**: Blog posts, news articles, editorial content

```json
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "SEO Copywriting: The Complete Guide",
  "description": "Learn how to write content that ranks on Google and converts readers into customers.",
  "image": "https://yoursite.com/images/seo-copywriting.jpg",
  "author": {
    "@type": "Person",
    "name": "Jane Smith",
    "url": "https://yoursite.com/author/jane-smith"
  },
  "publisher": {
    "@type": "Organization",
    "name": "Your Site Name",
    "logo": {
      "@type": "ImageObject",
      "url": "https://yoursite.com/logo.png"
    }
  },
  "datePublished": "2026-02-01",
  "dateModified": "2026-02-04"
}
```

**Key properties**:
- `headline`: Article title (required)
- `author`: Who wrote it (required)
- `datePublished`: When published
- `dateModified`: Last update (signals freshness)
- `image`: Featured image

### FAQPage Schema

**Use for**: FAQ sections (can earn expandable FAQ rich results)

```json
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "What is SEO copywriting?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "SEO copywriting is the practice of creating keyword-optimized content designed to rank in search engines while engaging human readers."
      }
    },
    {
      "@type": "Question",
      "name": "How long should a blog post be?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "There's no ideal length. Write until you've fully covered the topic. Most successful blog posts are 1,500-3,000 words."
      }
    }
  ]
}
```

**Requirements**:
- Questions must be visible on the page
- Answers must match the on-page content
- Don't use for promotional content only

### HowTo Schema

**Use for**: Step-by-step tutorials and guides

```json
{
  "@context": "https://schema.org",
  "@type": "HowTo",
  "name": "How to Write an SEO-Optimized Blog Post",
  "description": "A step-by-step guide to writing blog posts that rank on Google.",
  "totalTime": "PT2H",
  "step": [
    {
      "@type": "HowToStep",
      "name": "Research your keyword",
      "text": "Use a keyword research tool to find a topic with search volume and manageable competition.",
      "url": "https://yoursite.com/guide#step1"
    },
    {
      "@type": "HowToStep",
      "name": "Analyze search intent",
      "text": "Search your keyword and analyze the top 10 results to understand what format and content Google prefers.",
      "url": "https://yoursite.com/guide#step2"
    },
    {
      "@type": "HowToStep",
      "name": "Create an outline",
      "text": "Structure your content with H2s and H3s that cover the topic comprehensively.",
      "url": "https://yoursite.com/guide#step3"
    }
  ]
}
```

**Key properties**:
- `totalTime`: Estimated time (ISO 8601 format)
- `step`: Array of HowToStep objects
- Can include `tool` and `supply` if relevant

### Product Schema

**Use for**: Product pages, reviews, comparisons

```json
{
  "@context": "https://schema.org",
  "@type": "Product",
  "name": "LocalRank.so",
  "description": "Local SEO rank tracking and citation management software.",
  "brand": {
    "@type": "Brand",
    "name": "LocalRank"
  },
  "offers": {
    "@type": "Offer",
    "price": "49",
    "priceCurrency": "USD",
    "availability": "https://schema.org/InStock"
  },
  "aggregateRating": {
    "@type": "AggregateRating",
    "ratingValue": "4.8",
    "reviewCount": "127"
  }
}
```

### Review Schema

**Use for**: Product reviews, software reviews

```json
{
  "@context": "https://schema.org",
  "@type": "Review",
  "itemReviewed": {
    "@type": "SoftwareApplication",
    "name": "Ahrefs",
    "applicationCategory": "SEO Tool"
  },
  "reviewRating": {
    "@type": "Rating",
    "ratingValue": "4.8",
    "bestRating": "5"
  },
  "author": {
    "@type": "Person",
    "name": "Jane Smith"
  },
  "reviewBody": "Ahrefs is the most comprehensive SEO tool I've used..."
}
```

### LocalBusiness Schema

**Use for**: Local business pages (relevant for LocalRank.so content)

```json
{
  "@context": "https://schema.org",
  "@type": "LocalBusiness",
  "name": "Business Name",
  "address": {
    "@type": "PostalAddress",
    "streetAddress": "123 Main St",
    "addressLocality": "Vancouver",
    "addressRegion": "BC",
    "postalCode": "V6B 1A1",
    "addressCountry": "CA"
  },
  "telephone": "+1-604-555-0123",
  "openingHours": "Mo-Fr 09:00-17:00",
  "geo": {
    "@type": "GeoCoordinates",
    "latitude": "49.2827",
    "longitude": "-123.1207"
  }
}
```

### Organization Schema

**Use for**: Company/brand pages

```json
{
  "@context": "https://schema.org",
  "@type": "Organization",
  "name": "Indexsy",
  "url": "https://indexsy.com",
  "logo": "https://indexsy.com/logo.png",
  "sameAs": [
    "https://twitter.com/indexsy",
    "https://linkedin.com/company/indexsy"
  ],
  "contactPoint": {
    "@type": "ContactPoint",
    "telephone": "+1-XXX-XXX-XXXX",
    "contactType": "customer service"
  }
}
```

### BreadcrumbList Schema

**Use for**: Navigation breadcrumbs

```json
{
  "@context": "https://schema.org",
  "@type": "BreadcrumbList",
  "itemListElement": [
    {
      "@type": "ListItem",
      "position": 1,
      "name": "Home",
      "item": "https://yoursite.com"
    },
    {
      "@type": "ListItem",
      "position": 2,
      "name": "Blog",
      "item": "https://yoursite.com/blog"
    },
    {
      "@type": "ListItem",
      "position": 3,
      "name": "SEO Copywriting Guide",
      "item": "https://yoursite.com/blog/seo-copywriting"
    }
  ]
}
```

---

## Schema Implementation

### Method 1: Manual JSON-LD

Add directly to your HTML:

```html
<head>
  <script type="application/ld+json">
  {
    "@context": "https://schema.org",
    "@type": "Article",
    ...
  }
  </script>
</head>
```

### Method 2: WordPress Plugins

**Popular options**:
- Yoast SEO (basic schema)
- Rank Math (comprehensive schema)
- Schema Pro (dedicated schema plugin)
- All in One Schema Rich Snippets

### Method 3: CMS Built-in

Many modern CMS platforms have schema built in:
- Shopify (Product schema)
- Webflow (basic schema options)
- Wix (automatic schema)

### Method 4: Tag Manager

Google Tag Manager can inject JSON-LD dynamically:
1. Create Custom HTML tag
2. Add your JSON-LD script
3. Set triggers for relevant pages

---

## Testing Schema

### Google Rich Results Test

**URL**: https://search.google.com/test/rich-results

- Paste URL or code
- Shows which rich results are eligible
- Identifies errors and warnings

### Schema.org Validator

**URL**: https://validator.schema.org/

- Validates against Schema.org standards
- More technical, less Google-specific

### Google Search Console

After deployment:
1. Go to Enhancements section
2. Check for errors by schema type
3. Monitor rich result impressions

---

## Schema Best Practices

### Do's

✅ **Use JSON-LD format** (Google's preferred)

✅ **Match visible content** (schema must reflect on-page content)

✅ **Include all required properties** (check Google's docs)

✅ **Add recommended properties** (more data = better rich results)

✅ **Keep it accurate** (prices, ratings, availability must be current)

✅ **Test before deploying** (use Rich Results Test)

✅ **Monitor in Search Console** (check for errors)

### Don'ts

❌ **Don't add schema for content not on page** (Google will ignore or penalize)

❌ **Don't fake reviews or ratings** (against guidelines)

❌ **Don't use schema for hidden content** (must be user-visible)

❌ **Don't mark up irrelevant content** (don't add Recipe schema to blog posts)

❌ **Don't duplicate schema** (one instance per entity)

---

## Schema Priority for Content Types

### Blog Posts

**Must have**:
- Article schema
- BreadcrumbList

**Should have**:
- FAQPage (if FAQ section exists)
- HowTo (if step-by-step content)

**Nice to have**:
- Author Person schema
- Organization schema (publisher)

### Product Reviews

**Must have**:
- Review schema
- Product schema

**Should have**:
- AggregateRating (if multiple reviews)
- FAQPage

### Landing Pages

**Must have**:
- Organization or Product schema
- BreadcrumbList

**Should have**:
- FAQPage
- Service schema (if applicable)

### Local Business Content

**Must have**:
- LocalBusiness schema
- Address and contact info

**Should have**:
- OpeningHoursSpecification
- GeoCoordinates
- Review/AggregateRating

---

## Schema Templates

### Blog Post Template

```json
{
  "@context": "https://schema.org",
  "@type": "Article",
  "mainEntityOfPage": {
    "@type": "WebPage",
    "@id": "[PAGE_URL]"
  },
  "headline": "[ARTICLE_TITLE]",
  "description": "[META_DESCRIPTION]",
  "image": "[FEATURED_IMAGE_URL]",
  "author": {
    "@type": "Person",
    "name": "[AUTHOR_NAME]",
    "url": "[AUTHOR_PAGE_URL]"
  },
  "publisher": {
    "@type": "Organization",
    "name": "[SITE_NAME]",
    "logo": {
      "@type": "ImageObject",
      "url": "[LOGO_URL]"
    }
  },
  "datePublished": "[YYYY-MM-DD]",
  "dateModified": "[YYYY-MM-DD]"
}
```

### FAQ Section Template

```json
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "[QUESTION_1]",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "[ANSWER_1]"
      }
    },
    {
      "@type": "Question",
      "name": "[QUESTION_2]",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "[ANSWER_2]"
      }
    }
  ]
}
```

### How-To Template

```json
{
  "@context": "https://schema.org",
  "@type": "HowTo",
  "name": "[HOW_TO_TITLE]",
  "description": "[BRIEF_DESCRIPTION]",
  "totalTime": "PT[X]H[Y]M",
  "step": [
    {
      "@type": "HowToStep",
      "name": "[STEP_1_NAME]",
      "text": "[STEP_1_DESCRIPTION]",
      "url": "[PAGE_URL]#step1"
    },
    {
      "@type": "HowToStep",
      "name": "[STEP_2_NAME]",
      "text": "[STEP_2_DESCRIPTION]",
      "url": "[PAGE_URL]#step2"
    }
  ]
}
```

---

## Combining Multiple Schema Types

You can include multiple schema types on one page:

```html
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@graph": [
    {
      "@type": "Article",
      "headline": "How to Write SEO Content",
      ...
    },
    {
      "@type": "BreadcrumbList",
      "itemListElement": [...]
    },
    {
      "@type": "FAQPage",
      "mainEntity": [...]
    }
  ]
}
</script>
```

The `@graph` array lets you include multiple entities in one script tag.

---

## Measuring Schema Impact

### Track Rich Results

In Search Console:
1. Performance report
2. Filter by Search appearance
3. Compare CTR for rich vs. non-rich results

### Key Metrics

- **Rich result impressions**: How often your rich results show
- **Rich result CTR**: Click-through rate on rich results
- **Coverage**: How many pages have valid schema
- **Errors**: Schema validation issues to fix

---

## Sources

- Google Search Central: Structured Data Documentation
- Schema.org: Full vocabulary reference
- Google: Rich Results Gallery
- Google Case Studies: Schema impact on CTR
