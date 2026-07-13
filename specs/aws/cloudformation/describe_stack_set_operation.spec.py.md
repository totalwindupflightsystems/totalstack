---
id: "@specs/aws/cloudformation/describe_stack_set_operation"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/cloudformation/plan"
  - "@specs/aws/cloudformation/docs/API_DescribeStackSetOperation"
---

# DescribeStackSetOperation

> **spec:trace:** specs/aws/cloudformation/cloudformation.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/cloudformation/describe_stack_set_operation
> **spec:implements:** @kind:operation DescribeStackSetOperation
> **AWS Protocol:** query
> **HTTP:** POST /
> **@ref:** specs/aws/cloudformation/docs/API_DescribeStackSetOperation.spec.md

Returns the description of the specified StackSet operation. This API provides strongly consistent reads meaning it will always return the most up-to-date data.

## Input Shape: DescribeStackSetOperationInput

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| CallAs | Any  # complex shape |  | [Service-managed permissions] Specifies whether you are acting as an account administrator in the organization's managem |
| OperationId | Any  # complex shape | ✓ | The unique ID of the StackSet operation. |
| StackSetName | Any  # complex shape | ✓ | The name or the unique stack ID of the StackSet for the stack operation. |

## Output Shape: DescribeStackSetOperationOutput

- **StackSetOperation** (Any  # complex shape): The specified StackSet operation.

## Errors
- **StackSetNotFoundException**: The specified StackSet doesn't exist.
- **OperationNotFoundException**: The specified ID refers to an operation that doesn't exist.

## Implementation

```speclang
def describe_stack_set_operation(store, request: dict) -> dict:
    """Returns the description of the specified StackSet operation. This API provides strongly consistent reads meaning it will always return the most up-to-date data."""
    operation_id = request.get("OperationId", "").strip() if isinstance(request.get("OperationId"), str) else request.get("OperationId")
    if not operation_id:
        raise ValidationException("OperationId is required")
    stack_set_name = request.get("StackSetName", "").strip() if isinstance(request.get("StackSetName"), str) else request.get("StackSetName")
    if not stack_set_name:
        raise ValidationException("StackSetName is required")

    resource = store.stack_set_operations(stack_set_name)
    if not resource:
        raise ResourceNotFoundException(f"Resource stack_set_name not found")
    return {"StackSetName": stack_set_name, **resource}
```
