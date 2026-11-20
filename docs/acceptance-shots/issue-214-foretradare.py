"""issue-214-foretradare.py: prov för ärende #214, kört från lagrets rot.

    python3 docs/acceptance-shots/issue-214-foretradare.py

Ärendet gäller åtgärden under Dataskydd i exemplet om analysfunktionen hos Myndigheten för
föreningsstöd. Tabellen med Företrädare i datalagret är en kopia utan eget syfte. Myndigheten får
gallra den enligt Riksarkivets föreskrift (RA-FS 2021:6) och ska dokumentera det. En kopia som har
ett nytt syfte i ett annat beteende får däremot en egen rad i informationshanteringsplanen, också
när formen är densamma. Beslut 68 säger den regeln med kopian av ansökningsformuläret i ett
tillsynsärende.

Provet läser sidan Informationskartläggning, exemplet Myndigheten för föreningsstöd och beslut 68.
Ett stycke är en rad i filen. Provet faller (slutkod 1) om

- sidan eller exemplet inte har exakt ett stycke med åtgärden under Dataskydd,
- åtgärden inte säger på båda ställena att kopian saknar nytt syfte, att Riksarkivets föreskrift
  är grunden och att myndigheten skriver in gallringen i informationshanteringsplanen,
- åtgärden lyder olika på de två ställena,
- beslut 68 saknar regeln om en kopia i samma form med nytt syfte, eller regeln saknar exemplet
  med tillsynsärendet och att arkivet redovisar kopian där,
- beslut 68 saknar regeln om en representation utan nytt syfte, eller regeln saknar exemplet med
  tabellen med Företrädare och att den inte får någon egen rad,
- beslut 68 inte citerar föreskriftens ord "samma form och innehåll",
- anmärkningen till Representation (C-085) eller Gallring (C-200) inte nämner kopian i ett
  tillsynsärende, eller sidans checklista inte frågar efter en representation i ny form eller i
  samma.
"""
import sys
from pathlib import Path

PAGE = Path('docs/informationskartlaggning.md')
EXAMPLE = Path('docs/exempel/myndigheten-for-foreningsstod.md')
BOTH_PLACES = (PAGE, EXAMPLE)
DECISIONS = Path('docs/adr')
# Sidan har också genomgångens fråga under samma rubrik. Åtgärden är stycket som börjar med vem som beslutar.
ACTION_START = '- **Dataskydd.** Chefen'
GROUNDS_IN_THE_ACTION = ('inget nytt syfte', 'Riksarkivets föreskrift låter myndigheten gallra', 'skriver in gallringen i informationshanteringsplanen')
# De två regler som ärendet gav beslut 68, som stycket börjar, med orden som regelns exempel och följd bär.
RULES_IN_DECISION_68 = {
    '- **En kopia i samma form får också en egen rad': ('tillsynsärende', 'arkivet redovisar den där'),
    '- **En representation utan nytt syfte är en kopia i föreskriftens mening': ('Tabellen med Företrädare', 'ingen egen rad'),
}
WORDS_OF_THE_REGULATION = 'samma form och innehåll'
CONCEPT_REMARKS = (Path('concepts/C-085 Representation.md'), Path('concepts/C-200 Gallring.md'))
SAME_FORM_IN_THE_REMARKS = 'tillsynsärende'
CHECKLIST_QUESTION = 'i ny form eller i samma'


def paragraphs_starting(path: Path, start: str) -> list[str]:
    return [line for line in path.read_text(encoding='utf-8').splitlines() if line.startswith(start)]


def action_under_data_protection() -> tuple[list[str], list[str]]:
    """Return the action paragraphs found and the failures: one per place, the grounds in it, the same wording."""
    found = {path: paragraphs_starting(path, ACTION_START) for path in BOTH_PLACES}
    failures = [f'{path}: {len(lines)} stycken börjar med "{ACTION_START}", väntade 1'
                for path, lines in found.items() if len(lines) != 1]
    if failures:
        return [line for lines in found.values() for line in lines], failures
    for path, (line,) in found.items():
        failures += [f'{path}: åtgärden under Dataskydd säger inte "{ground}"'
                     for ground in GROUNDS_IN_THE_ACTION if ground not in line]
    if found[PAGE] != found[EXAMPLE]:
        failures.append('åtgärden under Dataskydd lyder olika på sidan och i exemplet')
    return [found[PAGE][0], found[EXAMPLE][0]], failures


def decision_68() -> list[str]:
    found = sorted(DECISIONS.glob('0068-*.md'))
    if len(found) != 1:
        return [f'{DECISIONS}: {len(found)} filer för beslut 68, väntade 1']
    failures = []
    for rule, words in RULES_IN_DECISION_68.items():
        lines = paragraphs_starting(found[0], rule)
        if len(lines) != 1:
            failures.append(f'beslut 68: {len(lines)} stycken börjar med "{rule}", väntade 1')
            continue
        failures += [f'beslut 68: regeln "{rule}" säger inte "{word}"' for word in words if word not in lines[0]]
    if WORDS_OF_THE_REGULATION not in found[0].read_text(encoding='utf-8'):
        failures.append(f'beslut 68 citerar inte föreskriftens ord "{WORDS_OF_THE_REGULATION}"')
    return failures


def remarks_and_checklist() -> list[str]:
    failures = [f'{path}: anmärkningen nämner inte kopian i samma form, "{SAME_FORM_IN_THE_REMARKS}"'
                for path in CONCEPT_REMARKS if SAME_FORM_IN_THE_REMARKS not in path.read_text(encoding='utf-8')]
    if CHECKLIST_QUESTION not in PAGE.read_text(encoding='utf-8'):
        failures.append(f'{PAGE}: checklistan frågar inte efter en representation "{CHECKLIST_QUESTION}"')
    return failures


def main() -> int:
    actions, failures = action_under_data_protection()
    failures += decision_68() + remarks_and_checklist()
    for line in actions:
        print(line)
    for failure in failures:
        print(f'FEL: {failure}')
    print(f'{len(failures)} fel')
    return 1 if failures else 0


if __name__ == '__main__':
    sys.exit(main())
