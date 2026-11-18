"""Prov för ärende #179: texterna följer beslut 58, 60 och 62.

Körs från lagrets rot: python3 docs/acceptance-shots/issue-179-klassen.py

Provet läser begreppen, sidan Informationskartläggning och de två exemplen. Det faller, med slutkod 1 och raden
FALLER, när en text säger något som besluten har tagit bort, eller när en text som besluten kräver saknas.
"""

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
PAGE = ROOT / "docs" / "informationskartlaggning.md"
EXAMPLES = sorted((ROOT / "docs" / "exempel").glob("*.md"))
CONCEPTS = sorted((ROOT / "concepts").glob("*.md"))

# Det besluten har tagit bort: mönstret och vad det betyder att det står kvar.
REMOVED = [
    (r"fyra klasser", "säger fyra klasser (beslut 58: två klasser och två krav)"),
    (r"Av klassningen bär kartan", "säger att kartan bär nivån (beslut 58)"),
    (r"lagret räknar med den", "säger att lagret räknar med klassen (beslut 58)"),
    (r"klassen ärvs nedåt|ger klassen nedåt", "säger att klassen ärvs nedåt i lagret (beslut 58 och 60)"),
    (r"känsligare än varje företrädare", "säger att mängden gör klassen högre (beslut 58)"),
    (r"sammanställningseffekten", "säger att en sammanställning klassas högre för att den är en samling (beslut 58)"),
    (r"oftast högre", "säger att en sammanställning oftast klassas högre (beslut 58)"),
    (r"SKR:s KLASSA", "hänvisar till SKR:s KLASSA för spårbarheten (#179)"),
    (r"en ägare och en klass, och klarar", "har huvudfrågan från före beslut 58"),
    (r"[Hh]ög tillgänglighet som behov", "sätter tillgängligheten på objektet (beslut 58)"),
]

# Det besluten kräver: filen, texten som ska stå där och varför.
REQUIRED = [
    (
        PAGE,
        "Har informationsägaren tagit ställning till varje objekt på kartan, själv eller genom området, "
        "och klarar varje lagringsyta det förteckningen kräver?",
        "huvudfrågan i informationssäkerheten (beslut 60)",
    ),
    (
        PAGE,
        "Vilka objekt har grundnivån genom sitt område, och håller den för vart och ett?",
        "följdfrågan om grundnivån (beslut 60)",
    ),
    (
        PAGE,
        "Vilka objekt på lagringsytan går att koppla ihop till en ny uppgift?",
        "följdfrågan om kopplingen (beslut 58)",
    ),
    (PAGE, "Vilka beteenden har åtkomst till lagringsytan", "följdfrågan om vilka beteenden som når ytan (beslut 62)"),
    (PAGE, "grundnivån räcker", "tillägget om vad klassningsbeslutet säger för ett objekt med grundnivån (beslut 60)"),
    (PAGE, "målarkitekturen", "att det genomgången kräver blir krav i målarkitekturen (beslut 58)"),
    (ROOT / "concepts" / "C-198 Informationsområde.md", "grundnivån", "meningen om grundnivån (beslut 60)"),
    (ROOT / "concepts" / "C-165 Lagringsyta.md", "fyra delar", "ytans krav i fyra delar (beslut 58)"),
    (ROOT / "concepts" / "C-101 har åtkomst till.md", "C-165 Lagringsyta", "lagringsytan som mål (beslut 62)"),
    (ROOT / "concepts" / "C-206 Processägare.md", "spårbarhet", "processägarens två krav (beslut 58)"),
    (ROOT / "concepts" / "C-168 Behandling.md", "spårbarhet", "kraven på paret (beslut 58)"),
]


def main() -> int:
    failures = []
    scanned = [*CONCEPTS, PAGE, *EXAMPLES]
    for path in scanned:
        if not path.exists():
            failures.append(f"{path.relative_to(ROOT)}: filen saknas")
            continue
        for number, line in enumerate(path.read_text(encoding="utf-8").splitlines(), start=1):
            for pattern, meaning in REMOVED:
                if re.search(pattern, line):
                    failures.append(f"{path.relative_to(ROOT)} rad {number}: {meaning}")
            # Baslinje hör till Nulägesarkitektur (C-057); om klassningen heter det grundnivå (beslut 60).
            if re.search(r"[Bb]aslinje", line) and re.search(r"klass", line):
                failures.append(f"{path.relative_to(ROOT)} rad {number}: säger baslinje om klassningen (beslut 60)")
    for path, text, meaning in REQUIRED:
        if not path.exists() or text not in path.read_text(encoding="utf-8"):
            failures.append(f"{path.relative_to(ROOT)}: saknar {meaning}")
    if failures:
        print("FALLER:")
        for failure in failures:
            print(f"- {failure}")
        return 1
    print(f"Lästa filer: {len(scanned)}. Borttagna formuleringar: 0 träffar på {len(REMOVED) + 1} mönster.")
    print(f"Krävda texter: {len(REQUIRED)} av {len(REQUIRED)} finns.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
