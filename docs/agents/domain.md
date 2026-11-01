# Domain Docs

How the engineering skills should consume this repo's domain documentation when exploring the catalogue.

## Before exploring, read these

- **`CONTEXT.md`** at the repo root: the glossary of the words the catalogue itself is built from (concept, term, mapping, perspective, element type), not a second copy of the concepts.
- **`docs/adr/`**: read ADRs that touch the area you're about to work in. Here an ADR is a decision about the catalogue: why a concept exists, where its border with the neighbour runs, what was chosen against.

If either does not exist yet, **proceed silently**. Don't flag the absence; don't suggest creating them upfront. The `/domain-modeling` skill (reached via `/grill-with-docs`) creates them lazily when terms or decisions actually get resolved.

## File structure

Single-context:

```
/
├── CONTEXT.md
├── docs/adr/
│   ├── 0009-....md
│   └── 0010-....md
├── concepts/
└── mapping/
```

## Use the glossary's vocabulary

When your output names a domain concept (in an issue title, a proposal, a hypothesis), use the term as the catalogue defines it, and write the id beside it: "Uppdrag (C-149)" (`CLAUDE.md` § Skriv ut termen). Don't drift to synonyms the catalogue explicitly lists as rejected.

If the concept you need isn't in the catalogue yet, that's a signal: either you're inventing language the catalogue doesn't use (reconsider) or there's a real gap (file it as an issue; a definition is Nicklas's to change).

## Flag ADR conflicts

If your output contradicts an existing ADR, surface it explicitly rather than silently overriding:

> _Contradicts ADR-0017 (handläggning är en elementtyp), but worth reopening because…_

## What is particular to this repo

- **The catalogue in `concepts/` is where a concept is defined.** `CONTEXT.md` is the glossary that talks about the catalogue; when the two disagree, the catalogue is the one definition and the glossary is wrong (`CLAUDE.md` § Katalogens enda hem).
- **ADRs 0009 to 0024 came with the move from the private store** (`nickdin/arkitektur` #32), cleaned of every real organisation; `CONTEXT.md`, the glossary in Swedish, is still on its way (#4). ADR numbering continues from them; the first ADR written here takes the next free number, so the series never restarts at 0001.
- **ADRs are content, and public.** They are written in Swedish, cite law and general frameworks freely, and draw every example from the two example organisations in `docs/exempel/` (`CLAUDE.md` § Ingen verklig organisation).
- **Element, relation, description and view files are written with the `interlingua` commands, never by hand**; prose under a file's headings may be added.
