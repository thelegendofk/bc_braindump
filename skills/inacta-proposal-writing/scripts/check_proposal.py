#!/usr/bin/env python3
"""Heuristic proposal draft checker.

Scans a proposal draft and flags likely issues against the method:
  1. Label-style headings instead of full-sentence action titles.
  2. Little or no quantified impact (few numbers, percentages, or money).
  3. A firm-first opening (company introduction before the client situation).
  4. Main body longer than a target.

This is an aid for the author, not a gate. It is heuristic, it can be wrong, and it
never edits the file. Read the flags, use judgement.

Supports Markdown (.md) and Word (.docx). For .docx it reads the document text and
treats the built-in heading styles as headings.

Usage:
    python3 check_proposal.py <draft.md|.docx> [--max-words 4000]

No em-dashes. Swiss spelling where German is used (ss not the sharp s).
"""

import argparse
import os
import re
import sys
import zipfile

LABEL_WORDS = {
    "introduction", "executive summary", "summary", "overview", "situation",
    "context", "background", "solution", "our solution", "approach", "methodology",
    "delivery", "project plan", "plan", "timeline", "roadmap", "team", "the team",
    "commercial", "commercial offer", "pricing", "price", "offer", "why us",
    "why inacta", "about us", "about", "company", "references", "appendix",
    "appendices", "risks", "conclusion", "next steps", "scope",
    # German labels
    "einleitung", "zusammenfassung", "uebersicht", "uebersicht", "ausgangslage",
    "loesung", "loesungsvorschlag", "vorgehen", "vorgehensvorschlag", "projektplan",
    "team", "kommerzielles", "angebot", "preis", "warum", "ueber uns", "referenzen",
    "anhang", "risiken", "fazit", "naechste schritte",
}

VERB_HINT = re.compile(r"\b\w+(s|es|ed|t|en|ert|iert)\b", re.IGNORECASE)
NUMBER_HINT = re.compile(r"(\d+\s?%|\bCHF\b|\bEUR\b|\bUSD\b|\d+[\s'.,]?\d*\s?(days|day|weeks|week|months|month|Tage|Tagen|Wochen|Monate|Monaten)|\b\d{2,}\b)")


def read_md(path):
    with open(path, encoding="utf-8") as f:
        text = f.read()
    headings = [(m.group(2).strip())
                for m in re.finditer(r"^(#{1,4})\s+(.*)$", text, re.MULTILINE)]
    return text, headings


def read_docx(path):
    ns = "{http://schemas.openxmlformats.org/wordprocessingml/2006/main}"
    try:
        z = zipfile.ZipFile(path)
        xml = z.read("word/document.xml").decode("utf-8", "ignore")
    except Exception as e:
        print("error: cannot read docx: %s" % e, file=sys.stderr)
        sys.exit(1)
    # crude paragraph split, keep style names
    paras = re.findall(r"<w:p[ >].*?</w:p>", xml, re.DOTALL)
    text_parts = []
    headings = []
    for p in paras:
        runs = re.findall(r"<w:t[^>]*>(.*?)</w:t>", p, re.DOTALL)
        ptext = re.sub(r"<[^>]+>", "", "".join(runs)).strip()
        if not ptext:
            continue
        text_parts.append(ptext)
        style = re.search(r'w:pStyle w:val="([^"]*)"', p)
        if style and "eading" in style.group(1):
            headings.append(ptext)
    return "\n".join(text_parts), headings


def is_label(heading):
    h = heading.strip().rstrip(":").lower()
    h = re.sub(r"^\d+[\.\)]?\s*", "", h)  # strip leading numbering
    if h in LABEL_WORDS:
        return True
    # short heading with no verb and no number is probably a label
    words = h.split()
    if len(words) <= 4 and not VERB_HINT.search(h) and not NUMBER_HINT.search(heading):
        return True
    return False


def main():
    ap = argparse.ArgumentParser(description="Heuristic proposal draft checker.")
    ap.add_argument("draft", help="Path to the draft (.md or .docx)")
    ap.add_argument("--max-words", type=int, default=4000,
                    help="Target maximum word count for the main body (default 4000)")
    args = ap.parse_args()

    if not os.path.isfile(args.draft):
        print("error: file not found: %s" % args.draft, file=sys.stderr)
        sys.exit(1)

    ext = os.path.splitext(args.draft)[1].lower()
    if ext == ".md":
        text, headings = read_md(args.draft)
    elif ext == ".docx":
        text, headings = read_docx(args.draft)
    else:
        print("error: unsupported file type %s, use .md or .docx" % ext, file=sys.stderr)
        sys.exit(1)

    print("Proposal check for: %s\n" % os.path.basename(args.draft))
    flags = 0

    # 1. Action titles
    labels = [h for h in headings if is_label(h)]
    print("1. Action titles")
    if not headings:
        print("   note: no headings detected, cannot judge titles.")
    elif labels:
        flags += 1
        print("   flag: %d of %d headings look like labels, not action titles:"
              % (len(labels), len(headings)))
        for h in labels[:12]:
            print("        - %s" % h)
        if len(labels) > 12:
            print("        ... and %d more" % (len(labels) - 12))
    else:
        print("   ok: headings read as full-sentence titles.")

    # 2. Quantified impact
    print("\n2. Quantified impact")
    nums = NUMBER_HINT.findall(text)
    if len(nums) < 3:
        flags += 1
        print("   flag: very few quantified figures found (%d). Add measurable "
              "impact (%%, CHF, days)." % len(nums))
    else:
        print("   ok: %d quantified figures found." % len(nums))

    # 3. Firm-first opening
    print("\n3. Client-first ordering")
    low = text.lower()
    firm_markers = ["about us", "who we are", "das sind wir", "ueber uns", "company profile", "unternehmensprofil"]
    client_markers = ["your situation", "understanding your", "ihre ausgangslage", "ihre situation", "situation", "ausgangslage", "your challenges", "ihre herausforderungen"]
    firm_pos = min([low.find(m) for m in firm_markers if low.find(m) != -1] or [10 ** 9])
    client_pos = min([low.find(m) for m in client_markers if low.find(m) != -1] or [10 ** 9])
    first_third = max(1, len(low) // 3)
    # only a concern if the firm intro sits early (first third) and ahead of the client
    if firm_pos != 10 ** 9 and firm_pos < first_third and firm_pos < client_pos:
        flags += 1
        print("   flag: a firm introduction appears early, before the client "
              "situation. Move the client's situation first.")
    else:
        print("   ok: no firm-first opening detected (heuristic).")

    # 4. Length
    print("\n4. Length")
    wc = len(text.split())
    if wc > args.max_words:
        flags += 1
        print("   flag: about %d words in the body, over the target of %d. Push "
              "detail to appendices." % (wc, args.max_words))
    else:
        print("   ok: about %d words, within the target of %d." % (wc, args.max_words))

    print("\n----")
    if flags:
        print("%d area(s) flagged. These are hints, not verdicts, use judgement." % flags)
    else:
        print("No heuristic flags. Still run the review skills before sending.")


if __name__ == "__main__":
    main()
