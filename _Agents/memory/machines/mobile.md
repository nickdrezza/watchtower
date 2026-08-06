# Profile: phone

**There is no vault on this device** — no clone, no shell, no filesystem.

## What that means

An agent reached from the phone is a **harness with no local checkout**. Everything in this repo has to
be reachable another way or it is unreachable.

| Need | On a laptop | On the phone |
|---|---|---|
| Read this repo | local clone | the git host's web view — the harness needs its own access |
| Load skills | symlink | not discoverable; read `SKILL.md` as a file from the repo |
| Run anything | a shell | **nothing runs.** No `git`, no `ssh`, no `python` |
| Reach live systems | MCP *or* a local CLI | **MCP connectors only** |
| Write a note | edit and commit | dictate into the chat; a laptop session files it later |

## Operating rules here

- **Read-only by default.** If something needs writing, capture it in the conversation and let a laptop
  session file it. Don't invent a commit path that doesn't exist.
- **Anything hands-on is blocked, not broken.** Say it's blocked on the device and what would unblock
  it, rather than trying.
- **Skill auto-discovery does not happen.** Never report a skill unavailable because nothing auto-loaded
  it — `SKILL.md` is plain Markdown.

## Why this profile is worth having

Most of what makes the vault useful assumes a filesystem. Writing that down keeps an agent from
confidently instructing a `bash` command into a client that has no shell.

**The corollary shaped the repo:** the entrance has to work as plain prose read top-to-bottom, because
on this device that's the only way in.
