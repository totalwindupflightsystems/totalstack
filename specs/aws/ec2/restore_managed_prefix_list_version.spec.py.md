---
id: "@specs/aws/ec2/restore_managed_prefix_list_version"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_RestoreManagedPrefixListVersion"
---

# RestoreManagedPrefixListVersion

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/restore_managed_prefix_list_version
> **spec:implements:** @kind:operation RestoreManagedPrefixListVersion
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_RestoreManagedPrefixListVersion.spec.md

Restores the entries from a previous version of a managed prefix list to a new version of the prefix list.

## Input Shape: RestoreManagedPrefixListVersionRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| CurrentVersion | int | ✓ | The current version number for the prefix list. |
| DryRun | bool |  | Checks whether you have the required permissions for the action, without actually making the request, and provides an er |
| PrefixListId | Any  # complex shape | ✓ | The ID of the prefix list. |
| PreviousVersion | int | ✓ | The version to restore. |

## Output Shape: RestoreManagedPrefixListVersionResult

- **PrefixList** (list[Any  # complex shape]): Information about the prefix list.

## Implementation

```speclang
def restore_managed_prefix_list_version(store, request: dict) -> dict:
    """Restores the entries from a previous version of a managed prefix list to a new version of the prefix list."""
    current_version = request.get("CurrentVersion", "").strip() if isinstance(request.get("CurrentVersion"), str) else request.get("CurrentVersion")
    if not current_version:
        raise ValidationException("CurrentVersion is required")
    prefix_list_id = request.get("PrefixListId", "").strip() if isinstance(request.get("PrefixListId"), str) else request.get("PrefixListId")
    if not prefix_list_id:
        raise ValidationException("PrefixListId is required")
    previous_version = request.get("PreviousVersion", "").strip() if isinstance(request.get("PreviousVersion"), str) else request.get("PreviousVersion")
    if not previous_version:
        raise ValidationException("PreviousVersion is required")

    items = store.list_restore_managed_prefix_list_versions()
    return {"PrefixList": list(items.values())}
```
