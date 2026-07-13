---
id: "@specs/aws/cloudformation/describe_stack_set"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/cloudformation/plan"
  - "@specs/aws/cloudformation/docs/API_DescribeStackSet"
---

# DescribeStackSet

> **spec:trace:** specs/aws/cloudformation/cloudformation.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/cloudformation/describe_stack_set
> **spec:implements:** @kind:operation DescribeStackSet
> **AWS Protocol:** query
> **HTTP:** POST /
> **@ref:** specs/aws/cloudformation/docs/API_DescribeStackSet.spec.md

Returns the description of the specified StackSet. This API provides strongly consistent reads meaning it will always return the most up-to-date data.

## Input Shape: DescribeStackSetInput

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| CallAs | Any  # complex shape |  | [Service-managed permissions] Specifies whether you are acting as an account administrator in the organization's managem |
| StackSetName | Any  # complex shape | ✓ | The name or unique ID of the StackSet whose description you want. |

## Output Shape: DescribeStackSetOutput

- **StackSet** (Any  # complex shape): The specified StackSet.

## Errors
- **StackSetNotFoundException**: The specified StackSet doesn't exist.

## Implementation

```speclang
def describe_stack_set(store, request: dict) -> dict:
    """Returns the description of the specified StackSet. This API provides strongly consistent reads meaning it will always return the most up-to-date data."""
    stack_set_name = request.get("StackSetName", "").strip() if isinstance(request.get("StackSetName"), str) else request.get("StackSetName")
    if not stack_set_name:
        raise ValidationException("StackSetName is required")

    resource = store.stack_sets(stack_set_name)
    if not resource:
        raise ResourceNotFoundException(f"Resource stack_set_name not found")
    return {"StackSetName": stack_set_name, **resource}
```
