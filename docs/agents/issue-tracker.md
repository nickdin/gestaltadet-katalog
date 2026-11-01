# Issue tracker: GitHub

Issues and specs for this repo live as GitHub issues at **`nickdin/gestaltadet-katalog`**, public. Use the `gh` CLI for all operations. `gh` resolves the repository from `origin`; no flag is needed.

**This tracker takes work on the catalogue only**: a concept, a mapping row, a decision behind them, the two example organisations. Work on the program that reads the catalogue, a feature, a bug, a command that misbehaves, goes to `nickdin/interlingua` even when it is discovered here (`CLAUDE.md` § Frågor in, ändringar hans). Issue text here is Swedish, like the data.

**The tracker is public, and readers are invited to file here.** A reader's question or objection is a `question` until it turns into a change; the answer closes it, and a change in a definition is Nicklas's to make. No issue, comment or label text names a real organisation, unit, system or internal document (`CLAUDE.md` § Ingen verklig organisation): an example is drawn from Myndigheten för föreningsstöd or the housing company in `docs/exempel/`.

## Conventions

- **Create an issue**: `gh issue create --title "..." --body "..."`. Use a heredoc for multi-line bodies.
- **Read an issue**: `gh issue view <number> --comments`, filtering comments by `jq` and also fetching labels.
- **List issues**: `gh issue list --state open --json number,title,body,labels,comments --jq '[.[] | {number, title, body, labels: [.labels[].name], comments: [.comments[].body]}]'` with appropriate `--label` and `--state` filters.
- **Comment on an issue**: `gh issue comment <number> --body "..."`
- **Apply / remove labels**: `gh issue edit <number> --add-label "..."` / `--remove-label "..."`
- **Close**: `gh issue close <number> --comment "..."`

**Pace bulk issue creation at about 15 s per call.** GitHub has a secondary content-creation limit that `gh api rate_limit` does not report: it read 5000 of 5000 remaining while every call failed, and took 12 minutes to clear. Measured on `vault-recorder` 2026-08-27 (failed on the 28th unpaced) and `daemon-monitor` 2026-08-31 (25 in a row at 15 s, no failures).

## Blocking and sub-issue links

Two relationships that must exist as **real links**, not as sentences in a body. A "Blocked by" heading is for a human reading the ticket; nothing else can see it, so a tracker built on prose alone never updates itself.

- **Sub-issue**: a ticket belongs to the spec it came from. This link is what draws the progress bar on the parent, which is how a milestone's progress is read without opening anything. `gh issue create --parent <parent> ...`, or `gh issue edit <parent> --add-sub-issue <child>` afterwards (`gh` 2.94+). Older `gh`: GraphQL `addSubIssue(input:{issueId, subIssueId})`, on `node_id`s rather than numbers: `gh api graphql -f query='mutation{addSubIssue(input:{issueId:"<parent-node-id>",subIssueId:"<child-node-id>"}){clientMutationId}}'`. Get a `node_id` with `gh issue view <n> --json id --jq .id`.
- **Blocked by**: GitHub's native issue dependencies, the canonical, UI-visible representation. `gh api --method POST repos/nickdin/gestaltadet-katalog/issues/<child>/dependencies/blocked_by -F issue_id=<blocker-db-id>`, where `<blocker-db-id>` is the blocker's numeric **database id** (`gh api repos/nickdin/gestaltadet-katalog/issues/<n> --jq .id`, *not* the `#number` or `node_id`). GitHub reports `issue_dependencies_summary.blocked_by`, counting open blockers only, which is the live gate. A ticket is unblocked when every blocker is closed.

Native dependency links are also why no `blocked` label exists here: a link keeps itself true when the blocker closes, and a label does not.

Where sub-issues or dependencies are unavailable, fall back to a task list in the parent body and a `Blocked by: #<n>, #<n>` line at the top of the child, and say in the ticket that the link is prose.

## Pull requests as a triage surface

**PRs as a request surface: no.** _(Set to `yes` if this repo treats external PRs as feature requests; `/issue-triage` reads this flag.)_

When set to `yes`, PRs run through the same labels and states as issues, using the `gh pr` equivalents:

- **Read a PR**: `gh pr view <number> --comments` and `gh pr diff <number>` for the diff.
- **List external PRs for triage**: `gh pr list --state open --json number,title,body,labels,author,authorAssociation,comments` then keep only `authorAssociation` of `CONTRIBUTOR`, `FIRST_TIME_CONTRIBUTOR`, or `NONE` (drop `OWNER`/`MEMBER`/`COLLABORATOR`).
- **Comment / label / close**: `gh pr comment`, `gh pr edit --add-label`/`--remove-label`, `gh pr close`.

GitHub shares one number space across issues and PRs, so a bare `#42` may be either: resolve with `gh pr view 42` and fall back to `gh issue view 42`.

## When a skill says "publish to the issue tracker"

Create a GitHub issue.

## When a skill says "fetch the relevant ticket"

Run `gh issue view <number> --comments`.


## The board

https://github.com/users/nickdin/projects/22: seven lanes: Todo, In Progress, Done, Blocked, Awaiting you, Parked, Triage. `/work-the-board` only runs in a repo that has one.

**Two of its workflows cannot be enabled through any API and are Nicklas's clicks:** *Auto-add to project* (this repo, filter `is:issue is:open`) and *Item closed* (target status Done). Until both are on, a new issue never reaches the board and a closed issue's card never moves to Done, silently, in both directions. Add cards explicitly with `gh project item-add` while they are off.

**A card that auto-add creates has no lane.** An issue made with `gh issue create` outside a board run lands under *No status* and stays there (measured on interlingua 2026-10-02, its #278–#281). `~/.claude/scripts/board-status.sh` files cards from what the tracker already says, so run it rather than setting lanes by hand:

- **After filing an issue, changing a status label, or adding or removing a blocking edge**: `~/.claude/scripts/board-status.sh sync`. It reads every open issue's labels and native blocked-by links and files each card into its lane (`needs-triage` → Triage, `ready-for-human` → Awaiting you, `parked` → Parked, `ready-for-agent` → Todo, Blocked while an open blocker remains). `/issue-triage` runs it as its last step because this line names it.
- **When you start working an issue**: `~/.claude/scripts/board-status.sh <number> in-progress`. No label says work has started, so `sync` cannot make that move.
- **To check**: `~/.claude/scripts/board-status.sh list none` prints the issues whose card has no lane; it should print nothing.

Confirm with:

```bash
gh api graphql -f query='{user(login:"nickdin"){projectV2(number:22){workflows(first:20){nodes{name enabled}}}}}'
```

**A fresh board may not list `Auto-add to project` at all** (measured on `backup`, 2026-08-31), so that one has to be confirmed by eye; only *Item closed* is verifiable this way.

**Board writes are throttled by a GraphQL *point* budget that `gh api rate_limit` reports as untouched while every call fails.** An exhausted budget makes `gh project item-add` answer `unknown owner type`, which reads like a bad `--owner` flag and not like a limit. Probe with `gh api graphql -f query='{viewer{login}}'`; never trust `rate_limit` about GraphQL. Pace board writes at about 6 s.

## Wayfinding operations

Used by `/wayfinder`. The **map** is a single issue with **child** issues as tickets.

- **Map**: a single issue labelled `wayfinder:map`, holding the Notes / Decisions-so-far / Fog body. `gh issue create --label wayfinder:map`.
- **Child ticket**: an issue linked to the map as a sub-issue, see § Blocking and sub-issue links above. Labels: `wayfinder:<type>` (`research`/`prototype`/`grilling`/`task`). Once claimed, the ticket is assigned to the driving dev.
- **Blocking**: native issue dependencies, see § Blocking and sub-issue links above for the command and the fallback.
- **Frontier query**: list the map's open children (`gh issue list --state open`, scoped to the map's sub-issues / task list), drop any with an open blocker (`issue_dependencies_summary.blocked_by > 0`, or an open issue in the `Blocked by` line) or an assignee; first in map order wins.
- **Claim**: `gh issue edit <n> --add-assignee @me`, the session's first write.
- **Resolve**: `gh issue comment <n> --body "<answer>"`, then `gh issue close <n>`, then append a context pointer (gist + link) to the map's Decisions-so-far.

The five `wayfinder:*` labels are not created here. `/wayfinder` creates them on its first run.
