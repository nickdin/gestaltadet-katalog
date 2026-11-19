"""Prov för ärende #200: arbetsflödet Publicera katalogen hämtar hela historiken.

Sidan Historik på gestaltadet.se läses ur lagrets commits. Steget actions/checkout
hämtar bara den senaste commiten om det inte får fetch-depth: 0, och då har sidan
en enda rad. Provet läser .github/workflows/publicera.yml och faller om steget
actions/checkout saknar fetch-depth: 0.

Körs från lagrets rot: python3 docs/acceptance-shots/issue-200-historik.py
Slutkod 0 och HÅLLER när steget hämtar hela historiken, annars 1 och FALLER.
"""

import re
import sys
from pathlib import Path

WORKFLOW = Path(".github/workflows/publicera.yml")


def checkout_step(text: str) -> str:
    """Returnerar raderna för steget actions/checkout, fram till nästa steg."""
    lines = text.splitlines()
    for i, line in enumerate(lines):
        if re.match(r"\s*- uses: actions/checkout@", line):
            step = [line]
            for following in lines[i + 1:]:
                if re.match(r"\s*- ", following) or not following.strip():
                    break
                step.append(following)
            return "\n".join(step)
    return ""


def main() -> int:
    step = checkout_step(WORKFLOW.read_text(encoding="utf-8"))
    print("Steget actions/checkout:")
    print(step or "(saknas)")
    if re.search(r"^\s*fetch-depth:\s*0\s*$", step, re.MULTILINE):
        print("HÅLLER: steget hämtar hela historiken (fetch-depth: 0).")
        return 0
    print("FALLER: steget hämtar bara den senaste commiten, så sidan Historik får en rad.")
    return 1


if __name__ == "__main__":
    sys.exit(main())
