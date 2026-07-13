---
id: "@specs/aws/cloudformation/list_stack_refactor_actions"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/cloudformation/plan"
  - "@specs/aws/cloudformation/docs/API_ListStackRefactorActions"
---

# ListStackRefactorActions

> **spec:trace:** specs/aws/cloudformation/cloudformation.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/cloudformation/list_stack_refactor_actions
> **spec:implements:** @kind:operation ListStackRefactorActions
> **AWS Protocol:** query
> **HTTP:** POST /
> **@ref:** specs/aws/cloudformation/docs/API_ListStackRefactorActions.spec.md

Lists the stack refactor actions that will be taken after calling the ExecuteStackRefactor action.

## Input Shape: ListStackRefactorActionsInput

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| MaxResults | Any  # complex shape |  | The maximum number of results to be returned with a single call. If the number of available results exceeds this maximum |
| NextToken | Any  # complex shape |  | The token for the next set of items to return. (You received this token from a previous call.) |
| StackRefactorId | Any  # complex shape | ✓ | The ID associated with the stack refactor created from the CreateStackRefactor action. |

## Output Shape: ListStackRefactorActionsOutput

- **NextToken** (Any  # complex shape): If the request doesn't return all the remaining results, NextToken is set to a token. To retrieve the next set of result
- **StackRefactorActions** (Any  # complex shape): The stack refactor actions.

## Implementation

```speclang
def list_stack_refactor_actions(store, request: dict) -> dict:
    """Lists the stack refactor actions that will be taken after calling the ExecuteStackRefactor action."""
    stack_refactor_id = request.get("StackRefactorId", "").strip() if isinstance(request.get("StackRefactorId"), str) else request.get("StackRefactorId")
    if not stack_refactor_id:
        raise ValidationException("StackRefactorId is required")

    items = store.list_stack_refactor_actionss()
    return {"StackRefactorActions": list(items.values())}
```
