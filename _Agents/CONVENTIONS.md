# Skill authoring conventions

The spec every skill under `_Agents/skills/` follows. Built on the open
[Agent Skills specification](https://agentskills.io/specification) so skills stay portable across
tools. If you only read one thing: **`name` + `description` + a clear body are the only things that
have to be right** — everything else is optional.

## Anatomy of a skill

```
_Agents/skills/
└── my-skill/
    ├── SKILL.md        # required — the entrypoint
    ├── reference.md    # optional — deep detail, loaded only when SKILL.md points to it
    ├── examples.md     # optional — worked examples
    └── scripts/        # optional — executable helpers (run, not read into context)
        └── helper.py
```

- **Folder name = skill name = `name` frontmatter.** All lowercase-hyphenated, e.g. `pdf-extract`.
- One skill per folder. No nesting skills inside skills.

## SKILL.md frontmatter

### Required (portable — every tool reads these)

```yaml
---
name: my-skill                 # lowercase-hyphenated, matches the folder
description: >                  # what it does AND when to use it (this is the trigger!)
  Extracts tables from PDF files into CSV. Use when the user uploads a PDF and asks to
  pull tabular data, convert a PDF table to a spreadsheet, or scrape figures from a report.
---
```

**Writing a good `description`** — this single field decides whether any platform loads the skill:
- Lead with the capability, then the triggers ("Use when…", "Trigger on phrases like…").
- Include concrete trigger words a user would actually type.
- Be specific enough to *not* fire on unrelated requests.
- Keep it tight. Claude Code caps the combined description listing (~1,536 chars per skill budget),
  so don't write a paragraph where two sentences do.

### Optional (tool-specific — safe to include, ignored elsewhere)

These are mostly Claude Code extensions. Include them when useful; never let a skill *break* without
them:

```yaml
allowed-tools: [Read, Write, Bash]   # Claude Code: restrict tools
model: claude-opus-4-8                # Claude Code: pin a model
user-invocable: true                  # Claude Code: expose as /my-skill
argument-hint: "<file.pdf>"           # Claude Code: arg hint for slash use
```

Document any reliance on these in the body so a reader on another platform knows the fallback.

## The body

- Markdown after the frontmatter. Write it as instructions to the agent.
- **Lean:** aim for under ~500 lines. If it's growing, split detail into `reference.md` and link to
  it ("For the full field mapping, read `reference.md`"). This is *progressive disclosure* — keep
  the always-loaded part small and pull in detail on demand.
- Reference sibling files by relative path. Put runnable code in `scripts/` and tell the agent to
  execute it rather than pasting large code blocks inline.
- Prefer portable tooling (POSIX shell, python3, common CLIs). Call out any tool-specific step.

## Adding a new skill to this repo — the full flow

1. **Decide it's a skill, not memory.** A skill is *how to perform a task*; `_Agents/memory/` is *what
   is true about this environment*. If what you're writing is mostly facts (ids, paths, credential
   locations, cron expressions), it belongs in memory. A skill may well need both — write the procedure
   here and point at the memory file for the facts.
2. **Scaffold it.**

   ```bash
   _Agents/scripts/new-skill.sh <skill-name>
   ```

   It's a portable bash script — `cp -r` plus a `sed`-to-temp-file (a bare `sed -i` is GNU-only and
   fails on macOS, so don't reintroduce one). On the Mac, run it directly. On the Windows machine run
   it from **WSL** (`wsl.exe -d ubuntu -e bash -lc '...'`, quoting the vault path) or from Git Bash — the
   repo is on the Windows filesystem, so either can reach it. See
   `_Agents/memory/machines/` for the target you're on.
3. **Write it**, starting with the `description` — that field is the trigger. Then the body, per the
   sections above.
4. **Register it in the three index tables.** These are hand-maintained; a new skill is invisible to a
   reader (and to an agent that didn't auto-discover it) until they're updated. `vault-doctor` checks
   all three and fails if any one is missing the skill — none of them is optional:
   - `_Agents/skills/watchtower/SKILL.md` → the skills table under "The agent layer"
   - `_Agents/README.md` → the Skills table
   - `../_Docs/Skills Repo.md` → "The skills" table (the vault-visible index)
5. **Refresh the Claude Code mirror**, or Claude Code won't see the new skill — `.claude/skills/` is a
   **copy**, not a live link:

   ```bash
   _Agents/scripts/install-skills.sh --here
   ```

   (Other harnesses read `_Agents/skills/` directly and need nothing.)
6. **Run the checklist below, then branch + PR.** Never push to `main`.

## Checklist before committing a skill

- [ ] Folder name, `name`, lowercase-hyphenated, all match.
- [ ] `description` states what it does *and* when to use it, with real trigger phrases.
- [ ] Body is lean; heavy detail moved to `reference.md` / `scripts/`.
- [ ] No hard dependency on a single tool's proprietary feature (or fallback documented).
- [ ] Works when dropped into `~/.agents/skills/` unchanged (the universal location).
- [ ] If it touches this repo's notes, it defers to the `watchtower` skill's hard rules rather
      than restating (or contradicting) them.
- [ ] No environment facts hard-coded in the body — account ids, file paths, cron expressions, roles,
      and credential locations belong in `_Agents/memory/`. Point at the memory file instead.
- [ ] **No secret values.** Same hard rule as the rest of this repo: reference where a credential lives
      (path, env-var name, your secret manager item), never the value. See `_Agents/memory/credentials.md`.
- [ ] **If it writes anything, it asks first.** A skill that produces a note, doc, log, ticket, or wiki
      page must tell the agent to verify what's checkable, batch the rest into one multiple-choice
      question set *before* the write, and state its understanding concretely enough to be
      contradicted. Root `AGENTS.md` → **Ask instead of assuming** is the rule; don't restate it, point
      at it and say what the questions are for this task.
- [ ] Registered in the three index tables (step 4 above), and the `.claude/skills/` mirror refreshed.
