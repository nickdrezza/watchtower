# Gemini Instructions

**Read [`AGENTS.md`](AGENTS.md).** It is the single source of instructions for every agent working
in this repo and applies to you unchanged. (`GEMINI.md` takes precedence over `AGENTS.md` on
conflict, so this file deliberately adds nothing of its own.)

Load skills and vault context only when the request matches them; `AGENTS.md` defines routing.

Gemini CLI and Antigravity read skills from `_Agents/skills/` natively, so no setup is needed.
