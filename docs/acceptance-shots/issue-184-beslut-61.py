"""Prov för ärende #184: begreppen och sidan Informationskartläggning följer beslut 61.

Körs från lagrets rot: python3 docs/acceptance-shots/issue-184-beslut-61.py

Provet läser de fem begreppen och sidan som ärendet räknar upp. Varje ruta i ärendet har en eller flera texter som
ska stå i rutans fil. Provet faller, med slutkod 1 och raden FALLER, när en sådan text saknas, när tillägget om
återställningstiden står före slutet av listan i Lagringsyta (C-165), eller när meningen i steg 2 på sidan har ändrats.

Provet prövar bara att de 18 krävda texterna står i sina filer. Varje text söks i hela filen, inte i ett visst
stycke eller steg: texten om återställningstiden godtas var den än står på sidan, inte bara i steg 4. Provet läser
inte texten runt de krävda texterna, och prövar alltså inte att den följer beslut 61.
"""

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
CONCEPTS = ROOT / "concepts"
BEHAVIOUR = CONCEPTS / "C-157 Verksamhetsbeteende.md"
PROCESS_OWNER = CONCEPTS / "C-206 Processägare.md"
STORAGE = CONCEPTS / "C-165 Lagringsyta.md"
ASSET = CONCEPTS / "C-166 Informationstillgång.md"
APPLICATION = CONCEPTS / "C-071 Applikation.md"
PAGE = ROOT / "docs" / "informationskartlaggning.md"

TWO_MEASURES = "hur länge beteendet klarar sig utan objektet, och hur mycket av objektet som får gå förlorat"

# Det beslut 61 kräver: filen, texten som ska stå där och vilken del av rutan texten uppfyller.
REQUIRED = [
    (BEHAVIOUR, "Processägaren ställer ett kontinuitetskrav på beteendet", "processägaren ställer kontinuitetskravet"),
    (BEHAVIOUR, "den längsta tid beteendet får stå still", "kravet är den längsta tid beteendet får stå still"),
    (BEHAVIOUR, "gäller värsta fallet", "värsta fallet gäller"),
    (
        BEHAVIOUR,
        "Nuläget delar beteendet först när verksamheten utför delen för sig",
        "nuläget delar beteendet först när verksamheten utför delen för sig",
    ),
    (PROCESS_OWNER, "Processägaren ställer också kontinuitetskravet", "processägaren ställer kontinuitetskravet"),
    (
        PROCESS_OWNER,
        "Reservrutinen är en bärare ([[C-016 Bärare]])",
        "processägaren fastställer reservrutinen som en bärare (C-016)",
    ),
    (PROCESS_OWNER, "Avvägningen mellan två beteenden följer beslut 50", "avvägningen följer beslut 50"),
    (
        PROCESS_OWNER,
        "Prioritetsordningen är en sådan princip",
        "prioritetsordningen är en princip (C-018)",
    ),
    (PROCESS_OWNER, "[[C-018 Princip]]", "länken till princip (C-018)"),
    (STORAGE, "Tillgängligheten läses i två mått", "tillgängligheten läses i två mått"),
    (
        STORAGE,
        "Den härleds ur kontinuitetskravet",
        "återställningstiden härleds ur kontinuitetskravet",
    ),
    (STORAGE, "En reservrutin kan skapa en ny lagringsyta", "en reservrutin kan skapa en ny lagringsyta"),
    (
        STORAGE,
        "Pärmen måste klara konfidentialiteten för Hyresgäst",
        "den nya lagringsytan måste klara objektets konfidentialitet",
    ),
    (ASSET, "Tillgängligheten har två mått: " + TWO_MEASURES, "tillgänglighetens två mått"),
    (
        APPLICATION,
        "Återställningstiden är ett krav ([[C-021 Krav]]) på applikationen",
        "återställningstiden är ett krav (C-021) på applikationen",
    ),
    (PAGE, "Frågan räknar in återställningstiden", "frågan i steg 4 räknar in återställningstiden"),
    (
        PAGE,
        "Kontinuiteten gäller beteendet och alla dess resurser",
        "kontinuiteten gäller beteendet och alla dess resurser",
    ),
    (
        PAGE,
        "Informationssäkerheten läser den del som rör information och applikationer",
        "informationssäkerheten läser delen om information och applikationer",
    ),
]

# Det som ska stå orört: filen, texten och varför.
KEPT = [
    (
        PAGE,
        "Arkitekten fångar också vilka lagringsytor beteendet använder. "
        "På kartan har beteendet åtkomst till var och en av dem.",
        "meningen i steg 2, som en ritning ska återge ordagrant",
    ),
    (STORAGE, "Lagringsytans krav läses fram i fyra delar:", "listan i fyra delar (beslut 58)"),
]

LIST_INTRO = "Lagringsytans krav läses fram i fyra delar:"


def shown(path: Path) -> str:
    """Filens sökväg från lagrets rot, som den står i en rad om ett fel."""
    return str(path.relative_to(ROOT))


def storage_list_failures() -> list[str]:
    """Fel i var Lagringsyta (C-165) säger återställningstiden: listan har fyra punkter, och ordet står först efter dem."""
    lines = STORAGE.read_text(encoding="utf-8").splitlines()
    if LIST_INTRO not in lines:
        return []
    start = lines.index(LIST_INTRO)
    items = []
    for line in lines[start + 1 :]:
        if line.startswith("- "):
            items.append(line)
        elif line.strip() and items:
            break
    failures = []
    if len(items) != 4:
        failures.append(f"{shown(STORAGE)}: listan över lagringsytans krav har {len(items)} punkter, inte fyra")
    before_end = lines[: start + 1] + items
    if any("återställningstid" in line.lower() for line in before_end):
        failures.append(f"{shown(STORAGE)}: återställningstiden står i listan eller före den, inte efter")
    return failures


def main() -> int:
    failures = []
    # Varje krävd text söks i hela filen. Provet prövar att texten står där, inte var i filen den står.
    for path, text, meaning in REQUIRED:
        if text not in path.read_text(encoding="utf-8"):
            failures.append(f"{shown(path)}: saknar {meaning}")
    for path, text, meaning in KEPT:
        if text not in path.read_text(encoding="utf-8"):
            failures.append(f"{shown(path)}: har ändrat {meaning}")
    failures.extend(storage_list_failures())
    if failures:
        print("FALLER:")
        for failure in failures:
            print(f"- {failure}")
        return 1
    files = sorted({shown(path) for path, _, _ in REQUIRED})
    print(f"Krävda texter: {len(REQUIRED)} av {len(REQUIRED)} finns i {len(files)} filer.")
    print(f"Orörda texter: {len(KEPT)} av {len(KEPT)} står kvar.")
    print("Lagringsyta (C-165): listan har fyra punkter, och återställningstiden står efter den.")
    print("HÅLLER: begreppen och sidan säger det beslut 61 kräver.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
