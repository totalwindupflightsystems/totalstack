---
id: "@specs/aws/ec2/describe_volumes_modifications"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_DescribeVolumesModifications"
---

# DescribeVolumesModifications

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/describe_volumes_modifications
> **spec:implements:** @kind:operation DescribeVolumesModifications
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_DescribeVolumesModifications.spec.md

Describes the most recent volume modification request for the specified EBS volumes. For more information, see Monitor the progress of volume modifications in the Amazon EBS User Guide .

## Input Shape: DescribeVolumesModificationsRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| DryRun | bool |  | Checks whether you have the required permissions for the action, without actually making the request, and provides an er |
| Filters | list[Any  # complex shape] |  | The filters. modification-state - The current modification state (modifying | optimizing | completed | failed). original |
| MaxResults | int |  | The maximum number of results (up to a limit of 500) to be returned in a paginated request. For more information, see Pa |
| NextToken | str |  | The token returned from a previous paginated request. Pagination continues from the end of the items returned by the pre |
| VolumeIds | list[Any  # complex shape] |  | The IDs of the volumes. |

## Output Shape: DescribeVolumesModificationsResult

- **NextToken** (str): The token to include in another request to get the next page of items. This value is null when there are no more items t
- **VolumesModifications** (list[Any  # complex shape]): Information about the volume modifications.

## Implementation

```speclang
def describe_volumes_modifications(store, request: dict) -> dict:
    """Describes the most recent volume modification request for the specified EBS volumes. For more information, see Monitor the progress of volume modifications in the Amazon EBS User Guide ."""

    # Auto-generated get handler — verify resource key
    return store.get_resource(request)
```
