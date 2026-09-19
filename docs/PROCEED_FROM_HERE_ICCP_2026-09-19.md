# PROCEED FROM HERE — ICCP INTERACTIVE EXPERIENCE
Date: 2026-09-19
Status: CHECKPOINT / SAFE HANDOFF
Owner: Helen M. Dupree / SOUBEL

## PURPOSE
This workstream is rebuilding the ICCP explainer for the SOUBEL website.
The user wants an actual interactive website experience — not a standalone generated image.
The explainer must look believable to someone familiar with field pipeline work.
Technical realism includes proportion, field context, equipment placement, materials, and serviceability.

## NON-NEGOTIABLE DESIGN DIRECTION
Do NOT continue polishing the old schematic family as the final experience.
Do NOT present another standalone AI-generated image as if it were the website.
Do NOT let the rectifier become visually oversized relative to the pipeline.
Do NOT mount the rectifier unrealistically high.
The technician must be able to open the rectifier cabinet and adjust CP output at comfortable working height.
Use browser overlays for labels, callouts, current paths, and interaction.
Use realistic scene construction for the physical world.

## USER REACTION / TARGET
The user liked the latest realistic field concept very much.
That concept showed a technician at a pole-mounted rectifier, a test station, buried pipeline cross-section,
an anode bed, natural right-of-way/field context, and blue current-flow arrows.
The user immediately asked whether it was in the website.
That confirmed the target: FIELD REALISM + ACTUAL WEBSITE INTERACTION.
## REPOSITORY / WORKTREE
Repository worktree:
C:\GitHub\soubel-iccp-interactive

Current branch:
design/iccp-interactive-v0.1

Do not merge to public main without explicit approval.
The SOUBEL public main branch is protected by the Pre-Publish Security Check.
This ICCP work is isolated from live/public production.

Local prototype server:
http://127.0.0.1:8015/

## OLD WEB EXPERIMENTS — FREEZE, DO NOT TREAT AS FINAL BASE
prototypes/iccp-interactive-v0.1.html
Commit bf2c55e — first interactive technical SVG explainer.

prototypes/iccp-interactive-v0.2.html
Commit 677fa2c — lighter canvas / clearer hierarchy.

prototypes/iccp-interactive-v0.3.html
Commit 2099ed0 — pole-mounted rectifier and larger labels.

prototypes/iccp-interactive-v0.4.html
Commit 9bd0aec — label/callout reflow.

prototypes/iccp-interactive-v0.5.html
Commit 5a4741a — attempted 'realistic' SVG/web scene.
User correctly observed v0.2–v0.5 were essentially the same drawing with tweaks.
Do not keep renovating that architecture.
## BLENDER INSTALLATION
Blender is installed and verified:
C:\Program Files\Blender Foundation\Blender 5.2\blender.exe
Version verified: Blender 5.2.2 LTS.

The user does NOT need to learn Blender.
Use Blender Python scripting / automation whenever practical.

## SCALE BASELINE
The first scale study established:
Representative pipeline OD: 30 in / 0.762 m.
Representative cover: 36 in / 0.914 m above pipe crown.
Human reference: 1.70 m.

Initial rectifier was too small and too high.
User clarified the technician must access the cabinet to adjust CP voltage/output.
The rectifier was lowered and enlarged.

Approved-enough scale baseline:
blender/build_iccp_scale_blockout_v2.py
blender/iccp_scale_blockout_v2.blend
blender/iccp_scale_blockout_v2.png
Commit 9b5a543 — Lock ICCP operator-access scale baseline v2.

Representative v2 cabinet:
about 22 x 18 x 30 in.
Bottom around 1.07 m / 42 in above grade.
Center around 1.45 m / 57 in.
These are visualization anchors, NOT engineering design specifications.
## BLENDER REALISM STUDY
blender/build_iccp_realism_v3.py
blender/iccp_realism_v3.blend
blender/iccp_realism_v3.png
Commit 882da04 — Add ICCP realism study v3.

v3 added:
textured soil/materials,
galvanized cabinet treatment,
pipeline coating,
wood pole treatment,
cabinet meter/vent/warning/handle/rain hood,
improved test station,
perspective camera,
more natural lighting.

User reaction to v3:
'Does this look like I just walked onto a pipeline project? No.'
That assessment is correct.
Treat v3 as a developmental 3D block/material study, not a finished field scene.

## WHAT REALISM MUST MEAN NEXT
The physical installation should feel like a real pipeline right-of-way / CP field installation.
The pipeline project itself must become the scene.
The technical explanation should be layered on later.
Avoid textbook elevation composition.
Avoid giant floating development labels in final visuals.
Use terrain variation, believable backfill/soil, vegetation, utility hardware, conduit,
mounting brackets, hinges/latches, weathering, shadows, sky/environment, and atmospheric depth.
Camera should feel like a person standing in the field, not an engineering orthographic view.
## REQUIRED FINAL ARCHITECTURE
Build a fresh ICCP Interactive Experience v1, not v0.6.

Layer 1 — Realistic physical scene:
utility feed, pole, operator-access rectifier, test station, groundbed/anodes,
buried coated steel pipeline, soil/backfill, right-of-way context.

Layer 2 — Live browser technical overlays:
large editable labels,
numbered callouts,
positive lead/current path,
negative return path,
electrolyte current flow,
component highlighting.

Layer 3 — Interaction:
Play Sequence,
pause/replay,
five-step progression,
clickable/hoverable components,
short explanatory narrative per stage.

Suggested five-step sequence:
1. Power & conversion
2. Positive circuit
3. Electrolyte path
4. Protected structure
5. Return & monitoring

Do not bake technical labels or explanatory arrows permanently into the visual base.
Keep them editable/live in HTML/SVG/JS.
## LATEST VISUAL TARGET
A generated field-realism concept was produced in chat immediately before this checkpoint.
It was NOT integrated into the repo or website.
It showed:
- realistic outdoor pipeline right-of-way
- wooden utility pole
- pole-mounted rectifier at accessible technician height
- technician standing at/opening/adjusting the rectifier
- realistic test station
- buried pipeline cross-section
- anode bed in backfill
- natural vegetation / sky / field / service vehicle
- current-flow arrows through soil toward the pipeline

The user said: 'That's great! is that in our website?'
This is the clearest visual-direction approval so far.
The answer was no; the next task is to make the WEBSITE achieve that direction.

Do not repeat the mistake of generating another pretty standalone image and stopping there.

## NEXT ACTION ON RESUME
1. Inspect current repo status and this handoff.
2. Preserve v2 as the scale baseline.
3. Use v3 only as a Blender-development reference.
4. Start a fresh web/visual architecture for ICCP Interactive Experience v1.
5. Build the realistic field scene deliberately.
6. Then integrate it into a browser prototype with live overlay/animation controls.
7. Show the user the browser page — not merely a rendered image.

No public publish/merge until the user explicitly approves.
## RECENT COMMIT CHAIN
9b5a543 Lock ICCP operator-access scale baseline v2
882da04 Add ICCP realism study v3
1e9d854 Add true-scale ICCP Blender blockout
5a4741a Build realistic interactive ICCP web prototype
9bd0aec Reflow ICCP callouts for readable layout
2099ed0 Add pole-mounted rectifier and larger ICCP labels
677fa2c Lighten ICCP explainer for clearer hierarchy
bf2c55e Prototype interactive ICCP technical explainer

## IMPORTANT USER WORKING STYLE
Helen is nontechnical and expects the assistant to execute coding/build work directly.
Do not hand her code unless unavoidable.
Give one human action at a time only when needed.
She likes humor, but execution must stay clear.
If she says 'website', she means actual browser/site implementation, not a concept image.

## CHECKPOINT RULE
Repository truth beats chat memory.
Read this file first in the next chat.
Then inspect git status/log before making changes.
No reset, force push, destructive clean, merge, deploy, or publish without explicit approval.

## LATE-NIGHT STOP POINT — 2026-09-19

The ICCP browser architecture is now substantially proven in:
- prototypes/iccp-interactive-experience-v1.1.html — approved overall architecture/direction
- prototypes/iccp-interactive-experience-v1.2.html — WIP technical-overlay cleanup; NOT final

User reaction to the v1.1 browser experience: "holy crap you did it. wow."
Key approved page architecture:
- realistic field scene dominates left side
- compact ICCP sequence/control panel on the RIGHT
- controls visible above the fold
- Play Sequence + five selectable stages
- live browser overlays, not baked explanatory graphics
- no floating explanatory dialog covering the field scene; explanation belongs in right panel

CRITICAL: FINAL BASE IMAGE IS NOT YET LOCKED.
Do not pretend otherwise. Several later image-render candidates were rejected because each correction introduced new technical errors.

LATEST REQUIRED PHYSICAL SCENE / TECHNICAL RULES:
1. Rural pipeline ROW / field context, with technician in hardhat/PPE and pickup truck retained.
2. Green-coated buried steel pipeline.
3. Utility/power pole may appear as AC supply context, BUT the cathodic-protection rectifier MUST NOT be mounted on the electric utility company's pole.
4. Rectifier must be mounted on a separate operator-owned pole/post/support nearby, at technician-access/service height, with believable cabinet scale (roughly the previously accepted ~22 x 18 x 30 in neighborhood; not "small car" scale).
5. Rectifier negative/structure cable gets its OWN separate connection to the pipeline.
6. Test-station structure/pipe lead gets its OWN separate connection to the pipeline. Do NOT merge it with the rectifier negative lead into a common fitting.
7. Pipe cable attachment must look like a realistically small insulated conductor lying flat/tangentially along the pipe into a compact exothermic-weld / pin-braze attachment area protected by a weld cap / mastic / coating repair. No giant plumbing fitting or copper-tube-looking object.
8. Test station must visibly have separate buried measurement conductors:
   - structure/pipe lead -> its own pipeline attachment
   - reference-electrode lead -> buried permanent reference electrode beside the pipeline
   The reference electrode is NOT bonded to the pipe.
9. Anode bed must show every anode lead connected; no missing far-right lead.
10. Positive rectifier circuit -> anode bed; protective current shown through soil -> pipeline; pipeline -> rectifier negative completes the DC power circuit.
11. Test station is measurement/verification, not the main DC return path.
12. NO baked-in text, labels, numbered badges, arrows, legends, dialog boxes, or SOUBEL branding in the base image. Those are live HTML/SVG overlays.

RESEARCH CONFIRMATION USED DURING THIS SESSION:
- Farwest standard drawings list 2-wire CP test stations with copper-sulfate reference electrodes.
- Published CP design guidance shows stationary reference electrodes near the pipeline, with separate test leads terminating in the test station.
- The web explainer should therefore visually distinguish power-circuit wiring from measurement/reference wiring.

STOP RULE FOR NEXT SESSION:
Do NOT redesign the website again.
Do NOT resume overlay coordinate polishing before the final clean base image is locked.
First finish/correct the base image while preserving the accepted field composition. Then replace the image asset in the existing v1.1/v1.2 architecture and retune overlay coordinates.

Tonight's rejected render problems:
- oversized rectifier
- rectifier incorrectly mounted on utility company's power pole
- rectifier negative and test-station structure lead visually merged into a common pipeline connection
- cable/connection rendered like oversized copper tubing/plumbing
- some renders omitted the reference electrode or its test-station lead
- some renders omitted an anode lead
- some renders baked labels/callouts into the image

No public integration, PR, merge, deploy, or publish has been authorized for this ICCP build.
