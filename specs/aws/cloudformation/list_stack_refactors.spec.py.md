---
id: "@specs/aws/cloudformation/list_stack_refactors"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/cloudformation/plan"
  - "@specs/aws/cloudformation/docs/API_ListStackRefactors"
---

# ListStackRefactors

> **spec:trace:** specs/aws/cloudformation/cloudformation.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/cloudformation/list_stack_refactors
> **spec:implements:** @kind:operation ListStackRefactors
> **AWS Protocol:** query
> **HTTP:** POST /
> **@ref:** specs/aws/cloudformation/docs/API_ListStackRefactors.spec.md

Lists all account stack refactor operations and their statuses.

## Input Shape: ListStackRefactorsInput

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| ExecutionStatusFilter | Any  # complex shape |  | Execution status to use as a filter. Specify one or more execution status codes to list only stack refactors with the sp |
| MaxResults | Any  # complex shape |  | The maximum number of results to be returned with a single call. If the number of available results exceeds this maximum |
| NextToken | Any  # complex shape |  | The token for the next set of items to return. (You received this token from a previous call.) |

## Output Shape: ListStackRefactorsOutput

- **NextToken** (Any  # complex shape): If the request doesn't return all the remaining results, NextToken is set to a token. To retrieve the next set of result
- **StackRefactorSummaries** (Any  # complex shape): Provides a summary of a stack refactor, including the following: StackRefactorId Status StatusReason ExecutionStatus Exe

## Implementation

```speclang
def list_stack_refactors(store, request: dict) -> dict:
    """Lists all account stack refactor operations and their statuses."""

    items = store.list_stack_refactorss()
    return {"StackRefactorSummaries": list(items.values())}
```
