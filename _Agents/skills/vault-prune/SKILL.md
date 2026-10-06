---
name: vault-prune
description: >
  Finds slop, near-duplicates, bloated or stale notes, orphans, and gaps, and proposes each change for
  approval. Use for "prune my vault", "clean up the vault", "any duplicates", "what should I delete",
  or "what's missing".
user-invocable: true
argument-hint: "[folder|all]"
---

# Vault prune

The vault's value is being scannable in two years. Growth without curation is how it stops being that
— and a careless agent adding bloated notes is the fastest way there. This is the backstop.

**Run `vault-doctor` first.** It handles everything mechanical; this skill only makes judgement calls,
and every one of them needs approval.

## The hard constraint

**Hard rule 3: never delete a note or rewrite his wording.** This skill *proposes*; he decides. That is
not a formality — a pruning pass with delete authority is the single most destructive thing in this
repo.

- **Per-item approval, always.** One batched decision table, then act only on approved rows. Silence is
  not approval.
- **Consolidation carries the original wording across.** Merging two notes means both texts survive in
  the target, restructured — never re-summarized in your voice.
- **Never prune his rough notes for being rough.** Raw dumps and half-formed reflections are supposed to
  read that way. The target is *agent-generated* bloat and genuine redundancy, not his voice.
- Deleting is the last resort. Prefer merge → simplify → archive (`status: done`, move to `Archive/`)
  → delete.

## Scope it before you start

The whole vault is 400+ notes; a single pass over all of it produces a table nobody reads. Default to
one folder or one space per run, say which you swept, and **state plainly what you did not look at.** A
cap that reads as "that's everything" is the failure mode here.

## What to look for

| Category | The test | Default action |
|---|---|---|
| **Slop** | Written by an agent, and fails `AGENTS.md` hard rule 7 — closing summaries, "In conclusion", padded intros, headers over one sentence, evaluative adjectives about the work, invented "next steps" | Simplify to the facts. Delete only if nothing survives |
| **Near-duplicate** | Two notes cover the same subject with no distinct nuance | Merge into the more-linked one, carry both wordings, leave the other as a redirect or delete it |
| **Bloated** | Says in five paragraphs what a table says in five lines | Restructure. **Cut words, never facts** — the gotcha, the id, the reason all survive |
| **Stale** | A claim now contradicted by the code, the data, or a newer note | Correct it and date it, or mark it superseded. Never silently overwrite something he wrote deliberately |
| **Orphan** | Nothing links to it and it links to nothing | Usually needs a link or an index row, not deletion. Genuinely inert → propose archiving |
| **Misfiled** | Acme material in a personal space, or vice versa | Move it (hard rule 4). Use `vault-edit` so links and indexes follow |
| **Gap** | A concept referenced repeatedly with no note behind it, or a `topic/*` with no concept | Propose creating it — don't create it silently |

Memory files have their own pruning rule inside `vault-memory` (*"prune while you're in there"*). Don't
duplicate that work here; if a memory file needs it, hand off.

## The pass

1. **`vault-doctor` first.** Mechanical noise makes quality judgement unreliable.
2. **Inventory the scope** — paths, sizes, last-modified, inbound link counts. Size and link count
   together find both bloat and orphans cheaply.
3. **Read the candidates in full.** Never judge a note from its filename or first paragraph.
4. **Build the decision table** — one row per proposal: path, category, evidence, proposed action, what
   is lost. Rank worst-first, cap at ~15, and say what the cap left out.
5. **Ask, per item.** Batched, before any write. Anything you inferred rather than read gets flagged as
   inferred.
6. **Apply only approved rows**, on a branch, in a PR (the diff is the preview).
7. **Report** — counts by category, what was left alone and why, and gaps recorded as open questions
   rather than invented content.

## Before you finish

- [ ] Nothing deleted that wasn't explicitly approved, by path.
- [ ] Every merge carries the original wording; nothing re-voiced.
- [ ] Links and indexes updated for every move (`vault-edit` owns the mechanics).
- [ ] `_Agents/tags.md` updated in the same commit as any tag change.
- [ ] Re-ran `vault-doctor` — a prune pass breaks links if you let it.
- [ ] Report says what you *didn't* sweep.

## Related

- `vault-doctor` — the mechanical half. Always first.
- `vault-edit` — how to actually move, rename, merge, or delete without breaking the graph.
- `vault-memory` — prunes `_Agents/memory/` as part of its own run.
- `watchtower` — hard rules and the writing standard this skill enforces.
