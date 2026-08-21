# Verdict: TS-GAP-033

**Task:** Add fail-fast health check when emulator unreachable
**Evaluated:** 2026-08-20T11:00:46.646394
**Result:** ✗ FAIL

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

[90m6:00AM[0m [32mINF[0m [1mscanned ~107267909
- ✗ **tier2**
  - INCOMPLETE

Evaluator error: LLM call failed: LLM request failed after 3 attempts

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

[90m6:00AM[0m [32mINF[0m [1mscanned ~107267909

Stage tier2: FAIL
  INCOMPLETE

Evaluator error: LLM call failed: LLM request failed after 3 attempts

Overall: FAIL ✗
