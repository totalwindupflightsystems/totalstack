# TotalStack — Model Router Task Matrix

**Core purpose:** Local AWS cloud stack emulator (S3, Lambda, DynamoDB, etc.) for offline development and CI — 76 services, 1864 integration tests, Docker-based.

## Active Tasks

| ID | Task | Priority | Complexity | Deps | Tags | Model | Reasoning | Fallback |
|----|------|----------|------------|------|------|-------|-----------|----------|
| CI-FAILURE | Investigate fork CI failures — ci.yml 3 consecutive red (Jul 19) | High | 2 (investigation) | — | +ci, +terminal | DeepSeek V4 Pro | Fork CI failing on board-update + code-fix commits; needs root cause | GLM-5.2 |
|| PITFALL-GITLEAKS | ~~Narrow .gitleaks.toml allowlist — remove specs/, docs/, *.md, tests/ from paths~~ | High | 1 (config) | — | +security, +config | DeepSeek V4 Pro | ✅ DONE — be6b13ecd. Removed 5 allowlist entries. 8162 commits re-scanned clean. | — |
| DUCKBRAIN-SYNC | Populate DuckBrain with totalstack fleet status, architecture, pitfalls | Medium | 2 (content) | — | +duckbrain | DeepSeek V4 Pro | Zero entries in DuckBrain; no institutional memory | GLM-5.2 |
| WIRING-PLUX | Wire totalstack providers to plux.ini — 70 services with no registry entries | High | 3 (integration) | — | +wiring, +integration | DeepSeek V4 Pro | Providers exist (shape-validated) but LocalStack won't load them without plux.ini entries | GLM-5.2 |
| CI-003 | Push 37 unpushed commits and verify CI on fork | Medium | 1 (admin) | — | +terminal | — | AGENTS.md forbids `git push` from agent; requires human/explicit override | — |
| NEVER-DONE | 11-point audit sweep | High | 2 | — | ++code-review, +testing | DeepSeek V4 Pro | Audit runs every tick | GLM-5.2 |

**Assumptions:** 1864/1864 integration tests pass locally; 76/76 services pass shape validator; 38 commits unpushed (was 37); fork CI requires manual push; AWS credential workflows disabled on fork.

**Routing Notes:** 3 remaining tasks from NEVER-DONE audit. CI-FAILURE (fork ci.yml 3x red), DUCKBRAIN-SYNC (zero entries), WIRING-PLUX (70 providers not in plux.ini). PITFALL-GITLEAKS completed this tick (be6b13ecd). CI-003 remains blocked on human push.

**Execution Order:** CI-FAILURE (investigate) → WIRING-PLUX (integration) → DUCKBRAIN-SYNC (documentation).

**Escalation Conditions:** CI-FAILURE reveals breaking code regressions → create CI-FIX tasks. WIRING-PLUX reveals provider incompatibilities → create INTEGRATION tasks.

**Scheduler Health:** CooldownS=1800s (default), Enabled=true, Provider=deepseek-foreman. Fork retry errors during audit (host resource pressure). Audit checks 4, 6, 7 skipped due to resource pressure.

## Completed Summary

**CI-GAP-064:** All 76 services pass shape validation. Fixed 8 remaining services (36→0 errors) via test_inputs additions and Speclang model corrections. Final batch: emr(12), athena(13), network-firewall(3), rds(3), glue(1), fis(1), organizations(1), grafana(2). Total CI-GAP sprint: 63→76 services, 87→0 errors across multiple ticks.
**CI-FIX (Integration Tests):** 6 fixes for amp, fsx, kafka, sesv2, verifiedpermissions, fsx regression. Shape-parity alignment (CI-FIX-011: adapted all 6 test files to AWS-correct model shapes).
**Infrastructure:** 74 per-service test_inputs/*.py files (QUALITY-001 refactor, 5350→400 lines). All CI workflows modernized.
**Quality:** CONTRIBUTING.md (147 lines). 1864/1864 integration tests local green baseline.
**Security:** PITFALL-GITLEAKS — narrowed .gitleaks.toml allowlist (be6b13ecd). Removed 5 broad patterns (specs/, docs/, *.md, *.spec.md, tests/). 8,162 commits re-scanned clean.
**CI Status:** Local all green. 38 unpushed commits. Fork push events need manual trigger. Fork ci.yml FAILING (3 consecutive red, Jul 19).

## [x] PITFALL-GITLEAKS — Narrowed .gitleaks.toml allowlist (be6b13ecd)
## [x] CI-GAP-064 — Shape validator: 76/76 services pass (c8053630d)
## [ ] NEVER-DONE — Run coding-hermes-never-done 11-point audit
