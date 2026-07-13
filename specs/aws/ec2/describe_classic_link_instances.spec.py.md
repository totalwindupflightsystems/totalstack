---
id: "@specs/aws/ec2/describe_classic_link_instances"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_DescribeClassicLinkInstances"
---

# DescribeClassicLinkInstances

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/describe_classic_link_instances
> **spec:implements:** @kind:operation DescribeClassicLinkInstances
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_DescribeClassicLinkInstances.spec.md

This action is deprecated. Describes your linked EC2-Classic instances. This request only returns information about EC2-Classic instances linked to a VPC through ClassicLink. You cannot use this request to return information about other instances.

## Input Shape: DescribeClassicLinkInstancesRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| DryRun | bool |  | Checks whether you have the required permissions for the action, without actually making the request, and provides an er |
| Filters | list[Any  # complex shape] |  | The filters. group-id - The ID of a VPC security group that's associated with the instance. instance-id - The ID of the  |
| InstanceIds | list[Any  # complex shape] |  | The instance IDs. Must be instances linked to a VPC through ClassicLink. |
| MaxResults | Any  # complex shape |  | The maximum number of items to return for this request. To get the next page of items, make another request with the tok |
| NextToken | str |  | The token returned from a previous paginated request. Pagination continues from the end of the items returned by the pre |

## Output Shape: DescribeClassicLinkInstancesResult

- **Instances** (list[Any  # complex shape]): Information about one or more linked EC2-Classic instances.
- **NextToken** (str): The token to include in another request to get the next page of items. This value is null when there are no more items t

## Implementation

```speclang
def describe_classic_link_instances(store, request: dict) -> dict:
    """This action is deprecated. Describes your linked EC2-Classic instances. This request only returns information about EC2-Classic instances linked to a VPC through ClassicLink. You cannot use this reque"""

    # Auto-generated get handler — verify resource key
    return store.get_resource(request)
```
