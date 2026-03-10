# Reddit Placements - Full Knowledge Base

## Overview

Reusable procedural workflow for discovering, posting, and maintaining high-intent Reddit placements that influence search visibility and conversions.

## Purpose
This SOP defines a repeatable system to:
- Find threads tied to buyer-intent queries (recommendations, comparisons, reviews)
- Contribute genuinely helpful comments that survive moderation and earn visibility
- Support comment visibility with ethical engagement patterns (no brigading, no vote manipulation)
- Track placement status over time (live/removed/filtered) and maintain winners

## Outcomes
If executed properly, this workflow produces:
- Consistent placements in relevant threads that already rank in Google or have strong internal Reddit traffic
- Higher comment visibility (often top section of a thread)
- Compounding "owned thread library" for a niche/keyword set
- Lower removal rates through better subreddit fit and comment style discipline

## Core Principles
1. Participate, don't pitch.
2. Relevance beats volume.
3. Thread selection matters more than writing talent.
4. Variability prevents pattern risk (tone, timing, structure).
5. Maintain winners; don't constantly chase new threads.

---

## Anti-Detection Deep Dive

### How GEO Bots Get Detected (Source: r/SEO analysis)

**Red Flag Profile:**
- Aged account (1+ year) with almost no karma (2-10)
- Zero or near-zero contributions
- Posts AI-sounding content (hallucinations, robotic phrasing)
- Only gets approved in low-moderation subs (GEO platforming communities)
- Gets removed/disapproved in well-moderated subs
- Pattern of identical or similar posts across subs

**What Triggers Suspicion:**
1. Account age doesn't match activity level
2. Sudden burst of promotional-sounding comments
3. Only posts in "best X" or recommendation threads
4. Never engages in casual conversation
5. Perfect grammar + no personality = AI voice
6. Links in every comment
7. Same talking points across threads

### How to Stay Undetected

**Account Hygiene:**
- Build real karma through genuine participation FIRST
- Minimum 100 karma before any strategic posts
- Diverse subreddit presence (not just marketing/SEO subs)
- Mix of posts and comments
- Occasional upvoted jokes, helpful answers, casual chat

**Content Authenticity:**
- Write like a human, not a press release
- Include specific details only a real user would know
- Mention drawbacks and alternatives
- Use casual language ("tbh", "imo", typos ok)
- Reference your own constraints ("budget was tight", "needed X feature")

**Behavioral Patterns:**
- Never post from multiple accounts in same thread
- Vary posting times (not always 9am Monday)
- Don't comment on back-to-back days
- 80% genuine engagement, 20% strategic
- Respond to replies naturally

**Subreddit Selection:**
- Post in well-moderated subs (harder but more credible)
- Avoid obvious GEO/SEO platforming subs
- Survive in r/SEO, r/Entrepreneur, niche subs = credible
- Low-mod subs are watched and flagged

---

## Inputs

### Required
- `offer`: the product/service/brand being mentioned (or reputation to defend)
- `targets`: keyword set (buyer intent + comparisons + reviews)
- `vertical`: niche category (local services, SaaS, ecom, etc.)
- `constraints`: forbidden claims, disallowed links, brand safety notes

### Optional
- `geo`: location targeting for city subreddits or local service demand
- `competitors`: known alternatives to reference neutrally
- `subreddit_allowlist`: preferred communities
- `subreddit_blocklist`: communities to avoid

---

## Outputs

### Primary Deliverables
- `opportunity_list`: ranked target threads with intent score + risk score
- `comment_plan`: per thread
  - main comment (helpful mini-story)
  - 1–3 threaded replies (supporting details, nuance, clarification)
- `placement_log`: tracking sheet
  - thread URL, subreddit, timestamp
  - comment permalink
  - status: live / removed / filtered
  - observed position (top, mid, buried)
- `maintenance_queue`: threads to revisit and update or re-engage

---

## Workflow

### 1) Opportunity Discovery

**Goal:** Find threads with real demand where a helpful comment can meaningfully influence decisions.

**Discovery Methods:**

Google patterns:
```
best [category] site:reddit.com
[product] vs [competitor] reddit
is [brand] worth it reddit
[service] [city] reddit
```

Reddit search patterns:
- "best", "recommend", "worth it", "alternatives", "vs"
- filter by last year + sort by relevance/top when applicable

**Selection Rules (Prefer):**
- Buyer-intent OP phrasing (they're choosing soon)
- Existing engagement (comments present)
- Thread still receiving activity OR evergreen query that ranks in Google
- Moderation style compatible with participation (not overly link-hostile if linking is required)

**Output:** `opportunity_list` with columns:
- Thread URL
- Subreddit
- Intent strength: High / Medium / Low
- Engagement depth: comments/upvotes (rough)
- Age: new / active / evergreen
- Risk: Low / Medium / High
- Recommended action: comment / observe / skip

---

### 2) Subreddit Fit & Risk Mapping

**Goal:** Avoid removals by matching the community's tone and rules.

**Steps:**
- Read subreddit rules and sticky posts
- Review top comments in similar threads
- Note link tolerance: none / rare / acceptable
- Note "promo sensitivity": low / medium / high

**Output:** A small "tone map" per subreddit:
- Tone: casual / analytical / supportive / blunt
- Link policy: none / limited / ok
- Risk: low / medium / high
- Best comment style: story / comparison / checklist / Q&A

---

### 3) Comment Crafting

**Goal:** Write comments that feel human, are genuinely useful, and naturally include the recommendation when appropriate.

**Comment Template (5-Part):**
1. **Empathy hook:** mirror OP's pain or situation
2. **Context:** what you tried or what you were deciding between
3. **Helpful breakdown:** pros/cons, what mattered, what to watch for
4. **Soft recommendation:** mention brand/service naturally (no "sales voice")
5. **Exit line:** offer to answer questions or share constraints ("depends on budget", etc.)

**Style Rules:**
- Avoid marketing language and exaggerated outcomes
- Avoid certainty: use "in my experience," "might be worth," "depends"
- Include specific details (constraints, tradeoffs) to sound real
- Prefer mentions over links unless the community is link-tolerant
- Add human touches: casual phrasing, occasional typos, personality

**Output:** Per thread:
- 1 main comment (3–10 sentences)
- 1–3 replies (shorter, each adds new detail)

---

### 4) Conversation Stacking (Optional)

**Goal:** Create a natural discussion shape that increases perceived credibility.

**Pattern:**
- Main comment: experience + recommendation + tradeoff
- Reply #1: specific detail ("support was good", "pricing structure", "setup time")
- Reply #2: nuance ("if you're X, choose Y; if you're Z, choose A")
- Reply #3: answer the OP or another commenter's question

**Guardrails:**
- Replies must add value, not repeat
- Avoid over-coordination or obvious scripting patterns
- NEVER use multiple accounts in same thread

---

### 5) Ethical Visibility Support (No Vote Manipulation)

**Goal:** Increase comment visibility through legitimate means.

**Allowed Tactics:**
- Post early in newer threads where possible
- Be the most helpful comment in the thread (depth wins)
- Respond quickly to follow-up questions
- Encourage natural engagement by asking clarifying questions
- Cross-reference related context without spamming

**NOT Allowed:**
- Coordinated upvoting/vote manipulation
- Brigading communities
- Fake personas or impersonation
- Mass posting identical comments
- Multiple accounts in same thread

---

### 6) Placement Monitoring

**Goal:** Track what sticks, what fails, and what to maintain.

**Status Checks:**
- Confirm comment is visible while logged out/incognito
- Track:
  - Live
  - Removed (mod delete)
  - Filtered (appears to you but not others)

**Response SOP:**
- Removed: adjust tone/structure, avoid links, reduce "promo feel," try a different thread
- Filtered: do not fight it; move on and improve subreddit fit
- Hostile thread: disengage politely; don't escalate

**Output:** `placement_log` updated daily for 3–7 days post-comment, then weekly.

---

### 7) Scaling System

**Weekly Cadence (Conservative - 10 accounts):**
- Discover 10-20 new threads
- Select best 10 (one per account maximum)
- Place 10 comments (1 per account per week MAX)
- Monitor all placements
- Maintain top performers (reply if needed)

**Monthly Cadence:**
- Expand into adjacent keyword clusters
- Build a "thread library" of evergreen threads to revisit
- Standardize what works into reusable comment patterns (with variation)
- Retire flagged accounts, warm replacements

---

## Reputation & Defense Mode (Optional)

**Goal:** Reduce impact of negative ranking threads by adding calm, factual counterpoints.

**Guidelines:**
- Do not attack the original poster
- Share balanced experiences and tradeoffs
- Provide helpful alternatives
- Keep tone calm and neutral

---

## Measurement

### Leading Indicators
- Survival rate: % live vs removed/filtered
- Top-section presence: % of comments landing near the top cluster
- Thread library growth: count of "owned" evergreen threads

### Lagging Indicators
- Branded search lift (if trackable)
- Referral/direct traffic lift (if trackable)
- Assisted conversions (if trackable)

### Reporting Rhythm
- Weekly: placements + survival + notable wins + next actions
- Monthly: thread library growth + what patterns worked + risk notes

---

## Failure Modes & Fixes

### Failure: High removals
**Fix:**
- Improve subreddit fit
- Remove links
- Reduce promotional phrasing
- Increase usefulness and specificity

### Failure: Low visibility
**Fix:**
- Choose better threads (intent + activity)
- Comment earlier
- Write deeper, more practical comments
- Engage in follow-ups

### Failure: Pattern risk / Detection
**Fix:**
- Vary tone and structure
- Avoid repeating phrasing
- Avoid batching many posts in the same subreddit
- Increase genuine engagement ratio
- Retire compromised accounts

---

## Quick-Start Checklist

- [ ] Define 10–20 buyer-intent keywords
- [ ] Verify account health (100+ karma, diverse history)
- [ ] Build subreddit tone map (top 10 communities)
- [ ] Select 10 strong threads (one per account)
- [ ] Draft 1 main comment per thread (5-part template)
- [ ] Post (1 per account per week max)
- [ ] Monitor for 7 days (incognito checks)
- [ ] Build maintenance queue of winners
- [ ] Maintain 80/20 genuine/strategic ratio

---

## Example Comment Structures

### SaaS Recommendation
```
Been in a similar spot last year. We were comparing [Brand] vs [Competitor A] vs [Competitor B].

Ended up going with [Brand] mostly because [specific feature] was way better for our use case (we needed X). The onboarding was a bit rough tbh but their support helped us through it.

Main tradeoff: it's not the cheapest option, but the time savings made up for it. If budget is tight, [Competitor A] might be worth looking at first.

Happy to share more details if you want - what's your main priority?
```

### Local Service Recommendation
```
I actually just went through this. Tried a few places in [area] before finding one that worked.

[Business Name] on [Street] ended up being solid for me. What I liked: [specific detail]. What wasn't perfect: [honest drawback].

Depends what matters most to you though - if it's [Factor A], they're great. If it's [Factor B], might want to check out [Alternative] instead.
```

---

## Account Rotation Strategy

With 10 accounts:
- Weeks 1-2: Accounts 1-5 post (one each)
- Weeks 3-4: Accounts 6-10 post (one each)
- Accounts not posting should engage genuinely (upvotes, casual comments)
- Rotate which accounts are "active" vs "resting"
- Never let an account go silent for 30+ days
