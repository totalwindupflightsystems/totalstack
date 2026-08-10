# Verdict: ts-gap-014

**Task:** awslocal AWS_ENDPOINT_URL preflight (TS-GAP-014)
**Evaluated:** 2026-08-10T00:05:12.794845
**Result:** ✓ PASS

## Pipeline Stages

- ✓ **tier1**
  -   ✓ lint: F841 Local variable `errors` is assigned to but never used
   --> development/aws-spec-to-speclang.p
  ✓ secrets: [90m7:02PM[0m [32mINF[0m [1mscanned ~107678678 bytes (107.68 MB) in 4.61s[0m
[90m7:02PM[0m 
  ✓ tests: ============================= test session starts ==============================
platform linux -- P
- ✓ **tier2**
  - COMPLETE
  ✓ with AWS_ENDPOINT_URL exported, scripts/awslocal sqs list-queues emits an explicit warning and targets localhost:4566: scripts/awslocal (lines 20-24) detects AWS_ENDPOINT_URL via `env | grep -E '^AWS_ENDPOINT_URL(=|_)'`, emits 'totalstack: warning: AWS_ENDPOINT_URL is set (...) — unsetting it so awslocal targets http://localhost:4566' and unsets the var. Verified by running with AWS_ENDPOINT_URL=http://example.com:9999: warning emitted and [AWS_ENDPOINT_URL]=UNSET after, then `exec awslocal "$@"` (line 34) uses the localhost:4566 default. bash -n syntax OK.
  ✓ README documents the AWS_ENDPOINT_URL/AWS_PROFILE conflict and the scripts/awslocal wrapper: README.md lines 109-116 document that AWS_ENDPOINT_URL (or AWS_ENDPOINT_URL_<SERVICE>), AWS_PROFILE or AWS_DEFAULT_PROFILE silently override awslocal's localhost:4566 default (real-cloud traffic leak risk), and direct users to the scripts/awslocal wrapper (warns about the conflict and forces the local endpoint) or to unset those variables.
Both criteria pass: scripts/awslocal emits an explicit warning and unsets AWS_ENDPOINT_URL so awslocal targets localhost:4566 (verified by execution), and README documents the AWS_ENDPOINT_URL/AWS_PROFILE conflict and the wrapper.

## Summary

Judge Result: ts-gap-014

Stage tier1: PASS
    ✓ lint: F841 Local variable `errors` is assigned to but never used
   --> development/aws-spec-to-speclang.p
  ✓ secrets: [90m7:02PM[0m [32mINF[0m [1mscanned ~107678678 bytes (107.68 MB) in 4.61s[0m
[90m7:02PM[0m 
  ✓ tests: ============================= test session starts ==============================
platform linux -- P

Stage tier2: PASS
  COMPLETE
  ✓ with AWS_ENDPOINT_URL exported, scripts/awslocal sqs list-queues emits an explicit warning and targets localhost:4566: scripts/awslocal (lines 20-24) detects AWS_ENDPOINT_URL via `env | grep -E '^AWS_ENDPOINT_URL(=|_)'`, emits 'totalstack: warning: AWS_ENDPOINT_URL is set (...) — unsetting it so awslocal targets http://localhost:4566' and unsets the var. Verified by running with AWS_ENDPOINT_URL=http://example.com:9999: warning emitted and [AWS_ENDPOINT_URL]=UNSET after, then `exec awslocal "$@"` (line 34) uses the localhost:4566 default. bash -n syntax OK.
  ✓ README documents the AWS_ENDPOINT_URL/AWS_PROFILE conflict and the scripts/awslocal wrapper: README.md lines 109-116 document that AWS_ENDPOINT_URL (or AWS_ENDPOINT_URL_<SERVICE>), AWS_PROFILE or AWS_DEFAULT_PROFILE silently override awslocal's localhost:4566 default (real-cloud traffic leak risk), and direct users to the scripts/awslocal wrapper (warns about the conflict and forces the local endpoint) or to unset those variables.
Both criteria pass: scripts/awslocal emits an explicit warning and unsets AWS_ENDPOINT_URL so awslocal targets localhost:4566 (verified by execution), and README documents the AWS_ENDPOINT_URL/AWS_PROFILE conflict and the wrapper.

Overall: PASS ✓
