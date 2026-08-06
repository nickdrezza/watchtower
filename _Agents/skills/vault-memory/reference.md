# Vault memory — source adapters

Per-source queries, the concrete tool binding, and a portable fallback for each. The AI-platform
sources are true anywhere; the tracker / email / GitHub / Drive halves assume you've connected those.

Environment facts referenced throughout live in `_Agents/memory/environment.md` (which shell reaches
what) and the matching `_Agents/memory/machines/` profile. **Never hardcode a path here** — that's the
machine profile's job.

## 1. Claude Code sessions

Highest-yield source. Use the **session-mgmt MCP**, not raw files — it's structured and searchable.

```
list_sessions                      # titles + dates; filter to the window
search_session_transcripts         # keyword search across transcripts
get_session                        # one session's detail
```

Two-pass, because transcripts are expensive:

1. `list_sessions` over the window. Titles alone usually reveal which sessions solved something
   durable ("connect to X", "why is Y failing", "set up Z").
2. Only for those, `search_session_transcripts` on terms that signal a durable fact — `gotcha`,
   `read-only`, `expired`, `403`, `401`, `permission`, `credential`, `profile`, `role`, `passphrase`,
   `rebase`, `stale`, `grain`, `fan out`, `cycle`, `WHERE 1=0`.

**Raw fallback** — `<claude-home>/projects/<slug>/*.jsonl`, one directory per project, plus
`<claude-home>/history.jsonl` for prompt history. `<claude-home>` is per-machine; get it from the
machine profile, not from memory of another machine.

⚠️ **Every machine you use holds its own history, and you can only see the one you're on.** Scan it,
then **say in the report which machine you covered** — the others are a known blind spot, not an empty
set. A path that is a symlink or a stale copy of another machine's store (a common WSL case) should be
recorded as such in the machine profile and skipped.

**Per-project memory already exists** at `<claude-home>/projects/<slug>/memory/` with a `MEMORY.md`
index. Treat it as a **first-class source**: anything there that isn't in `_Agents/memory/` is a
candidate, and anything in both should agree. It is the highest-value read in this whole skill —
already-distilled facts, no transcript mining. **Check it every run**; it accumulates silently between
syncs and is invisible to git.

## 2. Codex

`<codex-home>` per machine profile.

| Path | Contains |
|---|---|
| `session_index.jsonl` | Session index — start here; small, one line per session |
| `sessions/`, `archived_sessions/` | Full session transcripts |
| `memories/` + `memories_*.sqlite` | **Codex's own memory store** — already-distilled facts |
| `logs_*.sqlite` | Verbose logs. Last resort; expensive |
| `rules/`, `skills/` | Codex's own instruction layer — useful for spotting drift vs ours |

Read `session_index.jsonl` first and filter by date. `memories/` is the best value per token — it's
Codex having already done this skill's job for itself.

sqlite reads need a client, and `sqlite3` is not guaranteed on every target. Prefer the JSONL and flat
files; if a sqlite read is genuinely needed, use Python's stdlib `sqlite3`.

Other agent stores (Continue, Copilot, Antigravity, Zed) are deliberately **not** scanned — VS
Code-style sqlite with undocumented, brittle schemas. If the user wants one, treat it as new work.

## 3. The tracker

Whatever issue tracker `connectors.md` names as authoritative, via its MCP.

```
assignee = currentUser() AND updated >= "YYYY-MM-DD" ORDER BY updated DESC
project = <KEY> AND updated >= "YYYY-MM-DD" ORDER BY updated DESC
```

⚠️ Request only the fields you need — key, summary, status, resolution, updated, assignee. Pulling
descriptions or `*all` for a long key list blows the token budget. Don't assume `jq` exists; parse
dumped JSON with Python or the shell's native JSON support.

**Fallback:** trackers' MCPs drop in and out. When one is down, reconstruct the work from its
notification emails.

## 4. Email

The email MCP's thread search / message read. Search the window for decisions, data requests, and
stakeholder constraints.

What earns a memory entry: a **constraint or decision** ("filter on `sync_active`", "keep the 8:05am
cron"). What doesn't: the fact that a thread happened.

**Fallback:** ask the user to forward or summarize.

## 5. GitHub

`gh`, from whichever shell holds the authenticated identity — the machine profile says which.

```bash
gh search prs --author @me --merged --merged-at ">=YYYY-MM-DD" --json repository,title,url,closedAt
gh search prs --author @me --state open --json repository,title,url
gh api "repos/<owner>/<repo>/commits?author=<login>&since=YYYY-MM-DDT00:00:00Z" --jq '.[].commit.message'
```

Merged PRs are the strongest evidence of what shipped. Map each to its project block in `projects.md`.
A PR that changed a **gotcha** — a rebase that fixed CI, a grain fix — belongs in the relevant topic
file too, not just `projects.md`.

**Fallback:** `git log` in the local repos the machine profile lists.

## 6. Drive — auto-generated meeting notes

The Drive MCP's recent-files / search / read calls. Meeting-notes docs are usually titled predictably
("Notes by <assistant>", "\<Meeting\> — YYYY/MM/DD").

Extract decisions and follow-ups only. **Never import verbatim.** Personal work context → a vault
meeting note (hand to `watchtower`); team "how it works" → propose for the shared vault via
`knowledge-router`, as a separate approved step.

⚠️ Drive connectors often **cannot edit in place** — each revision is a new doc and URL. When you
create one, tell the user which older ids to trash.

**Fallback:** ask for the folder or link.

## Deciding the target file

| The fact is about… | Goes to |
|---|---|
| This machine, shells, paths, venvs, runner scripts | the matching `machines/` profile |
| What's true on every target, and how to tell them apart | `environment.md` |
| Where a credential lives, or a rotation obligation | `credentials.md` |
| Which connector owns a question, and where each one lies | `connectors.md` |
| Warehouse connection, roles, object topology, modelling gotchas | `warehouse.md` |
| A standing instruction from the user | `working-preferences.md` |
| Project status, tickets, what's next | `projects.md` |

Add a topic file per platform you actually work in — one per system, named for it. A fact that fits two
files goes in the more specific one, with a one-line pointer from the other. **Never duplicate the
body.**

## Cadence

Suits a scheduled run (weekly). When scheduled, still produce the candidate table and **hold for
approval** — never auto-edit memory unattended unless the user has explicitly opted into that.
