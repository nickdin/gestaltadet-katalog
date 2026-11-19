"""Hjälpskript för ärende #197: skriver tre ändrade kopior av publicerade sidor, där bara meningen om AI är fel.

Körs från lagrets rot: python3 docs/acceptance-shots/issue-197-andrade-sidor.py SIDOR MÅL

SIDOR är en mapp som interlingua publish har skrivit, med meningen en gång överst på history/index.html. MÅL är
en mapp utanför lagret. Skriptet skriver tre mappar i MÅL, var och en med startsidan oändrad och en ändrad historiksida:

- saknas: meningen är borttagen.
- tva: meningen står två gånger.
- efter: meningen är flyttad till efter historikens första rad.

Provet docs/acceptance-shots/issue-127-installningar.py läser sedan var och en med --sidor och ska falla på alla tre.
Skriptet slutar med ett fel om SIDOR inte har meningen exakt en gång eller saknar rader i historiken.
"""

import re
import shutil
import sys
from pathlib import Path

NOTE = re.compile(r'<p class="history-ai-note">.*?</p>\n?', re.S)
ROW = re.compile(r'<li>.*?<span class="version-meta">.*?</span></li>', re.S)


def main() -> int:
    if len(sys.argv) != 3:
        sys.exit("Användning: issue-197-andrade-sidor.py SIDOR MÅL")
    pages, target = Path(sys.argv[1]), Path(sys.argv[2])
    history = (pages / "history" / "index.html").read_text(encoding="utf-8")
    notes = NOTE.findall(history)
    if len(notes) != 1:
        sys.exit(f"history/index.html i {pages} har meningen {len(notes)} gånger, inte en: inget att ändra.")
    note = notes[0]
    without = history.replace(note, "")
    first_row = ROW.search(without)
    if first_row is None:
        sys.exit(f"history/index.html i {pages} har inga rader: meningen kan inte flyttas till efter den första.")
    changed = {
        "saknas": without,
        "tva": history.replace(note, note + note),
        "efter": without[: first_row.end()] + note + without[first_row.end() :],
    }
    for name, text in changed.items():
        folder = target / name
        (folder / "history").mkdir(parents=True, exist_ok=True)
        shutil.copy(pages / "index.html", folder / "index.html")
        (folder / "history" / "index.html").write_text(text, encoding="utf-8")
        print(f"Skrev {folder}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
