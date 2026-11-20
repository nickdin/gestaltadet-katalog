"""Hjälpskript för ärende #198: skriver två ändrade kopior av de tre ritningarna, var och en med ett fel i bilden.

Körs från lagrets rot: python3 docs/acceptance-shots/issue-198-kopior.py MÅL

MÅL är en mapp utanför lagret. Skriptet skriver två mappar i MÅL, var och en med de tre ritningarna ur layout/Exempel:

- pil-genom-ruta: i Analysfunktionen karta är pilen från Analysfunktionen till Datalagret dragen rakt ned genom
  rutorna Företrädare och Kopiorna i datalagret. De två andra ritningarna är oändrade.
- krympt-ruta: i Informationskartläggning steg är rutan för steg 2 krympt från 174 till 120 i höjd, kring samma mitt,
  så att texten klipps. De två andra ritningarna är oändrade.

Varje ändring görs i den inbäddade ritningen, och draw.io skriver sedan bilden på nytt, som när ritningen sparas.
Skriptet kräver därför draw.io, och xvfb-run på en maskin utan skärm. Det ändrar ingenting i lagret.

Provet docs/acceptance-shots/issue-198-bilden.py läser sedan var och en med --ritningar och ska falla på båda.
"""
import os
import re
import shutil
import subprocess
import sys
import xml.etree.ElementTree as ET
from pathlib import Path

FOLDER = Path('layout/Exempel')
MAP = 'Analysfunktionen karta.drawio.svg'
MAP_FINDINGS = 'Analysfunktionen karta med fynd.drawio.svg'
STEPS = 'Informationskartläggning steg.drawio.svg'

# Pilen som dras om, och punkterna den går genom i kopian: rakt ned genom Företrädare och Kopiorna i datalagret.
ARROW = 'e-access-datalager'
ARROW_POINTS = [(615, 92), (615, 640), (497.5, 640), (497.5, 732)]

# Cellerna i rutan för steg 2 och hur mycket lägre var och en blir. Gruppen flyttas ned halva sänkningen, så att
# mitten ligger kvar och pilarna in och ut går rakt.
STEP_2 = {'group': 's1', 'frame': 'b-s1', 'text': 's1-def'}
SHRINK = 54


def diagram_of(path):
    """Den inbäddade ritningen som träd."""
    return ET.fromstring(ET.parse(path).getroot().attrib['content'])


def geometry_of(tree, cell_id):
    cells = [c for c in tree.iter('mxCell') if c.get('id') == cell_id]
    if len(cells) != 1:
        sys.exit(f'cellen "{cell_id}" finns {len(cells)} gånger i ritningen, inte en')
    return cells[0].find('mxGeometry')


def reroute_arrow(tree):
    geometry = geometry_of(tree, ARROW)
    for old in geometry.findall('Array'):
        geometry.remove(old)
    points = ET.SubElement(geometry, 'Array', {'as': 'points'})
    for x, y in ARROW_POINTS:
        ET.SubElement(points, 'mxPoint', {'x': f'{x:g}', 'y': f'{y:g}'})


def shrink_step_2(tree):
    for cell_id in STEP_2.values():
        geometry = geometry_of(tree, cell_id)
        geometry.set('height', f'{float(geometry.get("height")) - SHRINK:g}')
    group = geometry_of(tree, STEP_2['group'])
    group.set('y', f'{float(group.get("y")) + SHRINK / 2:g}')


def export(tree, original, target):
    """Skriver ritningen som en bild med ritningen inbäddad, med samma växlar och samma huvud som originalet."""
    source = target.with_suffix('').with_suffix('.drawio')
    source.write_text(ET.tostring(tree, encoding='unicode'), encoding='utf-8')
    command = ['drawio', '--no-sandbox', '--disable-gpu', '--export', '--format', 'svg', '--embed-diagram',
               '--svg-theme', 'light', '--output', str(target), str(source)]
    if not os.environ.get('DISPLAY'):
        command = ['xvfb-run', '-a'] + command
    target.unlink(missing_ok=True)  # en bild från en tidigare körning får inte gälla som den här körningens
    result = subprocess.run(command, capture_output=True, text=True, timeout=180)
    if result.returncode != 0 or not target.exists():
        sys.exit(f'draw.io skrev inte {target}: slutkod {result.returncode}\n{result.stderr}')
    source.unlink()
    # draw.io skriver ibland ett annat huvud än originalets; bildens bakgrund och färgschema tas från originalet.
    style = re.search(r'<svg [^>]*?style="([^"]*)"', original.read_text(encoding='utf-8')).group(1)
    svg = target.read_text(encoding='utf-8')
    target.write_text(re.sub(r'(<svg [^>]*?style=")[^"]*"', lambda m: f'{m.group(1)}{style}"', svg, count=1),
                      encoding='utf-8')


def main():
    if len(sys.argv) != 2:
        sys.exit('Användning: issue-198-kopior.py MÅL')
    target = Path(sys.argv[1])
    for name, drawing, change in (('pil-genom-ruta', MAP, reroute_arrow), ('krympt-ruta', STEPS, shrink_step_2)):
        folder = target / name
        folder.mkdir(parents=True, exist_ok=True)
        for unchanged in {MAP, MAP_FINDINGS, STEPS} - {drawing}:
            shutil.copyfile(FOLDER / unchanged, folder / unchanged)
        tree = diagram_of(FOLDER / drawing)
        change(tree)
        export(tree, FOLDER / drawing, folder / drawing)
        print(f'{folder}: {drawing} är ändrad, de två andra ritningarna är kopior')


main()
