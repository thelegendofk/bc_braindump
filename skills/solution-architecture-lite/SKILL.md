---
name: solution-architecture-lite
description: >-
  Solution architecture at building level, for a proposal or concept that actually designs a
  distributed software system. Groups the requirements, cuts the system into building blocks
  with a named criterion, tests the cut, and produces the internal artifacts the proposal
  skills turn into the client-facing solution section, a functional decomposition, a scope
  sheet, a blueprint, a capacity sheet and a trade-off memo. Triggers: "solution architecture",
  "Lösungsarchitektur", "Systemarchitektur", "Systemschnitt", "funktionale Zerlegung",
  "functional decomposition", "Anforderungen gruppieren", "Bausteine", "building blocks",
  "separation of concerns", "information hiding", "Mengengerüst", "sizing",
  "Architekturskizze", "wie schneiden wir das System", "wie skaliert das".
  Engagement-generic: scaffolds no folders, runs no reviews. Boundary: designs one building.
  City plan inacta-ea-method, prose inacta-proposal-writing, delivery docs the arc42 skills.
  Refuses EA-only, process-only and pure discovery mandates.
---

# Solution Architecture (lite)

## Purpose

Design the system before writing about it. This skill owns the middle layer between the
enterprise architecture and the delivery documentation: the building-level design that has
to appear in an offer, with named components, main flows, stated scale assumptions and the
two or three trade-offs that decide the deal.

It produces four internal artifacts and nothing client-facing. It does not scaffold folders,
does not draw the final diagrams, does not write the offer text and does not review.

Stance: a solution architect who has to defend the design in front of a CIO and a
procurement lead, not in front of an interviewer. The questions that get asked are: what do
we already have, buy or build, year-one cost, where the data lives, who runs it at 02:00,
and what happens if this is wrong. Consistent hashing is not one of them.

## The gate: when this skill runs, and when it refuses

Run only when the mandate designs a software system that has components, flows and load.

**Refuse and say so plainly when:**

- the mandate is EA only, a capability map, a target picture, a roadmap. That is
  `inacta-ea-method`.
- the mandate is process only, an operating model, a governance design, a target
  organisation.
- the mandate is a package implementation with no design freedom, for example a standard
  product rollout with configuration only. Name the integration points instead and stop.
- the mandate is pure discovery, a study or an assessment with no system to design.
  Assessment of an existing solution is `ict-audit`.
- the system is a small internal tool. Two boxes and one sentence is the honest answer.
  Do not draw a twenty-box reference architecture for it.

A refusal is a result. State which skill owns the work and stop, do not produce a design
sketch nobody asked for.

## Where this sits in the lifecycle

Two entry points, one skill.

**Proposal or pitch chain**, after the win layer and before the prose:

```
engagement-setup -> method-selector
  -> shipley-proposal        (win strategy, compliance matrix, storyboard)
  -> solution-architecture-lite   (this skill: scope, blueprint, capacity, trade-offs)
  -> inacta-proposal-writing (the client-facing solution approach section)
  -> docx or inacta-proposal-deck, plus drawio-diagrams-enhanced and human-writing
  -> the review chain in LOOP.md section 3
```

**Architecture or target-picture chain**, beside the EA work, only for the systems the
mandate actually designs:

```
engagement-setup -> method-selector
  -> inacta-ea-method        (city plan: SCN, CBM, gap, transition, governance)
  -> solution-architecture-lite   (this skill, per system the mandate designs)
  -> docx or deck, plus drawio-diagrams-enhanced and human-writing
  -> the review chain in LOOP.md section 3
```

If the engagement folder does not exist yet, point the user to `engagement-setup` and stop.
Do not scaffold here.

## What this skill keeps and skips

Keeps: the four-step design spine rewritten for a sponsor, the back-of-the-envelope
worksheet, the scaling ladder as shared language for the growth path, and a short internal
pattern index.

Skips on purpose:

- Win themes, discriminators, compliance matrix, storyboard: `shipley-proposal`.
- Narrative, action titles, business case, pricing, the section the client reads:
  `inacta-proposal-writing`.
- Capability model, gap analysis, transition roadmap, architecture governance:
  `inacta-ea-method`.
- Assessment of an existing solution: `ict-audit`.
- Delivery-phase architecture documentation, arc42 sections, design by contract, test
  derivation: the V-Model skills. This skill stops at the offer.
- Diagram production: `drawio-diagrams-enhanced`, PNG before embedding.
- Reviews, publication boundary, send check, export: the chain in `LOOP.md` section 3.
- Effort and price: the calculation instruments in `99 Methods/Kalkulation & Offerten/`,
  and the AI cost model in `inacta-proposal-writing` step 4b.
- Interview ceremony: no timeboxed pacing, no whiteboard performance, no design written to
  impress a reviewer.

The most common failure here is drawing a reference architecture instead of designing this
client's system. If the section could be pasted into another client's proposal after a
find-and-replace, it failed.

## Step 0: Context intake (always first)

Read without flooding the main context, using a sub-agent for multi-file work if the runtime
offers one, otherwise a separate focused reading pass:

- **AGENTS.md** of the engagement, then `AGENT.md`, then `CLAUDE.md` (legacy, still valid).
  First found wins. Settings, guardrails, avoid list. Do not change them.
- **GOAL.md** if present. The `Stop if` conditions apply to this skill too.
- **GLOSSARY.md** at client level if present. System names and spellings come from there, a
  term with status Heard is not used unchecked.
- **Style guide** if present, for example `reference/Stilrichtlinie*.md`.
- **The brief**: RFP, requirement catalogue, client input in `brief/`. Read only.
- **Shipley outputs** in `reference/` if this follows Shipley: win themes, discriminators,
  compliance matrix. The design has to carry the win themes, not contradict them.
- **EA outputs** in `reference/` if this follows the EA method: the capabilities this system
  serves, the standards it has to respect.

If a needed input is missing, ask. Never invent a user count, a volume, an SLA, a budget or
a deadline.

### Preflight: this skill's own files

The method of this skill lives in `references/`, not in the prose above. Before Step 1,
confirm that every one of them is readable: `design-scope-sheet.md`,
`functional-decomposition.md`, `blueprint-guide.md`, `principle-tests.md`,
`capacity-worksheet.md`, `tradeoff-memo.md`, `scaling-ladder.md`, `pattern-index.md`.

If one of them cannot be read, name the missing file and stop. Do not reconstruct a worksheet
from this SKILL.md, and do not carry on with the steps that depend on it. The likely cause is
a partial install, where the skill was registered from its SKILL.md alone, and the fix is to
import the skill archive again. Say so, because a skill registered without its references
carries a correct description, triggers normally, and then fails quietly.

## Folder mapping

| Artifact | Folder | Nature |
|---|---|---|
| RFP, requirement catalogue, client input | `brief/` | read only |
| Design scope sheet | `reference/` | internal only |
| Functional decomposition | `reference/` | internal only |
| High-level blueprint | `reference/` | internal only |
| Capacity sheet | `reference/` | internal only |
| Trade-off and deep-dive memo | `reference/` | internal only |
| The solution section of the offer | `deliverables/` | written by `inacta-proposal-writing` |

Naming: `<Client>_<Engagement>_<Type>_<YYYY-MM-DD>.<ext>`, in line with the house
convention.

All four artifacts are internal. Nothing moves from `reference/` to `deliverables/` without
a deliberate promotion step, and the pattern index never moves at all, see the publication
boundary section below.

## Step 1: Scope and constraints

Establish what is being designed before designing it. Use
`references/design-scope-sheet.md`.

Five blocks, each of them sourced or marked TBC:

1. **Functional scope**: the three to seven things the system must do. Not a requirement
   dump, the load-bearing functions.
2. **Non-functional requirements**: availability, latency, throughput, retention,
   recoverability, security and audit needs. Take them from the RFP where they are stated.
   Where the RFP is silent, record an open question and mark it TBC.
3. **Scale assumptions**: users, transactions, documents, growth over the contract term.
   Every figure carries a source or the marker TBC.
4. **Existing estate**: what already runs at the client, what they are contractually or
   politically bound to, which standards the EA sets, who operates it today. This is the
   block that keeps the design from becoming generic.
5. **Explicit out of scope**: what this design does not cover, and what is deliberately not
   decided yet.

A scope sheet where block 4 is empty is not finished. Every client we work for has an
estate.

Close the step by naming the **two or three qualities that will shape the cut**. Not the
whole list from block 2. The ones where the required level is high enough that it changes
where a boundary goes: a recovery objective that forces a failure domain, a retention or
residency rule that forces a separate store, an audit duty that forces an append-only path,
a latency path that cannot cross an integration. Write them down. Step 2 uses them as a
cutting criterion and Step 4 tests against them. A quality nobody can point at in the brief
is TBC, not a design driver.

## Step 2: From requirements to building blocks

Group, cut, draw, test, in that order. Use `references/functional-decomposition.md`,
`references/blueprint-guide.md` and `references/principle-tests.md`.

### 2a. Group the requirements

Before deciding what the system is made of, decide how the scope is organised. Use
`references/functional-decomposition.md`. The artifact is an `.xlsx` in `reference/`.

Two cases, and the first job is to say which one applies:

- **The requirement list already carries a usable structure.** Chapters, functional areas,
  modules, a process model. Adopt it, in the client's own names and order, and note only
  where we deviate and why. The evaluator wrote that structure and often scored against it,
  so a silent deviation reads as carelessness.
- **No usable structure exists.** The requirements arrive flat, as prose, or spread across
  annexes. Then we group them and show every requirement landing in the grouping. Here the
  artifact earns its place, because the grouping is the evidence that we read the scope. A
  bidder who hands the flat list back has demonstrated nothing.

Name the grouping criterion, in this order of preference: a business process or lifecycle
stage the client already names, a business object, the actor served, or a regulatory regime
that governs a set of requirements together.

**Never group by technical layer.** Front end, back end, database is a component cut wearing
a functional label. It describes how we build software rather than how their business works.

Where `shipley-proposal` has built a compliance matrix, add one `Functional area` column to
it rather than rebuilding the requirement list. Two workbooks listing the same requirements
is the maintenance failure the matrix exists to prevent.

Run the coverage check before moving on: which requirements have no area, which sit in more
than one, which areas hold nothing. An unmapped Must is the serious one, because it means the
grouping does not cover the scope we are claiming to have understood.

### 2b. The cut

Decide what makes something a box before drawing any. A list of components that nobody can
give a criterion for is a function tree, and a function tree is not an architecture.
Decomposition becomes architectural when the line you draw isolates something you intend to
isolate: a concern, a secret, a team, or a quality.

**Start from the functional areas, and expect to diverge.** An area is a candidate for a
block, not a block. Copying the areas into the blueprint one for one produces a component
structure organised by the shape of the requirement document, which is nobody's design. One
area becomes several blocks where parts of it change independently. Several areas collapse
into one where they change together and share a secret. Every one of those relations gets a
reason, and the divergences are where the architecture argument actually lives.

Take the cutting criterion in this order of preference:

1. **Expected independent change.** Anything that will be changed at a different time, by
   different people, for a different reason, belongs in its own block. This is the strongest
   criterion and it is usually available.
2. **A domain concern the client already names.** A register, a policy engine, a channel, a
   settlement run. Their vocabulary, from `GLOSSARY.md` where one exists. A boundary the
   organisation already recognises costs nothing to explain and survives handover.
3. **Runtime isolation forced by a quality.** A failure domain, a latency path, a residency
   boundary, an audit path. Only from the qualities named at the end of Step 1.

Give every block one primary concern and one secret, the thing it hides that the others must
not depend on. If a block needs two secrets that change for different reasons, split it, or
record why not. Name the interface each block exposes, at the level of what crosses it, not
as a signature.

A cut that only reproduces the current team chart is a finding, not a target, unless the
client has stated that the team structure is fixed.

### 2c. The drawing

- Draw the boxes from the cut. Keep the count honest. A box budget guideline is in the
  reference.
- Draw the two main flows, one write path and one read path, as numbered steps through the
  boxes. If the system's centre of gravity is a batch or a file transfer, that is the write
  path.
- Mark on every box whether it is **existing**, **to be extended**, or **new**. This single
  marking is what turns a reference architecture into this client's design.
- Present options only where they change cost or risk. Two or three options at most, each
  with what it costs and what it risks. An option that changes neither is not an option, it
  is a preference, and it is decided silently.
- Get buy-in before the deep dive. In an offer the buy-in step is internal, the bid team and
  the delivery lead confirm the blueprint before anyone writes prose against it.

### 2d. Test the cut

Run the five tests in `references/principle-tests.md` over the blocks: separation of
concerns, cohesion, coupling, information hiding, modularity. Each is a question with a fail
signal, not a definition. Then check the cut against the qualities named at the end of Step
1, and only those.

Change the cut where a test fails and the failure matters for this mandate. Record the cuts
you rejected and why. A rejected alternative with a reason is the cheapest defence the
design has, and `red-team-review` will ask for it.

Diagram production is handed to `drawio-diagrams-enhanced`. The blueprint file in
`reference/` carries the box list with concern, secret and interface, the flows, the
markings and the rejected cuts, so the drawing can be redone without re-deciding anything.

## Step 3: Deep dive on the discriminators

Two or three points, no more. Use `references/tradeoff-memo.md`.

Choose the points that win or lose the deal, not the points that are technically
interesting. A point qualifies when at least one holds:

- the evaluator scores it, it stands in the criteria catalogue,
- it drives a material share of the cost,
- it is where the client has been burned before, or where the estate resists,
- it is where our approach differs from the obvious approach, so it carries a
  discriminator,
- it is where being wrong is expensive to reverse.

For each point: the question, the options, the criteria, the choice, what it costs, what it
risks, and what would make us change our mind. A trade-off with no losing side has not been
analysed.

Where a pattern applies, read the matching page in `references/pattern-index.md` for the
default components, the usual failure modes and the questions to ask the client. Use it as
a prompt for your own thinking. It is internal, it is never quoted, and its content is never
pasted into a document.

## Step 4: Capacity sheet

Build the back-of-the-envelope numbers as a working instrument, not as prose. Per the house
rule of 31.08.2026 this artifact is an `.xlsx`, built with the `xlsx` skill. The method,
the sheet layout and the formulas are in `references/capacity-worksheet.md`.

The rules that make the numbers defensible:

- Assumptions on their own sheet, one row each, every row with a source or the marker TBC.
- Computed values are formulas over the assumptions, never typed-in results. Change one
  assumption, the whole sheet moves.
- Label every unit. Requests per second, gigabytes per year, megabits per second, concurrent
  users. An unlabelled number is a defect.
- Peak is computed from average with a stated peak factor, and the factor itself is an
  assumption with a source.
- Add cost and data residency rows where the mandate needs them, which for Swiss regulated
  clients is most of the time.
- Never carry a latency or hardware figure from a textbook. Any performance number comes
  from the client estate, from a vendor statement with a date, or it does not appear.

The sheet is an estimate under stated assumptions, and it says so on its own legend sheet.
It is never presented as a measurement.

## Step 5: Wrap-up

Close the design with what a sponsor actually asks for, written into the trade-off memo:

- **Risks**: what could make this design wrong, and what we would do about it. Three to five,
  each with the trigger that would show it early.
- **Growth path**: how the system moves if the load grows, expressed with the scaling ladder
  in `references/scaling-ladder.md`. The ladder is the language for the growth path, it is
  never the architecture. Name where the design sits today and what the next rung would cost.
- **What we are not deciding yet**: the choices deliberately left open, and when each one
  falls due. This protects the offer and it is honest.

## Step 6: Handoff

Do not write the client-facing section here.

- **Prose**: hand the four artifacts to `inacta-proposal-writing`, which owns the solution
  approach section, the action titles and the narrative. It reads the blueprint and the
  trade-off memo from `reference/`.
- **Diagrams**: `drawio-diagrams-enhanced`, PNG before embedding, every figure with an
  action caption as a full sentence.
- **Effort and price**: the calculation instruments in `99 Methods/Kalkulation & Offerten/`.
  The capacity sheet is an input to the estimate, it is not an estimate.
- **Public-sector method**: where HERMES applies, the Systemkonzept and the Meilenstein
  Lösungsarchitektur are owned by `hermes-lite`, and this skill feeds that work.
- **Delivery**: if the mandate is won and the system is built, the arc42 skills take over.
  The blueprint is an input to arc42 section 5, not a substitute for it.
- **Review**: `tech-executive-review`, then `red-team-review`, then
  `publication-boundary-review`, per `LOOP.md` section 3. Do not review here.

## Publication boundary

`references/pattern-index.md` is class **A, INTERNAL** in the vocabulary of
`publication-boundary-review`. So are the four working artifacts while they sit in
`reference/`.

What that means in practice:

- Facts and decisions may be extracted into a client document.
- The pattern pages, their existence, their structure and their wording may not.
- Never cite the pattern index, the source repository or any book behind it in a client
  document.
- When the review builds the source map, these files are class A rows.

## Operating principles

- Never invent facts. A user count, an SLA, a cost, a volume or a deadline that is not in an
  input is an open question, not an assumption. Write TBC and keep going.
- No product without a client constraint. A named product enters the design only when the
  estate, a standard, a licence already held or an explicit requirement forces it. Otherwise
  name the component by what it does.
- The estate comes first. Every design starts from what already runs, what the client is
  bound to, and who operates it. A greenfield design at a client with a landscape is wrong
  even when it is elegant.
- One blueprint. Views multiply, understanding does not.
- Every cut names the concern it isolates. A box list nobody can give a criterion for is a
  function tree wearing a diagram.
- Weakest defensible form. Where the evidence carries less than the sentence claims, write
  less. Check with `weakest-claim-check`.
- Options only where they change cost or risk.
- Value over completeness. A short design that gets read beats a complete one that does not.
- Internal stays internal. The pattern index and the working artifacts do not leak into the
  draft.
- No em-dashes anywhere, use commas. German text uses Swiss spelling, ss instead of the
  sharp s, and real umlauts ä, ö, ü. English text is written for non-native readers, short sentences, plain
  words.

## Parameterization per engagement

Fixed: the steps, the folder mapping, the refusal list, the principles. Read or adapt
per mandate: the AGENTS.md settings, the style guide, the client glossary, the deliverable
type, the applicable method, HERMES or IPM or none, the regulatory frame, and the naming
convention. Defaults follow Swiss High German and Inacta conventions.

## Portability

- Runs on any Agent Skills compatible runtime. No runtime-specific tool is required. Where
  this skill says to ask the user, use whatever structured question mechanism the runtime
  offers, otherwise ask in plain chat. Where it says to hand a file over, use whatever file
  delivery the runtime offers.
- Operating brief of the engagement: look for `AGENTS.md`, then `AGENT.md`, then `CLAUDE.md`
  (legacy, still valid). Use the first one found. Never rename or overwrite an existing brief
  silently. If none exists, use `engagement-setup` first.
- A persistent project folder is expected. Without one, work on the files available in the
  current session, keep the same structure in the output, and say plainly that nothing was
  persisted. Do not pretend that persistent files exist.
- The capacity sheet needs a spreadsheet capability. If none is available, produce the same
  rows as a Markdown table, say plainly that it is not the house format, and note that it
  has to be rebuilt as `.xlsx` before it is used as a working instrument.
- No scripts. Every step is a judgement step, and the arithmetic belongs in the spreadsheet
  where it can be inspected.
