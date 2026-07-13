---
id: "@specs/aws/ec2/describe_volumes"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_DescribeVolumes"
---

# DescribeVolumes

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/describe_volumes
> **spec:implements:** @kind:operation DescribeVolumes
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_DescribeVolumes.spec.md

Describes the specified EBS volumes or all of your EBS volumes. If you are describing a long list of volumes, we recommend that you paginate the output to make the list more manageable. For more information, see Pagination . For more information about EBS volumes, see Amazon EBS volumes in the Amazon EBS User Guide . We strongly recommend using only paginated requests. Unpaginated requests are susceptible to throttling and timeouts. The order of the elements in the response, including those within nested structures, might vary. Applications should not assume the elements appear in a particular order.

## Input Shape: DescribeVolumesRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| DryRun | bool |  | Checks whether you have the required permissions for the action, without actually making the request, and provides an er |
| Filters | list[Any  # complex shape] |  | The filters. attachment.attach-time - The time stamp when the attachment initiated. attachment.delete-on-termination - W |
| MaxResults | int |  | The maximum number of items to return for this request. To get the next page of items, make another request with the tok |
| NextToken | str |  | The token returned from a previous paginated request. Pagination continues from the end of the items returned by the pre |
| VolumeIds | list[Any  # complex shape] |  | The volume IDs. If not specified, then all volumes are included in the response. |

## Output Shape: DescribeVolumesResult

- **NextToken** (str): The token to include in another request to get the next page of items. This value is null when there are no more items t
- **Volumes** (list[Any  # complex shape]): Information about the volumes.

## Implementation

```speclang
def describe_volumes(store, request: dict) -> dict:
    """Describes the specified EBS volumes or all of your EBS volumes. If you are describing a long list of volumes, we recommend that you paginate the output to make the list more manageable. For more infor"""

    # Auto-generated get handler — verify resource key
    return store.get_resource(request)
```
