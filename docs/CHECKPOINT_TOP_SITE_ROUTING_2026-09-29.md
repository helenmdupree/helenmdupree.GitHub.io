# CHECKPOINT — TOP SITE ROUTING CLEANUP — 2026-09-29

## Architecture vocabulary
- Top Site = Helen Lobby / portfolio.
- Bottom Site = original/deep SOUBEL website.
- Doorway = Repository / Down the Rabbit Hole.
- Locked rule: Top Site visitors must remain in the Top Site unless they explicitly choose Down the Rabbit Hole.

## Completed locally for this checkpoint
- Get to Know Me body destinations now have Top Site copies.
- Top Site Career in Motion, Thought Pieces, Reading & Influence, Books That Stayed, Gumbo?, The Inheritance, and Where's My Bike? routes remain upstairs.
- Duplicated pages use the Top Site navigation, not the Bottom Site menu.
- Top Site LinkedIn destination changed to Helen's personal LinkedIn profile.
- Down the Rabbit Hole control on Get to Know Me was lifted slightly for discoverability.
- All audited Top Site routes return HTTP 200 locally.
- Old /about/reading-influence and /about/career-in-motion body routes were removed from the new Top Site copies.

## Explicitly rejected / NOT part of checkpoint
A first Bottom Site menu experiment placed the navigation inside a minimal outlined box. Helen rejected it. That CSS was removed before this checkpoint. Do not restore it.

## Next task after checkpoint
Return to http://localhost:8015/soubel/ and redesign the Bottom Site navigation so it is visually intuitive as a menu. Preserve the quiet/minimal repository entrance. Do not add the rejected minimal box treatment.

## Safety
Production should only receive reviewed checkpoint changes through a clean branch/PR and successful pre-publish gate. Do not publish from the dirty historical OneDrive tree.
