---
id: "@specs/aws/ec2/describe_vpcs"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_DescribeVpcs"
---

# DescribeVpcs

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/describe_vpcs
> **spec:implements:** @kind:operation DescribeVpcs
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_DescribeVpcs.spec.md

Describes your VPCs. The default is to describe all your VPCs. Alternatively, you can specify specific VPC IDs or filter the results to include only the VPCs that match specific criteria.

## Input Shape: DescribeVpcsRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| DryRun | bool |  | Checks whether you have the required permissions for the action, without actually making the request, and provides an er |
| Filters | list[Any  # complex shape] |  | The filters. cidr - The primary IPv4 CIDR block of the VPC. The CIDR block you specify must exactly match the VPC's CIDR |
| MaxResults | Any  # complex shape |  | The maximum number of items to return for this request. To get the next page of items, make another request with the tok |
| NextToken | str |  | The token returned from a previous paginated request. Pagination continues from the end of the items returned by the pre |
| VpcIds | list[Any  # complex shape] |  | The IDs of the VPCs. |

## Output Shape: DescribeVpcsResult

- **NextToken** (str): The token to include in another request to get the next page of items. This value is null when there are no more items t
- **Vpcs** (list[Any  # complex shape]): Information about the VPCs.

## Implementation

```speclang
def describe_vpcs(store, request: dict) -> dict:
    """Describes your VPCs. The default is to describe all your VPCs. Alternatively, you can specify specific VPC IDs or filter the results to include only the VPCs that match specific criteria."""

    # Auto-generated get handler — verify resource key
    return store.get_resource(request)
```
