---
name: arc42-risk-audit
description: Perform systematic architecture risk audits and produce mitigation plans in arc42 Section 11 format. Use when the user asks for risk analysis, technical debt audit, architecture review, security audit, risk mitigation planning, or code quality assessment. Two-phase methodology, Phase 1 identifies risks via category-driven checklist, Phase 2 produces prioritized remediation plans with project task templates.
---

# Arc42 Risk Audit and Mitigation

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

- **Inception**: Design-time risk. Emphasise Categories 2, 3, 7 (referential integrity, data consistency, input/output contracts) against the target architecture.
- **Build**: Run targeted audits on the categories touched by each change.
- **Run**: Operational risk. Emphasise Categories 1, 5, 6 (access control, performance, operational gaps) and maintain the risk delta against the last deployment baseline.

Systematically identify architectural risks and technical debt in any codebase, document them in arc42 Section 11 format, and produce actionable mitigation plans. This skill codifies a repeatable, category-driven audit process with concrete remediation outputs.

## When to Use

- The user asks for a risk analysis, architecture review, or technical debt audit
- The user asks to identify security gaps, missing constraints, or code quality issues
- The user asks for a risk mitigation plan or remediation roadmap
- The user wants to update Section 11 of their arc42 documentation
- The user asks "what could go wrong?" or "what should we fix next?"

## Relationship to Companion Skills

This skill works alongside two companion skills:

| Skill | Relationship |
|-------|-------------|
| `arc42-documentation` | Defines the Section 11 format this skill writes into. Risk entries use the R-00x format from the documentation skill's Section 11 template. |
| `arc42-design-by-contract` | Provides formal component specifications (preconditions, postconditions, invariants) that serve as the behavioral baseline. Phase 1 auditing compares implementation against these contracts to find violations. |

**Typical workflow**: Generate arc42 documentation → Add DbC specifications → Run risk audit → Produce mitigation plan.

---

## Phase 1: Risk Audit

### Overview

Scan the codebase systematically using the category checklist below. For each category, examine specific code patterns and record any findings as risk entries.

### Pre-Audit Setup

Before beginning the audit:

1. **Read existing Section 11** (if it exists) to avoid duplicating already-documented risks. Note the highest R-00x number so new entries continue the sequence.
2. **Read Section 5.4** (if it exists) to load DbC component specifications. These serve as the formal behavioral baseline, any implementation that violates a spec is a finding.
3. **Identify the tech stack**, note the ORM, web framework, auth library, and validation library so you know which code patterns to look for.

### Category Checklist

Work through each category in order. For every finding, record it using the Risk Entry Template (below).

#### Category 1: Access Control

Scan for authorization and data visibility gaps.

| What to Look For | Where to Look | Example Finding |
|-------------------|--------------|-----------------|
| Read queries that do not filter by `userId` or tenant ID | Route handlers, ORM queries | "All contacts visible to any authenticated user" |
| Missing ownership checks on UPDATE/DELETE | Route handlers | "Any user can delete any deal" |
| No role differentiation (admin vs. editor vs. viewer) | Middleware, route guards | "All authenticated users have identical permissions" |
| Session management gaps (no expiry cleanup, no revocation) | Session store, auth middleware | "Expired sessions accumulate without cleanup" |
| Missing CSRF protection on state-changing endpoints | Middleware pipeline | "POST/PUT/DELETE endpoints lack CSRF tokens" |

#### Category 2: Referential Integrity

Scan for foreign key and relationship enforcement gaps.

| What to Look For | Where to Look | Example Finding |
|-------------------|--------------|-----------------|
| Polymorphic `entityId` columns without DB foreign keys | Schema definitions | "`entity_tags.entity_id` references multiple tables but has no FK constraint" |
| Application-only FK enforcement (not backed by DB constraint) | Validation logic vs. schema | "Parent existence checked in JS but not by DB FK" |
| Missing cascade or set-null on parent deletion | Schema ON DELETE clauses, delete handlers | "Deleting a company orphans its contacts" |
| Orphaned rows after parent deletion | Delete handlers | "Deleting a contact does not remove its tag associations" |
| Dual/competing representations of the same relationship | Schema columns | "Both `company` text field and `companyId` FK exist on contacts" |

#### Category 3: Data Consistency

Scan for rules that the database should enforce but does not.

| What to Look For | Where to Look | Example Finding |
|-------------------|--------------|-----------------|
| CHECK constraints enforced only in application code | validation schemas vs. DB schema | "Probability must be 0-100 per the validation layer, but no DB CHECK" |
| "At least one FK" constraints not enforced at DB level | Schema, validation | "Note must have contactId, dealId, or companyId, only validated in API" |
| ENUM values defined in the validation layer/app code but not in DB enum type | validation schemas vs. pgEnum definitions | "New stage types accepted by API but not by DB" |
| UNIQUE constraints missing at DB level | Schema vs. business rules | "Tag names should be unique per type, but DB allows duplicates" |
| Default values that differ between DB and application | Schema defaults vs. route handler defaults | "DB defaults probability to NULL, route handler defaults to 0" |

#### Category 4: Behavioral Consistency

Scan for operations that should produce identical side effects but do not.

| What to Look For | Where to Look | Example Finding |
|-------------------|--------------|-----------------|
| Single-record and bulk-record operations with different side effects | CRUD handlers vs. bulk action handlers | "Bulk stage change skips audit trail that single update generates" |
| Inconsistent audit trail generation | Audit/activity creation logic | "Update generates audit entry, but bulk update does not" |
| Event/notification gaps between equivalent operations | Webhook or notification logic | "Manual deal close sends notification, bulk close does not" |
| Computed field updates missing from some code paths | Calculated field logic | "Weighted value recalculated on single update but not on bulk" |

#### Category 5: Performance and Scalability

Scan for patterns that degrade under load.

| What to Look For | Where to Look | Example Finding |
|-------------------|--------------|-----------------|
| N+1 query patterns (loop with individual DB calls) | Route handlers with loops | "CSV import inserts one row per iteration" |
| In-memory aggregation instead of SQL aggregation | Report/analytics endpoints | "Pipeline summary loads all deals into JS array, then reduces" |
| Missing pagination on list endpoints | GET collection handlers | "GET /contacts returns all records with no LIMIT" |
| Missing database indexes on filtered/sorted columns | Schema, query WHERE/ORDER BY clauses | "Deals filtered by stageId but no index on that column" |
| Unbounded result sets from joins | Complex queries | "Activity feed joins 4 tables with no row limit" |

#### Category 6: Operational Gaps

Scan for missing operational infrastructure.

| What to Look For | Where to Look | Example Finding |
|-------------------|--------------|-----------------|
| No request rate limiting | Middleware pipeline | "API has no throttling, any client can send unlimited requests" |
| No API versioning | Route prefixes | "All routes under /api with no version prefix" |
| No health check endpoint | Route definitions | "No /health or /readiness endpoint for monitoring" |
| Hardcoded configuration that should be dynamic | Route handlers, constants | "Default pipeline stages hardcoded in route handler" |
| Missing error monitoring/alerting | Error handling middleware | "Errors logged to console only, no external error tracking" |
| No database backup/migration strategy | Schema management config | "Using ORM push with no versioned migration files" |

#### Category 7: Input/Output Contracts

Scan for API boundary weaknesses.

| What to Look For | Where to Look | Example Finding |
|-------------------|--------------|-----------------|
| Missing input validation on endpoints | Route handlers | "PUT endpoint accepts body without the validation layer validation" |
| Response shape inconsistencies | API spec vs. actual response | "OpenAPI spec says `amount: number` but handler returns string" |
| Hardcoded formatting that ignores configurable settings | Formatting logic | "Audit trail uses `$` symbol ignoring currency setting" |
| File upload without size/type validation | Upload handlers | "CSV import accepts any file type, no size limit" |
| Error responses that leak internal details | Error handling | "Database errors returned verbatim to client" |

### Risk Entry Template

For each finding, produce an entry in this format:

```markdown
### R-0XX: [Concise Risk Title]

**Severity**: High | Medium | Low

**Description**: [1-3 sentences: what the gap is and where it exists in the code]

**Impact**: [What happens if this risk materializes, data corruption, security breach, performance degradation, etc.]

**Mitigation**: [High-level approach to fix it, 1-2 sentences]

**DbC Principle Violated**: [Optional, only if a formal spec exists in §5.4. State which precondition, postcondition, or invariant is violated]
```

### Severity Classification

| Severity | Criteria | Examples |
|----------|----------|---------|
| **High** | Data can be corrupted, unauthorized access is possible, or the system can be rendered unavailable | Missing access control, no tenant isolation, cascading delete gaps on critical entities |
| **Medium** | Functionality is degraded, performance suffers at scale, or maintenance burden is significant | In-memory aggregation, inconsistent audit trails, large monolithic files, missing indexes |
| **Low** | Code quality issue, minor inconsistency, or cosmetic problem with no functional impact | Hardcoded currency symbol, duplicated utility functions, missing API versioning |

### Post-Audit Checklist

After completing all seven categories:

- [ ] Every finding has a unique R-00x identifier continuing from the existing sequence
- [ ] Severity is assigned consistently using the classification table
- [ ] Findings from DbC contract violations reference the specific spec in §5.4
- [ ] No duplicate findings (check against existing Section 11 entries)
- [ ] Technical debt items (low-severity, non-risk issues) go in the §11.2 table, not as R-00x entries

---

## Phase 2: Mitigation Planning

### Overview

Take the risk entries produced in Phase 1 (or pre-existing R-00x entries from Section 11) and produce concrete, actionable remediation plans. Each plan is detailed enough to become a project task.

### Prioritization Framework

Process risks in this order:

| Priority | Severity | Rationale |
|----------|----------|-----------|
| P1, Fix immediately | High | Security vulnerabilities, data integrity threats, authorization gaps |
| P2, Fix in next sprint | Medium | Performance issues, behavioral inconsistencies, maintainability blockers |
| P3, Fix when convenient | Low | Code quality improvements, cosmetic issues, nice-to-haves |

Within the same severity level, prioritize by:
1. **Blast radius**, how many components/users are affected
2. **Exploitability**, how easily the risk can be triggered (intentionally or accidentally)
3. **Fix complexity**, simpler fixes first (quick wins build momentum)

### Mitigation Plan Template

For each risk (or group of related risks), produce a plan:

```markdown
## Mitigation: R-0XX: [Risk Title]

**Priority**: P1 | P2 | P3
**Estimated Effort**: Small (< 1 day) | Medium (1-3 days) | Large (3+ days)

### What to Change

| File | Change Description |
|------|-------------------|
| `path/to/file.ts` | [Specific change: add middleware, modify query, add constraint, etc.] |
| `path/to/schema.ts` | [Schema change: add FK, add CHECK, add index, etc.] |
| `path/to/test.ts` | [Test: add test case to verify the fix] |

### Fix Description

[2-4 sentences describing the technical approach. Be specific about the pattern to apply.]

### Acceptance Criteria

- [ ] [Criterion 1: observable behavior that proves the fix works]
- [ ] [Criterion 2: edge case that must be handled]
- [ ] [Criterion 3: regression that must not occur]

### Dependencies

- [Other R-0XX entries that must be fixed first, or "None"]
- [External dependencies: new packages, DB migrations, etc.]
```

### Project Task Template

When the user wants to turn mitigation plans into project tasks, use this template:

```markdown
# [Risk Title]: Remediation

## What & Why
[1-2 sentences: what risk is being addressed and why it matters]
References: Section 11 R-0XX.

## Done looks like
- [Acceptance criterion 1]
- [Acceptance criterion 2]
- [Acceptance criterion 3]

## Out of scope
- [What this task deliberately does not address]

## Tasks
1. [First concrete step]
2. [Second concrete step]
3. [Verification/testing step]

## Relevant files
- `path/to/file1.ts`
- `path/to/file2.ts`
```

Group related risks into a single task when they share the same files and can be fixed together (e.g., R-001 and R-002 might both be addressed by an access control layer).

---

## Audit Execution Guidelines

### For a Full Audit

1. Run Phase 1 completely, all seven categories, in order
2. Present findings to the user as a summary table before writing to Section 11
3. After user approval, update `docs/arc42/11-risks-and-technical-debt.md`
4. Run Phase 2 on all new findings, produce mitigation plans
5. Ask the user which risks to turn into project tasks

### For a Targeted Audit

If the user asks about a specific concern (e.g., "check our access control"), run only the relevant category from Phase 1. Still produce the full risk entry and mitigation plan.

### For an Incremental Update

If Section 11 already has entries:
1. Read existing entries and note the highest R-00x number
2. Run Phase 1, skipping any issues already documented
3. Add only new findings, continuing the R-00x sequence
4. Update the technical debt table if needed

### Output Artifacts

| Artifact | Location | When to Create |
|----------|----------|----------------|
| Risk entries (R-00x) | `docs/arc42/11-risks-and-technical-debt.md` §11.1 | After Phase 1, with user approval |
| Technical debt items | `docs/arc42/11-risks-and-technical-debt.md` §11.2 | After Phase 1, for low-severity non-risk items |
| Mitigation plans | Presented to user in chat or written to a companion doc | After Phase 2 |
| Project tasks | Created via `project_tasks` skill | When user requests actionable tasks |

## Portability

This skill is stack-neutral. It resolves everything project-specific, the language,
frameworks, database, test and deploy commands, ID prefixes, and the current
lifecycle phase, from `.vmodel.yml` and `docs/project-context.md` (see "Project
Context" above). To adopt it in a new project, run the `vmodel-setup` skill to scaffold the two
context files, fill in the stack and the current phase, and the skill adapts
automatically. It carries no assumption about any specific platform or vendor.
