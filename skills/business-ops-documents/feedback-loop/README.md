# Feedback Loop - Local Performance Tracking

A privacy-first feedback system for OpenClaw that tracks model performance, skill success rates, and usage patterns locally.

## Installation

1. Clone or copy this skill to your OpenClaw skills directory:
```bash
cp -r feedback-loop ~/clawd/indexsy-skills/
```

2. Ensure the memory directory exists:
```bash
mkdir -p ~/clawd/memory
```

3. No additional dependencies required - uses Python standard library only.

## Quick Start

```bash
# Navigate to the skill directory
cd ~/clawd/indexsy-skills/feedback-loop

# Log a manual rating (1-5 scale)
python feedback.py rate 4 --comment "Good result"

# Log a skill outcome
python feedback.py log --skill reddit --task post --status success --duration 45

# View recent feedback
python feedback.py recent --limit 10

# Run analysis
python analyze.py --days 7
```

## Core Features

- **Manual Ratings**: Rate interactions 1-5 with optional comments
- **Automated Capture**: Log skill outcomes, durations, and status
- **Local Storage**: All data stays in `memory/feedback.jsonl`
- **Analytics**: Model performance, skill success rates, failure patterns
- **Time Patterns**: Identify usage trends and peak times

## Data Privacy

All feedback data stays local:
- Stored in: `~/clawd/memory/feedback.jsonl`
- No external APIs called
- No data leaves your machine
- You own and control all data

## Command Reference

### feedback.py

| Command | Description |
|---------|-------------|
| `rate <1-5>` | Log manual rating |
| `log --skill X --task Y --status Z` | Log automated signal |
| `recent [--limit N]` | View recent entries |
| `stats [--days N]` | Show summary statistics |
| `export [--output path]` | Export data to JSON |

### analyze.py

| Flag | Description |
|------|-------------|
| `--days N` | Analyze last N days |
| `--models` | Model performance report |
| `--skills` | Skill success rates |
| `--failures` | Failure pattern analysis |
| `--time` | Time-based patterns |
| `--export path` | Export insights to JSON |

## File Structure

```
feedback-loop/
├── README.md         # This file
├── SKILL.md          # Full documentation
├── EXAMPLES.md       # Usage examples
├── feedback.py       # Core tracking script
└── analyze.py        # Analytics engine
```

## Contributing

This is a personal skill - modify and extend as needed for your workflow.

## License

MIT - Use freely in your OpenClaw setup.
