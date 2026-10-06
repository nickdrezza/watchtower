---
type: memory
title: "Worktrees, ports, and the other agents you can't see"
description: "Rules for parallel agents: keep the primary clone on main, use one worktree per branch, check port owners, and remove worktrees at merge."
updated: 2026-08-06
---

# Worktrees, ports, and the other agents you can't see


Several agents run at once on different branches of the same repo, none aware of the others. There is
no coordination channel between them, so every rule here is one an agent can check **alone, from the
outside**. Follow them even when nothing looks contended — by the time a collision is visible, an
agent has already reported on the wrong code.

**The primary clone stays on the default branch and never runs a server.** It is the reference copy —
what `origin/main` actually looks like. Don't switch its branch, don't start a dev server in it, don't
leave it dirty. Other agents need that to be true to diff against.

**One worktree per branch, as a sibling directory:**

```bash
git -C <repo> worktree add ../<repo>-<slug> -b <branch>
```

Name `<slug>` for the work, not the ticket number — the directory name is how the next agent learns
what is in flight.

**Before starting any server, find out who already holds the port.** Never assume it's free, and never
assume the thing answering on it is yours:

```bash
lsof -nP -iTCP:<port> -sTCP:LISTEN        # taken?
lsof -a -p <pid> -d cwd -Fn | tail -1     # which worktree owns it
```

Occupied means another agent is mid-task. **Don't kill it.** Either read from it knowing it serves
*that* worktree's code, or bind yours elsewhere and accept that every hardcoded reference still points
at the original.

**A silently shifted port is worse than a failed start.** Most dev servers take the next free port and
only warn — while the MCP config, the docs, and any registered callback URL still name the original.
An agent then reads a different worktree's code and reports on it with full confidence. If the port
you need is taken, say so and stop; never drift onto another one quietly.

**Anything else keyed to that port is a shared resource too.** A dev server that registers itself
somewhere — a tunnel, a webhook, a vendor deployment slug — binds *one* identity to *one* URL. Copying
the env file into a second worktree makes both fight over it, and the last one to start wins silently.
Give each worktree its own registration, or accept that only one at a time can be live. Record which
in the platform's memory file.

**Clean up in the same step as the merge**, not later:

```bash
git -C <repo> worktree remove <path> && git -C <repo> branch -D <branch>
```

A merged branch's worktree is a trap as much as it is disk: a later agent finds code that is neither
`main` nor in flight and works from it. `git worktree prune` will not help — it only clears entries
whose directory is already gone.
