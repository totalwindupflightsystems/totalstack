---
id: "@specs/aws/ec2/delete_managed_prefix_list"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_DeleteManagedPrefixList"
---

# DeleteManagedPrefixList

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/delete_managed_prefix_list
> **spec:implements:** @kind:operation DeleteManagedPrefixList
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_DeleteManagedPrefixList.spec.md

Deletes the specified managed prefix list. You must first remove all references to the prefix list in your resources.

## Input Shape: DeleteManagedPrefixListRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| DryRun | bool |  | Checks whether you have the required permissions for the action, without actually making the request, and provides an er |
| PrefixListId | Any  # complex shape | ✓ | The ID of the prefix list. |

## Output Shape: DeleteManagedPrefixListResult

- **PrefixList** (list[Any  # complex shape]): Information about the prefix list.

## Implementation

```speclang
def delete_managed_prefix_list(store, request: dict) -> dict:
    """Deletes the specified managed prefix list. You must first remove all references to the prefix list in your resources."""
    prefix_list_id = request.get("PrefixListId", "").strip() if isinstance(request.get("PrefixListId"), str) else request.get("PrefixListId")

    if not store.managed_prefix_lists(prefix_list_id):
        raise ResourceNotFoundException(f"Resource prefix_list_id not found")
    store.delete_managed_prefix_lists(prefix_list_id)
    return {}
```
