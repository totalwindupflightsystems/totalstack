---
id: "@specs/aws/ec2/describe_locked_snapshots"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_DescribeLockedSnapshots"
---

# DescribeLockedSnapshots

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/describe_locked_snapshots
> **spec:implements:** @kind:operation DescribeLockedSnapshots
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_DescribeLockedSnapshots.spec.md

Describes the lock status for a snapshot.

## Input Shape: DescribeLockedSnapshotsRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| DryRun | bool |  | Checks whether you have the required permissions for the action, without actually making the request, and provides an er |
| Filters | list[Any  # complex shape] |  | The filters. lock-state - The state of the snapshot lock ( compliance-cooloff | governance | compliance | expired ). |
| MaxResults | Any  # complex shape |  | The maximum number of items to return for this request. To get the next page of items, make another request with the tok |
| NextToken | str |  | The token returned from a previous paginated request. Pagination continues from the end of the items returned by the pre |
| SnapshotIds | list[Any  # complex shape] |  | The IDs of the snapshots for which to view the lock status. |

## Output Shape: DescribeLockedSnapshotsResult

- **NextToken** (str): The token to include in another request to get the next page of items. This value is null when there are no more items t
- **Snapshots** (list[Any  # complex shape]): Information about the snapshots.

## Implementation

```speclang
def describe_locked_snapshots(store, request: dict) -> dict:
    """Describes the lock status for a snapshot."""

    # Auto-generated get handler — verify resource key
    return store.get_resource(request)
```
