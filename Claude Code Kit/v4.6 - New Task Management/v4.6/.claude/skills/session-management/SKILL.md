---
name: session-management
description: "Complete session-based development workflow for implementation tasks"
---

# Session-Based Workflow System

Use this skill for multi-phase implementations requiring coordination across specialists.

---

## Quick Reference: Session Types

| Type            | When to Use                           | Key Protocol                               |
| --------------- | ------------------------------------- | ------------------------------------------ |
| **Development** | Building features, implementing plans | Design-first, batch execution              |
| **Debugging**   | Fixing bugs, investigating failures   | Iron law: root cause before fix            |
| **Migration**   | Refactoring, replacing code           | Feature inventory required                 |
| **Review**      | Code review (self or peer)            | Technical rigor, no performative agreement |
| **TDD**         | Test-driven development               | RED-GREEN-REFACTOR cycle                   |
| **Research**    | Investigation, exploration            | No implementation until complete           |

**Session type files**: `session-types/*.md`

---

## Cross-Cutting Practices

These apply to ALL session types:

| Practice              | Purpose                           | File                             |
| --------------------- | --------------------------------- | -------------------------------- |
| **Verification**      | Evidence before completion claims | `practices/verification.md`      |
| **Branch Completion** | Finishing work on branches        | `practices/branch-completion.md` |

**Note**: For parallel vs sequential agent dispatch rules, see the `sub-agent-invocation` skill.

---

## Architecture

```
┌─────────────────────────────────────────────────────────────────────┐
│                    SESSION-BASED SYSTEM                             │
├─────────────────────────────────────────────────────────────────────┤
│                                                                     │
│  ┌──────────────┐    ┌─────────────────┐    ┌─────────────────────┐ │
│  │ CENTRAL AI   │    │ MASTER          │    │ SESSION FILES       │ │
│  │ Coordinator  │◄──►│ ORCHESTRATOR    │◄──►│ .claude/tasks/      │ │
│  │              │    │ Strategic Plan  │    │ Source of Truth     │ │
│  └──────────────┘    └─────────────────┘    └─────────────────────┘ │
│         │                      │                       │            │
│         │              ┌───────────────────┐           │            │
│         └─────────────►│ SESSION PIPELINE  │◄──────────┘            │
│                        │ Task Management   │                        │
│                        │ TaskList Sync     │                        │
│                        └───────────────────┘                        │
│                                 │                                   │
│  ┌──────────────────────────────┼─────────────────────────────────┐ │
│  │         SPECIALIST AGENTS    │                                 │ │
│  │  ┌─────────────┐ ┌─────────────┐ ┌─────────────┐               │ │
│  │  │ Frontend    │ │ Backend     │ │ Supabase    │               │ │
│  │  │ Specialist  │ │ Engineer    │ │ Specialist  │               │ │
│  │  └─────────────┘ └─────────────┘ └─────────────┘               │ │
│  │  ┌─────────────┐ ┌─────────────┐ ┌─────────────┐               │ │
│  │  │ Quality     │ │ Security    │ │ Performance │               │ │
│  │  │ Engineer    │ │ Auditor     │ │ Optimizer   │               │ │
│  │  └─────────────┘ └─────────────┘ └─────────────┘               │ │
│  └────────────────────────────────────────────────────────────────┘ │
└─────────────────────────────────────────────────────────────────────┘
```

---

## Session Status Lifecycle

```
PENDING → IN_PROGRESS → COMPLETE → VERIFIED
```

- **PENDING**: Session created, work not started
- **IN_PROGRESS**: Active work underway
- **COMPLETE**: All tasks done, awaiting verification
- **VERIFIED**: Verification passed, ready to archive

**Rule**: Update status as work progresses. Mark tasks `[x]` immediately upon completion.

---

## 6-Phase Session Flow

### Phase 1: Request Analysis & Initialization

**Central AI → Master Orchestrator**:

```
"USER'S ORIGINAL REQUEST: [verbatim request]

INITIALIZATION REQUIREMENTS:
- Create session file in .claude/tasks/
- Analyze complexity and scope
- Determine session type (Development/Debugging/Migration/Review/TDD/Research)
- Break down into atomic tasks (1-4 hours each)
- Assign to appropriate specialists

Think hard and provide comprehensive session planning."
```

**Output**: `session-current.md` with request, session type, success criteria, task breakdown.

---

### Phase 2: Research & Planning

**Knowledge Hierarchy**:

1. **Priority 1**: Relevant skills, session history, existing codebase patterns
2. **Priority 2**: Search project for code examples, extract architectural decisions
3. **Priority 3**: WebSearch for external best practices (when internal insufficient)

**Task Breakdown Requirements**:

- Atomic tasks (1-4 hours max)
- TaskList-compatible checklists (use TaskCreate for each item)
- Specialist assignment
- Parallel vs sequential execution plan
- Define dependencies with `addBlockedBy` / `addBlocks` parameters

---

### Phase 3: Task List Synchronization

Session checklists **must mirror the Task list**:

```markdown
# Session File:

- [ ] Task 1
- [ ] Task 2

# Task Tools:

TaskCreate(subject="Task 1", description="...", activeForm="Working on Task 1")
TaskCreate(subject="Task 2", description="...", activeForm="Working on Task 2")

# Set dependencies:

TaskUpdate(taskId="2", addBlockedBy=["1"])

# Update status as work progresses:

TaskUpdate(taskId="1", status="in_progress")
TaskUpdate(taskId="1", status="completed")
```

**Cross-Session Collaboration**:

For multi-agent or multi-session work, set environment variable:

```bash
CLAUDE_CODE_TASK_LIST_ID=project-name claude
```

This enables multiple Claude sessions to share and coordinate on the same task list.

**Central AI Coordination**:

1. Read session file for complete context
2. Create tasks with `TaskCreate`, set dependencies with `TaskUpdate`
3. Invoke specialists (parallel or sequential per `sub-agent-invocation` skill)
4. Monitor progress via `TaskList` and session updates
5. Press `Ctrl+T` to toggle task visibility in terminal

---

### Phase 4: Agent Execution

**Specialist Workflow**:

1. Read `session-current.md` for full context
2. Review prior agent work (dependencies)
3. Execute assigned tasks (following session type protocols)
4. Update session with implementation notes
5. Update Task status via `TaskUpdate(taskId, status="completed")` immediately
6. Prepare handoff context for next agent

**Session Update Pattern**:

```markdown
### [Agent Name] Work

**Status**: Completed
**Tasks Completed**:

- ✅ Task 1 - [brief outcome]

**Implementation Notes**: [Key decisions, patterns used]
**Next Agent Context**: [What next agent needs to know]
```

---

### Phase 5: Quality Gates

| Level               | Validation                                                   |
| ------------------- | ------------------------------------------------------------ |
| **Implementation**  | Code compiles, basic functionality works, local testing done |
| **Integration**     | API contracts validated, cross-component compatibility       |
| **Quality**         | Tests passing, performance benchmarks met                    |
| **User Acceptance** | User approves, business requirements met                     |

**Apply verification practice** (`practices/verification.md`) before claiming completion.

---

### Phase 6: Commit & Archive

Load the `git-commits` skill for commit creation.
Apply `practices/branch-completion.md` for branch handling.

**Session Continuity**:

- Extract incomplete work to new session
- Reference prior sessions for context
- `session-current.md` → archive in `.claude/tasks/archive/` after completion

---

## Session File Template

```markdown
# Session - [Title]

## Session Overview

**User Request**: [Verbatim user request]
**Session Type**: Development / Debugging / Migration / Review / TDD / Research
**Status**: `PENDING`
**Success Criteria**: [What defines completion]
**Quality Gates**: [Validation checkpoints]

## Strategic Analysis

**Complexity Assessment**: Simple / Complex
**Domain Coverage**: [List of domains involved]
**Dependencies**: [Internal and external dependencies]
**Risk Factors**: [Potential challenges]

## Task Breakdown

### Phase 1: [Phase Name]

**Assigned To**: [Specialist agent]

- [ ] Task 1 - [Specific implementation detail]
- [ ] Task 2 - [Specific implementation detail]

### Phase 2: [Phase Name]

**Assigned To**: [Specialist agent]

- [ ] Task 1 - [Specific implementation detail]

## Agent Work Sections

### Master Orchestrator

**Status**: Completed
**Planning Notes**: [Strategic decisions made]
**Research Findings**: [Key discoveries and context]

### [Specialist Agent Name]

**Status**: In Progress / Completed
**Tasks Completed**:

- ✅ Task 1 - [brief outcome]

**Implementation Notes**: [What was built, how, why]
**Integration Points**: [How it connects to other work]
**Next Agent Context**: [What next agent needs to know]

## Session Metrics

**Tasks Total**: X
**Tasks Completed**: Y
**Blockers**: [Any impediments]
**Follow-up Items**: [Work for next session]

## Quality Validation

- [ ] All tests passing
- [ ] Performance benchmarks met
- [ ] Security standards validated
- [ ] User acceptance achieved
- [ ] Verification evidence provided
```

---

## Directory Structure

```
session-management/
├── SKILL.md                    # This file - core orchestration
├── session-types/
│   ├── development.md          # Feature development sessions
│   ├── debugging.md            # Bug fixing sessions
│   ├── migration.md            # Refactoring/migration sessions
│   ├── review.md               # Code review sessions
│   ├── tdd.md                  # Test-driven development sessions
│   └── research.md             # Investigation sessions
└── practices/
    ├── verification.md         # Evidence-before-completion protocol
    └── branch-completion.md    # Branch finishing workflow
```

---

## Loading Session Type Protocols

When starting a session, load the appropriate type:

```markdown
# For debugging work:

Read: session-types/debugging.md

# For migrations:

Read: session-types/migration.md

# For TDD:

Read: session-types/tdd.md
```

The session type file contains specific protocols, checklists, and workflow requirements for that type of work.
