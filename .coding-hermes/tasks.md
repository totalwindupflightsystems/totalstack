# Task Board — TotalStack

## [ ] CI-GAP-004 — Fix Integration Tests (3.11): stores.py Python 3.12+ syntax breaks 3.11 matrix
    `class RegionBundle[BaseStoreType](dict)` at localstack-core/localstack/services/stores.py:193
    is Python 3.12+ generic syntax. CI integration tests run on 3.10, 3.11, 3.12 — the 3.11 job fails
    with SyntaxError, and 3.10/3.12 get cancelled (matrix cascade). Commit 26619a9be introduced this.
    Fix options: (a) backport to `class RegionBundle(Generic[BaseStoreType], dict)` for 3.11 compat,
    (b) drop 3.10 and 3.11 from CI matrix and only test 3.12.
    - [ ] Fix stores.py:193 RegionBundle syntax to be Python 3.11 compatible
    - [ ] Verify CI Integration Tests (3.11) passes
    - [ ] Verify stores.py still imports correctly (from typing import Generic if needed)
    Files: localstack-core/localstack/services/stores.py, .github/workflows/ci.yml

## [ ] CI-GAP-005 — Shape Validator: 6/76 services pass, 70 have errors
    AWS Shape Validator job (ci.yml:80-91) reports 6/76 services pass validation. Errors are
    across 70 services — shape mismatches between generated .code.py files and AWS API shapes.
    This is the broad remaining spec-gap work after SPEC-GAP-001 through SPEC-GAP-005.
    - [ ] Classify shape validator errors by type (missing ops, type mismatches, model gaps)
    - [ ] Identify top 5 highest-impact services (most errors or most operations)
    - [ ] Create per-service subtasks for the top 5
    Files: .github/workflows/ci.yml, development/aws-shape-validator.py
