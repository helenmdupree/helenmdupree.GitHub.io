# SOUBEL Website End-of-Day Handoff

**Session close:** 2026-09-16
**Resume date:** 2026-09-17
**Repository:** `helenmdupree/helenmdupree.GitHub.io`
**Authoritative branch:** `main`
**Public checkpoint at close:** `db4eb13ca2f5ab22075f3a6bf0a961db71db8171`
**Latest public PR at close:** #58 — `Remove retired Operational Trust CTA and reduce Resources heading scale`

## Core recovery rule

**REPOSITORY TRUTH > CHAT MEMORY**

Do not rebuild from conversation memory. Fetch current `origin/main`, inspect anything newer than the checkpoint above, then read this handoff and the architecture documents it references.

## Tomorrow's first development focus

Resume with the **Downstream & Refining segment under Markets**:

`/markets/downstream-refining/`

Do not start a broad redesign elsewhere first. Audit the Downstream page as a connected Markets page, compare it with the already-refined Markets and Midstream patterns, and preserve existing architecture unless there is a documented reason to change it.

The Downstream Practical Resources section was just cleaned in PR #58. The retired standalone `Operational Trust` button is gone; only the Resources CTA remains.

## Public work completed today

Major published checkpoints include PRs #47 through #58. The most recent public state includes:

- Markets/Midstream refinements and hero alignment.
- Analysis & Perspectives editorial refresh.
- Homepage spacing and Operational Trust™ cleanup.
- Knowledge Library V2 architecture and global search reconciliation.
- Home/About refresh and AIM/Pipeline architecture reconciliation.
- AIM hero polish, removal of redundant in-page jump buttons, removal of arrow-flow / Decision Cycle visuals, and Operational Trust™ treatment.
- Shared content/repository hero standard across Resources, Analysis & Perspectives, Corrosion & CP Knowledge, and AIM Technical Knowledge.
- Downstream Practical Resources cleanup and Resources heading-size correction in PR #58.

Read these before touching linked systems:

1. `docs/WEBSITE_RECOVERY_LATEST.md`
2. `docs/backups/20260916-website-session/WEBSITE_SESSION_CHECKPOINT_2026-09-16.md`
3. `docs/CONTENT_PAGE_HERO_STANDARD_2026-09-16.md`
4. `docs/PIPELINE_AIM_LINK_ARCHITECTURE_2026-09-16.md`
5. `docs/KNOWLEDGE_LIBRARY_V2_ARCHITECTURE_2026-09-16.md`
6. `docs/GLOBAL_SEARCH_AUDIT_2026-09-16.md`
7. `docs/ABOUT_HOME_REFRESH_ARCHITECTURE_2026-09-16.md`

## Important unpublished local work

A reviewed spacing edit exists for:

`/expertise/commercial-growth-strategic-accounts/playbook-system/`

The intended change reduces only the excessive vertical spacing around the three playbook sections: `The First 90 Days`, `From Market Signal to Revenue`, and `SOUBEL SCALE™`. Hero, operating philosophy, and final handoff spacing remain unchanged.

Local reviewed worktree:

`C:\Users\winst\OneDrive\Desktop\soubel-playbook-spacing2-20260916`

This edit is **NOT public** at this checkpoint. Reapply or verify it from current `origin/main` before publishing. Do not publish that entire old worktree wholesale.

## OneDrive / worktree safety rule

A OneDrive mass-delete warning appeared after temporary Git worktrees were created/cleaned under `OneDrive\Desktop`. The user correctly selected **Keep**. File and Git checks afterward showed the repositories and key files remained present.

From this point forward:

- Temporary review/publish worktrees belong under `C:\GitHub\...`, not OneDrive.
- Do not clean up the existing OneDrive worktrees casually.
- Do not delete hundreds of OneDrive files in response to Git worktree cleanup.
- Use clean isolated branches from current `origin/main` for publication.

## Standing publication discipline

For every public edit:

1. Fetch current `origin/main`.
2. Create a clean isolated worktree under `C:\GitHub\...`.
3. Apply only the reviewed change.
4. Inspect `git diff --name-status` and the actual diff.
5. Exclude screenshots, stale review artifacts, and unrelated changes.
6. Push and open a PR.
7. Confirm the PR file list is exact.
8. Wait for the **SOUBEL Public Pre-Publish Gate** to succeed.
9. Merge only after green.
10. Wait for GitHub Pages propagation.
11. Verify live HTML/CSS, not just GitHub merge state.

## Separate development systems

The public website is not the same governed workstream as Ask SOUBEL, Oil & Gas AI Lab, Regulatory Scout, WhoQual-IQ, or governed knowledge / Golden Answers. Do not alter those systems as a side effect of website work. Each has its own repository truth and recovery pointer.

## Design rules repeatedly confirmed by the user

Avoid monster H1s, tiny eyebrows, unreadable pale text, giant cards, huge blank vertical gaps, pointless buttons that scroll only a few inches, and decorative arrow-flow diagrams. Prefer concise titles, moderate readable typography, strong contrast, tighter section rhythm, meaningful navigation, and oil & gas-first positioning.

Use **Operational Trust™** in prominent branded uses where it functions as the named SOUBEL concept/standard. Do not reintroduce the retired standalone Operational Trust foreground destination.

## Resume instruction

Tomorrow: verify repository state first, then begin with the **Downstream & Refining Markets page audit**. Report what is already present and how it relates to Markets/Midstream before editing. Preserve the current connected architecture and publish only reviewed changes through the normal gate.
