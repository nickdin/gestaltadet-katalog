"""Prov för #187: de tretton ändrade definitionerna går att läsa hela i bilden.

Körs från lagrets rot:

    python3 docs/acceptance-shots/issue-187-rutor-bild.py

Ärende #183 bytte definitionstexten i tretton rutor i nio ritningar. Det här
provet läser bilden som sajten visar, inte bara den inbäddade draw.io-ritningen.
Bilden visas i /usr/bin/chromium --headless, och provet läser måtten där.

En begreppsruta är en grupp av celler. Rutan är den ritade ramen, och
definitionscellen är den cell i gruppen vars id slutar på "-def".

Provet gör fyra jämförelser för var och en av de tretton definitionscellerna
och slutar med slutkod 0 bara om alla fyra håller.

1. Textens höjd jämförs med cellens höjd. Cellen klipper text som går utanför
   den, så en text som är högre än cellen går inte att läsa hel. Höjden läses
   på två sätt: som webbläsaren bryter texten, och som draw.io mätte den när
   bilden exporterades (höjden på reservbilden i filen).
2. Cellen ska ligga inom sin ruta.
3. Cellen får inte ligga på en annan cell, och rutan får inte ligga på en cell
   utanför den egna gruppen. En ram som omsluter rutan helt räknas inte.
   Pilar räknas inte: ärende #183 ändrade ingen pil.
4. Cellens mått i bilden ska vara cellens mått i den inbäddade ritningen.
   Annars är bara den ena av de två ändrad.
"""
import glob
import html
import json
import os
import re
import subprocess
import sys
import tempfile
import xml.etree.ElementTree as ET

CHROMIUM = '/usr/bin/chromium'
# The thirteen definition cells that #183 changed, as issue-183-rutor.txt names them.
THIRTEEN = [
    ('layout/Arkitektur/Arkitektur beskrivningens form.drawio.svg', '5-def'),
    ('layout/Arkitektur/Arkitektur dimensioner.drawio.svg', '5-def'),
    ('layout/Arkitektur/Arkitektur dimensioner.drawio.svg', '7-def'),
    ('layout/Arkitektur/Arkitektur kedjan.drawio.svg', '15-def'),
    ('layout/Arkitektur/Arkitekturnivå.drawio.svg', 'g-los-def'),
    ('layout/Information/Verksamhetsinformation begreppsmodell.drawio.svg', 'g11-def'),
    ('layout/Principer/Begreppsmodell arkitekturprinciper.drawio.svg', '54-def'),
    ('layout/Principer/Begreppsmodell arkitekturprinciper.drawio.svg', '58-def'),
    ('layout/Styrning/Mandat och ansvar begreppsmodell.drawio.svg', '34-def'),
    ('layout/Styrning/Mandat och ansvar begreppsmodell.drawio.svg', '38-def'),
    ('layout/Styrning/Mandat och ansvar begreppsmodell.drawio.svg', 'd-def'),
    ('layout/Styrning/Målstyrning begreppsmodell.drawio.svg', 'g3-def'),
    ('layout/Styrning/Styrobjekt begreppsmodell.drawio.svg', '11-def'),
]
# Two edges that only touch differ by less than this, in the image's points.
SLACK = 0.01

# Runs in the page. For every cell of the image: the bounding box of its drawn shape, and for a
# cell with text the height the browser gives the text, the height the cell clips at, and the
# height of the fallback image that draw.io rendered at export.
MEASURE = r'''
const cells = {};
for (const g of document.querySelectorAll('g[data-cell-id]')) {
  const cell = {};
  const shape = g.querySelector(':scope > g');
  if (shape && shape.children.length) {
    const b = shape.getBBox();
    cell.box = [b.x, b.y, b.width, b.height];
  }
  const text = g.querySelector(':scope > g > g > switch > foreignObject > div > div > div');
  if (text) {
    cell.textHeight = text.getBoundingClientRect().height;
    cell.clipHeight = parseFloat(text.parentElement.style.maxHeight);
    cell.font = getComputedStyle(text).fontFamily;
  }
  const fallback = g.querySelector(':scope > g > g > switch > image');
  if (fallback) cell.fallbackHeight = parseFloat(fallback.getAttribute('height'));
  cells[g.getAttribute('data-cell-id')] = cell;
}
document.body.innerHTML = '<pre id="measured">' + JSON.stringify(cells).replace(/&/g, '&amp;').replace(/</g, '&lt;') + '</pre>';
'''


def terms():
    """Each concept's id mapped to its term."""
    found = {}
    for path in glob.glob('concepts/C-*.md'):
        text = open(path, encoding='utf-8').read()
        found[re.search(r'^id: (C-\d+)$', text, re.M).group(1)] = re.search(r'^term: (.*)$', text, re.M).group(1).strip('\'"')
    return found


def model_of(svg_text):
    """Every cell of the embedded draw.io model: its attributes and its width and height."""
    cells = {}
    for cell in ET.fromstring(ET.fromstring(svg_text).attrib['content']).iter('mxCell'):
        geometry = cell.find('mxGeometry')
        cells[cell.get('id')] = {
            'parent': cell.get('parent'), 'edge': cell.get('edge') == '1', 'style': cell.get('style') or '', 'value': cell.get('value') or '',
            'size': None if geometry is None or geometry.get('width') is None else (float(geometry.get('width')), float(geometry.get('height'))),
        }
    return cells


def image_of(svg_text, folder):
    """Every cell of the visible image, measured in headless Chromium."""
    image = re.sub(r'content="[^"]*"', '', svg_text, count=1)
    page = os.path.join(folder, 'page.html')
    with open(page, 'w', encoding='utf-8') as handle:
        handle.write('<!DOCTYPE html><html><head><meta charset="utf-8"></head><body style="margin:0">'
                     + image[image.index('<svg'):] + '<script>' + MEASURE + '</script></body></html>')
    run = subprocess.run([CHROMIUM, '--headless', '--no-sandbox', '--disable-gpu', '--dump-dom', 'file://' + page],
                         capture_output=True, text=True, timeout=300)
    measured = re.search(r'<pre id="measured">(.*?)</pre>', run.stdout, re.S)
    if measured is None:
        sys.exit(f'{CHROMIUM} gav inga mått (slutkod {run.returncode}): {run.stderr[-500:]}')
    return json.loads(html.unescape(measured.group(1)))


def inside(inner, outer):
    return (inner[0] >= outer[0] - SLACK and inner[1] >= outer[1] - SLACK
            and inner[0] + inner[2] <= outer[0] + outer[2] + SLACK and inner[1] + inner[3] <= outer[1] + outer[3] + SLACK)


def apart(a, b):
    return (a[0] + a[2] <= b[0] + SLACK or b[0] + b[2] <= a[0] + SLACK
            or a[1] + a[3] <= b[1] + SLACK or b[1] + b[3] <= a[1] + SLACK)


def is_arrow_part(model, cell_id):
    """True for an arrow, the rule inside a box, and a text that sits on an arrow."""
    cell = model[cell_id]
    return cell['edge'] or model.get(cell['parent'], {'edge': False})['edge']


def number(value):
    return f'{value:.2f}'.rstrip('0').rstrip('.').replace('.', ',')


def check():
    if not os.path.exists(CHROMIUM):
        sys.exit(f'{CHROMIUM} finns inte, och utan den kan bilden inte mätas')
    term_of = terms()
    too_tall = outside = on_another = mismatched = 0
    fonts = set()
    with tempfile.TemporaryDirectory() as folder:
        drawings = {}
        for path, def_id in THIRTEEN:
            if path not in drawings:
                svg_text = open(path, encoding='utf-8').read()
                drawings[path] = (model_of(svg_text), image_of(svg_text, folder))
            model, image = drawings[path]
            group = model[def_id]['parent']
            concept = re.sub(r'<[^>]+>', '', model[def_id[:-4] + '-id']['value']).strip()
            name = f'{path}: {term_of.get(concept, "?")} ({concept}), cell {def_id}'
            cell = image[def_id]
            box_x, box_y, width, height = cell['box']
            fonts.add(cell['font'])
            print(f'{name}: texten är {number(cell["textHeight"])} hög i webbläsaren och {number(cell["fallbackHeight"])} i reservbilden, '
                  f'cellen är {number(height)} hög')

            # 1. The text against the cell that clips it.
            for label, text_height in (('i webbläsaren', cell['textHeight']), ('i reservbilden', cell['fallbackHeight'])):
                if text_height > height + SLACK:
                    too_tall += 1
                    print(f'    TEXTEN ÄR HÖGRE ÄN CELLEN {label}: {number(text_height)} mot {number(height)}')

            # 2. The cell within its box: the largest drawn shape of the cell's own group.
            siblings = [i for i in model if model[i]['parent'] == group and i != def_id and not is_arrow_part(model, i) and 'box' in image.get(i, {})]
            frames = [i for i in siblings if not model[i]['style'].startswith('text')]
            if not frames:
                sys.exit(f'{name}: gruppen {group} har ingen ritad ruta')
            box_id = max(frames, key=lambda i: image[i]['box'][2] * image[i]['box'][3])
            box = image[box_id]['box']
            if not inside(cell['box'], box):
                outside += 1
                print(f'    CELLEN GÅR UTANFÖR SIN RUTA: cellen {[number(v) for v in cell["box"]]}, rutan {box_id} {[number(v) for v in box]} (x, y, bredd, höjd)')

            # 3. The cell on another cell, and the box on a cell outside its own group.
            for other_id, other in sorted(image.items()):
                if other_id in (def_id, box_id) or other_id not in model or 'box' not in other or is_arrow_part(model, other_id):
                    continue
                if model[other_id]['parent'] == group:
                    if not apart(cell['box'], other['box']):
                        on_another += 1
                        print(f'    CELLEN LIGGER PÅ EN ANNAN CELL: {other_id} {[number(v) for v in other["box"]]}, cellen {[number(v) for v in cell["box"]]} (x, y, bredd, höjd)')
                elif not apart(box, other['box']) and not inside(box, other['box']):
                    on_another += 1
                    print(f'    RUTAN LIGGER PÅ EN ANNAN CELL: {other_id} {[number(v) for v in other["box"]]}, rutan {box_id} {[number(v) for v in box]} (x, y, bredd, höjd)')

            # 4. The image against the embedded model.
            if (width, height) != model[def_id]['size'] or cell['clipHeight'] != height:
                mismatched += 1
                print(f'    BILDEN OCH DEN INBÄDDADE RITNINGEN HAR OLIKA MÅTT: bilden {number(width)} × {number(height)}, klipper vid {number(cell["clipHeight"])}, '
                      f'den inbäddade ritningen {" × ".join(number(v) for v in model[def_id]["size"])}')

    print(f'\nmätta definitionsceller: {len(THIRTEEN)} i {len(drawings)} ritningar, typsnitt i bilden: {", ".join(sorted(fonts))}')
    print(f'texter högre än cellen: {too_tall}')
    print(f'celler utanför sin ruta: {outside}')
    print(f'celler eller rutor som ligger på en annan cell: {on_another}')
    print(f'celler med olika mått i bilden och i den inbäddade ritningen: {mismatched}')
    return too_tall + outside + on_another + mismatched


if __name__ == '__main__':
    failures = check()
    print('\nHÅLLER: hela definitionen ryms i var och en av de tretton cellerna, och ingen cell eller ruta ligger på en annan.' if not failures
          else f'\nFALLER: {failures} fel.')
    sys.exit(1 if failures else 0)
