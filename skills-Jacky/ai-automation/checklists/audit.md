# AI Automation Checklists

> Comprehensive checklists for auditing, implementing, and maintaining AI automation.

---

## Process Audit Checklist

### 1. Discovery Questions

For each potential automation candidate, answer:

- [ ] What triggers this process?
- [ ] What are the inputs?
- [ ] What are the outputs?
- [ ] How often does it run?
- [ ] How long does it take?
- [ ] Who is involved?
- [ ] What tools are used?
- [ ] What are the pain points?
- [ ] Are there exceptions/edge cases?
- [ ] What happens when it fails?

### 2. Automation Suitability Assessment

| Criterion | Score (1-5) |
|-----------|-------------|
| Rules-based (clear logic) | ___ |
| Consistent format | ___ |
| High volume | ___ |
| Low risk if errors | ___ |
| Digital inputs/outputs | ___ |
| No regulatory barriers | ___ |
| **Total (higher = better candidate)** | ___/30 |

### 3. ROI Quick Calculator

```
Monthly Time Spent: ___ hours
Hourly Rate: $___ 
Current Monthly Cost: $___ (Time × Rate)

Estimated Automation Setup: ___ hours
Estimated Monthly Tool Cost: $___
Estimated Monthly Maintenance: ___ hours

Payback Period = Setup Cost / (Current Cost - New Cost)
```

---

## Pre-Implementation Checklist

### Technical Readiness

- [ ] Primary automation platform selected
- [ ] Account created and configured
- [ ] API credentials obtained for:
  - [ ] AI provider (Claude/OpenAI)
  - [ ] CRM
  - [ ] Email
  - [ ] Other integrations
- [ ] Test environment set up
- [ ] Monitoring/logging configured

### Process Documentation

- [ ] Current process documented step-by-step
- [ ] Success criteria defined
- [ ] Edge cases identified
- [ ] Error scenarios documented
- [ ] Fallback process defined

### Stakeholder Alignment

- [ ] Process owner identified
- [ ] Sign-off obtained
- [ ] Users notified
- [ ] Training scheduled
- [ ] Support channel established

---

## Implementation Checklist

### Workflow Building

- [ ] Trigger configured correctly
- [ ] All nodes/steps added
- [ ] Data mapping verified
- [ ] Error handling added
- [ ] Timeout limits set
- [ ] Rate limits considered
- [ ] Credentials secured

### AI Component Setup

- [ ] Model selected appropriately
- [ ] Prompt engineered and tested
- [ ] Output format validated
- [ ] Fallback model configured
- [ ] Token limits set
- [ ] Cost estimates calculated

### Testing

- [ ] Unit tests for each step
- [ ] End-to-end test with real data
- [ ] Edge cases tested
- [ ] Error handling tested
- [ ] Performance tested (timing)
- [ ] Cost per run calculated
- [ ] Load testing (if high volume)

### Documentation

- [ ] Workflow purpose documented
- [ ] Input/output specs documented
- [ ] Prompts saved to repository
- [ ] Runbook for common issues
- [ ] Escalation path documented

---

## Launch Checklist

### Pre-Launch

- [ ] Final review completed
- [ ] Stakeholder demo done
- [ ] Training completed
- [ ] Monitoring configured
- [ ] Alerts set up
- [ ] Rollback plan ready
- [ ] Support team briefed

### Launch Day

- [ ] Enable workflow
- [ ] Monitor first 10 executions closely
- [ ] Verify outputs are correct
- [ ] Check error rates
- [ ] Validate timing
- [ ] Confirm notifications working

### Post-Launch (Week 1)

- [ ] Daily performance review
- [ ] User feedback collected
- [ ] Errors investigated and fixed
- [ ] Documentation updated
- [ ] Cost tracking validated
- [ ] Success metrics reported

---

## Maintenance Checklist (Weekly)

### Performance Review

- [ ] Success rate acceptable (>95%)?
- [ ] Error types analyzed
- [ ] Timing within limits?
- [ ] Costs as expected?
- [ ] User complaints addressed?

### System Health

- [ ] API limits not approaching?
- [ ] Credentials still valid?
- [ ] No security alerts?
- [ ] Storage within limits?

### Optimization Opportunities

- [ ] Workflows that can be improved?
- [ ] New automations requested?
- [ ] Cost reduction possible?
- [ ] New features to leverage?

---

## AI-Specific Checklist

### Prompt Quality

- [ ] Clear instructions
- [ ] Relevant examples included
- [ ] Output format specified
- [ ] Constraints defined
- [ ] Edge cases handled
- [ ] Tested with variety of inputs

### Model Selection

- [ ] Complexity matches model tier
- [ ] Cost-efficient choice
- [ ] Performance acceptable
- [ ] Fallback configured
- [ ] Future-proofed (not hardcoded)

### Safety & Quality

- [ ] Output validation in place
- [ ] Human review for critical decisions
- [ ] PII handling compliant
- [ ] Hallucination checks
- [ ] Brand voice consistent

---

## Security Checklist

### Access Control

- [ ] Minimum necessary permissions
- [ ] API keys not in code
- [ ] Credentials encrypted
- [ ] Access audited
- [ ] Offboarding process

### Data Protection

- [ ] PII identified and protected
- [ ] Data retention policy applied
- [ ] Encryption in transit
- [ ] Encryption at rest (if applicable)
- [ ] GDPR/CCPA compliance

### Monitoring

- [ ] Unusual activity alerts
- [ ] Failed auth alerts
- [ ] Cost anomaly alerts
- [ ] Data access logging

---

## Scaling Checklist

### When to Scale

Signs you need to scale:
- [ ] Execution timeouts increasing
- [ ] Queue backing up
- [ ] Rate limits being hit
- [ ] Error rate increasing
- [ ] User complaints about speed

### Scaling Options

- [ ] Evaluate vertical scaling (bigger server)
- [ ] Evaluate horizontal scaling (more workers)
- [ ] Evaluate queue-based processing
- [ ] Consider batching
- [ ] Review architecture

### Cost at Scale

- [ ] Volume discounts available?
- [ ] Self-hosting ROI positive?
- [ ] Caching opportunities?
- [ ] Model tiering optimized?

---

## Quarterly Review Checklist

### Performance Analysis

- [ ] Review all automation metrics
- [ ] Calculate actual ROI
- [ ] Compare to projections
- [ ] Identify top performers
- [ ] Identify underperformers

### Technology Review

- [ ] New tools to evaluate
- [ ] Model updates to consider
- [ ] Platform updates available
- [ ] Technical debt to address

### Strategy Review

- [ ] Automation roadmap updated
- [ ] New opportunities identified
- [ ] Budget review
- [ ] Team capability assessment
- [ ] Training needs identified

### Documentation Update

- [ ] Playbooks current
- [ ] Architecture diagrams updated
- [ ] Lessons learned documented
- [ ] Best practices shared

---

## Department-Specific Checklists

### Marketing Automation Checklist

- [ ] Content workflow automated
- [ ] Social media scheduled
- [ ] Email personalization active
- [ ] Analytics reporting automated
- [ ] Ad performance monitoring

### Sales Automation Checklist

- [ ] Lead enrichment pipeline
- [ ] Lead scoring active
- [ ] Outreach personalization
- [ ] Meeting prep automated
- [ ] CRM updates automated

### Support Automation Checklist

- [ ] Ticket classification active
- [ ] Response drafting enabled
- [ ] FAQ auto-resolution
- [ ] SLA monitoring
- [ ] CSAT collection

### Operations Checklist

- [ ] Data entry automated
- [ ] Reporting automated
- [ ] Onboarding workflows
- [ ] Document processing
- [ ] Monitoring and alerts

---

## Quick Reference

### Daily Check (5 min)

- [ ] Workflow success rates green
- [ ] No critical alerts
- [ ] Costs normal

### Weekly Check (30 min)

- [ ] Full checklist above
- [ ] User feedback review
- [ ] Optimization opportunities

### Monthly Check (2 hours)

- [ ] ROI analysis
- [ ] Roadmap review
- [ ] New tool evaluation
- [ ] Training updates

### Quarterly Check (1 day)

- [ ] Full quarterly review
- [ ] Strategic planning
- [ ] Budget review
- [ ] Team assessment

---

## Emergency Runbook

### Automation Failure

1. Check error message
2. Review recent changes
3. Check API status pages
4. Test manually
5. Rollback if needed
6. Notify stakeholders
7. Document and postmortem

### AI Quality Issue

1. Stop auto-sending if applicable
2. Review recent outputs
3. Check for model changes
4. Audit prompts
5. Increase human review
6. Retrain/adjust
7. Gradual re-enablement

### Cost Spike

1. Identify source
2. Check for loops/errors
3. Pause if necessary
4. Implement limits
5. Review architecture
6. Optimize and resume

---

*Use these checklists iteratively. Not everything applies to every situation.*
