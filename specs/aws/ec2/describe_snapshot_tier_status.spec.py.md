---
id: "@specs/aws/ec2/describe_snapshot_tier_status"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_DescribeSnapshotTierStatus"
---

# DescribeSnapshotTierStatus

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/describe_snapshot_tier_status
> **spec:implements:** @kind:operation DescribeSnapshotTierStatus
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_DescribeSnapshotTierStatus.spec.md

Describes the storage tier status of one or more Amazon EBS snapshots.

## Input Shape: DescribeSnapshotTierStatusRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| DryRun | bool |  | Checks whether you have the required permissions for the action, without actually making the request, and provides an er |
| Filters | list[Any  # complex shape] |  | The filters. snapshot-id - The snapshot ID. volume-id - The ID of the volume the snapshot is for. last-tiering-operation |
| MaxResults | Any  # complex shape |  | The maximum number of items to return for this request. To get the next page of items, make another request with the tok |
| NextToken | str |  | The token returned from a previous paginated request. Pagination continues from the end of the items returned by the pre |

## Output Shape: DescribeSnapshotTierStatusResult

- **NextToken** (str): The token to include in another request to get the next page of items. This value is null when there are no more items t
- **SnapshotTierStatuses** (Any  # complex shape): Information about the snapshot's storage tier.

## Implementation

```speclang
def describe_snapshot_tier_status(store, request: dict) -> dict:
    """Describes the storage tier status of one or more Amazon EBS snapshots."""

    # Auto-generated get handler — verify resource key
    return store.get_resource(request)
```
