---
name: arc42-design-by-contract
description: Generate Eiffel-style Design by Contract (DbC) component specifications integrated into arc42 architecture documentation. Use when the user asks for architecture documentation, formal component specifications, design by contract, behavioral contracts, preconditions/postconditions/invariants, or arc42 documentation enrichment.
---

# Arc42 Design by Contract Specification

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

- **Inception**: Define the target contracts (preconditions, postconditions, invariants) for the key components from the architecture, before code exists. The contracts are the design intent.
- **Build**: Implement and verify contracts against the code, refine them as components take shape, and record any violations in Section 11.
- **Run**: Treat the contracts as the regression and monitoring reference. Only add or change a contract when behaviour changes through a fix or enhancement.

Generate formal Eiffel-style Design by Contract (DbC) component specifications and integrate them into arc42 architecture documentation. This skill codifies a methodology for specifying component behavior with preconditions, postconditions, and invariants, then placing those specifications in the correct arc42 sections with full source-file traceability.

## When to Use

- The user asks for formal architecture documentation or component specifications
- The user wants Design by Contract or behavioral contracts for their system
- The user asks to enrich existing arc42 documentation with formal specifications
- The user wants to document invariants, preconditions, or postconditions
- The user asks for component traceability (which source files implement which logical component)

## Arc42 Integration Rules

DbC content belongs in three standard arc42 sections, never create a non-standard section (e.g., Section 13):

| Content Type | Arc42 Location | Purpose |
|-------------|----------------|---------|
| Per-component contracts (invariant, require, ensure) | **Section 5 (Building Block View), §5.4** | Logical component layer above the physical package listing |
| System-wide invariants | **Section 8 (Cross-cutting Concepts), §8.8** | Architectural invariants that span all components |
| Contract violations / architectural debt | **Section 11 (Risks and Technical Debt)** | Known deviations from specified contracts |

### Section 5 Structure

Add a new subsection (e.g., §5.4 "Logical Component Specifications") after the existing package-level decomposition. Each component block has three parts:

1. **Responsibility**, one-sentence description of what the component does
2. **Implementation Mapping**, table linking source files to packages and roles
3. **Contract Specification**, fenced code block with DbC notation

### Section 8 Structure

Add a subsection (e.g., §8.8 "System-wide Architectural Invariants") containing a single `system` block with invariants that apply across all components. Cross-reference §5.4 and any existing contract enforcement documentation.

### Section 11 Structure

Add new risk entries (R-00x format) for each known contract violation. Each entry needs: severity, description, impact, mitigation, and the DbC principle violated.

## DbC Notation Convention

Include this table at the top of §5.4:

| Keyword | Meaning |
|---------|---------|
| `require` | Precondition, caller's obligation; must hold before feature execution |
| `ensure` | Postcondition, supplier's guarantee; must hold after feature execution |
| `invariant` | Class/component invariant, must hold at every stable state boundary |
| `old(expr)` | Value of `expr` at feature entry (before mutation) |
| `void` | Null / absent / undefined |
| `∀`, `∃` | Universal and existential quantifiers over sets |
| `⟹` | Logical implication |
| `∧`, `∨` | Logical conjunction and disjunction |
| `∈`, `∉` | Set membership and non-membership |
| `Σ` | Summation |

## Component Block Template

Use this template for each logical component in §5.4:

````markdown
### 5.4.N `ComponentName`

**Responsibility**: One-sentence description of what this component does.

#### Implementation Mapping

| Source File | Package | Role |
|-------------|---------|------|
| `path/to/file.ts` | `package-name` | Route handler / DB schema / Validation / Frontend page / the data-fetching layer hooks |

#### Contract Specification

```
component COMPONENT_NAME

invariant
    -- Data integrity rules that must hold at every stable state boundary
    -- Use quantifiers to express constraints over sets (tables)
    ∀ x ∈ table : x.field ≠ void ⟹ constraint_expression

    -- Deletion strategies (cascade or set-null)
    ∀ x ∈ old(parent_table) \ parent_table :
        ∀ y ∈ child_table : old(y.parentId) = x.id ⟹ y ∉ child_table  -- cascade
        -- OR: y.parentId = void  -- set-null

feature feature_name (params)
    require
        -- Authentication check
        request.isAuthenticated() = true
        -- Input validation (from validation schemas)
        body.requiredField ≠ void
        -- Referential integrity checks
        body.foreignKey ≠ void ⟹ ∃ ref ∈ referenced_table : ref.id = body.foreignKey
        -- Enum constraints
        body.enumField ≠ void ⟹ body.enumField ∈ {value1, value2, value3}
    ensure
        -- State mutation guarantee
        ∃ x ∈ table : x.field = body.field
        -- Attribution
        x.userId = request.user.id
        -- Response contract
        response.status = 201
        -- Side effects (e.g., audit trail)
        old(field) ≠ new(field) ⟹ ∃ audit ∈ audit_table : audit.entityId = x.id
```
````

## Step-by-Step Procedure

Follow this procedure to generate DbC specifications from an existing codebase:

### Step 1: Identify Domain Components

Scan the codebase for logical domain groupings that span multiple packages. Look for:

- **Route files**, each route module often corresponds to one domain component
- **Database schema files**, table definitions reveal entity boundaries
- **Frontend pages**, each major page usually maps to a domain component

Name each component using a descriptive noun (e.g., `ContactManager`, `OrderLifecycleManager`, `AuthenticationService`).

### Step 2: Trace Invariants from Schema

For each component, read the database schema and extract:

- **NOT NULL constraints** → `field ≠ void` invariants
- **CHECK constraints** → bounded value invariants (e.g., `0 ≤ probability ≤ 100`)
- **FOREIGN KEY constraints** → referential integrity invariants
- **UNIQUE constraints** → uniqueness invariants
- **ENUM types** → enumeration closure invariants
- **CASCADE/SET NULL rules** → deletion strategy invariants
- **Implicit constraints**, rules enforced by application logic but not by the database (mark these with comments noting the enforcement gap)

### Step 3: Trace Preconditions from Route Validation

For each feature (API endpoint), read the route handler and extract:

- **Authentication checks** → `request.isAuthenticated() = true`
- **the validation layer `safeParse` calls** → input schema validation preconditions
- **Existence checks** (e.g., "pipeline must exist") → `∃ x ∈ table : x.id = param`
- **Enum membership checks** → `field ∈ {value1, value2}`
- **Business rule checks** → domain-specific preconditions (e.g., "stage must belong to pipeline")

### Step 4: Trace Postconditions from Route Handlers

For each feature, read the handler's mutation logic and extract:

- **INSERT operations** → `∃ x ∈ table : x.field = body.field`
- **UPDATE operations** → `table[id] reflects body fields`
- **DELETE operations** → `x ∉ table` plus cascade/nullification effects
- **Side effects**, audit trail entries, notifications, computed field updates
- **Response shape** → `response.status = 201`, `response.body` structure

Pay special attention to **implicit postconditions**, side effects that happen alongside the main mutation (e.g., audit trail generation on deal updates).

### Step 5: Map Source Files

For each component, create the Implementation Mapping table by listing every source file that participates in the component's behavior:

| Role Category | What to Look For |
|---------------|-----------------|
| Route handler | Express/Fastify route files with CRUD endpoints |
| DB schema | the ORM/Prisma/TypeORM table definitions |
| Validation | the validation layer/Joi/Yup schema files (may be generated) |
| API spec | OpenAPI/Swagger definition files |
| Frontend page | React/Vue/Angular pages that consume the component's API |
| the data-fetching layer hooks | Generated or hand-written data fetching hooks |
| Middleware | Auth, validation, or logging middleware specific to this component |

### Step 6: Extract System-wide Invariants

After specifying all components, identify invariants that span multiple components:

- **Data visibility model**, who can see what data (e.g., all users see all data, or tenant isolation)
- **Contract-first patterns**, if schemas are generated from a spec, document the single-source-of-truth chain
- **Idempotency guarantees**, which operations are side-effect free
- **Deletion strategies**, document the system-wide approach to cascade vs. set-null
- **Enumeration closure**, list all enum types and their valid values

Place these in Section 8.8 as a single `system` block.

### Step 7: Identify Contract Violations

Review each component's specification against the actual implementation and note any gaps:

- **Missing DB constraints**, invariants enforced only by application code
- **Inconsistent side effects**, postconditions that hold for single operations but not bulk operations
- **Weak preconditions**, missing authorization or ownership checks
- **Representation ambiguities**, dual representations of the same data

Document each violation in Section 11 using the standard risk format with a "DbC Principle Violated" field.

## Maintenance Guidance

When adding to or updating the arc42 documentation:

- **New component**: Add a new §5.4.N block with all three parts (responsibility, mapping, contract)
- **New feature on existing component**: Add a new `feature` block within the existing component's contract
- **Schema change**: Update the relevant invariants and check whether postconditions are affected
- **New contract violation discovered**: Add to Section 11 with the R-00x format
- **System-wide rule change**: Update Section 8.8

## Portability

This skill is stack-neutral. It resolves everything project-specific, the language,
frameworks, database, test and deploy commands, ID prefixes, and the current
lifecycle phase, from `.vmodel.yml` and `docs/project-context.md` (see "Project
Context" above). To adopt it in a new project, run the `vmodel-setup` skill to scaffold the two
context files, fill in the stack and the current phase, and the skill adapts
automatically. It carries no assumption about any specific platform or vendor.
