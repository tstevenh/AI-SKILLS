#!/usr/bin/env python3
"""
feedback.py - Core tracking script for feedback loop system

Logs manual ratings and automated signals to memory/feedback.jsonl
Features rolling summaries, auto-archival, and smart loading for scale.
"""

import argparse
import json
import os
import subprocess
import sys
from collections import Counter, defaultdict
from datetime import datetime, timedelta
from pathlib import Path
from typing import Optional, Dict, List, Any

# Configuration
MEMORY_DIR = Path.home() / "clawd" / "memory"
FEEDBACK_FILE = MEMORY_DIR / "feedback.jsonl"
SUMMARY_FILE = MEMORY_DIR / "feedback-summary.json"
ARCHIVE_PATTERN = "feedback-archive-{year_month}.jsonl"

# Auto-update summary after N writes
SUMMARY_UPDATE_INTERVAL = 10

# Keep last N days in active feedback file
ARCHIVE_CUTOFF_DAYS = 30


def ensure_memory_dir():
    """Ensure the memory directory exists."""
    MEMORY_DIR.mkdir(parents=True, exist_ok=True)


def get_timestamp() -> str:
    """Get current ISO timestamp."""
    return datetime.now().isoformat()


def parse_timestamp(ts: str) -> datetime:
    """Parse ISO timestamp, handling various formats."""
    try:
        return datetime.fromisoformat(ts.replace('Z', '+00:00'))
    except (ValueError, AttributeError):
        return datetime.now()


def load_feedback(limit: Optional[int] = None) -> list:
    """Load feedback entries from file."""
    if not FEEDBACK_FILE.exists():
        return []
    
    entries = []
    with open(FEEDBACK_FILE, 'r') as f:
        for line in f:
            line = line.strip()
            if line:
                try:
                    entries.append(json.loads(line))
                except json.JSONDecodeError:
                    continue
    
    if limit:
        entries = entries[-limit:]
    
    return entries


def save_entry(entry: dict) -> int:
    """Append a single entry to the feedback file. Returns total entries count."""
    ensure_memory_dir()
    with open(FEEDBACK_FILE, 'a') as f:
        f.write(json.dumps(entry, separators=(',', ':')) + '\n')
    
    # Return approximate count (fast, doesn't require reading whole file)
    return count_entries_fast()


def count_entries_fast() -> int:
    """Count entries quickly using wc -l equivalent."""
    if not FEEDBACK_FILE.exists():
        return 0
    try:
        result = subprocess.run(['wc', '-l', str(FEEDBACK_FILE)], 
                              capture_output=True, text=True)
        return int(result.stdout.split()[0])
    except:
        # Fallback to counting
        return len(load_feedback())


def get_archive_path(year_month: str) -> Path:
    """Get path for monthly archive file."""
    return MEMORY_DIR / ARCHIVE_PATTERN.format(year_month=year_month)


def get_year_month(dt: datetime) -> str:
    """Get YYYY-MM format from datetime."""
    return dt.strftime("%Y-%m")


def should_archive(entry: dict, cutoff_date: datetime) -> bool:
    """Check if entry should be archived (older than cutoff)."""
    try:
        entry_date = parse_timestamp(entry.get('timestamp', ''))
        return entry_date < cutoff_date
    except:
        return False


def cmd_archive(args):
    """Archive old entries to monthly files."""
    ensure_memory_dir()
    
    if not FEEDBACK_FILE.exists():
        print("No feedback file found.")
        return
    
    cutoff = datetime.now() - timedelta(days=ARCHIVE_CUTOFF_DAYS)
    
    entries = load_feedback()
    if not entries:
        print("No entries to archive.")
        return
    
    to_archive = []
    to_keep = []
    
    for entry in entries:
        if should_archive(entry, cutoff):
            to_archive.append(entry)
        else:
            to_keep.append(entry)
    
    if not to_archive:
        print(f"No entries older than {ARCHIVE_CUTOFF_DAYS} days to archive.")
        return
    
    # Group by month
    by_month = defaultdict(list)
    for entry in to_archive:
        ts = parse_timestamp(entry.get('timestamp', ''))
        month_key = get_year_month(ts)
        by_month[month_key].append(entry)
    
    # Write archives
    archived_count = 0
    for month, month_entries in sorted(by_month.items()):
        archive_path = get_archive_path(month)
        
        # Append to existing archive if present
        mode = 'a' if archive_path.exists() else 'w'
        with open(archive_path, mode) as f:
            for entry in month_entries:
                f.write(json.dumps(entry, separators=(',', ':')) + '\n')
        
        archived_count += len(month_entries)
        print(f"  Archived {len(month_entries)} entries to {archive_path.name}")
    
    # Rewrite active file with remaining entries
    with open(FEEDBACK_FILE, 'w') as f:
        for entry in to_keep:
            f.write(json.dumps(entry, separators=(',', ':')) + '\n')
    
    print(f"\n✓ Archived {archived_count} entries, kept {len(to_keep)} in active file")


def load_archived_entries(year_month: Optional[str] = None) -> List[Dict]:
    """Load archived entries, optionally filtered by month."""
    entries = []
    
    if year_month:
        archive_path = get_archive_path(year_month)
        if archive_path.exists():
            with open(archive_path, 'r') as f:
                for line in f:
                    line = line.strip()
                    if line:
                        try:
                            entries.append(json.loads(line))
                        except json.JSONDecodeError:
                            continue
    else:
        # Load all archives
        for archive_file in sorted(MEMORY_DIR.glob("feedback-archive-*.jsonl")):
            with open(archive_file, 'r') as f:
                for line in f:
                    line = line.strip()
                    if line:
                        try:
                            entries.append(json.loads(line))
                        except json.JSONDecodeError:
                            continue
    
    return entries


def generate_summary() -> Dict[str, Any]:
    """Generate rolling summaries for different time windows."""
    ensure_memory_dir()
    
    now = datetime.now()
    
    # Load current entries
    current_entries = load_feedback()
    archived_entries = load_archived_entries()
    all_entries = current_entries + archived_entries
    
    # Time windows
    windows = {
        "last_7_days": now - timedelta(days=7),
        "last_30_days": now - timedelta(days=30),
        "all_time": datetime.min
    }
    
    summary = {
        "generated_at": now.isoformat(),
        "active_entries": len(current_entries),
        "archived_entries": len(archived_entries),
        "total_entries": len(all_entries)
    }
    
    for window_name, cutoff in windows.items():
        window_entries = [
            e for e in all_entries 
            if parse_timestamp(e.get('timestamp', '2000-01-01')) > cutoff
        ]
        
        summary[window_name] = calculate_window_stats(window_entries)
    
    return summary


def calculate_window_stats(entries: List[Dict]) -> Dict[str, Any]:
    """Calculate statistics for a time window."""
    if not entries:
        return {
            "total_ratings": 0,
            "avg_rating": 0,
            "model_performance": {},
            "skill_success": {},
            "top_failures": []
        }
    
    # Manual ratings
    manual = [e for e in entries if e.get('type') == 'manual_rating']
    ratings = [e.get('rating', 0) for e in manual if e.get('rating')]
    avg_rating = sum(ratings) / len(ratings) if ratings else 0
    
    # Automated signals
    automated = [e for e in entries if e.get('type') == 'automated_signal']
    
    # Model performance
    models = defaultdict(lambda: {"tasks": 0, "successes": 0})
    for entry in automated:
        model = entry.get('model', 'unknown')
        models[model]["tasks"] += 1
        if entry.get('status') == 'success':
            models[model]["successes"] += 1
    
    model_performance = {}
    for model, data in models.items():
        model_performance[model] = {
            "tasks": data["tasks"],
            "success_rate": round(data["successes"] / data["tasks"], 2) if data["tasks"] > 0 else 0
        }
    
    # Skill success rates
    skills = defaultdict(lambda: {"tasks": 0, "successes": 0})
    for entry in automated:
        skill = entry.get('skill', 'unknown')
        skills[skill]["tasks"] += 1
        if entry.get('status') == 'success':
            skills[skill]["successes"] += 1
    
    skill_success = {}
    for skill, data in skills.items():
        skill_success[skill] = round(data["successes"] / data["tasks"], 2) if data["tasks"] > 0 else 0
    
    # Top failures
    failures = [e for e in automated if e.get('status') == 'failure']
    failure_reasons = Counter()
    for entry in failures:
        error = entry.get('error', 'unspecified')
        if error and error != 'unspecified':
            failure_reasons[error] += 1
        elif entry.get('exit_code'):
            failure_reasons[f"exit_code_{entry['exit_code']}"] += 1
        else:
            failure_reasons['unknown'] += 1
    
    top_failures = [reason for reason, count in failure_reasons.most_common(5)]
    
    return {
        "total_ratings": len(ratings),
        "avg_rating": round(avg_rating, 2),
        "model_performance": model_performance,
        "skill_success": skill_success,
        "top_failures": top_failures
    }


def cmd_summarize(args):
    """Generate and save summary."""
    summary = generate_summary()
    
    with open(SUMMARY_FILE, 'w') as f:
        json.dump(summary, f, indent=2)
    
    if not args.quiet:
        print_summary(summary)
    
    return summary


def print_summary(summary: Dict):
    """Print summary in readable format."""
    print(f"=== Feedback Summary (Generated: {summary.get('generated_at', 'unknown')[:19]}) ===\n")
    print(f"Active entries: {summary['active_entries']}")
    print(f"Archived entries: {summary['archived_entries']}")
    print(f"Total tracked: {summary['total_entries']}\n")
    
    for window in ["last_7_days", "last_30_days", "all_time"]:
        if window not in summary:
            continue
        
        data = summary[window]
        title = window.replace('_', ' ').title()
        
        print(f"--- {title} ---")
        print(f"  Ratings: {data['total_ratings']} (avg: {data['avg_rating']}/5)")
        
        if data['model_performance']:
            print("  Model Performance:")
            for model, perf in sorted(data['model_performance'].items(), 
                                     key=lambda x: x[1]['success_rate'], reverse=True)[:3]:
                print(f"    - {model}: {perf['tasks']} tasks, {perf['success_rate']*100:.0f}% success")
        
        if data['skill_success']:
            print("  Top Skills:")
            for skill, rate in sorted(data['skill_success'].items(), 
                                    key=lambda x: x[1], reverse=True)[:3]:
                print(f"    - {skill}: {rate*100:.0f}% success")
        
        if data['top_failures']:
            print(f"  Top Failures: {', '.join(data['top_failures'][:3])}")
        
        print()


def load_summary() -> Optional[Dict]:
    """Load existing summary if available."""
    if SUMMARY_FILE.exists():
        try:
            with open(SUMMARY_FILE, 'r') as f:
                return json.load(f)
        except:
            return None
    return None


def maybe_update_summary():
    """Auto-update summary if needed (called after writes)."""
    # Check if we should update based on entry count
    entry_count = count_entries_fast()
    if entry_count % SUMMARY_UPDATE_INTERVAL == 0:
        summary = generate_summary()
        with open(SUMMARY_FILE, 'w') as f:
            json.dump(summary, f, indent=2)


def cmd_rate(args):
    """Log a manual rating."""
    rating = args.rating
    if not 1 <= rating <= 5:
        print("Error: Rating must be between 1 and 5", file=sys.stderr)
        sys.exit(1)
    
    entry = {
        "timestamp": get_timestamp(),
        "type": "manual_rating",
        "rating": rating,
    }
    
    if args.comment:
        entry["comment"] = args.comment
    
    if args.tags:
        entry["tags"] = args.tags.split(',')
    
    if args.context:
        entry["context"] = json.loads(args.context)
    
    if args.model:
        entry["model"] = args.model
    
    if args.skill:
        entry["skill"] = args.skill
    
    save_entry(entry)
    
    # Auto-update summary periodically
    maybe_update_summary()
    
    # Auto-archive if needed
    if args.auto_archive:
        cmd_archive(argparse.Namespace())
    
    print(f"✓ Rated {rating}/5")
    if args.comment:
        print(f"  Comment: {args.comment}")


def cmd_log(args):
    """Log an automated signal."""
    entry = {
        "timestamp": get_timestamp(),
        "type": "automated_signal",
    }
    
    if args.skill:
        entry["skill"] = args.skill
    if args.task:
        entry["task"] = args.task
    if args.status:
        entry["status"] = args.status
    if args.duration is not None:
        entry["duration"] = args.duration
    if args.exit_code is not None:
        entry["exit_code"] = args.exit_code
    if args.model:
        entry["model"] = args.model
    if args.error:
        entry["error"] = args.error
    if args.metadata:
        try:
            entry["metadata"] = json.loads(args.metadata)
        except json.JSONDecodeError:
            entry["metadata"] = {"raw": args.metadata}
    
    save_entry(entry)
    
    # Auto-update summary periodically
    maybe_update_summary()
    
    # Auto-archive if needed
    if args.auto_archive:
        cmd_archive(argparse.Namespace())
    
    parts = [f"✓ Logged signal"]
    if args.skill:
        parts.append(f"skill={args.skill}")
    if args.task:
        parts.append(f"task={args.task}")
    if args.status:
        parts.append(f"status={args.status}")
    
    print(" | ".join(parts))


def cmd_recent(args):
    """Show recent feedback entries."""
    entries = load_feedback(limit=args.limit)
    
    if not entries:
        print("No feedback entries found.")
        return
    
    print(f"=== Recent Feedback (Last {len(entries)} entries) ===\n")
    
    for entry in entries:
        ts = entry.get('timestamp', 'unknown')
        entry_type = entry.get('type', 'unknown')
        
        if entry_type == 'manual_rating':
            rating = entry.get('rating', '?')
            comment = entry.get('comment', '')
            print(f"[{ts}] Rating: {rating}/5 {comment}")
        
        elif entry_type == 'automated_signal':
            skill = entry.get('skill', 'unknown')
            task = entry.get('task', 'unknown')
            status = entry.get('status', 'unknown')
            duration = entry.get('duration')
            
            duration_str = f" ({duration}s)" if duration else ""
            print(f"[{ts}] {skill}/{task}: {status}{duration_str}")
        
        else:
            print(f"[{ts}] {entry_type}: {json.dumps(entry)}")


def cmd_search(args):
    """Search feedback entries using grep."""
    query = args.query
    
    # Search active file
    results = []
    
    if FEEDBACK_FILE.exists():
        try:
            result = subprocess.run(
                ['grep', '-i', query, str(FEEDBACK_FILE)],
                capture_output=True, text=True
            )
            if result.returncode == 0:
                for line in result.stdout.strip().split('\n'):
                    if line:
                        try:
                            results.append(json.loads(line))
                        except:
                            pass
        except:
            pass
    
    # Search archives if requested
    if args.include_archives:
        for archive_file in MEMORY_DIR.glob("feedback-archive-*.jsonl"):
            try:
                result = subprocess.run(
                    ['grep', '-i', query, str(archive_file)],
                    capture_output=True, text=True
                )
                if result.returncode == 0:
                    for line in result.stdout.strip().split('\n'):
                        if line:
                            try:
                                results.append(json.loads(line))
                            except:
                                pass
            except:
                pass
    
    if not results:
        print(f"No results found for '{query}'")
        return
    
    print(f"=== Search Results for '{query}' ({len(results)} matches) ===\n")
    
    for entry in results[:args.limit]:
        ts = entry.get('timestamp', 'unknown')
        entry_type = entry.get('type', 'unknown')
        
        if entry_type == 'manual_rating':
            rating = entry.get('rating', '?')
            comment = entry.get('comment', '')
            print(f"[{ts}] Rating: {rating}/5 - {comment}")
        elif entry_type == 'automated_signal':
            skill = entry.get('skill', 'unknown')
            status = entry.get('status', 'unknown')
            print(f"[{ts}] {skill}: {status}")
        else:
            print(f"[{ts}] {json.dumps(entry)[:100]}...")
    
    if len(results) > args.limit:
        print(f"\n... and {len(results) - args.limit} more (use --limit to see more)")


def cmd_stats(args):
    """Show summary statistics."""
    # Try summary first for performance
    summary = load_summary()
    
    if summary and not args.raw:
        # Use pre-computed summary
        print(f"=== Feedback Stats (from summary) ===\n")
        
        window = "last_7_days" if args.days and args.days <= 7 else \
                 "last_30_days" if args.days and args.days <= 30 else "all_time"
        
        data = summary.get(window, {})
        print(f"Total ratings: {data.get('total_ratings', 0)}")
        print(f"Average rating: {data.get('avg_rating', 0)}/5")
        print(f"Model performance: {len(data.get('model_performance', {}))} models")
        print(f"Skill success rates: {len(data.get('skill_success', {}))} skills")
        
        if args.verbose:
            print("\nModel Performance:")
            for model, perf in sorted(data.get('model_performance', {}).items(),
                                     key=lambda x: x[1].get('success_rate', 0), reverse=True):
                print(f"  - {model}: {perf['tasks']} tasks, {perf['success_rate']*100:.0f}%")
            
            print("\nSkill Success:")
            for skill, rate in sorted(data.get('skill_success', {}).items(),
                                     key=lambda x: x[1], reverse=True):
                print(f"  - {skill}: {rate*100:.0f}%")
        
        return
    
    # Fallback to raw data
    entries = load_feedback()
    
    if not entries:
        print("No feedback entries found.")
        return
    
    # Filter by days if specified
    if args.days:
        cutoff = datetime.now() - timedelta(days=args.days)
        entries = [
            e for e in entries 
            if parse_timestamp(e.get('timestamp', '2000-01-01')) > cutoff
        ]
    
    # Calculate stats
    total = len(entries)
    manual = [e for e in entries if e.get('type') == 'manual_rating']
    automated = [e for e in entries if e.get('type') == 'automated_signal']
    
    # Manual rating stats
    if manual:
        ratings = [e.get('rating', 0) for e in manual]
        avg_rating = sum(ratings) / len(ratings) if ratings else 0
    else:
        avg_rating = 0
    
    # Automated signal stats
    if automated:
        successes = sum(1 for e in automated if e.get('status') == 'success')
        failures = sum(1 for e in automated if e.get('status') == 'failure')
        total_auto = successes + failures
        success_rate = (successes / total_auto * 100) if total_auto > 0 else 0
    else:
        success_rate = 0
        successes = failures = 0
    
    # Print stats
    period = f" (Last {args.days} days)" if args.days else ""
    print(f"=== Feedback Stats{period} ===\n")
    print(f"Total entries: {total}")
    print(f"Manual ratings: {len(manual)} (avg: {avg_rating:.1f}/5)")
    print(f"Automated signals: {len(automated)}")
    print(f"Success rate: {success_rate:.1f}% ({successes}/{successes + failures})")
    
    # Top skills
    if automated:
        from collections import Counter
        skills = [e.get('skill', 'unknown') for e in automated if e.get('skill')]
        if skills:
            print("\nTop skills:")
            for skill, count in Counter(skills).most_common(5):
                print(f"  - {skill}: {count}")


def cmd_export(args):
    """Export feedback data to JSON."""
    # Load from all sources
    entries = load_feedback()
    
    if args.include_archives:
        entries.extend(load_archived_entries())
    
    # Filter by date range
    if args.since:
        since_dt = parse_timestamp(args.since)
        entries = [e for e in entries if parse_timestamp(e.get('timestamp', '2000-01-01')) >= since_dt]
    
    if args.until:
        until_dt = parse_timestamp(args.until)
        entries = [e for e in entries if parse_timestamp(e.get('timestamp', '2099-12-31')) <= until_dt]
    
    # Filter by status if specified
    if args.filter:
        key, value = args.filter.split('=', 1)
        entries = [e for e in entries if str(e.get(key, '')) == value]
    
    # Output
    output = json.dumps(entries, indent=2)
    
    if args.output and args.output != '-':
        with open(args.output, 'w') as f:
            f.write(output)
        print(f"✓ Exported {len(entries)} entries to {args.output}")
    else:
        print(output)


def cmd_list_archives(args):
    """List available archive files."""
    archives = sorted(MEMORY_DIR.glob("feedback-archive-*.jsonl"))
    
    if not archives:
        print("No archives found.")
        return
    
    print("=== Available Archives ===\n")
    
    total_entries = 0
    for archive in archives:
        # Count entries
        try:
            result = subprocess.run(['wc', '-l', str(archive)],
                                  capture_output=True, text=True)
            count = int(result.stdout.split()[0])
            total_entries += count
            print(f"  {archive.name}: {count} entries")
        except:
            print(f"  {archive.name}: ? entries")
    
    print(f"\nTotal archived: ~{total_entries} entries")


def main():
    parser = argparse.ArgumentParser(
        description="Feedback Loop - Track performance and ratings (Scale Edition)",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  %(prog)s rate 4 --comment "Good result"
  %(prog)s log --skill reddit --task post --status success --duration 45
  %(prog)s recent --limit 10
  %(prog)s stats --days 7
  %(prog)s summarize              # Generate rolling summaries
  %(prog)s archive                # Archive old entries
  %(prog)s search "reddit"        # Search with grep
        """
    )
    
    subparsers = parser.add_subparsers(dest='command', help='Command to run')
    
    # rate command
    rate_parser = subparsers.add_parser('rate', help='Log a manual rating (1-5)')
    rate_parser.add_argument('rating', type=int, help='Rating from 1-5')
    rate_parser.add_argument('--comment', '-c', help='Optional comment')
    rate_parser.add_argument('--tags', '-t', help='Comma-separated tags')
    rate_parser.add_argument('--context', help='JSON context data')
    rate_parser.add_argument('--model', '-m', help='Model used')
    rate_parser.add_argument('--skill', '-s', help='Skill name')
    rate_parser.add_argument('--auto-archive', action='store_true', help='Auto-archive old entries')
    rate_parser.set_defaults(func=cmd_rate)
    
    # log command
    log_parser = subparsers.add_parser('log', help='Log an automated signal')
    log_parser.add_argument('--skill', '-s', help='Skill name')
    log_parser.add_argument('--task', '-t', help='Task type')
    log_parser.add_argument('--status', choices=['success', 'failure'], help='Outcome status')
    log_parser.add_argument('--duration', type=int, help='Duration in seconds')
    log_parser.add_argument('--exit-code', type=int, help='Process exit code')
    log_parser.add_argument('--model', '-m', help='Model used')
    log_parser.add_argument('--error', '-e', help='Error message')
    log_parser.add_argument('--metadata', help='Additional JSON metadata')
    log_parser.add_argument('--auto-archive', action='store_true', help='Auto-archive old entries')
    log_parser.set_defaults(func=cmd_log)
    
    # recent command
    recent_parser = subparsers.add_parser('recent', help='Show recent feedback')
    recent_parser.add_argument('--limit', '-n', type=int, default=10, help='Number of entries')
    recent_parser.set_defaults(func=cmd_recent)
    
    # stats command
    stats_parser = subparsers.add_parser('stats', help='Show summary statistics')
    stats_parser.add_argument('--days', '-d', type=int, help='Limit to last N days')
    stats_parser.add_argument('--verbose', '-v', action='store_true', help='Show detailed stats')
    stats_parser.add_argument('--raw', action='store_true', help='Force raw data (ignore summary)')
    stats_parser.set_defaults(func=cmd_stats)
    
    # summarize command
    summarize_parser = subparsers.add_parser('summarize', help='Generate rolling summaries')
    summarize_parser.add_argument('--quiet', '-q', action='store_true', help='Suppress output')
    summarize_parser.set_defaults(func=cmd_summarize)
    
    # archive command
    archive_parser = subparsers.add_parser('archive', help='Archive old entries')
    archive_parser.set_defaults(func=cmd_archive)
    
    # search command
    search_parser = subparsers.add_parser('search', help='Search feedback entries')
    search_parser.add_argument('query', help='Search query')
    search_parser.add_argument('--limit', '-n', type=int, default=20, help='Max results')
    search_parser.add_argument('--include-archives', '-a', action='store_true', 
                              help='Include archived entries')
    search_parser.set_defaults(func=cmd_search)
    
    # export command
    export_parser = subparsers.add_parser('export', help='Export feedback data')
    export_parser.add_argument('--output', '-o', default='-', help='Output file (default: stdout)')
    export_parser.add_argument('--since', help='Start date (ISO format)')
    export_parser.add_argument('--until', help='End date (ISO format)')
    export_parser.add_argument('--filter', '-f', help='Filter by key=value')
    export_parser.add_argument('--include-archives', '-a', action='store_true',
                              help='Include archived entries')
    export_parser.set_defaults(func=cmd_export)
    
    # list-archives command
    list_archives_parser = subparsers.add_parser('list-archives', help='List archive files')
    list_archives_parser.set_defaults(func=cmd_list_archives)
    
    args = parser.parse_args()
    
    if not args.command:
        parser.print_help()
        sys.exit(1)
    
    args.func(args)


if __name__ == '__main__':
    main()
