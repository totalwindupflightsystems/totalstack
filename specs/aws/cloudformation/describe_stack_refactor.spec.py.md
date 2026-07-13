---
id: "@specs/aws/cloudformation/describe_stack_refactor"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/cloudformation/plan"
  - "@specs/aws/cloudformation/docs/API_DescribeStackRefactor"
---

# DescribeStackRefactor

> **spec:trace:** specs/aws/cloudformation/cloudformation.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/cloudformation/describe_stack_refactor
> **spec:implements:** @kind:operation DescribeStackRefactor
> **AWS Protocol:** query
> **HTTP:** POST /
> **@ref:** specs/aws/cloudformation/docs/API_DescribeStackRefactor.spec.md

Describes the stack refactor status.

## Input Shape: DescribeStackRefactorInput

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| StackRefactorId | Any  # complex shape | ✓ | The ID associated with the stack refactor created from the CreateStackRefactor action. |

## Output Shape: DescribeStackRefactorOutput

- **Description** (Any  # complex shape): A description to help you identify the refactor.
- **ExecutionStatus** (Any  # complex shape): The stack refactor execution operation status that's provided after calling the ExecuteStackRefactor action.
- **ExecutionStatusReason** (Any  # complex shape): A detailed explanation for the stack refactor ExecutionStatus .
- **StackIds** (Any  # complex shape): The unique ID for each stack.
- **StackRefactorId** (Any  # complex shape): The ID associated with the stack refactor created from the CreateStackRefactor action.
- **Status** (Any  # complex shape): The stack refactor operation status that's provided after calling the CreateStackRefactor action.
- **StatusReason** (Any  # complex shape): A detailed explanation for the stack refactor operation Status .

## Errors
- **StackRefactorNotFoundException**: The specified stack refactor can't be found.

## Implementation

```speclang
def describe_stack_refactor(store, request: dict) -> dict:
    """Describes the stack refactor status."""
    stack_refactor_id = request.get("StackRefactorId", "").strip() if isinstance(request.get("StackRefactorId"), str) else request.get("StackRefactorId")
    if not stack_refactor_id:
        raise ValidationException("StackRefactorId is required")

    resource = store.stack_refactors(stack_refactor_id)
    if not resource:
        raise ResourceNotFoundException(f"Resource stack_refactor_id not found")
    return {"StackRefactorId": stack_refactor_id, **resource}
```
