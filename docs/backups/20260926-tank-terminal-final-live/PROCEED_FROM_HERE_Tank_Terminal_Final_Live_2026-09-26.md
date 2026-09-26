# PROCEED FROM HERE — Tank & Terminal Integrity Final Live — 2026-09-26

## STATUS AT HANDOFF

The Tank & Terminal Integrity redesign is LIVE:
- https://soubel.com/knowledge-library/tank-terminal-integrity/
- Related edited page: https://soubel.com/expertise/asset-integrity-management/application-domains/

Publish path:
- Development branch: tank-application-cards-v0.1
- Development commit: f313ea8097a02e39e552bddff0daec93b48bab78
- Pull request: PR #107 — Tank & Terminal Integrity visual redesign
- Live merge commit: cd49f1a3353d265211ca1557d844f2faebf1bdb1
- Recovery branch: backup/tank-terminal-final-2026-09-26

The deployment was verified after propagation from the public soubel.com site.

## LIVE VERIFICATION COMPLETED

Verified HTTP 200:
- Tank & Terminal Integrity page
- AIM Application Domains page
- transfer-containment-response-hero.png
- application-terminal.jpg
- application-refinery.jpg
- application-midstream.jpg
- application-utilities.jpg
- application-manufacturing.jpg
- application-water.png

Verified live Tank page markers:
- visible six-item EXPLORE THIS PAGE navigation
- Section 03 interactive Transfer / Containment / Response visual
- all six Application Environments images
- 05 · STANDARDS & REGULATION
- 06 · LIFECYCLE & DECISION CONTINUITY
- Lifecycle instruction: Hover or tap each stage to view its definition.

Verified live AIM Application Domains:
- old SOUBEL applies AIM thinking language removed
- revised neutral AIM intro live
- arrow encoding repaired
- no obvious mojibake remains

## LOCKED / APPROVED TANK PAGE CHANGES

### Hero / page navigation
The former large Explore this page dropdown and hero AIM Application Domains button were removed.

The hero now displays a six-item visible navigation band:
1. Tank Integrity
2. Inspection & Condition Evidence
3. Transfer, Containment & Response
4. Application Environments
5. Standards & Regulation
6. Lifecycle & Decision Continuity

Each nav item wraps cleanly and includes a visible downward navigation cue. EXPLORE THIS PAGE appears above the band.

The AIM Application Domains button was moved to the bottom of the page near the final Lifecycle / related-material area.

### Section 02 — Inspection & Condition Evidence
Keep the existing daytime inspection visual and technical-term hover definitions.

The existing field-evidence callout remains:
Field evidence still has to be reconciled with the asset history.

A blue/aqua divider was added between Section 02 and Section 03.

### Section 03 — Transfer, Containment & Response
The former three white cards were replaced by a compact dark photographic interactive section using:
assets/transfer-containment-response-hero.png

Three HTML/CSS overlay panels remain separate from the image:
- Transfer & Mechanical Systems
- Overfill & Secondary Containment
- Release Response

Approved direction:
- translucent dark panels
- image remains visible under overlays
- compact visual scale
- API 2350 and EPA SPCC buttons centered below the visual

Do NOT replace this with the earlier giant mockup or bake explanatory text into the image.

### Section 04 — Application Environments
The former plain six-card text grid was redesigned into overlapping photographic image + text compositions.

Images:
- Petroleum Terminals & Tank Farms → application-terminal.jpg
- Refining & Petrochemical → application-refinery.jpg
- Midstream & Pipeline Facilities → application-midstream.jpg
- Utilities & Industrial Infrastructure → application-utilities.jpg
- Manufacturing & Process Facilities → application-manufacturing.jpg
- Water & Wastewater → application-water.png

The section is narrowed and centered. Forced card heights were removed so text panels hug their content.

### Section 05 — Standards & Regulation
This is now its own numbered section:
05 · STANDARDS & REGULATION

Current intro:
Tank integrity is governed within a standards and regulatory framework that varies with service, tank type, jurisdiction, material, and facility configuration. Current source material should govern the requirement, and qualified engineering judgment should govern how it is applied.

The redundant bottom Source discipline paragraph was removed.

Organization logos were deliberately NOT added. Keep organization names as text:
- U.S. EPA
- STI/SPFA
- API 653
- API 2350

Reason: safer trademark / affiliation treatment and cleaner source-navigation design.

### Section 06 — Lifecycle & Decision Continuity
This is now its own final numbered section:
06 · LIFECYCLE & DECISION CONTINUITY

A blue/aqua divider separates Section 05 and Section 06.

The original lifecycle graphic is retained:
assets/tank-terminal-lifecycle-decision-continuity.jpg

The intro copy is light enough to read on the dark section.

Lifecycle definitions exist for:
- Baseline
- Operate
- Inspect
- Assess
- Repair / Mitigate
- Return to Service
- Reassess

Instruction inside lower-left water area:
Hover or tap each stage to view its definition.

IMPORTANT IMPLEMENTATION NOTE:
The lifecycle source image is exactly 1100 × 619 pixels. Earlier percentage-offset hotspot attempts drifted because placement was initially treated as top-left rather than centered coordinates. The current implementation uses centered positioning with transform: translate(-50%,-50%) and coordinates derived from the source image geometry.

Do not revert to the earlier large/free-floating hotspot versions or the shared definition panel. Definitions should remain near the relevant lifecycle stage.

If hotspot refinement is needed tomorrow, use the 1100×619 source geometry and exact center coordinates. Do not eyeball new percentage positions.

## AIM APPLICATION DOMAINS CHANGE

Page:
/expertise/asset-integrity-management/application-domains/

The branded sentence beginning SOUBEL applies AIM thinking was removed.

Current intro:
Asset Integrity Management spans multiple industrial environments, where asset types, degradation mechanisms, inspection methods, standards, operating conditions, and technical authorities vary while the need for decision continuity remains.

Broken encoding characters were repaired, including:
- Condition → Context → Evidence → Decision → Execution → Learning
- footer middots
- copyright range
- footer separators

## TOMORROW — EXPERT PROCEED-FROM-HERE INSTRUCTIONS

Start from the LIVE merge commit / recovery branch. Do not reopen an older Tank worktree or reintroduce pre-PR #107 markup.

Recommended order:
1. FIRST: open the live Tank & Terminal Integrity page at normal desktop width and confirm lifecycle hotspot registration after a fresh browser load. This interaction received multiple precision iterations tonight.
2. Check each of the seven lifecycle definitions one by one for: trigger inside the stage bubble; visually consistent trigger placement; definition stays within the image; definition opens close to its stage.
3. Do one mobile/tablet review of: six-item Explore navigation; Section 03 overlay visual; Application Environment cards; Lifecycle interactions.
4. Do NOT redesign approved visual systems unless an actual responsive/layout defect appears.
5. If further refinement is desired, focus on micro-spacing and interaction polish rather than adding more content.
6. Preserve the narrative: asset → evidence → surrounding systems → application environment → standards/regulation → lifecycle/decision continuity.
7. Keep organization logos off standards cards unless explicit logo-use permission is later established.
8. Before any next live publish, use a new development branch and repeat the PR / live verification / backup routine.

## RECOVERY CONTENT

This checkpoint contains:
- PROCEED_FROM_HERE_Tank_Terminal_Final_Live_2026-09-26.md
- SOURCE_SNAPSHOT_Tank_Terminal_Integrity_index.html
- SOURCE_SNAPSHOT_AIM_Application_Domains_index.html

All seven newly added page image assets are preserved in the GitHub repository at the live merge and on the recovery branch.

## DO NOT CONFUSE WITH THE 2026-09-25 CHECKPOINT

The 2026-09-25 checkpoint predates tonight's substantial visual redesign.

Authoritative recovery point for tomorrow:
backup/tank-terminal-final-2026-09-26

Live merge:
cd49f1a3353d265211ca1557d844f2faebf1bdb1
