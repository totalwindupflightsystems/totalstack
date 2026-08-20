# Verdict: ts-gap-035

**Task:** Fix tzdata dep for unit tests (ZoneInfo EST)
**Evaluated:** 2026-08-20T17:21:28.855216
**Result:** ✗ FAIL

## Pipeline Stages

- ✗ **tier1**
  -   ✗ lint: I001 [*] Import block is un-sorted or un-formatted
 --> localstack-core/localstack/aws/api/acm/__ini
  ✗ secrets: [90m12:19PM[0m [32mINF[0m [1mscanned ~107272276 bytes (107.27 MB) in 4.43s[0m
[90m12:19PM[0m
  ✓ tests: ============================= test session starts ==============================
platform linux -- P
- ✓ **tier2**
  - COMPLETE
  ✓ requirements-test.txt (or equivalent) declares tzdata; PYTHONTZPATH=/nonexistent .venv/bin/python -m pytest tests/unit/test_common.py -q exits 0 with 0 failures: requirements-test.txt:442 declares `tzdata==2026.3` (also pyproject.toml:134 `tzdata>=2025.2` in the test extra). Ran `PYTHONTZPATH=/nonexistent .venv/bin/python -m pytest tests/unit/test_common.py -q` -> EXIT_CODE=0, output '67 passed, 1 warning in 1.13s' (0 failures). tzdata 2026.3 confirmed installed in .venv.
tzdata dependency is declared in requirements-test.txt and pyproject.toml, and the specified test command exits 0 with 67 passed and 0 failures.

## Summary

Judge Result: ts-gap-035

Stage tier1: FAIL
    ✗ lint: I001 [*] Import block is un-sorted or un-formatted
 --> localstack-core/localstack/aws/api/acm/__ini
  ✗ secrets: [90m12:19PM[0m [32mINF[0m [1mscanned ~107272276 bytes (107.27 MB) in 4.43s[0m
[90m12:19PM[0m
  ✓ tests: ============================= test session starts ==============================
platform linux -- P

Stage tier2: PASS
  COMPLETE
  ✓ requirements-test.txt (or equivalent) declares tzdata; PYTHONTZPATH=/nonexistent .venv/bin/python -m pytest tests/unit/test_common.py -q exits 0 with 0 failures: requirements-test.txt:442 declares `tzdata==2026.3` (also pyproject.toml:134 `tzdata>=2025.2` in the test extra). Ran `PYTHONTZPATH=/nonexistent .venv/bin/python -m pytest tests/unit/test_common.py -q` -> EXIT_CODE=0, output '67 passed, 1 warning in 1.13s' (0 failures). tzdata 2026.3 confirmed installed in .venv.
tzdata dependency is declared in requirements-test.txt and pyproject.toml, and the specified test command exits 0 with 67 passed and 0 failures.

Overall: FAIL ✗
