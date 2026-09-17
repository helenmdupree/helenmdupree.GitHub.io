# SOUBEL Website Session Checkpoint — 2026-09-16

## 1. Purpose

This is the end-of-session recovery record for the public SOUBEL website after the 2026-09-16 architecture, navigation, Knowledge Library, Home/About, AIM, search, and content-page standardization work.

Use this file to resume safely in a new chat or work session without reconstructing decisions from conversation memory.

**Repository truth is authoritative.**

## 2. Authoritative public state

- Repository: `helenmdupree/helenmdupree.GitHub.io`
- Public branch: `main`
- Known-good public checkpoint at session close: `2535c8ec3253e1baba6a4cda73f250eab7570d33`
- Latest public PR: **#56 — Standardize SOUBEL content page heroes**
- PR #56 passed **SOUBEL Public Pre-Publish Gate #72** before merge.
- Public site: `https://soubel.com/`

If `main` is newer than the checkpoint above, inspect every newer commit/PR before making changes. The checkpoint is a known-good reference, **not a rollback target**.

## 3. Public releases completed during this workstream

- PR #47 — Markets overview, Utilities, and Midstream refinements.
- PR #48 — Analysis & Perspectives editorial refresh.
- PR #49 — Midstream hero alignment.
- PR #50 — Homepage hero transition spacing.
- PR #51 — Center/simplify homepage Operational Trust section.
- PR #52 — Knowledge Library V2.
- PR #53 — Home/About refresh and global-search reconciliation.
- PR #54 — Pipeline Integrity / AIM architecture reconciliation.
- PR #55 — Homepage + AIM polish and Operational Trust™ treatment.
- PR #56 — Shared content/repository hero standard.

Do not recreate these changes from memory. They are already in public `main`.

## 4. Current site architecture decisions

### Public top navigation
Current foreground navigation is built around:
- Home
- Markets
- Expertise
- Oil & Gas AI Lab
- Ask SOUBEL
- Knowledge
- About
- Search icon

Generic **Industry Intelligence** is not a foreground navigation destination. The Oil & Gas AI Lab remains its own public top-level item.

The standalone **Operational Trust** destination has been retired from foreground navigation. Operational Trust™ remains a named SOUBEL concept/standard across the site.

### Knowledge architecture
The Knowledge Library is a compact technical front door, not a giant A–Z wall of topics.

The A–Z topic taxonomy is retained behind the foreground experience for future Ask SOUBEL/manual-browse support. It is not deleted.

AIM relationship:
- Asset Integrity Management expertise page = management/framework hub.
- AIM Technical Knowledge = Knowledge Library router.
- Pipeline Integrity, Tank & Terminal Integrity, Corrosion & CP, Asset Performance, Digital & AI = technical depth branches.
- AIM subpages = framework deep dives.
- Resources = practical tools.

### Global search
The search icon is a sitewide search interface. Its index was reconciled to current architecture in PR #53.
Search state must reset when the overlay closes and each time it reopens. Do not reintroduce retired/deferred routes into search without an architecture decision.

## 5. Standing design standard

Read `docs/CONTENT_PAGE_HERO_STANDARD_2026-09-16.md`.

For content/repository pages, the standard opening pattern is:
- SOUBEL masthead
- primary navigation
- white content hero
- readable teal eyebrow/kicker
- controlled dark H1 size (not billboard/monster scale)
- readable gray lead copy
- consistent left alignment, width, and spacing
- no redundant breadcrumb inside the hero unless it has a real navigation purpose

Pages standardized in PR #56:
- `/resources/`
- `/analysis-perspectives/`
- `/knowledge-library/corrosion-cathodic-protection/`
- `/knowledge-library/asset-integrity-management/`

Shared stylesheet: `assets/site-content-family-v1.css`

## 6. Home / About decisions already public

### Homepage
- Removed the redundant About / Intelligence Platform closing block.
- Tightened hero spacing so the supporting sentence is visible on initial load.
- Homepage Operational Trust section was simplified, centered, and stripped of the retired standalone Operational Trust link.
- Prominent branded uses apply **Operational Trust™**.

### About
- Layout refreshed and narrowed for better visual balance.
- Monster title sizing corrected.
- Professional Development / Continuous Learning section tightened.
- Technology & Information Systems is explicitly framed as a **Current Education Track**, not as mastered expertise.
- Founder and professional-development sections have reduced excess whitespace.

## 7. AIM / Pipeline architecture already public

Read `docs/PIPELINE_AIM_LINK_ARCHITECTURE_2026-09-16.md`.

Important rules:
- Pipeline Integrity knowledge page keeps its useful page-section dropdown.
- Pipeline Integrity links go directly to the canonical Asset Integrity Management expertise hub where appropriate.
- AIM Technical Knowledge is explicitly distinct from the AIM expertise/framework hub.
- Retired `/expertise/pipeline-asset-integrity/` should not be reintroduced as a foreground route.
- Retired standalone Operational Trust calls-to-action were removed from the audited AIM family.
- The AIM hub no longer includes the AIM Decision Cycle visual/section or arrow-flow strip.
- AIM hero uses meaningful deeper destinations instead of one-inch in-page jumps.
- Avoid decorative arrow-flow diagrams. The user explicitly dislikes them.

## 8. Knowledge Library decisions already public

Read `docs/KNOWLEDGE_LIBRARY_V2_ARCHITECTURE_2026-09-16.md`.

Key points:
- The old huge-card layout was replaced with a compact knowledge-area structure.
- Six active knowledge destinations are foregrounded.
- Developing subject shells exist for future expansion rather than pretending every subject is complete.
- The user intentionally removed some proposed subjects that did not fit her expertise/architecture.
- Integrity Software & Data Management remains within the integrity window rather than being automatically removed merely because Digital & AI exists.
- The foreground Knowledge Library search box was removed; global site search remains available via the search icon.

## 9. Analysis & Perspectives decisions already public

This is a living editorial repository, not an "archive."

Structure:
- 1 Featured Article.
- Up to 10 Recent Articles.
- Newest article becomes Featured; prior Featured moves to Recent.
- Article URLs remain stable.
- Deeper repository/index architecture can be added later as volume grows.
- Integrity Shift series thumbnails are preserved.

Current positioning line and structure should not be replaced casually; audit the existing page first.

## 10. Unpublished local work remaining at session close

These items are **NOT public at this checkpoint** and must be re-verified against current `origin/main` before publication.

### A. Integrity Methods AIM subpage
Local review copy contains an approved removal of the redundant button:
- Remove `Explore the method families` because it only jumps a few inches to the immediately following section.
- Keep `Return to AIM`.

Local file used during review:
`C:\Users\winst\OneDrive\Desktop\soubel-polish-review-20260916\expertise\asset-integrity-management\integrity-methods\index.html`

Do not copy that entire stale worktree into main. Reapply the single approved change surgically from current `origin/main`.

### B. Tank & Terminal Integrity page
Local review copy contains an approved contrast fix:
- White cards inside a dark section had beige/white headings that were unreadable.
- Approved fix: dark heading/body text on white cards while preserving teal eyebrows and the surrounding dark section.

The user also approved a title change in the lifecycle section:
- Replace `A terminal should remember what changed.`
- With `Lifecycle & Decision Continuity`

**Important:** at session close, that title replacement had been discussed/approved but the checked local file still showed the old title. Treat it as approved-but-not-yet-implemented, not completed.

The user also wanted the lifecycle graphic made smaller because it feels massive. Placement is conceptually correct inside the Lifecycle & Decision Continuity section, but the visual should be reduced and centered. This size reduction was discussed but was not confirmed implemented at session close.

Local review file:
`C:\Users\winst\OneDrive\Desktop\soubel-polish-review-20260916\knowledge-library\tank-terminal-integrity\index.html`

Again: reapply only approved changes from current `origin/main`; do not publish the full stale local worktree.

## 11. Corrosion & CP page status

Already public in PR #56:
- H1 size brought under the shared content-page standard.
- Hard-coded title line break removed so wrapping is natural.
- Source Discipline closing block now reads:
  - `SOURCE DISCIPLINE`
  - `Use the right source for the decision.`
- Supporting copy was simplified to clarify SOUBEL's role without awkward or legalistic language.

Do not regenerate screenshots or image mockups when the request is to edit the live/local HTML/CSS page. Edit the actual source.

## 12. Worktree / publication discipline

The local review worktree `soubel-polish-review-20260916` is **not** a safe source of truth for wholesale publication. It sits on an older branch and contains review artifacts and unpublished edits.

Required publication method:
1. Fetch current `origin/main`.
2. Create a clean isolated worktree/branch from current `origin/main`.
3. Reapply only the reviewed change(s).
4. Inspect `git diff --name-status` and the actual diff.
5. Exclude screenshots, helper files, stale static navigation, and unrelated work.
6. Push the isolated branch.
7. Open a PR.
8. Confirm the changed-file list is exactly expected.
9. Wait for **SOUBEL Public Pre-Publish Gate** success.
10. Merge only on green.
11. Wait for GitHub Pages propagation.
12. Verify the live HTML/CSS itself, not merely the merge state.

Never use `git reset` or overwrite newer work merely because a dated checkpoint exists. A checkpoint is a recovery reference, not permission to roll back later changes.

## 13. Parallel SOUBEL systems are separate governed workstreams

Do not casually mix public-site editing with private-engine development.

Separate workstreams include:
- Ask SOUBEL
- Oil & Gas AI Lab
- Regulatory Scout
- WhoQual-IQ
- Golden Answers / governed knowledge
- public website

For private-engine work, repository truth and that workstream's own recovery pointer govern. Do not mutate those systems as a side effect of website editing.

Oil & Gas AI Lab / Regulatory Scout governance remains separate; Regulatory Scout is not to be activated, scheduled, or made live without explicit approval.

Ask SOUBEL public presentation may consume governed outputs, but public-site layout work must not silently alter Approved Knowledge, Golden Answers, Trust Trails, WhoQual-IQ, or private research state.

## 14. Brand / editorial rules to preserve

- SOUBEL is positioned primarily around **oil & gas**, with adjacent energy infrastructure context. Do not make "industrial" the primary headline identity.
- Use **Operational Trust™** in prominent branded uses where it functions as the named SOUBEL concept/standard. Do not plaster ™ on every casual descriptive mention.
- Avoid em dashes in user-facing copy where possible.
- Avoid giant H1s, tiny eyebrows, unreadable pale text, massive empty whitespace, and decorative one-inch jump buttons.
- Avoid arrow-flow diagrams unless the user explicitly requests one.
- Prefer concise headings; do not turn every section title into an explanatory sentence.
- Keep visual hierarchy consistent across related page families.
- Do not reintroduce retired routes merely because old static HTML still contains them; check canonical navigation and current site.js behavior.

## 15. Resume order for the next website session

Recommended first tasks:
1. Verify current `origin/main` and inspect anything newer than this checkpoint.
2. Read `docs/WEBSITE_RECOVERY_LATEST.md` and this checkpoint in full.
3. Verify public pages still match the PR #56 design standard.
4. Create a clean review branch/worktree for the two remaining approved local edits only:
   - Integrity Methods: remove redundant `Explore the method families` jump button.
   - Tank & Terminal Integrity: preserve contrast fix; implement approved lifecycle heading `Lifecycle & Decision Continuity`; reduce/center lifecycle graphic after visual review.
5. Review Tank & Terminal page in the browser before publishing.
6. Publish through the normal gate only after approval.

Do not begin a new broad redesign before these pending reviewed items are reconciled.

## 16. Recovery principle

**SUBSTANTIVE DECISION -> DOCUMENT / COMMIT -> GITHUB CHECKPOINT -> RECOVERY RECORD**

The goal is that a new chat can reconstruct the state from the repository and this checkpoint without relying on chat memory.

