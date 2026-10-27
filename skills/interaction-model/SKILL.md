---
name: interaction-model
description: >
  Designs and audits the interaction model of a software user interface as seven layers:
  concepts, object model, object-action matrix, posture, spatial layers, interaction,
  motion. Build mode produces the layer artifacts in order, Audit mode rates an existing UI
  or screenshots against them. Works in a proposal (internal artifacts), a concept mandate
  (the UI concept is the deliverable) and a code project. Keeps Jackson, ORCA, Rosenberg,
  Cooper, Norman, Shneiderman and Apple's fluid motion, skips OOUX workshops and visual
  design. Triggers: "interaction model", "conceptual model", "object-action matrix",
  "OOUX", "UI concept", "screen design", "Interaktionsmodell", "Bedienkonzept",
  "UI-Konzept", "Objektmodell", "Oberfläche entwerfen", "UI prüfen". Engagement-generic,
  scaffolds no folders, runs no reviews. Boundary: system cut solution-architecture-lite,
  prose inacta-proposal-writing, documents clear-by-design, brand inacta-brand.
---

# Interaction model

## Purpose

Own the step between user needs and screens. The skill makes sure that an interface is
built from a clear conceptual model, and that the presentation only shows what the model
defines. It does not own requirements (`requirements-engineering`), personas
(`persona-analysis`), the system cut (`solution-architecture-lite`), brand and visual
style (`inacta-brand`, `inacta-proposal-deck`), client prose (`inacta-proposal-writing`),
documents and decks (`clear-by-design`), architecture documentation
(`arc42-documentation`) or tests (`test-strategy`).

Stance: an interaction designer who refuses to draw a screen before the objects are named.

## Where this sits

Three contexts. Find out which one applies in Step 0.

**Proposal that designs a UI.** The artifacts stay internal in `reference/`.

```
engagement-setup -> method-selector -> shipley-proposal (RFP only)
  -> solution-architecture-lite (if the offer designs a system)
  -> interaction-model (this skill, Build, usually L1 to L4)
  -> inacta-proposal-writing (writes the UI part of the solution section from it)
  -> review chain
```

**Concept mandate (UI concept, Bedienkonzept, Fachkonzept with an interface).** The
concept is the deliverable.

```
engagement-setup -> method-selector
  -> persona-analysis and requirements-engineering, as far as the mandate needs them
  -> interaction-model (this skill, Build, L1 to L6, L7 if the product is an app)
  -> docx or inacta-proposal-deck, plus drawio-diagrams-enhanced, clear-by-design,
     human-writing
  -> review chain
```

**Code project (V-Model).** After Phase 1, before Phase 2. Artifacts in `docs/ui/`. The
conceptual model goes into arc42 §8, the operational principles into `test-strategy`.
Audit mode runs again on the built UI.

If the engagement folder does not exist yet, point the user to `engagement-setup`. Do not
scaffold here.

## The layer rule

Work top down. A layer may only use what the layers above define. Never start L4 to L7
while L1 to L3 have open questions. Each layer has one source that owns it, see
`references/sources.md`. Templates are in `references/worksheets.md`.

| Layer | Question | Artifact |
|---|---|---|
| L1 Concepts | Which units of function exist, and why? | Concept inventory |
| L2 Object model | Which objects do users handle? | ORCA object map |
| L3 Grammar | Which action works on which object? | Object-action matrix |
| L4 Posture | How much screen and attention does it get? | Posture decision |
| L5 Space | Where does each thing live in depth? | Layer model (z-map) |
| L6 Interaction | How does the user find and do each action? | Signifier and reversibility table |
| L7 Motion | How does it respond while things change? | Motion rules |

Depth per context: a proposal usually needs L1 to L4, enough to show that we understood the
users' objects. A concept mandate needs L1 to L6. L7 only for apps with real transitions.

## What this skill keeps and skips

Keeps: concepts with one purpose and an operational principle (Jackson); objects,
relationships, calls to action, attributes (Prater, Johnson and Henderson); the
object-action matrix with sparse cells as findings (Rosenberg); sovereign, transient and
daemonic posture (Cooper); content layer and functional layer (Material 1, Liquid Glass);
signifiers, direct manipulation, reversible actions (Norman, Shneiderman); responsive,
interruptible, redirectable motion (Apple).

Skips on purpose: the full OOUX workshop format (too heavy, the worksheet covers the
result); Jackson's synchronization formalism (DbC covers behavior); Material elevation
values and shadows (brand); Liquid Glass materials (platform specific); component libraries
and widget choice (implementation); wireframes and mockups (production, after this skill).

## Step 0: Context intake (always first)

Read with a sub-agent if the runtime offers one, otherwise in a separate focused pass:

- Operating brief: `AGENTS.md`, otherwise `AGENT.md`, otherwise `CLAUDE.md`. Read only.
  It tells the context (proposal, concept, code project), the language and the guardrails.
- In a code project: `docs/project-context.md` and `.vmodel.yml` if present.
- Inputs: the RFP or brief in `brief/`, user stories, personas, process descriptions,
  screenshots of the current system.
- The client glossary (`client-glossary`). Object and action names come from it.
- Artifacts of `solution-architecture-lite` in `reference/`, if present. Concepts must not
  cut across its building blocks without a reason.
- In Audit mode: the UI itself, as screenshots or a running prototype. Look at it, do not
  only read the text or the code.

If a source is missing, ask. Never invent users, objects or actions.

## Folder mapping

| Artifact | Engagement folder | Code project |
|---|---|---|
| L1 to L7 worksheets | `reference/` (internal) | `docs/ui/` |
| UI concept for the client (concept mandate only) | `deliverables/` | not applicable |
| New terms | `client-glossary`, status Working | glossary of the project |

Naming in engagements: `<Client>_<Engagement>_InteractionModel_<YYYY-MM-DD>.md`.

## Build mode

1. **L1 Concepts.** From the user needs, list the concepts. Each has a name, one purpose,
   its state, its actions and an operational principle. Two purposes in one concept is a
   split. One purpose in two concepts is a merge.
2. **L2 Object map.** Per concept, the objects the user sees and handles. Per object:
   attributes, relationships, calls to action. Names from the glossary. No layout, no
   widgets.
3. **L3 Matrix.** Objects as rows, actions as columns. Each cell: `yes`, `no: <reason>` or
   `open`. A cell without a value is a finding. Prefer generic actions (open, create, edit,
   share, delete, undo) that behave the same on every object.
4. **L4 Posture.** One decision per surface: sovereign, transient or daemonic. Derive it
   from the personas (how long, how often). It sets the chrome budget.
5. **L5 Layers.** Every element gets one z position. Content at the bottom, the functional
   layer (controls, navigation) above it, transient surfaces (sheets, dialogs, toasts) on
   top. Nothing changes layer without a reason.
6. **L6 Interaction.** Per allowed matrix cell: the signifier, direct manipulation or
   command, and the undo path.
7. **L7 Motion.** Only for the transitions that matter. Each follows the input, can be
   interrupted and can be redirected.
8. **Handover.** By context:
   - Proposal: hand the L1 to L4 sheets to `inacta-proposal-writing`. The client reads the
     users' objects and the operational principles in plain words, never the matrix.
   - Concept mandate: build the deliverable with `docx` or `inacta-proposal-deck`. The
     object map and the layer model as diagrams (`drawio-diagrams-enhanced`), the matrix as
     an annex table, one operational principle per concept in the main text. Then
     `clear-by-design` and the review chain.
   - Code project: L1 to L3 into arc42 §8 (`arc42-documentation`), operational principles
     and undo rules into `test-strategy`, concept actions into `arc42-design-by-contract`.

## Audit mode

Rate an existing UI against L1 to L7, top down. Per layer a score from 1 to 5 and the
findings with location (screen, element) and one concrete fix. Report the three to five
most effective fixes first. Typical findings:

- A screen shows something that has no object in L2 (orphan element).
- The same action has different names or gestures on different objects (grammar break).
- An action exists on one object and is missing on a similar one without reason.
- A destructive action has a confirmation but no undo.
- An action has no visible signifier.
- Controls scroll away with the content, or content covers controls.
- An animation blocks input or cannot be stopped.

Audit mode also serves a proposal: rate the client's current system from screenshots and
use the top findings as the complication in the narrative. Hand that to
`inacta-proposal-writing`, do not write the prose here. Audit does not rate brand, color or
copy.

## Operating principles

- No layout before the matrix. If someone asks for a screen first, sketch the matrix first
  and say why.
- The user's words name the objects. A new term goes to `client-glossary` as Working.
- Every gap is a decision. Write the reason or open the question.
- Undo beats confirm.
- Controls live in the functional layer above the content.
- Every action has a visible signifier. Hidden gestures only as a shortcut.
- Motion starts from the input, can be interrupted and can be redirected.
- Never invent facts. Anything not in an input is an open question.
- Internal only stays internal. The matrix and the worksheets never go to the client in a
  proposal.

## Style rules for the outputs

The deliverable language follows the operating brief. No em-dashes, use a comma instead.
German uses the umlauts ä, ö, ü, Ä, Ö, Ü, never ae, oe, ue, and ss instead of ß (Swiss
standard German). English is written for non-native readers, short sentences, no idioms.

## Portability

- Runs on any Agent Skills runtime, Cowork and Claude Code included. No runtime specific
  tool is needed. Where this skill says ask, use the structured question mechanism of the
  runtime, otherwise ask in the chat.
- A persistent project folder is expected. If it is missing, work with the files of the
  session, keep the same structure and say openly that nothing was persisted.

## Parameterization

Fixed: the layer order, the artifacts, the principles. Per mandate: the context, the depth
(which layers), the storage location, the platform conventions (web, iOS, Android) and the
language.
