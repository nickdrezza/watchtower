# AGENTS.md — the vault

Instructions for **any** AI agent working in this repository (Claude Code, Codex, Cursor, Gemini
CLI, Copilot, Antigravity, Windsurf). This file is the [agents.md](https://agents.md) standard;
`CLAUDE.md`, `GEMINI.md`, and `.github/copilot-instructions.md` are stubs that point here. Behave
identically regardless of which harness loaded you.

## What this repo is

the vault: your **private, text-first Obsidian vault** *and* the single home for the
agent knowledge needed to run his work. Two halves, one repo:

| Half | Lives in | Audience |
|---|---|---|
| **The vault** — notes, projects, meetings, work logs, career, personal | `Spaces/`, `Concepts/`, `Maps/`, `Dashboards/`, `Inbox/`, `Daily Notes/`, `_Templates/`, `_Docs/` | Obsidian (a human) + agents |
| **The agent layer** — skills, operational memory, conventions, platform docs | `_Agents/` | agents, and visible in Obsidian |

## First move, every session

**Load `_Agents/skills/watchtower/SKILL.md` before you read or write anything here.** It is the
primary, always-applicable context for this repo — hard rules, layout, filing workflow, the memory
index, and the verification gate. Everything below is a summary of it; the skill (plus its
`reference.md`) is the detail. If this file and that skill ever disagree, they should be fixed — treat
the vault's own governance (`AGENTS.md`, `_Docs/`) as authoritative and say so.

Then, if your harness didn't auto-load skills, read `_Agents/skills/` yourself — see
**Skills** below.

**Before running anything hands-on, read `_Agents/memory/environment.md` and
`_Agents/memory/credentials.md`** — see **Memory** below.

## How agents work here

**One brain, many disposable agents.** This vault is the memory; the agents are not. Full model:
[`_Agents/docs/operating-model.md`](_Agents/docs/operating-model.md).

- **No hierarchy.** Every agent reads this same vault. No manager thread, no per-agent private memory.
  Subagents are for parallel *work* — never for holding context.
- **Fetch before asking.** Search this vault, then prior sessions across chats, then the connectors
  ([`_Agents/memory/connectors.md`](_Agents/memory/connectors.md)). Making him re-explain something
  already answerable from history is the most common waste here.
- **Decide what's yours to decide.** Reversible, conventional, cheap to undo, or answerable from the
  repo → decide. Irreversible, expensive, or a matter of his taste → ask. See **Ask instead of
  assuming** below.
- **Chats are disposable** — but only because memory gets written. See
  [`_Agents/memory/README.md`](_Agents/memory/README.md) → *When to write memory*.
- **Load context aggressively.** Reading the memory file and the note first is cheaper than one wrong
  assumption. Affordable only because the structure below makes retrieval precise.
- **Connectors are peers, not memory.** Durable facts live here; live state is queried, never cached.
- **Verify before reporting.** [`_Agents/docs/verification.md`](_Agents/docs/verification.md).

## Hard rules (never violate)

1. **No secrets, ever.** No API keys, passwords, private keys, `.env` contents, OAuth secrets,
   tokens — not in a note, not in a code block, not in a pasted log. If a dump contains one, strip
   it, tell the user, and point them at where it belongs. Documenting *where a credential lives*
   (a path, an env var name, a your secret manager item name) is fine and encouraged; pasting the value is
   never fine. The repo's extension-based check misses inline secrets — you are the backstop.
2. **No binaries.** Never commit images, PDFs, private keys, `.env` files, plugin bundles, JS, or
   CSS. Images live outside the vault; in-note use a `> Image removed:` callout and catalogue in
   `_Docs/Image Descriptions.md`. PDFs get text-extracted to `.md`.
3. **Never delete notes or rewrite the user's wording.** Preserve rough notes; add structure
   *around* them. Don't make notes sound generic, corporate, or AI-written. (Explicit
   consolidation is fine — carry the original wording into the target note.)
4. **Respect space boundaries.** Never mix employer-specific material into personal or future-work
   spaces.
5. **Never push straight to `main`.** Branch, commit, open a PR. See **Git** below.
6. **Never write a low-confidence inference as fact. Ask.** An informed guess is welcome as a
   *question*; it is not welcome in a note, a memory file, a work log, a ticket, or a team wiki page.
   See **Ask instead of assuming** below.
7. **No filler, no editorializing.** Every sentence you write into this repo — or into a task report
   in chat — must carry a fact a future reader needs. This is not a style preference: padding
   degrades the vault directly, because retrieval gets worse as the signal-to-noise ratio falls, and
   a vault of bloated notes is slower and *worse* to work in than a smaller one. See **How to write
   here** for the banned patterns and the test.

## Ask instead of assuming

Being uncertain is fine. Presenting uncertainty as fact is the failure this repo cares most about —
a wrong claim written down gets read as true for years, and it has cost real hours (the shared-vault's
misreading of the the networking app "Type ID" column is the standing example).

- **Verify first, ask second, assume never.** If the code, the PR, the ticket, or the email can settle
  it, go read them. Ask only about what evidence can't answer.
- **Batch the questions into one short multiple-choice set, and ask it *before* the write** — not a
  drip of one-liners, and not a post-hoc "let me know if any of that's wrong."
- **State your understanding and ask if it's right.** Concrete enough to be contradicted in one word:
  *"my understanding: the writeback keys on the legacy `md5(domain)`, not the resolved `company_id` —
  correct?"* Not *"is my understanding of the writeback correct?"*, which can't be answered.
- **Ask for approval per listed item, not by implication.** Silence is not approval, and one approval
  does not cover work that was not shown. A single confirmation after one complete preview approves
  exactly the files and changes shown in that preview.
- **Mark the seams in what you write.** Every claim is either verified (the source is nameable) or
  inferred (it was asked). Never bridge a gap with a plausible-sounding mechanism.
- **If he doesn't know either**, don't invent and don't silently drop it — leave it out and record the
  open question (an `## Open questions` section, or the shared-vault's `GAPS.md`).
- Use the same pass to confirm the **depth wanted** and whether anything's **missing**.

### …and when not to ask

This rule governs **claims that go into an artifact**. It is not an instruction to seek approval for
ordinary judgement, and an agent that asks about everything is as unusable as one that assumes
everything.

- **Decide it yourself** when it's reversible, conventional, cheap to undo, or answerable by reading
  the repo. Make the call, state the assumption in one line, and keep going.
- **Ask** when it's irreversible or expensive, when being wrong can't be recovered from, when it's a
  matter of his taste rather than correctness, or when it's business-side and genuinely his to do
  (see `_Agents/memory/working-preferences.md` → *Scope discipline*).
- **Never spend his attention on a lookup.** If evidence can settle it, go get the evidence — that's
  the first bullet above, and it is the most common way this rule gets misapplied.

## Verification preview before any vault write

This gate applies to every vault entry: personal notes, work logs, projects, reference notes,
meeting notes, Inbox items, indexes and landing pages, and `_Agents/memory/*.md`.

**One standing carve-out:** the memory **fast path** — a single durable fact appended to an existing
`_Agents/memory/` file, locations-only, rewriting nothing and contradicting nothing — is
pre-authorized and needs no preview. It exists so a fact learned mid-session doesn't wait for a sync
that may never come. Conditions and what stays behind the gate:
[`_Agents/memory/README.md`](_Agents/memory/README.md) → *When to write memory*.

- By default, prepare the content in conversation without writing files or indexes. Show a
  `vault preview` here before saving: every destination path, the complete proposed Markdown
  for each new or short file, and the exact changed Markdown or diff for each existing file. Include
  frontmatter, body text, links, tags, and landing-page/index changes. The user should not need to
  inspect a PR or open the local vault to understand what will be saved.
- Wait for approval after the preview. A plain confirmation approves only the complete set shown in
  that preview. Do not partially write an unapproved set.
- An explicit, positive bypass instruction in the current request skips this human preview and
  approval. Recognize case-insensitive phrases such as `full permissions`, `auto merge`, `automerge`,
  `auto-merge`, `just merge`, `skip the preview`, `skip verification`, `write it directly`, `save it
  without asking`, or `merge it now`. Clear equivalents are valid; vague requests such as “organize
  this” are not. A negated phrase such as “do not auto merge” never bypasses the gate.
- A bypass applies only to the preview/approval gate. It never permits secrets, binaries, broken space
  boundaries, a direct push to `main`, or writing an uncertain claim as fact. Preserve unresolved
  material as an open question or staging entry instead of guessing.

The preview is a chat handoff, not a request to make the user review the PR. The PR remains the
delivery mechanism; this is the content verification step before the write.

Standing instruction, in `_Agents/memory/working-preferences.md`; over-reaching here has gotten work
rejected. It applies to every deliverable, not just the weekly log.

## How to write here

The vault's value is being scannable in two years. Verbosity is the failure mode.

- **Say it once, plainly.** No preamble, no restating the question, no summarizing what you just wrote.
- **Nothing adjacent.** No recommendations or "you might also consider" unless the note's subject *is*
  that decision. Off-topic suggestions are the main source of clutter.
- **Don't overexplain — but don't presume.** One line still beats a paragraph. "Competent reader"
  means someone fluent in the craft who has *never seen this code*: they know what a lint rule or a
  migration is; they do not know what your `roster-base.ts` or your "persona bucket" is. Cut words,
  never the reader's footing.
- **Keep every nuance that changes an outcome** — the gotcha, the exact id, why a decision went that
  way, the thing that cost hours. Cut words, never facts.
- **Prefer structure to prose.** A table or labelled list carries more per line and ages better.
- Aim for elegance: the shortest form a future agent can act on with no follow-up questions.

### Plain first, then the names

Compression into jargon reads as expertise and lands as noise. A reader who can't tell what broke
can't check whether you fixed it.

- **Say what the thing is and what goes wrong in ordinary words, before naming a file, symbol, or
  ticket.** "The score that ranks who to invite was defined in three separate files, so retuning it
  made two screens disagree about the same person" — *then* name the constant.
- **Spell out an acronym or internal term the first time it appears.** One clause is enough.
- **Lead each item with the consequence; the mechanism is the second sentence.**
- **Never let a file path or a symbol name do the explaining.** It identifies. It does not inform.

This is not licence to pad (hard rule 7). Orientation is the fact the reader needs *most*; filler is
the sentence carrying none. Same word budget, spent on meaning rather than shorthand.

### Objectivity

Write what is, not how you feel about it. A note is a record, not a pitch.

- **No evaluative adjectives about the work.** Not "successfully implemented a robust solution" — say
  what changed. Strike `comprehensive`, `powerful`, `seamless`, `robust`, `significantly`,
  `state-of-the-art`, `best-in-class`.
- **No hedging frames.** "It's worth noting that", "it's important to understand", "keep in mind
  that" — delete the frame, keep the fact.
- **Attribute or mark as inferred.** A claim from a source names the source; a claim you reasoned to
  says so. Never a confident sentence over an unverified gap (hard rule 6).
- **No enthusiasm.** Exclamation marks and "great question" don't survive into a note.

### Banned patterns — delete on sight

Applies to notes, memory files, PR bodies, commit messages, and task reports in chat alike.

| Pattern | Instead |
|---|---|
| A closing paragraph summarizing what you just wrote | Stop when the content ends |
| "In conclusion", "Overall", "To summarize" | Nothing — he just read it |
| Restating the request before answering it | Answer it |
| A "Next steps" section nobody asked for | Nothing, unless the note's subject *is* the plan |
| Three bullets stating obvious things | One line, or nothing |
| A section header over one sentence | Merge it upward |
| "This is a critical/key/essential part of…" | Say why it matters, once, concretely |
| Glossing what a well-named function obviously does | Nothing — but do say what an unfamiliar *concept* is (see **Plain first, then the names**) |
| Praising the user's idea before doing it | Do it |

### The test, before you save or send

For each paragraph: **would a competent reader six weeks from now be worse off without this?** If no,
delete it.

Then once over the whole thing: **could a teammate who has never opened this code say what broke and
why it matters?** If not, you compressed into jargon — fix that before trimming another word.

Apply it to the task report in chat too. **A wall of text after a small change is the most common form
of this failure** — it trains him to stop reading, which costs more than the words did. Report what
changed, what you verified, and what you deliberately left out. Nothing else.

`vault-prune` enforces this retroactively; that is a backstop, not a licence to write loosely now.

## Tagging

**`Maps/Tag Registry.md` is the authority — every allowed tag, with when to apply it. Read it before
adding a tag, and update it in the same commit as any tag change.** A tag not in the registry should not
exist.

**Tags carry only what folders and properties cannot: graph scope, employer scope, and what a note is
*about*.** `personal` and `work` are deliberate graph-filter flags; do not add tags that merely
restate `type:`, `domain:`, or `workspace:`.

| Namespace | Meaning | Values |
|---|---|---|
| `personal` | Personal graph scope | one flag; mixed notes may also carry `work` |
| `work` | Professional graph scope | one flag; mixed notes may also carry `personal` |
| `ACME` | Employer scope — see below | one flag |
| `topic/*` | What the note is about | one per `Concepts/` note — see [[Tag Registry]] |

- **Never tag what a property already says just to duplicate it.** `type: weekly-log` needs no
  `work/log`; scope tags are the intentional exception because they enable cross-folder Graph view
  filters. The Dashboards filter on `type ==`, so properties still drive views.
- **A `topic/*` tag follows a link.** Tag `topic/transform` when the note links `dbt` — the tag and the
  `related:` entry go in together. Don't invent a topic with no concept note behind it; add the
  concept note first, list it in [[Concept Index]], and register the tag in [[Tag Registry]].
- **Index notes (`type: index`) get no `topic/*` tags.** They link to everything, so topics on them are
  noise.
- **Exceptions, left alone:** `source/pdf-converted` and `assets/images-converted` record provenance;
  `excalidraw` is required by the plugin — never strip it.
- Graph view groups structural roles by path (`path:Maps/`, `path:"Work Logs"`), not by tag.

### `#ACME`

Anything only meaningful **while you is at Acme Analytics** gets `ACME` in its frontmatter
`tags:`, so it can be archived in one query if he changes jobs and the rest of the vault survives.

- **Tag:** employer projects, tickets, systems, people, meeting notes, work logs, client/event material,
  and the employer-specific memory files.
- **Don't tag:** this machine's setup, git/agent conventions, personal notes, career and future-work
  material — anything reusable at a future employer.
- Mostly-portable file with one employer-specific section → inline `#ACME` on that section instead.
- Set it when you create or substantially edit a file. Backfilling is expensive.

## People

`Spaces/Work/Current Work/People/` — one note per person you actually works with, current
and former, Acme and external. Index: `Maps/People Index.md`.

- **`type: person`**, plus `person_org`, `person_group`, `role`, `email`, `github` where known.
  `status: active` for current, `former` for people who have left.
- **Link people from a note's `people:` property** — `people:\n  - "Raphael Roxas"`. Add it to work
  logs, meeting notes, and project notes. Inline `[[links]]` in prose are fine too where they read
  naturally.
- **Never a tag.** People are entities with attributes; see the reasoning in `Maps/Tag Registry.md`.
- **Full names as note titles**, so first-name ambiguity is explicit. Settled: `Taylor` = Taylor Possley,
  `MM` = Malena McClory, `MMal` = Matthew Malinowski. **Still open — ask, never guess: `Molly`, `Scott`,
  `Daniel`.** The full collision table is in `Maps/People Index.md`.
- **External teams get an org note** in `Spaces/Work/Current Work/Partners/`, indexed by
  `Maps/Partner Index.md`. A person's `person_org` links to it. Where a partner is also a subject-matter
  hub the note lives in `Concepts/` instead — the vendor platform is the one case, because two notes with the same
  basename would break `[[link]]` resolution.
- **An employer email domain does NOT prove employment.** Contractors and vendor staff often hold one.
  Read `person_org`; never infer an employer from a mail domain.
- **`Maps/People Roster.md`** holds all 116 addresses from the 28 Google Groups. Someone with no note
  goes there, not into a near-empty note — 90 stub notes would wreck the graph. Absence from every group
  is evidence of departure, not proof.
- **Work identity only.** Name, work email, role, org, GitHub handle, what they own. **No personal phone
  numbers, home addresses, or personal email addresses** — even though this repo is private.
- Titles drift. The roles came from the ACME Org Chart and mail signatures; verify before quoting one back
  to someone.

## Space boundaries

- current work → `Spaces/Work/Current Work`
- Future work/career → `Spaces/Work/Future Work`
- Personal → `Spaces/Personal`
- Cross-domain reusable → `Spaces/Shared`
- Mixed or uncertain raw dumps → `Inbox/Processed`

`Concepts/`, `Maps/`, `Dashboards/`, `_Templates/`, `_Docs/`, `_Agents/` are infrastructure, not a
work area.

## Memory

**`_Agents/memory/`** holds the operational knowledge the skills assume: the machine, where every
credential lives, how to reach each platform, how the the warehouse project is shaped, what's in flight, and how
you wants agents to work. This is the part that makes every harness behave the same — connecting
to a system is never left to whatever a particular tool happens to have configured.

Index: `_Agents/memory/README.md`. **Read `environment.md` and `credentials.md` before any hands-on
task** — they're short, and nearly every failure mode here is in one of them: wrong shell (the Bash tool
is Git Bash on Windows, *not* WSL), wrong AWS profile, expired SSO session, read-only SQL MCP, symlinks
across the WSL boundary, a Sheet not shared with the service account.

**Work happens on four targets and they share almost no paths** — the Mac, the Windows laptop (real work
inside WSL), the EC2 automation box, and the phone (no filesystem at all). `environment.md` holds what's
true everywhere and routes you to one profile in `_Agents/memory/machines/`. Read that profile before
running anything; a command written for the other laptop is the most common failure here. Never
hard-code one machine's path into a skill — put the fact in its profile and point at it.

Then by topic: `warehouse.md` · `transform.md` · `cloud-and-servers.md` · `workspace.md` · `crm.md` ·
`events-platform.md` · `newsletter.md` · `messaging.md` · `git-and-tickets.md` · `warehouse-project.md` · `vendor-platform.md` ·
`internal-apps.md` · `people.md` · `working-preferences.md` · `projects.md`.

Two rules for writing memory:

- **Locations, never values.** Record the path, env-var name, your secret manager item, the warehouse user/role. Never
  the key material, password, or token.
- **Point-in-time.** Environment facts are stable; code and data facts drift — verify before asserting,
  and date anything that will age.

A skill that hard-codes an account id, a path, or a cron expression is doing memory's job. Put the fact
in `_Agents/memory/` and have the skill point at it.

## When organizing a raw dump

Follow `_Docs/AI Note Intake Workflow.md`. In short:

1. Read the dump; identify date range, projects, meetings, tasks, links, people, open questions.
2. Decide the correct space **before** editing.
3. File durable Acme work under `Work Logs/2. Systems Dev Weekly Notes/…`, `Projects/…`,
   `Meeting Notes/…`, `Reference/…`, `Training/…`, or `Interviews/…`.
4. Add YAML properties matching the destination space (templates in **Preferred properties**),
   including `ACME` in `tags:` where it applies. Tags come from [[Tag Registry]] — don't coin a new one
   mid-intake; if the note needs a tag that isn't there, register it properly or leave it off.
5. Add `[[wiki-links]]` to existing Concepts and project notes.
6. Keep the user's wording. Apply **How to write here** to anything you author.
7. Genuinely uncertain material → `Inbox/Processed/` or an `## Open questions` section.
8. Verify: no binaries, no secrets, no needless broken links, no original content lost.

## Skills

Skills live in **`_Agents/skills/<name>/SKILL.md`** — the universal project-level location that
Codex, Cursor, Gemini CLI, Copilot, and Antigravity discover natively with no setup.

**Claude Code reads `.claude/skills/` instead.** It will not auto-discover `_Agents/skills/`. Two
ways to fix that, both fine:

```bash
_Agents/scripts/install-skills.sh --here      # mirror into ./.claude/skills (this repo only)
_Agents/scripts/install-skills.sh             # or install globally to ~/.agents/skills + ~/.claude/skills
```

**If neither has been run, just read the files.** `SKILL.md` is plain Markdown; open
`_Agents/skills/<name>/SKILL.md` directly. Never claim a skill is unavailable because your harness
didn't auto-load it.

| Skill | Use it for |
|---|---|
| `watchtower` | **The primary context. Load it first, every session.** Layout, hard rules, how to write here, the employer-scope tag, the memory index. |
| `bootstrap` | Sets up a new user or machine, seeds the memory maps, and teaches the operating model. |
| `weekly-work-log` | The weekly manager-facing work log, gathered from real evidence and kept short. |
| `vault-memory` | Refreshes `_Agents/memory/` from prior sessions and your connectors. |
| `vault-sync` | Pull → refresh → commit → PR → merge → concise summary. The single entry point for "sync my vault". |
| `vault-doctor` | Mechanical integrity checks — links, tags, frontmatter, skill-index drift, stale mirror. Read-only, script-backed. |
| `vault-prune` | Quality pass — slop, near-duplicates, bloat, stale claims, orphans, gaps. Per-item approval; never deletes unasked. |
| `vault-edit` | Safe create / move / rename / merge / split / archive / delete, and what must move with the file. |
| `knowledge-router` | Decides which knowledge base owns a task — this vault or the team's shared one. |
| `shared-vault-sync` | Both directions with the team vault in one command, drift check first. |
| `shared-vault-promote` | Outbound: what the team should have, rewritten for a team audience and stripped of anything private. |
| `shared-vault-ingest` | Inbound: indexes the team vault and absorbs its gotchas and constraints into memory. Never copies it. |
| `secrets` | Get, store, rotate, and inject credentials. **Never surfaces a value.** |
| `playwright-testing` | Real-browser tests for user-visible behavior — uploads, downloads, forms, navigation, responsive layout. |
| `personal-vault` | The front door for personal material; routes to the right section. |
| `personal-memory` | Past events, milestones, and life-history notes. |
| `personal-reflection` | Opinions, values, identity questions, and rambles. |
| `personal-entities` | People, pet, and location notes, and the links to them. |
| `personal-triage` | Classifies personal material staged in Uncategorized. |
| `diary` | Lightly cleaned daily entries that preserve your voice. |

Authoring a new skill: `_Agents/scripts/new-skill.sh <name>`, then follow
`_Agents/CONVENTIONS.md`. Per-tool paths: `_Agents/docs/platforms.md`. Portability model:
`_Agents/docs/portability.md`.

## Git

- Remote `git@github.com:<you>/<your-vault>.git` (**private** — it holds PII, interview
  notes, comp material, and employer internals; keep it private). Default branch `main`.
- **Branch + PR, always.** `content/<slug>` for note changes, `feat/<slug>` for agent-layer
  changes. Self-merging your own PR is expected on this solo repo — going through a PR is not.
- **`git fetch origin --prune` first.** Local refs go stale between sessions.
- **Stage only intended files.** The working tree usually carries `.obsidian/app.json` churn and
  stray `Untitled*.canvas` files — never `git add -A`.
- **Secret-scan the diff before committing:**
  `git diff | grep -nEi 'private key|password|client_secret|AKIA|api[_-]?key|ghp_|pat-na1|xox'`
- **Touched a tag? `Maps/Tag Registry.md` is in the same commit.** Added, renamed, retired, or changed
  what a tag means — the registry moves with it, or the vocabulary drifts.
- **Where the vault sits and how `git` must be invoked are per-machine** — check
  `_Agents/memory/machines/`. On the **Mac** it's `~/Development/watchtower` and `git`/`gh` work
  directly. On the **Windows laptop** the vault is `C:\Users\youBusato\Obsidian Vault` =
  `/mnt/c/Users/youBusato/Obsidian Vault`, and **`git`/`gh` must run from WSL**
  (`wsl.exe -d ubuntu -e bash -lc '...'`) — the SSH key and `gh` auth live there; Windows git-bash
  fails with `Permission denied (publickey)`. Spell out `youBusato` (the `GUILHE~1` 8.3 name
  won't resolve in WSL) and quote the path. Through that wrapper, write commit messages and PR bodies
  to a **file** and use `-F` / `--body-file`; inline `-m` mangles multi-line text and backticks.

## Preferred properties

`tags:` below carries only what the [Tagging](#tagging) section allows — `personal` or `work` for graph
scope, `ACME` for Acme employer scope, plus one `topic/*` per concept the note links. The canonical
copies are in `_Templates/`; match an existing note in the destination folder when in doubt.

Acme weekly log:

```yaml
type: weekly-log
date: YYYY-MM-DD
year: YYYY
quarter: Q1
domain: work
workspace: current-work
organization: Acme Analytics
area: work-log
role: systems-dev
status: active
tags:
  - work
  - ACME
  - topic/…            # one per concept the note links
related:
  - "Weekly Work Log Index"
```

Acme project note:

```yaml
type: project
status: active
domain: work
workspace: current-work
organization: Acme Analytics
area: data-platform
quarter: YYYY-Q1
tags:
  - work
  - ACME
  - topic/…
related:
  - "[[Project Index]]"
jira: []
```

Personal note:

```yaml
type: note
status: active
domain: personal
workspace: personal
tags:
  - personal         # add work too when the note genuinely spans both contexts
related:
  - "[[Personal Home]]"
```

Match existing notes in the destination folder when their frontmatter differs — consistency within
a folder wins.

## Entry points

- `Maps/the vault.md`, `Maps/Spaces Index.md`
- `Spaces/Work/Current Work/Current Work Home.md`
- `Spaces/Work/Future Work/Future Work Home.md`, `Spaces/Personal/Personal Home.md`
- `Maps/Tag Registry.md` — every allowed tag; `Maps/Concept Index.md` — the concept hubs
- `_Docs/Setup Guide.md` (new machine) · `_Docs/Usage Guide.md` (day to day)
- `_Docs/AI Note Intake Workflow.md`, `_Docs/Vault Architecture.md`, `_Docs/Skills Repo.md`,
  `_Docs/Agent Memory.md`
- `_Agents/README.md` — the agent layer's own map
- `_Agents/memory/README.md` — the memory index
