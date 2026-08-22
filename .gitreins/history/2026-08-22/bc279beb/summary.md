# Verdict: TS-GAP-038

**Task:** Fix 5 stale auto-wired providers (cloudfront/cloudtrail/cognito-identity/ecr/transfer) still using the old _w-named _attach_handler wrapper
**Evaluated:** 2026-08-22T10:58:49.983381
**Result:** ✗ FAIL

## Pipeline Stages

- ✗ **tier1**
  -   ✗ lint: I001 [*] Import block is un-sorted or un-formatted
 --> localstack-core/localstack/aws/api/acm/__ini
  ✗ secrets: [90m5:51AM[0m [32mINF[0m [1mscanned ~107147068 bytes (107.15 MB) in 5.38s[0m
[90m5:51AM[0m 
  ✓ tests: ============================= test session starts ==============================
platform linux -- P
- ✓ **tier2**
  - COMPLETE
  ✓ PASS: no totalstack/services/{cloudfront,cloudtrail,cognito-identity,ecr,transfer}/provider.py contains a _w-named handler wrapper; each provider dispatches under PROVIDER_OVERRIDE_<svc>=totalstack; regression tests cover all 5 services and pass; gitreins guard 5/5. EVIDENCE (committed, foreman-verified 2026-08-22): (1) grep -c "def _w" = 0 in all 5 provider files after commit 6c5de27de7 (local wrapper def renamed to _wrapper, runtime __name__/__qualname__ set to the op method name at attach time, so create_dispatch_table getattr(delegate, fn.__name__) resolves); (2) committed regression suite tests/unit/aws/test_totalstack_auto_wire.py (17 passed) sets PROVIDER_OVERRIDE_<svc>=totalstack for all 5 services, imports each provider class, builds MotoFallbackDispatcher dispatch tables in-process (the repo's dispatch mechanism; PROVIDER_OVERRIDE selection lives in localstack-core provider registration, not in the provider files), asserts wrapper.__name__ == method_name, and invokes ops incl. typed error mapping (test_stale_provider_attach_handler_names_wrapper_and_maps_errors); (3) gitreins guard Tier 1 5/5 PASS on both worker commit 1f3bfb3971 (foreman re-run 05:43) and foreman commit 6c5de27de7 (auto pre-commit hook); tier1 lint/secrets phantoms in judge runs are pre-existing upstream debt (localstack-core I001 acm/__init__.py, documented TS-GAP-031/037).: All 5 provider files (cloudfront/cloudtrail/cognito-identity/ecr/transfer) have the wrapper renamed to _wrapper (commit 6c5de27de7), with runtime __name__/__qualname__ set to method_name (provider.py:86-87); grep -nE 'def _w([^a-zA-Z_]|$)' finds no _w-named wrapper in any file. PROVIDER_OVERRIDE_<svc>=totalstack set for all 5 in tests/unit/aws/test_totalstack_auto_wire.py; totalstack/providers.py registers each via @aws_provider(api=..., name='totalstack') with MotoFallbackDispatcher. Regression suite: 17 passed (verified: .venv/bin/python -m pytest tests/unit/aws/test_totalstack_auto_wire.py --tb=short -q => '17 passed'), covering all 5 services via test_dispatch_table_builds_with_all_handler_ops and test_stale_provider_attach_handler_names_wrapper_and_maps_errors (asserts wrapper.__name__==method_name and typed CommonServiceException mapping). Changed files clean: ruff 'All checks passed!', no LSP diagnostics. gitreins guard: secrets/lint/static_analysis/lsp all pass; the only full-suite test failure is test_fsx_e2e.py (SubnetIds ParamValidationError) — a pre-existing FSx e2e issue unrelated to TS-GAP-038, consistent with the criterion's documented pre-existing upstream debt.


## Summary

Judge Result: TS-GAP-038

Stage tier1: FAIL
    ✗ lint: I001 [*] Import block is un-sorted or un-formatted
 --> localstack-core/localstack/aws/api/acm/__ini
  ✗ secrets: [90m5:51AM[0m [32mINF[0m [1mscanned ~107147068 bytes (107.15 MB) in 5.38s[0m
[90m5:51AM[0m 
  ✓ tests: ============================= test session starts ==============================
platform linux -- P

Stage tier2: PASS
  COMPLETE
  ✓ PASS: no totalstack/services/{cloudfront,cloudtrail,cognito-identity,ecr,transfer}/provider.py contains a _w-named handler wrapper; each provider dispatches under PROVIDER_OVERRIDE_<svc>=totalstack; regression tests cover all 5 services and pass; gitreins guard 5/5. EVIDENCE (committed, foreman-verified 2026-08-22): (1) grep -c "def _w" = 0 in all 5 provider files after commit 6c5de27de7 (local wrapper def renamed to _wrapper, runtime __name__/__qualname__ set to the op method name at attach time, so create_dispatch_table getattr(delegate, fn.__name__) resolves); (2) committed regression suite tests/unit/aws/test_totalstack_auto_wire.py (17 passed) sets PROVIDER_OVERRIDE_<svc>=totalstack for all 5 services, imports each provider class, builds MotoFallbackDispatcher dispatch tables in-process (the repo's dispatch mechanism; PROVIDER_OVERRIDE selection lives in localstack-core provider registration, not in the provider files), asserts wrapper.__name__ == method_name, and invokes ops incl. typed error mapping (test_stale_provider_attach_handler_names_wrapper_and_maps_errors); (3) gitreins guard Tier 1 5/5 PASS on both worker commit 1f3bfb3971 (foreman re-run 05:43) and foreman commit 6c5de27de7 (auto pre-commit hook); tier1 lint/secrets phantoms in judge runs are pre-existing upstream debt (localstack-core I001 acm/__init__.py, documented TS-GAP-031/037).: All 5 provider files (cloudfront/cloudtrail/cognito-identity/ecr/transfer) have the wrapper renamed to _wrapper (commit 6c5de27de7), with runtime __name__/__qualname__ set to method_name (provider.py:86-87); grep -nE 'def _w([^a-zA-Z_]|$)' finds no _w-named wrapper in any file. PROVIDER_OVERRIDE_<svc>=totalstack set for all 5 in tests/unit/aws/test_totalstack_auto_wire.py; totalstack/providers.py registers each via @aws_provider(api=..., name='totalstack') with MotoFallbackDispatcher. Regression suite: 17 passed (verified: .venv/bin/python -m pytest tests/unit/aws/test_totalstack_auto_wire.py --tb=short -q => '17 passed'), covering all 5 services via test_dispatch_table_builds_with_all_handler_ops and test_stale_provider_attach_handler_names_wrapper_and_maps_errors (asserts wrapper.__name__==method_name and typed CommonServiceException mapping). Changed files clean: ruff 'All checks passed!', no LSP diagnostics. gitreins guard: secrets/lint/static_analysis/lsp all pass; the only full-suite test failure is test_fsx_e2e.py (SubnetIds ParamValidationError) — a pre-existing FSx e2e issue unrelated to TS-GAP-038, consistent with the criterion's documented pre-existing upstream debt.


Overall: FAIL ✗
