---
id: "@specs/aws/ec2/describe_snapshots"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_DescribeSnapshots"
---

# DescribeSnapshots

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/describe_snapshots
> **spec:implements:** @kind:operation DescribeSnapshots
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_DescribeSnapshots.spec.md

Describes the specified EBS snapshots available to you or all of the EBS snapshots available to you. The snapshots available to you include public snapshots, private snapshots that you own, and private snapshots owned by other Amazon Web Services accounts for which you have explicit create volume permissions. The create volume permissions fall into the following categories: public : The owner of the snapshot granted create volume permissions for the snapshot to the all group. All Amazon Web Services accounts have create volume permissions for these snapshots. explicit : The owner of the snapshot granted create volume permissions to a specific Amazon Web Services account. implicit : An Amazon Web Services account has implicit create volume permissions for all snapshots it owns. The list of snapshots returned can be filtered by specifying snapshot IDs, snapshot owners, or Amazon Web Services accounts with create volume permissions. If no options are specified, Amazon EC2 returns all snapshots for which you have create volume permissions. If you specify one or more snapshot IDs, only snapshots that have the specified IDs are returned. If you specify an invalid snapshot ID, an error is returned. If you specify a snapshot ID for which you do not have access, it is not included in the returned results. If you specify one or more snapshot owners using the OwnerIds option, only snapshots from the specified owners and for which you have access are returned. The results can include the Amazon Web Services account IDs of the specified owners, amazon for snapshots owned by Amazon, or self for snapshots that you own. If you specify a list of restorable users, only snapshots with create snapshot permissions for those users are returned. You can specify Amazon Web Services account IDs (if you own the snapshots), self for snapshots for which you own or have explicit permissions, or all for public snapshots. If you are describing a long list of snapshots, we recommend that you paginate the output to make the list more manageable. For more information, see Pagination . For more information about EBS snapshots, see Amazon EBS snapshots in the Amazon EBS User Guide . We strongly recommend using only paginated requests. Unpaginated requests are susceptible to throttling and timeouts.

## Input Shape: DescribeSnapshotsRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| DryRun | bool |  | Checks whether you have the required permissions for the action, without actually making the request, and provides an er |
| Filters | list[Any  # complex shape] |  | The filters. description - A description of the snapshot. encrypted - Indicates whether the snapshot is encrypted ( true |
| MaxResults | int |  | The maximum number of items to return for this request. To get the next page of items, make another request with the tok |
| NextToken | str |  | The token returned from a previous paginated request. Pagination continues from the end of the items returned by the pre |
| OwnerIds | list[str] |  | Scopes the results to snapshots with the specified owners. You can specify a combination of Amazon Web Services account  |
| RestorableByUserIds | list[str] |  | The IDs of the Amazon Web Services accounts that can create volumes from the snapshot. |
| SnapshotIds | list[Any  # complex shape] |  | The snapshot IDs. Default: Describes the snapshots for which you have create volume permissions. |

## Output Shape: DescribeSnapshotsResult

- **NextToken** (str): The token to include in another request to get the next page of items. This value is null when there are no more items t
- **Snapshots** (list[Any  # complex shape]): Information about the snapshots.

## Implementation

```speclang
def describe_snapshots(store, request: dict) -> dict:
    """Describes the specified EBS snapshots available to you or all of the EBS snapshots available to you. The snapshots available to you include public snapshots, private snapshots that you own, and privat"""

    # Auto-generated get handler — verify resource key
    return store.get_resource(request)
```
