---
name: watchtower
description: >
  Primary operating context for "the vault" — your private Obsidian vault plus the agent
  skills and memory that run your work. Load for vault work, not for unrelated prompts. Use for:
  filing raw notes, meeting notes, interview notes, or work logs; creating or
  updating project/reference notes; answering personal, career, or Acme work-context questions from
  the vault; adding or editing a skill; and as the entry point to _Agents/memory/ — this machine, where
  credentials live, and how to connect to every platform you work in — the warehouse, the cloud
  account, the CRM, GitHub, the tracker. Triggers: "organize this into my vault", "add to the vault", "file
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
| **Agent layer** — skills, memory, conventions | `_Agents/` (also `.agents/`, a symlink) | agents, and readable in Obsidian |

**Location is per-machine.** Never assume a path — read the one `memory/machines/` profile
that applies to the target you're on. The path is the only thing that changes between machines;
everything else here is true everywhere. Some targets (a phone) have no clone at all.

## Hard rules

The eight hard rules live in root `AGENTS.md` and are not restated here. Three carry vault-specific
mechanics worth having in front of you:

1. **Secrets.** The repo's extension-based check misses inline secrets — **you are the backstop**.
   Recording *where* a credential lives is required, and that is `memory/credentials.md`'s job.
2. **Binaries.** Images → a `> Image removed:` callout plus an entry in `_Docs/Image Descriptions.md`.
   PDFs → text-extracted `.md`.
3. **The user's wording.** Add structure around rough notes; never rewrite them. Explicit
   consolidation is fine and carries the original wording across.

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

`AGENTS.md` → **Vault writes** is the rule; this is the phrase list it refers to. The gate covers every
entry in the repo — notes, indexes, landing pages, `_Agents/memory/*.md`. Show a `vault preview` with
every destination path and the complete proposed Markdown or exact diff, then wait. A confirmation
approves only the set shown.

Bypass, current-request only and case-insensitive: **`full perms`** is canonical; `full permissions`,
`skip the preview`, `skip verification`, `write it directly`, `save it without asking` are equivalent.
Clear equivalents count; vague requests like "organize this" do not, and a negated phrase never
bypasses. **Merge phrases are not a bypass** — `auto merge` / `just merge` mean the git operation and
nothing else; they collide with GitHub's own auto-merge setting.

A bypass skips the human preview. It never waives the hard rules.

## How to write here

The vault's value is being scannable in two years. Verbosity is the failure mode.

- **Say it once, plainly.** No preamble, no restating the question, no summarizing what you just wrote.
- **Nothing adjacent.** No recommendations, next steps, or "you might also consider" unless the note's
  subject *is* that decision. Off-topic suggestions are the main source of clutter.
- **Don't overexplain — but don't presume.** One line still beats a paragraph. A "competent reader" is
  fluent in the craft and has *never seen this code* — they know what a lint rule is, not what your
  `roster-base.ts` is. Cut words, never the reader's footing.
- **Plain first, then the names.** Say what the thing is and what goes wrong in ordinary words before
  naming a file, symbol, or ticket; lead each item with the consequence, not the mechanism. A path or
  symbol name identifies, it does not inform. Orientation isn't padding — it's the fact needed most.
- **Keep every nuance that changes an outcome** — the gotcha, the exact id, the reason a decision went
  the way it did, the thing that cost hours. Brevity is not omission; cut words, never facts.
- **Prefer structure to prose.** A table, a labelled list, or a short code block carries more per line
  than a paragraph and ages better.
- Aim for elegance: the shortest form that a future agent can act on with no follow-up questions.
- **Objectivity.** A note is a record, not a pitch. No evaluative adjectives about the work
  (`robust`, `comprehensive`, `seamless`, `significantly`), no hedging frames ("it's worth noting
  that"), no enthusiasm. Attribute every claim or mark it inferred.

**Hard rule 7 in root `AGENTS.md`** is the rule. Apply two tests — *would a
competent reader six weeks from now be worse off without this?* and *could a teammate who has never
opened this code say what broke and why it matters?* Both apply to your task report in chat exactly as
much as to a note; a wall of text after a small change is the most common way this breaks, and
compressing into jargon is the second.

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
- `_Agents/` — `skills/`, `memory/`, `CONVENTIONS.md`, `docs/`, `scripts/`
- Root `AGENTS.md` is the always-on instruction file; `CLAUDE.md` / `GEMINI.md` /
  `.github/copilot-instructions.md` are stubs pointing at it.

Wiki-links resolve by **note name**, not path — moving a note into `Archive/` doesn't break `[[links]]`.

## `_Agents/memory/` — load by task

The operational knowledge these skills assume. **This is what makes an agent behave the same in every
harness** — connecting to a system is never left to whatever a tool happens to have configured.

Do not preload this folder; the index is [`memory/README.md`](../../memory/README.md). Shell commands
or machine-dependent paths/tooling require `environment.md` and exactly one matching `machines/`
profile. Authentication, profiles, secret locations, or connection failures require `credentials.md`
plus the relevant platform file. Topic work requires only the matching topic memory. Live state comes
from its connector.

Memory is **point-in-time**. Environment facts (paths, accounts, which shell holds the SSH key) are
stable — act on them. Code and data facts drift — verify first. `vault-memory` keeps this current.

## Skills

Canonical at `_Agents/skills/<name>/SKILL.md` — the universal project path Codex, Cursor, Gemini CLI,
Copilot, and Antigravity read natively.

**Claude Code reads its own global skills folder** and won't auto-discover `_Agents/skills/`. Run
`_Agents/wt install` once, or **just read the files** — they're plain Markdown.
Never report a skill unavailable because your harness didn't load it.

**The skill index is [`_Agents/README.md`](../../README.md)** — one table, one place to update.
Employer-specific skills carry `ACME` in their frontmatter `tags:`, same convention as notes and memory.

**Skills vs memory:** a skill is *how to perform a task*; memory is *what is true about this
environment*. A skill hard-coding an account id, path, or cron expression is doing memory's job.

### Adding or editing a skill

New skills belong here, at `_Agents/skills/<name>/SKILL.md`. Edit there; Claude Code's skills folder only
holds links to it. Full flow and checklist: `_Agents/CONVENTIONS.md`. Short version:

1. Skill or memory? Mostly-facts → memory.
2. `cp -r _Agents/templates/skill-template _Agents/skills/<name>`, then set `name:` to match.
3. Write the `description` first; it's the trigger every platform reads.
4. Add a row to `_Agents/README.md`'s Skills table. `vault-doctor` fails if you miss it.
5. `_Agents/wt install` — links the new skill.
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
