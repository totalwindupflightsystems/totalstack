---
id: "@specs/aws/ec2/create_managed_prefix_list"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_CreateManagedPrefixList"
---

# CreateManagedPrefixList

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/create_managed_prefix_list
> **spec:implements:** @kind:operation CreateManagedPrefixList
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_CreateManagedPrefixList.spec.md

Creates a managed prefix list. You can specify entries for the prefix list. Each entry consists of a CIDR block and an optional description.

## Input Shape: CreateManagedPrefixListRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| AddressFamily | str | ✓ | The IP address type. Valid Values: IPv4 | IPv6 |
| ClientToken | str |  | Unique, case-sensitive identifier you provide to ensure the idempotency of the request. For more information, see Ensuri |
| DryRun | bool |  | Checks whether you have the required permissions for the action, without actually making the request, and provides an er |
| Entries | Any  # complex shape |  | One or more entries for the prefix list. |
| MaxEntries | int | ✓ | The maximum number of entries for the prefix list. |
| PrefixListName | str | ✓ | A name for the prefix list. Constraints: Up to 255 characters in length. The name cannot start with com.amazonaws . |
| TagSpecifications | list[Any  # complex shape] |  | The tags to apply to the prefix list during creation. |

## Output Shape: CreateManagedPrefixListResult

- **PrefixList** (list[Any  # complex shape]): Information about the prefix list.

## Implementation

```speclang
def create_managed_prefix_list(store, request: dict) -> dict:
    """Creates a managed prefix list. You can specify entries for the prefix list. Each entry consists of a CIDR block and an optional description."""
    address_family = request.get("AddressFamily", "").strip() if isinstance(request.get("AddressFamily"), str) else request.get("AddressFamily")
    if not address_family:
        raise ValidationException("AddressFamily is required")
    max_entries = request.get("MaxEntries", "").strip() if isinstance(request.get("MaxEntries"), str) else request.get("MaxEntries")
    if not max_entries:
        raise ValidationException("MaxEntries is required")
    prefix_list_name = request.get("PrefixListName", "").strip() if isinstance(request.get("PrefixListName"), str) else request.get("PrefixListName")
    if not prefix_list_name:
        raise ValidationException("PrefixListName is required")

    if store.managed_prefix_lists(prefix_list_name):
        raise ResourceInUseException(f"Resource prefix_list_name already exists")

    record = {
        "DryRun": dry_run,
        "PrefixListName": prefix_list_name,
        "Entries": entries,
        "MaxEntries": max_entries,
        "TagSpecifications": tag_specifications,
        "AddressFamily": address_family,
        "ClientToken": client_token,
    }

    store.managed_prefix_lists(prefix_list_name, record)

    return {
        "PrefixList": record.get("PrefixList", {}),
    }
```
