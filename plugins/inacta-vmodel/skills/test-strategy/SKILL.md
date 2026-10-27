---
name: test-strategy
description: Generate structured test strategies from specifications, closing the right side of the V-Model. Derives test scenarios from DbC contracts (arc42 §5.4), functional requirements, and user stories with full traceability. Use when the user asks for test strategy, test plan, test scenarios, acceptance tests, contract-based testing, or V-Model test generation.
---

# Test Strategy Generation

## Project Context (read first)

Before doing anything, read the project context so this skill adapts to the target
project instead of assuming a stack:

- `.vmodel.yml` at the project root: machine-readable stack and command hooks (language, frameworks, database, `test-command`, `security-scan-command`, `deploy-command`), the ID prefixes, the docs path, and the current `lifecycle-phase`.
- `docs/project-context.md`: the human-readable brief and house rules (no em-dashes, Swiss German spelling).

If neither file exists, use the `vmodel-setup` skill, which scaffolds both files from
its bundled templates. If that skill is not installed, ask the user for the stack and the
current lifecycle phase and write the two files by hand. Never hardcode a stack, a
platform, or a test or deploy command. Always resolve them from the context.

## Phase Adaptation (Inception / Build / Run)

This skill runs in every lifecycle phase but shifts its depth and output focus
based on `lifecycle-phase` in `.vmodel.yml`:

- **Inception**: Define the strategy and the acceptance criteria at the planning level, deriving the UT/FT/AT levels from contracts and requirements.
- **Build**: Generate and execute concrete scenarios per increment, and keep the traceability matrix current.
- **Run**: Focus on smoke, regression, and monitoring scenarios for the live system.

Generate structured, traceable test strategies that close the right side of the V-Model. This skill bridges specifications (DbC contracts, functional requirements, user stories) to test plans, producing test scenarios, acceptance criteria, test data specifications, and a traceability matrix linking every test back to its source requirement or contract.

## When to Use

- The user asks for a test strategy, test plan, or test scenarios
- The user wants tests derived from DbC contracts or formal specifications
- The user asks for acceptance test plans based on user stories
- The user wants a test traceability matrix
- The user asks to verify coverage of requirements or contracts
- After new DbC specifications or requirements are written and the user wants corresponding tests

## Relationship to Companion Skills

| Skill | Relationship |
|-------|-------------|
| `arc42-design-by-contract` | **Primary input.** DbC contracts in Section 5.4 are the source for unit/module test cases. `require` clauses become test inputs, `ensure` clauses become assertions, `invariant` clauses become property checks. |
| `persona-analysis` | Persona needs (P1-N1 format) from Section 01 feed into acceptance test scenarios. Each Critical/High persona need should have at least one acceptance test. |
| `arc42-documentation` | Quality scenarios from Section 10 map to system-level test cases. Functional decomposition provides capability groupings for organizing test suites. |
| `interaction-model` | Each operational principle of a concept ("after you do X, Y holds") becomes one acceptance test (AT-). Each undo path in the signifier and reversibility table becomes one functional test (FT-). |
| `arc42-risk-audit` | Risk entries (R-xxx) from Section 11 identify areas needing negative/failure test cases. High-severity risks warrant dedicated regression tests. |

**Typical workflow**: Write requirements → Generate DbC specs → **Generate test strategy** → Execute tests (the project's configured test runner).

## V-Model Testing Levels

This skill covers three testing levels corresponding to the right side of the V-Model:

```
Requirements ──────────────────────────── Acceptance Testing
    │                                           ↑
    ▼                                           │
Functional Spec ───────────────────── Functional Testing
    │                                           ↑
    ▼                                           │
DbC Contracts ─────────────────── Unit/Module Testing
    │                                           ↑
    ▼                                           │
Implementation ──────── Code ──────────────────┘
```

| Level | Source | Test Type | ID Prefix |
|-------|--------|-----------|-----------|
| **Unit/Module** | DbC contracts (§5.4) | Boundary tests, property checks, state assertions | `UT-` |
| **Functional** | Functional requirements (FR-xx.x) | End-to-end API and UI flow tests | `FT-` |
| **Acceptance** | User stories / persona needs | Scenario-based acceptance tests | `AT-` |

---

## Phase 1: Source Analysis

### Overview

Read and catalog all specification sources that will drive test generation. Produce a **source inventory** listing every testable specification element.

### Input Sources

Read these sources in order. Each source type yields a different category of test:

| Source | Location | Yields |
|--------|----------|--------|
| DbC contracts | `docs/arc42/05-building-block-view.md`, §5.4 | Unit/module tests (UT-) |
| Functional requirements | `docs/requirements.md` or functional decomposition | Functional tests (FT-) |
| User stories / persona needs | `docs/arc42/01-introduction-and-goals.md`, §1.4 | Acceptance tests (AT-) |
| Quality scenarios | `docs/arc42/10-quality-requirements.md` | Cross-cutting quality tests (FT-) |
| Risk entries | `docs/arc42/11-risks-and-technical-debt.md` | Negative/failure tests (FT-) |
| Operational principles, undo paths | `docs/ui/` (from `interaction-model`) | Acceptance tests (AT-), reversibility tests (FT-) |

### Source Inventory Template

Produce a catalog of testable elements:

```markdown
## Source Inventory

### DbC Components (§5.4)
| Component | Invariants | Features | Priority |
|-----------|-----------|----------|----------|
| DealLifecycleManager | 6 | 4 (create, update, delete, bulk) | High |
| AuthenticationService | 3 | 4 (login, callback, middleware, notes_auth) | Critical |

### Functional Requirements
| Req ID | Description | Source |
|--------|-------------|--------|
| FR-05.1 | Pipeline summary report | functional-decomposition.md |

### Persona Needs
| Need ID | Persona | Need | Priority |
|---------|---------|------|----------|
| P1-N1 | CEO | Cross-unit pipeline visibility | Critical |
```

---

## Phase 2: Test Scenario Generation

### Overview

Derive test cases from each source using the methodologies defined below. Each test case gets a unique ID, a clear description, and explicit linkage to its source.

### 2.1 Contract-to-Test Derivation (Unit/Module Tests)

Transform DbC contract elements into concrete test cases using these rules:

#### From `require` Clauses → Boundary Test Inputs

Each precondition generates **three categories** of test input:

| Category | Derivation Rule | Example |
|----------|----------------|---------|
| **Valid** | Input that satisfies the precondition | `body.title = "New Deal"` (satisfies `title ≠ void ∧ title.length > 0`) |
| **Invalid** | Input that violates the precondition | `body.title = ""` or `body.title = void` |
| **Edge** | Input at the boundary of the precondition | `body.title = "X"` (minimum length), `body.probability = 0`, `body.probability = 100` |

**Derivation procedure for each `require` clause:**

1. Identify the constraint type (non-null, range, membership, existence, composite)
2. For **non-null** (`field ≠ void`): test with value present (valid), value absent (invalid), value empty string if string type (edge)
3. For **range** (`0 ≤ x ≤ 100`): test within range (valid), below minimum (invalid: -1), above maximum (invalid: 101), at boundaries (edge: 0, 100)
4. For **membership** (`x ∈ {a, b, c}`): test with each valid member (valid), test with non-member value (invalid)
5. For **existence** (`∃ x ∈ table : x.id = param`): test with existing reference (valid), test with non-existent reference (invalid: id = 999999)
6. For **composite** (multiple conditions joined by `∧`): test each condition independently, then test combinations where one condition fails while others pass

#### From `ensure` Clauses → Expected Outcomes / Assertions

Each postcondition becomes an explicit assertion in the test case:

| Postcondition Pattern | Assertion Type | Test Assertion |
|----------------------|----------------|----------------|
| `∃ x ∈ table : x.field = value` | State creation | Verify record exists in database with expected field values |
| `response.status = 201` | Response code | Assert HTTP status code |
| `x.userId = request.user.id` | Attribution | Verify the created/modified record is attributed to the authenticated user |
| `old(x.field) ≠ x.field ⟹ ∃ audit` | Side effect | Verify audit trail entry is created when tracked field changes |
| `x ∉ table` | State deletion | Verify record no longer exists after delete operation |
| `table[id] reflects body fields` | State mutation | Verify each updated field matches the request body |

#### From `invariant` Clauses → Property-Based Checks

Each invariant becomes a **property check** that must hold before and after every operation:

| Invariant Pattern | Property Check |
|------------------|----------------|
| `∀ d ∈ deals : d.pipelineId ≠ void ∧ ∃ p ∈ pipelines` | After any deal operation, verify all deals reference valid pipelines |
| `∀ d ∈ deals : d.probability ≠ void ⟹ 0 ≤ d.probability ≤ 100` | After any deal mutation, verify probability bounds are maintained |
| Cascade deletion invariant | After deleting a parent, verify all children are removed |
| Referential nullification invariant | After deleting a referenced entity, verify FK fields are set to null |

#### Unit/Module Test Case Template

```markdown
### UT-XXX: [Test Name]

**Source**: §5.4.N `ComponentName`, feature `feature_name`, require/ensure/invariant clause
**Level**: Unit/Module
**Category**: Valid | Invalid | Edge | Property

**Preconditions**:
- [Setup state required before test execution]

**Test Input**:
- [Concrete input values]

**Expected Outcome**:
- [Specific assertions derived from `ensure` clauses]

**Invariant Checks**:
- [Post-operation invariant verification]
```

### 2.2 Requirement-to-Test Derivation (Functional Tests)

Transform functional requirements and quality scenarios into functional test cases:

#### From Acceptance Criteria → Functional Test Scenarios

Each acceptance criterion in a functional requirement becomes a test scenario:

1. **Read the requirement** (FR-xx.x) and identify its acceptance criteria
2. **Map each criterion to a user action**, what does the user do?
3. **Define the expected system response**, what should happen?
4. **Identify the verification method**, API response check, UI assertion, or database query

#### From Quality Scenarios → Quality Test Cases

Each quality scenario (QS-x) from Section 10 maps to a test:

| Quality Scenario Element | Test Element |
|-------------------------|-------------|
| Stimulus | Test action / trigger |
| Response | Expected behavior |
| Measure | Pass/fail criterion |

#### Functional Test Case Template

```markdown
### FT-XXX: [Test Name]

**Source**: FR-xx.x [Requirement Title] | QS-x [Quality Scenario]
**Level**: Functional

**User Action**:
- [Step-by-step user actions]

**Expected System Response**:
- [Observable system behavior]

**Verification**:
- [How to confirm the test passed, API response, UI state, DB state]
```

### 2.3 Story-to-Test Derivation (Acceptance Tests)

Transform user stories and persona needs into acceptance test scenarios:

#### From Persona Needs → Acceptance Scenarios

Each persona need (P1-N1 format) with Critical or High priority must have at least one acceptance test:

1. **Read the persona need** and its priority
2. **Construct a scenario** from the persona's perspective: "As [persona], I want to [action] so that [outcome]"
3. **Define acceptance criteria**, concrete, observable conditions that prove the need is met
4. **Map to existing features**, reference the capability mapping from persona analysis

#### Acceptance Test Case Template

```markdown
### AT-XXX: [Test Name]

**Source**: P1-N1 [Persona Need Description]
**Level**: Acceptance
**Persona**: [Persona name and role]

**Scenario**:
Given [initial state]
When [user action]
Then [expected outcome]

**Acceptance Criteria**:
- [ ] [Criterion 1]
- [ ] [Criterion 2]
```

---

## Phase 3: Test Data Specification

### Overview

Define the test data sets needed to execute the test scenarios from Phase 2. Test data specifications ensure tests are repeatable and cover boundary conditions.

### Test Data Categories

| Category | Purpose | Example |
|----------|---------|---------|
| **Seed data** | Baseline state required before tests run | A pipeline with 6 stages, an authenticated user |
| **Valid inputs** | Data that satisfies all preconditions | `{title: "New Deal", pipelineId: 1, stageId: 1}` |
| **Invalid inputs** | Data that violates one or more preconditions | `{title: "", pipelineId: 999}` |
| **Edge case inputs** | Data at precondition boundaries | `{probability: 0}`, `{probability: 100}`, `{value: "0.00"}` |
| **State transition data** | Data that triggers specific postcondition branches | `{stageId: 2}` on a deal currently at stageId 1 (triggers audit trail) |

### Test Data Specification Template

```markdown
## Test Data Sets

### DS-XXX: [Data Set Name]

**Used by**: UT-001, UT-002, FT-010
**Category**: Seed | Valid | Invalid | Edge | State Transition

**Data**:
| Field | Value | Rationale |
|-------|-------|-----------|
| title | "Test Deal" | Satisfies `title ≠ void ∧ title.length > 0` |
| pipelineId | 1 | References existing pipeline (seed data) |
| probability | 100 | Edge: upper bound of `0 ≤ probability ≤ 100` |

**Prerequisites**:
- [Seed data that must exist before this data set is used]
```

---

## Phase 4: Test Traceability Matrix

### Overview

Produce a matrix linking every test case back to its source specification, establishing full traceability from requirements through to test execution.

### Traceability Matrix Format

```markdown
## Test Traceability Matrix

| Test ID | Test Name | Source | Source ID | Test Type | Level | Status |
|---------|-----------|--------|-----------|-----------|-------|--------|
| UT-001 | Create deal with valid input | DbC Contract | §5.4.2 create_deal require | Boundary (Valid) | Unit | Planned |
| UT-002 | Create deal with missing title | DbC Contract | §5.4.2 create_deal require | Boundary (Invalid) | Unit | Planned |
| UT-003 | Deal probability bounds maintained | DbC Contract | §5.4.2 invariant | Property | Unit | Planned |
| FT-001 | Pipeline summary accuracy | Quality Scenario | QS-7 | Functional | Functional | Planned |
| AT-001 | CEO views cross-unit pipeline | Persona Need | P1-N1 | Acceptance | Acceptance | Planned |
```

### Status Values

| Status | Meaning |
|--------|---------|
| **Planned** | Test case defined but not yet implemented |
| **Implemented** | Test code written (the e2e test runner, API test, etc.) |
| **Passing** | Test executes and passes |
| **Failing** | Test executes and fails (indicates a defect or spec drift) |
| **Blocked** | Test cannot run due to missing prerequisite (e.g., feature not built) |

### Coverage Summary

After the matrix, include a coverage summary:

```markdown
### Coverage Summary

| Source Type | Total Elements | Tests Derived | Coverage |
|-------------|---------------|---------------|----------|
| DbC Invariants | 12 | 15 | 100% |
| DbC Features (require) | 18 | 36 | 100% |
| DbC Features (ensure) | 24 | 24 | 100% |
| Functional Requirements | 8 | 12 | 100% |
| Persona Needs (Critical/High) | 6 | 8 | 100% |
| Quality Scenarios | 7 | 7 | 100% |
| **Total** | **75** | **102** | **100%** |
```

## Portability

This skill is stack-neutral. It resolves everything project-specific, the language,
frameworks, database, test and deploy commands, ID prefixes, and the current
lifecycle phase, from `.vmodel.yml` and `docs/project-context.md` (see "Project
Context" above). To adopt it in a new project, run the `vmodel-setup` skill to scaffold the two
context files, fill in the stack and the current phase, and the skill adapts
automatically. It carries no assumption about any specific platform or vendor.

## Output Document Structure

The skill produces a single test strategy document at `docs/test-strategy.md` with the following structure:

```markdown
# Test Strategy: [Project Name]

## 1. Source Inventory
[Phase 1 output]

## 2. Test Scenarios
### 2.1 Unit/Module Tests (from DbC Contracts)
[UT-xxx test cases grouped by component]

### 2.2 Functional Tests (from Requirements)
[FT-xxx test cases grouped by capability]

### 2.3 Acceptance Tests (from User Stories)
[AT-xxx test cases grouped by persona]

## 3. Test Data Specification
[DS-xxx data set definitions]

## 4. Test Traceability Matrix
[Full matrix + coverage summary]

## 5. Feeding into Test Execution
[Guidance on translating test cases to the e2e test runner/API tests]
```

### Feeding into Test Execution

The test strategy document is designed to feed into test execution. When handing off to the project's configured test runner:

1. **UT-xxx tests** → API-level tests using an HTTP client against the running server
2. **FT-xxx tests** → Mixed API and UI tests using the e2e test runner
3. **AT-xxx tests** → Full end-to-end scenarios simulating user journeys

Each test case's **Test Input** and **Expected Outcome** sections translate directly to test code:
- Test Input → test setup and action
- Expected Outcome → assertions
- Invariant Checks → post-action database queries

---

## Execution Guidelines

### For Full Strategy Generation

1. **Phase 1**: Read all specification sources (§5.4, requirements, persona needs, quality scenarios, risks)
2. **Phase 2**: Derive test cases from each source using the appropriate methodology
3. **Phase 3**: Define test data sets covering seed, valid, invalid, edge, and state transition categories
4. **Phase 4**: Build the traceability matrix and compute coverage
5. **Write**: Produce `docs/test-strategy.md` with the full document structure
6. **Present**: Summarize coverage statistics to the user before finalizing

### For Targeted Generation (Single Component)

When the user asks for tests for a specific component:

1. Read only the relevant DbC contract from §5.4
2. Derive UT-xxx test cases for that component's features and invariants
3. Check if any functional requirements or persona needs map to this component
4. Produce a focused test strategy section (can be appended to an existing document)
5. Update the traceability matrix incrementally

### For Incremental Updates (Specs Changed)

When specifications have been added or modified:

1. Read the existing `docs/test-strategy.md`
2. Note the highest UT-xxx, FT-xxx, AT-xxx, and DS-xxx numbers
3. Derive new test cases only for changed or added specification elements
4. Add new test cases continuing the ID sequence
5. Update the traceability matrix and recalculate coverage
6. Mark any tests affected by changed specs as needing review (status → Planned)

### Interaction Guidelines

| Situation | Action |
|-----------|--------|
| No DbC contracts exist in §5.4 | Inform the user and suggest running the `arc42-design-by-contract` skill first |
| No requirements document exists | Derive functional tests from quality scenarios (§10) and DbC contracts only; note the gap |
| No persona analysis exists | Skip acceptance tests (AT-xxx); note that acceptance-level coverage is missing |
| User asks for tests for a feature not yet specified | Suggest writing the DbC contract first, then generating tests |
| Existing test strategy exists | Run incremental update, preserving existing test IDs |
| User wants test code, not test plans | Clarify that this skill produces plans; recommend the project's configured test runner for execution |
