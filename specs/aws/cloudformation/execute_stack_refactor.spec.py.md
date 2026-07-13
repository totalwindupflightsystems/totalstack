---
id: "@specs/aws/cloudformation/execute_stack_refactor"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/cloudformation/plan"
  - "@specs/aws/cloudformation/docs/API_ExecuteStackRefactor"
---

# ExecuteStackRefactor

> **spec:trace:** specs/aws/cloudformation/cloudformation.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/cloudformation/execute_stack_refactor
> **spec:implements:** @kind:operation ExecuteStackRefactor
> **AWS Protocol:** query
> **HTTP:** POST /
> **@ref:** specs/aws/cloudformation/docs/API_ExecuteStackRefactor.spec.md

Executes the stack refactor operation.

## Input Shape: ExecuteStackRefactorInput

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| StackRefactorId | Any  # complex shape | ✓ | The ID associated with the stack refactor created from the CreateStackRefactor action. |

## Implementation

```speclang
def execute_stack_refactor(store, request: dict) -> dict:
    """Executes the stack refactor operation."""
    stack_refactor_id = request.get("StackRefactorId", "").strip() if isinstance(request.get("StackRefactorId"), str) else request.get("StackRefactorId")
    if not stack_refactor_id:
        raise ValidationException("StackRefactorId is required")

    # Auto-generated handler — operation not classified as CRUD
    return store.execute("ExecuteStackRefactor", request)
```
