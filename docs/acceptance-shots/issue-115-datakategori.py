"""Prov för ärende #115: de fyra datakategorierna bär slaget data-category, Datakategori (C-201) bär det inte, och beslut 32 säger de fyra.

Körs från katalogens rot utan argument: python3 docs/acceptance-shots/issue-115-datakategori.py

Provet prövar fyra saker:

1. Resursdata (C-202), Referensdata (C-203), Transaktionsdata (C-204) och Händelsedata (C-205) har
   raden kind: data-category i sitt huvud, och deras generic pekar kvar på Informationsobjekt (C-060).
2. Datakategori (C-201) har ingen rad kind i sitt huvud.
3. Programmet läser märkningen: interlingua category-elements . C-nnn svarar med slutkod 0 för var
   och en av de fyra och vägrar Datakategori (C-201) med slutkod 1.
4. Beslut 32 säger "De fyra kategorierna märks med ett eget slag", säger inte längre "De fem
   begreppen märks", och bär skälet: allt som är märkt är ett giltigt värde.

Provet slutar med slutkod 1 och raden FALLER om något av de fyra inte håller.

Programmet hittas i miljövariabeln INTERLINGUA, annars i ~/Devbox/interlingua/.venv/bin/interlingua.
"""
import os
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path('.')
INTERLINGUA = os.environ.get('INTERLINGUA') or str(Path.home() / 'Devbox/interlingua/.venv/bin/interlingua')
CATEGORIES = {
    'C-202': 'Resursdata',
    'C-203': 'Referensdata',
    'C-204': 'Transaktionsdata',
    'C-205': 'Händelsedata',
}
DIVISION = ('C-201', 'Datakategori')
KIND = 'data-category'
GENERIC = 'C-060'
FOUR = 'De fyra kategorierna märks med ett eget slag'
FIVE = 'De fem begreppen märks'
REASON = 'allt som är märkt är ett giltigt värde'


def front_matter(concept_id, term):
    """Raderna i begreppsfilens huvud, mellan de två första raderna ---."""
    text = (ROOT / 'concepts' / f'{concept_id} {term}.md').read_text(encoding='utf-8')
    parts = text.split('---\n', 2)
    if len(parts) < 3 or parts[0] != '':
        raise ValueError(f'{concept_id} {term}: filen har inget huvud mellan två rader ---')
    return parts[1].splitlines()


def value(lines, key):
    """Värdet på en nyckel i huvudets yttersta nivå, eller None om nyckeln saknas."""
    for line in lines:
        found = re.match(rf'{key}:\s*(.*)$', line)
        if found:
            return found.group(1).strip().strip('\'"')
    return None


def listing(concept_id):
    """Slutkod och första svarsrad från interlingua category-elements . <id>."""
    ran = subprocess.run([INTERLINGUA, 'category-elements', '.', concept_id], capture_output=True, text=True)
    answer = (ran.stdout + ran.stderr).strip().splitlines()
    return ran.returncode, answer[0] if answer else '(inget svar)'


def main():
    failures = []

    for concept_id, term in CATEGORIES.items():
        lines = front_matter(concept_id, term)
        kind = value(lines, 'kind')
        generic = value(lines, 'generic')
        print(f'{term} ({concept_id}): kind: {kind}, generic: {generic}')
        if kind != KIND:
            failures.append(f'{term} ({concept_id}) har kind: {kind}, inte {KIND}')
        if generic is None or GENERIC not in generic:
            failures.append(f'{term} ({concept_id}) har generic: {generic}, inte {GENERIC}')

    division_kind = value(front_matter(*DIVISION), 'kind')
    print(f'{DIVISION[1]} ({DIVISION[0]}): kind: {division_kind}')
    if division_kind is not None:
        failures.append(f'{DIVISION[1]} ({DIVISION[0]}) har kind: {division_kind}, men ska inte vara märkt')

    for concept_id, term in CATEGORIES.items():
        code, answer = listing(concept_id)
        print(f'category-elements . {concept_id}: slutkod {code}: {answer}')
        if code != 0:
            failures.append(f'programmet läser inte {term} ({concept_id}) som datakategori: {answer}')
    code, answer = listing(DIVISION[0])
    print(f'category-elements . {DIVISION[0]}: slutkod {code}: {answer}')
    if code == 0:
        failures.append(f'programmet läser {DIVISION[1]} ({DIVISION[0]}) som datakategori')

    decisions = sorted((ROOT / 'docs' / 'adr').glob('0032-*.md'))
    if len(decisions) != 1:
        failures.append(f'docs/adr/ har {len(decisions)} filer som börjar på 0032-, inte en')
    else:
        text = decisions[0].read_text(encoding='utf-8')
        for line in text.splitlines():
            if 'märks med ett eget slag' in line or FIVE in line:
                sentence = next(s for s in re.split(r'(?<=\.)\s+', line) if 'märks' in s)
                print(f'Beslut 32: {sentence}')
        if FOUR not in text:
            failures.append(f'beslut 32 säger inte "{FOUR}"')
        if FIVE in text:
            failures.append(f'beslut 32 säger fortfarande "{FIVE}"')
        if REASON not in text:
            failures.append(f'beslut 32 säger inte varför: "{REASON}"')

    if failures:
        print('FALLER:')
        for failure in failures:
            print(f'- {failure}')
        return 1
    print('HÅLLER: de fyra kategorierna bär slaget, Datakategori (C-201) bär det inte, och beslut 32 säger de fyra.')
    return 0


if __name__ == '__main__':
    sys.exit(main())
