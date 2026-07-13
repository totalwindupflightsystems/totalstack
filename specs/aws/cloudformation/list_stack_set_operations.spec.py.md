---
id: "@specs/aws/cloudformation/list_stack_set_operations"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/cloudformation/plan"
  - "@specs/aws/cloudformation/docs/API_ListStackSetOperations"
---

# ListStackSetOperations

> **spec:trace:** specs/aws/cloudformation/cloudformation.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/cloudformation/list_stack_set_operations
> **spec:implements:** @kind:operation ListStackSetOperations
> **AWS Protocol:** query
> **HTTP:** POST /
> **@ref:** specs/aws/cloudformation/docs/API_ListStackSetOperations.spec.md

Returns summary information about operations performed on a StackSet. This API provides eventually consistent reads meaning it may take some time but will eventually return the most up-to-date data.

## Input Shape: ListStackSetOperationsInput

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| CallAs | Any  # complex shape |  | [Service-managed permissions] Specifies whether you are acting as an account administrator in the organization's managem |
| MaxResults | Any  # complex shape |  | The maximum number of results to be returned with a single call. If the number of available results exceeds this maximum |
| NextToken | Any  # complex shape |  | The token for the next set of items to return. (You received this token from a previous call.) |
| StackSetName | Any  # complex shape | ✓ | The name or unique ID of the StackSet that you want to get operation summaries for. |

## Output Shape: ListStackSetOperationsOutput

- **NextToken** (Any  # complex shape): If the request doesn't return all results, NextToken is set to a token. To retrieve the next set of results, call ListOp
- **Summaries** (Any  # complex shape): A list of StackSetOperationSummary structures that contain summary information about operations for the specified StackS

## Errors
- **StackSetNotFoundException**: The specified StackSet doesn't exist.

## Implementation

```speclang
def list_stack_set_operations(store, request: dict) -> dict:
    """Returns summary information about operations performed on a StackSet. This API provides eventually consistent reads meaning it may take some time but will eventually return the most up-to-date data."""
    stack_set_name = request.get("StackSetName", "").strip() if isinstance(request.get("StackSetName"), str) else request.get("StackSetName")
    if not stack_set_name:
        raise ValidationException("StackSetName is required")

    items = store.list_stack_set_operationss()
    return {"Summaries": list(items.values())}
```
