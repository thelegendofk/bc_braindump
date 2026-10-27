---
name: inacta-proposal-writing
description: >-
  Proposal writing and narrative method for a set-up engagement. Turns an agreed win strategy
  and section plan into a persuasive, well structured client proposal: a
  Situation-Complication-Resolution narrative, full-sentence action titles, a client-first
  section order, a quantified business case, tiered pricing, social proof, and a risks and
  mitigation table. Triggers: "proposal", "offer", "Offerte", "Angebot", "pitch", "executive
  summary", "action titles", "SCR", "SCQA", "pyramid principle", "Minto", "why us", "business
  case in a proposal", "pricing options", "proposal structure", "Vorgehensvorschlag",
  "Angebotsstruktur". Engagement-generic: reads the client structure, boilerplate, and style
  guide per mandate, does not scaffold folders or run reviews. Boundary: owns the writing and
  structure layer only. If no win strategy and no compliance matrix exist yet, use
  shipley-proposal first. For slides use inacta-proposal-deck, for the sentence-level voice
  human-writing.
---

# Inacta Proposal Writing

## Purpose

Make a proposal persuasive and easy to decide on. This skill owns the writing and
structure layer of the proposal lifecycle: how the argument is ordered, how each
section leads, how value is quantified, and how the price is framed. It turns an
agreed win strategy and section plan into a client-ready draft.

It does not decide the win strategy, and it does not review. Those jobs belong to
other skills in the library. It also does not own the house visual style, that is
`inacta-proposal-deck`.

Stance: a proposal writer trained on top-tier consulting practice (Minto pyramid,
Situation-Complication-Resolution) who has seen many technically strong proposals
lose because they told the vendor's story, not the client's. Every section leads
with the point. The client's world comes first. Numbers beat adjectives.

## Where this sits in the lifecycle

```
engagement-setup   (folder plus AGENTS.md, work type "Proposal / pitch")
  -> shipley-proposal   (win strategy, win themes, compliance matrix, storyboard)
  -> solution-architecture-lite   (only if the offer designs a software system)
  -> inacta-proposal-writing   (this skill: narrative, structure, action titles, business case)
  -> inacta-proposal-deck (house look) or docx (Word), plus human-writing (voice)
  -> tech-executive-review (buyer view), then red-team-review
  -> engagement-package-export
```

Two entry points:

- **After shipley-proposal**, for an RFP response. Shipley has produced the win
  strategy, the compliance matrix, and the storyboard. This skill writes the draft.
- **Directly after engagement-setup**, for a proactive proposal where there is no
  RFP to triage. Shipley's compliance matrix does not apply, but the narrative and
  structure rules here still do. In that case, capture the win themes and
  discriminators lightly first (Shipley step 2 gives the format), then write.

If the engagement folder does not exist, stop and point the user to
`engagement-setup`. Do not create the skeleton here.

## What this skill keeps and skips

Keeps: the narrative framework (SCR and the pyramid principle), action titles, the
client-first section order, the business case and ROI, social proof, tiered
pricing, the risks and mitigation table, and conciseness.

Skips on purpose: win strategy and win themes, the compliance matrix, and the
storyboard (all `shipley-proposal`). The house visual style, brand, and slide
layout (`inacta-proposal-deck`). Sentence-level voice and de-AI-ing
(`human-writing`). Folder setup (`engagement-setup`). Review
(`tech-executive-review`, `red-team-review`). Export (`engagement-package-export`).

The single most common failure here is duplicating Shipley. If you find yourself
writing win themes or a compliance matrix, stop, that is Shipley's job. This skill
starts from those outputs and writes.

## Step 0: Context intake (always first)

Do not flood the main context. Delegate multi-file reading to a sub-agent if the runtime offers one, otherwise do a separate focused reading pass first. Read:

- **AGENTS.md** of the engagement: client, goal, deliverable type (Word or deck),
  guardrails, and the avoid list. Settings, do not change them.
- **Style guide** if present (for example `reference/Stilrichtlinie*.md`).
- **Shipley outputs** in `reference/` if this follows Shipley: win strategy, win
  themes, value propositions, storyboard, compliance matrix.
- **Solution architecture artifacts** in `reference/` if the offer designs a software
  system: the blueprint and the trade-off memo from `solution-architecture-lite`. They carry
  the components, the flows, the markings existing, extend and new, and the two or three
  trade-offs. Write the solution approach section from them. Do not design here, and do not
  repeat a capacity figure without its assumption. If they are missing and the offer really
  designs a system, run `solution-architecture-lite` first.
- **The RFP and client input** in `brief/` if present. Input, never edit.
- **Any house structure, boilerplate, or template** the mandate points to. The
  client-facing structure and any standing company facts are read per mandate, this
  skill does not carry them.

If a needed input is missing, ask. Never invent a requirement, a number, a
reference client, or a deadline.

## Step 1: Choose the narrative spine (SCR)

Structure the whole proposal, and the executive summary in particular, as a
Situation-Complication-Resolution arc (or SCQA, Situation-Complication-Question-
Answer). This is the Minto pyramid applied to a proposal. Detail and templates in
`references/narrative-scr-pyramid.md`.

- **Situation**: the client's current state, stated so they recognize it as their
  own.
- **Complication**: why this is urgent and costly now. This creates the reason to
  act.
- **Resolution**: what you propose, and the outcome it delivers.

Write the resolution to answer the complication directly. If a proposed element
does not answer the complication, it is a candidate to cut.

## Step 2: Order the proposal client-first

Reorder so the client's world comes before your firm. A generic client-first flow,
adapted to the RFP or the house template per mandate:

1. Cover and a personal cover letter
2. Executive summary (the SCR arc)
3. Understanding your situation (client challenges and goals)
4. Our solution approach
5. Delivery plan and roadmap
6. Your team
7. Why us (differentiators, plus a short firm intro as proof)
8. Commercial offer and next steps
9. Appendices (detailed CVs, case studies, technical deep-dives)

The company introduction moves after the solution, where it reads as proof of
capability, not as a preamble. More in `references/proposal-structure.md`. If the
RFP mandates a structure, follow it, and apply the client-first idea within each
section instead.

## Step 3: Write action titles

Every section heading and every slide title is a full sentence that states the
takeaway, not a label. The test: a reader who reads only the titles understands the
whole proposal. Rules and many before-and-after examples in
`references/action-titles.md`.

- Not "Executive summary", but "A modular approach cuts claims processing time and
  keeps full regulatory compliance."
- Not "Commercial offer", but "Phased pricing ties investment to milestones,
  starting at a defined first phase."

This is the highest-leverage single change in the whole method. Do it everywhere.

## Step 4: Make the case with evidence

Apply the persuasion elements, detailed in `references/persuasion-elements.md`.
Each is optional per mandate, but each lifts win rate:

- **Business case and ROI**: add a short business case that estimates measurable
  impact (cost saved, time reduced, risk lowered, revenue enabled). Put numbers in
  the action titles. Use before-and-after where you have it.
- **Social proof**: embed one or two-sentence mini case studies inside the solution
  section, each with industry, challenge, solution, and a measurable outcome. Add a
  references page. Only use real, cleared references, never invent one.
- **Why us**: one concentrated section with three or four concrete differentiators,
  each a bold claim plus evidence. Position by what makes your approach different,
  without naming competitors.
- **Tiered pricing**: offer two or three options (for example Essential,
  Recommended, Premium), and anchor the middle as recommended. Give the client a
  spectrum, not a binary yes or no.
- **Risks and mitigation**: a short table of three to five key risks, each with
  likelihood, impact, and your mitigation, framed as challenges you have
  anticipated.

Never invent facts. A number, a saving, a reference client, or a certification that
is not in an input is an open question, not an assumption. Flag it for the client
or for the account lead.

## Step 4b: Settle the AI cost model and the recording logic

For any proposal that involves AI-assisted development, two things must be stated, and
both belong in the commercial part of the document:

- **How time is recorded.** Only active work on the client's solution is charged,
  including the steering and review of automated steps. Longer or unattended runs are
  not charged as working time. This is a firm rule, not a negotiating position.
- **How tool, model and token cost reach the price.** Exactly one of three variants per
  proposal: a premium hourly rate, a fixed price per result, or a separate position.
  Never two of them for the same work, that is charging the same cost twice.

The decision, the comparison of the three variants, the coverage check for the premium
rate, the placement in the document and the answers to the usual objections are in
`references/ki-kostenmodell.md`. The approved clause wording, German and English, comes
from `tender-document-library`, do not write your own version of it.

The choice of variant belongs to the project lead and has to be documented before the
project starts. If it has not been made, ask. Do not pick one silently, and do not put a
guideline figure from the reference into a client document, the number comes from the
mandate's own calculation.

## Step 5: Keep it concise

Lead with the message, push detail to appendices. Apply the pyramid principle
inside every section: conclusion first, then support. Target a short main body (for
example 12 to 15 pages for a Word proposal, 15 to 20 slides for a deck), with
depth in the appendix. Exact limits come from the RFP or the mandate.

## Step 6: Draft handoff

Write into `deliverables/` only after the structure and the action titles are
agreed.

- Word proposal: use the `docx` skill for structure, `human-writing` for voice.
- Deck: use the `inacta-proposal-deck` skill for the house style, still
  `human-writing` for the text, and reuse the action titles from Step 3.
- Diagrams: `drawio-diagrams-enhanced`, export to PNG before embedding. Every
  figure gets an action caption, a full sentence, not a label.

Optional check: run `scripts/check_proposal.py <draft.md|.docx>` for a quick,
heuristic scan that flags label-style titles, missing quantified impact, a
firm-first opening, and length over target. It is an aid, not a gate, and it never
edits the file.

## Step 7: Review handoff

Do not review here. Hand off to `tech-executive-review` for the buyer read (does
the client believe it, want it, and take the next step), then `red-team-review` to
make it defensible. Loop accepted findings back into the draft, then use
`engagement-package-export`.

## Operating principles

- Client first, firm second. The client should feel understood before they learn
  about you.
- Lead with the point. Every section and every title states its conclusion first.
- Numbers beat adjectives. Quantify impact wherever a real number exists.
- Never invent facts. A reference client, a saving, or a certification not in an
  input is an open question.
- Do not duplicate Shipley. Start from the win strategy and storyboard, do not
  rebuild them.
- Every figure earns its caption. Captions state the conclusion, not the label.
- Ghost only what you know. Position against a competing approach without naming or
  inventing a competitor.
- Internal stays internal. Win strategy and the business case working notes do not
  leak into the client draft unless promoted on purpose.
- No em-dashes anywhere, use commas. German text uses Swiss spelling (ss not ß)
  and real umlauts ä, ö, ü. English text is written for non-native readers: short
  sentences, plain words.

## Parameterization per engagement

Fixed: the narrative framework, the action-title rule, the client-first idea, the
principles. Read or adapt per mandate: the AGENTS.md settings, the style guide, the
client-facing structure and any house boilerplate, the deliverable type (Word or
deck), the page or slide limits, and the naming convention. Defaults follow Swiss
High German and Inacta conventions.

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
- Scripts in `scripts/` need Python 3. Dependencies: none, standard library only. If a dependency is missing, say
  so and take the manual path, rather than skipping the step silently.
