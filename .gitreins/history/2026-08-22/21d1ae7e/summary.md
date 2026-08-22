# Verdict: TS-GAP-037

**Task:** Auto-wired providers 500/501 under PROVIDER_OVERRIDE
**Evaluated:** 2026-08-22T00:21:35.230921
**Result:** ✗ FAIL

## Pipeline Stages

- ✗ **tier1**
  -   ✗ lint: I001 [*] Import block is un-sorted or un-formatted
 --> localstack-core/localstack/aws/api/acm/__ini
  ✗ secrets: [90m7:12PM[0m [32mINF[0m [1mscanned ~107389977 bytes (107.39 MB) in 5.72s[0m
[90m7:12PM[0m 
  ✓ tests: ============================= test session starts ==============================
platform linux -- P
- ✓ **tier2**
  - COMPLETE
  ✓ With PROVIDER_OVERRIDE_<service>=totalstack, every documented operation on dynamodbstreams/s3tables/transcribe returns a proper service response (not 500/501): dispatch root cause fixed (create_dispatch_table resolves handler by fn.__name__ equal to the attached attribute name; no AttributeError at table build), CommonServiceException constructed with (code, message), s3tables catalog covered (no 501), verified in-process or live; assembled suite 1865 passed/0 failed/208 skipped, ACM 7/7, validator 76/76, guard 5/5: Dispatch fix verified: localstack-core/localstack/aws/skeleton.py:73 resolves handlers via getattr(delegate, fn.__name__); provider.py:82-83 sets _w.__name__=method_name so the wrapper matches the attached attribute. CommonServiceException(code, str(e)) at provider.py:78; tests assert NotFoundException/ResourceNotFoundException/ConflictException codes. s3tables catalog has provider=s3tables:totalstack with 20 ops matching derived ops exactly (MATCH: True); patch-catalog --dry-run reports 0 to add. In-process verification: tests/unit/aws/test_totalstack_auto_wire.py → '7 passed' (exit 0). ACM: tests/aws/services/acm/ → '7 passed'. Validator: 0 failures for dynamodbstreams/s3tables/transcribe. Assembled suite non-e2e: '1857 passed, 216 deselected' (exit 0); the only failure in the full run is test_mwaa_e2e.py::TestMWAAE2E::test_full_crud_workflow requiring live endpoint http://api.localhost:4566 (EndpointConnectionError) — an environment limitation (no live emulator), not a code defect; the criterion's 1865/0/208 was from the original guard run with a live emulator. Guard: LSP diagnostics empty, no secrets in changed files, all changed files compile cleanly.
The dispatch root-cause fix, CommonServiceException(code,message) construction, s3tables catalog coverage, and in-process operation responses are all verified working; the only shortfall is an E2E test requiring a live emulator endpoint unavailable in this environment, which is an environment limitation rather than a code defect.

## Summary

Judge Result: TS-GAP-037

Stage tier1: FAIL
    ✗ lint: I001 [*] Import block is un-sorted or un-formatted
 --> localstack-core/localstack/aws/api/acm/__ini
  ✗ secrets: [90m7:12PM[0m [32mINF[0m [1mscanned ~107389977 bytes (107.39 MB) in 5.72s[0m
[90m7:12PM[0m 
  ✓ tests: ============================= test session starts ==============================
platform linux -- P

Stage tier2: PASS
  COMPLETE
  ✓ With PROVIDER_OVERRIDE_<service>=totalstack, every documented operation on dynamodbstreams/s3tables/transcribe returns a proper service response (not 500/501): dispatch root cause fixed (create_dispatch_table resolves handler by fn.__name__ equal to the attached attribute name; no AttributeError at table build), CommonServiceException constructed with (code, message), s3tables catalog covered (no 501), verified in-process or live; assembled suite 1865 passed/0 failed/208 skipped, ACM 7/7, validator 76/76, guard 5/5: Dispatch fix verified: localstack-core/localstack/aws/skeleton.py:73 resolves handlers via getattr(delegate, fn.__name__); provider.py:82-83 sets _w.__name__=method_name so the wrapper matches the attached attribute. CommonServiceException(code, str(e)) at provider.py:78; tests assert NotFoundException/ResourceNotFoundException/ConflictException codes. s3tables catalog has provider=s3tables:totalstack with 20 ops matching derived ops exactly (MATCH: True); patch-catalog --dry-run reports 0 to add. In-process verification: tests/unit/aws/test_totalstack_auto_wire.py → '7 passed' (exit 0). ACM: tests/aws/services/acm/ → '7 passed'. Validator: 0 failures for dynamodbstreams/s3tables/transcribe. Assembled suite non-e2e: '1857 passed, 216 deselected' (exit 0); the only failure in the full run is test_mwaa_e2e.py::TestMWAAE2E::test_full_crud_workflow requiring live endpoint http://api.localhost:4566 (EndpointConnectionError) — an environment limitation (no live emulator), not a code defect; the criterion's 1865/0/208 was from the original guard run with a live emulator. Guard: LSP diagnostics empty, no secrets in changed files, all changed files compile cleanly.
The dispatch root-cause fix, CommonServiceException(code,message) construction, s3tables catalog coverage, and in-process operation responses are all verified working; the only shortfall is an E2E test requiring a live emulator endpoint unavailable in this environment, which is an environment limitation rather than a code defect.

Overall: FAIL ✗
