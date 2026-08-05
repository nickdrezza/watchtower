---
name: watchtower
description: >
  Primary operating context for "the vault" — your private Obsidian vault plus the agent
  skills and memory that run his work. Load FIRST, every session, before reading or writing anything
  in that repo. Use for: filing raw notes, meeting notes, interview notes, or work logs; creating or
  updating project/reference notes; answering personal, career, or Acme work-context questions from
  the vault; adding or editing a skill; and as the entry point to .agents/memory/ — this machine, where
  credentials live, and how to connect to the warehouse, dbt Cloud, AWS/EC2, the events platform, the CRM, Google
  Workspace, GitHub, and the tracker. Triggers: "organize this into my vault", "add to the vault", "file
  these notes", "update my project note", "what does my vault say about…", "add a skill", "how do I
  connect to…", "where do the credentials live". Team "how does X work" questions → shared-vault instead
  (see knowledge-router).
---

# the vault

A working repo, not prose to polish. Private — PII, interview notes, comp material, Acme internals.
Every edit gets committed, so treat it that way.

| Half | Path | Read by |
|---|---|---|
| **Vault** — notes, projects, meetings, work logs, career, personal | `Spaces/` `Concepts/` `Maps/` `Dashboards/` `Inbox/` `Daily Notes/` `_Templates/` `_Docs/` | Obsidian + agents |
| **Agent layer** — skills, memory, conventions | `.agents/` | agents only (dot-dir; Obsidian ignores it) |

**Location is per-machine.** Never assume a path — read the one `memory/machines/` profile
that applies to the target you're on. The path is the only thing that changes between machines;
everything else here is true everywhere. Some targets (a phone) have no clone at all.

## The model, in one line

**One brain, many disposable agents.** This vault is the memory; you are not. Search it — and prior
sessions across chats — before asking him to re-explain anything, and write durable facts back so the
next chat doesn't re-derive them. Full model: `.agents/docs/operating-model.md`. How to know you're
done: `.agents/docs/verification.md`.

## Hard rules

1. **No secret values.** Not in a note, a code block, or a pasted log. Found one in a dump? Strip it,
   say so, point at where it belongs. **Recording where a credential lives is required** — path,
   env-var name, your secret manager item, the warehouse user/role. That's `memory/credentials.md`'s whole job. The
   repo's extension-based check misses inline secrets; you are the backstop.
2. **No binaries.** No images, PDFs, plugin bundles, JS, CSS. Images → a `> Image removed:` callout +
   an entry in `_Docs/Image Descriptions.md`. PDFs → text-extracted `.md`.
3. **Never delete notes or rewrite his wording.** Add structure around rough notes. Explicit
   consolidation is fine — carry the original wording across.
4. **Respect space boundaries.** Never mix Acme material into personal or future-work spaces.
5. **Never push to `main`.** Branch → PR. Use `vault-sync`.
6. **Never write a low-confidence inference as fact.** Ask. See below.
7. **No filler, no editorializing.** Every sentence carries a fact a future reader needs — in a note
   *and* in your task report. Banned patterns and the test: root `AGENTS.md` hard rule 7.

## Ask instead of assuming

Uncertainty is fine; **writing it down as fact is not** — a wrong claim in a note reads as true for
years. Verify first (the code, the PR, the ticket, the email), ask second, assume never.

- **One batched multiple-choice question set, before the write.** Not a drip of one-liners, not a
  post-hoc "correct me if that's wrong."
- **State your understanding so it can be contradicted in one word** — *"my understanding: X keys on
  the legacy `md5(domain)`, not `company_id`. Correct?"* — never *"is my understanding correct?"*.
- **Approval is per listed item.** Silence is not approval; one yes covers only the complete set shown
  in the preview, not later or unlisted work.
- **Mark the seams.** Each claim is verified (name the source) or inferred (ask it). Never bridge a gap
  with a plausible-sounding mechanism.
- He doesn't know either → record it as an open question. Don't invent, don't silently drop.

## Verification preview before any vault write

Apply this gate to every entry in the repo: personal notes, work logs, projects, reference and meeting
notes, Inbox items, indexes and landing pages, and `.agents/memory/*.md`.

- By default, prepare the content in conversation without writing files or indexes. Show a
  `vault preview` with every destination path, the complete proposed Markdown for each new or
  short file, and the exact changed Markdown or diff for each existing file. Include frontmatter,
  body text, links, tags, and landing-page/index changes so the user does not need to inspect a PR or
  open the local vault to know what will be saved.
- Wait for approval after the preview. A confirmation approves only the complete set shown; never
  partially apply an unapproved set.
- An explicit, positive bypass in the current request skips this human preview and approval. Recognize
  case-insensitive phrases such as `full permissions`, `auto merge`, `automerge`, `auto-merge`, `just
  merge`, `skip the preview`, `skip verification`, `write it directly`, `save it without asking`, or
  `merge it now`. Clear equivalents are valid; vague requests such as “organize this” are not. A
  negated phrase such as “do not auto merge” never bypasses the gate.
- The bypass does not waive the hard rules: no secrets or binaries, no space-boundary violations, no
  direct push to `main`, and no uncertain claim written as fact. Preserve unresolved material as an
  open question or staging entry instead of guessing.

This is a chat content handoff, not a request for the user to review the PR. The PR remains the
delivery mechanism; this preview is the content verification step before the write.

Full rule in root `AGENTS.md`; standing instruction in `memory/working-preferences.md`.

## How to write here

The vault's value is being scannable in two years. Verbosity is the failure mode.

- **Say it once, plainly.** No preamble, no restating the question, no summarizing what you just wrote.
- **Nothing adjacent.** No recommendations, next steps, or "you might also consider" unless the note's
  subject *is* that decision. Off-topic suggestions are the main source of clutter.
- **Don't overexplain.** Assume a competent reader. One line beats a paragraph.
- **Keep every nuance that changes an outcome** — the gotcha, the exact id, the reason a decision went
  the way it did, the thing that cost hours. Brevity is not omission; cut words, never facts.
- **Prefer structure to prose.** A table, a labelled list, or a short code block carries more per line
  than a paragraph and ages better.
- Aim for elegance: the shortest form that a future agent can act on with no follow-up questions.
- **Objectivity.** A note is a record, not a pitch. No evaluative adjectives about the work
  (`robust`, `comprehensive`, `seamless`, `significantly`), no hedging frames ("it's worth noting
  that"), no enthusiasm. Attribute every claim or mark it inferred.

**Hard rule 7 in root `AGENTS.md`** carries the full banned-patterns table and the test — *would a
competent reader six weeks from now be worse off without this?* It applies to your task report in chat
exactly as much as to a note; a wall of text after a small change is the most common way this breaks.

## Tagging

**`Maps/Tag Registry.md` is the authority** — every allowed tag with when to apply it. Read it before
tagging; **update it in the same commit as any tag change.** A tag not in the registry shouldn't exist.

Tags carry graph scope, employer scope, and subject matter. `personal` and `work` are deliberate
graph-filter flags; the full policy is in root `AGENTS.md` and [[Tag Registry]].

| Namespace | Meaning |
|---|---|
| `personal` | Personal graph scope; mixed notes may also carry `work` |
| `work` | Professional graph scope; mixed notes may also carry `personal` |
| `ACME` | Employer scope — below |
| `topic/*` | Subject matter; one per `Concepts/` note, listed in `Maps/Concept Index.md` |

- **Never add a tag merely to restate a property.** No `work/log` on a `type: weekly-log` note. The
  scope tags are the intentional exception because Graph view needs cross-folder filters.
- **A `topic/*` tag rides along with a `[[link]]`** to that concept. No concept note → no topic tag;
  create the concept, list it in `Maps/Concept Index.md`, and register the tag in `Maps/Tag Registry.md`.
- `type: index` notes get no `topic/*` tags — they link to everything.
- Leave `source/pdf-converted`, `assets/images-converted`, and `excalidraw` alone.

### `#ACME`

Anything only meaningful **while the user is at Acme Analytics** gets tagged `ACME`, so it can one
day be swept into an archive with a single query and the rest of the vault survives a job change.

- **Mechanism:** `ACME` in the file's frontmatter `tags:`. For a file that is mostly portable with one
  employer-specific section, use an inline `#ACME` on that section instead.
- **Tag:** Acme projects, tickets, systems, people, meeting notes, work logs, client/event material,
  and the employer-specific memory files.
- **Don't tag:** this machine's setup, git/agent conventions, personal notes, career and future-work
  material, or anything reusable at a future employer.
- When you create or substantially edit a file, set this correctly. It is cheap now and expensive to
  backfill.

## Layout

- `Spaces/Work/Current Work/` — Projects, Meeting Notes, Work Logs, Reference, Training,
  Interviews, Visual Notes · `Spaces/Work/Future Work/` · `Spaces/Personal/` · `Spaces/Shared/`
- `Concepts/` durable concept notes · `Maps/` MOCs and indexes · `Dashboards/` Obsidian `.base` files
- `_Templates/` · `_Docs/` governance · `Inbox/{Raw Dumps,Processed}/` · `Daily Notes/`
- `.agents/` — `skills/`, `memory/`, `CONVENTIONS.md`, `docs/`, `scripts/`
- Root `AGENTS.md` is the always-on instruction file; `CLAUDE.md` / `GEMINI.md` /
  `.github/copilot-instructions.md` are stubs pointing at it.

Wiki-links resolve by **note name**, not path — moving a note into `Archive/` doesn't break `[[links]]`.

## `.agents/memory/` — read before any hands-on work

The operational knowledge these skills assume. **This is what makes an agent behave the same in every
harness** — connecting to a system is never left to whatever a tool happens to have configured.

**Read `environment.md` and `credentials.md` first**, and let `environment.md` route you to the one
`machines/` profile that applies. Nearly every failure mode here is in one of them: **wrong machine**,
wrong shell (on Windows the Bash tool is Git Bash, *not* WSL), a CLI that isn't installed on this target,
wrong AWS profile, expired SSO session, read-only SQL MCP, symlinks across the WSL boundary, a Sheet not
shared with the service account.

| Need | File |
|---|---|
| Which target am I on, and what's true everywhere | `environment.md` |
| This machine's paths, shells, and missing CLIs | `machines/{macos,windows-wsl,ec2,mobile}.md` |
| Where a key / token / profile lives | `credentials.md` |
| Which connector owns a question, and where each one lies | `connectors.md` |
| **When to write memory** — the fast path vs the reviewed pass | `README.md` |
| the warehouse account, roles, read-only MCP + how to run DDL anyway | `warehouse.md` |
| dbt Cloud ids, why local `dbt build` fails, slow CI | `transform.md` |
| AWS accounts, EC2 automation server, cron, CloudWatch, DR | `cloud-and-servers.md` |
| Sheets/Drive/email, the service account + Editor-share gotcha | `workspace.md` |
| the CRM sync mechanisms, object ids, association types | `crm.md` |
| events-api subprojects, cron cadence, custom fields | `events-platform.md` |
| the newsletter platform share, SFTP, the CC-email job, validity codes, subscription classes, sending domains | `newsletter.md` |
| The three the messaging platform pipelines, and why its open rates are overstated | `messaging-platform.md` |
| `gh` identities per shell, repos, the tracker, shared-vault access | `git-and-tickets.md` |
| the warehouse project layers, table grains, costly gotchas | `warehouse.md` |
| the vendor platform personas, the filter UDF, the recurring CI failure | `vendor-platform.md` |
| the pipeline dashboard / the list-builder app, Streamlit-in-the warehouse gotchas | `internal-apps.md` |
| Who's who and what they own | `people.md` |
| Standing instructions from the user | `working-preferences.md` |
| Active project state and pointers | `projects.md` |

Memory is **point-in-time**. Environment facts (paths, accounts, which shell holds the SSH key) are
stable — act on them. Code and data facts drift — verify first. `vault-memory` keeps this current.

## Skills

Canonical at `.agents/skills/<name>/SKILL.md` — the universal project path Codex, Cursor, Gemini CLI,
Copilot, and Antigravity read natively.

**Claude Code reads `.claude/skills/`** and won't auto-discover `.agents/skills/`. Run
`.agents/scripts/install-skills.sh --here` once, or **just read the files** — they're plain Markdown.
Never report a skill unavailable because your harness didn't load it.

| Skill | Use for |
|---|---|
| `watchtower` | **The primary context. Load it first, every session.** Layout, hard rules, how to write here, the employer-scope tag, the memory index. |
| `bootstrap` | Sets up a new user or machine, seeds the memory maps, and teaches the operating model. |
| `vault-memory` | Refreshes `.agents/memory/` from prior sessions and your connectors. |
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

employer-specific skills carry `ACME` in their frontmatter `tags:`, same convention as notes and memory.

**Skills vs memory:** a skill is *how to perform a task*; memory is *what is true about this
environment*. A skill hard-coding an account id, path, or cron expression is doing memory's job.

### Adding or editing a skill

New skills belong here, at `.agents/skills/<name>/SKILL.md`. Edit there, never the `.claude/skills/`
mirror. Full flow and checklist: `.agents/CONVENTIONS.md`. Short version:

1. Skill or memory? Mostly-facts → memory.
2. `.agents/scripts/new-skill.sh <name>` (bash — run from WSL or Git Bash).
3. Write the `description` first; it's the trigger every platform reads.
4. Register it in the three hand-maintained index tables: this file's table above,
   `.agents/README.md`, `_Docs/Skills Repo.md`. Otherwise it's invisible.
5. `.agents/scripts/install-skills.sh --here` — the mirror is a copy, not a link.
6. Branch `feat/<slug>` + PR.

## Filing a raw dump

Per `_Docs/AI Note Intake Workflow.md`:

1. Identify date range, projects, meetings, tasks, links, people, open questions.
2. Pick the space **before** editing.
3. File under the right subfolder (`Work Logs/2. Systems Dev Weekly Notes/…`, `Projects/…`,
   `Meeting Notes/…`, `Reference/…`, `Training/…`, `Interviews/…`).
4. Add YAML properties for that space (templates in `reference.md`) — including `ACME` when it applies.
5. Add `[[wiki-links]]` to existing Concepts and project notes.
6. Keep his wording. Apply **How to write here** to anything you author.
7. Genuinely uncertain or mixed → `Inbox/Processed/` or an `## Open questions` section. Don't guess.

## Before you finish

- `git status` / `git diff` show only intended changes — never `git add -A` (the tree carries
  `.obsidian/app.json` churn and stray `Untitled*.canvas` files).
- Secret-scan the diff:
  `git diff | grep -nEi 'private key|password|client_secret|AKIA|api[_-]?key|ghp_|pat-na1|xox'`
- Properties valid, `ACME` set where it applies, links resolve, nothing deleted unasked.
- **Any tag added, renamed, or retired → `Maps/Tag Registry.md` updated in the same commit.**

Full folder map, per-space property templates, the status/dashboard convention, and the
secret-handling checklist: [`reference.md`](reference.md).
