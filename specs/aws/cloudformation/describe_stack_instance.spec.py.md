---
id: "@specs/aws/cloudformation/describe_stack_instance"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/cloudformation/plan"
  - "@specs/aws/cloudformation/docs/API_DescribeStackInstance"
---

# DescribeStackInstance

> **spec:trace:** specs/aws/cloudformation/cloudformation.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/cloudformation/describe_stack_instance
> **spec:implements:** @kind:operation DescribeStackInstance
> **AWS Protocol:** query
> **HTTP:** POST /
> **@ref:** specs/aws/cloudformation/docs/API_DescribeStackInstance.spec.md

Returns the stack instance that's associated with the specified StackSet, Amazon Web Services account, and Amazon Web Services Region. For a list of stack instances that are associated with a specific StackSet, use ListStackInstances .

## Input Shape: DescribeStackInstanceInput

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| CallAs | Any  # complex shape |  | [Service-managed permissions] Specifies whether you are acting as an account administrator in the organization's managem |
| StackInstanceAccount | Any  # complex shape | ✓ | The ID of an Amazon Web Services account that's associated with this stack instance. |
| StackInstanceRegion | Any  # complex shape | ✓ | The name of a Region that's associated with this stack instance. |
| StackSetName | Any  # complex shape | ✓ | The name or the unique stack ID of the StackSet that you want to get stack instance information for. |

## Output Shape: DescribeStackInstanceOutput

- **StackInstance** (Any  # complex shape): The stack instance that matches the specified request parameters.

## Errors
- **StackSetNotFoundException**: The specified StackSet doesn't exist.
- **StackInstanceNotFoundException**: The specified stack instance doesn't exist.

## Implementation

```speclang
def describe_stack_instance(store, request: dict) -> dict:
    """Returns the stack instance that's associated with the specified StackSet, Amazon Web Services account, and Amazon Web Services Region. For a list of stack instances that are associated with a specific"""
    stack_instance_account = request.get("StackInstanceAccount", "").strip() if isinstance(request.get("StackInstanceAccount"), str) else request.get("StackInstanceAccount")
    if not stack_instance_account:
        raise ValidationException("StackInstanceAccount is required")
    stack_instance_region = request.get("StackInstanceRegion", "").strip() if isinstance(request.get("StackInstanceRegion"), str) else request.get("StackInstanceRegion")
    if not stack_instance_region:
        raise ValidationException("StackInstanceRegion is required")
    stack_set_name = request.get("StackSetName", "").strip() if isinstance(request.get("StackSetName"), str) else request.get("StackSetName")
    if not stack_set_name:
        raise ValidationException("StackSetName is required")

    resource = store.stack_instances(stack_set_name)
    if not resource:
        raise ResourceNotFoundException(f"Resource stack_set_name not found")
    return {"StackSetName": stack_set_name, **resource}
```
