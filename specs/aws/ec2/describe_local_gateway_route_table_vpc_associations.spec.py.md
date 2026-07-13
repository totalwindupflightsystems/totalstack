---
id: "@specs/aws/ec2/describe_local_gateway_route_table_vpc_associations"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_DescribeLocalGatewayRouteTableVpcAssociations"
---

# DescribeLocalGatewayRouteTableVpcAssociations

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/describe_local_gateway_route_table_vpc_associations
> **spec:implements:** @kind:operation DescribeLocalGatewayRouteTableVpcAssociations
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_DescribeLocalGatewayRouteTableVpcAssociations.spec.md

Describes the specified associations between VPCs and local gateway route tables.

## Input Shape: DescribeLocalGatewayRouteTableVpcAssociationsRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| DryRun | bool |  | Checks whether you have the required permissions for the action, without actually making the request, and provides an er |
| Filters | list[Any  # complex shape] |  | One or more filters. local-gateway-id - The ID of a local gateway. local-gateway-route-table-arn - The Amazon Resource N |
| LocalGatewayRouteTableVpcAssociationIds | Any  # complex shape |  | The IDs of the associations. |
| MaxResults | Any  # complex shape |  | The maximum number of results to return with a single call. To retrieve the remaining results, make another call with th |
| NextToken | str |  | The token for the next page of results. |

## Output Shape: DescribeLocalGatewayRouteTableVpcAssociationsResult

- **LocalGatewayRouteTableVpcAssociations** (Any  # complex shape): Information about the associations.
- **NextToken** (str): The token to use to retrieve the next page of results. This value is null when there are no more results to return.

## Implementation

```speclang
def describe_local_gateway_route_table_vpc_associations(store, request: dict) -> dict:
    """Describes the specified associations between VPCs and local gateway route tables."""

    # Auto-generated get handler — verify resource key
    return store.get_resource(request)
```
