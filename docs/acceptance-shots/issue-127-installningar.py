"""Prov för ärende #127 och #128: sajten ska länka namnet i sidhuvudet och skriva AI-versioner som "Nicklas med AI".

Körs från lagrets rot: python3 docs/acceptance-shots/issue-127-installningar.py

Provet klonar den utcheckning det körs i till en tillfällig mapp, utanför lagret, och kör interlingua publish på
klonen. Sedan läser det två saker i de skrivna sidorna.

1. Sajtnamnet i sidhuvudet på katalogens startsida. Med site_address i settings.yaml är det en länk till
   https://gestaltadet.se/ (ärende #128). Utan nyckeln är det ren text: <p class="site">GestaltaDet</p>.
2. Historiken. Provet väljer den senaste versionen vars commit har en Co-Authored-By med noreply@anthropic.com
   och läser hur historiksidan skriver den. Med ai_coauthor_addresses i settings.yaml står det "Nicklas med AI"
   (ärende #127). Utan nyckeln står det "Nicklas".

Provet slutar med slutkod 1 och raden FALLER om någon av de två läsningarna ger det gamla svaret. Klonen bär bara
det som är committat, så en ändring som inte är committad syns inte i provet. Publiceringen tar flera minuter.
"""

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


def main() -> int:
    with tempfile.TemporaryDirectory(prefix="issue-127-") as tmp:
        clone = Path(tmp) / "store"
        pages = Path(tmp) / "pages"
        run(["git", "clone", "-q", str(ROOT), str(clone)], ROOT)
        subject = latest_ai_subject(clone)
        run([str(INTERLINGUA), "publish", ".", str(pages)], clone)

        start = (pages / "index.html").read_text(encoding="utf-8")
        header = re.search(r'<p class="site">(.*?)</p>', start, re.S)
        header_html = header.group(1) if header else "(ingen <p class=\"site\"> hittad)"

        history = (pages / "history" / "index.html").read_text(encoding="utf-8")
        rows = re.findall(r"<li>(.*?)<span class=\"version-meta\">(.*?)</span></li>", history, re.S)
        meta = [html.unescape(m) for text, m in rows if html.unescape(text).strip() == subject]

        print(f"Sidhuvudet på startsidan: {header_html}")
        print(f"Versionen '{subject}' står i historiken som: {meta[0] if meta else '(hittades inte)'}")

        link_ok = header_html == f'<a href="{SITE_ADDRESS}">{SITE_NAME}</a>'
        history_ok = bool(meta) and meta[0].rstrip().endswith("Nicklas med AI")
        print(f"Namnet är en länk till {SITE_ADDRESS}: {'ja' if link_ok else 'nej'}")
        print(f"AI-versionen står som Nicklas med AI: {'ja' if history_ok else 'nej'}")
        if link_ok and history_ok:
            print("OK")
            return 0
        print("FALLER")
        return 1


if __name__ == "__main__":
    sys.exit(main())
