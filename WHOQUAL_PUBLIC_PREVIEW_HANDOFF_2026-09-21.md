# WhoQual-IQ™ Public Preview — Proceed From Here

Date: 2026-09-21

## Repository

- Repo: `C:\GitHub\soubel-whoqual-public-preview`
- Branch: `whoqual-public-one-screen-v0.1`
- This branch is an unpublished public-preview design branch.
- Do not merge or deploy without Helen's explicit approval.
- Local preview server has been running at `http://127.0.0.1:8030/whoqual-iq/`.

## Product naming

Use exactly:

**WhoQual-IQ™**

Do not use WhoQual-iQ, WhoQual IQ, or WhoQual-IQT.

The Texas public-facing candidate-authority label is:

**Texas Authority IQ**
## Design direction approved / preferred

The public front is a **single-screen, no-scroll product preview**, similar in spirit to Ask SOUBEL but visually distinct.

Current concept:
- dark futuristic / industrial intelligence aesthetic
- SOUBEL dark teal palette
- geometric beveled-panel background treatment
- subtle HUD / scan / ambient-motion effects
- stacked 3D product-preview cards
- real Houston Leaflet / OpenStreetMap context inside the Project Intelligence card
- right-side status cards
- prominent private-development status at the top

User explicitly prefers a futuristic feel over a conventional enterprise dashboard.

Motion should mean **more layered ambient movement, not faster movement**.
## Stacked-card concept

Four preview cards currently exist:

1. Project Intelligence — blue
2. Authority Stack — bronze/brown
3. Verification & Readiness — green
4. Project Document Analysis — teal

The exposed card edges need to make it obvious there are multiple cards in the deck.

The carousel arrows were deliberately enlarged and brightened.

The authority color was changed away from yellow/marigold. User disliked marigold. Current direction is deep bronze / brown / smoked-copper.

Card colors should coordinate with the right-side status palette without forcing an inaccurate one-to-one semantic mapping.
## Copy / public-disclosure decisions

Avoid marketing jargon and slogans.

Removed / avoid:
- "REAL WORK · RIGHT PEOPLE · A SAFER TOMORROW"
- "A stronger tomorrow built on a more qualified today"
- similar promotional language

Top functional strip currently uses:
**PROJECT CONTEXT · AUTHORITY · EVIDENCE · READINESS**

Top-right status should remain prominent:
**PRIVATE DEVELOPMENT UNDERWAY**
**PUBLIC PREVIEW · NOT YET RELEASED**

The public preview should tease the product without exposing too much of the internal reasoning architecture.
## Latest user decision before handoff

The six-step left public reasoning rail:
PROJECT → TASK → AUTHORITY → OQ → EVIDENCE → READINESS

was judged to reveal too much internal process for a public preview.

User decided to **remove it entirely**, not replace it with a shorter public process list.

That rail has now been removed from the HTML/layout.

Also pending from the immediately previous review:
- the main ™ mark was too small and too high
- it has now been made larger and lowered closer to the WhoQual-IQ wordmark

Do not re-add the six-step rail unless Helen explicitly asks.
## Files actively edited

- `whoqual-iq/index.html`
- `assets/site-whoqual-preview-v2.css`
- this handoff file

Current page remains `noindex,nofollow`.

The real WhoQual private engine is not exposed or connected to this public preview.

The Project Intelligence card uses Leaflet/OpenStreetMap and public Houston energy-context markers, plus a public pipeline-context request. It is presentation-only and should not imply field locating, ownership, operating status, or jurisdiction.
## Development-process guardrails

Private WhoQual engine repo was stabilized separately before public-preview work.

For this public-preview repo:
- keep one local preview server only
- document its port/PID
- stop it when the design session ends
- avoid leaving orphaned preview servers
- validate JS and HTTP before checkpointing
- do not publish without explicit approval

## Immediate next task in the next chat

1. Re-open the local preview on port 8030.
2. Visually review the no-left-rail layout and the adjusted ™ placement.
3. Check whether reclaiming the left-rail width improves balance; refine card-stage proportions if needed.
4. Continue visual refinement only after Helen reviews that result.
5. Preserve the current futuristic layered-motion direction.
