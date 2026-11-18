"""Prov för #183: begreppsrutorna i ritningarna bär begreppens definitioner.

Körs från lagrets rot:

    python3 docs/acceptance-shots/issue-183-rutor.py

Provet gör tre jämförelser och slutar med slutkod 0 bara om alla tre håller.

1. Varje ruta med id och definition i varje ritning under layout/ jämförs med
   raden "**Definition:**" i begreppets fil i concepts/. En ruta vars id inte
   är ett begrepp i lagret räknas inte, men den skrivs ut.
2. Samma rutor jämförs med bilden som sajten visar: texten som bilden bär för
   rutans definition ska vara begreppets definition.
3. De nio ritningar som ärendet pekar ut jämförs cell för cell med facit,
   issue-183-facit.json, som är ritningarna avkodade ur baskommitten. Bara en
   definitionstext och en rutas läge och storlek får skilja sig. Varje pil är
   densamma: källa, mål, text, stil och brytpunkter. Ingen cell är tillagd
   eller borttagen.

    python3 docs/acceptance-shots/issue-183-rutor.py --skriv-facit <commit>

skriver facit ur den commit som anges, och görs en gång, före ändringen.
"""
import glob
import html
import json
import os
import re
import subprocess
import sys
import xml.etree.ElementTree as ET

FACIT = os.path.join(os.path.dirname(__file__), 'issue-183-facit.json')
NINE = [
    'layout/Arkitektur/Arkitektur beskrivningens form.drawio.svg',
    'layout/Arkitektur/Arkitektur dimensioner.drawio.svg',
    'layout/Arkitektur/Arkitektur kedjan.drawio.svg',
    'layout/Arkitektur/Arkitekturnivå.drawio.svg',
    'layout/Information/Verksamhetsinformation begreppsmodell.drawio.svg',
    'layout/Principer/Begreppsmodell arkitekturprinciper.drawio.svg',
    'layout/Styrning/Mandat och ansvar begreppsmodell.drawio.svg',
    'layout/Styrning/Målstyrning begreppsmodell.drawio.svg',
    'layout/Styrning/Styrobjekt begreppsmodell.drawio.svg',
]
BOX_GEOMETRY = ('x', 'y', 'width', 'height')


def concepts():
    """Each concept's id mapped to its term and its "**Definition:**" line."""
    found = {}
    for path in glob.glob('concepts/C-*.md'):
        text = open(path, encoding='utf-8').read()
        cid = re.search(r'^id: (C-\d+)$', text, re.M).group(1)
        term = re.search(r'^term: (.*)$', text, re.M).group(1).strip('\'"')
        line = re.search(r'^\*\*Definition:\*\*[ \t]*(.*)$', text, re.M)
        if line is None:
            sys.exit(f'{path}: saknar raden **Definition:**')
        found[cid] = (term, line.group(1).strip())
    return found


def cells_of(svg_text):
    """Every cell of the embedded draw.io model, in a form that can be compared."""
    model = ET.fromstring(ET.fromstring(svg_text).attrib['content'])
    cells = {}
    for cell in model.iter('mxCell'):
        attributes = dict(cell.attrib)
        geometry = cell.find('mxGeometry')
        cells[attributes.pop('id')] = {
            'attributes': attributes,
            'geometry': None if geometry is None else ET.tostring(geometry, encoding='unicode').strip(),
            'box': None if geometry is None else {k: geometry.get(k) for k in BOX_GEOMETRY},
        }
    return cells


def plain(markup):
    """A cell's or the image's text without markup and with single spaces."""
    return ' '.join(html.unescape(re.sub(r'<[^>]+>', ' ', markup)).split())


def shown(svg_text, cell_id):
    """The text the visible image carries for one cell, or None when it carries none."""
    image = re.sub(r'content="[^"]*"', '', svg_text, count=1)
    start = image.find(f'<g data-cell-id="{cell_id}">')
    if start < 0:
        return None
    end = image.find('<g data-cell-id="', start + 1)
    block = image[start:end if end > 0 else len(image)]
    text = re.search(r'<foreignObject.*?</foreignObject>', block, re.S)
    return None if text is None else plain(text.group(0))


def is_arrow_part(cells, cell_id):
    """True for an arrow, the rule inside a box, and a text that sits on an arrow."""
    cell = cells[cell_id]['attributes']
    parent = cells.get(cell.get('parent'), {'attributes': {}})['attributes']
    return cell.get('edge') == '1' or parent.get('edge') == '1'


def write_facit(commit):
    facit = {}
    for path in NINE:
        svg_text = subprocess.run(['git', 'show', f'{commit}:{path}'], check=True, capture_output=True, text=True).stdout
        facit[path] = cells_of(svg_text)
    json.dump({'commit': commit, 'drawings': facit}, open(FACIT, 'w', encoding='utf-8'), ensure_ascii=False, indent=0, sort_keys=True)
    print(f'facit skrivet ur {commit}: {len(facit)} ritningar, {sum(len(c) for c in facit.values())} celler')


def compare_boxes(defined):
    print('1 och 2. Rutorna mot begreppsfilerna, i den inbäddade ritningen och i bilden')
    boxes = counted = deviations = image_deviations = 0
    skipped = {}
    for path in sorted(glob.glob('layout/**/*.drawio.svg', recursive=True)):
        svg_text = open(path, encoding='utf-8').read()
        cells = cells_of(svg_text)
        for cell_id in sorted(cells):
            def_id = cell_id[:-3] + '-def'
            if not cell_id.endswith('-id') or def_id not in cells:
                continue
            boxes += 1
            cid = plain(cells[cell_id]['attributes'].get('value', ''))
            if cid not in defined:
                skipped.setdefault(path, []).append(cid)
                continue
            counted += 1
            term, definition = defined[cid]
            in_model = cells[def_id]['attributes'].get('value', '')
            if in_model != definition:
                deviations += 1
                print(f'AVVIKER: {path}: {term} ({cid})\n    rutan säger:   {in_model}\n    begreppet har: {definition}')
            in_image = shown(svg_text, def_id)
            if in_image != definition:
                image_deviations += 1
                print(f'BILDEN AVVIKER: {path}: {term} ({cid})\n    bilden säger:  {in_image}\n    begreppet har: {definition}')
    for path, ids in sorted(skipped.items()):
        print(f'räknas inte, id:t är inget begrepp i lagret: {path}: {len(ids)} rutor ({", ".join(sorted(set(ids)))})')
    print(f'rutor med id och definition: {boxes}, varav {counted} för begrepp som finns i lagret')
    print(f'avvikelser i den inbäddade ritningen: {deviations}')
    print(f'avvikelser i bilden: {image_deviations}')
    return deviations + image_deviations


def compare_with_facit():
    facit = json.load(open(FACIT, encoding='utf-8'))
    print(f'\n3. De nio ritningarna cell för cell mot facit ur {facit["commit"]}')
    faults = 0
    for path in NINE:
        before = facit['drawings'][path]
        after = cells_of(open(path, encoding='utf-8').read())
        added, removed = sorted(set(after) - set(before)), sorted(set(before) - set(after))
        texts, moved, arrows, other = [], [], [], []
        for cell_id in sorted(set(before) & set(after)):
            old, new = before[cell_id], after[cell_id]
            if old == new:
                continue
            if is_arrow_part(before, cell_id) or is_arrow_part(after, cell_id):
                arrows.append(cell_id)
                continue
            old_attributes, new_attributes = dict(old['attributes']), dict(new['attributes'])
            if cell_id.endswith('-def') and old_attributes.get('value') != new_attributes.get('value'):
                texts.append(cell_id)
                old_attributes.pop('value', None), new_attributes.pop('value', None)
            if old['box'] != new['box']:
                moved.append(cell_id)
            # A changed position or size is only listed above: it never counts as a fault, whichever cell it is on
            # and however large it is. Only what is left of the geometry once position and size are set aside
            # must be the same.
            strip = lambda g: re.sub(r' (?:x|y|width|height)="[^"]*"', '', g or '')
            if old_attributes != new_attributes or strip(old['geometry']) != strip(new['geometry']):
                other.append(cell_id)
        faults += len(added) + len(removed) + len(arrows) + len(other)
        print(f'{path}: {len(after)} celler, {len(texts)} definitionstexter ändrade, {len(moved)} celler med ändrat läge eller ändrad storlek, '
              f'{len(arrows)} pilar ändrade, {len(added)} celler tillagda, {len(removed)} borttagna, {len(other)} andra ändringar')
        for label, ids in (('ändrad text', texts), ('ändrat läge eller ändrad storlek', moved), ('PIL ÄNDRAD', arrows),
                           ('TILLAGD', added), ('BORTTAGEN', removed), ('ANNAN ÄNDRING', other)):
            if ids:
                print(f'    {label}: {", ".join(ids)}')
    print(f'otillåtna ändringar mot facit: {faults}')
    return faults


if __name__ == '__main__':
    if sys.argv[1:2] == ['--skriv-facit']:
        write_facit(sys.argv[2])
        sys.exit(0)
    failures = compare_boxes(concepts()) + compare_with_facit()
    print('\nHÅLLER: varje ruta bär begreppets definition, och bara definitionstexter, lägen och storlekar skiljer mot facit.' if not failures
          else f'\nFALLER: {failures} fel.')
    sys.exit(1 if failures else 0)
