---
name: clear-by-design
description: >-
  Makes slide decks and reports clear, understandable and pleasant to read, based on research
  from cognitive psychology and behavioral economics (Cognitive Load, Mayer, Processing
  Fluency, Gestalt, Tufte, Knaflic, Assertion-Evidence, pyramid principle, Kahneman, Cialdini,
  Nudge and Sludge). Two modes: Build supports the creation of a new deck or report, Audit
  rates an existing document across six dimensions with concrete fixes. Decks and reports, DE
  and EN. Triggers: "clear by design", "mach das klarer", "besser lesbar", "Deck verbessern",
  "Bericht aufräumen", "storytelling", "make this clearer", "improve this
  deck", "polish this report". Also use when someone has a document reviewed for impact.
  Boundary: rates clarity, cognitive load and information design, not the substance. For
  substance and attack surface red-team-review, for the buyer view tech-executive-review, for
  overspecificity weakest-claim-check, for the mechanical final check send-prep.
---

# Clear by Design

## Purpose

Make a document clear, understandable and pleasant. Clear means the message is there at one
glance. Understandable means the reader carries little cognitive load. Pleasant means the
reading feels light, and light processing demonstrably raises comprehension, trust and
agreement (Processing Fluency). This is the "why it lands" layer, not the brand look and not
the final check.

Basic idea from behavioral economics: most readers decide first with System 1, fast and
effort-averse. Every unnecessary hurdle (Sludge) costs attention and agreement, every useful
relief (good choice design) wins them. A good deck or a good report is choice architecture:
it makes the important path the easy path.

## Place in the sequence

- `clear-by-design` makes sure that structure, message and design land and give pleasure.
- `inacta-proposal-deck` delivers the visual house brand (navy, Inacta pink, fonts, cards).
  This skill says what belongs on the slide and why, that one says how it looks.
- `human-writing` governs the prose voice (articles, posts).
- `red-team-review` and `tech-executive-review` challenge the substance and the buying
  judgement.
- `send-prep` is the mechanical final check before sending.

Sequence: the substance stands (reviews), then `clear-by-design` for impact and reading
pleasure, then `send-prep` as the last pass. This skill does not argue the facts again and
does not change the house brand.

## Two modes

### Build mode (support a new document)

When creating a deck or a report, apply the principles from `references/principles.md` and
take the patterns from `references/patterns.md` as a template. Procedure:

1. **Addressee and one core message first.** Who reads it, what should they think or do
   afterwards, what is the one message. Audience trumps all else. Without this one message no
   layout.
2. **Answer-first structure.** The answer first, then the reasoning (pyramid principle,
   BLUF). After the first paragraph or the first slide the reader should know the result.
3. **One message per slide, one per section.** Slide title as a complete assertion sentence
   (Assertion-Evidence), below it the visual piece of evidence, not a bullet list.
4. **Lower the cognitive load.** Only what carries the message (Coherence). Text and matching
   image close together (Spatial Contiguity). Do not read out and show the same thing at the
   same time (Redundancy). Guide the eye with one signal (Signaling).
5. **Data honest and calm.** Chartjunk out, data ink up (Tufte), one point per chart, guide
   the eye to what matters, label axes and titles (Knaflic).
6. **Behavioral design, honest.** Design the recommended option as the obvious choice
   (default), make evidence for authority and social proof visible (Cialdini), free every call
   to action from sludge (one step, clear next step).
7. **Reading pleasure.** Generous white space, clear typographic hierarchy, calm alignment.
   Beautiful feels lighter and lighter feels more credible (Aesthetic-Usability, Fluency).

### Audit mode (rate an existing document)

Go through the six dimensions from `references/audit-rubric.md`, rate each 1 to 5, form the
weighted total score, and name one concrete fix with a location per weak point. Procedure:

1. **Context.** Type (deck or report), language, addressee, one core message. For engagement
   work read the AGENTS.md of the engagement.
2. **Look at it, do not only read it.** For decks and formatted reports export the document to
   PDF or images and look at it. Design, white space and hierarchy are seen only by the eye,
   not by the text.
3. **Rate six dimensions** (structure and story, clarity and cognitive load, visual design and
   hierarchy, data integrity, impact and behavioral design, fluency and reading pleasure).
4. **Report.** Score per dimension, overall judgement, then the three to five most effective
   fixes first. No rewrite, but prioritized, workable proposals.

## Limits and ethics

Behavioral design here is clarity and honest relief, not manipulation. Nudges are allowed if
they are transparent and in the reader's interest. No dark pattern, no hiding of
disadvantages, no invented social proof. Lowering sludge means taking work off the reader, not
pushing them.

## Style rules for the skill outputs

The deliverable language follows the engagement, not this file. Read it from the operating
brief (`AGENTS.md`). These rules apply in both languages: no em-dashes, use a comma instead.
German texts use the umlauts ä, ö, ü, Ä, Ö, Ü, never the ASCII replacements ae, oe, ue, and
use ss instead of ß (Swiss standard German). English texts are written for non-native readers,
with short sentences and no idioms. State things directly, avoid the formulaic contrast
pattern. Use client terms in the spelling held in `client-glossary`. Reports and accompanying
texts stay short and concrete, location instead of generality.

## Portability

- Runs on any Agent-Skills-compatible runtime. No runtime-specific tool is needed. Where this
  skill says to ask the user, use the structured question mechanism of the runtime, otherwise
  ask in the chat. Where it says to hand over a file, use the file output of the runtime.
- Operating brief of the engagement: look for `AGENTS.md`, otherwise `AGENT.md`, otherwise
  `CLAUDE.md` (legacy, still valid). Use the first file found. Never rename or overwrite an
  existing file silently. If it is missing completely, run `engagement-setup` first.
- A persistent project folder is expected. If it is missing, work with the files of the
  running session, keep the same structure in the result and say openly that nothing was
  persisted. Do not pretend that persistent files exist.
