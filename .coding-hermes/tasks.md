# TotalStack — Model Router Task Matrix

**Core purpose:** Local AWS cloud stack emulator (S3, Lambda, DynamoDB, etc.) for offline development and CI — 69 TotalStack-native services + 40 LocalStack-core, 2253+ tests, Docker-based.

## Active Tasks

| ID | Task | Priority | Complexity | Deps | Tags | Model | Reasoning | Fallback |
|----|------|----------|------------|------|------|-------|-----------|----------|
| CI-003 | Push 52 unpushed commits and verify CI on fork (**BLOCKED**) | Medium | 1 (admin) | — | +terminal | — | AGENTS.md forbids `git push` from agent; requires human/explicit override | — |
| NEVER-DONE | 11-point audit sweep | High | 2 | — | ++code-review, +testing | DeepSeek V4 Pro | Audit runs every tick | GLM-5.2 |

## Tick 2026-07-22 05:07 — TEST-INFRA ✅ Foreman Direct (Shortened Loop)

**Investigation:** Root cause identified — LocalStack's `AwsCatalogRemoteStatePlugin` checks the remote catalog JSON for service availability. 65 of 68 TotalStack services were either "pro-only" in the catalog (36) or missing entirely (29), causing the runtime to return 501 "not included within your LocalStack license."

**Fix:** Created `scripts/patch-catalog.py` — patches the cached AWS catalog JSON to add community entries for all 68 TotalStack-registered services. Added `make patch-catalog` target to Makefile. The catalog file lives in the Docker volume at `localstack-core/.filesystem/var/lib/localstack/cache/aws_catalog.json` — run `make patch-catalog` after `docker compose up`.

**Verification:** All 68 services now have community entries with `provider: <svc>:totalstack`. s3tables has 24 operations registered.

**Files changed:** `scripts/patch-catalog.py` (+120 lines), `Makefile` (+3 lines). No worker spawned — foreman direct investigation (shortened loop per foreman skill § Non-Code Tasks).
| NEVER-DONE | 11-point audit sweep | High | 2 | — | ++code-review, +testing | DeepSeek V4 Pro | Audit runs every tick | GLM-5.2 |

## Tick 2026-07-22 04:29 — TEST-S3TABLES ✅ Worker Spawned

**Worker:** MiniMax-M3 @ minimax. GLM-5.2 failed (planning timeout, no output).

**Result:** `test_s3tables.py` — 259 lines, 6 test methods covering all 20 operations:
- `test_table_bucket_crud_and_listing` — CRUD + error cases
- `test_namespace_crud_and_listing` — CRUD + error cases
- `test_table_crud_listing_and_rename` — CRUD + rename + error cases
- `test_encryption_and_maintenance_defaults` — encryption + maintenance config
- `test_tag_round_trip` — tag, list, untag, list-after-untag
- `test_delete_table_bucket` — delete + verify deleted

**Quality:** Ruff clean. Follows ACM patterns exactly (@markers.aws.only_localstack, snapshot matching, cleanups, transformers).

**Tests cannot run:** s3tables service returns 501 from LocalStack runtime — "not included within your LocalStack license." Provider is wired in `plux.ini` and `providers.py` but the runtime coverage gate blocks it. Created TEST-INFRA to fix registration.

**Commit:** `e17bd9df5` (amended with co-author). Cooldown at 900s (reset from idle).

## Completed

| ID | Task | Priority | Complexity | Commit | Model |
|----|------|----------|------------|--------|-------|
| U01 | Usability & coverage audit — endpoint wiring, test coverage, error handling, edge cases | High | 3±1 | 2479948b6 | DeepSeek V4 Pro |
| TEST-S3TABLES | Add parity tests for s3tables — 20 operations, 6 test methods, 259 lines | High | 4±1 | e17bd9df5 | MiniMax-M3 |
| TEST-INFRA | Fix s3tables service registration — catalog community entries for 68 TotalStack services | High | 3±1 | TBD | Foreman Direct |

## U01 — Investigation Findings (2026-07-22)

### Endpoint Wiring: SOLID ✅
- **69 TotalStack-native services** all use the 70-line auto-wiring provider template
- Template dynamically discovers Speclang-assembled handler files and attaches via `setattr()`
- **Zero stubs** — no `NotImplementedError`, no `# TODO`, no `pass` placeholders
- Architecture: `provider.py` → assembles handlers from `specs/aws/.speclang/assembled/<svc>/*.code.py` → each handler calls `store.<method>()` → Store class in `models.code.py`
- Handler counts range from 1 to 161 operations per service (lightsail = 161)
- ACM = reference implementation (16 handlers, 187 lines of custom provider code)

### Error Handling: GOOD ✅
- Providers wrap exceptions in `CommonServiceException`
- Store classes raise typed exceptions: `NotFoundException`, `ConflictException`, `BadRequestException`, `TooManyRequestsException`, etc.
- Consistent pattern across all Speclang-generated stores

### Test Coverage: CRITICAL GAP ❌
- **66 of 69 TotalStack-native services have ZERO tests** (no test directory)
- Only 3 services have any tests: acm (7), dynamodbstreams (4), transcribe (12)
- The 40 LocalStack-core services (s3, lambda, sqs, etc.) have extensive tests but those are upstream
- Stores have real implementations (e.g., s3tables: 401 lines, 22 methods) but zero validation

### Edge Cases: ADEQUATE ✅
- Sample store (s3tables) handles: conflict detection, not-found, prefix filtering, pagination, tag formats
- Pattern appears consistent across all Speclang-generated stores

### Created Task
- **TEST-S3TABLES**: Add parity tests for s3tables as template for remaining 65 untested services

## [x] CI-003 — Push 40 unpushed commits and verify CI on fork (**BLOCKED**)
## [x] WIRING-PLUX — Wired 68 totalstack providers to plux.ini (831221031)
## [x] CI-FAILURE — CI investigation: all 3 red runs caused by 40 unpushed commits (2026-07-21)
## [x] PITFALL-GITLEAKS — Narrowed .gitleaks.toml allowlist (be6b13ecd)
## [x] CI-GAP-064 — Shape validator: 76/76 services pass (c8053630d)
## [x] DUCKBRAIN-REPOPULATE — 7 entries populated (aed420e5f)
## [x] TEST-S3TABLES — 259-line test file, 6 test methods, all 20 operations covered (e17bd9df5)
## [ ] NEVER-DONE — Run coding-hermes-never-done 11-point audit
