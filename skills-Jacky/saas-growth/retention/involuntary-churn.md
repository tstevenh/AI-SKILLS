# Reducing Involuntary Churn

## Introduction

Involuntary churn—customers lost due to payment failures rather than active cancellation—typically accounts for 20-40% of total churn. The good news: it's highly preventable. With the right systems in place, you can recover 50-70% of failed payments. This guide covers payment failure handling, dunning best practices, card update campaigns, and grace periods.

---

## 1. Understanding Payment Failures

### Why Payments Fail

| Reason | Frequency | Preventability |
|--------|-----------|----------------|
| Card expired | 30-40% | High |
| Insufficient funds | 20-30% | Medium |
| Card stolen/blocked | 10-15% | Low |
| Bank decline (fraud flag) | 10-15% | Medium |
| Network errors | 5-10% | High |
| Hard declines | 5-10% | Low |

### Payment Failure Types

**Soft Declines (Temporary):**
- Insufficient funds
- Card activity limits
- Issuer timeout
- Network issues

**Action:** Retry payment

**Hard Declines (Permanent):**
- Card expired
- Card cancelled
- Fraudulent card
- Account closed

**Action:** Request new payment method

### Payment Failure Metrics

| Metric | Good | Target |
|--------|------|--------|
| Initial payment failure rate | <5% | <3% |
| Dunning recovery rate | >50% | >70% |
| Involuntary churn rate | <1.5% | <1% |
| Failed payment to churn | <40% | <25% |

---

## 2. Dunning Email Best Practices

### Dunning Email Sequence

**Email 1: Friendly Notice (Day 0)**
```
Subject: Quick heads up about your payment

Hi [Name],

We tried to process your [Product] payment, but it didn't 
go through. No big deal—this happens sometimes.

Your account is still fully active. Just update your 
payment info to keep things running smoothly:

[Button: Update Payment →]

Common reasons this happens:
• Card expired
• Temporary bank hold
• Card limit reached

Need help? Just reply to this email.

[Your Name]
[Product] Team
```

**Email 2: Second Notice (Day 3)**
```
Subject: Your [Product] payment still needs attention

Hi [Name],

We've tried a few times to process your payment, but 
we're having trouble.

To keep your [Product] account active:
[Button: Update Payment Info →]

Quick fixes:
• Check your card expiration date
• Try a different payment method
• Contact your bank if you're unsure

Your data is safe—we won't delete anything. But we'd 
hate for you to lose access.

Questions? Just reply.

[Your Name]
```

**Email 3: Urgent Notice (Day 7)**
```
Subject: ⚠️ Action needed: Your [Product] access

Hi [Name],

We still haven't been able to process your payment. 
Your [Product] access may be limited soon.

What happens next:
• [Date]: Account moves to limited access
• Your data stays safe
• You can restore full access anytime

Update now to avoid interruption:
[Button: Update Payment Now →]

If there's an issue with the charge itself, please 
let me know. I'm here to help.

[Your Name]
```

**Email 4: Final Notice (Day 10)**
```
Subject: Last chance: [Product] account

Hi [Name],

This is our final notice about your payment. Tomorrow, 
your account will move to limited access.

Your [data/projects/work] is safe. You won't lose anything.
But you'll need to update payment to continue using 
[premium features/full access].

[Button: Update Payment →]

After tomorrow, you can still reactivate anytime by 
updating your payment method.

If there's anything I can help with, please reach out.

[Your Name]
```

### Dunning Email Best Practices

**Tone:**
- Day 0-3: Friendly, helpful
- Day 4-7: Slightly urgent
- Day 8+: Clear, not threatening

**Content:**
- Always explain what happens
- Provide clear action
- Offer help/support
- Don't shame the customer

**Design:**
- Single clear CTA
- Easy to update payment
- Mobile-friendly
- Clear sender

**Timing:**
- Space emails 2-4 days apart
- Consider day of week (avoid weekends)
- Send at reasonable hours

---

## 3. Payment Retry Strategy

### Smart Retry Logic

**Don't retry:**
- Hard declines (wasted effort)
- Fraud flags (risk)
- Closed accounts (impossible)

**Do retry:**
- Soft declines
- Insufficient funds (try different day)
- Network errors
- Timeouts

### Retry Schedule

**For Soft Declines:**
```
Day 0: Initial attempt (failed)
Day 1: First retry
Day 3: Second retry
Day 5: Third retry
Day 7: Fourth retry
Day 10: Fifth retry
```

**For Insufficient Funds:**
```
Try around paydays:
- 1st of month
- 15th of month
- End of month

Different times of day:
- Morning (after midnight processing)
- Evening (after deposits clear)
```

### Retry Optimization

**Variables to Test:**
- Time of day
- Day of week
- Days between retries
- Number of retries

**Industry Data:**
- 15% recover on first retry
- 10% on second retry
- 5% on third retry
- Diminishing after 5 retries

---

## 4. Card Update Campaigns

### Proactive Card Update

**Expiring Card Warning (30 Days):**
```
Subject: Heads up: Your card expires soon

Hi [Name],

Just a friendly reminder—the card we have on file 
expires on [Date].

To avoid any interruption to your [Product] account, 
update your payment info:

[Button: Update Card →]

Takes less than a minute!

[Your Name]
```

**Expiring Card Warning (7 Days):**
```
Subject: Your card expires in 7 days

Hi [Name],

Quick reminder: Your payment card expires on [Date].

Update now to keep your [Product] access uninterrupted:
[Button: Update Card →]

If you've already updated, you can ignore this email.

[Your Name]
```

### In-App Card Update Prompts

**Banner:**
```
┌─────────────────────────────────────────────────────────┐
│ 💳 Your card expires on [Date]. Update to avoid         │
│ interruption. [Update Card]                    [✕]     │
└─────────────────────────────────────────────────────────┘
```

**Modal (7 days out):**
```
┌─────────────────────────────────────────────────────────┐
│                                                         │
│        Your payment card expires in 7 days             │
│                                                         │
│   Update now to keep your [Product] running.           │
│                                                         │
│              [Update Payment Method]                    │
│                                                         │
│              [Remind Me Later]                          │
│                                                         │
└─────────────────────────────────────────────────────────┘
```

### Card Updater Services

Many payment processors offer automatic card updates:

**Stripe:**
- Automatic Card Updater
- Updates expired cards automatically
- Works with many issuers

**Chargebee/Recurly:**
- Similar card update services
- Configurable retry logic
- Integrated dunning

**Benefits:**
- Recovers 10-20% of would-be failures
- Zero customer effort
- Invisible to customer

---

## 5. Grace Periods

### What is a Grace Period?

Time after payment failure before access is restricted.

### Grace Period Design

**Short Grace (3-7 days):**
- For monthly billing
- Maintains urgency
- Lower risk of abuse

**Medium Grace (7-14 days):**
- Standard for most SaaS
- Balance of urgency and fairness
- Allows time for customer action

**Long Grace (14-30 days):**
- For annual billing
- High-value accounts
- Enterprise relationships

### Grace Period Communication

**Day 1 of Grace:**
```
Your payment didn't process. You have [X] days to update 
before your account is affected.
```

**Mid Grace:**
```
[X] days left to update your payment and keep full access.
```

**End of Grace:**
```
Your grace period ends tomorrow. Update now to continue.
```

### After Grace Period

**What to Restrict:**
- New feature creation
- Premium features
- Advanced functionality
- BUT: Don't delete data

**What to Preserve:**
- Read access to data
- Export functionality
- Account recovery option
- Customer support

**Example Implementation:**
```
After grace period:
- Account switches to "Past Due" status
- Read-only access to existing data
- New projects/features blocked
- "Update payment" prominent everywhere
- Data preserved for 90+ days
```

---

## 6. Payment Recovery Optimization

### Multi-Channel Dunning

**Channels:**
1. Email (primary)
2. In-app notifications
3. SMS (with permission)
4. Push notifications (mobile)
5. Phone (high-value accounts)

**Sequence Example:**
```
Day 0: Email + In-app
Day 2: Retry payment + Email 2
Day 4: In-app modal + SMS
Day 6: Retry + Email 3
Day 9: Phone call (if high value)
Day 10: Final email
```

### Recovery Metrics Dashboard

```
Payment Recovery Dashboard
═══════════════════════════════════════════════════
This Month:
─────────────────────────────────────────────────
Failed Payments:        500
├─ Recovered:          350 (70%)
│   ├─ Retry (auto):   150 (30%)
│   ├─ Dunning email:  120 (24%)
│   ├─ Card updater:    50 (10%)
│   └─ Support:         30 (6%)
├─ Pending:             50 (10%)
└─ Churned:            100 (20%)

Recovery by Day:
Day 1-3:   200 (57% of recovered)
Day 4-7:   100 (29% of recovered)
Day 8+:     50 (14% of recovered)
═══════════════════════════════════════════════════
```

### Involuntary Churn Reduction Tactics

| Tactic | Impact | Effort |
|--------|--------|--------|
| Card updater service | High | Low |
| Smart retry logic | Medium | Medium |
| Multi-channel dunning | High | Medium |
| Proactive expiration alerts | Medium | Low |
| Grace period | Medium | Low |
| Support intervention | Medium | High |

---

## Summary: Involuntary Churn Prevention

### Key Strategies

1. **Prevent failures**: Proactive card update alerts
2. **Recover quickly**: Smart retry logic
3. **Communicate well**: Multi-channel dunning
4. **Be patient**: Grace periods work
5. **Measure everything**: Track recovery rates

### Involuntary Churn Checklist

- [ ] Payment retry logic configured
- [ ] Dunning email sequence created
- [ ] Card expiration alerts set up
- [ ] Card updater service enabled
- [ ] Grace period defined
- [ ] In-app notifications added
- [ ] Recovery metrics tracked
- [ ] Support intervention for high-value

### Target Metrics

| Metric | Current | Target |
|--------|---------|--------|
| Payment failure rate | ? | <3% |
| Dunning recovery rate | ? | >70% |
| Involuntary churn | ? | <1% |
| Days to recover (avg) | ? | <5 |

---

*Next: [Cancellation Flow](./cancellation-flow.md)*
