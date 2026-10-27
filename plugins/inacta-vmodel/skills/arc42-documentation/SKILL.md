---
name: arc42-documentation
description: Generate and maintain arc42 architecture documentation for any project. Covers all 12 standard sections plus optional companion documents (requirements, functional decomposition). Use when the user asks for architecture documentation, arc42, system documentation, technical documentation, or architectural overview. Enforces strict adherence to the 12-section arc42 standard, new topics go into existing sections, never as non-standard sections.
---

# Arc42 Architecture Documentation

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

- **Inception**: Establish the frame: Sections 1, 3, 4, 5, 9 (goals, scope and context, solution strategy, top-level building blocks, key decisions).
- **Build**: Keep Sections 5, 6, 7, 8 current as the system is built, and add an ADR for each significant decision.
- **Run**: Focus on freshness and the operational sections 7, 10, 11 (deployment view, quality, risks and technical debt).

Generate comprehensive architecture documentation following the [arc42 template](https://arc42.org) standard. This skill produces one markdown file per section, a README index, and optional companion documents, all derived by analyzing the actual codebase.

## When to Use

- The user asks for architecture documentation, system documentation, or technical documentation
- The user asks for arc42 documentation specifically
- The user wants to document their system's architecture, decisions, or risks
- The user asks for a building block view, deployment view, or similar architectural artifact
- The user wants to create or update architectural documentation for an existing codebase

## Core Principle: Strict Standard Adherence

Arc42 defines exactly **12 sections**. Never create a Section 13 or beyond. If a topic does not have its own section, it belongs inside an existing one:

| Topic | Where It Goes | Rationale |
|-------|---------------|-----------|
| Design by Contract / behavioral specs | Section 5 (Building Block View, §5.4) | Component specifications are part of the building block decomposition |
| System-wide invariants | Section 8 (Cross-cutting Concepts) | Invariants are cross-cutting by definition |
| Contract violations / arch debt | Section 11 (Risks and Technical Debt) | Violations are a form of technical debt |
| API documentation | Section 5 (packages) + Section 6 (runtime flows) | API is part of the system's structure and behavior |
| Performance characteristics | Section 10 (Quality Requirements) | Performance is a quality attribute |
| Monitoring / observability | Section 7 (Deployment) or Section 8 (Cross-cutting) | Infrastructure concern or cross-cutting pattern |
| Security architecture | Section 8 (Cross-cutting Concepts) | Security is a cross-cutting concern |
| User interface concept (interaction model) | Section 8 (Cross-cutting Concepts) | One concept for all screens. Summarize the concept inventory, object map and object-action matrix from `interaction-model` (`docs/ui/`), link the full sheets, do not copy them |
| Data model / ERD | Section 5 (Building Block View) | Data model is part of the system's structure |
| Migration strategy | Section 9 (Architecture Decisions) | Migrations are architectural choices |
| Coding conventions | Section 2 (Architecture Constraints) | Conventions are constraints on development |

If you genuinely cannot fit a topic into any of the 12 sections, create a **companion document** (like `requirements.md` or `functional-decomposition.md`) and reference it from the README, but this should be rare.

## File Structure

```
docs/arc42/
├── README.md                      # Index with section table and maintenance guidance
├── 01-introduction-and-goals.md   # Purpose, requirements, quality goals, stakeholders
├── 02-architecture-constraints.md # Technical, organizational, and convention constraints
├── 03-system-scope-and-context.md # Business and technical context boundaries
├── 04-solution-strategy.md        # Key technology and architecture decisions
├── 05-building-block-view.md      # Package decomposition, dependencies, component specs
├── 06-runtime-view.md             # Key interaction scenarios as sequence diagrams
├── 07-deployment-view.md          # Hosting, routing, environments, process management
├── 08-cross-cutting-concepts.md   # Auth, validation, audit trails, patterns, invariants
├── 09-architecture-decisions.md   # ADRs (Architecture Decision Records)
├── 10-quality-requirements.md     # Quality tree and quality scenarios
├── 11-risks-and-technical-debt.md # Known risks (R-00x) and debt items table
├── 12-glossary.md                 # Domain and technical term definitions
├── requirements.md                # (Optional companion) Functional requirements
└── functional-decomposition.md    # (Optional companion) Capability breakdown
```

## Step-by-Step Generation Procedure

### Phase 1: Codebase Analysis

Before writing any documentation, thoroughly analyze the codebase:

1. **Identify the tech stack**, frameworks, languages, ORMs, build tools, package managers
2. **Map the package/module structure**, deployable artifacts vs shared libraries
3. **Read database schemas**, table definitions, relationships, constraints, enums
4. **Read route/controller files**, API endpoints, middleware pipeline, validation patterns
5. **Read frontend entry points**, routing, state management, component organization
6. **Check deployment configuration**, environment variables, process management, hosting
7. **Identify authentication/authorization**, auth flow, session management, access control
8. **Look for codegen or contract-first patterns**, OpenAPI specs, generated code, schema validation
9. **Note architectural decisions**, patterns chosen and alternatives rejected
10. **Find risks and debt**, missing constraints, hardcoded values, TODO comments, missing tests

### Phase 2: Write Sections (In Order)

Generate each section using the templates below. Write all sections before presenting to the user.

---

## Section Templates

### Section 01: Introduction and Goals

```markdown
# Section 01: Introduction and Goals

## 1.1 Purpose
[1-2 paragraphs: what the system does and why it exists]

## 1.2 Requirements Overview
| Priority | Requirement | Description |
|----------|-------------|-------------|
| 1 | [Top requirement] | [Brief description] |
[List the top 5-10 requirements driving the architecture]

## 1.3 Quality Goals
| Quality Goal | Description |
|--------------|-------------|
| [Goal name] | [How the architecture achieves it] |
[3-5 quality goals that shaped architectural decisions]

## 1.4 Stakeholders
| Stakeholder | Role | Expectations |
|-------------|------|--------------|
| [Who] | [Their role] | [What they expect from the system] |
```

**How to fill it**: Read the project README, package.json description, and any product documentation. Identify the primary users, the core problem being solved, and the quality attributes that matter most.

---

### Section 02: Architecture Constraints

```markdown
# Section 02: Architecture Constraints

## 2.1 Technical Constraints
| Constraint | Description |
|------------|-------------|
| [Constraint name] | [What it means and why it's imposed] |

## 2.2 Organizational Constraints
| Constraint | Description |
|------------|-------------|
| [Constraint name] | [Team size, process, licensing, etc.] |

## 2.3 Conventions
| Convention | Description |
|------------|-------------|
| [Convention name] | [Coding standards, naming, patterns adopted] |
```

**How to fill it**: Check the hosting platform, language/framework requirements, dependency constraints, team structure, and any coding conventions visible in the codebase (linting configs, naming patterns, file organization).

---

### Section 03: System Scope and Context

```markdown
# Section 03: System Scope and Context

## 3.1 Business Context
[Mermaid C4Context diagram showing the system, external actors, and external systems]

| Actor / System | Direction | Description |
|----------------|-----------|-------------|
| [Actor] | → System | [What they do] |

## 3.2 Technical Context
[Mermaid flowchart showing protocols, ports, databases, external APIs]

### Communication Channels
| Channel | Protocol | Description |
|---------|----------|-------------|
| [From ↔ To] | [HTTP/HTTPS/WS/etc.] | [What flows through this channel] |
```

**How to fill it**: Identify every external system the application communicates with (databases, auth providers, third-party APIs, message queues, CDNs). Draw the boundary between "our system" and "everything else."

---

### Section 04: Solution Strategy

```markdown
# Section 04: Solution Strategy

## 4.1 Technology Decisions
| Decision | Technology | Rationale |
|----------|-----------|-----------|
| [Decision area] | [Chosen tech] | [Why this was chosen] |

## 4.2 Architecture Approach
[Describe key architectural patterns: monolith vs microservices, contract-first,
 layered vs clean architecture, event-driven, etc. Include Mermaid diagrams for
 data flow or codegen pipelines if applicable.]

## 4.3 Key Design Decisions
[2-4 paragraphs on the most important design choices and their tradeoffs]
```

**How to fill it**: Read `package.json` / `requirements.txt` for technology choices. Identify the dominant architectural patterns from the code structure. Focus on decisions that have wide-reaching impact.

---

### Section 05: Building Block View

```markdown
# Section 05: Building Block View

## 5.1 Top-Level Decomposition
[Mermaid diagram showing packages/modules and their relationships]

## 5.2 Package Details
### Libraries
#### `package-name`: Description
- **Responsibility**: [What it does]
- **Key Files**: [Important files]
- **Consumers**: [Who uses it]

### Artifacts (Deployable)
#### `artifact-name`: Description
- **Responsibility**: [What it does]
- **Key Components**: [Important modules within it]

## 5.3 Dependency Summary
| Package | Depends On |
|---------|------------|
| `pkg-a` | `pkg-b`, `pkg-c` |
```

**How to fill it**: Map the directory structure. For monorepos, list each package/workspace. For single-app projects, list the major modules/directories. Show import relationships.

**Optional enrichment**: Add §5.4 "Logical Component Specifications" with Design by Contract specs. See the `arc42-design-by-contract` skill for details.

---

### Section 06: Runtime View

```markdown
# Section 06: Runtime View

## 6.1 [Scenario Name]
[Mermaid sequence diagram showing the interaction]

### Key Points
- [Notable aspects of this flow]
```

**How to fill it**: Identify the 3-6 most important runtime scenarios:
- Authentication / login flow
- The primary CRUD operation (e.g., creating the main domain entity)
- Any complex multi-step flow (e.g., stage transitions with side effects)
- Error handling scenarios
- Background jobs or async processing (if any)

Use Mermaid `sequenceDiagram` syntax with participants labeled clearly.

---

### Section 07: Deployment View

```markdown
# Section 07: Deployment View

## 7.1 Infrastructure Overview
[Mermaid diagram showing servers, containers, databases, proxies]

## 7.2 Routing / Service Mapping
| Path / Port | Service | Description |
|-------------|---------|-------------|
| [route] | [service] | [what it serves] |

## 7.3 Environment Variables
| Variable | Purpose |
|----------|---------|
| `VAR_NAME` | [What it configures] |

## 7.4 Development vs Production
| Aspect | Development | Production |
|--------|-------------|------------|
| [Aspect] | [Dev setup] | [Prod setup] |
```

**How to fill it**: Check deployment configs, Dockerfiles, platform settings, environment variables, process management tools, and CI/CD pipelines. Document how traffic reaches each service.

---

### Section 08: Cross-cutting Concepts

```markdown
# Section 08: Cross-cutting Concepts

## 8.1 [Concept Name]
[Description of the cross-cutting pattern, how it works, and where it applies]
```

**How to fill it**: Identify patterns that appear across multiple components:
- Authentication and authorization
- Validation / contract enforcement
- Logging / error handling
- Audit trails
- Polymorphic patterns (shared tables, generic associations)
- Data ownership / tenancy model
- Pagination and sorting conventions
- Caching strategies

Each concept gets its own subsection. Order from most important to least.

---

### Section 09: Architecture Decisions

Use the ADR (Architecture Decision Record) format:

```markdown
# Section 09: Architecture Decisions

## ADR-001: [Decision Title]

**Status**: Accepted | Deprecated | Superseded

**Context**: [Why this decision was needed]

**Decision**: [What was decided]

**Consequences**:
- (+) [Positive consequence]
- (−) [Negative consequence / tradeoff]

---
```

**How to fill it**: Look for decisions that shaped the architecture:
- Framework and language choices
- Database design patterns (e.g., polymorphic FKs, JSONB vs normalized)
- API design approach (REST, GraphQL, contract-first)
- Authentication strategy
- Monolith vs microservices
- Code generation vs manual typing
- Service layer vs route-handler-only

Aim for 4-8 ADRs covering the most impactful decisions.

---

### Section 10: Quality Requirements

```markdown
# Section 10: Quality Requirements

## 10.1 Quality Tree
[Mermaid mindmap showing quality attributes as branches]

## 10.2 Quality Scenarios

### QS-1: [Scenario Title]
| Attribute | Value |
|-----------|-------|
| **Quality** | [Which quality attribute] |
| **Stimulus** | [What triggers this scenario] |
| **Response** | [How the system responds] |
| **Measure** | [How to verify the response is correct] |
```

**How to fill it**: Derive quality attributes from Section 1.3 quality goals. Create concrete, testable scenarios for each. Common quality attributes: type safety, runtime validation, security, performance, extensibility, usability, maintainability.

---

### Section 11: Risks and Technical Debt

```markdown
# Section 11: Risks and Technical Debt

## 11.1 Risks

### R-001: [Risk Title]
**Severity**: High | Medium | Low
**Description**: [What the risk is]
**Impact**: [What happens if it materializes]
**Mitigation**: [How to address it]

---

## 11.2 Technical Debt
| Item | Severity | Description |
|------|----------|-------------|
| [Debt item] | Medium | [What it is and why it matters] |
```

**How to fill it**: Look for:
- Missing access control or authorization gaps
- Missing database constraints (app-enforced only)
- Large files that need refactoring
- Duplicated code
- Missing tests
- Hardcoded values that should be configurable
- Missing rate limiting, caching, or performance optimizations
- Missing monitoring or observability

Assign R-00x identifiers to risks for cross-referencing.

---

### Section 12: Glossary

```markdown
# Section 12: Glossary

## Domain Terms
| Term | Definition |
|------|-----------|
| [Term] | [What it means in this system's domain] |

## Technical Terms
| Term | Definition |
|------|-----------|
| [Term] | [What the technology/tool/pattern is] |
```

**How to fill it**: Extract domain terms from database table names, API endpoints, and UI labels. Extract technical terms from the dependency list and architectural patterns used. Define every term that a new team member would need to look up.

---

### README Index

```markdown
# [Project Name]: arc42 Architecture Documentation

## Section Overview
| File | Section | Purpose |
|------|---------|---------|
| [`01-introduction-and-goals.md`](01-introduction-and-goals.md) | Introduction and Goals | ... |
[One row per section + companion documents]

## How to Maintain and Extend
1. **When adding a new domain entity**, Update Sections 05, 12, and companion docs
2. **When adding a new API route**, Update Section 06 if novel pattern
3. **When changing infrastructure**, Update Sections 02, 07
4. **When making an architecture decision**, Add ADR to Section 09
5. **When introducing a cross-cutting concern**, Section 08
6. **When identifying new risks**, Section 11
[Add project-specific maintenance items]

### Conventions
- Use Mermaid syntax for diagrams
- Mark uncertain information with `[ASSUMPTION]`
- Cross-reference sections using relative markdown links
- Keep terminology consistent with the Glossary
```

---

## Optional Companion Documents

These are **not** arc42 sections. They live alongside the 12 sections as supplementary references.

### Requirements Specification (`requirements.md`)

Use when the project has detailed functional requirements that would clutter Section 1:

```markdown
# Requirements Specification

## Functional Requirements
### FR-01: [Feature Area]
| ID | Requirement | Implementation |
|----|-------------|----------------|
| FR-01.1 | [Requirement text] | [Which code implements it] |
```

### Functional Decomposition (`functional-decomposition.md`)

Use when you want a hierarchical capability breakdown with implementation traceability:

```markdown
# Functional Decomposition

## 1. [Capability Area]
### 1.1 [Sub-capability]
- **CRUD Operations**: [files that implement it]
- **Listing with Filters**: [filter dimensions]
- **Bulk Actions**: [available bulk operations]
```

---

## Writing Guidelines

1. **Be factual, not aspirational**, document what the system *is*, not what it should be. Use `[ASSUMPTION]` for unverified claims.
2. **Use Mermaid diagrams**, they render in GitHub, GitLab, and most doc tools. Prefer `flowchart`, `sequenceDiagram`, `C4Context`, and `mindmap`.
3. **Cross-reference between sections**, use relative markdown links: `[see Section 05](05-building-block-view.md)`.
4. **Keep tables aligned**, tables are easier to scan than prose for structured information.
5. **Be precise about files**, reference actual source file paths, not abstract module names.
6. **Mark uncertainty**, if you're inferring behavior from code without running it, say `[ASSUMPTION]`.
7. **Keep the glossary complete**, every domain term and non-obvious technical term should be defined.
8. **Maintain consistency**, use the same term everywhere (check the glossary). Don't call something "Order" in one section and "Purchase" in another.
9. **Update incrementally**, when the codebase changes, update the affected sections. The README's maintenance guidance tells you which sections to touch.

## Quality Checklist

Before delivering the documentation, verify:

- [ ] All 12 sections are present (no more, no less)
- [ ] README has a complete index table and maintenance guidance
- [ ] Section 03 has both business and technical context diagrams
- [ ] Section 05 lists every package/module with responsibilities
- [ ] Section 06 has at least 3 runtime scenarios with sequence diagrams
- [ ] Section 07 documents all environment variables and routing
- [ ] Section 08 covers authentication and at least 2 other cross-cutting concerns
- [ ] Section 09 has at least 3 ADRs
- [ ] Section 10 has a quality tree and at least 3 quality scenarios
- [ ] Section 11 has at least 2 risks and a technical debt table
- [ ] Section 12 covers all domain terms and key technical terms
- [ ] All Mermaid diagrams use valid syntax
- [ ] Cross-references between sections use correct relative links
- [ ] No non-standard sections (13+) exist

## Relationship to Other Skills

- **`arc42-design-by-contract`**, Use this companion skill to enrich Section 5 with formal Eiffel-style DbC component specifications. It provides the notation convention, component block template, worked example, and codebase analysis procedure for generating behavioral contracts. Always integrate DbC content into the standard sections (5, 8, 11), never as a separate section.

## Portability

This skill is stack-neutral. It resolves everything project-specific, the language,
frameworks, database, test and deploy commands, ID prefixes, and the current
lifecycle phase, from `.vmodel.yml` and `docs/project-context.md` (see "Project
Context" above). To adopt it in a new project, run the `vmodel-setup` skill to scaffold the two
context files, fill in the stack and the current phase, and the skill adapts
automatically. It carries no assumption about any specific platform or vendor.
