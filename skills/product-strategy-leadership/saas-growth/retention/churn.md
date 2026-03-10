# Understanding Churn

## Introduction

Churn is the silent killer of SaaS businesses. While acquisition gets the glory, retention determines whether your business is building on solid ground or filling a leaky bucket. Understanding churn—its types, causes, prediction, and benchmarks—is essential for sustainable growth.

---

## 1. Churn Types

### Voluntary Churn

Customer actively decides to cancel.

**Reasons:**
- No longer need product
- Switched to competitor
- Budget constraints
- Poor experience
- Missing features

**Characteristics:**
- Customer initiated
- Often preventable
- Feedback available
- Can be predicted

### Involuntary Churn

Customer lost due to payment failure.

**Reasons:**
- Card expired
- Insufficient funds
- Card reported stolen
- Processing error

**Characteristics:**
- Not customer's choice
- Highly preventable
- Often goes unnoticed
- Significant at scale

### Churn Split

Typical split:
- Voluntary: 60-70%
- Involuntary: 30-40%

**Implication:** Fixing involuntary churn is often easiest win.

---

## 2. Churn Reasons

### Top Reasons Customers Churn

| Reason | Frequency | Preventability |
|--------|-----------|----------------|
| No longer needs product | 25-30% | Low |
| Too expensive | 15-20% | Medium |
| Switched to competitor | 15-20% | Medium |
| Poor experience/support | 10-15% | High |
| Missing features | 10-15% | Medium |
| Business closed | 5-10% | None |
| Payment failure | 20-30% | High |

### Understanding Churn Feedback

**Cancellation Survey:**
```
We're sorry to see you go!
Help us improve—why are you canceling?

○ No longer need this
○ Too expensive
○ Missing features I need
○ Switched to another product
○ Poor experience/support
○ Business closing
○ Other: [_______________]
```

**Exit Interview:**
For high-value accounts, conduct exit interviews:
- What led to this decision?
- What could we have done differently?
- What are you switching to?
- Would you consider returning?

---

## 3. Churn Prediction

### Leading Indicators

**Engagement Signals:**

| Signal | Churn Risk |
|--------|-----------|
| Login frequency dropping | High |
| Core feature usage declining | High |
| Support tickets increasing | Medium |
| Not using new features | Medium |
| Seat utilization low | Medium |

### Customer Health Score

**Building a Health Score:**

Combine multiple signals into single score:

```
Health Score = 
  (Login Frequency × 0.25) +
  (Feature Usage × 0.30) +
  (Support Satisfaction × 0.20) +
  (Growth/Expansion × 0.15) +
  (Tenure × 0.10)

Score 0-100:
- 80-100: Healthy (low churn risk)
- 60-79: Moderate (watch closely)
- 40-59: At risk (proactive outreach)
- 0-39: Critical (urgent intervention)
```

### Predictive Churn Model

**Features for ML Model:**
- Days since last login
- Feature adoption %
- Support ticket volume
- NPS score
- Contract value
- Renewal date proximity
- Usage trend (up/down)

**Model Output:**
- Churn probability (0-100%)
- Key risk factors
- Recommended actions

---

## 4. Cohort Churn Analysis

### Building Churn Cohorts

**By Signup Month:**

| Cohort | M1 | M3 | M6 | M12 |
|--------|-----|-----|-----|-----|
| Jan | 15% | 28% | 40% | 52% |
| Feb | 18% | 32% | 45% | - |
| Mar | 12% | 25% | 38% | - |

**Reading:** Jan cohort lost 52% of customers by month 12.

**By Acquisition Channel:**

| Channel | M6 Churn |
|---------|----------|
| Organic | 35% |
| Paid Search | 45% |
| Referral | 28% |
| AppSumo | 65% |

**Insight:** Referral customers retain better; AppSumo customers churn heavily.

### Survival Analysis

**Kaplan-Meier Curve:**

```
Survival Rate
100% ┤━━━━━━
     │      ╲
 75% │       ╲━━━━━━
     │              ╲
 50% │               ╲━━━━━━
     │                      ╲
 25% │                       ╲━━━
     │
  0% └──────────────────────────────
        M1   M3   M6   M12   M24

Steeper drop = more churn in that period
Flatten = stabilization (sticky customers)
```

---

## 5. Churn Benchmarks

### By Business Model

| Model | Monthly Churn | Annual Churn |
|-------|---------------|--------------|
| Consumer B2C | 5-15% | 45-85% |
| SMB | 3-8% | 30-60% |
| Mid-Market | 1-3% | 12-30% |
| Enterprise | 0.5-1.5% | 5-17% |

### By Price Point

| ACV | Expected Monthly Churn |
|-----|----------------------|
| <$1K | 5-10% |
| $1K-$10K | 3-5% |
| $10K-$50K | 1-3% |
| >$50K | <1% |

### By Contract Type

| Contract | Typical Churn |
|----------|---------------|
| Monthly | 3-8% monthly |
| Annual | 10-25% at renewal |
| Multi-year | 5-15% at renewal |

### Good vs. Great

| Segment | Good | Great | Elite |
|---------|------|-------|-------|
| SMB | <5% monthly | <3% | <2% |
| Enterprise | <15% annual | <10% | <5% |

---

## Summary: Churn Understanding Framework

### Key Churn Questions

1. **What's our churn rate?**
   - Gross revenue churn
   - Logo churn
   - Net revenue churn

2. **Who is churning?**
   - By segment
   - By cohort
   - By acquisition source

3. **Why are they churning?**
   - Cancellation feedback
   - Exit interviews
   - Behavior analysis

4. **When do they churn?**
   - Time-based patterns
   - Trigger events
   - Renewal cycles

5. **Can we predict it?**
   - Health scores
   - Leading indicators
   - Predictive models

### Churn Analysis Checklist

- [ ] Churn metrics defined and tracked
- [ ] Voluntary vs involuntary split known
- [ ] Cancellation survey implemented
- [ ] Cohort analysis available
- [ ] Health score model built
- [ ] Churn by segment understood
- [ ] Benchmarks established

---

*Next: [Customer Success](./customer-success.md)*
