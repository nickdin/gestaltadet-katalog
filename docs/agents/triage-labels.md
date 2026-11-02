# Triage Labels

The skills speak in terms of five canonical triage roles. This file maps those roles to the actual label strings used in this repo's issue tracker, and records the rest of the vocabulary around them.

## The five canonical roles

| Label in mattpocock/skills | Label in our tracker | Meaning                                  |
| -------------------------- | -------------------- | ---------------------------------------- |
| `needs-triage`             | `needs-triage`       | Maintainer needs to evaluate this issue  |
| `needs-info`               | `needs-info`         | Waiting on reporter for more information |
| `ready-for-agent`          | `ready-for-agent`    | Fully specified, ready for an AFK agent  |
| `ready-for-human`          | `ready-for-human`    | Requires human implementation            |
| `wontfix`                  | `wontfix`            | Will not be actioned                     |

When a skill mentions a role (e.g. "apply the AFK-ready triage label"), use the corresponding label string from this table. The strings are unchanged from the defaults, so no translation is needed.

## Every open issue carries two labels, one from each family

The two families answer different questions, and neither substitutes for the other.

**Type: what the issue *is*.**

- `bug`: it does something wrong today, and you could reproduce it. In a catalogue that means a definition that contradicts another, a mapping row that points at the wrong concept, a file `interlingua check` rejects.
- `enhancement`: new behaviour we want. A new concept, a new mapping table, a fuller example organisation.
- `question`: it produces an **answer** rather than a change, and closes when we know something. This is the label most readers' issues start with: the catalogue is one way of seeing things, and an objection that holds becomes a change, often an article (`README.md`).

**Status: whether anyone should pick it up.** The five roles above, plus:

- `parked`: recorded deliberately, waiting on nobody, and **not** a decision never to do it. Without it such an issue sits bare, indistinguishable from one nobody got round to labelling, and `wontfix` would wrongly claim the question was settled.

## Topic tags are a legitimate third family

Used where they help, never as a substitute for a type or a status. The tree-wide `rehaul` tag is deliberately absent: this repo is outside the rehaul, born on this machine 2026-10-31. No other topic tag exists here yet; the engineering ones (`code-quality`, `ops`, `invariant`, `risk`) belong to interlingua, where the program lives.

**`needs-grilling`, a topic tag standard in every repo of this tree since 2026-10-31 (Nicklas).** Not sharp enough to build; the next step is a grilling with Nicklas, and the tag is there so such a ticket reads on the board at a glance. The board files it in Awaiting you, since the grilling is Nicklas's, and its status label is `ready-for-human` for the same reason (Nicklas, 2026-11-02). `/to-spec` takes it off when the spec is published. Distinct from `wayfinder:grilling`, which marks a map's child ticket and nothing else.

## What is deliberately not here

- **GitHub's unused defaults**: `documentation`, `duplicate`, `good first issue`, `help wanted`, `invalid`, `accessibility`, deleted at setup. Each was a fourth type competing with the three above, and none had ever been used across the four repos in this tree that carried them.
- **`blocked` / `blocker`**: native issue dependencies say the same thing and keep themselves true. A label drifts the moment somebody closes the blocker and forgets. See `issue-tracker.md` § Blocking and sub-issue links.
