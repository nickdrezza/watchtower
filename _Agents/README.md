# `_Agents/` — the agent layer

Everything an AI agent needs to operate in this repo and on your work. Reachable as `.agents/` too —
a committed symlink, so every coding agent finds the universal path while Obsidian indexes the
undotted real folder.

Repo-wide instructions live in the root [`AGENTS.md`](../AGENTS.md). This folder is the machinery.

```
_Agents/
├── README.md                 you are here
├── memory/                   memory true in every space (space memory: Spaces/<Name>/memory/)
│   ├── README.md             the memory index + WHEN TO WRITE MEMORY
│   ├── machines/             one profile per target — add one per machine you work on
│   └── working-preferences/  how you want agents to work
├── skills/                   the skills — one folder per skill, canonical source of truth
│   └── <name>/
│       ├── SKILL.md          required: frontmatter (name + description) + Markdown body
│       ├── reference.md      optional: deep detail, loaded only when SKILL.md points to it
│       └── scripts/          optional: executable helpers (run, not read into context)
├── archive/                  old agent-layer pages, kept as history
├── tags.md                   the tag registry
├── image-descriptions.md     text for images removed from the vault
├── placeholders.md           the stand-in values to replace after setup
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

Read [`memory/machines/index.md`](memory/machines/index.md) plus exactly one machine profile before
machine-dependent commands. Read [`Spaces/Work/memory/credentials/`](../Spaces/Work/memory/credentials/index.md) only for
authentication, profiles, secret locations, or connection failures. Full routing index:
[`memory/README.md`](memory/README.md).

Skills say *how to perform a task*; memory says *what is true about this environment*. Keep the facts in
memory and have skills point at them. **Locations, never values** — the path or env-var name, never the
secret itself. employer-specific files carry `ACME` in their frontmatter `tags:` so they can be archived in
one query if you changes jobs; `vault-memory` keeps the folder current.

## Skills

| Skill | What it does |
|---|---|
| [`watchtower`](skills/watchtower/) | Vault-specific context: layout, writing, the PR-as-preview rule, employer scope, filing, adding a skill, and memory routing. |
| [`bootstrap`](skills/bootstrap/) | Sets up a new user or machine, seeds the memory maps, and teaches the operating model. |
| [`weekly-work-log`](../Spaces/Work/skills/weekly-work-log/) | Writes or updates the weekly manager-facing work log, from evidence only, in the house format. |
| [`vault-memory`](skills/vault-memory/) | Refreshes `_Agents/memory/` from prior sessions and your connectors. |
| [`vault-sync`](skills/vault-sync/) | Pull → refresh → commit → PR → merge → concise summary. The single entry point for "sync my vault". |
| [`vault-doctor`](skills/vault-doctor/) | Mechanical integrity checks — links, tags, frontmatter, skill-index drift, secrets. Backed by `wt doctor`. |
| [`vault-prune`](skills/vault-prune/) | Quality pass — slop, near-duplicates, bloat, stale claims, orphans, gaps. Per-item approval; never deletes unasked. |
| [`vault-edit`](skills/vault-edit/) | Safe create / move / rename / merge / split / archive / delete, and what must move with the file. |
| [`shared-vault`](../Spaces/Work/skills/shared-vault/) | Moves vault knowledge into the team shared vault as a PR, rewritten for a team audience and stripped of private content. To read team knowledge, read the shared vault clone directly. |
| [`secrets`](skills/secrets/) | Get, store, rotate, and inject credentials. **Never surfaces a value.** |
| [`playwright-testing`](skills/playwright-testing/) | Real-browser tests for user-visible behavior — uploads, downloads, forms, navigation, responsive layout. |
| [`personal`](../Spaces/Personal/skills/personal/) | Personal material: diary, memories, reflections, people, places, pets, and triage of Uncategorized notes. One router, one reference file for each note type. |

Skills here are the owner's only. Team skills live in the team's skills repo and are not copied here.

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

Path table for each harness and the Windows↔WSL note: [`../README.md`](../README.md#set-up).

## Authoring a skill

Shared skills go in `_Agents/skills/<name>/`; a skill for one space goes in `Spaces/<Name>/skills/<name>/`.

```bash
cp -r _Agents/templates/skill-template _Agents/skills/my-skill-name
# set name: my-skill-name, then write the `description` first (it's the trigger)
_Agents/wt install            # link the new skill
```

Then **add a row to the Skills table above**. This file is the one hand-maintained skill index. Full
steps and rules: [`skills/watchtower/reference.md`](skills/watchtower/reference.md#adding-a-skill).

## History

These skills were a separate private repo, `<you>/skills`. They were merged into the vault so one
repo carries both the knowledge and the skills that operate on it — see [`skills/watchtower/reference.md`](skills/watchtower/reference.md#adding-a-skill). Treat
the old repo as archived; this folder is the source of truth.
