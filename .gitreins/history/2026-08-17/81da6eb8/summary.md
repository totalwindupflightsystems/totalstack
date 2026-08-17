# Verdict: ts-gap-029-readme-fork-docs

**Task:** README links fork docs (TS-GAP-029)
**Evaluated:** 2026-08-17T10:48:23.497656
**Result:** ✗ FAIL

## Pipeline Stages

- ✗ **tier1**
  -   ✗ lint: F841 Local variable `errors` is assigned to but never used
   --> development/aws-spec-to-speclang.p
  ✗ secrets: [90m5:43AM[0m [32mINF[0m [1mscanned ~106985691 bytes (106.99 MB) in 5.13s[0m
[90m5:43AM[0m 
  ✓ tests: ============================= test session starts ==============================
platform linux -- P
- ✓ **tier2**
  - COMPLETE
  ✓ README.md top nav and Usage section link the fork's own docs/API.md and docs/README.md (grep -c 'docs/API.md' README.md >= 1 AND grep -c 'docs/README.md' README.md >= 1); docs.localstack.cloud occurrence count in README.md reduced from baseline 16 (or at least fork docs linked alongside); ONLY README.md modified (git status shows no other tracked file changed); no push; gitreins guard passes: README.md:39-40 top nav links docs/API.md and docs/README.md; README.md:190 Usage section links both. grep -c 'docs/API.md'=2, 'docs/README.md'=2 (both >=1). docs.localstack.cloud=16 (not reduced, but fork docs linked alongside satisfies alternative). Commit fad11c445c modified ONLY README.md (4 insertions). No push: 'git branch -r --contains fad11c445c' empty. Guard: spec tests 1865 passed/208 skipped, ACM 7 passed, exit=0, 'Tier 1 Guards: PASS'.
README.md links fork docs in top nav and Usage section, only README.md was modified in the task commit, no push occurred, and the gitreins guard passes (1865+7 tests passed, exit 0).

## Summary

Judge Result: ts-gap-029-readme-fork-docs

Stage tier1: FAIL
    ✗ lint: F841 Local variable `errors` is assigned to but never used
   --> development/aws-spec-to-speclang.p
  ✗ secrets: [90m5:43AM[0m [32mINF[0m [1mscanned ~106985691 bytes (106.99 MB) in 5.13s[0m
[90m5:43AM[0m 
  ✓ tests: ============================= test session starts ==============================
platform linux -- P

Stage tier2: PASS
  COMPLETE
  ✓ README.md top nav and Usage section link the fork's own docs/API.md and docs/README.md (grep -c 'docs/API.md' README.md >= 1 AND grep -c 'docs/README.md' README.md >= 1); docs.localstack.cloud occurrence count in README.md reduced from baseline 16 (or at least fork docs linked alongside); ONLY README.md modified (git status shows no other tracked file changed); no push; gitreins guard passes: README.md:39-40 top nav links docs/API.md and docs/README.md; README.md:190 Usage section links both. grep -c 'docs/API.md'=2, 'docs/README.md'=2 (both >=1). docs.localstack.cloud=16 (not reduced, but fork docs linked alongside satisfies alternative). Commit fad11c445c modified ONLY README.md (4 insertions). No push: 'git branch -r --contains fad11c445c' empty. Guard: spec tests 1865 passed/208 skipped, ACM 7 passed, exit=0, 'Tier 1 Guards: PASS'.
README.md links fork docs in top nav and Usage section, only README.md was modified in the task commit, no push occurred, and the gitreins guard passes (1865+7 tests passed, exit 0).

Overall: FAIL ✗
