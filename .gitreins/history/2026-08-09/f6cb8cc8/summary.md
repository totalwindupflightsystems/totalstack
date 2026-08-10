# Verdict: ts-gap-014

**Task:** awslocal AWS_ENDPOINT_URL preflight (TS-GAP-014)
**Evaluated:** 2026-08-09T23:54:41.843590
**Result:** ✗ FAIL

## Pipeline Stages

- ✗ **tier1**
  -   ✓ lint: F841 Local variable `errors` is assigned to but never used
   --> development/aws-spec-to-speclang.p
  ✓ secrets: [90m6:53PM[0m [32mINF[0m [1mscanned ~107678678 bytes (107.68 MB) in 9.6s[0m
[90m6:53PM[0m [
  ✗ tests: ============================= test session starts ==============================
platform linux -- P
- ✓ **tier2**
  - COMPLETE
  ✓ with AWS_ENDPOINT_URL exported, scripts/awslocal sqs list-queues emits an explicit warning and targets localhost:4566: scripts/awslocal (lines 14-22) greps env for '^AWS_ENDPOINT_URL(=|_)', emits 'totalstack: warning: AWS_ENDPOINT_URL is set (...) — unsetting it so awslocal targets http://localhost:4566' and unsets the var so awslocal's default localhost:4566 wins. Verified by running `AWS_ENDPOINT_URL=http://example.com PATH=.venv/bin:$PATH bash scripts/awslocal --version` which emitted the warning and executed awslocal (EXIT 0).
  ✓ README documents the AWS_ENDPOINT_URL/AWS_PROFILE conflict and the scripts/awslocal wrapper: README.md lines 108-116 document that AWS_ENDPOINT_URL/AWS_ENDPOINT_URL_<SERVICE>/AWS_PROFILE/AWS_DEFAULT_PROFILE silently override awslocal's localhost:4566 default (real-cloud traffic leak risk) and direct users to 'Use the scripts/awslocal wrapper (it warns about the conflict and forces the local endpoint) or unset those variables'.
Both criteria pass: scripts/awslocal emits an explicit warning and unsets AWS_ENDPOINT_URL so awslocal targets localhost:4566, and README documents the conflict and the wrapper.

## Summary

Judge Result: ts-gap-014

Stage tier1: FAIL
    ✓ lint: F841 Local variable `errors` is assigned to but never used
   --> development/aws-spec-to-speclang.p
  ✓ secrets: [90m6:53PM[0m [32mINF[0m [1mscanned ~107678678 bytes (107.68 MB) in 9.6s[0m
[90m6:53PM[0m [
  ✗ tests: ============================= test session starts ==============================
platform linux -- P

Stage tier2: PASS
  COMPLETE
  ✓ with AWS_ENDPOINT_URL exported, scripts/awslocal sqs list-queues emits an explicit warning and targets localhost:4566: scripts/awslocal (lines 14-22) greps env for '^AWS_ENDPOINT_URL(=|_)', emits 'totalstack: warning: AWS_ENDPOINT_URL is set (...) — unsetting it so awslocal targets http://localhost:4566' and unsets the var so awslocal's default localhost:4566 wins. Verified by running `AWS_ENDPOINT_URL=http://example.com PATH=.venv/bin:$PATH bash scripts/awslocal --version` which emitted the warning and executed awslocal (EXIT 0).
  ✓ README documents the AWS_ENDPOINT_URL/AWS_PROFILE conflict and the scripts/awslocal wrapper: README.md lines 108-116 document that AWS_ENDPOINT_URL/AWS_ENDPOINT_URL_<SERVICE>/AWS_PROFILE/AWS_DEFAULT_PROFILE silently override awslocal's localhost:4566 default (real-cloud traffic leak risk) and direct users to 'Use the scripts/awslocal wrapper (it warns about the conflict and forces the local endpoint) or unset those variables'.
Both criteria pass: scripts/awslocal emits an explicit warning and unsets AWS_ENDPOINT_URL so awslocal targets localhost:4566, and README documents the conflict and the wrapper.

Overall: FAIL ✗
