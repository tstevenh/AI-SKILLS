#!/usr/bin/env python3
"""
analyze.py - Analytics engine for feedback loop system

Analyzes feedback data to generate insights about:
- Model performance by task type
- Skill success rates
- Time-based patterns
- Failure pattern detection

Smart Loading: Uses pre-computed summaries for fast queries,
falls back to raw logs for detailed/custom analysis.
"""

import argparse
import json
import subprocess
import sys
from collections import Counter, defaultdict
from datetime import datetime, timedelta
from pathlib import Path
from typing import Dict, List, Any, Optional

# Configuration
MEMORY_DIR = Path.home() / "clawd" / "memory"
FEEDBACK_FILE = MEMORY_DIR / "feedback.jsonl"
SUMMARY_FILE = MEMORY_DIR / "feedback-summary.json"


def load_summary() -> Optional[Dict]:
    """Load pre-computed summary if available."""
    if SUMMARY_FILE.exists():
        try:
            with open(SUMMARY_FILE, 'r') as f:
                return json.load(f)
        except (json.JSONDecodeError, IOError):
            return None
    return None


def load_feedback(limit: Optional[int] = None) -> List[Dict]:
    """Load feedback entries from active file."""
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


def load_archived_entries(year_month: Optional[str] = None) -> List[Dict]:
    """Load archived entries for deeper analysis."""
    entries = []
    
    if year_month:
        archive_path = MEMORY_DIR / f"feedback-archive-{year_month}.jsonl"
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


def load_all_entries() -> List[Dict]:
    """Load all entries (active + archived)."""
    return load_feedback() + load_archived_entries()


def parse_timestamp(ts: str) -> datetime:
    """Parse ISO timestamp."""
    try:
        return datetime.fromisoformat(ts.replace('Z', '+00:00'))
    except (ValueError, AttributeError):
        return datetime.now()


def filter_by_days(entries: List[Dict], days: int) -> List[Dict]:
    """Filter entries to last N days."""
    if not days:
        return entries
    
    cutoff = datetime.now() - timedelta(days=days)
    return [
        e for e in entries
        if parse_timestamp(e.get('timestamp', '2000-01-01')) > cutoff
    ]


class SummaryAnalyzer:
    """Fast analysis using pre-computed summaries."""
    
    def __init__(self, summary: Dict):
        self.summary = summary
    
    def get_window(self, days: Optional[int] = None) -> Dict:
        """Get appropriate time window from summary."""
        if days and days <= 7:
            return self.summary.get('last_7_days', {})
        elif days and days <= 30:
            return self.summary.get('last_30_days', {})
        else:
            return self.summary.get('all_time', {})
    
    def overall(self, days: Optional[int] = None) -> Dict[str, Any]:
        """Get overall statistics."""
        data = self.get_window(days)
        
        return {
            "total_ratings": data.get('total_ratings', 0),
            "avg_rating": data.get('avg_rating', 0),
            "model_count": len(data.get('model_performance', {})),
            "skill_count": len(data.get('skill_success', {})),
            "top_failures": data.get('top_failures', [])
        }
    
    def models(self, days: Optional[int] = None) -> Dict[str, Any]:
        """Get model performance."""
        data = self.get_window(days)
        return data.get('model_performance', {})
    
    def skills(self, days: Optional[int] = None) -> Dict[str, Any]:
        """Get skill success rates."""
        data = self.get_window(days)
        skills_data = data.get('skill_success', {})
        
        # Convert to detailed format
        result = {}
        for skill, rate in skills_data.items():
            result[skill] = {
                "success_rate": rate * 100,  # Convert to percentage
                "tasks": "N/A (from summary)"  # Summary doesn't have exact counts
            }
        return result
    
    def failures(self, days: Optional[int] = None) -> Dict[str, Any]:
        """Get failure patterns."""
        data = self.get_window(days)
        return {
            "top_failures": data.get('top_failures', []),
            "message": "Failure patterns from summary (use --deep for full analysis)"
        }


class RawAnalyzer:
    """Deep analysis using raw log data."""
    
    def __init__(self, entries: List[Dict]):
        self.entries = entries
    
    def overall(self) -> Dict[str, Any]:
        """Generate overall statistics."""
        total = len(self.entries)
        manual = [e for e in self.entries if e.get('type') == 'manual_rating']
        automated = [e for e in self.entries if e.get('type') == 'automated_signal']
        
        # Manual ratings
        if manual:
            ratings = [e.get('rating', 0) for e in manual]
            avg_rating = sum(ratings) / len(ratings)
            rating_dist = Counter(ratings)
        else:
            avg_rating = 0
            rating_dist = Counter()
        
        # Automated signals
        if automated:
            statuses = [e.get('status') for e in automated]
            status_counts = Counter(statuses)
            success_rate = status_counts.get('success', 0) / len(automated) * 100 if automated else 0
        else:
            status_counts = Counter()
            success_rate = 0
        
        return {
            "total_entries": total,
            "manual_ratings": {
                "count": len(manual),
                "average": round(avg_rating, 2),
                "distribution": dict(rating_dist)
            },
            "automated_signals": {
                "count": len(automated),
                "status_counts": dict(status_counts),
                "success_rate": round(success_rate, 1)
            }
        }
    
    def models(self) -> Dict[str, Any]:
        """Analyze model performance."""
        automated = [e for e in self.entries if e.get('type') == 'automated_signal']
        
        models = defaultdict(lambda: {"tasks": 0, "successes": 0, "failures": 0, "ratings": [], "durations": []})
        
        for entry in automated:
            model = entry.get('model', 'unknown')
            models[model]["tasks"] += 1
            
            if entry.get('status') == 'success':
                models[model]["successes"] += 1
            elif entry.get('status') == 'failure':
                models[model]["failures"] += 1
            
            if entry.get('duration'):
                models[model]["durations"].append(entry['duration'])
        
        # Add manual ratings by model
        manual = [e for e in self.entries if e.get('type') == 'manual_rating']
        for entry in manual:
            context = entry.get('context', {})
            model = context.get('model', entry.get('model', 'unknown'))
            if model in models:
                models[model]["ratings"].append(entry.get('rating', 0))
        
        # Calculate stats
        results = {}
        for model, data in models.items():
            total = data["successes"] + data["failures"]
            results[model] = {
                "tasks": data["tasks"],
                "success_rate": round(data["successes"] / total * 100, 1) if total > 0 else 0,
                "avg_rating": round(sum(data["ratings"]) / len(data["ratings"]), 2) if data["ratings"] else None,
                "avg_duration": round(sum(data["durations"]) / len(data["durations"]), 1) if data["durations"] else None
            }
        
        return results
    
    def skills(self) -> Dict[str, Any]:
        """Analyze skill success rates."""
        automated = [e for e in self.entries if e.get('type') == 'automated_signal']
        
        skills = defaultdict(lambda: {"tasks": 0, "successes": 0, "failures": 0, "durations": []})
        
        for entry in automated:
            skill = entry.get('skill', 'unknown')
            skills[skill]["tasks"] += 1
            
            if entry.get('status') == 'success':
                skills[skill]["successes"] += 1
            elif entry.get('status') == 'failure':
                skills[skill]["failures"] += 1
            
            if entry.get('duration'):
                skills[skill]["durations"].append(entry['duration'])
        
        # Calculate stats
        results = {}
        for skill, data in skills.items():
            total = data["successes"] + data["failures"]
            results[skill] = {
                "tasks": data["tasks"],
                "successes": data["successes"],
                "failures": data["failures"],
                "success_rate": round(data["successes"] / total * 100, 1) if total > 0 else 0,
                "avg_duration": round(sum(data["durations"]) / len(data["durations"]), 1) if data["durations"] else None
            }
        
        # Sort by success rate
        return dict(sorted(results.items(), key=lambda x: x[1]["success_rate"], reverse=True))
    
    def failures(self) -> Dict[str, Any]:
        """Analyze failure patterns."""
        failures = [e for e in self.entries if e.get('status') == 'failure']
        
        if not failures:
            return {"message": "No failures recorded"}
        
        # Group by skill and error type
        patterns = defaultdict(lambda: {"count": 0, "errors": []})
        
        for entry in failures:
            skill = entry.get('skill', 'unknown')
            error = entry.get('error', 'unspecified')
            key = f"{skill}:{error}"
            
            patterns[key]["count"] += 1
            patterns[key]["skill"] = skill
            patterns[key]["error"] = error
        
        # Get top patterns
        sorted_patterns = sorted(patterns.items(), key=lambda x: x[1]["count"], reverse=True)
        
        # Also check by skill alone
        skill_failures = Counter(e.get('skill', 'unknown') for e in failures)
        
        return {
            "total_failures": len(failures),
            "failures_by_skill": dict(skill_failures.most_common()),
            "common_patterns": [
                {"skill": p[1]["skill"], "error": p[1]["error"], "count": p[1]["count"]}
                for p in sorted_patterns[:10]
            ]
        }
    
    def time_patterns(self) -> Dict[str, Any]:
        """Analyze time-based patterns."""
        if not self.entries:
            return {"message": "No data available"}
        
        # Extract hour from timestamps
        hours = []
        weekdays = []
        
        for entry in self.entries:
            try:
                ts = parse_timestamp(entry['timestamp'])
                hours.append(ts.hour)
                weekdays.append(ts.strftime('%A'))
            except (KeyError, ValueError):
                continue
        
        hour_dist = Counter(hours)
        weekday_dist = Counter(weekdays)
        
        # Peak hours
        peak_hours = sorted(hour_dist.items(), key=lambda x: x[1], reverse=True)[:3]
        
        # Ratings by time of day
        ratings_by_hour = defaultdict(list)
        for entry in self.entries:
            if entry.get('type') == 'manual_rating':
                try:
                    ts = parse_timestamp(entry['timestamp'])
                    ratings_by_hour[ts.hour].append(entry.get('rating', 0))
                except (KeyError, ValueError):
                    continue
        
        avg_rating_by_hour = {
            h: round(sum(r) / len(r), 2) for h, r in ratings_by_hour.items()
        }
        
        return {
            "peak_hours": [h[0] for h in peak_hours],
            "hourly_distribution": dict(sorted(hour_dist.items())),
            "weekday_distribution": dict(weekday_dist),
            "avg_rating_by_hour": dict(sorted(avg_rating_by_hour.items()))
        }


def search_with_grep(query: str, include_archives: bool = False) -> List[Dict]:
    """Search entries using grep for fast targeted queries."""
    results = []
    
    # Search active file
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
    if include_archives:
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
    
    return results


def print_overall(stats: Dict, source: str = "summary"):
    """Print overall statistics."""
    if source == "summary":
        print(f"Total ratings: {stats['total_ratings']}")
        print(f"Average rating: {stats['avg_rating']}/5")
        if stats.get('top_failures'):
            print(f"Top issues: {', '.join(stats['top_failures'][:3])}")
    else:
        print(f"Total entries: {stats['total_entries']}")
        
        manual = stats['manual_ratings']
        print(f"Manual ratings: {manual['count']} (avg: {manual['average']}/5)")
        if manual['distribution']:
            print("  Distribution:", end="")
            for rating, count in sorted(manual['distribution'].items()):
                print(f" {rating}★:{count}", end="")
            print()
        
        auto = stats['automated_signals']
        print(f"Automated signals: {auto['count']}")
        print(f"Success rate: {auto['success_rate']}%")
    print()


def print_models(models: Dict, source: str = "summary"):
    """Print model performance."""
    if not models:
        print("No model data available.")
        return
    
    if source == "summary":
        print(f"{'Model':<25} {'Tasks':<10} {'Success Rate'}")
        print("-" * 50)
        for model, data in sorted(models.items(), key=lambda x: x[1].get('success_rate', 0), reverse=True):
            print(f"{model:<25} {data['tasks']:<10} {data['success_rate']*100:.0f}%")
    else:
        print(f"{'Model':<25} {'Tasks':<8} {'Success':<10} {'Rating':<8} {'Avg Time'}")
        print("-" * 65)
        
        for model, data in models.items():
            success = f"{data['success_rate']}%"
            rating = f"{data['avg_rating']}/5" if data['avg_rating'] else "-"
            duration = f"{data['avg_duration']}s" if data['avg_duration'] else "-"
            print(f"{model:<25} {data['tasks']:<8} {success:<10} {rating:<8} {duration}")
    print()


def print_skills(skills: Dict, source: str = "summary"):
    """Print skill success rates."""
    if not skills:
        print("No skill data available.")
        return
    
    if source == "summary":
        print(f"{'Skill':<20} {'Success Rate'}")
        print("-" * 35)
        # Handle both format where rate could be 0-1 or already 0-100
        def get_rate(v):
            if isinstance(v, dict):
                r = v.get('success_rate', 0)
            else:
                r = v
            # If rate > 1, it's probably already a percentage
            return r if r > 1 else r * 100
        for skill, rate_data in sorted(skills.items(), key=lambda x: get_rate(x[1]), reverse=True):
            rate = get_rate(rate_data)
            print(f"{skill:<20} {rate:.0f}%")
    else:
        print(f"{'Skill':<20} {'Tasks':<8} {'Success':<10} {'Fail':<8} {'Rate':<8} {'Avg Time'}")
        print("-" * 70)
        
        for skill, data in skills.items():
            success_rate = f"{data['success_rate']}%"
            duration = f"{data['avg_duration']}s" if data['avg_duration'] else "-"
            print(f"{skill:<20} {data['tasks']:<8} {data['successes']:<10} {data['failures']:<8} {success_rate:<8} {duration}")
    print()


def print_failures(failures: Dict, source: str = "summary"):
    """Print failure analysis."""
    if "message" in failures:
        print(failures["message"])
        return
    
    if source == "summary":
        print("Top failure patterns:")
        for pattern in failures.get('top_failures', []):
            print(f"  - {pattern}")
    else:
        print(f"Total failures: {failures['total_failures']}")
        print("\nFailures by skill:")
        for skill, count in failures['failures_by_skill'].items():
            print(f"  - {skill}: {count}")
        
        print("\nCommon patterns:")
        for pattern in failures['common_patterns'][:5]:
            print(f"  - {pattern['skill']}: {pattern['error']} ({pattern['count']} times)")
    print()


def print_time_patterns(patterns: Dict):
    """Print time-based patterns."""
    if "message" in patterns:
        print(patterns["message"])
        return
    
    print(f"Peak hours: {', '.join(f'{h}:00' for h in patterns['peak_hours'])}")
    
    print("\nWeekday distribution:")
    for day, count in patterns['weekday_distribution'].items():
        print(f"  - {day}: {count}")
    
    if patterns['avg_rating_by_hour']:
        print("\nBest-rated hours (avg rating):")
        sorted_ratings = sorted(patterns['avg_rating_by_hour'].items(), key=lambda x: x[1], reverse=True)
        for hour, rating in sorted_ratings[:3]:
            print(f"  - {hour}:00: {rating}/5")
    print()


def main():
    parser = argparse.ArgumentParser(
        description="Analyze feedback data for insights (Smart Loading Edition)",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  %(prog)s --days 7                    # Fast summary-based analysis
  %(prog)s --deep --days 30            # Deep analysis with raw logs
  %(prog)s --search "reddit"           # Grep-based search
  %(prog)s --models --deep             # Force raw data for models
  %(prog)s --export insights.json      # Export all insights

Smart Loading:
  By default, uses pre-computed summaries for instant results.
  Use --deep to force analysis of raw log data (slower, more detailed).
        """
    )
    
    parser.add_argument('--days', '-d', type=int, help='Analyze last N days')
    parser.add_argument('--models', '-m', action='store_true', help='Model performance report')
    parser.add_argument('--skills', '-s', action='store_true', help='Skill success rates')
    parser.add_argument('--failures', '-f', action='store_true', help='Failure pattern analysis')
    parser.add_argument('--time', '-t', action='store_true', help='Time-based patterns')
    parser.add_argument('--all', '-a', action='store_true', help='Show all analyses')
    parser.add_argument('--export', '-o', help='Export insights to JSON file')
    parser.add_argument('--deep', action='store_true', help='Force raw log analysis (ignore summary)')
    parser.add_argument('--search', help='Search for specific term (uses grep)')
    parser.add_argument('--include-archives', action='store_true', help='Include archived data')
    
    args = parser.parse_args()
    
    # Handle search separately (fast path)
    if args.search:
        results = search_with_grep(args.search, args.include_archives)
        print(f"=== Search Results for '{args.search}' ({len(results)} matches) ===\n")
        for entry in results[:20]:
            ts = entry.get('timestamp', 'unknown')
            entry_type = entry.get('type', 'unknown')
            if entry_type == 'manual_rating':
                print(f"[{ts}] Rating: {entry.get('rating', '?')}/5 - {entry.get('comment', '')}")
            elif entry_type == 'automated_signal':
                print(f"[{ts}] {entry.get('skill', 'unknown')}: {entry.get('status', 'unknown')}")
        return
    
    # Determine analysis mode
    use_summary = not args.deep
    summary = None
    
    if use_summary:
        summary = load_summary()
        if summary:
            print("ℹ️  Using pre-computed summary for fast analysis (use --deep for raw data)\n")
        else:
            print("⚠️  No summary found, falling back to raw data analysis")
            print("   Run: python feedback.py summarize\n")
    
    # Initialize analyzer
    if summary and use_summary:
        analyzer = SummaryAnalyzer(summary)
        source = "summary"
    else:
        # Load raw data
        if args.include_archives:
            entries = load_all_entries()
        else:
            entries = load_feedback()
        
        entries = filter_by_days(entries, args.days)
        
        if not entries:
            print("No feedback data found. Start logging with feedback.py")
            sys.exit(0)
        
        analyzer = RawAnalyzer(entries)
        source = "raw"
    
    # Determine what to analyze
    show_all = args.all or not any([args.models, args.skills, args.failures, args.time])
    
    insights = {}
    
    # Overall stats (always included)
    if show_all:
        period = f" (Last {args.days} days)" if args.days else ""
        print(f"=== Feedback Analysis{period} [{source}] ===\n")
        overall = analyzer.overall(args.days if source == "summary" else None)
        print_overall(overall, source)
        insights['overall'] = overall
    
    # Model performance
    if args.models or show_all:
        if show_all:
            print("=== Model Performance ===")
        models = analyzer.models(args.days if source == "summary" else None)
        print_models(models, source)
        insights['models'] = models
    
    # Skill success rates
    if args.skills or show_all:
        if show_all:
            print("=== Skill Success Rates ===")
        skills = analyzer.skills(args.days if source == "summary" else None)
        print_skills(skills, source)
        insights['skills'] = skills
    
    # Failure patterns
    if args.failures or show_all:
        if show_all:
            print("=== Failure Analysis ===")
        failures = analyzer.failures() if source == "raw" else analyzer.failures(args.days)
        print_failures(failures, source)
        insights['failures'] = failures
    
    # Time patterns (only from raw data)
    if (args.time or show_all) and source == "raw":
        if show_all:
            print("=== Time Patterns ===")
        time_patterns = analyzer.time_patterns()
        print_time_patterns(time_patterns)
        insights['time_patterns'] = time_patterns
    elif (args.time or show_all) and source == "summary":
        print("=== Time Patterns ===")
        print("(Time patterns require --deep mode for full analysis)\n")
    
    # Export if requested
    if args.export:
        with open(args.export, 'w') as f:
            json.dump(insights, f, indent=2)
        print(f"✓ Exported insights to {args.export}")


if __name__ == '__main__':
    main()
