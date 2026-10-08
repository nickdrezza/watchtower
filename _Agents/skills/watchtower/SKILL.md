---
name: watchtower
description: >
  Operating rules for the private vault and its agent memory. Use to file notes, meeting notes, or
  work logs, update project notes, answer from the vault, add a skill, or find how to connect to a
  system. Triggers: "add to the vault", "file these notes", "how do I connect to…".
---

# the vault

A working repo, not prose to polish. Private — PII, interview notes, comp material, Acme internals.
Every edit gets committed, so treat it that way.

| Half | Path | Read by |
|---|---|---|
| **Vault** — notes, projects, meetings, work logs, career, personal | `Spaces/` `Concepts/` `Inbox/` `_Templates/` `README.md` | Obsidian + agents |
| **Agent layer** — skills, memory, tag registry, `wt` | `_Agents/` (also `.agents/`, a symlink) | agents, and readable in Obsidian |

**Location is per-machine.** Never assume a path — read the one `memory/machines/` profile
that applies to the target you're on, routed by `memory/machines/index.md`. The path is the only thing that changes between machines;
everything else here is true everywhere. Some targets (a phone) have no clone at all.

## Hard rules

The eight hard rules live in root `AGENTS.md` and are not restated here. Three carry vault-specific
mechanics worth having in front of you:

1. **Secrets.** The repo's extension-based check misses inline secrets — **you are the backstop**.
   Recording *where* a credential lives is required, and that is the space's `memory/credentials/`'s job.
2. **Binaries.** Images → a `> Image removed:` callout plus an entry in `_Agents/image-descriptions.md`.
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
- **Approval is per listed item.** Silence is not approval; one yes covers only the items that you
  listed, not later or unlisted work.
- **Mark the seams.** Each claim is verified (name the source) or inferred (ask it). Never bridge a gap
  with a plausible-sounding mechanism.
- He doesn't know either → record it as an open question. Don't invent, don't silently drop.

## The PR is the preview

`AGENTS.md` → **Write to the vault** is the rule. Every write to this repo — notes, indexes, landing
pages, `_Agents/memory/`, `Spaces/*/memory/` — goes on a branch, in a commit, in a PR to this repo. The
user reviews the diff and merges it. Do not show a chat preview first; show the Markdown or diff in chat
only when the user asks. A memory fast-path fact is one commit on the working branch
(`_Agents/memory/README.md`).

The PR does not waive the hard rules or **Ask instead of assuming**: ask the batched questions before
you write. `auto merge` / `just merge` mean the git operation and nothing else.

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

**`_Agents/tags.md` is the authority** — every allowed tag with when to apply it. Read it before
tagging; **update it in the same commit as any tag change.** A tag not in the registry shouldn't exist.

**Topic tags (`topic/*`) are the graph:** they connect notes across folders and spaces, and `wt search`
uses each registered topic as a search word. **Scope tags (`personal`, `work`, `ACME`) are optional on
new notes:** the folder already says which space a note is in. Keep them on existing notes (Obsidian
graph filters use them); `wt doctor` still flags an `ACME` tag under Personal or Career.

| Namespace | Meaning |
|---|---|
| `personal` | Personal graph scope; mixed notes may also carry `work` |
| `work` | Professional graph scope; mixed notes may also carry `personal` |
| `ACME` | Employer scope — below |
| `topic/*` | Subject matter; one per `Concepts/` note, listed in `Concepts/index.md` |

- **Never add a tag merely to restate a property.** No `work/log` on a `type: weekly-log` note. The
  scope tags are the intentional exception because Graph view needs cross-folder filters.
- **A `topic/*` tag rides along with a `[[link]]`** to that concept. No concept note → no topic tag;
  create the concept, check that it shows in `Concepts/index.md`, and register the tag in `_Agents/tags.md`.
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

`Spaces/{Personal,Work,Career}/` hold the notes; each space has its own `memory/` and `skills/`.
`Concepts/` holds one note per durable subject. `Inbox/{Raw Dumps,Processed}/` holds material with no
home yet. `_Templates/` holds note templates. `_Agents/` holds shared skills, shared memory, `tags.md`,
and `wt`. Full tree: [`reference.md`](reference.md#folder-layout).

Wiki-links resolve by **note name**, not path — moving a note into `Archive/` doesn't break `[[links]]`.

## Which knowledge base

| Request | Goes to |
|---|---|
| Personal, career, or "my" work context (plans, logs, my view of a project) | this vault |
| "How does X work", "why did we decide Y", runbooks, team policy | the team shared vault — read its clone directly |
| "How do I connect to X", "where do the credentials live" | the active space's `memory/`, then `_Agents/memory/`; for a system fact the shared vault wins, for this machine memory wins |
| "Should the team know this", "put this in the dev wiki" | `shared-vault` skill |

Never copy vault content into the shared vault, and never copy shared-vault facts into this vault.
Refer to the other base with a short summary and a link. A task that spans both is two writes.

## Memory — load by task

Shared memory is in `_Agents/memory/` (true in every space). Each space keeps its own memory in
`Spaces/<Name>/memory/` (for work, `Spaces/Work/memory/`). Put a fact in the narrowest folder where it
is true.

The operational knowledge these skills assume. **This is what makes an agent behave the same in every
harness** — connecting to a system is never left to whatever a tool happens to have configured.

Do not preload this folder; the index is [`memory/README.md`](../../memory/README.md). Shell commands
or machine-dependent paths/tooling require `machines/index.md` and exactly one matching `machines/`
profile. Authentication, profiles, secret locations, or connection failures require the space's
`memory/credentials/` plus the relevant platform file. Topic work requires only the matching topic memory. Live state comes
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
Skills here are the owner's, also work-topic ones. Team skills live only in the team's skills repo;
do not copy them in.

**Skills vs memory:** a skill is *how to perform a task*; memory is *what is true about this
environment*. A skill hard-coding an account id, path, or cron expression is doing memory's job.

### Adding or editing a skill

Shared skills go in `_Agents/skills/<name>/`; a skill for one space goes in `Spaces/<Name>/skills/<name>/`.
Edit the real folder; the global skills folders only hold links to it. Copy
`_Agents/templates/skill-template`, write the `description` first, add a row to `_Agents/README.md`,
run `_Agents/wt install`, and open a PR. Full steps: [`reference.md`](reference.md#adding-a-skill).

## Filing a raw dump

Follow [`reference.md` → Filing a raw dump](reference.md#filing-a-raw-dump). In short: pick the space
**before** you edit, file under the correct subfolder, add the properties for that space (with `ACME`
when it applies), link existing concepts and project notes, keep the user's wording, and put material
that is truly uncertain or mixed in `Inbox/Processed/` or an `## Open questions` section. Treat
identifiers in a dictated dump as not verified.

## Before you finish

- `git status` / `git diff` show only intended changes — never `git add -A` (the tree carries
  `.obsidian/app.json` churn and stray `Untitled*.canvas` files).
- Secret-scan the diff:
  `git diff | grep -nEi 'private key|password|client_secret|AKIA|api[_-]?key|ghp_|pat-na1|xox'`
- Properties valid, `ACME` set where it applies, links resolve, nothing deleted unasked.
- **Any tag added, renamed, or retired → `_Agents/tags.md` updated in the same commit.**

Folder tree, property templates, status and dashboards, filing steps, adding a skill, and the
secret and binary checklist: [`reference.md`](reference.md).
