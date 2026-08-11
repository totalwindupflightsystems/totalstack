# Verdict: ts-gap-020

**Task:** awslocal wrapper resolves venv binary without PATH (TS-GAP-020)
**Evaluated:** 2026-08-11T10:03:43.752311
**Result:** ✗ FAIL

## Pipeline Stages

- ✗ **tier1**
  -   ✓ lint: F841 Local variable `errors` is assigned to but never used
   --> development/aws-spec-to-speclang.p
  ✓ secrets: 
    ○
    │╲
    │ ○
    ○ ░
    ░    gitleaks

[90m5:01AM[0m [32mINF[0m [1mscanned ~107995128
  ✗ tests: Command timed out
- ✗ **tier2**
  - INCOMPLETE

Evaluator error: LLM call failed: LLM request failed after 3 attempts

## Summary

Judge Result: ts-gap-020

Stage tier1: FAIL
    ✓ lint: F841 Local variable `errors` is assigned to but never used
   --> development/aws-spec-to-speclang.p
  ✓ secrets: 
    ○
    │╲
    │ ○
    ○ ░
    ░    gitleaks

[90m5:01AM[0m [32mINF[0m [1mscanned ~107995128
  ✗ tests: Command timed out

Stage tier2: FAIL
  INCOMPLETE

Evaluator error: LLM call failed: LLM request failed after 3 attempts

Overall: FAIL ✗
