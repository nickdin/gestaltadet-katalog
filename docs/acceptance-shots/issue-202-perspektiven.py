"""issue-202-perspektiven.py: prov för ärende #202, kört från lagrets rot.

    python3 docs/acceptance-shots/issue-202-perspektiven.py

Ärendet följer beslut 64: informationshanteringen har tre perspektiv, informationsförsörjningen är
arkitekturarbete, och sidan Informationskartläggning säger för varje perspektiv vilka dokument det
håller och vad de pekar på i kartan. Provet läser alla textfiler och ritningar i katalogen utom
besluten (docs/adr), underlagen (docs/research) och proven själva (docs/acceptance-shots).
Ett stycke är en rad i filen. Provet faller (slutkod 1) om

- orden fyra perspektiv står kvar,
- informationsförsörjningen står som punkt i en perspektivlista eller som egen rubrik på sidan
  eller i exemplet,
- sidan saknar ett stycke per perspektiv, med listan under det, som nämner dokumenten, säger vad
  de pekar på och hänvisar till en källa,
- sidan inte säger att processägaren ställer kraven på behandlingarna och att informationssäkerheten
  håller dokumentationen av dem,
- sidan saknar stycket om informationsförsörjningen som arkitekturarbete med exemplet om datalagret,
- sidan inte nämner cybersäkerhetslagen, att klassningsförteckningen är en rekommendation, eller
  dokumentationen av it-miljön och att den pekar på applikationen,
- sidan och exemplet inte har samma mening om när varvet slutar,
- sidan kallar ett dokument förteckning, lista eller register utöver dem som källorna namnger,
- ritningen Informationskartläggning steg inte har exakt tre rutor märkta Steg 4 - genomgång, eller
  har färre pilar än de tolv den hade före ärendet.

Provet skriver också ut varje rad som nämner informationsförsörjningen, så att läsaren ser vad
ordet betyder på varje ställe.
"""
import html
import re
import sys
import xml.etree.ElementTree as ET
from pathlib import Path

PAGE = Path('docs/informationskartlaggning.md')
EXAMPLE = Path('docs/exempel/myndigheten-for-foreningsstod.md')
STEPS_DRAWING = Path('layout/Exempel/Informationskartläggning steg.drawio.svg')
EXCLUDED = ('.git/', 'docs/adr/', 'docs/research/', 'docs/acceptance-shots/')
TEXT_SUFFIXES = {'.md', '.yaml', '.yml', '.css'}
# Varje perspektiv med den källa som dess stycke på sidan ska hänvisa till.
PERSPECTIVE_SOURCES = {'Informationssäkerhet': 'MSBFS 2020:7', 'Dataskydd': 'artikel 30', 'Offentlighet och arkiv': 'RA-FS 1991:1'}
PERSPECTIVES = tuple(PERSPECTIVE_SOURCES)
ARROWS_BEFORE_THE_TICKET = 12
STEP_FOUR_LABEL = 'Steg 4 - genomgång'
END_OF_ROUND = 'Varvet slutar när de tre perspektivens fynd har beslut.'

FOUR_PERSPECTIVES = re.compile(r'fyra perspektiv', re.IGNORECASE)
INFORMATION_SUPPLY = re.compile(r'informationsförsörjning', re.IGNORECASE)
SUPPLY_AS_PERSPECTIVE = re.compile(r'^(- \*\*Informationsförsörjning[.:]|#+ Informationsförsörjning\s*$)')
# Dokument som källorna själva kallar förteckning eller register: metodstödet för systematiskt
# informationssäkerhetsarbete (förteckning över klassad information), dataskyddsförordningen
# artikel 30 (register över behandling) och RA-FS 1991:1 (arkivförteckning). Ordet
# registerförteckning står varken i artikel 30 eller på Integritetsskyddsmyndighetens sida Föra
# register över behandling, och räknas därför inte.
SOURCED_NAMES = re.compile(r'klassningsförteckning|arkivförteckning|regist(?:er|ret) över behandling', re.IGNORECASE)
REGISTER_WORD = re.compile(r'\w*förteckning\w*|\w*regist(?:er|ret)\b|\b\w*list(?:a|an|or|orna)\b', re.IGNORECASE)
# Orden som bara är källans när stycket också skriver ut dokumentets hela namn.
BARE_WORDS = {'förteckning', 'förteckningen', 'register', 'registret'}
# Föreningsregistret är en applikation hos Myndigheten för föreningsstöd, inget dokument i ett perspektiv.
NOT_A_DOCUMENT = re.compile(r'föreningsregistret', re.IGNORECASE)
UNIT_NAME = 'Register- och tillsynsenheten'  # en enhet hos Myndigheten för föreningsstöd, inget dokument

Paragraph = tuple[int, str]
Place = tuple[str, str]  # var texten står, skrivet för läsaren, och texten


def paragraphs(path: Path) -> list[Paragraph]:
    return [(number, line) for number, line in enumerate(path.read_text(encoding='utf-8').splitlines(), 1) if line.strip()]


def catalogue_files() -> list[Path]:
    files = []
    for path in sorted(Path('.').rglob('*')):
        relative = path.as_posix()
        if not path.is_file() or any(relative.startswith(prefix) for prefix in EXCLUDED):
            continue
        if path.suffix in TEXT_SUFFIXES or relative.endswith('.drawio.svg'):
            files.append(path)
    return files


def drawing_cells(path: Path) -> list[ET.Element]:
    """Cellerna i den redigerbara ritning som ligger i svg-filens content-attribut."""
    embedded = re.search(r'content="([^"]*)"', path.read_text(encoding='utf-8'))
    if embedded is None:
        raise SystemExit(f'{path} bär ingen redigerbar ritning i content-attributet')
    return list(ET.fromstring(html.unescape(embedded.group(1))).iter('mxCell'))


def searchable_texts(path: Path) -> list[Place]:
    if path.suffix == '.svg':
        return [(f'{path}, cell {cell.get("id")}', cell.get('value', '')) for cell in drawing_cells(path) if cell.get('value')]
    return [(f'{path}:{number}', text) for number, text in paragraphs(path)]


def search_the_catalogue() -> list[str]:
    failures = []
    four, supply = [], []
    for path in catalogue_files():
        for place, text in searchable_texts(path):
            if FOUR_PERSPECTIVES.search(text):
                four.append((place, text))
            if INFORMATION_SUPPLY.search(text):
                supply.append((place, text))
    print(f'Rader med orden fyra perspektiv: {len(four)}')
    for place, text in four:
        print(f'  {place}: {text}')
        failures.append(f'{place} säger fyra perspektiv')
    print(f'Rader som nämner informationsförsörjningen: {len(supply)}')
    for place, text in supply:
        as_perspective = bool(SUPPLY_AS_PERSPECTIVE.search(text))
        print(f'  {place}: {"SOM PERSPEKTIV" if as_perspective else "inte som perspektiv"}')
        print(f'    {text}')
        if as_perspective:
            failures.append(f'{place} ställer informationsförsörjningen bland perspektiven')
    return failures


def blocks(page: list[Paragraph], opening: str) -> list[Paragraph]:
    """Varje stycke som börjar med opening, läst ihop med listan som står direkt under det."""
    found = []
    for index, (number, text) in enumerate(page):
        if not text.startswith(opening):
            continue
        items = []
        for _, following in page[index + 1:]:
            if not following.startswith('- '):
                break
            items.append(following)
        found.append((number, '\n    '.join([text, *items])))
    return found


def one_paragraph_per_perspective(page: list[Paragraph]) -> list[str]:
    failures = []
    print('Stycken på sidan om varje perspektivs dokumentation:')
    for perspective, source in PERSPECTIVE_SOURCES.items():
        found = [
            (number, text) for number, text in blocks(page, f'**{perspective}.**')
            if 'dokument' in text and 'pekar på' in text
        ]
        referring = [(number, text) for number, text in found if source in text]
        print(f'  {perspective}: {len(found)} stycken, {len(referring)} med hänvisning till {source}')
        for number, text in found:
            print(f'    {PAGE}:{number}: {text}')
        if not found:
            failures.append(f'sidan saknar stycket om dokumentationen i {perspective}')
        elif not referring:
            failures.append(f'stycket om {perspective} hänvisar inte till {source}')
    return failures


def page_says(page: list[Paragraph], description: str, *needles: str) -> list[str]:
    """Ett stycke på sidan ska innehålla alla orden i needles."""
    found = [(number, text) for number, text in page if all(needle.lower() in text.lower() for needle in needles)]
    print(f'{description}: {len(found)} stycken')
    for number, _ in found:
        print(f'  {PAGE}:{number}')
    return [] if found else [f'sidan saknar: {description}']


def same_end_of_round(page: list[Paragraph], example: list[Paragraph]) -> list[str]:
    failures = []
    for path, lines in ((PAGE, page), (EXAMPLE, example)):
        found = [number for number, text in lines if END_OF_ROUND in text]
        print(f'Meningen "{END_OF_ROUND}" i {path}: rad {found}')
        if not found:
            failures.append(f'{path} saknar meningen om när varvet slutar')
    return failures


def unsourced_document_names(page: list[Paragraph]) -> list[str]:
    failures = []
    print('Ord på sidan med förteckning, lista eller register:')
    for number, text in page:
        for word in REGISTER_WORD.findall(text.replace(UNIT_NAME, '')):
            if NOT_A_DOCUMENT.search(word):
                continue
            named_in_full = text if word.lower() in BARE_WORDS else word
            unsourced = not SOURCED_NAMES.search(named_in_full)
            print(f'  {PAGE}:{number}: {word}: {"UTAN KÄLLA" if unsourced else "källans ord"}')
            if unsourced:
                failures.append(f'{PAGE}:{number} kallar ett dokument {word} utan att en källa gör det')
    return failures


def steps_drawing_shows_three() -> list[str]:
    cells = drawing_cells(STEPS_DRAWING)
    step_four = [cell for cell in cells if cell.get('value') == STEP_FOUR_LABEL]
    arrows = [cell for cell in cells if cell.get('edge') == '1' and cell.get('source') and cell.get('target')]
    titles = []
    for cell in step_four:
        box = cell.get('parent')
        titles += [other.get('value') for other in cells if other.get('id') == f't-{box}']
    print(f'Rutor märkta {STEP_FOUR_LABEL} i ritningen: {len(step_four)}: {", ".join(titles)}')
    print(f'Pilar mellan rutor i ritningen: {len(arrows)}')
    failures = []
    if sorted(titles) != sorted(PERSPECTIVES):
        failures.append(f'ritningen visar inte de tre perspektiven som steg 4, utan: {", ".join(titles)}')
    if len(arrows) < ARROWS_BEFORE_THE_TICKET:
        failures.append(f'ritningen har {len(arrows)} pilar, färre än {ARROWS_BEFORE_THE_TICKET}')
    return failures


def main() -> int:
    page = paragraphs(PAGE)
    example = paragraphs(EXAMPLE)
    failures = search_the_catalogue()
    failures += one_paragraph_per_perspective(page)
    failures += page_says(page, 'processägaren ställer kraven och informationssäkerheten håller dokumentationen',
                          'processägaren ställer kraven', 'informationssäkerheten håller')
    failures += page_says(page, 'informationsförsörjningen är arkitekturarbete, med datalagret',
                          'informationsförsörjningen', 'arkitekturarbete', 'datalagret')
    failures += page_says(page, 'cybersäkerhetslagen ställer fler krav', 'cybersäkerhetslagen', 'fler krav')
    failures += page_says(page, 'klassningsförteckningen är en rekommendation', 'klassningsförteckningen', 'rekommendation')
    failures += page_says(page, 'dokumentationen av it-miljön pekar på applikationen', 'it-miljön', 'pekar på applikationen')
    failures += same_end_of_round(page, example)
    failures += unsourced_document_names(page)
    failures += steps_drawing_shows_three()
    print()
    if failures:
        print(f'FALLER: {len(failures)}')
        for failure in failures:
            print(f'  {failure}')
        return 1
    print('HÅLLER: katalogen har tre perspektiv, och sidan säger vad varje perspektivs dokumentation pekar på.')
    return 0


if __name__ == '__main__':
    sys.exit(main())
