---
name: skills-sync
description: >
  Publishes selected Watchtower skills out to an external skills destination — a team plugin
  marketplace repo, a shared `.claude/skills` repo, a client's agent repo — and keeps the two copies
  from drifting. Reformats each skill to whatever shape the destination actually uses, strips what
  must not travel, and ships a PR. Use when the user says "share this skill with the team", "push my
  skills to the org repo", "sync my skills to <repo>", "which of my skills should the team have",
  "is my copy of <skill> behind the shared one", or "publish <skill> to <destination>". Nothing is
  ever exported without them naming the skills explicitly, one by one.
user-invocable: true
argument-hint: "[drift|out|in] [destination]"
---

# Skills sync

The Watchtower is where skills are authored. Other places — a team plugin marketplace, a shared
`.claude/skills` repo, a client repo — are **destinations**: copies that other people load. This skill
moves selected skills out to a destination, in that destination's own format, and keeps the copies
honest afterwards.

The `shared-vault-*` family's shape applied to skills. **Nothing is exported unless the user names them** —
not "the obvious ones", not the rest of a bundle, not a skill that an approved skill references. See
[The confirmation gate](#the-confirmation-gate).

**This skill never commits the vault.** Whatever a run writes on this side — the ledger, a skill edited
to be exportable — `vault-sync` ships. The destination side goes as its own PR. Never push to `main` on
either.

| Direction | What it does | Writes |
|---|---|---|
| **drift** | Compares each exported skill against its destination copy | Nothing |
| **out** | Vault → destination, per-skill confirmed | A PR to the destination + a ledger row |
| **in** | Destination → vault, when the destination's copy moved ahead | A vault edit, then hand to `vault-sync` |

## Why a destination is not a mirror

Different audience, different format, different governance. **The vault copy is the source and wins**
(`AGENTS.md` → *Context loading*); the destination copy is a build artifact. A skill written for one
person is not a skill the team can run — anything reading `_Agents/memory/`, a `machines/` profile, or
a path only this machine has must be rewritten to ask or to degrade. A skill that can't degrade isn't
exportable yet; say so rather than shipping something that fails on first use for everyone else.

## The confirmation gate

A skill is executable instruction that other people's agents run unattended, often against real data
or infrastructure. Shipping one they didn't intend to ship is worse than filing a wiki page nobody reads.

1. **Present the full candidate table first** (Step 3). Don't draft, format, or branch before it is
   answered.
2. **They name the skills.** By name — if they say "all", read the list back and get a confirmation on
   the read-back. **Silence is not approval**, and an empty answer ends the run with nothing shipped.
3. **Approving a skill approves that skill only.** Its `reference.md`, `scripts/`, and assets travel
   with it because they are the same skill. A *different* skill it references does not — flag the
   dangling reference and let them decide.
4. **Show the adapted, sanitized text before committing** — the frontmatter translation, every line
   removed, every line rewritten. They approve what ships, not the idea of shipping it. If that pass
   changes the picture for a skill (unsanitizable, a secret, an unexportable dependency), re-ask for
   that skill rather than shipping a diminished version.

Not waived by `full perms`, `skip the preview`, or `just do it` — those bypass the vault's own write
gate, not publishing to somewhere other people load code from. Root `AGENTS.md` hard rule 5 is the
authority.

## Destinations

The registry — repo, layout adapter, owner, review rule — is the table at the top of
[`../../../_Docs/Skill Exports.md`](../../../_Docs/Skill%20Exports.md). Clone paths are per-machine:
read them from `_Agents/memory/machines/<target>.md`, routed by `environment.md`. Which `gh` identity
you get is per-shell — `_Agents/memory/environment.md`.

A destination not yet in the registry gets added as part of the run — repo, layout, reviewer, and what
may not travel there.

## 1. Read the destination's own rules — always first

**Never publish in a format you remember.** Pull the clone and read, in this order: `README.md`,
`CONTRIBUTING.md`, `CLAUDE.md`/`AGENTS.md`, any marketplace or plugin manifest, and **two existing
skills in the folder you're targeting**. The existing skills are the real spec — they show the
frontmatter fields actually in use, the directory names (`references/` vs `reference.md`, `scripts/`,
`assets/`), and the house tone.

Note four things: **layout** (where the folder goes, what manifest changes with it), **frontmatter**
(which fields it keeps), **index surfaces** (README table, plugin map, manifest description — landing a
skill without them is a half-contribution), and **prohibitions** (its rules on secrets, vendored
skills, and review gates bind in addition to this vault's, never instead). Adapter recipes:
[`reference.md`](reference.md).

## 2. Drift check

Cheap, read-only, and the reason this is a *sync* rather than an export. Two copies of an executable
instruction that silently disagree is worse than one copy in the wrong place.

For every skill with a ledger row, compare the vault copy against the destination copy and classify:

| State | Meaning | Action |
|---|---|---|
| **In step** | Both match the ledger's exported revision | Nothing |
| **Vault ahead** | Vault edited since export | An `out` candidate — pre-flag it in Step 3 |
| **Destination ahead** | Someone edited the destination copy | **`in` candidate.** Never overwrite it — read Step 5 |
| **Forked** | Both moved | Stop and show both diffs. His call, per skill. Never auto-merge executable instructions |

Also report **shadowing**: a skill offered under both the unprefixed name and a `plugin:skill` one.
Which copy answers is already settled — `AGENTS.md` → *Context loading* makes it the vault's. So report
shadowing as **drift to reconcile**, never as a precedence question, and never propose deleting the
local copy to make the duplicate go away. The published copy is the one allowed to be behind.

## 3. Candidate table, then the gate

Rank by what the destination would gain. Cap the first pass at ~10–15 and say what you swept and what
you left out — never let a cap read as "that's everything." Each row needs: skill · why it's worth the destination having · drift state from Step 2 · a
**portability verdict** · what sanitization would remove · dangling skill references. Row format and
a worked table: [`reference.md`](reference.md).

**Portability verdict** — the honest one, not the optimistic one:

- **Portable** — works for anyone who loads it.
- **Needs rewriting** — depends on this machine or `_Agents/memory/`, but can be made to ask the user
  or degrade to a lesser mode. Name the rewrite in the row; it happens in Step 4.
- **Not exportable** — the skill *is* the personal thing (the vault family, the personal-\* family,
  anything documenting their own credential store). Say so and don't propose it again next run.

Then **stop and run the gate.** Nothing below this line happens without named approval.

## 4. Adapt and sanitize

Per approved skill:

1. **Translate the frontmatter** to the destination's field set. `name` and `description` must survive
   intact — the description is the trigger, and a trimmed one never fires.
2. **Rewrite the machine-bound parts.** A `_Agents/memory/` pointer becomes either an inline fact
   (durable, non-sensitive) or an instruction to ask the user. A hardcoded path becomes a question. An
   "on this machine" becomes a capability check with a stated fallback.
3. **Sanitize** — checklist in [`reference.md`](reference.md). The four that matter: no secret values
   (locations are fine), no personal machine paths, no PII beyond "who owns this system", no account
   identifiers the destination doesn't need.
4. **Rewrite cross-references** to skills that aren't at the destination — either it travels too, with
   its own approval, or the pointer is replaced with the fact it was reaching for.
5. **Re-read it as a stranger.** Someone with no Watchtower and none of their access loads this cold:
   does it work, or fail on step one? If it fails, back to the gate.

## 5. Ship

**Out:** branch → commit → push → PR on the destination repo. One coherent contribution per PR;
coupled skills that reference each other go together, because a cross-reference that lands in a later
PR dangles in between. Update the destination's index surfaces in the same change. Write the PR body
for someone with no Watchtower context — what the skill does, why the destination wants it, what was
changed to make it portable, and what it still can't do. `_Agents/memory/working-preferences.md`
§ *Writing about code* governs that body.

**In:** the destination copy moved ahead. Read the change, decide whether it belongs in the vault copy
too, and if so apply it **here** and let `vault-sync` ship it — the vault is the source, so a
destination-side improvement has to come home or it will be clobbered by the next `out`. If it
shouldn't come home, say why in the ledger, because that row is now a permanent fork and the drift
check will keep reporting it.

**Never push to `main`** on either side.

## 6. Log it

`_Docs/Skill Exports.md`, one row per skill per destination, updated in the same change: date, skill,
destination, PR, **the vault git SHA it was exported from**, and what sanitization removed. The SHA is
what makes Step 2 computable — without it drift is a guess.

Declines get a row too, with the condition that would reverse them. Same rule as
`_Docs/Shared Vault Promotions.md`: a decline is a judgement at a date, not a standing no.

## 7. Report

```
Destination  <repo> · adapter <name> · read <n> governing files
Drift        <n> in step · <n> vault ahead · <n> destination ahead · <n> forked · <n> shadowed
Proposed     <n>   Approved <n>   Shipped <n> (PR #<n>)   Declined <n>
Inbound      <n> changes adopted into the vault (uncommitted — vault-sync ships them)
Open         <questions>
Skipped      <what you deliberately didn't sweep, and why>
```

## Before you open the destination PR

- [ ] Destination's governing files re-read **this session**.
- [ ] **Every shipped skill was named by the user in this run**, and the adapted text was approved —
      not just the intent to ship.
- [ ] No secret values, no personal machine paths, no PII, no `_Agents/memory/` or `machines/`
      references left in the exported copy.
- [ ] Cross-references resolve at the destination, or were replaced.
- [ ] Destination index surfaces updated in the same change; ledger row written with the source SHA.
- [ ] Vault side left uncommitted for `vault-sync`. Branch + PR on both sides.

## Related

- `shared-vault-sync` · `shared-vault-promote` — the same two-base pattern for documentation. Read
  `shared-vault-promote` for the promotion judgement calls; this skill deliberately doesn't restate them.
- `knowledge-router` — which base owns a thing at all, and the PII boundary.
- `vault-sync` — ships everything this skill wrote on the vault side.
- `vault-doctor` — run after an `in` adoption; it checks the skill index and the skill's
  frontmatter, both of which an edited skill can break.
- `_Agents/CONVENTIONS.md` — the authoring spec every exported skill still has to satisfy.
