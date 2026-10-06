# Verification

How an agent knows it's done. Companion to [`operating-model.md`](operating-model.md): that file says
how to gather context, this one says how to earn a claim.

**"It should work" is not a result.** Neither is "the code looks correct."

## The rule

Every claim in a deliverable traces to something checkable — a command's output, a merged PR, a
ticket, a query result, an email, or his own words. This is the standing instruction in
[`../memory/working-preferences/`](../memory/working-preferences/index.md) → *Verify; never fabricate*;
it has gotten work rejected before.

## What counts as evidence

| Strong | Weak | Not evidence |
|---|---|---|
| Command output you ran and read | "The tests exist" | "This should pass" |
| A row count from the actual query | A count from a similar query | An estimated count |
| A merged PR / a ticket transition | An open PR | An intention to open one |
| A screenshot or DOM read of the real page | The component's source | The component's props |

**Numbers earn trust.** "397 of 404 rows" convinces in one line where prose takes five — see
`working-preferences.md` → *Writing about code*.

## Test the thing, not a model of the thing

- **Prefer the real system over a mock.** A mock proves your mock works.
- **Prefer the real data shape.** Empty and single-row cases pass almost anything.
- **Scale-only bugs slip past small supervised tests.** This is a lesson already paid for — the
  the enrichment vendor `personIds` cap only showed up above the tested batch size
  ([`Spaces/Work/memory/warehouse/`](../../Spaces/Work/memory/warehouse/index.md)). If behavior can change with volume,
  concurrency, or time, say so explicitly rather than implying the small run generalizes.
- **Run it twice** when a script is meant to be idempotent or scheduled. Most re-run bugs are invisible
  on the first pass.

## Test design

Tests should be the smallest set that completely covers the behavior. Test each distinct use case,
failure mode, and outcome-changing edge case once at the lowest reliable level. Do not add multiple
tests that prove the same behavior unless a different layer, integration, or regression risk requires
it.

## Browser testing

Warranted when the thing being changed is user-visible behavior — uploads, downloads, forms,
navigation, responsive layout, or a multi-step flow. Reading the source is not a substitute for
loading the page.

The executable arm is the **`playwright-testing`** skill: reusable tests that live in the repo, not
one-off manual clicks. Platform-specific auth and iframe constraints are in
[`Spaces/Work/memory/connectors/`](../../Spaces/Work/memory/connectors/index.md) — check it before concluding an app can't be tested.

## Before saying it's done

- [ ] The thing was actually run, not just written.
- [ ] The failure case was tried, not only the happy path.
- [ ] Anything that could differ at scale, on a re-run, or on another machine is named.
- [ ] Numbers in the report came from output you read, not from inference.
- [ ] Steps you skipped are stated as skipped.

## Testing checklists

When handing off a new feature for human testing, provide the shortest checklist that covers every
user-visible use case and outcome-changing edge case. Assume the tester is unfamiliar with the
feature: identify where to start, the exact control to use, and the visible result that proves the
behavior. Under each feature or ticket heading, use numbered navigation → action → verification
steps. Omit implementation detail, repeated setup, and checks already covered by another item.

## Reporting

State what happened. If tests failed, show the output. If a step was skipped, say which. **Don't take
a subagent's or a tool's summary at face value** — the "0 bugs, all clean" report has been wrong
before. Full rule: `working-preferences.md` → *Reporting*.
