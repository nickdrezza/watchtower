# Claude Instructions

**Read [`AGENTS.md`](AGENTS.md).** It is the single source of instructions for every agent working
in this repo and applies to you unchanged.

Load skills and vault context only when the request matches them; `AGENTS.md` defines routing.

Claude-Code-specific notes (everything else is in `AGENTS.md`):

- Skills are canonical at `_Agents/skills/`. Claude Code reads `.claude/skills/`, so either run
  `_Agents/scripts/install-skills.sh --here` once to mirror them into this repo, or just read
  `_Agents/skills/<name>/SKILL.md` directly — they're plain Markdown. Never report a skill as
  unavailable because it wasn't auto-discovered.
- `.claude/skills/` is gitignored (it's a generated mirror). Edit the files under `_Agents/skills/`.
- Run `git`/`gh` through `wsl.exe -d ubuntu -e bash -lc '...'`; see `AGENTS.md` → Git for the
  quoting and `--body-file` gotchas.
