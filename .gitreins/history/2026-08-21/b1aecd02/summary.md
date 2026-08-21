# Verdict: ts-gap-034

**Task:** Per-service API reference tables in docs/API.md (TS-GAP-034)
**Evaluated:** 2026-08-21T17:35:30.895966
**Result:** ✗ FAIL

## Pipeline Stages

- ✗ **tier1**
  -   ✗ lint: I001 [*] Import block is un-sorted or un-formatted
 --> localstack-core/localstack/aws/api/acm/__ini
  ✗ secrets: [90m12:33PM[0m [32mINF[0m [1mscanned ~107042144 bytes (107.04 MB) in 3.82s[0m
[90m12:33PM[0m
  ✓ tests: ============================= test session starts ==============================
platform linux -- P
- ✓ **tier2**
  - COMPLETE
  ✓ docs/API.md contains an operations table for acm and at least 2 other services (dynamodbstreams, s3tables, or transcribe), each row listing operation name, implemented-vs-Moto-fallback status, and error behavior; commit message references TS-GAP-034: HEAD commit 64ed9037aa adds per-service tables to docs/API.md for acm, dynamodbstreams, s3tables, and transcribe (git show HEAD:docs/API.md | grep '^### ' confirms all four). Each table has columns 'Operation | Status | Notable errors/behavior'; rows list operation name, Implemented/Moto fallback status, and error behavior (e.g. acm RequestCertificate: 'Implemented | LimitExceededException past 1000 certs; creates AMAZON_ISSUED cert in PENDING_VALIDATION...'; transcribe rows show 'Moto fallback | State kept in Moto; Moto error shapes'). acm plus 3 other services satisfies the 'at least 2' requirement. Commit message: 'docs(api): add per-service operation reference tables to docs/API.md — op-level implemented/Moto-fallback status and error behavior for acm + 3 tested services. Addresses TS-GAP-034.' explicitly references TS-GAP-034.
docs/API.md contains operations tables for acm, dynamodbstreams, s3tables, and transcribe with operation name, implemented/Moto-fallback status, and error behavior per row, and the commit message references TS-GAP-034.

## Summary

Judge Result: ts-gap-034

Stage tier1: FAIL
    ✗ lint: I001 [*] Import block is un-sorted or un-formatted
 --> localstack-core/localstack/aws/api/acm/__ini
  ✗ secrets: [90m12:33PM[0m [32mINF[0m [1mscanned ~107042144 bytes (107.04 MB) in 3.82s[0m
[90m12:33PM[0m
  ✓ tests: ============================= test session starts ==============================
platform linux -- P

Stage tier2: PASS
  COMPLETE
  ✓ docs/API.md contains an operations table for acm and at least 2 other services (dynamodbstreams, s3tables, or transcribe), each row listing operation name, implemented-vs-Moto-fallback status, and error behavior; commit message references TS-GAP-034: HEAD commit 64ed9037aa adds per-service tables to docs/API.md for acm, dynamodbstreams, s3tables, and transcribe (git show HEAD:docs/API.md | grep '^### ' confirms all four). Each table has columns 'Operation | Status | Notable errors/behavior'; rows list operation name, Implemented/Moto fallback status, and error behavior (e.g. acm RequestCertificate: 'Implemented | LimitExceededException past 1000 certs; creates AMAZON_ISSUED cert in PENDING_VALIDATION...'; transcribe rows show 'Moto fallback | State kept in Moto; Moto error shapes'). acm plus 3 other services satisfies the 'at least 2' requirement. Commit message: 'docs(api): add per-service operation reference tables to docs/API.md — op-level implemented/Moto-fallback status and error behavior for acm + 3 tested services. Addresses TS-GAP-034.' explicitly references TS-GAP-034.
docs/API.md contains operations tables for acm, dynamodbstreams, s3tables, and transcribe with operation name, implemented/Moto-fallback status, and error behavior per row, and the commit message references TS-GAP-034.

Overall: FAIL ✗
