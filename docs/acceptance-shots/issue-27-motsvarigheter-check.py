#!/usr/bin/env python3
"""Check that every concept file keeps its correspondences under `## Motsvarigheter`, in the fixed order.

Ticket #27 (the catalogue splits a concept's remark into the general part and the
correspondences in specifications). This script is the proof that can fail: it reads
sentence by sentence, not file by file.

Run:  python3 -I docs/acceptance-shots/issue-27-motsvarigheter-check.py <store folder>

It reads every `<store folder>/concepts/*.md`, prints one line per breach and a total
line, and exits 1 on any breach, 0 on none.

Three rules:

1. Outside `## Motsvarigheter` and `## Exempel` (the remark, and any text under no
   heading), every sentence that names a specification needs that specification named
   somewhere under `## Motsvarigheter` in the same file, or must itself point there by
   containing the word "Motsvarigheter". The title line and the definition line are not
   read.
2. Under `## Motsvarigheter`, take each sentence's first-named specification. The
   sequence of those must never go backwards in the fixed order: archimate, aris, bacm,
   bmm, bpmn, cmmn, dmn, sbvr, sdmn, uml, vdml, pm3, togaf, edgy, then the two canvases.
   A sentence naming no specification (a lone "Beslut 22.") is skipped.
   How a comparative aside is told from the sentence's own specification: a name
   directly after a comparing word ("som", "liksom", "likt", "i likhet med", "till
   skillnad från", "jämfört med") is an aside and does not count. The sentence's
   specification is the first name that is not an aside; a sentence with only asides is
   skipped.
3. `## Motsvarigheter` occurs at most once, comes after `## Anmärkning` and before
   `## Exempel`, and is never empty.
"""

import re
import sys
from pathlib import Path

# The fixed order, with the names each specification goes by in the text.
# Acronyms are matched case-sensitively so that "SDMN" is not read as "DMN".
ORDER = [
    ("archimate", r"ArchiMate"),
    ("aris", r"\bARIS\b"),
    ("bacm", r"\bBACM\b|Business Architecture Core Metamodel"),
    ("bmm", r"\bBMM\b|Business Motivation Model"),
    ("bpmn", r"\bBPMN\b"),
    ("cmmn", r"\bCMMN\b"),
    ("dmn", r"\bDMN\b|Decision Model and Notation"),
    ("sbvr", r"\bSBVR\b"),
    ("sdmn", r"\bSDMN\b"),
    ("uml", r"\bUML\b|Unified Modeling Language"),
    ("vdml", r"\bVDML\b|Value Delivery Modeling Language"),
    ("pm3", r"\bpm3\b"),
    ("togaf", r"\bTOGAF\b"),
    ("edgy", r"\bEDGY\b"),
    # The canvases are in no list of the ticket's; they stand last (the first worker's rule).
    ("canvas", r"Value Proposition Canvas|Business Model Canvas"),
]
RANK = {name: number for number, (name, _) in enumerate(ORDER)}
PATTERNS = [(name, re.compile(pattern)) for name, pattern in ORDER]
# Specifications rule 1 asks about: all but the canvases.
RULE_ONE = {name for name, _ in ORDER if name != "canvas"}

COMPARING = re.compile(
    r"(?:\b(?:som|liksom|likt)|i likhet med|till skillnad från|jämfört med)\s+(?:\w+\s+){0,2}?$",
    re.IGNORECASE,
)
ABBREVIATIONS = ("t.ex.", "bl.a.", "m.m.", "d.v.s.", "o.s.v.", "m.fl.", "s.k.", "dvs.", "ca.", "jfr.", "resp.", "ev.", "inkl.", "osv.")
WIKILINK = re.compile(r"\[\[[^\]]*\]\]")
HEADING = re.compile(r"^## (.+?)\s*$")


def split_file(text):
    """Return the body (front matter removed) as a list of lines."""
    lines = text.splitlines()
    if lines and lines[0].strip() == "---":
        for number in range(1, len(lines)):
            if lines[number].strip() == "---":
                return lines[number + 1 :]
    return lines


def sections(body):
    """Return [(heading or None, [paragraph text, ...])] in file order.

    The title line (`# C-nnn ...`) and the definition line are left out: the
    definition names things as definitions do and is not the remark.
    """
    result = [(None, [])]
    paragraph = []

    def flush():
        if paragraph:
            result[-1][1].append(" ".join(paragraph))
            paragraph.clear()

    for line in body:
        match = HEADING.match(line)
        if match:
            flush()
            result.append((match.group(1), []))
        elif line.startswith("# ") or line.startswith("**Definition:**"):
            flush()
        elif not line.strip():
            flush()
        else:
            paragraph.append(line.strip())
    flush()
    return result


def sentences(paragraphs):
    found = []
    for paragraph in paragraphs:
        text = WIKILINK.sub(" ", paragraph)
        for abbreviation in ABBREVIATIONS:
            text = text.replace(abbreviation, abbreviation.replace(".", "․"))
        for piece in re.split(r"(?<=[.!?])\s+(?=[A-ZÅÄÖ«\"(\[])", text):
            piece = piece.replace("․", ".").strip()
            if piece:
                found.append(piece)
    return found


def mentions(sentence):
    """All (position, name, is_aside) for the specifications a sentence names, in text order."""
    found = []
    for name, pattern in PATTERNS:
        for match in pattern.finditer(sentence):
            aside = bool(COMPARING.search(sentence[: match.start()]))
            found.append((match.start(), name, aside))
    return sorted(found)


def named(sentence):
    return {name for _, name, _ in mentions(sentence)}


def own_specification(sentence):
    for _, name, aside in mentions(sentence):
        if not aside:
            return name
    return None


def check_file(path):
    breaches = []
    parts = sections(split_file(path.read_text(encoding="utf-8")))
    headings = [heading for heading, _ in parts if heading is not None]
    correspondence = [paragraphs for heading, paragraphs in parts if heading == "Motsvarigheter"]

    # Rule 3: placement and emptiness.
    if headings.count("Motsvarigheter") > 1:
        breaches.append("rubriken Motsvarigheter står mer än en gång")
    if correspondence:
        if not correspondence[0]:
            breaches.append("rubriken Motsvarigheter är tom")
        at = headings.index("Motsvarigheter")
        if "Anmärkning" not in headings or headings.index("Anmärkning") > at:
            breaches.append("Motsvarigheter står inte efter Anmärkning")
        if "Exempel" in headings and headings.index("Exempel") < at:
            breaches.append("Motsvarigheter står efter Exempel")

    under = sentences([p for paragraphs in correspondence for p in paragraphs])
    under_named = set()
    for sentence in under:
        under_named |= named(sentence)

    # Rule 1: a specification named outside Motsvarigheter and Exempel needs a counterpart.
    for heading, paragraphs in parts:
        if heading in ("Motsvarigheter", "Exempel"):
            continue
        for sentence in sentences(paragraphs):
            if "Motsvarigheter" in sentence:
                continue
            for name in sorted(named(sentence) & RULE_ONE):
                if name not in under_named:
                    place = heading or "utan rubrik"
                    breaches.append(f"{name} nämns i {place} utan motsvarighet under Motsvarigheter: {sentence[:90]}")

    # Rule 2: the first-named specification of each sentence never goes backwards.
    last = None
    for sentence in under:
        name = own_specification(sentence)
        if name is None:
            continue
        if last is not None and RANK[name] < RANK[last]:
            breaches.append(f"ordningen går bakåt, {name} efter {last}: {sentence[:90]}")
        last = name
    return breaches


def main(argv):
    if len(argv) != 2:
        print("usage: python3 -I issue-27-motsvarigheter-check.py <store folder>", file=sys.stderr)
        return 2
    concepts = sorted((Path(argv[1]) / "concepts").glob("*.md"))
    if not concepts:
        print(f"no concept files under {argv[1]}/concepts", file=sys.stderr)
        return 2
    total = 0
    files = 0
    for path in concepts:
        breaches = check_file(path)
        files += bool(breaches)
        for breach in breaches:
            print(f"{path.name}: {breach}")
        total += len(breaches)
    print(f"total: {total} breaches in {files} of {len(concepts)} files")
    return 1 if total else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
