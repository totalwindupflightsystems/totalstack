---
id: "@specs/aws/cloudformation/list_stacks"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/cloudformation/plan"
  - "@specs/aws/cloudformation/docs/API_ListStacks"
---

# ListStacks

> **spec:trace:** specs/aws/cloudformation/cloudformation.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/cloudformation/list_stacks
> **spec:implements:** @kind:operation ListStacks
> **AWS Protocol:** query
> **HTTP:** POST /
> **@ref:** specs/aws/cloudformation/docs/API_ListStacks.spec.md

Returns the summary information for stacks whose status matches the specified StackStatusFilter . Summary information for stacks that have been deleted is kept for 90 days after the stack is deleted. If no StackStatusFilter is specified, summary information for all stacks is returned (including existing stacks and stacks that have been deleted).

## Input Shape: ListStacksInput

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| NextToken | Any  # complex shape |  | The token for the next set of items to return. (You received this token from a previous call.) |
| StackStatusFilter | Any  # complex shape |  | Stack status to use as a filter. Specify one or more stack status codes to list only stacks with the specified status co |

## Output Shape: ListStacksOutput

- **NextToken** (Any  # complex shape): If the output exceeds 1 MB in size, a string that identifies the next page of stacks. If no additional page exists, this
- **StackSummaries** (Any  # complex shape): A list of StackSummary structures that contains information about the specified stacks.

## Implementation

```speclang
def list_stacks(store, request: dict) -> dict:
    """Returns the summary information for stacks whose status matches the specified StackStatusFilter . Summary information for stacks that have been deleted is kept for 90 days after the stack is deleted. """

    items = store.list_stackss()
    return {"StackSummaries": list(items.values())}
```
