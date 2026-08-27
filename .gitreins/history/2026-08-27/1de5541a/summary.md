# Verdict: TS-GAP-044

**Task:** Investigate lambda update-vs-deliver CancelledError race (S3 event-source)
**Evaluated:** 2026-08-27T04:58:10.827821
**Result:** ✓ PASS

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

[90m11:57PM[0m [32mINF[0m [1mscanned ~10748058
- ✓ **tier2**
  - COMPLETE
  ✓ Investigate the CancelledError invocation race after lambda update_function_code in the vendored core lambda invocation path (version_manager.py/executor_endpoint.py); document root cause with evidence and the practical workaround in repo docs; do NOT modify localstack-core/ (DO-NOT-EDIT); commit findings with Co-authored-by trailer.: Commit 146f7e3ab5 adds docs/dogfood/2026-08-27-lambda-update-race.md (239 lines) root-causing the race: update_function_code triggers async rollover; executor_endpoint.py:180-184 shutdown() cancels invocation_future; version_manager.py:276-298 invoke() only catches StatusErrorException so CancelledError propagates; assignment.py:94-97 logs 'Failed invocation <class concurrent.futures._base.CancelledError>' (l.s.l.i.assignment); event_manager.py:334-336 re-enqueues with delay 2**retries capped 5min. All line refs verified against actual localstack-core code. Workaround documented (section 4): wait State==Active AND LastUpdateStatus==Successful, warm-up RequestResponse invoke, poll 60-90s, idempotent handlers. No files under localstack-core/ modified (git show --name-only grep localstack-core exit 1). Commit message contains 'Co-authored-by: Alexis Okuwa <wojonstech@gmail.com>'; commit present in repo history.
The CancelledError update-vs-deliver race was fully investigated with source-level evidence, root cause and practical workaround documented in repo docs, localstack-core untouched, and findings committed with a Co-authored-by trailer.

## Summary

Judge Result: TS-GAP-044

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

[90m11:57PM[0m [32mINF[0m [1mscanned ~10748058

Stage tier2: PASS
  COMPLETE
  ✓ Investigate the CancelledError invocation race after lambda update_function_code in the vendored core lambda invocation path (version_manager.py/executor_endpoint.py); document root cause with evidence and the practical workaround in repo docs; do NOT modify localstack-core/ (DO-NOT-EDIT); commit findings with Co-authored-by trailer.: Commit 146f7e3ab5 adds docs/dogfood/2026-08-27-lambda-update-race.md (239 lines) root-causing the race: update_function_code triggers async rollover; executor_endpoint.py:180-184 shutdown() cancels invocation_future; version_manager.py:276-298 invoke() only catches StatusErrorException so CancelledError propagates; assignment.py:94-97 logs 'Failed invocation <class concurrent.futures._base.CancelledError>' (l.s.l.i.assignment); event_manager.py:334-336 re-enqueues with delay 2**retries capped 5min. All line refs verified against actual localstack-core code. Workaround documented (section 4): wait State==Active AND LastUpdateStatus==Successful, warm-up RequestResponse invoke, poll 60-90s, idempotent handlers. No files under localstack-core/ modified (git show --name-only grep localstack-core exit 1). Commit message contains 'Co-authored-by: Alexis Okuwa <wojonstech@gmail.com>'; commit present in repo history.
The CancelledError update-vs-deliver race was fully investigated with source-level evidence, root cause and practical workaround documented in repo docs, localstack-core untouched, and findings committed with a Co-authored-by trailer.

Overall: PASS ✓
