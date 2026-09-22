# Downstream, Refining & LNG — Recovery Handoff — 2026-09-21

Current objective: redesign the SOUBEL Downstream page quickly, visually, and in alignment with the Midstream market page.

## Current local page state
- Working page: markets/downstream-refining/index.html
- New isolated stylesheet: assets/site-downstream-v1.css
- Pre-redesign backup: markets/downstream-refining/index-before-redesign-2026-09-21.html
- Local preview: http://127.0.0.1:8003/markets/downstream-refining/
- NOTHING from this redesign has been pushed live yet.

## Important assessment
The first local redesign is NOT approved. Helen flagged:
- title rendered white / unreadable
- headings/fonts are much too large
- too much white space
- page lacks the polished visual hierarchy of Midstream
- current five-box refinery flow is not the desired visual solution

## Approved direction
Reframe page as: "Downstream, Refining & LNG".
Use a proper executive market schematic comparable in spirit to the Midstream & Pipelines visual.

Visual architecture:
REFINING lane:
Crude Receipt → Distillation → Conversion Units → Treating / Blending → Product Storage → Terminal / Market Delivery

LNG lane:
Pipeline Gas / Feedgas → Pretreatment → Liquefaction → LNG Storage → Marine Loading / Export

Shared layer:
Utilities & Offsites, including power/steam, water, flare/relief, electrical/instrumentation and shared reliability/integrity context.

## Visual asset
A new Downstream, Refining & LNG visual was generated in the previous chat.
Helen manually saved the visual to her "Soubel Pictures" folder.
Do NOT regenerate it until the saved version has been inspected.
Next chat should locate/use Helen's saved image and integrate it into the page.

## Next actions
1. Inspect Helen's saved Downstream, Refining & LNG visual.
2. Replace the current box-based refinery diagram with that visual.
3. Fix hero/title contrast and reduce heading scale substantially.
4. Tighten vertical spacing/white space throughout.
5. Preserve the current SOUBEL navigation shell.
6. Verify desktop and mobile locally.
7. Only after Helen visually approves: commit/push this page work cleanly and verify backup/mirror status.

## Repository caution
The local public-site repo currently contains many unrelated modified/untracked files from other approved work today.
Do NOT mass-commit or mass-reset.
Isolate Downstream changes carefully.
GitHub should remain source of truth; Google Drive should serve as backup/archive mirror once work is cleanly committed.
