# Pattern index

**Classification: A, INTERNAL, non publishable.** In the vocabulary of
`publication-boundary-review` this file is a class A source. Facts and decisions taken from
it may appear in a client document. This file, its structure, its wording and its existence
may not. Never cite it. Never paste a page into an offer. When a source map is built for a
package that used it, it is a class A row.

---

## What this is

A thinking prompt, eight pages long, for the patterns that recur in our mandates at banks,
insurers, energy utilities, healthcare organisations and public-sector clients. Each page
says when the pattern applies, which components usually appear, how it usually fails, what
to ask the client, and what a design drawn on a blank page would miss.

It is not a catalogue of designs. It does not contain a recommended architecture, and using
a page as one is the failure this whole skill is built against. Our offers start from an
existing estate, a budget, a delivery model, an information-security frame and often a
public-sector method. A page here has none of that context, so it can only ask questions.

**How to use a page:** read it before the deep dive, ask the questions it lists, then close
it and design against what the client answered.

**Adding a page:** only when a real mandate needed one. A page that was written for
completeness has never been read by anybody.

---

## P1 Notification and messaging to people

**When it applies.** The system has to tell a human something: a payment posted, a claim
decided, a meter reading due, an appointment, a deadline, an outage. Almost every client
system we design has this somewhere, and it is almost always underestimated.

**Default components.** A trigger source, a notification service holding templates and
routing rules, per-channel adapters (email, SMS, push, letter, an in-product inbox), a
preference and consent store, a delivery log.

**Usual failure modes.** Duplicate sends after a retry. A template change deployed without
review reaching thousands of people at once. Silent failure of one channel while the others
work. Bounce and opt-out handling never built. The delivery log missing when someone asks
"did the customer receive it", which in a regulated client is the actual requirement.

**Ask the client.** Which channels are legally sufficient for which message, letters
included. Who owns the templates and who approves a change. What proof of delivery has to
be retained, and for how long. Which messages are consent-based and which are contractual.
What the existing channel infrastructure is, because most of our clients already have an
output-management or campaign system that nobody mentioned in the RFP.

**What a blank-page design misses.** Physical letters and the print provider. Consent as a
legal object rather than a checkbox. The proof-of-delivery requirement. The existing
output-management platform, which usually makes half the design unnecessary.

---

## P2 Document and object storage

**When it applies.** Contracts, policies, claims files, patient documents, scans, plans,
evidence, exports. Endemic in insurance, healthcare and public administration.

**Default components.** An object store, a metadata index, an ingestion path with virus
scanning and format normalisation, a rendering or preview service, a retention and disposal
engine, access control at document level.

**Usual failure modes.** Retention designed as "keep everything", which is a legal defect
and not only a cost problem. Metadata modelled after the storage rather than after the
business process, so nothing can be found. Permissions on the folder rather than on the
document. Migration of the existing archive discovered late and costing more than the new
system. Full-text search promised and then not budgeted.

**Ask the client.** What retention rules apply per document class, and where they come from.
What happens at the end of retention, delete or archive. Which archive exists today, how
much is in it, and whether it moves. Who may see which document, and is that per role or per
case. Are documents evidence in a legal sense, which raises the integrity requirement.

**What a blank-page design misses.** The existing archive and its migration. Legal disposal
duties. The document classes that must be immutable, see P5. The fact that scan quality and
format chaos in the existing stock will break any automated processing assumption.

---

## P3 Batch and file ingestion

**When it applies.** The counterparty is another organisation's system and the interface is
a file: a nightly delivery, a clearing file, a meter-data export, a payroll run, a register
extract. This is the single most common integration shape at our clients, and it is the one
most often missing from a modern-looking design.

**Default components.** A landing zone, a validation step with a rejection path, an
idempotent load, a reconciliation step, an operational log with a per-run status, an alerting
path for a missing or late file.

**Usual failure modes.** No idempotency, so a re-delivered file doubles the data. Partial
loads with no defined restart point. The rejection path built as a log line nobody reads
rather than as work for a named person. Late or missing file detected by a user rather than
by monitoring. Reconciliation never built, so nobody can prove that what arrived is what was
sent. A format change at the sender with no version handling.

**Ask the client.** Who sends the file, under what agreement, and what is the escalation
path when it is late. Is a re-delivery possible, and how is it distinguished from a new one.
What is the cut-off, and what depends on the load being finished. Who works the rejections,
and in which system. How is a mismatch reconciled today.

**What a blank-page design misses.** That the sender is a different organisation with its own
release calendar and no interest in our schedule. The operational reality that somebody has
to look at the rejections every morning. The reconciliation duty, which in a financial
context is not optional.

---

## P4 Integration and API layer

**When it applies.** The system has to talk to core systems that already exist and will not
change: a core banking system, a policy system, an ERP, a patient record, a register.

**Default components.** An integration layer or gateway, per-system adapters, a translation
between the client's domain terms and the core system's terms, a timeout and retry policy, a
circuit breaker or degradation behaviour, an interface contract per integration.

**Usual failure modes.** The core system's availability window silently becomes the new
system's availability. Synchronous chains where one slow core call blocks the user request.
No degradation behaviour, so the whole system is down when one integration is. Interface
change on the core side with no contract and no test. The integration team on the client
side being a shared, booked-out resource, which is a schedule risk and not a technical one.

**Ask the client.** What service hours and maintenance windows each core system has, and
whether ours may be longer. Which interface exists today, and who owns changing it. What the
lead time on a core-side change is. What the system should do when a core system is
unavailable. Is there an existing integration platform we are expected to use, and who
governs it.

**What a blank-page design misses.** Maintenance windows. The ownership and lead time of
core-side changes. The existing integration platform and its governance body, which usually
has to approve our design. That "read from the core system" often means a batch extract and
not an API.

---

## P5 Audit trail and immutability

**When it applies.** Somebody has to prove later what happened: a supervisory requirement, a
legal-evidence requirement, a medical record, a public-sector decision, a change to a
regulated calculation. Common across every one of our client sectors.

**Default components.** An append-only event or audit store, a defined event vocabulary,
actor and timestamp on every entry, integrity protection appropriate to the requirement, a
retention rule, and a way to read it that a non-engineer can use.

**Usual failure modes.** Audit built as application logging, which is not the same thing and
does not survive an audit. No defined actor for machine-triggered actions. Audit data
mutable by an administrator with no trace. Retention of the audit shorter than the retention
of the thing audited. No usable read path, so answering one supervisory question takes a
developer and two days.

**Ask the client.** Who audits this, and what have they asked for in the past. What has to be
provable, and for how long. Is a technical log sufficient or is a business-level record
required. Who may read the audit trail, and does reading it get audited too. Is there an
existing archive or audit platform with a retention frame already approved.

**What a blank-page design misses.** That the reader of the audit trail is an auditor or a
supervisor, not an engineer, so the read path is a requirement. That immutability has degrees
and the required degree comes from the legal frame, not from our preference. That the audit
retention often outlives the system itself.

---

## P6 Identity, access and roles

**When it applies.** Always, and it is usually settled by the estate rather than designed.

**Default components.** The client's existing identity provider, a federation or single
sign-on path, a role model, an authorisation decision point, a joiner-mover-leaver process,
elevated access handling for support and operations.

**Usual failure modes.** A role model designed by engineers and never reconciled with the
organisation, so it fits nobody and everybody ends up with a wide role. Support and
operations access designed last, then granted broadly under time pressure. External users
(customers, partners, citizens) treated with the same model as internal staff, when they need
a different one. Deprovisioning not built, so leavers keep access. Delegation and
representation cases, common in insurance and public administration, discovered late.

**Ask the client.** Which identity provider is mandatory. Are external users in scope, and
through which identity. What the existing role concept is and who owns it. How support staff
access production data, and under what control. What happens on a leaver. Are there
representation, delegation or four-eyes cases in the process.

**What a blank-page design misses.** That this is a constraint, not a design space. The
external-user identity question. Support access as a designed path rather than an exception.
The client's own segregation-of-duties rules, which can forbid an otherwise sensible design.

---

## P7 Throttling and load protection

**When it applies.** The system exposes an interface that others call, or it depends on a
core system that must not be overloaded. Also whenever a batch and an interactive load share
a resource.

**Default components.** A limit at the edge per caller, a policy per client or contract, a
queue or backpressure mechanism toward the protected system, a defined response when the
limit is reached, and visibility of who is being limited.

**Usual failure modes.** Limits set without knowing normal load, so they either never trigger
or throttle legitimate use on day one. No differentiation between a partner under contract
and an anonymous caller. The limit protecting our system while the core system behind it
still gets flooded. Rejection with no useful signal, so the caller retries immediately and
makes it worse. No alerting, so throttling is discovered through a complaint.

**Ask the client.** Who calls this, under which agreement, and what have they been promised.
What load does the core system behind it actually tolerate. What should happen when the limit
is hit, reject or queue, and who is told. Is there an existing gateway that already does
this.

**What a blank-page design misses.** That the limit is a commercial and contractual object
before it is a technical one. The existing gateway. The batch job that will hit the same
interface at 03:00 with no rate limit at all.

---

## P8 Payment-like and value-bearing flows

**When it applies.** Money, entitlements, claims payments, benefits, settlements, meter-based
billing. Anything where a wrong or duplicated record has a direct financial consequence.

**Default components.** An idempotency key per instruction, a state machine per instruction
with explicit terminal states, a reconciliation against the counterparty, a correction path
that reverses rather than deletes, a dual-control step where the amount or the risk warrants
it, and a complete audit trail per P5.

**Usual failure modes.** Retry without idempotency, producing a double payment, which is the
most expensive single defect in this whole index. Correction implemented as an update, so the
history is lost. No reconciliation, so a discrepancy is found by the counterparty. Failure
states not modelled, so an instruction sits in limbo with no owner. Rounding and currency
handling decided by a developer. Cut-off times and value dates treated as display logic.

**Ask the client.** What the counterparty is and what the settlement rhythm is. What the
reconciliation process is today and who runs it. What limits require dual control, and what
is the current rule. How corrections are handled today, and what the accounting treatment is.
What the cut-off and value-date rules are. What the regulatory frame requires to be provable.

**What a blank-page design misses.** Reconciliation as a designed, staffed process. Dual
control. Correction as a reversal with history. Cut-off and value dates as domain rules. That
the finance and accounting side of the client is a stakeholder in the design, not a consumer
of it.

---

## Maintenance

Owner: the skill. A page changes when a mandate proves it wrong or incomplete, not on a
schedule. A new page is added only when a real mandate needed one, and it follows the same
five headings. Keep every page under roughly forty lines, a page nobody finishes reading has
no effect on any design.
