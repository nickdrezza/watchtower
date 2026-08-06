---
name: playwright-testing
description: >
  Adds and runs reusable Playwright browser tests for personal websites and web apps, so user-visible
  behavior is verified in a real browser instead of inferred from the source. Use when building,
  repairing, or extending a site and the change touches uploads, downloads, forms, navigation,
  responsive layout, authentication, or any multi-step flow — and when the user says "test this in a
  browser", "does the upload work", "write a Playwright test", "check it on mobile", "verify the form",
  or "did that actually fix it". the vendor platform apps add their own auth and iframe constraints on top; see
  _Agents/memory/vendor-platform.md before concluding an app cannot be tested.
---

# Playwright testing

Give each maintained site a browser test suite that an agent can run without manual clicking.

## Set up

1. Read the repo instructions and preserve its package manager, lockfile, framework, and existing test layout.
2. Install `@playwright/test` as a development dependency and install Chromium when it is absent.
3. Keep browser tests separate from unit tests, normally under `tests/e2e/`.
4. Add explicit scripts:
   - `test:e2e` — headless suite
   - `test:e2e:ui` — optional interactive debugging
   - include `test:e2e` in CI only after it is stable there
5. Configure:
   - a deterministic `baseURL`;
   - the app’s direct development command in `webServer`;
   - `reuseExistingServer: !process.env.CI`;
   - trace, screenshot, and video retention on failure;
   - bounded action, navigation, and test timeouts.

Do not treat a config file alone as working infrastructure. Confirm the package is declared, the
browser is installed, at least one real Playwright test is discovered, and the documented command runs it.

## Test user outcomes

Drive the public interface. Prefer roles, labels, and visible text over CSS selectors or implementation details.

For each changed feature, cover:

1. the main successful journey;
2. the most important validation or failure state;
3. the final user-visible result.

For uploads and generated files:

- use small deterministic fixtures checked into the application repo;
- upload through the file input or drop target;
- wait for a visible processing state and completion state;
- capture the browser download event;
- verify the suggested filename, MIME type, non-empty output, and relevant size constraint;
- inspect the generated file when correctness depends on its structure.

Do not mock the code under test merely to make the browser flow pass. Mock only external systems that
are outside the application’s responsibility, and make that boundary explicit.

## Diagnose before changing code

Run the smallest browser flow that reproduces the report. Record:

- failed network requests;
- uncaught page errors;
- relevant console errors;
- the last visible application state;
- downloaded-file metadata when a download occurred.

Classify failures before fixing them:

- server unavailable or wrong start command;
- missing dependency or browser binary;
- unsupported browser capability;
- test-environment or authentication setup;
- application regression.

A passing static-source assertion is not evidence that the application works in a browser.

## Verify the change

Run:

1. the focused Playwright test while iterating;
2. the complete browser suite;
3. unit tests;
4. the production build.

Report what journeys passed and any browser, codec, authentication, or platform limitations that remain.

## the vendor platform applications

Vendor-hosted data apps build on this workflow but cannot use an ordinary standalone localhost page.
Before testing one, read `_Agents/memory/vendor-platform.md` and the app host’s `tests/README.md`.

The vendor-platform layer adds:

- a saved authenticated vendor-platform session;
- `/api/open/<appSlug>` as the supported entry;
- local-network permission for the localhost iframe;
- selection of the iframe by exact host and port;
- the filtered app-host development command;
- status-code classification for unregistered hosts.

Keep those platform constraints in the vendor-platform documentation. Keep the reusable browser-testing
workflow here.
