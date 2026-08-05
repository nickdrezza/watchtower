# How I want agents to work

Standing instructions, not suggestions. **Replace these with your own** — the value of this file is that
it records corrections you've actually had to make, so they only get made once.

## Git and shipping

**Always open a PR. Never commit or push straight to `main`.** Branch → commit → push → open the PR.
Self-merging on a solo repo is expected; skipping the PR is not.

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

Hard rule 7 in root `AGENTS.md` carries the banned-patterns table and the test.

## Prod writes

**I prefer to run production DDL myself.** Hand me copy-paste SQL, then verify with a `SELECT`.

## Comment, don't edit

**Propose ticket changes as a comment; leave the original text intact.** When scope shifts, add a
comment pointing at the reframed ticket rather than rewriting the description.

## Reporting

State what actually happened. If tests failed, show the output. If a step was skipped, say which. **Don't
take a subagent's or a tool's summary at face value** — a "0 bugs, all clean" report can be wrong.
