---
id: "@specs/aws/ec2/modify_managed_prefix_list"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_ModifyManagedPrefixList"
---

# ModifyManagedPrefixList

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/modify_managed_prefix_list
> **spec:implements:** @kind:operation ModifyManagedPrefixList
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_ModifyManagedPrefixList.spec.md

Modifies the specified managed prefix list. Adding or removing entries in a prefix list creates a new version of the prefix list. Changing the name of the prefix list does not affect the version. If you specify a current version number that does not match the true current version number, the request fails.

## Input Shape: ModifyManagedPrefixListRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| AddEntries | Any  # complex shape |  | One or more entries to add to the prefix list. |
| CurrentVersion | int |  | The current version of the prefix list. |
| DryRun | bool |  | Checks whether you have the required permissions for the action, without actually making the request, and provides an er |
| IpamPrefixListResolverSyncEnabled | bool |  | Indicates whether synchronization with an IPAM prefix list resolver should be enabled for this managed prefix list. When |
| MaxEntries | int |  | The maximum number of entries for the prefix list. You cannot modify the entries of a prefix list and modify the size of |
| PrefixListId | Any  # complex shape | ✓ | The ID of the prefix list. |
| PrefixListName | str |  | A name for the prefix list. |
| RemoveEntries | Any  # complex shape |  | One or more entries to remove from the prefix list. |

## Output Shape: ModifyManagedPrefixListResult

- **PrefixList** (list[Any  # complex shape]): Information about the prefix list.

## Implementation

```speclang
def modify_managed_prefix_list(store, request: dict) -> dict:
    """Modifies the specified managed prefix list. Adding or removing entries in a prefix list creates a new version of the prefix list. Changing the name of the prefix list does not affect the version. If y"""
    prefix_list_id = request.get("PrefixListId", "").strip() if isinstance(request.get("PrefixListId"), str) else request.get("PrefixListId")
    if not prefix_list_id:
        raise ValidationException("PrefixListId is required")

    items = store.list_managed_prefix_lists()
    return {"PrefixList": list(items.values())}
```
