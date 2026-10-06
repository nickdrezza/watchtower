# The environment

**Pick a machine profile before you run anything.** Most failures here are not bugs — they're a command
written for a different machine. This file holds only what's true *everywhere*.

## 1. Which target am I on?

```bash
uname -s                     # Darwin → macos
                             # MINGW*/MSYS* → Windows, Git Bash side
                             # Linux → WSL, a server, or a container
uname -r | grep -qi microsoft && echo WSL
```

No shell at all — a chat client with no filesystem — means **phone**.

| Target | Tell | Profile |
|---|---|---|
| **Laptop (macOS)** | `Darwin` | [`machines/macos.md`](machines/macos.md) |
| **Laptop (Windows + WSL)** | `MINGW*` or WSL `Linux` | [`machines/windows-wsl.md`](machines/windows-wsl.md) |
| **Phone** | no shell, no filesystem | [`machines/mobile.md`](machines/mobile.md) |

Add a profile per target you actually use. **Read the profile; don't assume the other one.**

## 2. True on every target

- **Never push straight to `main`.** Branch → commit → PR, on every repo.
- **Locations, never values.** Where a credential lives goes in `credentials.md`; the value goes nowhere.
- **Use the harness's session scratchpad**, not `/tmp`, for working files that aren't deliverables.
- **Python is per-repo.** Activate the repo's own venv; never assume a package is present.
- **Verify before asserting.** Environment facts here are stable; anything about code or data drifts.
- **A skill that won't auto-load is not unavailable.** `SKILL.md` is plain Markdown — read it directly.

## 3. What differs, and where it's written down

Never carry one of these across profiles from memory — look it up.

| Differs by machine | Look in |
|---|---|
| Whether the shell is real, wrapped, or absent | the profile |
| Where this repo and your work repos are checked out | the profile |
| Which CLIs are installed | the profile |
| Which git identity you get | the profile |
| Where each harness stores its session history | the profile |

## 4. Cross-machine gotchas

- **A skill that hard-codes a path is a bug.** Skills describe *how*; the path belongs in a profile.
- **Two machines means two states.** A credential migrated on one is not migrated on the other.
- **Symlinks across a Windows↔WSL boundary are fragile.** Use `_Agents/wt install --copy` there.

## 5. Bringing a new target up

1. Clone this repo; read root `README.md` → `AGENTS.md`.
2. `_Agents/wt install` (or `--copy` across a WSL boundary): global instruction stubs, skill links,
   the search hook, and the pre-commit hook. You can run it again at any time.
3. `_Agents/wt doctor` — must report 0 errors.
4. Authenticate your git CLI; set a per-repo `user.email` if the global one is personal.
5. **Write a profile for it** in [`machines/`](machines/README.md) — including what is *not* installed.
   That list is as load-bearing as the paths.
