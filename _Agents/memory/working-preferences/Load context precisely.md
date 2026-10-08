---
type: memory
title: "Load context precisely"
description: "Open only the skill, memory, or note the request needs; load machine and credential memory only for actions that need them."
updated: 2026-10-06
---

# Load context precisely

Spend input tokens deliberately. Start from the prompt, search for precise terms, and open only the
matching skill, memory file, note, or prior-session evidence. `machines/index.md` plus one machine profile
is required only for machine-dependent actions; `credentials/` is required only for authentication,
secret-location, profile, or connection work. Retrieval should expand when evidence points outward,
not because a file is adjacent or linked.
