"""issue-198-bilden.py: prov för ärende #198, kört från lagrets rot.

    python3 docs/acceptance-shots/issue-198-bilden.py                     provet på ritningarna i layout/Exempel
    python3 docs/acceptance-shots/issue-198-bilden.py --ritningar MAPP    provet på de tre ritningarna i MAPP

Provet läser de två kartorna över analysfunktionen och ritningen över arbetssättets steg, och mäter i bilden som
sajten visar, inte i den inbäddade ritningen. Det jämför ingenting med ett tidigare läge, så det går att köra efter
varje ändring i ritningarna. Jämförelsen med läget före ärende #185 gör docs/acceptance-shots/issue-185-pilar.py.

Provet faller (slutkod 1) om

- en text i rutan för steg 2 är ritad utanför rutans ram i bilden, eller är högre än utrymmet dess cell visar, så att
  den klipps,
- en pils sträcka i bilden skär någon annan ruta än pilens egna två ändar, i någon av de tre ritningarna.

draw.io lägger en bild av varje text i filen, och den bildens höjd är textens fulla höjd också när texten klipps.
En pils sträckor läses ur pilens linje och pilspets, och en båge räknas som åtta raka sträckor. En pil skär en ruta
också när den ligger på rutans kant.

Provet ser inte en text som klipps i sidled: bildens bredd är alltid cellens bredd, också när ett ord är bredare
än cellen.

Växeln --ritningar läser de tre ritningarna ur en annan mapp, med samma filnamn. Den finns för att provet ska kunna
köras på ändrade kopior, som docs/acceptance-shots/issue-198-kopior.py skriver.
"""
import html
import os
import re
import sys
import xml.etree.ElementTree as ET

FOLDER = 'layout/Exempel'
MAP = 'Analysfunktionen karta.drawio.svg'
MAP_FINDINGS = 'Analysfunktionen karta med fynd.drawio.svg'
STEPS = 'Informationskartläggning steg.drawio.svg'
# Gruppen som är rutan för steg 2 i ritningen över stegen.
STEP_2 = 's1'
SVG = '{http://www.w3.org/2000/svg}'
# Så långt utanför en rutas ritade ram en pil räknas som att den skär rutan. Ramens linje är 1 bred, så en pil
# som ligger på linjen skymmer den. Pilens egna två rutor prövas aldrig, så att pilen slutar på deras kant stör inte.
NEAR = 0.5
# Antalet raka sträckor en båge i en pil räknas som.
CURVE_PIECES = 8

failures = []


def fail(message):
    failures.append(message)


def plain(value):
    return ' '.join(html.unescape(re.sub('<[^>]+>', ' ', value or '')).split())


def cells_of(svg):
    """Den inbäddade ritningens celler, id -> cell. Provet läser bara vad som hör ihop ur dem, inga mått."""
    return {c.get('id'): c for c in ET.fromstring(svg.attrib['content']).iter('mxCell')}


def group_of(cells, box_id):
    """Rutan en cell hör till: cellen själv om den är en grupp, annars dess förälder."""
    return box_id if cells[box_id].get('style') == 'group' else cells[box_id].get('parent')


def name_of(cells, box_id):
    """Rutans namn om den har ett, texten i storlek 12 i rutans grupp, annars gruppens id."""
    group = group_of(cells, box_id)
    titles = [plain(c.get('value')) for c in cells.values()
              if c.get('parent') == group and 'fontSize=12' in (c.get('style') or '')]
    return titles[0] if len(titles) == 1 else group


def drawn_of(name, svg):
    """Det som är ritat för varje cell i bilden: id -> lista av (element, förskjutning i x, förskjutning i y)."""
    drawn = {}

    def walk(element, cell_id, dx, dy):
        cell_id = element.get('data-cell-id', cell_id)
        moved = re.fullmatch(r'translate\(([-\d.]+),([-\d.]+)\)', element.get('transform') or '')
        if moved:
            dx, dy = dx + float(moved.group(1)), dy + float(moved.group(2))
        elif element.get('transform'):
            fail(f'{name}: bilden har en förflyttning provet inte kan läsa: {element.get("transform")}')
        drawn.setdefault(cell_id, []).append((element, dx, dy))
        for child in element:
            walk(child, cell_id, dx, dy)

    walk(svg, None, 0.0, 0.0)
    return drawn


def frames_of(name, cells, drawn):
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
            fail(f'{name}: rutan "{name_of(cells, group)}" har {len(rectangles)} ritade ramar i bilden, inte en')
            continue
        x, y, width, height = rectangles[0]
        frames[group] = (x, y, x + width, y + height)
    return frames


def stretches_of(name, d):
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
            fail(f'{name}: en pil är ritad med "{command}", som provet inte kan läsa: {d}')
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


def check_arrows(name, cells, drawn, frames):
    """Ingen pils sträcka i bilden skär någon annan ruta än pilens egna två ändar."""
    # En linje vars förälder är en ruta är linjen under rutans namn, ingen pil. Teckenförklaringens linjer prövas med.
    arrows = [i for i, c in cells.items()
              if c.get('edge') and cells.get(c.get('parent'), c).get('style') != 'group']
    hits = 0
    for arrow in arrows:
        # Varje ritad linje med sin egen förskjutning: (sträckorna, dx, dy).
        lines = [(stretches_of(name, e.get('d')), dx, dy)
                 for e, dx, dy in drawn.get(arrow, []) if e.tag == SVG + 'path']
        if not lines:
            fail(f'{name}: pilen "{arrow}" är inte ritad i bilden')
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
                fail(f'{name}: pilen {label} ("{arrow}") skär rutan "{name_of(cells, group)}" i bilden')
    print(f'{len(arrows)} pilar och linjer prövade mot {len(frames)} rutors ramar, '
          + ('ingen skär en annan ruta än sina egna ändar' if not hits else f'{hits} gånger skär en pil en ruta'))


def check_text_frames(name, cells, drawn, frames, group):
    """Varje text i rutan är ritad inom rutans ram i bilden, och är inte högre än utrymmet dess cell visar."""
    if group not in frames:
        fail(f'{name}: rutan för steg 2, gruppen "{group}", har ingen ritad ram i bilden att mäta texten mot')
        return
    frame = frames[group]
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
                fail(f'{name}: texten "{child}" har ingen ritad ram i bilden')
                continue
            texts += 1
            left, top = float(image.get('x')) + dx, float(image.get('y')) + dy
            height = float(image.get('height'))
            right, bottom = left + float(image.get('width')), top + height
            print(f'texten "{child}" är ritad {left:g}-{right:g} i sidled och {top:g}-{bottom:g} i höjdled'
                  + (f', höjd {height:g} av {float(limit.group(1)):g} som cellen visar' if limit else ''))
            if left < frame[0] or top < frame[1] or right > frame[2] or bottom > frame[3]:
                wrong += 1
                fail(f'{name}: texten "{child}" är ritad utanför ramen för rutan "{name_of(cells, group)}" i bilden: '
                     f'texten når {left:g}-{right:g} i sidled och {top:g}-{bottom:g} i höjdled, '
                     f'ramen {frame[0]:g}-{frame[2]:g} och {frame[1]:g}-{frame[3]:g}')
            if limit and height > float(limit.group(1)):
                wrong += 1
                fail(f'{name}: texten "{child}" i rutan "{name_of(cells, group)}" klipps i bilden: '
                     f'texten är {height:g} hög, och cellen visar {float(limit.group(1)):g}')
    if not texts:
        fail(f'{name}: rutan "{name_of(cells, group)}" har ingen ritad text i bilden')
    print(f'rutan för steg 2 har ramen {frame[0]:g}-{frame[2]:g} i sidled och {frame[1]:g}-{frame[3]:g} i höjdled, '
          + (f'och alla {texts} texter ryms i den' if not wrong else 'och texten ryms inte'))


def main():
    if sys.argv[1:] == []:
        folder = FOLDER
    elif sys.argv[1:2] == ['--ritningar'] and len(sys.argv) == 3:
        folder = sys.argv[2]
    else:
        sys.exit('Användning: issue-198-bilden.py [--ritningar MAPP]')
    print(f'Ritningarna läses ur {folder}.')
    for name in (MAP, MAP_FINDINGS, STEPS):
        print(f'\n{name}:')
        svg = ET.parse(os.path.join(folder, name)).getroot()
        cells, drawn = cells_of(svg), drawn_of(name, svg)
        frames = frames_of(name, cells, drawn)
        if name == STEPS:
            check_text_frames(name, cells, drawn, frames, STEP_2)
        check_arrows(name, cells, drawn, frames)


main()
if failures:
    print('\nFALLER:')
    print('\n'.join(f'- {f}' for f in failures))
    sys.exit(1)
print('\nHÅLLER: i bilden ryms texten i rutan för steg 2, och ingen pil skär en annan ruta än sina egna ändar.')
