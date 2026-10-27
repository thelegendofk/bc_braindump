---
name: vmodel-setup
description: Set up the per-project V-Model context that every other V-Model skill reads before it acts. Scaffolds `.vmodel.yml` and `docs/project-context.md` from the bundled templates, after asking for the stack, the command hooks, and the current lifecycle phase (Inception, Build, Run). Use when the user starts using the V-Model skills on a project for the first time, when a V-Model skill reports that the project context is missing, or when the user says "vmodel setup", "set up the V-Model", "initialise the project context", "V-Model aufsetzen". Run this before `vmodel-workflow`. It only writes the two context files, it does not plan or produce documentation.
---

# V-Model Setup

Initialise the per-project context that every V-Model skill reads before it does
anything. This skill replaces the Claude specific `/vmodel-setup` command with a
runtime-neutral workflow. The Claude command still exists as a thin adapter and
delegates here, so both entry points do the same thing.

## What this produces

| File | Location | Nature |
|---|---|---|
| `.vmodel.yml` | project root | machine-readable stack, command hooks, ID prefixes, docs path, `lifecycle-phase` |
| `docs/project-context.md` | project `docs/` | human-readable brief and house rules |

Nothing else. Documentation, requirements and tests are the job of the other skills.

## Workflow

### 1. Check for existing context

Look for `.vmodel.yml` at the project root and `docs/project-context.md`.

- If both exist, tell the user they are set up, show the current `lifecycle-phase` and
  the declared stack, and ask whether they want to update anything. Do not overwrite.
- If only one exists, create the missing one and keep the existing one as the source of
  truth for anything it already declares.
- If neither exists, continue.

### 2. Ask for what the templates need

Ask the user in one compact round. Use whatever structured question mechanism the
runtime offers, otherwise ask in plain chat. Ask only for what materially affects the
files, and accept "unknown" or "none" for any field:

- **Lifecycle phase**: Inception, Build, or Run.
- **Stack**: language, frontend, backend, database, ORM, validation, API style, auth model.
- **Command hooks**: test command, e2e test command, security scan command, build command, deploy command. Leave blank where the project has no such step yet.
- **Project name** and a one line description.

If the user says "use sensible defaults for my stack", infer from files already in the
project (package manifest, lock files, config files, CI definitions) and confirm the
inferred values before writing anything.

### 3. Write the two files

- Fill `assets/vmodel.template.yml` with the answers and write it as `.vmodel.yml` at the
  project root.
- Fill `assets/project-context.template.md` and write it as `docs/project-context.md`.
  Create the `docs/` directory if needed.
- Keep the house rules block as it stands: no em-dashes, Swiss German spelling with
  ss instead of the sharp s, English written for non-native readers.
- Leave a field blank or as "unknown" rather than inventing a value. A wrong command
  hook is worse than an empty one, because later skills will run it.

### 4. Confirm and hand off

- Show the user the two files you created and where they are.
- Say that the set is ready and that `vmodel-workflow` will now plan the work for the
  current lifecycle phase.
- Describe what was set up in plain language. Do not expose internal skill or package
  paths in the summary.

## Relationship to other skills

- **Required predecessor for**: `vmodel-workflow` and every other V-Model skill. They all
  read the two files this skill writes.
- **Recommended successor**: `vmodel-workflow`, which plans the phase-appropriate work.
- **Not related to**: `engagement-setup`, which sets up a consulting engagement folder and
  its `AGENTS.md` operating brief (legacy names `AGENT.md` and `CLAUDE.md` stay valid). The two are independent and can both apply when a
  mandate contains a software project. If both exist, the engagement brief governs client
  facing content and `.vmodel.yml` governs the engineering workflow.

## Portability

- Runs on any Agent Skills compatible runtime. No runtime-specific tool is required.
- A persistent project filesystem is required, because the whole point is two files that
  later sessions read. If the runtime has no persistent files, say so plainly, output the
  two file contents in the chat so the user can save them, and do not pretend they were
  written.
- The templates ship inside this skill under `assets/`, so the skill is self-contained
  when installed on its own. The collection-level `_shared/` folder holds the same two
  templates for backward compatibility with the earlier plugin layout.
