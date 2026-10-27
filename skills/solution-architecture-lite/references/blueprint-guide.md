# Blueprint guide

One picture of the system, the two main flows through it, and a marking on every box that
says whether it already exists. That is the whole artifact.

File: `reference/<Client>_<Engagement>_Blueprint_<YYYY-MM-DD>.md`. Internal. The drawing
itself is produced by `drawio-diagrams-enhanced` from this file.

---

## Why the file and the drawing are separate

The file carries the decisions. The drawing carries the picture. Keeping them apart means a
diagram can be redrawn, restyled or moved into a deck without anyone re-deciding what is in
it, and it means the design survives a change of drawing tool.

## The box budget

An honest count, matched to the system, not to the space on the slide.

| System size | Boxes | Flows |
|---|---|---|
| Small internal tool | 2 to 5 | one is often enough |
| Departmental system, one client organisation | 6 to 12 | write path and read path |
| Platform with several consumers or channels | 12 to 18 | write, read, and one integration path |

Above eighteen boxes the picture stops explaining and starts decorating. If the system
really is that large, cut it into two blueprints along a boundary the client recognises, for
example channel and core, or per business domain.

The reverse error is the more expensive one. A twenty-box reference architecture drawn for a
small internal tool tells the evaluator that we did not read the brief.

## What is a box

A box is a block of the cut from Step 2b, drawn. The criterion came first, the picture second.
If a box cannot be given a concern and a secret, it is a heading, and it does not get a box.

- **Components** we build, extend or run. Named by what they do, not by a product, unless
  the estate forces the product.
- **Stores**. A database, a document store, a queue, a cache. Say what is in it, not just
  its type.
- **External systems** at the client or at third parties, with the direction of the
  integration.
- **Actors**. The human roles and the machine callers, at the edge of the picture.

What is not a box: layers, phases, principles, and anything that is a heading rather than a
thing that runs.

## The marking that makes it this client's design

Every box carries exactly one of three markings:

| Marking | Meaning | Question it answers for the sponsor |
|---|---|---|
| **existing** | Runs today, unchanged | What are we reusing |
| **extend** | Runs today, we change or configure it | What are we touching |
| **new** | Does not exist yet | What are we actually building |

Count the three at the end. The ratio is the single most informative number in the
blueprint, and it drives the estimate, the risk and the "buy versus build" answer more than
any technology choice does.

A blueprint where every box is marked new, at a client with an estate, is wrong. Go back to
block 4 of the scope sheet.

## Concern, secret and interface

Three more columns on the box table, and they are what makes the table a design record
rather than an inventory.

| Column | What goes in it | Fail signal |
|---|---|---|
| **Concern** | The one reason this block exists, in a sentence. From the cutting criterion. | A list instead of a reason |
| **Secret** | What the block hides that the others must not depend on: a data layout, an algorithm, a vendor product, a legal rule, a protocol | Empty, or something that will never change |
| **Interface** | What crosses the boundary, at the level of what is exchanged, not a signature | A technology name instead of a content |

The secret column is the one that gets skipped and the one that pays. It is the record of
what the design is betting will change. Where a block genuinely hides nothing, say so, and
expect `red-team-review` to ask why it is a separate block.

## Module and runtime are two cuts, not one picture

The box table is the module cut: who owns what, and who may depend on whom. The flows below
are the runtime cut: what talks to what while the system is running. They are not the same
shape and they are not supposed to be.

**Record where they diverge.** One module served by three runtime processes, or three modules
in one deployable, is normal and it is worth a line. The divergence is often where the design
actually is, and it is the first thing a technical evaluator looks for.

**Allocation is a third cut**, who runs it and where, and it is drawn only when deployment,
operating responsibility, teams or platform zones are in scope for this mandate. In an offer
it usually is, because the operating question decides the price. Keep it to a note on the box
table rather than a third picture, unless the client asked for one.

A C4 container diagram mixes module and runtime by design. That is fine, and it is what many
clients use. Label it for what it is, and keep the concern and the secret on every box
whatever notation the client mandates.

## The flows

Two numbered flows, written as steps, not drawn as arrows only.

**Write path.** How data enters the system and becomes durable. If the system's centre of
gravity is a nightly batch, a file delivery or a message feed, that is the write path, not
a web form. Say where the transaction boundary is, and what happens if the step after it
fails.

**Read path.** How a user or a consuming system gets an answer. Say what is served from
where, and what the freshness of the answer is.

Add a third flow only where it carries a decision: an integration path, an approval path, a
failure path.

### Flow template

```markdown
### Flow 1, write: <name in the client's words>

1. <Actor or system> does <what> at <box>
2. <box> validates <what>, against <what source>
3. <box> writes to <store>. Transaction boundary is here.
4. <box> notifies <box> asynchronously. If this fails, <what happens>.
5. ...

Freshness: <how long until the result is visible on the read path>
Failure behaviour: <what the user sees, what is retried, what needs a human>
Volume: <points at the capacity sheet, no figure repeated here>
```

Do not repeat capacity figures in the blueprint. Point at the capacity sheet. A number that
lives in two files will be wrong in one of them within a week.

## Options

Show an option only where it changes cost or risk. Each option gets:

| Option | What changes | Cost effect | Risk effect | Reversible |
|---|---|---|---|---|
| A, recommended | | | | |
| B | | | | |

Two or three options at most, and the recommendation is stated. An option that changes
neither cost nor risk is a preference and is decided quietly, without asking the client to
carry it.

## Template

```markdown
# Blueprint, <System name>

Status: draft | agreed internally | agreed with client
Date: <YYYY-MM-DD>
Scope sheet: <file name>

## Boxes

| ID | Box | Concern, the one reason it exists | Secret, what it hides | Interface, what crosses | Serves area | Marking | Depends on |
|---|---|---|---|---|---|---|---|
| C1 | | | | | FA-n | existing / extend / new | |

Count: <n> existing, <n> extend, <n> new.

Cutting criterion used, per block or for the set: expected independent change, a domain
concern the client names, or runtime isolation forced by a quality.

## From functional areas to blocks

The `Serves area` column carries the `FA-n` IDs from the functional decomposition. Where a
block serves more than one, list them.

Then record the divergence, because that is the part a technical evaluator reads.

| Functional area | Blocks that serve it | Relation | Reason |
|---|---|---|---|
| FA-n | C-n | one to one / split / merged | |

- **Split**, one area over several blocks: parts of it change independently, or a quality
  forces a runtime boundary inside it.
- **Merged**, several areas in one block: they change together, share a secret, and splitting
  them would create an interface nobody wants to own.
- **One to one**: fine, and it still needs a reason rather than silence.

A blueprint whose blocks match the areas one for one everywhere is claiming that the business
structure and the change structure are identical. That can be true. It needs a sentence saying
so, because the reader cannot tell it apart from a cut that was never made.

## Cuts we rejected

| Alternative cut | Why it was considered | Why it was not taken |
|---|---|---|

Keep this table even when it is short. A cut with no rejected alternative reads as a cut that
was never made.

## Flows

### Flow 1, write: <name>
...

### Flow 2, read: <name>
...

## Boundaries

- Trust boundary: <where it runs, which zone>
- Data residency boundary: <what may leave which jurisdiction>
- Operating boundary: <who runs which box, us, the client, a provider>

## Options with a cost or risk effect

| Option | What changes | Cost effect | Risk effect | Reversible |
|---|---|---|---|---|

## What this picture deliberately does not show

<the views left out, and why>
```

## Handing it to the drawing

Give `drawio-diagrams-enhanced` the box table and the flows. Conventions that hold across
the house:

- Export to PNG before embedding.
- Every figure carries an action caption, a full sentence stating the point the reader takes
  away, placed directly under the object. See `shipley-proposal`,
  `references/graphics-and-captions.md`.
- The three markings need a visible, printable distinction that survives greyscale. Do not
  rely on colour alone.
- Keep the client's own names for their systems, from `GLOSSARY.md` where one exists.

## Quality check before moving on

- The box count fits the system size, in both directions.
- Every box carries a marking, and the three counts are stated.
- Every box has a concern and a secret, or a recorded reason why it has no secret.
- The module cut and the runtime cut are both present, and their divergence is noted.
- The rejected-cuts table has at least one row, or a line saying no alternative was on the
  table and why.
- The five tests in `principle-tests.md` have been run over the blocks.
- Every block names the functional area it serves, and the area-to-block table states the
  relation and the reason for each.
- The write path names its transaction boundary and its failure behaviour.
- No capacity figure is repeated here.
- No product name appears without a constraint in block 4 of the scope sheet that forces it.
- Someone who has not read the brief could not guess which client this is from the picture.
  If they could not tell it apart from a generic diagram, it is not finished.
