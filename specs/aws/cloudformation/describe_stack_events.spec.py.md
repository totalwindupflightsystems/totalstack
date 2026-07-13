---
id: "@specs/aws/cloudformation/describe_stack_events"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/cloudformation/plan"
  - "@specs/aws/cloudformation/docs/API_DescribeStackEvents"
---

# DescribeStackEvents

> **spec:trace:** specs/aws/cloudformation/cloudformation.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/cloudformation/describe_stack_events
> **spec:implements:** @kind:operation DescribeStackEvents
> **AWS Protocol:** query
> **HTTP:** POST /
> **@ref:** specs/aws/cloudformation/docs/API_DescribeStackEvents.spec.md

Returns all stack related events for a specified stack in reverse chronological order. For more information about a stack's event history, see Understand CloudFormation stack creation events in the CloudFormation User Guide . You can list events for stacks that have failed to create or have been deleted by specifying the unique stack identifier (stack ID).

## Input Shape: DescribeStackEventsInput

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| NextToken | Any  # complex shape |  | The token for the next set of items to return. (You received this token from a previous call.) |
| StackName | Any  # complex shape | ✓ | The name or the unique stack ID that's associated with the stack, which aren't always interchangeable: Running stacks: Y |

## Output Shape: DescribeStackEventsOutput

- **NextToken** (Any  # complex shape): If the output exceeds 1 MB in size, a string that identifies the next page of events. If no additional page exists, this
- **StackEvents** (Any  # complex shape): A list of StackEvents structures.

## Implementation

```speclang
def describe_stack_events(store, request: dict) -> dict:
    """Returns all stack related events for a specified stack in reverse chronological order. For more information about a stack's event history, see Understand CloudFormation stack creation events in the Cl"""
    stack_name = request.get("StackName", "").strip() if isinstance(request.get("StackName"), str) else request.get("StackName")
    if not stack_name:
        raise ValidationException("StackName is required")

    resource = store.stack_eventss(stack_name)
    if not resource:
        raise ResourceNotFoundException(f"Resource stack_name not found")
    return {"StackName": stack_name, **resource}
```
