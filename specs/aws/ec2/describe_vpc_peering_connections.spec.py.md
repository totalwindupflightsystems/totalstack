---
id: "@specs/aws/ec2/describe_vpc_peering_connections"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_DescribeVpcPeeringConnections"
---

# DescribeVpcPeeringConnections

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/describe_vpc_peering_connections
> **spec:implements:** @kind:operation DescribeVpcPeeringConnections
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_DescribeVpcPeeringConnections.spec.md

Describes your VPC peering connections. The default is to describe all your VPC peering connections. Alternatively, you can specify specific VPC peering connection IDs or filter the results to include only the VPC peering connections that match specific criteria.

## Input Shape: DescribeVpcPeeringConnectionsRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| DryRun | bool |  | Checks whether you have the required permissions for the action, without actually making the request, and provides an er |
| Filters | list[Any  # complex shape] |  | The filters. accepter-vpc-info.cidr-block - The IPv4 CIDR block of the accepter VPC. accepter-vpc-info.owner-id - The ID |
| MaxResults | Any  # complex shape |  | The maximum number of items to return for this request. To get the next page of items, make another request with the tok |
| NextToken | str |  | The token returned from a previous paginated request. Pagination continues from the end of the items returned by the pre |
| VpcPeeringConnectionIds | list[Any  # complex shape] |  | The IDs of the VPC peering connections. Default: Describes all your VPC peering connections. |

## Output Shape: DescribeVpcPeeringConnectionsResult

- **NextToken** (str): The token to include in another request to get the next page of items. This value is null when there are no more items t
- **VpcPeeringConnections** (list[Any  # complex shape]): Information about the VPC peering connections.

## Implementation

```speclang
def describe_vpc_peering_connections(store, request: dict) -> dict:
    """Describes your VPC peering connections. The default is to describe all your VPC peering connections. Alternatively, you can specify specific VPC peering connection IDs or filter the results to include"""

    # Auto-generated get handler — verify resource key
    return store.get_resource(request)
```
