# Install: method-selector

A thin meta skill that selects and orders the fitting method skills for an engagement. It
does not run the methods, it recommends the chain and writes a
method plan.

## Contents

```
method-selector/
  SKILL.md                    the flow and the principles
  references/
    method-map.md             the mapping table, the only truth
```

## Installation

This is a standard Agent Skills package: a folder with `SKILL.md` in the root, plus one
`references/` folder. This skill carries no scripts and no assets. It contains no runtime
specific manifest and therefore installs the same way on every compatible runtime.

- **Any runtime**: copy the folder `method-selector/` into the directory that the runtime
  searches for skills, leave the folder structure unchanged.
- **Claude (Cowork or Claude Code)**: import the zipped file `method-selector.skill` in the
  skill settings, or put the folder into the skills source directory.
- **ChatGPT / OpenAI**: install the same folder through the skill import of that runtime.
  The exact click path is runtime specific, see the `README.md` of the library.

Triggers:
"welche Methode", "Methodenwahl", "Methodenplan", "wie gehe ich
   das Mandat an", "method selection", "which method", "method plan", "engagement
   triage".

## Where it sits

```
engagement-setup -> method-selector -> the chosen method skills
   -> review -> export
```

## Maintenance, important

The only place with method knowledge is `references/method-map.md`. If a
method skill is newly built, changed or removed, adjust only this table and package the
skill again. That keeps the selector thin and it does not go stale.

## Connection to engagement-setup

`engagement-setup` points at the end to this selector, so that the method plan is created
directly after the setup. This link sits in `engagement-setup`. After a
change to the library, import the affected skill again in the runtime, so that
the change becomes active.

## Source basis

Derived from the method survey (`99 Methods/Methods_Survey.md`) and the
existing method skills. Engagement-generic, carries no fixed client data.
