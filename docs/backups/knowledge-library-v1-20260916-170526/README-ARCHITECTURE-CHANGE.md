# Knowledge Library V2 structural checkpoint

Date: 2026-09-16
Status: LOCAL DRAFT / NOT PUBLISHED

## Why this change exists
The public Knowledge Library had accumulated several generations of site architecture. Giant branch cards, an AIM deep-dive block, a full A-Z topic index, perspective links, content-type labels, and older navigation concepts were competing on one page.

The V2 decision is to make the Knowledge Library a compact front door for durable technical knowledge rather than a visual sitemap.

## Preserved architecture
- Knowledge Library search remains intact and continues to use library-search-index.js + library-search.js.
- Existing knowledge branch routes remain intact.
- The A-Z taxonomy is preserved, not deleted.
- A-Z is moved out of the foreground page and retained as a background/manual-browse capability for future Ask SOUBEL integration.
- Ask SOUBEL remains in development; no runtime or governed knowledge behavior is changed by this website edit.

## Ask SOUBEL alignment
The private design contract ASK_SOUBEL_PUBLIC_PAGE_ARCHITECTURE_V0.1_2026-09-10.md states that Ask SOUBEL is the primary public-facing knowledge experience and the traditional alphabetical library should be a quiet Browse A-Z fallback, not a competing foreground destination.

## Safety
No production publish is authorized by this checkpoint. Review the local V2 page before publishing or changing canonical navigation.
