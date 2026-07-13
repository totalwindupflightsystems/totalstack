---
id: "@specs/aws/cloudformation/list_stack_set_operation_results"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/cloudformation/plan"
  - "@specs/aws/cloudformation/docs/API_ListStackSetOperationResults"
---

# ListStackSetOperationResults

> **spec:trace:** specs/aws/cloudformation/cloudformation.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/cloudformation/list_stack_set_operation_results
> **spec:implements:** @kind:operation ListStackSetOperationResults
> **AWS Protocol:** query
> **HTTP:** POST /
> **@ref:** specs/aws/cloudformation/docs/API_ListStackSetOperationResults.spec.md

Returns summary information about the results of a StackSet operation. This API provides eventually consistent reads meaning it may take some time but will eventually return the most up-to-date data.

## Input Shape: ListStackSetOperationResultsInput

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| CallAs | Any  # complex shape |  | [Service-managed permissions] Specifies whether you are acting as an account administrator in the organization's managem |
| Filters | Any  # complex shape |  | The filter to apply to operation results. |
| MaxResults | Any  # complex shape |  | The maximum number of results to be returned with a single call. If the number of available results exceeds this maximum |
| NextToken | Any  # complex shape |  | The token for the next set of items to return. (You received this token from a previous call.) |
| OperationId | Any  # complex shape | ✓ | The ID of the StackSet operation. |
| StackSetName | Any  # complex shape | ✓ | The name or unique ID of the StackSet that you want to get operation results for. |

## Output Shape: ListStackSetOperationResultsOutput

- **NextToken** (Any  # complex shape): If the request doesn't return all results, NextToken is set to a token. To retrieve the next set of results, call ListOp
- **Summaries** (Any  # complex shape): A list of StackSetOperationResultSummary structures that contain information about the specified operation results, for 

## Errors
- **StackSetNotFoundException**: The specified StackSet doesn't exist.
- **OperationNotFoundException**: The specified ID refers to an operation that doesn't exist.

## Implementation

```speclang
def list_stack_set_operation_results(store, request: dict) -> dict:
    """Returns summary information about the results of a StackSet operation. This API provides eventually consistent reads meaning it may take some time but will eventually return the most up-to-date data."""
    operation_id = request.get("OperationId", "").strip() if isinstance(request.get("OperationId"), str) else request.get("OperationId")
    if not operation_id:
        raise ValidationException("OperationId is required")
    stack_set_name = request.get("StackSetName", "").strip() if isinstance(request.get("StackSetName"), str) else request.get("StackSetName")
    if not stack_set_name:
        raise ValidationException("StackSetName is required")

    items = store.list_stack_set_operation_resultss()
    return {"Summaries": list(items.values())}
```
