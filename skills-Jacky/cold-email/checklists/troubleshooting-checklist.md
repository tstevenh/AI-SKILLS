# Troubleshooting Checklist

Use this checklist to diagnose and fix common cold email problems.

---

## Low Open Rates (<30%)

### Check Deliverability
- [ ] Run spam test (mail-tester.com)
- [ ] Check Google Postmaster reputation
- [ ] Verify SPF/DKIM/DMARC passing
- [ ] Check blacklist status
- [ ] Send test to seed accounts

### Check Subject Lines
- [ ] Review for spam trigger words
- [ ] Verify personalization working
- [ ] Check length (3-7 words ideal)
- [ ] Test new subject line approaches

### Check List Quality
- [ ] Verify email addresses are valid
- [ ] Review data freshness
- [ ] Check bounce rate
- [ ] Assess if targeting is correct

### Fixes to Try
- [ ] Pause and clean list
- [ ] Improve subject lines
- [ ] Rest/rotate domains
- [ ] Re-warm mailboxes

---

## Low Reply Rates (<3%)

### Check Message Relevance
- [ ] Review if value prop matches ICP
- [ ] Check if pain points are real
- [ ] Assess personalization quality
- [ ] Verify right person is targeted

### Check Email Quality
- [ ] Review CTA clarity
- [ ] Check email length
- [ ] Assess tone and language
- [ ] Look for trust signals

### Check Targeting
- [ ] Review ICP definition
- [ ] Check if reaching decision makers
- [ ] Assess company fit

### Fixes to Try
- [ ] Test new value propositions
- [ ] Improve personalization
- [ ] Simplify CTA
- [ ] Adjust targeting criteria

---

## High Bounce Rates (>2%)

### Immediate Actions
- [ ] Stop sending from affected sources
- [ ] Remove bounced addresses
- [ ] Check suppression list

### Diagnosis
- [ ] Review list source
- [ ] Check verification status
- [ ] Identify bounce types (hard vs soft)

### Fixes
- [ ] Re-verify entire list
- [ ] Find better data sources
- [ ] Implement verification before adding

---

## Spam Folder Issues

### Diagnosis
- [ ] Check spam content score
- [ ] Review authentication
- [ ] Check sender reputation
- [ ] Run inbox placement test

### Content Fixes
- [ ] Remove spam trigger words
- [ ] Reduce links (1-2 max)
- [ ] Simplify formatting
- [ ] Remove images

### Technical Fixes
- [ ] Verify SPF/DKIM/DMARC
- [ ] Request blacklist removal
- [ ] Warm new infrastructure
- [ ] Reduce sending volume

---

## Quick Diagnosis Guide

| Symptom | Likely Cause | First Check |
|---------|--------------|-------------|
| Opens <30% | Deliverability or subject | Postmaster Tools |
| Opens good, replies <3% | Copy or targeting | Message relevance |
| Bounces >5% | List quality | Verification status |
| Landing in spam | Content or reputation | Spam score test |
| Complaints spike | Relevance or frequency | Review messaging |
| Sudden drop in all metrics | Technical issue | Authentication |

---

## Emergency Protocol

If major issues detected:

1. **STOP** all sending immediately
2. **DIAGNOSE** the specific problem
3. **FIX** root cause before resuming
4. **REST** affected infrastructure (2-4 weeks)
5. **RESTART** gradually with monitoring
