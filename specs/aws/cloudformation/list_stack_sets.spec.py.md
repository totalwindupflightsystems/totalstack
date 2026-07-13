---
id: "@specs/aws/cloudformation/list_stack_sets"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/cloudformation/plan"
  - "@specs/aws/cloudformation/docs/API_ListStackSets"
---

# ListStackSets

> **spec:trace:** specs/aws/cloudformation/cloudformation.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/cloudformation/list_stack_sets
> **spec:implements:** @kind:operation ListStackSets
> **AWS Protocol:** query
> **HTTP:** POST /
> **@ref:** specs/aws/cloudformation/docs/API_ListStackSets.spec.md

Returns summary information about StackSets that are associated with the user. This API provides strongly consistent reads meaning it will always return the most up-to-date data. [Self-managed permissions] If you set the CallAs parameter to SELF while signed in to your Amazon Web Services account, ListStackSets returns all self-managed StackSets in your Amazon Web Services account. [Service-managed permissions] If you set the CallAs parameter to SELF while signed in to the organization's management account, ListStackSets returns all StackSets in the management account. [Service-managed permissions] If you set the CallAs parameter to DELEGATED_ADMIN while signed in to your member account, ListStackSets returns all StackSets with service-managed permissions in the management account.

## Input Shape: ListStackSetsInput

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| CallAs | Any  # complex shape |  | [Service-managed permissions] Specifies whether you are acting as an account administrator in the management account or  |
| MaxResults | Any  # complex shape |  | The maximum number of results to be returned with a single call. If the number of available results exceeds this maximum |
| NextToken | Any  # complex shape |  | The token for the next set of items to return. (You received this token from a previous call.) |
| Status | Any  # complex shape |  | The status of the StackSets that you want to get summary information about. |

## Output Shape: ListStackSetsOutput

- **NextToken** (Any  # complex shape): If the request doesn't return all of the remaining results, NextToken is set to a token. To retrieve the next set of res
- **Summaries** (Any  # complex shape): A list of StackSetSummary structures that contain information about the user's StackSets.

## Implementation

```speclang
def list_stack_sets(store, request: dict) -> dict:
    """Returns summary information about StackSets that are associated with the user. This API provides strongly consistent reads meaning it will always return the most up-to-date data. [Self-managed permiss"""

    items = store.list_stack_setss()
    return {"Summaries": list(items.values())}
```
