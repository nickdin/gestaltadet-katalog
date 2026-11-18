"""Prov för ärende #144: en omärkt ram runt ett informationsobjekt läses som består av (C-062).

Körs från lagrets rot: python3 docs/acceptance-shots/issue-144-ram.py

Provet klonar den utcheckning det körs i till en tillfällig mapp och rör aldrig lagret självt. I klonen skapar det
ett arkitekturobjekt och en beskrivning, eftersom interlingua importerar en ritning till en beskrivning. Sedan
importerar det en ritning med interlinguas kommando import drawio. Ritningen har två ramar, och ingen av dem bär
en egen märkning. Den ena ramen är informationsobjektet Föreningsinformation runt informationsobjektet Förening.
Den andra är lagringsytan Datalagret runt representationen Kopiorna i datalagret.

Provet skriver ut relationerna som importen skrev. Båda ska gå från ramen till rutan. Ramen runt
informationsobjektet ska läsas som består av (C-062), och ramen runt lagringsytan som aggregerar (C-100).
Annars slutar provet med slutkod 1 och raden FALLER. Så går det på en utcheckning där Informationsobjekt (C-060)
inte anger nesting_relation_type: där läses båda ramarna efter settings.yaml, som aggregerar (C-100). Så går det
också om settings.yaml får composed_of i stället för begreppet: då läses lagringsytans ram som består av (C-062).

Klonen bär bara det som är committat. En ändring som inte är committad syns alltså inte i provet.
"""

import re
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
INTERLINGUA = Path.home() / "Devbox" / "interlingua" / ".venv" / "bin" / "interlingua"

INFORMATION_OBJECT = "C-060"
BUSINESS_DOMAIN = "C-008"
COMPOSED_OF = "C-062"
AGGREGATES = "C-100"
FRAME = "Föreningsinformation"
INNER = "Förening"
OTHER_FRAME = "Datalagret"
OTHER_INNER = "Kopiorna i datalagret"
EXPECTED = [(OTHER_FRAME, AGGREGATES, OTHER_INNER), (FRAME, COMPOSED_OF, INNER)]

# Ramarna n1 och n3 bär varken nesting_relation_type eller store_id, bara sin typ och sitt namn.
# Rutan n2 ligger i ramen n1 och rutan n4 i ramen n3.
DRAWING = (
    '<mxfile host="prov"><diagram id="p1" name="Sida-1"><mxGraphModel><root><mxCell id="0"/><mxCell id="1" parent="0"/>'
    f'<object id="n1" label="{FRAME}" type="Informationsobjekt"><mxCell vertex="1" parent="1">'
    '<mxGeometry x="40" y="40" width="240" height="160" as="geometry"/></mxCell></object>'
    f'<object id="n2" label="{INNER}" type="Informationsobjekt"><mxCell vertex="1" parent="n1">'
    '<mxGeometry x="60" y="60" width="120" height="60" as="geometry"/></mxCell></object>'
    f'<object id="n3" label="{OTHER_FRAME}" type="Lagringsyta"><mxCell vertex="1" parent="1">'
    '<mxGeometry x="320" y="40" width="240" height="160" as="geometry"/></mxCell></object>'
    f'<object id="n4" label="{OTHER_INNER}" type="Representation"><mxCell vertex="1" parent="n3">'
    '<mxGeometry x="60" y="60" width="120" height="60" as="geometry"/></mxCell></object>'
    "</root></mxGraphModel></diagram></mxfile>"
)


class StepFailed(Exception):
    """Ett kommando som provet behöver gick inte igenom."""


def run(*command: str, cwd: Path | None = None) -> str:
    """Kör ett kommando och ge det som skrevs ut; ett kommando som faller stoppar provet."""
    result = subprocess.run(command, cwd=cwd, capture_output=True, text=True, check=False)
    if result.returncode != 0:
        raise StepFailed(f"{' '.join(command)}: slutkod {result.returncode}: {result.stderr.strip()}")
    return result.stdout


def commit(store: Path, message: str) -> None:
    """Committa allt i klonen: interlinguas skrivande kommandon vägrar köra med ändringar som inte är committade."""
    run("git", "add", "--all", cwd=store)
    run("git", "-c", "user.name=prov", "-c", "user.email=prov@example.invalid", "commit", "-q", "-m", message, cwd=store)


def new_id(output: str, prefix: str) -> str:
    """Id:t som ett interlinguakommando skrev ut för det det skapade."""
    found = re.search(rf"\b{prefix}-\d+\b", output)
    if not found:
        raise StepFailed(f"kommandot skrev inte ut något {prefix}-id: {output.strip()}")
    return found.group(0)


def front_matter(path: Path) -> dict[str, str]:
    """Nycklarna på översta nivån i en fils front matter, som text."""
    _, block, _ = path.read_text(encoding="utf-8").split("---\n", 2)
    pairs = (line.split(":", 1) for line in block.splitlines() if line and not line.startswith((" ", "-")))
    return {key.strip(): value.strip().strip("'\"") for key, value in pairs}


def link_text(value: str) -> str:
    """Texten i en länk: '[[E-0002 Förening]]' ger 'E-0002 Förening'."""
    return value.replace("[[", "").replace("]]", "")


def link_id(value: str) -> str:
    """Id:t först i en länk: '[[C-062 består av]]' ger 'C-062'."""
    return link_text(value).split(" ", 1)[0]


def with_id_last(value: str) -> str:
    """En länk skriven med termen först: '[[C-062 består av]]' ger 'består av (C-062)'."""
    identifier, _, term = link_text(value).partition(" ")
    return f"{term} ({identifier})"


def declared_default(store: Path) -> str:
    """Det begreppet Informationsobjekt (C-060) anger om sin ram i den här utcheckningen."""
    concept = next((store / "concepts").glob(f"{INFORMATION_OBJECT} *.md"))
    return front_matter(concept).get("nesting_relation_type", "inget")


def settings_default(store: Path) -> str:
    """Värdet på nesting_relation_type i klonens settings.yaml."""
    for line in (store / "settings.yaml").read_text(encoding="utf-8").splitlines():
        if line.startswith("nesting_relation_type:"):
            return line.split(":", 1)[1].strip()
    return "inget"


def import_drawing(scratch: Path) -> tuple[Path, str]:
    """Klona utcheckningen, lägg en beskrivning i klonen och importera ritningen dit; ge klonen och importens svar."""
    store = scratch / "lager"
    run("git", "clone", "-q", str(ROOT), str(store))
    created = run(
        str(INTERLINGUA), "element", "new", str(store), "--name", "Föreningsstöd", "--type", BUSINESS_DOMAIN,
        "--level", "conceptual", "--description", "Myndighetens arbete med stöd till föreningar.",
    )
    domain = new_id(created, "E")
    commit(store, "Provets arkitekturobjekt")
    created = run(
        str(INTERLINGUA), "description", "new", str(store), "--object", domain, "--kind", "current-state",
        "--as-of", "2026", "--level", "conceptual", "--owner", "Informationsägaren", "--title", "Provets beskrivning",
    )
    description = new_id(created, "D")
    commit(store, "Provets beskrivning")
    drawing = scratch / "ram.drawio"
    drawing.write_text(DRAWING, encoding="utf-8")
    answer = run(str(INTERLINGUA), "import", "drawio", str(store), str(drawing), "--description", description)
    return store, answer.replace(str(scratch), "<tillfällig mapp>").strip()


def main() -> int:
    head = run("git", "log", "-1", "--format=%h", cwd=ROOT).strip()
    with tempfile.TemporaryDirectory(prefix="issue-144-ram-") as folder:
        try:
            store, answer = import_drawing(Path(folder))
        except StepFailed as failure:
            print(f"FALLER: {failure}")
            return 1
        print(f"Utcheckning: {head}")
        print(f"Informationsobjekt (C-060) anger nesting_relation_type: {declared_default(store)}")
        print(f"settings.yaml anger nesting_relation_type: {settings_default(store)}")
        print(f"Importens svar: {answer}")
        relations = sorted((store / "relations").glob("*.md")) if (store / "relations").is_dir() else []
        print(f"Relationer som importen skrev: {len(relations)}")
        lines = []
        for relation in relations:
            fields = front_matter(relation)
            source = link_text(fields["from"]).split(" ", 1)[1]
            target = link_text(fields["to"]).split(" ", 1)[1]
            kind = fields.get("type", "")
            print(f"{source} --[{with_id_last(kind) if kind else 'ingen typ'}]--> {target}")
            lines.append((source, link_id(kind) if kind else "", target))
    if sorted(lines) == sorted(EXPECTED):
        print(
            f"HÅLLER: ramen {FRAME} består av (C-062) rutan {INNER}, "
            f"och ramen {OTHER_FRAME} aggregerar (C-100) rutan {OTHER_INNER}."
        )
        return 0
    print(
        f"FALLER: importen skulle ha skrivit två relationer, {FRAME} består av (C-062) {INNER} "
        f"och {OTHER_FRAME} aggregerar (C-100) {OTHER_INNER}."
    )
    return 1


if __name__ == "__main__":
    sys.exit(main())
