# The scaling ladder

Shared language for the growth path. It answers "what happens when this gets bigger" without
turning the answer into the architecture.

---

## What the ladder is for

A sponsor wants to know whether this will hold, and what the next step costs. The ladder
answers both in a vocabulary that survives the meeting, because each rung is a distinct
decision with a distinct price.

**The ladder is not the design.** A system does not have to climb it, and most of the systems
we design for our clients sit on the first two or three rungs for their whole life. Drawing
the top of the ladder as the target architecture is the classic failure of this method: it
buys operating complexity today against load that never arrives.

## The rungs

| # | Rung | What changes | What it buys | What it costs |
|---|---|---|---|---|
| 1 | Single node | Everything on one machine or one managed service | Simplicity, one thing to run and to reason about | One failure domain, one maintenance window |
| 2 | Split tiers | Application and data separated, each sized on its own | Independent sizing, clearer operations | One more thing to run and to secure between them |
| 3 | Cache and content delivery | Frequently read data served without touching the store | Read load falls, response gets faster | Staleness becomes a design question, and cache invalidation becomes a bug class |
| 4 | Stateless application tier | Session state out of the application node | Nodes become interchangeable, deployment gets easier | Session store becomes a dependency, and a new failure domain |
| 5 | Read replica | Reads served from a copy | Read capacity grows without touching the write path | Replication lag becomes visible to users, and someone has to decide what may be stale |
| 6 | Partitioning or sharding | Data split by a key | Write capacity grows past one store | The partition key is close to irreversible, cross-partition queries get expensive, operations get harder |
| 7 | Asynchronous processing, queue | Work decoupled from the request | Peaks absorbed, slow work removed from the user's wait | Eventual consistency in the user's experience, ordering and retry become explicit work, monitoring gets harder |

Rungs 3 to 7 are not strictly sequential. A system can take the queue before the replica.
The order in the table is the usual order of pressure, not a mandatory path.

## How to use it in an offer

Three sentences, no more, in the growth-path part of the solution section:

1. **Where the design sits today.** "The design as proposed sits at split tiers with a read
   cache."
2. **What the next rung would be, and what triggers it.** "If document volume grows past the
   figure in the capacity sheet, the next step is a read replica."
3. **What that step costs, in the honest currency.** Usually not licence money. Usually an
   operating decision, a consistency decision, or a person at 02:00.

Then stop. The rung after next is speculation, and a sponsor can tell.

## The questions the ladder answers well

- Does this design have a way to grow, or does it have a wall.
- Is the growth step a configuration change, a deployment change, or a redesign.
- Which growth step is irreversible. Partitioning usually is, and the partition key more so
  than the partitioning itself.
- Where does growth stop being a technical question and become an operating question.

## The questions it does not answer

- What the system should be today. That is the scope sheet and the blueprint.
- Whether to buy or build. That is a trade-off, see `tradeoff-memo.md`.
- Whether the client can operate the result. That is the sharpest question in the whole
  method and it lives in the trade-off memo, not here.

## Anti-patterns

- **Climbing for the picture.** Adding a queue, a cache and a shard to the blueprint so the
  design looks serious. Each rung is an operating cost that somebody carries for years.
- **Presenting the ladder as the roadmap.** A roadmap has dates, owners and money. The ladder
  has none of these, and a transition roadmap belongs to `inacta-ea-method`.
- **Skipping to the top because a reference architecture does.** The reference architecture
  was written for a load nobody at this client has.
- **Using the ladder as the answer to a capacity question.** The ladder says how to grow. The
  capacity sheet says whether growth is coming.
