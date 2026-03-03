# Cancellation Flow Design

## Introduction

The cancellation flow is your last chance to save a customer. Done poorly, it frustrates departing customers and damages your brand. Done well, it can recover 5-15% of cancellations, collect valuable feedback, and leave the door open for return. This guide covers cancellation survey design, save offers, downgrade options, pause features, and win-back timing.

---

## 1. Cancellation Survey Design

### Purpose of Cancellation Survey

**Goals:**
1. Understand why customers leave
2. Identify recoverable customers
3. Collect actionable feedback
4. Maintain positive relationship

### Survey Structure

**Step 1: Reason Selection**
```
We're sad to see you go! 
Help us improve—why are you canceling?

○ It's too expensive
○ Missing features I need
○ Switched to another product
○ No longer need this type of product
○ Technical issues
○ Poor customer support
○ Business is closing
○ Other: [_____________]
```

**Step 2: Deeper Understanding (Conditional)**

If "Too expensive":
```
Help us understand:
○ Found a cheaper alternative
○ Budget cuts at company
○ Price doesn't match value
○ Need to pause spending temporarily
```

If "Missing features":
```
What features are you missing?
[_________________________________]

Would you stay if we added these features?
○ Yes, definitely
○ Maybe
○ No, I've already decided
```

If "Switched to competitor":
```
Which product are you switching to?
[_________________________________]

What made you choose them?
[_________________________________]
```

**Step 3: Final Feedback (Optional)**
```
Any other feedback for us?
[_________________________________]

Would you consider returning in the future?
○ Yes, if things change
○ Maybe
○ No
```

### Survey Best Practices

**Do:**
- Keep it short (1-2 minutes max)
- Make it required (valuable data)
- Use conditional logic
- Ask specific questions
- Allow open-ended feedback

**Don't:**
- Make it too long
- Guilt trip
- Make cancellation hard
- Ignore the data

---

## 2. Save Offers

### When to Show Save Offers

**After survey, based on reason:**

| Reason | Offer Type | Success Rate |
|--------|-----------|--------------|
| Too expensive | Discount | 10-20% |
| Missing features | Feature preview | 5-10% |
| Temporary need | Pause | 15-25% |
| Poor experience | Support escalation | 10-15% |
| Competitor switch | Migration help | 5-10% |

### Save Offer Templates

**Discount Offer (Too Expensive):**
```
┌─────────────────────────────────────────────────────────┐
│                                                         │
│         Before you go—special offer just for you       │
│                                                         │
│  We'd hate to lose you over price. What if we could    │
│  offer you 30% off for the next 3 months?              │
│                                                         │
│  Your price: $99/mo → $69/mo                           │
│                                                         │
│       [Accept Offer]      [No Thanks, Cancel]          │
│                                                         │
└─────────────────────────────────────────────────────────┘
```

**Downgrade Offer:**
```
┌─────────────────────────────────────────────────────────┐
│                                                         │
│            Stay with us at a lower tier                │
│                                                         │
│  Instead of canceling, switch to our Starter plan:     │
│                                                         │
│  • Keep your data                                      │
│  • Access core features                                │
│  • Only $29/month                                      │
│                                                         │
│       [Downgrade to Starter]    [Cancel Anyway]        │
│                                                         │
└─────────────────────────────────────────────────────────┘
```

**Pause Offer:**
```
┌─────────────────────────────────────────────────────────┐
│                                                         │
│              Need a break? Pause instead               │
│                                                         │
│  Life happens. Instead of canceling, pause your        │
│  subscription for up to 3 months.                      │
│                                                         │
│  • No charges during pause                             │
│  • Your data stays safe                               │
│  • Resume anytime                                      │
│                                                         │
│       [Pause My Account]       [Cancel Instead]        │
│                                                         │
└─────────────────────────────────────────────────────────┘
```

**Support Escalation:**
```
┌─────────────────────────────────────────────────────────┐
│                                                         │
│              Let's try to make this right              │
│                                                         │
│  You mentioned [issue]. I'd like to personally help    │
│  resolve this before you leave.                        │
│                                                         │
│  Can we schedule a quick call?                         │
│                                                         │
│  [Schedule Call]     [Book a Time]     [Cancel]        │
│                                                         │
└─────────────────────────────────────────────────────────┘
```

### Save Offer Guidelines

**Discount Offers:**
- Reserve for price-sensitive cancellations
- Time-limit the discount (3-6 months)
- Don't train customers to cancel for discounts
- Track if discounted customers stay long-term

**Downgrade Offers:**
- Always offer as alternative to cancel
- Show what they keep
- Make it feel like a reasonable step
- Easy upgrade path later

**When NOT to Offer Saves:**
- Business closing (can't save)
- Clear competitor preference (may feel desperate)
- Angry/upset customer (may backfire)
- Already accepted one save offer before

---

## 3. Downgrade Options

### Downgrade vs. Cancel Strategy

**The Logic:**
- A downgrade preserves the relationship
- Downgrades can upgrade later
- Downgrades generate some revenue
- Downgrades keep data/work

### Downgrade Flow

```
User clicks "Cancel"
       ↓
[Survey: Why are you canceling?]
       ↓
[Save Offer based on reason]
       ↓
If rejected:
[Would you consider downgrading?]
       ↓
If rejected:
[Final confirmation + feedback]
       ↓
[Cancellation complete]
```

### Presenting Downgrade

**Show Clear Comparison:**
```
Instead of canceling, consider downgrading:

                    Current (Pro)    Starter
Price               $99/mo           $29/mo
Projects            Unlimited        10
Team members        25               5
Storage             100GB            10GB
Support             Priority         Email

Your data will stay safe. You can upgrade anytime.

[Downgrade to Starter]    [Continue Canceling]
```

**Highlight What They Keep:**
- All existing data
- Account history
- Team members (if under limit)
- Integrations (if applicable)
- Future upgrade option

### Downgrade Metrics

| Metric | Target |
|--------|--------|
| Downgrade acceptance | 10-20% |
| Downgrade → Upgrade rate | 20-30% |
| Downgrade retention (12mo) | 50-70% |

---

## 4. Pause Options

### When to Offer Pause

**Good Pause Candidates:**
- Seasonal businesses
- Budget constraints
- Parental leave
- Job transitions
- "Need time to think"

**Pause Not Suitable:**
- Switching to competitor
- Product not right fit
- Business closing
- Consistently unhappy

### Pause Implementation

**Pause Duration:**
- Minimum: 1 month
- Maximum: 3-6 months
- Customer chooses

**What Happens During Pause:**
- No billing
- Data preserved
- Login disabled (or limited)
- Auto-resumes at end

**Pause Communication:**
```
30 days before resume:
"Your pause ends in 30 days. Ready to come back?"

7 days before resume:
"Your [Product] account resumes in 7 days."

Resume day:
"Welcome back! Your account is active."
```

### Pause Metrics

| Metric | Target |
|--------|--------|
| Pause acceptance rate | 15-25% |
| Pause → Active rate | 60-80% |
| Pause duration (avg) | 1-2 months |

---

## 5. Win-Back Timing

### Win-Back Timeline

| Time | Action | Message Focus |
|------|--------|---------------|
| Day 0 | Exit confirmation | Leave door open |
| Day 7 | First win-back | What you're missing |
| Day 30 | Product updates | What's new |
| Day 60 | Incentive | Special offer |
| Day 90 | Final direct | Last targeted attempt |
| Ongoing | Newsletter | Stay connected |

### Win-Back Based on Churn Reason

**Churned: Too Expensive**
```
Wait: 60 days (for budget cycle)
Offer: Discount or lower tier promotion
Message: "Your budget, our priority"
```

**Churned: Missing Features**
```
Trigger: When requested feature ships
Offer: Free trial of new feature
Message: "Remember that feature you wanted?"
```

**Churned: Competitor**
```
Wait: 90 days (honeymoon period ends)
Offer: Competitive comparison update
Message: "See what you're missing"
```

**Churned: No Longer Needed**
```
Wait: 6+ months
Trigger: Industry changes or new features
Message: "Times change—here's how we've evolved"
```

### Win-Back Email Examples

**7 Days Post-Churn:**
```
Subject: We miss you at [Product]

Hi [Name],

It's been a week since you left [Product]. I hope 
you've found what you were looking for.

Just so you know:
• Your data is still here
• Your login still works
• You can resume anytime

If anything changes, we'd love to have you back.

[Button: Reactivate Account]

Best,
[Your Name]
```

**30 Days (What's New):**
```
Subject: Here's what's new at [Product]

Hi [Name],

Since you left, we've been busy improving [Product]:

✨ NEW: [Feature 1]
🚀 IMPROVED: [Feature 2]
🔧 FIXED: [Common issue]

Thought you'd like to know, especially since 
[relevant to their use case].

[Button: See What's New]

[Your Name]
```

**60 Days (Incentive):**
```
Subject: Come back with 30% off

Hi [Name],

It's been a couple months, and I wanted to reach out 
one more time.

If you'd like to give [Product] another shot, I'd like 
to offer you 30% off for the next 3 months.

Use code: COMEBACK30

[Button: Reactivate with Discount]

No pressure either way. Thanks for being a customer.

[Your Name]
```

---

## 6. Post-Cancellation Experience

### Confirmation Email

```
Subject: We're sorry to see you go

Hi [Name],

Your [Product] subscription has been cancelled.

What happens now:
• Your last billing date was [Date]
• Your data will be available until [Date + 90 days]
• You can reactivate anytime

We'd love to have you back someday. If anything changes:
[Button: Reactivate Account]

Thanks for being a customer. We wish you the best.

[Your Name]
[Product] Team

P.S. If you have feedback, I'd genuinely love to hear it.
Just reply to this email.
```

### Data Retention

**Best Practice:**
- Keep data 90+ days after cancellation
- Allow export before final deletion
- Send reminder before deletion
- Easy reactivation with data

**Final Deletion Notice:**
```
Subject: Your [Product] data will be deleted in 30 days

Hi [Name],

We're preparing to delete your [Product] data on [Date].

Before we do, would you like to:
• [Export your data]
• [Reactivate your account]

After [Date], your data will be permanently removed.

If you have questions, just reply.

[Your Name]
```

---

## Summary: Cancellation Flow Framework

### Cancellation Flow Checklist

- [ ] Cancellation survey implemented
- [ ] Save offers based on reason
- [ ] Discount offer for price
- [ ] Downgrade option available
- [ ] Pause option available
- [ ] Support escalation for issues
- [ ] Win-back sequence created
- [ ] Data retention policy set

### Key Metrics

| Metric | Target |
|--------|--------|
| Survey completion | >80% |
| Save offer acceptance | 10-20% |
| Downgrade acceptance | 10-20% |
| Pause acceptance | 15-25% |
| Win-back rate | 5-15% |

### Principles

1. **Make it easy**: Don't frustrate departing customers
2. **Collect feedback**: Every cancellation is learning
3. **Offer alternatives**: Downgrade and pause options
4. **Stay connected**: Newsletter, win-back campaigns
5. **Leave door open**: Data retention, easy reactivation

---

*End of Retention Section*
