# Complete Prospecting Guide

A comprehensive guide to building high-quality prospect lists from scratch.

---

## Part 1: Defining Your Target

### The ICP Interview Process

Before prospecting, answer these questions:

**About Your Best Customers**:
1. What companies have gotten the most value from your product?
2. What do they have in common (industry, size, challenges)?
3. Which customers have the shortest sales cycles?
4. Which customers have the highest retention/expansion?
5. Which customers are most referenceable?

**About Your Product/Service**:
1. What problem do you solve?
2. For whom is this problem most acute?
3. What triggers make this problem urgent?
4. What budget range does your solution require?
5. What technical requirements exist?

**About Your Market**:
1. What's the total addressable market size?
2. What verticals are most receptive?
3. What company stages are ideal (startup, growth, enterprise)?
4. What geographies can you serve?

### ICP Documentation Template

```markdown
# [Company] Ideal Customer Profile

## Company Attributes
- **Industry**: [Primary and secondary industries]
- **Company Size**: [Employee range and revenue range]
- **Geography**: [Target regions/countries]
- **Business Model**: [B2B, B2C, SaaS, Services, etc.]
- **Stage**: [Startup, Growth, Established, Enterprise]

## Technology Indicators
- **Must Have**: [Technologies they must use]
- **Good to Have**: [Technologies that indicate fit]
- **Exclude**: [Technologies that indicate poor fit]

## Trigger Events
- [Trigger 1]: [Why it matters]
- [Trigger 2]: [Why it matters]
- [Trigger 3]: [Why it matters]

## Buyer Personas
### Primary Buyer
- Titles: [Specific job titles]
- Department: [Department]
- Responsibilities: [Key responsibilities]
- Goals: [What they're trying to achieve]
- Challenges: [Problems they face]

### Secondary Buyer
- [Same format]

## Exclusion Criteria
- [What disqualifies a company]
- [What disqualifies an individual]

## Prioritization Criteria
- Tier 1: [Highest priority characteristics]
- Tier 2: [Medium priority]
- Tier 3: [Lower priority but still ICP]
```

---

## Part 2: Finding Prospects

### LinkedIn Sales Navigator Deep Dive

**Setting Up Your Ideal Searches**

**Step 1: Account Search**
Create saved search for companies:
```
- Industry: [Your targets]
- Company Size: [Employee range]
- Geography: [HQ location]
- Company Type: [Public, Private, etc.]
```

**Step 2: Lead Search Within Accounts**
From your account list, find contacts:
```
- Current Title: [Target titles]
- Seniority Level: [VP, Director, etc.]
- Function: [Sales, Marketing, etc.]
- Years in Position: [Optional - newer = more receptive]
```

**Step 3: Build Lead Lists**
- Save leads to organized lists
- Segment by priority or characteristic
- Export for enrichment

**Advanced Sales Navigator Tactics**:

**Boolean Search for Titles**:
```
"VP of Sales" OR "Vice President of Sales" OR "VP Sales" OR "Head of Sales"
```

**Job Change Filter**:
Filter for people who changed jobs in last 90 days—they're more receptive.

**Posted on LinkedIn Filter**:
Find people actively sharing content—easier to personalize.

**TeamLink**:
See who in your company is connected to prospects.

### Apollo.io Deep Dive

**Building Targeted Lists**

**Step 1: Set Company Filters**
```
- Industry: [Selections]
- Employee Count: [Range]
- Annual Revenue: [Range]
- Technologies: [Specific tools they use]
- Keywords: [Keywords in company description]
- Funding: [Stage and recency]
```

**Step 2: Set Contact Filters**
```
- Titles: [Exact and similar]
- Seniority: [Levels]
- Departments: [Functions]
- Personal Email Excluded: Yes
```

**Step 3: Review and Export**
- Review sample results
- Adjust filters as needed
- Export to CSV or add to sequence

**Apollo Credit Optimization**:
- Use filters before revealing contacts
- Verify value before using credits
- Export in batches
- Consider annual plans for better rates

### ZoomInfo Strategies (If Budget Allows)

**When to Use ZoomInfo**:
- Enterprise targets
- Accuracy is critical
- Phone numbers needed
- Budget > $15K/year

**Effective ZoomInfo Workflows**:
1. Build account lists with intent filters
2. Export contacts with org chart data
3. Use intent scores for prioritization
4. Leverage website visitor identification

### Alternative Data Sources

**Job Boards for Intent**:
- LinkedIn Jobs
- Indeed
- Glassdoor
- Angelist/Wellfound

**What to Look For**:
- Hiring for roles your product supports
- Specific skills/tools in job descriptions
- Volume of hiring (growth signal)

**Funding Databases**:
- Crunchbase
- PitchBook (enterprise)
- AngelList
- TechCrunch

**What to Track**:
- Recent rounds (2-8 weeks old ideal)
- Round size (budget indicator)
- Investors (thesis indicator)

**Technology Detection**:
- BuiltWith
- Wappalyzer
- HG Insights

**What to Find**:
- Companies using complementary tools
- Companies using competitor tools
- Technology gaps you fill

---

## Part 3: Enrichment Workflows

### Basic Enrichment Workflow

**Input**: Company name and domain
**Output**: Contacts with verified emails

```
Step 1: Start with company list
       ↓
Step 2: Find contacts via Apollo/LinkedIn
       ↓
Step 3: Get email addresses
       ↓
Step 4: Verify all emails
       ↓
Step 5: Export clean list
```

### Advanced Enrichment Workflow (Clay)

**Input**: Company list
**Output**: Fully enriched, personalized-ready data

```
Step 1: Import company list
       ↓
Step 2: Enrich with Clearbit (company data)
       ↓
Step 3: Find contacts via Apollo
       ↓
Step 4: Enrich contacts with LinkedIn data
       ↓
Step 5: Pull recent LinkedIn posts
       ↓
Step 6: AI-generate personalized first lines
       ↓
Step 7: Verify emails
       ↓
Step 8: Export to sending tool
```

### Waterfall Enrichment

Try multiple data sources to maximize coverage:

```
Source 1: Apollo (primary)
    ↓ If no result
Source 2: Hunter (backup)
    ↓ If no result
Source 3: Clearbit (tertiary)
    ↓ If no result
Mark as "Not Found"
```

---

## Part 4: List Quality Control

### Pre-Import Verification

Before adding any data to your system:

**1. Source Verification**
- Where did this data come from?
- Is the source reputable?
- How was it collected?
- When was it last updated?

**2. Data Quality Check**
- Sample 20-50 records manually
- Check accuracy of key fields
- Verify email format validity
- Look for obvious junk data

**3. Email Verification**
- Run through verification tool
- Remove invalid/risky results
- Target <2% expected bounce

**4. Deduplication**
- Check against existing data
- Remove duplicates before import
- Merge records where appropriate

### Data Freshness Guidelines

| Data Type | Refresh Frequency |
|-----------|-------------------|
| Email Address | Verify before each campaign |
| Job Title | Every 6 months |
| Company | Annually |
| Phone | Every 6 months |
| LinkedIn | Real-time during research |

### Quality Scoring

Assign quality scores to records:

**A-Quality** (Score 90-100):
- Verified email
- Confirmed current title
- Recent engagement or data
- Strong ICP match

**B-Quality** (Score 70-89):
- Verified email
- Title may be slightly dated
- Good ICP match
- No red flags

**C-Quality** (Score 50-69):
- Email unverified but likely valid
- Title uncertain
- Moderate ICP match
- Some data gaps

**D-Quality** (Score <50):
- Email uncertain
- Multiple data gaps
- Questionable ICP fit
- Consider excluding

---

## Part 5: Segmentation Strategies

### By Engagement Likelihood

**Hot Segment**: Most likely to engage
- Strong ICP match
- Recent trigger event
- Mutual connections
- Previous interactions

**Warm Segment**: Good fit, no urgency
- Strong ICP match
- No specific trigger
- No prior relationship

**Cold Segment**: Broader targeting
- Marginal ICP match
- No triggers
- No connections

### By Account Value

**Enterprise Tier**: Highest potential value
- Large companies
- Long sales cycles
- High deal values
- Multi-threading required

**Mid-Market Tier**: Balanced effort/reward
- Medium companies
- Moderate cycles
- Good deal values
- 1-2 contacts usually sufficient

**SMB Tier**: Volume play
- Small companies
- Quick cycles
- Lower deal values
- Efficient outreach required

### By Persona

**Executive Segment**: C-level contacts
- Strategic messaging
- Business outcomes focus
- Shorter emails
- High personalization

**Manager Segment**: Director/VP contacts
- Balanced tactical/strategic
- ROI and efficiency focus
- Moderate personalization

**Practitioner Segment**: Individual contributors
- Tactical messaging
- Day-to-day pain points
- Features/capabilities focus

---

## Part 6: List Building at Scale

### Building 10,000 Prospect Lists

**Week 1: Foundation**
- Define clear ICP
- Set up tools
- Create search templates
- Build initial 1,000

**Week 2-3: Scale**
- Run searches across all segments
- Enrich in batches
- Verify continuously
- QA sample throughout

**Week 4: Polish**
- Final verification
- Deduplication
- Segmentation
- Priority scoring

### Maintaining Large Lists

**Continuous Hygiene**:
- Remove bounces immediately
- Update job changes monthly
- Re-verify quarterly
- Sunset unengaged annually

**Data Governance**:
- Clear ownership
- Documented processes
- Regular audits
- Compliance checks

---

## Part 7: Trigger-Based Prospecting

### Setting Up Trigger Monitoring

**Funding Triggers**:
1. Create Crunchbase alerts for your segments
2. Monitor relevant news sources
3. Set up automated workflows

**Hiring Triggers**:
1. LinkedIn Jobs saved searches
2. Indeed alerts
3. Company career page monitoring

**News Triggers**:
1. Google Alerts for companies
2. Industry publication monitoring
3. Social media tracking

### Trigger-to-Outreach Workflow

```
Day 0: Trigger detected (funding, hire, news)
       ↓
Day 1: Research company and context
       ↓
Day 1-2: Find relevant contacts
       ↓
Day 2: Verify emails
       ↓
Day 2-3: Personalize outreach
       ↓
Day 3-7: Send (while trigger is fresh)
```

---

## Part 8: Industry-Specific Prospecting

### SaaS/Technology

**Best Sources**:
- Apollo (great tech coverage)
- LinkedIn Sales Navigator
- BuiltWith/Wappalyzer
- G2/Capterra

**Key Signals**:
- Funding rounds
- Technology changes
- Scaling hiring
- Product launches

### Healthcare

**Best Sources**:
- Definitive Healthcare
- LinkedIn
- CMS databases
- State licensing boards

**Key Signals**:
- Regulatory changes
- Acquisitions/mergers
- Leadership changes
- Technology investments

### Financial Services

**Best Sources**:
- LinkedIn
- SEC filings
- Bloomberg
- Industry associations

**Key Signals**:
- Regulatory changes
- M&A activity
- Technology initiatives
- Leadership changes

### Manufacturing

**Best Sources**:
- ThomasNet
- LinkedIn
- Industry directories
- Trade publications

**Key Signals**:
- Expansion announcements
- Technology investments
- Supply chain changes
- Leadership hires

---

## Part 9: Prospecting Metrics

### Metrics to Track

**Volume Metrics**:
- Prospects researched
- Prospects added to list
- Prospects verified
- Prospects uploaded

**Quality Metrics**:
- Verification pass rate
- ICP match rate
- Reply rate by segment
- Conversion rate by source

### Source Quality Tracking

Track performance by data source:

| Source | Contacts Added | Verified | Response Rate | Cost/Contact |
|--------|---------------|----------|---------------|--------------|
| Apollo | | | | |
| LinkedIn | | | | |
| Hunter | | | | |
| Other | | | | |

Cut sources with poor ROI.

---

## Part 10: Compliance in Prospecting

### Data Collection Compliance

**GDPR (EU)**:
- Document legitimate interest
- Source transparency
- Data minimization
- Subject rights processes

**CCPA (California)**:
- Disclosure requirements
- Opt-out rights
- Data access rights

**CASL (Canada)**:
- Consent requirements
- Documentation
- Clear identification

### Ethical Prospecting

**Do**:
- Use publicly available information
- Respect opt-out requests
- Provide clear identification
- Document data sources

**Don't**:
- Scrape private platforms illegally
- Use deceptive methods
- Ignore unsubscribes
- Collect more than needed

---

## Prospecting Checklist

### Before Starting
- [ ] ICP clearly defined
- [ ] Tools set up and configured
- [ ] Budget allocated
- [ ] Compliance understood

### During Prospecting
- [ ] Following ICP criteria
- [ ] Verifying data quality
- [ ] Documenting sources
- [ ] Maintaining organization

### Before Using List
- [ ] All emails verified
- [ ] Duplicates removed
- [ ] Properly segmented
- [ ] Checked against suppression

---

*Quality prospecting is the foundation of cold email success. Invest the time to build great lists.*
