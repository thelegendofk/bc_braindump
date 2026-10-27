# The five tests on the cut

Run after the blocks are named, before the drawing is handed to production. Each test is a
question with a fail signal. None of them is a definition to quote, and none of them belongs
in a client document.

The tests do not tell you what the right cut is. They tell you when the cut you have made
will cost somebody something later, and roughly what.

---

## T1. Separation of concerns

**Question.** How many reasons does this block have to change?

**Fail signal.** More than one, and the reasons come from different places. A block that
changes when the tax rules change and also when the channel front end changes is carrying
both. So is a block that the regulator can force to change and that the marketing department
can also force to change.

**What it costs if you leave it.** Every release touches the block, so every release needs
the people who understand both concerns, and the test surface never shrinks.

**When to leave it anyway.** The block is small, both concerns change on the same rhythm, and
splitting it would create an interface nobody wants to own. Record the decision.

---

## T2. Cohesion

**Question.** Do the responsibilities inside this block belong together for one reason a
person can state in a sentence?

**Fail signal.** The only honest description of the block is a list. "Handles validation,
notification, reporting and the nightly export" is a list, not a reason. A name ending in
Manager, Service, Handler or Utility with no domain word in it is the same signal.

**What it costs if you leave it.** Nobody can predict where a change lands, so every change
starts with a search. The block grows because it is the obvious place to put anything.

**When to leave it anyway.** It is a deliberate seam for a single team in a small system,
and the alternative is more blocks than the system deserves.

---

## T3. Coupling

**Question.** What does this block have to know about another block, and can that knowledge
be made smaller?

**Fail signal.** A block that knows another block's data layout, its internal states, its
deployment schedule, or its error codes beyond a documented set. Two blocks that must be
released together are one block that has been drawn as two.

**What it costs if you leave it.** The blocks stop being independently changeable, which was
the point of drawing them apart. The estimate for any change in one has to include the
other.

**Where this bites hardest in our mandates.** Integration with a core system the client will
not change. The coupling is real and it is not ours to remove, so name it, and design so
that it sits behind one adapter rather than spread across the system.

---

## T4. Information hiding

**Question.** What secret does this block hide, and is that secret likely to change on its
own?

**Fail signal.** The block has no secret, only responsibilities. Or the secret is stable
forever, in which case hiding it buys nothing. Or the secret leaks: it is visible in the
interface, in a shared table, in a file format, or in an identifier that another block
parses.

**What it costs if you leave it.** The design has no protection against the change it was
built to absorb. When the secret changes, the change spreads, and it spreads through the
places nobody documented.

**The useful version of the question.** What are we betting will change here, and who else
finds out when it does. If the answer is nobody, the boundary is doing its job.

---

## T5. Modularity

**Question.** Could a competent newcomer understand this block, and could a different
supplier replace it, from its interface and its stated secret alone, without reading the
internals of its neighbours?

**Fail signal.** Explaining the block requires explaining two others first. Or replacing it
would require a coordinated change in blocks that were supposed to be independent.

**What it costs if you leave it.** Handover gets expensive, second-supplier scenarios are
not credible, and the client is locked in whether or not anybody intended that.

**Why this one matters commercially.** In a public-sector mandate the client may have to
show that the result is not a lock-in. In a private one they will ask what happens if the
supplier relationship ends. This test is where that answer comes from, and it is worth a
sentence in the offer.

---

## Running the pass

Go block by block rather than test by test. A whole block takes a few minutes, and the pattern
of failures across blocks is more informative than any single failure.

**Then run the quality check.** Take only the two or three qualities named at the end of
Step 1 and ask, for each, whether the cut protects it or works against it. A recovery
objective that requires a failure domain the cut does not have is a finding. A latency path
that now crosses three blocks and an integration is a finding. Everything else in the
non-functional list is out of scope for this pass.

**Change what matters, record the rest.** Not every failed test earns a redesign. A failure
earns a change when the thing it costs is something this mandate will actually pay. The
others go into the trade-off memo as known and accepted, with the reason. That list is worth
more than a clean sheet, because a clean sheet reads as a cut that was never tested.

## What does not go in a client document

The names of these tests, the framework behind them, and the pass itself. What goes in is
the result: the criterion of the cut in a few sentences, the blocks with their concerns, and
the alternatives that were rejected with the reason. A client who reads "we applied
separation of concerns and information hiding" learns nothing. A client who reads "the
policy engine is separate because the cantonal rules change on their own schedule and we do
not want a release of the portal to be blocked by them" learns the design.
