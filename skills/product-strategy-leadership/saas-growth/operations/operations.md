# SaaS Operations

## Introduction

Operational excellence separates good SaaS companies from great ones. As you scale, processes that worked with 100 customers break at 1,000. Manual tasks that seemed fine become bottlenecks. This guide covers billing operations, support operations, success operations, and reporting cadence for scalable SaaS businesses.

---

## 1. Billing Operations

### Subscription Management

**Key Billing Processes:**

| Process | Description | Frequency |
|---------|-------------|-----------|
| Subscription creation | New customer setup | Per signup |
| Upgrades/Downgrades | Plan changes | As needed |
| Renewals | Annual contract processing | Monthly/Quarterly |
| Cancellations | Offboarding | As requested |
| Proration | Mid-cycle changes | As needed |
| Dunning | Failed payment recovery | Ongoing |

### Billing Automation

**Automate:**
- Subscription provisioning
- Proration calculations
- Invoice generation
- Payment retries
- Dunning emails
- Usage metering

**Manual Review:**
- Enterprise deals
- Custom pricing
- Large refunds
- Disputed charges

### Common Billing Issues

| Issue | Root Cause | Solution |
|-------|-----------|----------|
| Double charges | Migration error | Audit, refund, process fix |
| Missing invoices | Email delivery | Verify email, resend |
| Wrong amount | Proration bug | Calculate manually, fix system |
| Upgrade not applied | Timing issue | Apply manually, investigate |
| Tax errors | Configuration | Review tax rules |

### Billing Reconciliation

**Daily:**
- Payment processing verification
- Failed payment review
- Refund processing

**Monthly:**
- Revenue recognition
- Churn calculation
- MRR reconciliation
- Tax remittance

**Quarterly:**
- Revenue audit
- Billing system health check
- Process optimization

### Billing Metrics to Track

| Metric | Target | Alert Threshold |
|--------|--------|-----------------|
| Payment success rate | >97% | <95% |
| Dunning recovery rate | >70% | <50% |
| Billing errors | <0.1% | >0.5% |
| Invoice delivery rate | >99% | <98% |
| Time to resolve disputes | <48 hours | >72 hours |

---

## 2. Support Operations

### Support Tiers

**Tier 1: Self-Service**
- Knowledge base
- FAQ
- Community forum
- Chatbot

**Tier 2: Email/Chat Support**
- Basic troubleshooting
- How-to questions
- Account issues
- Feature questions

**Tier 3: Advanced Support**
- Complex issues
- Bug investigation
- Escalated cases
- Technical deep-dives

**Tier 4: Engineering**
- Bug fixes
- Performance issues
- Security incidents
- Custom solutions

### Support SLAs

| Priority | Definition | First Response | Resolution |
|----------|-----------|----------------|------------|
| P1 - Critical | Service down | 15 minutes | 4 hours |
| P2 - High | Major feature broken | 2 hours | 24 hours |
| P3 - Medium | Feature degraded | 8 hours | 72 hours |
| P4 - Low | Minor issue/question | 24 hours | 1 week |

### Support Metrics

**Volume Metrics:**
| Metric | Calculation |
|--------|-------------|
| Tickets created | Count per period |
| Tickets resolved | Count per period |
| Ticket backlog | Open tickets |
| Tickets per customer | Total / Active customers |

**Quality Metrics:**
| Metric | Target |
|--------|--------|
| First response time | <4 hours |
| Average resolution time | <24 hours |
| First contact resolution | >70% |
| CSAT score | >90% |
| Escalation rate | <10% |

### Support Optimization

**Reduce Volume:**
- Improve onboarding (fewer confusion tickets)
- Better documentation
- In-app guidance
- Proactive communication
- Self-service tools

**Improve Efficiency:**
- Canned responses
- Automation rules
- Triage workflows
- AI assistance
- Knowledge management

**Improve Quality:**
- Agent training
- Quality reviews
- Customer feedback
- Process improvements
- Tool optimization

### Support Staffing

**Tickets per Agent:**
| Complexity | Tickets/Day |
|------------|-------------|
| Simple (chat, basic) | 30-50 |
| Medium (email, how-to) | 15-25 |
| Complex (technical) | 5-10 |

**Calculating Headcount:**
```
Daily tickets: 200
Average complexity: Medium (20/day capacity)
Full coverage needs: 200 / 20 = 10 agents

Add buffer for:
- PTO/sick time (+15%)
- Training (+5%)
- Meetings (+10%)

Total needed: 10 × 1.30 = 13 agents
```

---

## 3. Success Operations

### Customer Success Processes

**Onboarding:**
- Handoff from sales
- Kickoff meeting
- Implementation plan
- Training sessions
- Success milestone tracking

**Ongoing:**
- Health monitoring
- Check-in cadence
- QBR preparation
- Expansion identification
- Risk intervention

**Renewal:**
- Renewal outreach (90 days)
- Success summary
- Renewal negotiation
- Contract processing

### CSM Workflows

**Daily:**
- Review health alerts
- Check inbox/notifications
- Follow up on actions
- Log activities

**Weekly:**
- Portfolio review
- At-risk accounts
- Upcoming renewals
- Team sync

**Monthly:**
- Book of business review
- Expansion pipeline
- Churn analysis
- Process improvement

**Quarterly:**
- Customer QBRs
- Forecast review
- Account planning
- Goal setting

### Success Automation

**Automate:**
- Health score calculation
- Engagement triggers
- Lifecycle emails
- Usage alerts
- Renewal reminders
- Survey distribution

**Human Touch:**
- QBRs
- Executive relationships
- Complex issues
- Expansion negotiations
- At-risk interventions

### CS Metrics Dashboard

```
Customer Success Dashboard
══════════════════════════════════════════════════

PORTFOLIO HEALTH
────────────────────────────────────────────────
Total accounts: 200
Healthy (>70): 150 (75%)
At risk (40-70): 35 (17.5%)
Critical (<40): 15 (7.5%)

RENEWAL FORECAST
────────────────────────────────────────────────
Renewals this quarter: 50
Forecast to renew: 45 (90%)
At risk: 5 (10%)
ARR at risk: $150,000

EXPANSION
────────────────────────────────────────────────
Expansion opportunities: 30
Pipeline value: $500,000
Closed this quarter: $200,000
Target: $300,000

CSM PERFORMANCE
────────────────────────────────────────────────
                    Target    Actual
Retention:          90%       92%
NPS:               40        45
CSAT:              90%       88%
QBR completion:    100%      85%
══════════════════════════════════════════════════
```

---

## 4. Reporting Cadence

### Daily Metrics

**What to Track:**
- New signups
- Conversions
- Support tickets
- Health alerts
- Revenue (if applicable)

**Format:** Dashboard or automated alert

### Weekly Metrics

**What to Track:**
- MRR movement
- Conversion rates
- Support metrics
- Activation metrics
- Pipeline status

**Format:** Team meeting, weekly report

**Example Weekly Report:**
```
Weekly Metrics Report - Week of [Date]
═══════════════════════════════════════

REVENUE
• Starting MRR: $200,000
• New MRR: $15,000
• Expansion: $5,000
• Churn: -$3,000
• Ending MRR: $217,000
• WoW Growth: 8.5%

CUSTOMERS
• New customers: 30
• Churned: 5
• Net new: 25
• Total active: 425

CONVERSION
• Trials started: 200
• Trials converted: 30 (15%)
• PQLs: 50
• MQLs: 100

SUPPORT
• Tickets created: 150
• Tickets resolved: 145
• Avg response time: 3.2 hours
• CSAT: 92%

SUCCESS
• At-risk accounts: 15
• Renewals due: 20
• Renewed: 18 (90%)
• Expansion closed: $5,000

KEY ACTIONS
□ Follow up on 5 at-risk accounts
□ Close 3 expansion deals in pipeline
□ Address support ticket spike
═══════════════════════════════════════
```

### Monthly Metrics

**What to Track:**
- Full MRR waterfall
- Cohort analysis
- Churn breakdown
- CAC and LTV
- Team performance

**Format:** Monthly business review, detailed report

### Quarterly Metrics

**What to Track:**
- Quarterly targets vs. actual
- ARR growth
- Unit economics
- Team planning
- Strategic initiatives

**Format:** Board deck, strategic review

### Annual Metrics

**What to Track:**
- Year-over-year growth
- Annual retention
- Market position
- Strategic review
- Planning for next year

**Format:** Annual review, investor update

---

## Summary: Operations Framework

### Operations Checklist

**Billing:**
- [ ] Subscription management automated
- [ ] Dunning sequences active
- [ ] Reconciliation process
- [ ] Error handling defined
- [ ] Metrics tracked

**Support:**
- [ ] Tier structure defined
- [ ] SLAs established
- [ ] Escalation paths clear
- [ ] Documentation maintained
- [ ] Metrics tracked

**Customer Success:**
- [ ] Playbooks documented
- [ ] Health scoring active
- [ ] Workflows automated
- [ ] QBR process defined
- [ ] Metrics tracked

**Reporting:**
- [ ] Daily dashboards
- [ ] Weekly reports
- [ ] Monthly reviews
- [ ] Quarterly planning
- [ ] Annual review

---

*Next: [Financial Planning](./financial-planning.md)*
