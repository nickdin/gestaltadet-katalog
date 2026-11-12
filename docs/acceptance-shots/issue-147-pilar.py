"""arrows.py FILE.drawio.svg TERM... — print every arrow in an editable drawing that touches one of the terms, as 'from --[name]--> to'."""
import sys, re, html
import xml.etree.ElementTree as ET
mx = ET.fromstring(ET.parse(sys.argv[1]).getroot().attrib['content'])
cells = {c.get('id'): c for c in mx.iter('mxCell')}
def term(box):
    group = cells[box].get('parent')
    return next(c.get('value') for c in cells.values() if c.get('parent') == group and 'fontSize=12' in (c.get('style') or ''))
lines = []
for i, c in cells.items():
    if c.get('edge') and c.get('source') and c.get('target'):
        name = ' '.join(html.unescape(re.sub('<[^>]+>', ' ', k.get('value') or '')) for k in cells.values() if k.get('parent') == i and re.search('[A-ZÅÄÖ]{2}', k.get('value') or ''))
        a, b = term(c.get('source')), term(c.get('target'))
        if {a, b} & set(sys.argv[2:]): lines.append(f'{a} --[{name}]--> {b}')
print('\n'.join(sorted(lines)) or '(inga)')
