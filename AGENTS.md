# AGENTS.md — the vault

Always-on instructions for every AI agent working with this vault's owner. This file is intentionally
small; the vault holds the rest as searchable skills, memory, notes, and prior-session pointers.

## Context loading

1. **Start with the request and this file. Do not preload the vault.**
2. **Search before implementing.** When the request may depend on prior context, run:
   ```bash
   _Agents/wt search <2-5 specific nouns or phrases from the request>
   ```
   Read only relevant results. If the first terms miss, try safe synonyms, identifiers, project names,
   and obvious typo corrections before asking the user.
3. **Load skills on demand.** Read a skill's complete `SKILL.md` when the request names it or matches
   its description. Load `_Agents/skills/watchtower/SKILL.md` only for vault work: reading, filing,
   editing, restructuring, governing, or answering from this vault.
   **When a skill name exists twice, this repo's copy wins — always.** Skills published from here to a
   marketplace or a shared repo come back as installed copies, so a name can appear both unprefixed
   (`my-skill` — this repo, deployed to `~/.agents/skills`) and prefixed (`some-plugin:my-skill`).
   **Invoke the unprefixed one.** This repo is the source; a prefixed copy is a build artifact that may
   be behind or edited by someone else. Use a `plugin:skill` name only when no unprefixed skill of that
   name exists. Ledger of what is published and currently duplicated: `_Docs/Skill Exports.md`.
4. **Load operational context only when the action needs it:**
   - Shell commands or machine-dependent paths/tooling → `_Agents/memory/environment.md`, then exactly
     one matching `_Agents/memory/machines/` profile.
   - Authentication, secret locations, profiles, or connection failures →
     `_Agents/memory/credentials.md` plus the relevant platform memory.
   - Live external state → the authoritative connector named in `_Agents/memory/connectors.md`.
   - Prior decisions or unfinished work → the relevant note/memory first, then prior sessions.
5. **Pointers are not content.** Search results and indexes tell you what to open; they do not require
   reading every linked file.

Order: request → this bootstrap → search → matching skill/context → action. Read
`_Agents/docs/operating-model.md` only when changing agent governance or retrieval behavior.

## Hard rules

1. **No secret values.** Never put keys, passwords, tokens, private keys, `.env` contents, or OAuth
   secrets in notes, code blocks, logs, commits, or chat. Recording locations is allowed.
2. **No binaries in the vault.** No images, PDFs, private keys, `.env`, plugin bundles, JS, or CSS.
   Extract PDFs to Markdown; catalogue removed images in `_Docs/Image Descriptions.md`.
3. **Preserve the user's wording and data.** Never delete notes or rewrite rough material into generic
   prose. Add structure around it; explicit consolidation must carry the original wording forward.
4. **Respect space boundaries.** Employer-specific material stays out of personal and future-work
   spaces.
5. **Never push straight to `main`.** Use a branch and PR. Do not publish, push, open a PR, or send
   external communication without explicit authorization for that external action.
6. **Never write a low-confidence inference as fact.** Verify from evidence; if evidence cannot settle
   it, ask one concrete batched question before writing.
7. **No filler or editorializing.** Every sentence must carry a fact a future reader needs. Report
   what changed, what was verified, and what was deliberately left out.
8. **Build the smallest maintainable change that fully solves the request.** Keep scope, machinery,
   documentation, and testing proportional to behavior and risk.

## Working model

- **One brain, many disposable agents.** The vault is shared memory; chats and agents are not.
- **Fetch before asking.** Search this vault, then relevant prior sessions, then live connectors.
- **Decide reversible, conventional, evidence-answerable details.** Ask about irreversible, expensive,
  unrecoverable, or taste-dependent choices.
- **Durable facts live here; live state does not.** Query tickets, row counts, schedules, and current
  status from their source instead of caching them in memory.
- **Verify before reporting.** Use `_Agents/docs/verification.md` when completion criteria are unclear.

## Vault writes

The full filing, writing, tagging, template, and structural rules live in the matching skill. For any
vault write, load `watchtower` and any operation skill such as `vault-edit` first.

Default gate: show a `vault preview` containing every destination and the exact proposed content or
diff, then wait for approval. A clear current-turn instruction such as `full perms`, `skip the
preview`, `write it directly`, or `save it without asking` bypasses only that preview gate. It never
waives the hard rules. A memory fast path is defined in `_Agents/memory/README.md`.

Structural edits must update links, indexes, frontmatter, and tags together. `Maps/Tag Registry.md` is
the tag authority. Employer-specific material uses the configured employer tag; graph scope uses
`work` and `personal`. Verify vault edits with the `vault-doctor` skill.

## Git and completion

- Fetch before branching when remote state matters; stage only intended files, never `git add -A`.
- Preserve unrelated user changes in a dirty tree.
- Secret-scan the diff before committing.
- Use the matching machine profile for paths, shells, installed tools, and git identity.
- Do not treat focused tests as proof that an external deployment or live system changed.

## Page conventions

These apply to new and moved pages. Existing pages change in later redesign steps.
Obsidian, GitHub, and Isomorphic read the same files.

- **Frontmatter:** `type`, `description`, `updated`. Add `title` only when it is different from the
  file name. A folder note does not need `type`.
- **Folder notes:** a folder's overview page is `<folder>/index.md`. In Obsidian, set the folder-notes
  plugin to use the name `index`.
- **Titles:** each content page has a unique title. `index.md` and `SKILL.md` are exempt.
- **Listings:** use an `okf-view` block, not a hand-kept list. `_Agents/wt index` writes the cached
  snapshot under it, so Obsidian and GitHub show the list. Isomorphic computes it live.
- **Paths:** `.isomorphic.json` declares which folders are content and which are system.
- **Plugin files** (`.excalidraw.md`, `.base`) are extras. They are never the only index of anything.
- **Moves and renames:** use `git mv`, then `_Agents/wt doctor --fix`. Merge only with 0 broken links.

## Entry points

- Skills: `_Agents/skills/<name>/SKILL.md`
- Memory index: `_Agents/memory/README.md`
- Agent-layer map: `_Agents/README.md`
- Vault structure and indexes: `_Agents/skills/watchtower/reference.md`, `Maps/`
- Skill authoring: `_Agents/CONVENTIONS.md`
- Platform/harness paths: `_Agents/docs/platforms.md`
