# `_Agents/` — the agent layer

Everything an AI agent needs to operate in this repo and on your work. Reachable as `.agents/` too —
a committed symlink, so every coding agent finds the universal path while Obsidian indexes the
undotted real folder.

Repo-wide instructions live in the root [`AGENTS.md`](../AGENTS.md). This folder is the machinery.

```
_Agents/
├── README.md                 you are here
├── CONVENTIONS.md            how to author a skill (the SKILL.md spec + pre-commit checklist)
├── memory/                   operational knowledge — the environment, credentials, platforms
│   ├── README.md             the memory index + WHEN TO WRITE MEMORY
│   ├── connectors.md         the live systems: who owns what, and where each one lies
│   └── machines/             one profile per target — add one per machine you work on
├── skills/                   the skills — one folder per skill, canonical source of truth
│   └── <name>/
│       ├── SKILL.md          required: frontmatter (name + description) + Markdown body
│       ├── reference.md      optional: deep detail, loaded only when SKILL.md points to it
│       └── scripts/          optional: executable helpers (run, not read into context)
├── docs/                     agent doctrine (vs ../_Docs/, which is human/vault governance)
│   ├── operating-model.md    HOW TO BEHAVE — one brain, fetch before asking, chats are disposable
│   ├── verification.md       how to know you're done; what counts as evidence
│   ├── platforms.md          per-tool path matrix (where each harness reads skills + instructions)
│   └── portability.md        the portability model + when to reach for rulesync
├── templates/skill-template/ starter SKILL.md for a new skill
├── global-instructions.md    the text `wt install` writes into each harness's global instruction file
├── search-fixtures.json      prompts and the pages search must (or must not) return
├── wt.json                   this vault's search trigger words and account names for `wt`
└── wt                        the one tool: search · doctor [--fix] · install · index
```

## Start here

Root [`AGENTS.md`](../AGENTS.md) is the small always-on bootstrap. Use this map after prompt-specific
search points into the agent layer; do not read it or its linked files wholesale at session start.

## Memory

[`memory/`](memory/) is the operational half: which machine we're on, **where every credential lives**,
how to connect to each platform you work in, who's who, what's in flight, and how you want agents to
work.

Read [`memory/environment.md`](memory/environment.md) plus exactly one machine profile before
machine-dependent commands. Read [`memory/credentials.md`](memory/credentials.md) only for
authentication, profiles, secret locations, or connection failures. Full routing index:
[`memory/README.md`](memory/README.md).

Skills say *how to perform a task*; memory says *what is true about this environment*. Keep the facts in
memory and have skills point at them. **Locations, never values** — the path or env-var name, never the
secret itself. employer-specific files carry `ACME` in their frontmatter `tags:` so they can be archived in
one query if you changes jobs; `vault-memory` keeps the folder current.

## Skills

| Skill | What it does |
|---|---|
| [`watchtower`](skills/watchtower/) | Vault-specific context: layout, writing, preview gate, employer scope, filing, and memory routing. |
| [`bootstrap`](skills/bootstrap/) | Sets up a new user or machine, seeds the memory maps, and teaches the operating model. |
| [`weekly-work-log`](skills/weekly-work-log/) | Writes or updates the weekly manager-facing work log, from evidence only, in the house format. |
| [`vault-memory`](skills/vault-memory/) | Refreshes `_Agents/memory/` from prior sessions and your connectors. |
| [`vault-sync`](skills/vault-sync/) | Pull → refresh → commit → PR → merge → concise summary. The single entry point for "sync my vault". |
| [`vault-doctor`](skills/vault-doctor/) | Mechanical integrity checks — links, tags, frontmatter, skill-index drift, secrets. Backed by `wt doctor`. |
| [`vault-prune`](skills/vault-prune/) | Quality pass — slop, near-duplicates, bloat, stale claims, orphans, gaps. Per-item approval; never deletes unasked. |
| [`vault-edit`](skills/vault-edit/) | Safe create / move / rename / merge / split / archive / delete, and what must move with the file. |
| [`skills-sync`](skills/skills-sync/) | Publishes selected skills to an external destination — a plugin marketplace, a shared skills repo — reformatted to that destination's own layout and sanitized of anything machine-bound. Requires the user to name every skill explicitly; also reports drift and shadowing between the two copies. Ledger: [`_Docs/Skill Exports.md`](../_Docs/Skill%20Exports.md). |
| [`knowledge-router`](skills/knowledge-router/) | Decides which knowledge base owns a task — this vault or the team's shared one. |
| [`shared-vault-sync`](skills/shared-vault-sync/) | Both directions with the team vault in one command, drift check first. |
| [`shared-vault-promote`](skills/shared-vault-promote/) | Outbound: what the team should have, rewritten for a team audience and stripped of anything private. |
| [`shared-vault-ingest`](skills/shared-vault-ingest/) | Inbound: indexes the team vault and absorbs its gotchas and constraints into memory. Never copies it. |
| [`secrets`](skills/secrets/) | Get, store, rotate, and inject credentials. **Never surfaces a value.** |
| [`playwright-testing`](skills/playwright-testing/) | Real-browser tests for user-visible behavior — uploads, downloads, forms, navigation, responsive layout. |
| [`personal-vault`](skills/personal-vault/) | The front door for personal material; routes to the right section. |
| [`personal-memory`](skills/personal-memory/) | Past events, milestones, and life-history notes. |
| [`personal-reflection`](skills/personal-reflection/) | Opinions, values, identity questions, and rambles. |
| [`personal-entities`](skills/personal-entities/) | People, pet, and location notes, and the links to them. |
| [`personal-triage`](skills/personal-triage/) | Classifies personal material staged in Uncategorized. |
| [`diary`](skills/diary/) | Lightly cleaned daily entries that preserve your voice. |

The middle three are the **vault family**: `vault-sync` orchestrates, calling `weekly-work-log` and
`vault-memory`. Run `vault-sync` and you get all of it.

## Two standards, used deliberately

| Layer | Standard | Lives in | What it's for |
|---|---|---|---|
| **Skills** | [`SKILL.md`](https://agentskills.io/specification) | `_Agents/skills/` | Discrete, lazily-loaded capabilities — one folder each |
| **Repo instructions** | [`AGENTS.md`](https://agents.md) | [`../AGENTS.md`](../AGENTS.md) | How an agent should behave *in this repo*, always loaded |
| **Memory** | (ours) | `_Agents/memory/` | Durable facts about the environment, read on demand |

`CLAUDE.md`, `GEMINI.md`, and `.github/copilot-instructions.md` at the repo root are stubs pointing
at `AGENTS.md`, so no harness gets a different set of rules.

## Getting a harness to see the skills

`.agents/skills/` is read natively at project level by Codex, Cursor, Gemini CLI, Copilot, and
Antigravity — nothing to do. (`.agents` is a committed symlink to the real `_Agents/`; the dot had to
go so Obsidian would index the folder.) **Claude Code reads `.claude/skills/`**, so either:

```bash
_Agents/wt install            # one link per skill in ~/.agents/skills + ~/.claude/skills
_Agents/wt install --copy     # copies instead of links (Windows/WSL)
```

…or just read `_Agents/skills/<name>/SKILL.md` directly. It's plain Markdown; auto-discovery is a
convenience, not a requirement.

Full path matrix: [`docs/platforms.md`](docs/platforms.md). Why it's built this way:
[`docs/portability.md`](docs/portability.md).

## Authoring a skill

**New skills belong here**, at `_Agents/skills/<name>/SKILL.md`.

```bash
cp -r _Agents/templates/skill-template _Agents/skills/my-skill-name
# set name: my-skill-name, then write the `description` first (it's the trigger)
_Agents/wt install            # link the new skill
```

Then **add a row to the Skills table above** — this file is the one hand-maintained skill index, so a
new skill is invisible to a reader until it's there, and `vault-doctor` fails without it. The
`watchtower` skill and `_Docs/Skills Repo.md` used to carry duplicate copies of this table and now
point here; don't reintroduce them.

Rules of thumb (full flow and checklist in [`CONVENTIONS.md`](CONVENTIONS.md)):

- One skill per folder; folder name = `name:` frontmatter = lowercase-hyphenated, and they match.
- **Only `name` and `description` are load-bearing.** Everything else is optional, tool-specific
  sugar. Never let a skill *break* without a Claude-only field.
- `description` is the trigger — state what it does *and* when to use it, with phrases the user
  would actually type.
- Keep `SKILL.md` under ~500 lines; push detail into `reference.md`, code into `scripts/`.
- Prefer POSIX shell / `python3` / common CLIs. Isolate and document any tool-specific step.

## History

These skills were a separate private repo, `<you>/skills`. They were merged into the vault so one
repo carries both the knowledge and the skills that operate on it — see [`../_Docs/Skills Repo.md`](../_Docs/Skills%20Repo.md). Treat
the old repo as archived; this folder is the source of truth.
