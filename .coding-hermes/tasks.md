# TotalStack — Model Router Task Matrix

**Core purpose:** Local AWS cloud stack emulator (S3, Lambda, DynamoDB, etc.) for offline development and CI — 76 services, 1864 integration tests, Docker-based.

## Active Tasks

| ID | Task | Priority | Complexity | Deps | Tags | Model | Reasoning | Fallback |
|----|------|----------|------------|------|------|-------|-----------|----------|
| WIRING-PLUX | Wire totalstack providers to plux.ini — 70 services with no registry entries | High | 3 (integration) | — | +wiring, +integration | DeepSeek V4 Pro | Providers exist (shape-validated) but LocalStack won't load them without plux.ini entries | GLM-5.2 |
| DUCKBRAIN-SYNC | Populate DuckBrain with totalstack fleet status, architecture, pitfalls | Medium | 2 (content) | — | +duckbrain | DeepSeek V4 Pro | Zero entries in DuckBrain; no institutional memory | GLM-5.2 |
| CI-003 | Push 40 unpushed commits and verify CI on fork (**BLOCKED**) | Medium | 1 (admin) | — | +terminal | — | AGENTS.md forbids `git push` from agent; requires human/explicit override | — |
| NEVER-DONE | 11-point audit sweep | High | 2 | — | ++code-review, +testing | DeepSeek V4 Pro | Audit runs every tick | GLM-5.2 |

**Assumptions:** 1864/1864 integration tests pass locally; 76/76 services pass shape validator; 40 commits unpushed; fork CI requires manual push; AWS credential workflows disabled on fork. All CI failures resolved in unpushed commits — no code changes needed.

**Routing Notes:** 3 remaining tasks. WIRING-PLUX (70 providers not in plux.ini), DUCKBRAIN-SYNC (zero DuckBrain entries), CI-003 (BLOCKED on human push). CI-FAILURE investigation complete: shape validator failures (39→76 resolved in 40 unpushed commits), integration test failures (bedrock-agent DELETING assertion fixed in e5730fb6e), GitReins guard PASS. CI-003 updated to 40 commits.

**Execution Order:** WIRING-PLUX (integration) → DUCKBRAIN-SYNC (documentation). CI-003 remains blocked.

**Escalation Conditions:** WIRING-PLUX reveals provider incompatibilities → create INTEGRATION tasks.

**Scheduler Health:** CooldownS=1800s (default), Enabled=true, Provider=deepseek-foreman. 40 commits unpushed (was 37/38). CI-FAILURE investigation complete — all 3 consecutive red runs caused by unpushed commits, not code regressions.

## Completed Summary

**CI-GAP-064:** All 76 services pass shape validation. Fixed 8 remaining services (36→0 errors) via test_inputs additions and Speclang model corrections. Final batch: emr(12), athena(13), network-firewall(3), rds(3), glue(1), fis(1), organizations(1), grafana(2). Total CI-GAP sprint: 63→76 services, 87→0 errors across multiple ticks.
**CI-FIX (Integration Tests):** 6 fixes for amp, fsx, kafka, sesv2, verifiedpermissions, fsx regression. Shape-parity alignment (CI-FIX-011: adapted all 6 test files to AWS-correct model shapes).
**Infrastructure:** 74 per-service test_inputs/*.py files (QUALITY-001 refactor, 5350→400 lines). All CI workflows modernized.
**Quality:** CONTRIBUTING.md (147 lines). 1864/1864 integration tests local green baseline.
**Security:** PITFALL-GITLEAKS — narrowed .gitleaks.toml allowlist (be6b13ecd). Removed 5 broad patterns (specs/, docs/, *.md, *.spec.md, tests/). 8,162 commits re-scanned clean.
**CI Status:** Local all green. 40 unpushed commits. Fork push events need manual trigger. CI-FAILURE investigation: all 3 consecutive red runs (Jul 19) caused by 40 unpushed commits — shape validator 39→76 fixed in CI-GAP-064, bedrock-agent DELETING assertion fixed in e5730fb6e. GitReins guard PASS. No code changes needed.

## [x] CI-FAILURE — CI investigation: all 3 red runs caused by 40 unpushed commits (2026-07-21)
## [x] PITFALL-GITLEAKS — Narrowed .gitleaks.toml allowlist (be6b13ecd)
## [x] CI-GAP-064 — Shape validator: 76/76 services pass (c8053630d)
## [ ] NEVER-DONE — Run coding-hermes-never-done 11-point audit
