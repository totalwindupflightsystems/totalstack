# TotalStack — Model Router Task Matrix

**Core purpose:** Local AWS cloud stack emulator (S3, Lambda, DynamoDB, etc.) for offline development and CI — 76 services, 1864 integration tests, Docker-based.

## Active Tasks

| ID | Task | Priority | Complexity | Deps | Tags | Model | Reasoning | Fallback |
|----|------|----------|------------|------|------|-------|-----------|----------|
| CI-003 | Push 40 unpushed commits and verify CI on fork (**BLOCKED**) | Medium | 1 (admin) | — | +terminal | — | AGENTS.md forbids `git push` from agent; requires human/explicit override | — |
| NEVER-DONE | 11-point audit sweep | High | 2 | — | ++code-review, +testing | DeepSeek V4 Pro | Audit runs every tick | GLM-5.2 |

## Idle Tick #4 — Self-Pause 2026-07-21 20:48

**Cooldown reversion #2:** Scheduler showed CooldownS=1800 (30m) instead of 43200 (12h) set by prior tick. Cause: daemon restart → TOML default overwrote API PUT. Re-fixed to 43200s via PUT. Verified: GET shows CooldownS=43200, Enabled=True.

**NEVER-DONE 11-point audit:**
- ✅ Check 1 (SPEC): 1494 spec files, 1996 assembled .code.py files, 63 service spec dirs, 69/71 services have provider.py
- ✅ Check 2 (DOC): AGENTS.md comprehensive (14,800 chars)
- ✅ Check 3 (TEST): 414 integration test files, ~25,359 tests (5 pre-existing collection errors)
- ⚠️ Check 4 (DEPS): 20+ outdated packages. `typeguard 2.13.3→4.5.2` (blocked), `pydantic-core` blocked at 2.46.4 (pydantic constraint). No new actionable deps — same as prior ticks.
- ✅ Check 5 (PITFALL): 618 TODO/FIXME in test files only (expected for AWS emulator). Gitleaks allowlist already narrowed. No new stubs or vulnerabilities.
- ✅ Check 6 (PERF): N/A (emulator project, no benchmarks)
- ⚠️ Check 7 (ENDPOINTS): Docker not running (dev tool, not live service). 69/71 services have provider.py — well-covered.
- ⚠️ Check 8 (CI): AWS/Archive ✅, upgrade-python-dependencies ❌ (pre-existing). 47 unpushed commits (CI-003 BLOCKED).
- ✅ Check 9 (DUCKBRAIN): 7 entries, consistent with DUCKBRAIN-REPOPULATE.
- ✅ Check 10 (CODE QUALITY): Clean worktree, .gitignore has 83 lines (`.coverage` covered). No untracked artifacts.
- ✅ Check 11 (WIRING): 274 provider registrations in providers.py. Well-wired.

**GitReins:** All 15 tasks complete — board consistent.

**Finding: 0 new tasks.** 3 pre-existing issues (DEPS, CI failure, unpushed commits) are deferred or blocked.

**Board fix:** Removed stale DUCKBRAIN-REPOPULATE from Active table (already `[x]` in Completed).

**Counter: 4/7 idle ticks.** Cooldown at 12h. At 7 idle ticks → escalate to Bane.

**Scheduler Health:** CooldownS=43200s (12h), Enabled=True. Reversion #2 (re-fixed this tick).

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
