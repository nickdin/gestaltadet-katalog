"""Prov för ärende #144: beslut 30 säger hur ramen runt ett informationsobjekt läses.

Körs från lagrets rot: python3 docs/acceptance-shots/issue-144-beslut-30.py

Provet läser beslut 30 i docs/adr/. Det faller, med slutkod 1 och raden FALLER, när beslutet fortfarande säger
att områdets ram märks för hand i ritningen, eller när någon av de meningar som ärendet kräver saknas.
"""

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]

# Det ärendet tar bort: texten och vad det betyder att den står kvar.
REMOVED = [
    ("märks `composed_of` i ritningen", "säger att områdets ram märks för hand i ritningen"),
    ("tills interlingua kan läsa en ram efter typ", "väntar på att interlingua ska kunna läsa en ram efter typ"),
]

# Det ärendet kräver: texten och vilken följd den bär.
REQUIRED = [
    (
        "Informationsobjekt (`C-060`) anger att dess ram läses som består av (`C-062`)",
        "följd 1, att Informationsobjekt (C-060) anger hur dess ram läses",
    ),
    (
        "Relationen går från ramen till rutan inuti, som består av (`C-062`) och aggregerar (`C-100`) redan definierar.",
        "följd 2, att relationen går från ramen till rutan inuti",
    ),
    (
        "Varje ram runt ett informationsobjekt läses som består av, också ett grovt objekt runt sina förfinade.",
        "följd 3, att varje ram runt ett informationsobjekt läses som består av (C-062)",
    ),
    ("En sammanställning (`C-162`) ritas inte som ram.", "följd 3, att en sammanställning (C-162) inte ritas som ram"),
    ("Det är levererat med interlingua #954.", "hänvisningen till interlingua #954 i sista avsnittet"),
    ("Beslutat av Nicklas 2 november 2026", "beslutets första rad om vem som beslutade"),
]


def main() -> int:
    decisions = sorted((ROOT / "docs" / "adr").glob("0030-*.md"))
    if len(decisions) != 1:
        print(f"FALLER: docs/adr/ har {len(decisions)} filer som börjar på 0030-, inte en.")
        return 1
    text = decisions[0].read_text(encoding="utf-8")
    failures = [f"beslut 30 {meaning}" for phrase, meaning in REMOVED if phrase in text]
    failures += [f"beslut 30 saknar {meaning}" for phrase, meaning in REQUIRED if phrase not in text]
    if failures:
        print("FALLER:")
        for failure in failures:
            print(f"- {failure}")
        return 1
    print(f"Borttagna formuleringar: 0 träffar på {len(REMOVED)}. Krävda texter: {len(REQUIRED)} av {len(REQUIRED)} finns.")
    print("HÅLLER: beslut 30 säger att Informationsobjekt (C-060) anger att dess ram läses som består av (C-062).")
    return 0


if __name__ == "__main__":
    sys.exit(main())
