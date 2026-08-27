# Verdict: ts-gap-043

**Task:** TS-GAP-043: document in-Lambda endpoint rule (use injected AWS_ENDPOINT_URL, not localhost:4566)
**Evaluated:** 2026-08-26T22:29:09.489344
**Result:** ✗ FAIL

## Pipeline Stages

- ✗ **tier1**
  -   ✗ lint: I001 [*] Import block is un-sorted or un-formatted
 --> localstack-core/localstack/aws/api/acm/__ini
  ✗ secrets: [90m5:27PM[0m [32mINF[0m [1mscanned ~107464394 bytes (107.46 MB) in 9.75s[0m
[90m5:27PM[0m 
  ✓ tests: ============================= test session starts ==============================
platform linux -- P
- ✓ **tier2**
  - COMPLETE
  ✓ README.md and AGENTS.md must document the in-Lambda endpoint rule: inside a Lambda container the emulator is reached via the injected AWS_ENDPOINT_URL (docker bridge gateway, e.g. http://172.17.0.1:4566), localhost:4566 does not resolve, and handlers must use os.environ['AWS_ENDPOINT_URL'] or plain boto3 without endpoint_url. README must contain the explicit note plus a working handler snippet. Verify: grep -c 'inside Lambda' README.md >= 1 and README contains AWS_ENDPOINT_URL in a Lambda handler context; AGENTS.md mentions the rule; skills/totalstack-usage RULE 3 stays consistent. Commit with Co-authored-by trailer.: Commit fc98fc48ed: README.md grep -c 'inside Lambda' = 1 (>=1). README lines 126-146 contain explicit note (AWS_ENDPOINT_URL docker bridge gateway http://172.17.0.1:4566, localhost:4566 does NOT resolve, handlers must use os.environ['AWS_ENDPOINT_URL'] or plain boto3 without endpoint_url) plus working handler snippet showing both correct approaches and the broken one. AGENTS.md lines 42-50 document the rule. skills/totalstack-usage/SKILL.md RULE 3 (lines 64-79) consistent (same guidance). Commit message includes 'Co-authored-by: Alexis Okuwa <wojonstech@gmail.com>' trailer. Docs-only change, no test suite applicable.
All documentation requirements for the in-Lambda endpoint rule are met in README.md, AGENTS.md, and skills/totalstack-usage RULE 3, with the Co-authored-by trailer present.

## Summary

Judge Result: ts-gap-043

Stage tier1: FAIL
    ✗ lint: I001 [*] Import block is un-sorted or un-formatted
 --> localstack-core/localstack/aws/api/acm/__ini
  ✗ secrets: [90m5:27PM[0m [32mINF[0m [1mscanned ~107464394 bytes (107.46 MB) in 9.75s[0m
[90m5:27PM[0m 
  ✓ tests: ============================= test session starts ==============================
platform linux -- P

Stage tier2: PASS
  COMPLETE
  ✓ README.md and AGENTS.md must document the in-Lambda endpoint rule: inside a Lambda container the emulator is reached via the injected AWS_ENDPOINT_URL (docker bridge gateway, e.g. http://172.17.0.1:4566), localhost:4566 does not resolve, and handlers must use os.environ['AWS_ENDPOINT_URL'] or plain boto3 without endpoint_url. README must contain the explicit note plus a working handler snippet. Verify: grep -c 'inside Lambda' README.md >= 1 and README contains AWS_ENDPOINT_URL in a Lambda handler context; AGENTS.md mentions the rule; skills/totalstack-usage RULE 3 stays consistent. Commit with Co-authored-by trailer.: Commit fc98fc48ed: README.md grep -c 'inside Lambda' = 1 (>=1). README lines 126-146 contain explicit note (AWS_ENDPOINT_URL docker bridge gateway http://172.17.0.1:4566, localhost:4566 does NOT resolve, handlers must use os.environ['AWS_ENDPOINT_URL'] or plain boto3 without endpoint_url) plus working handler snippet showing both correct approaches and the broken one. AGENTS.md lines 42-50 document the rule. skills/totalstack-usage/SKILL.md RULE 3 (lines 64-79) consistent (same guidance). Commit message includes 'Co-authored-by: Alexis Okuwa <wojonstech@gmail.com>' trailer. Docs-only change, no test suite applicable.
All documentation requirements for the in-Lambda endpoint rule are met in README.md, AGENTS.md, and skills/totalstack-usage RULE 3, with the Co-authored-by trailer present.

Overall: FAIL ✗
