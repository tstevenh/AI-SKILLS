# Reddit Account Warmup

> Warmup workflow for Reddit accounts before strategic posting.
> Each account should have a unique persona. Run daily via cron or manually.

---

## Trigger Commands

- "Warm up Reddit accounts"
- "Run Reddit warmup"
- "Fill warmup quota"

---

## Warmup Phases (Per Account)

| Phase | Duration | Activity |
|-------|----------|----------|
| 1 | Week 1 | Reply to comments on own viral post ONLY |
| 2 | Weeks 1-2 | Browse home sub 5-30 min/day, max 1 comment/week |
| 3 | Week 3-4 | Home sub only, max 2 comments/day |
| 4 | Week 5+ | Expand to r/all, general engagement |

---

## Batch Workflow

```
[Start]
    ↓
[1] Load account list
    ↓
[2] For each account with remaining quota:
    ↓
    [2-1] Open browser profile for account
    [2-2] Load account persona
    [2-3] Check warmup phase (based on start date)
    [2-4] Execute phase-appropriate activity:
          - Phase 1: Check viral post for new comments, reply if any
          - Phase 2-3: Browse home sub, find post, write comment
          - Phase 4: Browse r/all, engage naturally
    [2-5] Update daily tracking log
    [2-6] Close browser profile
    [2-7] Wait 2-5 minutes before next account
    ↓
[3] Generate completion report
    ↓
[End]
```

---

## Comment Writing Rules

### STRICT RULES (All Accounts)
- ❌ **NO EM DASHES (—)** — Never use em dashes, use commas or periods instead
- ❌ No AI-sounding phrases ("I'd be happy to", "Great question!")
- ❌ No marketing language
- ❌ No links unless absolutely natural
- ✅ Match the persona's unique voice
- ✅ Include typos/casual language occasionally
- ✅ Keep it short (1-3 sentences usually)
- ✅ Sound like a real person

### Per-Account Persona
Each account should have a unique writing style defined in a persona file:
- Vocabulary preferences
- Sentence structure patterns
- Emoji usage (or not)
- Casual vs formal tone
- Interests reflected in comments

---

## Single Comment Workflow

### Step 1: Navigate to Target
```
Phase 1-3: Go to reddit.com/r/{home_sub}/new/
Phase 4: Go to reddit.com/r/all/rising/
```

### Step 2: Find Suitable Post
```
Criteria:
- Has < 50 comments (not oversaturated)
- Posted within last 24 hours
- Topic matches account interests (from persona)
- NOT already commented on today
```

### Step 3: Analyze Post
```
- Read post content fully
- Understand what OP wants
- Check existing comments for tone
- Decide if comment adds value
```

### Step 4: Write Comment (Using Persona)
```
1. Load persona file
2. Draft comment matching persona voice
3. Verify NO em dashes
4. Keep authentic and short
```

### Step 5: Post & Track
```
1. Click comment box, type, submit
2. Copy comment permalink
3. Update daily tracking log
```

---

## Tracking File Format

Daily tracking log example:

```markdown
# Reddit Warmup - YYYY-MM-DD

## Summary
| Account | Phase | Home Sub | Comments | Browse Time |
|---------|-------|----------|----------|-------------|
| account-1 | 1 | r/example | 0 | 12 min |
| account-2 | 3 | r/hobby | 1 | 8 min |

## Activity Log

### [HH:MM] account-1
- **Action**: Browsed r/example
- **Duration**: 12 minutes
- **Posts viewed**: 5
- **Comments**: 0

### [HH:MM] account-2
- **Action**: Commented on r/hobby
- **Post**: [Title](URL)
- **Comment**: "love the colors on this one"
- **Permalink**: [link]
```

---

## Error Handling

| Error | Response |
|-------|----------|
| Browser profile won't start | Skip account, note in log |
| Reddit rate limit | Wait 10 min, retry once |
| Account suspended | STOP, alert team immediately |
| Proxy blocked | Skip account, note for proxy rotation |
| No suitable posts | Browse only, skip commenting |

---

## Completion Report

```
---
## Warmup Completion - YYYY-MM-DD

**Accounts processed**: 8/10
**Total browse time**: 47 minutes
**Comments posted**: 3

### Per Account
| Account | Status | Activity |
|---------|--------|----------|
| account-1 | ✅ | Browsed 12 min |
| account-2 | ✅ | Commented 1x |
| account-3 | ⏸️ | Skipped (LOW TRUST) |

### Issues
- account-4: Still needs viral post
---
```

---

## Suggested File Structure

| File | Purpose |
|------|---------|
| `personas/[account].md` | Unique writing style per account |
| `tracking/YYYY-MM-DD.md` | Daily activity log |
| `accounts.md` | Account list + status |
