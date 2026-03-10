# Packaging

## Introduction

Packaging is how you bundle features, limits, and services into purchasable products. While pricing determines how much customers pay, packaging determines what they get. Great packaging makes decisions easy, maximizes value capture, and creates natural upgrade paths.

This guide covers packaging frameworks, feature differentiation, enterprise tier design, add-ons, pricing page design, and 10+ real-world pricing page examples.

---

## 1. Good-Better-Best Framework

### The Classic Three-Tier Structure

**Good (Starter/Basic):**
- Entry-level tier
- Core functionality only
- Lower price point
- Gateway to paid

**Better (Pro/Professional):**
- Target tier for most customers
- Full self-serve functionality
- Mid-range price
- Best value positioning

**Best (Business/Enterprise):**
- Complete offering
- All features included
- Highest price point
- Signals premium option

### Why Good-Better-Best Works

**Psychological Principles:**

1. **Decoy Effect**: Middle option seems best by comparison
2. **Anchoring**: High tier makes middle seem affordable
3. **Choice Architecture**: Three options is cognitively manageable
4. **Loss Aversion**: Missing features in lower tiers feels like loss

**Business Benefits:**

1. **Segment Capture**: Different tiers for different customers
2. **Upgrade Path**: Clear progression
3. **Value Anchoring**: Enterprise anchors perception
4. **Revenue Optimization**: Capture more willingness to pay

### Designing Good-Better-Best

**Step 1: Define Target Tier**

Most customers should land in the middle tier:
- Design this tier first
- Price it for your target segment
- Include everything needed for success

**Step 2: Create Entry Tier**

Remove features that:
- Power users need (not beginners)
- Scale-related (higher limits)
- Team-oriented (collaboration)
- Advanced use cases

**Step 3: Create Premium Tier**

Add features that:
- Enterprise requires (security, compliance)
- Large scale demands (higher limits)
- Advanced users want (power features)
- Justify 2-3x price increase

### Tier Distribution Goals

```
Target Distribution:
┌────────────────────────────────────────────────┐
│                                                │
│  ████░░░░░░░░  Starter (20-30%)               │
│                                                │
│  ████████████░░░░░░░  Pro (50-60%)            │
│                                                │
│  ████░░░░░░░░  Enterprise (15-25%)            │
│                                                │
└────────────────────────────────────────────────┘
```

**If Distribution Is Wrong:**

| Actual | Problem | Solution |
|--------|---------|----------|
| 70% Starter | Starter too good | Add limits or move features |
| 10% Pro | Pro not compelling | Better value or lower price |
| 5% Enterprise | Enterprise not differentiated | Add exclusive features |

---

## 2. Feature Differentiation

### What to Gate (and What Not To)

**Gate These Features:**

| Feature Type | Example | Why Gate |
|--------------|---------|----------|
| Scale/Limits | 10 vs. 100 projects | Usage grows with value |
| Advanced | Custom reporting | Power users need |
| Team | Permissions, roles | Larger teams need |
| Compliance | SSO, audit logs | Enterprise requires |
| Support | Priority, dedicated | Service differentiator |
| Integrations | Premium integrations | Extended value |

**DON'T Gate These:**

| Feature Type | Example | Why Keep Free |
|--------------|---------|---------------|
| Core Value | Main functionality | Needed to experience value |
| Security Basics | Encryption, 2FA | Reflects poorly to charge |
| Basic Support | Email support | Creates frustration |
| Onboarding | Setup guides | Blocks activation |

### Feature Allocation Strategy

**Feature Prioritization Matrix:**

```
                    LOW COST TO DELIVER
                    ↑
          │         │
   Gate   │ Include │  Don't gate low-cost,
   Higher │ in All  │  high-value features
   Tiers  │ Tiers   │
          │         │
LOW ──────┼─────────┼────────── HIGH
DEMAND    │         │           DEMAND
          │         │
   Don't  │  Gate   │  Gate high-demand,
   Build  │ Middle  │  high-cost features
          │ Tier    │
          │         │
                    ↓
                    HIGH COST TO DELIVER
```

**Example Allocation:**

| Feature | Starter | Pro | Enterprise |
|---------|:-------:|:---:|:----------:|
| Core Editor | ✓ | ✓ | ✓ |
| 10 Projects | ✓ | ✓ | ✓ |
| Unlimited Projects | | ✓ | ✓ |
| Team Collaboration | | ✓ | ✓ |
| Custom Branding | | ✓ | ✓ |
| API Access | | ✓ | ✓ |
| Advanced Analytics | | | ✓ |
| SSO/SAML | | | ✓ |
| Dedicated Support | | | ✓ |
| Custom Integrations | | | ✓ |

### Creating Upgrade Triggers

**Natural Upgrade Moments:**

1. **Limit Reached**: "You've used 10 of 10 projects"
2. **Feature Needed**: "Team permissions is a Pro feature"
3. **Growth Event**: "Adding 6th user? Upgrade for team features"
4. **Time Milestone**: "6 months of great work—here's what Pro offers"

**Designing Upgrade Friction:**

```
Good Friction (creates upgrade consideration):
- Soft limit warning at 80%
- Feature preview with gate
- Upgrade CTA when relevant

Bad Friction (creates frustration):
- Hard cutoff mid-work
- Features visible but locked
- Constant upgrade nagging
```

---

## 3. Enterprise Tier Design

### What Makes Enterprise "Enterprise"

**Core Enterprise Requirements:**

| Requirement | Why |
|-------------|-----|
| SSO/SAML | IT control over access |
| SCIM Provisioning | Automated user management |
| Audit Logs | Compliance requirements |
| Advanced Permissions | Granular access control |
| Data Residency | Regulatory requirements |
| Uptime SLA | Business criticality |
| Dedicated Support | High-touch needs |
| Custom Contracts | Legal/procurement needs |

### Enterprise Packaging Patterns

**Pattern 1: Feature-Based Enterprise**
```
Enterprise = Everything in Pro + Enterprise Features
- SSO/SAML
- Advanced admin
- Audit logs
- API rate limits raised
- Dedicated support

Price: $X/user/month (higher per-seat)
```

**Pattern 2: Service-Based Enterprise**
```
Enterprise = Pro Features + Enterprise Service
- Same features as Pro
- Dedicated account manager
- Priority support
- Custom onboarding
- QBRs

Price: $X/user/month + service fee
```

**Pattern 3: Platform Enterprise**
```
Enterprise = Unlimited + Platform Features
- Unlimited everything
- Multiple workspaces
- Cross-workspace analytics
- Org-level admin
- Custom integrations

Price: Custom (annual contract)
```

### Enterprise Pricing Approaches

**Option 1: Published Pricing**
```
Enterprise: $45/user/month
- Transparent
- Self-serve possible
- Volume discounts available
```

**Option 2: "Contact Us"**
```
Enterprise: Contact Sales
- Custom negotiations
- Flexibility
- Higher deal sizes possible
```

**Option 3: Hybrid**
```
Enterprise: Starting at $45/user/month
- Published base price
- Custom for large deals
- Best of both worlds
```

### Enterprise Sales Considerations

**Enterprise Buyers Need:**
- Security documentation (SOC 2, etc.)
- Compliance certifications
- Data processing agreements
- SLAs
- References
- Custom terms capability

**Enterprise Sales Process:**
- Longer cycles (3-12 months)
- Multiple stakeholders
- Pilots/POCs common
- Procurement involvement
- Legal review

---

## 4. Add-Ons and Modules

### Add-On Strategy

**What Are Add-Ons?**
Optional features/services purchased separately from base plan.

**Why Add-Ons:**
- Don't bloat core plans
- Capture value from power users
- Flexible packaging
- Incremental revenue

### Types of Add-Ons

**Feature Add-Ons:**
```
Base Plan: $99/month
+ Advanced Reporting: +$29/month
+ API Access: +$49/month
+ White Labeling: +$79/month
```

**Capacity Add-Ons:**
```
Base Plan: 10,000 contacts
+ Additional 10K contacts: +$20/month
+ Additional 50K contacts: +$80/month
```

**Service Add-Ons:**
```
Base Plan: Standard support
+ Priority Support: +$199/month
+ Dedicated CSM: +$499/month
+ Custom Training: +$1,500 one-time
```

**User Type Add-Ons:**
```
Base Plan: 5 editor seats
+ Additional Editor: +$15/month
+ Viewer Seats: Free (unlimited)
+ Admin Seats: +$25/month
```

### Add-On Best Practices

**1. Keep Core Plans Complete**
- Add-ons for extras, not essentials
- Base plan should satisfy most users
- Add-ons for power users/edge cases

**2. Bundle for Value**
- "Power User Bundle" vs. 5 add-ons
- Simplify decisions
- Increase average deal size

**3. Price for Incremental Value**
- Add-on should clearly deliver value
- Easy to justify cost
- Clear ROI

**4. Avoid Nickel-and-Diming**
- Too many add-ons feels sleazy
- Core experience shouldn't feel incomplete
- Transparent pricing

---

## 5. Pricing Page Design

### Pricing Page Anatomy

```
┌─────────────────────────────────────────────────────────┐
│                    PRICING HEADER                       │
│         "Simple pricing for teams of all sizes"         │
│              [Monthly] [Annual - Save 20%]              │
├─────────────────────────────────────────────────────────┤
│                                                         │
│  ┌───────────┐  ┌───────────┐  ┌───────────┐          │
│  │  STARTER  │  │    PRO    │  │ENTERPRISE │          │
│  │           │  │ POPULAR ⭐│  │           │          │
│  │   $29     │  │   $99     │  │  $249     │          │
│  │  /month   │  │  /month   │  │  /month   │          │
│  │           │  │           │  │           │          │
│  │ ✓ Feature │  │ ✓ Feature │  │ ✓ Feature │          │
│  │ ✓ Feature │  │ ✓ Feature │  │ ✓ Feature │          │
│  │           │  │ ✓ Feature │  │ ✓ Feature │          │
│  │           │  │ ✓ Feature │  │ ✓ Feature │          │
│  │           │  │           │  │ ✓ Feature │          │
│  │           │  │           │  │           │          │
│  │[Start]    │  │[Get Pro]  │  │[Contact]  │          │
│  └───────────┘  └───────────┘  └───────────┘          │
│                                                         │
├─────────────────────────────────────────────────────────┤
│              FEATURE COMPARISON TABLE                   │
│  ┌─────────────────┬─────────┬────────┬──────────┐    │
│  │ Feature         │ Starter │  Pro   │Enterprise│    │
│  ├─────────────────┼─────────┼────────┼──────────┤    │
│  │ Projects        │   10    │ Unlim  │  Unlim   │    │
│  │ Users           │   3     │  10    │  Unlim   │    │
│  │ Storage         │  5GB    │ 50GB   │  500GB   │    │
│  │ Support         │ Email   │Priority│Dedicated │    │
│  │ SSO             │    -    │   -    │    ✓     │    │
│  └─────────────────┴─────────┴────────┴──────────┘    │
│                                                         │
├─────────────────────────────────────────────────────────┤
│                         FAQ                             │
│  "Can I change plans?" "What payment methods?"...       │
│                                                         │
├─────────────────────────────────────────────────────────┤
│                    SOCIAL PROOF                         │
│  "Trusted by 10,000+ teams including [logos]"          │
│                                                         │
└─────────────────────────────────────────────────────────┘
```

### Key Pricing Page Elements

**1. Clear Tier Names**
- Reflect customer stage
- Memorable
- Not just "Plan 1, 2, 3"

**2. Prominent Pricing**
- Easy to find
- Per-unit clarity (per user/month)
- Annual/monthly toggle

**3. Highlighted Recommended**
- Visual distinction
- "Most Popular" or "Best Value"
- Guides decision

**4. Feature Lists**
- Scannable
- Highlight differences
- Consistent formatting

**5. Clear CTAs**
- "Start Free Trial"
- "Get Started"
- "Contact Sales"

**6. Billing Toggle**
- Monthly vs. Annual
- Show savings clearly
- Default to better value

**7. Comparison Table**
- All features compared
- Easy to scan
- Mobile-friendly

**8. FAQ**
- Address common concerns
- Reduce friction
- Build trust

**9. Social Proof**
- Customer logos
- Trust badges
- Testimonials

### Pricing Page Best Practices

**Do:**
- Make recommended tier obvious
- Show annual savings prominently
- Include free trial CTA
- Answer objections on page
- Mobile-optimize

**Don't:**
- Hide prices behind "Contact Us" (unless enterprise)
- Require login to see pricing
- Over-complicate with too many options
- Use confusing tier names
- Forget social proof

---

## 6. 10+ Pricing Page Examples

### Example 1: Slack
- **Structure**: Free, Pro, Business+, Enterprise Grid
- **Notable**: Per-user pricing, free tier prominent
- **Comparison**: Feature checklist below plans
- **Good**: Clear limits on free, obvious upgrade path

### Example 2: Notion
- **Structure**: Free, Plus, Business, Enterprise
- **Notable**: Free for personal, paid for teams
- **Comparison**: Clean comparison table
- **Good**: Strong free tier, simple progression

### Example 3: Airtable
- **Structure**: Free, Team, Business, Enterprise Scale
- **Notable**: Record and automation limits by tier
- **Comparison**: Detailed feature table
- **Good**: Clear usage limits as differentiators

### Example 4: Figma
- **Structure**: Free, Professional, Organization, Enterprise
- **Notable**: Editor vs. viewer pricing
- **Comparison**: Feature comparison by use case
- **Good**: Free viewers = viral, editors pay

### Example 5: Linear
- **Structure**: Free, Standard, Plus
- **Notable**: Very simple, 3 tiers
- **Comparison**: Minimal feature differences
- **Good**: Clean design, easy decision

### Example 6: Intercom
- **Structure**: Complex (multiple products)
- **Notable**: MAU-based + seat-based hybrid
- **Comparison**: Product-specific pricing
- **Learning**: Complexity can confuse

### Example 7: HubSpot
- **Structure**: Free Tools → Starter → Professional → Enterprise
- **Notable**: Multiple product hubs
- **Comparison**: Bundle discounts
- **Good**: Free CRM as land, paid as expand

### Example 8: Webflow
- **Structure**: Starter, Basic, CMS, Business, Enterprise
- **Notable**: Site plans + workspace plans
- **Comparison**: Detailed feature breakdown
- **Good**: Per-site pricing makes sense for use case

### Example 9: Calendly
- **Structure**: Free, Standard, Teams, Enterprise
- **Notable**: Individual vs. team focus
- **Comparison**: Event type and integration limits
- **Good**: Clear individual → team upgrade path

### Example 10: Loom
- **Structure**: Starter, Business, Enterprise
- **Notable**: Video limits by tier
- **Comparison**: Recording and transcription features
- **Good**: Generous free tier drives virality

### Common Patterns Observed

1. **Free tiers are common** (drive adoption)
2. **3-4 tiers is standard** (not too complex)
3. **Per-user is dominant** (for collaboration tools)
4. **Annual discounts 15-25%** (encourage commitment)
5. **Enterprise is custom** (flexibility for large deals)
6. **Feature tables below cards** (detail for comparison)
7. **Social proof prominent** (build trust)

---

## Summary: Packaging Excellence

### Packaging Checklist

**Tier Structure:**
- [ ] Clear tier names and positioning
- [ ] Target tier identified and optimized
- [ ] Appropriate feature differentiation
- [ ] Logical upgrade path

**Enterprise:**
- [ ] Enterprise-specific features included
- [ ] Security/compliance requirements met
- [ ] Service options available
- [ ] Custom contract capability

**Add-Ons:**
- [ ] Optional add-ons for power users
- [ ] Bundles for common combinations
- [ ] Clear pricing for add-ons

**Pricing Page:**
- [ ] Clean, scannable design
- [ ] Recommended tier highlighted
- [ ] Annual/monthly toggle
- [ ] Feature comparison table
- [ ] FAQ section
- [ ] Social proof
- [ ] Clear CTAs

---

*Next: [Pricing Psychology](./psychology.md)*
