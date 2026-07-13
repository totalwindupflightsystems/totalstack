---
id: "@specs/aws/cloudformation/describe_stack_resource"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/cloudformation/plan"
  - "@specs/aws/cloudformation/docs/API_DescribeStackResource"
---

# DescribeStackResource

> **spec:trace:** specs/aws/cloudformation/cloudformation.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/cloudformation/describe_stack_resource
> **spec:implements:** @kind:operation DescribeStackResource
> **AWS Protocol:** query
> **HTTP:** POST /
> **@ref:** specs/aws/cloudformation/docs/API_DescribeStackResource.spec.md

Returns a description of the specified resource in the specified stack. For deleted stacks, DescribeStackResource returns resource information for up to 90 days after the stack has been deleted.

## Input Shape: DescribeStackResourceInput

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| LogicalResourceId | Any  # complex shape | ✓ | The logical name of the resource as specified in the template. |
| StackName | Any  # complex shape | ✓ | The name or the unique stack ID that's associated with the stack, which aren't always interchangeable: Running stacks: Y |

## Output Shape: DescribeStackResourceOutput

- **StackResourceDetail** (Any  # complex shape): A StackResourceDetail structure that contains the description of the specified resource in the specified stack.

## Implementation

```speclang
def describe_stack_resource(store, request: dict) -> dict:
    """Returns a description of the specified resource in the specified stack. For deleted stacks, DescribeStackResource returns resource information for up to 90 days after the stack has been deleted."""
    logical_resource_id = request.get("LogicalResourceId", "").strip() if isinstance(request.get("LogicalResourceId"), str) else request.get("LogicalResourceId")
    if not logical_resource_id:
        raise ValidationException("LogicalResourceId is required")
    stack_name = request.get("StackName", "").strip() if isinstance(request.get("StackName"), str) else request.get("StackName")
    if not stack_name:
        raise ValidationException("StackName is required")

    resource = store.stack_resources(logical_resource_id)
    if not resource:
        raise ResourceNotFoundException(f"Resource logical_resource_id not found")
    return {"LogicalResourceId": logical_resource_id, **resource}
```
