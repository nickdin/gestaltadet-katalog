"""Prov för ärende #171: ingen mening i de fjorton filerna använder fynd som om det vore ett begrepp.

Körs från lagrets rot: python3 docs/acceptance-shots/issue-171-fynd.py

Provet läser de tretton begreppen och sidan om lagarna som ärendet räknar upp. Det skriver ut varje mening med
ordet fynd, i vilken form som helst, med sin fil. Beslut 54 säger att fynd inte är något begrepp: ordet får bara
stå kvar där det betyder något som någon har hittat. En sådan mening står i KEPT nedan med skälet. Varje annan
mening med ordet fäller provet, med slutkod 1 och raden FALLER.

Provet skriver också ut varje mening med ordet avvikelse i samma filer. Avvikelse (C-213) är rätt ord bara där en
organisation har fastställt en princip, så listan ska gå att jämföra mellan basen och grenen.
"""

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]

# De fjorton filerna i ärendet.
FILES = [
    "concepts/C-209 Ansvar.md",
    "concepts/C-220 Centralisering.md",
    "concepts/C-008 Verksamhetsdomän.md",
    "concepts/C-012 Initiativ.md",
    "concepts/C-055 Lösning.md",
    "concepts/C-156 Forum.md",
    "concepts/C-189 Mandat.md",
    "concepts/C-211 Koppling.md",
    "concepts/C-214 Delegation.md",
    "concepts/C-219 Komplexitet.md",
    "concepts/C-217 Samordning.md",
    "concepts/C-215 Produktionsstyrning.md",
    "concepts/C-218 Granskning.md",
    "docs/lagar.md",
]

# Meningar där ordet bara betyder något som någon har hittat: meningen ordagrant och skälet.
KEPT: dict[str, str] = {}

WORD = re.compile(r"\bfynd\w*", re.IGNORECASE)
DEVIATION = re.compile(r"\bavvikelse\w*", re.IGNORECASE)
SENTENCE_END = re.compile(r"(?<=[.?!])\s+")


def sentences(path: Path) -> list[str]:
    """Return the sentences of a file, one paragraph line at a time."""
    found = []
    for line in path.read_text(encoding="utf-8").splitlines():
        found.extend(part.strip() for part in SENTENCE_END.split(line) if part.strip())
    return found


def main() -> int:
    with_word = []
    with_deviation = []
    for name in FILES:
        for sentence in sentences(ROOT / name):
            if WORD.search(sentence):
                with_word.append((name, sentence))
            if DEVIATION.search(sentence):
                with_deviation.append((name, sentence))

    print(f"Meningar med ordet fynd i de fjorton filerna: {len(with_word)}")
    failures = []
    for name, sentence in with_word:
        reason = KEPT.get(sentence)
        if reason is None:
            print(f"- {name}: {sentence}")
            failures.append((name, sentence))
        else:
            print(f"- {name}: {sentence}\n  står kvar: {reason}")

    print(f"\nMeningar med ordet avvikelse i de fjorton filerna: {len(with_deviation)}")
    for name, sentence in with_deviation:
        print(f"- {name}: {sentence}")

    if failures:
        print(f"\nFALLER: {len(failures)} meningar använder fynd utan att stå bland dem som får stå kvar")
        return 1
    print("\nHÅLLER: ingen mening använder fynd som om det vore ett begrepp")
    return 0


if __name__ == "__main__":
    sys.exit(main())
