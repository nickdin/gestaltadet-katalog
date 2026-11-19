"""issue-199-enhet.py: prov för ärende #199, kört från lagrets rot.

    python3 docs/acceptance-shots/issue-199-enhet.py <tom mapp utanför lagret>

Provet publicerar lagret det körs i till mappen, med `interlingua publish`, och läser den publicerade
sidan Formbibliotek. Den publicerade sidan märker varje ord som är en term i katalogen: ordet får en
streckad understrykning och en ruta med begreppets definition. Provet faller (slutkod 1) om

- sidan inte är publicerad, på adressen PAGE,
- steget som säger draw.io:s menyval inte står på sidan, eller saknar menyordet Enhet,
- något ord i det steget är märkt som en term: steget säger bara menyord, och ett menyord är ingen term,
- något ord på sidan är märkt som Enhet (C-080): sidan talar aldrig om katalogens begrepp Enhet.

Provet skriver också ut steget som läsaren ser det och varje märkt ord på sidan med sitt begrepp.

Programmet hittas i INTERLINGUA i miljön, annars i ~/Devbox/interlingua/.venv/bin/interlingua.
"""
import html
import os
import re
import subprocess
import sys
from pathlib import Path

PAGE = 'document/docs/formbibliotek.md/index.html'
CONCEPT = 'C-080'  # Enhet (C-080), begreppet som menyordet togs för
MENU_WORD = 'Enhet'  # draw.io:s menyval för datorn som filen ligger på
STEP_PHRASE = 'Öppna bibliotek från'  # menyvalet som bara steget med menyorden säger
# Ett märkt ord: ordet, sedan rutan med länken till begreppets sida och begreppets namn.
MARK = re.compile(r'<span class="term-mark"[^>]*>(.*?)<span class="term-box"[^>]*><a href="([^"]*)">(.*?)</a>', re.DOTALL)
BOX = re.compile(r'<span class="term-box"[^>]*>.*?</span>\s*</span>', re.DOTALL)  # rutan, med definitionen i sig
ITEM = re.compile(r'<li>(.*?)</li>', re.DOTALL)


def publish(folder: Path) -> None:
    program = os.environ.get('INTERLINGUA') or str(Path.home() / 'Devbox/interlingua/.venv/bin/interlingua')
    done = subprocess.run([program, 'publish', '.', str(folder)], capture_output=True, text=True)
    if done.returncode != 0:
        sys.exit(f'publish gick inte igenom (slutkod {done.returncode}):\n{done.stdout}{done.stderr}')


def words(markup: str) -> str:
    """Markeringen som ren text, med teckenkoderna utbytta."""
    return html.unescape(re.sub(r'<[^>]+>', '', markup)).strip()


def marks(markup: str) -> list[tuple[str, str, str]]:
    """Varje märkt ord i markeringen som (ordet, begreppets namn, adressen till begreppets sida)."""
    return [(words(word), words(name), html.unescape(href)) for word, href, name in MARK.findall(markup)]


def is_concept(href: str, concept: str) -> bool:
    """Om adressen leder till begreppets sida: begreppets id är ett helt led i adressen."""
    return concept in [part for part in href.split('/') if part]


def as_read(markup: str) -> str:
    """Markeringen som läsaren ser den: rutorna är dolda tills läsaren pekar på ordet, så de tas bort."""
    marked = re.sub(r'<span class="term-mark"[^>]*>', '', markup)
    return words(BOX.sub('</span>', marked))


def main() -> int:
    if len(sys.argv) != 2:
        sys.exit(__doc__)
    folder = Path(sys.argv[1]).resolve()
    publish(folder)
    failures: list[str] = []

    page = folder / PAGE
    if not page.is_file():
        print(f'FALLER:\n- {PAGE}: sidan är inte publicerad')
        return 1
    text = page.read_text(encoding='utf-8')
    print(f'Sidan finns: {PAGE}')

    steps = [item for item in ITEM.findall(text) if STEP_PHRASE in words(item)]
    if len(steps) != 1:
        failures.append(f'{PAGE}: {len(steps)} steg säger "{STEP_PHRASE}", väntat ett enda')
    for step in steps:
        print(f'Steget som läsaren ser det: {as_read(step)}')
        if not re.search(rf'\b{MENU_WORD}\b', as_read(step)):
            failures.append(f'{PAGE}: steget saknar menyordet {MENU_WORD}')
        in_step = marks(step)
        print(f'Märkta ord i steget: {len(in_step)}')
        for word, name, _ in in_step:
            failures.append(f'{PAGE}: menyordet "{word}" i steget är märkt som termen {name}')

    all_marks = marks(text)
    print(f'Märkta ord på sidan: {len(all_marks)}')
    for word, name, href in all_marks:
        print(f'  "{word}" märkt som {name} ({href})')
    as_concept = [word for word, _, href in all_marks if is_concept(href, CONCEPT)]
    print(f'Ord märkta som Enhet ({CONCEPT}): {len(as_concept)}')
    if as_concept:
        failures.append(f'{PAGE}: {len(as_concept)} ord är märkta som Enhet ({CONCEPT}): {", ".join(as_concept)}')

    if failures:
        print('FALLER:')
        for failure in failures:
            print(f'- {failure}')
        return 1
    print('HÅLLER')
    return 0


if __name__ == '__main__':
    sys.exit(main())
