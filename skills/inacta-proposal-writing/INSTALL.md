# Install: inacta-proposal-writing

A method skill in the Inacta skills library for the writing and structure layer of a proposal. It turns
an agreed win strategy and section plan into a persuasive, client-first draft:
Situation-Complication-Resolution narrative, action titles, a quantified business
case, tiered pricing, social proof, and a risks table.

## Contents

```
inacta-proposal-writing/
  SKILL.md                              the workflow and operating principles
  references/
    narrative-scr-pyramid.md            SCR arc and the Minto pyramid principle
    action-titles.md                    how to write full-sentence action titles
    proposal-structure.md               client-first section order, adapt per mandate
    persuasion-elements.md              business case, social proof, why us, pricing, risks
    proposal-checklist.md               pre-submission quality gate
  scripts/
    check_proposal.py                   heuristic draft checker (.md and .docx)
```

## Install

This is a standard Agent Skills package: a folder with `SKILL.md` at its root plus
`references/`, `scripts/` and `assets/` where needed. It carries no runtime specific
manifest, so it installs the same way on any compatible runtime.

- **Any runtime**: copy the `inacta-proposal-writing/` folder into the directory your runtime scans for
  skills, keeping the folder layout intact.
- **Claude (Cowork or Claude Code)**: import the zipped `inacta-proposal-writing.skill` file in the skill
  settings, or place the folder in the skills source directory.
- **ChatGPT / OpenAI**: install the same folder through that runtime's skill import. The
  exact click path is runtime specific, see the library `README.md`.

Triggers:
proposal drafting, "proposal", "offer", "Offerte", "Angebot",
   "executive summary", "action titles", "SCR", "pyramid principle", "why us",
   "pricing options", "proposal structure", and the German equivalents.

Alternatively, drop the `inacta-proposal-writing/` folder into the skills
source directory next to the other method skills.

## Where it fits in the lifecycle

```
engagement-setup   (folder plus AGENTS.md, work type "Proposal / pitch")
   -> shipley-proposal        (win strategy, win themes, compliance matrix, storyboard)
   -> inacta-proposal-writing (this skill: narrative, structure, action titles, business case)
   -> inacta-proposal-deck (house look) or docx (Word), plus human-writing (voice)
   -> tech-executive-review, then red-team-review
   -> engagement-package-export
```

Two entry points: after `shipley-proposal` for an RFP response, or directly after
`engagement-setup` for a proactive proposal with no RFP to triage.

## Separation from the neighboring skills

This skill owns only the writing and structure layer. It does not rebuild:

- Win strategy, win themes, compliance matrix, storyboard, which are
  `shipley-proposal`.
- The house visual style, brand, and slide layout, which is `inacta-proposal-deck`.
- Sentence-level voice and de-AI-ing, which is `human-writing`.
- Folder setup, review, and export, which belong to other skills in the library.

## Using the checker

```
python3 scripts/check_proposal.py "<path-to>/draft.md"
python3 scripts/check_proposal.py "<path-to>/draft.docx" --max-words 4000
```

It flags label-style titles, thin quantified impact, a firm-first opening, and
length over target. It is a heuristic aid, not a gate, and it never edits the file.

## Optional follow-up (opt-in, not done automatically)

To chain automatically, add a next-step hint from `shipley-proposal` (at its Step 5
draft handoff) pointing to `inacta-proposal-writing`, and a note in
`inacta-proposal-deck` to reuse this skill's action titles. Both are one-line edits,
do them only if you want the auto-chain.

## Source basis

Built from `99 Methods/New_Proposal_Method/Inacta_Proposal_Improvements.docx`
(February 2026), an analysis of more than 20 past proposals benchmarked against
top-tier consulting practice (Minto pyramid, SCR, action titles, client-first
ordering), plus the proposal templates and estimate sheets in the same folder. The
skill is engagement-generic and carries no fixed client facts or company boilerplate,
those are read per mandate.
