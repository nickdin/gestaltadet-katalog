# Board models

Which model runs which step of a `/work-the-board` run in this repo. The general table is `~/.claude/skills/work-the-board/SKILL.md` § 2a; this file is the exception that section allows, and `board-lint.py` and `board-prompt-check.sh` read the two lines below.

```
worker: fable
review: fable
```

## What it covers

Nicklas, 2026-11-18: every step of a board run that creates text or relations between things runs on Fable.

A ticket is covered when its change writes or rewrites text a reader meets, or adds, changes or removes a relation in the store. That includes a concept's definition, description or remark, a decision under `docs/adr/`, an example under `docs/exempel/`, the glossary `CONTEXT.md`, a page's own wording on gestaltadet.se, and any relation or element written with the `interlingua` commands.

A ticket is not covered when it changes no such text and no relation: a drawing whose shapes move, a setting in `settings.yaml`, the workflow that publishes the site, a stylesheet. It runs on `sonnet` as the general table says.

A ticket that does both is covered.

## What runs on Fable

- **The worker** of a covered ticket, at effort `medium`.
- **The fix worker** for a finding against a covered ticket, and **the wave's wording worker**, at `medium`.
- **Both reviews** of a wave that holds at least one covered ticket, at `low`. A wave that holds none reviews on `opus`.

A covered ticket that parks restarts on Fable. The plan, the wave sessions, the accept link, triage and the finish stay on the models the general table names.

## What the plan writes

Per ticket in `plan.md`: covered or not, and the sentence of the ticket that decided it. Per wave: the model its reviews start on.
