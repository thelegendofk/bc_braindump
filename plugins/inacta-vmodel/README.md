# Inacta V-Model

A phase-aware V-Model engineering method as a set of Agent Skills. Eleven skills carry a
project from inception to operation, grouped into three coarse lifecycle phases:
Inception, Build, and Run. The set is stack-neutral and runtime-neutral. Every skill
reads a per-project context file instead of assuming a technology stack, and no skill
depends on a particular AI runtime.

## Layout

```
vmodel/
  skills/            the canonical skills, this is the method
  _shared/           collection-level copy of the two context templates
  platform/
    claude/          thin Claude plugin adapter (plugin.json, slash command)
    openai/          notes for ChatGPT and OpenAI runtimes
```

The method lives in `skills/`. Everything under `platform/` is packaging. Neither adapter
is required to use the method, and the skills never read anything from `platform/`.

## How it works

Two files in the target project are the single source of truth:

1. `.vmodel.yml` at the project root: stack, command hooks (test, security scan, build, deploy), ID prefixes, docs path, and the current `lifecycle-phase`.
2. `docs/project-context.md`: the human-readable brief and house rules.

Use the `vmodel-setup` skill to create both from the bundled templates. No skill
hardcodes a stack, a platform, or a test or deploy command. All of it is resolved from
these two files.

## The three lifecycle phases

| Phase | Goal | V-Model emphasis |
|-------|------|------------------|
| Inception | Frame the problem and design the solution | Left side of the V plus discovery |
| Build | Construct and validate | Bottom plus the ascending right side |
| Run | Operate and maintain | Deployment readiness and operational risk |

Each skill has a "Phase Adaptation" section that shifts its depth and output to match
the current phase. `vmodel-workflow` orchestrates the whole set and activates only the
phases relevant to the current work.

## Skills

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
| `inacta-brand` | Inacta corporate identity reference for any user interface or document |

## Installing

- **Any runtime**: install the folders under `skills/` the way that runtime installs
  skills. Each one is self-contained. Individual `.skill` archives are generated into
  `dist/` by the library build script.
- **Claude**: install the generated `inacta-vmodel.plugin` from the library root, which
  is built from this folder plus `platform/claude/`. The `/vmodel-setup` command stays
  available and delegates to the `vmodel-setup` skill.
- **ChatGPT and OpenAI**: install the skill folders directly. See
  `platform/openai/README.md`.

## Templates

The context templates ship inside the `vmodel-setup` skill under `assets/`, so that skill
works when installed alone. `_shared/` holds the same two templates at collection level
for backward compatibility with the earlier plugin layout. The two copies are kept in
sync by the library build script.

## House rules

Deliverables use commas, never em-dashes. German text uses the umlauts and ss instead of
the sharp s. English text is written for non-native readers.
