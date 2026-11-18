"""Prov för ärende #191: pilen AGGREGERAR mellan Portfölj (C-011) och Initiativ (C-012)
i ritningen Mandat och ansvar begreppsmodell är ritad som den relation lagret har.

Körs från katalogens rot utan argument: python3 docs/acceptance-shots/issue-191-pil.py

Provet svarar på fyra frågor och slutar med slutkod 0 bara om alla fyra håller.

1. Vilken relation har lagret mellan de två begreppen? En delrelation (partitive) kräver
   en pil med romb vid helheten. En associerad relation kräver en pil utan romb.
2. Är pilen i den inbäddade draw.io-ritningen av den sorten? Provet läser pilens stil:
   romben ska sitta i den ände som är fäst vid helhetens ruta, och bara där.
3. Visar bilden som sajten ser samma sak? Provet läser pilens former i bilden: en
   delrelation har en sluten form med fyra hörn, och den ligger närmast helhetens ruta.
4. Är pilens text, ändar och väg kvar, och är alla andra celler orörda? Provet jämför
   med ritningen i commit 7dd4a06, som är basen för ärendet. Bara pilens stil får skilja.
"""
import html
import re
import subprocess
import sys
import xml.etree.ElementTree as ET
from pathlib import Path

ROOT = Path('.')
DRAWING = 'layout/Styrning/Mandat och ansvar begreppsmodell.drawio.svg'
BASE = '7dd4a06'
PORTFOLIO, INITIATIVE = 'C-011', 'C-012'
LABEL = 'AGGREGERAR'
DIAMONDS = ('diamond', 'diamondThin')

errors = []


def fail(message):
    errors.append(message)
    print('  FEL: ' + message)


def plain(value):
    """Cellens text utan märkning, läsriktningens triangel och extra blanksteg."""
    text = html.unescape(re.sub(r'<[^>]+>', ' ', value or ''))
    return ' '.join(re.sub('[▶◀▲▼]', ' ', text).split())


def front_matter(concept_id):
    path = next((ROOT / 'concepts').glob(concept_id + ' *.md'))
    return path.as_posix(), path.read_text(encoding='utf-8').split('---')[1].splitlines()


def relation_in_store(a, b):
    """Säger hur lagret binder ihop a och b: (sort, helhet, del, plats) eller None.

    Delrelationen står hos delen, under nyckeln partitive. En associerad relation står
    under nyckeln associative hos det begrepp den utgår från.
    """
    found = []
    for part, whole in ((a, b), (b, a)):
        name, lines = front_matter(part)
        key = None
        for number, line in enumerate(lines, start=1):
            top = re.match(r'^([a-z_]+):', line)
            if top:
                key = top.group(1)
            if f'[[{whole} ' not in line:
                continue
            if key == 'partitive':
                found.append(('delrelation', whole, part, f'{name}:{number}'))
            elif key == 'associative':
                found.append(('associerad relation', None, None, f'{name}:{number}'))
    return found


def model_of(text):
    """Den inbäddade draw.io-ritningens celler: id -> cell."""
    content = ET.fromstring(text).attrib['content']
    return {cell.get('id'): cell for cell in ET.fromstring(content).iter('mxCell')}


def boxes_of(cells):
    """Rutorna med begreppets id: gruppens cell-id -> C-id."""
    return {cell.get('parent'): plain(cell.get('value'))
            for cell in cells.values() if re.fullmatch(r'C-\d+', plain(cell.get('value')))}


def box_of(cells, cell_id):
    boxes = boxes_of(cells)
    cell = cells.get(cell_id)
    return None if cell is None else boxes.get(cell_id) or boxes.get(cell.get('parent'))


def style_of(cell):
    pairs = [part.split('=', 1) for part in (cell.get('style') or '').split(';') if '=' in part]
    return dict(pairs)


def whole_cell(node):
    """Cellen hel, med attributen i fast ordning, så att två avkodningar går att jämföra."""
    return [node.tag, sorted(node.attrib.items()), [whole_cell(child) for child in node]]


def numbers(text):
    return [float(n) for n in re.findall(r'-?\d+(?:\.\d+)?', text)]


def group_of(picture, cell_id):
    """Formerna som bilden ritar för en cell: texten mellan cellens <g> och nästa cells."""
    start = picture.find(f'data-cell-id="{cell_id}"')
    if start < 0:
        return None
    end = picture.find('data-cell-id="', start + 1)
    return picture[start:end if end > 0 else len(picture)]


def centre_of_box(picture, cell_id):
    group = group_of(picture, cell_id) or ''
    rect = re.search(r'<rect[^>]*>', group)
    if not rect:
        return None
    get = lambda name: float(re.search(rf'\b{name}="([-\d.]+)"', rect.group(0)).group(1))
    return get('x') + get('width') / 2, get('y') + get('height') / 2


def main():
    print(f'1. Relationen i lagret mellan Portfölj ({PORTFOLIO}) och Initiativ ({INITIATIVE})')
    relations = relation_in_store(PORTFOLIO, INITIATIVE)
    for sort, whole, part, where in relations:
        detail = f', helheten är {whole} och delen {part}' if whole else ''
        print(f'  {sort}{detail}: {where}')
    if len(relations) != 1:
        fail(f'lagret har {len(relations)} relationer mellan de två begreppen, provet väntar sig exakt en')
        return finish()
    sort, whole, part, _ = relations[0]
    wanted = 'romb vid helheten' if sort == 'delrelation' else 'ingen romb'
    print(f'  pilen ska därför ha: {wanted}')

    print('2. Pilen i den inbäddade draw.io-ritningen')
    text = (ROOT / DRAWING).read_text(encoding='utf-8')
    cells = model_of(text)
    arrows = [cell for cell in cells.values()
              if cell.get('edge') and {box_of(cells, cell.get('source')), box_of(cells, cell.get('target'))}
              == {PORTFOLIO, INITIATIVE}]
    print(f'  pilar mellan de två rutorna: {len(arrows)}')
    if len(arrows) != 1:
        fail(f'ritningen har {len(arrows)} pilar mellan de två rutorna, inte en')
        return finish()
    arrow = arrows[0]
    arrow_id = arrow.get('id')
    style = style_of(arrow)
    ends = {'start': box_of(cells, arrow.get('source')), 'end': box_of(cells, arrow.get('target'))}
    diamond_at = [ends[end] for end in ('start', 'end') if style.get(end + 'Arrow', 'none') in DIAMONDS]
    other_heads = [f'{end}Arrow={style[end + "Arrow"]}' for end in ('start', 'end')
                   if style.get(end + 'Arrow', 'none') not in DIAMONDS + ('none',)]
    print(f'  cell {arrow_id}: startArrow={style.get("startArrow", "saknas")} vid {ends["start"]}, '
          f'endArrow={style.get("endArrow", "saknas")} vid {ends["end"]}')
    print(f'  romb vid: {", ".join(diamond_at) if diamond_at else "ingen ände"}')
    if 'endArrow' not in style:
        fail('pilens stil saknar endArrow, och draw.io ritar då en pilspets i målet')
    if other_heads:
        fail(f'pilen har en pilspets som inte hör till sorten: {", ".join(other_heads)}')
    if sort == 'delrelation' and diamond_at != [whole]:
        fail(f'lagret har en delrelation med helheten {whole}, men den inbäddade ritningen har romb vid: '
             + (', '.join(diamond_at) if diamond_at else 'ingen ände'))
    if sort != 'delrelation' and diamond_at:
        fail(f'lagret har en associerad relation, men den inbäddade ritningen har romb vid {", ".join(diamond_at)}')

    print('3. Pilen i bilden som sajten visar')
    picture = re.sub(r'content="[^"]*"', '', text, count=1)
    group = group_of(picture, arrow_id)
    if group is None:
        fail(f'bilden har inga former för cell {arrow_id}')
        return finish()
    paths = re.findall(r'<path d="([^"]+)"', group)
    closed = [numbers(d) for d in paths if d.strip().endswith('Z') and len(numbers(d)) == 8]
    print(f'  former i pilen: {len(paths)}, varav slutna med fyra hörn (romber): {len(closed)}')
    centres = {concept: centre_of_box(picture, box) for box, concept in
               ((arrow.get('source'), ends['start']), (arrow.get('target'), ends['end']))}
    near = []
    for corners in closed:
        x, y = sum(corners[0::2]) / 4, sum(corners[1::2]) / 4
        distance = {concept: ((x - cx) ** 2 + (y - cy) ** 2) ** 0.5 for concept, (cx, cy) in centres.items()}
        near.append(min(distance, key=distance.get))
        print(f'  rombens mitt: ({x:.0f}, {y:.0f}), närmast rutan {near[-1]}')
    if sort == 'delrelation' and near != [whole]:
        fail(f'lagret har en delrelation med helheten {whole}, men bilden har romb vid: '
             + (', '.join(near) if near else 'ingen ände'))
    if sort != 'delrelation' and near:
        fail(f'lagret har en associerad relation, men bilden har en romb vid {", ".join(near)}')
    label = plain(group_of(picture, arrow_id + '-l') or '')
    print(f'  pilens text i bilden: {LABEL if LABEL in label else "saknas"}')
    if LABEL not in label:
        fail(f'bilden saknar texten {LABEL} på pilen')

    print(f'4. Resten av ritningen mot commit {BASE}')
    shown = subprocess.run(['git', 'show', f'{BASE}:{DRAWING}'], capture_output=True, text=True)
    if shown.returncode != 0:
        fail(f'git show {BASE}:{DRAWING} gav slutkod {shown.returncode}')
        return finish()
    base = model_of(shown.stdout)
    changed = sorted(i for i in set(base) | set(cells)
                     if i != arrow_id and (i not in base or i not in cells or whole_cell(base[i]) != whole_cell(cells[i])))
    print(f'  celler på basen: {len(base)}, celler nu: {len(cells)}, ändrade utom {arrow_id}: {len(changed)}')
    for cell_id in changed:
        fail(f'cell {cell_id} är ändrad, tillagd eller borttagen')
    old = base.get(arrow_id)
    if old is None:
        fail(f'basen har ingen cell {arrow_id}')
        return finish()
    same = {
        'källa och mål': (old.get('source'), old.get('target')) == (arrow.get('source'), arrow.get('target')),
        'väg (geometry)': [whole_cell(child) for child in old] == [whole_cell(child) for child in arrow],
        'text': [whole_cell(cell) for cell in base.values() if cell.get('parent') == arrow_id]
                == [whole_cell(cell) for cell in cells.values() if cell.get('parent') == arrow_id],
    }
    for what, kept in same.items():
        print(f'  pilens {what}: {"som på basen" if kept else "ÄNDRAD"}')
        if not kept:
            fail(f'pilens {what} är inte som på basen')
    old_style, differs = style_of(old), []
    for key in sorted(set(old_style) | set(style)):
        if old_style.get(key) != style.get(key):
            differs.append(f'{key}: {old_style.get(key, "saknas")} -> {style.get(key, "saknas")}')
    print('  pilens stil mot basen: ' + ('; '.join(differs) if differs else 'samma'))
    other = [d for d in differs if not re.match(r'(start|end)(Arrow|Fill|Size):', d)]
    if other:
        fail(f'pilens stil är ändrad i annat än pilens ändar: {"; ".join(other)}')
    return finish()


def finish():
    if errors:
        print(f'FALLER: {len(errors)} fel.')
        return 1
    print('HÅLLER: pilen är ritad som den relation lagret har, i den inbäddade ritningen och i bilden.')
    return 0


if __name__ == '__main__':
    sys.exit(main())
