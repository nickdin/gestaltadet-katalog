"""Prov för ärende #179: texterna följer beslut 58, 60 och 62.

Körs från lagrets rot: python3 docs/acceptance-shots/issue-179-klassen.py

Provet läser begreppen, sidan Informationskartläggning, de två exemplen och ritningen över stegen. Det faller, med
slutkod 1 och raden FALLER, när en text säger något som besluten har tagit bort, eller när en text som besluten
kräver saknas.
"""

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
CONCEPTS = ROOT / "concepts"
PAGE = ROOT / "docs" / "informationskartlaggning.md"
AGENCY = ROOT / "docs" / "exempel" / "myndigheten-for-foreningsstod.md"
HOUSING = ROOT / "docs" / "exempel" / "brinkstadsbostader.md"
STEP_DRAWING = ROOT / "layout" / "Exempel" / "Informationskartläggning steg.drawio.svg"

# Det besluten har tagit bort: mönstret och vad det betyder att det står kvar.
REMOVED = [
    (r"fyra klasser", "säger fyra klasser (beslut 58: två klasser och två krav)"),
    (r"Av klassningen bär kartan|bär (bara )?nivån i varje klass", "säger att kartan bär nivån (beslut 58)"),
    (r"lagret räknar med den", "säger att lagret räknar med klassen (beslut 58)"),
    (r"klassen ärvs nedåt|ger klassen nedåt", "säger att klassen ärvs nedåt i lagret (beslut 58 och 60)"),
    (r"med ägare och klass", "säger att kartan börjar med en klass på området (beslut 58)"),
    (r"känsligare än varje företrädare", "säger att mängden gör klassen högre (beslut 58)"),
    (r"kan bli högre än delarna", "säger att mängden gör klassen högre (beslut 58)"),
    (r"sammanställningseffekten", "säger att en sammanställning klassas högre för att den är en samling (beslut 58)"),
    (r"oftast högre", "säger att en sammanställning oftast klassas högre (beslut 58)"),
    (r"SKR:s KLASSA", "hänvisar till SKR:s KLASSA för spårbarheten (#179)"),
    (r"en ägare och en klass, och klarar", "har huvudfrågan från före beslut 58"),
    (r"[Hh]ög tillgänglighet som behov", "sätter tillgängligheten på objektet (beslut 58)"),
    # Baslinje hör till Nulägesarkitektur (C-057); om klassningen heter det grundnivå (beslut 60).
    (r"[Bb]aslinje.*klass|klass.*[Bb]aslinje", "säger baslinje om klassningen (beslut 60)"),
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
    (
        PAGE,
        "säger beslutet bara att grundnivån räcker, utan analys",
        "tillägget om vad klassningsbeslutet säger för ett objekt med grundnivån (beslut 60)",
    ),
    (PAGE, "målarkitekturen", "att det genomgången kräver blir krav i målarkitekturen (beslut 58)"),
    (
        STEP_DRAWING,
        "Har informationsägaren tagit ställning till varje objekt på kartan, själv eller genom området",
        "huvudfrågan i informationssäkerheten, som sidan (beslut 60)",
    ),
    (CONCEPTS / "C-060 Informationsobjekt.md", "Klassen är konfidentialitet och riktighet", "de två klasserna (beslut 58)"),
    (CONCEPTS / "C-162 Sammanställning.md", "Mängden gör aldrig klassen högre", "provet om mängden (beslut 58)"),
    (CONCEPTS / "C-165 Lagringsyta.md", "fyra delar", "ytans krav i fyra delar (beslut 58)"),
    (CONCEPTS / "C-166 Informationstillgång.md", "två klasser och två krav", "två klasser och två krav (beslut 58)"),
    (
        CONCEPTS / "C-167 Informationsägare.md",
        "utan att känna den framtida användningen",
        "klassningen utan den framtida användningen (beslut 58)",
    ),
    (CONCEPTS / "C-198 Informationsområde.md", "grundnivån", "meningen om grundnivån (beslut 60)"),
    (CONCEPTS / "C-101 har åtkomst till.md", "C-165 Lagringsyta", "lagringsytan som mål (beslut 62)"),
    (CONCEPTS / "C-206 Processägare.md", "spårbarhet", "processägarens två krav (beslut 58)"),
    (CONCEPTS / "C-168 Behandling.md", "spårbarhet", "kraven på paret (beslut 58)"),
    (AGENCY, "samma konfidentialitet som Företrädare", "förteckningen över företrädare utan högre klass (beslut 58)"),
    (AGENCY, "Tillgängligheten är ett krav på behandlingen", "tillgängligheten per behandling (beslut 58)"),
    (HOUSING, "inom en timme", "kravet på paret i Åtgärda en felanmälan (beslut 58)"),
    (HOUSING, "står i nuläget bara om bolaget redan hanterar", "när Utsatt roll står i nuläget (beslut 58)"),
]


def shown(path: Path) -> str:
    """Filens sökväg från lagrets rot, som den står i en rad om ett fel."""
    return str(path.relative_to(ROOT))


def main() -> int:
    failures = []
    scanned = [*sorted(CONCEPTS.glob("*.md")), PAGE, AGENCY, HOUSING, STEP_DRAWING]
    for path in scanned:
        if not path.exists():
            failures.append(f"{shown(path)}: filen saknas")
            continue
        for number, line in enumerate(path.read_text(encoding="utf-8").splitlines(), start=1):
            for pattern, meaning in REMOVED:
                if re.search(pattern, line):
                    failures.append(f"{shown(path)} rad {number}: {meaning}")
    for path, text, meaning in REQUIRED:
        if path.exists() and text not in path.read_text(encoding="utf-8"):
            failures.append(f"{shown(path)}: saknar {meaning}")
    if failures:
        print("FALLER:")
        for failure in failures:
            print(f"- {failure}")
        return 1
    print(f"Lästa filer: {len(scanned)}. Borttagna formuleringar: 0 träffar på {len(REMOVED)} mönster.")
    print(f"Krävda texter: {len(REQUIRED)} av {len(REQUIRED)} finns.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
