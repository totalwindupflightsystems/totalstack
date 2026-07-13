---
id: "@specs/aws/ec2/list_snapshots_in_recycle_bin"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_ListSnapshotsInRecycleBin"
---

# ListSnapshotsInRecycleBin

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/list_snapshots_in_recycle_bin
> **spec:implements:** @kind:operation ListSnapshotsInRecycleBin
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_ListSnapshotsInRecycleBin.spec.md

Lists one or more snapshots that are currently in the Recycle Bin.

## Input Shape: ListSnapshotsInRecycleBinRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| DryRun | bool |  | Checks whether you have the required permissions for the action, without actually making the request, and provides an er |
| MaxResults | Any  # complex shape |  | The maximum number of items to return for this request. To get the next page of items, make another request with the tok |
| NextToken | str |  | The token returned from a previous paginated request. Pagination continues from the end of the items returned by the pre |
| SnapshotIds | list[Any  # complex shape] |  | The IDs of the snapshots to list. Omit this parameter to list all of the snapshots that are in the Recycle Bin. |

## Output Shape: ListSnapshotsInRecycleBinResult

- **NextToken** (str): The token to include in another request to get the next page of items. This value is null when there are no more items t
- **Snapshots** (list[Any  # complex shape]): Information about the snapshots.

## Implementation

```speclang
def list_snapshots_in_recycle_bin(store, request: dict) -> dict:
    """Lists one or more snapshots that are currently in the Recycle Bin."""

    items = store.list_snapshots_in_recycle_bins()
    return {"Snapshots": list(items.values())}
```
