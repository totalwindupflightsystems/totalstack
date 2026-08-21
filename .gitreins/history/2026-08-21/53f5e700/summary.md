# Verdict: ts-gap-032

**Task:** Warn when pytest integration suites attach to an ambient emulator on :4566
**Evaluated:** 2026-08-21T04:47:16.709575
**Result:** ✗ FAIL

## Pipeline Stages

- ✗ **tier1**
  -   ✗ lint: I001 [*] Import block is un-sorted or un-formatted
 --> localstack-core/localstack/aws/api/acm/__ini
  ✗ secrets: [90m11:38PM[0m [32mINF[0m [1mscanned ~107023895 bytes (107.02 MB) in 5.88s[0m
[90m11:38PM[0m
  ✓ tests: ============================= test session starts ==============================
platform linux -- P
- ✓ **tier2**
  - COMPLETE
  ✓ PASS: with make start running (ambient instance on :4566), pytest tests/aws/services/acm/ -q prints an explicit 'reusing running instance at :4566' warning (or produces zero acm traffic in the make-start log); with no emulator, the TS-GAP-033 fail-fast still exits non-zero within ~60s with the explicit reachability error: Both parts verified via live runs. (1) Ambient emulator: started a health-answering HTTP server on :4566, ran `.venv/bin/python -m pytest tests/aws/services/acm/ --tb=short -q`; output contained 'WARNING: reusing running instance at :4566 — integration tests will run against the ambient emulator and may mutate its state' (exact required substring present). Implemented in tests/aws/conftest.py: pytest_sessionstart (line 288) detects ambient via _detect_ambient_emulator; autouse fixture _emulator_reachability_check (line 310) calls _warn_reusing_instance (line 262) which emits the warning. (2) No emulator: with TEST_AWS_ENDPOINT_URL=http://localhost:59999 (dead port), pytest exited EXIT=1 and printed 'ERROR: emulator not reachable at http://localhost:59999 — run `make start` before running this suite (no healthy response within 30s (last error: <urlopen error [Errno 111] Connection refused>))'; os._exit(1) at conftest.py:352 guarantees non-zero exit within ~30s health timeout + boot, well under 60s. Baseline suite passes: '7 passed, 12 warnings in 26.13s'. No LSP diagnostics.
The TS-GAP-032 warning and TS-GAP-033 fail-fast behaviors are both implemented in tests/aws/conftest.py and verified via live pytest runs: ambient emulator on :4566 triggers the 'reusing running instance at :4566' warning, and an unreachable emulator triggers a non-zero exit with the explicit reachability error within ~60s.

## Summary

Judge Result: ts-gap-032

Stage tier1: FAIL
    ✗ lint: I001 [*] Import block is un-sorted or un-formatted
 --> localstack-core/localstack/aws/api/acm/__ini
  ✗ secrets: [90m11:38PM[0m [32mINF[0m [1mscanned ~107023895 bytes (107.02 MB) in 5.88s[0m
[90m11:38PM[0m
  ✓ tests: ============================= test session starts ==============================
platform linux -- P

Stage tier2: PASS
  COMPLETE
  ✓ PASS: with make start running (ambient instance on :4566), pytest tests/aws/services/acm/ -q prints an explicit 'reusing running instance at :4566' warning (or produces zero acm traffic in the make-start log); with no emulator, the TS-GAP-033 fail-fast still exits non-zero within ~60s with the explicit reachability error: Both parts verified via live runs. (1) Ambient emulator: started a health-answering HTTP server on :4566, ran `.venv/bin/python -m pytest tests/aws/services/acm/ --tb=short -q`; output contained 'WARNING: reusing running instance at :4566 — integration tests will run against the ambient emulator and may mutate its state' (exact required substring present). Implemented in tests/aws/conftest.py: pytest_sessionstart (line 288) detects ambient via _detect_ambient_emulator; autouse fixture _emulator_reachability_check (line 310) calls _warn_reusing_instance (line 262) which emits the warning. (2) No emulator: with TEST_AWS_ENDPOINT_URL=http://localhost:59999 (dead port), pytest exited EXIT=1 and printed 'ERROR: emulator not reachable at http://localhost:59999 — run `make start` before running this suite (no healthy response within 30s (last error: <urlopen error [Errno 111] Connection refused>))'; os._exit(1) at conftest.py:352 guarantees non-zero exit within ~30s health timeout + boot, well under 60s. Baseline suite passes: '7 passed, 12 warnings in 26.13s'. No LSP diagnostics.
The TS-GAP-032 warning and TS-GAP-033 fail-fast behaviors are both implemented in tests/aws/conftest.py and verified via live pytest runs: ambient emulator on :4566 triggers the 'reusing running instance at :4566' warning, and an unreachable emulator triggers a non-zero exit with the explicit reachability error within ~60s.

Overall: FAIL ✗
