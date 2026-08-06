---
name: vault-edit
description: >
  The safe way to perform any CRUD operation on the vault — create, read, update, move, rename, merge,
  split, archive, or delete a note — without breaking wiki-links, indexes, dashboards, or tags. Use
  whenever the user says "create a note for X", "rename this note", "move this to the other space",
  "merge these two notes", "split this up", "archive that project", "delete this", "restructure this
  folder", "add a field to these notes", or asks for any structural edit. Also the reference for what
  each operation must update alongside the file itself.
user-invocable: true
argument-hint: "<operation> <note>"
---

# Vault edit

Every structural edit has side effects. A note is not a standalone file — it is a node in a link graph,
a row in one or more indexes, and a record the Dashboards filter on. **This skill is the checklist of
what else has to move.**

Load `watchtower` first for the hard rules and the writing standard. This skill is the mechanics.

## The three facts that make everything else make sense

1. **Wiki-links resolve by note *name*, not path.** Moving a note between folders breaks nothing.
   **Renaming it breaks every `[[link]]` to it.** This is the single most important asymmetry here.
2. **Dashboards filter on `type ==`**, not on tags or folders. Frontmatter is what makes a note visible
   to a view; get `type:` wrong and the note vanishes from the UI while looking fine on disk.
3. **Indexes are hand-maintained.** Nothing generates `Maps/*.md`. An unlisted note is invisible to a
   reader even though it exists.

## Per operation — what must move with the file

| Operation | Also update | Watch for |
|---|---|---|
| **Create** | The folder's index in `Maps/`; frontmatter from `_Templates/`; `related:` backlink; `topic/*` tag **only** if the concept note exists | Right space (hard rule 4). Register any new tag in `Maps/Tag Registry.md` in the same commit |
| **Read** | — | Read the whole note; don't answer from the first paragraph |
| **Update** | `updated`-style fields if the folder uses them; the index row if the title changed | **Never rewrite his wording** (hard rule 3). Add structure around it |
| **Move** | Index rows that name the folder; scope tags if the space changed | Links survive a move. `#ACME` may need adding or removing |
| **Rename** | **Every `[[old name]]` in the repo** — `grep -rn '\[\[Old Name\]\]'`; index rows; `related:` in other notes | The break-everything operation. Rename, then sweep, then verify zero hits remain |
| **Merge** | Target gets **both** wordings, restructured, nothing re-voiced; source becomes a redirect or is deleted; every inbound link repointed | Hard rule 3. Consolidation is allowed *because* the original text travels |
| **Split** | New notes indexed; the original keeps a pointer to the parts so nothing looks lost | Don't split a note that is fine as one |
| **Archive** | `status: done` (+ `completed:` where the folder uses it); optionally move to a sibling `Archive/` | Prefer this to deleting. `Active Projects.base` filters `status != "done"`, so the status is what retires it — not the move |
| **Delete** | Every inbound link; every index row | **Approval per path, explicitly.** Hard rule 3 — deleting is the last resort, after merge/simplify/archive |
| **Bulk field edit** | Every touched note; the registry if tags changed | Parse frontmatter **line-wise**, never with a DOTALL regex — that reads the next key as part of this one and eats file bodies |

## Order of operations

1. **Read the target(s) in full**, and the destination folder's existing notes — match their frontmatter
   over the generic template when they differ. Consistency within a folder wins.
2. **Find the inbound links** before touching anything:
   ```bash
   grep -rn '\[\[Note Name\]\]' --include='*.md' .
   ```
3. **Preview.** Every destination path, the exact Markdown or diff, frontmatter, links, tags, and index
   changes — per the vault-wide gate. Deletes and merges get per-path approval regardless.
4. **Apply**, then **update the indexes in the same change** — not as a follow-up.
5. **Verify with `vault-doctor`.** Structural edits are exactly what it exists to catch.

## Never

- Rename a note without sweeping its links. Half a rename is worse than none.
- `git add -A` — the tree carries `.obsidian/app.json` churn and stray `Untitled*.canvas`.
- Move Acme material into a personal or future-work space, or the reverse (hard rule 4).
- Delete anything staged in `Inbox/` or personal `Uncategorized.md` because it looks unfinished. That is
  what those places are for; `personal-triage` classifies them.
- Push to `main`. Branch → PR, via `vault-sync`.

## Related

- `vault-doctor` — verify after any structural edit.
- `vault-prune` — decides *what* to merge, simplify, or retire; this skill executes it safely.
- `personal-vault` / `personal-triage` — routing and classification inside `Spaces/Personal`.
- `watchtower` — hard rules, layout, property templates, the filing workflow.
