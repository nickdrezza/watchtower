---
name: shared-vault-ingest
description: >
  Brings the Acme team shared-vault INTO the vault — the inbound counterpart to
  `shared-vault-promote`. Indexes every wiki doc, extracts the operational facts and gotchas agents
  need into `_Agents/memory/`, links team docs from the matching `Concepts/` notes, and tracks a
  watermark so later runs only look at what changed. Use when the user says "pull the dev wiki into
  my watchtower", "sync the wiki into my vault", "index the team wiki", "what's new in the dev wiki",
  "pull the <X> page into my vault", or "is my vault stale vs the wiki". To write OUT to the wiki use
  `shared-vault-promote`; to answer a question from the wiki use `shared-vault-read`.
tags:
  - ACME
---

# Ingesting the shared vault

One direction only: shared-vault → vault. The mirror image of `shared-vault-promote`, and it inherits
that skill's discipline — decide what's worth carrying, mark every seam, ask before asserting.

## The rule that shapes everything

**The wiki is not copied in.** It stays the source of truth for team-system facts; the vault absorbs
the *payload* and indexes the rest. Copying 80+ team docs into a private vault would create two truths
for the same systems, and the wiki moves several times a week — the vault's copy would be confidently
wrong within a quarter, exactly the way the wiki itself was about the ZI cadence until its 2026-07-09
audit.

Three tiers, no mirror:

| Tier | Artifact | Coverage |
|---|---|---|
| **Index** | `Maps/Shared Vault Index.md` — every wiki doc, one line, grouped by folder, linked | every doc |
| **Hub links** | a `## Team docs` section on the matching `Concepts/` note | subject entry points |
| **Payload** | facts and gotchas into `_Agents/memory/<topic>.md`; substantial lookups into `Reference/` | what an agent must know |

The payload tier is the point. Incidents and ADRs are the highest-value inbound material in the whole
wiki — "the gotcha, the reason a decision went the way it did, the thing that cost hours" is this
vault's own retention test, and a post-mortem is nothing but that.

## Load order and who owns what

| Concern | Authority |
|---|---|
| This repo's rules (secrets, binaries, his wording, `#ACME`, how to write) | `watchtower` skill — **load first, always** |
| Which knowledge base a thing belongs to | `knowledge-router` |
| Tag vocabulary | `Maps/Tag Registry.md` — update in the same commit as any tag change |
| Where the wiki clone is, which identity pushes | `_Agents/memory/git-and-tickets.md` + `machines/` profile |
| Memory file conventions | `_Agents/memory/README.md`, `_Docs/Agent Memory.md` |
| What to carry across and what to leave | This skill |

**Never work from your memory of the wiki's contents.** Pull the clone first. The wiki's own
`CHANGELOG.md` is the fastest read of what actually changed.

## Where each wiki type lands

| shared-vault | Nature | Vault destination |
|---|---|---|
| `incidents/` | post-mortems | `_Agents/memory/<topic>.md` — the gotcha, the tell, the fix. Highest value inbound. |
| `decisions/` | ADRs | memory "why it's this way" + a line on the concept note. Never restate the ADR; carry the *constraint it imposes*. |
| `systems/` | how a system we run works | memory facts + concept-note link. Enough substance and no concept home → `Spaces/Work/Current Work/Reference/<System>.md`. |
| `runbooks/` | operate / recover | memory: pointer + the gotcha only. Do not re-prose a procedure that lives elsewhere. |
| `references/` | lookups | `Spaces/Work/Current Work/Reference/` — the closest shape match in this vault. |
| `guides/` | learn a task | index + concept link only. `Training/` only if he personally worked through it. |
| `policies/` | team rules | index + concept link only. They are the team's rules, not his standing preferences — never fold them into `working-preferences.md`. |
| `GAPS.md` | open questions | **not** `TODO.md` — that file is scoped to gaps in *this vault*. A wiki gap he could fill is a `shared-vault-promote` candidate; surface it as one. |
| `CHANGELOG.md` | the frontier | read as the sync driver. Never copied. |
| `systems/registry.yml` | repo catalog | pointer from the index page. Don't transcribe it; it changes and it's machine-readable where it lives. |
| `meta/` | the wiki's own tooling | **excluded** — irrelevant here. |
| `notebooks/` | per-dev scratch | **excluded, all of it.** Other devs' space isn't his to absorb; his own `notebooks/<you>/` is unused because this vault is where he thinks. |

## Modes

**A — Backfill.** First run, or after a long gap. Sweep every doc, present the mapping table, take
per-item approval, write. Expect this to be the long one.

**B — Incremental.** Steady state. Read the watermark from the ledger, then
`git log <sha>..HEAD --name-status` plus the new `CHANGELOG.md` bullets. Only changed docs are
candidates. A doc whose change was cosmetic is a no-op — say so rather than re-writing the vault entry.

**C — Targeted.** "Pull the Definitive page into my vault." One doc, same tests, no watermark move
(a targeted run doesn't mean everything else was reviewed).

**D — Drift check.** Read-only. Where does a vault claim now contradict the wiki? Report; write
nothing. The wiki wins on team-system facts, memory wins on this-machine facts (`knowledge-router`) —
but a contradiction is a question for him, not an auto-overwrite of something he may have written
deliberately.

Default to B if a watermark exists, A if it doesn't. Say which mode you're running and why.

## The test each candidate fact must pass

All four, or it doesn't come across.

- **Agent-actionable** — an agent behaves differently for knowing it. A gotcha, a threshold, an id, a
  constraint. Not narrative.
- **Not already here** — grep the vault and memory first. Usually the right move is *adding a line to
  an existing memory file*, not creating a note.
- **Durable** — true next quarter. Wiki status sections, open-item lists, and "as of" build numbers
  are not; the mechanism behind them is.
- **Stable in the wiki** — a doc the wiki itself flags as inferred or pending stays flagged here. Never
  launder an inferred wiki claim into a flat vault assertion.

## Watermark and ledger

`_Docs/Shared Vault Ingest.md`. Two jobs:

- **The watermark** — the wiki commit SHA everything through has been considered, with its date. Moved
  only by a completed A or B run, and only over docs actually reviewed.
- **Per-doc disposition** — `absorbed`, `indexed` (index-only, by design), `skipped` (with the reason),
  or `deferred` (with what would change the call). Same memory-aid-not-a-gate principle as
  `_Docs/Shared Vault Promotions.md`: a skip records a judgement at a date, and a later run may reverse it.

**Provenance is mandatory on every absorbed fact** — the wiki path and the SHA it was read at. That's
the only thing that makes drift detectable instead of silent. Format in `reference.md`.

## Tagging

Wiki-derived content carries **`ACME`** (Acme-only by definition) and **`source/shared-vault`** — the
provenance namespace `Maps/Tag Registry.md` already defines, alongside `source/pdf-converted`. It
records where the content came from, which nothing else in the vault captures.

- **Frontmatter** on files that are wiki-derived as a whole: `Maps/Shared Vault Index.md`, any inbound
  `Reference/` note, and the employer-specific memory files that carry wiki-sourced facts.
- **Inline `#source/shared-vault`** on the `## Team docs` section of a `Concepts/` note — the note is
  mostly his own material with one derived section, which is the same shape the `#ACME` inline rule
  already covers.
- `topic/*` as normal, and only where a concept note exists to link. A wiki subject with no concept
  home gets no topic tag until the concept is created — that rule is not this skill's to bend.
- **Register any tag change in `Maps/Tag Registry.md` in the same commit.** Hard rule.

## Asking instead of assuming

Root `AGENTS.md` → **Ask instead of assuming** is the rule; this is what the questions are for here:

- **Which docs to absorb vs index**, as one batched multiple-choice set before any write — not a drip.
  Approval is per item.
- **Every mechanism you're about to state as fact**, phrased to be contradicted in one word: *"my
  understanding: an the newsletter platform `XE` validity code is the address vendor's mapping of a the validation vendor `R` verdict, and
  the 10-soft/1-hard bounce counts are backfilled synthetically — the address never bounced. Correct?"*
- **Where a fact goes** when two memory files could hold it. Guessing splits the truth in two.
- Wiki says one thing, vault says another → surface both verbatim and ask. Never silently pick.
- He doesn't know either → it stays out, and the question goes in the wiki's `GAPS.md` (via
  `shared-vault-promote`). Don't invent, don't quietly drop.

## vault write preview

When this skill writes an index, concept/reference note, or `_Agents/memory` file, follow the
vault-wide preview protocol: show the exact Markdown, paths, links, tags, and index changes in
chat before writing unless the current request explicitly says `full perms`, `skip verification`,
`write it directly`, or a clear equivalent. Those phrases skip only the human preview; they do not permit invented facts, secrets, binaries, or broken boundaries.

## Before you open the PR

- [ ] Wiki clone pulled this session; watermark and ledger read before deciding anything.
- [ ] No wiki prose pasted. Every absorbed fact carries its wiki path + SHA.
- [ ] Index page covers every doc in scope; exclusions stated, not silently dropped.
- [ ] `ACME` + `source/shared-vault` set correctly (frontmatter vs inline); `Maps/Tag Registry.md` current.
- [ ] `topic/*` tags only where a concept note exists and is linked.
- [ ] **No binaries.** The wiki has screenshots under `guides/assets/` and `runbooks/assets/` — those
      become a `> Image removed:` callout plus an `_Docs/Image Descriptions.md` entry, never a commit.
- [ ] Nothing of his rewritten. A wiki fact merged into an existing note adds to it.
- [ ] Wiki status/open-item/build-number content left behind.
- [ ] Ledger updated: watermark moved only over docs actually reviewed, dispositions recorded.
- [ ] Secret-scanned; only intended files staged; branch + PR, never `main`.

## Related skills

- `watchtower` — this repo's rules. First, always.
- `shared-vault-promote` — the outbound twin. Read its boundary section; this skill is its inverse and
  deliberately does not restate it.
- `knowledge-router` — personal vs team, and which side wins a disagreement.
- `shared-vault-read` — the team-managed skill for reading the wiki. Its token pre-flight is wrong for
  the Mac; `_Agents/memory/git-and-tickets.md` has the working access path.
- `vault-memory` — the same extract-and-file discipline applied to local AI-platform history. This
  skill writes into the same memory files, so read its conventions before adding one.
