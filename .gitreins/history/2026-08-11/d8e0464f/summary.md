# Verdict: ts-gap-015

**Task:** awslocal wrapper wired as venv awslocal + profile neutralization (TS-GAP-015)
**Evaluated:** 2026-08-11T10:09:35.658340
**Result:** ✓ PASS

## Pipeline Stages

- ✓ **tier1**
  -   ✓ lint: F841 Local variable `errors` is assigned to but never used
   --> development/aws-spec-to-speclang.p
  ✓ secrets: [90m5:06AM[0m [32mINF[0m [1mscanned ~107995128 bytes (108 MB) in 4.34s[0m
[90m5:06AM[0m [32
  ✓ tests: ============================= test session starts ==============================
platform linux -- P
- ✓ **tier2**
  - COMPLETE
  ✓ make install-test installs scripts/awslocal as .venv/bin/awslocal (upstream renamed awslocal-upstream): Makefile:57-70 install-test target does `mv .venv/bin/awslocal .venv/bin/awslocal-upstream` and `cp scripts/awslocal .venv/bin/awslocal`. Verified: `diff scripts/awslocal .venv/bin/awslocal` = IDENTICAL; `.venv/bin/awslocal-upstream` exists (9607 bytes, no wrapper marker).
  ✓ with AWS_ENDPOINT_URL and AWS_PROFILE exported, venv awslocal sqs list-queues targets localhost:4566 with zero non-local network contact: Ran `AWS_ENDPOINT_URL=http://evil.example.com AWS_PROFILE=nonexistent-profile .venv/bin/awslocal sqs list-queues`. Wrapper (scripts/awslocal) warned and unset both vars, then error 'Could not connect to the endpoint URL: http://localhost:4566/' — zero contact with evil.example.com, all traffic to localhost:4566.
  ✓ dangling AWS_PROFILE does not crash the wrapper (ProfileNotFound): Ran `AWS_PROFILE=nonexistent-profile .venv/bin/awslocal sqs list-queues`. Wrapper unset AWS_PROFILE before exec and proceeded to attempt localhost:4566 connection — no ProfileNotFound crash.
All three TS-GAP-015 criteria pass: install-test wires the wrapper as .venv/bin/awslocal with upstream renamed, the wrapper neutralizes AWS_ENDPOINT_URL/AWS_PROFILE to force localhost:4566 with zero non-local contact, and a dangling AWS_PROFILE does not crash it.

## Summary

Judge Result: ts-gap-015

Stage tier1: PASS
    ✓ lint: F841 Local variable `errors` is assigned to but never used
   --> development/aws-spec-to-speclang.p
  ✓ secrets: [90m5:06AM[0m [32mINF[0m [1mscanned ~107995128 bytes (108 MB) in 4.34s[0m
[90m5:06AM[0m [32
  ✓ tests: ============================= test session starts ==============================
platform linux -- P

Stage tier2: PASS
  COMPLETE
  ✓ make install-test installs scripts/awslocal as .venv/bin/awslocal (upstream renamed awslocal-upstream): Makefile:57-70 install-test target does `mv .venv/bin/awslocal .venv/bin/awslocal-upstream` and `cp scripts/awslocal .venv/bin/awslocal`. Verified: `diff scripts/awslocal .venv/bin/awslocal` = IDENTICAL; `.venv/bin/awslocal-upstream` exists (9607 bytes, no wrapper marker).
  ✓ with AWS_ENDPOINT_URL and AWS_PROFILE exported, venv awslocal sqs list-queues targets localhost:4566 with zero non-local network contact: Ran `AWS_ENDPOINT_URL=http://evil.example.com AWS_PROFILE=nonexistent-profile .venv/bin/awslocal sqs list-queues`. Wrapper (scripts/awslocal) warned and unset both vars, then error 'Could not connect to the endpoint URL: http://localhost:4566/' — zero contact with evil.example.com, all traffic to localhost:4566.
  ✓ dangling AWS_PROFILE does not crash the wrapper (ProfileNotFound): Ran `AWS_PROFILE=nonexistent-profile .venv/bin/awslocal sqs list-queues`. Wrapper unset AWS_PROFILE before exec and proceeded to attempt localhost:4566 connection — no ProfileNotFound crash.
All three TS-GAP-015 criteria pass: install-test wires the wrapper as .venv/bin/awslocal with upstream renamed, the wrapper neutralizes AWS_ENDPOINT_URL/AWS_PROFILE to force localhost:4566 with zero non-local contact, and a dangling AWS_PROFILE does not crash it.

Overall: PASS ✓
