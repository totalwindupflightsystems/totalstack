---
id: "@specs/aws/cloudformation/list_stack_instances"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/cloudformation/plan"
  - "@specs/aws/cloudformation/docs/API_ListStackInstances"
---

# ListStackInstances

> **spec:trace:** specs/aws/cloudformation/cloudformation.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/cloudformation/list_stack_instances
> **spec:implements:** @kind:operation ListStackInstances
> **AWS Protocol:** query
> **HTTP:** POST /
> **@ref:** specs/aws/cloudformation/docs/API_ListStackInstances.spec.md

Returns summary information about stack instances that are associated with the specified StackSet. You can filter for stack instances that are associated with a specific Amazon Web Services account name or Region, or that have a specific status.

## Input Shape: ListStackInstancesInput

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| CallAs | Any  # complex shape |  | [Service-managed permissions] Specifies whether you are acting as an account administrator in the organization's managem |
| Filters | Any  # complex shape |  | The filter to apply to stack instances |
| MaxResults | Any  # complex shape |  | The maximum number of results to be returned with a single call. If the number of available results exceeds this maximum |
| NextToken | Any  # complex shape |  | The token for the next set of items to return. (You received this token from a previous call.) |
| StackInstanceAccount | Any  # complex shape |  | The name of the Amazon Web Services account that you want to list stack instances for. |
| StackInstanceRegion | Any  # complex shape |  | The name of the Region where you want to list stack instances. |
| StackSetName | Any  # complex shape | ✓ | The name or unique ID of the StackSet that you want to list stack instances for. |

## Output Shape: ListStackInstancesOutput

- **NextToken** (Any  # complex shape): If the request doesn't return all the remaining results, NextToken is set to a token. To retrieve the next set of result
- **Summaries** (Any  # complex shape): A list of StackInstanceSummary structures that contain information about the specified stack instances.

## Errors
- **StackSetNotFoundException**: The specified StackSet doesn't exist.

## Implementation

```speclang
def list_stack_instances(store, request: dict) -> dict:
    """Returns summary information about stack instances that are associated with the specified StackSet. You can filter for stack instances that are associated with a specific Amazon Web Services account na"""
    stack_set_name = request.get("StackSetName", "").strip() if isinstance(request.get("StackSetName"), str) else request.get("StackSetName")
    if not stack_set_name:
        raise ValidationException("StackSetName is required")

    items = store.list_stack_instancess()
    return {"Summaries": list(items.values())}
```
