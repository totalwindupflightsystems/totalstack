---
id: "@specs/aws/cloudformation/delete_change_set"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/cloudformation/plan"
  - "@specs/aws/cloudformation/docs/API_DeleteChangeSet"
---

# DeleteChangeSet

> **spec:trace:** specs/aws/cloudformation/cloudformation.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/cloudformation/delete_change_set
> **spec:implements:** @kind:operation DeleteChangeSet
> **AWS Protocol:** query
> **HTTP:** POST /
> **@ref:** specs/aws/cloudformation/docs/API_DeleteChangeSet.spec.md

Deletes the specified change set. Deleting change sets ensures that no one executes the wrong change set. If the call successfully completes, CloudFormation successfully deleted the change set. If IncludeNestedStacks specifies True during the creation of the nested change set, then DeleteChangeSet will delete all change sets that belong to the stacks hierarchy and will also delete all change sets for nested stacks with the status of REVIEW_IN_PROGRESS .

## Input Shape: DeleteChangeSetInput

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| ChangeSetName | Any  # complex shape | ✓ | The name or Amazon Resource Name (ARN) of the change set that you want to delete. |
| StackName | Any  # complex shape |  | If you specified the name of a change set to delete, specify the stack name or Amazon Resource Name (ARN) that's associa |

## Output Shape: DeleteChangeSetOutput


## Errors
- **InvalidChangeSetStatusException**: The specified change set can't be used to update the stack. For example, the change set status might be CREATE_IN_PROGRESS , or the stack status might be UPDATE_IN_PROGRESS .

## Implementation

```speclang
def delete_change_set(store, request: dict) -> dict:
    """Deletes the specified change set. Deleting change sets ensures that no one executes the wrong change set. If the call successfully completes, CloudFormation successfully deleted the change set. If Inc"""
    change_set_name = request.get("ChangeSetName", "").strip() if isinstance(request.get("ChangeSetName"), str) else request.get("ChangeSetName")

    if not store.change_sets(change_set_name):
        raise ResourceNotFoundException(f"Resource change_set_name not found")
    store.delete_change_sets(change_set_name)
    return {}
```
