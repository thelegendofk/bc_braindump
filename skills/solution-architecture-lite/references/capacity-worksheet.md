# Capacity worksheet

The back-of-the-envelope numbers, built as a working instrument that recalculates, not as
prose that goes stale.

File: `reference/<Client>_<Engagement>_Capacity_<YYYY-MM-DD>.xlsx`. Internal. Built with the
`xlsx` skill, per the house rule of 31.08.2026 that anything filtered, sorted or carried
forward becomes Excel.

---

## The one rule that matters

**Assumptions are typed, results are computed.** Every displayed number is either an input
cell with a source, or a formula over input cells. Nothing in between. When the client says
in week three that it is 40'000 users and not 25'000, one cell changes and the sheet is
correct again.

A capacity sheet with typed-in results is a screenshot of one afternoon's thinking. It will
be wrong before the offer is submitted, and nobody will notice.

## Sheet layout

Four sheets. Not more.

### Sheet 1, `Annahmen` (assumptions)

The only sheet with typed numbers. Input cells blue, per the house xlsx convention.

| Col | Content |
|---|---|
| ID | A1, A2, ... referenced by the formulas |
| Grösse | what it is |
| Wert | the number, blue input cell |
| Einheit | the unit, always filled |
| Quelle | RFP section with date, meeting with date, client document, or the marker **TBC** |
| Status | `sourced` or `TBC` |
| Bemerkung | what would change it |

Typical rows: users total, users concurrent at peak, transactions per day, documents per
year, average object size, retention period, growth per year, peak factor, working hours per
day, replication factor, overhead factor for indexes and metadata.

**The peak factor is an assumption, not a constant.** State it, source it where possible, and
say what it is derived from, for example "Monday morning batch plus counter opening hours".
A peak factor carried in from another mandate is TBC until this client confirms it.

### Sheet 2, `Berechnung` (computation)

No typed numbers at all. Every cell is a formula over `Annahmen`.

| Group | Rows |
|---|---|
| Load | requests per second, average. Requests per second, peak. Concurrent sessions. |
| Write volume | records or documents per day, per year. Bytes per day, per year. |
| Storage | raw per year. With replication. With index and metadata overhead. Over the retention period. |
| Bandwidth | ingress and egress, average and peak, in Mbit/s. |
| Growth | each of the above at the end of the contract term. |

Show the formula intent in a `Formel` column in words, for example "transactions per day
divided by working seconds per day, times peak factor". A reviewer who cannot read the
formula bar can still check the logic.

**Label every unit in its own column.** Requests per second, gigabytes per year, megabits
per second, concurrent users. An unlabelled number in a client-bound document is a defect,
and the unit error is the most common one in this whole method.

### Sheet 3, `Kosten und Ablage` (cost and residency)

Only where the mandate needs it, which for Swiss regulated clients is most of the time.

- Compute-, storage- and transfer-relevant quantities carried over from `Berechnung`.
- Unit prices only where a real price exists: a client framework contract, a current
  provider price list with its capture date, an internal rate. No list price from memory.
- Data residency rows: which data class, which jurisdiction it may be stored in, which
  jurisdiction it may be processed in, and the source of the rule. For Swiss personal data
  the Inacta ISMS conduct rules apply, questions go to the CISO, and processing outside Switzerland needs
  written client approval.
- Where a price is not available, the row says TBC and the offer says the cost is not yet
  quantified. It does not say a number.

### Sheet 4, `Legende` (legend, assumptions and sources)

Per the house xlsx convention. It carries:

- what blue and black cells mean,
- the full source list with capture dates,
- the sentence that states what this sheet is: an estimate under the stated assumptions, as
  of the stated date, not a measurement,
- the list of open questions the TBC rows generate.

## Performance and hardware figures

**Never carry a latency, throughput-per-node or hardware figure in from a textbook, a
training-set memory or an older estimate.** Any performance number that appears in this sheet
comes from one of three places:

1. a measurement in the client's own estate, with what was measured and when,
2. a vendor or provider statement, with the document and its date,
3. our own test, with the setup described.

If none of the three exists, the sheet does not carry the number. It carries a TBC row and
an open question. Sizing figures age badly, and a defended-sounding number from an unknown
year is worse than an honest gap, because it cannot be corrected by anyone who reads it
later.

## Worked shape, not worked numbers

The arithmetic is deliberately shown without example values, because example values get
copied.

```
requests per second, average  =  transactions per day / seconds in the working day
requests per second, peak     =  requests per second, average * peak factor
bytes per day                 =  objects per day * average object size
storage per year, raw         =  bytes per day * 365
storage, provisioned          =  storage per year, raw * retention years
                                 * replication factor * (1 + overhead factor)
bandwidth peak, Mbit/s        =  requests per second, peak * average payload bytes * 8 / 10^6
concurrent sessions           =  users concurrent at peak (from assumptions, not derived)
```

Every one of those is a formula cell. None of them is typed.

## Where the sheet is used and where it is not

**Used for:** the sizing statements in the solution section, the infrastructure line of the
estimate, the scaling ladder conversation, and the question of whether the design holds at
the end of the contract term.

**Not used for:** the price. Effort and price come from the calculation instruments in
`99 Methods/Kalkulation & Offerten/`. The capacity sheet is an input to the estimate, it is
not an estimate.

**Never used as:** a fact table in a client document. Where a figure from this sheet appears
in an offer, it appears with its assumption attached, in the weakest defensible form. "Under
the assumptions in section X, the design carries about N transactions per day" is
defensible. "The system handles N transactions per day" is a commitment we have not tested.

## Quality check before moving on

- Sheet `Berechnung` contains no typed number.
- Every row in `Annahmen` has a source or the status TBC.
- Every computed row has a unit.
- The peak factor is stated and its basis is named.
- No performance or hardware figure appears without one of the three sources above.
- The legend sheet says the sheet is an estimate, and carries the date.
- No formula errors when handed over. Run the xlsx skill's own check.
