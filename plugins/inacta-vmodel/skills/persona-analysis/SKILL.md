---
name: persona-analysis
description: Perform structured stakeholder persona analysis for any project. Identifies personas, elicits prioritized needs, maps needs to existing codebase capabilities, produces a gap matrix, and generates a prioritized remediation roadmap. Use when the user asks for persona analysis, stakeholder analysis, user needs assessment, capability gap analysis, or feature gap audit.
---

# Persona Analysis

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

- **Inception**: Full run. Identify personas, elicit prioritised needs, and build the gap matrix that seeds requirements. This is the skill's home phase.
- **Build**: Light revisit only when scope shifts or a new component changes who is affected.
- **Run**: Rare. Trigger only when a new stakeholder class appears in operations or support.

Systematically identify stakeholder personas, elicit their prioritized needs, map those needs to existing codebase capabilities, and produce a gap matrix with a remediation roadmap. This skill codifies a repeatable, project-agnostic methodology that works on any codebase.

## When to Use

- The user asks for a persona analysis, stakeholder analysis, or user needs assessment
- The user asks "who are the users and what do they need?"
- The user wants to identify feature gaps relative to stakeholder needs
- The user asks for a capability gap analysis or feature gap audit
- The user wants to prioritize what to build next based on user needs
- The user wants to enrich arc42 Section 01 with detailed persona profiles

## Relationship to Companion Skills

This skill works alongside three companion skills in the arc42 ecosystem:

| Skill | Relationship |
|-------|-------------|
| `arc42-documentation` | Persona profiles (assembled from Phase 1 Discovery + Phase 2 Needs Elicitation) are written into **Section 01 (Introduction and Goals), §1.4 Stakeholders**. The gap matrix from Phase 4 feeds into **Section 11 (Risks and Technical Debt)** as product debt items (§11.3). The requirements companion document (`requirements.md`) receives the stakeholder traceability matrix from Phase 5. |
| `arc42-risk-audit` | Product debt items (PD-xxx) from Phase 4 complement the technical risks (R-xxx) identified by the risk audit. Risk audit Category 1 (Access Control) findings often overlap with persona needs around role-based visibility, cross-reference to avoid duplication. |
| `arc42-design-by-contract` | DbC specifications in Section 5.4 define the behavioral contracts that capabilities are measured against. When a persona need maps to a feature whose DbC postcondition is violated, the gap entry should reference the specific contract violation. |

**Typical workflow**: Generate arc42 documentation → Run persona analysis → Add DbC specifications → Run risk audit → Merge product debt and technical debt into a unified remediation roadmap.

---

## Phase 1: Discovery: Identify Personas

### Overview

Identify the distinct stakeholder personas who use (or will use) the system. A persona is a role-based archetype, not an individual person. The goal is a **persona roster**, a concise list with role descriptions.

### Sources for Discovery

Investigate these sources in order. Use codebase investigation first; ask the user only for what cannot be inferred.

| Source | What to Look For | Infer or Ask? |
|--------|-----------------|---------------|
| Project README / documentation | Stated users, target audience, product description | Infer |
| Database schema, user/role tables | Role enums, permission flags, team/org structures | Infer |
| Frontend navigation / sidebar | Menu items grouped by function suggest different user types | Infer |
| Route middleware / guards | Auth roles, permission checks, admin-only routes | Infer |
| Existing arc42 Section 01 | Previously documented stakeholders | Infer |
| The user / product owner | Organization structure, team sizes, business units, who uses the system day-to-day | Ask |

### When to Ask the User

Ask the user clarifying questions when:

- The codebase has no role/permission model and you cannot infer user types from the UI
- The organization structure matters (e.g., business units, reporting hierarchy) but is not in the code
- You need to confirm whether a discovered role is actually a distinct persona or a sub-role
- The project is greenfield with no existing users

Do NOT ask the user when:

- The codebase clearly defines roles (e.g., `enum Role { ADMIN, EDITOR, VIEWER }`)
- Navigation and page structure reveals distinct user journeys
- Documentation already describes user types

### Persona Roster Template

Produce a roster table as the Phase 1 deliverable:

| ID | Persona | Description | Key Responsibility |
|----|---------|-------------|-------------------|
| P1 | [Role Name] | [1-2 sentences: who they are, what they care about] | [Primary job-to-be-done] |
| P2 | [Role Name] | [1-2 sentences] | [Primary job-to-be-done] |

Assign each persona a short ID (P1, P2, …) for traceability in later phases.

---

## Phase 2: Needs Elicitation: Define Prioritized Needs

### Overview

For each persona, define their specific needs from the system. Each need gets a priority level and a traceable ID.

### ID Scheme

Use the format `P{persona}-N{need}` for full traceability:

- `P1-N1` = Persona 1, Need 1
- `P3-N4` = Persona 3, Need 4

This is the default and recommended format. Short mnemonic prefixes (e.g., `C1` for CEO Need 1) may be used only when persona names are unambiguous and the user or existing documentation already uses that convention.

### Priority Levels

| Priority | Definition |
|----------|-----------|
| **Critical** | The persona cannot do their job without this. Blocks their primary workflow. |
| **High** | Significant impact on productivity or effectiveness. The persona works around it daily. |
| **Medium** | Noticeable improvement. The persona would benefit but can function without it. |
| **Low** | Nice-to-have. Improves experience but has minimal impact on core workflows. |

### Needs Elicitation Process

1. **Start from the persona's job-to-be-done**, what is their primary responsibility?
2. **Decompose into specific needs**, what does the system need to provide for them to fulfill that responsibility?
3. **Prioritize ruthlessly**, use the priority definitions above. Most personas should have 3-7 needs, with at most 2 marked Critical.
4. **Cross-check against the codebase**, does the system already address some of these needs? (This informs Phase 3 but helps calibrate priority now.)

### Sources for Needs

| Source | What It Reveals |
|--------|----------------|
| The user / product owner | Real-world workflows, pain points, feature requests |
| Existing feature set | What needs are already met (may reveal gaps by contrast) |
| Industry conventions | Standard needs for this type of system (e.g., CRM → pipeline visibility, reporting) |
| Support tickets / feedback | Unmet needs expressed as complaints or requests |

### Needs Table Template

Produce one table per persona:

```markdown
### [Persona Name]

[1-2 sentence description of role and primary concern]

| # | Need | Priority |
|---|------|----------|
| P1-N1 | [Need description] | Critical |
| P1-N2 | [Need description] | High |
| P1-N3 | [Need description] | Medium |
```

---

## Phase 3: Capability Mapping: Map Needs to Features

### Overview

Systematically investigate the codebase and map each persona need to existing features. Determine coverage status for every need.

### Codebase Investigation Checklist

Work through each category to ensure thorough capability mapping. Check every item relevant to the project's tech stack.

#### Frontend Investigation

| What to Check | Where to Look | What It Reveals |
|---------------|--------------|-----------------|
| Pages / views | `src/pages/`, `src/views/`, route definitions | Available user-facing screens |
| Navigation / sidebar | Layout components, nav config | Feature organization and user journey |
| Filter / sort controls | List page components, filter dropdowns | Data slicing capabilities |
| Dashboard / report components | Dashboard pages, chart components | Analytics and visibility features |
| Forms / create dialogs | Modal components, form components | Data entry capabilities |
| Bulk action controls | Toolbar components, selection handlers | Multi-record operations |
| Import / export UI | File upload components, download buttons | Data migration capabilities |
| Settings / admin pages | Settings routes, admin panels | Configuration capabilities |
| Search components | Search bar, global search, entity search | Discovery and lookup capabilities |

#### Backend Investigation

| What to Check | Where to Look | What It Reveals |
|---------------|--------------|-----------------|
| API endpoints | Route files, controller files | Available operations |
| Query filters | WHERE clauses, query builders | Supported filtering dimensions |
| Aggregation endpoints | Report/analytics routes | Reporting capabilities |
| Role / permission checks | Middleware, guards, decorators | Access control model |
| Webhook / notification handlers | Event handlers, notification services | Automation capabilities |
| Background jobs / cron | Job schedulers, task queues | Automated processing |
| Integration endpoints | Third-party API calls, OAuth flows | External system connections |

#### Schema Investigation

| What to Check | Where to Look | What It Reveals |
|---------------|--------------|-----------------|
| Entity tables | Schema definitions, migrations | Domain model scope |
| Enum types | Enum definitions, CHECK constraints | Supported categories and statuses |
| Relationship columns | Foreign keys, join tables | Entity associations |
| Metadata / custom fields | JSON columns, EAV patterns, custom column tables | Extensibility |
| Audit / activity tables | Activity logs, history tables | Tracking and audit capabilities |
| Configuration tables | Settings, preferences, feature flags | Customization capabilities |

### Coverage Status

Assign one of three statuses to each need:

| Status | Symbol | Definition |
|--------|--------|-----------|
| **Full** | ✅ | The need is fully met by existing features. |
| **Partial** | ⚠️ | Some aspects of the need are met, but gaps remain. |
| **Gap** | ❌ | The need is not met at all by existing features. |

### Capability Mapping Table Template

Produce a single consolidated table:

```markdown
| Need ID | Need | Mapped Feature(s) | Coverage | Notes |
|---------|------|--------------------|----------|-------|
| P1-N1 | [Need description] | [Feature name, page, endpoint] | ✅ Full | [Brief note] |
| P1-N2 | [Need description] | [Partial feature] | ⚠️ Partial | [What's missing] |
| P2-N3 | [Need description] |, | ❌ Gap | [No existing capability] |
```

---

## Phase 4: Gap Analysis: Identify and Classify Gaps

### Overview

For each need with Partial or Gap coverage, produce a detailed gap entry. Assign severity, list affected personas, and describe the gap precisely.

### Gap Entry ID Scheme

Use the format `PD-{number}` (Product Debt) for consistency with arc42 Section 11 conventions. Continue from the highest existing PD-xxx number if Section 11 already has product debt entries.

### Severity Classification

| Severity | Criteria |
|----------|----------|
| **Critical** | Blocks a persona's primary workflow entirely. Multiple personas affected. |
| **High** | Significant capability missing. Persona can work around it but with major friction. |
| **Medium** | Notable gap but persona can function. Single persona or secondary workflow affected. |
| **Low** | Nice-to-have. Improves experience but does not block any workflow. |

### Cross-Referencing with Technical Risks

When a gap overlaps with an existing technical risk (R-xxx in Section 11):

- Reference the risk entry: "Prerequisite: fix R-001 (access control) first"
- Do not duplicate, if the risk audit already covers the technical aspect, the product debt entry should focus on the user-facing capability gap
- Example: R-001 (no multi-tenant isolation) is a technical risk; PD-001 (role-based cross-user visibility) is the corresponding product debt

### Gap Entry Template

```markdown
### PD-XXX: [Gap Title] {#pd-xxx}

**Severity**: Critical | High | Medium | Low, **Personas**: [List affected persona IDs and names]

[2-4 sentences: what is missing, why the persona needs it, and what workaround (if any) exists today.]
```

### Cross-Persona Gap Matrix Template

Produce a matrix showing which gaps affect which personas:

```markdown
| Gap | P1 | P2 | P3 | P4 | P5 | Severity |
|-----|:--:|:--:|:--:|:--:|:--:|----------|
| PD-001: [Title] | X | X | | | X | Critical |
| PD-002: [Title] | | | X | X | | High |
```

This matrix is the key deliverable for prioritization, gaps that affect multiple personas are typically higher priority.

---

## Phase 5: Deliverables: Produce Output Artifacts

### Overview

Assemble the outputs from Phases 1-4 into structured deliverables. These can be standalone or integrated into arc42 documentation.

### Deliverable Checklist

| Deliverable | Format | Destination |
|-------------|--------|-------------|
| Persona profiles with needs tables | Markdown sections | arc42 Section 01, §1.4 |
| Capability-to-feature traceability matrix | Markdown table | arc42 companion doc (`requirements.md`) or standalone |
| Cross-persona gap matrix | Markdown table | arc42 Section 11, §11.3 |
| Product debt entries (PD-xxx) | Markdown sections | arc42 Section 11, §11.3 |
| Prioritized remediation roadmap | Numbered list | arc42 Section 11, §11.3 (bottom) |

### Arc42 Integration Points

#### Section 01: Introduction and Goals (§1.4 Stakeholders)

Replace or enrich the stakeholder table with full persona profiles. Each persona gets:

1. A heading with role name
2. A 1-2 sentence description
3. A needs table with ID, need description, and priority

Add a cross-reference to the requirements companion for the traceability matrix:

```markdown
See the [Stakeholder Traceability](requirements.md#stakeholder-traceability) matrix
in the requirements companion for the mapping between persona needs and functional requirements.
```

#### Section 11: Risks and Technical Debt (§11.3 Product Debt)

Add a new subsection `§11.3 Product Debt` (if it does not exist) containing:

1. The cross-persona gap matrix
2. Individual PD-xxx entries with severity, affected personas, and description
3. A remediation priority list at the bottom

#### Requirements Companion (requirements.md)

Add a `Stakeholder Traceability` section mapping persona need IDs to functional requirement IDs:

```markdown
## Stakeholder Traceability

| Persona Need | Requirement(s) | Coverage |
|-------------|----------------|----------|
| C1 (CEO: pipeline visibility) | FR-05.1, FR-05.2 | ✅ Full |
| M2 (Marketing: target contacts) | FR-01.3 | ⚠️ Partial |
```

### Remediation Roadmap Template

Order gaps by priority, considering:

1. **Severity**, Critical before High before Medium before Low
2. **Cross-persona impact**, gaps affecting more personas rank higher
3. **Dependencies**, items that unblock other items come first
4. **Technical prerequisites**, note R-xxx risks that must be fixed before a PD-xxx can be addressed

```markdown
### Remediation Priority

1. **PD-001 ([Title])**, [Why first]. Prerequisite: [R-xxx if applicable].
2. **PD-002 ([Title])**, [Why second].
3. **PD-003 ([Title])**, [Why third].
```

---

## Execution Guidelines

### For a Full Analysis

1. Run Phase 1, identify personas from codebase and user input
2. Run Phase 2, elicit needs for each persona
3. Run Phase 3, systematically investigate the codebase using the checklist
4. Run Phase 4, produce gap entries and the cross-persona matrix
5. Run Phase 5, write deliverables to arc42 sections
6. Present a summary to the user before writing files

### For a Targeted Analysis

If the user asks about a specific persona or capability area:

1. Focus Phase 1-2 on the relevant persona(s)
2. Run Phase 3 only for the relevant capability area
3. Produce gap entries only for identified gaps
4. Update the relevant arc42 sections incrementally

### For an Incremental Update

If persona analysis already exists in Section 01/Section 11:

1. Read existing persona profiles and PD-xxx entries
2. Note the highest PD-xxx number
3. Run phases only for new or changed personas
4. Add new entries, continuing the PD-xxx sequence
5. Update the cross-persona gap matrix

### Interaction Guidelines

| Situation | Action |
|-----------|--------|
| Organization structure is unknown | Ask the user about team structure, business units, and user roles |
| Persona list seems complete from codebase | Present the roster to the user for confirmation before proceeding |
| A need's priority is ambiguous | Infer from codebase usage patterns; ask only if genuinely uncertain |
| A feature's coverage status is unclear | Investigate the codebase more deeply before marking as Partial |
| The user disagrees with a priority or gap assessment | Defer to the user, they know their organization better than the code reveals |

---

## Portability

This skill is stack-neutral. It resolves everything project-specific, the language,
frameworks, database, test and deploy commands, ID prefixes, and the current
lifecycle phase, from `.vmodel.yml` and `docs/project-context.md` (see "Project
Context" above). To adopt it in a new project, run the `vmodel-setup` skill to scaffold the two
context files, fill in the stack and the current phase, and the skill adapts
automatically. It carries no assumption about any specific platform or vendor.
