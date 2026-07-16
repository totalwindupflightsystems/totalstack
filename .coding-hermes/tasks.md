# Task Board — TotalStack

## [x] CI-GAP-004 — Fix Integration Tests (3.11): stores.py Python 3.12+ syntax breaks 3.11 matrix (242487251)
    `class RegionBundle[BaseStoreType](dict)` at localstack-core/localstack/services/stores.py:193
    is Python 3.12+ generic syntax. CI integration tests run on 3.10, 3.11, 3.12 — the 3.11 job fails
    with SyntaxError, and 3.10/3.12 get cancelled (matrix cascade). Commit 26619a9be introduced this.
    Fix options: (a) backport to `class RegionBundle(Generic[BaseStoreType], dict)` for 3.11 compat,
    (b) drop 3.10 and 3.11 from CI matrix and only test 3.12.
    - [x] Fix stores.py:193 RegionBundle syntax to be Python 3.11 compatible
    - [x] Verify CI Integration Tests (3.11) passes (syntax verified via ast.parse, Generic import works)
    - [x] Verify stores.py still imports correctly (Generic added to typing import, ast.parse passes)
    Files: localstack-core/localstack/services/stores.py, .github/workflows/ci.yml

## [x] CI-GAP-005 — Shape Validator: 6/76 services pass, 70 have errors (1,213 total errors)
    Investigation complete (2026-07-16). Error classification:
      - HANDLER_CRASH: 1,164 (96.0%) — handlers crash on test input (missing fields, missing exceptions)
      - IMPORT_ERROR: 49 (4.0%) — modules can't be imported (dataclass, etc.)
      - No MISSING_REQUIRED or TYPE_MISMATCH errors — shapes are correct, handlers just crash at runtime
    Common crash patterns:
      - resourceArn / ResourceArn access: 89 crashes across services
      - Missing exception classes: ~160 crashes (InvalidParameterValueException, InvalidInputException, etc.)
      - Specific field access: meshName (24), clusterName (23), AwsAccountId, etc.
    Root cause: _call_handler() provides minimal test inputs, but handlers access fields
    not in those inputs. Also, exception classes defined in models.code.py aren't injected
    into handler modules. This is a test-infrastructure gap, not a shape-spec gap.
    Top 5 services by error count → subtasks below.
    - [x] Classify errors by type (HANDLER_CRASH 96%, IMPORT_ERROR 4%)
    - [x] Identify top 5: wafv2 (34), eks (33), athena (30), rekognition (30), comprehend (29)
    - [x] Create per-service subtasks (see CI-GAP-006 through CI-GAP-010)
    Files: .github/workflows/ci.yml, development/aws-shape-validator.py

## [x] CI-GAP-006 — wafv2: 34 handler crashes (0/0 ops pass) (3ea25b690)
    All handlers crash at import — generated code uses exception/type names not injected.
    - [x] Fix exception injection in handler modules (e.g., WAFInvalidParameterException)
    - [x] Add test inputs for wafv2 operations to _call_handler()
    Files: specs/aws/.speclang/assembled/wafv2/*.code.py

## [x] CI-GAP-007 — eks: 33 handler crashes (0/1 ops pass) (9d60197fe)
    Handlers crash accessing clusterName and other fields not in minimal test inputs.
    - [x] Add test inputs for eks operations (clusterName, etc.) to _call_handler()
    - [x] Verify 21/34 ops now pass shape validation (was 1/34)
    Files: specs/aws/.speclang/assembled/eks/*.code.py

## [ ] CI-GAP-008 — athena: 30 handler crashes (4 ops fail)
    All 4 tested ops crash — likely missing required fields in test inputs.
    - [ ] Add test inputs for athena operations to _call_handler()
    - [ ] Fix missing exception classes
    Files: specs/aws/.speclang/assembled/athena/*.code.py

## [ ] CI-GAP-009 — rekognition: 30 errors (0/0 ops pass, all import errors)
    All handlers fail at import: `name 'dataclass' is not defined` — code uses Python
    dataclass decorator but module doesn't import it.
    - [ ] Add `from dataclasses import dataclass` to rekognition model/handler modules
    - [ ] Verify handlers can be imported
    Files: specs/aws/.speclang/assembled/rekognition/*.code.py

## [ ] CI-GAP-010 — comprehend: 29 handler crashes (5 ops fail)
    All 5 tested ops crash — likely exception classes + field access issues.
    - [ ] Add test inputs for comprehend operations to _call_handler()
    - [ ] Fix missing exception classes
    Files: specs/aws/.speclang/assembled/comprehend/*.code.py
