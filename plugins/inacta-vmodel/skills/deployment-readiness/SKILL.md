---
name: deployment-readiness
description: Deployment Readiness Checklist for the Run phase of the V-Model (Phase 8). Runs a structured pre-deployment validation covering security, risk delta, documentation freshness, integration health, and smoke test coverage, producing a go/no-go recommendation. Use when the user asks to check deployment readiness, validate before deploying, run a pre-deployment checklist, or verify the system is ready for production.
---

# Deployment Readiness Checklist

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

- **Inception**: Define the release criteria and the minimum smoke-test set the project will need. No go/no-go decision yet.
- **Build**: Rehearse the checklist as a pre-merge gate on significant increments.
- **Run**: Full go/no-go before every release, with risk-delta and documentation-freshness checks against the deployment baseline. This is the skill's home phase.

Run a structured pre-deployment validation before publishing the application. This skill covers the Run phase of the lifecycle (V-Model Phase 8, Deployment Readiness), verifying that the system is *ready* to be deployed, not performing the deployment itself (that is the project's deploy command).

## When to Use

- The user asks to deploy, publish, or go live, run this checklist *before* invoking the deploy command
- The user asks "are we ready to deploy?" or "what's blocking deployment?"
- The user requests a pre-deployment review, release readiness check, or go/no-go assessment
- After a major feature merge, before cutting a release

## Relationship to Other Skills

| Skill | Relationship |
|-------|-------------|
| security scanner (project hook) | Category 1 invokes the security scan and interprets its results |
| `arc42-risk-audit` | Category 2 compares current Section 11 risks against the last deployment baseline |
| `arc42-documentation` | Category 3 checks whether arc42 docs reflect the current codebase |
| deploy command (project hook) | This skill produces a go/no-go recommendation; the deploy command performs the actual publish |
| test runner (project hook) | Category 5 defines smoke tests; the test runner can execute them |

**Typical workflow**: Run deployment readiness checklist → Fix blockers → Re-run checklist → Deploy.

---

## Severity Classification

Every finding is classified into one of three severity levels:

| Severity | Symbol | Meaning | Deployment Impact |
|----------|--------|---------|-------------------|
| **Blocker** | 🔴 | Must be fixed before deployment | Deployment is **blocked**, go/no-go = NO-GO |
| **Warning** | 🟡 | Acceptable risk, but should be addressed soon | Deployment **allowed** with documented risk acceptance |
| **Info** | 🟢 | Informational observation, no action required | No deployment impact |

**Rule**: Any single Blocker means the overall recommendation is **NO-GO**. Warnings alone result in **GO with conditions**.

---

## Checklist Execution

Work through all five categories in order. For each category, record findings using the Finding Template (below). After completing all categories, produce the Readiness Report.

### Finding Template

```markdown
#### [CATEGORY-ID]-[NNN]: [Finding Title]

**Severity**: Blocker | Warning | Info
**Category**: Security | Risk Delta | Documentation Freshness | Integration Health | Smoke Test Coverage
**Description**: [What was found]
**Remediation**: [What to do about it, or "None required" for Info items]
```

---

## Category 1: Security

Invoke the project's security scanner and interpret the results.

### Procedure

1. Invoke the security scanner's dependency audit check for known vulnerabilities in dependencies
2. Invoke the security scanner's SAST (static analysis) check for code-level security findings
3. Invoke the security scanner's secrets/sensitive data scan for hardcoded credentials or API keys
4. Interpret the results using the classification below

### Classification

| Scan Result | Severity |
|-------------|----------|
| Critical or High vulnerability in a production dependency | **Blocker** |
| Medium vulnerability in a production dependency | **Warning** |
| Low vulnerability or vulnerability in a dev-only dependency | **Info** |
| Hardcoded secrets or API keys detected in source code | **Blocker** |
| SAST finding with direct security impact (SQL injection, XSS, etc.) | **Blocker** |
| SAST finding with indirect impact (code quality, complexity) | **Warning** |
| No findings in a scan category | **Info**, record as "No issues found" |

### What to Record

For each scan type, record:
- Number of findings by severity
- Specific Blocker-level findings with file paths and descriptions
- Summary of Warning-level findings

---

## Category 2: Risk Delta

Compare the current state of Section 11 risks against the last known deployment baseline. New high-severity risks that appeared since the last deployment are potential blockers.

### Procedure

1. If the `arc42-risk-audit` skill has not been run recently, consider running a targeted audit (at minimum Categories 1 and 6, Access Control and Operational Gaps) to ensure Section 11 is current before comparing against the baseline
2. Read `docs/arc42/11-risks-and-technical-debt.md` to get the current risk inventory
3. Identify the **deployment baseline**, the set of risks that were present at the last deployment. If no baseline exists (first deployment), all existing risks are the baseline and the delta is empty.
4. Classify new or changed risks:

### Classification

| Risk Change | Severity |
|-------------|----------|
| New **High-severity** risk (R-0XX) added since last deployment | **Blocker** |
| Existing High-severity risk with **worsened** description or impact | **Blocker** |
| New **Medium-severity** risk added since last deployment | **Warning** |
| New **Low-severity** risk added since last deployment | **Info** |
| Existing risk with unchanged severity | **Info**, no delta |
| Risk **resolved** (removed or mitigated) since last deployment | **Info**, positive finding |

### What to Record

- Total risk count: current vs. baseline
- New risks added since baseline (list R-0XX IDs and titles)
- Risks resolved since baseline
- Any severity escalations

### Baseline Management

After a successful deployment, save the current risk inventory as the new baseline. Store the baseline as a comment or metadata note at the bottom of Section 11:

```markdown
<!-- Deployment Baseline: YYYY-MM-DD | Risks: R-001 through R-0XX | Debt items: N -->
```

---

## Category 3: Documentation Freshness

Verify that arc42 documentation reflects the current state of the codebase. Stale documentation can cause incorrect operational procedures and miscommunication during incidents.

### Procedure

1. Use the `arc42-documentation` skill's quality checklist (Section Templates and Quality Checklist) as the reference for what each section should contain
2. Check each documentation section against the current codebase:

| Check | How to Verify | Blocker If... | Warning If... |
|-------|---------------|---------------|---------------|
| **Section 05 (Building Blocks)** matches current packages | Compare `the workspace manifest` and `artifacts/` directory against Section 05 package list | N/A | New packages exist that are not documented |
| **Section 07 (Deployment View)** matches current artifacts | Compare registered artifacts and environment variables against Section 07 | Deployment topology has changed (new artifact, removed artifact) and Section 07 is outdated | Environment variables listed in Section 07 differ from actual `.env` or platform config |
| **Section 11 (Risks)** is current | Already checked in Category 2 | N/A | N/A, covered by Category 2 |
| **Section 12 (Glossary)** covers new domain terms | Check for new database tables, entities, or API resources not in the glossary | N/A | New domain entities exist without glossary entries |
| **Database schema** matches Section 05 data model | Compare the current ORM schema files against the data model documented in Section 05 | N/A | New tables or columns exist that are not documented |
| **API routes** match Section 06 scenarios | Check for new route files or major endpoint additions not covered in runtime view | N/A | New major API flows exist without runtime view scenarios |

### What to Record

- List of documentation sections that are current (up-to-date)
- List of documentation sections that need updates, with specific gaps identified
- Whether any gaps affect operational procedures (deployment, monitoring, incident response)

---

## Category 4: Integration Health

Verify that all external dependencies, environment variables, database connectivity, and authentication are properly configured for the target deployment environment.

### Procedure

#### 4.1 Environment Variables

Check that all required environment variables are set and non-empty:

| Variable | Required For | Blocker If Missing |
|----------|-------------|-------------------|
| `DATABASE_URL` | Database connectivity | Yes |
| `PORT` | Service binding | Warning on the hosting platform (auto-assigned); Blocker on other platforms |
| `AUTH_CLIENT_ID` | Authentication (OIDC client ID) | Yes, if auth is enabled |
| `ISSUER_URL` | Authentication (OIDC issuer) | Yes, if auth is enabled |
| `NODE_ENV` | Environment detection | Warning (defaults exist) |

Also check for any application-specific environment variables referenced in the codebase but not documented in Section 07.

#### 4.2 Database Connectivity

- Verify `DATABASE_URL` is set and the connection string format is valid
- Check that the database schema is up to date (no pending migrations or schema pushes)
- Verify that the database is reachable (if possible, attempt a simple query)

| Finding | Severity |
|---------|----------|
| `DATABASE_URL` not set | **Blocker** |
| Database unreachable | **Blocker** |
| Pending schema migrations | **Warning** |
| Schema drift detected (code schema differs from DB) | **Warning** |

#### 4.3 Authentication Configuration

- Verify OIDC configuration is complete (`AUTH_CLIENT_ID`, `ISSUER_URL`)
- Check that session management is configured (session store, secret)
- Verify callback URLs are appropriate for the deployment target

| Finding | Severity |
|---------|----------|
| Auth required but OIDC not configured | **Blocker** |
| Session secret is hardcoded or missing | **Blocker** |
| Unauthenticated mutation endpoints exposed in production (state-changing routes without auth middleware) | **Blocker** |
| Callback URLs reference localhost in production config | **Warning** |

#### 4.4 External API Dependencies

Scan the codebase for external API calls and verify their configuration:

- Third-party API keys or tokens referenced in code
- External service URLs (are they pointing to production endpoints?)
- Webhook configurations

| Finding | Severity |
|---------|----------|
| External API key referenced but not set | **Blocker** |
| External service URL points to staging/dev in production config | **Warning** |
| No external API dependencies | **Info** |

### What to Record

- Environment variable status (set/missing/empty) for each required variable
- Database connectivity status
- Authentication configuration status
- External dependency configuration status

---

## Category 5: Smoke Test Coverage

Define a minimal set of critical-path test scenarios that must pass after deployment. This category does not *execute* the tests, it specifies them. Execution is handled by the project's configured test runner or manual verification.

### Procedure

Generate smoke test scenarios by analyzing the application's critical paths:

1. **Identify entry points**, what does the user do first? (e.g., authentication, landing page)
2. **Identify core workflows**, what are the 3-5 most important user journeys? (e.g., create a contact, create a deal, view reports)
3. **Identify data integrity paths**, operations where data loss or corruption would be catastrophic (e.g., bulk delete, import)
4. **Identify integration touchpoints**, features that depend on external services (e.g., auth callback, API proxy)

### Smoke Test Template

For each critical path, define a scenario:

```markdown
#### ST-NNN: [Scenario Title]

**Critical Path**: [Which user journey this covers]
**Preconditions**: [Setup required, e.g., "User is authenticated", "At least one pipeline exists"]
**Steps**:
1. [Action 1]
2. [Action 2]
3. [Verify expected result]
**Expected Result**: [What success looks like]
**Failure Impact**: [What breaks if this fails, Blocker or Warning]
```

### Minimum Smoke Test Set

Every deployment must have smoke tests covering at minimum:

| Area | What to Test | Failure = |
|------|-------------|-----------|
| **App loads** | The frontend renders without JavaScript errors | Blocker |
| **Authentication** | User can log in and reach the authenticated area | Blocker |
| **Core CRUD** | The primary entity can be created, read, updated, deleted | Blocker |
| **Database** | A read query returns expected data (not empty, not error) | Blocker |
| **API health** | Key API endpoints return 200 (not 500) | Blocker |
| **Navigation** | All main navigation links resolve (no 404s) | Warning |
| **Reports/Dashboard** | Dashboard or report page renders with data | Warning |

### What to Record

- Number of smoke test scenarios defined
- Coverage assessment: are all minimum areas covered?
- Any critical paths that lack test coverage (flagged as Warning)

---

## Readiness Report

After completing all five categories, produce the Readiness Report in this format:

```markdown
# Deployment Readiness Report

**Date**: YYYY-MM-DD
**Application**: [Application name]
**Target Environment**: [Development / Staging / Production]
**Assessed By**: Agent

---

## Recommendation: GO / GO WITH CONDITIONS / NO-GO

[1-2 sentence summary of the recommendation and primary reason]

---

## Summary

| Category | Blockers | Warnings | Info | Status |
|----------|----------|----------|------|--------|
| Security | N | N | N | ✅ / ⚠️ / ❌ |
| Risk Delta | N | N | N | ✅ / ⚠️ / ❌ |
| Documentation Freshness | N | N | N | ✅ / ⚠️ / ❌ |
| Integration Health | N | N | N | ✅ / ⚠️ / ❌ |
| Smoke Test Coverage | N | N | N | ✅ / ⚠️ / ❌ |
| **Total** | **N** | **N** | **N** | |

**Legend**: ✅ = No blockers or warnings, ⚠️ = Warnings only, ❌ = Has blockers

---

## Blockers (Must Fix Before Deployment)

[List each Blocker finding with its category ID, title, and remediation]

| ID | Category | Finding | Remediation |
|----|----------|---------|-------------|
| SEC-001 | Security | [Title] | [What to do] |

*If no blockers: "No blockers identified."*

---

## Warnings (Acceptable Risk: Document and Monitor)

[List each Warning finding]

| ID | Category | Finding | Accepted Risk |
|----|----------|---------|---------------|
| DOC-001 | Documentation | [Title] | [Why this is acceptable for now] |

*If no warnings: "No warnings identified."*

---

## Informational

[Brief summary of Info items, or "No additional observations."]

---

## Smoke Test Specification

[List all smoke test scenarios from Category 5, ready for execution]

---

## Post-Deployment Actions

1. [Any actions to take immediately after deployment, e.g., "Run smoke tests", "Verify auth callback URL"]
2. [Update deployment baseline in Section 11]
3. [Address Warning items within [timeframe]]

---

## Deployment Baseline Update

After successful deployment, update the Section 11 baseline:
<!-- Deployment Baseline: YYYY-MM-DD | Risks: R-001 through R-0XX | Debt items: N -->
```

### Recommendation Logic

| Condition | Recommendation |
|-----------|---------------|
| Zero Blockers, Zero Warnings | **GO** |
| Zero Blockers, One or more Warnings | **GO WITH CONDITIONS**, list the conditions (accepted risks) |
| One or more Blockers | **NO-GO**, list all blockers with remediation steps |

---

## Portability

This skill is stack-neutral. It resolves everything project-specific, the language,
frameworks, database, test and deploy commands, ID prefixes, and the current
lifecycle phase, from `.vmodel.yml` and `docs/project-context.md` (see "Project
Context" above). To adopt it in a new project, run the `vmodel-setup` skill to scaffold the two
context files, fill in the stack and the current phase, and the skill adapts
automatically. It carries no assumption about any specific platform or vendor.

## Execution Guidelines

### Before Every Deployment

1. Run the full five-category checklist
2. Produce the Readiness Report
3. If NO-GO: fix all blockers, then re-run the checklist
4. If GO WITH CONDITIONS: document accepted risks, proceed with deployment
5. If GO: proceed with deployment
6. After deployment: run the smoke tests specified in Category 5
7. After smoke tests pass: update the deployment baseline in Section 11

### For Incremental Deployments

If deploying a small change (bug fix, minor feature):
- Categories 1 and 4 can be run in abbreviated mode (check only changed dependencies and affected environment variables)
- Categories 2, 3, and 5 should still be run fully
- The Readiness Report is still required

### Integrating with the Deploy Command

When the user asks to deploy:

1. **First**, run this deployment readiness checklist
2. **Then**, only if the recommendation is GO or GO WITH CONDITIONS, invoke the project's deploy command to perform the actual deployment
3. **Finally**, execute the smoke tests from Category 5 against the deployed environment

Never skip the readiness checklist to go directly to deployment unless the user explicitly overrides.

### Output Location

The Readiness Report can be:
- Presented to the user in chat (default)
- Written to `docs/deployment-readiness-report.md` if the user wants to persist it
- The deployment baseline should always be updated in `docs/arc42/11-risks-and-technical-debt.md` after a successful deployment
