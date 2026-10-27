# Install: interaction-model

A method skill for the interaction model of a software user interface: seven layers from
concepts to motion, with a Build and an Audit mode.

## Contents

```
interaction-model/
  SKILL.md                    the flow and the principles
  references/
    worksheets.md             one template per layer
    sources.md                which work owns which layer
```

## Installation

A standard Agent Skills package, no scripts, no runtime specific manifest.

- **Claude (Cowork or Claude Code)**: import `interaction-model.skill` in the skill
  settings, or put the folder into the skills source directory.
- **Any other runtime**: copy the folder into the skills directory of the runtime.

Install the updated `method-selector`, `solution-architecture-lite`,
`inacta-proposal-writing` and `clear-by-design` together with it, so the chains point to it.
