# Claude Instructions

**Read [`AGENTS.md`](AGENTS.md).** It is the single source of instructions for every agent working
in this repo and applies to you unchanged.

Load skills and vault context only when the request matches them; `AGENTS.md` defines routing.

Claude-Code-specific notes (everything else is in `AGENTS.md`):

- Skills are canonical at `_Agents/skills/`. `_Agents/wt install` links each one into
  `~/.claude/skills/`. Without it, read `_Agents/skills/<name>/SKILL.md` directly: it is plain
  Markdown. Never report a skill as unavailable because it was not auto-discovered.
- On Windows, run `git`/`gh` through WSL. `_Agents/memory/machines/windows-wsl.md` has the quoting
  and `--body-file` rules.
