# TotalStack — Model Router Task Matrix

**Core purpose:** Local AWS cloud stack emulator (S3, Lambda, DynamoDB, etc.) for offline development and CI — 69 TotalStack-native services + 40 LocalStack-core, 2253+ tests, Docker-based.

## Active Tasks

| ID | Task | Priority | Complexity | Deps | Tags | Model | Reasoning | Fallback |
|----|------|----------|------------|------|------|-------|-----------|----------|
| CI-003 | Push 40 unpushed commits and verify CI on fork (**BLOCKED**) | Medium | 1 (admin) | — | +terminal | — | AGENTS.md forbids `git push` from agent; requires human/explicit override | — |
| TEST-S3TABLES | Add parity tests for s3tables — 25 operations (20 of 49 AWS), 401-line Store with CRUD + error handling + pagination + tags. 0 tests currently. Follow ACM test patterns. | High | 4±1 | — | +++testing, +speclang, -vision | GLM-5.2 | High | MiniMax-M3 |
| NEVER-DONE | 11-point audit sweep | High | 2 | — | ++code-review, +testing | DeepSeek V4 Pro | Audit runs every tick | GLM-5.2 |

## Completed

| ID | Task | Priority | Complexity | Commit | Model |
|----|------|----------|------------|--------|-------|
| U01 | Usability & coverage audit — endpoint wiring, test coverage, error handling, edge cases | High | 3±1 | (this tick) | DeepSeek V4 Pro |

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
## [ ] NEVER-DONE — Run coding-hermes-never-done 11-point audit
