"""Prov för ärende #189: avsnittet Vad kartan bär och inte bär säger var kontinuitetskravet och återställningstiden står.

Körs från katalogens rot utan argument: python3 docs/acceptance-shots/issue-189-forteckningen.py

Provet publicerar katalogen med `interlingua publish` till en tom tillfällig mapp. Det letar upp
sidan Informationskartläggning bland de publicerade filerna och läser avsnittet under rubriken
Vad kartan bär och inte bär, fram till nästa rubrik på samma nivå. HTML-taggarna och sajtens
förklaringsrutor för termer tas bort, så att texten är den läsaren ser.

Avsnittet har en punktlista med en punkt per förteckning. Provet letar upp punkten som börjar med
Förteckningen över kraven på behandlingarna. Provet slutar med slutkod 1 och raden FALLER om den
punkten saknar något av orden kontinuitetskrav och återställningstid.

Provet prövar inte om meningarna är klarspråk. Den granskningen står i issue-189-forteckningen.txt.
"""
import html
import re
import subprocess
import sys
import tempfile
from pathlib import Path

INTERLINGUA = Path.home() / 'Devbox' / 'interlingua' / '.venv' / 'bin' / 'interlingua'
PAGE_TITLE = 'Informationskartläggning'
HEADING = 'Vad kartan bär och inte bär'
LIST_ITEM_START = 'Förteckningen över kraven på behandlingarna'
REQUIREMENTS = ('kontinuitetskrav', 'återställningstid')
# En förklaringsruta är en span med klassen term-box som innehåller en länk och en span med definitionen.
TERM_BOX = re.compile(r'<span class="term-box".*?</span>\s*</span>', re.S)


def section_blocks(page):
    """Avsnittets stycken och listpunkter som ren text, eller None om rubriken HEADING saknas."""
    match = re.search(r'<h(\d)[^>]*>(?:(?!</h\d>).)*?' + re.escape(HEADING) + r'.*?</h\1>', page, re.S)
    if match is None:
        return None
    rest = page[match.end():]
    end = re.search(r'<h[1-%s][\s>]' % match.group(1), rest)
    body = TERM_BOX.sub('', rest[:end.start()] if end else rest)
    blocks = re.split(r'</(?:p|li)>', body)
    cleaned = (' '.join(html.unescape(re.sub(r'<[^>]+>', '', block)).split()) for block in blocks)
    return [block for block in cleaned if block]


def main():
    with tempfile.TemporaryDirectory() as scratch:
        site = Path(scratch) / 'site'
        built = subprocess.run([str(INTERLINGUA), 'publish', '.', str(site)], capture_output=True, text=True)
        if built.returncode != 0:
            print(f'FALLER: interlingua publish gav slutkod {built.returncode}: {built.stderr.strip()}')
            return 1
        pages = [path for path in sorted(site.rglob('*.html'))
                 if re.search(r'<h1[^>]*>\s*' + PAGE_TITLE + r'\s*</h1>', path.read_text(encoding='utf-8'))]
        if len(pages) != 1:
            print(f'FALLER: {len(pages)} publicerade sidor har rubriken {PAGE_TITLE}, inte en.')
            return 1
        blocks = section_blocks(pages[0].read_text(encoding='utf-8'))
        print(f'Publicerad sida: {pages[0].relative_to(site).as_posix()}')
    if blocks is None:
        print(f'FALLER: sidan saknar rubriken {HEADING}.')
        return 1
    items = [block for block in blocks if block.startswith(LIST_ITEM_START)]
    if len(items) != 1:
        print(f'FALLER: avsnittet har {len(items)} punkter som börjar med {LIST_ITEM_START}, inte en.')
        return 1
    print(f'Punkten i avsnittet {HEADING}: {items[0]}')
    missing = [word for word in REQUIREMENTS if word not in items[0].lower()]
    for word in REQUIREMENTS:
        print(f'{word}: {"saknas" if word in missing else "står i punkten"}')
    if missing:
        print(f'FALLER: punkten säger inte var {len(missing)} av {len(REQUIREMENTS)} krav står.')
        return 1
    print('HÅLLER: punkten säger att båda kraven står i förteckningen över kraven på behandlingarna.')
    return 0


if __name__ == '__main__':
    sys.exit(main())
