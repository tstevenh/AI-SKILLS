# Ghost: Complete Platform Guide

Ghost is the open-source publishing platform that gives creators complete control over their newsletter and website. It's the power-user choice for publishers who need customization and ownership.

---

## Platform Overview

### What Ghost Is

Ghost is a professional publishing platform designed for:
- Publishers wanting full customization
- Technical teams who value ownership
- Media brands building comprehensive sites
- Creators who want complete control

### History and Positioning

Founded in 2013 by John O'Nolan through a Kickstarter campaign, Ghost was created as a modern, open-source alternative to WordPress. It evolved from pure blogging into a full membership/newsletter platform.

**Key Philosophy:**
- Open source and transparent
- Publishing-first design
- Full ownership of everything
- No platform lock-in

### Ghost Pro vs. Self-Hosted

**Ghost(Pro) - Managed Hosting:**
- Ghost runs everything
- Monthly subscription
- Automatic updates
- Managed deliverability
- Technical support

**Self-Hosted:**
- You run on your own server
- Software is free
- Full control
- Technical responsibility
- No licensing fees

---

## Pricing Deep Dive (2026)

### Ghost(Pro) Plans

| Plan | Price | Members | Staff Users | Key Features |
|------|-------|---------|-------------|--------------|
| Starter | $18/mo | 1,000 | 1 | Basic newsletter + website |
| Publisher | $29/mo | 1,000 | 3 | Paid subs, custom themes |
| Business | $199/mo | 10,000 | 15 | Priority support, higher limits |
| Custom | Custom | Unlimited | Unlimited | Dedicated IP, SLA |

### Member Scaling (Publisher+)

| Members | Publisher | Business |
|---------|-----------|----------|
| 1,000 | $29/mo | $199/mo |
| 5,000 | $79/mo | $199/mo |
| 10,000 | $129/mo | $199/mo |
| 25,000 | $199/mo | $299/mo |
| 50,000 | $299/mo | $399/mo |
| 100,000 | $499/mo | $599/mo |

### Self-Hosted Costs

| Component | Cost |
|-----------|------|
| Ghost software | Free |
| Server (DigitalOcean/AWS) | $10-50/mo |
| Email sending (Mailgun) | $35-100+/mo |
| Custom domain | $12-50/yr |
| SSL certificate | Free (Let's Encrypt) |
| Your time | Priceless 😅 |

**Total self-hosted:** $50-150/mo + technical overhead

### Ghost Economics

**Key Advantage:** 0% take rate on subscriptions

| Revenue | Ghost Takes | You Keep |
|---------|-------------|----------|
| Any amount | $0 | 100% - Stripe fees |

Compare to Substack (10%) at scale:
- $10k/mo revenue: Save $1,000/mo vs. Substack
- $50k/mo revenue: Save $5,000/mo vs. Substack

---

## Core Features

### The Editor

**Builder Type:** Rich, modern editor with cards

**Strengths:**
- Beautiful writing experience
- Powerful content cards
- Clean design
- Flexible layouts

**Content Cards:**
- Markdown
- Images (with galleries)
- Videos
- Audio
- Embeds (Twitter, YouTube, etc.)
- Code blocks
- Bookmarks (link previews)
- Products
- Call-to-action buttons
- Toggle (expandable)
- NFT (Web3)
- Files
- Header cards
- Button cards

**Email-Specific Features:**
- Email-only content sections
- Personalization tokens
- Public/member/paid visibility
- Preview for different member types

### Website and CMS

Ghost doubles as a full website platform.

**Website Features:**
- Custom themes (or build your own)
- Custom pages
- Navigation control
- SEO optimization
- Code injection
- Integrations

**CMS Capabilities:**
- Authors and contributors
- Tags and categories
- Featured posts
- Scheduling
- Custom post types

### Themes

**Official Marketplace:**
- Free themes included
- Premium themes available
- Third-party marketplaces

**Customization Options:**
| Level | What You Can Do |
|-------|-----------------|
| Basic | Theme selection, colors, logo |
| Intermediate | Code injection, custom CSS |
| Advanced | Full theme development |
| Expert | Custom integrations, API |

**Theme Development:**
- Handlebars templating
- Full HTML/CSS control
- JavaScript support
- API access
- Complete design freedom

---

## Membership Features

### Membership Tiers

**Built-in Options:**
- Free members
- Paid members
- Multiple paid tiers
- Complimentary access

**Tier Configuration:**
| Tier Element | Options |
|--------------|---------|
| Name | Custom |
| Price | Any amount |
| Billing | Monthly, yearly, or both |
| Benefits | Custom description |
| Trial | Optional free trial |

### Content Access Control

**Visibility Options:**
- Public (anyone)
- Members only (free + paid)
- Paid members only
- Specific tier only

**Post-Level Control:**
- Each post can have different visibility
- Mix free and paid in same publication
- Drip content over time (with workarounds)

### Member Portal

**What Members Get:**
- Account management
- Subscription management
- Email preferences
- Payment method updates
- Cancel/upgrade options

### Offers and Discounts

**Capabilities:**
- Percentage discounts
- Fixed discounts
- Limited-time offers
- Special pricing pages
- Unique URLs per offer

---

## Email Newsletter Features

### Sending Newsletters

**Options:**
- Automatic send on publish
- Schedule for later
- Email-only posts (not on website)
- Selective sending (not all posts)

**Customization:**
- Header image
- Custom footer
- Personalization (name, etc.)
- Segment targeting

### Multiple Newsletters

**Ghost Supports:**
- Multiple newsletter types
- Subscribers choose which to receive
- Different send frequencies
- Different content types

**Example Setup:**
| Newsletter | Frequency | Content |
|------------|-----------|---------|
| Weekly Digest | Weekly | Main content |
| Breaking News | As needed | Updates |
| Premium Insights | Weekly | Paid only |

### Email Design

**Options:**
- Default minimal template
- Custom email templates
- Theme-based emails
- HTML customization (advanced)

### Deliverability

**Ghost(Pro) includes:**
- Managed deliverability
- Reputation monitoring
- Bounce handling
- Complaint management

**Self-Hosted requires:**
- Your own email provider (Mailgun recommended)
- SPF/DKIM/DMARC setup
- Reputation management
- More technical work

---

## Integrations

### Native Integrations

**Built-in:**
| Category | Options |
|----------|---------|
| Analytics | Google Analytics, Plausible, Fathom |
| Comments | Ghost comments, Disqus, Commento |
| CRM | Mailchimp, ConvertKit (partial sync) |
| E-commerce | Shopify |
| Social | Twitter cards, Facebook |
| Automation | Zapier, Make |

### API Access

**Content API (Public):**
- Read posts and pages
- Access public content
- Build custom frontends
- Create integrations

**Admin API (Private):**
- Create/edit content
- Manage members
- Send newsletters
- Full control

### Webhooks

**Supported Events:**
- Post published/updated/deleted
- Member created/updated/deleted
- Subscription created/updated/deleted
- Page events

### Zapier Integration

**Common Automations:**
- New member → Add to CRM
- New post → Tweet
- New paid subscriber → Welcome email
- Cancelled → Win-back sequence

---

## Analytics

### Built-in Analytics

**Post Level:**
- Email opens
- Click rates
- Member conversions
- Engagement over time

**Publication Level:**
- Total members (free + paid)
- MRR (monthly recurring revenue)
- Growth trends
- Retention data

**Advanced Analytics (Business+):**
- Deeper engagement data
- Attribution
- Source tracking

### Third-Party Analytics

Ghost supports full analytics integration:
- Google Analytics
- Plausible (privacy-focused)
- Fathom
- Custom scripts

---

## Self-Hosting Deep Dive

### Why Self-Host?

**Pros:**
- Complete ownership
- No monthly platform fees
- Full customization
- Data sovereignty
- No vendor lock-in

**Cons:**
- Technical responsibility
- Maintenance time
- Security management
- Deliverability challenges
- Scaling complexity

### Technical Requirements

**Server:**
- Linux (Ubuntu recommended)
- 2GB RAM minimum
- SSD storage
- Node.js support

**Recommended Providers:**
- DigitalOcean ($24-48/mo for production)
- AWS Lightsail
- Linode
- Vultr

### Self-Hosting Setup

**Basic Steps:**
1. Provision server
2. Install Ghost CLI
3. Configure with your domain
4. Set up SSL
5. Configure email provider
6. Set up backups
7. Configure CDN (optional)

**Email Provider Options:**
| Provider | Starting Cost | Notes |
|----------|--------------|-------|
| Mailgun | $35/mo | Ghost recommended |
| Amazon SES | Pay per email | Cheap at scale |
| Postmark | $15/mo | Good deliverability |
| SendGrid | $20/mo | Popular choice |

### Maintenance Requirements

**Regular Tasks:**
- Update Ghost (monthly-ish)
- Security patches
- Database backups
- Monitor uptime
- Check email deliverability

**Time Investment:** 2-5 hours/month for competent admin

---

## Who Ghost Is Best For

### Ideal Users

✅ **Technical publishers**
- Full customization
- Own your infrastructure
- Build exactly what you want

✅ **Media brands and publications**
- Professional appearance
- Multiple authors
- Complex site needs

✅ **Membership-focused businesses**
- 0% take rate
- Custom tiers
- Premium experience

✅ **SEO-focused publishers**
- Full website capabilities
- Custom optimization
- Content marketing integration

### Not Ideal For

❌ **Non-technical creators**
- Steeper learning curve
- Customization requires skill
- More decisions to make

❌ **Growth-focused operators**
- Limited built-in growth tools
- No referral program
- No ad network

❌ **Quick launchers**
- More setup than Substack
- Theme selection/customization
- Configuration overhead

❌ **Budget-conscious beginners**
- Ghost(Pro) more expensive
- Self-hosting has hidden costs
- Not free like Beehiiv/Substack

---

## Migration to Ghost

### From Substack

**Supported:**
- Full content import
- Subscriber import
- Paid subscriber migration (Stripe)

**Process:**
1. Export from Substack
2. Import content to Ghost
3. Import subscribers
4. Migrate Stripe subscriptions
5. Set up redirects
6. Communicate with audience

### From WordPress

**Supported:**
- Content import
- Author mapping
- Category/tag mapping

**Note:** Ghost isn't WordPress. Some features won't translate directly.

### From Beehiiv/Kit

**Manual Process:**
1. Export subscriber CSV
2. Export content
3. Import to Ghost
4. Recreate design
5. Rebuild automations (limited in Ghost)

---

## Ghost Tips and Best Practices

### Quick Wins

1. **Choose the right theme** - First impressions matter
2. **Set up multiple tiers** - Give options
3. **Use the API** - Extend functionality
4. **Optimize for SEO** - Ghost is great for this
5. **Set up redirects** - Protect existing links

### Advanced Tactics

1. **Custom theme development** - Stand out completely
2. **Headless Ghost** - Use as backend only
3. **Membership tiers strategy** - Tiered value
4. **Integration workflows** - Automate everything
5. **Content API for distribution** - Syndicate widely

### Common Mistakes

1. **Over-customizing early** - Get basics right first
2. **Ignoring mobile** - Test themes on mobile
3. **Skipping SEO basics** - Missed opportunity
4. **Complex tier structures** - Keep it simple
5. **Neglecting email design** - It matters

---

## Ghost vs. Alternatives Summary

| Factor | Ghost | Beehiiv | Kit | Substack |
|--------|-------|---------|-----|----------|
| Customization | ⭐⭐⭐⭐⭐ | ⭐⭐⭐ | ⭐⭐⭐ | ⭐⭐ |
| Website/SEO | ⭐⭐⭐⭐⭐ | ⭐⭐⭐ | ⭐⭐ | ⭐⭐⭐ |
| Growth tools | ⭐⭐ | ⭐⭐⭐⭐⭐ | ⭐⭐⭐ | ⭐⭐⭐ |
| Ease of use | ⭐⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ |
| Economics | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ | ⭐⭐⭐ | ⭐⭐⭐ |
| Ownership | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐⭐ |

**Bottom Line:** Ghost is the power-user platform for publishers who want complete control, full customization, and true ownership. The trade-off is complexity—you need technical capability (or budget for it) to maximize Ghost's potential. If you want simplicity and built-in growth tools, look elsewhere.

---

## The Ghost Decision Framework

**Choose Ghost if:**
- You want complete customization
- You're technical (or have technical team)
- You want 0% take rate
- You need a full website + newsletter
- You value ownership and control

**Choose alternatives if:**
- You want simplicity
- Growth tools are priority
- You're non-technical
- You need built-in monetization marketplace
- You want network discovery effects
