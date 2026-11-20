"""issue-185-pilar.py: prov för ärende #185, kört från lagrets rot.

    python3 docs/acceptance-shots/issue-185-pilar.py            provet
    python3 docs/acceptance-shots/issue-185-pilar.py --facit    skriver facit ur ritningarna som de står, körs bara på basen
    python3 docs/acceptance-shots/issue-185-pilar.py --ritningar MAPP    provet på de tre ritningarna i MAPP

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
- bilden som sajten visar inte bär samma texter som den inbäddade ritningen,
- en text i rutan för steg 2 är ritad utanför rutans ram i bilden, eller är högre än utrymmet dess cell visar, så att
  den klipps (ärende #198),
- en pils sträcka i bilden skär någon annan ruta än pilens egna två ändar, i någon av de tre ritningarna (ärende #198).

De två sista mäts i bilden som sajten visar, inte i den inbäddade ritningen. draw.io lägger en bild av varje text i
filen, och den bildens höjd är textens fulla höjd också när texten klipps. En pils sträckor läses ur pilens linje
och pilspets, och en båge räknas som åtta raka sträckor. En pil skär en ruta också när den ligger på rutans kant.

Provet ser inte en text som klipps i sidled: bildens bredd är alltid cellens bredd, också när ett ord är bredare
än cellen.

Växeln --ritningar läser de tre ritningarna ur en annan mapp än layout/Exempel, med samma filnamn. Den finns för att
provet ska kunna köras på ändrade kopior, som docs/acceptance-shots/issue-198-kopior.py skriver. Facit och sidan läses
alltid ur lagret.
"""
import glob
import html
import json
import os
import re
import sys
import xml.etree.ElementTree as ET

FOLDER = 'layout/Exempel'
MAP = f'{FOLDER}/Analysfunktionen karta.drawio.svg'
MAP_FINDINGS = f'{FOLDER}/Analysfunktionen karta med fynd.drawio.svg'
STEPS = f'{FOLDER}/Informationskartläggning steg.drawio.svg'
PAGE = 'docs/informationskartlaggning.md'
GOLDEN = 'docs/acceptance-shots/issue-185-facit.json'
SVG = '{http://www.w3.org/2000/svg}'
# Mappen ritningarna läses ur. Namnen ovan står kvar som de heter i lagret, i facit och i utskriften.
drawings = FOLDER
# Så långt utanför en rutas ritade ram en pil räknas som att den skär rutan. Ramens linje är 1 bred, så en pil
# som ligger på linjen skymmer den. Pilens egna två rutor prövas aldrig, så att pilen slutar på deras kant stör inte.
NEAR = 0.5
# Antalet raka sträckor en båge i en pil räknas som.
CURVE_PIECES = 8

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


def file_of(path):
    """Filen en ritning läses ur: samma filnamn i mappen som --ritningar pekar ut, annars ritningen i lagret."""
    return os.path.join(drawings, os.path.basename(path))


def cells_of(path):
    """Den inbäddade ritningens celler, id -> cell."""
    content = ET.parse(file_of(path)).getroot().attrib['content']
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


def titles_of(cells, box_id):
    """Namnen i rutan en cell hör till: texterna i storlek 12 i rutans grupp."""
    group = group_of(cells, box_id)
    return [plain(c.get('value')) for c in cells.values()
            if c.get('parent') == group and 'fontSize=12' in (c.get('style') or '')]


def title_of(cells, box_id):
    """Namnet på rutan en pil sitter i. Pilen får sitta i rutans grupp eller i rektangeln inuti gruppen."""
    titles = titles_of(cells, box_id)
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
    svg = open(file_of(path), encoding='utf-8').read()
    return plain(re.sub(r'content="[^"]*"', '', svg, count=1))


def drawn_of(path):
    """Det som är ritat för varje cell i bilden: id -> lista av (element, förskjutning i x, förskjutning i y)."""
    drawn = {}

    def walk(element, cell_id, dx, dy):
        cell_id = element.get('data-cell-id', cell_id)
        moved = re.fullmatch(r'translate\(([-\d.]+),([-\d.]+)\)', element.get('transform') or '')
        if moved:
            dx, dy = dx + float(moved.group(1)), dy + float(moved.group(2))
        elif element.get('transform'):
            fail(f'{path}: bilden har en förflyttning provet inte kan läsa: {element.get("transform")}')
        drawn.setdefault(cell_id, []).append((element, dx, dy))
        for child in element:
            walk(child, cell_id, dx, dy)

    walk(ET.parse(file_of(path)).getroot(), None, 0.0, 0.0)
    return drawn


def name_of(cells, box_id):
    """Rutans namn om den har ett, annars cellens id."""
    titles = titles_of(cells, box_id)
    return titles[0] if len(titles) == 1 else group_of(cells, box_id)


def frames_of(path, cells, drawn):
    """Varje rutas ritade rektangel i bilden: gruppens id -> (vänster, topp, höger, botten)."""
    frames = {}
    for group, cell in cells.items():
        if cell.get('style') != 'group':
            continue
        rectangles = [(float(e.get('x')) + dx, float(e.get('y')) + dy, float(e.get('width')), float(e.get('height')))
                      for child, c in cells.items() if c.get('parent') == group
                      for e, dx, dy in drawn.get(child, [])
                      if e.tag == SVG + 'rect' and e.get('stroke') not in (None, 'none')]
        if len(rectangles) != 1:
            fail(f'{path}: rutan "{name_of(cells, group)}" har {len(rectangles)} ritade ramar i bilden, inte en')
            continue
        x, y, width, height = rectangles[0]
        frames[group] = (x, y, x + width, y + height)
    return frames


def stretches_of(path, d):
    """En ritad linje som raka sträckor: ((x, y), (x, y)). En båge delas i CURVE_PIECES raka sträckor."""
    tokens = re.findall(r'[A-Za-z]|-?\d+(?:\.\d+)?', d)
    stretches, here, start, i = [], None, None, 0
    while i < len(tokens):
        command = tokens[i]
        if command == 'M':
            here = start = (float(tokens[i + 1]), float(tokens[i + 2]))
            i += 3
        elif command == 'L':
            there = (float(tokens[i + 1]), float(tokens[i + 2]))
            stretches.append((here, there))
            here = there
            i += 3
        elif command == 'Q':
            bend = (float(tokens[i + 1]), float(tokens[i + 2]))
            end = (float(tokens[i + 3]), float(tokens[i + 4]))
            first = here
            for piece in range(1, CURVE_PIECES + 1):
                t = piece / CURVE_PIECES
                there = tuple((1 - t) ** 2 * first[k] + 2 * (1 - t) * t * bend[k] + t ** 2 * end[k] for k in (0, 1))
                stretches.append((here, there))
                here = there
            i += 5
        elif command == 'Z':
            stretches.append((here, start))
            here = start
            i += 1
        else:
            fail(f'{path}: en pil är ritad med "{command}", som provet inte kan läsa: {d}')
            return stretches
    return stretches


def crosses(stretch, frame):
    """Sant om sträckan når in i rektangeln, eller närmare än NEAR från den."""
    (x0, y0), (x1, y1) = stretch
    left, top, right, bottom = frame[0] - NEAR, frame[1] - NEAR, frame[2] + NEAR, frame[3] + NEAR
    enter, leave = 0.0, 1.0
    for delta, low, high in ((x1 - x0, left - x0, right - x0), (y1 - y0, top - y0, bottom - y0)):
        if delta == 0:
            if not low < 0 < high:
                return False
            continue
        first, last = sorted((low / delta, high / delta))
        enter, leave = max(enter, first), min(leave, last)
    return enter < leave


def check_arrows(path, cells, drawn, frames):
    """Ingen pils sträcka i bilden skär någon annan ruta än pilens egna två ändar."""
    # En linje vars förälder är en ruta är linjen under rutans namn, ingen pil. Teckenförklaringens linjer prövas med.
    arrows = [i for i, c in cells.items()
              if c.get('edge') and cells.get(c.get('parent'), c).get('style') != 'group']
    hits = 0
    for arrow in arrows:
        # Varje ritad linje med sin egen förskjutning: (sträckorna, dx, dy).
        lines = [(stretches_of(path, e.get('d')), dx, dy)
                 for e, dx, dy in drawn.get(arrow, []) if e.tag == SVG + 'path']
        if not lines:
            fail(f'{path}: pilen "{arrow}" är inte ritad i bilden')
            continue
        ends = [cells[arrow].get(end) for end in ('source', 'target')]
        own = {group_of(cells, end) for end in ends if end in cells}
        label = ' -> '.join(name_of(cells, end) if end in cells else '(lös ände)' for end in ends)
        for group, frame in frames.items():
            if group in own:
                continue
            if any(crosses(s, (frame[0] - dx, frame[1] - dy, frame[2] - dx, frame[3] - dy))
                   for stretches, dx, dy in lines for s in stretches):
                hits += 1
                fail(f'{path}: pilen {label} ("{arrow}") skär rutan "{name_of(cells, group)}" i bilden')
    print(f'bilden: {len(arrows)} pilar och linjer prövade mot {len(frames)} rutors ramar, '
          + ('ingen skär en annan ruta än sina egna ändar' if not hits else f'{hits} gånger skär en pil en ruta'))


def check_text_frames(path, cells, drawn, frames, group):
    """Varje text i rutan är ritad inom rutans ram i bilden, och är inte högre än utrymmet dess cell visar."""
    frame = frames.get(group)
    if frame is None:
        return
    texts, wrong = 0, 0
    for child, cell in cells.items():
        if cell.get('parent') != group:
            continue
        for element, dx, dy in drawn.get(child, []):
            if element.tag != SVG + 'switch':
                continue
            image = element.find(SVG + 'image')
            limit = re.search(r'max-height: ([\d.]+)px', ET.tostring(element, encoding='unicode'))
            if image is None:
                fail(f'{path}: texten "{child}" har ingen ritad ram i bilden')
                continue
            texts += 1
            left, top = float(image.get('x')) + dx, float(image.get('y')) + dy
            height = float(image.get('height'))
            right, bottom = left + float(image.get('width')), top + height
            print(f'bilden: texten "{child}" är ritad {left:g}-{right:g} i sidled och {top:g}-{bottom:g} i höjdled'
                  + (f', höjd {height:g} av {float(limit.group(1)):g} som cellen visar' if limit else ''))
            if left < frame[0] or top < frame[1] or right > frame[2] or bottom > frame[3]:
                wrong += 1
                fail(f'{path}: texten "{child}" är ritad utanför ramen för rutan "{name_of(cells, group)}" i bilden: '
                     f'texten når {left:g}-{right:g} i sidled och {top:g}-{bottom:g} i höjdled, '
                     f'ramen {frame[0]:g}-{frame[2]:g} och {frame[1]:g}-{frame[3]:g}')
            if limit and height > float(limit.group(1)):
                wrong += 1
                fail(f'{path}: texten "{child}" i rutan "{name_of(cells, group)}" klipps i bilden: '
                     f'texten är {height:g} hög, och cellen visar {float(limit.group(1)):g}')
    if not texts:
        fail(f'{path}: rutan "{name_of(cells, group)}" har ingen ritad text i bilden')
    print(f'bilden: rutans ram är {frame[0]:g}-{frame[2]:g} i sidled och {frame[1]:g}-{frame[3]:g} i höjdled, '
          + (f'och alla {texts} texter ryms i den' if not wrong else 'och texten ryms inte'))


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
    drawn = drawn_of(path)
    check_arrows(path, cells, drawn, frames_of(path, cells, drawn))
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
    cells, drawn = cells_of(STEPS), drawn_of(STEPS)
    frames = frames_of(STEPS, cells, drawn)
    check_text_frames(STEPS, cells, drawn, frames, STEP_2['group'])
    check_arrows(STEPS, cells, drawn, frames)


def main():
    global drawings
    if sys.argv[1:2] == ['--ritningar'] and len(sys.argv) == 3:
        drawings = sys.argv[2]
        print(f'Ritningarna läses ur {drawings}, inte ur {FOLDER}.\n')
    elif sys.argv[1:] not in ([], ['--facit']):
        sys.exit('Användning: issue-185-pilar.py [--facit | --ritningar MAPP]')
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
          'och inget annat är ändrat mot basen. I bilden ryms texten i rutan för steg 2, och ingen pil skär en ruta.')
