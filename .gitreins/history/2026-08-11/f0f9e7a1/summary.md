# Verdict: ts-gap-020

**Task:** awslocal wrapper resolves venv binary without PATH (TS-GAP-020)
**Evaluated:** 2026-08-11T10:00:22.103351
**Result:** ✗ FAIL

## Pipeline Stages

- ✗ **tier1**
  -   ✓ lint: F841 Local variable `errors` is assigned to but never used
   --> development/aws-spec-to-speclang.p
  ✓ secrets: [90m4:59AM[0m [32mINF[0m [1mscanned ~107995128 bytes (108 MB) in 5.09s[0m
[90m4:59AM[0m [32
  ✗ tests: ============================= test session starts ==============================
platform linux -- P
- ✓ **tier2**
  - COMPLETE
  ✗ env -i PATH=/usr/bin:/bin ./scripts/awslocal --help exits 0 from repo root with venv not activated: Command exits 2, not 0. The wrapper correctly resolves the venv binary without PATH (verified: env -i PATH=/usr/bin:/bin ./scripts/awslocal --version exits 0, resolving .venv/bin/awslocal-upstream), but the underlying aws CLI requires a command with --help; even direct .venv/bin/awslocal-upstream --help exits 2. The literal exit-0 assertion is not met.
  ✓ wrapper never resolves to itself (no recursion): scripts/awslocal lines 27-45 guard every candidate with `! grep -q "TotalStack awslocal preflight wrapper"`; the marker is present in scripts/awslocal and .venv/bin/awslocal (wrapper copies) but absent in .venv/bin/awslocal-upstream (real binary), and candidate order prefers awslocal-upstream. Self-resolution is impossible.
The wrapper resolves the venv binary without PATH and has a solid no-recursion guard, but the literal --help smoke test exits 2 (not 0) due to the underlying aws CLI requiring a command.

## Summary

Judge Result: ts-gap-020

Stage tier1: FAIL
    ✓ lint: F841 Local variable `errors` is assigned to but never used
   --> development/aws-spec-to-speclang.p
  ✓ secrets: [90m4:59AM[0m [32mINF[0m [1mscanned ~107995128 bytes (108 MB) in 5.09s[0m
[90m4:59AM[0m [32
  ✗ tests: ============================= test session starts ==============================
platform linux -- P

Stage tier2: PASS
  COMPLETE
  ✗ env -i PATH=/usr/bin:/bin ./scripts/awslocal --help exits 0 from repo root with venv not activated: Command exits 2, not 0. The wrapper correctly resolves the venv binary without PATH (verified: env -i PATH=/usr/bin:/bin ./scripts/awslocal --version exits 0, resolving .venv/bin/awslocal-upstream), but the underlying aws CLI requires a command with --help; even direct .venv/bin/awslocal-upstream --help exits 2. The literal exit-0 assertion is not met.
  ✓ wrapper never resolves to itself (no recursion): scripts/awslocal lines 27-45 guard every candidate with `! grep -q "TotalStack awslocal preflight wrapper"`; the marker is present in scripts/awslocal and .venv/bin/awslocal (wrapper copies) but absent in .venv/bin/awslocal-upstream (real binary), and candidate order prefers awslocal-upstream. Self-resolution is impossible.
The wrapper resolves the venv binary without PATH and has a solid no-recursion guard, but the literal --help smoke test exits 2 (not 0) due to the underlying aws CLI requiring a command.

Overall: FAIL ✗
