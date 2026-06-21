---
id: "@specs/aws/elasticache/DeleteSnapshot"
version: 1.0.0
target_lang: py
status: active
owned-by: codegen
model_pool: code-gen
depends_on:
  - "@specs/aws/elasticache/meta"
  - "@specs/aws/elasticache/plan"
---

# DeleteSnapshot

Deletes an existing snapshot. When you receive a successful response from this operation, ElastiCache immediately begins deleting the snapshot; you cannot cancel or revert this operation.  This operation is valid for Valkey or Redis OSS only.

## Input Shape: DeleteSnapshotMessage
| Parameter | Type | Required |
|-----------|------|----------|
| SnapshotName | String | ✓ |

## Output Shape: DeleteSnapshotResult
- Snapshot: Snapshot

## Errors
SnapshotNotFoundFault, InvalidSnapshotStateFault, InvalidParameterValueException, InvalidParameterCombinationException

## Implementation

```speclang
def delete_snapshot(store, request):
    """Handle DeleteSnapshot — delete a resource."""
    resource_name = request.get("SnapshotName")
    if not resource_name:
        raise InvalidParameterValueException("SnapshotName is required")
    if resource_name not in store.snapshots:
        raise SnapshotNotFoundFault(f"Resource {resource_name} not found")
    del store.snapshots[resource_name]
    return {}
```
