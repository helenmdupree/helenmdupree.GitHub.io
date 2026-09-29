# SOUBEL DEVELOPMENT RECOVERY NOTE — 2026-09-29

## READ THIS BEFORE TOUCHING THE WEBSITE

This repository is in an active recovery situation after a Sep 29 editing session introduced a mixture of production changes and extensive local/uncommitted experiments.

**DO NOT continue editing from the dirty OneDrive working tree.**
**DO NOT try to “fix forward” from PR #138.**
**DO NOT force-reset GitHub history.**
**DO NOT make production changes until a clean recovery worktree has been built, audited, gated, and reviewed by Helen.**

## Known-good production checkpoint

The last deliberately reviewed and safely published baseline is:

- PR #135 — “Publish Deep SOUBEL cleanup and content refinements”
- Merge SHA: `980fe648d75d6274f23c6b2eff3cf9aace285339`
- SOUBEL Public Pre-Publish Gate #179: SUCCESS

That checkpoint contains the work Helen reviewed with the prior assistant, including Commercial Growth refinements, Channel Strategy, Strategic Accounts, CP Systems cleanup, Markets/Resources work, and related approved changes.

## What happened after #135

### PR #137 / commit `7497dfeecc2d9b4ff93c1272634c6283fc4b4287`
Commit title: “Repair contaminated GitHub Pages deployment”

Forensic review on Sep 29 confirmed this changed only:
`expertise/commercial-growth-strategic-accounts/index.html`

The substantive change is a harmless HTML comment used to force a clean GitHub Pages rebuild. It did not contain meaningful visible design/content work that must be preserved.

### PR #138 / commit `bc03860093c6fd1312e78ee3e0d10001c2f99a12`
Commit title: “Publish restrained expertise and AIM cleanup”

This changed 13 files across:
- Asset Integrity Management
- Asset Performance
- Corrosion / Cathodic Protection
- Digital Transformation & AI
- Knowledge Library Asset Performance

Forensic review found a mixture of intended cleanup and collateral problems. Examples include malformed markup (including a duplicate `class` attribute on a body element), emptied metadata on at least one AIM page, and a large Digital Transformation rewrite. Helen explicitly prefers to recover to the known-good #135 baseline rather than continue repairing #138 piecemeal.

**Recovery decision: discard #138 as a content baseline and restore its affected files from #135 through a normal recovery PR.**

## Current production truth at time of this note

At the start of the recovery audit, `origin/main` was:
`bc03860093c6fd1312e78ee3e0d10001c2f99a12`

This is #138 and is two commits ahead of the #135 checkpoint.

Before doing anything in a future session, fetch `origin/main` again and verify current truth. Do not assume the SHA above remains current.

## Dirty local working tree — QUARANTINE IT

Historical working copy:
`C:\Users\winst\OneDrive\Desktop\soubel-tank-application-cards-preview`

It contains many modified/untracked files from multiple sessions. On Sep 29, additional local-only edits were observed through roughly 1:03 PM, including files such as:
- `soubel/index.html`
- `repository/index.html`
- `get-to-know-me/index.html`
- portfolio/shell assets

These local changes are NOT automatically production truth and must not be swept into a release.

Use the dirty tree only as reference/evidence.

## REQUIRED RECOVERY PROCEDURE

1. Fetch current `origin/main`.
2. Read this note and the local authoritative recovery file:
   `C:\Users\winst\OneDrive\Desktop\soubel-tank-application-cards-preview\docs\WEBSITE_RECOVERY_LATEST.md`
3. Verify the #135 checkpoint SHA still exists:
   `980fe648d75d6274f23c6b2eff3cf9aace285339`
4. Create a BRAND-NEW clean Git worktree under `C:\GitHub\...`.
5. Base the recovery work on current `main` so history remains intact.
6. Restore the files affected by #138 to their exact #135 versions. Do not cherry-pick dirty local edits.
7. #137's rebuild comment does not need to be preserved unless there is a specific technical reason.
8. Inspect the resulting diff. The recovery PR should be narrowly limited to reverting the unwanted post-#135 content changes.
9. Run the SOUBEL Public Pre-Publish Gate.
10. Do not merge unless the gate succeeds.
11. Show/verify the recovered site locally and obtain Helen's approval before production merge.
12. Create a normal recovery PR. Do NOT force-push or rewrite main.
13. Merge only after approval.
14. Verify live production routes and make a fresh checkpoint/backup.

## Critical architecture that must survive recovery

- `/` = Helen M. Dupree front-door portfolio.
- `/soubel/` = Deep SOUBEL professional knowledge repository home.
- `/repository/` = Rabbit Hole / threshold doorway into SOUBEL.
- Physical QR materials are already mailed. Do not casually change QR-critical ingress.
- Deep SOUBEL Home navigation should ultimately point to `/soubel/`, not eject visitors to Helen's lobby.
- SOUBEL is Helen's professional knowledge repository/body of work, NOT a consulting firm.
- “Operational Trust” is being removed from the bones of the SOUBEL identity.
- Do not restore the old giant SOUBEL Operational Trust masthead or old logo lockup.

## Known remaining issue from the #135 state

The Downstream & Refining page still needs its SOUBEL logo/shell corrected:
`/markets/downstream-refining/`

Helen intentionally deferred that until after recovery.

## CP Systems guardrail

Helen explicitly rejected the old ICCP and galvanic CP diagrams as technically wrong. PR #135 removed them and reduced the giant/dark CP Systems hero treatment.

**DO NOT restore those rejected diagrams during recovery.**

## Working rule

**REPOSITORY TRUTH > THIS RECOVERY NOTE > LOCAL RECOVERY FILE > CHAT MEMORY**

If a future chat window opens after a crash, it should NOT ask Helen to teach the project again. It should read this note, inspect current repository truth, read WEBSITE_RECOVERY_LATEST.md, and continue the controlled recovery.

## STOP POINT

The current agreed next action is:

**Build a clean recovery worktree from current main and prepare a narrow recovery diff that restores #138-affected content to the known-good #135 versions. Do not merge until Helen has reviewed the recovered local result and the pre-publish gate passes.**
