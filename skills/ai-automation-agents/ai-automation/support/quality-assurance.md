# AI Support Quality Assurance

> Complete guide to ensuring AI-powered support maintains quality: monitoring, scoring, feedback loops, and continuous improvement.

---

## Table of Contents

1. [Quality Framework](#quality-framework)
2. [Response Quality Scoring](#response-quality-scoring)
3. [Automated Quality Checks](#automated-quality-checks)
4. [Human Review Processes](#human-review-processes)
5. [Feedback Collection](#feedback-collection)
6. [Continuous Improvement](#continuous-improvement)
7. [Compliance & Safety](#compliance--safety)
8. [Metrics & Reporting](#metrics--reporting)

---

## Quality Framework

### The Quality Triangle

```
                    ACCURACY
                       ▲
                      /│\
                     / │ \
                    /  │  \
                   /   │   \
                  /    │    \
                 /     │     \
                ───────┼───────
               /       │       \
              /        │        \
             ▼         │         ▼
          SPEED ◄─────┬─────► EMPATHY
                      │
                   BALANCE
```

**Accuracy:** Correct, factual, complete answers
**Speed:** Fast response times
**Empathy:** Appropriate tone, customer care

### Quality Dimensions

| Dimension | Description | Weight |
|-----------|-------------|--------|
| Factual accuracy | Information is correct | 25% |
| Completeness | All questions answered | 20% |
| Relevance | Response matches question | 20% |
| Tone | Appropriate, empathetic | 15% |
| Clarity | Easy to understand | 10% |
| Actionability | Clear next steps | 10% |

### Quality Tiers

```
Tier 1: Excellent (90-100)
├── Accurate and complete
├── Appropriate tone
├── Clear next steps
└── Could be sent without edit

Tier 2: Good (70-89)
├── Mostly accurate
├── May need minor edit
├── Tone acceptable
└── Sends with quick review

Tier 3: Acceptable (50-69)
├── Core question answered
├── Needs editing
├── Tone could improve
└── Requires agent review

Tier 4: Poor (0-49)
├── Inaccurate or incomplete
├── Inappropriate tone
├── Major revision needed
└── Escalate or regenerate
```

---

## Response Quality Scoring

### Automated Scoring System

```python
class ResponseQualityScorer:
    def __init__(self, llm, knowledge_base):
        self.llm = llm
        self.kb = knowledge_base
        
    async def score_response(
        self, 
        question: str, 
        response: str,
        context: dict
    ) -> dict:
        scores = {}
        
        # 1. Factual accuracy (verify against KB)
        scores["accuracy"] = await self.check_accuracy(response, question)
        
        # 2. Completeness (all parts of question addressed)
        scores["completeness"] = await self.check_completeness(question, response)
        
        # 3. Relevance (response matches question)
        scores["relevance"] = await self.check_relevance(question, response)
        
        # 4. Tone (appropriate for sentiment)
        scores["tone"] = await self.check_tone(response, context)
        
        # 5. Clarity (readability, structure)
        scores["clarity"] = self.check_clarity(response)
        
        # 6. Actionability (clear next steps)
        scores["actionability"] = await self.check_actionability(response)
        
        # Calculate weighted total
        weights = {
            "accuracy": 0.25,
            "completeness": 0.20,
            "relevance": 0.20,
            "tone": 0.15,
            "clarity": 0.10,
            "actionability": 0.10
        }
        
        total = sum(scores[k] * weights[k] for k in weights)
        
        return {
            "total_score": total,
            "breakdown": scores,
            "tier": self.get_tier(total),
            "needs_review": total < 70,
            "issues": self.identify_issues(scores),
            "suggestions": await self.get_suggestions(scores, response)
        }
    
    async def check_accuracy(self, response: str, question: str) -> float:
        # Extract facts from response
        facts = await self.llm.generate(f"""
        Extract all factual claims from this support response:
        {response}
        
        Return as list of claims.
        """)
        
        # Verify each fact against knowledge base
        verified = 0
        for fact in facts:
            kb_result = await self.kb.search(fact)
            if self.verify_fact(fact, kb_result):
                verified += 1
        
        return (verified / len(facts)) * 100 if facts else 100
    
    async def check_completeness(self, question: str, response: str) -> float:
        result = await self.llm.generate(f"""
        Evaluate completeness:
        
        Question: {question}
        Response: {response}
        
        Check:
        1. All explicit questions answered?
        2. Implicit needs addressed?
        3. Any important omissions?
        
        Score: 0-100
        Reasoning: Brief explanation
        """)
        return result["score"]
    
    async def check_relevance(self, question: str, response: str) -> float:
        result = await self.llm.generate(f"""
        Evaluate relevance:
        
        Question: {question}
        Response: {response}
        
        Score 0-100 on:
        - Does response directly address the question?
        - Is there irrelevant information?
        - Is the focus correct?
        """)
        return result["score"]
    
    async def check_tone(self, response: str, context: dict) -> float:
        expected_tone = self.determine_expected_tone(context)
        
        result = await self.llm.generate(f"""
        Evaluate tone:
        
        Response: {response}
        Customer sentiment: {context.get('sentiment', 'neutral')}
        Expected tone: {expected_tone}
        
        Score 0-100 on:
        - Appropriate formality
        - Empathy level
        - Professionalism
        - Match to customer's tone
        """)
        return result["score"]
    
    def check_clarity(self, response: str) -> float:
        scores = []
        
        # Readability score
        scores.append(self.calculate_readability(response))
        
        # Structure score
        scores.append(self.check_structure(response))
        
        # Jargon check
        scores.append(self.check_jargon(response))
        
        return sum(scores) / len(scores)
    
    async def check_actionability(self, response: str) -> float:
        result = await self.llm.generate(f"""
        Evaluate actionability:
        
        Response: {response}
        
        Score 0-100 on:
        - Are next steps clear?
        - Can customer act on this?
        - Is it specific enough?
        """)
        return result["score"]
```

### Scoring Prompts

#### Comprehensive Evaluation Prompt
```
Evaluate this AI support response:

CUSTOMER QUESTION:
{question}

AI RESPONSE:
{response}

CONTEXT:
- Customer tier: {tier}
- Sentiment: {sentiment}
- Previous interactions: {history_summary}

EVALUATE:

1. ACCURACY (0-100)
Is the information correct?
- Check facts against knowledge
- No contradictions
- Proper product/policy info

2. COMPLETENESS (0-100)
Did it answer everything?
- All questions addressed
- Necessary context provided
- Nothing important missing

3. RELEVANCE (0-100)
Is it on topic?
- Directly addresses question
- No irrelevant tangents
- Appropriate detail level

4. TONE (0-100)
Is the tone appropriate?
- Matches customer formality
- Empathetic if needed
- Professional

5. CLARITY (0-100)
Is it easy to understand?
- Clear language
- Logical structure
- No jargon

6. ACTIONABILITY (0-100)
Can customer act on this?
- Clear next steps
- Specific instructions
- Resources provided

OUTPUT:
{
  "scores": {
    "accuracy": 0,
    "completeness": 0,
    "relevance": 0,
    "tone": 0,
    "clarity": 0,
    "actionability": 0
  },
  "overall": 0,
  "tier": "excellent|good|acceptable|poor",
  "issues": [],
  "improvements": [],
  "auto_send_safe": true|false
}
```

---

## Automated Quality Checks

### Pre-Send Validation

```python
class ResponseValidator:
    def __init__(self, config):
        self.config = config
        
    def validate(self, response: str, context: dict) -> dict:
        issues = []
        warnings = []
        
        # Check length
        if len(response) < self.config["min_length"]:
            issues.append("Response too short")
        if len(response) > self.config["max_length"]:
            issues.append("Response too long")
        
        # Check for required elements
        if context.get("requires_greeting") and not self.has_greeting(response):
            issues.append("Missing greeting")
        if not self.has_closing(response):
            warnings.append("Consider adding closing")
        
        # Check for forbidden content
        forbidden = self.check_forbidden_content(response)
        if forbidden:
            issues.extend(forbidden)
        
        # Check for placeholder text
        if self.has_placeholder(response):
            issues.append("Contains placeholder text")
        
        # Check for broken formatting
        if self.has_broken_formatting(response):
            warnings.append("May have formatting issues")
        
        # Check brand voice
        brand_score = self.check_brand_voice(response)
        if brand_score < 70:
            warnings.append("Brand voice could be stronger")
        
        return {
            "valid": len(issues) == 0,
            "issues": issues,
            "warnings": warnings,
            "can_auto_send": len(issues) == 0 and len(warnings) == 0
        }
    
    def check_forbidden_content(self, response: str) -> list:
        issues = []
        
        # Never make promises we can't keep
        if any(phrase in response.lower() for phrase in [
            "i guarantee",
            "definitely will",
            "100% certain"
        ]):
            issues.append("Avoid guarantees we can't keep")
        
        # Check for competitor mentions
        competitors = self.config.get("competitors", [])
        for comp in competitors:
            if comp.lower() in response.lower():
                issues.append(f"Contains competitor mention: {comp}")
        
        # Check for PII handling
        if self.requests_pii_unsafely(response):
            issues.append("Unsafe PII handling")
        
        return issues
```

### Real-Time Checks

```yaml
workflow: Response Quality Gate

trigger: AI response generated

steps:
  - validate_response:
      checks:
        - length_check
        - forbidden_content
        - placeholder_check
        - formatting_check
        
  - score_response:
      model: quality_scorer
      threshold: 70
      
  - route:
      if score >= 85 and validation.passed:
        → auto_send
      elif score >= 70:
        → agent_review_queue
      else:
        → regenerate_or_escalate
```

### Batch Quality Audit

```python
async def daily_quality_audit():
    """Daily audit of AI responses"""
    
    # Get sample of yesterday's responses
    responses = await db.get_ai_responses(
        date=yesterday,
        sample_size=100,
        stratified_by=["category", "auto_sent"]
    )
    
    results = {
        "total_reviewed": len(responses),
        "scores": [],
        "issues_found": [],
        "patterns": {}
    }
    
    for response in responses:
        # Score response
        score = await quality_scorer.score_response(
            response.question,
            response.answer,
            response.context
        )
        
        results["scores"].append(score)
        
        if score["total_score"] < 70:
            results["issues_found"].append({
                "ticket_id": response.ticket_id,
                "score": score["total_score"],
                "issues": score["issues"]
            })
    
    # Analyze patterns
    results["patterns"] = analyze_quality_patterns(results["scores"])
    
    # Generate report
    report = generate_quality_report(results)
    
    # Alert if quality below threshold
    avg_score = sum(r["total_score"] for r in results["scores"]) / len(results["scores"])
    if avg_score < 80:
        await alert_quality_team(report)
    
    return report
```

---

## Human Review Processes

### Review Queue Management

```yaml
workflow: Human Review Queue

trigger: Response flagged for review

priority:
  - VIP customer: P1
  - Negative sentiment: P2
  - Low confidence: P3
  - Random sample: P4

routing:
  - Technical issues → Technical team
  - Billing issues → Billing team
  - Escalations → Senior agents

interface:
  - Show: Question, AI response, context
  - Actions:
    - Approve as-is
    - Edit and send
    - Regenerate with instructions
    - Write manual response
    - Escalate
  - Required: Feedback on AI response
```

### Review Interface Components

```markdown
## Review Interface

### Ticket Information
- **ID:** #12345
- **Customer:** John Doe (Premium)
- **Category:** Technical > Integration
- **Sentiment:** Frustrated

### Customer Message
> "I've been trying to set up the API for two hours and nothing works. 
> Your documentation is terrible and I keep getting 401 errors."

### AI Response (Score: 72)
[AI generated response shown here]

### Quality Assessment
| Dimension | Score | Note |
|-----------|-------|------|
| Accuracy | 85 | ✓ Correct |
| Completeness | 70 | Missing auth details |
| Tone | 65 | Could be more empathetic |

### Actions
[ Approve ] [ Edit ] [ Regenerate ] [ Manual ] [ Escalate ]

### Feedback (Required)
- [ ] Accurate
- [ ] Complete
- [ ] Good tone
- [ ] Would improve how: [text field]

### Notes for Improvement
[What would make this response better?]
```

### Calibration Sessions

```markdown
## Weekly Quality Calibration

### Purpose
Align team on quality standards

### Process
1. Select 10 responses (mix of scores)
2. Each reviewer scores independently
3. Discuss discrepancies
4. Update guidelines if needed

### Sample Responses

**Response 1:**
[Show response]

Individual scores:
- Reviewer A: 75
- Reviewer B: 82
- Reviewer C: 70

Discussion points:
- Why the variance?
- What's the "right" score?
- Should guidelines change?

### Outcomes
- Updated scoring rubric
- New examples for training
- Identified blind spots
```

---

## Feedback Collection

### Customer Feedback

```yaml
workflow: Post-Resolution Feedback

trigger: Ticket closed by AI

timing: 
  delay: 1 hour after resolution

channels:
  email:
    template: feedback_request
  in_app:
    show: feedback_widget

questions:
  - "Did this resolve your issue?"
    type: yes/no
    
  - "How would you rate your experience?"
    type: scale (1-5)
    
  - "What could we improve?"
    type: text (optional)

routing:
  negative_feedback:
    - Create follow-up ticket
    - Alert quality team
    - Flag for review
    
  positive_feedback:
    - Add to success examples
    - Thank customer
```

### Implicit Feedback

Track behavior signals:

```python
class ImplicitFeedbackTracker:
    def track_response(self, ticket_id: str, response_id: str):
        return {
            "reopened": self.check_if_reopened(ticket_id),
            "follow_up_needed": self.check_follow_up(ticket_id),
            "time_to_resolution": self.calculate_resolution_time(ticket_id),
            "customer_replied_positive": self.analyze_reply_sentiment(ticket_id),
            "escalated": self.check_if_escalated(ticket_id),
            "repeat_contact": self.check_repeat_contact(ticket_id)
        }
    
    def calculate_success_score(self, feedback: dict) -> float:
        """Convert implicit signals to success score"""
        score = 100
        
        if feedback["reopened"]:
            score -= 30
        if feedback["escalated"]:
            score -= 20
        if feedback["repeat_contact"]:
            score -= 15
        if not feedback["customer_replied_positive"]:
            score -= 10
        
        return max(0, score)
```

### Agent Feedback Loop

```yaml
workflow: Agent Feedback on AI

trigger: Agent reviews AI response

collect:
  - Action taken:
      - Used as-is
      - Edited slightly
      - Edited significantly
      - Replaced entirely
      
  - Issues (select all):
      - Inaccurate information
      - Missing information
      - Wrong tone
      - Too long/short
      - Off topic
      - Other: [text]
      
  - Better response (if replaced):
      [Free text]

use:
  - Train AI on corrections
  - Update knowledge base
  - Improve prompts
  - Track accuracy trends
```

---

## Continuous Improvement

### Feedback-to-Improvement Pipeline

```yaml
workflow: Improvement Pipeline

daily:
  - Collect feedback (customer + agent)
  - Identify patterns
  - Prioritize issues

weekly:
  - Analyze top issues
  - Update knowledge base
  - Refine prompts
  - Retrain if needed

monthly:
  - Deep performance review
  - Compare to baseline
  - Strategic adjustments
  - Report to leadership
```

### Pattern Analysis

```python
async def analyze_quality_patterns(period: str = "weekly"):
    """Identify recurring quality issues"""
    
    # Get all feedback for period
    feedback = await get_feedback(period)
    
    # Categorize issues
    issues_by_category = defaultdict(list)
    for f in feedback:
        for issue in f["issues"]:
            issues_by_category[issue["type"]].append(f)
    
    # Analyze each category
    patterns = []
    for category, items in issues_by_category.items():
        if len(items) >= 5:  # Minimum threshold
            pattern = await analyze_pattern(category, items)
            patterns.append(pattern)
    
    # Generate improvement recommendations
    recommendations = []
    for pattern in patterns:
        rec = await generate_recommendation(pattern)
        recommendations.append({
            "pattern": pattern,
            "recommendation": rec,
            "priority": calculate_priority(pattern),
            "estimated_impact": estimate_impact(pattern)
        })
    
    return sorted(recommendations, key=lambda x: x["priority"])
```

### A/B Testing Improvements

```yaml
workflow: Prompt A/B Test

setup:
  variants:
    A: current_prompt
    B: improved_prompt
  split: 50/50
  duration: 1 week
  metrics:
    - quality_score
    - customer_satisfaction
    - escalation_rate

execution:
  - Route traffic by variant
  - Track all metrics
  - Ensure statistical significance

analysis:
  - Compare metrics
  - Calculate confidence
  - Document learnings

decision:
  if B significantly better:
    → Roll out B
  if no difference:
    → Keep A (simpler)
  if B worse:
    → Analyze why, iterate
```

---

## Compliance & Safety

### Content Safety Checks

```python
class SafetyChecker:
    def check(self, response: str) -> dict:
        issues = []
        
        # Check for harmful content
        if self.contains_harmful(response):
            issues.append({
                "type": "harmful_content",
                "severity": "critical"
            })
        
        # Check for PII exposure
        pii = self.detect_pii(response)
        if pii:
            issues.append({
                "type": "pii_exposure",
                "severity": "high",
                "details": pii
            })
        
        # Check for legal risks
        if self.has_legal_risk(response):
            issues.append({
                "type": "legal_risk",
                "severity": "high"
            })
        
        # Check for policy violations
        violations = self.check_policy_compliance(response)
        issues.extend(violations)
        
        return {
            "safe": len([i for i in issues if i["severity"] in ["critical", "high"]]) == 0,
            "issues": issues
        }
```

### Audit Trail

```python
class QualityAuditLogger:
    async def log_quality_check(
        self,
        ticket_id: str,
        response_id: str,
        scores: dict,
        action: str,
        actor: str,
        changes: dict = None
    ):
        await self.db.insert("quality_audit_log", {
            "id": uuid4(),
            "timestamp": datetime.utcnow(),
            "ticket_id": ticket_id,
            "response_id": response_id,
            "quality_scores": scores,
            "action": action,  # approved, edited, rejected, escalated
            "actor": actor,    # agent_id or "system"
            "changes_made": changes,
            "metadata": {
                "review_time_seconds": ...,
                "edit_distance": ...,
                "version": ...
            }
        })
```

---

## Metrics & Reporting

### Quality Dashboard

```yaml
Quality Dashboard:
  
  Overall Metrics:
    - Average Quality Score: 84.2
    - Auto-send Rate: 67%
    - Escalation Rate: 8%
    - CSAT: 4.2/5
  
  Quality Distribution:
    - Excellent (90+): 45%
    - Good (70-89): 38%
    - Acceptable (50-69): 12%
    - Poor (<50): 5%
  
  Trend (Last 30 Days):
    [Line chart showing quality over time]
  
  Issues Breakdown:
    - Accuracy: 23%
    - Completeness: 31%
    - Tone: 18%
    - Other: 28%
  
  Top Improvement Areas:
    1. Product X documentation gaps
    2. Refund policy confusion
    3. Technical jargon in responses
```

### Executive Report Template

```markdown
# AI Support Quality Report

**Period:** [Date Range]
**Prepared by:** [Name]

## Executive Summary

AI support quality [improved/declined] by [X]% this period.
Key highlights:
- Quality score: [X] (target: [Y])
- Auto-resolution rate: [X]%
- Customer satisfaction: [X]/5

## Performance Metrics

| Metric | Current | Target | Trend |
|--------|---------|--------|-------|
| Quality Score | 84.2 | 85 | ↑ +2.1 |
| Auto-send Rate | 67% | 70% | ↑ +5% |
| Escalation Rate | 8% | <10% | ↓ -2% |
| CSAT (AI) | 4.2 | 4.0 | → stable |

## Quality Analysis

### Strengths
- [Strength 1]
- [Strength 2]

### Areas for Improvement
- [Area 1]: [Action being taken]
- [Area 2]: [Action being taken]

## Actions Taken

1. [Action 1] - Impact: [X]
2. [Action 2] - Impact: [Y]

## Next Period Focus

1. [Priority 1]
2. [Priority 2]
3. [Priority 3]

## Appendix

[Detailed data tables]
```

---

## Summary

### Quality Assurance Checklist

- [ ] Scoring system implemented
- [ ] Automated pre-send validation
- [ ] Human review queue configured
- [ ] Feedback collection active
- [ ] Pattern analysis running
- [ ] A/B testing infrastructure
- [ ] Safety checks enabled
- [ ] Audit logging complete
- [ ] Dashboard operational
- [ ] Regular calibration scheduled

### Key Metrics to Track

| Metric | Good | Great | World-Class |
|--------|------|-------|-------------|
| Quality Score | 75+ | 85+ | 90+ |
| Auto-send Rate | 50% | 70% | 80% |
| CSAT (AI) | 3.8 | 4.2 | 4.5+ |
| Escalation Rate | <15% | <10% | <5% |
| Accuracy | 90% | 95% | 98% |

See [chatbots.md](chatbots.md) for implementing support chatbots →
