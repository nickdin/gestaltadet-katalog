"""Prov för ärende #156: Lösningsstyrning ersätter Produktstyrning och Objektstyrning.

Körs från lagrets rot:

    python3 docs/acceptance-shots/issue-156-losningsstyrning.py

Provet visar sex saker och slutar med slutkod 1 och raden FALLER om någon av dem inte håller:

1. Inget begrepp, ingen mappning och inget exempel nämner det utgångna id:t C-048, och id:t står
   i retired-ids.yaml.
2. Orden produktstyrning och objektstyrning är avrådda ord på begreppet Lösningsstyrning.
3. Portfölj (C-011) väger Ram (C-210), och Initiativ (C-012) är en del av Portfölj (C-011).
4. Ritningen Styrning flöde saknar texten "styrobjekt: produkten" och pilorden PRODUKT och OBJEKT,
   och har rutan Lösningsstyrning med en pil LEVERABEL från Initiativstyrning.
5. Varje ruta i ritningen Mandat och ansvar begreppsmodell bär sitt begrepps definition, i den
   inbäddade ritningen och i bilden, och ritningen har rutorna och pilarna för Portfölj och Initiativ.
6. Varje pil som de två ritningarna hade på basen står kvar hel: källa, mål, text, stil, brytpunkter
   och de två rutornas läge. Bara de pilar ärendet nämner får vara borttagna eller tillagda.

Facit för punkt 6 är filen issue-156-facit.json. Den skrivs en gång ur basen:

    python3 docs/acceptance-shots/issue-156-losningsstyrning.py --skriv-facit <commit>
"""
import glob
import html
import json
import os
import re
import subprocess
import sys
import xml.etree.ElementTree as ET

FACIT = os.path.join(os.path.dirname(__file__), 'issue-156-facit.json')
RETIRED = 'C-048'
FLOW = 'layout/Styrning/Styrning flöde.drawio.svg'
MANDATE = 'layout/Styrning/Mandat och ansvar begreppsmodell.drawio.svg'
# The arrows the ticket names, by the text on them. Nothing else may be removed or added.
MAY_BE_REMOVED = {FLOW: {'PRODUKT', 'OBJEKT'}, MANDATE: set()}
MAY_BE_ADDED = {FLOW: {'LEVERABEL'}, MANDATE: {'VÄGER ▶', 'AGGREGERAR ▼'}}

faults = []


def fault(text):
    faults.append(text)
    print(f'  FEL: {text}')


def plain(markup):
    """A cell's or the image's text without markup and with single spaces."""
    return ' '.join(html.unescape(re.sub(r'<[^>]+>', ' ', markup)).split())


def model_of(svg_text):
    """The cells of the embedded draw.io model, by id."""
    model = ET.fromstring(ET.fromstring(svg_text).attrib['content'])
    return {cell.get('id'): cell for cell in model.iter('mxCell')}


def image_of(svg_text):
    """The visible image: the file without the embedded model."""
    return re.sub(r'content="[^"]*"', '', svg_text, count=1)


def shown(svg_text, cell_id):
    """The text the visible image carries for one cell, or None when it carries none."""
    image = image_of(svg_text)
    start = image.find(f'<g data-cell-id="{cell_id}">')
    if start < 0:
        return None
    end = image.find('<g data-cell-id="', start + 1)
    text = re.search(r'<foreignObject.*?</foreignObject>', image[start:end if end > 0 else len(image)], re.S)
    return None if text is None else plain(text.group(0))


def geometry(cell):
    found = cell.find('mxGeometry')
    return None if found is None else ET.tostring(found, encoding='unicode').strip()


def place(cells, cell_id):
    """Where a box stands: its own geometry and that of every group around it."""
    chain = []
    while cell_id in cells and cells[cell_id].find('mxGeometry') is not None:
        chain.append(geometry(cells[cell_id]))
        cell_id = cells[cell_id].get('parent')
    return chain


def arrows_of(svg_text):
    """Every arrow that joins two boxes, whole, keyed by its id."""
    cells = model_of(svg_text)
    arrows = {}
    for cell_id, cell in cells.items():
        if cell.get('edge') != '1' or cell.get('source') is None or cell.get('target') is None:
            continue
        labels = sorted(
            (plain(c.get('value', '')), c.get('style'), geometry(c))
            for c in cells.values() if c.get('parent') == cell_id
        )
        arrows[cell_id] = {
            'source': cell.get('source'),
            'target': cell.get('target'),
            'style': cell.get('style'),
            'geometry': geometry(cell),
            'labels': [list(label) for label in labels],
            'source-place': place(cells, cell.get('source')),
            'target-place': place(cells, cell.get('target')),
        }
    return arrows


def label_of(arrow):
    return ' / '.join(label[0] for label in arrow['labels']) or '(utan text)'


def box_of(cells, cell_id):
    """The text of the box a cell belongs to: every text cell in the same group."""
    group = cells[cell_id].get('parent')
    return [plain(c.get('value', '')) for c in cells.values() if c.get('parent') == group and plain(c.get('value', ''))]


def write_facit(commit):
    facit = {}
    for path in (FLOW, MANDATE):
        svg_text = subprocess.run(['git', 'show', f'{commit}:{path}'], check=True, capture_output=True, text=True).stdout
        facit[path] = arrows_of(svg_text)
    json.dump({'commit': commit, 'drawings': facit}, open(FACIT, 'w', encoding='utf-8'), ensure_ascii=False, indent=1, sort_keys=True)
    print(f'facit skrivet ur {commit}: ' + ', '.join(f'{len(arrows)} pilar i {os.path.basename(path)}' for path, arrows in facit.items()))


def front_matter(path):
    return open(path, encoding='utf-8').read().split('\n---\n', 1)[0]


def concept_file(cid):
    found = glob.glob(f'concepts/{cid} *.md')
    return found[0] if found else None


def retired_id():
    print(f'1. Det utgångna id:t {RETIRED}')
    naming = []
    for path in sorted(glob.glob('concepts/*.md') + glob.glob('mapping/**/*', recursive=True) + glob.glob('docs/exempel/**/*', recursive=True)):
        if os.path.isfile(path) and RETIRED in open(path, encoding='utf-8', errors='replace').read():
            naming.append(path)
    print(f'  filer under concepts/, mapping/ och docs/exempel/ som nämner {RETIRED}: {len(naming)}')
    for path in naming:
        fault(f'{path} nämner {RETIRED}')
    line = re.search(rf'^{RETIRED}:.*$', open('retired-ids.yaml', encoding='utf-8').read(), re.M)
    print(f'  raden i retired-ids.yaml: {line.group(0) if line else "saknas"}')
    if line is None:
        fault(f'{RETIRED} står inte i retired-ids.yaml')


def deprecated_terms():
    print('2. De avrådda orden på Lösningsstyrning')
    path = next((p for p in glob.glob('concepts/C-*.md') if re.search(r'^term: Lösningsstyrning$', front_matter(p), re.M)), None)
    if path is None:
        fault('inget begrepp har termen Lösningsstyrning')
        return
    head = front_matter(path)
    print(f'  begreppet: {path}')
    print('  ' + re.search(r'^definition: .*$', head, re.M).group(0))
    if 'definition: objektbaserad styrning där styrobjektet är en lösning\n' not in head + '\n':
        fault('definitionen är inte "objektbaserad styrning där styrobjektet är en lösning"')
    terms = re.findall(r'^  - term: (.*)\n((?:    .*\n)*)', head + '\n', re.M)
    for word in ('produktstyrning', 'objektstyrning'):
        status = next((re.search(r'status: (\S+)', rest) for term, rest in terms if term.lower() == word), None)
        print(f'  {word}: {status.group(0) if status else "ingen status eller inget sådant ord"}')
        if status is None or status.group(1) != 'deprecated':
            fault(f'{word} är inte ett avrått ord på begreppet')
    if not re.search(r"concept: '\[\[C-055 Lösning\]\]'\n    label: avgränsas av", head):
        fault('begreppet avgränsas inte av Lösning (C-055)')


def portfolio_relations():
    print('3. Portfölj (C-011) och dess två relationer')
    head = front_matter(concept_file('C-011'))
    weighs = re.search(r"concept: '\[\[C-210 Ram\]\]'\n    label: väger", head)
    print(f'  Portfölj (C-011) väger Ram (C-210): {"står i concepts/C-011" if weighs else "saknas"}')
    if not weighs:
        fault('Portfölj (C-011) har ingen relation väger till Ram (C-210)')
    part = re.search(r"^partitive: '\[\[C-011 Portfölj\]\]'$", front_matter(concept_file('C-012')), re.M)
    print(f'  Initiativ (C-012) är en del av Portfölj (C-011): {"står i concepts/C-012" if part else "saknas"}')
    if not part:
        fault('Initiativ (C-012) är inte en del av Portfölj (C-011)')


def flow_drawing():
    print('4. Ritningen Styrning flöde')
    svg_text = open(FLOW, encoding='utf-8').read()
    cells = model_of(svg_text)
    in_model = [plain(c.get('value', '')) for c in cells.values()]
    in_image = plain(image_of(svg_text))
    for text in ('styrobjekt: produkten', 'PRODUKT', 'OBJEKT', 'Produktstyrning', 'Objektstyrning'):
        model_hits = sum(1 for value in in_model if value == text)
        image_hits = len(re.findall(rf'(?<![\wåäöÅÄÖ]){re.escape(text)}(?![\wåäöÅÄÖ])', in_image))
        print(f'  "{text}": {model_hits} celler i den inbäddade ritningen, {image_hits} träffar i bilden')
        if model_hits or image_hits:
            fault(f'Styrning flöde bär texten "{text}"')
    arrows = arrows_of(svg_text)
    found = [a for a in arrows.values() if label_of(a) == 'LEVERABEL']
    for arrow in found:
        print(f'  pilen LEVERABEL går från {box_of(cells, arrow["source"])} till {box_of(cells, arrow["target"])}')
    good = [a for a in found if box_of(cells, a['source'])[:1] == ['Initiativstyrning'] and box_of(cells, a['target']) == ['Lösningsstyrning', 'styrobjekt: lösningen']]
    if len(found) != 1 or len(good) != 1:
        fault('Styrning flöde har inte exakt en pil LEVERABEL från Initiativstyrning till rutan "Lösningsstyrning – styrobjekt: lösningen"')
    for text in ('Lösningsstyrning', 'LEVERABEL'):
        if text not in in_image:
            fault(f'bilden av Styrning flöde visar inte "{text}"')


def mandate_drawing():
    print('5. Ritningen Mandat och ansvar begreppsmodell')
    svg_text = open(MANDATE, encoding='utf-8').read()
    cells = model_of(svg_text)
    boxes = {}
    for cell_id in sorted(cells):
        def_id = cell_id[:-3] + '-def'
        if not cell_id.endswith('-id') or def_id not in cells:
            continue
        cid = plain(cells[cell_id].get('value', ''))
        boxes[cid] = cell_id[:-3]
        path = concept_file(cid)
        if path is None:
            fault(f'rutan {cid} har inget begrepp i lagret')
            continue
        text = open(path, encoding='utf-8').read()
        term = re.search(r'^term: (.*)$', text, re.M).group(1).strip('\'"')
        definition = re.search(r'^\*\*Definition:\*\*[ \t]*(.*)$', text, re.M).group(1).strip()
        in_model = cells[def_id].get('value', '')
        in_picture = shown(svg_text, def_id)
        verdict = 'samma definition' if in_model == definition and in_picture == definition else 'AVVIKER'
        print(f'  {term} ({cid}): {verdict}')
        if in_model != definition:
            fault(f'{term} ({cid}): rutan säger "{in_model}", begreppet har "{definition}"')
        if in_picture != definition:
            fault(f'{term} ({cid}): bilden säger "{in_picture}", begreppet har "{definition}"')
        if term not in box_of(cells, cell_id):
            fault(f'rutan {cid} bär inte termen {term}')
    print(f'  rutor med id och definition: {len(boxes)}')
    for cid, term in (('C-011', 'Portfölj'), ('C-012', 'Initiativ')):
        if cid not in boxes:
            fault(f'ritningen saknar rutan {term} ({cid})')
    arrows = arrows_of(svg_text)

    def box_id(cell_id):
        return next((cid for cid, group in boxes.items() if cells.get(cell_id) is not None and cells[cell_id].get('parent') == group), None)

    for label, source, target in (('VÄGER ▶', 'C-011', 'C-210'), ('AGGREGERAR ▼', 'C-011', 'C-012')):
        hits = [a for a in arrows.values() if label_of(a) == label and box_id(a['source']) == source and box_id(a['target']) == target]
        print(f'  pilen {label} från {source} till {target}: {len(hits)}')
        if len(hits) != 1:
            fault(f'ritningen har inte exakt en pil {label} från {source} till {target}')
        if label not in plain(image_of(svg_text)):
            fault(f'bilden visar inte pilordet {label}')


def compare_with_facit():
    facit = json.load(open(FACIT, encoding='utf-8'))
    print(f'6. Pilarna mot facit ur basen {facit["commit"]}')
    for path, golden in facit['drawings'].items():
        now = arrows_of(open(path, encoding='utf-8').read())
        changed = [i for i in golden if i in now and now[i] != golden[i]]
        removed = [i for i in golden if i not in now]
        added = [i for i in now if i not in golden]
        print(f'  {os.path.basename(path)}: {len(golden)} pilar i facit, {len(changed)} ändrade, '
              f'{len(added)} tillagda ({", ".join(label_of(now[i]) for i in added) or "inga"}), '
              f'{len(removed)} borttagna ({", ".join(label_of(golden[i]) for i in removed) or "inga"})')
        for i in changed:
            parts = [key for key in golden[i] if golden[i][key] != now[i][key]]
            fault(f'{path}: pilen {label_of(golden[i])} (cell {i}) är ändrad i {", ".join(parts)}')
        for i in removed:
            if label_of(golden[i]) not in MAY_BE_REMOVED[path]:
                fault(f'{path}: pilen {label_of(golden[i])} (cell {i}) är borttagen')
        for i in added:
            if label_of(now[i]) not in MAY_BE_ADDED[path]:
                fault(f'{path}: pilen {label_of(now[i])} (cell {i}) är tillagd och nämns inte i ärendet')


def main():
    if sys.argv[1:2] == ['--skriv-facit']:
        write_facit(sys.argv[2])
        return 0
    for step in (retired_id, deprecated_terms, portfolio_relations, flow_drawing, mandate_drawing, compare_with_facit):
        before = len(faults)
        step()
        print(f'  -> {"håller" if len(faults) == before else "faller"}')
    print(f'FALLER: {len(faults)} fel.' if faults else 'HÅLLER: alla sex delarna.')
    return 1 if faults else 0


if __name__ == '__main__':
    sys.exit(main())
