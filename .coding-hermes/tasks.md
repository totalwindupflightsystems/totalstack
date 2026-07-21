# TotalStack — Model Router Task Matrix

**Core purpose:** Local AWS cloud stack emulator (S3, Lambda, DynamoDB, etc.) for offline development and CI — 76 services, 1864 integration tests, Docker-based.

## Active Tasks

| ID | Task | Priority | Complexity | Deps | Tags | Model | Reasoning | Fallback |
|----|------|----------|------------|------|------|-------|-----------|----------|
| CI-GAP-064 | Fix shape validator for 13 failing services (87 total errors) | Medium | 5 | — | ++code-generation, ++debugging, +testing | GLM-5.2 | 87 MISSING_REQUIRED/EXTRA shape errors across 13 services; PascalCase↔camelCase key mismatches; well-understood pattern from CI-GAP-054/055 | DeepSeek V4 Pro |
| CI-003 | Push 29 unpushed commits and verify CI on fork | Medium | 1 (admin) | — | +terminal | — | AGENTS.md forbids `git push` from agent; requires human/explicit override | — |
| NEVER-DONE | 11-point audit sweep | High | 2 | — | ++code-review, +testing | DeepSeek V4 Pro | Audit runs every tick | GLM-5.2 |

**Assumptions:** 1864/1864 integration tests pass locally; 63/76 services pass shape validator; 29 commits unpushed; fork CI requires manual push; AWS credential workflows disabled on fork.

**Routing Notes:** Only 2 open tasks — CI-GAP-064 is the remaining shape validator batch (well-understood pattern from 55+ prior CI-GAP fixes). CI-003 is blocked on push policy. Board nearly clean after massive CI-GAP sprint.

**Execution Order:** CI-GAP-064 → CI-003 (when unblocked).

**Escalation Conditions:** Shape validator fix introduces new integration test failures → escalate to CI-FIX pattern (adapt tests, don't revert shapes). Service model changes touch >2 files → split into per-service subtasks.

## Completed Summary

**CI-FIX (Integration Tests):** 6 fixes for amp, fsx, kafka, sesv2, verifiedpermissions, fsx regression. Shape-parity alignment (CI-FIX-011: adapted all 6 test files to AWS-correct model shapes).
**CI-GAP (Shape Validator):** 55+ services fixed — 96% of original errors were HANDLER_CRASH from missing test inputs. Started at 6/76 pass (1213 errors), now at 63/76 pass (87 remaining). Key patterns: service-prefixed keys to avoid dictionary collisions, lambda test inputs for prerequisite resources, PascalCase→camelCase model fixes. Load_store bug fixed (case-insensitive service name matching).
**Infrastructure:** 74 per-service test_inputs/*.py files (QUALITY-001 refactor, 5350→400 lines). All CI workflows modernized.
**Quality:** CONTRIBUTING.md (147 lines). 1721 integration tests local green baseline, now 1864/1864 after CI-FIX-011.
**CI Status:** Local all green. 29 unpushed commits. Fork push events need manual trigger.

## [ ] NEVER-DONE — Run coding-hermes-never-done 11-point audit
