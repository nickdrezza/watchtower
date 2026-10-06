# How I want agents to work

Standing instructions, not suggestions. **Replace these with your own** — the value of this file is that
it records corrections you've actually had to make, so they only get made once.

## Git and shipping

**Always open a PR. Never commit or push straight to `main`.** Branch → commit → push → open the PR.
Self-merging on a solo repo is expected; skipping the PR is not.

## Worktrees, ports, and the other agents you can't see

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

## Each skill exists once

The vault's skills are the owner's, also work-topic ones. Team skills exist only in the team's skills
repo, often shown as `plugin:skill`; edit them there by PR. Nothing is copied between the two, so no
copy can drift and there is nothing to sync. Ask "who runs this?", not "what is it about?".

## Verify; never fabricate

Every claim in a deliverable traces to a merged PR, a ticket, an email, a command's output, or my own
words. **Never invent specifics** — row counts, metrics, meetings, or "plan pending" work with no
evidence behind it.

## Writing about code

Applies to PR bodies, review comments, commit messages, and how work is reported back in chat.

- **Functional and plain.** A PR body should read in a minute.
- **Lead with what changed and why it matters** — not the investigation that got you there.
- **Keep the numbers that earn trust.** "397 of 404 rows" convinces in one line where prose takes five.
- **Cut the audit trail.** Which greps ran, every candidate eliminated: not valuable. If it mattered
  it's a finding; if it didn't, drop it.
- **Caveats stay in, short.** "Not tested against a real timeout" is one line and must survive.

## Concise — and no AI-slop

- Say it once, plainly. No preamble, no restating the question, no summarizing what you just wrote.
- **Nothing adjacent.** No recommendations or "you might also consider" unless that's the subject.
- **But keep every nuance that changes an outcome** — the gotcha, the exact id, why a decision went that
  way. Cut words, never facts.
- **Objectivity.** A note is a record, not a pitch. No evaluative adjectives about the work, no hedging
  frames, no enthusiasm.

Hard rule 7 in root `AGENTS.md` is the rule. The `watchtower` skill → *How to write here* has the two tests.

## Prod writes

**I prefer to run production DDL myself.** Hand me copy-paste SQL, then verify with a `SELECT`.

## Comment, don't edit

**Propose ticket changes as a comment; leave the original text intact.** When scope shifts, add a
comment pointing at the reframed ticket rather than rewriting the description.

## Reporting

State what actually happened. If tests failed, show the output. If a step was skipped, say which. **Don't
take a subagent's or a tool's summary at face value** — a "0 bugs, all clean" report can be wrong.
