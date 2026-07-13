---
id: "@specs/aws/cloudformation/stop_stack_set_operation"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/cloudformation/plan"
  - "@specs/aws/cloudformation/docs/API_StopStackSetOperation"
---

# StopStackSetOperation

> **spec:trace:** specs/aws/cloudformation/cloudformation.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/cloudformation/stop_stack_set_operation
> **spec:implements:** @kind:operation StopStackSetOperation
> **AWS Protocol:** query
> **HTTP:** POST /
> **@ref:** specs/aws/cloudformation/docs/API_StopStackSetOperation.spec.md

Stops an in-progress operation on a StackSet and its associated stack instances. StackSets will cancel all the unstarted stack instance deployments and wait for those are in-progress to complete.

## Input Shape: StopStackSetOperationInput

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| CallAs | Any  # complex shape |  | Specifies whether you are acting as an account administrator in the organization's management account or as a delegated  |
| OperationId | Any  # complex shape | ✓ | The ID of the stack operation. |
| StackSetName | Any  # complex shape | ✓ | The name or unique ID of the StackSet that you want to stop the operation for. |

## Output Shape: StopStackSetOperationOutput


## Errors
- **StackSetNotFoundException**: The specified StackSet doesn't exist.
- **OperationNotFoundException**: The specified ID refers to an operation that doesn't exist.
- **InvalidOperationException**: The specified operation isn't valid.

## Implementation

```speclang
def stop_stack_set_operation(store, request: dict) -> dict:
    """Stops an in-progress operation on a StackSet and its associated stack instances. StackSets will cancel all the unstarted stack instance deployments and wait for those are in-progress to complete."""
    operation_id = request.get("OperationId", "").strip() if isinstance(request.get("OperationId"), str) else request.get("OperationId")
    stack_set_name = request.get("StackSetName", "").strip() if isinstance(request.get("StackSetName"), str) else request.get("StackSetName")

    if not store.stack_set_operations(stack_set_name):
        raise ResourceNotFoundException(f"Resource stack_set_name not found")
    store.delete_stack_set_operations(stack_set_name)
    return {}
```
