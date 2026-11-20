"""issue-213-tabellerna.py: prov för ärende #213, kört från lagrets rot.

    python3 docs/acceptance-shots/issue-213-tabellerna.py

Beslut 68 säger att Analysenheten inte kopierar ansökningsformuläret. Den lagrar innehållet i en ny
form, ansökningstabellen. De två kartorna över analysfunktionen hos Myndigheten för föreningsstöd
kallade representationen i datalagret "Kopiorna i datalagret". Efter ärendet heter rutan
"Tabellerna i datalagret", och rutan med arkivfyndet säger exemplets mening om ansökningstabellen.

En ritning har texten på två ställen: i den inbäddade ritningen, som draw.io öppnar, och i bilden,
som sajten visar. Provet läser båda. Det faller (slutkod 1) om

- någon av de två ritningarna har kvar "Kopiorna i datalagret", "Kopior av Ansökan" eller
  "rad för kopiorna", i den inbäddade ritningen eller i bilden,
- rutans nya namn eller dess nya text saknas i sin cell i den inbäddade ritningen, eller i bilden,
  i någon av de två ritningarna,
- cellen med arkivfyndet i ritningen med fynd saknar meningen om ansökningstabellen, eller bilden
  saknar den,
- någon mening i cellen med arkivfyndet, efter rubriken, inte står ordagrant i exemplet
  Myndigheten för föreningsstöd.
"""
import html
import re
import sys
import xml.etree.ElementTree as ET
from pathlib import Path

FOLDER = Path('layout/Exempel')
MAP = FOLDER / 'Analysfunktionen karta.drawio.svg'
MAP_WITH_FINDINGS = FOLDER / 'Analysfunktionen karta med fynd.drawio.svg'
EXAMPLE = Path('docs/exempel/myndigheten-for-foreningsstod.md')
OLD_TEXTS = ('Kopiorna i datalagret', 'Kopior av Ansökan', 'rad för kopiorna')
BOX_NAME = 'Tabellerna i datalagret'
BOX_TEXT = 'Tabeller med Ansökan, Beslut, Utbetalning, Förening och Företrädare.'
FINDING = 'Informationshanteringsplanen har ingen rad för ansökningstabellen i datalagret.'
FINDING_HEADING = 'Offentlighet och arkiv: en bedömning.'
# Cellerna i den inbäddade ritningen: rutans namn, rutans text och raden med arkivfyndet.
NAME_CELL, TEXT_CELL, FINDING_CELL = 't-r-kopior', 'r-kopior-def', 'row-3'
TAG = re.compile(r'<[^>]+>')
SPACE = re.compile(r'\s+')


def plain(text: str) -> str:
    """The text a reader sees: markup removed, entities resolved, whitespace collapsed."""
    return SPACE.sub(' ', html.unescape(TAG.sub(' ', text))).strip()


def embedded_drawing(path: Path) -> str:
    """Every label in the drawing that draw.io opens, as one plain text."""
    tree = ET.fromstring(ET.parse(path).getroot().attrib['content'])
    return ' | '.join(plain(cell.get('value', '')) for cell in tree.iter('mxCell') if cell.get('value'))


def picture(path: Path) -> str:
    """Every text in the picture the site shows, as one plain text."""
    root = ET.parse(path).getroot()
    return ' | '.join(plain(' '.join(node.itertext())) for node in root.iter('{http://www.w3.org/2000/svg}foreignObject'))


def cell_text(path: Path, cell_id: str) -> str:
    """The plain label of one cell in the embedded drawing, or '' when the cell is missing."""
    tree = ET.fromstring(ET.parse(path).getroot().attrib['content'])
    return next((plain(cell.get('value', '')) for cell in tree.iter('mxCell') if cell.get('id') == cell_id), '')


def failures_in(path: Path, cells: dict[str, str]) -> list[str]:
    """Old texts gone from both places, each cell holding its new text, and the picture showing it."""
    failures = []
    shown = picture(path)
    for place, text in (('den inbäddade ritningen', embedded_drawing(path)), ('bilden', shown)):
        failures += [f'{path}: {place} har kvar "{old}"' for old in OLD_TEXTS if old in text]
    for cell_id, wanted in cells.items():
        if wanted not in cell_text(path, cell_id):
            failures.append(f'{path}: cellen "{cell_id}" i den inbäddade ritningen saknar "{wanted}"')
        if wanted not in shown:
            failures.append(f'{path}: bilden saknar "{wanted}"')
    return failures


def finding_stands_in_the_example() -> list[str]:
    """Every sentence after the bold heading in the finding's cell must stand word for word in the example."""
    example = EXAMPLE.read_text(encoding='utf-8')
    text = cell_text(MAP_WITH_FINDINGS, FINDING_CELL)
    sentences = [s.strip() for s in re.findall(r'[^.]+\.', text.split(FINDING_HEADING, 1)[-1])]
    return [f'{MAP_WITH_FINDINGS}: meningen i cellen "{FINDING_CELL}" står inte i exemplet: "{sentence}"'
            for sentence in sentences if sentence not in example]


def main() -> int:
    box = {NAME_CELL: BOX_NAME, TEXT_CELL: BOX_TEXT}
    failures = failures_in(MAP, box) + failures_in(MAP_WITH_FINDINGS, box | {FINDING_CELL: FINDING})
    failures += finding_stands_in_the_example()
    for failure in failures:
        print(f'FEL: {failure}')
    print(f'{len(failures)} fel')
    return 1 if failures else 0


if __name__ == '__main__':
    sys.exit(main())
