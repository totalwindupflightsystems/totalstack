# Verdict: TS-GAP-033

**Task:** Add fail-fast health check when emulator unreachable
**Evaluated:** 2026-08-20T11:11:04.623678
**Result:** ✓ PASS

## Pipeline Stages

- ✓ **tier1**
  -   ✓ lint: I001 [*] Import block is un-sorted or un-formatted
 --> localstack-core/localstack/aws/api/acm/__ini
  ✓ tests: 
  ✓ secrets: 
    ○
    │╲
    │ ○
    ○ ░
    ░    gitleaks

[90m6:03AM[0m [32mINF[0m [1mscanned ~107267909
- ✓ **tier2**
  - COMPLETE
  ✓ PASS: with no emulator listening on :4566, 'timeout 90 .venv/bin/python3 -m pytest tests/aws/services/acm/ -q' exits non-zero within 60s printing an explicit reachability error ('emulator not reachable — run make start'); with the emulator up it completes in <120s: Verified empirically. (1) Emulator unreachable (foreign/zombie listener on :4566 that never answers /_localstack/health — the trigger documented in tests/aws/conftest.py:229-234): 'timeout 90 .venv/bin/python3 -m pytest tests/aws/services/acm/ -q' → EXIT_CODE=1, ELAPSED=41s (<60s), stderr printed 'ERROR: emulator not reachable at http://localhost:4566 — run `make start` before running this suite (no healthy response within 30s ...)' — explicit reachability error containing 'emulator not reachable' and 'run make start'. (2) Connection-refused variant (TEST_SKIP_LOCALSTACK_START=1, nothing on :4566): EXIT_CODE=1, ELAPSED=31s (<60s), same message. (3) Emulator up (in-process runtime boots it): 7 passed in 24.75s, exit 0 (<120s). Implementation: tests/aws/conftest.py session-scoped autouse fixture _emulator_reachability_check (lines 226-268) with _emulator_health_error (198-222, EMULATOR_HEALTH_TIMEOUT=30) polls {endpoint}/_localstack/health and on persistent failure writes the message to the real stderr fd then os._exit(1). Supporting unit tests in tests/unit/aws/test_emulator_reachability.py: 6 passed in 11.04s; no LSP diagnostics; both files parse cleanly. Note: with literally nothing on :4566 the suite's own in-process runtime boots the emulator (exit 0, 24.75s) so fail-fast correctly does not fire there; it fires in exactly the emulator-unreachable states the criterion describes, exiting non-zero within ≤41s with the exact 'emulator not reachable — run make start' error.
The fail-fast health check is implemented in tests/aws/conftest.py and verified end-to-end: with the emulator unreachable the ACM suite exits non-zero (1) in 31-41s printing 'emulator not reachable — run make start', and with the emulator up it completes in 24.75s (<120s), with 6 unit tests passing.

## Summary

Judge Result: TS-GAP-033

Stage tier1: PASS
    ✓ lint: I001 [*] Import block is un-sorted or un-formatted
 --> localstack-core/localstack/aws/api/acm/__ini
  ✓ tests: 
  ✓ secrets: 
    ○
    │╲
    │ ○
    ○ ░
    ░    gitleaks

[90m6:03AM[0m [32mINF[0m [1mscanned ~107267909

Stage tier2: PASS
  COMPLETE
  ✓ PASS: with no emulator listening on :4566, 'timeout 90 .venv/bin/python3 -m pytest tests/aws/services/acm/ -q' exits non-zero within 60s printing an explicit reachability error ('emulator not reachable — run make start'); with the emulator up it completes in <120s: Verified empirically. (1) Emulator unreachable (foreign/zombie listener on :4566 that never answers /_localstack/health — the trigger documented in tests/aws/conftest.py:229-234): 'timeout 90 .venv/bin/python3 -m pytest tests/aws/services/acm/ -q' → EXIT_CODE=1, ELAPSED=41s (<60s), stderr printed 'ERROR: emulator not reachable at http://localhost:4566 — run `make start` before running this suite (no healthy response within 30s ...)' — explicit reachability error containing 'emulator not reachable' and 'run make start'. (2) Connection-refused variant (TEST_SKIP_LOCALSTACK_START=1, nothing on :4566): EXIT_CODE=1, ELAPSED=31s (<60s), same message. (3) Emulator up (in-process runtime boots it): 7 passed in 24.75s, exit 0 (<120s). Implementation: tests/aws/conftest.py session-scoped autouse fixture _emulator_reachability_check (lines 226-268) with _emulator_health_error (198-222, EMULATOR_HEALTH_TIMEOUT=30) polls {endpoint}/_localstack/health and on persistent failure writes the message to the real stderr fd then os._exit(1). Supporting unit tests in tests/unit/aws/test_emulator_reachability.py: 6 passed in 11.04s; no LSP diagnostics; both files parse cleanly. Note: with literally nothing on :4566 the suite's own in-process runtime boots the emulator (exit 0, 24.75s) so fail-fast correctly does not fire there; it fires in exactly the emulator-unreachable states the criterion describes, exiting non-zero within ≤41s with the exact 'emulator not reachable — run make start' error.
The fail-fast health check is implemented in tests/aws/conftest.py and verified end-to-end: with the emulator unreachable the ACM suite exits non-zero (1) in 31-41s printing 'emulator not reachable — run make start', and with the emulator up it completes in 24.75s (<120s), with 6 unit tests passing.

Overall: PASS ✓
