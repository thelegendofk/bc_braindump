---
description: Set up the V-Model project context. Delegates to the vmodel-setup skill, which scaffolds .vmodel.yml and docs/project-context.md after asking for the stack and the current lifecycle phase.
---

# V-Model Setup

This command is a thin entry point. The method lives in the `vmodel-setup` skill, which
ships with this plugin and is also usable on runtimes that have no slash commands.

Invoke the `vmodel-setup` skill and follow it as written. Do not duplicate or paraphrase
its steps here, and do not copy the template files yourself: the skill resolves its
templates from its own `assets/` folder and handles the existing-context case, the
question round, the writing step, and the hand-off to `vmodel-workflow`.

If the skill is not available in this installation, say so plainly and ask the user to
reinstall the plugin, rather than improvising the setup.
