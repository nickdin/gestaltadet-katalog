"""Prov för ärende #193: de meningar som är nya i beslut 30 sedan ärende #144 håller en tanke var.

Körs från katalogens rot utan argument: python3 docs/acceptance-shots/issue-193-klarsprak.py

Provet läser beslut 30 i docs/adr/ och samma fil i commit 9b3bf8c, som är läget före ärende #144.
En mening som står i filen nu men inte stod där då är ny. Provet prövar varje ny mening mot två
regler ur klarsprak-skillen, steg 3, "en tanke per mening":

A. Meningen hänger inte på en som-sats efter ett kommatecken. En sådan sats bär en andra tanke,
   och läsaren får gissa vad "som" syftar på. Den andra tanken ska stå i en egen mening.
B. Meningen är högst 25 ord.

Provet slutar med slutkod 1 och raden FALLER om någon ny mening bryter mot A eller B.

Provet är inte hela granskningen. Reglerna om aktör, verb, vardagliga ord och samma ord för samma
sak går inte att pröva med ett mönster. Den granskningen står mening för mening i
issue-193-klarsprak.txt.
"""
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path('.')
BEFORE = '9b3bf8c'
MAX_WORDS = 25
RELATIVE_AFTER_COMMA = re.compile(r',\s+som\b')


def sentences(text):
    """Filens meningar med radnummer: [(rad, mening)]. En punktlistas streck hör inte till meningen."""
    found = []
    for number, line in enumerate(text.splitlines(), start=1):
        line = re.sub(r'^\s*-\s+', '', line.strip())
        if not line or line.startswith('#'):
            continue
        for sentence in re.split(r'(?<=[.!?])\s+(?=[A-ZÅÄÖ`*"”])', line):
            found.append((number, sentence.strip()))
    return found


def main():
    decisions = sorted((ROOT / 'docs' / 'adr').glob('0030-*.md'))
    if len(decisions) != 1:
        print(f'FALLER: docs/adr/ har {len(decisions)} filer som börjar på 0030-, inte en.')
        return 1
    path = decisions[0].as_posix()
    shown = subprocess.run(['git', 'show', f'{BEFORE}:{path}'], capture_output=True, text=True)
    if shown.returncode != 0:
        print(f'FALLER: git show {BEFORE}:{path} gav slutkod {shown.returncode}.')
        return 1
    old = {sentence for _, sentence in sentences(shown.stdout)}
    new = [(number, sentence) for number, sentence in sentences(decisions[0].read_text(encoding='utf-8'))
           if sentence not in old]
    print(f'Beslut 30: {len(new)} meningar är nya sedan commit {BEFORE}, läget före ärende #144.')
    if not new:
        print('FALLER: provet hittar ingen ny mening att pröva.')
        return 1
    failures = 0
    for index, (number, sentence) in enumerate(new, start=1):
        words = len(sentence.split())
        broken = []
        if RELATIVE_AFTER_COMMA.search(sentence):
            broken.append('A, en som-sats efter kommatecken')
        if words > MAX_WORDS:
            broken.append(f'B, fler än {MAX_WORDS} ord')
        failures += bool(broken)
        verdict = 'BRYTER MOT ' + ' och '.join(broken) if broken else 'håller A och B'
        print(f'{index}. rad {number}, {words} ord, {verdict}: {sentence}')
    if failures:
        print(f'FALLER: {failures} av {len(new)} nya meningar bryter mot regel A eller B.')
        return 1
    print(f'HÅLLER: alla {len(new)} nya meningar håller regel A och B.')
    return 0


if __name__ == '__main__':
    sys.exit(main())
