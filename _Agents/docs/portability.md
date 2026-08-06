# The portability model

## Principle

Author each skill **once**, to the open [SKILL.md spec](https://agentskills.io/specification), with
only `name` + `description` + body as load-bearing. Every major tool understands that core. Then keep
them at the **one universal location** — `.agents/skills/` in a project, `~/.agents/skills/`
globally. (Here `.agents` is a symlink to the real `_Agents/`, so Obsidian can read the layer; the
universal path still resolves.)

```
        .agents/skills/  (this repo = single source of truth, via _Agents/)
                    │
                    ├── read in place, at project level, with zero setup
                    │   (Codex, Gemini CLI, Cursor, Antigravity, Copilot)
                    │
                    ├── _Agents/scripts/install-skills.sh --here
                    │   -> ./.claude/skills   (Claude Code, this repo)
                    │
                    └── _Agents/scripts/install-skills.sh
                        -> ~/.agents/skills + ~/.claude/skills  (global, any project)
```

We ship the universal format only. Claude Code reads `.claude/skills/`, so it gets a mirror — no
Claude-specific build step and no second copy of a skill's text.

**Worst case is still fine:** a harness that discovers nothing can be told to read
`_Agents/skills/<name>/SKILL.md` directly. That's what the root `AGENTS.md` instructs, so "the agent
didn't know how to connect here but did over there" can't happen.

## Two ways to deploy

### 1. Symlink (simplest, Unix/WSL-native)

```bash
_Agents/scripts/install-skills.sh           # ~/.agents/skills + ~/.claude/skills
```

Edits to the repo are instantly live everywhere. **Caveat:** symlinks across the **Windows↔WSL
boundary are fragile** — a symlink created in WSL won't resolve for a Windows-side app (Cursor.exe,
Antigravity.exe). If all your tools run inside WSL, symlinks are great. If some run on Windows, use
copy mode.

### 2. Copy (robust on Windows)

`_Agents/scripts/install-skills.sh --copy` copies the tree instead of linking. You re-run it after
changes, but it works regardless of OS boundary. This is the recommended default on this Windows/WSL
machine — and `--here` always copies for the same reason.

## When to graduate to `rulesync`

For just deploying skills, `install-skills.sh` is enough. Reach for
[`rulesync`](https://github.com/dyoshikawa/rulesync) when you want to:

- Generate **per-tool frontmatter** variants from one source (e.g. inject Claude-only fields).
- Also manage **rules, subagents, MCP configs, and slash commands** from one place — not just skills.
- Target 40+ tools without maintaining path lists yourself.

```bash
npx rulesync generate --targets claudecode,codex,cursor,copilot
```

It expects a `.rulesync/` source layout; if we adopt it, we'd add a thin mapping from
`_Agents/skills/` into `.rulesync/` rather than rewrite the skills. [`ruler`](https://github.com/intellectronica/ruler)
is the higher-starred alternative but is more rules-focused (less skill-aware).

## Why not pick one tool's native format as canonical?

Because the whole point is tool independence. The open SKILL.md spec is the lowest common
denominator that every tool already reads, so canonicalizing on it means *zero* conversion for the
common case and a clean fallback (symlink/copy) when a tool diverges.
