# Subagent Reference

## When to Deploy Each Agent

## Research

### external-context-researcher
Use when integrating external APIs, services, libraries, or adopting new frameworks. Gathers official documentation and creates implementation guides.

### codebase-explorer
Use for non-trivial tasks (complexity >3/10) requiring understanding of existing code, patterns, or git history before proceeding.

### project-architect
Use only when starting brand new projects from scratch. Creates initial scaffolding, directory structure, and configuration files.

## Documentation

### docs-weaver
Use after implementing features, modifying APIs, or merging significant changes. Generates documentation with verified code examples from tests.

### project-historian
Use after major changes (>500 lines, architectural refactors, migrations, or milestones). Creates checkpoint narratives with semantic tags.

## UI

### browser-navigator
Use for automated end-to-end UI testing of local web applications. Tests interactivity, validates layouts, and repairs runtime bugs.

### ux-copy-brainstormer
Use when creating or refining user-facing copy. Requires brand voice guidelines. Reviews interface text for clarity and consistency.

## Backend

### migration-planner
Use when modifying database schemas, ORM models, or planning data migrations. Designs zero-downtime strategies with rollback procedures.

### cache-strategy-architect
Use when repeated expensive operations (DB queries, API calls, computations) are detected or when planning performance-critical features. Designs multi-layered caching strategies with invalidation and observability.

### performance-profiler
Use when API/view latency exceeds budgets, CPU/memory spikes occur, or before launching performance-critical features.

## Testing

### backend-test-guardian
Use after implementing backend features, when CI tests fail, or when initializing testing infrastructure for new projects.

### pre-push-validator
Use before pushing code to GitHub. Runs comprehensive checks: style, linting, type safety, tests, and build integrity.

## Security

### secrets-env-auditor
Use before every commit, push, or deployment. Scans for exposed credentials and validates environment variable documentation.

### security-scanner
Use after authentication/authorization changes, dependency updates, or for scheduled security assessments (SAST, CVE scanning).

## CI/CD

### cicd-optimizer
Use when CI/CD pipeline duration exceeds target thresholds or build times show degradation trends. Creates parallelization and caching strategies.
