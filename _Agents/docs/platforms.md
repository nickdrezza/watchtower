# Platform path matrix

Where each tool reads **skills** and **always-on instructions** from. Use this to know where
`_Agents/wt install` links skills, and which instruction file to point at `AGENTS.md`.

## Skills (folder-per-skill `SKILL.md`)

| Tool | Global skills path | Project skills path | Notes |
|---|---|---|---|
| **Claude Code** | `~/.claude/skills/` | `.claude/skills/` | The holdout — does **not** read `.agents/skills/`. `wt install` links each skill there. |
| **OpenAI Codex** | `~/.agents/skills/` | `.agents/skills/` | Universal location. |
| **Gemini CLI** | `~/.agents/skills/` | `.agents/skills/` | `.agents/` preferred over `.gemini/skills/`. |
| **Cursor** | `~/.agents/skills/` | `.agents/skills/` | Native SKILL.md support added 2026. |
| **GitHub Copilot** | `~/.agents/skills/` | `.agents/skills/` | Agent mode. |
| **Google Antigravity** | `~/.agents/skills/` | `.agents/skills/` | Reads the universal location. |

⚠️ **The real directory here is `_Agents/`, and `.agents` is a committed symlink to it.** Obsidian
skips dot-folders, so the agent layer had to lose the dot to be readable in the vault; the symlink
keeps the universal path every tool above looks for. Both spellings resolve to the same files.

**Takeaway:** `.agents/skills/` (project) and `~/.agents/skills/` (global) cover nearly everything;
Claude Code needs its own `.claude/skills/` or `~/.claude/skills/`.
`_Agents/wt install` links each skill into both global paths.

Because this repo's canonical skills path **is** `.agents/skills/` (via that symlink), every harness except Claude Code
works with zero setup when opened here.

## Always-on instructions (`AGENTS.md` standard)

| Tool | File it reads | Strategy |
|---|---|---|
| **AGENTS.md-native** (Codex, Cursor, Copilot, Gemini, Windsurf, Antigravity, Claude Code¹) | `AGENTS.md` | Author here directly. |
| **Claude Code** | `CLAUDE.md` | Reads `AGENTS.md` as of spring 2026; keep `CLAUDE.md` as a stub → `See AGENTS.md`. |
| **Gemini / Antigravity** | `GEMINI.md` | `GEMINI.md` wins over `AGENTS.md` on conflict; keep it a stub. |
| **Copilot** | `.github/copilot-instructions.md` | Stub → `AGENTS.md`. |
| **Cursor (legacy)** | `.cursor/rules/*.mdc`, `.cursorrules` | Modern Cursor reads `AGENTS.md`; only needed for old versions. |
| **Windsurf** | `.windsurf/rules/*.md`, `.windsurfrules` | Reads `AGENTS.md`; stub the rest. |

¹ Claude Code added `AGENTS.md` support in spring 2026.

> This repo applies the mapping above to itself: [`../../AGENTS.md`](../../AGENTS.md) is
> authoritative, and `CLAUDE.md`, `GEMINI.md`, and `.github/copilot-instructions.md` at the repo
> root are stubs pointing at it. That's what makes every harness behave the same here — there is
> exactly one set of rules and one canonical skills path.

Sources: code.claude.com/docs/en/skills · agentskills.io/specification · agents.md ·
developers.openai.com/codex/skills · geminicli.com/docs/cli/skills
