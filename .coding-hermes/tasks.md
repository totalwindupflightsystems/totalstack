# TotalStack — Model Router Task Matrix

**Core purpose:** Local AWS cloud stack emulator (S3, Lambda, DynamoDB, etc.) for offline development and CI — 76 services, 1864 integration tests, Docker-based.

## Active Tasks

| ID | Task | Priority | Complexity | Deps | Tags | Model | Reasoning | Fallback |
|----|------|----------|------------|------|------|-------|-----------|----------|
| DUCKBRAIN-REPOPULATE | Repopulate DuckBrain totalstack namespace (1 entry found, prior tick claimed 29) | Medium | 1 (content) | — | +duckbrain | DeepSeek V4 Pro | Only 1 entry (`/projects/totalstack/investigation/ci-failure-2026-07-19`) exists; prior tick claimed 29 entries populated. Entries likely written to wrong namespace (hermes-dagger was current default at write time — known DuckBrain pitfall). Repopulate with architecture, fleet status, milestones, patterns, test fixes. | — |
| CI-003 | Push 40 unpushed commits and verify CI on fork (**BLOCKED**) | Medium | 1 (admin) | — | +terminal | — | AGENTS.md forbids `git push` from agent; requires human/explicit override | — |
| NEVER-DONE | 11-point audit sweep | High | 2 | — | ++code-review, +testing | DeepSeek V4 Pro | Audit runs every tick | GLM-5.2 |

## Idle Tick #3 — Self-Pause 2026-07-21 18:48

**Discovery sweep:** 0 new tasks. No TODOs/FIXMEs. 25,359 tests collected (5 pre-existing collection errors). 18 outdated deps (deferred — same as prior tick). CI: AWS/Archive ✅, upgrade-python-dependencies ❌ (pre-existing). 42 unpushed commits. CI-003 remains BLOCKED.

**Self-pause:** Board only has NEVER-DONE after 3 consecutive idle ticks. Set scheduler cooldown to 12h (43200s). Verified: GET shows CooldownS=43200, Enabled=True.

**Counter: 3/7 idle ticks.** At 7 idle ticks → escalate to Bane for project review.

**Scheduler Health:** CooldownS=43200s (12h), Enabled=True, Provider=deepseek-foreman.

**Hilo=useful** (12,232 edges, 1,664 files). **GitReins:** All 15 tasks complete, board consistent.

## Completed Summary

**WIRING-PLUX:** Wired 68 totalstack providers to plux.ini (68 entries added). Commit: 831221031.
**CI-GAP-064:** Shape validator: 76/76 services pass (c8053630d).
**CI-FAILURE:** CI investigation: all 3 red runs caused by 40 unpushed commits (2026-07-21).
**PITFALL-GITLEAKS:** Narrowed .gitleaks.toml allowlist (be6b13ecd).
**DUCKBRAIN-SYNC:** ~~Claimed 29 entries populated~~ — VERIFIED FALSE: only 1 entry exists. Repopulation needed (DUCKBRAIN-REPOPULATE).

## [x] WIRING-PLUX — Wired 68 totalstack providers to plux.ini (831221031)
## [x] CI-FAILURE — CI investigation: all 3 red runs caused by 40 unpushed commits (2026-07-21)
## [x] PITFALL-GITLEAKS — Narrowed .gitleaks.toml allowlist (be6b13ecd)
## [x] CI-GAP-064 — Shape validator: 76/76 services pass (c8053630d)
## [x] DUCKBRAIN-REPOPULATE — 7 entries populated (overview, architecture, cron, pitfalls, milestones, patterns/speclang-pipeline, investigation) (aed420e5f)
## [ ] NEVER-DONE — Run coding-hermes-never-done 11-point audit
