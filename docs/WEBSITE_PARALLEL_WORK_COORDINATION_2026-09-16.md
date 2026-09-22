# SOUBEL Website Parallel Work Coordination — 2026-09-16

## Canonical navigation rule
`assets/site.js` is the current runtime source of truth for the global desktop and mobile navigation.
Individual HTML pages may still contain older hard-coded fallback navigation. Do not infer the current rendered menu from legacy page-level header markup without checking `assets/site.js`.

## Midstream cleanup completed
The fallback/source navigation in `markets/midstream-pipelines/index.html` was reconciled to the current canonical navigation structure on 2026-09-16.
The page body beginning at `<main>` was byte-for-byte unchanged by this navigation cleanup.
The current Midstream hotspot refinements remain intact.

## Safety / parallel work
No branch checkout, stash, reset, merge, or publish was performed during this cleanup.
No changes were made to `assets/site.js`, Ask SOUBEL, the Oil & Gas AI Lab, private repositories, or other market/expertise pages.
Do not overwrite newer work from parallel chat windows.

## Recovery backup
Pre-cleanup copies are stored outside the repository at:
`C:\Users\winst\OneDrive\Desktop\SOUBEL_Backups\2026-09-16_1512_midstream_nav_cleanup`

Pre-cleanup Midstream SHA256:
`F881B96F2D2286ECD9C50394EBE1B9BDC53F42793D941D61274B9AEBA2C0DF88`

Post-cleanup Midstream SHA256:
`33910B43BC1EA2ACD2DEE68670FC4280718514126A6FB61BA4698C71977CB34C`