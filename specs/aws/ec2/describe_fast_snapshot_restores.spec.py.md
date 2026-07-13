---
id: "@specs/aws/ec2/describe_fast_snapshot_restores"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_DescribeFastSnapshotRestores"
---

# DescribeFastSnapshotRestores

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/describe_fast_snapshot_restores
> **spec:implements:** @kind:operation DescribeFastSnapshotRestores
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_DescribeFastSnapshotRestores.spec.md

Describes the state of fast snapshot restores for your snapshots.

## Input Shape: DescribeFastSnapshotRestoresRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| DryRun | bool |  | Checks whether you have the required permissions for the action, without actually making the request, and provides an er |
| Filters | list[Any  # complex shape] |  | The filters. The possible values are: availability-zone : The Availability Zone of the snapshot. For example, us-east-2a |
| MaxResults | Any  # complex shape |  | The maximum number of items to return for this request. To get the next page of items, make another request with the tok |
| NextToken | Any  # complex shape |  | The token returned from a previous paginated request. Pagination continues from the end of the items returned by the pre |

## Output Shape: DescribeFastSnapshotRestoresResult

- **FastSnapshotRestores** (Any  # complex shape): Information about the state of fast snapshot restores.
- **NextToken** (Any  # complex shape): The token to include in another request to get the next page of items. This value is null when there are no more items t

## Implementation

```speclang
def describe_fast_snapshot_restores(store, request: dict) -> dict:
    """Describes the state of fast snapshot restores for your snapshots."""

    # Auto-generated get handler — verify resource key
    return store.get_resource(request)
```
