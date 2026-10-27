---
name: interaction-model
description: >
  Designs and audits the interaction model of a software user interface as a fixed stack of
  layers: concepts, object model, object-action grammar, posture, spatial layers,
  interaction and motion. Build mode produces the layer artifacts in order, Audit mode rates
  an existing UI or prototype against them. Deliberately not by the book: keeps Jackson's
  concepts and operational principle, the ORCA object map, Rosenberg's object-action matrix,
  Cooper's posture, a z-layer model, signifiers and reversibility, and three motion rules;
  skips full OOUX workshops, visual design and component libraries (owned elsewhere).
  Triggers: "interaction model", "conceptual model", "object model", "object-action matrix",
  "OOUX", "ORCA", "UI concept", "screen design", "information architecture",
  "Interaktionsmodell", "Bedienkonzept", "UI-Konzept", "Objektmodell", "Oberfläche
  entwerfen", "UI prüfen". Engagement-generic: reads AGENTS.md / CLAUDE.md and the glossary,
  does not scaffold folders, does not choose brand values, does not run reviews.
---

# Interaction model

## Purpose

Own the step between user stories and screens. The skill makes sure that the interface is
built from a clear conceptual model, and that the presentation only shows what the model
defines. It does not own requirements (`requirements-engineering`), personas
(`persona-analysis`), brand and visual style (`inacta-brand`, `inacta-proposal-deck`),
architecture documentation (`arc42-documentation`) or tests (`test-strategy`).

Stance: an interaction designer who refuses to draw a screen before the objects are named.

## Where this sits in the lifecycle

```
persona-analysis, requirements-engineering
  -> interaction-model (this skill)
  -> arc42-documentation (§8 user interface concept), arc42-design-by-contract
  -> test-strategy (operational principles as acceptance scenarios)
  -> implementation, then interaction-model Audit on the running UI
```

In a proposal: after `solution-architecture-lite`, only if the offer designs a UI. The
artifacts stay internal, `inacta-proposal-writing` turns them into client prose.

## The layer rule

Work top down. A layer may only use what the layers above define. Never start L4 to L7
while L1 to L3 have open questions. Each layer has one source that owns it, see
`references/sources.md`.

| Layer | Artifact | Template |
|---|---|---|
| L1 Concepts | Concept inventory | `references/worksheets.md#l1` |
| L2 Object model | ORCA object map | `references/worksheets.md#l2` |
| L3 Grammar | Object-action matrix | `references/worksheets.md#l3` |
| L4 Posture | Posture decision | `references/worksheets.md#l4` |
| L5 Space | Layer model (z-map) | `references/worksheets.md#l5` |
| L6 Interaction | Signifier and reversibility table | `references/worksheets.md#l6` |
| L7 Motion | Motion rules | `references/worksheets.md#l7` |

## What this skill keeps and skips

Keeps: concept with one purpose and an operational principle (Jackson); objects,
relationships, calls to action, attributes (Prater, Johnson and Henderson); the
object-action matrix with sparse cells as findings (Rosenberg); sovereign versus transient
(Cooper); content layer and functional layer (Material 1, Liquid Glass); signifiers,
direct manipulation, reversible actions (Norman, Shneiderman); responsive, interruptible,
redirectable motion (Apple).

Skips on purpose: full OOUX workshop format (too heavy for most mandates, the worksheet
covers the result); Jackson's concept synchronization formalism (DbC covers the behavior);
Material's elevation values and shadows (visual style, owned by the brand); Liquid Glass
materials (platform specific); component libraries and widget choice (implementation).

## Step 0: Context intake (always first)

- Operating brief: `AGENTS.md`, otherwise `AGENT.md`, otherwise `CLAUDE.md`. Read only.
- `docs/project-context.md` and `.vmodel.yml` if present.
- User stories and personas from the V-Model docs.
- The client glossary (`client-glossary`). Object and action names come from it.
- In Audit mode: the running UI or screenshots. Look at it, do not only read the code.

If a source is missing, ask. Never invent users, objects or actions.

## Build mode

1. **L1 Concepts.** From the user stories, list the concepts. Each has a name, one purpose,
   its state, its actions and an operational principle. Two purposes in one concept is a
   split. One purpose in two concepts is a merge.
2. **L2 Object map.** For each concept, the objects the user sees and handles. Per object:
   attributes, relationships to other objects, calls to action. Names from the glossary. No
   layout, no widgets.
3. **L3 Matrix.** Objects as rows, actions as columns. Fill each cell: allowed, not allowed
   with reason, or open. An empty cell without reason is a finding. Prefer generic actions
   (open, edit, share, delete, undo) that work the same on every object.
4. **L4 Posture.** One decision for the app or for each surface: sovereign, transient or
   daemonic. Derive it from the personas (how long, how often). It sets the chrome budget.
5. **L5 Layers.** Assign every element one z position. Content layer at the bottom, the
   functional layer (controls, navigation) above it, transient surfaces (sheets, dialogs,
   toasts) on top. Nothing changes layer without a reason.
6. **L6 Interaction.** For each allowed matrix cell: how the user discovers it (signifier),
   whether it is direct manipulation or a command, and how it is undone.
7. **L7 Motion.** Only for the transitions that matter. Each follows the input, can be
   interrupted and can be redirected.
8. **Handover.** Conceptual model (L1 to L3) to `arc42-documentation` §8. Operational
   principles and reversibility rules to `test-strategy`. Concept actions to
   `arc42-design-by-contract`.

Store the artifacts in `docs/ui/` in a code project, or in `reference/` in an engagement
folder. They are internal.

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

Audit does not rate brand, color or copy. Hand those to `inacta-brand` and `human-writing`.

## Operating principles

- No layout before the matrix. If someone asks for a screen first, sketch the matrix first
  and say why.
- The user's words name the objects. A new term goes to `client-glossary` as "Working".
- Every gap is a decision. Write the reason or open the question.
- Undo beats confirm.
- Internal only stays internal.
- No em-dashes, use commas. German uses Swiss spelling and real umlauts. English is written
  for non-native readers.

## Parameterization

Fixed: the layer order, the artifacts, the principles. Per project: the storage location,
whether L7 applies (often not for internal tools), the platform conventions (web, iOS,
Android), and the language of the artifacts (from the operating brief).
