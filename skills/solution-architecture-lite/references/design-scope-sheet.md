# Design scope sheet

The first artifact and the one that most often decides whether the rest is any good. It
fixes what is being designed, under which constraints, against which estate, and what is
deliberately left out.

File: `reference/<Client>_<Engagement>_Design_scope_<YYYY-MM-DD>.md`. Internal.

Rule for the whole sheet: every figure and every commitment carries a **Source** or the
marker **TBC**. There is no third state. A number without either is a defect, and a reviewer
will find it.

---

## Template

```markdown
# Design scope, <System name>

Status: draft | agreed internally | agreed with client
Date: <YYYY-MM-DD>
Basis: <RFP section, meeting, document, with date>

## 1. What the system does

The three to seven load-bearing functions. Not the requirement list.

| # | Function | Who uses it | Source |
|---|---|---|---|
| F1 | | | RFP 3.2 |
| F2 | | | TBC |

One sentence on what the system is for, in the client's own words where we have them.

## 2. Non-functional requirements

| Property | Requirement | Source | Note |
|---|---|---|---|
| Availability | | RFP / TBC | service hours, not just a percentage |
| Latency or response time | | RFP / TBC | for which operation, measured where |
| Throughput | | RFP / TBC | peak, not average |
| Data retention | | law / RFP / TBC | how long, and what happens after |
| Recovery, RTO and RPO | | RFP / TBC | |
| Security and audit | | RFP / TBC | who has to be able to prove what |
| Data residency | | RFP / law / TBC | where the data may be stored and processed |
| Accessibility | | RFP / standard / TBC | relevant for public-sector front ends |
| Languages | | RFP / TBC | |

Anything not stated by the client is an open question, not an assumption. Write TBC and
carry it into the open-questions list of the engagement.

### 2b. Which of these will shape the cut

Most of the table above constrains how the system is built. Two or three entries constrain
**where the boundaries go**, and those are a different thing. Mark them.

| Quality | Required level | Why it moves a boundary | Source |
|---|---|---|---|

A quality belongs here when the required level is high enough to force a structural choice:
a recovery objective that needs its own failure domain, a residency or retention rule that
needs a separate store, an audit duty that needs an append-only path, a latency budget that
cannot afford to cross an integration.

Two or three. If everything in the list shapes the cut, nothing does, and the design will be
driven by whichever quality was discussed most recently. Step 2 uses these as a cutting
criterion and the principle-test pass in Step 2c checks the cut against these and no others.

## 3. Scale assumptions

| Quantity | Value | Unit | Source | Horizon |
|---|---|---|---|---|
| Users, total | | | | today |
| Users, concurrent peak | | | | today |
| Transactions | | per day | | today |
| Documents or objects | | per year | | today |
| Average object size | | MB | | |
| Growth | | percent per year | | contract term |

These feed the capacity sheet directly. Do not compute here, only collect.

## 4. Existing estate

The block that keeps the design from being generic. If it is empty, the sheet is not
finished.

| Element | What it is | Bearing on the design | Source |
|---|---|---|---|
| Systems it must integrate with | | | |
| Platforms and standards set by the client or its EA | | | |
| Licences and products already held | | | |
| Identity and access, how users are authenticated today | | | |
| Hosting and operating model, who runs it, in-house or provider | | | |
| Network and zone model, where the system may sit | | | |
| Release and change process it has to fit into | | | |
| Known pain, what went wrong last time | | | |

## 5. Explicit out of scope

| # | Not covered | Why | Who owns it instead |
|---|---|---|---|
| O1 | | | |

## 6. Not decided yet

Choices deliberately left open, with the point at which each falls due.

| # | Open choice | Falls due | What would decide it |
|---|---|---|---|
| D1 | | | |

## 7. Open questions to the client

| # | Question | Blocks what | Asked on |
|---|---|---|---|
| Q1 | | | |
```

---

## How to fill it

**Work through the blocks in order.** Blocks 1 and 2 come from the RFP or the brief. Block 3
comes from the client, and it is the one most often missing. Block 4 comes from the
conversation, from earlier mandates at this client, and from the EA outputs where they
exist. Blocks 5 to 7 are written last, from what the first four exposed.

**Do not negotiate with yourself over TBC.** A scope sheet with twelve TBC rows is an honest
statement about the state of the information. A scope sheet with twelve invented figures is
a liability that reaches the client under our letterhead.

**Non-functional requirements are where offers are won and lost.** Availability during
service hours, a recovery objective, an audit trail requirement and a residency rule each
change the design more than any functional requirement does. Read the RFP for them
specifically, they are usually scattered and rarely in one chapter.

**Watch for the requirement that is really a constraint.** "The system must use the existing
identity provider" belongs in block 4, as a constraint. Put it in block 1 and the design
never sees it.

## Quality check before moving on

- Every row has a source or TBC.
- Block 4 has at least three real entries.
- Block 2b names two or three qualities, not the whole list, and each says which boundary it
  moves.
- No figure appears that nobody can point at a source for.
- The out-of-scope block is not empty. An offer that scopes nothing out has not been read
  carefully.
- The functions in block 1 are recognisable to the client in their own vocabulary. Check
  against `GLOSSARY.md` at client level where one exists.
