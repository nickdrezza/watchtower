---
name: weekly-work-log
description: >
  Write or update the weekly work log in this vault — gather the week's real activity, verify it, ask
  before asserting anything uncertain, and produce a concise manager-facing log in the house format.
  Use when the user says "write my work log", "update my log for the week", "log my week", "fill in
  last week", "add my weekly log", or wants their weekly log written or updated. Also step 2 of
  vault-sync. Pairs with watchtower (writing rules) and vault-sync (ships it).
user-invocable: true
argument-hint: [week]
---

# Weekly work log

The log a manager reads, usually as an email. Two rules dominate: **only what actually happened**, and
**keep it short**.

Follow `watchtower`'s **How to write here** rules. This log is where AI-slop shows up fastest — resist
filler, framing, and adjacent suggestions.

## Where it lives

- `Spaces/Work/Current Work/Work Logs/<YYYY>/Q<n>/MM-DD-YYYY.md`, dated by the **Monday** of the week
  (week of Mon 2026-07-13 → `07-13-2026.md`), filed under the quarter that Monday falls in. Template:
  `_Templates/Weekly Work Log.md`.
- Add the new week's note to the weekly-log index in `Maps/` as a wiki-link — it isn't generated.
- The current-week file may already exist as a stub or a mid-week draft. **Update it, don't duplicate.**
- Frontmatter: the weekly-log template in `watchtower`'s `reference.md`, carrying both the `work` scope
  tag and your employer tag — work logs are employer-specific by definition.

## Gather the week's activity

Mon–Fri of the target week. Every bullet must trace to one of these:

| Source | How |
|---|---|
| **Merged PRs** | `gh search prs --author=@me` + `gh pr list` on the work repos, filtered to the week. Strongest evidence. |
| **The issue tracker** | Assigned and updated tickets, plus any support board. If its connector is down, reconstruct from notification emails. |
| **Email** | Support requests, data requests, meetings, decisions. |
| **Prior agent sessions** | Session titles give the week's topics; read transcripts only if a title isn't enough. |
| **Meeting notes** | Whatever your notetaker writes to shared drive storage. |
| **The user** | Their own dictation always wins over inference. |

Query details and token-budget cautions live with [`vault-memory`](../vault-memory/SKILL.md) — same
sources, and the one place they're documented.

## Hard rules

1. **Only verified work.** Every bullet ties to a PR, ticket, email, calendar item, or the user's own
   words. **Never invent** row counts, metrics, meetings, or work that isn't in the evidence.
   Over-reaching here gets logs rejected.
2. **Ask before asserting anything uncertain.** For anything inferred but not backed — work with no
   merged PR, a "plan pending", a detail you're guessing — ASK "did you do X?" rather than writing it
   as fact. Batch the checks into **one short multiple-choice set**, and use the same pass to confirm
   the detail level wanted and whether anything's missing. Ask **before** the final write.
3. **Concise, manager-facing.** Default **medium**: whole-week, ~2–3 short bullets per project, roughly
   one line each. Offer tighter (~1 line/project) or fuller on request. No wall of text, no per-day
   breakdown unless asked.

## Verification preview before saving

Follow the vault-wide verification preview before creating or updating the weekly Markdown file or the
index. By default, show the complete proposed work-log Markdown and the exact index changes in chat
before writing. An explicit current-request bypass such as `full permissions`, `auto merge`, `just
merge`, `skip verification`, or `write it directly` skips that human preview and approval. It does not
permit invented work, unsupported claims, secrets, or a direct push to `main`.

## Format

```
## Week of <Mon D> – <Fri D>            (append "(in progress)" only for a mid-week update)

📝 Work Log

PROJECT TITLE (TICKET / EPIC)
- what shipped + PR / ticket refs — one line each

---
## Weekly Self-performance Review
GOAL 1: <standing goal 1 text>
Results: ...
GOAL 2: ...   GOAL 3: ...
```

Keep the CAPS project headers, the PR/ticket refs, and the goal review. Goal statements come from the
prior week's log — carry them forward verbatim. Fill results honestly; "no dedicated X this week" beats
stretching.

## Finish

- Scratchpad backlog goes in a scratch note, not the log.
- **Sync only when asked**, or confirm first — hand off to `vault-sync`. A mid-week "so far" update is
  often left local. (When `vault-sync` invoked *you*, just report back; it handles shipping.)

## Related

- `watchtower` — writing rules, the employer-scope tag, vault layout.
- `vault-sync` — ships the log through a PR.
- `vault-memory` — same sources, different output: durable environment facts, not the manager log.
