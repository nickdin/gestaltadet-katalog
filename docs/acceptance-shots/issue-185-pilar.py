"""issue-185-pilar.py: prov för ärende #185, kört från lagrets rot.

    python3 docs/acceptance-shots/issue-185-pilar.py            provet
    python3 docs/acceptance-shots/issue-185-pilar.py --facit    skriver facit ur ritningarna som de står, körs bara på basen

Provet läser de två kartorna över analysfunktionen och ritningen över arbetssättets steg i layout/Exempel.
Sättet att läsa pilarna är lånat ur issue-174-pilar.py: varje pil skrivs som
'från --[text: relationstyp (C-id)]--> till'. Tabellen RELATION_OF är utökad så att läser och skriver också får gå
från en Verksamhetsfunktion (C-158) till en Lagringsyta (C-165), som beslut 62 säger.

Provet faller (slutkod 1) om

- en karta inte har 21 pilar, eller saknar en av de två nya pilarna,
- en pil går mellan andra slags rutor än tabellen RELATION_OF säger, eller har en lös ände,
- de två kartorna inte har samma pilar och samma rutor med samma text,
- en cell som fanns på basen har ändrats i en karta: en pil, en ruta, en text, en markering eller en rad under kartan
  med fynden (facit är issue-185-facit.json, basens ritningar cell för cell),
- en karta har fått någon annan ny cell än de två pilarna och deras texter,
- rutan för steg 2 inte bär sidans två meningar ordagrant, eller säger något annat än basens text med de två meningarna
  inskjutna,
- något annat i ritningen över stegen har ändrats än textens ord och höjden på rutan för steg 2, eller rutan ligger
  över en annan ruta,
- bilden som sajten visar inte bär samma texter som den inbäddade ritningen.
"""
import glob
import html
import json
import re
import sys
import xml.etree.ElementTree as ET

FOLDER = 'layout/Exempel'
MAP = f'{FOLDER}/Analysfunktionen karta.drawio.svg'
MAP_FINDINGS = f'{FOLDER}/Analysfunktionen karta med fynd.drawio.svg'
STEPS = f'{FOLDER}/Informationskartläggning steg.drawio.svg'
PAGE = 'docs/informationskartlaggning.md'
GOLDEN = 'docs/acceptance-shots/issue-185-facit.json'

# Pilens text -> relationstypen den är en pil av, och paren av slag den får gå mellan: från, till.
ACCESS = [('Verksamhetsfunktion (C-158)', 'Informationsobjekt (C-060)'),
          ('Verksamhetsfunktion (C-158)', 'Lagringsyta (C-165)')]
RELATION_OF = {
    'läser': ('C-101', ACCESS),
    'skriver': ('C-101', ACCESS),
    'aggregerar': ('C-100', [('Lagringsyta (C-165)', 'Representation (C-085)'),
                             ('Informationsobjekt (C-060)', 'Informationsobjekt (C-060)')]),
    'använder': ('C-095', [('Applikation (C-071)', 'Applikation (C-071)')]),
    'ger form åt': ('C-099', [('Representation (C-085)', 'Informationsobjekt (C-060)')]),
    'tillhandahåller': ('C-099', [('Applikation (C-071)', 'Lagringsyta (C-165)')]),
}

NEW_ARROWS = ['Analysfunktionen --[läser: har åtkomst till (C-101)]--> Datalagret',
              'Analysfunktionen --[skriver: har åtkomst till (C-101)]--> Grupprummet']
ARROWS_PER_MAP = 21
BOXES_PER_MAP = 15

# Sidans två meningar under steg 2, som rutan för steg 2 ska bära ordagrant.
PAGE_SENTENCES = ('Arkitekten fångar också vilka lagringsytor beteendet använder. '
                  'På kartan har beteendet åtkomst till var och en av dem.')
# Meningen i rutan som sidans två meningar står efter, i sidans ordning.
SENTENCE_BEFORE = 'lagringsytorna och applikationerna.'
STEP_2 = {'group': 's1', 'frame': 'b-s1', 'text': 's1-def'}

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
    """Den inbäddade ritningens celler, id -> cell."""
    content = ET.parse(path).getroot().attrib['content']
    return {c.get('id'): c for c in ET.fromstring(content).iter('mxCell')}


def record_of(cell):
    """En cell som ren data: egenskaperna, läget och storleken, och punkterna en pil går genom."""
    record = {'cell': dict(sorted(cell.attrib.items()))}
    geometry = cell.find('mxGeometry')
    if geometry is not None:
        record['geometry'] = dict(sorted(geometry.attrib.items()))
        record['points'] = [dict(sorted(p.attrib.items())) for p in geometry.iter('mxPoint')]
    return record


def records_of(path):
    return {cell_id: record_of(cell) for cell_id, cell in cells_of(path).items()}


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


def arrows_of(path, cells):
    """Kartans pilar som rader, och id:t för varje pil och dess text."""
    lines, ids = [], {}
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
        labels = [i for i, c in cells.items() if c.get('parent') == cell_id]
        label = ' '.join(plain(cells[i].get('value')) for i in labels)
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
        line = f'{source} --[{label}: {term} ({concept_id})]--> {target}'
        lines.append(line)
        ids[line] = [cell_id] + labels
    return sorted(lines), ids


def visible_of(path):
    """Texten i bilden som sajten visar: filen utan den inbäddade ritningen."""
    svg = open(path, encoding='utf-8').read()
    return plain(re.sub(r'content="[^"]*"', '', svg, count=1))


def check_map(path, golden):
    """En karta mot facit: de två nya pilarna finns, och ingenting som fanns på basen är ändrat."""
    cells = cells_of(path)
    records = {cell_id: record_of(cell) for cell_id, cell in cells.items()}
    arrows, ids = arrows_of(path, cells)
    print(f'Pilar i {path}: {len(arrows)}')
    print('\n'.join(arrows))
    if len(arrows) != ARROWS_PER_MAP:
        fail(f'{path}: {len(arrows)} pilar, inte {ARROWS_PER_MAP}')
    new_ids = set()
    for arrow in NEW_ARROWS:
        if arrow not in arrows:
            fail(f'{path}: pilen saknas: {arrow}')
        new_ids.update(ids.get(arrow, []))

    changed = sorted(i for i in golden if i in records and records[i] != golden[i])
    gone = sorted(i for i in golden if i not in records)
    added = sorted(i for i in records if i not in golden)
    for cell_id in changed:
        fail(f'{path}: cellen "{cell_id}" är ändrad mot basen')
    for cell_id in gone:
        fail(f'{path}: cellen "{cell_id}" fanns på basen och är borta')
    for cell_id in added:
        if cell_id not in new_ids:
            fail(f'{path}: cellen "{cell_id}" är ny och hör inte till de två nya pilarna')
    old_arrows = [a for a in arrows if a not in NEW_ARROWS]
    rows = sorted(i for i in golden if i.startswith(('row-', 'rowmark-', 'rows-', 'marker-')))
    print(f'mot basen: {len(golden) - len(changed) - len(gone)} av {len(golden)} celler är desamma, '
          f'{len(added)} celler är nya: {", ".join(added) or "inga"}')
    print(f'mot basen: {len(old_arrows)} övriga pilar och {len(boxes_of(cells))} rutors text är desamma'
          if not (changed or gone) else 'mot basen: något som fanns på basen är ändrat')
    if rows:
        same = [i for i in rows if records.get(i) == golden[i]]
        print(f'mot basen: {len(same)} av {len(rows)} celler i raderna under kartan och markeringarna är desamma')

    visible = visible_of(path)
    for word, cell_ids in (('läser', [i for i, c in cells.items() if plain(c.get('value')) == 'läser']),
                           ('skriver', [i for i, c in cells.items() if plain(c.get('value')) == 'skriver'])):
        # Teckenförklaringens rad "läser, skriver - har åtkomst till (C-101)" bär ordet en gång till.
        shown = len(re.findall(rf'(?<![\wåäö]){word}(?![\wåäö])', visible)) - 1
        print(f'bilden visar texten "{word}" på {shown} pilar, den inbäddade ritningen har {len(cell_ids)}')
        if shown != len(cell_ids):
            fail(f'{path}: bilden visar "{word}" på {shown} pilar, den inbäddade ritningen har {len(cell_ids)}')
    return arrows, boxes_of(cells)


def number(record, key):
    return float(record['geometry'].get(key, 0))


def check_steps(golden):
    """Ritningen över stegen mot facit: bara rutan för steg 2 är ändrad, i text och höjd."""
    page = open(PAGE, encoding='utf-8').read()
    step_2_on_page = page.split('## Steg 2', 1)[1].split('\n## ', 1)[0] if '## Steg 2' in page else ''
    if PAGE_SENTENCES not in step_2_on_page:
        fail(f'{PAGE}: meningarna står inte under steg 2 på sidan: "{PAGE_SENTENCES}"')

    records = records_of(STEPS)
    text = records[STEP_2['text']]['cell']['value']
    old_text = golden[STEP_2['text']]['cell']['value']
    wanted = old_text.replace(SENTENCE_BEFORE, f'{SENTENCE_BEFORE} {PAGE_SENTENCES}', 1)
    print(f'\nRutan för steg 2 i {STEPS}:')
    print(text)
    if PAGE_SENTENCES not in text:
        fail(f'{STEPS}: rutan för steg 2 bär inte sidans meningar ordagrant: "{PAGE_SENTENCES}"')
    elif text != wanted:
        fail(f'{STEPS}: rutan för steg 2 säger något annat än basens text med sidans två meningar inskjutna')
    else:
        print('sidans två meningar står ordagrant i rutan, och resten av texten är basens')
    if PAGE_SENTENCES not in visible_of(STEPS):
        fail(f'{STEPS}: bilden visar inte sidans meningar i rutan för steg 2')
    else:
        print('bilden visar samma två meningar')

    # Det enda som får skilja: textens ord, och höjden och läget i höjdled för rutan för steg 2.
    allowed = {STEP_2['group']: {'height', 'y'}, STEP_2['frame']: {'height'}, STEP_2['text']: {'height'}}
    others_changed = []
    for cell_id in sorted(set(golden) | set(records)):
        old, new = golden.get(cell_id), records.get(cell_id)
        if old == new:
            continue
        if old is None or new is None or cell_id not in allowed:
            others_changed.append(cell_id)
            continue
        cell_differs = {k for k in set(old['cell']) | set(new['cell']) if old['cell'].get(k) != new['cell'].get(k)}
        geometry_differs = {k for k in set(old['geometry']) | set(new['geometry'])
                            if old['geometry'].get(k) != new['geometry'].get(k)}
        if cell_differs - ({'value'} if cell_id == STEP_2['text'] else set()) or geometry_differs - allowed[cell_id] \
                or old['points'] != new['points']:
            others_changed.append(cell_id)
    for cell_id in others_changed:
        fail(f'{STEPS}: cellen "{cell_id}" är ändrad mot basen på ett sätt ärendet inte ber om')
    same = sum(1 for i in golden if records.get(i) == golden[i])
    print(f'mot basen: {same} av {len(golden)} celler är desamma, och ingen cell är ny eller borta'
          if set(golden) == set(records) else 'mot basen: en cell är ny eller borta')

    group, old_group = records[STEP_2['group']], golden[STEP_2['group']]
    middle = number(group, 'y') + number(group, 'height') / 2
    old_middle = number(old_group, 'y') + number(old_group, 'height') / 2
    print(f'rutan för steg 2: höjd {old_group["geometry"]["height"]} -> {group["geometry"]["height"]}, '
          f'mitten i höjdled {old_middle:g} -> {middle:g}')
    if middle != old_middle:
        fail(f'{STEPS}: rutan för steg 2 har flyttat sin mitt, så pilarna in och ut går inte längre rakt')
    frame, text_cell = records[STEP_2['frame']], records[STEP_2['text']]
    if number(group, 'height') != number(frame, 'height') \
            or number(text_cell, 'y') + number(text_cell, 'height') > number(frame, 'height'):
        fail(f'{STEPS}: texten i rutan för steg 2 ryms inte i rutans ram')
    left, top = number(group, 'x'), number(group, 'y')
    right, bottom = left + number(group, 'width'), top + number(group, 'height')
    for cell_id, record in records.items():
        if record['cell'].get('style') != 'group' or cell_id == STEP_2['group']:
            continue
        x, y = number(record, 'x'), number(record, 'y')
        if x < right and left < x + number(record, 'width') and y < bottom and top < y + number(record, 'height'):
            fail(f'{STEPS}: rutan för steg 2 ligger över rutan "{cell_id}"')


def main():
    if sys.argv[1:] == ['--facit']:
        golden = {path: records_of(path) for path in (MAP, MAP_FINDINGS, STEPS)}
        with open(GOLDEN, 'w', encoding='utf-8') as file:
            json.dump(golden, file, ensure_ascii=False, indent=1, sort_keys=True)
            file.write('\n')
        print(f'facit skrivet till {GOLDEN}: ' + ', '.join(f'{len(golden[p])} celler' for p in golden))
        return
    golden = json.load(open(GOLDEN, encoding='utf-8'))

    arrows, boxes = check_map(MAP, golden[MAP])
    print()
    arrows_with_findings, boxes_with_findings = check_map(MAP_FINDINGS, golden[MAP_FINDINGS])
    print()
    if arrows != arrows_with_findings:
        fail('de två kartorna har inte samma pilar')
    else:
        print('de två kartorna har samma pilar')
    if boxes != boxes_with_findings or len(boxes) != BOXES_PER_MAP:
        fail(f'de två kartorna har inte samma {BOXES_PER_MAP} rutor med samma text')
    else:
        print(f'de två kartorna har samma {len(boxes)} rutor med samma text')
    check_steps(golden[STEPS])


main()
if failures:
    print('\nFALLER:')
    print('\n'.join(f'- {f}' for f in failures))
    sys.exit(1)
if sys.argv[1:] != ['--facit']:
    print('\nHÅLLER: båda kartorna har de två nya pilarna, rutan för steg 2 bär sidans meningar, '
          'och inget annat är ändrat mot basen.')
