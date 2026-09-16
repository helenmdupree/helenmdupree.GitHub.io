# SOUBEL Global Search Audit

Date: 2026-09-16
Status: APPROVED FOR PUBLICATION

## Purpose
Reconcile the global search overlay with the current SOUBEL site architecture after the Knowledge Library, navigation, homepage, and About-page changes.

## Changes
- Rebuilt the global search index from current public-site HTML and published it as `assets/library-search-index-v2.js`.
- Search index contains 73 current destinations.
- Excluded retired/deferred routes: generic Industry Intelligence, standalone Operational Trust, Browse A-Z, and legacy Pipeline & Asset Integrity expertise route.
- Confirmed all 73 indexed destinations exist in the current site tree.
- Confirmed indexed pages load the analytics/search loader architecture.
- Search overlay reset now runs both on close and on every open: query, status, results, analytics query state, and overlay scroll position are cleared.
- Added cache-busted loader chain: page -> `analytics.js?v=3` -> `global-search.js?v=3` -> `library-search-index-v2.js?v=1`.
- Improved short-acronym matching so `AI` does not match letter fragments inside unrelated words.
- Public index is intentionally slim: route, title, H1, capped heading summary, and content type. Full page-body text is not shipped in the global search index.

## Recovery
Pre-audit copies are stored in the local working archive at `docs/backups/search-audit-20260916/`.
