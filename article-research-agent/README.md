# Article Research Agent

A multi-agent research and writing system for Claude Desktop. Researches 15-30 sources and writes articles in Harry's voice.

## Structure

```
article-research-agent/
├── CLAUDE.md                          # Main orchestrator (upload this)
├── harry-writing-style.md             # Writing style guide
├── README.md                          # This file
└── research-agents/
    ├── background-agent.md            # Context & foundation
    ├── data-agent.md                  # Statistics & numbers
    ├── examples-agent.md              # Case studies
    ├── experts-agent.md               # Quotes & opinions
    ├── criticism-agent.md             # Contrarian views
    └── trends-agent.md               # Breaking news & trends
```

## Setup

### Prerequisites
- Claude Desktop app (or Claude Code)
- Firecrawl MCP configured (recommended) or web search access

### Firecrawl MCP Setup
1. Open Claude Desktop → Settings → Developer → MCP Servers
2. Add Firecrawl with your API key
3. Get an API key at https://firecrawl.dev

## How to Use

### Option 1: Upload to Conversation (Quick)
1. Open Claude Desktop
2. Start new conversation
3. Upload `CLAUDE.md`
4. Say: "Write an article about [your topic]"
5. Wait 10-20 minutes while agent researches and writes

### Option 2: Set Up as Project (Repeated Use)
1. Create new Project in Claude Desktop
2. Upload ALL files as Project Knowledge
3. Any conversation in that project can use the agent
4. Just say: "Write an article about [topic]"

## Commands

- **Default**: Full research pipeline, 2,000-2,500 word article
- **"Quick"**: Reduced research, 1,000-1,500 word article
- **"More data"**: Double the data research
- **"More examples"**: Double the case study research
- **"Shorter"**: 1,000-1,500 words
- **"Longer"**: 3,000-4,000 words
- **"Thread format"**: Output as X/Twitter thread

## What You Get

1. Complete article in Harry's voice
2. Research summary with key findings
3. Full source list with URLs
4. 3-5 headline options

## Tips

- The more specific your brief, the better the output
- Include a "villain" or conventional wisdom to challenge
- Mention specific companies/people to research
- Specify your angle — what makes this take unique
