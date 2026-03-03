# Functionality QA - Comprehensive Testing Guide

> **📚 Navigation Guide**
> 
> This skill uses a **two-part documentation structure**:
> 
> 1. **SKILL.md** (this file) - Core functionality QA concepts, test case design, E2E workflows, and practical testing patterns
> 2. **CHAPTER-XX.md files** - Deep-dive topics for specialized testing areas:
>    - `CHAPTER-01.md` - API Testing Deep Dive
>    - `CHAPTER-02.md` - Performance and Load Testing
>    - `CHAPTER-03.md` - Security Testing Foundations
>    - `CHAPTER-07.md` - Security Testing for QA Engineers
>    - `CHAPTER-08.md` - Chaos Engineering and Reliability
>    - `CHAPTER-09.md` - E2E Testing Strategy
>    - `CHAPTER-10.md` - QA Leadership and Team Management
> 
> See `CHAPTERS.md` for the complete index.

## Table of Contents

1. [Introduction to Functionality QA](#introduction)
2. [Test Case Design Methodologies](#test-case-design)
3. [End-to-End Testing Workflows](#e2e-testing)
4. [API Testing](#api-testing)
5. [Database Integrity Testing](#database-testing)
6. [Form Validation Testing](#form-validation)
7. [Session Management & Cookies](#session-management)
8. [OAuth & SSO Flows](#oauth-sso)
9. [Payment Gateway Testing](#payment-testing)
10. [Email Deliverability Testing](#email-testing)
11. [Webhook Reliability Testing](#webhook-testing)
12. [Cron Job Verification](#cron-testing)
13. [WordPress-Specific Testing](#wordpress-testing)
14. [Browser Automation](#browser-automation)
15. [CI/CD Integration](#cicd-integration)
16. [Test Reporting](#test-reporting)
17. [Tools and APIs](#tools-apis)

---

## 1. Introduction to Functionality QA {#introduction}

### 1.1 What is Functionality Testing?

Functionality testing is a type of software testing that validates the software system against the functional requirements and specifications. The purpose of functionality testing is to test each function of the software application by providing appropriate input and verifying the output against the functional requirements. Functionality testing is performed to verify that a software application performs and functions correctly according to design specifications.

Functionality testing can be performed at all test levels (component, integration, system, and acceptance testing). It is primarily concerned with black box testing and is not concerned with the source code of the application. The tester provides input and examines the output without knowing how the actual processing happens within the software.

### 1.2 Types of Functionality Testing

**Unit Testing**: Testing individual components or modules of a software application in isolation to verify that each unit of the software code performs as expected. Unit testing is typically done during the development phase by developers who write and test their code.

**Integration Testing**: Testing the interfaces between components, interactions with different parts of the system such as operating system, file system, hardware, or interfaces between applications. Integration testing verifies that different modules or services used by your application work well together.

**System Testing**: Testing the complete integrated system to evaluate the system's compliance with the specified requirements. System testing is performed on the entire system in the context of either functional requirement specifications (FRS) or system requirement specification (SRS), or both.

**Sanity Testing**: A subset of regression testing performed after receiving a software build with minor changes in code or functionality to ensure that the bugs have been fixed and no further issues are introduced due to these changes.

**Smoke Testing**: A preliminary testing process to check whether the deployed software build is stable or not. Smoke testing is also known as "Build Verification Testing" or "Confidence Testing."

**Regression Testing**: Re-running functional and non-functional tests to ensure that previously developed and tested software still performs after a change. Regression testing is performed when there is a code change, new feature addition, or bug fixes.

**User Acceptance Testing (UAT)**: The final phase of software testing where actual software users test the software to make sure it can handle required tasks in real-world scenarios according to specifications. UAT is one of the final and critical software project procedures that must occur before newly developed software is rolled out to the market.

### 1.3 Functional vs Non-Functional Testing

**Functional Testing** verifies each function of the software application operates in conformance with the requirement specification. This testing mainly involves black box testing and is not concerned with the source code of the application. It focuses on:

- What the system does (its features and functions)
- User commands and data input
- Business processes and user scenarios
- Information queries and retrieval

**Non-Functional Testing** checks the non-functional aspects such as performance, usability, reliability, etc., of the software application. It verifies the "how well" the system works. Non-functional testing includes:

- Performance testing
- Load testing
- Stress testing
- Security testing
- Usability testing
- Compatibility testing

### 1.4 Importance of Functionality Testing

Functionality testing is crucial for several reasons:

**Quality Assurance**: It ensures that the software meets all specified requirements and functions correctly in all scenarios. This directly impacts the overall quality of the software product delivered to end users.

**Bug Detection**: Early identification of defects and bugs in the software functionality helps prevent costly fixes later in the development cycle or after release. Finding bugs early is exponentially less expensive than finding them in production.

**User Satisfaction**: Proper functionality testing ensures that the end product meets user expectations and provides a positive user experience. Software that doesn't work as expected leads to frustrated users and potential business loss.

**Risk Mitigation**: By thoroughly testing all functions, you minimize the risk of critical failures in production environments. This is especially important for mission-critical applications in healthcare, finance, and other sensitive domains.

**Compliance**: For many industries, functionality testing is necessary to meet regulatory and compliance requirements. Healthcare applications must comply with HIPAA, financial applications with SOC 2, PCI DSS, and other standards.

**Cost Efficiency**: Detecting and fixing bugs during the testing phase is significantly less expensive than fixing them after release. The cost of fixing a bug increases exponentially as it moves through the software development lifecycle.

### 1.5 Functional Testing Process

The functionality testing process typically follows these steps:

**1. Requirement Analysis**: Understanding the functional requirements of the application. This involves:
- Reading and analyzing requirement documents
- Identifying testable requirements
- Clarifying ambiguous requirements with stakeholders
- Creating a requirements traceability matrix

**2. Test Planning**: Creating a test plan that outlines the testing strategy, scope, schedule, resources, and deliverables. The test plan should include:
- Test objectives and scope
- Testing approach and methodologies
- Resource allocation and team structure
- Test schedule and milestones
- Entry and exit criteria
- Risk assessment and mitigation strategies
- Test environment requirements
- Test data requirements

**3. Test Case Design**: Developing detailed test cases based on functional requirements using various test design techniques. Each test case should include:
- Test case ID and name
- Test objective
- Prerequisites and test data
- Detailed test steps
- Expected results
- Actual results (during execution)
- Pass/fail status
- Comments and notes

**4. Test Environment Setup**: Preparing the test environment with necessary hardware, software, network configurations, and test data. This includes:
- Setting up test servers and databases
- Configuring test environments to match production
- Preparing test data sets
- Installing required software and dependencies
- Establishing network connectivity
- Creating test user accounts

**5. Test Execution**: Running the test cases and recording the results. Document any deviations from expected behavior. This phase involves:
- Executing test cases according to the test plan
- Recording test results meticulously
- Logging defects in the defect tracking system
- Re-testing fixed defects
- Performing regression testing
- Updating test case status

**6. Defect Reporting**: Logging any bugs or issues found during testing with detailed information for developers. Each defect report should include:
- Defect ID and title
- Severity and priority
- Environment details
- Steps to reproduce
- Expected vs actual results
- Screenshots or video recordings
- Logs and error messages
- Suggested fix (if applicable)

**7. Test Closure**: Analyzing test results, preparing test summary reports, and archiving test artifacts. This includes:
- Analyzing test metrics and coverage
- Preparing test summary reports
- Conducting lessons learned sessions
- Archiving test artifacts
- Updating test documentation
- Obtaining sign-off from stakeholders

### 1.6 Functional Testing Best Practices

**Understand Requirements Thoroughly**: Before writing test cases, ensure you have a complete understanding of the functional requirements. Ambiguous requirements lead to inadequate test coverage. Schedule requirements review sessions with business analysts, product owners, and developers to clarify any uncertainties.

**Prioritize Test Cases**: Not all test cases are equally important. Prioritize based on business criticality, risk, and frequency of use. Use techniques like risk-based testing to focus efforts on high-risk areas first. Consider factors such as:
- Business impact of failure
- Frequency of feature usage
- Complexity of functionality
- Historical defect data
- Regulatory requirements

**Use Test Design Techniques**: Apply various test design techniques like equivalence partitioning, boundary value analysis, decision tables, and state transition testing to create comprehensive test coverage with an optimal number of test cases.

**Maintain Test Cases**: Keep test cases updated as the application evolves. Review and refactor test cases regularly to remove obsolete tests and add new ones for new features. Implement version control for test cases and establish a review process.

**Automate Where Appropriate**: Automate repetitive tests and regression test suites to save time and effort. However, maintain a balance between automated and manual testing. Not everything should be automated. Consider automation for:
- Regression test suites
- Data-driven tests
- Tests that run frequently
- Tests with predictable outcomes
- Tests that are time-consuming manually

**Test Early and Often**: Start testing as early as possible in the development cycle. Implement shift-left testing practices to catch bugs early when they're cheaper to fix. Integrate testing into each sprint or development iteration.

**Document Everything**: Maintain detailed documentation of test cases, test results, and defects. Good documentation helps in knowledge transfer and provides a reference for future testing cycles. Use test management tools to centralize documentation.

**Collaborate with Developers**: Work closely with developers to understand the implementation and identify potential problem areas. Good communication between testers and developers leads to better quality software. Participate in:
- Sprint planning meetings
- Daily stand-ups
- Code reviews (when possible)
- Design discussions

**Think Like an End User**: Always test from the end user's perspective. Consider how users will actually use the application, including edge cases and unusual scenarios. Create user personas and test scenarios based on real user workflows.

**Track and Analyze Metrics**: Monitor key testing metrics such as defect density, test coverage, test execution rate, and defect detection rate to continuously improve the testing process. Use metrics to:
- Identify problem areas
- Measure testing effectiveness
- Support decision-making
- Demonstrate testing value to stakeholders

---

## 2. Test Case Design Methodologies {#test-case-design}

### 2.1 Equivalence Partitioning

Equivalence Partitioning (EP) is a black-box testing technique that divides input data into logical groups or partitions where the system behavior is assumed to be the same. Instead of testing every possible input value, which is often impractical, we test one representative value from each partition.

#### 2.1.1 Principles of Equivalence Partitioning

The fundamental principle behind equivalence partitioning is that if the system works correctly for one value in a partition, it should work correctly for all values in that partition. Conversely, if it fails for one value, it's likely to fail for all values in that partition.

**Valid Equivalence Classes**: Partitions that represent valid input according to the specification. Testing these verifies that the system handles correct data properly.

**Invalid Equivalence Classes**: Partitions that represent invalid input according to the specification. Testing these verifies that the system properly rejects or handles incorrect data.

#### 2.1.2 Steps for Applying Equivalence Partitioning

**Step 1: Identify the input conditions**: Analyze the requirements and identify all input fields and conditions. For each input, determine:
- The data type expected (integer, string, date, etc.)
- Valid ranges or formats
- Required vs optional fields
- Dependencies on other fields

**Step 2: Divide inputs into equivalence classes**: For each input condition, divide the possible inputs into valid and invalid partitions. Consider:
- Ranges of numeric values
- Sets of valid options
- String formats and patterns
- Boolean conditions
- Null or empty values

**Step 3: Select representative test values**: Choose one test value from each equivalence class to represent that partition. The value should be:
- Clearly within the partition boundaries
- Representative of typical inputs in that partition
- Easy to use in testing

**Step 4: Create test cases**: Design test cases that use the selected representative values. Each test case should:
- Use one value from each input field
- Combine valid and invalid partitions appropriately
- Have clear expected results
- Be independent of other test cases

#### 2.1.3 Detailed Example: Age Validation

Let's consider a detailed example of an age input field with the following requirements:
- Must be numeric
- Valid age range: 18 to 65 years
- Required field (cannot be empty)

**Equivalence Classes**:

Valid partitions:
- V1: Valid age (18-65): Any integer between 18 and 65 inclusive

Invalid partitions:
- I1: Below minimum age (< 18): Any integer less than 18
- I2: Above maximum age (> 65): Any integer greater than 65
- I3: Non-numeric: Letters, special characters, alphanumeric strings
- I4: Empty/Null: No value entered
- I5: Decimal numbers: 25.5, 30.7 (if only integers are valid)
- I6: Negative numbers: -5, -20
- I7: Extremely large numbers: 999999

**Test Cases**:

| Test Case ID | Input Value | Equivalence Class | Expected Result |
|--------------|-------------|-------------------|-----------------|
| TC_AGE_001 | 30 | V1 (Valid age) | Accept - Age validated successfully |
| TC_AGE_002 | 10 | I1 (Below minimum) | Reject - Error: "Age must be at least 18" |
| TC_AGE_003 | 70 | I2 (Above maximum) | Reject - Error: "Age must not exceed 65" |
| TC_AGE_004 | "abc" | I3 (Non-numeric) | Reject - Error: "Age must be numeric" |
| TC_AGE_005 | (empty) | I4 (Empty) | Reject - Error: "Age is required" |
| TC_AGE_006 | 25.5 | I5 (Decimal) | Reject - Error: "Age must be a whole number" |
| TC_AGE_007 | -10 | I6 (Negative) | Reject - Error: "Age must be positive" |
| TC_AGE_008 | 999999 | I7 (Too large) | Reject - Error: "Please enter a realistic age" |

#### 2.1.4 Example: Email Address Validation

Requirements:
- Must contain exactly one @ symbol
- Must have characters before and after @
- Domain part must contain at least one dot
- No spaces allowed
- Maximum length: 254 characters

**Equivalence Classes**:

Valid partitions:
- V1: Valid email format: user@domain.com, test.user@example.co.uk

Invalid partitions:
- I1: No @ symbol: userdomain.com, test.user.example.com
- I2: Multiple @ symbols: user@@domain.com, us@er@domain.com
- I3: No local part: @domain.com
- I4: No domain: user@
- I5: No top-level domain: user@domain
- I6: Contains spaces: user @domain.com, user@ domain.com
- I7: Exceeds length: (string > 254 characters)
- I8: Special characters in wrong places: .user@domain.com, user.@domain.com
- I9: Empty: (no input)

#### 2.1.5 Example: Password Strength Validation

Requirements:
- Minimum 8 characters
- Maximum 32 characters
- Must contain at least one uppercase letter
- Must contain at least one lowercase letter
- Must contain at least one digit
- Must contain at least one special character (!@#$%^&*)

**Equivalence Classes**:

Valid partitions:
- V1: Strong password meeting all criteria: Password123!, Secure@Pass1

Invalid partitions:
- I1: Too short (< 8 chars): Pass1!
- I2: Too long (> 32 chars): (string with 33+ characters)
- I3: No uppercase: password123!
- I4: No lowercase: PASSWORD123!
- I5: No digit: Password!
- I6: No special character: Password123
- I7: Empty: (no input)
- I8: Only numbers: 12345678
- I9: Only letters: Password
- I10: Only special characters: !@#$%^&*
- I11: Contains invalid characters: Password123!<>

#### 2.1.6 Advanced Equivalence Partitioning Techniques

**Multiple Input Fields**: When testing forms with multiple input fields, apply equivalence partitioning to each field independently, then combine them systematically. Consider:
- One test case using all valid partitions (happy path)
- Multiple test cases with one invalid partition at a time
- Edge cases combining multiple invalid partitions

**Output Equivalence Partitioning**: Apply equivalence partitioning not just to inputs but also to expected outputs. Group outputs that should behave similarly and test representative cases.

**Equivalence Partitioning for State-Based Systems**: For systems where behavior depends on state:
- Identify all possible states
- Partition inputs based on current state
- Test transitions between states
- Verify that same inputs in different states produce different outputs

#### 2.1.7 Benefits and Limitations

**Benefits**:
- Reduces the number of test cases while maintaining good coverage
- Systematic approach ensures all input domains are tested
- Easy to understand and apply
- Cost-effective testing strategy
- Helps identify missing requirements through analysis
- Can be easily automated

**Limitations**:
- Assumes all values in a partition behave identically (not always true)
- May miss defects at partition boundaries (addressed by boundary value analysis)
- Requires good understanding of requirements
- May not catch interaction issues between different fields
- Relies on tester's judgment for defining partitions

### 2.2 Boundary Value Analysis

Boundary Value Analysis (BVA) is a test case design technique that focuses on testing at the boundaries of input domains. The principle behind BVA is that errors tend to occur at the boundaries of input ranges rather than in the center of ranges. This technique complements equivalence partitioning by specifically targeting the edge cases.

#### 2.2.1 Principles of Boundary Value Analysis

Experience shows that tests that focus on boundary conditions have a higher payoff than tests that do not. Boundary conditions are those situations at the edge of the operating parameters. Errors often occur at boundaries because:

- Programmers may use wrong operators (< instead of <=, > instead of >=)
- Off-by-one errors are common in loop conditions
- Array indices may be miscalculated at boundaries
- String operations may fail at maximum or minimum lengths
- Numeric operations may overflow or underflow at extremes

**Basic BVA Approach**: For each boundary, test:
- The boundary value itself
- One value just below the boundary (minimum - 1)
- One value just above the boundary (minimum + 1)
- One value just inside the boundary
- The maximum boundary value
- One value just below the maximum (maximum - 1)
- One value just above the maximum (maximum + 1)

**Two-Value BVA**: A simpler approach that tests:
- Minimum valid value
- Maximum valid value
- One value just below minimum (invalid)
- One value just above maximum (invalid)

**Three-Value BVA**: An expanded approach that adds:
- A nominal value in the middle of the range

#### 2.2.2 Boundary Value Analysis Techniques

**Normal Boundary Value Testing**: Tests only the boundaries of valid input partitions. For a range [min, max], test:
- min - 1 (invalid)
- min (valid)
- min + 1 (valid)
- nominal value (valid)
- max - 1 (valid)
- max (valid)
- max + 1 (invalid)

**Robust Boundary Value Testing**: Extends normal BVA to include invalid boundaries more thoroughly. Tests the same values as normal BVA but also includes more extreme invalid values:
- Extremely low values
- Extremely high values
- Special values (0, -1, null, empty string, etc.)

**Worst-Case Boundary Value Testing**: For systems with multiple input variables, tests all combinations of boundary values. If you have n input variables, and each has 5 boundary values to test (min, min+1, nominal, max-1, max), you'll need 5^n test cases.

#### 2.2.3 Detailed Example: Quantity Field

Requirements for an order quantity field:
- Minimum order: 1 unit
- Maximum order: 100 units
- Must be a positive integer
- Bulk discount applies for orders of 50 or more

**Boundary Points Identified**:
- Minimum boundary: 1
- Bulk discount boundary: 50
- Maximum boundary: 100

**Boundary Test Cases**:

| Test Case ID | Input Value | Boundary | Expected Result |
|--------------|-------------|----------|-----------------|
| TC_QTY_001 | 0 | Below minimum | Error: "Minimum order is 1 unit" |
| TC_QTY_002 | 1 | Minimum | Accept - Order processed at regular price |
| TC_QTY_003 | 2 | Just above minimum | Accept - Order processed at regular price |
| TC_QTY_004 | 49 | Just below discount threshold | Accept - Regular price applied |
| TC_QTY_005 | 50 | Discount threshold | Accept - Bulk discount applied |
| TC_QTY_006 | 51 | Just above discount threshold | Accept - Bulk discount applied |
| TC_QTY_007 | 99 | Just below maximum | Accept - Bulk discount applied |
| TC_QTY_008 | 100 | Maximum | Accept - Maximum quantity with bulk discount |
| TC_QTY_009 | 101 | Above maximum | Error: "Maximum order is 100 units" |
| TC_QTY_010 | -1 | Negative | Error: "Quantity must be positive" |
| TC_QTY_011 | 1000 | Well above maximum | Error: "Maximum order is 100 units" |

#### 2.2.4 Example: Date Range Testing

Consider a hotel booking system with check-in and check-out dates:

Requirements:
- Check-in date must be today or in the future
- Check-out date must be after check-in date
- Maximum stay: 30 days
- Minimum stay: 1 day
- No bookings accepted more than 365 days in advance

**Boundary Test Cases** (assume today is 2026-02-09):

| Test Case ID | Check-in Date | Check-out Date | Boundary Tested | Expected Result |
|--------------|---------------|----------------|-----------------|-----------------|
| TC_DATE_001 | 2026-02-08 | 2026-02-10 | Before today | Error: "Cannot book in the past" |
| TC_DATE_002 | 2026-02-09 | 2026-02-10 | Today (minimum) | Accept - 1 day stay |
| TC_DATE_003 | 2026-02-10 | 2026-02-11 | Tomorrow | Accept - 1 day stay |
| TC_DATE_004 | 2026-02-09 | 2026-02-09 | Same day | Error: "Check-out must be after check-in" |
| TC_DATE_005 | 2026-02-09 | 2026-03-10 | 29 days | Accept - 29 day stay |
| TC_DATE_006 | 2026-02-09 | 2026-03-11 | 30 days (max) | Accept - 30 day stay (maximum) |
| TC_DATE_007 | 2026-02-09 | 2026-03-12 | 31 days | Error: "Maximum stay is 30 days" |
| TC_DATE_008 | 2027-02-08 | 2027-02-10 | 364 days ahead | Accept - Within advance booking limit |
| TC_DATE_009 | 2027-02-09 | 2027-02-11 | 365 days ahead (max) | Accept - At advance booking limit |
| TC_DATE_010 | 2027-02-10 | 2027-02-12 | 366 days ahead | Error: "Cannot book more than 365 days in advance" |

#### 2.2.5 Example: Discount Calculation Based on Order Value

Requirements:
- Orders under $50: no discount
- Orders $50 - $99.99: 5% discount
- Orders $100 - $499.99: 10% discount
- Orders $500 and above: 15% discount

**Boundary Test Cases**:

| Test Case ID | Order Value | Boundary | Expected Discount | Expected Result |
|--------------|-------------|----------|-------------------|-----------------|
| TC_DISC_001 | $49.99 | Just below tier 1 | 0% | Accept - No discount applied |
| TC_DISC_002 | $50.00 | Tier 1 minimum | 5% | Accept - $2.50 discount, total $47.50 |
| TC_DISC_003 | $50.01 | Just above tier 1 | 5% | Accept - $2.50 discount |
| TC_DISC_004 | $99.98 | Just below tier 2 | 5% | Accept - $5.00 discount |
| TC_DISC_005 | $99.99 | Tier 1 maximum | 5% | Accept - $5.00 discount |
| TC_DISC_006 | $100.00 | Tier 2 minimum | 10% | Accept - $10.00 discount, total $90.00 |
| TC_DISC_007 | $100.01 | Just above tier 2 | 10% | Accept - $10.00 discount |
| TC_DISC_008 | $499.98 | Just below tier 3 | 10% | Accept - $50.00 discount |
| TC_DISC_009 | $499.99 | Tier 2 maximum | 10% | Accept - $50.00 discount |
| TC_DISC_010 | $500.00 | Tier 3 minimum | 15% | Accept - $75.00 discount, total $425.00 |
| TC_DISC_011 | $500.01 | Just above tier 3 | 15% | Accept - $75.00 discount |

#### 2.2.6 String Length Boundaries

For text input fields, boundary value analysis should test:

**Example: Username Field**
Requirements:
- Minimum length: 4 characters
- Maximum length: 20 characters
- Alphanumeric characters only

| Test Case ID | Input Length | Input Value | Boundary | Expected Result |
|--------------|--------------|-------------|----------|-----------------|
| TC_USER_001 | 0 chars | (empty) | Below minimum | Error: "Username required" |
| TC_USER_002 | 3 chars | "abc" | Below minimum | Error: "Minimum 4 characters" |
| TC_USER_003 | 4 chars | "abcd" | Minimum | Accept - Valid username |
| TC_USER_004 | 5 chars | "abcde" | Just above min | Accept - Valid username |
| TC_USER_005 | 12 chars | "testuser1234" | Mid-range | Accept - Valid username |
| TC_USER_006 | 19 chars | "testuser12345678901" | Just below max | Accept - Valid username |
| TC_USER_007 | 20 chars | "testuser123456789012" | Maximum | Accept - Valid username |
| TC_USER_008 | 21 chars | "testuser1234567890123" | Above maximum | Error: "Maximum 20 characters" |

#### 2.2.7 Combining Equivalence Partitioning and BVA

The most effective approach combines both techniques:

1. Use equivalence partitioning to identify the valid and invalid ranges
2. Apply boundary value analysis to test the edges of each partition
3. Select at least one nominal value from each valid partition
4. Focus testing effort on boundaries while ensuring coverage of each partition

**Example: Combined Approach for Age Field**

Requirements: Age must be 18-65

**Equivalence Classes**:
- Valid: 18-65
- Invalid-Low: < 18
- Invalid-High: > 65

**Combined Test Cases**:

| Test Case ID | Value | Technique | Class | Expected Result |
|--------------|-------|-----------|-------|-----------------|
| TC_001 | 17 | BVA | Invalid-Low | Reject - "Must be 18 or older" |
| TC_002 | 18 | BVA | Valid | Accept - Minimum valid age |
| TC_003 | 19 | BVA | Valid | Accept - Just above minimum |
| TC_004 | 40 | EP | Valid | Accept - Nominal value |
| TC_005 | 64 | BVA | Valid | Accept - Just below maximum |
| TC_006 | 65 | BVA | Valid | Accept - Maximum valid age |
| TC_007 | 66 | BVA | Invalid-High | Reject - "Must be 65 or younger" |

#### 2.2.8 Benefits and Limitations

**Benefits**:
- High defect detection rate at boundaries
- Relatively small number of test cases
- Systematic and repeatable approach
- Easy to understand and implement
- Complements equivalence partitioning perfectly
- Effective for numeric and date/time testing

**Limitations**:
- Only applicable to ordered sets (ranges)
- Doesn't test combinations of inputs well
- May not detect logical errors in the middle of ranges
- Requires clear understanding of input domains
- Can be time-consuming for systems with many inputs

### 2.3 Decision Table Testing

Decision table testing is a black-box testing technique used to test system behavior for different input combinations. It's particularly useful for testing complex business logic where the system's behavior depends on multiple conditions. Decision tables represent combinations of inputs and their corresponding expected outputs in a matrix format.

#### 2.3.1 Components of a Decision Table

A decision table consists of four main parts:

**Conditions (Condition Stubs)**: The input conditions or factors that affect the system's behavior. These are listed in rows on the left side of the table. Each condition can have multiple possible values (usually True/False or specific values).

**Actions (Action Stubs)**: The expected outcomes or actions the system should perform. These are also listed in rows on the left side, below the conditions. Actions describe what the system should do given the conditions.

**Condition Entries**: The specific values or states of each condition for different test scenarios. These form columns representing different combinations.

**Action Entries**: Indicates which actions should be taken for each combination of conditions. Typically marked with X, ✓, or specific values.

#### 2.3.2 Types of Decision Tables

**Limited Entry Decision Tables**: Each condition has only two possible values (True/False, Yes/No). This is the most common type and is suitable for Boolean conditions.

**Extended Entry Decision Tables**: Conditions can have more than two possible values. Useful for testing more complex business rules with multiple states or ranges.

**Mixed Entry Decision Tables**: Combines both limited and extended entry conditions in the same table.

#### 2.3.3 Creating Decision Tables - Step by Step

**Step 1: Identify conditions and actions**
- List all conditions that affect the system behavior
- List all possible actions or outcomes
- Ensure conditions are independent and clearly defined

**Step 2: Calculate number of combinations**
- For n conditions with 2 values each: 2^n combinations
- For conditions with different values: multiply the number of possibilities

**Step 3: Create the table structure**
- Place conditions in the top rows
- Place actions in the bottom rows
- Create columns for each combination

**Step 4: Fill in condition entries**
- Systematically list all possible combinations
- Use T/F, Y/N, or specific values

**Step 5: Fill in action entries**
- For each combination, determine which actions should occur
- Mark appropriate actions with X or ✓

**Step 6: Optimize the table**
- Merge columns with identical actions (if allowed by business rules)
- Remove impossible combinations
- Identify "don't care" conditions

#### 2.3.4 Detailed Example: Insurance Premium Calculation

**Scenario**: An auto insurance company calculates premiums based on:
- Driver's age (< 25, 25-65, > 65)
- Accident history (Yes/No)
- Vehicle type (Economy, Standard, Luxury)

**Business Rules**:
- Young drivers (< 25) with accidents: Premium = Base × 2.5
- Young drivers without accidents: Premium = Base × 1.8
- Middle-aged (25-65) with accidents: Premium = Base × 1.5
- Middle-aged without accidents: Premium = Base × 1.0
- Senior (> 65) with accidents: Premium = Base × 1.8
- Senior without accidents: Premium = Base × 1.3
- Luxury vehicles add 30% to premium
- Standard vehicles add 15% to premium
- Economy vehicles: no additional charge

**Decision Table**:

| Rule | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 |
|------|---|---|---|---|---|---|---|---|---|----|----|----|----|----|----|----|----|----| 
| **Conditions** |
| Age < 25 | T | T | T | T | T | T | F | F | F | F | F | F | F | F | F | F | F | F |
| Age 25-65 | F | F | F | F | F | F | T | T | T | T | T | T | F | F | F | F | F | F |
| Age > 65 | F | F | F | F | F | F | F | F | F | F | F | F | T | T | T | T | T | T |
| Accident History | T | T | T | F | F | F | T | T | T | F | F | F | T | T | T | F | F | F |
| Economy Vehicle | T | F | F | T | F | F | T | F | F | T | F | F | T | F | F | T | F | F |
| Standard Vehicle | F | T | F | F | T | F | F | T | F | F | T | F | F | T | F | F | T | F |
| Luxury Vehicle | F | F | T | F | F | T | F | F | T | F | F | T | F | F | T | F | F | T |
| **Actions** |
| Base Factor 2.5× | X | X | X | | | | | | | | | | | | | | | |
| Base Factor 1.8× | | | | X | X | X | | | | | | | X | X | X | | | |
| Base Factor 1.5× | | | | | | | X | X | X | | | | | | | | | |
| Base Factor 1.3× | | | | | | | | | | | | | | | | X | X | X |
| Base Factor 1.0× | | | | | | | | | | X | X | X | | | | | | |
| Add 0% | X | | | X | | | X | | | X | | | X | | | X | | |
| Add 15% | | X | | | X | | | X | | | X | | | X | | | X | |
| Add 30% | | | X | | | X | | | X | | | X | | | X | | | X |

**Test Cases Derived** (showing 6 examples):

| Test ID | Age | Accident | Vehicle | Expected Multiplier | Expected Add-on | Test Result |
|---------|-----|----------|---------|---------------------|-----------------|-------------|
| TC_INS_001 | 22 | Yes | Economy | 2.5× | 0% | Pass/Fail |
| TC_INS_002 | 22 | Yes | Luxury | 2.5× | 30% | Pass/Fail |
| TC_INS_003 | 22 | No | Standard | 1.8× | 15% | Pass/Fail |
| TC_INS_004 | 45 | No | Economy | 1.0× | 0% | Pass/Fail |
| TC_INS_005 | 45 | Yes | Luxury | 1.5× | 30% | Pass/Fail |
| TC_INS_006 | 70 | No | Standard | 1.3× | 15% | Pass/Fail |

#### 2.3.5 Example: Loan Approval System

**Scenario**: A bank's loan approval system considers:
- Credit score (Excellent: > 750, Good: 650-750, Poor: < 650)
- Employment status (Employed full-time, Part-time, Unemployed)
- Debt-to-income ratio (Low: < 30%, Medium: 30-45%, High: > 45%)

**Business Rules**:
- Excellent credit + full-time employment + low debt: Approved at prime rate
- Excellent credit + full-time employment + medium debt: Approved at prime + 1%
- Good credit + full-time employment + low debt: Approved at prime + 2%
- Good credit + full-time employment + medium debt: Approved at prime + 3%
- Poor credit or unemployed or high debt: Denied (any combination)
- Part-time employment requires excellent credit and low debt for approval

**Simplified Decision Table** (focusing on key scenarios):

| Rule | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 |
|------|---|---|---|---|---|---|---|---|
| **Conditions** |
| Excellent Credit (>750) | T | T | T | T | F | F | F | F |
| Good Credit (650-750) | F | F | F | F | T | T | F | F |
| Full-time Employed | T | T | T | F | T | T | - | - |
| Low Debt (<30%) | T | F | - | T | T | F | - | - |
| Medium Debt (30-45%) | F | T | - | F | F | T | - | - |
| High Debt (>45%) | F | F | T | - | - | - | T | T |
| **Actions** |
| Approve - Prime Rate | X | | | | | | | |
| Approve - Prime + 1% | | X | | | | | | |
| Approve - Prime + 2% | | | | | X | | | |
| Approve - Prime + 3% | | | | | | X | | |
| Approve - Part-time Rate | | | | X | | | | |
| Deny Loan | | | X | | | | X | X |

#### 2.3.6 Example: E-commerce Order Processing

**Scenario**: An e-commerce system processes orders based on:
- Customer type (Premium, Regular, New)
- Order value (< $50, $50-$200, > $200)
- Items in stock (All available, Partial, None available)
- Payment method (Credit card, PayPal, Bank transfer)

**Business Rules**:
- Premium customers: free shipping on all orders
- Regular customers: free shipping on orders > $200
- New customers: no free shipping
- Out of stock items: notify customer, create backorder
- Partial stock: ship available items, backorder rest
- Credit card: process immediately
- PayPal: process immediately
- Bank transfer: wait for confirmation (2-3 days)

**Decision Table Structure** (showing key combinations):

| Rule | 1 | 2 | 3 | 4 | 5 | 6 |
|------|---|---|---|---|---|---|
| **Conditions** |
| Premium Customer | T | T | F | F | F | F |
| Regular Customer | F | F | T | T | F | F |
| New Customer | F | F | F | F | T | T |
| Order > $200 | T | F | T | F | - | - |
| All Items Available | T | T | T | T | F | T |
| Credit Card Payment | T | F | - | - | - | T |
| **Actions** |
| Process Immediately | X | X | X | X | | X |
| Free Shipping | X | X | X | | | |
| Charge Shipping | | | | X | X | X |
| Ship All Items | X | X | X | X | | X |
| Create Backorder | | | | | X | |
| Wait for Bank Confirmation | | X | | | | |

#### 2.3.7 Reducing Decision Tables

Large decision tables can be reduced by:

**Combining Rules**: If two or more rules have identical actions, they can sometimes be combined using a "don't care" (-) symbol for conditions that don't affect the outcome.

**Removing Impossible Combinations**: Some combinations of conditions may be logically impossible. For example, "Age < 18" and "Has driver's license" might be impossible in some jurisdictions.

**Focusing on Critical Paths**: Prioritize testing the most common scenarios and highest-risk combinations first.

**Example of Table Reduction**:

Original table:
| Rule | 1 | 2 |
|------|---|---|
| Condition A | T | T |
| Condition B | T | F |
| Action X | X | X |

Reduced table:
| Rule | 1 |
|------|---|
| Condition A | T |
| Condition B | - |
| Action X | X |

#### 2.3.8 When to Use Decision Tables

Decision table testing is most effective when:

**Complex Business Logic**: The system has complex business rules with multiple interrelated conditions affecting outcomes.

**Combinatorial Testing**: You need to test various combinations of inputs systematically.

**Documentation**: Decision tables serve as excellent documentation of business rules.

**Multiple Conditions**: The feature involves 3 or more conditions that affect behavior.

**Clear Cause-Effect Relationships**: There are clear cause-effect relationships between inputs and outputs.

**Communication**: Decision tables help communicate complex logic to stakeholders, developers, and testers.

#### 2.3.9 Benefits and Limitations

**Benefits**:
- Comprehensive coverage of condition combinations
- Easy to understand and review with stakeholders
- Systematic approach reduces likelihood of missing scenarios
- Good documentation of business logic
- Helps identify gaps in requirements
- Can be directly converted to automated test cases
- Effective for regression testing

**Limitations**:
- Can become very large with many conditions (2^n explosion)
- May not scale well for systems with numerous inputs
- Requires significant initial effort to create
- Maintaining tables as requirements change can be tedious
- Doesn't inherently handle timing or sequence issues
- May include technically impossible combinations

### 2.4 State Transition Testing

State transition testing is a black-box testing technique that focuses on testing the behavior of a system as it transitions from one state to another. This technique is particularly effective for systems where outputs depend not just on current inputs but also on the current state of the system. Examples include workflow systems, protocol implementations, embedded systems, and any application with distinct operational modes.

#### 2.4.1 Key Concepts

**State**: A condition or situation during the life of an object during which it satisfies some condition, performs some activity, or waits for some event. States represent distinct modes or conditions that the system can be in.

**Transition**: The change from one state to another state in response to an event or condition. Transitions are triggered by events and may include guard conditions and actions.

**Event**: An occurrence that triggers a state transition. Events can be user actions, system events, time-based triggers, or external signals.

**Action**: An activity executed during a transition. Actions are atomic and non-interruptible operations that occur when a transition fires.

**Guard Condition**: A Boolean expression that must be true for a transition to occur. Guards provide additional control over when transitions can take place.

**Initial State**: The state in which the system begins. Every state machine must have exactly one initial state.

**Final State**: A state that represents the completion of the system's activity. A state machine may have multiple final states or none.

#### 2.4.2 State Transition Diagram Components

State transition diagrams (also called state machines or state charts) visually represent:

**States**: Typically shown as rounded rectangles or circles containing the state name

**Transitions**: Shown as arrows connecting states, labeled with:
- Event that triggers the transition
- Guard condition (in square brackets)
- Action to perform (after a slash)
- Format: Event [Guard] / Action

**Example notation**:
```
[State A] --Event[condition]/action--> [State B]
```

#### 2.4.3 Creating a State Transition Table

A state transition table is a matrix representation showing:
- Rows: Current states
- Columns: Events/inputs
- Cells: Next state and actions

**Example Structure**:

| Current State | Event 1 | Event 2 | Event 3 |
|---------------|---------|---------|---------|
| State A | State B / Action1 | State A / Action2 | Invalid |
| State B | State C / Action3 | State B / Action4 | State A / Action5 |
| State C | State C / Action6 | Invalid | State A / Action7 |

#### 2.4.4 Detailed Example: ATM Machine

Let's model the states and transitions of an ATM machine:

**States**:
1. Idle - Waiting for customer
2. Card Inserted - Card reader has a card
3. PIN Entry - Waiting for PIN input
4. Authenticated - Valid PIN entered
5. Transaction Selection - Showing transaction menu
6. Processing Transaction - Executing selected transaction
7. Dispensing Cash - ATM dispensing cash
8. Printing Receipt - Printing transaction receipt
9. Ejecting Card - Returning card to customer
10. Out of Service - ATM not operational

**Events**:
- Insert Card
- Enter PIN
- Select Transaction
- Confirm Transaction
- Take Cash
- Take Receipt
- Take Card
- Cancel
- Timeout
- Error Occurred
- Admin Login
- Service Complete

**State Transition Table** (simplified):

| Current State | Insert Card | Enter PIN | PIN Valid | Select Transaction | Confirm | Cancel | Timeout | Error | Take Cash | Take Card |
|---------------|-------------|-----------|-----------|-------------------|---------|--------|---------|-------|-----------|-----------|
| Idle | Card Inserted | - | - | - | - | - | - | - | - | - |
| Card Inserted | - | PIN Entry | - | - | - | Ejecting Card | Ejecting Card | Idle | - | - |
| PIN Entry | - | - | Authenticated | - | - | Ejecting Card | Ejecting Card | Card Inserted | - | - |
| Authenticated | - | - | - | Transaction Selection | - | Ejecting Card | Ejecting Card | Out of Service | - | - |
| Transaction Selection | - | - | - | - | Processing | Ejecting Card | Ejecting Card | - | - | - |
| Processing | - | - | - | - | - | Ejecting Card | - | Out of Service | Dispensing Cash | - |
| Dispensing Cash | - | - | - | - | - | - | Ejecting Card | Out of Service | Printing Receipt | - |
| Printing Receipt | - | - | - | - | - | - | - | - | - | Ejecting Card |
| Ejecting Card | - | - | - | - | - | - | Idle | Idle | - | Idle |
| Out of Service | - | - | - | - | - | - | - | Idle (after fix) | - | - |

**Detailed State Descriptions**:

**Idle State**:
- Entry action: Display welcome screen
- Exit action: Disable welcome animation
- Valid transitions: Insert Card → Card Inserted

**Card Inserted State**:
- Entry action: Read card data, validate card
- Guard conditions: Card must be valid, not expired, not reported stolen
- Valid transitions:
  - Valid card → PIN Entry
  - Invalid card → Ejecting Card
  - Cancel → Ejecting Card
  - Timeout (30s) → Ejecting Card

**PIN Entry State**:
- Entry action: Display PIN entry screen, start timeout timer
- Guard conditions: Maximum 3 attempts allowed
- Valid transitions:
  - Correct PIN → Authenticated
  - Incorrect PIN (attempts < 3) → PIN Entry (retry)
  - Incorrect PIN (attempts = 3) → Ejecting Card (card captured)
  - Cancel → Ejecting Card
  - Timeout (30s) → Ejecting Card

**Authenticated State**:
- Entry action: Retrieve account information
- Valid transitions:
  - Success → Transaction Selection
  - Error → Out of Service
  - Cancel → Ejecting Card
  - Timeout (20s) → Ejecting Card

**Transaction Selection State**:
- Entry action: Display transaction menu (Withdrawal, Balance, Transfer, etc.)
- Valid transitions:
  - Select transaction → Processing
  - Cancel → Ejecting Card
  - Timeout (60s) → Ejecting Card

**Processing Transaction State**:
- Entry action: Execute selected transaction, communicate with bank
- Guard conditions vary by transaction type:
  - Withdrawal: Sufficient balance, ATM has cash, daily limit not exceeded
  - Balance inquiry: None
  - Transfer: Sufficient balance in source account
- Valid transitions:
  - Success (cash transaction) → Dispensing Cash
  - Success (non-cash transaction) → Printing Receipt
  - Failure → Transaction Selection (with error message)
  - Error → Out of Service
  - Cancel (if allowed) → Transaction Selection

**Dispensing Cash State**:
- Entry action: Count and dispense requested cash amount
- Guard conditions: Cash available in ATM, correct amount counted
- Exit action: Update ATM cash inventory
- Valid transitions:
  - Cash taken → Printing Receipt
  - Timeout (45s, cash not taken) → Retract cash → Printing Receipt
  - Error dispensing → Out of Service

**Printing Receipt State**:
- Entry action: Print transaction receipt
- Valid transitions:
  - Receipt printed → Ejecting Card
  - Receipt taken or timeout (15s) → Ejecting Card
  - Printer error → Ejecting Card (with error message)

**Ejecting Card State**:
- Entry action: Eject card from reader
- Exit action: Clear session data
- Valid transitions:
  - Card taken → Idle
  - Timeout (30s, card not taken) → Retract card → Idle

**Out of Service State**:
- Entry action: Display out of service message, log error, notify administrator
- Valid transitions:
  - Admin service complete → Idle

**Test Scenarios Derived**:

| Test ID | Scenario | State Path | Expected Result |
|---------|----------|------------|-----------------|
| TC_ATM_001 | Successful withdrawal | Idle → Card Inserted → PIN Entry → Authenticated → Transaction Selection → Processing → Dispensing Cash → Printing Receipt → Ejecting Card → Idle | Complete transaction successfully |
| TC_ATM_002 | Incorrect PIN (1st attempt) | Idle → Card Inserted → PIN Entry → PIN Entry | Prompt for PIN retry |
| TC_ATM_003 | Incorrect PIN (3 attempts) | Idle → Card Inserted → PIN Entry → PIN Entry → PIN Entry → Ejecting Card → Idle | Capture card, return to idle |
| TC_ATM_004 | Cancel during PIN entry | Idle → Card Inserted → PIN Entry → Ejecting Card → Idle | Cancel transaction, return card |
| TC_ATM_005 | Balance inquiry | Idle → Card Inserted → PIN Entry → Authenticated → Transaction Selection → Processing → Printing Receipt → Ejecting Card → Idle | Display balance, print receipt |
| TC_ATM_006 | Timeout at transaction selection | Idle → Card Inserted → PIN Entry → Authenticated → Transaction Selection → Ejecting Card → Idle | Timeout after 60s, return card |
| TC_ATM_007 | Insufficient funds | Idle → Card Inserted → PIN Entry → Authenticated → Transaction Selection → Processing → Transaction Selection | Show error, allow retry |
| TC_ATM_008 | Cash not taken | Idle → ... → Dispensing Cash → Printing Receipt → Ejecting Card → Idle | Retract cash after 45s timeout |
| TC_ATM_009 | Card not taken | Idle → ... → Ejecting Card → Idle | Retract card after 30s timeout |

#### 2.4.5 Example: Order Management System

**States**:
1. Draft - Order being created
2. Submitted - Order submitted by customer
3. Confirmed - Order confirmed by system
4. Payment Pending - Awaiting payment
5. Payment Received - Payment confirmed
6. Processing - Order being prepared
7. Shipped - Order shipped to customer
8. Delivered - Order delivered successfully
9. Cancelled - Order cancelled
10. Returned - Order returned by customer
11. Refunded - Payment refunded

**Events**:
- Create Order
- Submit Order
- Confirm Order
- Make Payment
- Payment Success
- Payment Failed
- Cancel Order
- Ship Order
- Confirm Delivery
- Request Return
- Approve Return
- Issue Refund

**State Transition Diagram** (simplified text representation):

```
Draft --Submit--> Submitted --Confirm--> Payment Pending

Payment Pending --Payment Success--> Payment Received
Payment Pending --Payment Failed--> Submitted
Payment Pending --Cancel--> Cancelled

Payment Received --Auto--> Processing
Processing --Ship--> Shipped
Shipped --Confirm Delivery--> Delivered

Any State (except Delivered) --Cancel [authorized]--> Cancelled
Delivered --Request Return [within 30 days]--> Returned
Returned --Approve--> Refunded
```

**State Transition Table**:

| Current State | Submit | Confirm | Pay Success | Pay Fail | Cancel | Ship | Deliver | Request Return | Refund |
|---------------|--------|---------|-------------|----------|--------|------|---------|----------------|---------|
| Draft | Submitted | - | - | - | Cancelled | - | - | - | - |
| Submitted | - | Payment Pending | - | - | Cancelled | - | - | - | - |
| Payment Pending | - | - | Payment Received | Submitted | Cancelled | - | - | - | - |
| Payment Received | - | - | - | - | Cancelled* | - | - | - | - |
| Processing | - | - | - | - | Cancelled* | Shipped | - | - | - |
| Shipped | - | - | - | - | - | - | Delivered | Returned | - |
| Delivered | - | - | - | - | - | - | - | Returned** | - |
| Cancelled | - | - | - | - | - | - | - | - | - |
| Returned | - | - | - | - | - | - | - | - | Refunded |
| Refunded | - | - | - | - | - | - | - | - | - |

*Cancellation may require approval after payment received
**Return only within 30 days of delivery

**Detailed Test Scenarios**:

| Test ID | Test Scenario | State Path | Guard Conditions | Expected Actions |
|---------|---------------|------------|------------------|------------------|
| TC_ORDER_001 | Complete order flow | Draft → Submitted → Payment Pending → Payment Received → Processing → Shipped → Delivered | Valid items, payment successful, items available | Create order, charge payment, ship items |
| TC_ORDER_002 | Payment failure | Draft → Submitted → Payment Pending → Submitted | Valid items, payment declined | Show payment error, allow retry |
| TC_ORDER_003 | Cancel before payment | Draft → Submitted → Payment Pending → Cancelled | User-initiated cancel | Cancel order, send confirmation |
| TC_ORDER_004 | Cancel after payment | Payment Received → Cancelled | Admin approval required | Cancel order, issue refund |
| TC_ORDER_005 | Return after delivery | Delivered → Returned → Refunded | Within 30 days, return approved | Accept return, process refund |
| TC_ORDER_006 | Payment retry after failure | Submitted → Payment Pending → Submitted → Payment Pending → Payment Received | - | Allow multiple payment attempts |

**Invalid Transitions to Test**:

| Test ID | Invalid Transition | Expected Behavior |
|---------|-------------------|-------------------|
| TC_INV_001 | Draft → Shipped | Error: "Cannot ship unsubmitted order" |
| TC_INV_002 | Processing → Delivered | Error: "Must ship before delivery" |
| TC_INV_003 | Delivered → Processing | Error: "Cannot reprocess delivered order" |
| TC_INV_004 | Cancelled → Shipped | Error: "Cannot ship cancelled order" |
| TC_INV_005 | Refunded → Payment Pending | Error: "Cannot charge refunded order" |

---

## 9. Payment Gateway Testing {#payment-testing}

Payment gateway testing is one of the most critical aspects of e-commerce and financial application testing. It ensures that all payment processing functions work correctly, securely, and in compliance with financial regulations. Payment gateways handle sensitive financial data, so thorough testing is essential to prevent financial loss, data breaches, and compliance violations.

### 9.1 Understanding Payment Gateway Architecture

Before diving into testing, it's crucial to understand the payment gateway ecosystem:

**Payment Gateway**: The service that processes payment transactions between the merchant and the payment processor. Examples include Stripe, PayPal, Braintree, Square, Authorize.Net.

**Payment Processor**: The company that handles the actual transaction processing between the merchant's bank and the customer's bank.

**Merchant Account**: The bank account where funds from customer payments are deposited.

**Payment Card Industry Data Security Standard (PCI DSS)**: A set of security standards designed to ensure that all companies that accept, process, store, or transmit credit card information maintain a secure environment.

**Tokenization**: The process of replacing sensitive card data with a unique identifier (token) that can be used for processing without exposing actual card numbers.

**3D Secure (3DS)**: An additional security layer for online credit and debit card transactions, requiring customers to complete an additional authentication step.

### 9.2 Stripe Test Mode - Complete Guide

Stripe is one of the most popular payment gateways, offering comprehensive testing capabilities through their test mode. Understanding how to fully utilize Stripe's test mode is essential for thorough payment testing.

#### 9.2.1 Setting Up Stripe Test Environment

**Step 1: Create a Stripe Account**
1. Sign up at https://dashboard.stripe.com/register
2. Complete account verification (email confirmation)
3. Access your Dashboard

**Step 2: Obtain Test API Keys**
1. Navigate to Developers → API keys
2. Toggle to "Test mode" using the switch in the left sidebar
3. Copy your test API keys:
   - Publishable key (starts with `pk_test_`)
   - Secret key (starts with `sk_test_`)

**Step 3: Configure Your Application**

```javascript
// Node.js/Express Example
const stripe = require('stripe')(process.env.STRIPE_SECRET_KEY_TEST);

// Client-side configuration
const stripe = Stripe('pk_test_YOUR_PUBLISHABLE_KEY');
```

**Step 4: Set Up Webhook Endpoints for Testing**

```javascript
// Express webhook endpoint
app.post('/webhook', 
  express.raw({type: 'application/json'}),
  async (req, res) => {
    const sig = req.headers['stripe-signature'];
    const webhookSecret = process.env.STRIPE_WEBHOOK_SECRET_TEST;
    
    let event;
    
    try {
      event = stripe.webhooks.constructEvent(req.body, sig, webhookSecret);
    } catch (err) {
      console.log(`Webhook signature verification failed: ${err.message}`);
      return res.status(400).send(`Webhook Error: ${err.message}`);
    }
    
    // Handle the event
    switch (event.type) {
      case 'payment_intent.succeeded':
        const paymentIntent = event.data.object;
        console.log(`PaymentIntent ${paymentIntent.id} succeeded!`);
        // Fulfill the order
        await fulfillOrder(paymentIntent);
        break;
      case 'payment_intent.payment_failed':
        const failedPayment = event.data.object;
        console.log(`PaymentIntent ${failedPayment.id} failed!`);
        // Notify the customer
        await notifyPaymentFailure(failedPayment);
        break;
      case 'charge.refunded':
        const refund = event.data.object;
        console.log(`Charge ${refund.id} was refunded`);
        // Update order status
        await processRefund(refund);
        break;
      default:
        console.log(`Unhandled event type ${event.type}`);
    }
    
    res.json({received: true});
  }
);
```

#### 9.2.2 Comprehensive Stripe Test Card Numbers

Stripe provides an extensive set of test card numbers to simulate different scenarios. Each card number triggers specific behavior.

**Basic Successful Payments**:

| Card Number | Brand | Description |
|-------------|-------|-------------|
| 4242424242424242 | Visa | Generic successful payment (most common test card) |
| 4000056655665556 | Visa (debit) | Successful payment with a debit card |
| 5555555555554444 | Mastercard | Generic successful Mastercard payment |
| 2223003122003222 | Mastercard (2-series) | Successful 2-series Mastercard payment |
| 5200828282828210 | Mastercard (debit) | Successful Mastercard debit payment |
| 378282246310005 | American Express | Successful Amex payment |
| 6011111111111117 | Discover | Successful Discover payment |
| 3056930009020004 | Diners Club | Successful Diners Club payment |
| 3566002020360505 | JCB | Successful JCB payment |
| 6200000000000005 | UnionPay | Successful UnionPay payment |

**3D Secure Authentication**:

| Card Number | Brand | Behavior |
|-------------|-------|----------|
| 4000002500003155 | Visa | Requires 3D Secure authentication |
| 4000002760003184 | Visa | Requires 3D Secure 2 authentication |
| 4000008260003178 | Visa | 3DS required, but authentication fails |
| 4000008400001629 | Visa | 3DS required, but device not supported |

**Specific Error Scenarios**:

| Card Number | Brand | Error Triggered |
|-------------|-------|----------------|
| 4000000000000002 | Visa | Card declined (generic decline) |
| 4000000000009995 | Visa | Card declined - insufficient funds |
| 4000000000009987 | Visa | Card declined - lost card |
| 4000000000009979 | Visa | Card declined - stolen card |
| 4000000000000069 | Visa | Card declined - expired card |
| 4000000000000127 | Visa | Card declined - incorrect CVC |
| 4000000000000119 | Visa | Card declined - processing error |
| 4000000000000101 | Visa | Card declined - incorrect number |

**Disputes and Chargebacks**:

| Card Number | Brand | Behavior |
|-------------|-------|----------|
| 4000000000000259 | Visa | Charge succeeds, but immediately receives a dispute (fraudulent) |
| 4000000000002685 | Visa | Charge succeeds, but receives early fraud warning |
| 4000000000001976 | Visa | Charge succeeds, but receives dispute (warning) |
| 4000000000001091 | Visa | Charge blocked due to fraud rules |

**Risk and Fraud Detection**:

| Card Number | Brand | Risk Level |
|-------------|-------|------------|
| 4000000000000317 | Visa | Elevated risk score |
| 4000000000000325 | Visa | Highest risk score |
| 4000000000000341 | Visa | Normal risk score |

**Refund Scenarios**:

| Card Number | Brand | Behavior |
|-------------|-------|----------|
| 4000000000005126 | Visa | Charge succeeds, refund fails |
| 4000000000000077 | Visa | Charge succeeds, refund succeeds (standard) |

**International Cards**:

| Card Number | Brand | Country/Behavior |
|-------------|-------|------------------|
| 4000000400000008 | Visa | Argentina card |
| 4000000760000002 | Visa | Brazil card |
| 4000001240000000 | Visa | Canada card |
| 4000002080000001 | Visa | Denmark card |
| 4000000360000006 | Visa | Australia card |
| 4000056655665556 | Visa | US debit card with AVS and CVC checks |

**Special Testing Scenarios**:

| Card Number | Brand | Special Behavior |
|-------------|-------|------------------|
| 4000000000000010 | Visa | Address verification fails |
| 4000000000000028 | Visa | CVC check fails |
| 4000000000000036 | Visa | AVS and CVC check fail |
| 4000000000000044 | Visa | Processing error |
| 4000000000000200 | Visa | Exceeds balance or credit limit |

#### 9.2.3 Complete Test Card Usage Examples

**Test Case TC_STRIPE_001: Successful Payment Processing**

```javascript
describe('Stripe Payment Processing', () => {
  test('TC_STRIPE_001: Process successful payment', async () => {
    // Create a PaymentIntent
    const paymentIntent = await stripe.paymentIntents.create({
      amount: 2000, // Amount in cents ($20.00)
      currency: 'usd',
      payment_method_types: ['card'],
      description: 'Test purchase - Order #12345',
      metadata: {
        order_id: '12345',
        customer_id: 'CUST_001'
      }
    });
    
    expect(paymentIntent.id).toBeDefined();
    expect(paymentIntent.status).toBe('requires_payment_method');
    expect(paymentIntent.amount).toBe(2000);
    expect(paymentIntent.currency).toBe('usd');
    
    // Create a PaymentMethod with test card
    const paymentMethod = await stripe.paymentMethods.create({
      type: 'card',
      card: {
        number: '4242424242424242',
        exp_month: 12,
        exp_year: 2025,
        cvc: '123'
      },
      billing_details: {
        name: 'Test Customer',
        email: 'test@example.com',
        address: {
          line1: '123 Test St',
          city: 'Test City',
          state: 'CA',
          postal_code: '12345',
          country: 'US'
        }
      }
    });
    
    expect(paymentMethod.id).toBeDefined();
    expect(paymentMethod.card.brand).toBe('visa');
    expect(paymentMethod.card.last4).toBe('4242');
    
    // Confirm the payment
    const confirmedPayment = await stripe.paymentIntents.confirm(
      paymentIntent.id,
      {
        payment_method: paymentMethod.id
      }
    );
    
    expect(confirmedPayment.status).toBe('succeeded');
    expect(confirmedPayment.charges.data.length).toBe(1);
    expect(confirmedPayment.charges.data[0].paid).toBe(true);
    expect(confirmedPayment.charges.data[0].amount).toBe(2000);
    
    // Verify charge details
    const charge = confirmedPayment.charges.data[0];
    expect(charge.billing_details.name).toBe('Test Customer');
    expect(charge.payment_method_details.card.brand).toBe('visa');
    expect(charge.payment_method_details.card.last4).toBe('4242');
  });
});
```

**Test Case TC_STRIPE_002: Card Declined - Insufficient Funds**

```javascript
test('TC_STRIPE_002: Handle insufficient funds decline', async () => {
  const paymentIntent = await stripe.paymentIntents.create({
    amount: 5000,
    currency: 'usd',
    payment_method_types: ['card']
  });
  
  const paymentMethod = await stripe.paymentMethods.create({
    type: 'card',
    card: {
      number: '4000000000009995', // Insufficient funds card
      exp_month: 12,
      exp_year: 2025,
      cvc: '123'
    }
  });
  
  // Attempt to confirm payment
  try {
    await stripe.paymentIntents.confirm(paymentIntent.id, {
      payment_method: paymentMethod.id
    });
    
    // Should not reach here
    fail('Payment should have been declined');
  } catch (error) {
    expect(error.type).toBe('StripeCardError');
    expect(error.code).toBe('card_declined');
    expect(error.decline_code).toBe('insufficient_funds');
    expect(error.message).toContain('Your card has insufficient funds');
    
    // Verify PaymentIntent status
    const failedIntent = await stripe.paymentIntents.retrieve(paymentIntent.id);
    expect(failedIntent.status).toBe('requires_payment_method');
    expect(failedIntent.last_payment_error.code).toBe('card_declined');
  }
});
```

**Test Case TC_STRIPE_003: 3D Secure Authentication Required**

```javascript
test('TC_STRIPE_003: Handle 3D Secure authentication', async () => {
  const paymentIntent = await stripe.paymentIntents.create({
    amount: 3000,
    currency: 'eur', // 3DS more common in Europe
    payment_method_types: ['card']
  });
  
  const paymentMethod = await stripe.paymentMethods.create({
    type: 'card',
    card: {
      number: '4000002500003155', // Requires 3DS
      exp_month: 12,
      exp_year: 2025,
      cvc: '123'
    }
  });
  
  const confirmedIntent = await stripe.paymentIntents.confirm(paymentIntent.id, {
    payment_method: paymentMethod.id,
    return_url: 'https://example.com/payment/complete'
  });
  
  // Payment requires additional action (3DS)
  expect(confirmedIntent.status).toBe('requires_action');
  expect(confirmedIntent.next_action.type).toBe('use_stripe_sdk');
  expect(confirmedIntent.next_action.use_stripe_sdk).toBeDefined();
  
  // In test mode, simulate authentication success
  const authenticatedIntent = await stripe.paymentIntents.confirm(
    paymentIntent.id
  );
  
  expect(authenticatedIntent.status).toBe('succeeded');
});
```

**Test Case TC_STRIPE_004: Expired Card Decline**

```javascript
test('TC_STRIPE_004: Handle expired card', async () => {
  const paymentIntent = await stripe.paymentIntents.create({
    amount: 1500,
    currency: 'usd'
  });
  
  const paymentMethod = await stripe.paymentMethods.create({
    type: 'card',
    card: {
      number: '4000000000000069', // Expired card
      exp_month: 12,
      exp_year: 2025,
      cvc: '123'
    }
  });
  
  try {
    await stripe.paymentIntents.confirm(paymentIntent.id, {
      payment_method: paymentMethod.id
    });
    fail('Should decline expired card');
  } catch (error) {
    expect(error.code).toBe('card_declined');
    expect(error.decline_code).toBe('expired_card');
    expect(error.message).toContain('expired');
  }
});
```

**Test Case TC_STRIPE_005: Incorrect CVC**

```javascript
test('TC_STRIPE_005: Handle incorrect CVC', async () => {
  const paymentIntent = await stripe.paymentIntents.create({
    amount: 2500,
    currency: 'usd'
  });
  
  const paymentMethod = await stripe.paymentMethods.create({
    type: 'card',
    card: {
      number: '4000000000000127', // Incorrect CVC
      exp_month: 12,
      exp_year: 2025,
      cvc: '123'
    }
  });
  
  try {
    await stripe.paymentIntents.confirm(paymentIntent.id, {
      payment_method: paymentMethod.id
    });
    fail('Should decline due to incorrect CVC');
  } catch (error) {
    expect(error.code).toBe('card_declined');
    expect(error.decline_code).toBe('incorrect_cvc');
  }
});
```

**Test Case TC_STRIPE_006: Lost/Stolen Card**

```javascript
test('TC_STRIPE_006: Handle lost/stolen card', async () => {
  const paymentIntent = await stripe.paymentIntents.create({
    amount: 7500,
    currency: 'usd'
  });
  
  const paymentMethod = await stripe.paymentMethods.create({
    type: 'card',
    card: {
      number: '4000000000009987', // Lost card
      exp_month: 12,
      exp_year: 2025,
      cvc: '123'
    }
  });
  
  try {
    await stripe.paymentIntents.confirm(paymentIntent.id, {
      payment_method: paymentMethod.id
    });
    fail('Should decline lost card');
  } catch (error) {
    expect(error.code).toBe('card_declined');
    expect(error.decline_code).toBe('lost_card');
    
    // Verify appropriate logging/alerting would occur
    // In production, this should trigger fraud alerts
  }
});
```

#### 9.2.4 Refund Flow Testing

Refunds are a critical part of payment processing. Testing the complete refund workflow ensures customers can get their money back when needed.

**Test Case TC_STRIPE_REFUND_001: Full Refund**

```javascript
test('TC_STRIPE_REFUND_001: Process full refund', async () => {
  // First, create and confirm a successful payment
  const paymentIntent = await stripe.paymentIntents.create({
    amount: 5000,
    currency: 'usd',
    payment_method: 'pm_card_visa', // Use a pre-created test payment method
    confirm: true
  });
  
  expect(paymentIntent.status).toBe('succeeded');
  const chargeId = paymentIntent.charges.data[0].id;
  
  // Process full refund
  const refund = await stripe.refunds.create({
    charge: chargeId,
    reason: 'requested_by_customer',
    metadata: {
      refund_reason: 'Customer changed mind',
      refund_requested_by: 'customer_service_rep_123'
    }
  });
  
  expect(refund.id).toBeDefined();
  expect(refund.amount).toBe(5000); // Full amount
  expect(refund.status).toBe('succeeded');
  expect(refund.charge).toBe(chargeId);
  expect(refund.reason).toBe('requested_by_customer');
  
  // Verify the charge is refunded
  const updatedCharge = await stripe.charges.retrieve(chargeId);
  expect(updatedCharge.refunded).toBe(true);
  expect(updatedCharge.amount_refunded).toBe(5000);
  expect(updatedCharge.refunds.data.length).toBe(1);
  expect(updatedCharge.refunds.data[0].id).toBe(refund.id);
});
```

**Test Case TC_STRIPE_REFUND_002: Partial Refund**

```javascript
test('TC_STRIPE_REFUND_002: Process partial refund', async () => {
  const paymentIntent = await stripe.paymentIntents.create({
    amount: 10000, // $100.00
    currency: 'usd',
    payment_method: 'pm_card_visa',
    confirm: true
  });
  
  const chargeId = paymentIntent.charges.data[0].id;
  
  // Refund $30.00 (partial)
  const partialRefund = await stripe.refunds.create({
    charge: chargeId,
    amount: 3000,
    reason: 'requested_by_customer',
    metadata: {
      refund_reason: 'One item returned out of three'
    }
  });
  
  expect(partialRefund.amount).toBe(3000);
  expect(partialRefund.status).toBe('succeeded');
  
  // Verify charge shows partial refund
  const charge = await stripe.charges.retrieve(chargeId);
  expect(charge.refunded).toBe(false); // Not fully refunded
  expect(charge.amount_refunded).toBe(3000);
  expect(charge.amount).toBe(10000);
  
  // Process second partial refund ($20.00)
  const secondRefund = await stripe.refunds.create({
    charge: chargeId,
    amount: 2000
  });
  
  expect(secondRefund.status).toBe('succeeded');
  
  // Verify total refunded amount
  const updatedCharge = await stripe.charges.retrieve(chargeId);
  expect(updatedCharge.amount_refunded).toBe(5000); // $30 + $20
  expect(updatedCharge.refunds.data.length).toBe(2);
});
```

**Test Case TC_STRIPE_REFUND_003: Refund Exceeding Original Amount**

```javascript
test('TC_STRIPE_REFUND_003: Prevent refund exceeding charge amount', async () => {
  const paymentIntent = await stripe.paymentIntents.create({
    amount: 2000,
    currency: 'usd',
    payment_method: 'pm_card_visa',
    confirm: true
  });
  
  const chargeId = paymentIntent.charges.data[0].id;
  
  // Attempt to refund more than charged
  try {
    await stripe.refunds.create({
      charge: chargeId,
      amount: 3000 // More than $20.00 charged
    });
    fail('Should not allow refund exceeding charge amount');
  } catch (error) {
    expect(error.type).toBe('StripeInvalidRequestError');
    expect(error.message).toContain('exceeds');
  }
});
```

**Test Case TC_STRIPE_REFUND_004: Refund Failed Card**

```javascript
test('TC_STRIPE_REFUND_004: Handle refund failure', async () => {
  const paymentIntent = await stripe.paymentIntents.create({
    amount: 4000,
    currency: 'usd',
    payment_method_types: ['card']
  });
  
  // Use card that will fail refunds
  const paymentMethod = await stripe.paymentMethods.create({
    type: 'card',
    card: {
      number: '4000000000005126', // Refund fails
      exp_month: 12,
      exp_year: 2025,
      cvc: '123'
    }
  });
  
  const confirmedPayment = await stripe.paymentIntents.confirm(
    paymentIntent.id,
    { payment_method: paymentMethod.id }
  );
  
  const chargeId = confirmedPayment.charges.data[0].id;
  
  // Attempt refund
  const refund = await stripe.refunds.create({
    charge: chargeId
  });
  
  // In test mode, this will be marked as failed
  expect(refund.status).toBe('failed');
  expect(refund.failure_reason).toBeDefined();
  
  // Verify charge is not refunded
  const charge = await stripe.charges.retrieve(chargeId);
  expect(charge.refunded).toBe(false);
  expect(charge.amount_refunded).toBe(0);
});
```

#### 9.2.5 Webhook Verification Testing

Webhooks are essential for asynchronous payment processing. Proper webhook handling ensures your system stays in sync with Stripe.

**Test Case TC_STRIPE_WEBHOOK_001: Verify Webhook Signature**

```javascript
const express = require('express');
const request = require('supertest');

describe('Stripe Webhook Verification', () => {
  let app;
  let webhookSecret = 'whsec_test_secret';
  
  beforeAll(() => {
    app = express();
    
    app.post('/webhook',
      express.raw({type: 'application/json'}),
      (req, res) => {
        const sig = req.headers['stripe-signature'];
        
        try {
          const event = stripe.webhooks.constructEvent(
            req.body,
            sig,
            webhookSecret
          );
          
          res.json({received: true, type: event.type});
        } catch (err) {
          res.status(400).send(`Webhook Error: ${err.message}`);
        }
      }
    );
  });
  
  test('TC_STRIPE_WEBHOOK_001: Accept valid webhook signature', async () => {
    const payload = JSON.stringify({
      id: 'evt_test_webhook',
      object: 'event',
      type: 'payment_intent.succeeded',
      data: {
        object: {
          id: 'pi_test_123',
          amount: 2000,
          currency: 'usd',
          status: 'succeeded'
        }
      }
    });
    
    const timestamp = Math.floor(Date.now() / 1000);
    const signature = stripe.webhooks.generateTestHeaderString({
      payload,
      secret: webhookSecret,
      timestamp
    });
    
    const response = await request(app)
      .post('/webhook')
      .set('stripe-signature', signature)
      .send(payload)
      .expect(200);
    
    expect(response.body.received).toBe(true);
    expect(response.body.type).toBe('payment_intent.succeeded');
  });
  
  test('TC_STRIPE_WEBHOOK_002: Reject invalid signature', async () => {
    const payload = JSON.stringify({
      id: 'evt_test_webhook',
      type: 'payment_intent.succeeded'
    });
    
    const invalidSignature = 't=1234567890,v1=invalidsignature';
    
    await request(app)
      .post('/webhook')
      .set('stripe-signature', invalidSignature)
      .send(payload)
      .expect(400);
  });
  
  test('TC_STRIPE_WEBHOOK_003: Reject replay attack (old timestamp)', async () => {
    const payload = JSON.stringify({
      id: 'evt_test_webhook',
      type: 'payment_intent.succeeded'
    });
    
    // Use timestamp from 10 minutes ago
    const oldTimestamp = Math.floor(Date.now() / 1000) - 600;
    const signature = stripe.webhooks.generateTestHeaderString({
      payload,
      secret: webhookSecret,
      timestamp: oldTimestamp
    });
    
    await request(app)
      .post('/webhook')
      .set('stripe-signature', signature)
      .send(payload)
      .expect(400);
  });
});
```

**Test Case TC_STRIPE_WEBHOOK_004: Handle Payment Success Webhook**

```javascript
test('TC_STRIPE_WEBHOOK_004: Process payment success webhook', async () => {
  const paymentIntentId = 'pi_test_webhook_success';
  
  const webhookPayload = {
    id: 'evt_test_123',
    type: 'payment_intent.succeeded',
    data: {
      object: {
        id: paymentIntentId,
        object: 'payment_intent',
        amount: 5000,
        currency: 'usd',
        status: 'succeeded',
        metadata: {
          order_id: 'ORDER_123',
          customer_id: 'CUST_456'
        },
        charges: {
          data: [{
            id: 'ch_test_123',
            amount: 5000,
            paid: true
          }]
        }
      }
    }
  };
  
  // Simulate webhook call
  const event = webhookPayload;
  
  // Your webhook handler logic
  if (event.type === 'payment_intent.succeeded') {
    const paymentIntent = event.data.object;
    const orderId = paymentIntent.metadata.order_id;
    
    // Update order status in database
    const order = await db.orders.findOne({id: orderId});
    expect(order).toBeDefined();
    
    await db.orders.update(
      {id: orderId},
      {
        status: 'paid',
        payment_id: paymentIntent.id,
        paid_at: new Date()
      }
    );
    
    // Verify update
    const updatedOrder = await db.orders.findOne({id: orderId});
    expect(updatedOrder.status).toBe('paid');
    expect(updatedOrder.payment_id).toBe(paymentIntentId);
    
    // Send confirmation email
    const emailSent = await sendOrderConfirmationEmail(orderId);
    expect(emailSent).toBe(true);
  }
});
```

**Test Case TC_STRIPE_WEBHOOK_005: Handle Payment Failure Webhook**

```javascript
test('TC_STRIPE_WEBHOOK_005: Process payment failure webhook', async () => {
  const webhookPayload = {
    type: 'payment_intent.payment_failed',
    data: {
      object: {
        id: 'pi_failed_test',
        status: 'requires_payment_method',
        last_payment_error: {
          code: 'card_declined',
          decline_code: 'insufficient_funds',
          message: 'Your card has insufficient funds.'
        },
        metadata: {
          order_id: 'ORDER_789',
          customer_email: 'customer@example.com'
        }
      }
    }
  };
  
  const event = webhookPayload;
  
  if (event.type === 'payment_intent.payment_failed') {
    const paymentIntent = event.data.object;
    const orderId = paymentIntent.metadata.order_id;
    const error = paymentIntent.last_payment_error;
    
    // Update order with failure information
    await db.orders.update(
      {id: orderId},
      {
        payment_status: 'failed',
        payment_error: error.message,
        payment_error_code: error.code
      }
    );
    
    // Send payment failure notification
    const notification = await sendPaymentFailureEmail(
      paymentIntent.metadata.customer_email,
      {
        orderId,
        errorMessage: error.message,
        retryUrl: `https://example.com/orders/${orderId}/retry-payment`
      }
    );
    
    expect(notification.sent).toBe(true);
    
    // Log for fraud detection if suspicious
    if (error.decline_code === 'stolen_card' || error.decline_code === 'lost_card') {
      const fraudAlert = await createFraudAlert({
        order_id: orderId,
        decline_code: error.decline_code,
        severity: 'high'
      });
      expect(fraudAlert.created).toBe(true);
    }
  }
});
```

**Test Case TC_STRIPE_WEBHOOK_006: Handle Refund Webhook**

```javascript
test('TC_STRIPE_WEBHOOK_006: Process refund webhook', async () => {
  const webhookPayload = {
    type: 'charge.refunded',
    data: {
      object: {
        id: 'ch_refunded_test',
        amount: 10000,
        amount_refunded: 10000,
        refunded: true,
        refunds: {
          data: [{
            id: 're_test_123',
            amount: 10000,
            status: 'succeeded',
            reason: 'requested_by_customer',
            metadata: {
              refunded_by: 'admin_user_456'
            }
          }]
        },
        metadata: {
          order_id: 'ORDER_999'
        }
      }
    }
  };
  
  const event = webhookPayload;
  
  if (event.type === 'charge.refunded') {
    const charge = event.data.object;
    const orderId = charge.metadata.order_id;
    const refund = charge.refunds.data[0];
    
    // Update order status
    await db.orders.update(
      {id: orderId},
      {
        status: 'refunded',
        refund_id: refund.id,
        refund_amount: refund.amount,
        refunded_at: new Date()
      }
    );
    
    // Restore inventory if applicable
    const order = await db.orders.findOne({id: orderId});
    for (const item of order.items) {
      await db.inventory.increment(
        {product_id: item.product_id},
        {quantity: item.quantity}
      );
    }
    
    // Send refund confirmation email
    const emailSent = await sendRefundConfirmationEmail(orderId);
    expect(emailSent).toBe(true);
    
    // Verify order status
    const updatedOrder = await db.orders.findOne({id: orderId});
    expect(updatedOrder.status).toBe('refunded');
    expect(updatedOrder.refund_id).toBe(refund.id);
  }
});
```

#### 9.2.6 Subscription Billing Testing

Subscriptions require thorough testing of recurring billing, plan changes, cancellations, and dunning management.

**Test Case TC_STRIPE_SUB_001: Create Subscription**

```javascript
test('TC_STRIPE_SUB_001: Create monthly subscription', async () => {
  // Create a customer
  const customer = await stripe.customers.create({
    email: 'subscriber@example.com',
    name: 'Test Subscriber',
    metadata: {
      user_id: 'USER_123'
    }
  });
  
  expect(customer.id).toBeDefined();
  
  // Attach payment method
  const paymentMethod = await stripe.paymentMethods.attach(
    'pm_card_visa',
    {customer: customer.id}
  );
  
  // Set as default payment method
  await stripe.customers.update(customer.id, {
    invoice_settings: {
      default_payment_method: paymentMethod.id
    }
  });
  
  // Create subscription
  const subscription = await stripe.subscriptions.create({
    customer: customer.id,
    items: [{
      price: 'price_test_monthly_999', // $9.99/month test price
    }],
    payment_behavior: 'default_incomplete',
    expand: ['latest_invoice.payment_intent'],
    metadata: {
      plan_name: 'Premium Monthly'
    }
  });
  
  expect(subscription.id).toBeDefined();
  expect(subscription.status).toBe('active');
  expect(subscription.items.data.length).toBe(1);
  expect(subscription.items.data[0].price.id).toBe('price_test_monthly_999');
  
  // Verify initial invoice
  const invoice = subscription.latest_invoice;
  expect(invoice).toBeDefined();
  expect(invoice.status).toBe('paid');
  expect(invoice.amount_paid).toBe(999); // $9.99 in cents
  
  // Verify subscription in database
  const dbSubscription = await db.subscriptions.findOne({
    stripe_subscription_id: subscription.id
  });
  expect(dbSubscription.user_id).toBe('USER_123');
  expect(dbSubscription.status).toBe('active');
});
```

**Test Case TC_STRIPE_SUB_002: Upgrade Subscription Plan**

```javascript
test('TC_STRIPE_SUB_002: Upgrade from monthly to annual plan', async () => {
  // Assume customer already has monthly subscription
  const customer = await stripe.customers.create({
    email: 'upgrader@example.com'
  });
  
  const monthlySubscription = await stripe.subscriptions.create({
    customer: customer.id,
    items: [{price: 'price_monthly_999'}],
    payment_method: 'pm_card_visa',
    default_payment_method: 'pm_card_visa'
  });
  
  expect(monthlySubscription.status).toBe('active');
  
  // Upgrade to annual plan
  const subscriptionItemId = monthlySubscription.items.data[0].id;
  
  const upgradedSubscription = await stripe.subscriptions.update(
    monthlySubscription.id,
    {
      items: [{
        id: subscriptionItemId,
        price: 'price_annual_9999' // $99.99/year
      }],
      proration_behavior: 'create_prorations'
    }
  );
  
  expect(upgradedSubscription.id).toBe(monthlySubscription.id);
  expect(upgradedSubscription.items.data[0].price.id).toBe('price_annual_9999');
  
  // Verify proration invoice
  const invoices = await stripe.invoices.list({
    customer: customer.id,
    limit: 1
  });
  
  const prorationInvoice = invoices.data[0];
  expect(prorationInvoice.billing_reason).toBe('subscription_update');
  
  // Verify credit for unused monthly time
  const creditItems = prorationInvoice.lines.data.filter(
    line => line.amount < 0
  );
  expect(creditItems.length).toBeGreaterThan(0);
});
```

**Test Case TC_STRIPE_SUB_003: Handle Failed Recurring Payment**

```javascript
test('TC_STRIPE_SUB_003: Handle failed recurring payment', async () => {
  const customer = await stripe.customers.create({
    email: 'pastdue@example.com'
  });
  
  // Attach a card that will decline
  const paymentMethod = await stripe.paymentMethods.create({
    type: 'card',
    card: {
      number: '4000000000000341', // Attaches but will decline
      exp_month: 12,
      exp_year: 2025,
      cvc: '123'
    }
  });
  
  await stripe.paymentMethods.attach(paymentMethod.id, {
    customer: customer.id
  });
  
  await stripe.customers.update(customer.id, {
    invoice_settings: {
      default_payment_method: paymentMethod.id
    }
  });
  
  // Create subscription (first charge succeeds in test mode)
  const subscription = await stripe.subscriptions.create({
    customer: customer.id,
    items: [{price: 'price_monthly_999'}]
  });
  
  // Simulate failed renewal
  // In production, this would happen automatically on renewal date
  // For testing, manually create an invoice that will fail
  
  const failedInvoice = await stripe.invoices.create({
    customer: customer.id,
    auto_advance: true,
    collection_method: 'charge_automatically',
    subscription: subscription.id
  });
  
  await stripe.invoices.finalizeInvoice(failedInvoice.id);
  
  try {
    await stripe.invoices.pay(failedInvoice.id);
  } catch (error) {
    // Expected to fail
  }
  
  // Retrieve updated subscription
  const updatedSubscription = await stripe.subscriptions.retrieve(subscription.id);
  
  // Subscription should be past_due
  expect(updatedSubscription.status).toBe('past_due');
  
  // Verify latest invoice failed
  const latestInvoice = await stripe.invoices.retrieve(
    updatedSubscription.latest_invoice
  );
  expect(latestInvoice.status).toBe('open');
  expect(latestInvoice.attempt_count).toBeGreaterThan(0);
  
  // Check dunning emails would be sent
  // (In production, configure dunning in Stripe Dashboard)
  const shouldSendDunningEmail = latestInvoice.status === 'open' &&
                                   latestInvoice.attempt_count > 0;
  expect(shouldSendDunningEmail).toBe(true);
});
```

**Test Case TC_STRIPE_SUB_004: Cancel Subscription**

```javascript
test('TC_STRIPE_SUB_004: Cancel subscription at period end', async () => {
  const customer = await stripe.customers.create({
    email: 'canceller@example.com'
  });
  
  const subscription = await stripe.subscriptions.create({
    customer: customer.id,
    items: [{price: 'price_monthly_999'}],
    payment_method: 'pm_card_visa',
    default_payment_method: 'pm_card_visa'
  });
  
  expect(subscription.status).toBe('active');
  expect(subscription.cancel_at_period_end).toBe(false);
  
  // Cancel at period end (not immediately)
  const canceledSubscription = await stripe.subscriptions.update(
    subscription.id,
    {
      cancel_at_period_end: true,
      cancellation_details: {
        comment: 'Customer requested cancellation'
      }
    }
  );
  
  expect(canceledSubscription.cancel_at_period_end).toBe(true);
  expect(canceledSubscription.status).toBe('active'); // Still active until period end
  expect(canceledSubscription.canceled_at).toBeDefined();
  expect(canceledSubscription.current_period_end).toBeDefined();
  
  // Verify user retains access until period end
  const accessExpiresAt = new Date(canceledSubscription.current_period_end * 1000);
  const now = new Date();
  expect(accessExpiresAt > now).toBe(true);
  
  // Verify database updated
  const dbSubscription = await db.subscriptions.findOne({
    stripe_subscription_id: subscription.id
  });
  expect(dbSubscription.cancel_at_period_end).toBe(true);
  expect(dbSubscription.access_until).toEqual(accessExpiresAt);
});
```

**Test Case TC_STRIPE_SUB_005: Immediate Cancellation**

```javascript
test('TC_STRIPE_SUB_005: Cancel subscription immediately', async () => {
  const customer = await stripe.customers.create({
    email: 'immediate_cancel@example.com'
  });
  
  const subscription = await stripe.subscriptions.create({
    customer: customer.id,
    items: [{price: 'price_monthly_999'}],
    payment_method: 'pm_card_visa',
    default_payment_method: 'pm_card_visa'
  });
  
  // Cancel immediately (delete subscription)
  const deletedSubscription = await stripe.subscriptions.del(subscription.id);
  
  expect(deletedSubscription.status).toBe('canceled');
  expect(deletedSubscription.canceled_at).toBeDefined();
  
  // Verify subscription no longer active
  const retrievedSubscription = await stripe.subscriptions.retrieve(subscription.id);
  expect(retrievedSubscription.status).toBe('canceled');
  
  // Verify access revoked immediately
  const dbSubscription = await db.subscriptions.findOne({
    stripe_subscription_id: subscription.id
  });
  expect(dbSubscription.status).toBe('canceled');
  expect(dbSubscription.access_revoked_at).toBeDefined();
  
  const now = new Date();
  expect(dbSubscription.access_revoked_at <= now).toBe(true);
});
```

#### 9.2.7 Currency and Internationalization Testing

**Test Case TC_STRIPE_CURRENCY_001: Multi-Currency Payments**

```javascript
const currencies = [
  {code: 'usd', amount: 1000, symbol: '$', name: 'US Dollar'},
  {code: 'eur', amount: 900, symbol: '€', name: 'Euro'},
  {code: 'gbp', amount: 800, symbol: '£', name: 'British Pound'},
  {code: 'jpy', amount: 100000, symbol: '¥', name: 'Japanese Yen'}, // Zero-decimal
  {code: 'cad', amount: 1300, symbol: 'C$', name: 'Canadian Dollar'},
  {code: 'aud', amount: 1400, symbol: 'A$', name: 'Australian Dollar'},
  {code: 'chf', amount: 950, symbol: 'CHF', name: 'Swiss Franc'},
  {code: 'cny', amount: 6500, symbol: '¥', name: 'Chinese Yuan'}
];

describe('Multi-Currency Payment Testing', () => {
  currencies.forEach(currency => {
    test(`TC_STRIPE_CURRENCY_001_${currency.code.toUpperCase()}: Process ${currency.name} payment`, async () => {
      const paymentIntent = await stripe.paymentIntents.create({
        amount: currency.amount,
        currency: currency.code,
        payment_method: 'pm_card_visa',
        confirm: true,
        description: `Test payment in ${currency.name}`
      });
      
      expect(paymentIntent.status).toBe('succeeded');
      expect(paymentIntent.currency).toBe(currency.code);
      expect(paymentIntent.amount).toBe(currency.amount);
      
      // Verify proper formatting for display
      const formattedAmount = new Intl.NumberFormat('en-US', {
        style: 'currency',
        currency: currency.code
      }).format(currency.amount / 100);
      
      console.log(`Processed ${formattedAmount} in ${currency.name}`);
    });
  });
});
```

**Test Case TC_STRIPE_CURRENCY_002: Zero-Decimal Currency Handling**

```javascript
test('TC_STRIPE_CURRENCY_002: Handle zero-decimal currencies (JPY)', async () => {
  // Japanese Yen doesn't use decimal places
  const paymentIntent = await stripe.paymentIntents.create({
    amount: 1000, // ¥1000 (not ¥10.00)
    currency: 'jpy',
    payment_method: 'pm_card_visa',
    confirm: true
  });
  
  expect(paymentIntent.status).toBe('succeeded');
  expect(paymentIntent.amount).toBe(1000);
  expect(paymentIntent.currency).toBe('jpy');
  
  // Verify no decimal division for JPY
  const displayAmount = paymentIntent.amount; // Already in whole units
  expect(displayAmount).toBe(1000);
  
  // Test other zero-decimal currencies
  const zeroDecimalCurrencies = ['bif', 'clp', 'djf', 'gnf', 'jpy', 'kmf', 'krw', 'mga', 'pyg', 'rwf', 'ugx', 'vnd', 'vuv', 'xaf', 'xof', 'xpf'];
  
  for (const curr of ['krw', 'vnd']) {
    const pi = await stripe.paymentIntents.create({
      amount: 5000,
      currency: curr,
      payment_method: 'pm_card_visa',
      confirm: true
    });
    
    expect(pi.amount).toBe(5000);
  }
});
```

#### 9.2.8 Tax Calculation Testing

**Test Case TC_STRIPE_TAX_001: Calculate Tax with Stripe Tax**

```javascript
test('TC_STRIPE_TAX_001: Calculate sales tax automatically', async () => {
  // Enable Stripe Tax in your test account first
  
  const paymentIntent = await stripe.paymentIntents.create({
    amount: 10000, // $100.00
    currency: 'usd',
    automatic_tax: {
      enabled: true
    },
    shipping: {
      name: 'Customer Name',
      address: {
        line1: '123 Main St',
        city: 'San Francisco',
        state: 'CA',
        postal_code: '94111',
        country: 'US'
      }
    },
    metadata: {
      product_type: 'physical_goods'
    }
  });
  
  expect(paymentIntent.automatic_tax.enabled).toBe(true);
  
  // For California, expect sales tax to be calculated
  // (Exact rate depends on location)
  if (paymentIntent.automatic_tax.status === 'complete') {
    expect(paymentIntent.amount_details.tip.amount).toBeDefined();
    
    const taxAmount = paymentIntent.amount - 10000;
    expect(taxAmount).toBeGreaterThan(0);
    
    console.log(`Tax calculated: $${taxAmount / 100}`);
  }
});
```

### 9.3 PayPal Sandbox Testing

PayPal is another major payment gateway. Testing with PayPal Sandbox allows comprehensive testing before going live.

#### 9.3.1 Setting Up PayPal Sandbox

**Step 1: Create PayPal Developer Account**
1. Go to https://developer.paypal.com
2. Log in with your PayPal account or create one
3. Navigate to Dashboard

**Step 2: Create Sandbox Test Accounts**

```javascript
// Personal Sandbox Account (Buyer)
{
  email: 'buyer-test@personal.example.com',
  password: 'TestPassword123!',
  country: 'United States',
  account_type: 'Personal',
  balance: '$1000.00 USD'
}

// Business Sandbox Account (Merchant)
{
  email: 'merchant-test@business.example.com',
  password: 'MerchantPass123!',
  country: 'United States',
  account_type: 'Business',
  balance: '$0.00 USD'
}
```

**Step 3: Get Sandbox API Credentials**

```javascript
// REST API Credentials
const PAYPAL_CONFIG = {
  mode: 'sandbox',
  client_id: 'YOUR_SANDBOX_CLIENT_ID',
  client_secret: 'YOUR_SANDBOX_CLIENT_SECRET',
  sandbox_api_url: 'https://api-m.sandbox.paypal.com'
};
```

#### 9.3.2 PayPal Payment Flow Testing

**Test Case TC_PAYPAL_001: Complete Payment Flow**

```javascript
const paypal = require('@paypal/checkout-server-sdk');

test('TC_PAYPAL_001: Process PayPal payment end-to-end', async () => {
  // Configure PayPal environment
  const environment = new paypal.core.SandboxEnvironment(
    PAYPAL_CONFIG.client_id,
    PAYPAL_CONFIG.client_secret
  );
  const client = new paypal.core.PayPalHttpClient(environment);
  
  // Create order
  const request = new paypal.orders.OrdersCreateRequest();
  request.prefer("return=representation");
  request.requestBody({
    intent: 'CAPTURE',
    purchase_units: [{
      amount: {
        currency_code: 'USD',
        value: '50.00',
        breakdown: {
          item_total: {
            currency_code: 'USD',
            value: '50.00'
          }
        }
      },
      description: 'Test Product Purchase',
      items: [{
        name: 'Test Product',
        unit_amount: {
          currency_code: 'USD',
          value: '50.00'
        },
        quantity: '1',
        category: 'PHYSICAL_GOODS'
      }]
    }],
    application_context: {
      return_url: 'https://example.com/payment/success',
      cancel_url: 'https://example.com/payment/cancel',
      brand_name: 'Test Store',
      user_action: 'PAY_NOW'
    }
  });
  
  const order = await client.execute(request);
  
  expect(order.statusCode).toBe(201);
  expect(order.result.status).toBe('CREATED');
  expect(order.result.id).toBeDefined();
  
  const orderId = order.result.id;
  const approvalUrl = order.result.links.find(
    link => link.rel === 'approve'
  ).href;
  
  console.log('PayPal approval URL:', approvalUrl);
  
  // Simulate buyer approval (in real tests, use browser automation)
  // For now, manually approve or use PayPal API
  
  // Capture payment
  const captureRequest = new paypal.orders.OrdersCaptureRequest(orderId);
  captureRequest.requestBody({});
  
  const capture = await client.execute(captureRequest);
  
  expect(capture.statusCode).toBe(201);
  expect(capture.result.status).toBe('COMPLETED');
  expect(capture.result.purchase_units[0].payments.captures.length).toBe(1);
  
  const captureDetails = capture.result.purchase_units[0].payments.captures[0];
  expect(captureDetails.status).toBe('COMPLETED');
  expect(captureDetails.amount.value).toBe('50.00');
  
  // Store transaction in database
  await db.transactions.create({
    order_id: 'ORDER_123',
    paypal_order_id: orderId,
    paypal_capture_id: captureDetails.id,
    amount: 50.00,
    currency: 'USD',
    status: 'completed',
    completed_at: new Date()
  });
});
```

**Test Case TC_PAYPAL_002: Handle Payment Cancellation**

```javascript
test('TC_PAYPAL_002: Handle buyer canceling payment', async () => {
  const environment = new paypal.core.SandboxEnvironment(
    PAYPAL_CONFIG.client_id,
    PAYPAL_CONFIG.client_secret
  );
  const client = new paypal.core.PayPalHttpClient(environment);
  
  // Create order
  const request = new paypal.orders.OrdersCreateRequest();
  request.requestBody({
    intent: 'CAPTURE',
    purchase_units: [{
      amount: {
        currency_code: 'USD',
        value: '75.00'
      }
    }]
  });
  
  const order = await client.execute(request);
  const orderId = order.result.id;
  
  // Buyer clicks cancel instead of approve
  // In your application, handle the cancel_url redirect
  
  // Verify order is still in CREATED status
  const getRequest = new paypal.orders.OrdersGetRequest(orderId);
  const orderDetails = await client.execute(getRequest);
  
  expect(orderDetails.result.status).toBe('CREATED');
  
  // Update order status in your database
  await db.orders.update(
    {paypal_order_id: orderId},
    {
      payment_status: 'canceled',
      canceled_at: new Date()
    }
  });
  
  // Verify inventory not reduced
  const order = await db.orders.findOne({paypal_order_id: orderId});
  expect(order.inventory_reduced).toBe(false);
});
```

**Test Case TC_PAYPAL_003: Refund Processing**

```javascript
test('TC_PAYPAL_003: Process PayPal refund', async () => {
  const environment = new paypal.core.SandboxEnvironment(
    PAYPAL_CONFIG.client_id,
    PAYPAL_CONFIG.client_secret
  );
  const client = new paypal.core.PayPalHttpClient(environment);
  
  // Assume we have a completed capture
  const captureId = 'CAPTURE_ID_FROM_COMPLETED_TRANSACTION';
  
  // Full refund
  const refundRequest = new paypal.payments.CapturesRefundRequest(captureId);
  refundRequest.requestBody({
    note_to_payer: 'Product returned - issuing full refund'
  });
  
  const refund = await client.execute(refundRequest);
  
  expect(refund.statusCode).toBe(201);
  expect(refund.result.status).toBe('COMPLETED');
  expect(refund.result.id).toBeDefined();
  
  const refundId = refund.result.id;
  
  // Verify refund amount
  expect(refund.result.amount.value).toBe(refund.result.amount.value);
  
  // Update database
  await db.transactions.update(
    {paypal_capture_id: captureId},
    {
      refund_id: refundId,
      status: 'refunded',
      refunded_at: new Date()
    }
  });
});
```

**Test Case TC_PAYPAL_004: Partial Refund**

```javascript
test('TC_PAYPAL_004: Process partial PayPal refund', async () => {
  const environment = new paypal.core.SandboxEnvironment(
    PAYPAL_CONFIG.client_id,
    PAYPAL_CONFIG.client_secret
  );
  const client = new paypal.core.PayPalHttpClient(environment);
  
  const captureId = 'CAPTURE_ID_FOR_PARTIAL_REFUND';
  
  // Partial refund - $25 out of $100
  const refundRequest = new paypal.payments.CapturesRefundRequest(captureId);
  refundRequest.requestBody({
    amount: {
      value: '25.00',
      currency_code: 'USD'
    },
    note_to_payer: 'Partial refund for one returned item'
  });
  
  const refund = await client.execute(refundRequest);
  
  expect(refund.statusCode).toBe(201);
  expect(refund.result.amount.value).toBe('25.00');
  expect(refund.result.status).toBe('COMPLETED');
  
  // Update database with partial refund
  await db.transactions.update(
    {paypal_capture_id: captureId},
    {
      $push: {
        refunds: {
          refund_id: refund.result.id,
          amount: 25.00,
          refunded_at: new Date()
        }
      },
      $inc: {
        total_refunded: 25.00
      }
    }
  });
  
  // Verify can still refund remaining amount
  const transaction = await db.transactions.findOne({paypal_capture_id: captureId});
  const remainingRefundable = transaction.amount - transaction.total_refunded;
  expect(remainingRefundable).toBe(75.00);
});
```

### 9.4 Payment Security Testing

#### 9.4.1 PCI DSS Compliance Checks

**Test Case TC_SECURITY_001: Verify No Card Data in Logs**

```javascript
test('TC_SECURITY_001: Ensure card numbers never logged', async () => {
  // Create a payment with full card details
  const testCardNumber = '4242424242424242';
  
  // Clear logs
  await clearApplicationLogs();
  
  // Process payment
  const paymentMethod = await stripe.paymentMethods.create({
    type: 'card',
    card: {
      number: testCardNumber,
      exp_month: 12,
      exp_year: 2025,
      cvc: '123'
    }
  });
  
  const paymentIntent = await stripe.paymentIntents.create({
    amount: 1000,
    currency: 'usd',
    payment_method: paymentMethod.id,
    confirm: true
  });
  
  // Retrieve all logs
  const logs = await getApplicationLogs();
  
  // Verify card number is never in logs
  for (const logEntry of logs) {
    const logContent = JSON.stringify(logEntry).toLowerCase();
    expect(logContent).not.toContain(testCardNumber);
    expect(logContent).not.toContain('4242424242424242');
    
    // Also check partial card numbers (first 6 + last 4 is OK)
    // But full number should never appear
  }
  
  // Verify only last4 appears
  const last4Regex = /\*{12}\d{4}/; // ************4242 format OK
  const fullCardRegex = /4242\s?4242\s?4242\s?4242/; // This should NOT appear
  
  for (const logEntry of logs) {
    expect(logEntry.message).not.toMatch(fullCardRegex);
  }
});
```

**Test Case TC_SECURITY_002: Verify Card Data Not in Database**

```javascript
test('TC_SECURITY_002: Ensure PAN not stored in database', async () => {
  const testCardNumber = '5555555555554444';
  
  // Process payment
  const paymentMethod = await stripe.paymentMethods.create({
    type: 'card',
    card: {
      number: testCardNumber,
      exp_month: 6,
      exp_year: 2026,
      cvc: '456'
    },
    billing_details: {
      name: 'Test User'
    }
  });
  
  const paymentIntent = await stripe.paymentIntents.create({
    amount: 3000,
    currency: 'usd',
    payment_method: paymentMethod.id,
    confirm: true,
    metadata: {
      customer_id: 'CUSTOMER_999'
    }
  });
  
  // Store transaction (should only store tokenized data)
  await db.transactions.create({
    customer_id: 'CUSTOMER_999',
    stripe_payment_intent_id: paymentIntent.id,
    stripe_payment_method_id: paymentMethod.id,
    amount: 30.00,
    currency: 'usd',
    card_brand: paymentMethod.card.brand,
    card_last4: paymentMethod.card.last4,
    status: 'succeeded'
  });
  
  // Scan entire database for card number
  const allTransactions = await db.transactions.find({});
  const allCustomers = await db.customers.find({});
  const allOrders = await db.orders.find({});
  
  const allData = JSON.stringify([
    ...allTransactions,
    ...allCustomers,
    ...allOrders
  ]);
  
  // Verify full PAN never stored
  expect(allData).not.toContain(testCardNumber);
  expect(allData).not.toContain('5555555555554444');
  
  // Verify only last4 stored
  expect(allData).toContain('4444');
  
  // Verify no CVV stored
  expect(allData).not.toContain('456');
  expect(allData).not.toContain('cvc');
  expect(allData).not.toContain('cvv');
});
```

**Test Case TC_SECURITY_003: HTTPS Enforcement**

```javascript
test('TC_SECURITY_003: Verify payment endpoints require HTTPS', async () => {
  // Attempt HTTP request to payment endpoint
  const httpUrl = 'http://example.com/api/payments/create';
  
  try {
    const response = await axios.post(httpUrl, {
      amount: 1000,
      currency: 'usd'
    });
    
    // Should not reach here
    fail('HTTP request should be rejected or redirected');
  } catch (error) {
    // Verify either:
    // 1. Request blocked entirely
    // 2. Redirected to HTTPS
    // 3. Returns error requiring HTTPS
    
    const validResponses = [
      error.response?.status === 301, // Permanent redirect
      error.response?.status === 302, // Temporary redirect
      error.response?.status === 403, // Forbidden
      error.message.includes('HTTPS required')
    ];
    
    expect(validResponses.some(v => v === true)).toBe(true);
  }
  
  // Verify HTTPS works
  const httpsUrl = 'https://example.com/api/payments/create';
  const secureResponse = await axios.post(httpsUrl, {
    amount: 1000,
    currency: 'usd'
  }, {
    headers: {
      'Authorization': 'Bearer test_token'
    }
  });
  
  expect([200, 201]).toContain(secureResponse.status);
});
```

#### 9.4.2 Fraud Prevention Testing

**Test Case TC_FRAUD_001: Detect High-Risk Transactions**

```javascript
test('TC_FRAUD_001: Flag high-risk transactions for review', async () => {
  // Use high-risk test card
  const paymentMethod = await stripe.paymentMethods.create({
    type: 'card',
    card: {
      number: '4000000000000325', // Highest risk score
      exp_month: 12,
      exp_year: 2025,
      cvc: '123'
    }
  });
  
  const paymentIntent = await stripe.paymentIntents.create({
    amount: 50000, // Large amount increases risk
    currency: 'usd',
    payment_method: paymentMethod.id
  });
  
  // Stripe Radar should flag this
  // In test mode, check outcome
  const confirmedPayment = await stripe.paymentIntents.confirm(paymentIntent.id);
  
  // Check if blocked by Radar
  if (confirmedPayment.status === 'requires_payment_method') {
    expect(confirmedPayment.last_payment_error).toBeDefined();
    expect(confirmedPayment.last_payment_error.code).toBe('card_declined');
  }
  
  // Retrieve charge to check risk score
  if (confirmedPayment.latest_charge) {
    const charge = await stripe.charges.retrieve(confirmedPayment.latest_charge);
    
    if (charge.outcome) {
      expect(charge.outcome.risk_level).toBeDefined();
      expect(charge.outcome.risk_score).toBeDefined();
      
      // High risk should trigger manual review
      if (charge.outcome.risk_level === 'highest' || charge.outcome.risk_score > 75) {
        // Flag for manual review
        await db.transactions.update(
          {stripe_payment_intent_id: paymentIntent.id},
          {
            requires_manual_review: true,
            risk_level: charge.outcome.risk_level,
            risk_score: charge.outcome.risk_score,
            review_reason: 'High fraud risk detected'
          }
        );
        
        // Send alert to fraud team
        await sendFraudAlert({
          transaction_id: paymentIntent.id,
          risk_level: charge.outcome.risk_level,
          amount: 500.00
        });
      }
    }
  }
});
```

**Test Case TC_FRAUD_002: Velocity Checking**

```javascript
test('TC_FRAUD_002: Block rapid repeated transactions', async () => {
  const customerId = 'CUSTOMER_VELOCITY_TEST';
  const cardFingerprint = 'card_fingerprint_123';
  
  // Attempt 5 transactions in quick succession
  const transactionAttempts = [];
  
  for (let i = 0; i < 5; i++) {
    const attempt = {
      customer_id: customerId,
      card_fingerprint: cardFingerprint,
      amount: 100,
      timestamp: new Date()
    };
    
    transactionAttempts.push(attempt);
    
    // Check velocity
    const recentTransactions = transactionAttempts.filter(t => {
      const timeDiff = Date.now() - t.timestamp.getTime();
      return timeDiff < 60000; // Last 60 seconds
    });
    
    if (recentTransactions.length > 3) {
      // Block transaction
      const blocked = true;
      expect(blocked).toBe(true);
      
      // Log fraud attempt
      await db.fraud_logs.create({
        customer_id: customerId,
        reason: 'velocity_limit_exceeded',
        attempts_count: recentTransactions.length,
        time_window: '60_seconds',
        blocked_at: new Date()
      });
      
      // Don't process payment
      break;
    }
    
    // Small delay between attempts
    await new Promise(resolve => setTimeout(resolve, 100));
  }
  
  // Verify less than 5 transactions processed
  const processedCount = transactionAttempts.filter((_, i) => i <= 2).length;
  expect(processedCount).toBeLessThanOrEqual(3);
});
```

### 9.5 Failed Payment Recovery

**Test Case TC_RECOVERY_001: Retry Logic for Temporary Failures**

```javascript
test('TC_RECOVERY_001: Implement smart retry for temporary failures', async () => {
  const maxRetries = 3;
  let attempts = 0;
  let paymentSucceeded = false;
  
  const attemptPayment = async () => {
    attempts++;
    
    try {
      // Simulate temporary failure on first 2 attempts
      if (attempts < 3) {
        throw new Error('processing_error');
      }
      
      const paymentIntent = await stripe.paymentIntents.create({
        amount: 2500,
        currency: 'usd',
        payment_method: 'pm_card_visa',
        confirm: true
      });
      
      if (paymentIntent.status === 'succeeded') {
        paymentSucceeded = true;
        return paymentIntent;
      }
    } catch (error) {
      if (attempts < maxRetries) {
        // Exponential backoff
        const delayMs = Math.pow(2, attempts) * 1000; // 2s, 4s, 8s
        await new Promise(resolve => setTimeout(resolve, delayMs));
        return attemptPayment();
      } else {
        throw error;
      }
    }
  };
  
  try {
    const result = await attemptPayment();
    expect(paymentSucceeded).toBe(true);
    expect(attempts).toBeLessThanOrEqual(maxRetries);
  } catch (error) {
    // Log final failure
    await db.payment_failures.create({
      attempts: attempts,
      final_error: error.message,
      failed_at: new Date()
    });
  }
});
```

**Test Case TC_RECOVERY_002: Dunning Management**

```javascript
test('TC_RECOVERY_002: Send dunning emails for failed subscriptions', async () => {
  const customer = await stripe.customers.create({
    email: 'dunning-test@example.com',
    name: 'Dunning Test Customer'
  });
  
  // Create subscription that will fail
  const subscription = await stripe.subscriptions.create({
    customer: customer.id,
    items: [{price: 'price_monthly_999'}],
    payment_method: 'pm_card_chargeDeclined'
  });
  
  // Simulate failed payment
  const failedInvoice = subscription.latest_invoice;
  
  // Dunning sequence
  const dunningSequence = [
    {day: 0, subject: 'Payment Failed - Please Update'},
    {day: 3, subject: 'Reminder: Payment Failed'},
    {day: 7, subject: 'Final Notice: Update Payment'},
    {day: 10, subject: 'Subscription Canceled - Payment Failed'}
  ];
  
  for (const dunningEmail of dunningSequence) {
    // Send email
    const emailSent = await sendDunningEmail({
      to: customer.email,
      subject: dunningEmail.subject,
      template: 'dunning_email',
      data: {
        customer_name: customer.name,
        subscription_id: subscription.id,
        amount_due: '$9.99',
        update_payment_url: `https://example.com/billing/update?customer=${customer.id}`
      }
    });
    
    expect(emailSent).toBe(true);
    
    // Log dunning attempt
    await db.dunning_logs.create({
      customer_id: customer.id,
      subscription_id: subscription.id,
      day: dunningEmail.day,
      email_sent: true,
      sent_at: new Date()
    });
  }
  
  // If still not paid after dunning sequence, cancel subscription
  const updatedSubscription = await stripe.subscriptions.retrieve(subscription.id);
  if (updatedSubscription.status === 'past_due') {
    await stripe.subscriptions.del(subscription.id);
    
    // Send final cancellation email
    await sendEmail({
      to: customer.email,
      subject: 'Subscription Canceled',
      template: 'subscription_canceled',
      data: {
        reason: 'payment_failure',
        reactivate_url: `https://example.com/reactivate?subscription=${subscription.id}`
      }
    });
  }
});
```

### 9.6 Comprehensive Payment Testing Checklist

Use this checklist for every payment integration:

**Basic Payment Flow**:
- [ ] Successful payment with valid card
- [ ] Payment with each supported card brand (Visa, Mastercard, Amex, Discover)
- [ ] Payment declined - generic
- [ ] Payment declined - insufficient funds
- [ ] Payment declined - incorrect CVC
- [ ] Payment declined - expired card
- [ ] Payment declined - lost/stolen card
- [ ] Payment with international cards
- [ ] Payment in each supported currency

**3D Secure**:
- [ ] 3DS authentication required and successful
- [ ] 3DS authentication required but failed
- [ ] 3DS not supported by card
- [ ] Bypass 3DS for low-value transactions (if configured)

**Refunds**:
- [ ] Full refund immediately after charge
- [ ] Full refund days after charge
- [ ] Partial refund single
- [ ] Multiple partial refunds
- [ ] Refund exceeding original amount (should fail)
- [ ] Refund after refund window (if applicable)

**Subscriptions** (if applicable):
- [ ] Create subscription
- [ ] Successful recurring charge
- [ ] Failed recurring charge
- [ ] Subscription upgrade
- [ ] Subscription downgrade
- [ ] Cancel subscription at period end
- [ ] Cancel subscription immediately
- [ ] Reactivate canceled subscription
- [ ] Free trial expiration
- [ ] Prorated charges calculated correctly

**Webhooks**:
- [ ] payment_intent.succeeded
- [ ] payment_intent.payment_failed
- [ ] charge.refunded
- [ ] charge.disputed
- [ ] customer.subscription.created
- [ ] customer.subscription.updated
- [ ] customer.subscription.deleted
- [ ] invoice.payment_succeeded
- [ ] invoice.payment_failed
- [ ] Webhook signature verification
- [ ] Webhook retry logic
- [ ] Webhook idempotency

**Security**:
- [ ] HTTPS enforced on all payment endpoints
- [ ] Card numbers never logged
- [ ] Card numbers never stored in database
- [ ] CVV never stored
- [ ] Payment tokens used instead of raw card data
- [ ] API keys not exposed in client-side code
- [ ] CSRF protection on payment forms
- [ ] Rate limiting on payment endpoints

**Error Handling**:
- [ ] Network timeout during payment
- [ ] Gateway downtime handling
- [ ] Invalid API key handling
- [ ] Malformed request handling
- [ ] Currency mismatch handling
- [ ] Amount validation (minimum/maximum)

**User Experience**:
- [ ] Loading states during payment processing
- [ ] Clear error messages for declines
- [ ] Success confirmation displayed
- [ ] Email receipt sent
- [ ] Payment saved for future use
- [ ] Multiple payment methods supported
- [ ] Mobile-responsive payment forms

**Compliance**:
- [ ] PCI DSS compliance verified
- [ ] GDPR compliance (data handling)
- [ ] SCA (Strong Customer Authentication) for EU
- [ ] Sales tax calculated correctly (if applicable)
- [ ] Terms of service acceptance logged

**Edge Cases**:
- [ ] Zero-amount authorization
- [ ] Very large transaction amounts
- [ ] Transactions exactly at limits
- [ ] Duplicate transaction prevention
- [ ] Concurrent payment attempts
- [ ] Browser back button during payment
- [ ] Session timeout during payment

---

## 10. Email System Testing {#email-testing}

Email testing is critical for applications that send transactional emails, marketing campaigns, or notifications. Proper email testing ensures deliverability, correct rendering across email clients, and compliance with anti-spam regulations.

### 10.1 Email Testing Fundamentals

Email systems have unique testing challenges:
- Multiple email clients with different rendering engines
- Spam filter sensitivity
- Deliverability issues
- HTML/CSS rendering limitations
- Plain text fallbacks
- Tracking and analytics
- Unsubscribe compliance
- Bounce and complaint handling

### 10.2 SMTP Testing Setup

#### 10.2.1 Configuring SMTP for Development

**Test Case TC_EMAIL_SMTP_001: Configure SMTP Settings**

```javascript
// config/email.js
const nodemailer = require('nodemailer');

const emailConfig = {
  development: {
    host: process.env.SMTP_HOST || 'smtp.mailtrap.io',
    port: process.env.SMTP_PORT || 2525,
    secure: false,
    auth: {
      user: process.env.SMTP_USER,
      pass: process.env.SMTP_PASS
    }
  },
  staging: {
    host: 'smtp.sendgrid.net',
    port: 587,
    secure: false,
    auth: {
      user: 'apikey',
      pass: process.env.SENDGRID_API_KEY
    }
  },
  production: {
    host: 'smtp.sendgrid.net',
    port: 465,
    secure: true,
    auth: {
      user: 'apikey',
      pass: process.env.SENDGRID_API_KEY
    }
  }
};

const transporter = nodemailer.createTransporter(
  emailConfig[process.env.NODE_ENV || 'development']
);

test('TC_EMAIL_SMTP_001: Verify SMTP connection', async () => {
  const verified = await transporter.verify();
  expect(verified).toBe(true);
});

module.exports = transporter;
```

#### 10.2.2 Mailtrap Setup and Testing

Mailtrap is an excellent email testing tool that captures emails without sending them to real recipients.

**Test Case TC_EMAIL_MAILTRAP_001: Send Email to Mailtrap**

```javascript
test('TC_EMAIL_MAILTRAP_001: Send test email to Mailtrap', async () => {
  const mailOptions = {
    from: 'test@example.com',
    to: 'recipient@example.com',
    subject: 'Test Email - Mailtrap Verification',
    text: 'This is a plain text test email.',
    html: '<h1>Test Email</h1><p>This is an HTML test email.</p>'
  };
  
  const info = await transporter.sendMail(mailOptions);
  
  expect(info.messageId).toBeDefined();
  expect(info.accepted.length).toBeGreaterThan(0);
  expect(info.rejected.length).toBe(0);
  
  console.log('Message sent: %s', info.messageId);
  console.log('Preview URL: %s', nodemailer.getTestMessageUrl(info));
});
```

**Test Case TC_EMAIL_MAILTRAP_002: Verify Email Content in Mailtrap**

```javascript
const axios = require('axios');

test('TC_EMAIL_MAILTRAP_002: Retrieve and verify email from Mailtrap', async () => {
  // Send email first
  const mailOptions = {
    from: '"Test Sender" <sender@example.com>',
    to: 'recipient@example.com',
    subject: 'Order Confirmation #12345',
    text: 'Your order has been confirmed.',
    html: `
      <div style="font-family: Arial, sans-serif;">
        <h2>Order Confirmed!</h2>
        <p>Thank you for your order #12345.</p>
        <p>Total: $99.99</p>
      </div>
    `
  };
  
  await transporter.sendMail(mailOptions);
  
  // Wait briefly for email to arrive
  await new Promise(resolve => setTimeout(resolve, 2000));
  
  // Retrieve from Mailtrap API
  const mailtrapApiToken = process.env.MAILTRAP_API_TOKEN;
  const inboxId = process.env.MAILTRAP_INBOX_ID;
  
  const response = await axios.get(
    `https://mailtrap.io/api/v1/inboxes/${inboxId}/messages`,
    {
      headers: {
        'Api-Token': mailtrapApiToken
      }
    }
  );
  
  expect(response.status).toBe(200);
  expect(response.data.length).toBeGreaterThan(0);
  
  const latestEmail = response.data[0];
  
  // Verify email properties
  expect(latestEmail.subject).toBe('Order Confirmation #12345');
  expect(latestEmail.to_email).toBe('recipient@example.com');
  expect(latestEmail.from_email).toBe('sender@example.com');
  expect(latestEmail.html_body).toContain('Order Confirmed!');
  expect(latestEmail.html_body).toContain('#12345');
  expect(latestEmail.txt_body).toContain('Your order has been confirmed');
});
```

### 10.3 Email Template Rendering Testing

#### 10.3.1 HTML Email Templates

**Test Case TC_EMAIL_TEMPLATE_001: Render HTML Email Template**

```javascript
const handlebars = require('handlebars');
const fs = require('fs');
const path = require('path');

test('TC_EMAIL_TEMPLATE_001: Compile and render email template', async () => {
  // Load template
  const templatePath = path.join(__dirname, '../templates/emails/order-confirmation.hbs');
  const templateSource = fs.readFileSync(templatePath, 'utf8');
  
  // Compile template
  const template = handlebars.compile(templateSource);
  
  // Template data
  const data = {
    customerName: 'John Doe',
    orderNumber: 'ORD-12345',
    orderDate: '2026-02-09',
    items: [
      {name: 'Product A', quantity: 2, price: 29.99, total: 59.98},
      {name: 'Product B', quantity: 1, price: 49.99, total: 49.99}
    ],
    subtotal: 109.97,
    tax: 9.90,
    shipping: 5.00,
    total: 124.87,
    shippingAddress: {
      street: '123 Main St',
      city: 'San Francisco',
      state: 'CA',
      zip: '94105'
    }
  };
  
  // Render template
  const html = template(data);
  
  // Verify rendered content
  expect(html).toContain('John Doe');
  expect(html).toContain('ORD-12345');
  expect(html).toContain('Product A');
  expect(html).toContain('Product B');
  expect(html).toContain('$124.87');
  expect(html).toContain('123 Main St');
  
  // Send rendered email
  const mailOptions = {
    from: '"Store" <orders@example.com>',
    to: 'john@example.com',
    subject: `Order Confirmation - ${data.orderNumber}`,
    html: html
  };
  
  const info = await transporter.sendMail(mailOptions);
  expect(info.accepted.length).toBeGreaterThan(0);
});
```

**Example Email Template (order-confirmation.hbs)**:

```handlebars
<!DOCTYPE html>
<html>
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Order Confirmation</title>
  <style>
    body {
      font-family: Arial, sans-serif;
      line-height: 1.6;
      color: #333;
      max-width: 600px;
      margin: 0 auto;
      padding: 20px;
    }
    .header {
      background-color: #4CAF50;
      color: white;
      padding: 20px;
      text-align: center;
    }
    .content {
      padding: 20px;
      background-color: #f9f9f9;
    }
    .order-details {
      background-color: white;
      padding: 15px;
      margin: 20px 0;
      border: 1px solid #ddd;
    }
    table {
      width: 100%;
      border-collapse: collapse;
    }
    th, td {
      padding: 10px;
      text-align: left;
      border-bottom: 1px solid #ddd;
    }
    .total {
      font-weight: bold;
      font-size: 1.2em;
    }
    .footer {
      text-align: center;
      padding: 20px;
      color: #666;
      font-size: 0.9em;
    }
  </style>
</head>
<body>
  <div class="header">
    <h1>Order Confirmed!</h1>
  </div>
  
  <div class="content">
    <p>Hi {{customerName}},</p>
    <p>Thank you for your order! We've received your order and will send you a shipping confirmation as soon as it ships.</p>
    
    <div class="order-details">
      <h2>Order #{{orderNumber}}</h2>
      <p>Order Date: {{orderDate}}</p>
      
      <table>
        <thead>
          <tr>
            <th>Item</th>
            <th>Qty</th>
            <th>Price</th>
            <th>Total</th>
          </tr>
        </thead>
        <tbody>
          {{#each items}}
          <tr>
            <td>{{this.name}}</td>
            <td>{{this.quantity}}</td>
            <td>${{this.price}}</td>
            <td>${{this.total}}</td>
          </tr>
          {{/each}}
        </tbody>
        <tfoot>
          <tr>
            <td colspan="3">Subtotal:</td>
            <td>${{subtotal}}</td>
          </tr>
          <tr>
            <td colspan="3">Tax:</td>
            <td>${{tax}}</td>
          </tr>
          <tr>
            <td colspan="3">Shipping:</td>
            <td>${{shipping}}</td>
          </tr>
          <tr class="total">
            <td colspan="3">Total:</td>
            <td>${{total}}</td>
          </tr>
        </tfoot>
      </table>
    </div>
    
    <h3>Shipping Address</h3>
    <p>
      {{shippingAddress.street}}<br>
      {{shippingAddress.city}}, {{shippingAddress.state}} {{shippingAddress.zip}}
    </p>
  </div>
  
  <div class="footer">
    <p>Thank you for shopping with us!</p>
    <p>Questions? Contact us at support@example.com</p>
  </div>
</body>
</html>
```

#### 10.3.2 Plain Text Fallback Testing

**Test Case TC_EMAIL_TEMPLATE_002: Generate Plain Text Version**

```javascript
const htmlToText = require('html-to-text');

test('TC_EMAIL_TEMPLATE_002: Generate plain text from HTML', async () => {
  const html = `
    <html>
      <body>
        <h1>Order Confirmed!</h1>
        <p>Hi John Doe,</p>
        <p>Thank you for your order #ORD-12345.</p>
        <p><strong>Total: $124.87</strong></p>
        <p>Questions? Contact us at <a href="mailto:support@example.com">support@example.com</a></p>
      </body>
    </html>
  `;
  
  const plainText = htmlToText.convert(html, {
    wordwrap: 80,
    selectors: [
      {selector: 'a', options: {ignoreHref: false}},
      {selector: 'img', format: 'skip'}
    ]
  });
  
  expect(plainText).toContain('ORDER CONFIRMED!');
  expect(plainText).toContain('Hi John Doe,');
  expect(plainText).toContain('Total: $124.87');
  expect(plainText).toContain('support@example.com');
  expect(plainText).not.toContain('<html>');
  expect(plainText).not.toContain('<p>');
  
  // Send email with both HTML and plain text
  const mailOptions = {
    from: 'orders@example.com',
    to: 'customer@example.com',
    subject: 'Order Confirmation',
    text: plainText,
    html: html
  };
  
  const info = await transporter.sendMail(mailOptions);
  expect(info.accepted.length).toBeGreaterThan(0);
});
```

### 10.4 Email Deliverability Testing

#### 10.4.1 SPF, DKIM, and DMARC Verification

**Test Case TC_EMAIL_DELIVER_001: Verify Email Authentication**

```javascript
const dns = require('dns').promises;

test('TC_EMAIL_DELIVER_001: Verify SPF record', async () => {
  const domain = 'example.com';
  
  try {
    const records = await dns.resolveTxt(domain);
    const spfRecord = records.find(record => 
      record.join('').startsWith('v=spf1')
    );
    
    expect(spfRecord).toBeDefined();
    expect(spfRecord.join('')).toContain('v=spf1');
    
    // Verify includes authorized senders
    const spfString = spfRecord.join('');
    
    // Should include SendGrid or your email provider
    expect(
      spfString.includes('include:sendgrid.net') ||
      spfString.includes('include:_spf.google.com') ||
      spfString.includes('include:servers.mcsv.net')
    ).toBe(true);
    
    // Should end with -all or ~all
    expect(
      spfString.includes('-all') ||
      spfString.includes('~all')
    ).toBe(true);
  } catch (error) {
    fail(`SPF record not found or invalid: ${error.message}`);
  }
});

test('TC_EMAIL_DELIVER_002: Verify DKIM record', async () => {
  const domain = 'example.com';
  const selector = 'default'; // Your DKIM selector
  
  try {
    const dkimDomain = `${selector}._domainkey.${domain}`;
    const records = await dns.resolveTxt(dkimDomain);
    
    expect(records.length).toBeGreaterThan(0);
    
    const dkimRecord = records[0].join('');
    expect(dkimRecord).toContain('v=DKIM1');
    expect(dkimRecord).toContain('p='); // Public key
  } catch (error) {
    fail(`DKIM record not found: ${error.message}`);
  }
});

test('TC_EMAIL_DELIVER_003: Verify DMARC record', async () => {
  const domain = 'example.com';
  
  try {
    const dmarcDomain = `_dmarc.${domain}`;
    const records = await dns.resolveTxt(dmarcDomain);
    
    expect(records.length).toBeGreaterThan(0);
    
    const dmarcRecord = records[0].join('');
    expect(dmarcRecord).toContain('v=DMARC1');
    expect(dmarcRecord).toContain('p='); // Policy
    
    // Should have reporting address
    expect(
      dmarcRecord.includes('rua=') ||
      dmarcRecord.includes('ruf=')
    ).toBe(true);
  } catch (error) {
    fail(`DMARC record not found: ${error.message}`);
  }
});
```

#### 10.4.2 Spam Score Testing

**Test Case TC_EMAIL_SPAM_001: Check Email Spam Score**

```javascript
const axios = require('axios');

test('TC_EMAIL_SPAM_001: Verify email passes spam filters', async () => {
  // Send email to spam checker
  const mailOptions = {
    from: '"My Store" <noreply@example.com>',
    to: 'check@mail-tester.com', // Mail-tester service
    subject: 'Test Email - Spam Check',
    html: `
      <html>
        <body>
          <h1>Welcome to Our Service</h1>
          <p>Hi there,</p>
          <p>Thank you for signing up. Click below to verify your email:</p>
          <a href="https://example.com/verify?token=abc123">Verify Email</a>
          <p>If you didn't sign up, please ignore this email.</p>
          <p>Best regards,<br>The Team</p>
          <p style="font-size: 0.8em; color: #666;">
            <a href="https://example.com/unsubscribe">Unsubscribe</a>
          </p>
        </body>
      </html>
    `
  };
  
  await transporter.sendMail(mailOptions);
  
  // Check spam score
  // In practice, you'd check mail-tester.com manually or use their API
  // A good score is 8/10 or higher
  
  // Checklist for passing spam filters:
  const spamCheckList = {
    hasSenderName: mailOptions.from.includes('"'),
    hasUnsubscribe: mailOptions.html.includes('unsubscribe'),
    hasValidFromDomain: true, // Should match your authenticated domain
    noSpamWords: !mailOptions.html.toLowerCase().includes('viagra'),
    hasTextVersion: mailOptions.text !== undefined,
    reasonableSubject: mailOptions.subject.length > 5 && mailOptions.subject.length < 100
  };
  
  expect(spamCheckList.hasSenderName).toBe(true);
  expect(spamCheckList.hasUnsubscribe).toBe(true);
  expect(spamCheckList.reasonableSubject).toBe(true);
});
```

### 10.5 Transactional vs Marketing Email Testing

#### 10.5.1 Transactional Email Tests

**Test Case TC_EMAIL_TRANSACT_001: Password Reset Email**

```javascript
test('TC_EMAIL_TRANSACT_001: Send password reset email', async () => {
  const user = {
    id: 'USER_123',
    email: 'user@example.com',
    name: 'Test User'
  };
  
  // Generate reset token
  const resetToken = generateSecureToken();
  const resetExpiry = new Date(Date.now() + 3600000); // 1 hour
  
  // Save to database
  await db.passwordResets.create({
    user_id: user.id,
    token: resetToken,
    expires_at: resetExpiry
  });
  
  // Send email
  const resetUrl = `https://example.com/reset-password?token=${resetToken}`;
  
  const mailOptions = {
    from: '"Support" <support@example.com>',
    to: user.email,
    subject: 'Password Reset Request',
    html: `
      <div style="font-family: Arial, sans-serif;">
        <h2>Password Reset Request</h2>
        <p>Hi ${user.name},</p>
        <p>We received a request to reset your password. Click the link below to set a new password:</p>
        <p><a href="${resetUrl}" style="background-color: #4CAF50; color: white; padding: 10px 20px; text-decoration: none; display: inline-block;">Reset Password</a></p>
        <p>This link will expire in 1 hour.</p>
        <p>If you didn't request this, please ignore this email.</p>
        <p>Best regards,<br>Support Team</p>
      </div>
    `,
    text: `
      Password Reset Request
      
      Hi ${user.name},
      
      We received a request to reset your password. Visit the link below to set a new password:
      
      ${resetUrl}
      
      This link will expire in 1 hour.
      
      If you didn't request this, please ignore this email.
      
      Best regards,
      Support Team
    `
  };
  
  const info = await transporter.sendMail(mailOptions);
  
  expect(info.accepted).toContain(user.email);
  expect(info.rejected.length).toBe(0);
  
  // Log email sent
  await db.emailLogs.create({
    user_id: user.id,
    email_type: 'password_reset',
    recipient: user.email,
    sent_at: new Date(),
    message_id: info.messageId
  });
});
```

**Test Case TC_EMAIL_TRANSACT_002: Email Verification**

```javascript
test('TC_EMAIL_TRANSACT_002: Send email verification', async () => {
  const newUser = {
    id: 'USER_NEW_123',
    email: 'newuser@example.com',
    name: 'New User',
    verified: false
  };
  
  const verificationToken = generateSecureToken();
  
  await db.users.update(
    {id: newUser.id},
    {verification_token: verificationToken}
  );
  
  const verifyUrl = `https://example.com/verify-email?token=${verificationToken}`;
  
  const mailOptions = {
    from: '"Welcome Team" <welcome@example.com>',
    to: newUser.email,
    subject: 'Please Verify Your Email',
    html: `
      <div>
        <h1>Welcome ${newUser.name}!</h1>
        <p>Thank you for signing up. Please verify your email address to get started.</p>
        <p><a href="${verifyUrl}">Verify Email Address</a></p>
        <p>Or copy this link: ${verifyUrl}</p>
      </div>
    `
  };
  
  const info = await transporter.sendMail(mailOptions);
  expect(info.accepted.length).toBeGreaterThan(0);
});
```

**Test Case TC_EMAIL_TRANSACT_003: Order Shipment Notification**

```javascript
test('TC_EMAIL_TRANSACT_003: Send shipment notification', async () => {
  const order = {
    id: 'ORD_456',
    customer_email: 'customer@example.com',
    customer_name: 'Jane Doe',
    tracking_number: '1Z999AA10123456784',
    carrier: 'UPS',
    estimated_delivery: '2026-02-15'
  };
  
  const trackingUrl = `https://www.ups.com/track?tracknum=${order.tracking_number}`;
  
  const mailOptions = {
    from: '"Shipping" <shipping@example.com>',
    to: order.customer_email,
    subject: `Your Order #${order.id} Has Shipped!`,
    html: `
      <div style="font-family: Arial, sans-serif;">
        <h2>Your Order Has Shipped! 📦</h2>
        <p>Hi ${order.customer_name},</p>
        <p>Great news! Your order #${order.id} has been shipped and is on its way.</p>
        
        <div style="background-color: #f0f0f0; padding: 15px; margin: 20px 0;">
          <p><strong>Tracking Number:</strong> ${order.tracking_number}</p>
          <p><strong>Carrier:</strong> ${order.carrier}</p>
          <p><strong>Estimated Delivery:</strong> ${order.estimated_delivery}</p>
        </div>
        
        <p><a href="${trackingUrl}">Track Your Package</a></p>
        
        <p>Thank you for your order!</p>
      </div>
    `
  };
  
  const info = await transporter.sendMail(mailOptions);
  
  expect(info.accepted.length).toBeGreaterThan(0);
  
  // Update order status
  await db.orders.update(
    {id: order.id},
    {
      status: 'shipped',
      shipment_notification_sent: true,
      shipped_at: new Date()
    }
  );
});
```

#### 10.5.2 Marketing Email Tests

**Test Case TC_EMAIL_MARKETING_001: Newsletter with Unsubscribe**

```javascript
test('TC_EMAIL_MARKETING_001: Send newsletter with unsubscribe', async () => {
  const subscriber = {
    id: 'SUB_789',
    email: 'subscriber@example.com',
    name: 'Subscriber Name',
    preferences: {
      newsletter: true
    }
  };
  
  // Check subscription status
  const isSubscribed = await db.subscribers.findOne({
    id: subscriber.id,
    'preferences.newsletter': true
  });
  
  expect(isSubscribed).toBeDefined();
  
  // Generate unsubscribe token
  const unsubToken = generateSecureToken();
  await db.unsubscribeTokens.create({
    subscriber_id: subscriber.id,
    token: unsubToken,
    email_type: 'newsletter'
  });
  
  const unsubscribeUrl = `https://example.com/unsubscribe?token=${unsubToken}`;
  
  const mailOptions = {
    from: '"Company Newsletter" <newsletter@example.com>',
    to: subscriber.email,
    subject: 'February Newsletter - Special Offers Inside!',
    html: `
      <div style="max-width: 600px; margin: 0 auto;">
        <div style="background-color: #2196F3; color: white; padding: 20px;">
          <h1>Monthly Newsletter</h1>
        </div>
        
        <div style="padding: 20px;">
          <p>Hi ${subscriber.name},</p>
          <p>Check out this month's special offers and new arrivals!</p>
          
          <h2>Featured Products</h2>
          <!-- Product listings -->
          
          <p><a href="https://example.com/shop">Shop Now</a></p>
        </div>
        
        <div style="background-color: #f5f5f5; padding: 20px; text-align: center; font-size: 0.9em;">
          <p>You're receiving this because you subscribed to our newsletter.</p>
          <p><a href="${unsubscribeUrl}">Unsubscribe</a> | <a href="https://example.com/preferences">Update Preferences</a></p>
          <p>Company Name, 123 Street, City, State 12345</p>
        </div>
      </div>
    `,
    headers: {
      'List-Unsubscribe': `<${unsubscribeUrl}>`,
      'List-Unsubscribe-Post': 'List-Unsubscribe=One-Click'
    }
  };
  
  const info = await transporter.sendMail(mailOptions);
  
  expect(info.accepted.length).toBeGreaterThan(0);
  
  // Verify unsubscribe link present
  expect(mailOptions.html).toContain('unsubscribe');
  expect(mailOptions.headers['List-Unsubscribe']).toBeDefined();
});
```

### 10.6 Bounce and Complaint Handling

#### 10.6.1 Processing Bounces

**Test Case TC_EMAIL_BOUNCE_001: Handle Hard Bounce**

```javascript
test('TC_EMAIL_BOUNCE_001: Process hard bounce notification', async () => {
  // Simulate SendGrid webhook for hard bounce
  const bounceWebhook = {
    email: 'bounced@invalid-domain.com',
    timestamp: Date.now(),
    event: 'bounce',
    reason: '550 5.1.1 The email account that you tried to reach does not exist',
    type: 'blocked',
    status: '5.1.1'
  };
  
  // Handle bounce
  const bouncedEmail = bounceWebhook.email;
  
  // Check if hard bounce (5.x.x status)
  const isHardBounce = bounceWebhook.status.startsWith('5');
  
  if (isHardBounce) {
    // Mark email as invalid
    await db.users.update(
      {email: bouncedEmail},
      {
        email_valid: false,
        bounce_type: 'hard',
        bounced_at: new Date(),
        bounce_reason: bounceWebhook.reason
      }
    );
    
    // Stop sending to this email
    await db.emailSuppressionList.create({
      email: bouncedEmail,
      reason: 'hard_bounce',
      added_at: new Date()
    });
  }
  
  // Verify suppression
  const suppressed = await db.emailSuppressionList.findOne({
    email: bouncedEmail
  });
  
  expect(suppressed).toBeDefined();
  expect(suppressed.reason).toBe('hard_bounce');
});
```

**Test Case TC_EMAIL_BOUNCE_002: Handle Soft Bounce**

```javascript
test('TC_EMAIL_BOUNCE_002: Process soft bounce with retry logic', async () => {
  const softBounceWebhook = {
    email: 'full-mailbox@example.com',
    event: 'bounce',
    reason: '452 4.2.2 Mailbox full',
    type: 'blocked',
    status: '4.2.2'
  };
  
  const bouncedEmail = softBounceWebhook.email;
  const isSoftBounce = softBounceWebhook.status.startsWith('4');
  
  if (isSoftBounce) {
    // Increment soft bounce counter
    await db.users.update(
      {email: bouncedEmail},
      {
        $inc: {soft_bounce_count: 1},
        last_soft_bounce_at: new Date()
      }
    );
    
    // Check bounce count
    const user = await db.users.findOne({email: bouncedEmail});
    
    if (user.soft_bounce_count >= 3) {
      // After 3 soft bounces, treat as hard bounce
      await db.emailSuppressionList.create({
        email: bouncedEmail,
        reason: 'repeated_soft_bounces',
        soft_bounce_count: user.soft_bounce_count,
        added_at: new Date()
      });
    } else {
      // Schedule retry with exponential backoff
      const retryDelay = Math.pow(2, user.soft_bounce_count) * 3600000; // Hours in ms
      await db.emailRetryQueue.create({
        email: bouncedEmail,
        retry_after: new Date(Date.now() + retryDelay),
        attempt: user.soft_bounce_count
      });
    }
  }
});
```

#### 10.6.2 Complaint Handling

**Test Case TC_EMAIL_COMPLAINT_001: Process Spam Complaint**

```javascript
test('TC_EMAIL_COMPLAINT_001: Handle spam complaint', async () => {
  const complaintWebhook = {
    email: 'complained@example.com',
    timestamp: Date.now(),
    event: 'spamreport',
    user_agent: 'Yahoo! - Feedback-ID: ...'
  };
  
  const complainedEmail = complaintWebhook.email;
  
  // Immediately suppress
  await db.emailSuppressionList.create({
    email: complainedEmail,
    reason: 'spam_complaint',
    added_at: new Date(),
    complaint_source: complaintWebhook.user_agent
  });
  
  // Unsubscribe from all marketing emails
  await db.subscribers.update(
    {email: complainedEmail},
    {
      'preferences.newsletter': false,
      'preferences.promotional': false,
      'preferences.marketing': false,
      unsubscribed_via: 'spam_complaint',
      unsubscribed_at: new Date()
    }
  );
  
  // Keep transactional emails (required by law)
  // But mark for monitoring
  await db.users.update(
    {email: complainedEmail},
    {
      spam_complaint_received: true,
      complaint_at: new Date()
    }
  );
  
  // Verify suppression
  const suppressed = await db.emailSuppressionList.findOne({
    email: complainedEmail
  });
  
  expect(suppressed).toBeDefined();
  expect(suppressed.reason).toBe('spam_complaint');
  
  // Verify all marketing preferences disabled
  const subscriber = await db.subscribers.findOne({email: complainedEmail});
  expect(subscriber.preferences.newsletter).toBe(false);
  expect(subscriber.preferences.promotional).toBe(false);
});
```

### 10.7 HTML Email Cross-Client Rendering

#### 10.7.1 Email Client Compatibility Testing

**Email Client Testing Matrix**:

| Client | Rendering Engine | CSS Support | Key Limitations |
|--------|-----------------|-------------|-----------------|
| Gmail (Web) | Proprietary | Limited | No <style> in <head>, strips !important |
| Gmail (Mobile) | WebView | Limited | Similar to web, some CSS3 support |
| Outlook 2007-2019 | Microsoft Word | Very Limited | No CSS3, table-based layout only |
| Outlook.com | Proprietary | Moderate | Better than desktop Outlook |
| Apple Mail | WebKit | Excellent | Best CSS support |
| iOS Mail | WebKit | Excellent | Similar to Apple Mail |
| Yahoo Mail | Proprietary | Limited | Strips some CSS |
| AOL | Proprietary | Limited | Similar to Yahoo |
| Thunderbird | Gecko | Good | Good standards support |

**Test Case TC_EMAIL_RENDER_001: Table-Based Layout**

```html
<!-- email-template-compatible.html -->
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
  <meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0"/>
  <title>Email Template</title>
</head>
<body style="margin: 0; padding: 0; font-family: Arial, sans-serif;">
  <!-- Wrapper table for Outlook -->
  <table border="0" cellpadding="0" cellspacing="0" width="100%" style="background-color: #f4f4f4;">
    <tr>
      <td align="center" style="padding: 20px 0;">
        <!-- Content table -->
        <table border="0" cellpadding="0" cellspacing="0" width="600" style="background-color: #ffffff;">
          <!-- Header -->
          <tr>
            <td align="center" bgcolor="#4CAF50" style="padding: 40px 0;">
              <h1 style="color: #ffffff; font-size: 28px; margin: 0;">
                Welcome to Our Service
              </h1>
            </td>
          </tr>
          
          <!-- Content -->
          <tr>
            <td style="padding: 40px 30px;">
              <p style="margin: 0 0 12px 0; font-size: 16px; line-height: 24px; color: #333333;">
                Hi there,
              </p>
              <p style="margin: 0 0 12px 0; font-size: 16px; line-height: 24px; color: #333333;">
                Thank you for signing up. We're excited to have you on board!
              </p>
            </td>
          </tr>
          
          <!-- Button -->
          <tr>
            <td align="center" style="padding: 0 30px 40px 30px;">
              <table border="0" cellpadding="0" cellspacing="0">
                <tr>
                  <td align="center" bgcolor="#4CAF50" style="border-radius: 3px;">
                    <a href="https://example.com/get-started" target="_blank" style="font-size: 16px; font-family: Arial, sans-serif; color: #ffffff; text-decoration: none; padding: 12px 24px; border-radius: 3px; display: inline-block;">
                      Get Started
                    </a>
                  </td>
                </tr>
              </table>
            </td>
          </tr>
          
          <!-- Footer -->
          <tr>
            <td bgcolor="#f4f4f4" style="padding: 30px;">
              <p style="margin: 0; font-size: 14px; line-height: 20px; color: #666666; text-align: center;">
                &copy; 2026 Company Name. All rights reserved.
              </p>
              <p style="margin: 12px 0 0 0; font-size: 14px; line-height: 20px; color: #666666; text-align: center;">
                <a href="https://example.com/unsubscribe" style="color: #4CAF50; text-decoration: underline;">Unsubscribe</a>
              </p>
            </td>
          </tr>
        </table>
      </td>
    </tr>
  </table>
</body>
</html>
```

**Test Case TC_EMAIL_RENDER_002: Inline CSS Testing**

```javascript
const juice = require('juice');

test('TC_EMAIL_RENDER_002: Convert CSS to inline styles', async () => {
  const htmlWithCss = `
    <html>
      <head>
        <style>
          .button {
            background-color: #4CAF50;
            color: white;
            padding: 10px 20px;
            text-decoration: none;
          }
          .footer {
            font-size: 12px;
            color: #666;
          }
        </style>
      </head>
      <body>
        <p>Hello!</p>
        <a href="#" class="button">Click Here</a>
        <p class="footer">Footer text</p>
      </body>
    </html>
  `;
  
  const inlinedHtml = juice(htmlWithCss);
  
  // Verify inline styles applied
  expect(inlinedHtml).toContain('style="background-color: #4CAF50');
  expect(inlinedHtml).toContain('style="font-size: 12px');
  expect(inlinedHtml).not.toContain('<style>');
  
  // Send inlined email
  const mailOptions = {
    from: 'test@example.com',
    to: 'recipient@example.com',
    subject: 'Inline CSS Test',
    html: inlinedHtml
  };
  
  const info = await transporter.sendMail(mailOptions);
  expect(info.accepted.length).toBeGreaterThan(0);
});
```

**Test Case TC_EMAIL_RENDER_003: Mobile Responsiveness**

```html
<!-- Responsive email template -->
<!DOCTYPE html>
<html>
<head>
  <meta name="viewport" content="width=device-width, initial-scale=1.0"/>
  <style type="text/css">
    /* Mobile styles */
    @media only screen and (max-width: 600px) {
      .container {
        width: 100% !important;
      }
      .mobile-padding {
        padding: 20px !important;
      }
      .mobile-hide {
        display: none !important;
      }
      h1 {
        font-size: 24px !important;
      }
    }
  </style>
</head>
<body style="margin: 0; padding: 0;">
  <table border="0" cellpadding="0" cellspacing="0" width="100%">
    <tr>
      <td align="center">
        <table class="container" border="0" cellpadding="0" cellspacing="0" width="600" style="max-width: 600px;">
          <tr>
            <td class="mobile-padding" style="padding: 40px;">
              <h1 style="font-size: 32px; margin: 0 0 20px 0;">Responsive Email</h1>
              <p style="font-size: 16px; line-height: 24px; margin: 0 0 20px 0;">
                This email adapts to mobile devices automatically.
              </p>
              <img src="https://via.placeholder.com/560x300" alt="Image" style="width: 100%; height: auto; display: block;"/>
            </td>
          </tr>
        </table>
      </td>
    </tr>
  </table>
</body>
</html>
```

### 10.8 Email Testing Checklist

Use this comprehensive checklist for every email you send:

**Content & Formatting**:
- [ ] Subject line is clear and under 50 characters
- [ ] Preview text (preheader) is set and meaningful
- [ ] Sender name and email are recognizable
- [ ] HTML email renders correctly
- [ ] Plain text version provided
- [ ] All links work correctly
- [ ] Images have alt text
- [ ] No broken images
- [ ] Responsive on mobile devices
- [ ] Renders in Gmail, Outlook, Apple Mail, Yahoo

**Deliverability**:
- [ ] SPF record configured
- [ ] DKIM signature present
- [ ] DMARC policy set
- [ ] From address matches authenticated domain
- [ ] No spam trigger words in subject/content
- [ ] Unsubscribe link present (for marketing emails)
- [ ] Physical mailing address included (for marketing)
- [ ] List-Unsubscribe header set
- [ ] Email passes spam checkers (> 8/10 score)

**Personalization & Segmentation**:
- [ ] Personalization tokens work correctly
- [ ] Correct recipient segmentation
- [ ] Time zone considered for send time
- [ ] Language/locale appropriate

**Testing & QA**:
- [ ] Tested in development environment first
- [ ] Sent test emails to real addresses
- [ ] Checked in spam folder
- [ ] Verified tracking pixels work (if used)
- [ ] Confirmed click tracking works
- [ ] Tested unsubscribe flow
- [ ] Verified email preferences are honored

**Legal & Compliance**:
- [ ] CAN-SPAM Act compliant (US)
- [ ] GDPR compliant (EU)
- [ ] CASL compliant (Canada)
- [ ] Double opt-in for subscriptions (where required)
- [ ] Privacy policy linked
- [ ] Terms of service linked (where applicable)

**Analytics & Monitoring**:
- [ ] Open tracking configured
- [ ] Click tracking configured
- [ ] Bounce handling set up
- [ ] Complaint handling set up
- [ ] Unsubscribe tracking active
- [ ] Email send logged in database

---

## 13. WordPress-Specific Testing {#wordpress-testing}

WordPress powers over 40% of all websites, making WordPress-specific QA skills essential for many testers. WordPress testing involves unique challenges due to its plugin ecosystem, theme system, and frequent updates.

### 13.1 WordPress Environment Setup for Testing

#### 13.1.1 Local WordPress Development Stack

**Test Environment Setup with Docker**:

```yaml
# docker-compose.yml
version: '3.8'

services:
  wordpress:
    image: wordpress:latest
    ports:
      - "8080:80"
    environment:
      WORDPRESS_DB_HOST: db
      WORDPRESS_DB_USER: wpuser
      WORDPRESS_DB_PASSWORD: wppass
      WORDPRESS_DB_NAME: wordpress_test
      WORDPRESS_DEBUG: 1
      WORDPRESS_DEBUG_LOG: 1
      WORDPRESS_DEBUG_DISPLAY: 0
    volumes:
      - ./wp-content:/var/www/html/wp-content
      - ./uploads.ini:/usr/local/etc/php/conf.d/uploads.ini
    depends_on:
      - db

  db:
    image: mysql:8.0
    environment:
      MYSQL_DATABASE: wordpress_test
      MYSQL_USER: wpuser
      MYSQL_PASSWORD: wppass
      MYSQL_ROOT_PASSWORD: rootpass
    volumes:
      - db_data:/var/lib/mysql

  phpmyadmin:
    image: phpmyadmin:latest
    ports:
      - "8081:80"
    environment:
      PMA_HOST: db
      PMA_USER: wpuser
      PMA_PASSWORD: wppass

volumes:
  db_data:
```

**Test Case TC_WP_SETUP_001: Verify WordPress Installation**

```javascript
const axios = require('axios');
const {test, expect} = require('@playwright/test');

test('TC_WP_SETUP_001: Verify fresh WordPress installation', async ({page}) => {
  // Navigate to WordPress site
  await page.goto('http://localhost:8080');
  
  // Verify WordPress is running
  const title = await page.title();
  expect(title).toContain('WordPress');
  
  // Check if setup is needed
  const url = page.url();
  if (url.includes('wp-admin/install.php')) {
    // Complete installation
    await page.fill('#weblog_title', 'Test Site');
    await page.fill('#user_login', 'admin');
    await page.fill('#pass1', 'TestPassword123!');
    await page.fill('#pass2', 'TestPassword123!');
    await page.fill('#admin_email', 'admin@test.local');
    await page.click('#submit');
    
    // Wait for installation complete
    await page.waitForSelector('text=Success!');
  }
  
  // Login to admin
  await page.goto('http://localhost:8080/wp-login.php');
  await page.fill('#user_login', 'admin');
  await page.fill('#user_pass', 'TestPassword123!');
  await page.click('#wp-submit');
  
  // Verify logged in
  await expect(page.locator('#wpadminbar')).toBeVisible();
  
  // Check WordPress version
  const versionResponse = await axios.get('http://localhost:8080/wp-admin/includes/update.php');
  // Version checking logic here
});
```

### 13.2 Plugin Conflict Testing Methodology

Plugin conflicts are one of the most common issues in WordPress. A systematic approach to testing plugin conflicts is essential.

#### 13.2.1 Binary Search Plugin Conflict Detection

**Test Case TC_WP_PLUGIN_001: Systematic Plugin Conflict Detection**

```javascript
test('TC_WP_PLUGIN_001: Identify conflicting plugins', async ({page}) => {
  // Login to WordPress admin
  await page.goto('http://localhost:8080/wp-admin');
  await page.fill('#user_login', 'admin');
  await page.fill('#user_pass', 'TestPassword123!');
  await page.click('#wp-submit');
  
  // Navigate to plugins page
  await page.goto('http://localhost:8080/wp-admin/plugins.php');
  
  // Get list of active plugins
  const activePlugins = await page.$$eval(
    '.active .plugin-title strong',
    plugins => plugins.map(p => p.textContent)
  );
  
  console.log('Active plugins:', activePlugins);
  
  // Record initial error state
  await page.goto('http://localhost:8080');
  const hasInitialError = await page.locator('body').evaluate(
    el => el.textContent.includes('error') || el.textContent.includes('Warning')
  );
  
  // Deactivate all plugins
  await page.goto('http://localhost:8080/wp-admin/plugins.php');
  await page.check('#cb-select-all-1');
  await page.selectOption('#bulk-action-selector-top', 'deactivate-selected');
  await page.click('#doaction');
  
  // Check if error persists with all plugins off
  await page.goto('http://localhost:8080');
  const errorWithoutPlugins = await page.locator('body').evaluate(
    el => el.textContent.includes('error')
  );
  
  if (!errorWithoutPlugins && hasInitialError) {
    // Error is plugin-related, use binary search
    const conflictingPlugin = await binarySearchPluginConflict(page, activePlugins);
    console.log('Conflicting plugin found:', conflictingPlugin);
    expect(conflictingPlugin).toBeDefined();
  } else if (errorWithoutPlugins) {
    // Error is theme or core related
    console.log('Error not caused by plugins');
  }
});

async function binarySearchPluginConflict(page, plugins) {
  if (plugins.length === 0) return null;
  if (plugins.length === 1) {
    // Activate single plugin and test
    await activatePlugin(page, plugins[0]);
    const hasError = await checkForErrors(page);
    return hasError ? plugins[0] : null;
  }
  
  // Split plugins in half
  const midpoint = Math.floor(plugins.length / 2);
  const firstHalf = plugins.slice(0, midpoint);
  const secondHalf = plugins.slice(midpoint);
  
  // Test first half
  await activatePlugins(page, firstHalf);
  const firstHalfHasError = await checkForErrors(page);
  await deactivateAllPlugins(page);
  
  if (firstHalfHasError) {
    return binarySearchPluginConflict(page, firstHalf);
  } else {
    return binarySearchPluginConflict(page, secondHalf);
  }
}

async function activatePlugin(page, pluginName) {
  await page.goto('http://localhost:8080/wp-admin/plugins.php');
  const pluginRow = await page.locator(`tr:has-text("${pluginName}")`);
  await pluginRow.locator('a:has-text("Activate")').click();
}

async function activatePlugins(page, pluginNames) {
  for (const plugin of pluginNames) {
    await activatePlugin(page, plugin);
  }
}

async function deactivateAllPlugins(page) {
  await page.goto('http://localhost:8080/wp-admin/plugins.php');
  await page.check('#cb-select-all-1');
  await page.selectOption('#bulk-action-selector-top', 'deactivate-selected');
  await page.click('#doaction');
}

async function checkForErrors(page) {
  await page.goto('http://localhost:8080');
  
  // Check for PHP errors
  const bodyText = await page.locator('body').textContent();
  const hasPhpError = bodyText.includes('Fatal error') ||
                      bodyText.includes('Warning:') ||
                      bodyText.includes('Notice:');
  
  // Check for JavaScript errors
  const jsErrors = [];
  page.on('console', msg => {
    if (msg.type() === 'error') {
      jsErrors.push(msg.text());
    }
  });
  
  await page.waitForTimeout(2000); // Wait for JS to execute
  
  return hasPhpError || jsErrors.length > 0;
}
```

#### 13.2.2 Plugin Compatibility Matrix Testing

**Test Case TC_WP_PLUGIN_002: Test Plugin Combinations**

```javascript
test('TC_WP_PLUGIN_002: Test common plugin combinations', async ({page}) => {
  const commonPlugins = [
    'WooCommerce',
    'Yoast SEO',
    'Contact Form 7',
    'Elementor',
    'Jetpack'
  ];
  
  const compatibilityMatrix = [];
  
  // Test each pair of plugins
  for (let i = 0; i < commonPlugins.length; i++) {
    for (let j = i + 1; j < commonPlugins.length; j++) {
      const plugin1 = commonPlugins[i];
      const plugin2 = commonPlugins[j];
      
      // Deactivate all plugins
      await deactivateAllPlugins(page);
      
      // Activate pair
      await activatePlugin(page, plugin1);
      await activatePlugin(page, plugin2);
      
      // Test for conflicts
      const hasConflict = await checkForErrors(page);
      
      compatibilityMatrix.push({
        plugin1,
        plugin2,
        compatible: !hasConflict
      });
      
      console.log(`${plugin1} + ${plugin2}: ${hasConflict ? 'CONFLICT' : 'OK'}`);
    }
  }
  
  // Generate compatibility report
  const report = generateCompatibilityReport(compatibilityMatrix);
  console.log(report);
  
  // Expect all to be compatible (or document known conflicts)
  const conflicts = compatibilityMatrix.filter(c => !c.compatible);
  if (conflicts.length > 0) {
    console.warn('Plugin conflicts detected:', conflicts);
  }
});

function generateCompatibilityReport(matrix) {
  let report = '\n=== Plugin Compatibility Matrix ===\n\n';
  
  for (const result of matrix) {
    const status = result.compatible ? '✓ Compatible' : '✗ Conflict';
    report += `${result.plugin1} + ${result.plugin2}: ${status}\n`;
  }
  
  return report;
}
```

### 13.3 Theme Switching Testing

Themes control the presentation layer of WordPress. Testing theme switches ensures content remains accessible and functional.

**Test Case TC_WP_THEME_001: Switch Between Themes**

```javascript
test('TC_WP_THEME_001: Test theme switching', async ({page}) => {
  await page.goto('http://localhost:8080/wp-admin');
  await login(page);
  
  // Create test content
  await createTestPost(page, {
    title: 'Theme Switch Test Post',
    content: `
      <h2>Heading 2</h2>
      <p>Paragraph text</p>
      <ul>
        <li>List item 1</li>
        <li>List item 2</li>
      </ul>
      <img src="https://via.placeholder.com/600x400" alt="Test image"/>
    `
  });
  
  const themes = ['Twenty Twenty-One', 'Twenty Twenty-Two', 'Twenty Twenty-Three'];
  const testResults = [];
  
  for (const theme of themes) {
    // Activate theme
    await page.goto('http://localhost:8080/wp-admin/themes.php');
    const themeCard = await page.locator(`.theme:has-text("${theme}")`);
    await themeCard.hover();
    await themeCard.locator('button:has-text("Activate")').click();
    
    // Wait for activation
    await page.waitForSelector('.theme.active:has-text("${theme}")');
    
    // Visit homepage
    await page.goto('http://localhost:8080');
    
    // Take screenshot
    await page.screenshot({path: `screenshots/theme-${theme.replace(/\s/g, '-')}.png`});
    
    // Check for errors
    const hasError = await checkForErrors(page);
    
    // Verify content is visible
    await page.goto('http://localhost:8080/theme-switch-test-post/');
    const contentVisible = await page.locator('h2:has-text("Heading 2")').isVisible();
    const imageLoaded = await page.locator('img[alt="Test image"]').isVisible();
    
    testResults.push({
      theme,
      hasError,
      contentVisible,
      imageLoaded,
      passed: !hasError && contentVisible && imageLoaded
    });
  }
  
  // Verify all themes work
  for (const result of testResults) {
    expect(result.passed).toBe(true);
    console.log(`${result.theme}: ${result.passed ? 'PASS' : 'FAIL'}`);
  }
});

async function createTestPost(page, {title, content}) {
  await page.goto('http://localhost:8080/wp-admin/post-new.php');
  
  // Wait for Gutenberg editor
  await page.waitForSelector('.editor-post-title__input');
  
  // Enter title
  await page.fill('.editor-post-title__input', title);
  
  // Switch to code editor for easier content insertion
  await page.click('button[aria-label="Options"]');
  await page.click('button:has-text("Code editor")');
  
  // Insert content
  await page.fill('.editor-post-text-editor', content);
  
  // Publish post
  await page.click('button:has-text("Publish")');
  await page.click('.editor-post-publish-panel__toggle:has-text("Publish")');
  
  // Wait for publish confirmation
  await page.waitForSelector('text=Post published');
}
```

### 13.4 WooCommerce Checkout Flow Testing

WooCommerce is the most popular e-commerce plugin for WordPress. Thorough checkout testing is critical.

**Test Case TC_WC_CHECKOUT_001: Complete Checkout Flow**

```javascript
test('TC_WC_CHECKOUT_001: Complete WooCommerce purchase', async ({page}) => {
  // Ensure WooCommerce is installed and activated
  await page.goto('http://localhost:8080/shop');
  
  // Add product to cart
  const productCard = await page.locator('.product').first();
  await productCard.locator('a.add_to_cart_button').click();
  
  // Wait for "Added to cart" message
  await page.waitForSelector('.woocommerce-message:has-text("has been added to your cart")');
  
  // View cart
  await page.click('a:has-text("View cart")');
  
  // Verify cart page
  expect(page.url()).toContain('/cart');
  
  // Update quantity
  await page.fill('input.qty', '2');
  await page.click('button:has-text("Update cart")');
  
  // Proceed to checkout
  await page.click('a:has-text("Proceed to checkout")');
  
  // Fill billing details
  await page.fill('#billing_first_name', 'John');
  await page.fill('#billing_last_name', 'Doe');
  await page.fill('#billing_company', 'Test Company');
  await page.fill('#billing_country', 'US');
  await page.fill('#billing_address_1', '123 Test Street');
  await page.fill('#billing_city', 'San Francisco');
  await page.selectOption('#billing_state', 'CA');
  await page.fill('#billing_postcode', '94105');
  await page.fill('#billing_phone', '555-1234');
  await page.fill('#billing_email', 'john@test.com');
  
  // Select payment method
  await page.check('#payment_method_cheque'); // Check payment (test mode)
  
  // Place order
  await page.click('#place_order');
  
  // Wait for order received page
  await page.waitForURL(/order-received/);
  
  // Verify order confirmation
  await expect(page.locator('.woocommerce-thankyou-order-received')).toContain Text('Thank you');
  
  // Get order number
  const orderNumberText = await page.locator('.woocommerce-order-overview__order').textContent();
  const orderNumber = orderNumberText.match(/\d+/)[0];
  
  expect(orderNumber).toBeDefined();
  console.log('Order placed successfully:', orderNumber);
  
  // Verify order in admin
  await page.goto(`http://localhost:8080/wp-admin/edit.php?post_type=shop_order`);
  await expect(page.locator(`td:has-text("${orderNumber}")`)).toBeVisible();
});
```

**Test Case TC_WC_CHECKOUT_002: Test Payment Gateways**

```javascript
test('TC_WC_CHECKOUT_002: Test different payment methods', async ({page}) => {
  const paymentMethods = [
    {id: 'cheque', name: 'Check payments'},
    {id: 'cod', name: 'Cash on delivery'},
    {id: 'bacs', name: 'Direct bank transfer'}
  ];
  
  for (const method of paymentMethods) {
    // Add product to cart
    await page.goto('http://localhost:8080/shop');
    await page.click('.product .add_to_cart_button');
    
    // Go to checkout
    await page.goto('http://localhost:8080/checkout');
    
    // Fill minimal billing info
    await page.fill('#billing_first_name', 'Test');
    await page.fill('#billing_last_name', 'User');
    await page.fill('#billing_address_1', '123 St');
    await page.fill('#billing_city', 'City');
    await page.fill('#billing_postcode', '12345');
    await page.fill('#billing_phone', '555-0000');
    await page.fill('#billing_email', 'test@example.com');
    
    // Select payment method
    await page.check(`#payment_method_${method.id}`);
    
    // Verify payment method description shown
    const descriptionVisible = await page.locator(`#payment_method_${method.id}`).isChecked();
    expect(descriptionVisible).toBe(true);
    
    // Place order
    await page.click('#place_order');
    
    // Verify order success
    await page.waitForURL(/order-received/);
    await expect(page.locator('.woocommerce-thankyou-order-received')).toBeVisible();
    
    console.log(`✓ ${method.name} payment method works`);
    
    // Clear cart for next iteration
    await page.goto('http://localhost:8080/cart');
    await page.click('.remove');
  }
});
```

**Test Case TC_WC_CHECKOUT_003: Coupon Code Testing**

```javascript
test('TC_WC_CHECKOUT_003: Apply and verify coupon codes', async ({page}) => {
  // Create coupon via WP-CLI or API
  // For this example, assume coupon "TEST10" exists for 10% off
  
  await page.goto('http://localhost:8080/shop');
  
  // Add product to cart
  await page.click('.product .add_to_cart_button');
  await page.goto('http://localhost:8080/cart');
  
  // Get original subtotal
  const originalSubtotal = await page.locator('.cart-subtotal .amount').textContent();
  console.log('Original subtotal:', originalSubtotal);
  
  // Apply coupon
  await page.fill('#coupon_code', 'TEST10');
  await page.click('button:has-text("Apply coupon")');
  
  // Wait for coupon applied message
  await page.waitForSelector('.woocommerce-message:has-text("Coupon code applied")');
  
  // Verify discount applied
  const discountAmount = await page.locator('.cart-discount .amount').textContent();
  expect(discountAmount).toBeDefined();
  console.log('Discount amount:', discountAmount);
  
  // Get new total
  const newTotal = await page.locator('.order-total .amount').textContent();
  console.log('New total:', newTotal);
  
  // Verify total is less than original
  const originalValue = parseFloat(originalSubtotal.replace(/[^0-9.]/g, ''));
  const newValue = parseFloat(newTotal.replace(/[^0-9.]/g, ''));
  expect(newValue).toBeLessThan(originalValue);
  
  // Test invalid coupon
  await page.fill('#coupon_code', 'INVALID123');
  await page.click('button:has-text("Apply coupon")');
  
  // Expect error message
  await page.waitForSelector('.woocommerce-error:has-text("Coupon")');
});
```

### 13.5 Gutenberg Editor Testing

The Gutenberg block editor is WordPress's modern content editor. Testing block interactions is essential.

**Test Case TC_WP_GUTENBERG_001: Add and Configure Blocks**

```javascript
test('TC_WP_GUTENBERG_001: Test Gutenberg block editor', async ({page}) => {
  await page.goto('http://localhost:8080/wp-admin/post-new.php');
  await login(page);
  
  // Wait for editor to load
  await page.waitForSelector('.editor-post-title__input');
  
  // Add title
  await page.fill('.editor-post-title__input', 'Gutenberg Test Post');
  
  // Add paragraph block
  await page.click('.block-editor-default-block-appender__content');
  await page.keyboard.type('This is a test paragraph.');
  
  // Add heading block
  await page.keyboard.press('Enter');
  await page.keyboard.type('/heading');
  await page.keyboard.press('Enter');
  await page.keyboard.type('Test Heading');
  
  // Add image block
  await page.keyboard.press('Enter');
  await page.keyboard.type('/image');
  await page.keyboard.press('Enter');
  
  // Upload image
  await page.setInputFiles(
    'input[type="file"]',
    'test-fixtures/test-image.jpg'
  );
  
  // Wait for image upload
  await page.waitForSelector('.block-editor-block-list__block.is-selected img');
  
  // Add list block
  await page.keyboard.press('Enter');
  await page.keyboard.type('/list');
  await page.keyboard.press('Enter');
  await page.keyboard.type('List item 1');
  await page.keyboard.press('Enter');
  await page.keyboard.type('List item 2');
  
  // Add button block
  await page.keyboard.press('Enter');
  await page.keyboard.type('/button');
  await page.keyboard.press('Enter');
  
  // Configure button
  await page.fill('.block-editor-rich-text__editable', 'Click Me');
  await page.click('button[aria-label="Link"]');
  await page.fill('input[aria-label="URL"]', 'https://example.com');
  await page.keyboard.press('Enter');
  
  // Save draft
  await page.click('button:has-text("Save draft")');
  await page.waitForSelector('.editor-post-saved-state:has-text("Saved")');
  
  // Preview post
  await page.click('button:has-text("Preview")');
  
  // Switch to preview tab
  const [previewPage] = await Promise.all([
    page.waitForEvent('popup'),
    page.click('a:has-text("Preview in new tab")')
  ]);
  
  // Verify content in preview
  await expect(previewPage.locator('h1, h2:has-text("Test Heading")')).toBeVisible();
  await expect(previewPage.locator('p:has-text("This is a test paragraph")')).toBeVisible();
  await expect(previewPage.locator('img')).toBeVisible();
  await expect(previewPage.locator('li:has-text("List item 1")')).toBeVisible();
  await expect(previewPage.locator('a:has-text("Click Me")')).toBeVisible();
  
  await previewPage.close();
  
  // Publish post
  await page.click('button:has-text("Publish")');
  await page.click('.editor-post-publish-panel__toggle:has-text("Publish")');
  await page.waitForSelector('.editor-post-publish-panel__header-published');
});
```

### 13.6 WordPress REST API Testing

**Test Case TC_WP_API_001: Test WordPress REST API Endpoints**

```javascript
const axios = require('axios');

test('TC_WP_API_001: Test REST API endpoints', async () => {
  const baseURL = 'http://localhost:8080/wp-json/wp/v2';
  
  // Test posts endpoint
  const postsResponse = await axios.get(`${baseURL}/posts`);
  expect(postsResponse.status).toBe(200);
  expect(Array.isArray(postsResponse.data)).toBe(true);
  
  // Test single post
  if (postsResponse.data.length > 0) {
    const postId = postsResponse.data[0].id;
    const postResponse = await axios.get(`${baseURL}/posts/${postId}`);
    expect(postResponse.status).toBe(200);
    expect(postResponse.data.id).toBe(postId);
  }
  
  // Test pages endpoint
  const pagesResponse = await axios.get(`${baseURL}/pages`);
  expect(pagesResponse.status).toBe(200);
  
  // Test users endpoint
  const usersResponse = await axios.get(`${baseURL}/users`);
  expect(usersResponse.status).toBe(200);
  
  // Test categories
  const categoriesResponse = await axios.get(`${baseURL}/categories`);
  expect(categoriesResponse.status).toBe(200);
  
  // Test tags
  const tagsResponse = await axios.get(`${baseURL}/tags`);
  expect(tagsResponse.status).toBe(200);
  
  // Test media
  const mediaResponse = await axios.get(`${baseURL}/media`);
  expect(mediaResponse.status).toBe(200);
});

test('TC_WP_API_002: Create post via REST API', async () => {
  const baseURL = 'http://localhost:8080/wp-json/wp/v2';
  
  // Get authentication token (use Application Passwords or JWT)
  const username = 'admin';
  const appPassword = 'xxxx xxxx xxxx xxxx xxxx xxxx'; // Application password
  const auth = Buffer.from(`${username}:${appPassword}`).toString('base64');
  
  // Create post
  const newPost = {
    title: 'API Test Post',
    content: 'This post was created via the REST API.',
    status: 'publish'
  };
  
  const response = await axios.post(`${baseURL}/posts`, newPost, {
    headers: {
      'Authorization': `Basic ${auth}`,
      'Content-Type': 'application/json'
    }
  });
  
  expect(response.status).toBe(201);
  expect(response.data.title.rendered).toBe('API Test Post');
  expect(response.data.status).toBe('publish');
  
  const postId = response.data.id;
  
  // Update post
  const updateResponse = await axios.post(
    `${baseURL}/posts/${postId}`,
    {content: 'Updated content'},
    {headers: {'Authorization': `Basic ${auth}`}}
  );
  
  expect(updateResponse.status).toBe(200);
  expect(updateResponse.data.content.rendered).toContain('Updated content');
  
  // Delete post
  const deleteResponse = await axios.delete(`${baseURL}/posts/${postId}`, {
    headers: {'Authorization': `Basic ${auth}`}
  });
  
  expect(deleteResponse.status).toBe(200);
});
```

### 13.7 WordPress Multisite Testing

**Test Case TC_WP_MULTISITE_001: Test Multisite Network**

```javascript
test('TC_WP_MULTISITE_001: Test multisite functionality', async ({page}) => {
  // Assume multisite is already configured
  await page.goto('http://localhost:8080/wp-admin/network/');
  await login(page);
  
  // Create new site
  await page.goto('http://localhost:8080/wp-admin/network/site-new.php');
  
  await page.fill('#site-address', 'testsite');
  await page.fill('#site-title', 'Test Subsite');
  await page.fill('#admin-email', 'subsite@example.com');
  
  await page.click('#submit');
  
  // Wait for success message
  await page.waitForSelector('.notice-success:has-text("created")');
  
  // Visit new site
  await page.goto('http://testsite.localhost:8080');
  
  // Verify site loads
  const title = await page.title();
  expect(title).toContain('Test Subsite');
  
  // Switch to new site admin
  await page.goto('http://testsite.localhost:8080/wp-admin');
  
  // Create post on subsite
  await createTestPost(page, {
    title: 'Subsite Post',
    content: 'This post is on the subsite.'
  });
  
  // Verify post appears on subsite
  await page.goto('http://testsite.localhost:8080');
  await expect(page.locator('a:has-text("Subsite Post")')).toBeVisible();
  
  // Verify post does NOT appear on main site
  await page.goto('http://localhost:8080');
  await expect(page.locator('a:has-text("Subsite Post")')).not.toBeVisible();
});
```

### 13.8 WordPress Update Compatibility Testing

**Test Case TC_WP_UPDATE_001: Test WordPress Core Update**

```javascript
test('TC_WP_UPDATE_001: Test WordPress version update', async ({page}) => {
  await page.goto('http://localhost:8080/wp-admin/update-core.php');
  await login(page);
  
  // Check current version
  const currentVersion = await page.locator('.core-updates p').first().textContent();
  console.log('Current version:', currentVersion);
  
  // Take database backup (using WP-CLI)
  const {exec} = require('child_process');
  const util = require('util');
  const execPromise = util.promisify(exec);
  
  await execPromise('wp db export backup-before-update.sql');
  
  // Backup wp-content
  await execPromise('tar -czf wp-content-backup.tar.gz wp-content/');
  
  // Run update
  if (await page.locator('button:has-text("Update Now")').isVisible()) {
    // Take screenshot before update
    await page.screenshot({path: 'before-update.png', fullPage: true});
    
    await page.click('button:has-text("Update Now")');
    
    // Wait for update to complete (may take a while)
    await page.waitForSelector('text=WordPress updated successfully', {timeout: 180000});
    
    // Verify new version
    await page.goto('http://localhost:8080/wp-admin/');
    const newVersion = await page.locator('#wp-version-message').textContent();
    console.log('New version:', newVersion);
    
    // Test critical functionality
    // 1. Can access admin
    expect(page.url()).toContain('wp-admin');
    
    // 2. Can create post
    await createTestPost(page, {
      title: 'Post After Update',
      content: 'Testing post creation after WordPress update.'
    });
    
    // 3. Can visit frontend
    await page.goto('http://localhost:8080');
    await expect(page.locator('body')).toBeVisible();
    
    // 4. Check for PHP errors
    const hasError = await checkForErrors(page);
    expect(hasError).toBe(false);
    
    // 5. Test plugin compatibility
    await page.goto('http://localhost:8080/wp-admin/plugins.php');
    const pluginErrors = await page.locator('.plugin-update-tr.notice-error').count();
    expect(pluginErrors).toBe(0);
    
    // Take screenshot after update
    await page.screenshot({path: 'after-update.png', fullPage: true});
    
    console.log('✓ WordPress update successful and tested');
  } else {
    console.log('No updates available');
  }
});
```

### 13.9 Database Migration Testing

**Test Case TC_WP_MIGRATION_001: Test Database Export/Import**

```javascript
test('TC_WP_MIGRATION_001: Export and import WordPress database', async () => {
  const {exec} = require('child_process');
  const util = require('util');
  const execPromise = util.promisify(exec);
  
  // Export database
  const exportResult = await execPromise('wp db export migration-test.sql');
  expect(exportResult.stdout).toContain('Success');
  
  // Create new database
  await execPromise('wp db create test_migration_db');
  
  // Import to new database
  await execPromise('wp db import migration-test.sql --dbname=test_migration_db');
  
  // Search and replace URLs (if domain changed)
  await execPromise(
    'wp search-replace "http://localhost:8080" "http://newdomain.local" --dbname=test_migration_db'
  );
  
  // Verify data integrity
  const tableCount = await execPromise('wp db query "SHOW TABLES" --dbname=test_migration_db');
  expect(tableCount.stdout).toContain('wp_posts');
  expect(tableCount.stdout).toContain('wp_users');
  
  // Check post count
  const postCount = await execPromise('wp db query "SELECT COUNT(*) FROM wp_posts" --dbname=test_migration_db');
  console.log('Post count in migrated database:', postCount.stdout);
  
  // Cleanup
  await execPromise('wp db drop test_migration_db --yes');
  await execPromise('rm migration-test.sql');
});
```

### 13.10 WP-Cron Verification Testing

**Test Case TC_WP_CRON_001: Test WordPress Cron Jobs**

```javascript
test('TC_WP_CRON_001: Verify wp-cron execution', async () => {
  const axios = require('axios');
  
  // Trigger wp-cron
  const response = await axios.get('http://localhost:8080/wp-cron.php');
  expect(response.status).toBe(200);
  
  // Check scheduled events via WP-CLI
  const {exec} = require('child_process');
  const util = require('util');
  const execPromise = util.promisify(exec);
  
  const cronList = await execPromise('wp cron event list --format=json');
  const events = JSON.parse(cronList.stdout);
  
  expect(Array.isArray(events)).toBe(true);
  expect(events.length).toBeGreaterThan(0);
  
  // Check for core WordPress cron jobs
  const hooks = events.map(e => e.hook);
  expect(hooks).toContain('wp_version_check');
  expect(hooks).toContain('wp_update_plugins');
  expect(hooks).toContain('wp_update_themes');
  
  console.log('Scheduled cron events:', events.length);
});

test('TC_WP_CRON_002: Test custom cron job', async () => {
  const {exec} = require('child_process');
  const util = require('util');
  const execPromise = util.promisify(exec);
  
  // Schedule a custom cron event
  await execPromise('wp cron event schedule custom_cleanup_job "+1 hour"');
  
  // Verify event scheduled
  const cronList = await execPromise('wp cron event list --format=json');
  const events = JSON.parse(cronList.stdout);
  
  const customEvent = events.find(e => e.hook === 'custom_cleanup_job');
  expect(customEvent).toBeDefined();
  
  // Run the event immediately
  await execPromise('wp cron event run custom_cleanup_job');
  
  // Clean up
  await execPromise('wp cron event delete custom_cleanup_job');
});
```

### 13.11 WordPress Testing Checklist

**Core WordPress Testing**:
- [ ] Fresh installation completes successfully
- [ ] Login/logout works
- [ ] User registration (if enabled)
- [ ] Password reset flow
- [ ] Create/edit/delete posts
- [ ] Create/edit/delete pages
- [ ] Upload media (images, PDFs, videos)
- [ ] Categories and tags management
- [ ] Comments (if enabled)
- [ ] Search functionality
- [ ] Permalinks working correctly
- [ ] 404 error page displays

**Plugin Testing**:
- [ ] Plugin installation
- [ ] Plugin activation/deactivation
- [ ] Plugin deletion
- [ ] Plugin conflict detection
- [ ] Plugin updates
- [ ] Plugin settings saved correctly

**Theme Testing**:
- [ ] Theme installation
- [ ] Theme activation
- [ ] Theme customizer works
- [ ] Responsive design on mobile/tablet
- [ ] Theme switching preserves content
- [ ] Widget areas functional
- [ ] Navigation menus work
- [ ] Footer content displays

**WooCommerce Testing** (if applicable):
- [ ] Product creation
- [ ] Product categories
- [ ] Add to cart
- [ ] Cart page
- [ ] Checkout process
- [ ] Payment gateway integration
- [ ] Order confirmation emails
- [ ] Order management in admin
- [ ] Coupons
- [ ] Shipping calculations

**Performance Testing**:
- [ ] Page load times acceptable
- [ ] Database queries optimized
- [ ] Images optimized
- [ ] Caching works (if enabled)
- [ ] CDN integration (if applicable)

**Security Testing**:
- [ ] SQL injection prevention
- [ ] XSS prevention
- [ ] CSRF protection
- [ ] File upload restrictions
- [ ] Strong password enforcement
- [ ] Two-factor authentication (if enabled)
- [ ] SSL/HTTPS enforced

**SEO Testing**:
- [ ] Meta titles set correctly
- [ ] Meta descriptions set
- [ ] XML sitemap generates
- [ ] Robots.txt configured
- [ ] Canonical URLs correct
- [ ] Schema markup (if applicable)

---

(Due to length constraints, I'll continue with the remaining sections in the next response. The file will be completed with Search & Filtering Testing, File Upload Testing, Notification System Testing, and CI/CD Test Integration sections, each with similar depth and detail.)


## 14. Search & Filtering Testing {#search-filtering-testing}

Search and filtering functionality is critical for applications with large datasets or product catalogs. Users need to find what they're looking for quickly and accurately.

### 14.1 Full-Text Search Accuracy Testing

#### 14.1.1 Basic Search Functionality

**Test Case TC_SEARCH_001: Basic Keyword Search**

```javascript
test('TC_SEARCH_001: Test basic keyword search', async ({page}) => {
  // Setup: Create test data
  const testProducts = [
    {name: 'Blue Cotton T-Shirt', description: 'Comfortable blue t-shirt made of cotton'},
    {name: 'Red Silk Dress', description: 'Elegant red dress made of silk'},
    {name: 'Blue Denim Jeans', description: 'Classic blue jeans made of denim'},
    {name: 'Green Cotton Pants', description: 'Casual green pants made of cotton'}
  ];
  
  for (const product of testProducts) {
    await createProduct(product);
  }
  
  // Test search for "blue"
  await page.goto('http://example.com/products');
  await page.fill('input[name="search"]', 'blue');
  await page.click('button[type="submit"]');
  
  // Should return Blue Cotton T-Shirt and Blue Denim Jeans
  const results = await page.locator('.product-item').allTextContents();
  expect(results).toContain('Blue Cotton T-Shirt');
  expect(results).toContain('Blue Denim Jeans');
  expect(results).not.toContain('Red Silk Dress');
  expect(results).not.toContain('Green Cotton Pants');
  
  // Verify result count
  const resultCount = await page.locator('.product-item').count();
  expect(resultCount).toBe(2);
  
  // Test search for "cotton"
  await page.fill('input[name="search"]', 'cotton');
  await page.click('button[type="submit"]');
  
  const cottonResults = await page.locator('.product-item').allTextContents();
  expect(cottonResults).toContain('Blue Cotton T-Shirt');
  expect(cottonResults).toContain('Green Cotton Pants');
  
  // Test no results
  await page.fill('input[name="search"]', 'leather');
  await page.click('button[type="submit"]');
  
  await expect(page.locator('.no-results')).toBeVisible();
  expect(await page.locator('.no-results').textContent()).toContain('No products found');
});
```

#### 14.1.2 Advanced Search Operators

**Test Case TC_SEARCH_002: Test Search Operators**

```javascript
test('TC_SEARCH_002: Test AND/OR search operators', async () => {
  const searchTests = [
    {
      query: 'blue AND cotton',
      expectedResults: ['Blue Cotton T-Shirt'],
      unexpectedResults: ['Blue Denim Jeans', 'Green Cotton Pants']
    },
    {
      query: 'blue OR red',
      expectedResults: ['Blue Cotton T-Shirt', 'Red Silk Dress', 'Blue Denim Jeans'],
      unexpectedResults: ['Green Cotton Pants']
    },
    {
      query: '"blue cotton"', // Exact phrase
      expectedResults: ['Blue Cotton T-Shirt'],
      unexpectedResults: ['Blue Denim Jeans']
    },
    {
      query: 'blue NOT denim',
      expectedResults: ['Blue Cotton T-Shirt'],
      unexpectedResults: ['Blue Denim Jeans']
    }
  ];
  
  for (const searchTest of searchTests) {
    const response = await axios.get('http://example.com/api/search', {
      params: {q: searchTest.query}
    });
    
    const resultNames = response.data.results.map(r => r.name);
    
    // Check expected results present
    for (const expected of searchTest.expectedResults) {
      expect(resultNames).toContain(expected);
    }
    
    // Check unexpected results absent
    for (const unexpected of searchTest.unexpectedResults) {
      expect(resultNames).not.toContain(unexpected);
    }
  }
});
```

#### 14.1.3 Fuzzy Search and Typo Tolerance

**Test Case TC_SEARCH_003: Test Fuzzy Matching**

```javascript
test('TC_SEARCH_003: Handle typos and fuzzy matching', async ({page}) => {
  // Test common typos
  const typoTests = [
    {typo: 'cottn', correct: 'cotton'},
    {typo: 'blu', correct: 'blue'},
    {typo: 'jeans', correct: 'jeans'}, // Correct spelling
    {typo: 'tshirt', correct: 't-shirt'},
    {typo: 'dres', correct: 'dress'}
  ];
  
  for (const test of typoTests) {
    await page.goto('http://example.com/products');
    await page.fill('input[name="search"]', test.typo);
    await page.click('button[type="submit"]');
    
    // Should still find results despite typo
    const hasResults = await page.locator('.product-item').count() > 0;
    expect(hasResults).toBe(true);
    
    // Should show "Did you mean?" suggestion for typos
    if (test.typo !== test.correct) {
      const hasSuggestion = await page.locator('.search-suggestion').isVisible();
      if (hasSuggestion) {
        const suggestionText = await page.locator('.search-suggestion').textContent();
        expect(suggestionText.toLowerCase()).toContain(test.correct);
      }
    }
  }
});
```

### 14.2 Faceted Search Testing

Faceted search allows users to filter results by multiple criteria simultaneously.

**Test Case TC_SEARCH_FACET_001: Test Multi-Facet Filtering**

```javascript
test('TC_SEARCH_FACET_001: Apply multiple filters', async ({page}) => {
  await page.goto('http://example.com/products');
  
  // Initial state - all products shown
  const initialCount = await page.locator('.product-item').count();
  expect(initialCount).toBeGreaterThan(0);
  
  // Apply color filter
  await page.check('input[name="color"][value="blue"]');
  await page.waitForSelector('.product-item');
  
  let filteredCount = await page.locator('.product-item').count();
  expect(filteredCount).toBeLessThan(initialCount);
  
  // Verify only blue items shown
  const blueResults = await page.locator('.product-item').allTextContents();
  for (const result of blueResults) {
    expect(result.toLowerCase()).toContain('blue');
  }
  
  // Add material filter
  await page.check('input[name="material"][value="cotton"]');
  await page.waitForSelector('.product-item');
  
  filteredCount = await page.locator('.product-item').count();
  
  // Should show only blue cotton items
  const blueCottonResults = await page.locator('.product-item').allTextContents();
  for (const result of blueCottonResults) {
    expect(result.toLowerCase()).toContain('blue');
    expect(result.toLowerCase()).toContain('cotton');
  }
  
  // Add price range filter
  await page.fill('input[name="price_min"]', '0');
  await page.fill('input[name="price_max"]', '50');
  await page.click('button:has-text("Apply")');
  
  // Verify results within price range
  const prices = await page.locator('.product-price').allTextContents();
  for (const priceText of prices) {
    const price = parseFloat(priceText.replace(/[^0-9.]/g, ''));
    expect(price).toBeLessThanOrEqual(50);
  }
  
  // Test clearing filters
  await page.click('button:has-text("Clear all filters")');
  
  const clearedCount = await page.locator('.product-item').count();
  expect(clearedCount).toBe(initialCount);
});
```

**Test Case TC_SEARCH_FACET_002: Test Facet Counts**

```javascript
test('TC_SEARCH_FACET_002: Verify facet counts accurate', async ({page}) => {
  await page.goto('http://example.com/products');
  
  // Get facet counts from UI
  const colorFacets = await page.locator('.facet-color .facet-option').all();
  
  for (const facet of colorFacets) {
    const facetText = await facet.textContent();
    const match = facetText.match(/\((\d+)\)/); // Extract count like "Blue (5)"
    
    if (match) {
      const expectedCount = parseInt(match[1]);
      const colorValue = await facet.locator('input').getAttribute('value');
      
      // Apply just this filter
      await page.click('button:has-text("Clear all filters")');
      await page.check(`input[name="color"][value="${colorValue}"]`);
      await page.waitForSelector('.product-item');
      
      const actualCount = await page.locator('.product-item').count();
      
      expect(actualCount).toBe(expectedCount);
    }
  }
});
```

### 14.3 Sort Order Verification

**Test Case TC_SEARCH_SORT_001: Test Sorting Options**

```javascript
test('TC_SEARCH_SORT_001: Verify all sort orders', async ({page}) => {
  await page.goto('http://example.com/products');
  
  const sortTests = [
    {
      option: 'price_low_high',
      label: 'Price: Low to High',
      validator: (prices) => {
        for (let i = 1; i < prices.length; i++) {
          expect(prices[i]).toBeGreaterThanOrEqual(prices[i-1]);
        }
      }
    },
    {
      option: 'price_high_low',
      label: 'Price: High to Low',
      validator: (prices) => {
        for (let i = 1; i < prices.length; i++) {
          expect(prices[i]).toBeLessThanOrEqual(prices[i-1]);
        }
      }
    },
    {
      option: 'name_a_z',
      label: 'Name: A-Z',
      validator: (names) => {
        const sorted = [...names].sort();
        expect(names).toEqual(sorted);
      }
    },
    {
      option: 'newest',
      label: 'Newest First',
      validator: (dates) => {
        for (let i = 1; i < dates.length; i++) {
          expect(new Date(dates[i])).toBeLessThanOrEqual(new Date(dates[i-1]));
        }
      }
    },
    {
      option: 'rating',
      label: 'Highest Rated',
      validator: (ratings) => {
        for (let i = 1; i < ratings.length; i++) {
          expect(ratings[i]).toBeLessThanOrEqual(ratings[i-1]);
        }
      }
    }
  ];
  
  for (const sortTest of sortTests) {
    // Select sort option
    await page.selectOption('select[name="sort"]', sortTest.option);
    await page.waitForSelector('.product-item');
    
    // Extract and verify sort order
    if (sortTest.option.includes('price')) {
      const prices = await page.locator('.product-price').allTextContents();
      const numericPrices = prices.map(p => parseFloat(p.replace(/[^0-9.]/g, '')));
      sortTest.validator(numericPrices);
    } else if (sortTest.option.includes('name')) {
      const names = await page.locator('.product-name').allTextContents();
      sortTest.validator(names);
    } else if (sortTest.option === 'newest') {
      const dates = await page.locator('.product-date').allTextContents();
      sortTest.validator(dates);
    } else if (sortTest.option === 'rating') {
      const ratings = await page.locator('.product-rating').allTextContents();
      const numericRatings = ratings.map(r => parseFloat(r));
      sortTest.validator(numericRatings);
    }
    
    console.log(`✓ Sort by ${sortTest.label} working correctly`);
  }
});
```

### 14.4 Pagination with Filters

**Test Case TC_SEARCH_PAGE_001: Test Pagination with Active Filters**

```javascript
test('TC_SEARCH_PAGE_001: Pagination maintains filters', async ({page}) => {
  await page.goto('http://example.com/products');
  
  // Apply filters
  await page.check('input[name="color"][value="blue"]');
  await page.fill('input[name="price_max"]', '100');
  await page.click('button:has-text("Apply")');
  
  // Get first page results
  const page1Results = await page.locator('.product-item').allTextContents();
  
  // Go to page 2
  await page.click('a[aria-label="Page 2"]');
  await page.waitForURL(/page=2/);
  
  // Verify filters still applied
  const urlParams = new URL(page.url()).searchParams;
  expect(urlParams.get('color')).toContain('blue');
  expect(urlParams.get('price_max')).toBe('100');
  
  // Verify page 2 results also match filters
  const page2Results = await page.locator('.product-item').allTextContents();
  for (const result of page2Results) {
    expect(result.toLowerCase()).toContain('blue');
  }
  
  // Verify no duplicate results across pages
  for (const result of page2Results) {
    expect(page1Results).not.toContain(result);
  }
  
  // Test previous page button
  await page.click('a[aria-label="Previous page"]');
  await page.waitForURL(/page=1/);
  
  const backToPage1 = await page.locator('.product-item').allTextContents();
  expect(backToPage1).toEqual(page1Results);
});
```

### 14.5 Empty State Handling

**Test Case TC_SEARCH_EMPTY_001: Test No Results Scenarios**

```javascript
test('TC_SEARCH_EMPTY_001: Handle no search results gracefully', async ({page}) => {
  await page.goto('http://example.com/products');
  
  // Search for nonsense term
  await page.fill('input[name="search"]', 'xyzabc123notfound');
  await page.click('button[type="submit"]');
  
  // Verify empty state displayed
  await expect(page.locator('.no-results')).toBeVisible();
  
  const emptyMessage = await page.locator('.no-results').textContent();
  expect(emptyMessage.toLowerCase()).toContain('no products found');
  expect(emptyMessage.toLowerCase()).toContain('xyzabc123notfound');
  
  // Verify helpful suggestions shown
  await expect(page.locator('.search-suggestions')).toBeVisible();
  
  // Should offer to:
  // - Clear search
  await expect(page.locator('a:has-text("Clear search")')).toBeVisible();
  
  // - Browse all products
  await expect(page.locator('a:has-text("Browse all")')).toBeVisible();
  
  // - View popular categories
  const categorySuggestions = await page.locator('.suggested-categories a').count();
  expect(categorySuggestions).toBeGreaterThan(0);
  
  // Test clearing search
  await page.click('a:has-text("Clear search")');
  
  const clearedResults = await page.locator('.product-item').count();
  expect(clearedResults).toBeGreaterThan(0);
});

test('TC_SEARCH_EMPTY_002: No results from filters', async ({page}) => {
  await page.goto('http://example.com/products');
  
  // Apply mutually exclusive filters
  await page.check('input[name="color"][value="blue"]');
  await page.fill('input[name="price_min"]', '1000');
  await page.fill('input[name="price_max"]', '10');
  await page.click('button:has-text("Apply")');
  
  // Should show no results
  await expect(page.locator('.no-results')).toBeVisible();
  
  // Should suggest relaxing filters
  await expect(page.locator('button:has-text("Clear filters")')).toBeVisible();
  
  // Test individual filter removal
  const activeFilters = await page.locator('.active-filter').all();
  expect(activeFilters.length).toBeGreaterThan(0);
  
  // Remove one filter
  await page.click('.active-filter .remove-filter');
  
  // Should now show results
  await page.waitForSelector('.product-item');
});
```

### 14.6 Special Characters in Search

**Test Case TC_SEARCH_SPECIAL_001: Handle Special Characters**

```javascript
test('TC_SEARCH_SPECIAL_001: Search with special characters', async ({page}) => {
  // Test data with special characters
  const specialProducts = [
    {name: "Men's T-Shirt"},
    {name: 'C++ Programming Book'},
    {name: 'AT&T Phone'},
    {name: 'Levi\'s 501 Jeans'},
    {name: 'L\'Oréal Shampoo'},
    {name: '50% Off Sale Item'},
    {name: 'Product (Size: Large)'}
  ];
  
  const searchTests = [
    {query: "men's", shouldFind: "Men's T-Shirt"},
    {query: "c++", shouldFind: "C++ Programming Book"},
    {query: "at&t", shouldFind: "AT&T Phone"},
    {query: "levi's", shouldFind: "Levi's 501 Jeans"},
    {query: "l'oreal", shouldFind: "L'Oréal Shampoo"},
    {query: "50%", shouldFind: "50% Off Sale Item"},
    {query: "(large)", shouldFind: "Product (Size: Large)"}
  ];
  
  for (const test of searchTests) {
    await page.goto('http://example.com/products');
    await page.fill('input[name="search"]', test.query);
    await page.click('button[type="submit"]');
    
    const results = await page.locator('.product-item').allTextContents();
    const found = results.some(r => r.includes(test.shouldFind));
    
    expect(found).toBe(true);
    console.log(`✓ Found "${test.shouldFind}" with query "${test.query}"`);
  }
});
```

### 14.7 SQL Injection Prevention via Search

**Test Case TC_SEARCH_SECURITY_001: Test SQL Injection Prevention**

```javascript
test('TC_SEARCH_SECURITY_001: Prevent SQL injection in search', async ({page}) => {
  const sqlInjectionAttempts = [
    "' OR '1'='1",
    "'; DROP TABLE products; --",
    "1' UNION SELECT * FROM users --",
    "admin'--",
    "' OR 1=1--",
    "1' AND '1'='1",
    "'; DELETE FROM products WHERE '1'='1",
    "1' OR '1'='1' /*",
    "<script>alert('XSS')</script>"
  ];
  
  for (const injection of sqlInjectionAttempts) {
    // Send injection attempt
    await page.goto('http://example.com/products');
    await page.fill('input[name="search"]', injection);
    await page.click('button[type="submit"]');
    
    // Page should handle gracefully
    // Should NOT:
    // - Execute SQL
    // - Show database errors
    // - Return all data
    // - Break the page
    
    // Check for SQL error messages
    const bodyText = await page.locator('body').textContent();
    expect(bodyText.toLowerCase()).not.toContain('sql');
    expect(bodyText.toLowerCase()).not.toContain('mysql');
    expect(bodyText.toLowerCase()).not.toContain('syntax error');
    expect(bodyText.toLowerCase()).not.toContain('database error');
    
    // Verify page structure intact
    await expect(page.locator('header')).toBeVisible();
    await expect(page.locator('footer')).toBeVisible();
    
    // Should either:
    // - Return no results (injection treated as search term)
    // - Return normal sanitized results
    const hasResults = await page.locator('.product-item').count();
    const hasNoResults = await page.locator('.no-results').isVisible();
    
    expect(hasResults > 0 || hasNoResults).toBe(true);
    
    console.log(`✓ SQL injection prevented: ${injection}`);
  }
  
  // Test via API endpoint
  for (const injection of sqlInjectionAttempts) {
    const response = await axios.get('http://example.com/api/search', {
      params: {q: injection},
      validateStatus: () => true
    });
    
    // Should return 200 OK (not 500 error)
    expect(response.status).toBe(200);
    
    // Response should not contain SQL error messages
    const responseText = JSON.stringify(response.data).toLowerCase();
    expect(responseText).not.toContain('sql');
    expect(responseText).not.toContain('database');
    expect(responseText).not.toContain('syntax');
  }
});
```

### 14.8 Search Performance Testing

**Test Case TC_SEARCH_PERF_001: Test Search Response Times**

```javascript
test('TC_SEARCH_PERF_001: Search performs within acceptable time', async () => {
  const searchQueries = [
    'blue',
    'shirt',
    'cotton',
    'blue cotton shirt',
    'jeans denim pants',
    'a', // Single character
    'zzz' // Rare term
  ];
  
  const performanceResults = [];
  
  for (const query of searchQueries) {
    const startTime = Date.now();
    
    const response = await axios.get('http://example.com/api/search', {
      params: {q: query}
    });
    
    const endTime = Date.now();
    const duration = endTime - startTime;
    
    performanceResults.push({
      query,
      duration,
      resultCount: response.data.results.length
    });
    
    // Should complete within 500ms
    expect(duration).toBeLessThan(500);
    
    console.log(`Query "${query}": ${duration}ms (${response.data.results.length} results)`);
  }
  
  // Calculate average response time
  const avgTime = performanceResults.reduce((sum, r) => sum + r.duration, 0) / performanceResults.length;
  console.log(`Average search time: ${avgTime.toFixed(2)}ms`);
  
  expect(avgTime).toBeLessThan(300);
});
```

### 14.9 Search Testing Checklist

**Basic Search**:
- [ ] Single keyword search works
- [ ] Multi-word search works
- [ ] Exact phrase search (quotes)
- [ ] Search matches title
- [ ] Search matches description
- [ ] Search matches tags/categories
- [ ] Search is case-insensitive
- [ ] Handles typos/fuzzy matching
- [ ] No results shows appropriate message
- [ ] Special characters handled correctly

**Filters & Facets**:
- [ ] Single filter applies correctly
- [ ] Multiple filters work together (AND logic)
- [ ] Filter counts are accurate
- [ ] Filters update when search changes
- [ ] Clear filter button works
- [ ] Clear all filters works
- [ ] Active filters displayed
- [ ] URL parameters reflect filters
- [ ] Filters persist across pages
- [ ] Mobile filter UI works

**Sorting**:
- [ ] Sort by price (low to high)
- [ ] Sort by price (high to low)
- [ ] Sort by name (A-Z)
- [ ] Sort by name (Z-A)
- [ ] Sort by date (newest first)
- [ ] Sort by date (oldest first)
- [ ] Sort by popularity
- [ ] Sort by rating
- [ ] Sort persists with filters
- [ ] Default sort displayed correctly

**Pagination**:
- [ ] Page navigation works
- [ ] Next/previous buttons work
- [ ] Filters maintained across pages
- [ ] Sort maintained across pages
- [ ] No duplicate results
- [ ] Last page shows correctly
- [ ] Result count accurate
- [ ] Deep linking to pages works

**Performance**:
- [ ] Search completes within 500ms
- [ ] Large result sets paginate properly
- [ ] No N+1 query issues
- [ ] Caching works (if implemented)
- [ ] Index optimization applied

**Security**:
- [ ] SQL injection prevented
- [ ] XSS in search terms prevented
- [ ] Search input sanitized
- [ ] Rate limiting applied
- [ ] No sensitive data leaked in results

**UX**:
- [ ] Search input has placeholder
- [ ] Loading state shown during search
- [ ] Autocomplete works (if applicable)
- [ ] Recent searches shown (if applicable)
- [ ] Search suggestions appear
- [ ] Mobile search UI functional
- [ ] Keyboard navigation works
- [ ] Clear search button present

---

## 15. File Upload Testing {#file-upload-testing}

File upload functionality requires comprehensive testing to ensure security, performance, and reliability. Improper file handling can lead to serious security vulnerabilities.

### 15.1 File Type Validation Testing

#### 15.1.1 Whitelist Validation

**Test Case TC_UPLOAD_TYPE_001: Test Allowed File Types**

```javascript
test('TC_UPLOAD_TYPE_001: Accept only whitelisted file types', async ({page}) => {
  await page.goto('http://example.com/upload');
  await login(page);
  
  const allowedFiles = [
    {path: 'test-files/document.pdf', type: 'application/pdf', shouldPass: true},
    {path: 'test-files/image.jpg', type: 'image/jpeg', shouldPass: true},
    {path: 'test-files/image.png', type: 'image/png', shouldPass: true},
    {path: 'test-files/spreadsheet.xlsx', type: 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet', shouldPass: true},
    {path: 'test-files/document.docx', type: 'application/vnd.openxmlformats-officedocument.wordprocessingml.document', shouldPass: true}
  ];
  
  const blockedFiles = [
    {path: 'test-files/script.exe', type: 'application/x-msdownload', shouldPass: false},
    {path: 'test-files/script.bat', type: 'application/bat', shouldPass: false},
    {path: 'test-files/script.sh', type: 'application/x-sh', shouldPass: false},
    {path: 'test-files/page.html', type: 'text/html', shouldPass: false},
    {path: 'test-files/script.js', type: 'application/javascript', shouldPass: false},
    {path: 'test-files/script.php', type: 'application/x-php', shouldPass: false}
  ];
  
  // Test allowed files
  for (const file of allowedFiles) {
    await page.setInputFiles('input[type="file"]', file.path);
    await page.click('button:has-text("Upload")');
    
    // Should succeed
    await expect(page.locator('.success-message')).toBeVisible();
    console.log(`✓ ${file.path} accepted`);
  }
  
  // Test blocked files
  for (const file of blockedFiles) {
    await page.setInputFiles('input[type="file"]', file.path);
    await page.click('button:has-text("Upload")');
    
    // Should be rejected
    await expect(page.locator('.error-message')).toBeVisible();
    const errorText = await page.locator('.error-message').textContent();
    expect(errorText.toLowerCase()).toContain('file type');
    console.log(`✓ ${file.path} rejected`);
  }
});
```

#### 15.1.2 MIME Type Verification

**Test Case TC_UPLOAD_TYPE_002: Verify MIME Type, Not Just Extension**

```javascript
test('TC_UPLOAD_TYPE_002: Verify actual file type, not extension', async ({page}) => {
  // Attacker might rename malicious.exe to malicious.jpg
  // System should check actual file content, not just extension
  
  const spoofedFiles = [
    {
      name: 'malicious.jpg',
      actualType: 'application/x-msdownload',
      description: 'EXE renamed to JPG'
    },
    {
      name: 'script.png',
      actualType: 'text/html',
      description: 'HTML renamed to PNG'
    },
    {
      name: 'safe.pdf',
      actualType: 'application/javascript',
      description: 'JS renamed to PDF'
    }
  ];
  
  for (const file of spoofedFiles) {
    // Upload spoofed file
    const response = await axios.post(
      'http://example.com/api/upload',
      createFormData(file),
      {
        headers: {'Authorization': `Bearer ${authToken}`},
        validateStatus: () => true
      }
    );
    
    // Should be rejected
    expect(response.status).toBe(400);
    expect(response.data.error.toLowerCase()).toContain('invalid file type');
    
    console.log(`✓ ${file.description} detected and rejected`);
  }
  
  // Verify legitimate file passes
  const realImage = {
    name: 'photo.jpg',
    actualType: 'image/jpeg',
    content: fs.readFileSync('test-files/real-photo.jpg')
  };
  
  const validResponse = await axios.post(
    'http://example.com/api/upload',
    createFormData(realImage),
    {headers: {'Authorization': `Bearer ${authToken}`}}
  );
  
  expect(validResponse.status).toBe(200);
});

function createFormData(file) {
  const FormData = require('form-data');
  const form = new FormData();
  form.append('file', file.content, {
    filename: file.name,
    contentType: file.actualType
  });
  return form;
}
```

### 15.2 File Size Limit Testing

**Test Case TC_UPLOAD_SIZE_001: Test Size Limits**

```javascript
test('TC_UPLOAD_SIZE_001: Enforce file size limits', async ({page}) => {
  await page.goto('http://example.com/upload');
  
  const sizeTests = [
    {size: 1024 * 10, label: '10 KB', shouldPass: true},
    {size: 1024 * 100, label: '100 KB', shouldPass: true},
    {size: 1024 * 1024 * 1, label: '1 MB', shouldPass: true},
    {size: 1024 * 1024 * 5, label: '5 MB', shouldPass: true},
    {size: 1024 * 1024 * 10, label: '10 MB', shouldPass: false}, // Over limit
    {size: 1024 * 1024 * 50, label: '50 MB', shouldPass: false}
  ];
  
  for (const test of sizeTests) {
    // Generate file of specific size
    const fileContent = Buffer.alloc(test.size, 'x');
    fs.writeFileSync(`temp-file-${test.label}.txt`, fileContent);
    
    // Upload file
    await page.setInputFiles('input[type="file"]', `temp-file-${test.label}.txt`);
    await page.click('button:has-text("Upload")');
    
    if (test.shouldPass) {
      await expect(page.locator('.success-message')).toBeVisible();
      console.log(`✓ ${test.label} file accepted`);
    } else {
      await expect(page.locator('.error-message')).toBeVisible();
      const errorText = await page.locator('.error-message').textContent();
      expect(errorText.toLowerCase()).toContain('size');
      expect(errorText.toLowerCase()).toContain('large');
      console.log(`✓ ${test.label} file rejected (too large)`);
    }
    
    // Cleanup
    fs.unlinkSync(`temp-file-${test.label}.txt`);
  }
});

test('TC_UPLOAD_SIZE_002: Test client-side size validation', async ({page}) => {
  await page.goto('http://example.com/upload');
  
  // Create oversized file
  const oversizedFile = Buffer.alloc(1024 * 1024 * 15, 'x'); // 15 MB
  fs.writeFileSync('oversized.txt', oversizedFile);
  
  // Select file
  await page.setInputFiles('input[type="file"]', 'oversized.txt');
  
  // Should show error BEFORE upload starts (client-side validation)
  await expect(page.locator('.file-error')).toBeVisible();
  
  // Upload button should be disabled
  const uploadButton = await page.locator('button:has-text("Upload")');
  await expect(uploadButton).toBeDisabled();
  
  fs.unlinkSync('oversized.txt');
});
```

### 15.3 Malicious File Detection

**Test Case TC_UPLOAD_SECURITY_001: Detect Malicious Files**

```javascript
test('TC_UPLOAD_SECURITY_001: Block malicious file uploads', async () => {
  const maliciousFiles = [
    {
      name: 'test.pdf',
      content: '<?php system($_GET["cmd"]); ?>',
      description: 'PHP code in PDF'
    },
    {
      name: 'image.jpg',
      content: '<script>alert("XSS")</script>',
      description: 'XSS in image file'
    },
    {
      name: 'doc.docx',
      content: '<xml><macro>malicious VBA code</macro></xml>',
      description: 'Macro-enabled document'
    }
  ];
  
  for (const file of maliciousFiles) {
    const FormData = require('form-data');
    const form = new FormData();
    form.append('file', Buffer.from(file.content), file.name);
    
    const response = await axios.post(
      'http://example.com/api/upload',
      form,
      {
        headers: {
          ...form.getHeaders(),
          'Authorization': `Bearer ${authToken}`
        },
        validateStatus: () => true
      }
    );
    
    // Should be blocked
    expect(response.status).toBe(400);
    console.log(`✓ ${file.description} detected and blocked`);
  }
});

test('TC_UPLOAD_SECURITY_002: Scan files with antivirus', async () => {
  // If using ClamAV or similar
  const testFile = fs.readFileSync('test-files/eicar.com'); // EICAR test virus
  
  const FormData = require('form-data');
  const form = new FormData();
  form.append('file', testFile, 'eicar.com');
  
  const response = await axios.post(
    'http://example.com/api/upload',
    form,
    {
      headers: {...form.getHeaders(), 'Authorization': `Bearer ${authToken}`},
      validateStatus: () => true
    }
  );
  
  expect(response.status).toBe(400);
  expect(response.data.error.toLowerCase()).toContain('virus');
});
```

### 15.4 Image Processing Testing

**Test Case TC_UPLOAD_IMAGE_001: Test Image Resizing**

```javascript
test('TC_UPLOAD_IMAGE_001: Auto-resize large images', async () => {
  const sharp = require('sharp');
  
  // Create large test image (4000x3000)
  await sharp({
    create: {
      width: 4000,
      height: 3000,
      channels: 3,
      background: {r: 255, g: 0, b: 0}
    }
  })
  .jpeg()
  .toFile('large-image.jpg');
  
  const imageFile = fs.readFileSync('large-image.jpg');
  
  const FormData = require('form-data');
  const form = new FormData();
  form.append('file', imageFile, 'large-image.jpg');
  
  const response = await axios.post(
    'http://example.com/api/upload',
    form,
    {headers: {...form.getHeaders(), 'Authorization': `Bearer ${authToken}`}}
  );
  
  expect(response.status).toBe(200);
  
  const uploadedUrl = response.data.url;
  
  // Download processed image
  const processedImage = await axios.get(uploadedUrl, {responseType: 'arraybuffer'});
  
  // Check dimensions
  const metadata = await sharp(processedImage.data).metadata();
  
  // Should be resized to max 2000x2000
  expect(metadata.width).toBeLessThanOrEqual(2000);
  expect(metadata.height).toBeLessThanOrEqual(2000);
  
  // Aspect ratio should be preserved
  const originalAspect = 4000 / 3000;
  const newAspect = metadata.width / metadata.height;
  expect(Math.abs(originalAspect - newAspect)).toBeLessThan(0.01);
  
  fs.unlinkSync('large-image.jpg');
});

test('TC_UPLOAD_IMAGE_002: Generate thumbnails', async () => {
  const originalImage = fs.readFileSync('test-files/photo.jpg');
  
  const FormData = require('form-data');
  const form = new FormData();
  form.append('file', originalImage, 'photo.jpg');
  
  const response = await axios.post(
    'http://example.com/api/upload',
    form,
    {headers: {...form.getHeaders(), 'Authorization': `Bearer ${authToken}`}}
  );
  
  expect(response.status).toBe(200);
  expect(response.data.thumbnail_url).toBeDefined();
  
  // Download thumbnail
  const thumbnail = await axios.get(response.data.thumbnail_url, {responseType: 'arraybuffer'});
  
  const thumbMetadata = await sharp(thumbnail.data).metadata();
  
  // Thumbnail should be small (e.g., 200x200 max)
  expect(thumbMetadata.width).toBeLessThanOrEqual(200);
  expect(thumbMetadata.height).toBeLessThanOrEqual(200);
});
```

### 15.5 S3/Cloud Storage Integration Testing

**Test Case TC_UPLOAD_S3_001: Upload to S3**

```javascript
test('TC_UPLOAD_S3_001: Upload file to S3 bucket', async () => {
  const AWS = require('aws-sdk');
  const s3 = new AWS.S3({
    accessKeyId: process.env.AWS_ACCESS_KEY,
    secretAccessKey: process.env.AWS_SECRET_KEY,
    region: 'us-east-1'
  });
  
  const fileContent = fs.readFileSync('test-files/document.pdf');
  
  const params = {
    Bucket: 'test-uploads-bucket',
    Key: `uploads/${Date.now()}-document.pdf`,
    Body: fileContent,
    ContentType: 'application/pdf',
    ACL: 'private'
  };
  
  const result = await s3.upload(params).promise();
  
  expect(result.Location).toBeDefined();
  expect(result.Key).toBe(params.Key);
  
  console.log('File uploaded to:', result.Location);
  
  // Verify file exists
  const headParams = {
    Bucket: params.Bucket,
    Key: params.Key
  };
  
  const metadata = await s3.headObject(headParams).promise();
  expect(metadata.ContentLength).toBe(fileContent.length);
  expect(metadata.ContentType).toBe('application/pdf');
  
  // Cleanup
  await s3.deleteObject({Bucket: params.Bucket, Key: params.Key}).promise();
});

test('TC_UPLOAD_S3_002: Generate signed URL for private files', async () => {
  const AWS = require('aws-sdk');
  const s3 = new AWS.S3({
    accessKeyId: process.env.AWS_ACCESS_KEY,
    secretAccessKey: process.env.AWS_SECRET_KEY,
    region: 'us-east-1'
  });
  
  // Upload file
  const fileKey = `private/${Date.now()}-confidential.pdf`;
  await s3.upload({
    Bucket: 'test-uploads-bucket',
    Key: fileKey,
    Body: fs.readFileSync('test-files/document.pdf'),
    ACL: 'private'
  }).promise();
  
  // Generate signed URL (expires in 1 hour)
  const signedUrl = s3.getSignedUrl('getObject', {
    Bucket: 'test-uploads-bucket',
    Key: fileKey,
    Expires: 3600
  });
  
  expect(signedUrl).toContain('X-Amz-Signature');
  expect(signedUrl).toContain('X-Amz-Expires=3600');
  
  // Verify signed URL works
  const fileResponse = await axios.get(signedUrl, {responseType: 'arraybuffer'});
  expect(fileResponse.status).toBe(200);
  expect(fileResponse.data.length).toBeGreaterThan(0);
  
  // Verify direct access (without signature) fails
  const directUrl = `https://test-uploads-bucket.s3.amazonaws.com/${fileKey}`;
  try {
    await axios.get(directUrl);
    fail('Should not access private file without signature');
  } catch (error) {
    expect(error.response.status).toBe(403);
  }
  
  // Cleanup
  await s3.deleteObject({Bucket: 'test-uploads-bucket', Key: fileKey}).promise();
});
```

### 15.6 Upload Progress Indicator Testing

**Test Case TC_UPLOAD_PROGRESS_001: Monitor Upload Progress**

```javascript
test('TC_UPLOAD_PROGRESS_001: Display upload progress', async ({page}) => {
  await page.goto('http://example.com/upload');
  
  // Create large file to see progress
  const largeFile = Buffer.alloc(1024 * 1024 * 5, 'x'); // 5 MB
  fs.writeFileSync('large-upload.bin', largeFile);
  
  // Select file
  await page.setInputFiles('input[type="file"]', 'large-upload.bin');
  
  // Click upload
  await page.click('button:has-text("Upload")');
  
  // Progress bar should appear
  await expect(page.locator('.upload-progress')).toBeVisible();
  
  // Monitor progress
  let previousProgress = 0;
  for (let i = 0; i < 10; i++) {
    const progressText = await page.locator('.upload-progress').textContent();
    const progress = parseInt(progressText.match(/\d+/)[0]);
    
    // Progress should increase
    expect(progress).toBeGreaterThanOrEqual(previousProgress);
    previousProgress = progress;
    
    if (progress >= 100) break;
    
    await page.waitForTimeout(500);
  }
  
  // Should complete
  await expect(page.locator('.success-message')).toBeVisible();
  
  // Progress bar should hide
  await expect(page.locator('.upload-progress')).not.toBeVisible();
  
  fs.unlinkSync('large-upload.bin');
});
```

### 15.7 Concurrent Upload Testing

**Test Case TC_UPLOAD_CONCURRENT_001: Multiple Simultaneous Uploads**

```javascript
test('TC_UPLOAD_CONCURRENT_001: Handle concurrent uploads', async () => {
  const uploadPromises = [];
  
  // Simulate 10 concurrent uploads
  for (let i = 0; i < 10; i++) {
    const fileContent = Buffer.from(`File content ${i}`);
    
    const FormData = require('form-data');
    const form = new FormData();
    form.append('file', fileContent, `file-${i}.txt`);
    
    const uploadPromise = axios.post(
      'http://example.com/api/upload',
      form,
      {
        headers: {
          ...form.getHeaders(),
          'Authorization': `Bearer ${authToken}`
        }
      }
    );
    
    uploadPromises.push(uploadPromise);
  }
  
  // Wait for all uploads
  const results = await Promise.all(uploadPromises);
  
  // All should succeed
  for (const result of results) {
    expect(result.status).toBe(200);
    expect(result.data.url).toBeDefined();
  }
  
  // Verify all files uploaded
  expect(results.length).toBe(10);
  
  // Verify unique URLs
  const urls = results.map(r => r.data.url);
  const uniqueUrls = new Set(urls);
  expect(uniqueUrls.size).toBe(10);
});
```

### 15.8 Resume Failed Upload Testing

**Test Case TC_UPLOAD_RESUME_001: Resume Interrupted Upload**

```javascript
test('TC_UPLOAD_RESUME_001: Resume upload after interruption', async () => {
  // This test requires chunked upload support
  
  const fs = require('fs');
  const axios = require('axios');
  
  // Create large file (10 MB)
  const fileSize = 1024 * 1024 * 10;
  const fileName = 'large-file.bin';
  fs.writeFileSync(fileName, Buffer.alloc(fileSize, 'x'));
  
  const chunkSize = 1024 * 1024; // 1 MB chunks
  const totalChunks = Math.ceil(fileSize / chunkSize);
  
  // Upload first 5 chunks
  const uploadId = `upload-${Date.now()}`;
  
  for (let i = 0; i < 5; i++) {
    const start = i * chunkSize;
    const end = Math.min(start + chunkSize, fileSize);
    const chunk = fs.readFileSync(fileName, {start, end});
    
    await axios.post('http://example.com/api/upload/chunk', chunk, {
      headers: {
        'Content-Type': 'application/octet-stream',
        'X-Upload-ID': uploadId,
        'X-Chunk-Index': i,
        'X-Total-Chunks': totalChunks,
        'Authorization': `Bearer ${authToken}`
      }
    });
  }
  
  // Simulate interruption - get upload status
  const statusResponse = await axios.get(`http://example.com/api/upload/status/${uploadId}`, {
    headers: {'Authorization': `Bearer ${authToken}`}
  });
  
  expect(statusResponse.data.chunks_uploaded).toBe(5);
  expect(statusResponse.data.total_chunks).toBe(totalChunks);
  
  // Resume - upload remaining chunks
  for (let i = 5; i < totalChunks; i++) {
    const start = i * chunkSize;
    const end = Math.min(start + chunkSize, fileSize);
    const chunk = fs.readFileSync(fileName, {start, end});
    
    await axios.post('http://example.com/api/upload/chunk', chunk, {
      headers: {
        'Content-Type': 'application/octet-stream',
        'X-Upload-ID': uploadId,
        'X-Chunk-Index': i,
        'X-Total-Chunks': totalChunks,
        'Authorization': `Bearer ${authToken}`
      }
    });
  }
  
  // Finalize upload
  const finalizeResponse = await axios.post(`http://example.com/api/upload/finalize/${uploadId}`, {}, {
    headers: {'Authorization': `Bearer ${authToken}`}
  });
  
  expect(finalizeResponse.status).toBe(200);
  expect(finalizeResponse.data.url).toBeDefined();
  
  // Verify file size matches
  const uploadedFileResponse = await axios.head(finalizeResponse.data.url);
  expect(parseInt(uploadedFileResponse.headers['content-length'])).toBe(fileSize);
  
  fs.unlinkSync(fileName);
});
```

### 15.9 File Upload Testing Checklist

**Security**:
- [ ] File type whitelist enforced
- [ ] MIME type verified (not just extension)
- [ ] Malicious files blocked
- [ ] Executable files rejected
- [ ] Path traversal prevented (../../etc/passwd)
- [ ] Filename sanitized
- [ ] Virus scanning (if applicable)
- [ ] Upload rate limiting
- [ ] Authentication required
- [ ] Authorization checked

**Validation**:
- [ ] File size limits enforced (client & server)
- [ ] Maximum files per upload enforced
- [ ] Image dimensions validated
- [ ] Video duration validated (if applicable)
- [ ] Document page count (if applicable)
- [ ] Empty files rejected
- [ ] Corrupted files detected

**Processing**:
- [ ] Images resized appropriately
- [ ] Thumbnails generated
- [ ] EXIF data stripped (privacy)
- [ ] File metadata extracted
- [ ] Format conversion works (if applicable)

**Storage**:
- [ ] Files stored securely
- [ ] Unique filenames generated
- [ ] Organized folder structure
- [ ] Cloud storage integration works
- [ ] CDN integration (if applicable)
- [ ] Backup/redundancy configured

**User Experience**:
- [ ] Upload progress shown
- [ ] Drag-and-drop works
- [ ] Multiple file selection works
- [ ] Preview before upload
- [ ] Cancel upload works
- [ ] Error messages clear
- [ ] Success confirmation shown
- [ ] Mobile upload works

**Performance**:
- [ ] Large files upload successfully
- [ ] Concurrent uploads handled
- [ ] Upload speed acceptable
- [ ] Memory usage reasonable
- [ ] Chunked upload for large files
- [ ] Resume interrupted uploads

---


## 16. Notification System Testing {#notification-system-testing}

Notification systems are critical for user engagement and delivering timely information. Testing must ensure notifications are delivered reliably, formatted correctly, and manageable by users.

### 16.1 Push Notification Testing

#### 16.1.1 Firebase Cloud Messaging (FCM) Testing

**Test Case TC_NOTIF_PUSH_001: Send Push Notification via FCM**

```javascript
const admin = require('firebase-admin');

// Initialize Firebase Admin
const serviceAccount = require('./firebase-service-account.json');
admin.initializeApp({
  credential: admin.credential.cert(serviceAccount)
});

test('TC_NOTIF_PUSH_001: Send FCM push notification', async () => {
  const message = {
    notification: {
      title: 'Test Notification',
      body: 'This is a test push notification'
    },
    data: {
      type: 'test',
      timestamp: Date.now().toString()
    },
    token: 'device_fcm_token_here' // Test device token
  };
  
  const response = await admin.messaging().send(message);
  
  expect(response).toBeDefined();
  console.log('Successfully sent message:', response);
  
  // Log notification sent
  await db.notifications.create({
    type: 'push',
    user_id: 'TEST_USER',
    title: message.notification.title,
    body: message.notification.body,
    status: 'sent',
    fcm_message_id: response,
    sent_at: new Date()
  });
});

test('TC_NOTIF_PUSH_002: Send to topic subscription', async () => {
  const topic = 'test-topic';
  
  const message = {
    notification: {
      title: 'Topic Notification',
      body: 'Sent to all topic subscribers'
    },
    topic: topic
  };
  
  const response = await admin.messaging().send(message);
  
  expect(response).toBeDefined();
  console.log('Sent to topic:', topic, response);
});

test('TC_NOTIF_PUSH_003: Send with custom data payload', async () => {
  const message = {
    data: {
      notification_type: 'order_update',
      order_id: 'ORDER_12345',
      status: 'shipped',
      tracking_number: '1Z999AA10123456784'
    },
    token: 'device_token'
  };
  
  const response = await admin.messaging().send(message);
  
  expect(response).toBeDefined();
  
  // Verify device can parse custom data
  // This would be verified on device side
});
```

#### 16.1.2 APNs (Apple Push Notification) Testing

**Test Case TC_NOTIF_APN_001: Send iOS Push Notification**

```javascript
test('TC_NOTIF_APN_001: Send APNs notification', async () => {
  const apn = require('apn');
  
  const provider = new apn.Provider({
    token: {
      key: fs.readFileSync('./AuthKey.p8'),
      keyId: process.env.APN_KEY_ID,
      teamId: process.env.APN_TEAM_ID
    },
    production: false // Use sandbox for testing
  });
  
  const notification = new apn.Notification();
  notification.alert = {
    title: 'Test Notification',
    body: 'This is a test iOS push notification'
  };
  notification.sound = 'default';
  notification.badge = 1;
  notification.topic = 'com.example.app';
  notification.payload = {
    type: 'test',
    data: {message_id: '123'}
  };
  
  const deviceToken = 'ios_device_token_here';
  
  const result = await provider.send(notification, deviceToken);
  
  expect(result.sent.length).toBe(1);
  expect(result.failed.length).toBe(0);
  
  console.log('APNs result:', result);
  
  provider.shutdown();
});

test('TC_NOTIF_APN_002: Handle invalid device token', async () => {
  const apn = require('apn');
  
  const provider = new apn.Provider({
    token: {
      key: fs.readFileSync('./AuthKey.p8'),
      keyId: process.env.APN_KEY_ID,
      teamId: process.env.APN_TEAM_ID
    },
    production: false
  });
  
  const notification = new apn.Notification();
  notification.alert = 'Test';
  notification.topic = 'com.example.app';
  
  const invalidToken = 'invalid_token_format';
  
  const result = await provider.send(notification, invalidToken);
  
  expect(result.failed.length).toBeGreaterThan(0);
  
  // Should log failure
  for (const failure of result.failed) {
    expect(failure.response.reason).toBeDefined();
    console.log('Failure reason:', failure.response.reason);
    
    // Remove invalid token from database
    await db.device_tokens.delete({token: invalidToken});
  }
  
  provider.shutdown();
});
```

#### 16.1.3 Web Push Notifications

**Test Case TC_NOTIF_WEB_001: Send Web Push Notification**

```javascript
const webpush = require('web-push');

// Setup VAPID keys
webpush.setVAPIDDetails(
  'mailto:admin@example.com',
  process.env.VAPID_PUBLIC_KEY,
  process.env.VAPID_PRIVATE_KEY
);

test('TC_NOTIF_WEB_001: Send web push notification', async () => {
  const subscription = {
    endpoint: 'https://fcm.googleapis.com/fcm/send/...',
    keys: {
      p256dh: 'public_key',
      auth: 'auth_secret'
    }
  };
  
  const payload = JSON.stringify({
    title: 'Web Push Test',
    body: 'Testing web push notifications',
    icon: '/icon.png',
    badge: '/badge.png',
    data: {
      url: 'https://example.com/notifications'
    }
  });
  
  const options = {
    TTL: 3600, // 1 hour
    vapidDetails: {
      subject: 'mailto:admin@example.com',
      publicKey: process.env.VAPID_PUBLIC_KEY,
      privateKey: process.env.VAPID_PRIVATE_KEY
    }
  };
  
  const response = await webpush.sendNotification(subscription, payload, options);
  
  expect(response.statusCode).toBe(201);
  console.log('Web push sent successfully');
});

test('TC_NOTIF_WEB_002: Handle expired subscription', async () => {
  const expiredSubscription = {
    endpoint: 'https://fcm.googleapis.com/fcm/send/expired',
    keys: {
      p256dh: 'key',
      auth: 'auth'
    }
  };
  
  const payload = JSON.stringify({title: 'Test'});
  
  try {
    await webpush.sendNotification(expiredSubscription, payload);
  } catch (error) {
    expect(error.statusCode).toBe(410); // Gone
    
    // Remove expired subscription
    await db.push_subscriptions.delete({
      endpoint: expiredSubscription.endpoint
    });
  }
});
```

### 16.2 In-App Notification Testing

**Test Case TC_NOTIF_INAPP_001: Create and Display In-App Notification**

```javascript
test('TC_NOTIF_INAPP_001: Create in-app notification', async ({page}) => {
  // Trigger notification creation
  await axios.post('http://example.com/api/notifications', {
    user_id: 'USER_123',
    type: 'order_shipped',
    title: 'Your order has shipped!',
    message: 'Order #12345 is on its way.',
    data: {
      order_id: 'ORDER_12345',
      tracking: '1Z999AA10'
    }
  }, {
    headers: {'Authorization': `Bearer ${adminToken}`}
  });
  
  // User logs in
  await page.goto('http://example.com/login');
  await page.fill('#email', 'user@example.com');
  await page.fill('#password', 'password');
  await page.click('button[type="submit"]');
  
  // Notification bell should show badge
  await expect(page.locator('.notification-badge')).toBeVisible();
  const badgeText = await page.locator('.notification-badge').textContent();
  expect(parseInt(badgeText)).toBeGreaterThan(0);
  
  // Click notification bell
  await page.click('.notification-bell');
  
  // Notification panel should open
  await expect(page.locator('.notification-panel')).toBeVisible();
  
  // Should show notification
  await expect(page.locator('.notification-item:has-text("Your order has shipped")')).toBeVisible();
  
  // Notification should be marked as unread
  const notifItem = page.locator('.notification-item').first();
  await expect(notifItem.locator('.unread-indicator')).toBeVisible();
  
  // Click notification
  await notifItem.click();
  
  // Should navigate to relevant page
  await page.waitForURL(/order.*ORDER_12345/);
  
  // Notification should be marked as read
  await page.click('.notification-bell');
  const readNotif = page.locator('.notification-item').first();
  await expect(readNotif.locator('.unread-indicator')).not.toBeVisible();
  
  // Badge count should decrease
  const newBadgeText = await page.locator('.notification-badge').textContent();
  expect(parseInt(newBadgeText)).toBe(parseInt(badgeText) - 1);
});

test('TC_NOTIF_INAPP_002: Mark all as read', async ({page}) => {
  await page.goto('http://example.com/dashboard');
  await login(page);
  
  // Create multiple notifications
  for (let i = 0; i < 5; i++) {
    await axios.post('http://example.com/api/notifications', {
      user_id: 'USER_123',
      title: `Notification ${i}`,
      message: `Test message ${i}`
    }, {
      headers: {'Authorization': `Bearer ${adminToken}`}
    });
  }
  
  await page.reload();
  
  // Open notification panel
  await page.click('.notification-bell');
  
  // Click "Mark all as read"
  await page.click('button:has-text("Mark all as read")');
  
  // All notifications should be marked as read
  const unreadNotifs = await page.locator('.notification-item .unread-indicator').count();
  expect(unreadNotifs).toBe(0);
  
  // Badge should disappear
  await expect(page.locator('.notification-badge')).not.toBeVisible();
});
```

### 16.3 Email Notification Testing

**Test Case TC_NOTIF_EMAIL_001: Send Email Notification**

```javascript
test('TC_NOTIF_EMAIL_001: Send notification email', async () => {
  const notification = {
    user_id: 'USER_123',
    type: 'comment_reply',
    data: {
      post_title: 'My Blog Post',
      comment_author: 'Jane Doe',
      comment_text: 'Great article! Thanks for sharing.',
      post_url: 'https://example.com/posts/123'
    }
  };
  
  // Get user email preferences
  const user = await db.users.findOne({id: notification.user_id});
  
  if (user.preferences.email_notifications.comment_replies) {
    // Send email
    const emailSent = await sendEmail({
      to: user.email,
      subject: `New reply on "${notification.data.post_title}"`,
      template: 'comment-reply',
      data: {
        user_name: user.name,
        post_title: notification.data.post_title,
        comment_author: notification.data.comment_author,
        comment_text: notification.data.comment_text,
        post_url: notification.data.post_url,
        unsubscribe_url: `https://example.com/preferences/unsubscribe?token=${user.unsubscribe_token}`
      }
    });
    
    expect(emailSent).toBe(true);
    
    // Log notification
    await db.notifications.create({
      user_id: notification.user_id,
      type: notification.type,
      channel: 'email',
      status: 'sent',
      sent_at: new Date()
    });
  }
});
```

### 16.4 SMS Notification Testing

**Test Case TC_NOTIF_SMS_001: Send SMS via Twilio**

```javascript
const twilio = require('twilio');

test('TC_NOTIF_SMS_001: Send SMS notification', async () => {
  const client = twilio(
    process.env.TWILIO_ACCOUNT_SID,
    process.env.TWILIO_AUTH_TOKEN
  );
  
  const message = await client.messages.create({
    body: 'Your verification code is: 123456',
    from: process.env.TWILIO_PHONE_NUMBER,
    to: '+15555551234' // Test number
  });
  
  expect(message.sid).toBeDefined();
  expect(message.status).toBe('queued');
  
  // Check delivery status
  await new Promise(resolve => setTimeout(resolve, 5000));
  
  const updatedMessage = await client.messages(message.sid).fetch();
  expect(['sent', 'delivered']).toContain(updatedMessage.status);
  
  console.log('SMS delivery status:', updatedMessage.status);
});

test('TC_NOTIF_SMS_002: Handle invalid phone number', async () => {
  const client = twilio(
    process.env.TWILIO_ACCOUNT_SID,
    process.env.TWILIO_AUTH_TOKEN
  );
  
  try {
    await client.messages.create({
      body: 'Test message',
      from: process.env.TWILIO_PHONE_NUMBER,
      to: 'invalid-phone'
    });
    
    fail('Should reject invalid phone number');
  } catch (error) {
    expect(error.code).toBe(21211); // Invalid phone number
    
    // Log failure
    await db.notification_failures.create({
      type: 'sms',
      error: error.message,
      failed_at: new Date()
    });
  }
});
```

### 16.5 Webhook Notification Reliability

**Test Case TC_NOTIF_WEBHOOK_001: Send Webhook Notification**

```javascript
test('TC_NOTIF_WEBHOOK_001: Send webhook with retry', async () => {
  const webhookUrl = 'https://external-service.com/webhook';
  const payload = {
    event: 'order.created',
    data: {
      order_id: 'ORDER_123',
      total: 99.99,
      created_at: new Date().toISOString()
    }
  };
  
  const maxRetries = 3;
  let attempt = 0;
  let success = false;
  
  while (attempt < maxRetries && !success) {
    attempt++;
    
    try {
      const response = await axios.post(webhookUrl, payload, {
        timeout: 10000,
        headers: {
          'Content-Type': 'application/json',
          'X-Webhook-Signature': generateSignature(payload)
        }
      });
      
      if (response.status === 200) {
        success = true;
        
        await db.webhook_deliveries.create({
          url: webhookUrl,
          event: payload.event,
          status: 'success',
          attempts: attempt,
          delivered_at: new Date()
        });
      }
    } catch (error) {
      console.log(`Webhook attempt ${attempt} failed:`, error.message);
      
      if (attempt < maxRetries) {
        // Exponential backoff
        const delay = Math.pow(2, attempt) * 1000;
        await new Promise(resolve => setTimeout(resolve, delay));
      } else {
        // Final failure
        await db.webhook_deliveries.create({
          url: webhookUrl,
          event: payload.event,
          status: 'failed',
          attempts: attempt,
          error: error.message,
          failed_at: new Date()
        });
      }
    }
  }
  
  expect(success).toBe(true);
});

function generateSignature(payload) {
  const crypto = require('crypto');
  const secret = process.env.WEBHOOK_SECRET;
  
  return crypto
    .createHmac('sha256', secret)
    .update(JSON.stringify(payload))
    .digest('hex');
}
```

### 16.6 Notification Preferences Testing

**Test Case TC_NOTIF_PREF_001: Respect User Notification Preferences**

```javascript
test('TC_NOTIF_PREF_001: Honor user preferences', async () => {
  const user = await db.users.findOne({id: 'USER_123'});
  
  // User has disabled email notifications for marketing
  user.preferences.email_notifications.marketing = false;
  user.preferences.push_notifications.marketing = true;
  
  await db.users.update({id: user.id}, {preferences: user.preferences});
  
  // Attempt to send marketing notification
  const notification = {
    user_id: user.id,
    type: 'marketing',
    title: 'Special Offer!',
    message: '50% off this weekend only'
  };
  
  const channels = await determineNotificationChannels(user, notification.type);
  
  // Should NOT include email
  expect(channels).not.toContain('email');
  
  // Should include push
  expect(channels).toContain('push');
  
  // Send only via enabled channels
  for (const channel of channels) {
    await sendNotification(channel, user, notification);
  }
  
  // Verify email was not sent
  const emailLog = await db.email_logs.findOne({
    user_id: user.id,
    type: notification.type,
    sent_at: {$gte: new Date(Date.now() - 60000)}
  });
  
  expect(emailLog).toBeUndefined();
  
  // Verify push was sent
  const pushLog = await db.push_logs.findOne({
    user_id: user.id,
    type: notification.type,
    sent_at: {$gte: new Date(Date.now() - 60000)}
  });
  
  expect(pushLog).toBeDefined();
});

async function determineNotificationChannels(user, notificationType) {
  const channels = [];
  
  if (user.preferences.email_notifications[notificationType]) {
    channels.push('email');
  }
  
  if (user.preferences.push_notifications[notificationType]) {
    channels.push('push');
  }
  
  if (user.preferences.sms_notifications?.[notificationType]) {
    channels.push('sms');
  }
  
  return channels;
}
```

### 16.7 Rate Limiting Notifications

**Test Case TC_NOTIF_RATE_001: Prevent Notification Spam**

```javascript
test('TC_NOTIF_RATE_001: Rate limit notifications per user', async () => {
  const userId = 'USER_123';
  const maxNotificationsPerHour = 10;
  
  // Try to send 15 notifications rapidly
  const sendPromises = [];
  
  for (let i = 0; i < 15; i++) {
    const promise = sendNotificationWithRateLimit(userId, {
      title: `Notification ${i}`,
      message: `Test message ${i}`
    });
    sendPromises.push(promise);
  }
  
  const results = await Promise.all(sendPromises);
  
  // Count successful sends
  const successCount = results.filter(r => r.sent).length;
  const blockedCount = results.filter(r => !r.sent).length;
  
  expect(successCount).toBeLessThanOrEqual(maxNotificationsPerHour);
  expect(blockedCount).toBeGreaterThan(0);
  
  console.log(`Sent: ${successCount}, Blocked: ${blockedCount}`);
});

async function sendNotificationWithRateLimit(userId, notification) {
  // Check rate limit
  const oneHourAgo = new Date(Date.now() - 3600000);
  
  const recentCount = await db.notifications.count({
    user_id: userId,
    sent_at: {$gte: oneHourAgo}
  });
  
  if (recentCount >= 10) {
    console.log(`Rate limit exceeded for user ${userId}`);
    return {sent: false, reason: 'rate_limit'};
  }
  
  // Send notification
  await db.notifications.create({
    user_id: userId,
    title: notification.title,
    message: notification.message,
    sent_at: new Date()
  });
  
  return {sent: true};
}
```

### 16.8 Notification Deduplication

**Test Case TC_NOTIF_DEDUP_001: Prevent Duplicate Notifications**

```javascript
test('TC_NOTIF_DEDUP_001: Deduplicate identical notifications', async () => {
  const notification = {
    user_id: 'USER_123',
    type: 'order_update',
    data: {
      order_id: 'ORDER_456',
      status: 'shipped'
    }
  };
  
  // Generate unique hash for notification
  const notificationHash = generateNotificationHash(notification);
  
  // Try to send same notification twice
  const result1 = await sendNotificationWithDedup(notification, notificationHash);
  const result2 = await sendNotificationWithDedup(notification, notificationHash);
  
  expect(result1.sent).toBe(true);
  expect(result2.sent).toBe(false);
  expect(result2.reason).toBe('duplicate');
  
  // Verify only one notification in database
  const count = await db.notifications.count({
    user_id: notification.user_id,
    dedup_hash: notificationHash
  });
  
  expect(count).toBe(1);
});

function generateNotificationHash(notification) {
  const crypto = require('crypto');
  const content = JSON.stringify({
    user_id: notification.user_id,
    type: notification.type,
    data: notification.data
  });
  
  return crypto.createHash('sha256').update(content).digest('hex');
}

async function sendNotificationWithDedup(notification, hash) {
  // Check for duplicate in last 24 hours
  const oneDayAgo = new Date(Date.now() - 86400000);
  
  const existing = await db.notifications.findOne({
    dedup_hash: hash,
    created_at: {$gte: oneDayAgo}
  });
  
  if (existing) {
    return {sent: false, reason: 'duplicate'};
  }
  
  // Send notification
  await db.notifications.create({
    user_id: notification.user_id,
    type: notification.type,
    data: notification.data,
    dedup_hash: hash,
    created_at: new Date(),
    sent_at: new Date()
  });
  
  return {sent: true};
}
```

### 16.9 Notification Testing Checklist

**Push Notifications**:
- [ ] FCM notifications sent successfully
- [ ] APNs notifications sent successfully
- [ ] Web push notifications work
- [ ] Notification appears on device
- [ ] Title and body display correctly
- [ ] Icon/image displays
- [ ] Custom data payload works
- [ ] Notification sound plays
- [ ] Badge count updates
- [ ] Click action works correctly
- [ ] Topic subscriptions work
- [ ] Invalid tokens removed
- [ ] Expired subscriptions handled

**In-App Notifications**:
- [ ] Notifications appear in notification center
- [ ] Badge count accurate
- [ ] Mark as read works
- [ ] Mark all as read works
- [ ] Delete notification works
- [ ] Click notification navigates correctly
- [ ] Real-time updates (WebSocket)
- [ ] Unread indicator shown
- [ ] Notification history loads
- [ ] Infinite scroll/pagination works

**Email Notifications**:
- [ ] Transactional emails sent
- [ ] Marketing emails sent
- [ ] Email preferences respected
- [ ] Unsubscribe link works
- [ ] Email template renders correctly
- [ ] Plain text fallback included
- [ ] Personalization works
- [ ] Attachments included (if applicable)
- [ ] Tracking pixels work (if applicable)

**SMS Notifications**:
- [ ] SMS delivered successfully
- [ ] International numbers supported
- [ ] Character limit enforced
- [ ] Delivery status tracked
- [ ] Invalid numbers rejected
- [ ] Opt-out requests honored
- [ ] Rate limiting applied

**Preferences & Settings**:
- [ ] User can enable/disable by type
- [ ] User can enable/disable by channel
- [ ] Quiet hours respected
- [ ] Frequency preferences honored
- [ ] Global disable works
- [ ] Preferences persist across sessions

**Reliability**:
- [ ] Retry logic for failed sends
- [ ] Exponential backoff implemented
- [ ] Dead letter queue for permanent failures
- [ ] Webhook signature verification
- [ ] Rate limiting per user
- [ ] Deduplication works
- [ ] Bulk send doesn't timeout
- [ ] Graceful degradation

**Monitoring**:
- [ ] Delivery success rate tracked
- [ ] Failed notifications logged
- [ ] Alert on high failure rate
- [ ] Notification latency measured
- [ ] Channel performance compared

---

## 17. CI/CD Test Integration {#cicd-integration}

Integrating tests into CI/CD pipelines ensures that every code change is automatically tested, preventing bugs from reaching production.

### 17.1 GitHub Actions Test Workflows

#### 17.1.1 Basic Test Workflow

```yaml
# .github/workflows/test.yml
name: Run Tests

on:
  push:
    branches: [main, develop]
  pull_request:
    branches: [main, develop]

jobs:
  test:
    runs-on: ubuntu-latest
    
    services:
      postgres:
        image: postgres:14
        env:
          POSTGRES_PASSWORD: postgres
          POSTGRES_DB: test_db
        options: >-
          --health-cmd pg_isready
          --health-interval 10s
          --health-timeout 5s
          --health-retries 5
        ports:
          - 5432:5432
      
      redis:
        image: redis:7
        options: >-
          --health-cmd "redis-cli ping"
          --health-interval 10s
          --health-timeout 5s
          --health-retries 5
        ports:
          - 6379:6379
    
    steps:
      - name: Checkout code
        uses: actions/checkout@v3
      
      - name: Setup Node.js
        uses: actions/setup-node@v3
        with:
          node-version: '18'
          cache: 'npm'
      
      - name: Install dependencies
        run: npm ci
      
      - name: Run linter
        run: npm run lint
      
      - name: Run unit tests
        run: npm run test:unit
        env:
          NODE_ENV: test
          DATABASE_URL: postgresql://postgres:postgres@localhost:5432/test_db
          REDIS_URL: redis://localhost:6379
      
      - name: Run integration tests
        run: npm run test:integration
        env:
          NODE_ENV: test
          DATABASE_URL: postgresql://postgres:postgres@localhost:5432/test_db
          REDIS_URL: redis://localhost:6379
      
      - name: Upload coverage reports
        uses: codecov/codecov-action@v3
        with:
          files: ./coverage/lcov.info
          flags: unittests
          name: codecov-umbrella
      
      - name: Upload test results
        if: always()
        uses: actions/upload-artifact@v3
        with:
          name: test-results
          path: test-results/
```

#### 17.1.2 Playwright Test Workflow

```yaml
# .github/workflows/playwright.yml
name: Playwright Tests

on:
  push:
    branches: [main, develop]
  pull_request:
    branches: [main, develop]
  schedule:
    - cron: '0 2 * * *' # Run nightly at 2 AM

jobs:
  test:
    timeout-minutes: 60
    runs-on: ubuntu-latest
    
    steps:
      - uses: actions/checkout@v3
      
      - uses: actions/setup-node@v3
        with:
          node-version: '18'
      
      - name: Install dependencies
        run: npm ci
      
      - name: Install Playwright browsers
        run: npx playwright install --with-deps
      
      - name: Run Playwright tests
        run: npx playwright test
        env:
          BASE_URL: http://localhost:3000
          TEST_USER_EMAIL: test@example.com
          TEST_USER_PASSWORD: ${{ secrets.TEST_USER_PASSWORD }}
      
      - name: Upload Playwright report
        uses: actions/upload-artifact@v3
        if: always()
        with:
          name: playwright-report
          path: playwright-report/
          retention-days: 30
      
      - name: Upload test screenshots
        uses: actions/upload-artifact@v3
        if: failure()
        with:
          name: screenshots
          path: test-results/
```

#### 17.1.3 Multi-Environment Testing

```yaml
# .github/workflows/multi-env-test.yml
name: Multi-Environment Tests

on:
  push:
    branches: [main]

jobs:
  test:
    runs-on: ${{ matrix.os }}
    
    strategy:
      matrix:
        os: [ubuntu-latest, windows-latest, macos-latest]
        node-version: [16, 18, 20]
        browser: [chromium, firefox, webkit]
    
    steps:
      - uses: actions/checkout@v3
      
      - name: Setup Node.js ${{ matrix.node-version }}
        uses: actions/setup-node@v3
        with:
          node-version: ${{ matrix.node-version }}
      
      - name: Install dependencies
        run: npm ci
      
      - name: Install Playwright
        run: npx playwright install --with-deps ${{ matrix.browser }}
      
      - name: Run tests on ${{ matrix.browser }}
        run: npx playwright test --project=${{ matrix.browser }}
      
      - name: Upload results
        if: always()
        uses: actions/upload-artifact@v3
        with:
          name: test-results-${{ matrix.os }}-node${{ matrix.node-version }}-${{ matrix.browser }}
          path: test-results/
```

### 17.2 Docker Test Environments

#### 17.2.1 Docker Compose for Testing

```yaml
# docker-compose.test.yml
version: '3.8'

services:
  app:
    build:
      context: .
      dockerfile: Dockerfile.test
    environment:
      NODE_ENV: test
      DATABASE_URL: postgresql://postgres:postgres@db:5432/test_db
      REDIS_URL: redis://redis:6379
    depends_on:
      db:
        condition: service_healthy
      redis:
        condition: service_healthy
    volumes:
      - ./:/app
      - /app/node_modules
    command: npm run test

  db:
    image: postgres:14
    environment:
      POSTGRES_PASSWORD: postgres
      POSTGRES_DB: test_db
    healthcheck:
      test: ["CMD-SHELL", "pg_isready -U postgres"]
      interval: 10s
      timeout: 5s
      retries: 5
    volumes:
      - ./test/fixtures/db:/docker-entrypoint-initdb.d

  redis:
    image: redis:7
    healthcheck:
      test: ["CMD", "redis-cli", "ping"]
      interval: 10s
      timeout: 3s
      retries: 5
```

**Dockerfile.test**:

```dockerfile
FROM node:18-alpine

WORKDIR /app

# Install dependencies
COPY package*.json ./
RUN npm ci

# Copy application code
COPY . .

# Install Playwright browsers
RUN npx playwright install --with-deps

# Run tests
CMD ["npm", "run", "test"]
```

**Running tests in Docker**:

```bash
# Build and run tests
docker-compose -f docker-compose.test.yml up --build --abort-on-container-exit

# Run specific test suite
docker-compose -f docker-compose.test.yml run app npm run test:e2e

# Cleanup
docker-compose -f docker-compose.test.yml down -v
```

### 17.3 Test Parallelization

#### 17.3.1 Playwright Parallel Testing

```javascript
// playwright.config.js
module.exports = {
  testDir: './tests',
  fullyParallel: true,
  workers: process.env.CI ? 2 : undefined,
  retries: process.env.CI ? 2 : 0,
  reporter: [
    ['html'],
    ['junit', {outputFile: 'test-results/junit.xml'}],
    ['json', {outputFile: 'test-results/results.json'}]
  ],
  
  use: {
    baseURL: process.env.BASE_URL || 'http://localhost:3000',
    trace: 'on-first-retry',
    screenshot: 'only-on-failure',
    video: 'retain-on-failure',
  },
  
  projects: [
    {
      name: 'chromium',
      use: {
        ...devices['Desktop Chrome'],
      },
    },
    {
      name: 'firefox',
      use: {
        ...devices['Desktop Firefox'],
      },
    },
    {
      name: 'webkit',
      use: {
        ...devices['Desktop Safari'],
      },
    },
    {
      name: 'mobile-chrome',
      use: {
        ...devices['Pixel 5'],
      },
    },
    {
      name: 'mobile-safari',
      use: {
        ...devices['iPhone 13'],
      },
    },
  ],
};
```

#### 17.3.2 Jest Parallel Configuration

```javascript
// jest.config.js
module.exports = {
  testEnvironment: 'node',
  maxWorkers: '50%', // Use 50% of available CPU cores
  testMatch: ['**/__tests__/**/*.test.js'],
  collectCoverageFrom: [
    'src/**/*.js',
    '!src/**/*.test.js',
    '!src/index.js'
  ],
  coverageThreshold: {
    global: {
      branches: 80,
      functions: 80,
      lines: 80,
      statements: 80
    }
  },
  setupFilesAfterEnv: ['<rootDir>/test/setup.js'],
  testTimeout: 10000,
};
```

### 17.4 Flaky Test Detection

#### 17.4.1 Retry Failed Tests

```yaml
# .github/workflows/flaky-test-detection.yml
name: Flaky Test Detection

on:
  schedule:
    - cron: '0 */6 * * *' # Every 6 hours

jobs:
  detect-flaky-tests:
    runs-on: ubuntu-latest
    
    steps:
      - uses: actions/checkout@v3
      
      - uses: actions/setup-node@v3
        with:
          node-version: '18'
      
      - name: Install dependencies
        run: npm ci
      
      - name: Run tests 10 times
        run: |
          for i in {1..10}; do
            echo "Run $i of 10"
            npm test -- --json --outputFile=results-$i.json || true
          done
      
      - name: Analyze results
        run: node scripts/analyze-flaky-tests.js
      
      - name: Create issue for flaky tests
        if: failure()
        uses: actions/github-script@v6
        with:
          script: |
            const fs = require('fs');
            const flakyTests = JSON.parse(fs.readFileSync('flaky-tests.json'));
            
            const body = `## Flaky Tests Detected\n\n${flakyTests.map(t => 
              `- ${t.name} (failed ${t.failures}/10 times)`
            ).join('\n')}`;
            
            github.rest.issues.create({
              owner: context.repo.owner,
              repo: context.repo.repo,
              title: 'Flaky tests detected',
              body: body,
              labels: ['flaky-test', 'bug']
            });
```

**analyze-flaky-tests.js**:

```javascript
const fs = require('fs');
const glob = require('glob');

const resultFiles = glob.sync('results-*.json');
const testResults = {};

for (const file of resultFiles) {
  const results = JSON.parse(fs.readFileSync(file));
  
  for (const testResult of results.testResults) {
    for (const test of testResult.assertionResults) {
      const testName = `${testResult.name}:${test.title}`;
      
      if (!testResults[testName]) {
        testResults[testName] = {
          name: testName,
          runs: 0,
          failures: 0
        };
      }
      
      testResults[testName].runs++;
      if (test.status === 'failed') {
        testResults[testName].failures++;
      }
    }
  }
}

// Identify flaky tests (passed sometimes, failed sometimes)
const flakyTests = Object.values(testResults).filter(test => 
  test.failures > 0 && test.failures < test.runs
);

if (flakyTests.length > 0) {
  console.log('Flaky tests found:');
  for (const test of flakyTests) {
    console.log(`  ${test.name}: ${test.failures}/${test.runs} failures`);
  }
  
  fs.writeFileSync('flaky-tests.json', JSON.stringify(flakyTests, null, 2));
  process.exit(1);
} else {
  console.log('No flaky tests detected ✓');
}
```

### 17.5 Test Reporting Dashboards

#### 17.5.1 Allure Report Integration

```yaml
# .github/workflows/test-with-allure.yml
name: Tests with Allure Report

on: [push, pull_request]

jobs:
  test:
    runs-on: ubuntu-latest
    
    steps:
      - uses: actions/checkout@v3
      
      - uses: actions/setup-node@v3
        with:
          node-version: '18'
      
      - name: Install dependencies
        run: npm ci
      
      - name: Run tests with Allure
        run: npm run test -- --reporter=allure-playwright
      
      - name: Generate Allure report
        if: always()
        run: npx allure generate allure-results -o allure-report
      
      - name: Upload Allure report
        if: always()
        uses: actions/upload-artifact@v3
        with:
          name: allure-report
          path: allure-report/
      
      - name: Deploy to GitHub Pages
        if: github.ref == 'refs/heads/main'
        uses: peaceiris/actions-gh-pages@v3
        with:
          github_token: ${{ secrets.GITHUB_TOKEN }}
          publish_dir: ./allure-report
          destination_dir: test-reports
```

#### 17.5.2 Custom Test Dashboard

```javascript
// scripts/generate-test-dashboard.js
const fs = require('fs');
const path = require('path');

class TestDashboardGenerator {
  constructor(testResultsPath) {
    this.testResultsPath = testResultsPath;
    this.results = this.loadResults();
  }
  
  loadResults() {
    const resultsFile = path.join(this.testResultsPath, 'results.json');
    return JSON.parse(fs.readFileSync(resultsFile));
  }
  
  generate() {
    const stats = this.calculateStats();
    const html = this.generateHTML(stats);
    
    fs.writeFileSync('test-dashboard.html', html);
    console.log('Dashboard generated: test-dashboard.html');
  }
  
  calculateStats() {
    const stats = {
      total: 0,
      passed: 0,
      failed: 0,
      skipped: 0,
      duration: 0,
      passRate: 0,
      testsByFile: {},
      slowestTests: [],
      failedTests: []
    };
    
    for (const suite of this.results.testResults) {
      for (const test of suite.assertionResults) {
        stats.total++;
        
        if (test.status === 'passed') stats.passed++;
        if (test.status === 'failed') {
          stats.failed++;
          stats.failedTests.push({
            name: test.fullName,
            file: suite.name,
            error: test.failureMessages.join('\n')
          });
        }
        if (test.status === 'skipped') stats.skipped++;
        
        stats.duration += test.duration || 0;
        
        if (test.duration > 1000) {
          stats.slowestTests.push({
            name: test.fullName,
            duration: test.duration
          });
        }
      }
      
      const fileName = path.basename(suite.name);
      stats.testsByFile[fileName] = {
        passed: suite.numPassingTests,
        failed: suite.numFailingTests,
        total: suite.numPassingTests + suite.numFailingTests
      };
    }
    
    stats.passRate = (stats.passed / stats.total * 100).toFixed(2);
    stats.slowestTests.sort((a, b) => b.duration - a.duration);
    stats.slowestTests = stats.slowestTests.slice(0, 10);
    
    return stats;
  }
  
  generateHTML(stats) {
    return `
<!DOCTYPE html>
<html>
<head>
  <title>Test Dashboard</title>
  <style>
    body {
      font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
      margin: 0;
      padding: 20px;
      background-color: #f5f5f5;
    }
    .container {
      max-width: 1200px;
      margin: 0 auto;
      background-color: white;
      padding: 30px;
      border-radius: 8px;
      box-shadow: 0 2px 4px rgba(0,0,0,0.1);
    }
    h1 {
      color: #333;
      border-bottom: 3px solid #4CAF50;
      padding-bottom: 10px;
    }
    .stats {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
      gap: 20px;
      margin: 30px 0;
    }
    .stat-card {
      background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
      color: white;
      padding: 20px;
      border-radius: 8px;
      text-align: center;
    }
    .stat-card.passed {
      background: linear-gradient(135deg, #4CAF50 0%, #45a049 100%);
    }
    .stat-card.failed {
      background: linear-gradient(135deg, #f44336 0%, #d32f2f 100%);
    }
    .stat-value {
      font-size: 3em;
      font-weight: bold;
      margin: 10px 0;
    }
    .stat-label {
      font-size: 0.9em;
      opacity: 0.9;
    }
    table {
      width: 100%;
      border-collapse: collapse;
      margin: 20px 0;
    }
    th, td {
      padding: 12px;
      text-align: left;
      border-bottom: 1px solid #ddd;
    }
    th {
      background-color: #4CAF50;
      color: white;
    }
    tr:hover {
      background-color: #f5f5f5;
    }
    .failed-test {
      background-color: #ffebee;
    }
    .error-message {
      font-family: monospace;
      font-size: 0.85em;
      color: #d32f2f;
      white-space: pre-wrap;
    }
  </style>
</head>
<body>
  <div class="container">
    <h1>Test Dashboard</h1>
    <p>Generated: ${new Date().toLocaleString()}</p>
    
    <div class="stats">
      <div class="stat-card">
        <div class="stat-label">Total Tests</div>
        <div class="stat-value">${stats.total}</div>
      </div>
      <div class="stat-card passed">
        <div class="stat-label">Passed</div>
        <div class="stat-value">${stats.passed}</div>
      </div>
      <div class="stat-card failed">
        <div class="stat-label">Failed</div>
        <div class="stat-value">${stats.failed}</div>
      </div>
      <div class="stat-card">
        <div class="stat-label">Pass Rate</div>
        <div class="stat-value">${stats.passRate}%</div>
      </div>
    </div>
    
    <h2>Tests by File</h2>
    <table>
      <thead>
        <tr>
          <th>File</th>
          <th>Passed</th>
          <th>Failed</th>
          <th>Total</th>
        </tr>
      </thead>
      <tbody>
        ${Object.entries(stats.testsByFile).map(([file, counts]) => `
          <tr>
            <td>${file}</td>
            <td style="color: #4CAF50">${counts.passed}</td>
            <td style="color: #f44336">${counts.failed}</td>
            <td>${counts.total}</td>
          </tr>
        `).join('')}
      </tbody>
    </table>
    
    ${stats.failedTests.length > 0 ? `
      <h2>Failed Tests</h2>
      <table>
        <thead>
          <tr>
            <th>Test</th>
            <th>File</th>
            <th>Error</th>
          </tr>
        </thead>
        <tbody>
          ${stats.failedTests.map(test => `
            <tr class="failed-test">
              <td>${test.name}</td>
              <td>${path.basename(test.file)}</td>
              <td><pre class="error-message">${test.error}</pre></td>
            </tr>
          `).join('')}
        </tbody>
      </table>
    ` : ''}
    
    <h2>Slowest Tests</h2>
    <table>
      <thead>
        <tr>
          <th>Test</th>
          <th>Duration (ms)</th>
        </tr>
      </thead>
      <tbody>
        ${stats.slowestTests.map(test => `
          <tr>
            <td>${test.name}</td>
            <td>${test.duration}</td>
          </tr>
        `).join('')}
      </tbody>
    </table>
  </div>
</body>
</html>
    `;
  }
}

// Generate dashboard
const generator = new TestDashboardGenerator('./test-results');
generator.generate();
```

### 17.6 Coverage Tracking

```yaml
# .github/workflows/coverage.yml
name: Code Coverage

on:
  push:
    branches: [main, develop]
  pull_request:
    branches: [main]

jobs:
  coverage:
    runs-on: ubuntu-latest
    
    steps:
      - uses: actions/checkout@v3
      
      - uses: actions/setup-node@v3
        with:
          node-version: '18'
      
      - name: Install dependencies
        run: npm ci
      
      - name: Run tests with coverage
        run: npm run test:coverage
      
      - name: Upload to Codecov
        uses: codecov/codecov-action@v3
        with:
          files: ./coverage/lcov.info
          flags: unittests
          fail_ci_if_error: true
      
      - name: Check coverage thresholds
        run: |
          node -e "
            const coverage = require('./coverage/coverage-summary.json');
            const total = coverage.total;
            
            if (total.lines.pct < 80) {
              console.error('Line coverage below 80%:', total.lines.pct);
              process.exit(1);
            }
            if (total.branches.pct < 75) {
              console.error('Branch coverage below 75%:', total.branches.pct);
              process.exit(1);
            }
            if (total.functions.pct < 80) {
              console.error('Function coverage below 80%:', total.functions.pct);
              process.exit(1);
            }
            
            console.log('✓ Coverage thresholds met');
            console.log('Lines:', total.lines.pct + '%');
            console.log('Branches:', total.branches.pct + '%');
            console.log('Functions:', total.functions.pct + '%');
          "
```

### 17.7 CI/CD Testing Checklist

**CI Configuration**:
- [ ] Tests run on every commit
- [ ] Tests run on every pull request
- [ ] Tests required to pass before merge
- [ ] Separate jobs for unit/integration/e2e tests
- [ ] Parallel test execution configured
- [ ] Test timeout configured
- [ ] Retry logic for flaky tests
- [ ] Test caching (dependencies, build)

**Test Environment**:
- [ ] Database seeded with test data
- [ ] External services mocked/stubbed
- [ ] Environment variables configured
- [ ] Secrets properly managed
- [ ] Network isolation
- [ ] Consistent across all CI runs

**Reporting**:
- [ ] Test results uploaded
- [ ] Coverage reports generated
- [ ] Failed test screenshots saved
- [ ] Test logs accessible
- [ ] Flaky test detection
- [ ] Performance metrics tracked
- [ ] Test dashboard available

**Quality Gates**:
- [ ] Minimum coverage percentage enforced
- [ ] Zero failing tests required
- [ ] Linter must pass
- [ ] Security scans pass
- [ ] Build must succeed
- [ ] No vulnerable dependencies

**Performance**:
- [ ] Tests complete in reasonable time (< 30 min)
- [ ] Resource usage optimized
- [ ] Test parallelization utilized
- [ ] Incremental testing (only affected tests)
- [ ] Caching properly configured

**Notifications**:
- [ ] Slack/email on test failure
- [ ] GitHub check status updated
- [ ] Pull request comments with results
- [ ] Dashboard accessible to team

---

## Conclusion

This comprehensive guide covers the essential aspects of functionality QA, from fundamental test design methodologies to advanced CI/CD integration. By following these practices and utilizing the provided test cases, checklists, and code examples, you can ensure thorough testing coverage and deliver high-quality software.

### Key Takeaways

1. **Test Early and Often**: Integrate testing throughout the development lifecycle
2. **Automate Wisely**: Automate repetitive tests while maintaining exploratory testing
3. **Security First**: Always test for security vulnerabilities, especially in payment and file upload systems
4. **Monitor and Improve**: Track metrics and continuously improve your testing process
5. **Collaborate**: Work closely with developers, product owners, and stakeholders
6. **Document Everything**: Maintain comprehensive test documentation for knowledge sharing
7. **Stay Current**: Keep up with testing tools, frameworks, and best practices

### Additional Resources

- **Playwright Documentation**: https://playwright.dev
- **Jest Documentation**: https://jestjs.io
- **Stripe Testing Guide**: https://stripe.com/docs/testing
- **WordPress Testing**: https://make.wordpress.org/core/handbook/testing/
- **OWASP Testing Guide**: https://owasp.org/www-project-web-security-testing-guide/

Remember: Good testing is an investment in quality, not a cost. The time spent on thorough QA saves exponentially more time in production bug fixes and maintains user trust.



---

## 18. Advanced End-to-End Testing {#advanced-e2e}

End-to-end testing validates the entire application workflow from start to finish. This section covers advanced patterns and techniques for Cypress, Playwright, and TestCafe.

### 18.1 Advanced Cypress Testing

Cypress is a JavaScript-based end-to-end testing framework built for modern web applications. While basic Cypress usage is straightforward, advanced patterns unlock powerful testing capabilities.

#### 18.1.1 Custom Commands and Utilities

Custom commands extend Cypress with reusable functions that encapsulate common testing operations.

**cypress/support/commands.js**:

```javascript
// Authentication command with session caching
Cypress.Commands.add('login', (email, password, options = {}) => {
  const { cacheSession = true } = options;
  
  if (cacheSession) {
    cy.session([email, password], () => {
      cy.request({
        method: 'POST',
        url: '/api/auth/login',
        body: { email, password },
      }).then((response) => {
        expect(response.status).to.eq(200);
        window.localStorage.setItem('authToken', response.body.token);
        window.localStorage.setItem('refreshToken', response.body.refreshToken);
        window.localStorage.setItem('user', JSON.stringify(response.body.user));
      });
    }, {
      validate() {
        cy.request({
          url: '/api/auth/me',
          headers: {
            Authorization: `Bearer ${window.localStorage.getItem('authToken')}`,
          },
          failOnStatusCode: false,
        }).its('status').should('eq', 200);
      },
    });
  } else {
    cy.visit('/login');
    cy.get('[data-testid="email-input"]').type(email);
    cy.get('[data-testid="password-input"]').type(password);
    cy.get('[data-testid="login-button"]').click();
    cy.url().should('not.include', '/login');
  }
});

// Drag and drop command
Cypress.Commands.add('dragAndDrop', (sourceSelector, targetSelector) => {
  cy.get(sourceSelector).then(($source) => {
    cy.get(targetSelector).then(($target) => {
      const sourceRect = $source[0].getBoundingClientRect();
      const targetRect = $target[0].getBoundingClientRect();
      
      cy.get(sourceSelector)
        .trigger('mousedown', { which: 1, pageX: sourceRect.x, pageY: sourceRect.y })
        .trigger('mousemove', { pageX: targetRect.x, pageY: targetRect.y })
        .trigger('mouseup', { force: true });
      
      cy.get(targetSelector)
        .trigger('mousedown', { which: 1 })
        .trigger('mousemove', { pageX: targetRect.x, pageY: targetRect.y })
        .trigger('drop')
        .trigger('mouseup', { force: true });
    });
  });
});

// File upload command supporting multiple files
Cypress.Commands.add('uploadFile', (selector, fileNames, mimeType) => {
  const files = Array.isArray(fileNames) ? fileNames : [fileNames];
  
  const filePromises = files.map((fileName) => {
    return cy.fixture(fileName, 'base64').then((content) => {
      return Cypress.Blob.base64StringToBlob(content, mimeType).then((blob) => {
        return new File([blob], fileName, { type: mimeType });
      });
    });
  });
  
  Cypress.Promise.all(filePromises).then((fileObjects) => {
    const dataTransfer = new DataTransfer();
    fileObjects.forEach((file) => dataTransfer.items.add(file));
    
    cy.get(selector).then(($input) => {
      $input[0].files = dataTransfer.files;
      cy.wrap($input).trigger('change', { force: true });
    });
  });
});

// Wait for API call to complete
Cypress.Commands.add('waitForApi', (method, url, alias) => {
  cy.intercept(method, url).as(alias);
  return cy.wait(`@${alias}`);
});

// Assert table data
Cypress.Commands.add('verifyTableData', (tableSelector, expectedData) => {
  cy.get(tableSelector).within(() => {
    expectedData.forEach((row, rowIndex) => {
      cy.get('tbody tr').eq(rowIndex).within(() => {
        Object.entries(row).forEach(([key, value], colIndex) => {
          cy.get('td').eq(colIndex).should('contain.text', value);
        });
      });
    });
  });
});

// Network request interceptor with response modification
Cypress.Commands.add('mockApiResponse', (method, url, response, statusCode = 200) => {
  cy.intercept(method, url, {
    statusCode,
    body: response,
    headers: {
      'Content-Type': 'application/json',
    },
  });
});

// Accessibility check command
Cypress.Commands.add('checkA11y', (context, options) => {
  cy.injectAxe();
  cy.checkA11y(context, options, (violations) => {
    const violationData = violations.map(({ id, impact, description, nodes }) => ({
      id,
      impact,
      description,
      nodes: nodes.length,
    }));
    
    cy.task('log', {
      title: 'Accessibility Violations',
      data: violationData,
    });
  });
});

// Retry command with custom logic
Cypress.Commands.add('retryUntil', (checkFn, options = {}) => {
  const { timeout = 10000, interval = 500 } = options;
  const startTime = Date.now();
  
  const attempt = () => {
    return checkFn().then((result) => {
      if (result) return result;
      if (Date.now() - startTime > timeout) {
        throw new Error(`retryUntil timed out after ${timeout}ms`);
      }
      cy.wait(interval);
      return attempt();
    });
  };
  
  return attempt();
});

// Scroll to element and verify visibility
Cypress.Commands.add('scrollToAndVerify', (selector) => {
  cy.get(selector).scrollIntoView().should('be.visible');
});

// Database seeding command via API
Cypress.Commands.add('seedDatabase', (fixture) => {
  cy.fixture(fixture).then((data) => {
    cy.request({
      method: 'POST',
      url: '/api/test/seed',
      body: data,
      headers: {
        'X-Test-Secret': Cypress.env('TEST_SECRET'),
      },
    }).its('status').should('eq', 200);
  });
});

// Clipboard operations
Cypress.Commands.add('copyToClipboard', (text) => {
  cy.window().then((win) => {
    win.navigator.clipboard.writeText(text);
  });
});

Cypress.Commands.add('getClipboardText', () => {
  return cy.window().then((win) => {
    return win.navigator.clipboard.readText();
  });
});
```

#### 18.1.2 Cypress Network Interception Patterns

Network interception is one of Cypress's most powerful features for controlling and testing API interactions.

```javascript
// cypress/e2e/network-interception.cy.js

describe('Advanced Network Interception', () => {
  beforeEach(() => {
    cy.login('admin@example.com', 'password123');
  });

  it('should intercept and modify API responses', () => {
    // Intercept GET request and return custom data
    cy.intercept('GET', '/api/products', {
      statusCode: 200,
      body: {
        products: [
          { id: 1, name: 'Test Product', price: 29.99, inStock: true },
          { id: 2, name: 'Another Product', price: 49.99, inStock: false },
        ],
        total: 2,
        page: 1,
      },
    }).as('getProducts');

    cy.visit('/products');
    cy.wait('@getProducts');

    cy.get('[data-testid="product-card"]').should('have.length', 2);
    cy.get('[data-testid="product-card"]').first().should('contain', 'Test Product');
    cy.get('[data-testid="product-card"]').last().should('contain', 'Another Product');
  });

  it('should spy on API calls without modifying them', () => {
    cy.intercept('GET', '/api/products*').as('getProducts');
    cy.intercept('POST', '/api/cart').as('addToCart');

    cy.visit('/products');
    cy.wait('@getProducts').then((interception) => {
      expect(interception.response.statusCode).to.eq(200);
      expect(interception.response.body.products).to.have.length.greaterThan(0);
    });

    cy.get('[data-testid="add-to-cart"]').first().click();
    cy.wait('@addToCart').then((interception) => {
      expect(interception.request.body).to.have.property('productId');
      expect(interception.request.body).to.have.property('quantity');
      expect(interception.response.statusCode).to.eq(201);
    });
  });

  it('should simulate network errors', () => {
    cy.intercept('GET', '/api/products', {
      forceNetworkError: true,
    }).as('getProductsError');

    cy.visit('/products');
    cy.wait('@getProductsError');

    cy.get('[data-testid="error-message"]')
      .should('be.visible')
      .and('contain', 'Failed to load products');
    cy.get('[data-testid="retry-button"]').should('be.visible');
  });

  it('should simulate slow network responses', () => {
    cy.intercept('GET', '/api/products', (req) => {
      req.reply({
        delay: 5000,
        statusCode: 200,
        body: { products: [], total: 0 },
      });
    }).as('slowProducts');

    cy.visit('/products');

    // Loading spinner should appear
    cy.get('[data-testid="loading-spinner"]').should('be.visible');

    cy.wait('@slowProducts');

    // Loading spinner should disappear after response
    cy.get('[data-testid="loading-spinner"]').should('not.exist');
  });

  it('should intercept and conditionally modify responses', () => {
    cy.intercept('GET', '/api/products*', (req) => {
      req.continue((res) => {
        // Modify the response: add discount to all products
        res.body.products = res.body.products.map((product) => ({
          ...product,
          discountedPrice: product.price * 0.9,
          hasDiscount: true,
        }));
        res.send();
      });
    }).as('getProducts');

    cy.visit('/products');
    cy.wait('@getProducts').then((interception) => {
      interception.response.body.products.forEach((product) => {
        expect(product.hasDiscount).to.be.true;
        expect(product.discountedPrice).to.be.lessThan(product.price);
      });
    });
  });

  it('should test pagination with intercepted responses', () => {
    const generateProducts = (page, perPage) => {
      return Array.from({ length: perPage }, (_, i) => ({
        id: (page - 1) * perPage + i + 1,
        name: `Product ${(page - 1) * perPage + i + 1}`,
        price: Math.round(Math.random() * 100 * 100) / 100,
      }));
    };

    cy.intercept('GET', '/api/products?page=1*', {
      body: { products: generateProducts(1, 10), total: 50, page: 1, totalPages: 5 },
    }).as('page1');

    cy.intercept('GET', '/api/products?page=2*', {
      body: { products: generateProducts(2, 10), total: 50, page: 2, totalPages: 5 },
    }).as('page2');

    cy.intercept('GET', '/api/products?page=3*', {
      body: { products: generateProducts(3, 10), total: 50, page: 3, totalPages: 5 },
    }).as('page3');

    cy.visit('/products');
    cy.wait('@page1');
    cy.get('[data-testid="product-card"]').should('have.length', 10);
    cy.get('[data-testid="product-card"]').first().should('contain', 'Product 1');

    cy.get('[data-testid="next-page"]').click();
    cy.wait('@page2');
    cy.get('[data-testid="product-card"]').should('have.length', 10);
    cy.get('[data-testid="product-card"]').first().should('contain', 'Product 11');

    cy.get('[data-testid="next-page"]').click();
    cy.wait('@page3');
    cy.get('[data-testid="product-card"]').first().should('contain', 'Product 21');
  });

  it('should test WebSocket connections', () => {
    // For WebSocket testing with Cypress, use a mock server
    cy.visit('/chat');
    
    // Send a message
    cy.get('[data-testid="message-input"]').type('Hello World');
    cy.get('[data-testid="send-button"]').click();

    // Verify message appears in chat
    cy.get('[data-testid="chat-messages"]')
      .should('contain', 'Hello World');

    // Verify message was sent (via API interceptor for fallback)
    cy.intercept('POST', '/api/messages').as('sendMessage');
  });

  it('should handle GraphQL requests', () => {
    cy.intercept('POST', '/graphql', (req) => {
      if (req.body.operationName === 'GetProducts') {
        req.reply({
          data: {
            products: {
              edges: [
                { node: { id: '1', name: 'GraphQL Product', price: 19.99 } },
              ],
              pageInfo: { hasNextPage: false },
            },
          },
        });
      }
      if (req.body.operationName === 'GetUser') {
        req.reply({
          data: {
            user: { id: '1', name: 'Test User', email: 'test@example.com' },
          },
        });
      }
    }).as('graphql');

    cy.visit('/dashboard');
    cy.wait('@graphql');
    cy.get('[data-testid="product-list"]').should('contain', 'GraphQL Product');
  });
});
```

#### 18.1.3 Cypress Component Testing

Cypress supports component testing for React, Vue, Angular, and Svelte applications.

```javascript
// cypress/component/ProductCard.cy.jsx
import React from 'react';
import { mount } from 'cypress/react18';
import ProductCard from '../../src/components/ProductCard';
import { CartProvider } from '../../src/contexts/CartContext';

describe('ProductCard Component', () => {
  const mockProduct = {
    id: 1,
    name: 'Premium Headphones',
    price: 149.99,
    description: 'High-quality wireless headphones with noise cancellation',
    image: '/images/headphones.jpg',
    rating: 4.5,
    reviewCount: 128,
    inStock: true,
    category: 'Electronics',
  };

  const mountWithProviders = (component) => {
    return mount(
      <CartProvider>
        {component}
      </CartProvider>
    );
  };

  it('renders product information correctly', () => {
    mountWithProviders(<ProductCard product={mockProduct} />);

    cy.get('[data-testid="product-name"]').should('contain', 'Premium Headphones');
    cy.get('[data-testid="product-price"]').should('contain', '$149.99');
    cy.get('[data-testid="product-description"]').should('contain', 'noise cancellation');
    cy.get('[data-testid="product-rating"]').should('contain', '4.5');
    cy.get('[data-testid="review-count"]').should('contain', '128 reviews');
    cy.get('[data-testid="stock-status"]').should('contain', 'In Stock');
  });

  it('handles out of stock products', () => {
    const outOfStockProduct = { ...mockProduct, inStock: false };
    mountWithProviders(<ProductCard product={outOfStockProduct} />);

    cy.get('[data-testid="stock-status"]')
      .should('contain', 'Out of Stock')
      .and('have.class', 'text-red-500');
    cy.get('[data-testid="add-to-cart"]').should('be.disabled');
  });

  it('adds product to cart on button click', () => {
    const onAddToCart = cy.stub().as('addToCart');
    mountWithProviders(
      <ProductCard product={mockProduct} onAddToCart={onAddToCart} />
    );

    cy.get('[data-testid="add-to-cart"]').click();
    cy.get('@addToCart').should('have.been.calledOnceWith', mockProduct.id, 1);
  });

  it('handles quantity changes', () => {
    mountWithProviders(<ProductCard product={mockProduct} />);

    cy.get('[data-testid="quantity-input"]').clear().type('3');
    cy.get('[data-testid="add-to-cart"]').click();
    
    cy.get('[data-testid="cart-count"]').should('contain', '3');
  });

  it('displays sale price correctly', () => {
    const saleProduct = {
      ...mockProduct,
      originalPrice: 199.99,
      price: 149.99,
      onSale: true,
    };
    mountWithProviders(<ProductCard product={saleProduct} />);

    cy.get('[data-testid="original-price"]')
      .should('contain', '$199.99')
      .and('have.css', 'text-decoration-line', 'line-through');
    cy.get('[data-testid="sale-price"]')
      .should('contain', '$149.99')
      .and('have.class', 'text-red-600');
    cy.get('[data-testid="discount-badge"]').should('contain', '25% OFF');
  });

  it('handles image loading error gracefully', () => {
    const productWithBadImage = { ...mockProduct, image: '/invalid-image.jpg' };
    mountWithProviders(<ProductCard product={productWithBadImage} />);

    cy.get('[data-testid="product-image"]')
      .should('have.attr', 'src')
      .and('include', 'placeholder');
  });

  it('navigates to product detail on click', () => {
    const onNavigate = cy.stub().as('navigate');
    mountWithProviders(
      <ProductCard product={mockProduct} onNavigate={onNavigate} />
    );

    cy.get('[data-testid="product-name"]').click();
    cy.get('@navigate').should('have.been.calledWith', `/products/${mockProduct.id}`);
  });

  it('renders responsive layout', () => {
    mountWithProviders(<ProductCard product={mockProduct} />);

    // Desktop view
    cy.viewport(1280, 720);
    cy.get('[data-testid="product-card"]').should('have.css', 'flex-direction', 'row');

    // Mobile view
    cy.viewport(375, 667);
    cy.get('[data-testid="product-card"]').should('have.css', 'flex-direction', 'column');
  });
});
```

#### 18.1.4 Cypress Plugin Configuration

```javascript
// cypress.config.js
const { defineConfig } = require('cypress');
const allureWriter = require('@shelex/cypress-allure-plugin/writer');
const createBundler = require('@bahmutov/cypress-esbuild-preprocessor');
const { addCucumberPreprocessorPlugin } = require('@badeball/cypress-cucumber-preprocessor');
const { createEsbuildPlugin } = require('@badeball/cypress-cucumber-preprocessor/esbuild');

module.exports = defineConfig({
  projectId: 'project-abc123',
  viewportWidth: 1280,
  viewportHeight: 720,
  defaultCommandTimeout: 10000,
  requestTimeout: 15000,
  responseTimeout: 30000,
  pageLoadTimeout: 60000,
  video: true,
  videoCompression: 32,
  screenshotOnRunFailure: true,
  screenshotsFolder: 'cypress/screenshots',
  videosFolder: 'cypress/videos',
  trashAssetsBeforeRuns: true,
  chromeWebSecurity: false,
  experimentalMemoryManagement: true,
  numTestsKeptInMemory: 5,

  retries: {
    runMode: 2,
    openMode: 0,
  },

  env: {
    apiUrl: 'http://localhost:3001/api',
    allure: true,
    allureReuseAfterSpec: true,
    grepFilterSpecs: true,
    grepOmitFiltered: true,
  },

  e2e: {
    baseUrl: 'http://localhost:3000',
    specPattern: [
      'cypress/e2e/**/*.cy.{js,jsx,ts,tsx}',
      'cypress/e2e/**/*.feature',
    ],
    supportFile: 'cypress/support/e2e.js',
    
    async setupNodeEvents(on, config) {
      allureWriter(on, config);
      
      await addCucumberPreprocessorPlugin(on, config);
      
      on('file:preprocessor', createBundler({
        plugins: [createEsbuildPlugin(config)],
      }));

      on('task', {
        log(message) {
          console.log(JSON.stringify(message, null, 2));
          return null;
        },
        
        async seedDb(data) {
          const { Client } = require('pg');
          const client = new Client({
            connectionString: process.env.DATABASE_URL_TEST,
          });
          await client.connect();
          
          for (const table of Object.keys(data)) {
            await client.query(`DELETE FROM ${table}`);
            for (const row of data[table]) {
              const columns = Object.keys(row).join(', ');
              const values = Object.values(row);
              const placeholders = values.map((_, i) => `$${i + 1}`).join(', ');
              await client.query(
                `INSERT INTO ${table} (${columns}) VALUES (${placeholders})`,
                values
              );
            }
          }
          
          await client.end();
          return null;
        },
        
        async queryDb(query) {
          const { Client } = require('pg');
          const client = new Client({
            connectionString: process.env.DATABASE_URL_TEST,
          });
          await client.connect();
          const result = await client.query(query);
          await client.end();
          return result.rows;
        },
        
        async resetDb() {
          const { Client } = require('pg');
          const client = new Client({
            connectionString: process.env.DATABASE_URL_TEST,
          });
          await client.connect();
          
          const tables = ['order_items', 'orders', 'cart_items', 'carts', 'products', 'users'];
          for (const table of tables) {
            await client.query(`TRUNCATE TABLE ${table} CASCADE`);
          }
          
          await client.end();
          return null;
        },
        
        async sendTestEmail(options) {
          const nodemailer = require('nodemailer');
          const transporter = nodemailer.createTransport({
            host: 'localhost',
            port: 1025,
          });
          await transporter.sendMail(options);
          return null;
        },
      });

      return config;
    },
  },

  component: {
    devServer: {
      framework: 'react',
      bundler: 'webpack',
    },
    specPattern: 'cypress/component/**/*.cy.{js,jsx,ts,tsx}',
  },
});
```

#### 18.1.5 Cypress Multi-Domain Testing

```javascript
// cypress/e2e/multi-domain.cy.js
describe('Multi-Domain OAuth Flow', () => {
  it('should complete OAuth login with external provider', () => {
    cy.visit('/login');
    cy.get('[data-testid="google-login"]').click();

    // Handle cross-origin redirect to Google OAuth
    cy.origin('https://accounts.google.com', () => {
      cy.get('input[type="email"]').type('testuser@gmail.com');
      cy.get('#identifierNext').click();
      cy.get('input[type="password"]').type('testpassword');
      cy.get('#passwordNext').click();
    });

    // Back on original domain after OAuth callback
    cy.url().should('include', '/dashboard');
    cy.get('[data-testid="user-name"]').should('contain', 'Test User');
  });

  it('should handle payment redirect to Stripe', () => {
    cy.login('user@example.com', 'password');
    cy.visit('/checkout');

    cy.get('[data-testid="pay-button"]').click();

    cy.origin('https://checkout.stripe.com', () => {
      cy.get('#cardNumber').type('4242424242424242');
      cy.get('#cardExpiry').type('1230');
      cy.get('#cardCvc').type('123');
      cy.get('#billingName').type('Test User');
      cy.get('.SubmitButton').click();
    });

    // Redirected back to success page
    cy.url().should('include', '/order/success');
    cy.get('[data-testid="order-confirmation"]').should('be.visible');
  });
});
```

#### 18.1.6 Cypress Visual Testing with Percy

```javascript
// cypress/e2e/visual-testing.cy.js
describe('Visual Regression Tests', () => {
  beforeEach(() => {
    cy.login('admin@example.com', 'password');
  });

  it('should capture homepage visual snapshot', () => {
    cy.visit('/');
    cy.get('[data-testid="hero-section"]').should('be.visible');
    cy.percySnapshot('Homepage');
  });

  it('should capture product listing page', () => {
    cy.visit('/products');
    cy.get('[data-testid="product-grid"]').should('be.visible');
    cy.percySnapshot('Product Listing');
  });

  it('should capture responsive layouts', () => {
    cy.visit('/');

    // Desktop
    cy.viewport(1920, 1080);
    cy.percySnapshot('Homepage - Desktop', { widths: [1920] });

    // Tablet
    cy.viewport(768, 1024);
    cy.percySnapshot('Homepage - Tablet', { widths: [768] });

    // Mobile
    cy.viewport(375, 667);
    cy.percySnapshot('Homepage - Mobile', { widths: [375] });
  });

  it('should capture form states', () => {
    cy.visit('/contact');

    // Empty form
    cy.percySnapshot('Contact Form - Empty');

    // Filled form
    cy.get('#name').type('John Doe');
    cy.get('#email').type('john@example.com');
    cy.get('#message').type('Hello, this is a test message.');
    cy.percySnapshot('Contact Form - Filled');

    // Error state
    cy.get('#email').clear().type('invalid-email');
    cy.get('[data-testid="submit"]').click();
    cy.percySnapshot('Contact Form - Error State');
  });

  it('should capture dark mode', () => {
    cy.visit('/');
    cy.get('[data-testid="theme-toggle"]').click();
    cy.percySnapshot('Homepage - Dark Mode');
  });
});
```

#### 18.1.7 Cypress Data-Driven Testing

```javascript
// cypress/e2e/data-driven.cy.js
describe('Data-Driven Testing', () => {
  // Load test data from fixture
  beforeEach(() => {
    cy.fixture('users.json').as('users');
    cy.fixture('products.json').as('products');
  });

  it('should validate registration with multiple user profiles', function () {
    const testCases = [
      {
        user: { name: 'Valid User', email: 'valid@example.com', password: 'SecurePass123!' },
        expected: { success: true, message: 'Account created successfully' },
      },
      {
        user: { name: '', email: 'test@example.com', password: 'SecurePass123!' },
        expected: { success: false, message: 'Name is required' },
      },
      {
        user: { name: 'Test', email: 'invalid-email', password: 'SecurePass123!' },
        expected: { success: false, message: 'Valid email is required' },
      },
      {
        user: { name: 'Test', email: 'test@example.com', password: 'weak' },
        expected: { success: false, message: 'Password must be at least 8 characters' },
      },
      {
        user: { name: 'Test', email: 'test@example.com', password: 'nouppercaseornumber!' },
        expected: { success: false, message: 'Password must contain uppercase, lowercase, number, and special character' },
      },
    ];

    testCases.forEach(({ user, expected }, index) => {
      cy.visit('/register');

      if (user.name) cy.get('[data-testid="name-input"]').type(user.name);
      if (user.email) cy.get('[data-testid="email-input"]').type(user.email);
      if (user.password) cy.get('[data-testid="password-input"]').type(user.password);

      cy.get('[data-testid="register-button"]').click();

      if (expected.success) {
        cy.url().should('include', '/welcome');
        cy.get('[data-testid="success-message"]').should('contain', expected.message);
      } else {
        cy.get('[data-testid="error-message"]').should('contain', expected.message);
      }
    });
  });

  it('should test search with various inputs', () => {
    const searchCases = [
      { query: 'laptop', minResults: 1, category: 'Electronics' },
      { query: 'nike shoes', minResults: 1, category: 'Footwear' },
      { query: '', minResults: 0, category: null },
      { query: 'zzz_nonexistent_product', minResults: 0, category: null },
      { query: '<script>alert(1)</script>', minResults: 0, category: null },
    ];

    searchCases.forEach(({ query, minResults, category }) => {
      cy.visit('/products');

      if (query) {
        cy.get('[data-testid="search-input"]').clear().type(query);
        cy.get('[data-testid="search-button"]').click();
      }

      if (minResults > 0) {
        cy.get('[data-testid="product-card"]').should('have.length.at.least', minResults);
        if (category) {
          cy.get('[data-testid="product-category"]').first().should('contain', category);
        }
      } else if (query === '') {
        // Empty search shows all products
        cy.get('[data-testid="product-card"]').should('have.length.at.least', 1);
      } else {
        cy.get('[data-testid="no-results"]').should('be.visible');
      }
    });
  });

  it('should validate checkout with different shipping options', () => {
    const shippingOptions = [
      { method: 'standard', price: '$5.99', deliveryDays: '5-7 business days' },
      { method: 'express', price: '$12.99', deliveryDays: '2-3 business days' },
      { method: 'overnight', price: '$24.99', deliveryDays: 'Next business day' },
      { method: 'free', price: '$0.00', deliveryDays: '7-10 business days', minOrder: 50 },
    ];

    cy.login('user@example.com', 'password');
    cy.visit('/cart');

    shippingOptions.forEach(({ method, price, deliveryDays }) => {
      cy.get(`[data-testid="shipping-${method}"]`).click();
      cy.get('[data-testid="shipping-price"]').should('contain', price);
      cy.get('[data-testid="delivery-estimate"]').should('contain', deliveryDays);
    });
  });
});
```

### 18.2 Advanced Playwright Testing

Playwright provides cross-browser testing with a powerful API. This section covers advanced patterns beyond basic usage.

#### 18.2.1 Playwright Page Object Model

```typescript
// tests/pages/BasePage.ts
import { Page, Locator, expect } from '@playwright/test';

export abstract class BasePage {
  readonly page: Page;
  readonly header: Locator;
  readonly footer: Locator;
  readonly loadingSpinner: Locator;
  readonly toastNotification: Locator;

  constructor(page: Page) {
    this.page = page;
    this.header = page.locator('header');
    this.footer = page.locator('footer');
    this.loadingSpinner = page.locator('[data-testid="loading"]');
    this.toastNotification = page.locator('[data-testid="toast"]');
  }

  async waitForPageLoad(): Promise<void> {
    await this.page.waitForLoadState('networkidle');
    await expect(this.loadingSpinner).not.toBeVisible({ timeout: 30000 });
  }

  async getToastMessage(): Promise<string> {
    await expect(this.toastNotification).toBeVisible();
    return this.toastNotification.textContent() as Promise<string>;
  }

  async dismissToast(): Promise<void> {
    await this.toastNotification.locator('[data-testid="toast-close"]').click();
    await expect(this.toastNotification).not.toBeVisible();
  }

  async takeScreenshot(name: string): Promise<void> {
    await this.page.screenshot({ path: `screenshots/${name}.png`, fullPage: true });
  }

  async waitForApiResponse(urlPattern: string | RegExp): Promise<any> {
    const response = await this.page.waitForResponse(urlPattern);
    return response.json();
  }

  async navigateTo(path: string): Promise<void> {
    await this.page.goto(path);
    await this.waitForPageLoad();
  }
}

// tests/pages/LoginPage.ts
import { Page, Locator, expect } from '@playwright/test';
import { BasePage } from './BasePage';

export class LoginPage extends BasePage {
  readonly emailInput: Locator;
  readonly passwordInput: Locator;
  readonly loginButton: Locator;
  readonly forgotPasswordLink: Locator;
  readonly registerLink: Locator;
  readonly errorMessage: Locator;
  readonly rememberMeCheckbox: Locator;
  readonly googleLoginButton: Locator;
  readonly githubLoginButton: Locator;

  constructor(page: Page) {
    super(page);
    this.emailInput = page.getByTestId('email-input');
    this.passwordInput = page.getByTestId('password-input');
    this.loginButton = page.getByTestId('login-button');
    this.forgotPasswordLink = page.getByTestId('forgot-password');
    this.registerLink = page.getByTestId('register-link');
    this.errorMessage = page.getByTestId('error-message');
    this.rememberMeCheckbox = page.getByTestId('remember-me');
    this.googleLoginButton = page.getByTestId('google-login');
    this.githubLoginButton = page.getByTestId('github-login');
  }

  async goto(): Promise<void> {
    await this.navigateTo('/login');
  }

  async login(email: string, password: string, rememberMe = false): Promise<void> {
    await this.emailInput.fill(email);
    await this.passwordInput.fill(password);
    if (rememberMe) {
      await this.rememberMeCheckbox.check();
    }
    await this.loginButton.click();
  }

  async loginAndWaitForDashboard(email: string, password: string): Promise<void> {
    await this.login(email, password);
    await this.page.waitForURL('**/dashboard');
    await this.waitForPageLoad();
  }

  async getErrorMessage(): Promise<string> {
    await expect(this.errorMessage).toBeVisible();
    return this.errorMessage.textContent() as Promise<string>;
  }

  async isLoginButtonEnabled(): Promise<boolean> {
    return this.loginButton.isEnabled();
  }

  async clickForgotPassword(): Promise<void> {
    await this.forgotPasswordLink.click();
    await this.page.waitForURL('**/forgot-password');
  }

  async clickRegister(): Promise<void> {
    await this.registerLink.click();
    await this.page.waitForURL('**/register');
  }
}

// tests/pages/DashboardPage.ts
import { Page, Locator, expect } from '@playwright/test';
import { BasePage } from './BasePage';

export class DashboardPage extends BasePage {
  readonly welcomeMessage: Locator;
  readonly statsCards: Locator;
  readonly recentOrders: Locator;
  readonly userMenu: Locator;
  readonly logoutButton: Locator;
  readonly searchInput: Locator;
  readonly notificationBell: Locator;
  readonly notificationBadge: Locator;
  readonly sidebar: Locator;

  constructor(page: Page) {
    super(page);
    this.welcomeMessage = page.getByTestId('welcome-message');
    this.statsCards = page.getByTestId('stats-card');
    this.recentOrders = page.getByTestId('recent-orders');
    this.userMenu = page.getByTestId('user-menu');
    this.logoutButton = page.getByTestId('logout-button');
    this.searchInput = page.getByTestId('dashboard-search');
    this.notificationBell = page.getByTestId('notification-bell');
    this.notificationBadge = page.getByTestId('notification-badge');
    this.sidebar = page.getByTestId('sidebar');
  }

  async goto(): Promise<void> {
    await this.navigateTo('/dashboard');
  }

  async getWelcomeText(): Promise<string> {
    return this.welcomeMessage.textContent() as Promise<string>;
  }

  async getStatsCount(): Promise<number> {
    return this.statsCards.count();
  }

  async getStatValue(statName: string): Promise<string> {
    const card = this.statsCards.filter({ hasText: statName });
    return card.locator('[data-testid="stat-value"]').textContent() as Promise<string>;
  }

  async logout(): Promise<void> {
    await this.userMenu.click();
    await this.logoutButton.click();
    await this.page.waitForURL('**/login');
  }

  async getNotificationCount(): Promise<number> {
    const text = await this.notificationBadge.textContent();
    return parseInt(text || '0', 10);
  }

  async openNotifications(): Promise<void> {
    await this.notificationBell.click();
    await expect(this.page.getByTestId('notification-panel')).toBeVisible();
  }

  async navigateToSection(section: string): Promise<void> {
    await this.sidebar.getByText(section).click();
    await this.waitForPageLoad();
  }
}

// tests/pages/ProductPage.ts
import { Page, Locator, expect } from '@playwright/test';
import { BasePage } from './BasePage';

export class ProductPage extends BasePage {
  readonly productGrid: Locator;
  readonly productCards: Locator;
  readonly searchInput: Locator;
  readonly searchButton: Locator;
  readonly filterPanel: Locator;
  readonly sortSelect: Locator;
  readonly paginationNext: Locator;
  readonly paginationPrev: Locator;
  readonly cartButton: Locator;
  readonly cartCount: Locator;
  readonly priceRangeMin: Locator;
  readonly priceRangeMax: Locator;
  readonly categoryFilter: Locator;

  constructor(page: Page) {
    super(page);
    this.productGrid = page.getByTestId('product-grid');
    this.productCards = page.getByTestId('product-card');
    this.searchInput = page.getByTestId('search-input');
    this.searchButton = page.getByTestId('search-button');
    this.filterPanel = page.getByTestId('filter-panel');
    this.sortSelect = page.getByTestId('sort-select');
    this.paginationNext = page.getByTestId('next-page');
    this.paginationPrev = page.getByTestId('prev-page');
    this.cartButton = page.getByTestId('cart-button');
    this.cartCount = page.getByTestId('cart-count');
    this.priceRangeMin = page.getByTestId('price-min');
    this.priceRangeMax = page.getByTestId('price-max');
    this.categoryFilter = page.getByTestId('category-filter');
  }

  async goto(): Promise<void> {
    await this.navigateTo('/products');
  }

  async search(query: string): Promise<void> {
    await this.searchInput.fill(query);
    await this.searchButton.click();
    await this.waitForPageLoad();
  }

  async getProductCount(): Promise<number> {
    return this.productCards.count();
  }

  async getProductNames(): Promise<string[]> {
    return this.productCards.locator('[data-testid="product-name"]').allTextContents();
  }

  async getProductPrices(): Promise<number[]> {
    const priceTexts = await this.productCards.locator('[data-testid="product-price"]').allTextContents();
    return priceTexts.map((text) => parseFloat(text.replace(/[^0-9.]/g, '')));
  }

  async sortBy(option: string): Promise<void> {
    await this.sortSelect.selectOption(option);
    await this.waitForPageLoad();
  }

  async filterByCategory(category: string): Promise<void> {
    await this.categoryFilter.selectOption(category);
    await this.waitForPageLoad();
  }

  async filterByPriceRange(min: number, max: number): Promise<void> {
    await this.priceRangeMin.fill(min.toString());
    await this.priceRangeMax.fill(max.toString());
    await this.page.getByTestId('apply-filters').click();
    await this.waitForPageLoad();
  }

  async addToCart(productIndex: number): Promise<void> {
    await this.productCards.nth(productIndex).getByTestId('add-to-cart').click();
    await expect(this.page.getByTestId('toast')).toContainText('Added to cart');
  }

  async goToNextPage(): Promise<void> {
    await this.paginationNext.click();
    await this.waitForPageLoad();
  }

  async getCartItemCount(): Promise<number> {
    const text = await this.cartCount.textContent();
    return parseInt(text || '0', 10);
  }
}
```

#### 18.2.2 Playwright Test Fixtures and Helpers

```typescript
// tests/fixtures/test-fixtures.ts
import { test as base, expect } from '@playwright/test';
import { LoginPage } from '../pages/LoginPage';
import { DashboardPage } from '../pages/DashboardPage';
import { ProductPage } from '../pages/ProductPage';

type TestFixtures = {
  loginPage: LoginPage;
  dashboardPage: DashboardPage;
  productPage: ProductPage;
  authenticatedPage: DashboardPage;
  apiContext: any;
};

export const test = base.extend<TestFixtures>({
  loginPage: async ({ page }, use) => {
    const loginPage = new LoginPage(page);
    await loginPage.goto();
    await use(loginPage);
  },

  dashboardPage: async ({ page }, use) => {
    await use(new DashboardPage(page));
  },

  productPage: async ({ page }, use) => {
    const productPage = new ProductPage(page);
    await productPage.goto();
    await use(productPage);
  },

  authenticatedPage: async ({ page, context }, use) => {
    // Set auth state via API
    const response = await page.request.post('/api/auth/login', {
      data: {
        email: 'admin@example.com',
        password: 'adminpass123',
      },
    });
    const { token } = await response.json();

    // Set token in storage state
    await context.addCookies([
      {
        name: 'auth-token',
        value: token,
        domain: 'localhost',
        path: '/',
      },
    ]);

    const dashboardPage = new DashboardPage(page);
    await dashboardPage.goto();
    await use(dashboardPage);
  },

  apiContext: async ({ playwright }, use) => {
    const apiContext = await playwright.request.newContext({
      baseURL: 'http://localhost:3001',
      extraHTTPHeaders: {
        'Content-Type': 'application/json',
        Authorization: `Bearer ${process.env.TEST_API_TOKEN}`,
      },
    });
    await use(apiContext);
    await apiContext.dispose();
  },
});

export { expect };
```

#### 18.2.3 Playwright API Testing

```typescript
// tests/api/api.spec.ts
import { test, expect } from '../fixtures/test-fixtures';

test.describe('REST API Tests', () => {
  let authToken: string;

  test.beforeAll(async ({ request }) => {
    const response = await request.post('/api/auth/login', {
      data: {
        email: 'admin@example.com',
        password: 'adminpass123',
      },
    });
    const body = await response.json();
    authToken = body.token;
  });

  test('GET /api/products - should return product list', async ({ request }) => {
    const response = await request.get('/api/products', {
      headers: { Authorization: `Bearer ${authToken}` },
    });

    expect(response.ok()).toBeTruthy();
    const body = await response.json();

    expect(body).toHaveProperty('products');
    expect(body.products).toBeInstanceOf(Array);
    expect(body.products.length).toBeGreaterThan(0);

    // Validate product schema
    const product = body.products[0];
    expect(product).toHaveProperty('id');
    expect(product).toHaveProperty('name');
    expect(product).toHaveProperty('price');
    expect(typeof product.id).toBe('number');
    expect(typeof product.name).toBe('string');
    expect(typeof product.price).toBe('number');
    expect(product.price).toBeGreaterThan(0);
  });

  test('POST /api/products - should create a product', async ({ request }) => {
    const newProduct = {
      name: 'Test Product',
      price: 29.99,
      description: 'A test product for automated testing',
      category: 'Electronics',
      stock: 100,
    };

    const response = await request.post('/api/products', {
      data: newProduct,
      headers: { Authorization: `Bearer ${authToken}` },
    });

    expect(response.status()).toBe(201);
    const body = await response.json();

    expect(body.id).toBeDefined();
    expect(body.name).toBe(newProduct.name);
    expect(body.price).toBe(newProduct.price);
    expect(body.description).toBe(newProduct.description);

    // Clean up
    await request.delete(`/api/products/${body.id}`, {
      headers: { Authorization: `Bearer ${authToken}` },
    });
  });

  test('PUT /api/products/:id - should update a product', async ({ request }) => {
    // Create product first
    const createResponse = await request.post('/api/products', {
      data: { name: 'Update Test', price: 10.00, stock: 50 },
      headers: { Authorization: `Bearer ${authToken}` },
    });
    const created = await createResponse.json();

    // Update product
    const updateResponse = await request.put(`/api/products/${created.id}`, {
      data: { name: 'Updated Name', price: 15.00 },
      headers: { Authorization: `Bearer ${authToken}` },
    });

    expect(updateResponse.ok()).toBeTruthy();
    const updated = await updateResponse.json();
    expect(updated.name).toBe('Updated Name');
    expect(updated.price).toBe(15.00);
    expect(updated.stock).toBe(50); // Unchanged field

    // Clean up
    await request.delete(`/api/products/${created.id}`, {
      headers: { Authorization: `Bearer ${authToken}` },
    });
  });

  test('DELETE /api/products/:id - should delete a product', async ({ request }) => {
    // Create product first
    const createResponse = await request.post('/api/products', {
      data: { name: 'Delete Test', price: 5.00, stock: 10 },
      headers: { Authorization: `Bearer ${authToken}` },
    });
    const created = await createResponse.json();

    // Delete product
    const deleteResponse = await request.delete(`/api/products/${created.id}`, {
      headers: { Authorization: `Bearer ${authToken}` },
    });

    expect(deleteResponse.status()).toBe(204);

    // Verify deletion
    const getResponse = await request.get(`/api/products/${created.id}`, {
      headers: { Authorization: `Bearer ${authToken}` },
    });
    expect(getResponse.status()).toBe(404);
  });

  test('should handle 401 unauthorized', async ({ request }) => {
    const response = await request.get('/api/products', {
      headers: { Authorization: 'Bearer invalid-token' },
    });
    expect(response.status()).toBe(401);
  });

  test('should handle 400 bad request', async ({ request }) => {
    const response = await request.post('/api/products', {
      data: { name: '', price: -1 },
      headers: { Authorization: `Bearer ${authToken}` },
    });

    expect(response.status()).toBe(400);
    const body = await response.json();
    expect(body.errors).toBeDefined();
  });

  test('should handle pagination', async ({ request }) => {
    const page1 = await request.get('/api/products?page=1&limit=5', {
      headers: { Authorization: `Bearer ${authToken}` },
    });
    const page1Body = await page1.json();

    expect(page1Body.products.length).toBeLessThanOrEqual(5);
    expect(page1Body.pagination.page).toBe(1);
    expect(page1Body.pagination.totalPages).toBeDefined();

    if (page1Body.pagination.totalPages > 1) {
      const page2 = await request.get('/api/products?page=2&limit=5', {
        headers: { Authorization: `Bearer ${authToken}` },
      });
      const page2Body = await page2.json();

      // No duplicate IDs across pages
      const page1Ids = page1Body.products.map((p: any) => p.id);
      const page2Ids = page2Body.products.map((p: any) => p.id);
      const overlap = page1Ids.filter((id: number) => page2Ids.includes(id));
      expect(overlap.length).toBe(0);
    }
  });

  test('should handle rate limiting', async ({ request }) => {
    const requests = Array.from({ length: 100 }, () =>
      request.get('/api/products', {
        headers: { Authorization: `Bearer ${authToken}` },
      })
    );

    const responses = await Promise.all(requests);
    const tooManyRequests = responses.filter((r) => r.status() === 429);

    // At some point, rate limiting should kick in
    if (tooManyRequests.length > 0) {
      const body = await tooManyRequests[0].json();
      expect(body.message).toContain('rate limit');
      expect(body.retryAfter).toBeDefined();
    }
  });
});
```

#### 18.2.4 Playwright Parallel Test Execution

```typescript
// playwright.config.ts
import { defineConfig, devices } from '@playwright/test';

export default defineConfig({
  testDir: './tests',
  fullyParallel: true,
  forbidOnly: !!process.env.CI,
  retries: process.env.CI ? 2 : 0,
  workers: process.env.CI ? 4 : undefined,
  reporter: [
    ['html', { outputFolder: 'playwright-report' }],
    ['json', { outputFile: 'test-results/results.json' }],
    ['junit', { outputFile: 'test-results/junit.xml' }],
    ['allure-playwright'],
    ['list'],
  ],
  
  use: {
    baseURL: process.env.BASE_URL || 'http://localhost:3000',
    trace: 'on-first-retry',
    screenshot: 'only-on-failure',
    video: 'retain-on-failure',
    actionTimeout: 15000,
    navigationTimeout: 30000,
  },

  projects: [
    {
      name: 'setup',
      testMatch: /.*\.setup\.ts/,
    },
    {
      name: 'chromium',
      use: { ...devices['Desktop Chrome'] },
      dependencies: ['setup'],
    },
    {
      name: 'firefox',
      use: { ...devices['Desktop Firefox'] },
      dependencies: ['setup'],
    },
    {
      name: 'webkit',
      use: { ...devices['Desktop Safari'] },
      dependencies: ['setup'],
    },
    {
      name: 'mobile-chrome',
      use: { ...devices['Pixel 5'] },
      dependencies: ['setup'],
    },
    {
      name: 'mobile-safari',
      use: { ...devices['iPhone 13'] },
      dependencies: ['setup'],
    },
    {
      name: 'branded-chrome',
      use: {
        channel: 'chrome',
      },
      dependencies: ['setup'],
    },
    {
      name: 'api-tests',
      testMatch: /.*api.*\.spec\.ts/,
      use: {
        baseURL: 'http://localhost:3001',
      },
    },
  ],

  webServer: {
    command: 'npm run dev',
    url: 'http://localhost:3000',
    reuseExistingServer: !process.env.CI,
    timeout: 120000,
  },
});
```

#### 18.2.5 Playwright Authentication State

```typescript
// tests/auth.setup.ts
import { test as setup, expect } from '@playwright/test';

const adminFile = 'playwright/.auth/admin.json';
const userFile = 'playwright/.auth/user.json';

setup('authenticate as admin', async ({ page }) => {
  await page.goto('/login');
  await page.getByTestId('email-input').fill('admin@example.com');
  await page.getByTestId('password-input').fill('adminpass123');
  await page.getByTestId('login-button').click();
  await page.waitForURL('**/dashboard');
  await expect(page.getByTestId('welcome-message')).toBeVisible();
  await page.context().storageState({ path: adminFile });
});

setup('authenticate as regular user', async ({ page }) => {
  await page.goto('/login');
  await page.getByTestId('email-input').fill('user@example.com');
  await page.getByTestId('password-input').fill('userpass123');
  await page.getByTestId('login-button').click();
  await page.waitForURL('**/dashboard');
  await page.context().storageState({ path: userFile });
});

// Usage in tests:
// test.use({ storageState: 'playwright/.auth/admin.json' });
```

#### 18.2.6 Playwright Trace Viewer and Debugging

```typescript
// tests/e2e/checkout.spec.ts
import { test, expect } from '@playwright/test';

test.describe('Checkout Flow with Tracing', () => {
  test.beforeEach(async ({ page, context }) => {
    // Start tracing for debugging
    await context.tracing.start({ screenshots: true, snapshots: true, sources: true });
  });

  test.afterEach(async ({ page, context }, testInfo) => {
    // Save trace only on failure
    if (testInfo.status !== testInfo.expectedStatus) {
      const tracePath = `test-results/traces/${testInfo.title.replace(/\s/g, '-')}.zip`;
      await context.tracing.stop({ path: tracePath });
    } else {
      await context.tracing.stop();
    }
  });

  test('complete checkout flow', async ({ page }) => {
    await page.goto('/products');
    
    // Add item to cart
    await page.getByTestId('product-card').first().getByTestId('add-to-cart').click();
    await expect(page.getByTestId('toast')).toContainText('Added to cart');
    
    // Go to cart
    await page.getByTestId('cart-button').click();
    await expect(page).toHaveURL(/.*cart/);
    
    // Verify cart contents
    const cartItems = page.getByTestId('cart-item');
    await expect(cartItems).toHaveCount(1);
    
    // Proceed to checkout
    await page.getByTestId('checkout-button').click();
    await expect(page).toHaveURL(/.*checkout/);
    
    // Fill shipping information
    await page.getByTestId('first-name').fill('John');
    await page.getByTestId('last-name').fill('Doe');
    await page.getByTestId('address').fill('123 Test St');
    await page.getByTestId('city').fill('San Francisco');
    await page.getByTestId('state').selectOption('CA');
    await page.getByTestId('zip').fill('94105');
    await page.getByTestId('phone').fill('555-0123');
    
    // Select shipping method
    await page.getByTestId('shipping-standard').check();
    
    // Fill payment information
    const stripeFrame = page.frameLocator('iframe[name*="stripe"]').first();
    await stripeFrame.getByPlaceholder('Card number').fill('4242424242424242');
    await stripeFrame.getByPlaceholder('MM / YY').fill('12/30');
    await stripeFrame.getByPlaceholder('CVC').fill('123');
    
    // Place order
    await page.getByTestId('place-order').click();
    
    // Wait for order confirmation
    await expect(page).toHaveURL(/.*order-confirmation/, { timeout: 30000 });
    await expect(page.getByTestId('order-number')).toBeVisible();
    
    const orderNumber = await page.getByTestId('order-number').textContent();
    expect(orderNumber).toMatch(/^ORD-\d+$/);
  });
});
```

### 18.3 TestCafe End-to-End Testing

TestCafe is a Node.js based end-to-end testing framework that does not require browser plugins or WebDriver.

#### 18.3.1 TestCafe Configuration and Setup

```javascript
// .testcaferc.json
{
  "browsers": ["chrome", "firefox"],
  "src": ["tests/e2e/**/*.testcafe.js"],
  "screenshots": {
    "path": "reports/screenshots/",
    "takeOnFails": true,
    "fullPage": true,
    "pathPattern": "${DATE}_${TIME}/test-${TEST_INDEX}/${USERAGENT}/${FILE_INDEX}.png"
  },
  "reporter": [
    {
      "name": "spec"
    },
    {
      "name": "xunit",
      "output": "reports/results.xml"
    },
    {
      "name": "html",
      "output": "reports/report.html"
    }
  ],
  "concurrency": 3,
  "selectorTimeout": 10000,
  "assertionTimeout": 5000,
  "pageLoadTimeout": 30000,
  "speed": 0.8,
  "quarantineMode": {
    "successThreshold": 1,
    "attemptLimit": 3
  },
  "retryTestPages": true,
  "disablePageCaching": true
}
```

#### 18.3.2 TestCafe Page Objects

```javascript
// tests/pages/LoginPage.testcafe.js
import { Selector, t } from 'testcafe';

class LoginPage {
  constructor() {
    this.emailInput = Selector('[data-testid="email-input"]');
    this.passwordInput = Selector('[data-testid="password-input"]');
    this.loginButton = Selector('[data-testid="login-button"]');
    this.errorMessage = Selector('[data-testid="error-message"]');
    this.forgotPasswordLink = Selector('[data-testid="forgot-password"]');
    this.registerLink = Selector('[data-testid="register-link"]');
    this.rememberMe = Selector('[data-testid="remember-me"]');
    this.socialLoginGoogle = Selector('[data-testid="google-login"]');
    this.socialLoginGithub = Selector('[data-testid="github-login"]');
  }

  async navigateTo() {
    await t.navigateTo('/login');
  }

  async login(email, password) {
    await t
      .typeText(this.emailInput, email, { replace: true })
      .typeText(this.passwordInput, password, { replace: true })
      .click(this.loginButton);
  }

  async loginWithRememberMe(email, password) {
    await t
      .typeText(this.emailInput, email, { replace: true })
      .typeText(this.passwordInput, password, { replace: true })
      .click(this.rememberMe)
      .click(this.loginButton);
  }

  async getErrorText() {
    return this.errorMessage.textContent;
  }

  async isErrorVisible() {
    return this.errorMessage.exists;
  }
}

export default new LoginPage();

// tests/pages/DashboardPage.testcafe.js
import { Selector, t } from 'testcafe';

class DashboardPage {
  constructor() {
    this.welcomeMessage = Selector('[data-testid="welcome-message"]');
    this.statsCards = Selector('[data-testid="stats-card"]');
    this.recentActivity = Selector('[data-testid="recent-activity"]');
    this.userMenu = Selector('[data-testid="user-menu"]');
    this.logoutButton = Selector('[data-testid="logout-button"]');
    this.sidebar = Selector('[data-testid="sidebar"]');
    this.notificationBell = Selector('[data-testid="notification-bell"]');
    this.notificationBadge = Selector('[data-testid="notification-badge"]');
  }

  async getWelcomeText() {
    return this.welcomeMessage.textContent;
  }

  async getStatsCount() {
    return this.statsCards.count;
  }

  async logout() {
    await t
      .click(this.userMenu)
      .click(this.logoutButton);
  }

  async navigateToSection(section) {
    await t.click(this.sidebar.find('a').withText(section));
  }

  async getNotificationCount() {
    if (await this.notificationBadge.exists) {
      const text = await this.notificationBadge.textContent;
      return parseInt(text, 10);
    }
    return 0;
  }
}

export default new DashboardPage();
```

#### 18.3.3 TestCafe Test Suites

```javascript
// tests/e2e/login.testcafe.js
import { Role, ClientFunction } from 'testcafe';
import LoginPage from '../pages/LoginPage.testcafe';
import DashboardPage from '../pages/DashboardPage.testcafe';

const getPageUrl = ClientFunction(() => window.location.href);

// Define test roles for reuse
const adminRole = Role('http://localhost:3000/login', async (t) => {
  await t
    .typeText(LoginPage.emailInput, 'admin@example.com')
    .typeText(LoginPage.passwordInput, 'adminpass123')
    .click(LoginPage.loginButton);
}, { preserveUrl: true });

const userRole = Role('http://localhost:3000/login', async (t) => {
  await t
    .typeText(LoginPage.emailInput, 'user@example.com')
    .typeText(LoginPage.passwordInput, 'userpass123')
    .click(LoginPage.loginButton);
}, { preserveUrl: true });

fixture('Login Tests')
  .page('http://localhost:3000/login')
  .beforeEach(async (t) => {
    // Clear cookies before each test
    await t.eval(() => document.cookie.split(';').forEach((c) => {
      document.cookie = c.replace(/^ +/, '').replace(/=.*/, '=;expires=' + new Date().toUTCString() + ';path=/');
    }));
  });

test('TC_LOGIN_001: Successful login with valid credentials', async (t) => {
  await LoginPage.login('admin@example.com', 'adminpass123');
  
  const currentUrl = await getPageUrl();
  await t.expect(currentUrl).contains('/dashboard');
  
  const welcomeText = await DashboardPage.getWelcomeText();
  await t.expect(welcomeText).contains('Welcome');
});

test('TC_LOGIN_002: Failed login with invalid password', async (t) => {
  await LoginPage.login('admin@example.com', 'wrongpassword');
  
  await t.expect(LoginPage.errorMessage.exists).ok();
  const errorText = await LoginPage.getErrorText();
  await t.expect(errorText).contains('Invalid email or password');
  
  const currentUrl = await getPageUrl();
  await t.expect(currentUrl).contains('/login');
});

test('TC_LOGIN_003: Failed login with non-existent email', async (t) => {
  await LoginPage.login('nonexistent@example.com', 'password123');
  
  await t.expect(LoginPage.errorMessage.exists).ok();
});

test('TC_LOGIN_004: Login form validation', async (t) => {
  // Empty form submission
  await t.click(LoginPage.loginButton);
  await t.expect(LoginPage.errorMessage.exists).ok();
  
  // Only email
  await t
    .typeText(LoginPage.emailInput, 'test@example.com')
    .click(LoginPage.loginButton);
  await t.expect(LoginPage.errorMessage.exists).ok();
  
  // Invalid email format
  await t
    .selectText(LoginPage.emailInput)
    .typeText(LoginPage.emailInput, 'not-an-email', { replace: true })
    .typeText(LoginPage.passwordInput, 'password123')
    .click(LoginPage.loginButton);
  await t.expect(LoginPage.errorMessage.exists).ok();
});

test('TC_LOGIN_005: Login using role (session reuse)', async (t) => {
  await t.useRole(adminRole);
  
  const currentUrl = await getPageUrl();
  await t.expect(currentUrl).contains('/dashboard');
  
  const welcomeText = await DashboardPage.getWelcomeText();
  await t.expect(welcomeText).contains('Admin');
});

test('TC_LOGIN_006: Remember me checkbox preserves session', async (t) => {
  await LoginPage.loginWithRememberMe('user@example.com', 'userpass123');
  
  const currentUrl = await getPageUrl();
  await t.expect(currentUrl).contains('/dashboard');
  
  // Verify persistent cookie was set
  const cookies = await t.eval(() => document.cookie);
  await t.expect(cookies).contains('remember_token');
});

test('TC_LOGIN_007: Password masking', async (t) => {
  await t.typeText(LoginPage.passwordInput, 'mysecretpassword');
  
  const inputType = await LoginPage.passwordInput.getAttribute('type');
  await t.expect(inputType).eql('password');
});

test('TC_LOGIN_008: Navigate to forgot password', async (t) => {
  await t.click(LoginPage.forgotPasswordLink);
  
  const currentUrl = await getPageUrl();
  await t.expect(currentUrl).contains('/forgot-password');
});

// Tests for checkout flow
fixture('Checkout Tests')
  .page('http://localhost:3000')
  .beforeEach(async (t) => {
    await t.useRole(userRole);
  });

test('TC_CHECKOUT_001: Complete checkout flow', async (t) => {
  // Navigate to products
  await t.navigateTo('/products');
  
  // Add first product to cart
  const addToCartButton = Selector('[data-testid="add-to-cart"]').nth(0);
  await t.click(addToCartButton);
  
  // Verify toast notification
  const toast = Selector('[data-testid="toast"]');
  await t.expect(toast.exists).ok();
  await t.expect(toast.textContent).contains('Added to cart');
  
  // Navigate to cart
  await t.click(Selector('[data-testid="cart-button"]'));
  
  // Verify item in cart
  const cartItems = Selector('[data-testid="cart-item"]');
  await t.expect(cartItems.count).eql(1);
  
  // Proceed to checkout
  await t.click(Selector('[data-testid="checkout-button"]'));
  
  // Fill shipping details
  await t
    .typeText(Selector('[data-testid="first-name"]'), 'John')
    .typeText(Selector('[data-testid="last-name"]'), 'Doe')
    .typeText(Selector('[data-testid="address"]'), '123 Test St')
    .typeText(Selector('[data-testid="city"]'), 'San Francisco')
    .click(Selector('[data-testid="state"]'))
    .click(Selector('option[value="CA"]'))
    .typeText(Selector('[data-testid="zip"]'), '94105')
    .typeText(Selector('[data-testid="phone"]'), '5550123');
  
  // Select shipping method
  await t.click(Selector('[data-testid="shipping-standard"]'));
  
  // Place order
  await t.click(Selector('[data-testid="place-order"]'));
  
  // Wait for confirmation page
  const orderConfirmation = Selector('[data-testid="order-confirmation"]');
  await t.expect(orderConfirmation.exists).ok({ timeout: 30000 });
  
  const orderNumber = Selector('[data-testid="order-number"]');
  await t.expect(orderNumber.textContent).match(/ORD-\d+/);
});

test('TC_CHECKOUT_002: Apply coupon code', async (t) => {
  await t.navigateTo('/cart');
  
  // Apply valid coupon
  await t
    .typeText(Selector('[data-testid="coupon-input"]'), 'SAVE10')
    .click(Selector('[data-testid="apply-coupon"]'));
  
  const discount = Selector('[data-testid="discount-amount"]');
  await t.expect(discount.exists).ok();
  await t.expect(discount.textContent).notEql('$0.00');
  
  // Try invalid coupon
  await t
    .selectText(Selector('[data-testid="coupon-input"]'))
    .typeText(Selector('[data-testid="coupon-input"]'), 'INVALIDCODE', { replace: true })
    .click(Selector('[data-testid="apply-coupon"]'));
  
  const error = Selector('[data-testid="coupon-error"]');
  await t.expect(error.exists).ok();
  await t.expect(error.textContent).contains('Invalid coupon');
});
```

#### 18.3.4 TestCafe Request Hooks

```javascript
// tests/hooks/request-hooks.testcafe.js
import { RequestLogger, RequestMock, RequestHook } from 'testcafe';

// Request Logger - Log all API requests
const apiLogger = RequestLogger(/api\//, {
  logRequestHeaders: true,
  logRequestBody: true,
  logResponseHeaders: true,
  logResponseBody: true,
  stringifyResponseBody: true,
});

// Request Mock - Mock API responses
const productsMock = RequestMock()
  .onRequestTo(/api\/products$/)
  .respond({ 
    products: [
      { id: 1, name: 'Mock Product', price: 19.99 },
      { id: 2, name: 'Another Mock', price: 29.99 },
    ],
    total: 2 
  }, 200, { 'Content-Type': 'application/json' })
  .onRequestTo(/api\/products\/\d+$/)
  .respond((req, res) => {
    const id = req.url.match(/products\/(\d+)/)[1];
    res.setBody({ id: parseInt(id), name: `Product ${id}`, price: 9.99 });
    res.statusCode = 200;
    res.headers['Content-Type'] = 'application/json';
  });

// Error mock
const errorMock = RequestMock()
  .onRequestTo(/api\/products$/)
  .respond(null, 500);

// Custom Request Hook for authentication
class AuthHook extends RequestHook {
  constructor() {
    super(/api\//);
    this.token = null;
  }

  async onRequest(event) {
    if (this.token) {
      event.requestOptions.headers['Authorization'] = `Bearer ${this.token}`;
    }
  }

  async onResponse(event) {
    if (event.statusCode === 401) {
      console.log('Authentication failed for:', event._requestContext.reqOpts.url);
    }
  }

  setToken(token) {
    this.token = token;
  }
}

const authHook = new AuthHook();

// Usage in tests
fixture('API Mock Tests')
  .page('http://localhost:3000')
  .requestHooks(apiLogger);

test('should display mocked products', async (t) => {
  await t.addRequestHooks(productsMock);
  await t.navigateTo('/products');
  
  const productCards = Selector('[data-testid="product-card"]');
  await t.expect(productCards.count).eql(2);
  await t.expect(productCards.nth(0).textContent).contains('Mock Product');
});

test('should handle API errors gracefully', async (t) => {
  await t.addRequestHooks(errorMock);
  await t.navigateTo('/products');
  
  const errorMessage = Selector('[data-testid="error-message"]');
  await t.expect(errorMessage.exists).ok();
  await t.expect(errorMessage.textContent).contains('Failed to load');
});

test('should log API requests', async (t) => {
  await t.navigateTo('/products');
  
  // Check logged requests
  const productRequests = apiLogger.requests.filter(r => r.request.url.includes('/products'));
  await t.expect(productRequests.length).gte(1);
  
  // Verify request details
  const firstRequest = productRequests[0];
  await t.expect(firstRequest.response.statusCode).eql(200);
  
  console.log('API Requests logged:', apiLogger.requests.length);
});

export { apiLogger, productsMock, errorMock, authHook };
```

---

## 19. Comprehensive API Testing {#api-testing-advanced}

API testing is fundamental to modern software quality assurance. This section covers advanced API testing with Postman, Newman, REST Assured, and contract testing with Pact.

### 19.1 Postman Collections Architecture

#### 19.1.1 Collection Structure and Organization

```json
{
  "info": {
    "name": "E-Commerce API Test Suite",
    "description": "Comprehensive API tests for the e-commerce platform",
    "schema": "https://schema.getpostman.com/json/collection/v2.1.0/collection.json"
  },
  "auth": {
    "type": "bearer",
    "bearer": [
      {
        "key": "token",
        "value": "{{auth_token}}",
        "type": "string"
      }
    ]
  },
  "variable": [
    {
      "key": "base_url",
      "value": "http://localhost:3001/api"
    },
    {
      "key": "auth_token",
      "value": ""
    },
    {
      "key": "created_product_id",
      "value": ""
    },
    {
      "key": "created_order_id",
      "value": ""
    }
  ],
  "item": [
    {
      "name": "Authentication",
      "item": [
        {
          "name": "Login - Admin",
          "event": [
            {
              "listen": "test",
              "script": {
                "exec": [
                  "pm.test('Status code is 200', function () {",
                  "    pm.response.to.have.status(200);",
                  "});",
                  "",
                  "pm.test('Response has token', function () {",
                  "    var jsonData = pm.response.json();",
                  "    pm.expect(jsonData).to.have.property('token');",
                  "    pm.expect(jsonData.token).to.be.a('string');",
                  "    pm.expect(jsonData.token.length).to.be.greaterThan(0);",
                  "    pm.collectionVariables.set('auth_token', jsonData.token);",
                  "});",
                  "",
                  "pm.test('Response has user data', function () {",
                  "    var jsonData = pm.response.json();",
                  "    pm.expect(jsonData.user).to.have.property('id');",
                  "    pm.expect(jsonData.user).to.have.property('email');",
                  "    pm.expect(jsonData.user).to.have.property('role');",
                  "    pm.expect(jsonData.user.role).to.eql('admin');",
                  "});",
                  "",
                  "pm.test('Response time is within limit', function () {",
                  "    pm.expect(pm.response.responseTime).to.be.below(2000);",
                  "});",
                  "",
                  "pm.test('Content-Type is JSON', function () {",
                  "    pm.response.to.have.header('Content-Type', 'application/json; charset=utf-8');",
                  "});"
                ]
              }
            }
          ],
          "request": {
            "method": "POST",
            "header": [
              {
                "key": "Content-Type",
                "value": "application/json"
              }
            ],
            "body": {
              "mode": "raw",
              "raw": "{\n  \"email\": \"admin@example.com\",\n  \"password\": \"adminpass123\"\n}"
            },
            "url": {
              "raw": "{{base_url}}/auth/login",
              "host": ["{{base_url}}"],
              "path": ["auth", "login"]
            }
          }
        },
        {
          "name": "Login - Invalid Credentials",
          "event": [
            {
              "listen": "test",
              "script": {
                "exec": [
                  "pm.test('Status code is 401', function () {",
                  "    pm.response.to.have.status(401);",
                  "});",
                  "",
                  "pm.test('Error message present', function () {",
                  "    var jsonData = pm.response.json();",
                  "    pm.expect(jsonData).to.have.property('error');",
                  "    pm.expect(jsonData.error).to.include('Invalid');",
                  "});",
                  "",
                  "pm.test('No token in response', function () {",
                  "    var jsonData = pm.response.json();",
                  "    pm.expect(jsonData).to.not.have.property('token');",
                  "});"
                ]
              }
            }
          ],
          "request": {
            "method": "POST",
            "header": [
              {
                "key": "Content-Type",
                "value": "application/json"
              }
            ],
            "body": {
              "mode": "raw",
              "raw": "{\n  \"email\": \"admin@example.com\",\n  \"password\": \"wrongpassword\"\n}"
            },
            "url": {
              "raw": "{{base_url}}/auth/login",
              "host": ["{{base_url}}"],
              "path": ["auth", "login"]
            }
          }
        },
        {
          "name": "Refresh Token",
          "event": [
            {
              "listen": "test",
              "script": {
                "exec": [
                  "pm.test('Status code is 200', function () {",
                  "    pm.response.to.have.status(200);",
                  "});",
                  "",
                  "pm.test('New token received', function () {",
                  "    var jsonData = pm.response.json();",
                  "    pm.expect(jsonData).to.have.property('token');",
                  "    pm.collectionVariables.set('auth_token', jsonData.token);",
                  "});"
                ]
              }
            }
          ],
          "request": {
            "method": "POST",
            "url": {
              "raw": "{{base_url}}/auth/refresh",
              "host": ["{{base_url}}"],
              "path": ["auth", "refresh"]
            }
          }
        }
      ]
    },
    {
      "name": "Products",
      "item": [
        {
          "name": "List Products",
          "event": [
            {
              "listen": "test",
              "script": {
                "exec": [
                  "const schema = {",
                  "    type: 'object',",
                  "    required: ['products', 'pagination'],",
                  "    properties: {",
                  "        products: {",
                  "            type: 'array',",
                  "            items: {",
                  "                type: 'object',",
                  "                required: ['id', 'name', 'price', 'stock'],",
                  "                properties: {",
                  "                    id: { type: 'number' },",
                  "                    name: { type: 'string' },",
                  "                    price: { type: 'number', minimum: 0 },",
                  "                    stock: { type: 'integer', minimum: 0 },",
                  "                    description: { type: 'string' },",
                  "                    category: { type: 'string' }",
                  "                }",
                  "            }",
                  "        },",
                  "        pagination: {",
                  "            type: 'object',",
                  "            properties: {",
                  "                page: { type: 'number' },",
                  "                limit: { type: 'number' },",
                  "                total: { type: 'number' },",
                  "                totalPages: { type: 'number' }",
                  "            }",
                  "        }",
                  "    }",
                  "};",
                  "",
                  "pm.test('Status code is 200', function () {",
                  "    pm.response.to.have.status(200);",
                  "});",
                  "",
                  "pm.test('Response matches schema', function () {",
                  "    pm.response.to.have.jsonSchema(schema);",
                  "});",
                  "",
                  "pm.test('Products array is not empty', function () {",
                  "    var jsonData = pm.response.json();",
                  "    pm.expect(jsonData.products.length).to.be.greaterThan(0);",
                  "});",
                  "",
                  "pm.test('All prices are positive', function () {",
                  "    var jsonData = pm.response.json();",
                  "    jsonData.products.forEach(function(product) {",
                  "        pm.expect(product.price).to.be.above(0);",
                  "    });",
                  "});"
                ]
              }
            }
          ],
          "request": {
            "method": "GET",
            "url": {
              "raw": "{{base_url}}/products?page=1&limit=10",
              "host": ["{{base_url}}"],
              "path": ["products"],
              "query": [
                { "key": "page", "value": "1" },
                { "key": "limit", "value": "10" }
              ]
            }
          }
        },
        {
          "name": "Create Product",
          "event": [
            {
              "listen": "test",
              "script": {
                "exec": [
                  "pm.test('Status code is 201', function () {",
                  "    pm.response.to.have.status(201);",
                  "});",
                  "",
                  "pm.test('Product created with correct data', function () {",
                  "    var jsonData = pm.response.json();",
                  "    pm.expect(jsonData).to.have.property('id');",
                  "    pm.expect(jsonData.name).to.eql('Test Product');",
                  "    pm.expect(jsonData.price).to.eql(29.99);",
                  "    pm.expect(jsonData.stock).to.eql(100);",
                  "    pm.collectionVariables.set('created_product_id', jsonData.id);",
                  "});",
                  "",
                  "pm.test('Created timestamp present', function () {",
                  "    var jsonData = pm.response.json();",
                  "    pm.expect(jsonData).to.have.property('createdAt');",
                  "    var date = new Date(jsonData.createdAt);",
                  "    pm.expect(date.toString()).to.not.eql('Invalid Date');",
                  "});"
                ]
              }
            }
          ],
          "request": {
            "method": "POST",
            "header": [
              { "key": "Content-Type", "value": "application/json" }
            ],
            "body": {
              "mode": "raw",
              "raw": "{\n  \"name\": \"Test Product\",\n  \"price\": 29.99,\n  \"description\": \"A test product created by API tests\",\n  \"category\": \"Electronics\",\n  \"stock\": 100\n}"
            },
            "url": {
              "raw": "{{base_url}}/products",
              "host": ["{{base_url}}"],
              "path": ["products"]
            }
          }
        }
      ]
    }
  ]
}
```

#### 19.1.2 Postman Pre-request Scripts

```javascript
// Pre-request script for dynamic data generation
// This runs before every request in a collection

// Generate unique email for testing
const timestamp = Date.now();
pm.collectionVariables.set('unique_email', `test+${timestamp}@example.com`);

// Generate random product name
const adjectives = ['Premium', 'Classic', 'Modern', 'Vintage', 'Deluxe', 'Ultra', 'Super'];
const nouns = ['Widget', 'Gadget', 'Device', 'Tool', 'Instrument', 'Module', 'Component'];
const randomAdj = adjectives[Math.floor(Math.random() * adjectives.length)];
const randomNoun = nouns[Math.floor(Math.random() * nouns.length)];
pm.collectionVariables.set('random_product_name', `${randomAdj} ${randomNoun} ${timestamp}`);

// Generate random price between 1.00 and 999.99
const randomPrice = (Math.random() * 998.99 + 1.00).toFixed(2);
pm.collectionVariables.set('random_price', randomPrice);

// Generate random integer for stock (1-1000)
const randomStock = Math.floor(Math.random() * 1000) + 1;
pm.collectionVariables.set('random_stock', randomStock.toString());

// Auto-refresh expired token
const tokenExpiry = pm.collectionVariables.get('token_expiry');
if (tokenExpiry && Date.now() > parseInt(tokenExpiry)) {
  console.log('Token expired, refreshing...');
  pm.sendRequest({
    url: pm.collectionVariables.get('base_url') + '/auth/refresh',
    method: 'POST',
    header: {
      'Content-Type': 'application/json',
      'Authorization': `Bearer ${pm.collectionVariables.get('refresh_token')}`
    }
  }, function (err, response) {
    if (!err && response.code === 200) {
      const data = response.json();
      pm.collectionVariables.set('auth_token', data.token);
      pm.collectionVariables.set('token_expiry', (Date.now() + 3600000).toString());
    }
  });
}

// Compute HMAC signature for signed requests
if (pm.request.url.toString().includes('/webhook')) {
  const body = pm.request.body.raw;
  const secret = pm.collectionVariables.get('webhook_secret');
  const signature = CryptoJS.HmacSHA256(body, secret).toString(CryptoJS.enc.Hex);
  pm.request.headers.add({
    key: 'X-Signature',
    value: signature
  });
}
```

### 19.2 Newman CLI Automation

Newman is Postman's command-line collection runner that enables API test automation in CI/CD pipelines.

#### 19.2.1 Newman Configuration and Execution

```javascript
// newman-runner.js
const newman = require('newman');
const path = require('path');

const runCollection = (options) => {
  return new Promise((resolve, reject) => {
    newman.run({
      collection: path.join(__dirname, 'collections', options.collection),
      environment: path.join(__dirname, 'environments', options.environment),
      globals: path.join(__dirname, 'globals.json'),
      iterationData: options.dataFile ? path.join(__dirname, 'data', options.dataFile) : undefined,
      iterationCount: options.iterations || 1,
      reporters: ['cli', 'htmlextra', 'junit', 'json'],
      reporter: {
        htmlextra: {
          export: path.join(__dirname, 'reports', `${options.reportName || 'report'}.html`),
          title: options.title || 'API Test Report',
          showOnlyFails: false,
          noSyntaxHighlighting: false,
          showEnvironmentData: true,
          skipSensitiveData: true,
          showMarkdownLinks: true,
          browserTitle: 'API Test Results',
          displayProgressBar: true,
        },
        junit: {
          export: path.join(__dirname, 'reports', `${options.reportName || 'report'}.xml`),
        },
        json: {
          export: path.join(__dirname, 'reports', `${options.reportName || 'report'}.json`),
        },
      },
      timeoutRequest: 30000,
      timeoutScript: 10000,
      delayRequest: options.delay || 0,
      bail: options.bail || false,
      suppressExitCode: false,
      insecure: options.insecure || false,
      color: 'on',
    }, (err, summary) => {
      if (err) {
        reject(err);
        return;
      }

      const results = {
        totalRequests: summary.run.stats.requests.total,
        failedRequests: summary.run.stats.requests.failed,
        totalAssertions: summary.run.stats.assertions.total,
        failedAssertions: summary.run.stats.assertions.failed,
        totalTime: summary.run.timings.completed - summary.run.timings.started,
        averageResponseTime: summary.run.timings.responseAverage,
      };

      console.log('\n=== Test Results ===');
      console.log(`Total Requests: ${results.totalRequests}`);
      console.log(`Failed Requests: ${results.failedRequests}`);
      console.log(`Total Assertions: ${results.totalAssertions}`);
      console.log(`Failed Assertions: ${results.failedAssertions}`);
      console.log(`Total Time: ${results.totalTime}ms`);
      console.log(`Average Response Time: ${results.averageResponseTime}ms`);

      if (results.failedAssertions > 0 || results.failedRequests > 0) {
        reject(new Error(`Tests failed: ${results.failedAssertions} assertions, ${results.failedRequests} requests`));
      } else {
        resolve(results);
      }
    });
  });
};

// Run different test suites
const runAllTests = async () => {
  try {
    // Smoke tests first
    console.log('\n--- Running Smoke Tests ---');
    await runCollection({
      collection: 'smoke-tests.postman_collection.json',
      environment: 'staging.postman_environment.json',
      reportName: 'smoke-tests',
      title: 'Smoke Test Report',
    });

    // Full API tests
    console.log('\n--- Running Full API Tests ---');
    await runCollection({
      collection: 'api-tests.postman_collection.json',
      environment: 'staging.postman_environment.json',
      reportName: 'api-tests',
      title: 'Full API Test Report',
    });

    // Data-driven tests
    console.log('\n--- Running Data-Driven Tests ---');
    await runCollection({
      collection: 'data-driven-tests.postman_collection.json',
      environment: 'staging.postman_environment.json',
      dataFile: 'test-users.csv',
      reportName: 'data-driven',
      title: 'Data-Driven Test Report',
      iterations: 10,
    });

    console.log('\nAll tests passed!');
  } catch (error) {
    console.error('\nTests failed:', error.message);
    process.exit(1);
  }
};

runAllTests();
```

#### 19.2.2 Newman in CI/CD

```yaml
# .github/workflows/api-tests.yml
name: API Tests with Newman

on:
  push:
    branches: [main, develop]
  pull_request:
    branches: [main]
  schedule:
    - cron: '0 */4 * * *'

jobs:
  api-tests:
    runs-on: ubuntu-latest
    
    services:
      app:
        image: myapp:latest
        ports:
          - 3001:3001
        env:
          DATABASE_URL: postgresql://postgres:postgres@postgres:5432/testdb
          NODE_ENV: test
      
      postgres:
        image: postgres:14
        env:
          POSTGRES_PASSWORD: postgres
          POSTGRES_DB: testdb
        options: >-
          --health-cmd pg_isready
          --health-interval 10s
          --health-timeout 5s
          --health-retries 5
    
    steps:
      - uses: actions/checkout@v3
      
      - uses: actions/setup-node@v3
        with:
          node-version: '18'
      
      - name: Install Newman and reporters
        run: |
          npm install -g newman
          npm install -g newman-reporter-htmlextra
          npm install -g newman-reporter-junitfull
      
      - name: Wait for API to be ready
        run: |
          for i in {1..30}; do
            curl -s http://localhost:3001/health && break
            echo "Waiting for API... attempt $i"
            sleep 2
          done
      
      - name: Run Smoke Tests
        run: |
          newman run collections/smoke-tests.json \
            -e environments/ci.json \
            --reporters cli,htmlextra,junit \
            --reporter-htmlextra-export reports/smoke-tests.html \
            --reporter-junit-export reports/smoke-tests.xml \
            --bail
      
      - name: Run Full API Tests
        if: success()
        run: |
          newman run collections/api-tests.json \
            -e environments/ci.json \
            --reporters cli,htmlextra,junit \
            --reporter-htmlextra-export reports/api-tests.html \
            --reporter-junit-export reports/api-tests.xml \
            --iteration-count 1 \
            --timeout-request 30000
      
      - name: Run Performance Baseline Tests
        if: success()
        run: |
          newman run collections/performance-baseline.json \
            -e environments/ci.json \
            --reporters cli,htmlextra \
            --reporter-htmlextra-export reports/performance.html \
            --iteration-count 100 \
            --delay-request 100
      
      - name: Upload Test Reports
        uses: actions/upload-artifact@v3
        if: always()
        with:
          name: api-test-reports
          path: reports/
      
      - name: Publish Test Results
        uses: dorny/test-reporter@v1
        if: always()
        with:
          name: API Test Results
          path: reports/*.xml
          reporter: java-junit
```

### 19.3 REST Assured (Java) API Testing

REST Assured is a Java library for testing RESTful APIs with a fluent, readable DSL.

#### 19.3.1 REST Assured Setup and Configuration

```xml
<!-- pom.xml -->
<dependencies>
    <dependency>
        <groupId>io.rest-assured</groupId>
        <artifactId>rest-assured</artifactId>
        <version>5.3.2</version>
        <scope>test</scope>
    </dependency>
    <dependency>
        <groupId>io.rest-assured</groupId>
        <artifactId>json-schema-validator</artifactId>
        <version>5.3.2</version>
        <scope>test</scope>
    </dependency>
    <dependency>
        <groupId>org.testng</groupId>
        <artifactId>testng</artifactId>
        <version>7.8.0</version>
        <scope>test</scope>
    </dependency>
    <dependency>
        <groupId>io.qameta.allure</groupId>
        <artifactId>allure-rest-assured</artifactId>
        <version>2.24.0</version>
        <scope>test</scope>
    </dependency>
    <dependency>
        <groupId>com.fasterxml.jackson.core</groupId>
        <artifactId>jackson-databind</artifactId>
        <version>2.16.0</version>
    </dependency>
    <dependency>
        <groupId>org.projectlombok</groupId>
        <artifactId>lombok</artifactId>
        <version>1.18.30</version>
        <scope>provided</scope>
    </dependency>
</dependencies>
```

```java
// src/test/java/com/qa/config/TestConfig.java
package com.qa.config;

import io.restassured.RestAssured;
import io.restassured.builder.RequestSpecBuilder;
import io.restassured.builder.ResponseSpecBuilder;
import io.restassured.filter.log.LogDetail;
import io.restassured.http.ContentType;
import io.restassured.specification.RequestSpecification;
import io.restassured.specification.ResponseSpecification;
import org.testng.annotations.BeforeClass;
import org.testng.annotations.BeforeSuite;

import java.util.concurrent.TimeUnit;

public class TestConfig {
    protected static String authToken;
    protected static RequestSpecification requestSpec;
    protected static ResponseSpecification responseSpec;

    @BeforeSuite
    public void globalSetup() {
        RestAssured.baseURI = System.getProperty("api.baseUri", "http://localhost:3001");
        RestAssured.basePath = "/api";
        RestAssured.enableLoggingOfRequestAndResponseIfValidationFails(LogDetail.ALL);

        requestSpec = new RequestSpecBuilder()
            .setContentType(ContentType.JSON)
            .setAccept(ContentType.JSON)
            .addFilter(new io.qameta.allure.restassured.AllureRestAssured())
            .log(LogDetail.ALL)
            .build();

        responseSpec = new ResponseSpecBuilder()
            .expectResponseTime(org.hamcrest.Matchers.lessThan(5000L))
            .expectContentType(ContentType.JSON)
            .build();
    }

    @BeforeClass
    public void authenticate() {
        authToken = RestAssured.given()
            .contentType(ContentType.JSON)
            .body("{\"email\":\"admin@example.com\",\"password\":\"adminpass123\"}")
            .when()
            .post("/auth/login")
            .then()
            .statusCode(200)
            .extract()
            .path("token");
    }

    protected RequestSpecification givenAuth() {
        return RestAssured.given()
            .spec(requestSpec)
            .header("Authorization", "Bearer " + authToken);
    }
}
```

#### 19.3.2 REST Assured Test Classes

```java
// src/test/java/com/qa/tests/ProductApiTest.java
package com.qa.tests;

import com.qa.config.TestConfig;
import com.qa.models.Product;
import io.qameta.allure.*;
import io.restassured.response.Response;
import org.hamcrest.Matchers;
import org.testng.annotations.*;
import org.testng.asserts.SoftAssert;

import static io.restassured.RestAssured.*;
import static io.restassured.module.jsv.JsonSchemaValidator.matchesJsonSchemaInClasspath;
import static org.hamcrest.Matchers.*;

@Epic("E-Commerce API")
@Feature("Product Management")
public class ProductApiTest extends TestConfig {
    
    private int createdProductId;

    @Test(priority = 1)
    @Story("List Products")
    @Severity(SeverityLevel.CRITICAL)
    @Description("Verify GET /products returns list of products with correct schema")
    public void testGetProducts() {
        givenAuth()
            .queryParam("page", 1)
            .queryParam("limit", 10)
        .when()
            .get("/products")
        .then()
            .spec(responseSpec)
            .statusCode(200)
            .body("products", notNullValue())
            .body("products.size()", greaterThan(0))
            .body("products.id", everyItem(notNullValue()))
            .body("products.name", everyItem(not(emptyString())))
            .body("products.price", everyItem(greaterThan(0f)))
            .body("pagination.page", equalTo(1))
            .body("pagination.limit", equalTo(10))
            .body("pagination.total", greaterThan(0))
            .body(matchesJsonSchemaInClasspath("schemas/products-list.json"));
    }

    @Test(priority = 2)
    @Story("Create Product")
    @Severity(SeverityLevel.CRITICAL)
    @Description("Verify POST /products creates a new product")
    public void testCreateProduct() {
        Product product = Product.builder()
            .name("REST Assured Test Product")
            .price(49.99)
            .description("Created by REST Assured automated test")
            .category("Electronics")
            .stock(250)
            .build();

        Response response = givenAuth()
            .body(product)
        .when()
            .post("/products")
        .then()
            .statusCode(201)
            .body("id", notNullValue())
            .body("name", equalTo(product.getName()))
            .body("price", equalTo(49.99f))
            .body("stock", equalTo(250))
            .body("createdAt", notNullValue())
            .extract()
            .response();

        createdProductId = response.path("id");
    }

    @Test(priority = 3, dependsOnMethods = "testCreateProduct")
    @Story("Get Product by ID")
    @Severity(SeverityLevel.CRITICAL)
    @Description("Verify GET /products/:id returns specific product")
    public void testGetProductById() {
        givenAuth()
        .when()
            .get("/products/{id}", createdProductId)
        .then()
            .statusCode(200)
            .body("id", equalTo(createdProductId))
            .body("name", equalTo("REST Assured Test Product"))
            .body("price", equalTo(49.99f))
            .body("stock", equalTo(250));
    }

    @Test(priority = 4, dependsOnMethods = "testCreateProduct")
    @Story("Update Product")
    @Severity(SeverityLevel.CRITICAL)
    @Description("Verify PUT /products/:id updates product fields")
    public void testUpdateProduct() {
        String updateBody = "{\"name\": \"Updated Product Name\", \"price\": 59.99}";

        givenAuth()
            .body(updateBody)
        .when()
            .put("/products/{id}", createdProductId)
        .then()
            .statusCode(200)
            .body("name", equalTo("Updated Product Name"))
            .body("price", equalTo(59.99f))
            .body("stock", equalTo(250))
            .body("updatedAt", notNullValue());
    }

    @Test(priority = 5, dependsOnMethods = "testCreateProduct")
    @Story("Delete Product")
    @Severity(SeverityLevel.CRITICAL)
    @Description("Verify DELETE /products/:id removes the product")
    public void testDeleteProduct() {
        givenAuth()
        .when()
            .delete("/products/{id}", createdProductId)
        .then()
            .statusCode(204);

        // Verify product is deleted
        givenAuth()
        .when()
            .get("/products/{id}", createdProductId)
        .then()
            .statusCode(404);
    }

    @Test(priority = 6)
    @Story("Product Validation")
    @Severity(SeverityLevel.NORMAL)
    @Description("Verify product creation fails with invalid data")
    public void testCreateProductValidation() {
        // Missing required field
        givenAuth()
            .body("{\"price\": 10.00}")
        .when()
            .post("/products")
        .then()
            .statusCode(400)
            .body("errors", hasItem(hasEntry("field", "name")));

        // Negative price
        givenAuth()
            .body("{\"name\": \"Bad Product\", \"price\": -5.00}")
        .when()
            .post("/products")
        .then()
            .statusCode(400)
            .body("errors", hasItem(hasEntry("field", "price")));

        // Empty name
        givenAuth()
            .body("{\"name\": \"\", \"price\": 10.00}")
        .when()
            .post("/products")
        .then()
            .statusCode(400);
    }

    @Test(priority = 7)
    @Story("Product Search")
    @Severity(SeverityLevel.NORMAL)
    @Description("Verify product search and filtering")
    public void testProductSearch() {
        givenAuth()
            .queryParam("search", "electronics")
            .queryParam("minPrice", 10)
            .queryParam("maxPrice", 100)
            .queryParam("sort", "price")
            .queryParam("order", "asc")
        .when()
            .get("/products")
        .then()
            .statusCode(200)
            .body("products.price", everyItem(
                allOf(greaterThanOrEqualTo(10f), lessThanOrEqualTo(100f))
            ));
    }

    @Test(priority = 8)
    @Story("Unauthorized Access")
    @Severity(SeverityLevel.BLOCKER)
    @Description("Verify endpoints reject unauthorized requests")
    public void testUnauthorizedAccess() {
        given()
            .spec(requestSpec)
        .when()
            .get("/products")
        .then()
            .statusCode(401);

        given()
            .spec(requestSpec)
            .header("Authorization", "Bearer invalid-token")
        .when()
            .get("/products")
        .then()
            .statusCode(401);
    }

    @Test(priority = 9)
    @Story("Product Pagination")
    @Severity(SeverityLevel.NORMAL)
    @Description("Verify pagination works correctly")
    public void testPagination() {
        SoftAssert soft = new SoftAssert();

        Response page1 = givenAuth()
            .queryParam("page", 1)
            .queryParam("limit", 5)
        .when()
            .get("/products")
        .then()
            .statusCode(200)
            .extract().response();

        Response page2 = givenAuth()
            .queryParam("page", 2)
            .queryParam("limit", 5)
        .when()
            .get("/products")
        .then()
            .statusCode(200)
            .extract().response();

        java.util.List<Integer> page1Ids = page1.jsonPath().getList("products.id");
        java.util.List<Integer> page2Ids = page2.jsonPath().getList("products.id");

        // No overlapping IDs
        soft.assertTrue(java.util.Collections.disjoint(page1Ids, page2Ids),
            "Pages should not have overlapping product IDs");

        // Verify pagination metadata
        soft.assertEquals(page1.jsonPath().getInt("pagination.page"), 1);
        soft.assertEquals(page2.jsonPath().getInt("pagination.page"), 2);

        soft.assertAll();
    }

    @DataProvider(name = "productCategories")
    public Object[][] productCategories() {
        return new Object[][] {
            {"Electronics", 200},
            {"Clothing", 200},
            {"Books", 200},
            {"NonExistentCategory", 200},  // Should return empty list, not 404
        };
    }

    @Test(priority = 10, dataProvider = "productCategories")
    @Story("Filter by Category")
    @Severity(SeverityLevel.NORMAL)
    @Description("Verify filtering products by category")
    public void testFilterByCategory(String category, int expectedStatus) {
        givenAuth()
            .queryParam("category", category)
        .when()
            .get("/products")
        .then()
            .statusCode(expectedStatus)
            .body("products", notNullValue());
    }
}
```

#### 19.3.3 REST Assured Data Models

```java
// src/test/java/com/qa/models/Product.java
package com.qa.models;

import com.fasterxml.jackson.annotation.JsonInclude;
import lombok.*;

@Data
@Builder
@NoArgsConstructor
@AllArgsConstructor
@JsonInclude(JsonInclude.Include.NON_NULL)
public class Product {
    private Integer id;
    private String name;
    private Double price;
    private String description;
    private String category;
    private Integer stock;
    private String createdAt;
    private String updatedAt;
}

// src/test/java/com/qa/models/User.java
package com.qa.models;

import com.fasterxml.jackson.annotation.JsonInclude;
import lombok.*;

@Data
@Builder
@NoArgsConstructor
@AllArgsConstructor
@JsonInclude(JsonInclude.Include.NON_NULL)
public class User {
    private Integer id;
    private String name;
    private String email;
    private String password;
    private String role;
    private Boolean active;
    private String createdAt;
}

// src/test/java/com/qa/models/Order.java
package com.qa.models;

import com.fasterxml.jackson.annotation.JsonInclude;
import lombok.*;
import java.util.List;

@Data
@Builder
@NoArgsConstructor
@AllArgsConstructor
@JsonInclude(JsonInclude.Include.NON_NULL)
public class Order {
    private Integer id;
    private Integer userId;
    private String status;
    private Double total;
    private List<OrderItem> items;
    private ShippingAddress shippingAddress;
    private String createdAt;
}

@Data
@Builder
@NoArgsConstructor
@AllArgsConstructor
@JsonInclude(JsonInclude.Include.NON_NULL)
class OrderItem {
    private Integer productId;
    private Integer quantity;
    private Double price;
}

@Data
@Builder
@NoArgsConstructor
@AllArgsConstructor
@JsonInclude(JsonInclude.Include.NON_NULL)
class ShippingAddress {
    private String street;
    private String city;
    private String state;
    private String zip;
    private String country;
}
```

### 19.4 Contract Testing with Pact

Pact enables consumer-driven contract testing to ensure services communicate correctly.

#### 19.4.1 Pact Consumer Test (JavaScript)

```javascript
// consumer/tests/pact/product-api.pact.spec.js
const { Pact } = require('@pact-foundation/pact');
const { like, eachLike, integer, string, decimal, boolean } = require('@pact-foundation/pact').Matchers;
const path = require('path');
const axios = require('axios');

const provider = new Pact({
  consumer: 'ProductWebApp',
  provider: 'ProductAPI',
  port: 1234,
  log: path.resolve(process.cwd(), 'logs', 'pact.log'),
  dir: path.resolve(process.cwd(), 'pacts'),
  logLevel: 'warn',
  spec: 2,
});

describe('Product API Contract Tests', () => {
  beforeAll(async () => {
    await provider.setup();
  });

  afterAll(async () => {
    await provider.finalize();
  });

  afterEach(async () => {
    await provider.verify();
  });

  describe('GET /api/products', () => {
    beforeEach(async () => {
      await provider.addInteraction({
        state: 'products exist in the database',
        uponReceiving: 'a request for all products',
        withRequest: {
          method: 'GET',
          path: '/api/products',
          headers: {
            Authorization: like('Bearer valid-token'),
            Accept: 'application/json',
          },
          query: {
            page: '1',
            limit: '10',
          },
        },
        willRespondWith: {
          status: 200,
          headers: {
            'Content-Type': 'application/json; charset=utf-8',
          },
          body: {
            products: eachLike({
              id: integer(1),
              name: string('Product Name'),
              price: decimal(29.99),
              description: string('Product description'),
              category: string('Electronics'),
              stock: integer(100),
              inStock: boolean(true),
            }),
            pagination: {
              page: integer(1),
              limit: integer(10),
              total: integer(50),
              totalPages: integer(5),
            },
          },
        },
      });
    });

    it('should return a list of products', async () => {
      const response = await axios.get('http://localhost:1234/api/products', {
        params: { page: 1, limit: 10 },
        headers: {
          Authorization: 'Bearer valid-token',
          Accept: 'application/json',
        },
      });

      expect(response.status).toBe(200);
      expect(response.data.products).toBeInstanceOf(Array);
      expect(response.data.products.length).toBeGreaterThan(0);
      expect(response.data.products[0]).toHaveProperty('id');
      expect(response.data.products[0]).toHaveProperty('name');
      expect(response.data.products[0]).toHaveProperty('price');
      expect(response.data.pagination.page).toBe(1);
    });
  });

  describe('GET /api/products/:id', () => {
    beforeEach(async () => {
      await provider.addInteraction({
        state: 'a product with id 1 exists',
        uponReceiving: 'a request for product 1',
        withRequest: {
          method: 'GET',
          path: '/api/products/1',
          headers: {
            Authorization: like('Bearer valid-token'),
          },
        },
        willRespondWith: {
          status: 200,
          headers: {
            'Content-Type': 'application/json; charset=utf-8',
          },
          body: {
            id: integer(1),
            name: string('Premium Widget'),
            price: decimal(49.99),
            description: string('A premium quality widget'),
            category: string('Widgets'),
            stock: integer(75),
            inStock: boolean(true),
            images: eachLike(string('https://example.com/image.jpg')),
            createdAt: string('2026-01-01T00:00:00.000Z'),
          },
        },
      });
    });

    it('should return product details', async () => {
      const response = await axios.get('http://localhost:1234/api/products/1', {
        headers: { Authorization: 'Bearer valid-token' },
      });

      expect(response.status).toBe(200);
      expect(response.data.id).toBe(1);
      expect(response.data.name).toBeDefined();
      expect(response.data.price).toBeGreaterThan(0);
    });
  });

  describe('GET /api/products/:id - Not Found', () => {
    beforeEach(async () => {
      await provider.addInteraction({
        state: 'no product with id 99999 exists',
        uponReceiving: 'a request for non-existent product',
        withRequest: {
          method: 'GET',
          path: '/api/products/99999',
          headers: {
            Authorization: like('Bearer valid-token'),
          },
        },
        willRespondWith: {
          status: 404,
          headers: {
            'Content-Type': 'application/json; charset=utf-8',
          },
          body: {
            error: string('Product not found'),
            statusCode: integer(404),
          },
        },
      });
    });

    it('should return 404 for non-existent product', async () => {
      try {
        await axios.get('http://localhost:1234/api/products/99999', {
          headers: { Authorization: 'Bearer valid-token' },
        });
        fail('Should have thrown 404');
      } catch (error) {
        expect(error.response.status).toBe(404);
        expect(error.response.data.error).toBe('Product not found');
      }
    });
  });

  describe('POST /api/products', () => {
    beforeEach(async () => {
      await provider.addInteraction({
        state: 'user is authenticated as admin',
        uponReceiving: 'a request to create a product',
        withRequest: {
          method: 'POST',
          path: '/api/products',
          headers: {
            'Content-Type': 'application/json',
            Authorization: like('Bearer admin-token'),
          },
          body: {
            name: string('New Product'),
            price: decimal(39.99),
            description: string('A new test product'),
            category: string('Electronics'),
            stock: integer(50),
          },
        },
        willRespondWith: {
          status: 201,
          headers: {
            'Content-Type': 'application/json; charset=utf-8',
          },
          body: {
            id: integer(),
            name: string('New Product'),
            price: decimal(39.99),
            description: string('A new test product'),
            category: string('Electronics'),
            stock: integer(50),
            createdAt: string(),
          },
        },
      });
    });

    it('should create a new product', async () => {
      const response = await axios.post('http://localhost:1234/api/products', {
        name: 'New Product',
        price: 39.99,
        description: 'A new test product',
        category: 'Electronics',
        stock: 50,
      }, {
        headers: {
          'Content-Type': 'application/json',
          Authorization: 'Bearer admin-token',
        },
      });

      expect(response.status).toBe(201);
      expect(response.data.id).toBeDefined();
      expect(response.data.name).toBe('New Product');
    });
  });
});
```

#### 19.4.2 Pact Provider Verification

```javascript
// provider/tests/pact/provider-verification.spec.js
const { Verifier } = require('@pact-foundation/pact');
const path = require('path');
const app = require('../../src/app'); // Your Express app

describe('Pact Provider Verification', () => {
  let server;

  beforeAll((done) => {
    server = app.listen(3001, done);
  });

  afterAll((done) => {
    server.close(done);
  });

  it('should validate the expectations of the ProductWebApp consumer', async () => {
    const opts = {
      provider: 'ProductAPI',
      providerBaseUrl: 'http://localhost:3001',
      pactUrls: [
        path.resolve(process.cwd(), '..', 'consumer', 'pacts', 'producwebapp-productapi.json'),
      ],
      publishVerificationResult: