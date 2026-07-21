# TotalStack — Model Router Task Matrix

**Core purpose:** Local AWS cloud stack emulator (S3, Lambda, DynamoDB, etc.) for offline development and CI — 76 services, 1864 integration tests, Docker-based.

## Active Tasks

| ID | Task | Priority | Complexity | Deps | Tags | Model | Reasoning | Fallback |
|----|------|----------|------------|------|------|-------|-----------|----------|
| CI-003 | Push 32 unpushed commits and verify CI on fork | Medium | 1 (admin) | — | +terminal | — | AGENTS.md forbids `git push` from agent; requires human/explicit override | — |
| NEVER-DONE | 11-point audit sweep | High | 2 | — | ++code-review, +testing | DeepSeek V4 Pro | Audit runs every tick | GLM-5.2 |

**Assumptions:** 1864/1864 integration tests pass locally; 76/76 services pass shape validator; 32 commits unpushed; fork CI requires manual push; AWS credential workflows disabled on fork.

**Routing Notes:** Only 1 open task + NEVER-DONE. CI-003 is blocked on push policy. Board nearly clean — CI-GAP sprint complete (76/76 shape validator, 67→76 services over last 3 ticks).

**Execution Order:** NEVER-DONE audit → CI-003 (when unblocked by human push).

**Escalation Conditions:** CI-003 push triggers new failures → create CI-FIX tasks.

## Completed Summary

**CI-GAP-064:** All 76 services pass shape validation. Fixed 8 remaining services (36→0 errors) via test_inputs additions and Speclang model corrections. Final batch: emr(12), athena(13), network-firewall(3), rds(3), glue(1), fis(1), organizations(1), grafana(2). Total CI-GAP sprint: 63→76 services, 87→0 errors across multiple ticks.
**CI-FIX (Integration Tests):** 6 fixes for amp, fsx, kafka, sesv2, verifiedpermissions, fsx regression. Shape-parity alignment (CI-FIX-011: adapted all 6 test files to AWS-correct model shapes).
**Infrastructure:** 74 per-service test_inputs/*.py files (QUALITY-001 refactor, 5350→400 lines). All CI workflows modernized.
**Quality:** CONTRIBUTING.md (147 lines). 1864/1864 integration tests local green baseline.
**CI Status:** Local all green. 32 unpushed commits. Fork push events need manual trigger.

## [x] CI-GAP-064 — Shape validator: 76/76 services pass (c8053630d)
## [ ] NEVER-DONE — Run coding-hermes-never-done 11-point audit
