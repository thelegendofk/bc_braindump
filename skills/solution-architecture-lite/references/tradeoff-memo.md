# Trade-off and deep-dive memo

Two or three points, analysed properly, plus the wrap-up. This is the artifact that survives
into the offer as substance, and it is the one a technically strong evaluator reads first.

File: `reference/<Client>_<Engagement>_Tradeoffs_<YYYY-MM-DD>.md`. Internal.

---

## Choosing the points

A point earns a deep dive when at least one of these holds:

1. **The evaluator scores it.** It stands in the criteria catalogue with weight.
2. **It drives cost.** A material share of the build or the run.
3. **The client has scar tissue there.** It failed before, or the estate resists it.
4. **It carries a discriminator.** Our approach differs from the obvious one, and the
   difference is defensible.
5. **Being wrong is expensive.** Hard to reverse once built.

A point that is only technically interesting does not qualify. Neither does a point where
every credible bidder will write the same paragraph.

**Two or three. Not five.** A memo with five deep dives has no deep dives, it has an
overview, and the reader stops at the second one.

## Structure per point

```markdown
## Deep dive <n>: <the question, as a question>

**Why this one.** <which of the five criteria, in one sentence, with the evidence>

**What is actually being decided.** <the decision in the client's terms, not in ours>

**Options.**

| Option | What it is | Cost | Risk | Fits the estate | Reversible |
|---|---|---|---|---|---|
| A | | | | | |
| B | | | | | |
| C | | | | | |

**Criteria we decided on.** <the two or three criteria that did the work, and why those>

**Choice, and the losing side.** <what we propose, and what we give up by proposing it. A
trade-off with no losing side has not been analysed.>

**What it costs to be wrong.** <what has to change if this turns out badly, and when we
would find out>

**What would change our mind.** <the fact or the client answer that flips the decision>

**Status.** decided | recommended, client to confirm | open, needs input
```

## The questions that decide most of our deals

Not every point, but these come up in almost every mandate at a Swiss regulated client, and
they are usually the real discriminators. Check them before choosing anything more exotic.

- **Buy or build.** What the client already owns, what a product covers, what the gap costs
  to close, and what the licence and the lock-in cost over the contract term. Name what
  building buys that buying does not, or recommend the product.
- **Where the data lives and who may process it.** Jurisdiction for storage and for
  processing, per data class, with the rule and its source. For Swiss personal data, the
  CISO decides. This is a design constraint before it is a compliance chapter.
- **Who operates it at 02:00.** The client's own operations, a provider, or us. The answer
  changes the design, not only the price. A design the client cannot run is a design that
  fails after handover, and the failure will be attributed to the design.
- **Year-one cost, and what it is made of.** Build, licence, infrastructure, run. Where the
  figures are not available, the memo says so, and the offer does not invent them.

## Integration with the estate

Where the design touches something that already runs, the memo says for each touch point:

| Touch point | Interface that exists today | What we need | Who owns the change | Lead time |
|---|---|---|---|---|

Lead time on a client-side interface change is a schedule risk more often than a technical
one, and it belongs in the risk list below.

## The wrap-up

Written at the end of the memo, and it is what the sponsor actually reads.

### Risks

Three to five. Each one with the trigger that would show it early, so the client sees a
managed risk rather than a warning.

| # | Risk | Effect if it happens | What we do about it | Trigger that shows it early |
|---|---|---|---|---|

Do not write risks that flatter us. "The client may not provide data on time" is real, and
it belongs in, phrased as a joint dependency rather than a complaint.

### Growth path

Three sentences using `scaling-ladder.md`: where the design sits today, what the next rung
is and what triggers it, and what that rung costs in operating terms. Not a roadmap.

### What we are not deciding yet

| # | Open choice | Falls due at | What will decide it | Why it is safe to wait |
|---|---|---|---|---|

This section protects the offer and it reads as confidence rather than as a gap, provided
each row says why waiting is safe. An open choice with no reason to be open is an unfinished
decision.

## Style rules that apply to this memo specifically

- **Weakest defensible form.** Where the evidence carries less than the sentence claims,
  write less. Run `weakest-claim-check` before any of this reaches a client document.
- **No product without a constraint.** A named product enters only where the estate, a
  standard, a licence already held, or an explicit requirement forces it.
- **State the losing side.** Every trade-off costs something. Naming it is what makes the
  rest credible.
- **Numbers point at the capacity sheet.** They are not repeated here.
- **Internal reasoning stays internal.** Our win themes, our margin thinking, our view of the
  competition and our doubts about the client's estate belong in this memo and never in the
  offer. `publication-boundary-review` will look for exactly this.

## Quality check before handing over

- Two or three deep dives, not five.
- Each one names which of the five criteria qualified it.
- Each one has a losing side.
- The four standard questions are at least considered, and their absence is deliberate.
- The risk list has triggers, not just mitigations.
- The growth path is three sentences and uses the ladder vocabulary.
- Nothing in the memo assumes a figure that the capacity sheet does not carry with a source.
