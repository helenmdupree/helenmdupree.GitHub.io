# PROCEED FROM HERE — ICCP CINEMATIC MASTER HANDOFF
## SOUBEL ICCP Interactive / Cinematic — September 19, 2026

This file is the authoritative recovery package for continuing the ICCP cinematic build in a new ChatGPT window.
It is intentionally explicit. Do not redesign the project, restart from old screenshots, or substitute AI image generation for the controlled Blender scene.

## 1. USER / OPERATING RULES

- Helen does not write code. The assistant performs the development work through Remote Desktop Commander.
- If Remote Desktop Commander disconnects, say plainly that it disconnected. Do not invent another explanation.
- Do not ask Helen to repeat decisions already recorded here.
- Do not use image generation to recreate, retouch, or "photorealize" this technical scene.
- Blender owns the geometry, component relationships, camera, animation, and final technical visual.
- Preserve prior master files; create new versioned Blender files for major stages.
- Never reset, overwrite, clean, or delete the worktree to solve a local problem.
- There are deliberate untracked WIP renders/assets. Do NOT run git clean.
- Do not deploy/publish the cinematic to soubel.com without Helen's explicit approval.
## 2. REPOSITORY / BRANCH / CURRENT AUTHORITATIVE STATE

Local isolated worktree:
C:\GitHub\soubel-iccp-v5-cleanstart

Git branch:
design/iccp-cinematic-v5-cleanstart

Remote:
https://github.com/helenmdupree/helenmdupree.GitHub.io.git

Latest protected commits:
- 232de83 — Lock ICCP master scene and two-arm technician.
- 97a528c — Checkpoint ICCP v6 cinematography path.
- 324a80c — Build slower ICCP v7 camera path with wider pipeline framing.
- 8bc4039 — Correct ICCP pipe cadweld connections with mastic mounds.
- 7b573ac — Build ICCP v8 Blender realism materials and lighting.
- c7e7d69 — Replace ICCP truck with generic work pickup and verify cadweld mastic.
- e211ac7 — Add ICCP v9 controlled current-path animation.
- 71e76a7 — Correct ICCP negative return current direction.
- 161718d — Create ICCP v10 production render master.
- 26f015f — Add resumable ICCP v10 production encoder.

At handoff creation, HEAD is expected to be at least 26f015f. Verify actual HEAD before making changes.
## 3. AUTHORITATIVE BLENDER FILES

Do not reopen an old experimental file and continue from it.

Current production master:
blender/iccp_cinematic_v10_production.blend

Immediate predecessor with corrected technical animation:
blender/iccp_cinematic_v9_1_return_direction.blend

Realism + corrected truck predecessor:
blender/iccp_cinematic_v8_1_realism_truckfix.blend

Locked earlier geometry master:
blender/iccp_cinematic_v5.blend

Important build scripts:
- blender/build_v8_1_truckfix.py
- blender/build_v9_current_animation.py
- blender/fix_v9_1_negative_return_direction.py
- blender/build_v10_production.py
- blender/encode_v10_production.py

Important render output directory:
blender/v10_frames

Final production MP4 target:
blender/iccp_cinematic_v10_production_720p24.mp4
## 4. LOCKED TECHNICAL / VISUAL DECISIONS

The scene is a controlled 3D master of a conceptual buried-pipeline impressed-current cathodic protection system.

Do not change these relationships merely to make a prettier shot:
- 30-inch coated buried pipeline.
- Pipeline is buried at a believable depth; it must not sit directly under the grass surface.
- Rectifier is on its own support.
- Utility power pole is separate and visually offset in the background, not two feet from the rectifier.
- Test station is separate above grade.
- Permanent reference electrode is a separate object in the soil.
- Reference electrode is NOT mounted on, penetrating, or sticking out of the pipeline.
- Side-offset groundbed logic is required.
- Five vertical anodes are used.
- Five distinct anode leads are used.
- Positive circuit and groundbed remain physically separate from the pipeline.
- Technician has exactly two arms and is grounded on the ROW surface.
- Technician interacts with the rectifier.
- Camera choreography is deliberately slower than the early v6 pass.
- Pipeline is kept at medium distance during the below-grade sequence; do not dive into a giant green-pipe close-up.
## 5. CADWELD / PIPE CONNECTION REQUIREMENT — DO NOT REGRESS

This was explicitly corrected after earlier wrong geometry.

Required appearance:
- Pipe electrical connections are flat against the pipe surface.
- The cadweld itself is not shown as an upright spike, post, or protruding block.
- A small low black blob-like protective mastic/epoxy mound covers the connection.
- Negative-return and test-structure pipe attachments use this treatment.

Correct Blender objects:
- Negative Cadweld Mastic
- Test Lead Cadweld Mastic

The old rigid rectangular attachment geometry was removed from the corrected masters.

The blue negative-return lead physically terminates at the pipeline connection and the black protective mound covers that connection.
The permanent reference electrode remains separate in the surrounding soil.

If a future render again shows a vertical white cylinder or spike apparently mounted on the pipe, stop immediately and inspect which object is being rendered. Do not continue to production with that error.
## 6. TRUCK REQUIREMENT — DO NOT REGRESS

The AI-generated mashup truck was rejected and is NOT part of the development path.

The corrected Blender master uses:
Truck Generic Work Pickup

Source asset:
blender/assets/3dassets/generic_work_pickup_canopy/generic_work_pickup_canopy.glb

Measured imported envelope:
approximately 5.39 m long x 2.08 m wide x 1.81 m tall.

Design intent:
- Generic, unbranded full-size double-cab work pickup.
- Hard bed canopy.
- No recognizable manufacturer badge.
- No mixed-brand front/rear styling.
- Neutral fleet-white paint.
- Same general roadside/service-track location as the approved scene.

The older Truck Real Pickup 09 hierarchy remains hidden only for rollback. Do not unhide it for production.
## 7. ICCP CURRENT ANIMATION — CORRECT DIRECTION

The animation uses conventional current flow.

Required sequence:
1. Rectifier positive -> positive main/header.
2. Positive header -> five separate anode leads.
3. Anodes -> surrounding soil/electrolyte.
4. Protective current through soil -> pipeline.
5. Current cue along the protected pipeline.
6. Pipeline -> black mastic-covered negative connection.
7. Negative-return lead -> rectifier negative terminal.
8. Test-station/reference-electrode cue is measurement/verification, NOT part of the main return-current path.

Critical correction:
The v9 blue negative-return overlay originally animated in the wrong direction (rectifier -> pipe).
That was corrected in v9.1.

Correct animated return overlay object:
FX Negative Return

Verified corrected spline order:
START at pipe approximately (-4.15, -0.24, -0.999)
END at rectifier approximately (-5.65, 0.15, 1.08)

The v10 build script contains a guardrail that fails if this direction is reversed again.
## 8. CURRENT V10 PRODUCTION RENDER

Production master:
blender/iccp_cinematic_v10_production.blend

Render target:
1280 x 720
24 fps
624 frames
Approximately 26 seconds
Blender EEVEE
8 render samples
AgX view transform
Motion blur enabled, shutter approximately 0.22

Production output is deliberately a PNG sequence:
blender/v10_frames/frame_0001.png through frame_0624.png

Reason:
A PNG sequence is resumable. If Remote Desktop Commander disconnects or ChatGPT crashes, completed frames remain safe on disk.

At handoff creation, the render was actively running and had passed frame 178.
DO NOT trust that old count after restart. Recount the directory immediately.

Current render command is conceptually:
Blender -b blender/iccp_cinematic_v10_production.blend -s <next frame> -e 624 -a

Do not restart from frame 1 unless the frame directory is intentionally discarded after explicit approval.
## 9. RECOVERY AFTER CHAT / REMOTE-DESKTOP DISCONNECT

First action in a new chat:
- Reconnect Remote Desktop Commander.
- Verify the device is online.
- Verify repository path and current branch.
- Verify current HEAD.
- Count rendered v10 PNG frames.
- Check whether a Blender process is still rendering v10.
- Do NOT launch a second render until process state is known.

PowerShell progress check:
$root='C:\GitHub\soubel-iccp-v5-cleanstart'
$dir=Join-Path $root 'blender\v10_frames'
$count=(Get-ChildItem $dir -Filter 'frame_*.png' -ErrorAction SilentlyContinue | Measure-Object).Count
Write-Output ('COUNT='+$count)
Get-CimInstance Win32_Process | Where-Object {$_.CommandLine -like '*iccp_cinematic_v10_production.blend*'} | Select-Object ProcessId,CommandLine

If Blender is still rendering:
- Leave it alone.
- Monitor frame count only.

If Blender is no longer rendering and count is less than 624:
- Find the highest completed frame.
- Restart from the NEXT frame only.
- Example: if highest is frame_0317.png, restart with -s 318 -e 624 -a.
- Never overwrite earlier completed frames unless there is evidence they are corrupt.
## 10. FINAL MOVIE ASSEMBLY

Encoder script:
blender/encode_v10_production.py

The encoder was tested against the first 24 production PNG frames and successfully created an H.264 MP4.

The encoder contains a hard missing-frame guard:
- It verifies all 624 frames exist.
- If any frame is missing, it exits instead of creating a partial movie.

Final production target:
blender/iccp_cinematic_v10_production_720p24.mp4

Do NOT encode until frame count is 624.

After frame 624 exists:
1. Run blender/encode_v10_production.py in Blender background/factory-startup mode.
2. Confirm output MP4 exists and has a nontrivial file size.
3. Open the MP4 in Chrome.
4. Review the complete movie once from beginning to end.
5. Specifically verify the negative-return animation still travels pipe -> rectifier.
6. Verify the generic work truck is visible, not the hidden old truck.
7. Verify the reference electrode remains separate from the pipe.
8. Verify the mastic-covered pipe connections read correctly.
## 11. FINAL SOUBEL BRANDING — REQUIRED FUTURE STEP

Helen explicitly requested:
- Add SOUBEL.com along the bottom of the FINAL version.
- Consider adding the SOUBEL logo as well.

Important:
Do NOT bake branding into the current 624-frame Blender production render.
Add branding during final movie assembly / post-production so visual branding can be adjusted without rerendering the entire 3D sequence.

Existing transparent branding assets found in the repository:
- assets/soubel-logo-horizontal.png — 640 x 113, 32-bit ARGB. Best current full horizontal logo candidate.
- assets/soubel-header-emblem-v6.png — 240 x 124, 32-bit ARGB.
- assets/soubel-header-text-v6.png — 420 x 67, 32-bit ARGB.
- assets/soubel-header-v3-rgba.png — 600 x 106, 32-bit ARGB.

Branding instruction:
- SOUBEL.com text is REQUIRED in the final version.
- Logo inclusion is desired/likely, but placement and exact treatment should be visually reviewed before final lock.
- Keep branding refined and unobtrusive. It should not cover technical features, current-flow cues, or labels.
- Prefer lower-edge placement with safe margins.
- Do not regenerate the logo with AI.
- Use the existing approved transparent asset.
## 12. NEXT ACTIONS AFTER RECOVERY

Immediate priority is NOT more redesign.

Proceed in this order:
1. Verify whether the active v10 frame render is still running.
2. If running, leave it alone until complete.
3. If stopped early, resume from the first missing frame.
4. When all 624 PNG frames exist, run the tested v10 encoder.
5. Open and review the completed v10 720p/24 fps movie.
6. Confirm technical motion: positive side, groundbed, soil-to-pipeline current, pipeline cue, pipe-to-rectifier negative return, and separate measurement cues.
7. Confirm visual corrections: generic work truck, flat black cadweld/mastic mounds, separate reference electrode, technician, utility pole offset.
8. Add SOUBEL.com branding in post-production.
9. Evaluate whether to include the horizontal SOUBEL logo with the URL.
10. Only after Helen approves the complete branded movie should a final web-delivery export be prepared.
11. Do not publish or integrate into soubel.com without explicit approval.

Current live snapshot when this handoff was finalized:
- v10 production frames present: 230 / 624
- Production render process: RUNNING
- Snapshot time: September 19, 2026, approximately 11:30 PM Central
- This number is only a recovery snapshot. Always recount on restart.
## 13. KNOWN FAILURE MODES / THINGS NOT TO DO

- Do not use AI image generation to "fix" the truck, cadwelds, technician, reference electrode, or other technical geometry.
- Do not recreate the scene from screenshots.
- Do not revert to the old three-armed technician image.
- Do not reintroduce the old mixed-brand / visually inconsistent truck.
- Do not animate the blue negative return rectifier -> pipe. The correct conventional-current return is pipe -> rectifier.
- Do not imply the reference-electrode lead carries the ICCP return current.
- Do not make the pipeline fill the frame during the below-grade sequence.
- Do not move the utility pole back next to the rectifier.
- Do not collapse the side-offset groundbed into the pipeline trench.
- Do not convert the flat mastic-covered pipe connections back into upright posts.
- Do not run multiple Blender production renders against the same frame range/output directory at the same time.
- Do not assume a Remote Desktop tool timeout means Blender stopped; inspect the real Blender process first.
- Do not encode the production MP4 before all 624 PNG frames exist.
- Do not git-add the entire blender/assets cache or render-frame directory unless intentionally required.
- Do not git clean the worktree.
- Do not publish to the live site without Helen's explicit approval.

This handoff is designed so the next chat can continue without asking Helen to reconstruct today's decisions.
