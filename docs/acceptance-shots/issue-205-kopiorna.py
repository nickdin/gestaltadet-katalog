"""issue-205-kopiorna.py: prov för ärende #205, kört från lagrets rot.

    python3 docs/acceptance-shots/issue-205-kopiorna.py

Ärendet följer beslut 68. En kopierad representation ger ingen ny handlingstyp. Innehåll som ett
beteende lagrar i ny form är en ny representation, och den får en egen rad i
informationshanteringsplanen när den har ett nytt syfte i ett annat beteende. En statlig myndighet
beslutar inte själv om gallring: den begär beslut hos Riksarkivet (arkivförordningen 14 §).

Provet läser sidan Informationskartläggning, exemplet Myndigheten för föreningsstöd, besluten och
anmärkningarna till Representation (C-085) och Gallring (C-200). Ett stycke är en rad i filen.
Provet faller (slutkod 1) om

- sidan eller exemplet har ett stycke som talar om både kopior och gallring. Före ärendet beslutade
  chefen för Analysenheten där att en kopia gallras när originalet gallras,
- sidan eller exemplet inte har exakt ett stycke med fyndet och ett med åtgärden under
  Offentlighet och arkiv,
- fyndet inte nämner ansökningstabellen, eller åtgärden inte nämner ansökningstabellen och
  Riksarkivet, på båda ställena,
- fyndet eller åtgärden lyder olika på de två ställena,
- sidans checklista har kvar frågan "Har kopiorna en rad?", eller sidan saknar villkoret
  "nytt syfte i ett annat beteende",
- anmärkningen till Representation (C-085) eller Gallring (C-200) inte hänvisar till beslut 68 och
  inte säger villkoret,
- beslut 67 har kvar exemplet "Analysenheten kopierar Ansökan till datalagret",
- beslut 68 saknas, eller någon av dess fem regler saknar sitt exempel i regelns eget stycke:
  pdf:en i handläggarens mapp, ansökningstabellen, Excelfilen i grupprummet, Excelfilen på kartan
  och listan som ingen har tagit fram.
"""
import re
import sys
from pathlib import Path

PAGE = Path('docs/informationskartlaggning.md')
EXAMPLE = Path('docs/exempel/myndigheten-for-foreningsstod.md')
BOTH_PLACES = (PAGE, EXAMPLE)
DECISIONS = Path('docs/adr')
CONCEPT_REMARKS = (Path('concepts/C-085 Representation.md'), Path('concepts/C-200 Gallring.md'))
FINDING_START = '- **Offentlighet och arkiv: en bedömning.**'
# Sidan har också genomgångens fråga under samma rubrik. Åtgärden är stycket som börjar med vem som beslutar.
ACTION_START = '- **Offentlighet och arkiv.** Chefen'
COPY = re.compile(r'kopi(?:a|an|or|orna)\b', re.IGNORECASE)
DISCARD = re.compile(r'gallr', re.IGNORECASE)
OLD_CHECKLIST_QUESTION = 'Har kopiorna en rad?'
CONDITION = 'nytt syfte i ett annat beteende'
NEW_DECISION = 'beslut 68'
OLD_EXAMPLE_IN_DECISION_67 = 'Analysenheten kopierar Ansökan till datalagret'
TABLE = 'ansökningstabellen'
NATIONAL_ARCHIVES = 'Riksarkivet'
# Varje regel i beslut 68, som stycket börjar, med ordet som bara regelns exempel bär.
RULES_IN_DECISION_68 = {
    '- **En kopierad representation ger ingen ny handlingstyp.**': 'pdf',
    '- **Innehåll som ett beteende lagrar i ny form är en ny representation': 'Analysenheten läser Ansökan',
    '- **Den nya representationen får en egen rad': 'Excelfil i grupprummet',
    '- **En representation utan egen rad står ändå på kartan.**': 'ser Excelfilen',
    '- **Den potentiella handlingen får ingen rad.**': 'ingen har gjort det',
}


def paragraphs(path: Path) -> list[str]:
    return path.read_text(encoding='utf-8').splitlines()


def paragraphs_starting(path: Path, start: str) -> list[str]:
    return [line for line in paragraphs(path) if line.startswith(start)]


def copies_discarded(path: Path) -> list[str]:
    """One failure per paragraph that speaks of both copies and discarding."""
    return [f'{path}:{number}: stycket talar om både kopior och gallring'
            for number, line in enumerate(paragraphs(path), start=1)
            if COPY.search(line) and DISCARD.search(line)]


def same_paragraph_in_both_places(start: str, name: str, *words: str) -> tuple[list[str], list[str]]:
    """Return the paragraphs found and the failures: one per place, the words in it, the same wording."""
    failures = []
    found = {path: paragraphs_starting(path, start) for path in BOTH_PLACES}
    for path, lines in found.items():
        if len(lines) != 1:
            failures.append(f'{path}: {len(lines)} stycken börjar med "{start}", väntade 1')
    if failures:
        return [line for lines in found.values() for line in lines], failures
    for path, (line,) in found.items():
        failures += [f'{path}: {name} under Offentlighet och arkiv nämner inte {word}' for word in words if word not in line]
    if found[PAGE] != found[EXAMPLE]:
        failures.append(f'{name} under Offentlighet och arkiv lyder olika på sidan och i exemplet')
    return [found[PAGE][0], found[EXAMPLE][0]], failures


def page_checklist() -> list[str]:
    text = PAGE.read_text(encoding='utf-8')
    failures = []
    if OLD_CHECKLIST_QUESTION in text:
        failures.append(f'{PAGE}: checklistan har kvar frågan "{OLD_CHECKLIST_QUESTION}"')
    if CONDITION not in text:
        failures.append(f'{PAGE}: saknar villkoret "{CONDITION}"')
    return failures


def concept_remarks() -> list[str]:
    failures = []
    for path in CONCEPT_REMARKS:
        text = path.read_text(encoding='utf-8')
        failures += [f'{path}: anmärkningen saknar "{needle}"' for needle in (NEW_DECISION, CONDITION) if needle not in text]
    return failures


def decision_files(number: int) -> list[Path]:
    return sorted(DECISIONS.glob(f'{number:04d}-*.md'))


def decision_67() -> list[str]:
    found = decision_files(67)
    if len(found) != 1:
        return [f'{DECISIONS}: {len(found)} filer för beslut 67, väntade 1']
    if OLD_EXAMPLE_IN_DECISION_67 in found[0].read_text(encoding='utf-8'):
        return [f'beslut 67 har kvar exemplet "{OLD_EXAMPLE_IN_DECISION_67}"']
    return []


def decision_68() -> list[str]:
    found = decision_files(68)
    if len(found) != 1:
        return [f'{DECISIONS}: {len(found)} filer för beslut 68, väntade 1']
    failures = []
    for rule, example in RULES_IN_DECISION_68.items():
        lines = paragraphs_starting(found[0], rule)
        if len(lines) != 1:
            failures.append(f'beslut 68: {len(lines)} stycken börjar med "{rule}", väntade 1')
        elif example not in lines[0]:
            failures.append(f'beslut 68: regeln "{rule}" saknar sitt exempel, "{example}"')
    return failures


def main() -> int:
    failures = [failure for path in BOTH_PLACES for failure in copies_discarded(path)]
    findings, finding_failures = same_paragraph_in_both_places(FINDING_START, 'fyndet', TABLE)
    actions, action_failures = same_paragraph_in_both_places(ACTION_START, 'åtgärden', TABLE, NATIONAL_ARCHIVES)
    failures += finding_failures + action_failures + page_checklist() + concept_remarks() + decision_67() + decision_68()

    for line in findings + actions:
        print(line)
    for failure in failures:
        print(f'FEL: {failure}')
    print(f'{len(failures)} fel')
    return 1 if failures else 0


if __name__ == '__main__':
    sys.exit(main())
