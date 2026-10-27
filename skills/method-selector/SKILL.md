---
name: method-selector
description: >
  Selects the fitting method skills for a set-up engagement and puts them in the
  right order, instead of running them itself. Reads the context of the engagement
  (work type, goal, deliverable), recommends the chain of method skills, names the
  matching reference methods that have no skill of their own, and writes a method
  plan into the `## Methodenplan` section of the PLAN.md. It points to the skills, it does not repeat their content.
  The only truth is a compact mapping table. Triggers: "welche
  Methode", "Methodenwahl", "Methodenplan", "wie gehe ich das Mandat an", "method
  selection", "which method", "method plan", "engagement triage", "how should I
  approach this engagement", "Methoden auswählen", "Vorgehen wählen". Runs after
  engagement-setup and before the method skills. Does not create folders and does not
  run reviews.
---

# Method Selector

## Purpose

Choose and order the right methods for an engagement. This skill is a decision
helper, not an executor. It says which method skills make sense in which order,
which reference methods without a skill of their own fit alongside, and what is
deliberately left out. After that it hands over to the chosen skills.

It does not replace the automatic skill selection through the descriptions. Its
added value lies in what no single skill owns: the chain and the order, mixed or
unclear engagements, and the visibility of the reference methods.

## Golden rule: point, do not repeat

This skill never describes how a method works. That stands in the respective
SKILL.md. The only truth here is the mapping table in
`references/method-map.md`, engagement type to methods and order. If a skill
changes, only this table changes. That keeps the selector thin and it does not go stale.

## Where this sits in the lifecycle

```
engagement-setup   (folder plus AGENTS.md, work type set)
  -> method-selector   (this skill: method plan)
  -> the chosen method skills, in the recommended order
  -> review (tech-executive-review, red-team-review)
  -> publication boundary (publication-boundary-review, release gate)
  -> send check (client-glossary check, then send-prep)
  -> export (engagement-package-export, project-knowledge-bundle)

across all of this, at client level:
  client-glossary   (create the vocabulary, maintain it, check documents against it)
```

If no engagement folder with an AGENTS.md exists yet, first point to `engagement-setup`.
No skeleton is created here.

## Step 0: Read the context

First read the AGENTS.md of the engagement: work type, goal, deliverables, language,
guardrails. If that is not enough, ask the user briefly. Invent nothing. If the
AGENTS.md is missing, point to `engagement-setup` and stop.

## Step 1: Classify the engagement

Assign the engagement to one or more types (see `references/method-map.md`):
proposal, EA and architecture, audit and assessment, project setup, research, or
internal project. Many engagements are mixed, for example a proposal with an
architecture part. Multiple assignments are allowed.

## Step 2: Propose the chain

Derive the method skills and their order from the table. Almost every
client-facing deliverable ends with the review skills and an export. The
production skills (docx, pptx, drawio, human-writing) hang on the creation of the
deliverable, not on the method.

## Step 3: Resolve overlaps

Where two methods come into question, choose with the short decision aid in
`references/method-map.md`. Rules of thumb: `inacta-ea-method` designs a
target picture, `ict-audit` checks an existing solution. `shipley-proposal` does the
strategy and compliance, `inacta-proposal-writing` does the text and the structure.
Do not propose anything twice.

## Step 4: Name the reference methods

If a method without a skill of its own fits, name it, do not hide it. For example
Wardley Mapping for a build versus buy or positioning question, Design
Thinking for a real discovery or co-creation phase, Consultative or
Challenger Sales for business development. These run as a light addition, not
as a mandatory step.

## Step 5: Write the method plan

Write the result into the `## Methodenplan` section of the `PLAN.md` of the engagement, or
if no `PLAN.md` is present to `reference/Method_Plan.md`. That section is owned by this
skill, it is replaced on a re-run, and nothing else in `PLAN.md` is touched. The plan names:

- the chosen method skills in order,
- one sentence per skill, why,
- the review and export steps,
- the recommended reference methods,
- what is deliberately left out and why.

Keep it short. The plan is a recommendation, the user decides.

## Working principles

- Point, do not repeat. One table is the truth, no second place for
  method content.
- Recommend, do not force. The user can overrule every choice.
- Do not push a method. If none fits, say so.
- Order and combination are the added value, not a copy of the
  skill triggers.
- Invent nothing. If the work type is missing, ask instead of guessing.
- Maintain the table. A new or changed skill means, adjust only the table.
- No em-dashes, use a comma instead. The deliverable language follows the
  engagement. German texts use the umlauts ä, ö, ü and ss instead of ß. English
  texts are written for non-native readers.

## Parameterisation per engagement

Fixed: the mapping table, the principles. Per engagement read: the AGENTS.md, the
work type, the language of the deliverable. The defaults follow Swiss standard
German and the Inacta conventions.

## Portability

- Runs on any Agent Skills compatible runtime. No runtime specific tool is needed. Where this
  skill says to ask the user, use the structured question mechanism of the runtime, otherwise
  ask in the chat. Where it says to hand over a file, use the file output of the runtime.
- Operating brief of the engagement: look for `AGENTS.md`, otherwise `AGENT.md`, otherwise
  `CLAUDE.md` (legacy, still valid). Use the first file found. Never rename or overwrite an
  existing file silently. If it is missing entirely, first `engagement-setup`.
- A persistent project folder is expected. If it is missing, work with the files of the running
  session, keep the same structure in the result and say openly that nothing was persisted. Do
  not pretend that persistent files exist.
