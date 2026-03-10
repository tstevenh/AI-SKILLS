# 37. Design QA Metrics and KPIs


Measuring design quality requires establishing meaningful metrics and Key Performance Indicators (KPIs). Data-driven design QA enables teams to track quality trends, identify problem areas, and demonstrate the value of quality investments.

### 37.1 Quality Metrics Categories

Design quality can be measured across multiple dimensions.

**Visual Consistency Metrics**: Track visual consistency across applications. Measure color usage consistency (percentage of elements using design system colors), typography consistency (percentage of text using approved fonts/sizes), spacing consistency (alignment with design system spacing scale), component usage (percentage of UI using design system components), and design system coverage (what percentage of UI patterns are in design system).

**Accessibility Metrics**: Accessibility can be quantified. Track WCAG compliance level (A, AA, AAA), number of accessibility violations (automated audits), keyboard navigation coverage (percentage of flows keyboard-accessible), screen reader compatibility (percentage of content accessible to screen readers), color contrast pass rate (percentage of elements meeting contrast requirements), and accessibility fix velocity (time to fix accessibility issues).

**Performance Metrics**: Visual performance affects user experience. Measure Core Web Vitals scores (LCP, FID, CLS), image optimization rate (percentage of images appropriately optimized), font loading performance (font-display, FOIT/FOUT handling), animation performance (60fps consistency), and time to interactive (TTI).

**Cross-Browser Consistency**: Track consistency across environments. Measure browser-specific bug count, cross-browser visual regression coverage, testing coverage by browser version, and time to detect cross-browser issues.

### 37.2 Defect Metrics

Tracking defects provides insight into quality trends.

**Defect Discovery**: Measure how defects are found. Track defects found in development vs production, defects by category (visual, functional, accessibility), defects by severity (critical, major, minor), defects by component (which components have most issues), and time from introduction to discovery.

**Defect Resolution**: Measure how quickly issues are fixed. Track average time to fix (MTTR - Mean Time To Repair), reopen rate (percentage of fixes that need rework), escape rate (defects that reach production), and backlog trends (is quality improving or degrading over time).

### 37.3 Process Metrics

Process metrics evaluate the QA process itself.

**Testing Coverage**: Measure how much is being tested. Track visual regression test coverage (percentage of UI covered), manual test coverage (percentage of flows manually tested), accessibility audit coverage, responsive breakpoint coverage, and cross-browser coverage.

**Review Efficiency**: Measure how efficiently reviews happen. Track time from PR to design QA approval, review rejection rate (percentage requiring changes), review iteration count (average number of back-and-forths), and review turnaround time by priority.

### 37.4 User Experience Metrics

User behavior provides quality insights.

**User-Reported Issues**: Track issues users actually encounter. Measure support tickets related to visual issues, user feedback mentioning design problems, app store reviews mentioning UI/UX, social media mentions of issues, and user complaints by category.

**Behavioral Indicators**: User behavior indicates quality issues. Track bounce rate (high bounce may indicate poor first impression), task completion rate (abandoned flows), error rate (form validation failures), engagement metrics (time on site, pages per session), and conversion rate (design impacts conversion).

### 37.5 Quality Scorecards

Quality scorecards consolidate metrics into actionable dashboards.

**Component Quality Score**: Rate each design system component. Criteria include visual consistency (matches design specs), accessibility compliance, cross-browser compatibility, documentation completeness, usage adoption, and bug count. Score each component and prioritize improvement efforts on lowest-scoring components.

**Page Quality Score**: Rate key pages. Criteria include Core Web Vitals performance, accessibility score, cross-browser consistency, visual regression pass rate, and user-reported issues. Track page scores over time to identify improvement or degradation.

**Team Quality Metrics**: Track quality by team. Metrics include defect rate by team, review rejection rate by team, accessibility violations by team, and component adherence by team. Use to identify coaching opportunities and recognize high-performing teams.

### 37.6 Quality Metrics Checklist

Comprehensive quality metrics checklist:

**Establishing Metrics**:
☐ Define quality metrics aligned with business goals
☐ Establish baseline measurements
☐ Set targets for each metric
☐ Implement automated metric collection where possible
☐ Create dashboards for visibility
☐ Review metrics regularly

**Tracking and Reporting**:
☐ Track visual consistency metrics
☐ Track accessibility compliance metrics
☐ Track performance metrics (Core Web Vitals)
☐ Track defect discovery and resolution
☐ Track testing coverage
☐ Track user-reported issues

**Action on Metrics**:
☐ Prioritize work based on metric trends
☐ Celebrate improvements
☐ Investigate metric degradations
☐ Share metrics across teams
☐ Use metrics to justify quality investments
☐ Iterate on metrics as needed

---
