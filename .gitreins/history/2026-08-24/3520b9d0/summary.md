# Verdict: TS-GAP-040

**Task:** Docs: annotate test auto-pickup claim + state TEST_PATH override requirement
**Evaluated:** 2026-08-24T18:13:51.905532
**Result:** ✗ FAIL

## Pipeline Stages

- ✗ **tier1**
  -   ✗ lint: I001 [*] Import block is un-sorted or un-formatted
 --> localstack-core/localstack/aws/api/acm/__ini
  ✗ secrets: [90m1:11PM[0m [32mINF[0m [1mscanned ~107429166 bytes (107.43 MB) in 4.49s[0m
[90m1:11PM[0m 
  ✓ tests: ============================= test session starts ==============================
platform linux -- P
- ✓ **tier2**
  - COMPLETE
  ✓ Update docs/testing/integration-tests/README.md so it explicitly states that bare 'make test' defaults to TEST_PATH=tests/unit only, that tests/integration and tests/aws suites require the TEST_PATH= override (e.g. TEST_PATH='tests/aws/services/acm/' make test), and that the claim that tests matching tests/integration/**/test_*.py or tests/aws/**/test_*.py are 'picked up automatically' is annotated or removed. Verify the edited file contains the TEST_PATH override requirement and no longer states unconditional automatic pickup.: docs/testing/integration-tests/README.md (HEAD, commit 8b0633d1b9) line 24: 'Tests matching the pattern tests/integration/**/test_*.py or tests/aws/**/test_*.py are part of the integration test suite — but they are **not** picked up by a bare make test: the Makefile default is TEST_PATH ?= tests/unit'; line 80: 'By default, make test runs the **unit test suite only** (TEST_PATH ?= tests/unit ...). Integration and AWS parity tests ... are **not** picked up automatically: you must set the TEST_PATH variable'; lines 84-85 show overrides 'TEST_PATH="tests/integration" make test' and 'TEST_PATH="tests/aws/services/acm/" make test'. Makefile:6 confirms 'TEST_PATH ?= tests/unit'. The original unconditional 'it will be picked up by the integration test suite' claim is removed/annotated. Docs-only task, no test suite applicable.
The README was correctly updated to state the TEST_PATH=tests/unit default, require the TEST_PATH override for integration/aws suites (with the acm example), and annotate/remove the unconditional auto-pickup claim.

## Summary

Judge Result: TS-GAP-040

Stage tier1: FAIL
    ✗ lint: I001 [*] Import block is un-sorted or un-formatted
 --> localstack-core/localstack/aws/api/acm/__ini
  ✗ secrets: [90m1:11PM[0m [32mINF[0m [1mscanned ~107429166 bytes (107.43 MB) in 4.49s[0m
[90m1:11PM[0m 
  ✓ tests: ============================= test session starts ==============================
platform linux -- P

Stage tier2: PASS
  COMPLETE
  ✓ Update docs/testing/integration-tests/README.md so it explicitly states that bare 'make test' defaults to TEST_PATH=tests/unit only, that tests/integration and tests/aws suites require the TEST_PATH= override (e.g. TEST_PATH='tests/aws/services/acm/' make test), and that the claim that tests matching tests/integration/**/test_*.py or tests/aws/**/test_*.py are 'picked up automatically' is annotated or removed. Verify the edited file contains the TEST_PATH override requirement and no longer states unconditional automatic pickup.: docs/testing/integration-tests/README.md (HEAD, commit 8b0633d1b9) line 24: 'Tests matching the pattern tests/integration/**/test_*.py or tests/aws/**/test_*.py are part of the integration test suite — but they are **not** picked up by a bare make test: the Makefile default is TEST_PATH ?= tests/unit'; line 80: 'By default, make test runs the **unit test suite only** (TEST_PATH ?= tests/unit ...). Integration and AWS parity tests ... are **not** picked up automatically: you must set the TEST_PATH variable'; lines 84-85 show overrides 'TEST_PATH="tests/integration" make test' and 'TEST_PATH="tests/aws/services/acm/" make test'. Makefile:6 confirms 'TEST_PATH ?= tests/unit'. The original unconditional 'it will be picked up by the integration test suite' claim is removed/annotated. Docs-only task, no test suite applicable.
The README was correctly updated to state the TEST_PATH=tests/unit default, require the TEST_PATH override for integration/aws suites (with the acm example), and annotate/remove the unconditional auto-pickup claim.

Overall: FAIL ✗
