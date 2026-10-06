---
name: shared-vault
description: >
  Moves knowledge from this vault into the team shared vault as a PR. Use for "add this to the dev
  wiki", "document X for the team", "scan my vault for wiki-worthy stuff", "what should the team
  know", or "fill a gap in GAPS.md". To read the wiki, read its clone directly.
tags:
  - ACME
---

# Contributing to the shared vault

One direction only: vault → shared-vault. This skill decides *what* is worth promoting, strips what
must not travel, and ships it as a PR. It does **not** own the wiki's format.

The other direction has no skill. To use team knowledge, read the shared vault's clone directly. Do
not copy its facts into this vault. When a vault note refers to a team doc, keep a short summary and
a link to that doc ("point, don't copy").

## Load order and who owns what

| Concern | Authority |
|---|---|
| This repo's rules (secrets, wording, `#ACME`, how to write) | `watchtower` skill — **load first, always** |
| Which knowledge base a thing belongs to at all | `watchtower` skill → *Which knowledge base* |
| shared-vault **format, folders, template, changelog, commit mechanics** | The **live shared-vault repo** — `README.md`, `CLAUDE.md`, `_template.md`, the folder `README.md`, `systems/registry.yml`. Re-read them every time; the `shared-vault-read` skill has the per-type recipe. |
| Where the repo is, which identity pushes | `_Agents/memory/git-and-tickets.md` and `environment.md` |
| Deciding *what* to promote, and asking before you do | This skill |

**Never rely on your memory of the wiki's layout.** Conventions drift, folders get added. Pull the
clone, read the governing docs, read one or two existing docs in the target folder, then write.

## The boundary (hard)

vault content is **never pasted** into the shared vault. What travels is the *distilled,
team-relevant mechanism*, rewritten for a team audience. What never travels:

- Any secret value. Same hard rule as the rest of this repo — where a credential lives is fine
  (`password-secrets-management.md` and `guides/secrets.md` already cover that pattern), the value
  never is.
- PII, personal contact details, and anything from `People/` beyond "who owns this system".
- Interview notes, comp and career material, performance opinions about individuals, personal
  frustration or politics, vendor pricing.
- your own planning, status, and daily/weekly logs. The *mechanism he learned* can be
  promoted; the log entry cannot.

Team-relevant but half-baked → `notebooks/<you>/` in the wiki, which has no template or review
bar. Private → stays here. See `watchtower` → *Which knowledge base* for the full boundary.

**The wiki's own source-of-truth rule bites here.** If a fact belongs to exactly one code repo
(setup, config, run instructions, identifiers), it belongs in *that repo's* README or `docs/` — the
wiki links out, never copies. When a candidate turns out to be a single-repo fact, say so and propose
the repo instead of filing it in the wiki anyway.

## Access and shipping

The wiki is a normal clone on this machine — path, identity, and the PR flow are in
`_Agents/memory/git-and-tickets.md`. Two standing rules:

- **Branch → commit → push → `gh pr create`. Never commit to `main`**, not even a one-line changelog
  fix. The team works PR-per-change and the merge notification depends on it.
- **One coherent contribution per PR.** Batch only if the user asks. If `main` moves and
  `CHANGELOG.md` conflicts, resolve by keeping **both** bullets in date order — never drop one.

## Mode A — Scan

Everything in the vault is in scope. the user flags add-or-skip; your job is to surface
candidates worth reading, not to pre-filter aggressively or to dump the whole vault.

1. **Establish the frontier.** Read the ledger `_Docs/Shared Vault Promotions.md` (what's shipped, what
   was declined and why). Pull the wiki clone and read `GAPS.md`, the folder `README.md` indexes, and
   `systems/registry.yml` — that's what's already covered and what the team has explicitly asked for.
2. **Sweep, in this order** — highest signal first, so the top of the candidate list is the best part:
   `_Agents/memory/*.md` (dense, already high-signal, needs the tightest filter) → `Spaces/Work/
   Acme Analytics/` (`Projects/`, `Reference/`, `Meeting Notes/`, `Work Logs/`) → `Concepts/` and
   `Maps/`. Then a **gap-driven pass**: for each open item in `GAPS.md`, grep the vault for material
   that would fill it.
3. **Test each candidate** — all five, or it's not a candidate. Details and worked judgement calls in
   - **Team-useful:** another dev needs it to build, operate, or decide — not just the user.
   - **Durable:** true next quarter. Status, numbers, and this week's state are not.
   - **Uncovered:** the wiki doesn't already say it, and it *spans* repos or has no repo home.
   - **Survives sanitization** with substance left.
   - **Ownable:** there's a real owner. Someone else's system → propose them and ask first.
4. **Present the candidate table** (format in `reference.md`), ranked, capped at ~10–15 on the first
   pass. State plainly what you swept, what you left out, and why — never let a cap read as "that's
   everything." Flag per row: needs-owner, single-repo-fact, sanitization-heavy, inferred-not-verified.
5. **Re-raise the interesting declines.** A "declined" ledger row is not permanent. List separately
   any previously-declined material whose conditions have changed — the team hit the problem, a new
   system now depends on it, a `GAPS.md` entry appeared, someone asked in Chat — with the specific
   reason it's worth reconsidering now. Don't re-raise a decline with nothing new to say.
6. **Get flags, then run the understanding check** (below) on the approved rows *before* drafting.
7. **Draft, ship, log.** Live conventions, correct folder, folder index + `CHANGELOG.md` in the same
   change, PR. Then update the ledger.

## Mode B — On demand

"I just worked on X — compile notes and add it to the dev wiki."

1. **Gather evidence; don't write from recall.** The vault note, the merged PRs, the ticket, the code,
   this session's own transcript. Every mechanism you state must trace to one of those or to
   your own words — see `working-preferences.md` on verify-never-fabricate.
2. **Run the understanding check before drafting** (below). This is where the skill earns its keep:
   restating the mechanism wrongly in a team-visible wiki is worse than not documenting it.
3. **Classify by document type** — rule vs task vs system vs break-glass vs lookup vs decision vs
   post-mortem. Confirm against the live tables; ask when it's genuinely between two folders.
4. **Check the single-repo litmus** before filing. Single-repo fact → propose the repo's own docs.
5. **Draft from `_template.md`**, matching the tone of one or two existing docs in that folder.
   `owner` is required and a doc with no owner rots — if it isn't the user, ask who.
6. **Ship and log**, as in Mode A step 7.

## Asking instead of assuming

Both modes, non-negotiable. Low confidence is fine; **presenting low confidence as fact is not.**

- **Batch the questions into one short multiple-choice set, before the write** — not a drip of
  one-liners, and not a post-hoc "let me know if that's wrong."
- **Approval is per item.** "Add this to the PR?" for each candidate. Silence is not approval.
- **State your understanding and ask if it's right.** Spell the mechanism out concretely enough to be
  falsifiable — *"my understanding: that mapping's 'Type ID' column is really a per-event registration-type
  id, so it changes every event. Correct?"* — not *"is my understanding of the mapping correct?"*, which
  can't be answered.
- **Mark the seams.** Every claim is either verified (name the source) or inferred (ask). Never
  bridge a gap with a plausible-sounding mechanism.
- **If he doesn't know either**, don't invent and don't quietly drop it: leave it out of the doc and
  add the question to the wiki's `GAPS.md`, or say what would settle it.
- Use the same pass to confirm the **depth wanted** (orientation page vs full reference) and whether
  anything's **missing**.

## The ledger

`_Docs/Shared Vault Promotions.md` — one row per decision, shipped or declined. Read it at the start of
every scan; update it in the same PR as the contribution.

It is a **memory aid, not a gate**. A decline records a judgement made under the conditions of that
date. When those conditions change, raise it again (Mode A step 5). Never treat a past decline as a
standing "no", and never re-file something already shipped without checking whether the existing page
should just be *updated* instead.

## Before you open the PR

- [ ] Live shared-vault governing docs re-read this session; folder, filename, and frontmatter match them.
- [ ] `title` / `description` / `owner` / `updated` present; `owner` is a real person or team.
- [ ] Sanitization pass done: no secrets, no PII, no comp/interview/performance material, no
      vault text pasted verbatim.
- [ ] No single-repo facts duplicated in; `systems/` pages carry the source-of-truth banner.
- [ ] Folder `README.md` entry + `CHANGELOG.md` bullet (top, dated) in the same change.
- [ ] New `systems/` entry also in `systems/registry.yml`; a filled gap struck from `GAPS.md`.
- [ ] Every assertion traces to evidence or to an answer the user gave. Nothing inferred silently.
- [ ] ADRs and incidents not rewritten — supersede or link forward instead.
- [ ] Branch + PR, not `main`. Ledger updated. Both repos' diffs contain only intended files.

## Related skills

- `watchtower` — this repo's rules. First, always.
- `shared-vault-read` — the team-managed skill: reading the wiki, and the per-type authoring recipe.
  Its token pre-flight is wrong for this machine; `_Agents/memory/git-and-tickets.md` has the working
  access path.
- `weekly-work-log` — the same verify-and-ask discipline applied to the personal log.
