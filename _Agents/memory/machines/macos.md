# Profile: macOS laptop

Example profile — replace the values with yours.

| Fact | Value |
|---|---|
| User | `<you>` |
| This repo | `~/Development/watchtower` |
| Work repos | `~/Development/<repo>` |
| Shell | Real. Bash and zsh both work; no wrapper needed |
| Git identity | One identity, over SSH. `git push` works from any clone |
| Secret manager CLI | `~/.secrets/` — CLI not on `PATH`, call it by full path |
| Harness history | Claude Code `~/.claude/`, Codex `~/.codex/` |

## Installed

`git`, `gh`, `python3`, `node`, the secret-manager CLI.

## Deliberately not installed

The cloud provider CLI, the warehouse CLI, the transform CLI. **Any skill that needs one of these cannot
run on this machine** — say so up front rather than discovering it mid-task.

## Notes

- `~/.claude/CLAUDE.md` and `~/.codex/AGENTS.md` point at this repo, written by
  `_Agents/wt install`. Re-run it after a fresh install.
- Skills are linked one per skill: `~/.claude/skills/<name>` and `~/.agents/skills/<name>` → this repo's
  `_Agents/skills/<name>`. Edits are live immediately.
