---
id: "@specs/aws/cloudformation/delete_stack_set"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/cloudformation/plan"
  - "@specs/aws/cloudformation/docs/API_DeleteStackSet"
---

# DeleteStackSet

> **spec:trace:** specs/aws/cloudformation/cloudformation.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/cloudformation/delete_stack_set
> **spec:implements:** @kind:operation DeleteStackSet
> **AWS Protocol:** query
> **HTTP:** POST /
> **@ref:** specs/aws/cloudformation/docs/API_DeleteStackSet.spec.md

Deletes a StackSet. Before you can delete a StackSet, all its member stack instances must be deleted. For more information about how to complete this, see DeleteStackInstances .

## Input Shape: DeleteStackSetInput

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| CallAs | Any  # complex shape |  | [Service-managed permissions] Specifies whether you are acting as an account administrator in the organization's managem |
| StackSetName | Any  # complex shape | ✓ | The name or unique ID of the StackSet that you're deleting. You can obtain this value by running ListStackSets . |

## Output Shape: DeleteStackSetOutput


## Errors
- **StackSetNotEmptyException**: You can't yet delete this StackSet, because it still contains one or more stack instances. Delete all stack instances from the StackSet before deleting the StackSet.
- **OperationInProgressException**: Another operation is currently in progress for this StackSet. Only one operation can be performed for a stack set at a given time.

## Implementation

```speclang
def delete_stack_set(store, request: dict) -> dict:
    """Deletes a StackSet. Before you can delete a StackSet, all its member stack instances must be deleted. For more information about how to complete this, see DeleteStackInstances ."""
    stack_set_name = request.get("StackSetName", "").strip() if isinstance(request.get("StackSetName"), str) else request.get("StackSetName")

    if not store.stack_sets(stack_set_name):
        raise ResourceNotFoundException(f"Resource stack_set_name not found")
    store.delete_stack_sets(stack_set_name)
    return {}
```
