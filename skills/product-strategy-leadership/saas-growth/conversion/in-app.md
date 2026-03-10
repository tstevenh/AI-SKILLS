# In-App Conversion

## Introduction

In-app conversion happens where users are most engaged—inside your product. Strategic placement of upgrade prompts, usage notifications, feature discovery, and upgrade flows can significantly impact conversion rates without feeling pushy. The key is contextual relevance and value-focused messaging.

---

## 1. Upsell Prompts

### Types of In-App Upsell Prompts

**Modal Dialogs:**
```
┌─────────────────────────────────────────┐
│                   ✕                     │
│     Unlock Advanced Analytics          │
│                                         │
│  Get deeper insights into your data    │
│  with custom reports and exports.      │
│                                         │
│  [Upgrade to Pro - $99/mo]             │
│                                         │
│  [Maybe Later]                         │
└─────────────────────────────────────────┘
```

**Use for:** Major upgrade opportunities, high-impact moments

**Banners:**
```
┌─────────────────────────────────────────────────────────┐
│ ⚡ Your trial ends in 3 days. Upgrade now to keep access │
│                                        [Upgrade] [✕]   │
└─────────────────────────────────────────────────────────┘
```

**Use for:** Trial reminders, announcements, persistent nudges

**Inline Prompts:**
```
Feature Area:
┌─────────────────────────────────────────┐
│ [Normal Feature Content]                │
│                                         │
│ Want advanced filters? Available in Pro │
│ [Learn More]                            │
└─────────────────────────────────────────┘
```

**Use for:** Feature-adjacent upsells, contextual suggestions

**Tooltips:**
```
   [Pro Feature Button]
         ↓
   ┌─────────────────┐
   │ Pro Feature     │
   │ Upgrade to      │
   │ unlock this     │
   │ [Upgrade]       │
   └─────────────────┘
```

**Use for:** Locked feature explanation, soft prompts

### Upsell Prompt Timing

**Good Triggers:**
- User attempts locked feature
- Usage approaching limit
- After value moment (success)
- At natural pause points
- Session count milestones

**Bad Triggers:**
- First session (too early)
- Mid-task (disruptive)
- After frustration
- Too frequently (fatigue)

### Upsell Copy Best Practices

**Focus on Value:**
```
❌ "Upgrade to Pro"
✓ "Unlock unlimited projects"

❌ "Buy premium"
✓ "Get deeper insights with advanced analytics"

❌ "Your account is limited"
✓ "Ready for more? Upgrade for unlimited access"
```

**Be Specific:**
```
❌ "Upgrade for more features"
✓ "Upgrade for:
   • Unlimited projects
   • Advanced reporting
   • Priority support"
```

---

## 2. Usage Limit Notifications

### Progressive Limit Notifications

**At 50% Usage:**
```
┌─────────────────────────────────────────┐
│ 📊 Usage Update                         │
│                                         │
│ You've used 5,000 of 10,000 events.    │
│ Great progress!                         │
│                                         │
│ [View Usage] [Dismiss]                  │
└─────────────────────────────────────────┘
```

Tone: Informative, celebratory

**At 80% Usage:**
```
┌─────────────────────────────────────────┐
│ ⚠️ Approaching Your Limit               │
│                                         │
│ You've used 8,000 of 10,000 events.    │
│                                         │
│ Upgrade to avoid interruption:          │
│ [Upgrade to Pro]   [View Usage]         │
└─────────────────────────────────────────┘
```

Tone: Helpful warning, clear action

**At 100% Usage:**
```
┌─────────────────────────────────────────┐
│ 🛑 You've Reached Your Limit            │
│                                         │
│ You've used all 10,000 events.         │
│                                         │
│ To continue:                            │
│ [Upgrade Now]                           │
│                                         │
│ Or wait until [Date] when limit resets  │
└─────────────────────────────────────────┘
```

Tone: Clear, actionable, not punitive

### Soft vs. Hard Limits

**Soft Limit:**
- Warning at threshold
- Continued access with notice
- Upgrade encouraged, not forced

**Hard Limit:**
- Feature blocked at threshold
- Must upgrade to continue
- Clear communication

**Best Practice:** Use soft limits where possible, hard limits where necessary (e.g., API rate limits, storage).

---

## 3. Feature Discovery

### Promoting Underused Features

**New Feature Announcements:**
```
┌─────────────────────────────────────────┐
│ ✨ NEW: Dark Mode                       │
│                                         │
│ Work easier on your eyes.              │
│ Try dark mode in Settings.              │
│                                         │
│ [Try It]   [Later]                      │
└─────────────────────────────────────────┘
```

**Contextual Feature Tips:**
```
User creates 10th project:
┌─────────────────────────────────────────┐
│ 💡 Tip: Use folders                     │
│                                         │
│ Organize your projects with folders.    │
│ [Show Me How]   [Got It]                │
└─────────────────────────────────────────┘
```

**Feature Spotlights:**
```
┌─────────────────────────────────────────┐
│ Did you know?                           │
│                                         │
│ You can keyboard shortcut everything!   │
│ Press ? to see all shortcuts.           │
│                                         │
│ [View Shortcuts]   [Dismiss]            │
└─────────────────────────────────────────┘
```

### Feature Discovery Triggers

| Trigger | Feature to Promote |
|---------|-------------------|
| 5th project created | Folders/organization |
| First collaborator added | Permissions/roles |
| Week 2 of usage | Advanced features |
| First export | Automated exports |
| After task completion | Related features |

---

## 4. Upgrade Flows

### Upgrade Flow Design

**Step 1: Plan Selection**
```
Current plan: Free

┌─────────────┐  ┌─────────────┐  ┌─────────────┐
│    Free     │  │    Pro      │  │ Enterprise  │
│  (Current)  │  │  $29/mo     │  │  Custom     │
│             │  │ [Select]    │  │ [Contact]   │
└─────────────┘  └─────────────┘  └─────────────┘
```

**Step 2: Billing Options**
```
How would you like to pay?

○ Monthly: $29/mo
● Annual: $24/mo (Save $60/year)

[Continue]
```

**Step 3: Payment**
```
Payment Details
───────────────
Card Number: [________________]
Expiry: [__/__]  CVC: [___]

Billing Address: [________________]

[Complete Upgrade]
```

**Step 4: Confirmation**
```
🎉 Welcome to Pro!

You now have access to:
✓ Unlimited projects
✓ Advanced analytics
✓ Priority support

[Start Using Pro Features]
```

### Upgrade Flow Best Practices

**Reduce Friction:**
- Pre-fill known information
- Minimal required fields
- Clear progress indicator
- Save state if interrupted

**Build Confidence:**
- Show what they're getting
- Display trust badges
- Offer money-back guarantee
- Provide support option

**Optimize Conversion:**
- Default to annual (if better for you)
- Show savings clearly
- Single clear CTA per step
- Mobile-optimized

---

## 5. In-App Conversion Best Practices

### Frequency Limits

**Avoid Upgrade Fatigue:**
- Max 1-2 upgrade prompts per session
- Don't repeat dismissed prompts immediately
- Vary message types
- Track dismissal behavior

**Smart Frequency:**
```
Rule: If user dismisses upgrade modal:
- Wait 7 days before showing again
- Try different trigger/message next time
- After 3 dismissals, pause modals for 30 days
```

### Personalization

**Segment-Based Messaging:**
```
Heavy user: "You're a power user! Unlock more with Pro."
Light user: "Get more done with Pro features."
Team lead: "Bring your team to Pro for collaboration."
```

**Behavior-Based Timing:**
- Show after success moment (positive state)
- Show when feature need demonstrated
- Don't show when user is frustrated

### A/B Testing In-App

**What to Test:**
- Copy variations
- CTA button text
- Timing/triggers
- Placement/design
- Frequency

**Measurement:**
- Click-through rate
- Upgrade conversion
- User sentiment (dismissal rate)
- Feature adoption

---

## Summary: In-App Conversion Framework

### In-App Conversion Checklist

**Upsell Prompts:**
- [ ] Modals for major opportunities
- [ ] Banners for persistent reminders
- [ ] Inline prompts for contextual upsells
- [ ] Tooltips for locked features

**Usage Notifications:**
- [ ] 50% usage notification
- [ ] 80% warning
- [ ] 100% limit message
- [ ] Clear upgrade path

**Feature Discovery:**
- [ ] New feature announcements
- [ ] Contextual tips
- [ ] Feature spotlights
- [ ] Trigger-based education

**Upgrade Flow:**
- [ ] Clear plan selection
- [ ] Annual/monthly toggle
- [ ] Simple payment
- [ ] Success confirmation

**Best Practices:**
- [ ] Frequency limits set
- [ ] Personalization implemented
- [ ] A/B testing running
- [ ] Mobile optimized

### In-App Metrics

| Element | Metric | Target |
|---------|--------|--------|
| Upsell Modal | Click rate | >3% |
| Limit Banner | Click rate | >5% |
| Upgrade Flow | Completion | >50% |
| Overall | In-app upgrades | 20-40% of total |

---

*End of Conversion Section*
