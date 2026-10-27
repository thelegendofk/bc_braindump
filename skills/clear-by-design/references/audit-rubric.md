# Audit rubric

Six dimensions, each 1 to 5. The weighted total score shows how far the document is from
"lands and gives pleasure". More important than the number are the concrete fixes. First look
at it (export deck or formatted report to PDF), then rate.

Scale per dimension: 1 blocks understanding, 2 costs the reader effort, 3 works, 4 is good,
5 is clear and pleasant.

Weighting (sum 100):
- Structure and story 25
- Clarity and cognitive load 20
- Visual design and hierarchy 20
- Data integrity 10
- Impact and behavioral design 15
- Fluency and reading pleasure 10

Total score = sum (dimension score divided by 5, times weight). Result 0 to 100.

---

## 1. Structure and story (weight 25)

Checks: Does the answer stand at the front (answer-first, pyramid principle)? Is there a core
message that carries through? Does every slide or every section carry exactly one message, as
a sentence? Does a recognizable bracket lead from the starting position to the next step?

- 5: After the first slide or the first paragraph the reader knows the result, every unit has
  a sentence message, the arc is clear.
- Typical fix at 2: rebuild the management summary answer-first, rewrite topic titles into
  assertion sentences (Assertion-Evidence), split slides with two messages.

## 2. Clarity and cognitive load (weight 20)

Checks: Does everything visible contribute to the message (Coherence)? Does text stand close
to the image it belongs to (Spatial Contiguity)? Is the same content not served twice in the
same channel (Redundancy)? Is the material divided into digestible units (Segmenting)?

- 5: Nothing superfluous, label at the object, clear portions, one thought per paragraph.
- Typical fix at 2: delete decoration and side information, reduce full-text slides to the
  core message plus image, split long blocks into sections with intermediate messages.

## 3. Visual design and hierarchy (weight 20)

Checks: Is there a clear first point of focus per page? Do proximity and similarity group what
belongs together (Gestalt)? Is there enough white space? Is the alignment calm, the grid
consistent? Does a signal guide the eye to what matters (Signaling)?

- 5: The eye knows at once where it starts, groups are clear through distance, calm grid, one
  deliberate accent.
- Typical fix at 2: replace separating lines and boxes with white space, align elements to the
  grid, set a hierarchy through size and weight, one accent instead of five.

## 4. Data integrity (weight 10)

Checks: Does every chart make one point, and does it stand next to it as a sentence? Chartjunk
out, data ink up (Tufte)? Axes and titles labelled, eye guided (Knaflic)? Axes honest, no
distorted area?

- 5: Plain charts, one point per chart as a sentence, honest axes, calm rest.
- Typical fix at 2: remove 3D, gradients and superfluous grids, highlight the important
  element, set the chart title as a message, start the axis at zero where needed.

## 5. Impact and behavioral design (weight 15)

Checks: Is the recommended option designed as the obvious choice (default, framing)? Is real
evidence for authority and social proof visible (Cialdini)? Is every call to action freed from
sludge, one clear easy next step? Honest, without dark pattern?

- 5: The recommendation is the easy choice, evidence stands where the decision falls, the next
  step is one step, everything transparent.
- Typical fix at 2: mark the recommendation visually as the default, bring a reference or a
  piece of evidence next to the decision, reduce a multi-stage request to one clear step.

## 6. Fluency and reading pleasure (weight 10)

Checks: Is the typesetting readable (font size, contrast, spacing)? Is the language clear and
fitting for the addressee (short sentences, simple for non-native readers)? Does the whole
feel clean and pleasant (Aesthetic-Usability)?

- 5: Pleasant to read, high contrast, calm typography, clear language, it feels light.
- Typical fix at 2: enlarge the font and raise the contrast, open up line and paragraph
  spacing, split endless sentences, bring ornate or too many typefaces back to one calm
  hierarchy.

---

## Output format of the audit

1. **Score table.** Six dimensions, score 1 to 5, short reason, total score 0 to 100.
2. **Overall judgement.** One paragraph: does it land, does it give pleasure, where does it
   lose the reader.
3. **The most effective fixes first.** Three to five, each with location (slide, page),
   finding and concrete proposal. Sorted by expected impact, not by order in the document.
4. **No rewrite.** Proposals for the authoring team, no silent rewriting.

Note: This rubric rates impact and reading pleasure. Facts and the buying judgement belong to
red-team-review and tech-executive-review, the mechanical readiness for delivery to send-prep.
