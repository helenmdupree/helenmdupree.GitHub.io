# Knowledge Library V2 structural checkpoint

Date: 2026-09-16
Status: APPROVED FOR PUBLICATION / KNOWLEDGE LIBRARY V2

## Why this change exists
The public Knowledge Library had accumulated several generations of site architecture. Giant branch cards, an AIM deep-dive block, a full A-Z topic index, perspective links, content-type labels, and older navigation concepts were competing on one page.

The V2 decision is to make the Knowledge Library a compact front door for durable technical knowledge rather than a visual sitemap.

## Preserved architecture
- Existing knowledge branch routes remain intact.
- The foreground Knowledge Library no longer loads the large search interface.
- Search code remains preserved in `assets/library-search-index.js` and `assets/library-search.js` for future governed reuse, especially with Ask SOUBEL.
- The A-Z taxonomy is preserved, not deleted.
- The A-Z manual-browse route remains deferred from public release until its older links are fully reconciled with Ask SOUBEL and the current site architecture.
- Ask SOUBEL remains in development; no runtime or governed knowledge behavior is changed by this website edit.

## Ask SOUBEL alignment
The private design contract ASK_SOUBEL_PUBLIC_PAGE_ARCHITECTURE_V0.1_2026-09-10.md states that Ask SOUBEL is the primary public-facing knowledge experience and the traditional alphabetical library should be a quiet Browse A-Z fallback, not a competing foreground destination.

## Publication boundary
The user approved publication on 2026-09-16 after local review. Public scope is limited to the Knowledge Library V2 page, its dedicated stylesheet, the canonical navigation removal of generic `Industry Intelligence`, and this architecture/backup record. The deferred A-Z route is not part of this release.

## V2.2 scalable subject directory decision

The foreground Knowledge Library no longer carries a large search interface. Search code remains preserved in `assets/library-search-index.js` and `assets/library-search.js` for future reuse, especially within Ask SOUBEL or another governed retrieval experience.

The main library now functions as a browse-first subject directory. Existing substantive destinations remain clickable. Future subjects are represented as non-clickable `Developing` entries until enough governed material exists to justify a real destination.

Current active subjects:
- Pipeline Integrity
- Corrosion & Cathodic Protection
- Tank & Terminal Integrity
- Asset Performance
- Digital & AI Knowledge
- Asset Integrity Management

Future plug-and-play subject shells:
- AC Mitigation
- Internal Corrosion
- Coatings & Linings
- Leak Detection & Monitoring
- Reliability & Maintenance
- Regulatory & Standards

Do not create empty destination pages solely to activate these entries. Activate a subject only after substantive governed content exists behind it.

## Subject-boundary note

- Materials / Metallurgy / Failure Analysis remains a secondary integrity topic and may be surfaced within Pipeline Integrity, Tank & Terminal Integrity, Corrosion & Cathodic Protection, or Ask SOUBEL routing where relevant. It is not a standalone top-level Knowledge Library lane.
- Integrity software and data-management concepts remain within Digital & AI Knowledge and related integrity contexts. They are not a standalone top-level Knowledge Library lane.
