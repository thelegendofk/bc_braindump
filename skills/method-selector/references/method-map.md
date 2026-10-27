# Method Map

The only truth of the selector. If a skill changes, adjust it only here. The
table points to the skills, it does not repeat their content.

## Method inventory

What each skill owns, in one sentence. The details are in the respective SKILL.md.

| Skill | Owns | Phase |
|---|---|---|
| engagement-setup | Folder skeleton and AGENTS.md, the operating brief | Setup, first of all |
| method-selector | Method choice and order, this plan | Selection |
| shipley-proposal | Proposal strategy, win themes, compliance matrix, storyboard | Proposal |
| inacta-proposal-writing | Proposal narrative, structure, action titles, business case | Proposal |
| inacta-proposal-deck | Proposal in the Inacta house style (PPTX) | Proposal, production |
| inacta-ea-method | SCN and CBM, target architecture, gap, roadmap, governance | EA |
| solution-architecture-lite | Building-level solution design for a system the mandate actually designs: scope sheet, one blueprint, capacity sheet, trade-off memo. Internal only | Proposal or EA, before the client-facing prose |
| ict-audit | Assessment of an existing solution, question catalogue, audit report | Audit |
| ipm-project-setup | Project setup per IPM, charter, definition, risk log | Project |
| premortem-review | Assumed failure reconstructed: failure paths, fragile assumptions, smallest interventions. Optional, for high stakes and hard to reverse work | Review, ahead of the substance reviews |
| publication-boundary-review | Publication boundary, provenance leaks, internal sources and reasoning, metadata | Review, before the send check |
| tech-executive-review | Review from the buyer view, buying verdict | Review |
| red-team-review | Adversarial review, make it defendable | Review |
| engagement-package-export | Handover package as ZIP | Export |
| project-knowledge-bundle | Make the corpus queryable as a Claude project | Export |
| rag-corpus-export | RAG corpus ready for embedding | Export |
| human-writing | Language and voice smoothing for prose | Production |
| docx, pptx, pdf, xlsx | Document, deck, PDF, spreadsheet production | Production |
| drawio-diagrams-enhanced | Diagrams, as PNG before embedding | Production |
| method-onboarding, skill-creator | Turn a method into a skill | Meta |

## Reference methods without a skill of their own

Name them as a light addition when they fit. Not a mandatory step.

| Reference method | Fits for | Location |
|---|---|---|
| Wardley Mapping | Build versus buy, positioning, legacy versus modern, strategy | 99 Methods/Mapping (Primer plus Cheat Sheet) |
| Design Thinking | A real discovery or co-creation phase with the client in the room | 99 Methods/Design Thinking |
| Consultative / Challenger Sales | Business development, first contact, opportunity work | 99 Methods/Consultative Selling |

## Standard chains per engagement type

Order from left to right. Review and export apply to almost every
client-facing deliverable.

### Proposal / pitch (RFP or proactive)

```
engagement-setup -> method-selector
  -> shipley-proposal (only for an RFP: strategy, compliance, storyboard)
  -> solution-architecture-lite (only if the offer designs a software system)
  -> inacta-proposal-writing (narrative, structure, action titles)
  -> inacta-proposal-deck (deck) or docx (Word) + human-writing
  -> premortem-review (optional, on the first complete draft)
  -> tech-executive-review -> red-team-review
  -> publication-boundary-review (release gate, before the final client document)
  -> engagement-package-export
```

For a proactive proposal without an RFP keep the shipley-proposal light (only win themes
and discriminators), the rest stays the same.

### EA / architecture (target picture, strategy)

```
engagement-setup -> method-selector
  -> inacta-ea-method (SCN/CBM, AS-IS and TO-BE, gap, roadmap, governance)
  -> solution-architecture-lite (only for the systems the mandate actually designs)
  -> docx or inacta-proposal-deck + drawio-diagrams-enhanced + human-writing
  -> premortem-review (optional, on the first complete draft)
  -> tech-executive-review -> red-team-review
  -> publication-boundary-review (release gate)
  -> engagement-package-export or project-knowledge-bundle
```

Addition: Wardley Mapping, when build versus buy or positioning is in the
foreground.

### Audit / assessment (check an existing solution)

```
engagement-setup -> method-selector
  -> ict-audit (package completeness, interviews, audit report)
  -> docx (report) or inacta-proposal-deck + human-writing
  -> premortem-review (optional, on the first complete draft)
  -> tech-executive-review -> red-team-review
  -> publication-boundary-review (release gate)
  -> engagement-package-export
```

### Project setup / delivery

```
engagement-setup -> method-selector
  -> ipm-project-setup (charter, definition, risk log, team charter)
  -> running deliverables with docx, pptx, xlsx, drawio as needed
  -> review before every client-facing version
```

### Research / study

```
engagement-setup -> method-selector
  -> research and analysis (web, sources, existing corpus)
  -> docx or inacta-proposal-deck + human-writing
  -> premortem-review (optional, on the first complete draft)
  -> tech-executive-review -> red-team-review
  -> publication-boundary-review (release gate)
  -> project-knowledge-bundle or rag-corpus-export, if the corpus lives on
```

### Internal project

```
engagement-setup (leave out the admin part) -> method-selector
  -> depending on the content EA, audit or project setup
  -> light review, often only red-team-review
```

## Short decision aid on overlap

- **EA method or ICT audit?** Designing a target picture and a roadmap is EA. Assessing an
  existing solution is audit. Both together are possible, then audit
  first (fact base), then EA (target picture).
- **EA method or solution-architecture-lite?** The EA method is the city plan: capabilities,
  target picture, gaps, a transition roadmap for the enterprise. solution-architecture-lite
  designs one building: the components, the flows, the load and the two or three trade-offs of
  a single system. Pull it only when the mandate actually designs a distributed software
  system, and it produces internal artifacts that the proposal skills consume. It refuses to
  run for EA-only, process-only, package implementation and pure discovery mandates, and it
  stops at the offer. Once the mandate is won and the system is built, the arc42 skills take
  over.
- **Shipley or proposal writing?** Both for an RFP, one after the other. Shipley
  does strategy and compliance, proposal writing does text and structure. For
  a very small proactive proposal, proposal writing alone is often enough.
- **Proposal deck or docx?** Deck for a pitch and a presentation, docx for formal
  proposals and reports. Both are possible, same content.
- **Which export?** Handover to a human is engagement-package-export. As
  queryable knowledge it is project-knowledge-bundle. For an own retrieval system
  it is rag-corpus-export.
- **Premortem or red team?** red-team-review defends a document against a critical reader on
  our own side. premortem-review assumes the purpose was missed and reconstructs why, which
  also covers what happens after the document is accepted. Order: premortem first, while a
  substantial change is still cheap, then the substance reviews. Pull the premortem
  deliberately, for high stakes, for a hard to reverse decision, or when the subject is a
  planned course of action with no document yet. It is not a step every deliverable takes.
- **Review, which one first?** tech-executive-review checks whether the client buys or
  acts. red-team-review then makes it defendable. Order: first the buyer view,
  then the defence. publication-boundary-review comes after both, because a rewrite in a
  substance review can introduce a fresh provenance leak. It is the last content review
  before send-prep, and for a final client document it runs in Release gate mode.

## When no method fits

If no method skill fits, say so openly and recommend the generic production and
review skills. If a new method need keeps coming back, point to
`method-onboarding`, to turn it into a skill.
