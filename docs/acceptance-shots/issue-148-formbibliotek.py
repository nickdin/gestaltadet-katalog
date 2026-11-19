"""issue-148-formbibliotek.py: prov för ärende #148, kört från lagrets rot.

    python3 docs/acceptance-shots/issue-148-formbibliotek.py <tom mapp utanför lagret>

Provet publicerar lagret det körs i till mappen, med `interlingua publish`, och läser de publicerade
filerna. Det faller (slutkod 1) om

- sidan om formbiblioteket inte är publicerad som dokument, på adressen PAGE,
- sidan inte säger adresserna till de två filerna, eller en av filerna inte är publicerad,
- sidan inte länkar till beslut 42, eller länken leder till en sida som inte är publicerad,
- startsidan inte länkar till sidan, eller länken leder till en sida som inte är publicerad,
- startsidan skiljer sig från basens startsida (BASE) med något annat än en enda tillagd rad:
  varje rad i basen ska stå kvar, oförändrad och i samma ordning.

Provet skriver också ut om adresserna till de två filerna är klickbara länkar på sidan eller bara
text. Det avgör inte utfallet, men ärendet frågar efter länkar, så svaret ska synas.

Programmet hittas i INTERLINGUA i miljön, annars i ~/Devbox/interlingua/.venv/bin/interlingua.
"""
import difflib
import html
import os
import re
import subprocess
import sys
from pathlib import Path

BASE = 'eb48f9d'  # main efter våg 2, basen ärendet byggdes på
START_PAGE = '.github/pages/index.html'
PAGE = 'document/docs/formbibliotek.md/index.html'
SITE = 'https://gestaltadet.se/katalog/'
LIBRARIES = ['library/drawio/library-drawio.xml', 'library/excalidraw/library-excalidraw.excalidrawlib']
DECISION = 'document/docs/adr/0042-'  # början på adressen till beslut 42:s sida, räknad från den publicerade mappen
ANCHOR = re.compile(r'<a\b[^>]*\shref="([^"]*)"[^>]*>(.*?)</a>', re.DOTALL)


def publish(folder: Path) -> None:
    program = os.environ.get('INTERLINGUA') or str(Path.home() / 'Devbox/interlingua/.venv/bin/interlingua')
    done = subprocess.run([program, 'publish', '.', str(folder)], capture_output=True, text=True)
    if done.returncode != 0:
        sys.exit(f'publish gick inte igenom (slutkod {done.returncode}):\n{done.stdout}{done.stderr}')


def anchors(text: str) -> list[tuple[str, str]]:
    """Varje länk i texten som (adress, ord), med teckenkoderna utbytta och taggarna i orden borttagna."""
    return [(html.unescape(href), re.sub(r'<[^>]+>', '', html.unescape(words)).strip()) for href, words in ANCHOR.findall(text)]


def reached(here: Path, href: str) -> Path:
    """Filen en relativ länk på sidan `here` leder till; en adress som slutar på / leder till mappens index.html."""
    target = (here.parent / href.split('#')[0]).resolve()
    return target / 'index.html' if href.endswith('/') or target.is_dir() else target


def main() -> int:
    if len(sys.argv) != 2:
        sys.exit(__doc__)
    folder = Path(sys.argv[1]).resolve()
    publish(folder)
    failures: list[str] = []

    page = folder / PAGE
    if not page.is_file():
        failures.append(f'{PAGE}: sidan är inte publicerad')
    else:
        text = page.read_text(encoding='utf-8')
        heading = re.search(r'<h1[^>]*>(.*?)</h1>', text, re.DOTALL)
        print(f'Sidan finns: {PAGE}')
        print(f'Sidans rubrik: {re.sub(r"<[^>]+>", "", heading.group(1)).strip() if heading else "(ingen)"}')
        links = anchors(text)
        for library in LIBRARIES:
            address = SITE + library
            said = address in html.unescape(re.sub(r'<[^>]+>', '', text))
            published = (folder / library).is_file()
            clickable = any(href == address or (':' not in href and reached(page, href) == (folder / library).resolve()) for href, _ in links)
            print(f'Adressen {address}: står på sidan: {"ja" if said else "nej"}; filen är publicerad: {"ja" if published else "nej"}; klickbar länk: {"ja" if clickable else "nej, bara text"}')
            if not said:
                failures.append(f'{PAGE}: adressen {address} står inte på sidan')
            if not published:
                failures.append(f'{library}: filen är inte publicerad')
        decision = [(href, words) for href, words in links if ':' not in href and reached(page, href).as_posix().startswith((folder / DECISION).as_posix())]
        if not decision:
            failures.append(f'{PAGE}: ingen länk till beslut 42')
        for href, words in decision:
            there = reached(page, href).is_file()
            print(f'Länk till beslut 42: "{words}" -> {href} (sidan finns: {"ja" if there else "nej"})')
            if not there:
                failures.append(f'{PAGE}: länken till beslut 42 leder till en sida som inte är publicerad')

    # Arbetsflödet lägger startsidan i mappen ovanför katalogen; därför räknas länken från katalogens mapp.
    start = Path(START_PAGE).read_text(encoding='utf-8')
    to_page = [(href, words) for href, words in anchors(start) if href.startswith('katalog/') and 'formbibliotek' in href]
    if not to_page:
        failures.append(f'{START_PAGE}: ingen länk till sidan om formbiblioteket')
    for href, words in to_page:
        target = folder / href.removeprefix('katalog/')
        target = target / 'index.html' if href.endswith('/') else target
        there = target.is_file()
        print(f'Startsidans länk: "{words}" -> {href} (sidan finns: {"ja" if there else "nej"})')
        if not there:
            failures.append(f'{START_PAGE}: länken {href} leder till en sida som inte är publicerad')

    base = subprocess.run(['git', 'show', f'{BASE}:{START_PAGE}'], capture_output=True, text=True, check=True).stdout
    changes = [line for line in difflib.ndiff(base.splitlines(), start.splitlines()) if line[:2] in ('- ', '+ ')]
    removed = [line[2:] for line in changes if line.startswith('- ')]
    added = [line[2:] for line in changes if line.startswith('+ ')]
    print(f'Startsidan mot basen {BASE}: {len(base.splitlines())} rader i basen, {len(removed)} borttagna eller ändrade, {len(added)} tillagda')
    for line in added:
        print(f'Tillagd rad: {line.strip()}')
    for line in removed:
        failures.append(f'{START_PAGE}: basens rad står inte kvar oförändrad: {line.strip()}')
    if len(added) != 1:
        failures.append(f'{START_PAGE}: {len(added)} tillagda rader, väntat en enda')
    elif 'formbibliotek' not in added[0]:
        failures.append(f'{START_PAGE}: den tillagda raden bär inte länken till sidan om formbiblioteket')

    if failures:
        print('FALLER:')
        for failure in failures:
            print(f'- {failure}')
        return 1
    print('HÅLLER: sidan om formbiblioteket är publicerad med de två adresserna och länken till beslut 42, och startsidan har fått en enda rad, den med länken.')
    return 0


if __name__ == '__main__':
    sys.exit(main())
