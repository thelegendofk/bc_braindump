# V-Model Skill Set: Shared Context

This folder holds the project-context contract that makes the V-Model skills
portable and phase-aware. It is the mechanism that replaces the earlier
hardcoded stack assumptions.

## How it works

Every skill reads two files from the target project before doing anything:

1. `.vmodel.yml` at the project root: machine-readable stack, command hooks, conventions, and the current `lifecycle-phase`.
2. `docs/project-context.md`: the human-readable brief.

No skill hardcodes a stack, a platform, or a test or deploy command. All of that
is resolved from these two files. A skill that needs to run tests, scan for
vulnerabilities, or deploy calls the matching command from `hooks:` in
`.vmodel.yml`, never a vendor built-in.

## The three lifecycle phases

The set works across the full lifecycle from inception to operation, grouped
into three coarse phases:

| Phase | Meaning | V-Model emphasis |
|-------|---------|------------------|
| Inception | Frame the problem and design the solution | Left side of the V plus discovery |
| Build | Construct and validate | Bottom plus the ascending right side |
| Run | Operate and maintain | Deployment readiness and operational risk |

Each skill carries a "Phase Adaptation (Inception / Build / Run)" section that
describes how its depth and output shift per phase. The `vmodel-workflow` skill
orchestrates the whole set and activates only the phases relevant to the current
work, reading `lifecycle-phase` to decide.

## Setup for a new project

Use the `vmodel-setup` skill. It asks for the stack, the command hooks and the current
phase, then writes both files from the same two templates that sit in this folder.

By hand, if you prefer:

1. Copy `vmodel.template.yml` to the target project root as `.vmodel.yml`.
2. Copy `project-context.template.md` to `docs/project-context.md`.
3. Fill in the stack, the command hooks, and set `lifecycle-phase`.
4. Run `vmodel-workflow`. It reads the phase and plans the work accordingly.

The same two templates ship inside the `vmodel-setup` skill under `assets/`, so that
skill stays self-contained when it is installed on its own. This folder is the
collection-level copy, kept for backward compatibility with the earlier plugin layout.

## Skills in the set

| Skill | Role |
|-------|------|
| `vmodel-setup` | Scaffolds the two project-context files, run this first |
| `vmodel-workflow` | Phase-aware orchestrator over the whole set |
| `persona-analysis` | Stakeholder personas, needs, gap matrix |
| `requirements-engineering` | User stories, functional and non-functional requirements, traceability |
| `arc42-documentation` | The 12-section arc42 architecture documentation |
| `arc42-design-by-contract` | Behavioural contracts for components (arc42 section 5.4) |
| `arc42-risk-audit` | Architecture and operational risk audit (arc42 section 11) |
| `arc42-docs-viewer` | Browsable web viewer for the arc42 docs |
| `test-strategy` | Test scenarios (UT/FT/AT) with traceability |
| `deployment-readiness` | Pre-release go/no-go checklist |
| `inacta-brand` | Inacta corporate identity reference for any UI or document |
