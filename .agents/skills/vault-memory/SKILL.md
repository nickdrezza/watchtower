---
name: vault-memory
description: >
  Refresh the vault's .agents/memory/ from everything that happened since it was last updated —
  local AI-platform history (Claude Code sessions, Codex sessions and its own memory store) plus the tracker,
  email, GitHub, and Drive meeting notes. Extracts the durable facts an agent would otherwise
  rediscover — how a platform connects, where a credential lives, a gotcha that cost hours, a decision
  and its reason, project state — and files them into the right memory file. Use when the user says
  "update my memory", "catch up my agent memory", "dump this week's context", "what did I learn this
  week", "refresh the memory directory", "save this before I forget", or as step 2 of vault-sync.
  Writes ONLY to .agents/memory/ — for vault notes use watchtower, for the weekly log use
  weekly-work-log.
user-invocable: true
argument-hint: "update my memory"
---

# Vault memory

`.agents/memory/` is the sub-vault agents dump context into so it survives past the session that
learned it. This skill closes the gap between "an agent figured that out three weeks ago" and "it's
written down."

Follow `watchtower`'s **How to write here** rules — they apply to memory files just as hard.
Verbosity is the failure mode; a memory file nobody can scan is a memory file nobody reads.

## Scope

**In:** `.agents/memory/*.md`. **Out:** vault notes, the weekly log, the shared vault. If something belongs
in a note rather than memory, say so and hand off — don't write it in both places.

Memory holds **durable environment facts**. It is not a diary. The test for a candidate fact:

> Would a fresh agent, six weeks from now, do the job worse without this?

If no, drop it. Session narrative, one-off numbers with no decision attached, and anything already
obvious from the code all fail that test.

## 1. Set the window

Default start = the last commit touching memory:

```bash
git log -1 --format=%cI -- .agents/memory/
```

Use that, or the user's stated window. If nothing has ever been committed, ask how far back to go
rather than scanning everything. State the window you're using before you scan.

## 2. Gather**. Sources, in
descending value:

| Source | Where | Yields |
|---|---|---|
| **Claude Code** | session-mgmt MCP (`list_sessions`, `search_session_transcripts`) | The richest source — solved problems, connection recipes, gotchas |
| **Claude Code memory** | `<claude-home>/projects/<slug>/memory/` + its `MEMORY.md` | **Already-distilled facts.** Highest value per token; check it every run — it grows silently and isn't in git |
| **Codex** | `<codex-home>`: `session_index.jsonl`, `sessions/`, `archived_sessions/`, `memories/` | Same, from the other agent |
| **the tracker** | the tracker MCP — assigned + updated in window, PROJ and SR | Ticket state, scope changes, decisions |
| **email** | email MCP | Requests, decisions, stakeholder constraints |
| **GitHub** | `gh` — merged + open PRs (on Windows, from WSL) | What actually shipped |
| **Drive** | Drive MCP — Gemini meeting notes | Decisions and follow-ups |

**Both laptops are live** — the Mac and the Windows box each hold their own Claude and Codex history, and
you can only see the one you're running on. Scan it, then **say in the report which machine you covered**;
the other one's sessions are a known blind spot, not an empty set. Paths per target are in
`reference.md`; WSL `~/.claude` and `~/.codex` are the one stale pair — skip them. Continue, Copilot,
Antigravity, and Zed stores are deliberately **not** scanned
(VS Code-style sqlite, undocumented schemas, brittle); if the user wants them, treat it as new work.

Titles and metadata first. Only pull full transcripts for sessions that look like they carry a durable
fact — transcript reads are expensive and most sessions carry nothing.

## 3. Triage into a candidate table

One row per candidate fact. Present this **before writing anything**.

| fact | target file | new / updates / contradicts | evidence | `#ACME`? |
|---|---|---|---|---|

- **target file** — one of the 16 in `.agents/memory/`. If a fact fits nowhere, propose a new file and
  say why; don't force it.
- **contradicts** is the important column. Memory that disagrees with itself is worse than missing
  memory. Flag the conflict, say which side you believe and why, and let the user settle it.
- Merge duplicates across sources into one row.

## 4. Ask

Ask about anything you inferred rather than read, any contradiction, and any fact that would be
embarrassing to get wrong (an account id, a role, a path). **One batched multiple-choice set**, before
writing. Don't ask about the obvious.

## Verification preview before writing

This skill always runs the **full path** — a multi-fact run is never fast-path eligible. (The fast
path is for a single fact captured mid-session in some other context; conditions in
[`../../memory/README.md`](../../memory/README.md) → *When to write memory*.)

After the candidate facts are settled, follow the vault-wide verification preview. By default,
show the exact proposed Markdown or diff for every `.agents/memory/*.md` change here before writing.
An explicit current-request bypass such as `full permissions`, `auto merge`, `just merge`, `skip
verification`, or `write it directly` skips that human preview and approval. The bypass does not allow
invented facts or secret values; unresolved facts remain open questions.

## 5. Write

- Slot each approved fact into the **existing** structure — extend a table, add a bullet, tighten a
  paragraph. Don't append a dated changelog section; memory is organized by topic, not by when it was
  learned.
- **Date anything that will age**: counts, ticket statuses, "as of" numbers, "verified <date>".
- **Locations, never values** — the hard rule. Recording that a token lives in
  `events-api/env/.env` as `HS_PROSPECT_SYNC_TOKEN` is the goal; the token itself never lands here.
- **Tag `#ACME`** on employer-specific files and sections, per `watchtower`. Portable files
  (`environment.md`, `credentials.md`'s non-Acme rows, `git-and-tickets.md`'s tooling half,
  `working-preferences.md`) stay untagged.
- **Prune while you're in there.** Delete facts now proven wrong, collapse duplicates, drop
  project blocks that closed. Growth without pruning is how this becomes unreadable.
- Keep `projects.md` compact — a pointer plus what's needed to resume. Deep narrative belongs in
  `Spaces/Work/Current Work/Projects/`.
- Update `.agents/memory/README.md` if you added or removed a file.

## 6. Report

Concise: window scanned, sources reached (and any that were unavailable), facts added / updated /
pruned, and open questions. **Don't sync** — `vault-sync` ships it. Say whether there's anything worth
committing.

## Related

- `watchtower` — the writing rules, the `#ACME` convention, the memory index.
- `vault-sync` — commits and ships what this produces.
- `weekly-work-log` — same sources, different output: the manager-facing log, not memory.
