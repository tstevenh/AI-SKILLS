# Skool: Complete Platform Deep Dive

## Platform Overview

Skool is a community platform founded in 2019 by Sam Ovens (CEO) and Daniel Kang (CTO), with Alex Hormozi partnering in 2024 to create The Skool Games. Based in Los Angeles with approximately 30 employees, Skool has positioned itself as the simplest, most streamlined community platform for creators, coaches, and course sellers.

### Core Philosophy

Skool's philosophy centers on simplicity and all-in-one functionality. Rather than offering extensive customization options, Skool provides an opinionated, focused experience that works well for most community use cases without requiring technical expertise or third-party integrations.

**Key Differentiators**:
- All-in-one platform (community + courses + calendar + gamification)
- Simplest setup among major platforms (under 30 minutes)
- Built-in gamification with points and leaderboards
- Mobile-first design
- Lowest transaction fees in the industry (2.9% on Pro plan)
- Discover page for organic community discovery

### Target Audience

Skool is ideal for:
- Course creators wanting community engagement
- Coaches running group programs
- Experts monetizing knowledge
- Entrepreneurs building paid communities
- Creators who value simplicity over customization

Skool is NOT ideal for:
- Large enterprises needing custom integrations
- Tech communities wanting extensive bot/automation capabilities
- Organizations requiring SSO or advanced security
- Brands needing heavy customization/white-labeling
- Free communities (Skool requires paid plan for hosts)

---

## Features Walkthrough

### 1. Community Features

**Discussion Feed**
The heart of Skool is its discussion feed—a clean, Facebook-like experience where members post, comment, and engage. Features include:

- Text posts with rich formatting
- Image attachments
- Video embeds (YouTube, Vimeo, Loom)
- GIF support
- Polls
- Post categories for organization
- Pinned posts
- Post sorting (trending, recent, following)
- @mentions
- Likes and comments

**Categories**
Organize discussions with custom categories. Each category can be:
- Named and described
- Given a unique emoji
- Set with posting permissions (all members, admins only)
- Used to filter the feed

**Best Practice Categories**:
```
📢 Announcements (admin only)
👋 Introductions (all members)
🎯 Wins & Celebrations
❓ Questions & Support
💡 Tips & Resources
🗣️ General Discussion
📚 Course Discussion
```

**Member Directory**
Browse all community members with:
- Profile photos
- Bio/description
- Points and level
- Join date
- Direct message capability

**Direct Messaging**
One-on-one conversations between members:
- Text messages
- Image sharing
- Notification controls
- Message history

### 2. Course Features (Classroom)

Skool includes a built-in course hosting platform called "Classroom" that allows you to:

**Course Structure**:
```
Classroom
├── Module 1: Getting Started
│   ├── Lesson 1.1: Welcome Video
│   ├── Lesson 1.2: Setting Up
│   └── Lesson 1.3: Your First Steps
├── Module 2: Core Training
│   ├── Lesson 2.1: Fundamentals
│   └── ...
└── Module 3: Advanced Topics
    └── ...
```

**Lesson Types**:
- Video lessons (upload directly or embed)
- Text/article lessons
- PDF attachments
- Audio files
- Mixed media lessons

**Course Features**:
- Progress tracking
- Completion certificates (coming)
- Drip content (timed release)
- Sequential unlocking (optional)
- Course-specific discussions
- Comments on lessons

**Video Hosting**:
Skool provides unlimited video hosting with:
- No storage limits
- Adaptive streaming quality
- Mobile optimization
- Download prevention
- Chapter markers

### 3. Calendar & Events

**Event Types**:
- Live video calls (integrated video or Zoom link)
- In-person meetups
- Workshops
- AMAs
- Office hours

**Calendar Features**:
- Monthly calendar view
- Timezone conversion
- RSVP tracking
- Event reminders
- Recurring events
- Event descriptions and attachments
- Post-event recordings

**Live Streaming**:
Skool includes built-in live streaming:
- No third-party tools needed
- Screen sharing
- Chat integration
- Recording capability
- Unlimited viewers (on paid plans)

### 4. Gamification System

Skool's gamification is one of its most distinctive features, designed to drive engagement through game mechanics.

**Points System**:
Members earn points for:
- Posting (varies by category)
- Commenting
- Receiving likes
- Course completion
- Event attendance
- Logging in daily

**Point Values** (customizable):
```
Default Point Values:
- Creating a post: +2 points
- Commenting: +1 point
- Receiving a like: +1 point
- Daily login: +1 point
- Completing a lesson: +2 points
```

**Levels**:
Members progress through levels based on point accumulation:
```
Level 1: 0-99 points (New Member)
Level 2: 100-249 points
Level 3: 250-499 points
Level 4: 500-999 points
Level 5: 1,000-1,999 points
Level 6: 2,000-3,999 points
Level 7: 4,000-7,999 points
Level 8: 8,000-15,999 points
Level 9: 16,000+ points (Legend)
```

**Leaderboards**:
- Weekly leaderboard (resets each week)
- Monthly leaderboard
- All-time leaderboard
- Visible to all members
- Creates healthy competition

**Unlockable Content**:
Lock content behind level requirements:
- Certain course modules require Level 3
- Exclusive category requires Level 5
- Direct messaging requires Level 2

**Gamification Best Practices**:
1. Set meaningful unlock thresholds
2. Celebrate level-ups publicly
3. Reference leaderboard in calls
4. Give prizes for top contributors
5. Balance points to reward quality, not spam

### 5. Monetization Features

**Subscription Options**:
- Monthly subscriptions
- Annual subscriptions
- One-time payments (lifetime access)
- Free communities (but host still pays Skool)

**Payment Processing**:
- Stripe integration
- Automatic billing
- Failed payment handling
- Member management
- Revenue reporting

**Transaction Fees**:
```
Hobby Plan ($9/month): 10% transaction fee
Pro Plan ($99/month): 2.9% transaction fee only (lowest in industry)

Comparison:
- Discord: 10%
- Patreon: 5-12%
- Circle: 0.5-7%
- Mighty Networks: 0.5-2%
```

**Pricing Flexibility**:
- Custom price points
- Discount codes
- Trial periods
- Payment plans
- Currency support (via Stripe)

### 6. Discovery (Skool Discover)

Unique to Skool is the "Discover" feature—a marketplace of public communities:

**How It Works**:
- Communities can opt into being discoverable
- Listed by category, popularity, activity
- Members can browse and join directly
- Free organic traffic for community owners

**Discovery Categories**:
- Business
- Health & Fitness
- Personal Development
- Money & Finance
- Relationships
- Hobbies & Interests
- And more...

**Discovery Optimization**:
To rank well on Discover:
1. Complete community profile
2. High engagement rate
3. Active posting
4. Good member retention
5. Compelling description

### 7. Admin & Analytics

**Admin Features**:
- Member management (add, remove, ban)
- Role management (admin, moderator, member)
- Content moderation
- Bulk actions
- Export member data
- Email all members

**Analytics Dashboard**:
```
Key Metrics:
- Total members
- New members (daily/weekly/monthly)
- Active members
- Posts and comments
- Course progress
- Revenue (MRR, churn)
- Engagement trends
```

---

## Pricing and Fees

### Current Pricing (2024-2026)

**Hobby Plan: $9/month**
- All features included
- Unlimited members
- Unlimited video hosting
- Unlimited live streaming
- 10% transaction fee on payments
- Basic analytics
- Skool branding visible
- Listed in Discover (optional)

**Pro Plan: $99/month**
- Everything in Hobby
- 2.9% transaction fee (credit card processing only)
- Hide suggested communities
- Advanced analytics
- Custom URL
- Priority support
- Remove some Skool branding

**Per-Member Costs**: None—flat monthly fee regardless of community size

**Total Cost Examples**:
```
100 members at $49/month = $4,900 revenue
Hobby Plan: $9 + ($4,900 × 10%) = $499/month to Skool
Pro Plan: $99 + ($4,900 × 2.9%) = $241/month to Skool

500 members at $49/month = $24,500 revenue
Hobby Plan: $9 + ($24,500 × 10%) = $2,459/month to Skool
Pro Plan: $99 + ($24,500 × 2.9%) = $810/month to Skool

Breakeven: ~$900/month revenue (switch from Hobby to Pro)
```

### Fee Comparison

| Platform | Monthly Fee | Transaction Fee | 500 members @ $49 |
|----------|-------------|-----------------|-------------------|
| Skool Hobby | $9 | 10% | $2,459/month |
| Skool Pro | $99 | 2.9% | $810/month |
| Circle Pro | $89 | 4% | $1,069/month |
| Mighty Scale | $179 | 1% | $424/month |
| Discord | Free | 10% | $2,450/month |

---

## Setup Guide

### Step 1: Create Your Community

1. Go to skool.com and sign up
2. Click "Create Community"
3. Enter community name
4. Choose category
5. Write description (important for Discover)
6. Upload community photo and cover image

**Naming Best Practices**:
- Clear and descriptive
- Include niche/topic
- Avoid generic names
- Consider SEO (people search on Discover)

### Step 2: Configure Settings

**General Settings**:
- Community URL (choose carefully—can't change easily)
- Privacy (public or private)
- Discover visibility
- Currency and pricing

**Membership Settings**:
- Access level (free or paid)
- Price and billing cycle
- Trial period (if any)
- Welcome message

### Step 3: Set Up Categories

Create 5-8 categories to organize discussions:

```
Recommended Structure:
1. 📢 Announcements - Admin-only posting
2. 👋 Introductions - All members, encourage new posts
3. 🎯 Wins - Celebrate member achievements
4. ❓ Questions - Support and Q&A
5. 💡 Resources - Tips, tools, links
6. 🗣️ General - Off-topic, casual chat
7. 📚 [Course Name] - Course-specific discussion
```

### Step 4: Create Course Content

1. Go to Classroom
2. Create first module
3. Add lessons within module
4. Upload or embed videos
5. Add text content
6. Set unlock rules (if using gamification)

**Content Recommendations**:
- Start with 3-5 modules minimum
- Include quick win in Module 1
- Mix video, text, and downloadable resources
- Add discussion prompts in lessons

### Step 5: Configure Gamification

1. Go to Settings > Gamification
2. Adjust point values for actions
3. Set level thresholds
4. Create unlockable content
5. Name your levels (optional custom names)

**Gamification Strategy**:
```
Level 1-2: Full access to basics
Level 3: Unlock advanced modules
Level 4: Unlock exclusive content
Level 5+: Recognition and bragging rights
```

### Step 6: Write Guidelines

Create a pinned post in Announcements with community guidelines:
- Expected behavior
- Posting guidelines
- Self-promotion rules
- Conflict resolution
- Consequences for violations

### Step 7: Invite Founding Members

1. Copy invite link
2. Send to beta/founding members
3. Personally welcome each one
4. Guide them to intro post
5. Seed initial discussions

### Step 8: Launch Publicly

1. Announce on email list
2. Share on social media
3. Enable Discover (if desired)
4. Monitor closely first week
5. Adjust based on feedback

---

## Growth Tactics on Skool

### 1. Leverage the Discover Page

**Optimize Your Listing**:
- Compelling community name
- Strong description with keywords
- High-quality images
- Active engagement (improves ranking)
- Good retention (improves ranking)

**Discover SEO**:
- Include target keywords in name and description
- Choose the right category
- Maintain high activity levels
- Encourage member engagement

### 2. The Skool Games

Alex Hormozi's Skool Games is a monthly competition where communities compete based on growth and engagement metrics. Participating can:
- Provide accountability
- Generate exposure if you win
- Connect you with other Skool creators
- Access Hormozi's community-building tactics

**How to Participate**:
- Join the Skool Games community
- Follow the monthly challenges
- Report your metrics
- Learn from top performers

### 3. Cross-Promotion

**Partner with Other Skool Communities**:
- Find complementary (not competing) communities
- Propose mutual promotion
- Guest expert exchanges
- Joint events

**Example**:
```
Your Community: Copywriting Mastery
Partner Community: Facebook Ads Academy

Cross-Promotion:
- You post about FB ads as traffic source
- They post about copy for ad performance
- Both communities benefit
```

### 4. Content Marketing Flywheel

**Use Skool Content Externally**:
```
Community Post → Expand to Blog Post → Share on Social → Drive to Community
                                     ↓
                              → YouTube Video → Call to Action → Community
                                     ↓
                              → Podcast Episode → Mention Community
```

### 5. Member Referral Program

**Built-in Affiliate Feature**:
Skool allows members to refer others for commission:
- Set commission percentage
- Members get unique referral links
- Automatic tracking and payouts

**Referral Program Best Practices**:
- 20-30% commission is standard
- First-month only or recurring (your choice)
- Promote the program regularly
- Celebrate successful referrers

### 6. Free to Paid Funnel

**Create a Free Community as Top of Funnel**:
```
Free Community (lead gen)
├── Valuable free content
├── Community experience demo
├── Trust building
└── Upsell path to paid community

Conversion Tactics:
- Regular mentions of paid community
- Exclusive previews for free members
- Success stories from paid members
- Limited-time founding member offers
```

### 7. Event-Based Growth

**Use Live Events to Drive Signups**:
- Host public workshops
- Require Skool signup to attend
- Deliver massive value
- Pitch community at end

**Event Funnel**:
```
Social/Ads → Free Workshop Registration → Skool Signup → Event → Paid Community Pitch
```

---

## Successful Skool Communities Analysis

### Case Study 1: Hormozi's Skool Community

**Community**: Skool Games / Acquisition.com Community
**Size**: 30,000+ members
**Price**: Free
**Model**: Lead generation for Acquisition.com

**Success Factors**:
- Alex Hormozi's personal brand and reach
- High-value free content
- Active engagement from Alex himself
- Gamification heavily used
- Clear funnel to paid services

**Lessons**:
1. Personal brand accelerates growth
2. Free can work with strong back-end monetization
3. Founder engagement matters at scale
4. Gamification drives activity

### Case Study 2: Classroom Model Success

**Community**: [Typical Course Creator Community]
**Size**: 500-1,000 members
**Price**: $49/month
**Model**: Course + community subscription

**Typical Structure**:
```
Revenue: $25,000-50,000/month
Content: 20-50 hours of course content
Calls: Weekly group calls
Support: Daily community engagement
Team: Founder + 1 community manager
```

**Success Factors**:
- Strong course content
- Active community engagement
- Weekly live touchpoints
- Clear transformation promise
- Good onboarding

### Case Study 3: High-Ticket Skool

**Community**: Executive/B2B Mastermind
**Size**: 50-100 members
**Price**: $500-2,000/month
**Model**: Premium mastermind

**Structure**:
```
Revenue: $25,000-200,000/month
Content: Exclusive frameworks/playbooks
Calls: Multiple per week (hot seats, Q&A)
Access: Direct access to expert/founder
Vetting: Application required
```

**Success Factors**:
- High-value, exclusive access
- Strict member vetting
- Intimate community size
- Significant results for members
- Premium positioning

---

## Pros and Cons

### Pros

1. **Simplicity**: Set up in under 30 minutes, no technical skills needed
2. **All-in-One**: Community, courses, calendar, payments in one platform
3. **Lowest Fees**: 2.9% transaction fee on Pro plan beats all competitors
4. **Gamification Built-In**: Points, levels, leaderboards included
5. **Mobile-First**: Excellent mobile experience
6. **Discover Page**: Free organic traffic opportunity
7. **Unlimited Video**: No storage limits for course content
8. **Flat Pricing**: No per-member fees
9. **Clean UX**: Facebook-like familiarity
10. **Fast Updates**: Active development, new features regularly

### Cons

1. **Limited Customization**: Can't customize look/feel significantly
2. **No White-Label**: Skool branding always present
3. **No API**: Can't integrate with other tools (except Zapier basics)
4. **No Sub-Groups**: Can't create sub-communities within community
5. **Basic Analytics**: Less depth than some competitors
6. **No Native Email**: Need external email marketing tool
7. **Single Community per Plan**: Each community requires separate plan
8. **No SSO**: Can't integrate with enterprise authentication
9. **Limited Payment Options**: No native support for payment plans
10. **No Comments Threading**: Flat comment structure only

### Best Use Cases

**Ideal for**:
- Solo course creators
- Coaches running group programs
- Experts monetizing knowledge
- Creators wanting simple, fast setup
- Anyone prioritizing low fees
- Mobile-first communities
- Communities wanting gamification

**Not Ideal for**:
- Large enterprises
- Heavily branded experiences
- Complex integration needs
- Multiple sub-communities
- Anonymous/private communities
- Technical/developer communities
- Free communities (host must still pay)

---

## Skool vs Alternatives

### Skool vs Circle

| Factor | Skool | Circle |
|--------|-------|--------|
| Setup Time | 30 minutes | 1-2 hours |
| Pricing | $9-99/month | $89-199+/month |
| Transaction Fee | 2.9-10% | 0.5-7% |
| Customization | Limited | Extensive |
| Courses | Built-in | Built-in |
| Gamification | Strong | Basic |
| API/Integrations | Limited | Extensive |
| Best For | Simplicity seekers | Professional brands |

### Skool vs Discord

| Factor | Skool | Discord |
|--------|-------|---------|
| Setup Time | 30 minutes | 1-4 hours |
| Platform Cost | $9-99/month | Free |
| Transaction Fee | 2.9-10% | 10% |
| Courses | Built-in | Not available |
| Gamification | Built-in | Via bots |
| Target Demo | Professionals | Gaming/tech |
| Mobile App | Good | Excellent |
| Best For | Course creators | Tech/gaming communities |

### Skool vs Mighty Networks

| Factor | Skool | Mighty Networks |
|--------|-------|-----------------|
| Setup Time | 30 minutes | 2-4 hours |
| Pricing | $9-99/month | $79-354+/month |
| Transaction Fee | 2.9-10% | 0.5-2% |
| Native Apps | No | Yes (paid tier) |
| White Label | No | Yes (paid tier) |
| AI Features | Limited | AI Cohost |
| Best For | Simplicity | Full membership site |

---

## Implementation Checklist

### Week 1: Foundation
- [ ] Sign up for Skool
- [ ] Choose plan (start with Pro if charging)
- [ ] Create community with strong name
- [ ] Write compelling description
- [ ] Upload quality images
- [ ] Set up payment processing
- [ ] Configure membership price

### Week 2: Content Setup
- [ ] Create 5-7 categories
- [ ] Set up initial course modules
- [ ] Upload first course content
- [ ] Write welcome message
- [ ] Create community guidelines post
- [ ] Set gamification levels
- [ ] Configure unlock rules

### Week 3: Pre-Launch
- [ ] Invite 10-20 founding members
- [ ] Get feedback on setup
- [ ] Make adjustments
- [ ] Create intro post template
- [ ] Schedule first live event
- [ ] Prepare launch content

### Week 4: Launch
- [ ] Send launch emails
- [ ] Share on social media
- [ ] Enable Discover (if desired)
- [ ] Welcome all new members personally
- [ ] Host first live call
- [ ] Gather initial testimonials

### Ongoing
- [ ] Daily community engagement
- [ ] Weekly live calls
- [ ] Monthly content updates
- [ ] Quarterly gamification prizes
- [ ] Regular member spotlights
- [ ] Continuous onboarding optimization

---

## Advanced Skool Strategies

### 1. The Engagement Flywheel

Create a self-sustaining engagement system:

```
New Member Joins
      ↓
Welcome Message + Intro Prompt
      ↓
Intro Post → Likes & Comments from Existing Members
      ↓
Member feels welcomed, starts exploring
      ↓
Finds content → Engages → Earns points
      ↓
Levels up → Unlocks content → More engagement
      ↓
Sees wins → Posts own wins → Gets celebrated
      ↓
Becomes active member → Welcomes new members
      ↓
Cycle continues
```

### 2. Content Batching Strategy

Maximize efficiency with batched content creation:

```
Monthly Batch:
- 4 course lessons
- 4 educational posts
- 4 discussion prompts
- 4 win celebration posts
- 1 member spotlight

Schedule:
Monday: New lesson drops
Tuesday: Discussion prompt
Wednesday: Educational post
Thursday: Win celebration
Friday: Casual/community post
```

### 3. The Hot Seat Model

Weekly calls using hot seat format:

```
Call Structure (60 minutes):
- 5 min: Welcome and wins
- 15 min: Hot seat #1 (member presents challenge, gets advice)
- 15 min: Hot seat #2
- 15 min: Hot seat #3
- 10 min: Q&A and close

Benefits:
- Structured yet personal
- High-value for participants
- Others learn from each hot seat
- Creates FOMO for non-attendees
```

### 4. Leaderboard Leveraging

Turn gamification into engagement driver:

```
Weekly Rituals:
- Monday: Post weekly leaderboard
- Friday: Shout out top 3 contributors
- Monthly: Prize for #1 (free month, coaching call, swag)

Level Milestones:
- Level 5: Personal congratulations DM
- Level 7: Feature in member spotlight
- Level 9: Special badge/recognition
```

### 5. The Challenge Model

Run periodic challenges to spike engagement:

```
30-Day Challenge Example:
- Daily action required
- Points for completion
- Accountability partners
- Daily check-in post
- Prizes for completion

Results:
- Massive engagement spike
- Member bonding
- Transformation stories
- Content for marketing
```

---

## Troubleshooting Common Issues

### Low Engagement
**Symptoms**: Few posts, comments, low activity
**Solutions**:
- Increase founder posting frequency
- Ask direct questions
- Create easier ways to engage (polls, reactions)
- Review gamification settings
- Reach out to inactive members directly

### High Churn
**Symptoms**: Members leaving quickly
**Solutions**:
- Improve onboarding
- Send engagement surveys
- Add more value/content
- Personal outreach before cancellation
- Exit surveys

### Content Overwhelm
**Symptoms**: Too much content, members confused
**Solutions**:
- Create start here guide
- Simplify category structure
- Add progress paths
- Reduce posting frequency
- Curate best content

### Toxic Members
**Symptoms**: Negativity, conflict, complaints
**Solutions**:
- Clear guidelines
- Fast moderation
- Private warnings first
- Don't hesitate to remove
- Protect community culture

---

## Resources

### Official Resources
- Skool Help Center: help.skool.com
- Skool Community: skool.com/skool
- Skool Games: skool.com/games

### Recommended Skool Communities to Study
- Skool Games (Hormozi)
- The Copywriting Community
- Fitness business communities
- Course creator communities

### Tools That Integrate with Skool
- Zapier (basic automation)
- Stripe (payments)
- Email marketing tools (manual integration)
- Calendar tools (for events)

---

## Summary

Skool is the ideal platform for creators and coaches who want to launch quickly with minimal technical overhead and keep more of their revenue. Its gamification system and all-in-one nature make it particularly effective for course-based communities.

**Choose Skool if you**:
- Value simplicity over customization
- Want to launch in under a day
- Appreciate gamification features
- Care about minimizing fees
- Don't need extensive integrations

**Don't choose Skool if you**:
- Need heavy branding/white-labeling
- Require complex integrations
- Want multiple sub-communities
- Need enterprise features (SSO, etc.)
- Prefer free community hosting
