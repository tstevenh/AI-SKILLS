# Duplicate Skill Audit

This repo now uses a single canonical `skills/` library.

## Versioned duplicates collapsed

### Claude Code Kit

Compared:

- `Claude Code Kit/v4.5 - Opus Optimized!/v4.5/.claude/skills/`
- `Claude Code Kit/v4.6 - New Task Management/v4.6/.claude/skills/`

Decision:

- Keep v4.6 as canonical.
- v4.6 had 8 extra files and 58 changed shared files, so it is a true successor rather than a copy.

### Growth Kit

Compared:

- `Claude Code Kit/v1.5-Growth-Kit-Seo-Edition/growth-kit/`
- `Claude Code Kit/v2-Growth-Kit-(SEOBoost+CRO)/growth-kit/`

Decision:

- Keep v2 as canonical.
- v2 adds CRO, growth loops, paid ads, pricing, and broader SEO coverage.

## Cross-pack duplicates merged directly

### `direct-response-copy`

- Base logic: Vibe
- Donor improvements: Jacky
- Canonical result: stronger trigger metadata and writing voice, plus better intake, awareness matching, and DR checklisting

### `keyword-research`

- Base logic: Vibe
- Donor improvements: Jacky
- Canonical result: strategy-first clustering plus optional SERP, gap, weakness, and cannibalization analysis

### `newsletter`

- Base logic: Vibe
- Donor improvements: Jacky
- Canonical result: editorial issue-writing plus growth, monetization, and operator workflows

### `seo-content`

- Base logic: Vibe
- Donor improvements: Jacky, Claude Code Kit, James Goldbach
- Canonical result: human-first SEO article workflow plus AI-search, E-E-A-T, tiered execution, and brand consistency

## Similar clusters that are now merged

### `frontend`

Sources merged:

- `Claude Code Kit/.../frontend-design`
- `James Goldbach Skool/skills/frontend`
- `skills-Jacky/web-design`

Base choice:

- `skills-Jacky/web-design` for its richer design references and inspiration files

Donor additions:

- `James Goldbach Skool/skills/frontend` scripts and implementation references
- `frontend-design` aesthetic and anti-generic design direction

Canonical result:

- one skill that covers frontend design direction, component implementation, performance, responsiveness, and UI review

### `security`

Sources merged:

- `James Goldbach Skool/skills/security`
- `James Goldbach Skool/skills/security-ops`
- `skills-Jacky/penetration-testing`
- `skills-Jacky/prompt-injection-defense`

Base choice:

- `skills-Jacky/penetration-testing` for the deepest reference corpus

Donor additions:

- James security engineering scripts and references
- James secops scanning/compliance scripts and references
- prompt injection defense references for agentic and research workflows

Canonical result:

- one security skill with architecture, secops, pentest, and LLM-agent defense modes

### `testing`

Sources merged:

- `James Goldbach Skool/skills/qa-testing`
- `James Goldbach Skool/skills/web-testing`
- `skills-Jacky/functionality-qa`
- `skills-Jacky/design-qa`
- `skills-Jacky/adversarial-qa`

Base choice:

- `skills-Jacky/functionality-qa` for the broadest functional QA foundation

Donor additions:

- Playwright/browser scripts from `web-testing`
- generic QA scripts and references from `qa-testing`
- visual QA corpus from `design-qa`
- break-it and abuse-testing corpus from `adversarial-qa`

Canonical result:

- one testing skill that covers functional QA, browser automation, design QA, and adversarial testing

## Notable gap kept for follow-up

- `skills-Jacky/README.md` references a merged `seo-auditor`, but that skill does not exist in the repo snapshot. That should be rebuilt separately if you want a canonical SEO audit skill.
