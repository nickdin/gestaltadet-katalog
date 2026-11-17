"""issue-174-pilar.py: prov för ärende #174, kört från lagrets rot.

Läser de två kartorna över analysfunktionen i layout/Exempel och skriver ut varje pil
som 'från --[text: relationstyp (C-id)]--> till'. Provet faller (slutkod 1) om

- en av de tre ritningarna saknas, eller mappen inte står under drawings: i settings.yaml,
- en pil saknar text, eller textens relationstyp inte finns som relationstyp i concepts/,
- en pil har en lös ände, eller går mellan andra slags rutor eller åt annat håll än tabellen RELATION_OF säger,
- teckenförklaringen inte nämner en relationstyp som en pil använder,
- de två kartorna inte har samma pilar och samma rutor med samma text,
- en rutas namn inte står i exemplet docs/exempel/myndigheten-for-foreningsstod.md,
- en rad under kartan med fynden inte börjar med sitt perspektiv, eller en mening i den inte står ordagrant i exemplet,
- kartan med fynden inte har markeringarna 1 till 5, eller kartan utan fynd har någon.
"""
import glob
import html
import re
import sys
import xml.etree.ElementTree as ET

FOLDER = 'layout/Exempel'
MAP = f'{FOLDER}/Analysfunktionen karta.drawio.svg'
MAP_FINDINGS = f'{FOLDER}/Analysfunktionen karta med fynd.drawio.svg'
STEPS = f'{FOLDER}/Informationskartläggning steg.drawio.svg'
EXAMPLE = 'docs/exempel/myndigheten-for-foreningsstod.md'

# Pilens text -> relationstypen den är en pil av, och paren av slag den får gå mellan: från, till.
RELATION_OF = {
    'läser': ('C-101', [('Verksamhetsfunktion (C-158)', 'Informationsobjekt (C-060)')]),
    'skriver': ('C-101', [('Verksamhetsfunktion (C-158)', 'Informationsobjekt (C-060)')]),
    'aggregerar': ('C-100', [('Lagringsyta (C-165)', 'Representation (C-085)'),
                             ('Informationsobjekt (C-060)', 'Informationsobjekt (C-060)')]),
    'använder': ('C-095', [('Applikation (C-071)', 'Applikation (C-071)')]),
    'ger form åt': ('C-099', [('Representation (C-085)', 'Informationsobjekt (C-060)')]),
    'tillhandahåller': ('C-099', [('Applikation (C-071)', 'Lagringsyta (C-165)')]),
}

# Raden under kartan med fynden -> meningen den börjar med.
ROW_OPENS_WITH = {
    'row-1': 'Informationssäkerhet: en avvikelse.',
    'row-2': 'Dataskydd: en bedömning.',
    'row-3': 'Offentlighet och arkiv: en bedömning.',
    'row-4': 'Informationsförsörjning: en bedömning.',
    'row-5': 'En skillnad är inget fynd.',
}

failures = []


def fail(message):
    failures.append(message)


def plain(value):
    return ' '.join(html.unescape(re.sub('<[^>]+>', ' ', value or '')).split())


def relation_type(concept_id):
    """Termen för ett begrepp som är en relationstyp, annars None."""
    files = glob.glob(f'concepts/{concept_id} *.md')
    if len(files) != 1:
        return None
    text = open(files[0], encoding='utf-8').read()
    if not re.search(r'^kind: relation-type$', text, re.M):
        return None
    return re.search(r'^term: (.+)$', text, re.M).group(1).strip()


def cells_of(path):
    try:
        content = ET.parse(path).getroot().attrib['content']
    except (OSError, KeyError) as error:
        fail(f'{path}: går inte att läsa som redigerbar ritning ({error.__class__.__name__})')
        return None
    return {c.get('id'): c for c in ET.fromstring(content).iter('mxCell')}


def group_of(cells, box_id):
    return box_id if cells[box_id].get('style') == 'group' else cells[box_id].get('parent')


def kind_of(cells, box_id):
    """Slaget av ruta, raden uppe till vänster i rutan, till exempel 'Lagringsyta (C-165)'."""
    group = group_of(cells, box_id)
    return ' '.join(plain(c.get('value')) for c in cells.values()
                    if c.get('parent') == group and 'fontSize=7' in (c.get('style') or ''))


def boxes_of(cells):
    """Varje ruta som (slag, namn, text), sorterat."""
    boxes = []
    for cell_id, cell in cells.items():
        if cell.get('style') != 'group':
            continue
        texts = {size: ' '.join(plain(c.get('value')) for c in cells.values()
                                if c.get('parent') == cell_id and f'fontSize={size};' in (c.get('style') or ''))
                 for size in (7, 12, 9)}
        boxes.append((texts[7], texts[12], texts[9]))
    return sorted(boxes)


def title_of(cells, box_id):
    """Namnet på rutan en pil sitter i. Pilen får sitta i rutans grupp eller i rektangeln inuti gruppen."""
    group = group_of(cells, box_id)
    titles = [plain(c.get('value')) for c in cells.values()
              if c.get('parent') == group and 'fontSize=12' in (c.get('style') or '')]
    if len(titles) != 1:
        fail(f'en pil sitter i cellen "{box_id}", som inte är en ruta med ett namn')
        return f'(okänd ruta {box_id})'
    return titles[0]


def arrows_of(path, cells, example):
    lines = []
    all_text = ' '.join(plain(c.get('value')) for c in cells.values())
    for cell_id, cell in cells.items():
        if not cell.get('edge') or cells.get(cell.get('parent'), cell).get('style') == 'group':
            continue  # ingen pil, eller linjen under namnet i en ruta
        if cell_id.startswith(('legend-', 'rows-')):
            continue  # teckenförklaringens exempelpilar och linjen över raderna
        if not (cell.get('source') and cell.get('target')):
            fail(f'{path}: pilen "{cell_id}" har en lös ände')
            continue
        source, target = title_of(cells, cell.get('source')), title_of(cells, cell.get('target'))
        label = ' '.join(plain(c.get('value')) for c in cells.values() if c.get('parent') == cell_id)
        concept_id, allowed = RELATION_OF.get(label, (None, []))
        term = relation_type(concept_id) if concept_id else None
        if term is None:
            fail(f'{path}: pilen {source} -> {target} har texten "{label}", som inte hör till en relationstyp i concepts/')
            continue
        if f'{term} ({concept_id})' not in all_text:
            fail(f'{path}: teckenförklaringen nämner inte {term} ({concept_id})')
        kinds = (kind_of(cells, cell.get('source')), kind_of(cells, cell.get('target')))
        if kinds not in allowed:
            fail(f'{path}: pilen {source} -> {target} med texten "{label}" går från {kinds[0]} till {kinds[1]}, '
                 f'inte mellan {allowed}')
        lines.append(f'{source} --[{label}: {term} ({concept_id})]--> {target}')
    for _kind, name, _text in boxes_of(cells):
        if name.lower() not in example.lower():
            fail(f'{path}: rutan "{name}" står inte i exemplet')
    return sorted(lines)


def markers_of(cells):
    return sorted(plain(c.get('value')) for i, c in cells.items() if i.startswith('marker-'))


def main():
    settings = open('settings.yaml', encoding='utf-8').read()
    if not re.search(rf'^  - {FOLDER}$', settings, re.M):
        fail(f'settings.yaml: {FOLDER} står inte under drawings:')
    example = open(EXAMPLE, encoding='utf-8').read().replace('**', '')

    cells_of(STEPS)  # anmäler själv om ritningen med stegen inte går att läsa
    plain_map, findings_map = cells_of(MAP), cells_of(MAP_FINDINGS)
    if plain_map is None or findings_map is None:
        return

    arrows = arrows_of(MAP, plain_map, example)
    arrows_with_findings = arrows_of(MAP_FINDINGS, findings_map, example)
    print(f'Pilar i {MAP}: {len(arrows)}')
    print('\n'.join(arrows))
    print(f'\nPilar i {MAP_FINDINGS}: {len(arrows_with_findings)}')
    if arrows != arrows_with_findings:
        fail('de två kartorna har inte samma pilar')
    else:
        print('samma pilar som kartan utan fynd')
    if boxes_of(plain_map) != boxes_of(findings_map):
        fail('de två kartorna har inte samma rutor med samma text')
    else:
        print(f'samma {len(boxes_of(plain_map))} rutor med samma text som kartan utan fynd')

    if markers_of(plain_map):
        fail(f'{MAP}: kartan utan fynd har markeringar')
    if markers_of(findings_map) != ['1', '2', '3', '4', '5']:
        fail(f'{MAP_FINDINGS}: markeringarna är {markers_of(findings_map)}, inte 1 till 5')

    rows = sorted((i, plain(c.get('value'))) for i, c in findings_map.items() if i.startswith('row-'))
    print(f'\nRader under kartan med fynden: {len(rows)}')
    if [row_id for row_id, _text in rows] != sorted(ROW_OPENS_WITH):
        fail(f'{MAP_FINDINGS}: raderna under kartan är {[r for r, _t in rows]}, inte {sorted(ROW_OPENS_WITH)}')
    for row_id, text in rows:
        sentences = [s.strip() for s in re.split(r'(?<=\.)\s+', text) if s.strip()]
        opening = ROW_OPENS_WITH.get(row_id)
        if len(sentences) < 2 or sentences[0] != opening:
            fail(f'{MAP_FINDINGS}: {row_id} börjar inte med "{opening}" följt av minst en mening')
        missing = [s for s in sentences if s not in example]
        for sentence in missing:
            fail(f'{MAP_FINDINGS}: meningen står inte i exemplet: "{sentence}"')
        print(f'{row_id}: {len(sentences) - len(missing)} av {len(sentences)} meningar står ordagrant i exemplet')


main()
if failures:
    print('\nFALLER:')
    print('\n'.join(f'- {f}' for f in failures))
    sys.exit(1)
print('\nHÅLLER: varje pil har en relationstyp som katalogen har, och fynden är exemplets.')
