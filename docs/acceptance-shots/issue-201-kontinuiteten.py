"""issue-201-kontinuiteten.py: prov för ärende #201, kört från lagrets rot.

    python3 docs/acceptance-shots/issue-201-kontinuiteten.py

Ärendet flyttar kontinuitetskravet och återställningstiden ur förteckningen över kraven på
behandlingarna till dokumentationen av kontinuiteten. Provet läser sidan Informationskartläggning,
begreppen, ordlistan och besluten. Ett stycke är en rad i filen. Provet faller (slutkod 1) om

- ett stycke på sidan, i begreppen eller i ordlistan som nämner förteckningen över kraven på
  behandlingarna också nämner kontinuiteten, återställningstiden eller hur länge något får stå still,
- sidan inte nämner dokumentationen av kontinuiteten,
- sidans exempel inte lägger både Genomföra ansökningsomgången och Föreningsregistret i
  dokumentationen av kontinuiteten,
- sidan inte säger att kartan saknar personalen och lokalerna,
- dokumentationen av kontinuiteten står som en punkt i en lista,
- arbetsnamnet förteckningen över kontinuitetskraven står kvar utanför beslut 64, som säger att
  det är ett arbetsnamn.

Provet skriver också ut varje stycke som nämner förteckningen över kraven på behandlingarna.
"""
import re
import sys
from pathlib import Path

PAGE = Path('docs/informationskartlaggning.md')
STATING_FILES = [PAGE, Path('CONTEXT.md'), *sorted(Path('concepts').glob('*.md'))]  # texterna som säger vad som gäller
DECISIONS = sorted(Path('docs/adr').glob('*.md'))
DECISION_DECLARING_WORKING_NAME = '0064-'  # beslut 64 säger själv att namnet är ett arbetsnamn
# Ärende #202 gav dokumentet namnet dokumentationen av kraven på behandlingarna. Provet läser båda namnen.
PROCESSING_REGISTER = re.compile(r'(förteckning(en)? över|dokumentation(en)? av) kraven på behandlingarna', re.IGNORECASE)
CONTINUITY_DOCUMENTATION = re.compile(r'dokumentationen av kontinuiteten', re.IGNORECASE)
WORKING_NAME = re.compile(r'förteckning(en)? över kontinuitetskrav', re.IGNORECASE)
CONTINUITY = re.compile(r'kontinuitet|återställningstid|stå still', re.IGNORECASE)

Paragraph = tuple[int, str]


def paragraphs(path: Path) -> list[Paragraph]:
    return [(number, line) for number, line in enumerate(path.read_text(encoding='utf-8').splitlines(), 1) if line.strip()]


def register_mixed_with_continuity() -> list[str]:
    failures = []
    print('Stycken som nämner förteckningen över kraven på behandlingarna:')
    for path in STATING_FILES:
        for number, text in paragraphs(path):
            if not PROCESSING_REGISTER.search(text):
                continue
            mixed = bool(CONTINUITY.search(text))
            print(f'  {path}:{number}: {"NÄMNER KONTINUITETEN" if mixed else "bara tillgänglighet och spårbarhet"}')
            print(f'    {text}')
            if mixed:
                failures.append(f'{path}:{number} lägger kontinuiteten i förteckningen över kraven på behandlingarna')
    return failures


def page_names_the_documentation(page: list[Paragraph]) -> list[str]:
    failures = []
    named = [(number, text) for number, text in page if CONTINUITY_DOCUMENTATION.search(text)]
    print(f'Stycken på sidan som nämner dokumentationen av kontinuiteten: {len(named)}')
    if not named:
        failures.append('sidan nämner inte dokumentationen av kontinuiteten')
    for number, text in named:
        if text.lstrip().startswith(('- ', '* ')):
            failures.append(f'{PAGE}:{number} har dokumentationen av kontinuiteten som en punkt i en lista')

    example = [number for number, text in named if 'Genomföra ansökningsomgången' in text and 'Föreningsregistret' in text]
    print(f'Exemplet med Genomföra ansökningsomgången och Föreningsregistret: rad {example or "saknas"}')
    if not example:
        failures.append('sidans exempel lägger inte båda raderna i dokumentationen av kontinuiteten')
    return failures


def page_says_what_the_map_lacks(page: list[Paragraph]) -> list[str]:
    lacks = [number for number, text in page if 'personalen och lokalerna' in text and 'bär kartan inte' in text]
    print(f'Stycket om att kartan inte bär personalen och lokalerna: rad {lacks or "saknas"}')
    return [] if lacks else ['sidan säger inte att kartan saknar personalen och lokalerna']


def working_name_left() -> list[str]:
    failures = []
    for path in [*STATING_FILES, *DECISIONS]:
        if path.name.startswith(DECISION_DECLARING_WORKING_NAME):
            continue
        for number, text in paragraphs(path):
            if WORKING_NAME.search(text):
                failures.append(f'{path}:{number} har kvar arbetsnamnet förteckningen över kontinuitetskraven')
    return failures


def main() -> int:
    page = paragraphs(PAGE)
    failures = [
        *register_mixed_with_continuity(),
        *page_names_the_documentation(page),
        *page_says_what_the_map_lacks(page),
        *working_name_left(),
    ]
    for failure in failures:
        print(f'  {failure}')
    print(f'FALLER: {len(failures)} fel.' if failures else 'HÅLLER')
    return 1 if failures else 0


if __name__ == '__main__':
    sys.exit(main())
