# Feedback Loop Skill

## Overview

The **Feedback Loop** skill provides local, privacy-first feedback tracking and performance optimization for OpenClaw. It captures both manual ratings and automated signals to build insights about:

- Model performance by task type
- Skill success rates
- Error patterns
- Time-based trends

**New in Scale Edition:** Handles 5,000+ entries without context bloat through rolling summaries, auto-archival, and smart loading.

---

## Quick Start

**Rate the last interaction:**
```bash
python ~/clawd/indexsy-skills/feedback-loop/feedback.py rate 4
```

**Log a skill outcome:**
```bash
python ~/clawd/indexsy-skills/feedback-loop/feedback.py log --skill reddit --task post --status success --duration 45
```

**View recent feedback:**
```bash
python ~/clawd/indexsy-skills/feedback-loop/feedback.py recent --limit 10
```

**Fast analysis (uses summary):**
```bash
python ~/clawd/indexsy-skills/feedback-loop/analyze.py --days 7
```

**Search feedback:**
```bash
python ~/clawd/indexsy-skills/feedback-loop/feedback.py search "reddit"
```

---

## Architecture

### Scale-Optimized Design

```
┌─────────────────┐     ┌──────────────────┐     ┌─────────────────┐
│  New Entries    │────▶│  feedback.jsonl  │────▶│  Auto-Archive   │
│  (Real-time)    │     │  (Last 30 days)  │     │  (Monthly)      │
└─────────────────┘     └──────────────────┘     └─────────────────┘
                                │                           │
                                ▼                           ▼
                       ┌──────────────────┐     ┌──────────────────┐
                       │  Auto-Summary    │     │  Archive Files   │
                       │  (Every 10 logs) │     │  YYYY-MM.jsonl   │
                       └──────────────────┘     └──────────────────┘
                                │
                                ▼
                       ┌──────────────────┐
                       │  Summary File    │
                       │  feedback-       │
                       │  summary.json    │
                       └──────────────────┘
```

### Storage Tiers

| Tier | Location | Retention | Access Speed |
|------|----------|-----------|--------------|
| Active | `feedback.jsonl` | 30 days | Instant |
| Archive | `feedback-archive-YYYY-MM.jsonl` | Permanent | Fast (grep) |
| Summary | `feedback-summary.json` | Rolling windows | Instant |

---

## Core Concepts

### Manual Ratings (`/rate` command pattern)

Users can rate interactions on a scale of 1-5:

- **1** - Failed completely, needs retry
- **2** - Major issues, barely usable
- **3** - Acceptable but could be better
- **4** - Good result, minor improvements possible
- **5** - Excellent, exceeded expectations

These ratings include:
- Timestamp
- Rating value
- Optional comment
- Context (session, model, tools used)

### Automated Signal Capture

The system automatically captures:

| Signal | Source | Purpose |
|--------|--------|---------|
| Exit codes | Tool executions | Success/failure detection |
| Error types | Tool outputs | Pattern identification |
| Duration | Tool timing | Performance tracking |
| Model used | Session context | Model comparison |
| Skill invoked | Command detection | Skill success rates |

### Rolling Summaries

Pre-computed statistics updated every 10 entries:

```json
{
  "last_7_days": {
    "total_ratings": 12,
    "avg_rating": 4.3,
    "model_performance": {
      "claude-sonnet-4-5": {"tasks": 45, "success_rate": 0.89}
    },
    "skill_success": {"reddit": 0.67, "wordpress": 0.92},
    "top_failures": ["browser timeout", "API rate limit"]
  },
  "last_30_days": { ... },
  "all_time": { ... }
}
```

### Auto-Archival

Entries older than 30 days are automatically moved to monthly archives:
- Archives named: `feedback-archive-YYYY-MM.jsonl`
- Archives stored in: `~/clawd/memory/`
- Archives loaded on-demand for historical queries

---

## Commands Reference

### feedback.py

```bash
# Log a manual rating
python feedback.py rate <1-5> [--comment "..."] [--model "..."] [--skill "..."]

# Log automated signal
python feedback.py log --skill <name> --task <type> --status <success|failure> [--duration <seconds>]

# Query recent feedback (from active file only)
python feedback.py recent [--limit N]

# Generate/regenerate rolling summaries
python feedback.py summarize [--quiet]

# Archive old entries (older than 30 days)
python feedback.py archive

# Search feedback with grep (fast)
python feedback.py search <query> [--include-archives] [--limit N]

# Get summary stats (uses pre-computed summary)
python feedback.py stats [--days N] [--verbose]

# List archive files
python feedback.py list-archives

# Export feedback data
python feedback.py export [--output path.json] [--since YYYY-MM-DD] [--include-archives]
```

### analyze.py

```bash
# Fast analysis using pre-computed summary
python analyze.py [--days 30]

# Deep analysis using raw log data (slower, more detail)
python analyze.py --deep [--days 30]

# Model performance report
python analyze.py --models [--days 30]

# Skill success rates
python analyze.py --skills [--days 30]

# Failure pattern analysis
python analyze.py --failures [--days 30]

# Search for specific term
python analyze.py --search "term" [--include-archives]

# Export insights
python analyze.py --export insights.json [--days 30]
```

---

## Smart Loading

The system intelligently chooses data sources based on query type:

### Fast Path (Uses Summary)
- Overall statistics
- Model performance trends
- Skill success rates
- Recent failure patterns
- Queries ≤ 30 days

### Deep Path (Uses Raw Logs)
- Time-based patterns
- Custom date ranges
- Detailed failure analysis
- Full entry search
- Historical deep dives

### Grep Path (Uses System Tools)
- Targeted searches
- Specific skill/model queries
- Archive searches
- Pattern matching

---

## Data Format

### Active Feedback Entry

```json
{
  "timestamp": "2026-02-16T18:15:00",
  "type": "manual_rating",
  "rating": 4,
  "comment": "Good result but took a while",
  "model": "claude-sonnet-4-5",
  "skill": "reddit",
  "context": {
    "session_id": "abc123",
    "tools_used": ["browser", "exec"]
  }
}
```

```json
{
  "timestamp": "2026-02-16T18:20:00",
  "type": "automated_signal",
  "skill": "reddit",
  "task": "post",
  "status": "success",
  "duration": 45,
  "exit_code": 0,
  "model": "claude-sonnet-4-5"
}
```

### Summary Format

```json
{
  "generated_at": "2026-02-16T18:00:00",
  "active_entries": 150,
  "archived_entries": 4850,
  "total_entries": 5000,
  "last_7_days": {
    "total_ratings": 12,
    "avg_rating": 4.3,
    "model_performance": {...},
    "skill_success": {...},
    "top_failures": [...]
  },
  "last_30_days": {...},
  "all_time": {...}
}
```

---

## Configuration

### Environment Variables

| Variable | Default | Description |
|----------|---------|-------------|
| `FEEDBACK_ARCHIVE_DAYS` | 30 | Days to keep in active file |
| `FEEDBACK_SUMMARY_INTERVAL` | 10 | Entries between summary updates |

### Constants (in feedback.py)

```python
ARCHIVE_CUTOFF_DAYS = 30          # Move entries older than this
SUMMARY_UPDATE_INTERVAL = 10      # Update summary every N writes
```

---

## Design Principles

1. **Scale-First**: Handles 5,000+ entries without performance degradation
2. **Smart Loading**: Uses appropriate data source for query type
3. **Privacy-Safe**: Data stays local in workspace
4. **Actionable**: Insights drive model/skill selection
5. **Low Overhead**: Auto-summary every 10 writes, minimal I/O

---

## Performance Characteristics

| Operation | 100 entries | 1,000 entries | 5,000+ entries |
|-----------|-------------|---------------|----------------|
| `stats` (summary) | 10ms | 10ms | 10ms |
| `analyze --models` | 50ms | 50ms | 50ms |
| `search` (grep) | 20ms | 100ms | 500ms |
| `analyze --deep` | 100ms | 500ms | 3,000ms |
| `archive` | 50ms | 200ms | 1,000ms |

---

## File Structure

```
feedback-loop/
├── SKILL.md                    # This file - core documentation
├── README.md                   # Installation and quick start
├── EXAMPLES.md                 # Usage examples and workflows
├── feedback.py                 # Core tracking script (scale edition)
├── analyze.py                  # Analytics with smart loading
└── tests/
    └── test_feedback.py

memory/
├── feedback.jsonl              # Active entries (last 30 days)
├── feedback-summary.json       # Rolling summaries
├── feedback-archive-2026-01.jsonl  # January archive
├── feedback-archive-2026-02.jsonl  # February archive
└── ...
```

---

## Troubleshooting

### Summary is outdated
```bash
python feedback.py summarize  # Force regenerate
```

### Active file too large
```bash
python feedback.py archive    # Archive old entries
```

### Need historical data
```bash
python feedback.py export --include-archives --since 2026-01-01
```

### Slow queries
Use summary-based commands instead of `--deep`:
```bash
# Fast
python analyze.py --models --days 7

# Slow (but detailed)
python analyze.py --deep --models --days 7
```

---

## Future Enhancements

- [x] Rolling summaries (auto-generated)
- [x] Auto-archival (monthly files)
- [x] Smart loading (summary-first)
- [x] Grep-based search
- [ ] Model recommendation engine
- [ ] Trend alerts (anomaly detection)
- [ ] Export to external analytics
- [ ] Web dashboard
