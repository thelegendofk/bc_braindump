# Functional decomposition

Group the requirements before designing anything, and show the grouping. This is the artifact
that proves we read the scope, and it is what the component cut is derived from.

File: `reference/<Client>_<Engagement>_Functional_decomposition_<YYYY-MM-DD>.xlsx`. Internal.
Built with the `xlsx` skill, per the house rule of 31.08.2026.

---

## Two modes, and the first question is which one applies

**Adopt.** The requirement list already carries a usable structure, chapters, functional areas,
modules, a process model. Take it. Use the client's own names and their order, from
`GLOSSARY.md` where one exists. Note only where we deviate, and give the reason on the spot.

Deviating from a client's own structure in a tender, without saying why, reads as carelessness
rather than as insight. The evaluator wrote that structure, and often scored against it.

**Propose.** No usable structure exists. The requirements arrive as a flat list, as prose, or
scattered across annexes. Then we build the grouping and show every requirement landing in it.

This is the case where the artifact earns its place. The grouping itself is the evidence that
we understood the scope, and it is often the first thing in the offer that a technical
evaluator can judge. A bidder who hands back a flat list has demonstrated nothing.

**Mixed is normal.** The client structures part of the scope and leaves the rest loose. Adopt
what they gave, propose for the remainder, and mark in the legend which areas are theirs and
which are ours. Never present our grouping as if it came from them.

---

## The grouping criterion

Pick one and name it. In preference order:

1. **A business process or lifecycle stage the client already names.** Application, assessment,
   decision, payment, archiving. Their words. Costs nothing to explain, survives handover, and
   matches how the organisation is actually run.
2. **A business object.** A contract, a claim, a meter reading, a dossier, a case file. Strong
   where several processes touch the same object and the object is what the client argues
   about.
3. **The actor served.** Citizen, case worker, partner organisation, supervisor. Useful where
   the same function looks completely different per audience, common in public-sector portals.
4. **A regulatory or legal regime.** Where a set of requirements is governed together and will
   change together, that shared fate is a real boundary.

Mixing criteria across areas is allowed where the scope genuinely mixes, but say so. Mixing
them silently produces a grouping nobody can extend.

### Never group by technical layer

Front end, back end, database, integration, reporting. That is a component cut wearing a
functional label. It tells the reader how we build software, not how their business works, and
it makes the grouping read as our org chart rather than their world. The technical structure
comes later, in the cut, and it is allowed to look different.

---

## Sheets

### Sheet 1, `Bereiche` (areas)

One row per functional area.

| Column | What goes in it |
|---|---|
| Area ID | `FA-1`, `FA-2`, stable, used everywhere downstream |
| Name | In the client's vocabulary. Check `GLOSSARY.md`, and do not use a term with status Heard unchecked |
| What it covers | One sentence, in business terms, no technology |
| Criterion | Which of the four above put this boundary here |
| Source | Client structure, ours, or mixed |
| Note | Open questions, overlaps, anything deliberately unresolved |

**No count column.** A column counting the requirements per area is banned by the writing
guidelines, section 0.2, and it goes stale the moment a requirement moves. What the reader
actually needs to know is whether the scope is covered, and the check below answers that.

### Sheet 2, `Zuordnung` (mapping)

One row per requirement.

Where `shipley-proposal` has built a compliance matrix, **do not rebuild it here.** Add a single
`Functional area` column to that matrix instead, and keep this sheet for the requirements the
matrix does not carry. One place to filter, one place to maintain. This skill is a declared
writer of that one column and touches nothing else in the workbook.

Where no compliance matrix exists, a proactive proposal or a concept without an RFP, this sheet
carries the requirements itself.

| Column | What goes in it |
|---|---|
| Req ID | The stable ID, `R-01`, the join key to the compliance matrix |
| Source | Where the requirement comes from, section and page |
| Requirement | Short text. By formula from the matrix where one exists, typed only where none does |
| Area ID | Exactly one. A requirement that belongs in more than one area needs splitting |
| Sub-function | Optional, only where an area is large enough to need one level more |
| Note | Why this landing was not obvious, where it was not |

### Sheet 3, `Legende` (legend)

The criterion, which areas are the client's and which are ours, the coverage check result, the
open questions, and the date. Same convention as the capacity sheet, blue input cells, formulas
in black.

---

## The coverage check

Answered by formula in the legend sheet:

- **Which requirements have no area.** Every one of them is either an unmapped requirement or a
  sign that an area is missing. Both are findings.
- **Which requirements sit in more than one area.** A compound requirement that needs splitting,
  which is also what the compliance matrix guide asks for.
- **Which areas hold nothing.** An area with no requirement is either scope the client forgot,
  which is worth raising, or an area we invented, which is worth deleting.

An unmapped Must is the serious one. It means the grouping does not cover the scope, and the
grouping is the thing we are using to claim we understood it.

---

## Depth

Go one level, two only where an area is genuinely large. A decomposition three levels deep is a
requirement list with indentation, and it has stopped being a grouping.

Keep the number of areas in a range a reader can hold, which in practice means a handful to
around a dozen. Too few and the grouping says nothing. Too many and it is the flat list again.

---

## The handover to the cut

This is the point of the artifact, and it is the part that most often gets skipped.

**A functional area is a candidate for a building block. It is not a block.** Copying the areas
into the blueprint one for one is the failure mode. It produces a component structure organised
by the shape of the requirement document, which is nobody's design.

Three relations, and every one of them gets recorded in the blueprint:

- **One area becomes several blocks.** Parts of it change independently, or a quality forces a
  runtime boundary inside it. Common where an area mixes a stable core with a volatile rule set.
- **Several areas collapse into one block.** They change together, they share a secret, and
  splitting them would create an interface nobody wants to own.
- **One area maps to one block.** Fine, and it needs a reason like the others, not silence.

**The divergences are the architecture argument.** Where the component cut differs from the
functional grouping, that difference is a decision we made and can defend, and it is what a
technical evaluator reads to see whether there is an architect behind the document. Record each
one in the rejected-cuts and mapping tables of `blueprint-guide.md`, with the reason.

A blueprint whose blocks match the functional areas one for one, with no divergence anywhere,
makes a claim: that the business structure and the change structure are identical. That can be
true, and it needs a sentence of its own, because the reader cannot tell it apart from a cut
that was never made.

---

## What reaches the client

The area list with what each covers, the criterion in a sentence or two, and, where we proposed
the structure, the fact that we proposed it. The mapping sheet stays internal, unless the RFP
asks for a requirement traceability table, in which case produce a clean client-facing copy the
way the compliance matrix guide describes.

Where we proposed the grouping, say so. And keep it in its place, it is how the scope is
organised. The architecture is what comes out of the cut.

## Quality check before moving on

- The mode is stated, adopt or propose or mixed, and the legend says which areas are whose.
- The criterion is named, and it is not a technical layer.
- Every requirement has exactly one area, or appears in the coverage check as a finding.
- No area is empty, or the empty one is explained.
- Area names come from the client's vocabulary where one exists.
- The depth stays at one level, with a second only where an area needed it.
- The relation to the cut is recorded in the blueprint, divergences with reasons.
