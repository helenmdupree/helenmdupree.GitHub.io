# Pipeline Integrity + Asset Integrity Management link architecture

Date: 2026-09-16
Status: APPROVED / PUBLISHED VIA CONTROLLED PR

## Purpose
Keep the AIM and technical-knowledge pages connected without creating ambiguous loops or legacy navigation paths.

## Standing architecture
- `/expertise/asset-integrity-management/` is the primary AIM framework / expertise hub.
- `/knowledge-library/asset-integrity-management/` is the AIM technical-knowledge router.
- `/knowledge-library/pipeline-asset-integrity/` is the Pipeline Integrity technical-depth branch.
- Other Knowledge Library branches provide subject depth for Tank & Terminal Integrity, Corrosion & CP, Asset Performance, and Digital & AI.
- AIM subpages provide framework depth: Application Domains, Evidence to Execution, Governance & Assurance, Asset Lifecycle, and Integrity Methods.
- `/resources/` provides practical decision tools and guides.

## Link-language rule
Use `Asset Integrity Management` or `Explore Asset Integrity Management` only for the expertise/framework hub.
Use `AIM Technical Knowledge` for the Knowledge Library AIM router.
Use subject-specific labels such as `Pipeline Integrity Knowledge` for technical branches.

## 2026-09-16 reconciliation
- Pipeline Integrity hero and decision-test links now point directly to the canonical AIM expertise hub.
- Legacy `/expertise/pipeline-asset-integrity/` links were removed from the audited page family.
- Pipeline Integrity keeps its page-section dropdown unchanged because all anchors resolve correctly.
- The Pipeline Integrity page now distinguishes the AIM framework hub from the AIM technical-knowledge router.
- The AIM hero no longer promotes the retired standalone Operational Trust page; it now links to AIM Technical Knowledge.
- Governance & Assurance follows the same rule.
- Static navigation markup across the AIM family and Pipeline Integrity page was reconciled to the current canonical site navigation.

## Recovery
Before-state copies are stored in `docs/backups/20260916-pipeline-aim-link-audit/`.

