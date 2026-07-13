---
id: "@specs/aws/ec2/describe_subnets"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_DescribeSubnets"
---

# DescribeSubnets

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/describe_subnets
> **spec:implements:** @kind:operation DescribeSubnets
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_DescribeSubnets.spec.md

Describes your subnets. The default is to describe all your subnets. Alternatively, you can specify specific subnet IDs or filter the results to include only the subnets that match specific criteria. For more information, see Subnets in the Amazon VPC User Guide .

## Input Shape: DescribeSubnetsRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| DryRun | bool |  | Checks whether you have the required permissions for the action, without actually making the request, and provides an er |
| Filters | list[Any  # complex shape] |  | The filters. availability-zone - The Availability Zone for the subnet. You can also use availabilityZone as the filter n |
| MaxResults | Any  # complex shape |  | The maximum number of items to return for this request. To get the next page of items, make another request with the tok |
| NextToken | str |  | The token returned from a previous paginated request. Pagination continues from the end of the items returned by the pre |
| SubnetIds | list[Any  # complex shape] |  | The IDs of the subnets. Default: Describes all your subnets. |

## Output Shape: DescribeSubnetsResult

- **NextToken** (str): The token to include in another request to get the next page of items. This value is null when there are no more items t
- **Subnets** (list[Any  # complex shape]): Information about the subnets.

## Implementation

```speclang
def describe_subnets(store, request: dict) -> dict:
    """Describes your subnets. The default is to describe all your subnets. Alternatively, you can specify specific subnet IDs or filter the results to include only the subnets that match specific criteria. """

    # Auto-generated get handler — verify resource key
    return store.get_resource(request)
```
