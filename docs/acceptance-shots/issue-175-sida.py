"""issue-175-sida.py: prov för ärende #175, kört från lagrets rot.

Läser sidan docs/informationskartlaggning.md och skriver ut vad den länkar till.
Provet faller (slutkod 1) om

- sidan saknas, eller inte står under documents: i settings.yaml,
- sidan har en uppgift om godkännande (authorship) i sitt huvud,
- en länk [[C-nnn ...]] pekar på ett begrepp som inte finns i concepts/, eller skriver begreppets term fel,
- ett begrepp som ärendet eller beslut 55 nämner med id inte är länkat på sidan,
- sidan inte har sju rubriker som börjar med Steg 1 till Steg 7,
- en av de fyra huvudfrågorna inte står ordagrant som i beslut 55,
- en mening i listan över exemplets fynd inte står ordagrant i exemplet,
- en av de tre ritningarna i layout/Exempel saknas eller inte nämns vid namn på sidan.
"""
import glob
import os
import re
import sys

PAGE = 'docs/informationskartlaggning.md'
EXAMPLE = 'docs/exempel/myndigheten-for-foreningsstod.md'
DECISION = glob.glob('docs/adr/0055-*.md')[0]
DRAWINGS = ['Analysfunktionen karta', 'Analysfunktionen karta med fynd', 'Informationskartläggning steg']

# Begreppen som ärendet #175 och beslut 55 nämner med id.
REQUIRED = ['C-019', 'C-060', 'C-071', 'C-085', 'C-107', 'C-165', 'C-167', 'C-168', 'C-185', 'C-186',
            'C-196', 'C-198', 'C-202', 'C-206', 'C-213']

# Meningen varje punkt i listan över exemplets fynd börjar med.
FINDING_OPENS_WITH = [
    'Informationssäkerhet: en avvikelse.',
    'Dataskydd: en bedömning.',
    'Offentlighet och arkiv: en bedömning.',
    'Informationsförsörjning: en bedömning.',
]

failures = []


def fail(message):
    failures.append(message)


def without_links(text):
    """Texten som läsaren ser: [[mål|ord]] blir ord, [[mål]] blir mål, och fetstil försvinner."""
    text = re.sub(r'\[\[[^\]|]+\|([^\]]*)\]\]', r'\1', text)
    text = re.sub(r'\[\[([^\]]+)\]\]', r'\1', text)
    return text.replace('**', '')


def sentences(text):
    return [part.strip() for part in re.split(r'(?<=[.?])\s+', text) if part.strip()]


if not os.path.exists(PAGE):
    fail(f'{PAGE}: sidan saknas')
    page = ''
else:
    page = open(PAGE, encoding='utf-8').read()

settings = open('settings.yaml', encoding='utf-8').read()
listed = re.search(r'^documents:\n((?:  - .*\n)+)', settings, re.M)
if not listed or f'  - {PAGE}\n' not in listed.group(1):
    fail(f'settings.yaml: {PAGE} står inte under documents:')

if page.startswith('---') or re.search(r'^authorship\s*:', page, re.M):
    fail(f'{PAGE}: sidan har ett huvud eller en uppgift om godkännande')

linked = {}
for target in re.findall(r'\[\[([^\]|]+)(?:\|[^\]]*)?\]\]', page):
    concept_id = target.split(' ')[0]
    files = glob.glob(f'concepts/{concept_id} *.md')
    if not files:
        fail(f'{PAGE}: länken [[{target}]] pekar på ett begrepp som inte finns')
        continue
    name = os.path.basename(files[0]).removesuffix('.md')
    if target not in (concept_id, name):
        fail(f'{PAGE}: länken [[{target}]] skriver inte begreppet som {name}')
    linked[concept_id] = name

for concept_id in REQUIRED:
    if concept_id not in linked:
        fail(f'{PAGE}: {concept_id} är inte länkat')

steps = re.findall(r'^## Steg (\d)', page, re.M)
if steps != [str(number) for number in range(1, 8)]:
    fail(f'{PAGE}: rubrikerna Steg 1 till Steg 7 finns inte i ordning, fann {steps}')

decision = open(DECISION, encoding='utf-8').read().replace('`', '')
questions = re.findall(r'^  - ([^:\n]+): (.+\?)$', decision, re.M)
if len(questions) != 4:
    fail(f'{DECISION}: fann {len(questions)} huvudfrågor, väntade fyra')
shown = without_links(page)
for perspective, question in questions:
    plain = re.sub(r' \(C-\d+\)', '', question)
    plain = plain[0].upper() + plain[1:]
    if plain not in shown:
        fail(f'{PAGE}: huvudfrågan för {perspective} står inte som i beslut 55: {plain}')

example = without_links(open(EXAMPLE, encoding='utf-8').read())
finding_lines = [without_links(line[2:]) for line in page.split('\n')
                 if line.startswith('- **') and any(opening in without_links(line) for opening in FINDING_OPENS_WITH)]
if len(finding_lines) != 4:
    fail(f'{PAGE}: listan över exemplets fynd har {len(finding_lines)} punkter, väntade fyra')
checked = 0
for line in finding_lines:
    for sentence in sentences(line):
        checked += 1
        if sentence not in example:
            fail(f'{PAGE}: meningen står inte i exemplet: {sentence}')

for drawing in DRAWINGS:
    if not os.path.exists(f'layout/Exempel/{drawing}.drawio.svg'):
        fail(f'layout/Exempel/{drawing}.drawio.svg: ritningen saknas')
    if drawing not in page:
        fail(f'{PAGE}: ritningen {drawing} nämns inte')

if failures:
    print('FALLER:')
    for failure in failures:
        print(f'- {failure}')
    sys.exit(1)

print(f'Länkade begrepp på {PAGE}: {len(linked)}')
for concept_id in sorted(linked):
    print(linked[concept_id])
print(f'Steg: {len(steps)}')
print(f'Huvudfrågor som står som i beslut 55: {len(questions)}')
print(f'Meningar om exemplets fynd som står ordagrant i exemplet: {checked}')
print(f'Ritningar som nämns vid namn: {len(DRAWINGS)}')
print('HÅLLER: sidan finns, länkar till varje begrepp den ska och följer beslut 55 och exemplet.')
