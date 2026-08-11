# Verdict: ts-gap-015

**Task:** awslocal wrapper wired as venv awslocal + profile neutralization (TS-GAP-015)
**Evaluated:** 2026-08-11T07:52:05.423715
**Result:** ✗ FAIL

## Pipeline Stages

- ✓ **tier1**
  -   ✓ lint: F841 Local variable `errors` is assigned to but never used
   --> development/aws-spec-to-speclang.p
  ✓ tests: 
  ✓ secrets: 
    ○
    │╲
    │ ○
    ○ ░
    ░    gitleaks

[90m2:52AM[0m [32mINF[0m [1mscanned ~107995128
- ✗ **tier2**
  - INCOMPLETE

Evaluator error: LLM call failed: LLM request failed after 3 attempts

## Summary

Judge Result: ts-gap-015

Stage tier1: PASS
    ✓ lint: F841 Local variable `errors` is assigned to but never used
   --> development/aws-spec-to-speclang.p
  ✓ tests: 
  ✓ secrets: 
    ○
    │╲
    │ ○
    ○ ░
    ░    gitleaks

[90m2:52AM[0m [32mINF[0m [1mscanned ~107995128

Stage tier2: FAIL
  INCOMPLETE

Evaluator error: LLM call failed: LLM request failed after 3 attempts

Overall: FAIL ✗
