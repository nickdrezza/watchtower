---
type: documentation
title: Watchtower
description: "The guide for a new user: what this vault template is, how to set it up, and how to use it each day."
updated: 2026-10-06
---

# Watchtower

> **A shared brain for your AI agents.** One plain-Markdown vault that every agent reads as memory, so
> your chats become disposable and nothing gets explained twice.

This is a **template** for a private, text-first Obsidian vault: your notes for work, personal life,
and career, and the memory for each AI agent that works with you. Claude Code, Codex, Cursor, Gemini
CLI, Copilot, and Antigravity read the same skills and memory, so they operate the same way. There is
no manager agent: a chat can stop at any time, because the durable facts are in the vault. Agents read
[`AGENTS.md`](AGENTS.md); this page is for people. **Keep your copy private.**

## Layout

```text
AGENTS.md            agent instructions; CLAUDE.md, GEMINI.md, copilot-instructions.md point to it
README.md            this guide, and the Obsidian home page
Spaces/
  Personal/          personal life
  Work/              work for your current employer (tag ACME)
  Career/            resume and future work
Concepts/            one note for each durable subject; the targets of topic/* tags
_Agents/             the agent layer (.agents is a symlink to it)
  skills/            shared skills, one folder for each skill
  memory/            facts that are true in all spaces: machines/, working-preferences/
  templates/         the starter files for a new skill
  archive/           old agent-layer pages, kept as history
  tags.md            the tag registry
  placeholders.md    the stand-in values to replace after setup
  wt                 the vault tool: search, doctor, install, index
_Templates/          note templates for each space
Inbox/               Raw Dumps/ and Processed/: material with no home yet
```

A space keeps its own `memory/` and `skills/`. A **skill** tells an agent how to do a task. **Memory**
tells it what is true about your systems and machines. A skill that hard-codes an account ID or a path
does the job of memory.

## Spaces

- [Personal](Spaces/Personal/index.md) — diary, memories, reflections, people, places, and pets. Space
  rules: [Personal Vault Guide](<Spaces/Personal/Personal Vault Guide.md>).
- [Work](Spaces/Work/index.md) — projects, people, work logs, meeting notes, reference, and dashboards.
  Space rules: [`Spaces/Work/AGENTS.md`](Spaces/Work/AGENTS.md).
- [Career](Spaces/Career/index.md) — resume, career plans, and material for future work.

Work material stays in `Spaces/Work/`. Material with no clear home goes to `Inbox/Processed/`.

## Set up

1. Make your own private repo from the template, then clone it. Any path is correct; record it in the
   machine profile (step 5).
   ```bash
   gh repo create my-vault --template <you>/watchtower --private --clone
   ```
2. **Fast path:** open the repo in any agent and say "set me up". The
   [`bootstrap`](_Agents/skills/bootstrap/SKILL.md) skill does steps 3–7 with you, removes the example
   content, and teaches the operating model.
3. Run `_Agents/wt install --dry-run` to see the changes, then `_Agents/wt install` (safe to run
   again). It writes the stub `_Agents/global-instructions.md` into each harness's global instruction
   file (`~/.claude/CLAUDE.md`, `~/.codex/AGENTS.md`, `~/.gemini/GEMINI.md`, `~/.cursor/AGENTS.md`;
   a hand-written file is kept unless you add `--force`), links each skill into `~/.agents/skills/`
   and `~/.claude/skills/`, adds the Claude Code search hook (`wt search --hook` on each prompt), and
   adds a git pre-commit hook that runs `wt doctor --errors-only`.
4. Test it. Open a new chat in a folder that is not this repo, and ask: "What are the hard rules of my
   vault, and where is my agent memory?" If the agent does not know, the install did not reach that
   harness. Make sure that its config folder exists, then run `wt install` again.
5. Copy the nearest profile in `_Agents/memory/machines/`: paths, shell, CLIs installed and not
   installed, `gh` identity, git author email. Add it to `_Agents/memory/machines/index.md`.
6. Record where each credential is in `Spaces/Work/memory/credentials/`, never the value.
7. Connect your MCP connectors; record which one owns which data in `Spaces/Work/memory/connectors/`.
8. Replace the placeholders: your handle and vault name, then the employer tag `ACME`. The list and the
   grep checks are in [`_Agents/placeholders.md`](_Agents/placeholders.md). Add your account names to
   `users` in `_Agents/wt.json`.
9. Optional: open the repo as an Obsidian vault. Nothing needs Obsidian.

Where each harness reads skills and instructions:

| Harness | Skills | Instructions |
|---|---|---|
| Claude Code | `~/.claude/skills/`, `.claude/skills/` | `CLAUDE.md` (stub); it also reads `AGENTS.md` |
| Codex, Cursor, Copilot | `~/.agents/skills/`, `.agents/skills/` | `AGENTS.md`; Copilot also reads `.github/copilot-instructions.md` (stub) |
| Gemini CLI, Antigravity | `~/.agents/skills/`, `.agents/skills/` | `AGENTS.md` and `GEMINI.md` (stub; `GEMINI.md` wins on a conflict) |
| Old Cursor, Windsurf | — | `.cursor/rules/`, `.windsurf/rules/`; new versions read `AGENTS.md` |

`.agents` is a committed symlink to `_Agents/` (Obsidian hides dot-folders). If a harness does not
find a skill, tell the agent to read `_Agents/skills/<name>/SKILL.md`. It is plain Markdown.

**Windows and WSL:** a WSL symlink does not resolve for a Windows app (Cursor.exe, Antigravity.exe).
For those, use `_Agents/wt install --copy`, and run it again after each skill change. For
tool-specific variants of skills, rules, or MCP configs from one source, look at `rulesync`.

## Daily use

- **Say what you want.** Do not paste context or summarize the last chat. The agent searches the
  vault, old sessions, and connectors first. If it asks you to explain a thing that it can find, that
  is a bug: usually a missing memory page, or a harness that `wt install` did not reach.
- **Dump raw material. Do not sort it first.** Put it in the chat or in `Inbox/Raw Dumps/` and say
  "file these notes". The agent keeps your words and adds the structure.
- **Use voice** for debriefs, work-log material, and personal capture. Speech recognition changes
  identifiers (ticket keys, paths, SQL, URLs) and the result looks correct: speak the prose, paste the
  exact strings, never speak a credential. On the phone, dictate; a laptop session files it later.
- **Let chats end.** A new chat loses nothing that is in memory. The test for a fact: "Will a new agent
  do the job worse in six weeks without this?" If yes, say "save that".
- **Review agent writes in the PR.** The diff is the preview; ask for a chat preview only when you want
  one. Nothing goes to `main` without a PR.
- **Sync** with "sync my vault": `vault-sync` pulls, updates the log and memory, and ships a PR.
- **Use few subagents**, only for independent work, never to own a topic. **One fact, one home.**
  Verify a report before you trust it, also a report from an agent.

### When something goes wrong

| Problem | Usual cause and fix |
|---|---|
| The agent asks you to explain known context | `wt install` did not reach that harness. Run it again. |
| The agent says that a skill is not available | It did not find the skill. Tell it to read `_Agents/skills/<name>/SKILL.md`. |
| The agent states a wrong fact with confidence | A stale memory page. Fix the page, not only the chat. |
| The agent asks permission for each step | See `_Agents/memory/working-preferences/Decide vs ask.md`: decide reversible details, ask about irreversible ones. |
| Commands fail with wrong paths | Wrong machine profile. Start at `_Agents/memory/machines/index.md`. |

## Skills

| Skill | What it does |
|---|---|
| [`watchtower`](_Agents/skills/watchtower/SKILL.md) | The vault rules: layout, writing, tags, filing, adding a skill. Load it before a vault write |
| [`bootstrap`](_Agents/skills/bootstrap/SKILL.md) | Sets up a new user or machine, and teaches the operating model |
| [`vault-memory`](_Agents/skills/vault-memory/SKILL.md) | Updates memory from prior sessions and your connectors |
| [`vault-sync`](_Agents/skills/vault-sync/SKILL.md) | Pull, update, commit, PR, merge, summary |
| [`weekly-work-log`](Spaces/Work/skills/weekly-work-log/SKILL.md) | Writes the weekly work log from verified activity |
| [`vault-doctor`](_Agents/skills/vault-doctor/SKILL.md) | Mechanical checks, backed by `wt doctor`. Read-only |
| [`vault-prune`](_Agents/skills/vault-prune/SKILL.md) | Finds slop, duplicates, bloat, stale claims, and gaps |
| [`vault-edit`](_Agents/skills/vault-edit/SKILL.md) | Create, move, rename, merge, or delete notes without breaking links |
| [`shared-vault`](Spaces/Work/skills/shared-vault/SKILL.md) | Moves vault knowledge into a team wiki as a PR |
| [`secrets`](_Agents/skills/secrets/SKILL.md) | Gets, stores, rotates, and injects credentials; never shows a value |
| [`playwright-testing`](_Agents/skills/playwright-testing/SKILL.md) | Real-browser tests for user-visible behavior |
| [`personal`](Spaces/Personal/skills/personal/SKILL.md) | Files personal material and keeps your voice |

The full index, which `wt doctor` checks, is [`_Agents/README.md`](_Agents/README.md). Skills in this
vault are yours. Team skills live only in the team's skills repo and are never copied in. A team wiki is
a separate repo; the `shared-vault` skill moves material there as a rewrite, never a paste.

MIT licensed. Built on the open [`AGENTS.md`](https://agents.md) and
[`SKILL.md`](https://agentskills.io/specification) standards, so nothing here is locked to one vendor.

## Moving to Isomorphic

The vault is a valid [Isomorphic](https://github.com/isomorphic-team/isomorphic-app) brain: `validate`
reports 0 broken links (checked against Isomorphic `a99ae2c`).

- To check again: in an Isomorphic checkout, run `pnpm try <copy of this vault>` (it commits into the
  folder, so use a copy), then call `validate` from an MCP client.
- Each space can become its own brain: its `index.md`, `AGENTS.md`, `memory/`, `skills/`, and `source/`
  are already in place. `_Agents/` becomes shared through cross-brain search.
- `.isomorphic.json` sets which folders are content, source, and system. `wt doctor` reports the links
  Isomorphic cannot follow (`ambiguous-link`, `link-to-non-page`); `--fix` repairs them.
