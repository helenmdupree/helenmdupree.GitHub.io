# SOUBEL Global Search Audit

Date: 2026-09-16
Status: APPROVED FOR PUBLICATION

## Purpose
Reconcile the global search overlay with the current SOUBEL site architecture after the Knowledge Library, navigation, homepage, and About-page changes.

## Changes
- Rebuilt `assets/library-search-index.js` from current public-site HTML.
- Search index now contains 73 current destinations.
- Excluded retired/deferred routes: generic Industry Intelligence, standalone Operational Trust, Browse A-Z, and legacy Pipeline & Asset Integrity expertise route.
- Confirmed all 73 indexed destinations exist locally.
- Confirmed all 73 indexed pages load `assets/analytics.js`, which loads the global search control.
- Added search-overlay reset on close: query, status, results, analytics query state, and overlay scroll position are cleared.
- Added cache-busted global search and index asset versions.
- Improved short-acronym matching so `AI` does not match letter fragments inside unrelated words.

## Recovery
Pre-audit copies are stored at `docs/backups/search-audit-20260916/`.
