# Feedback Loop - Usage Examples

## Table of Contents

1. [Manual Rating Flows](#manual-rating-flows)
2. [Automated Tracking Integration](#automated-tracking-integration)
3. [Fast Analysis with Summaries](#fast-analysis-with-summaries)
4. [Archive Management](#archive-management)
5. [Search and Discovery](#search-and-discovery)
6. [Weekly Performance Review](#weekly-performance-review)
7. [Optimization Workflows](#optimization-workflows)
8. [Scale Workflows (5k+ Entries)](#scale-workflows)

---

## Manual Rating Flows

### Rate the Last Interaction

```bash
# Basic rating (1-5)
python ~/clawd/indexsy-skills/feedback-loop/feedback.py rate 5

# Rating with comment
python ~/clawd/indexsy-skills/feedback-loop/feedback.py rate 4 \
    --comment "Accurate but could be faster"

# Rating with model context
python ~/clawd/indexsy-skills/feedback-loop/feedback.py rate 5 \
    --model "claude-sonnet-4-5" \
    --skill "reddit" \
    --comment "Excellent post creation"

# Rating a specific interaction type
python ~/clawd/indexsy-skills/feedback-loop/feedback.py rate 3 \
    --comment "Browser automation failed twice" \
    --tags browser,automation
```

### Batch Ratings

```bash
# Rate multiple tasks at end of session
python ~/clawd/indexsy-skills/feedback-loop/feedback.py rate 5 --comment "Research task"
python ~/clawd/indexsy-skills/feedback-loop/feedback.py rate 4 --comment "Code generation"
python ~/clawd/indexsy-skills/feedback-loop/feedback.py rate 2 --comment "Browser kept failing"
```

---

## Automated Tracking Integration

### Capture Tool Outcomes

```bash
#!/bin/bash
# Wrapper script that logs outcomes

run_with_feedback() {
    local skill=$1
    local task=$2
    shift 2
    
    local start=$(date +%s)
    "$@"
    local exit_code=$?
    local end=$(date +%s)
    local duration=$((end - start))
    
    if [ $exit_code -eq 0 ]; then
        status="success"
    else
        status="failure"
    fi
    
    python ~/clawd/indexsy-skills/feedback-loop/feedback.py log \
        --skill "$skill" \
        --task "$task" \
        --status "$status" \
        --duration "$duration" \
        --exit-code "$exit_code"
    
    return $exit_code
}

# Usage
run_with_feedback "reddit" "post" python scripts/reddit_post.py
```

### Capture Model Performance

```bash
# After model switch, log performance
python ~/clawd/indexsy-skills/feedback-loop/feedback.py log \
    --model "claude-sonnet-4-5" \
    --skill "code_review" \
    --task "analyze" \
    --status "success" \
    --duration 120
```

### Capture Skill Invocation

```bash
# Log skill usage
python ~/clawd/indexsy-skills/feedback-loop/feedback.py log \
    --skill "cro" \
    --task "audit" \
    --status "success" \
    --duration 300 \
    --metadata '{"pages": 5, "findings": 12}'
```

---

## Fast Analysis with Summaries

### Daily Summary (Instant)

```bash
# Check today's performance (uses summary, <10ms)
python ~/clawd/indexsy-skills/feedback-loop/analyze.py --days 1

# Output:
# ℹ️  Using pre-computed summary for fast analysis
# 
# === Feedback Analysis (Last 1 days) [summary] ===
# 
# Total ratings: 8
# Average rating: 4.1/5
# Top issues: browser timeout
```

### Model Comparison (Fast)

```bash
# Compare model performance (uses summary)
python ~/clawd/indexsy-skills/feedback-loop/analyze.py --models --days 7

# Output:
# === Model Performance ===
# Model                      Tasks      Success Rate
# --------------------------------------------------
# claude-sonnet-4-5          45         91%
# gpt-4o                     12         83%
```

### Deep Analysis (Detailed but Slower)

```bash
# Force raw data analysis for full details
python ~/clawd/indexsy-skills/feedback-loop/analyze.py --deep --models --days 7

# Output includes avg_duration, avg_rating per model
```

---

## Archive Management

### Manual Archive Run

```bash
# Archive entries older than 30 days
python ~/clawd/indexsy-skills/feedback-loop/feedback.py archive

# Output:
#   Archived 150 entries to feedback-archive-2026-01.jsonl
#   Archived 89 entries to feedback-archive-2025-12.jsonl
# 
# ✓ Archived 239 entries, kept 150 in active file
```

### List Archives

```bash
# See all archive files
python ~/clawd/indexsy-skills/feedback-loop/feedback.py list-archives

# Output:
# === Available Archives ===
# 
#   feedback-archive-2025-12.jsonl: 523 entries
#   feedback-archive-2026-01.jsonl: 891 entries
#   feedback-archive-2026-02.jsonl: 423 entries
# 
# Total archived: ~1837 entries
```

### Auto-Archive on Write

```bash
# Enable auto-archival when logging
python ~/clawd/indexsy-skills/feedback-loop/feedback.py log \
    --skill reddit \
    --task post \
    --status success \
    --auto-archive
```

### Archive-Aware Export

```bash
# Export including historical archives
python ~/clawd/indexsy-skills/feedback-loop/feedback.py export \
    --include-archives \
    --since 2026-01-01 \
    --output q1-feedback.json
```

---

## Search and Discovery

### Quick Search (Active File)

```bash
# Search current feedback
python ~/clawd/indexsy-skills/feedback-loop/feedback.py search "reddit"

# Output:
# === Search Results for 'reddit' (15 matches) ===
# 
# [2026-02-16T10:23:00] reddit: success
# [2026-02-16T09:15:00] reddit: failure
# ...
```

### Deep Search (All Archives)

```bash
# Search everything including archives
python ~/clawd/indexsy-skills/feedback-loop/feedback.py search "browser" \
    --include-archives \
    --limit 50

# Or use analyze.py search
python ~/clawd/indexsy-skills/feedback-loop/analyze.py --search "timeout" \
    --include-archives
```

### Grep-Based Filtering

```bash
# Use shell grep for complex queries
grep -h "failure" ~/clawd/memory/feedback*.jsonl | \
    python3 -c "import sys,json; [print(json.loads(l).get('skill','?')) for l in sys.stdin]" | \
    sort | uniq -c | sort -rn

# Output: Most failing skills
#   15 reddit
#    8 browser
#    3 wordpress
```

---

## Weekly Performance Review

### Automated Weekly Report

```bash
#!/bin/bash
# weekly-review.sh - Run every Monday

echo "=== Weekly Performance Report ==="
echo "Generated: $(date)"
echo ""

# Overall stats (fast summary)
echo "📊 Overall Stats (Last 7 days):"
python ~/clawd/indexsy-skills/feedback-loop/analyze.py --days 7

echo ""
echo "🤖 Model Performance:"
python ~/clawd/indexsy-skills/feedback-loop/analyze.py --models --days 7

echo ""
echo "🛠️  Skill Success Rates:"
python ~/clawd/indexsy-skills/feedback-loop/analyze.py --skills --days 7

echo ""
echo "⚠️  Areas for Improvement:"
python ~/clawd/indexsy-skills/feedback-loop/analyze.py --failures --days 7

echo ""
echo "📁 Archive Status:"
python ~/clawd/indexsy-skills/feedback-loop/feedback.py list-archives
```

### Monthly Deep Dive

```bash
#!/bin/bash
# monthly-deep-dive.sh

month=$1  # e.g., 2026-01

echo "=== Deep Analysis for $month ==="
echo ""

# Export the month's data
python ~/clawd/indexsy-skills/feedback-loop/feedback.py export \
    --since "${month}-01" \
    --until "${month}-31" \
    --include-archives \
    --output "/tmp/${month}-feedback.json"

echo "Exported $(cat /tmp/${month}-feedback.json | jq '. | length') entries"
echo ""

# Full analysis with raw data
echo "📈 Full Analysis:"
python ~/clawd/indexsy-skills/feedback-loop/analyze.py --deep \
    --all \
    --export "/tmp/${month}-insights.json"

echo ""
echo "Insights saved to /tmp/${month}-insights.json"
```

---

## Optimization Workflows

### Pre-Task Model Selection

```bash
#!/bin/bash
# suggest-model.sh

task_type=$1

echo "Analyzing best model for: $task_type"
echo ""

# Query recent performance for this task type
python ~/clawd/indexsy-skills/feedback-loop/analyze.py --models --days 14 | \
    grep -A 2 "$task_type" || echo "No recent data for this task type"

echo ""
echo "Recommendation based on historical performance"
```

### Skill Health Check

```bash
#!/bin/bash
# skill-health.sh

echo "=== Skill Health Check ==="
echo ""

# Get skills with < 80% success rate (from summary)
python ~/clawd/indexsy-skills/feedback-loop/analyze.py --skills --days 7 | \
    awk '/^  / && /[0-9]+%$/ {
        match($0, /([0-9]+)%/, arr)
        if (arr[1] < 80) print $0
    }'

echo ""
echo "Skills listed above may need attention"
```

### Continuous Improvement Loop

```bash
#!/bin/bash
# improvement-loop.sh - Run daily via cron

# 1. Collect stats from summary
python ~/clawd/indexsy-skills/feedback-loop/feedback.py stats --days 1 > /tmp/daily-stats.txt

# 2. Check for declining performance
current_rating=$(grep "Average" /tmp/daily-stats.txt | awk '{print $3}' | cut -d/ -f1)
if (( $(echo "$current_rating < 3.5" | bc -l) )); then
    echo "⚠️ Average rating below 3.5: $current_rating"
    echo "Recent failures:"
    python ~/clawd/indexsy-skills/feedback-loop/feedback.py search "failure" --limit 5
fi

# 3. Update memory with insights
cat >> ~/clawd/memory/feedback-insights.md << EOF

## $(date +%Y-%m-%d)
- Daily avg rating: $current_rating/5
- Status: $(if (( $(echo "$current_rating >= 4" | bc -l) )); then echo "✅ Good"; else echo "⚠️ Needs attention"; fi)
EOF

# 4. Auto-archive if needed
entry_count=$(wc -l < ~/clawd/memory/feedback.jsonl)
if [ $entry_count -gt 500 ]; then
    python ~/clawd/indexsy-skills/feedback-loop/feedback.py archive
fi
```

---

## Scale Workflows

### Handling 5,000+ Entries

```bash
# 1. Initial setup for large datasets
echo "Setting up archival for scale..."
python ~/clawd/indexsy-skills/feedback-loop/feedback.py archive
python ~/clawd/indexsy-skills/feedback-loop/feedback.py summarize

# 2. Daily operations (fast)
python ~/clawd/indexsy-skills/feedback-loop/analyze.py --days 7      # Uses summary
python ~/clawd/indexsy-skills/feedback-loop/feedback.py stats        # Uses summary
python ~/clawd/indexsy-skills/feedback-loop/feedback.py search "..." # Uses grep

# 3. Weekly maintenance
python ~/clawd/indexsy-skills/feedback-loop/feedback.py archive      # Move old entries
python ~/clawd/indexsy-skills/feedback-loop/feedback.py summarize    # Regenerate summary

# 4. Monthly deep analysis (slow but thorough)
python ~/clawd/indexsy-skills/feedback-loop/analyze.py --deep --all --include-archives
```

### Performance Benchmark

```bash
#!/bin/bash
# benchmark.sh - Test performance at scale

echo "=== Feedback Loop Performance Benchmark ==="
echo ""

# Count entries
total_active=$(wc -l < ~/clawd/memory/feedback.jsonl 2>/dev/null || echo 0)
echo "Active entries: $total_active"

# Count archives
archive_count=$(ls ~/clawd/memory/feedback-archive-*.jsonl 2>/dev/null | wc -l)
echo "Archive files: $archive_count"

# Time operations
echo ""
echo "⏱️  Timing operations..."

echo -n "Summary-based stats: "
time (python ~/clawd/indexsy-skills/feedback-loop/feedback.py stats >/dev/null 2>&1)

echo -n "Summary-based analyze: "
time (python ~/clawd/indexsy-skills/feedback-loop/analyze.py --days 7 >/dev/null 2>&1)

echo -n "Grep search: "
time (python ~/clawd/indexsy-skills/feedback-loop/feedback.py search "test" >/dev/null 2>&1)

echo -n "Deep analysis: "
time (python ~/clawd/indexsy-skills/feedback-loop/analyze.py --deep --days 30 >/dev/null 2>&1)

echo ""
echo "✅ Benchmark complete"
```

### Export and Backup Strategy

```bash
#!/bin/bash
# backup-strategy.sh

DATE=$(date +%Y%m%d)
BACKUP_DIR="~/clawd/backups/feedback"

mkdir -p $BACKUP_DIR

# 1. Export current active data
python ~/clawd/indexsy-skills/feedback-loop/feedback.py export \
    --output "$BACKUP_DIR/active-${DATE}.json"

# 2. Export with archives (full backup)
python ~/clawd/indexsy-skills/feedback-loop/feedback.py export \
    --include-archives \
    --output "$BACKUP_DIR/full-${DATE}.json"

# 3. Export summary
python ~/clawd/indexsy-skills/feedback-loop/feedback.py summarize --quiet
cp ~/clawd/memory/feedback-summary.json "$BACKUP_DIR/summary-${DATE}.json"

# 4. Compress
tar -czf "$BACKUP_DIR/feedback-${DATE}.tar.gz" -C "$BACKUP_DIR" \
    "active-${DATE}.json" "full-${DATE}.json" "summary-${DATE}.json"

# 5. Cleanup old backups (keep last 30)
ls -t $BACKUP_DIR/feedback-*.tar.gz | tail -n +31 | xargs rm -f

echo "✅ Backup complete: $BACKUP_DIR/feedback-${DATE}.tar.gz"
```

### Migration from Old Format

```bash
#!/bin/bash
# migrate-to-scale.sh - Convert existing feedback to scale format

echo "Migrating existing feedback to scale format..."

# 1. Ensure memory directory exists
mkdir -p ~/clawd/memory

# 2. Run archival to organize by month
python ~/clawd/indexsy-skills/feedback-loop/feedback.py archive

# 3. Generate initial summary
python ~/clawd/indexsy-skills/feedback-loop/feedback.py summarize

echo ""
echo "✅ Migration complete"
echo ""
python ~/clawd/indexsy-skills/feedback-loop/feedback.py list-archives
echo ""
python ~/clawd/indexsy-skills/feedback-loop/feedback.py stats
```

---

## Integration with Session Workflow

### Session Start

```bash
# Add to session start hook
echo "=== Feedback Status ==="
python ~/clawd/indexsy-skills/feedback-loop/feedback.py stats --days 1
python ~/clawd/indexsy-skills/feedback-loop/feedback.py recent --limit 3
```

### Session End

```bash
# Add to session end hook
python ~/clawd/indexsy-skills/feedback-loop/feedback.py summarize --quiet

echo "Rate this session? (1-5, or Enter to skip)"
read rating
if [ -n "$rating" ]; then
    python ~/clawd/indexsy-skills/feedback-loop/feedback.py rate "$rating" \
        --comment "End of session rating" \
        --auto-archive
fi
```

---

## Creating Custom Reports

### JSON to CSV Conversion

```bash
# Convert to CSV for spreadsheet analysis
python ~/clawd/indexsy-skills/feedback-loop/feedback.py export --output - | \
    jq -r '.[] | [.timestamp, .type, .status, .skill, .rating] | @csv' \
    > feedback-report.csv
```

### Model Performance Trend

```bash
# Track model performance over time
for month in 2026-01 2026-02 2026-03; do
    echo "=== $month ==="
    python ~/clawd/indexsy-skills/feedback-loop/analyze.py --search "$month" --include-archives | \
        grep -A 5 "Model Performance" || echo "No data"
done
```

### Failure Rate by Hour

```bash
# Analyze when failures happen most
python ~/clawd/indexsy-skills/feedback-loop/feedback.py export --output - | \
    jq -r '.[] | select(.status=="failure") | .timestamp' | \
    cut -dT -f2 | cut -d: -f1 | \
    sort | uniq -c | sort -rn | head -5
```
