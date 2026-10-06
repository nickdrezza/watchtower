# Watchtower

> **A shared brain for your AI agents.** One plain-Markdown vault that every harness reads as memory —
> so your chats become disposable and nothing gets re-explained twice.

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Docs: Markdown](https://img.shields.io/badge/docs-Markdown-blue.svg)](#whats-in-here)
[![Works with](https://img.shields.io/badge/works%20with-Claude%20Code%20·%20Codex%20·%20Cursor%20·%20Gemini%20·%20Copilot-8A2BE2.svg)](_Agents/docs/platforms.md)

This is a **template**. Generate your own repo from it, run one skill, and start working.

---

## The idea

Most people scale AI development by building a *hierarchy* — a manager agent that owns context and
delegates to specialists, each with its own private memory. That means orchestration to maintain,
hand-off protocols, and context that dies when a thread does.

This does the opposite. **One vault, read by every agent.** No manager thread, no per-agent memory, no
message passing. Every agent knows everything.

What that buys you:

- **A new chat is cheap.** It rehydrates from the vault, from your prior sessions, and from your
  connectors — without being told to.
- **Chats are disposable.** End them freely. When a project resurfaces a month later, open a new chat
  instead of hunting the old one.
- **Nothing gets re-explained.** The gotcha that cost you three hours is written down once.
- **Every tool behaves the same.** One set of rules, one skills directory, every harness.

Subagents still earn their place on large work — roughly one per feature or commit — but for parallel
*execution*, never to hold context.

## Quickstart

```bash
gh repo create my-vault --template <you>/watchtower --private
cd my-vault
```

Then open it in any agent and say **"set me up"** — the [`bootstrap`](_Agents/skills/bootstrap/) skill
installs the skills, wires the global instruction bridge, writes your machine profile, seeds the
credential and connector maps, and deletes the example content.

Prefer to do it by hand? [`_Docs/Setup Guide.md`](_Docs/Setup%20Guide.md) — about 15 minutes.

**Keep it private.** This fills up with credential locations, work context, and personal notes.

## What's in here

Two halves, one repo.

```text
AGENTS.md                authoritative rules for every agent  ← the entrance
CLAUDE.md, GEMINI.md,    stubs -> AGENTS.md, so no harness gets different rules
  .github/copilot-instructions.md

_Agents/                 the agent layer (also .agents/, a symlink for tool auto-discovery)
  docs/
    operating-model.md   HOW TO BEHAVE — the model above, as instructions
    verification.md      how to know you're done; what counts as evidence
    platforms.md         where each harness reads skills and instructions
    portability.md       why it's built this way
  memory/                what is TRUE about your environment
    README.md            the index + WHEN TO WRITE MEMORY
    connectors.md        which live system owns which question
    machines/            one profile per target — paths, shells, what's NOT installed
  skills/<name>/         one folder per skill, read by every harness
  scripts/               install-skills · install-instructions · check_vault
  CONVENTIONS.md         how to author a skill

Spaces/                  your actual notes — Work / Personal / Shared
Concepts/                durable topic notes; the targets of topic/* tags
Maps/                    indexes, and Tag Registry — the tag authority
Dashboards/              Obsidian .base views (they filter on `type ==`)
Inbox/                   Raw Dumps + Processed — where uncertain material lands
_Templates/  _Docs/      frontmatter templates · Setup & Usage guides, governance
```

**Skills vs memory** is the distinction that keeps this clean. A skill is *how to perform a task*.
Memory is *what is true about this environment*. A skill that hard-codes an account id or a path is
doing memory's job.

## The skills

| Skill | What it does |
|---|---|
| [`watchtower`](_Agents/skills/watchtower/) | **The primary context. Loaded first, every session.** |
| [`bootstrap`](_Agents/skills/bootstrap/) | Sets up a new user or machine, and teaches the model |
| [`vault-memory`](_Agents/skills/vault-memory/) | Refreshes memory from prior sessions and your connectors |
| [`vault-sync`](_Agents/skills/vault-sync/) | Pull → refresh → commit → PR → merge → summary |
| [`weekly-work-log`](_Agents/skills/weekly-work-log/) | Writes the weekly work log from verified activity |
| [`skills-sync`](_Agents/skills/skills-sync/) | Publishes selected skills to a team skills repo |
| [`vault-doctor`](_Agents/skills/vault-doctor/) | Mechanical integrity checks. Read-only, script-backed |
| [`vault-prune`](_Agents/skills/vault-prune/) | Finds slop, duplicates, bloat, stale claims, gaps |
| [`vault-edit`](_Agents/skills/vault-edit/) | Safe CRUD — and what must move with the file |
| [`knowledge-router`](_Agents/skills/knowledge-router/) | Personal vault vs shared team vault |
| [`shared-vault-sync`](_Agents/skills/shared-vault-sync/) | Both directions with a team wiki, drift check first |
| [`shared-vault-promote`](_Agents/skills/shared-vault-promote/) · [`-ingest`](_Agents/skills/shared-vault-ingest/) | The two one-way halves |
| [`secrets`](_Agents/skills/secrets/) | Get, store, rotate, inject — never surfacing a value |
| [`playwright-testing`](_Agents/skills/playwright-testing/) | Real-browser tests for user-visible behavior |
| [`personal-vault`](_Agents/skills/personal-vault/) + 5 siblings | Routes personal material and preserves your voice |

## The rules that make it work

Full text in [`AGENTS.md`](AGENTS.md). The load-bearing ones:

1. **No secret values, ever.** Recording *where* a credential lives is required; pasting the value never is.
2. **No binaries.** Plain text outlives every tool.
3. **Never delete notes or rewrite the user's wording.** Add structure around rough notes.
4. **Respect space boundaries.** Work material stays out of personal spaces.
5. **Never push straight to `main`.** Branch → PR.
6. **Never write a low-confidence inference as fact. Ask.** A wrong claim reads as true for years.
7. **No filler, no editorializing.** Every sentence carries a fact a future reader needs. Padding
   degrades retrieval, which degrades everything else.

Rule 7 has one test: *would a competent reader six weeks from now be worse
off without this?* It applies to an agent's chat reply as much as to a note.

## Two things people get wrong

**Skipping the global instruction bridge.** Run `install-instructions.sh`. Without it your agents only
see these rules when opened *on* this repo — which is not where you work most of the time.

**Never building the memory habit.** The vault only makes chats disposable if facts actually get written
back. The rule is deliberately bounded so it's cheap to follow:
[`_Agents/memory/README.md`](_Agents/memory/README.md) → *When to write memory*.

## Team knowledge

A personal vault is not a team wiki. The companion template for the shared half is
**[`nickdrezza/dev-wiki`](https://github.com/nickdrezza/dev-wiki)** — strict, documentation-heavy, filed
by document type, no PII. Run both and you have a complete personal + team knowledge system.

Three skills manage the boundary: `knowledge-router` decides which base owns a topic, and
`shared-vault-promote` / `shared-vault-ingest` carry material across **as a rewrite, never a paste** —
the team vault stays the source of truth for team facts, and your vault holds the constraint plus a
pointer.

## License

MIT — see [`LICENSE`](LICENSE). Built on the open
[`AGENTS.md`](https://agents.md) and [`SKILL.md`](https://agentskills.io/specification) standards, so
nothing here is locked to one vendor.
