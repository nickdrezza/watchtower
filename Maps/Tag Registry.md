---
type: index
status: active
domain: system
workspace: vault
related:
  - "[[Home]]"
  - "[[Concept Index]]"
  - "[[Vault Architecture]]"
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
[`.agents/docs/operating-model.md`](../.agents/docs/operating-model.md) → *Structure exists to make
retrieval cheap*.

Live counts are in Obsidian's **Tags** pane; they're deliberately not duplicated here, so this page
can't go stale on numbers alone.

## Scope

| Tag | Apply to |
|---|---|
| `personal` | Personal-life notes under `Spaces/Personal`, including diary, memories, reflections, personal people/locations/pets, literature, and personal staging notes. A genuinely mixed note may also carry `work`. |
| `work` | Professional material under `Spaces/Work`, including current Acme work and future-work/career notes. A genuinely mixed note may also carry `personal`. |
| `ACME` | Anything only meaningful while you is at Acme Analytics — projects, tickets, systems, people, meeting notes, work logs, client and event material, and employer-specific memory files. Acme work normally carries both `work` and `ACME`. **Don't** tag machine setup, personal notes, or portable future-work material. A mostly-portable file with one employer-specific section gets an inline `#ACME` on that section instead. |

## Subject matter — `topic/*`

One per note in `Concepts/`, and **a `topic/*` tag always rides along with a `[[link]]` to its concept**.
Tag and link go in together or neither does. Full concept list: [[Concept Index]].

| Tag | Concept | What it marks |
|---|---|---|
| `topic/agents` | [[AI Agents]] | AI agents, prompts, and the agent layer that operates this vault — skills, memory, intake workflow. |
| `topic/aws` | AWS | AWS work of any kind: the EC2 automation server, CloudWatch, DR, and the AWS training material. |
| `topic/warehouse` | the warehouse project | The Acme the warehouse project — its layers, table grains, and the models that build it. |
| `topic/data-quality` | Data Quality | DQ scores, rules, drift, coverage, and the remediation epics against them. |
| `topic/transform` | dbt | dbt models, tests, and dbt Cloud jobs and CI. |
| `topic/networking-app` | the networking app | the networking app, the event networking platform fed from the events platform registration data. |
| `topic/crm` | the CRM | the CRM objects, properties, associations, and the syncs into and out of it. |
| `topic/tickets` | Tickets | Ticket-level work — issues, sprints, epics, and the roadmap. |
| `topic/segmentation` | Segmentation | The events Matching & Sorting process: client personas, priority lists, and the matching logic. |
| `topic/newsletter` | the newsletter platform | the newsletter platform — the newsletter/subscriber platform, its share, SFTP, and ad stats. |
| `topic/warehouse-db` | the warehouse | the warehouse itself: accounts, roles, warehouses, and SQL run against it. |
| `topic/events` | the events platform | the events platform — events, registrations, registrant types, and the `the events platform_API` jobs. |
| `topic/vendor` | the vendor platform | the vendor platform, the vendor integration with write access into the the warehouse project. |

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
| `repo/docs` | Agent-layer only (`.agents/README.md`). The agent layer is a dot-dir Obsidian never indexes, so it sits outside the vault's tag policy. |

## People are notes, not tags

There is no `person/*` namespace, and there should not be one. A person is an **entity** with attributes
— email, role, org, current or former — and a tag can hold none of them. People live in
`Spaces/Work/Current Work/People/`, indexed by [[People Index]], and are linked from a note's
`people:` property. That gives real graph nodes and real backlinks: open a person, see every log and
project that involved them. A tag would give a flat list and nothing else.

## What is deliberately untagged

Infrastructure notes carry **no scope tags**: the `Maps/` indexes, `_Templates/`, and agent-layer
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
3. Register it here, add the concept to [[Concept Index]], and set the tag on the concept note itself.
   This page is the only place the tag-to-concept mapping is written down — keep it that way.
4. Backfill it onto existing notes that already link the concept — derive it from the links, don't
   reclassify by hand.

Adding or changing a scope tag:

1. Use `personal` for personal-space content and `work` for work-space content; mixed notes may carry
   both. Use `ACME` only when the material is employer-specific.
2. Do not use a scope tag as a substitute for `type:`, `domain:`, or `workspace:` — it exists so
   Graph view can filter across folders.
3. Update this registry and add a dated line to [[Vault Maintenance]] in the same commit.

Renaming or retiring a tag:

1. Update this page first, so the diff shows the intent.
2. Sweep every note's frontmatter; confirm nothing is left with `grep -rn '<tag>' --include='*.md'`.
3. Check `Dashboards/*.base` — Bases filter on `type ==` today, so a tag change shouldn't touch them.
   If one ever does filter on a tag, fix it in the same commit.
4. Add a dated line to [[Vault Maintenance]].

Full policy and rationale: root `AGENTS.md` and [[Vault Architecture]].
