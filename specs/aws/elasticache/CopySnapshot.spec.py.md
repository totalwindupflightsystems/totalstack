---
id: "@specs/aws/elasticache/CopySnapshot"
version: 1.0.0
target_lang: py
status: active
owned-by: codegen
model_pool: code-gen
depends_on:
  - "@specs/aws/elasticache/meta"
  - "@specs/aws/elasticache/plan"
---

# CopySnapshot

Makes a copy of an existing snapshot.  This operation is valid for Valkey or Redis OSS only.   Users or groups that have permissions to use the CopySnapshot operation can create their own Amazon S3 buckets and copy snapshots to it. To control access to your snapshots, use an IAM policy to control who has the ability to use the CopySnapshot operation. For more information about using IAM to control the use of ElastiCache operations, see Exporting Snapshots and Authentication &amp; Access Control.

## Input Shape: CopySnapshotMessage
| Parameter | Type | Required |
|-----------|------|----------|
| SourceSnapshotName | String | ✓ |
| TargetSnapshotName | String | ✓ |
| TargetBucket | String |  |
| KmsKeyId | String |  |
| Tags | TagList |  |

## Output Shape: CopySnapshotResult
- Snapshot: Snapshot

## Errors
SnapshotAlreadyExistsFault, SnapshotNotFoundFault, SnapshotQuotaExceededFault, InvalidSnapshotStateFault, TagQuotaPerResourceExceeded, InvalidParameterValueException

## Implementation

```speclang
def copy_snapshot(store, request):
    """Handle CopySnapshot — copy a snapshot."""
    source = request.get("SourceSnapshotName")
    target = request.get("TargetSnapshotName")
    if not source or not target:
        raise InvalidParameterValueException("SourceSnapshotName and TargetSnapshotName are required")
    if source not in store.snapshots:
        raise SnapshotNotFoundFault(f"Snapshot {source} not found")
    if target in store.snapshots:
        raise SnapshotAlreadyExistsFault(f"Snapshot {target} already exists")
    # Copy snapshot record
    store.snapshots[target] = dict(store.snapshots[source])
    store.snapshots[target]["SnapshotName"] = target
    return {"Snapshot": store.snapshots[target]}
```
