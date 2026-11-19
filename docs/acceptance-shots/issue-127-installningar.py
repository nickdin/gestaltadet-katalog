"""Prov för ärende #127, #128 och #197: sidhuvudets länk, "Nicklas med AI" och meningen överst i historiken.

Körs från lagrets rot: python3 docs/acceptance-shots/issue-127-installningar.py

Provet klonar den utcheckning det körs i till en tillfällig mapp, utanför lagret, och kör interlingua publish på
klonen. Sedan läser det tre saker i de skrivna sidorna.

1. Sajtnamnet i sidhuvudet på katalogens startsida. Med site_address i settings.yaml är det en länk till
   https://gestaltadet.se/ (ärende #128). Utan nyckeln är det ren text: <p class="site">GestaltaDet</p>.
2. Historiken. Provet väljer den senaste versionen vars commit har en Co-Authored-By med noreply@anthropic.com
   och läser hur historiksidan skriver den. Med ai_coauthor_addresses i settings.yaml står det "Nicklas med AI"
   (ärende #127). Utan nyckeln namnger programmet modellen ur commitens rad, till exempel "Nicklas med Claude Opus 5.5".
3. Meningen om att beskrivningarna är skrivna av AI (ärende #197). Provet räknar hur många gånger meningen står på
   history/index.html och läser om den står före historikens första rad. Med ai_coauthor_addresses står den en
   gång, överst. Utan nyckeln står den inte alls.

Provet slutar med slutkod 1 och raden FALLER om någon av de tre läsningarna ger fel svar: det gamla svaret för de
två första, och för den tredje varje annat antal än ett eller en mening som står efter första raden. Klonen bär
bara det som är committat, så en ändring som inte är committad syns inte i provet. Publiceringen tar flera minuter.

Med --sidor MAPP läser provet en redan publicerad mapp i stället för att publicera på nytt. Klonen görs ändå,
eftersom provet läser den senaste AI-versionen ur dess historik. Mappen ska därför vara publicerad ur samma commit
som utcheckningen står på; annars finns versionen inte i mappens historik och den andra läsningen faller.
"""

import argparse
import html
import re
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
INTERLINGUA = Path.home() / "Devbox" / "interlingua" / ".venv" / "bin" / "interlingua"
AI_ADDRESS = "noreply@anthropic.com"
SITE_ADDRESS = "https://gestaltadet.se/"
SITE_NAME = "GestaltaDet"
AI_SENTENCE = "Beskrivningarna av ändringar gjorda med AI är skrivna av AI och inte granskade."
ROW = re.compile(r"<li>(.*?)<span class=\"version-meta\">(.*?)</span></li>", re.S)


def run(args: list[str], cwd: Path) -> str:
    done = subprocess.run(args, cwd=cwd, capture_output=True, text=True)
    if done.returncode != 0:
        sys.exit(f"{' '.join(args)} slutade med {done.returncode}:\n{done.stdout}{done.stderr}")
    return done.stdout


def latest_ai_subject(clone: Path) -> str:
    """The subject of the newest commit that names the AI address in a Co-Authored-By line."""
    log = run(["git", "log", "--format=%H%x1f%s%x1f%(trailers:key=Co-Authored-By,valueonly)%x1e"], clone)
    for entry in log.split("\x1e"):
        parts = entry.strip("\n").split("\x1f")
        if len(parts) == 3 and AI_ADDRESS in parts[2]:
            return parts[1]
    sys.exit(f"Ingen commit i klonen har en Co-Authored-By med {AI_ADDRESS}: provet har inget att läsa.")


def read_ai_sentence(history: str) -> tuple[int, bool, bool]:
    """How many times the AI sentence stands on the history page, whether its first occurrence precedes the first row, and whether the page has any row."""
    text = html.unescape(history)
    count = text.count(AI_SENTENCE)
    first_row = ROW.search(text)
    before_first_row = count > 0 and first_row is not None and text.index(AI_SENTENCE) < first_row.start()
    return count, before_first_row, first_row is not None


def judge_pages(pages: Path, subject: str) -> int:
    """Reads the three things in the published pages, prints each reading, and returns the exit code: 0 when all three hold."""
    start = (pages / "index.html").read_text(encoding="utf-8")
    header = re.search(r'<p class="site">(.*?)</p>', start, re.S)
    header_html = header.group(1) if header else "(ingen <p class=\"site\"> hittad)"

    history = (pages / "history" / "index.html").read_text(encoding="utf-8")
    meta = [html.unescape(m) for text, m in ROW.findall(history) if html.unescape(text).strip() == subject]
    count, before_first_row, has_rows = read_ai_sentence(history)

    print(f"Sidhuvudet på startsidan: {header_html}")
    print(f"Versionen '{subject}' står i historiken som: {meta[0] if meta else '(hittades inte)'}")
    print(f"Meningen '{AI_SENTENCE}' står på history/index.html: {count} gånger")
    if not has_rows:
        print("Historiken har inga rader: meningen kan inte stå före den första.")

    link_ok = header_html == f'<a href="{SITE_ADDRESS}">{SITE_NAME}</a>'
    history_ok = bool(meta) and meta[0].rstrip().endswith("Nicklas med AI")
    sentence_ok = count == 1 and before_first_row
    print(f"Namnet är en länk till {SITE_ADDRESS}: {'ja' if link_ok else 'nej'}")
    print(f"AI-versionen står som Nicklas med AI: {'ja' if history_ok else 'nej'}")
    print(f"Meningen står före historikens första rad: {'ja' if before_first_row else 'nej'}")
    print(f"Meningen står exakt en gång, före första raden: {'ja' if sentence_ok else 'nej'}")
    if link_ok and history_ok and sentence_ok:
        print("OK")
        return 0
    print("FALLER")
    return 1


def main() -> int:
    parser = argparse.ArgumentParser(description="Prov för ärende #127, #128 och #197.")
    parser.add_argument("--sidor", type=Path, help="läs en redan publicerad mapp i stället för att publicera på nytt")
    args = parser.parse_args()
    with tempfile.TemporaryDirectory(prefix="issue-127-") as tmp:
        clone = Path(tmp) / "store"
        run(["git", "clone", "-q", str(ROOT), str(clone)], ROOT)
        subject = latest_ai_subject(clone)
        if args.sidor is not None:
            return judge_pages(args.sidor.resolve(), subject)
        pages = Path(tmp) / "pages"
        run([str(INTERLINGUA), "publish", ".", str(pages)], clone)
        return judge_pages(pages, subject)


if __name__ == "__main__":
    sys.exit(main())
