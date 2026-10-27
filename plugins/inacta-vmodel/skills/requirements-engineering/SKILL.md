---
name: requirements-engineering
description: Structured requirements engineering methodology for the V-Model left side. Guides the agent from project brief through stakeholder interviews, user story elicitation with acceptance criteria, functional requirements specification, and traceability matrix generation, all before development begins. Use when the user asks for requirements analysis, user stories, acceptance criteria, feature specification, or wants to plan a new project or feature systematically.
---

# Requirements Engineering

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

- **Inception**: Full elicitation. User stories, functional and non-functional requirements, and the traceability matrix, before construction starts. This is the skill's home phase.
- **Build**: Capture deltas per increment: new stories and requirements as scope grows.
- **Run**: Drive requirements from change requests and incidents, and keep traceability intact.

Capture, structure, and validate requirements *before* development begins, the left side of the V-Model. This skill produces user stories with acceptance criteria, a functional requirements specification, and a traceability matrix linking stories → requirements → test scenarios. It is designed to run at the start of a new project or feature, producing artifacts that feed directly into arc42 documentation and downstream development.

## When to Use

- The user wants to plan a new project or feature before writing code
- The user asks for user stories, acceptance criteria, or a requirements specification
- The user says "what should we build?" or "let's define the requirements"
- The user has a project brief, feature request, or product idea and wants structured analysis
- The user wants to create a traceability matrix linking requirements to test scenarios
- The user wants to enrich arc42 Section 01 with structured requirements before implementation

## When NOT to Use

- The user wants to analyze an *existing* codebase retroactively → use `persona-analysis` instead
- The user wants architecture documentation for what already exists → use `arc42-documentation`
- The user wants to run tests or define test execution strategy → use `test-strategy` and the project's test runner
- The user wants formal component contracts for existing code → use `arc42-design-by-contract`

## Relationship to Companion Skills

This skill sits at the beginning of the arc42 lifecycle, it produces inputs that the other skills consume:

```
requirements-engineering ──→ arc42-documentation ──→ arc42-design-by-contract
        │                           │                         │
        │ personas (input)          │ Sections 01, 11         │ §5.4 contracts
        ▼                           ▼                         ▼
   persona-analysis ◄──── arc42-risk-audit ◄──── implementation
   (retroactive validation)   (risk overlay)       (V-Model right side)
```

| Skill | Relationship |
|-------|-------------|
| `persona-analysis` | **Input**: If a persona roster already exists (P1, Pn with needs in PX-NX format), use it as the starting point for Phase 1 instead of rediscovering personas. **Output**: User stories produced here validate whether the persona roster is complete, if a story has no matching persona, a new persona may be needed. |
| `arc42-documentation` | **Output**: User stories feed into **Section 01 §1.2** (Requirements Overview). Functional requirements are written in FR-XX.X format compatible with the `requirements.md` companion document. The traceability matrix is added to `requirements.md` as a **Stakeholder Traceability** section. |
| `arc42-design-by-contract` | **Output**: Acceptance criteria from user stories become inputs for DbC contract generation. Each acceptance criterion maps to a precondition, postcondition, or invariant in the §5.4 component specification. The mapping is recorded in the traceability matrix. |

---

## Phase 1: Project Brief Analysis

### Overview

Understand the project or feature scope by analyzing the project brief, user conversation, or existing documentation. Produce a **scope statement** and a **persona roster** (or validate an existing one).

### Input Sources

| Source | What to Extract | Priority |
|--------|----------------|----------|
| Project brief / feature request | Goals, constraints, target users, success criteria | Primary |
| User conversation | Pain points, desired outcomes, priorities | Primary |
| Existing persona roster (`persona-analysis` output) | Known personas with needs (P1-N1 format) | Reuse if available |
| Existing arc42 Section 01 | Previously documented stakeholders and requirements | Reuse if available |
| Domain knowledge / industry conventions | Standard user roles and workflows for this type of system | Supplement |

### When to Ask the User

Ask clarifying questions when:

- The brief does not specify who the users are or what roles exist
- The success criteria are vague ("make it better") and you need measurable outcomes
- There are conflicting priorities and only the user can resolve them
- The project scope is ambiguous, is it a new system or a feature addition?

Do NOT ask when:

- The brief clearly states the users, goals, and scope
- A persona roster already exists from a previous `persona-analysis` run
- Industry conventions provide obvious answers (e.g., a CRM has salespeople)

### Scope Statement Template

Produce a concise scope statement as the Phase 1 deliverable:

```markdown
## Scope Statement

**Project / Feature**: [Name]
**Objective**: [1-2 sentences: what this achieves and why it matters]
**In Scope**: [Bulleted list of what will be specified]
**Out of Scope**: [Bulleted list of what will NOT be specified]
**Key Constraints**: [Technical, organizational, or timeline constraints]
**Success Criteria**: [Measurable outcomes that define "done"]
```

### Persona Roster

If no persona roster exists, produce one using the `persona-analysis` Phase 1 format:

| ID | Persona | Description | Key Responsibility |
|----|---------|-------------|-------------------|
| P1 | [Role Name] | [1-2 sentences] | [Primary job-to-be-done] |

If a persona roster already exists, validate it against the project brief:

1. Do all personas relevant to this feature appear in the roster?
2. Are any new personas implied by the brief that are not yet in the roster?
3. If new personas are needed, add them with the next available P-number.

---

## Phase 2: User Story Elicitation

### Overview

For each persona relevant to the feature, elicit user stories with acceptance criteria. Each story follows the standard format and is traceable to a persona need.

### User Story Format

```markdown
### US-XXX: [Story Title]

**As a** [Persona Name (ID)],
**I want to** [goal/action],
**So that** [benefit/value].

**Traces to**: [Persona Need ID, use P{persona}-N{need} format (e.g., P1-N1) by default, or mnemonic shorthand (e.g., C1, S4) if the existing persona roster already uses that convention]

#### Acceptance Criteria

| # | Given | When | Then |
|---|-------|------|------|
| AC-XXX.1 | [precondition/context] | [action/trigger] | [expected outcome] |
| AC-XXX.2 | [precondition/context] | [action/trigger] | [expected outcome] |
```

### Story ID Scheme

Use `US-XXX` where XXX is a three-digit sequential number starting from 001. Group stories by feature area:

- US-001, US-099: Core feature stories
- US-100, US-199: Administrative / configuration stories
- US-200, US-299: Reporting / analytics stories
- US-300, US-399: Integration stories

### Acceptance Criteria Guidelines

Each user story MUST have at least 2 acceptance criteria. Use the Given/When/Then format:

| Element | Definition | Example |
|---------|-----------|---------|
| **Given** | The precondition or context | "Given I am logged in as a Sales user and viewing my pipeline" |
| **When** | The action or trigger | "When I click 'Send Follow-up' on a deal" |
| **Then** | The expected, observable outcome | "Then an email draft opens pre-filled with the contact's email and deal context" |

Write acceptance criteria that are:

- **Testable**, each criterion can be verified by a specific test scenario
- **Unambiguous**, only one interpretation is possible
- **Independent**, each criterion tests one thing
- **Boundary-aware**, include edge cases (empty inputs, maximum values, unauthorized access)

### Story Elicitation Process

1. **Start from persona needs**, each need (P1-N1) should generate at least one user story
2. **Decompose large needs**, if a need is too broad for one story, split it into multiple stories
3. **Cross-reference personas**, if multiple personas share a need, write the story for the primary persona and note secondary personas in the "Traces to" field
4. **Prioritize using MoSCoW**, tag each story as Must / Should / Could / Won't (this iteration)

### Priority Classification

| Priority | Definition |
|----------|-----------|
| **Must** | The feature cannot ship without this story. Blocks the primary use case. |
| **Should** | Important for a complete experience. The feature works without it but feels incomplete. |
| **Could** | Desirable enhancement. Include if time permits. |
| **Won't** | Out of scope for this iteration but documented for future reference. |

---

## Phase 3: Functional Requirements Specification

### Overview

Transform user stories into formal functional requirements using the FR-XX.X format compatible with the arc42 `requirements.md` companion document. Each requirement is implementation-ready and traceable to one or more user stories.

### FR-XX.X Format

Group requirements by feature area (FR-01 = Feature Area 1, FR-01.1 = first requirement in that area):

```markdown
### FR-XX: [Feature Area Name]

| ID | Requirement | Source Story | Priority |
|----|-------------|-------------|----------|
| FR-XX.1 | [Precise requirement statement] | US-XXX | Must |
| FR-XX.2 | [Precise requirement statement] | US-XXX | Should |
```

### Requirement Writing Rules

1. **One requirement, one capability**, each FR-XX.X describes exactly one thing the system must do
2. **Use active voice**, "The system shall [verb] [object]" or "The user can [verb] [object]"
3. **Be specific about data**, name the fields, formats, and constraints (e.g., "email address in RFC 5322 format" not "valid email")
4. **Specify error behavior**, what happens when the precondition fails? (e.g., "returns 400 with field-level error messages")
5. **Include non-functional aspects**, response time, data retention, concurrency behavior where relevant
6. **Trace to stories**, every requirement must reference at least one US-XXX

### Numbering Compatibility

When adding to an existing `requirements.md`, continue the FR-XX numbering sequence:

1. Read the existing `requirements.md` to find the highest FR-XX number
2. Start new feature areas at the next available FR-XX number
3. If extending an existing feature area, add new sub-requirements at the next available FR-XX.X number

### Non-Functional Requirements

Capture non-functional requirements in a separate table:

```markdown
### Non-Functional Requirements

| ID | Category | Requirement | Source Story |
|----|----------|-------------|-------------|
| NFR-XX | [Performance / Security / Usability / ...] | [Requirement statement] | US-XXX |
```

---

## Phase 4: Traceability Matrix

### Overview

Produce a comprehensive traceability matrix that links every user story to its functional requirements and forward to test scenario stubs. This matrix is the primary deliverable for V-Model traceability, it connects the left side (requirements) to the right side (validation).

### Traceability Matrix Template

```markdown
## Traceability Matrix

| User Story | Persona Need | Functional Req(s) | Acceptance Criteria | Test Scenario Stub | DbC Contract |
|------------|-------------|-------------------|--------------------|--------------------|-------------|
| US-001 | P1-N1 | FR-01.1, FR-01.2 | AC-001.1, AC-001.2 | TS-001: [brief description] | §5.4.N `ComponentName`, feature_name |
| US-002 | P2-N3 | FR-02.1 | AC-002.1 | TS-002: [brief description] |, |
```

### Column Definitions

| Column | Content | Source |
|--------|---------|--------|
| **User Story** | US-XXX identifier | Phase 2 output |
| **Persona Need** | P-N identifier (e.g., P1-N1 or C1) | Phase 1 roster / persona-analysis |
| **Functional Req(s)** | FR-XX.X identifiers | Phase 3 output |
| **Acceptance Criteria** | AC-XXX.X identifiers | Phase 2 output |
| **Test Scenario Stub** | TS-XXX with brief description | Generated here |
| **DbC Contract** | Reference to §5.4 component and feature | Future arc42-design-by-contract input |

### Test Scenario Stubs

For each user story, generate a test scenario stub that can be expanded into a full test case during implementation:

```markdown
### TS-XXX: [Test Scenario Title]

**Validates**: US-XXX (AC-XXX.1, AC-XXX.2)
**Type**: [Unit / Integration / E2E / Manual]
**Preconditions**: [Setup required before the test]
**Steps**:
1. [Step 1]
2. [Step 2]
**Expected Result**: [What success looks like]
**Edge Cases**:
- [Edge case 1]
- [Edge case 2]
```

### DbC Mapping

For each acceptance criterion, note the corresponding DbC contract element:

| AC Element | DbC Element | Example |
|-----------|-------------|---------|
| **Given** (precondition) | `require` block | "Given the user is authenticated" → `require request.isAuthenticated() = true` |
| **Then** (expected outcome) | `ensure` block | "Then the email is sent" → `ensure ∃ e ∈ sent_emails : e.recipientId = contact.id` |
| **Data constraints** | `invariant` block | "Email must be valid format" → `invariant ∀ c ∈ contacts : c.email ≠ void ⟹ c.email matches RFC5322` |

This mapping is not generated automatically, it serves as a guide for when `arc42-design-by-contract` is run after development begins.

---

## Phase 5: Output Assembly

### Overview

Assemble all outputs into structured deliverables. These integrate into the arc42 ecosystem or can stand alone as a requirements package.

### Deliverable Checklist

| Deliverable | Format | Destination |
|-------------|--------|-------------|
| Scope statement | Markdown section | Standalone or arc42 Section 01 §1.1 |
| Persona roster (new or validated) | Markdown table | arc42 Section 01 §1.4 |
| User stories with acceptance criteria | Markdown sections | `docs/requirements/user-stories.md` or `requirements.md` |
| Functional requirements (FR-XX.X) | Markdown tables | `requirements.md` companion doc |
| Non-functional requirements | Markdown table | `requirements.md` companion doc |
| Traceability matrix | Markdown table | `requirements.md`, Stakeholder Traceability section |
| Test scenario stubs | Markdown sections | `docs/requirements/test-scenarios.md` or inline |

### Arc42 Integration Points

#### Section 01: Introduction and Goals

- **§1.1 Purpose**: Update with the scope statement if this is a new project
- **§1.2 Requirements Overview**: Add or update FR-XX.X entries from Phase 3
- **§1.4 Stakeholders**: Add new personas discovered in Phase 1; update needs tables if new needs were identified

Add a cross-reference to the requirements package:

```markdown
See the [Requirements Engineering Package](requirements.md#user-stories) for
the complete user stories, acceptance criteria, and traceability matrix.
```

#### Requirements Companion (`requirements.md`)

Add or update these sections:

1. **User Stories**, full user story specifications from Phase 2
2. **Functional Requirements**, FR-XX.X tables from Phase 3
3. **Stakeholder Traceability**, the traceability matrix from Phase 4

If `requirements.md` already exists with FR-XX.X entries, merge new requirements into the existing structure using the numbering compatibility rules from Phase 3.

#### Section 11: Risks and Technical Debt

If Phase 1 or Phase 2 reveals gaps (persona needs that cannot be met by the planned feature), add them as PD-xxx (Product Debt) entries in §11.3, following the `persona-analysis` format.

### File Organization

For larger projects, organize requirements artifacts in a dedicated directory:

```
docs/requirements/
├── scope-statement.md          # Phase 1 output
├── user-stories.md             # Phase 2 output (all stories with ACs)
├── functional-requirements.md  # Phase 3 output (FR-XX.X tables)
├── traceability-matrix.md      # Phase 4 output
└── test-scenarios.md           # Phase 4 test scenario stubs
```

For smaller projects or single-feature analyses, consolidate into `requirements.md` alongside the arc42 docs.

---

## Execution Guidelines

### Full Analysis (New Project)

1. **Phase 1**, Analyze the project brief. Produce scope statement and persona roster. Ask the user to validate personas before proceeding.
2. **Phase 2**, Elicit user stories for every persona. Present stories to the user for review. Iterate on acceptance criteria until the user confirms.
3. **Phase 3**, Transform stories into FR-XX.X requirements. Cross-check against existing requirements if any.
4. **Phase 4**, Generate the traceability matrix and test scenario stubs.
5. **Phase 5**, Assemble deliverables, write to arc42 sections, present summary.

Present a summary to the user after Phase 2 (story review checkpoint) and after Phase 5 (final deliverables).

### Targeted Analysis (Single Feature)

When adding a feature to an existing project:

1. Read existing `requirements.md` and arc42 Section 01 to understand current state
2. Focus Phase 1 on validating existing personas against the new feature, add new personas only if needed
3. Elicit stories only for the new feature (use the next available US-XXX number)
4. Add requirements continuing the existing FR-XX.X sequence
5. Extend the traceability matrix with new rows
6. Update arc42 sections incrementally

### Incremental Update

When refining existing requirements:

1. Read the current requirements package
2. Note the highest US-XXX, FR-XX.X, and TS-XXX numbers
3. Add, modify, or deprecate stories/requirements as needed
4. Update the traceability matrix to reflect changes
5. Mark deprecated items with ~~strikethrough~~ rather than deleting them

## Portability

This skill is stack-neutral. It resolves everything project-specific, the language,
frameworks, database, test and deploy commands, ID prefixes, and the current
lifecycle phase, from `.vmodel.yml` and `docs/project-context.md` (see "Project
Context" above). To adopt it in a new project, run the `vmodel-setup` skill to scaffold the two
context files, fill in the stack and the current phase, and the skill adapts
automatically. It carries no assumption about any specific platform or vendor.
