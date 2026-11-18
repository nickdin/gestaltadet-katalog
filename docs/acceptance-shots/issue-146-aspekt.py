"""Prov för ärende #146: ritningarna visar att Styrmedel (C-015) kan ta sikte på Aspekt (C-004).

Körs från katalogens rot utan argument: python3 docs/acceptance-shots/issue-146-aspekt.py

Provet svarar på fyra frågor och slutar med slutkod 0 bara om alla fyra håller.

1. Vilka ritningar under layout/ visar Aspekt (C-004) tillsammans med Styrmedel (C-015)
   eller en sort av styrmedel, och har var och en av dem pilen "kan ta sikte på"?
   Pilen ska vara en association. Den ska gå från Styrmedel när Styrmedel är med i
   ritningen, annars från en sort av styrmedel (README.md, regeln om ärvda relationer).
   De tre ritningar som ärendet ändrar ska alla ha pilen.
2. Säger bilden som sajten visar samma sak som den inbäddade draw.io-ritningen?
3. Har varje pil i de ändrade ritningarna en relation i lagret?
4. Är varje cell som fanns i de ändrade ritningarna på basen oförändrad? Facit är
   issue-146-facit.json, ritningarna avkodade ur basen. Nya celler får bara vara
   rutan Aspekt och den nya pilen.

Med argumentet --skriv-facit skriver provet facit ur arbetskopian i stället för att pröva.
"""
import html
import json
import re
import sys
import xml.etree.ElementTree as ET
from pathlib import Path

ROOT = Path('.')
FACIT = ROOT / 'docs/acceptance-shots/issue-146-facit.json'
STYRMEDEL, ASPEKT = 'C-015', 'C-004'
LABEL = 'kan ta sikte på'

# Ritningarna som ärendet ändrar -> cellerna som får vara nya i dem.
ASPEKT_BOX = {'g-aspekt', 'b-g-aspekt', 't-g-aspekt', 'r-g-aspekt', 'g-aspekt-id', 'g-aspekt-def'}
CHANGED = {
    'layout/Styrning/Styrmedel översikt.drawio.svg': ASPEKT_BOX | {'e-styrmedel-aspekt', 'l-e-styrmedel-aspekt'},
    'layout/Principer/Begreppsmodell arkitekturprinciper.drawio.svg': ASPEKT_BOX | {'e-styrmedel-aspekt', 'l-e-styrmedel-aspekt'},
    'layout/Principer/Princip detalj.drawio.svg': ASPEKT_BOX | {'e-princip-aspekt', 'l-e-princip-aspekt'},
}

# Lagret skriver "fastställs av" (C-183) som nyckeln decided_by på styrmedlets sort. Värdet är slaget
# av beskrivning som fastställer: reference är Referensarkitektur (C-041).
DECIDED_BY = {'reference': 'C-041'}

errors = []


def fail(message):
    errors.append(message)
    print('  FEL: ' + message)


def plain(value):
    """Cellens text utan märkning, läsriktningens triangel och extra blanksteg."""
    text = html.unescape(re.sub(r'<[^>]+>', ' ', value or ''))
    return ' '.join(re.sub('[▶◀▲▼]', ' ', text).split())


def read_store():
    """Lagrets begrepp: id -> term, överordnat begrepp, helhet och associationer."""
    store = {}
    for path in sorted((ROOT / 'concepts').glob('C-*.md')):
        front = path.read_text(encoding='utf-8').split('---')[1]
        concept = {'term': '', 'generic': [], 'partitive': [], 'aggregation': [], 'associative': [], 'decided_by': []}
        key = target = None
        for line in front.splitlines():
            top = re.match(r'^([a-z_]+):\s*(.*)$', line)
            if top:
                key, rest = top.groups()
                if key == 'term':
                    concept['term'] = rest.strip('\'"')
                if key == 'decided_by':
                    concept['decided_by'] = [DECIDED_BY.get(kind, kind) for kind in re.findall(r'[a-z_]+', rest)]
                ref = re.search(r'\[\[(C-\d+)', rest)
                if ref and key in concept:
                    concept[key].append(ref.group(1))
                continue
            ref = re.search(r'\[\[(C-\d+)', line)
            if ref and key in ('generic', 'partitive', 'aggregation') and 'concept:' not in line:
                concept[key].append(ref.group(1))
            elif ref and 'concept:' in line:
                target = ref.group(1)
                if key in ('partitive', 'aggregation'):
                    concept[key].append(target)
            elif key == 'associative' and target and re.match(r'^\s+label:', line):
                concept['associative'].append((line.split(':', 1)[1].strip().strip('\'"'), target))
        store[path.name.split(' ')[0]] = concept
    return store


def ancestors(store, concept_id):
    """Begreppets överordnade begrepp, närmast först."""
    found, queue = [], list(store.get(concept_id, {}).get('generic', []))
    while queue:
        parent = queue.pop(0)
        if parent not in found:
            found.append(parent)
            queue.extend(store.get(parent, {}).get('generic', []))
    return found


def model_of(path):
    """Den inbäddade draw.io-ritningens celler: id -> cell."""
    content = ET.parse(path).getroot().attrib['content']
    return {cell.get('id'): cell for cell in ET.fromstring(content).iter('mxCell')}


def picture_of(path):
    """Texten i bilden som sajten visar, utan den inbäddade ritningen."""
    svg = re.sub(r'content="[^"]*"', '', path.read_text(encoding='utf-8'), count=1)
    return html.unescape(re.sub(r'<[^>]+>', ' ', svg))


def boxes_of(cells):
    """Rutorna med begreppets id: gruppens cell-id -> C-id."""
    return {cell.get('parent'): plain(cell.get('value'))
            for cell in cells.values() if re.fullmatch(r'C-\d+', plain(cell.get('value')))}


def kind_of(style):
    if 'endArrow=block' in style or 'startArrow=block' in style:
        return 'är en typ av'
    if 'diamondThin' in style:
        return 'består av' if 'startFill=1' in style or 'endFill=1' in style else 'har'
    if 'dashed=1' in style:
        return 'beroende'
    return 'association'


def arrows_of(cells):
    """Pilarna mellan två rutor: (pilens id, från, till, slag, text). Från och till är C-id eller None."""
    boxes = boxes_of(cells)

    def box(cell_id):
        cell = cells.get(cell_id)
        if cell is None:
            return None
        return boxes.get(cell_id) or boxes.get(cell.get('parent'))

    arrows = []
    for cell_id, cell in cells.items():
        if not (cell.get('edge') and cell.get('source') and cell.get('target')):
            continue
        names = [plain(kid.get('value')) for kid in cells.values()
                 if kid.get('parent') == cell_id and re.search('[A-Za-zÅÄÖåäö]{2}', kid.get('value') or '')]
        arrows.append((cell_id, box(cell.get('source')), box(cell.get('target')),
                       kind_of(cell.get('style') or ''), ' '.join(names).lower()))
    return arrows


def named(store, concept_id):
    return f"{store[concept_id]['term']} ({concept_id})" if concept_id in store else str(concept_id)


def relation_in_store(store, shown, source, target, kind, label):
    """Säger var i lagret pilens relation står, eller None. Läsriktningen prövas åt båda håll."""
    for a, b in ((source, target), (target, source)):
        for subject in [a] + ancestors(store, a):
            concept = store.get(subject)
            if concept is None:
                continue
            hit = ((kind == 'är en typ av' and b in concept['generic'])
                   or (kind == 'består av' and b in concept['partitive'])
                   or (kind == 'har' and b in concept['aggregation'] + concept['partitive'])
                   or (kind in ('association', 'beroende') and (label, b) in concept['associative'])
                   or (kind == 'association' and label == 'fastställs av' and b in concept['decided_by']))
            if hit and subject == a and label == 'fastställs av' and b in concept['decided_by']:
                return 'finns i lagret, som decided_by'
            if hit and subject == a:
                return 'finns i lagret'
            if hit and kind != 'är en typ av':
                where = 'som är med i ritningen' if subject in shown else 'som inte är med i ritningen'
                return f'ärvd från {named(store, subject)}, {where}'
    return None


def canonical(cell):
    """Cellen hel, med attributen i fast ordning, så att två avkodningar går att jämföra."""
    def walk(node):
        return [node.tag, sorted(node.attrib.items()), [walk(child) for child in node]]
    return json.dumps(walk(cell), ensure_ascii=False)


def write_facit():
    facit = {name: {cell_id: canonical(cell) for cell_id, cell in model_of(ROOT / name).items()}
             for name in CHANGED}
    FACIT.write_text(json.dumps(facit, ensure_ascii=False, indent=0) + '\n', encoding='utf-8')
    print(f'facit skrivet: {FACIT}, ' + ', '.join(f'{len(cells)} celler' for cells in facit.values()))


def main():
    store = read_store()
    sorts = {c for c in store if STYRMEDEL in ancestors(store, c)}
    drawings = sorted((ROOT / 'layout').rglob('*.drawio.svg'))

    print(f'1. Ritningar som visar Aspekt ({ASPEKT}) och Styrmedel ({STYRMEDEL}) eller en sort av styrmedel')
    with_arrow = []
    for path in drawings:
        name = path.as_posix()
        cells = model_of(path)
        shown = set(boxes_of(cells).values())
        family = sorted(shown & (sorts | {STYRMEDEL}))
        if not family:
            continue
        if ASPEKT not in shown:
            print(f'- {name}: visar {", ".join(named(store, c) for c in family)} men inte Aspekt ({ASPEKT})')
            continue
        print(f'- {name}: visar Aspekt ({ASPEKT}) och {", ".join(named(store, c) for c in family)}')
        hits = [(a, b, kind, label) for _, a, b, kind, label in arrows_of(cells)
                if ASPEKT in (a, b) and ({a, b} - {ASPEKT}) & set(family)]
        for a, b, kind, label in hits:
            print(f'  pil: {named(store, a)} --[{label}, {kind}]--> {named(store, b)}')
        want = STYRMEDEL if STYRMEDEL in shown else None
        good = [h for h in hits if h[1] == ASPEKT and h[2] == 'association' and h[3] == LABEL
                and (h[0] == want if want else h[0] in sorts)]
        if len(good) == 1 and len(hits) == 1:
            origin = 'Styrmedel' if want else 'en sort av styrmedel, eftersom Styrmedel inte är med i ritningen'
            print(f'  PILEN FINNS: en association "{LABEL}" från {origin}')
            with_arrow.append(name)
        else:
            fail(f'{name} visar båda men har inte exakt en pil "{LABEL}" från '
                 + ('Styrmedel (C-015)' if want else 'en sort av styrmedel') + f': {len(hits)} pilar, {len(good)} rätta')
    print(f'  ritningar med pilen: {len(with_arrow)}')
    for name in CHANGED:
        if name not in with_arrow:
            fail(f'{name} har inte pilen "{LABEL}" till Aspekt ({ASPEKT})')

    print('2. Bilden som sajten visar')
    for name in with_arrow:
        text = picture_of(ROOT / name)
        missing = [word for word in (ASPEKT, store[ASPEKT]['term'], LABEL.upper()) if word not in text]
        definition = definition_of(ASPEKT)
        if not all(word in text for word in definition.split()):
            missing.append('definitionens alla ord')
        if missing:
            fail(f'bilden av {name} saknar: {", ".join(missing)}')
        else:
            print(f'- {name}: bilden bär {ASPEKT}, Aspekt, {LABEL.upper()} och definitionens alla ord')

    print('3. Pilarna i de ändrade ritningarna mot lagret')
    for name in CHANGED:
        cells = model_of(ROOT / name)
        shown = set(boxes_of(cells).values())
        arrows = arrows_of(cells)
        lacking = 0
        print(f'- {name}: {len(arrows)} pilar mellan rutor')
        for cell_id, a, b, kind, label in sorted(arrows, key=lambda arrow: str(arrow)):
            if a is None or b is None:
                print(f'  {cell_id}: går till en ruta utan begrepps-id, prövas inte')
                continue
            where = relation_in_store(store, shown, a, b, kind, label)
            text = label if kind == 'association' else f'{kind}' + (f', text "{label}"' if label and label != kind else '')
            print(f'  {named(store, a)} --[{text}]--> {named(store, b)}: {where or "SAKNAS I LAGRET"}')
            if where is None:
                lacking += 1
                if cell_id in CHANGED[name]:
                    fail(f'den nya pilen {cell_id} i {name} saknar relation i lagret')
        print(f'  pilar utan relation i lagret: {lacking}')

    print('4. Cellerna mot facit, ritningarna avkodade ur basen')
    facit = json.loads(FACIT.read_text(encoding='utf-8'))
    for name, allowed in CHANGED.items():
        cells = {cell_id: canonical(cell) for cell_id, cell in model_of(ROOT / name).items()}
        before = facit[name]
        removed = sorted(set(before) - set(cells))
        added = sorted(set(cells) - set(before))
        changed = sorted(c for c in before if c in cells and before[c] != cells[c])
        print(f'- {name}: {len(before)} celler i facit, {len(before) - len(removed) - len(changed)} oförändrade, '
              f'{len(changed)} ändrade, {len(removed)} borttagna, {len(added)} nya')
        if added:
            print(f'  nya: {", ".join(added)}')
        for cell_id in changed:
            fail(f'{name}: cellen {cell_id} är ändrad mot facit')
        for cell_id in removed:
            fail(f'{name}: cellen {cell_id} är borttagen')
        for cell_id in added:
            if cell_id not in allowed:
                fail(f'{name}: den nya cellen {cell_id} är varken rutan Aspekt eller den nya pilen')

    print(f'FALLER: {len(errors)} fel.' if errors else 'HÅLLER')
    return 1 if errors else 0



def definition_of(concept_id):
    """Definitionen ordagrant ur begreppets fil."""
    path = next((ROOT / 'concepts').glob(concept_id + ' *.md'))
    return re.search(r'^\*\*Definition:\*\* (.+)$', path.read_text(encoding='utf-8'), re.M).group(1).strip()


if __name__ == '__main__':
    if sys.argv[1:] == ['--skriv-facit']:
        write_facit()
    else:
        sys.exit(main())
