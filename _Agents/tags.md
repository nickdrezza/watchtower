---
type: index
status: active
domain: system
workspace: vault
title: "Tag Registry"
description: "Every tag allowed in this vault and when to apply it; wt doctor reports any tag not listed here."
updated: 2026-10-06
related:
  - "[[README|Watchtower]]"
  - "[[Concepts/index|Concept Index]]"
---

# Tag Registry

**Every tag allowed in this vault, and when to apply it.** A tag not on this page should not exist — if
you need one, add it here in the same commit (see [Changing a tag](#changing-a-tag)).

Tags carry three useful facets: **graph scope**, **employer scope**, and **subject matter**. Everything
structural — what a note *is*, its lifecycle, its dates — lives in properties, where the Bases read it.
The `personal` and `work` scope tags are deliberate graph-filter flags; do not add tags that merely
restate `type:`, `domain:`, or `workspace:`.

## Why the vocabulary is deliberately small

Graph view is the visible reason. **The load-bearing one is retrieval.** A small, registry-bound
vocabulary is what lets an agent fetch exactly what a task needs and pull in nothing else — and that
matters *more* as the vault grows, not less. A vault that accumulates tags freely gets slower and
worse to work in, because every fetch drags unrelated material along with it.

So the discipline is the point, not the bureaucracy: one tag per concept, a concept note behind every
`topic/*`, and no tag that merely restates a property. See
[*Structure exists to make retrieval cheap*](<memory/working-preferences/Structure makes retrieval cheap.md>).

Live counts are in Obsidian's **Tags** pane; they're deliberately not duplicated here, so this page
can't go stale on numbers alone.

## Scope

| Tag | Apply to |
|---|---|
| `personal` | Personal-life notes under `Spaces/Personal`, including diary, memories, reflections, personal people/locations/pets, literature, and personal staging notes. A genuinely mixed note may also carry `work`. |
| `work` | Professional material under `Spaces/Work` (current Acme work) and `Spaces/Career` (career notes). A genuinely mixed note may also carry `personal`. |
| `ACME` | Anything only meaningful while you is at Acme Analytics — projects, tickets, systems, people, meeting notes, work logs, client and event material, and employer-specific memory files. Acme work normally carries both `work` and `ACME`. **Don't** tag machine setup, personal notes, or portable future-work material. A mostly-portable file with one employer-specific section gets an inline `#ACME` on that section instead. |

## Subject matter — `topic/*`

One per note in `Concepts/`, and **a `topic/*` tag always rides along with a `[[link]]` to its concept**.
Tag and link go in together or neither does. Full concept list: [[Concepts/index|Concept Index]].

| Tag | Concept | What it marks |
|---|---|---|
| `topic/agents` | [[AI Agents]] | AI agents, prompts, and the agent layer that operates this vault — skills, memory, intake workflow. |

**One row ships, deliberately.** `topic/agents` is the worked example; the vocabulary is meant to grow
out of your notes, not to arrive pre-filled with someone else's subjects. Expect a handful within a
month — the systems you actually work in, one row each.

Adding one is three steps in one commit, in this order:

1. Write the concept note in `Concepts/`.
2. Run `_Agents/wt index` so it shows in [[Concepts/index|Concept Index]].
3. Add the row here.

Do it in the other order and you get a tag with nothing behind it, which is the failure this registry
exists to prevent — `vault-doctor` flags any tag used but not registered.

## Provenance

Not subject matter — these record where a note *came from*, which nothing else captures. Leave them
alone; don't add new ones without a reason this concrete.

| Tag | Meaning |
|---|---|
| `source/pdf-converted` | The note is text extracted from a PDF, because this vault holds no binaries. Currently the 2023 AWS Innovate material. |
| `source/shared-vault` | The content is derived from the Acme team **shared-vault**, which stays its source of truth. Marks what to re-check when the wiki moves. Frontmatter on files that are wiki-derived as a whole (Shared Vault Index, inbound `Reference/` notes, the memory files carrying wiki facts); inline `#source/shared-vault` on the one derived section of a note that is otherwise his own. Applied by the `shared-vault-ingest` skill; ledger is Shared Vault Ingest. |
| `assets/images-converted` | The note holds text descriptions standing in for image embeds that were removed. |

## Reserved

| Tag | Meaning |
|---|---|
| `excalidraw` | **Required by the Excalidraw plugin to render the file — never strip it.** Not a vault convention and not subject to this policy. |
| `repo/docs` | Agent-layer only (`_Agents/README.md`). The agent layer is written for agents, not for the graph, so it sits outside the vault's tag and frontmatter policy even though Obsidian indexes it. |

## People are notes, not tags

There is no `person/*` namespace, and there should not be one. A person is an **entity** with attributes
— email, role, org, current or former — and a tag can hold none of them. People live in
`Spaces/Work/People/`, indexed by [[Spaces/Work/People/index|People Index]], and are linked from a note's
`people:` property. That gives real graph nodes and real backlinks: open a person, see every log and
project that involved them. A tag would give a flat list and nothing else.

## What is deliberately untagged

Infrastructure notes carry **no scope tags**: `README.md`, `_Templates/`, and agent-layer
documentation. Personal and work landing pages live inside their respective spaces and do carry
their scope tag so Graph view can filter those spaces consistently. `type: index` notes still get no
`topic/*` tags — they link to everything, so inherited topics are pure noise.

## Changing a tag

**This page is the authority. Any tag change updates it in the same commit** — otherwise the vocabulary
drifts and the next agent invents a parallel one.

Adding a `topic/*` tag:

1. Confirm it's subject matter, not something `type:`/`domain:`/`workspace:` already says. If a property
   covers it, stop — no tag.
2. There must be a note in `Concepts/` behind it. No concept note → create the concept first, or don't
   add the tag. A `topic/*` with nothing to link to is a dead node in the graph.
3. Register it here, check that the concept shows in [[Concepts/index|Concept Index]], and set the tag on the concept note itself.
   This page is the only place the tag-to-concept mapping is written down — keep it that way.
4. Backfill it onto existing notes that already link the concept — derive it from the links, don't
   reclassify by hand.

Adding or changing a scope tag:

1. Use `personal` for personal-space content and `work` for work-space content; mixed notes may carry
   both. Use `ACME` only when the material is employer-specific.
2. Do not use a scope tag as a substitute for `type:`, `domain:`, or `workspace:` — it exists so
   Graph view can filter across folders.
3. Update this registry in the same commit, and say so in the PR description.

Renaming or retiring a tag:

1. Update this page first, so the diff shows the intent.
2. Sweep every note's frontmatter; confirm nothing is left with `grep -rn '<tag>' --include='*.md'`.
3. Check `Spaces/Work/Dashboards/*.base` — Bases filter on `type ==` today, so a tag change shouldn't touch them.
   If one ever does filter on a tag, fix it in the same commit.
4. Say so in the PR description.

Full policy and rationale: root `AGENTS.md` and the `watchtower` skill → *Tagging*.
