---
name: reddit
description: Reddit organic marketing skill for placing helpful brand mentions in high-intent threads. Use when running Reddit placement campaigns, finding buyer-intent threads, crafting authentic comments, or scaling Reddit presence with anti-detection rules. Also includes account warmup workflow.
---

## Related Files
- **WARMUP.md** - Account warmup workflow (daily engagement)
- **personas/** - Unique writing style per account (10 files)
- **tracking/** - Daily activity logs

---

# Reddit Skill

Systematic approach to placing helpful brand mentions in high-intent Reddit threads that rank in Google. Focus on being genuinely useful while staying undetected.

## Quick Start

**To run a Reddit placement campaign, I need:**
1. **Offer** - product/service/brand being mentioned
2. **Target keywords** - buyer intent queries (recommendations, comparisons, reviews)
3. **Vertical** - niche category (local services, SaaS, ecom, etc.)
4. **Constraints** - forbidden claims, disallowed links, brand safety notes

**Optional:**
- Geo targeting (city subreddits)
- Competitor list (to reference neutrally)
- Subreddit allowlist/blocklist

---

## ⚠️ CRITICAL: Anti-Detection Rules

### Red Flags That Get Accounts Burned (AVOID)
1. **Aged account + Low karma** - 1yr old with 2 karma = obvious bot
2. **AI-sounding content** - Hallucinations, robotic phrasing, overly perfect grammar
3. **Only posts in low-moderation subs** - GEO platforming subs are watched
4. **Removed posts in moderated subs** - Pattern of removals = flagged
5. **Zero contribution diversity** - Only promotional comments
6. **Pattern posting** - Same times, same subs, same writing style

### Account Health Requirements (Before ANY Strategic Posts)
| Metric | Minimum | Ideal |
|--------|---------|-------|
| Karma | 100+ | 500+ |
| Account age | 30 days | 6+ months |
| Genuine comments | 20+ | 50+ |
| Subreddit diversity | 5+ subs | 10+ subs |
| Post history | Mixed (not just comments) | Posts + comments |

### Cadence Rules
- **1 comment per account per week MAXIMUM**
- 10 accounts = 10 placements/week max
- Spread across different days and times
- **80/20 rule**: 80% genuine engagement, 20% strategic placements
- Never batch posts in same subreddit from multiple accounts

---

## Workflow

### 1) Opportunity Discovery

**Google patterns:**
```
best [category] site:reddit.com
[product] vs [competitor] reddit
is [brand] worth it reddit
[service] [city] reddit
```

**Reddit search patterns:**
- "best", "recommend", "worth it", "alternatives", "vs"
- Filter by last year, sort by relevance/top

**Thread Selection Criteria:**
| Factor | Prefer | Avoid |
|--------|--------|-------|
| Intent | Buyer intent ("choosing soon") | Venting, complaints |
| Engagement | Active comments | Dead threads |
| Age | Evergreen OR new | Locked/archived |
| Moderation | Well-moderated subs | Low-mod GEO subs |
| Google ranking | Already ranks for keywords | No search visibility |

**Output:** `opportunity_list.md` with:
- Thread URL, Subreddit, Intent strength, Risk level, Recommended action

---

### 2) Subreddit Mapping

Before posting in any sub, document:
- **Rules** - Read sidebar, stickies
- **Tone** - casual / analytical / supportive / blunt
- **Link policy** - none / limited / ok
- **Promo sensitivity** - low / medium / high
- **Risk** - low / medium / high

**Output:** `subreddit_tone_maps.md`

---

### 3) Comment Crafting

**5-Part Template:**
1. **Empathy hook** - Mirror OP's situation
2. **Context** - What you tried/decided between
3. **Helpful breakdown** - Pros/cons, tradeoffs, what to watch for
4. **Soft recommendation** - Mention brand naturally (NO sales voice)
5. **Exit line** - Offer to answer questions, mention constraints

**Style Rules:**
- ❌ No marketing language or exaggerated outcomes
- ❌ No certainty ("this is the best") → ✅ Use "in my experience", "might be worth"
- ✅ Include specific details (constraints, tradeoffs)
- ✅ Add casual language, minor typos acceptable
- ✅ Mentions over links (unless sub is link-tolerant)
- ✅ Sound like a real person sharing experience

**Output:** 1 main comment (3-10 sentences) + 1-2 optional replies

---

### 4) Posting Execution

**Pre-flight checklist:**
- [ ] Account has 100+ karma
- [ ] Account has diverse post history
- [ ] Haven't posted from this account this week
- [ ] Comment sounds human (read aloud test)
- [ ] No links (unless sub allows)
- [ ] Subreddit tone matched

**Post-posting:**
- Screenshot comment with timestamp
- Log in placement tracker
- Check visibility in incognito after 1 hour

---

### 5) Monitoring

**Status checks (incognito/logged out):**
- **Live** - Visible, track position
- **Removed** - Mod deleted, note reason
- **Filtered** - Shadowbanned in thread, move on

**Response to issues:**
- Removed → Adjust tone, remove links, try different thread
- Filtered → Don't fight it, improve subreddit fit
- Hostile replies → Disengage politely, never escalate

**Check cadence:**
- Day 1, 3, 7 post-comment
- Then weekly for evergreen threads

---

### 6) Scaling

**Weekly cadence (with 10 accounts):**
- Discover 10-20 new threads
- Select best 10 (one per account)
- Place 10 comments (1 per account)
- Monitor all placements
- Maintain winners (reply to follow-ups)

**Monthly:**
- Expand keyword clusters
- Build "thread library" of evergreen winners
- Retire underperforming accounts, warm new ones
- Document what comment styles work

---

## Output Structure

```
~/clawd/projects/reddit/
├── opportunity_list.md      # Threads to target
├── placement_log.md         # What we posted, status, performance
├── subreddit_tone_maps.md   # Notes per community
├── comment_templates.md     # Reusable patterns (with variation)
└── account_health.md        # Karma, activity, last post date
```

---

## Measurement

**Leading indicators:**
- Survival rate (% live vs removed)
- Top-section presence (% near top)
- Thread library growth

**Lagging indicators:**
- Branded search lift
- Referral traffic
- Assisted conversions

---

## Failure Modes & Fixes

| Problem | Fix |
|---------|-----|
| High removals | Improve subreddit fit, remove links, reduce promo feel |
| Low visibility | Choose better threads, comment earlier, write deeper |
| Pattern detection | Vary tone, structure, timing, subreddits |
| Account flagged | Retire account, warm replacement |

---

## Full Knowledge Base

See: `./KNOWLEDGE-BASE.md` for complete methodology and examples.
