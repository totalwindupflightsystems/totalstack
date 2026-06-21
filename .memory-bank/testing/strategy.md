# TotalStack Testing Strategy

## Philosophy
> Mock tests are not good enough. Prove every spec-generated service works against a real LocalStack store and against a running emulator via boto3.

## Test Pyramid (TotalStack-specific)

```
        ┌─────────┐
        │   E2E   │  boto3 client → running localstack → full workflow
        │  (1-3)  │  Example: create_table → put_item → get_item → delete_table
        ├─────────┤
        │Integration│  Import generated code → real LocalStack store
        │ (5-10)   │  Example: create_table() with real DynamoDBStore
        ├─────────┤
        │  Unit   │  These are spec structure checks (GitReins eval)
        │ (spec)  │  Validates: meta/plan/ops exist, code generated, trace annotations
        └─────────┘
```

## Per-Service Minimum Bar

### Integration Tests (MANDATORY)
- **3+ operations tested** with real LocalStack stores
- **1 error path tested** per operation (validation, not-found, conflict)
- **Test file**: `specs/aws/.speclang/assembled/_tests/test_<service>_integration.py`
- **Runner**: `pytest -x --tb=short specs/aws/.speclang/assembled/_tests/`

### E2E Tests (MANDATORY)
- **1 complete workflow** per service (create → use → verify → cleanup)
- **Uses boto3** against a running localstack instance
- **Test file**: `specs/aws/.speclang/assembled/_tests/test_<service>_e2e.py`
- **Runner**: `pytest -x --tb=short` with `LOCALSTACK_ENDPOINT=http://localhost:4566`

### What "Done" Looks Like
A service is **done** ONLY when ALL of these pass:
1. ✅ Spec structure complete (meta + plan + all ops as .spec.py.md)
2. ✅ Code generated for all ops (.code.py files exist, >50 lines, valid Python)
3. ✅ Integration tests pass (3+ ops, real stores)
4. ✅ E2E tests pass (1+ workflow, boto3 against running instance)
5. ✅ GitReins guard passes (secrets + lint + tests)

## Installation Requirement
To run integration/E2E tests, `localstack` must be installed:
```bash
cd ~/totalstack && pip install -e localstack-core/
```

## GitReins Enforcement
Task criteria for every service MUST include:
- "Integration tests exist for at least 3 operations"
- "Integration tests pass (pytest exit code 0)"
- "E2E test exercises complete workflow via boto3"
- "E2E test passes against running localstack instance"

## Anti-Patterns (DO NOT DO)
- ❌ Claiming a service is "done" because specs exist and code was generated
- ❌ Mocking the store without verifying real store behavior
- ❌ Skipping E2E because "the integration test covers it"
- ❌ Writing tests that don't actually run (import errors, missing deps)
- ❌ Using `forward_request` in generated code without testing the delegation chain
