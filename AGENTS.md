# AGENTS.md — the vault

Instructions for every AI agent that works with this vault's owner. Keep this file short. The vault
holds the rest: skills, memory, and notes that you search and load when a task needs them.

## Load context

1. Start with the request and this file. Do not preload the vault.
2. Search before you act: `_Agents/wt search <2-5 specific terms>`. Open only the relevant results. If
   nothing matches, try synonyms, identifiers, and project names before you ask the user.
3. Load a skill when the request names it or matches its description. Vault skills are the owner's and
   live in `_Agents/skills/` and `Spaces/<Name>/skills/`. Team skills live only in the team's skills
   repo (often shown as `plugin:skill`); change them there by PR, never here. When you use a team
   skill: use the data tool that is connected, treat data imported into the skill as a dated snapshot
   and verify it live, draft before you publish, never get around a guardrail by switching roles or
   data sources, and never create infrastructure automatically.
4. Load operational memory only when the action needs it:
   - Shell commands or machine paths → `_Agents/memory/machines/index.md`, then one profile.
   - Credentials or connection failures → `Spaces/Work/memory/credentials/`.
   - Live state (tickets, counts, schedules) → the connector named in
     `Spaces/Work/memory/connectors/`. Never cache live state in memory.
5. A search result or index is a pointer. Open what you need, not everything it links.

How the user wants agents to work — evidence, decide vs ask, reporting, testing — is in
`_Agents/memory/working-preferences/`. Read the matching page when a task needs it.

## Hard rules

1. **No secret values.** Never put keys, passwords, tokens, private keys, `.env` contents, or OAuth
   secrets in notes, code, logs, commits, or chat. Record only where a secret lives.
2. **No binaries in the vault.** No images, PDFs, keys, `.env`, plugin bundles, JS, or CSS. Extract PDFs
   to Markdown. Record removed images in `_Agents/image-descriptions.md`.
3. **Keep the user's wording and data.** Never delete notes or rewrite rough material into generic
   prose. Add structure around it. A merge carries the original wording forward.
4. **Keep space boundaries.** Employer material stays out of the personal and career spaces.
5. **Never push to `main`.** Work on a branch and open a PR. Do not publish, message, or change
   another repo or system unless the user asks for that action.
6. **Never write a low-confidence inference as fact.** Verify from evidence. If evidence cannot settle
   it, ask one batched question before you write.
7. **No filler.** Every sentence carries a fact a future reader needs. Report what changed, what you
   verified, and what you left out.
8. **Make the smallest maintainable change that solves the request.** Keep code, docs, and tests in
   proportion to the risk.

## Write to the vault

- **The PR diff is the preview.** Write on a branch, commit, and open a PR to this repo. The user
  reviews and merges it. You do not need a chat preview first. Show the diff in chat only when the user
  asks.
- Load `watchtower` before a vault write, and `vault-edit` before a move, rename, merge, or delete.
- Moves use `git mv`, then `_Agents/wt doctor --fix`. Merge only with 0 errors from `wt doctor`.
- Write a durable fact to memory when you learn it. `_Agents/memory/README.md` says where.
- Tags must be in `_Agents/tags.md`. Employer material carries the employer tag (`ACME` in this
  template).

## Spaces

Each space holds its own notes, `memory/`, and `skills/`. Material that is true in every space stays
in `_Agents/`.

| Space | Holds | Space rules |
|---|---|---|
| `Spaces/Personal/` | Personal life | `Spaces/Personal/Personal Vault Guide.md` |
| `Spaces/Work/` | Work for your current employer (tag `ACME`) | `Spaces/Work/AGENTS.md` |
| `Spaces/Career/` | Resume, career plans, and future work | None |

- Find the active space from the working directory or the request. Search that space and `_Agents/`.
- A fact that one space needs goes in that space's `memory/`. A fact true everywhere goes in
  `_Agents/memory/`.
- `wt doctor` reports a tag that crosses a boundary (`_Agents/wt.json` → `boundaries`).
- To leave a job, archive its space folder. Its memory and skills go with it.

## Page conventions

Obsidian, GitHub, and Isomorphic read the same files. These rules apply to new and moved pages.

- Frontmatter: `type`, `description`, `updated`. Add `title` only when it differs from the file name.
- A folder's overview page is `<folder>/index.md`. Each content page has a unique title.
- Use an `okf-view` block for a listing, not a hand-kept list. `_Agents/wt index` writes its snapshot.
- `.isomorphic.json` says which folders are content and which are system.
- Plugin files (`.excalidraw.md`, `.base`) are extras, never the only index of anything.

## Git

- Fetch before you branch. Stage only the files you changed; never `git add -A` in a dirty tree.
- Keep unrelated changes that the user has not committed.
- The pre-commit hook runs `wt doctor`; CI runs `wt doctor`, the search tests, and gitleaks.
- A passing local test does not prove that a deployment or live system changed.

## Where things are

- Vault guide for people: `README.md`
- Skills: `_Agents/skills/`, `Spaces/<Name>/skills/` (table: `_Agents/README.md`)
- Memory: `_Agents/memory/README.md`
- Vault layout, templates, filing, and adding a skill: the `watchtower` skill and its `reference.md`
- The tool: `_Agents/wt` (`search`, `doctor`, `install`, `index`)
