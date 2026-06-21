# TotalStack Project Memory

## Overview
Community-maintained fork of LocalStack v4.14.0 (Apache 2.0). **Full system takeover** — we own the entire codebase.
This is NOT just using LocalStack as a library. We iterate on the full emulator: CLI, runtime, services, tests.
SpecLang encodes AWS API contracts as formal specs; generated code replaces/extends LocalStack service providers.

## Development Environment
- **Python**: `.venv/` (uv venv, CPython 3.13.13)
- **Install**: `source .venv/bin/activate && uv pip install -e ".[runtime,test]"`
- **LocalStack CLI**: `.venv/bin/localstack` or `.venv/bin/python -m localstack.cli.main`
- **Tests**: `.venv/bin/python -m pytest specs/aws/.speclang/assembled/_tests/ -c /dev/null`
- **Known issue**: `cbor2._decoder` missing — pytest needs `-c /dev/null` to skip LocalStack's conftest plugins

## Navigation
- [Testing Strategy & Standards](testing/strategy.md) — **READ FIRST** — integration/E2E test requirements
- [Integration Test Pattern](testing/integration-pattern.md) — per-operation integration test template
- [E2E Test Pattern](testing/e2e-pattern.md) — full-workflow E2E test template

## Key Decisions
- **Testing is NOT optional.** Mock tests that validate spec structure alone are insufficient.
  Every service MUST have integration tests (real stores) AND E2E tests (boto3 against running instance).
- **SpecLang cascade generates code; tests are hand-written** until the testwriter stage matures.
- **GitReins gates enforcement**: no service is "done" without passing integration + E2E tests.

## Current Services
| Service | Ops | Code Generated | Integration Tests | E2E Tests | Status |
|---------|-----|---------------|-------------------|-----------|--------|
| dynamodb | 57 | ✅ 36 files | ❌ 0 | ❌ 0 | Specs done, needs tests |
| translate | 19 | ⚠️ placeholder | ❌ 0 | ❌ 0 | Needs code + tests |
| cognito-idp | 10/50 | ✅ 10 ops | ❌ 0 | ❌ 0 | In progress |

## Repo Structure
- `specs/aws/<service>/` — SpecLang spec files (.spec.py.md, .spec.meta.md, .spec.plan.md)
- `specs/aws/.speclang/assembled/` — Generated code from cascade
- `specs/aws/.speclang/assembled/_tests/` — **TO CREATE**: Integration + E2E tests
- `.gitreins/tasks.yaml` — Quality gate task definitions
- `service-build-queue.txt` — Autonomous build queue (~392 services)
- `localstack-core/` — Original LocalStack source (v4.14.0)

## Cron Job
- `totalstack-service-builder` (d3ea29913b2a): hourly, builds one service per tick
