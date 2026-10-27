# Interaction design in the harness: integration proposal

Status: implemented as draft skills in this repo, not yet imported. Date: 2026-10-27.

## The problem in one paragraph

The harness has a method for requirements (`requirements-engineering`, `persona-analysis`),
for architecture (`arc42-*`, `solution-architecture-lite`), for tests (`test-strategy`) and
for documents (`clear-by-design`). It has no method for the user interface. The V-Model
workflow even lists "Phase 3 skipped: user interface only change" as a normal skip reason.
So when an agent builds a UI, it jumps from user stories straight to layout and widgets.
The reading list below gives us a method for the missing step.

## The core idea: one source owns one layer

The ten works are not ten opinions on the same thing. Each one answers a different question,
and the questions come in a fixed order. We stack them as layers. A lower layer must exist
before work on the next layer starts. This rule is the main thing we add to the harness.

| Layer | Question | Source that owns it | Artifact |
|---|---|---|---|
| L1 Concepts | Which units of function exist, and why? | Jackson, *The Essence of Software* | Concept inventory |
| L2 Object model | Which objects do users handle, with which attributes and actions? | Johnson and Henderson, *Conceptual Models*; Prater, OOUX / ORCA | Object map (ORCA) |
| L3 Grammar | Which action works on which object, and is the grid consistent? | Rosenberg, *UX Magic* (Semantic Interaction Design) | Object-action matrix |
| L4 Posture | How much screen and attention does this app get? | Cooper, application posture | Posture decision, chrome budget |
| L5 Space | Where does each thing live in depth? | Material Design 1, Environment; Apple, Liquid Glass | Layer model (z-map) |
| L6 Interaction | How does the user find and do each action? | Shneiderman, direct manipulation; Norman, *DOET* | Signifier and reversibility table |
| L7 Motion | How does the interface respond while things change? | Apple, *Designing Fluid Interfaces* | Motion rules |

L1 to L3 are the conceptual model. Johnson and Henderson are strict here: no layout and no
widgets in L1 to L3. L4 to L7 are the presentation, and they may only use what L1 to L3
define.

## Three ways to integrate, from light to full

### Option A: reference method only (one hour)

Add a row to "Reference methods without a skill of their own" in
`method-selector/references/method-map.md`:

| Reference method | Fits for | Location |
|---|---|---|
| Interaction model (layer stack) | A mandate that designs or reviews a user interface | 99 Methods/Interaction Design |

Put this README and the source list into `99 Methods/Interaction Design`. Cheap, but agents
will rarely apply it, because nothing forces the layer order.

### Option B: method skill `interaction-model` (recommended)

A lite method skill, built with `method-onboarding`, in the same shape as
`solution-architecture-lite`. Skill: [`skills/interaction-model/SKILL.md`](../../skills/interaction-model/SKILL.md).
Two modes:

- **Build**: produces the L1 to L7 artifacts for a new UI, in order.
- **Audit**: rates an existing UI or prototype against the layers, with one fix per finding.

Home: the general skill library, not the `inacta-vmodel` plugin. Reason: concept and
proposal work runs in engagement folders (Cowork), where `.vmodel.yml` and `docs/` do not
exist. The skill knows three contexts (proposal, concept mandate, code project) and hands
over to the V-Model skills in the third one.

### Option C: B plus harness rules (recommended together with B)

Short, always-on rules for coding agents, so the layer order holds even when nobody calls the
skill. See "Harness rules" below. They go into the project `CLAUDE.md` / `AGENTS.md`
template that `vmodel-setup` writes, not into every engagement.

## Where the skill plugs in

```
persona-analysis ──> posture (L4) and the users per concept
requirements-engineering ──> user stories feed the concept inventory (L1)
        │
        ▼
interaction-model  (L1 to L7, this skill)
        │
        ├──> arc42-documentation: the conceptual model goes into §8 Crosscutting Concepts
        │    (user interface concept). No new arc42 section.
        ├──> arc42-design-by-contract: each L1 concept action is a candidate contract
        │    (preconditions = when the action is allowed, postconditions = new state)
        ├──> test-strategy: each operational principle (L1) becomes one acceptance
        │    scenario, each reversibility rule (L6) one test
        ├──> client-glossary: object and action names in L2 and L3 must be glossary terms
        └──> inacta-brand: colors and type. This skill never chooses brand values.
```

Three links carry most of the value:

1. **Operational principle to test.** Jackson's operational principle is already a scenario
   ("after you reserve a table, the table is held for you until you arrive"). It maps
   one to one onto a `test-strategy` acceptance scenario. This closes the V for UI work.
2. **Object names to glossary.** Prater and Johnson and Henderson both insist that the user's
   words name the objects. `client-glossary` already holds the user's words with a status.
   An L2 object that is not in the glossary is a finding.
3. **Sparse matrix to finding.** Rosenberg treats gaps in the object-action matrix as
   cognitive load: the user learns an action on one object and expects it on the next. Every
   empty cell needs a reason or it becomes a finding. This is mechanical, so a script can
   check it.

## Changes to existing files

| File | Change |
|---|---|
| `inacta-vmodel/skills/vmodel-workflow/SKILL.md` | Phase 1 gets an optional step "interaction-model, if the change touches the UI". Remove "user interface only change" as a valid skip reason for Phase 3 and 4, replace with "UI change: run interaction-model Audit instead". |
| `inacta-vmodel/skills/arc42-documentation/SKILL.md` | §8: name the conceptual model (concept inventory, object map, matrix) as the content of the user interface concept. |
| `inacta-vmodel/skills/test-strategy/SKILL.md` | Add operational principles as a test source, next to DbC contracts and user stories. |
| `method-selector/references/method-map.md` | Inventory row for `interaction-model`; in the proposal chain add "interaction-model (only if the offer designs a UI)" after `solution-architecture-lite`. |
| `clear-by-design` | No change. It covers documents. Add one boundary line: "for software interfaces use interaction-model". |
| `vmodel-setup` (CLAUDE.md template) | Add the harness rules below. |

## Harness rules (for the project CLAUDE.md / AGENTS.md)

Short enough to be read every session:

```markdown
## User interface work
- No layout and no widgets before the object-action matrix exists for the objects you touch
  (docs/ui/object-action-matrix.md). If it is missing, run interaction-model first.
- Every UI object and action uses the term from the client glossary. New term, ask first.
- Every empty cell in the object-action matrix has a written reason.
- Every destructive or hard to reverse action is undoable. A confirmation dialog only where
  undo is impossible.
- Every action has a visible signifier. Hidden gestures only as a shortcut for a visible path.
- Controls and navigation live in the functional layer above the content. Content never
  floats above controls.
- Animations start from the user's input, can be interrupted and can be redirected. No
  animation blocks input.
- Respect the posture in docs/ui/posture.md: a transient tool gets minimal chrome.
```

## Our own way of working

Two habits change for us, not only for agents:

- **Artifacts we publish are UI too.** Most of our HTML artifacts and dashboards are
  transient in Cooper's sense: opened, read, closed. That sets a low chrome budget.
  A dashboard someone keeps open all day is sovereign and may carry more.
- **Review order.** In UI reviews we discuss the layers top down. A comment on a button
  color waits while the matrix still has unexplained gaps. This keeps reviews short.

## Cowork

Cowork loads the skills and plugins enabled on the claude.ai account. Once the updated
skills are imported there, they run in Cowork for concepts and proposals:

- `method-selector` proposes `interaction-model` in the proposal chain and in the new
  "Concept / UI concept" chain.
- The skill reads the engagement `AGENTS.md`, writes its sheets to `reference/` and, in a
  concept mandate, the UI concept to `deliverables/`.
- The harness rules in the V-Model template only reach code projects. In Cowork the same
  rules travel inside the skill (operating principles), so nothing depends on a CLAUDE.md.

## Open decisions

1. Decided: B plus C.
2. Decided: general skill library.
3. Do we keep L7 (motion) in the skill, or leave it as a reference? It matters for apps,
   less for internal tools and dashboards.
4. Do we build the matrix check script now, or after the first real use?
