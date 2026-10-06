---
name: vault-sync
description: >
  Syncs the vault to GitHub: pulls main, runs weekly-work-log and vault-memory, then commits on a
  branch, opens a PR, and merges it. Use for "sync my vault", "push my vault", "back up the vault", or
  "commit my vault".
user-invocable: true
argument-hint: "sync my vault"
---

# Vault sync

Get the vault current and onto `main` through a PR. This skill **orchestrates**; it doesn't author.
Writing rules and the `#ACME` convention come from `watchtower`.

Default flow: **pull → weekly-work-log → vault-memory → commit → PR → merge → summarize.**

Skip steps 2–3 for a plumbing-only sync ("just push what I've got"). If that's ambiguous and there are
already uncommitted edits, ask which they want.

## Verification preview for note-bearing syncs

The weekly log, memory, and any other vault Markdown written during sync follow the universal
`vault preview` gate. By default, show the exact proposed Markdown and index/diff changes in chat
before writing. An explicit current-request phrase such as `full perms`, `skip verification`, or
`write it directly` bypasses that human preview and approval. It does not bypass secret, binary, space-boundary, factual-integrity, branch, or PR safety rules.

## Environment

Remote `git@github.com:<you>/<your-vault>.git`, default branch `main`. Everything else here is
per-machine — **read `_Agents/memory/environment.md` and the one `machines/` profile it routes you to
before running a single command.** The vault path, whether `git`/`gh` need a shell wrapper, and which
`gh` identity you get all differ by target, and using the other machine's invocation is the most common
failure in this skill.

Two constraints that only apply on the wrapped target (the Windows box, `git`/`gh` from WSL):

- **Write commit messages and PR bodies to files**, then `-F` / `--body-file`. Inline `-m` through the
  `wsl.exe … -lc` wrapper mangles multi-line text and backticks; custom shell vars get mangled too, so
  use literal paths and `$HOME` only.
- Spell paths out in full and quote them — the 8.3 short name won't resolve across the boundary.

On an unwrapped target (the Mac) there is one shell and one identity: `git` and `gh` run directly.
Writing the message to a file is still the safer habit.

## 1. Pull first

```bash
git fetch origin --prune
git log --oneline origin/main -5
git status --short --branch
```

Local refs go stale between sessions, and the vault gets edited from other machines and the web. Note
whether `origin/main` moved and whether the tree is dirty / ahead / behind.

If `main` is behind and the tree is clean, `git merge --ff-only origin/main` so steps 2–3 read current
content. If the tree is dirty, leave `main` alone — step 5 branches off `origin/main` anyway.

## 2. Weekly work log

Hand off to **`weekly-work-log`**. It gathers the week's real activity, asks about anything uncertain,
and writes the log in the house format.

If this week's log already exists and is complete, say so and move on — don't rewrite it.

## 3. Memory

Hand off to **`vault-memory`**. It scans local AI-platform history plus the tracker/email/GitHub/Drive since
memory was last committed, produces a candidate table, asks, then writes to `_Agents/memory/` and the space `memory/` folders.

Both skills stop before committing. That's this skill's job.

## 4. Safety gate — before staging anything

- **Secret scan:**
  ```bash
  git diff | grep -nEi 'private key|password|client_secret|AKIA|api[_-]?key|ghp_|pat-na1|xox'
  ```
  A hit means stop, strip it, tell the user, and point at `~/.ssh` / your secret manager / `~/.credentials`. The
  repo's extension check misses inline secrets; you are the backstop. Expect benign hits on files that
  *document* these patterns — read each one rather than trusting the count.
- **No binaries:** confirm the diff is text only. `.gitignore` covers `*.pem`, `*.key`, `*.p8`, `*.p12`,
  `*.env`, images, PDFs — if one is staged, unstage it.
- **Stage only intended files.** Never `git add -A`. The tree routinely carries `.obsidian/app.json`
  churn and stray `Untitled*.canvas` files; both stay out.
- **`.claude/skills/` is gitignored** — an old copy. If it appears, don't commit it.
- Confirm `ACME` tags are set on new or edited employer-specific files.

## 5. Branch and commit

```bash
git checkout -b content/<slug> origin/main
```

`content/<slug>` for notes and memory, `feat/<slug>` for agent-layer changes. Branching off
`origin/main` carries uncommitted edits over cleanly when the file's base matches main.

Stage the intended files, then `git commit -F <msgfile>`. End the message with the Co-Authored-By
trailer.

## 6. Reconcile

Branching off `origin/main` usually means no divergence. If it advanced mid-flight,
`git rebase origin/main`. **On a conflict inside a note, keep both sides** — union the edits so nothing
he wrote is lost (`watchtower` hard rule 3). If a conflict is genuinely ambiguous, show both
versions and ask, then `git rebase --continue`.

## 7. PR and merge

```bash
git push -u origin content/<slug>
gh pr create --base main --title "<title>" --body-file <bodyfile>
gh pr merge <branch> --merge --delete-branch
```

Solo repo — self-merging is expected. **Always go through a PR**; never push straight to `main`.
`--delete-branch` cleans local + remote and returns you to `main`.

## 8. Verify and report

```bash
git fetch --prune
```

Confirm the PR is `MERGED`, the tree is back on a clean `main`, the change is on `main`, and no stray
branch remains (`git branch -a`).

Then report — **concise, no step-by-step narration**:

```
Synced. PR #<n> merged.

Work log   week of <Mon D–Fri D> — <n> projects
Memory     <n> added, <n> updated, <n> pruned — <files touched>
Notes      <anything else that shipped>
Skipped    <what you deliberately left out, if any>
```

Plus the PR URL and any open questions. If nothing needed syncing, say so in one line and stop.

## Related

- `watchtower` — writing rules, `#ACME`, and the hard rules this skill enforces.
- `weekly-work-log` (step 2) · `vault-memory` (step 3).
