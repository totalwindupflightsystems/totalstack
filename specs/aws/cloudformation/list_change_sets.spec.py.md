---
id: "@specs/aws/cloudformation/list_change_sets"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/cloudformation/plan"
  - "@specs/aws/cloudformation/docs/API_ListChangeSets"
---

# ListChangeSets

> **spec:trace:** specs/aws/cloudformation/cloudformation.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/cloudformation/list_change_sets
> **spec:implements:** @kind:operation ListChangeSets
> **AWS Protocol:** query
> **HTTP:** POST /
> **@ref:** specs/aws/cloudformation/docs/API_ListChangeSets.spec.md

Returns the ID and status of each active change set for a stack. For example, CloudFormation lists change sets that are in the CREATE_IN_PROGRESS or CREATE_PENDING state.

## Input Shape: ListChangeSetsInput

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| NextToken | Any  # complex shape |  | The token for the next set of items to return. (You received this token from a previous call.) |
| StackName | Any  # complex shape | ✓ | The name or the Amazon Resource Name (ARN) of the stack for which you want to list change sets. |

## Output Shape: ListChangeSetsOutput

- **NextToken** (Any  # complex shape): If the output exceeds 1 MB, a string that identifies the next page of change sets. If there is no additional page, this 
- **Summaries** (Any  # complex shape): A list of ChangeSetSummary structures that provides the ID and status of each change set for the specified stack.

## Implementation

```speclang
def list_change_sets(store, request: dict) -> dict:
    """Returns the ID and status of each active change set for a stack. For example, CloudFormation lists change sets that are in the CREATE_IN_PROGRESS or CREATE_PENDING state."""
    stack_name = request.get("StackName", "").strip() if isinstance(request.get("StackName"), str) else request.get("StackName")
    if not stack_name:
        raise ValidationException("StackName is required")

    items = store.list_change_setss()
    return {"Summaries": list(items.values())}
```
