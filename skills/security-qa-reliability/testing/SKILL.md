---
name: testing
description: "Comprehensive testing skill for functional QA, browser automation, design QA, and adversarial validation. Use when designing test plans, writing or running tests, checking UX and visual quality, automating browser workflows, or actively trying to break user flows and system assumptions."
---

# Testing

This is the merged testing skill for the repo.

It combines:

- functional QA
- browser and E2E automation
- design and visual QA
- adversarial and abuse-oriented testing

## Modes

### 1. Functional QA

Use for:

- requirements coverage
- regression planning
- form, API, auth, payments, and workflow validation

### 2. Browser automation

Use for:

- local app walkthroughs
- Playwright-style verification
- reproducing UI bugs
- scripted E2E flows

### 3. Design QA

Use for:

- visual regressions
- spacing, typography, and consistency checks
- responsive review
- accessibility-oriented visual checks

### 4. Adversarial testing

Use for:

- edge-case discovery
- stress and abuse scenarios
- race-condition thinking
- failure-mode and break-it validation

## Core workflow

Use this order:

`REQUIREMENTS -> HAPPY PATH -> EDGE CASES -> AUTOMATION -> VISUAL CHECKS -> ADVERSARIAL PASS -> REPORT`

### Requirements

Identify:

- critical user journeys
- business-critical failure points
- integrations
- assumptions that must hold true

### Happy path

Confirm the product works for normal use before attempting to break it.

### Edge cases

Then expand to:

- invalid inputs
- missing data
- retries and timeouts
- state transitions
- role and permission changes
- mobile and narrow-screen behavior

### Automation

Use the bundled browser scripts and QA helpers where repeatability matters.

### Visual checks

Verify:

- layout stability
- responsive behavior
- readable hierarchy
- consistent component states
- visible focus and error states

### Adversarial pass

Finally ask:

- what assumption can be violated?
- what if actions happen twice?
- what if data is malformed?
- what if dependencies fail?
- what if a hostile user actively tries to break this flow?

## Reporting standard

A good test report should state:

- scenario
- setup
- steps
- expected result
- actual result
- severity
- reproduction notes

## Available bundled material

This merged skill keeps:

- functional QA chapters from `functionality-qa`
- Playwright/browser helpers from `web-testing`
- generic QA scripts and references from `qa-testing`
- visual QA corpus from `design-qa`
- adversarial references from `adversarial-qa`

Use the lighter mode that matches the task. Do not jump straight to adversarial testing if basic functionality is still failing.
