"""Prov för ärende #114: flödar till (C-097) markeras flow: true, och programmet märker det.

Körs från lagrets rot: python3 docs/acceptance-shots/issue-114-flow.py

Provet kopierar lagret, med den C-097 som just den kopian har, till en egen mapp i en tillfällig katalog. I
kopian skriver det tre element med interlingua: verksamhetsaktiviteterna Handlägga ansökan och Besluta om stöd,
och verksamhetsobjektet Ansökan. Handläggningen skriver till ansökan, beslutet läser den, och en lagrad
relation flödar till (C-097) går från handläggningen till beslutet. Elementen och namnen är ur Myndigheten för
föreningsstöd (docs/exempel/).

Sedan kör provet interlingua check två gånger på samma fixtur: en gång som kopian är, och en gång med raden
flow: true borttagen ur C-097 i kopian. Det skriver ut check-raderna som talar om den lagrade relationen
(R-nnnn med flödar till). Slutkod 0 när kopian säger det en kopia med markeringen ska säga, annars 1 och raden
FALLER. På en kopia utan markeringen faller provet: programmet känner igen flödestypen bara på markeringen
(interlingua #989), så utan den skriver check ingenting om flödet.

Fixturen binds till ett läge hos lagret: bara C-097 skiljer mellan basen och grenen.
"""

import re
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
INTERLINGUA = "/home/nickdin/Devbox/interlingua/.venv/bin/interlingua"
FLOW_CONCEPT = "concepts/C-097 flödar till.md"
FLOW_LINE = "flow: true\n"
ACTIVITY_TYPE = "C-175"  # Verksamhetsaktivitet
OBJECT_TYPE = "C-159"  # Verksamhetsobjekt
ACCESS_TYPE = "C-101"  # har åtkomst till
FLOW_TYPE = "C-097"  # flödar till


def git(store: Path, *args: str) -> None:
    subprocess.run(
        ["git", "-c", "user.name=prov", "-c", "user.email=prov@example.invalid", *args],
        cwd=store,
        check=True,
        capture_output=True,
    )


def tool(*args: str) -> str:
    result = subprocess.run([INTERLINGUA, *args], capture_output=True, text=True)
    if result.returncode != 0:
        sys.exit(f"interlingua {' '.join(args)} gav slutkod {result.returncode}: {result.stdout}{result.stderr}")
    return result.stdout


def new_element(store: Path, name: str, element_type: str, description: str) -> str:
    out = tool("element", "new", str(store), "--name", name, "--type", element_type, "--level", "conceptual", "--description", description)
    git(store, "add", "-A")
    git(store, "commit", "-m", f"element {name}")
    return re.search(r"E-\d{4}", out).group(0)


def new_relation(store: Path, source: str, target: str, relation_type: str, description: str, *extra: str) -> str:
    out = tool("relation", "new", str(store), "--from", source, "--to", target, "--type", relation_type, "--description", description, *extra)
    git(store, "add", "-A")
    git(store, "commit", "-m", f"relation {description}")
    return re.search(r"R-\d{4}", out).group(0)


def build(scratch: Path) -> tuple[Path, str]:
    """Copy the store, write the fixture into it with interlingua and commit each step; return it and the flow's id."""
    store = scratch / "lager"
    shutil.copytree(ROOT, store, ignore=shutil.ignore_patterns(".git", "docs", "layout"))
    (store / "docs").mkdir()
    git(store, "init", "-q", "-b", "main")
    git(store, "add", "-A")
    git(store, "commit", "-q", "-m", "kopia av lagret")
    handle = new_element(store, "Handlägga ansökan", ACTIVITY_TYPE, "Steget där handläggaren prövar en ansökan om föreningsstöd.")
    decide = new_element(store, "Besluta om stöd", ACTIVITY_TYPE, "Steget där enhetschefen beslutar om en ansökan om föreningsstöd.")
    application = new_element(store, "Ansökan", OBJECT_TYPE, "Det som en förening skickar in för att få föreningsstöd.")
    new_relation(store, handle, application, ACCESS_TYPE, "Handlägga ansökan skriver Ansökan", "--access", "write")
    new_relation(store, decide, application, ACCESS_TYPE, "Besluta om stöd läser Ansökan", "--access", "read")
    flow = new_relation(store, handle, decide, FLOW_TYPE, "Handlägga ansökan flödar till Besluta om stöd")
    return store, flow


def check(store: Path) -> str:
    result = subprocess.run([INTERLINGUA, "check", str(store)], capture_output=True, text=True)
    return result.stdout + result.stderr


def about(output: str, flow: str) -> list[str]:
    """The check lines that name the stored flow."""
    return [line for line in output.splitlines() if flow in line.split(":")[0]]


def main() -> int:
    marked = FLOW_LINE in (ROOT / FLOW_CONCEPT).read_text(encoding="utf-8")
    print(f"{FLOW_CONCEPT} bär {FLOW_LINE.strip()}: {'ja' if marked else 'nej'}")
    with tempfile.TemporaryDirectory(prefix="issue-114-") as scratch_name:
        store, flow = build(Path(scratch_name))
        print(f"fixtur: handläggningen skriver ansökan, beslutet läser den, och {flow} är flödar till från handläggningen till beslutet")

        as_it_is = about(check(store), flow)
        print("check på kopian som den är:")
        print("\n".join(f"  {line}" for line in as_it_is) or "  (ingen rad om flödet)")

        concept = store / FLOW_CONCEPT
        concept.write_text(concept.read_text(encoding="utf-8").replace(FLOW_LINE, ""), encoding="utf-8")
        without = about(check(store), flow)
        print("check på samma fixtur, raden flow: true borttagen:")
        print("\n".join(f"  {line}" for line in without) or "  (ingen rad om flödet)")

    if len(as_it_is) == 1 and "is also concluded from" in as_it_is[0] and not without:
        print("OK: programmet märker det lagrade flödet, och bara på markeringen")
        return 0
    print("FALLER: kopian som den är säger inte det en kopia med flow: true ska säga")
    return 1


if __name__ == "__main__":
    sys.exit(main())
