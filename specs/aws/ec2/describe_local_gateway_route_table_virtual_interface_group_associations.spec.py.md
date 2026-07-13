---
id: "@specs/aws/ec2/describe_local_gateway_route_table_virtual_interface_group_associations"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_DescribeLocalGatewayRouteTableVirtualInterfaceGroupAssociations"
---

# DescribeLocalGatewayRouteTableVirtualInterfaceGroupAssociations

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/describe_local_gateway_route_table_virtual_interface_group_associations
> **spec:implements:** @kind:operation DescribeLocalGatewayRouteTableVirtualInterfaceGroupAssociations
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_DescribeLocalGatewayRouteTableVirtualInterfaceGroupAssociations.spec.md

Describes the associations between virtual interface groups and local gateway route tables.

## Input Shape: DescribeLocalGatewayRouteTableVirtualInterfaceGroupAssociationsRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| DryRun | bool |  | Checks whether you have the required permissions for the action, without actually making the request, and provides an er |
| Filters | list[Any  # complex shape] |  | One or more filters. local-gateway-id - The ID of a local gateway. local-gateway-route-table-arn - The Amazon Resource N |
| LocalGatewayRouteTableVirtualInterfaceGroupAssociationIds | Any  # complex shape |  | The IDs of the associations. |
| MaxResults | Any  # complex shape |  | The maximum number of results to return with a single call. To retrieve the remaining results, make another call with th |
| NextToken | str |  | The token for the next page of results. |

## Output Shape: DescribeLocalGatewayRouteTableVirtualInterfaceGroupAssociationsResult

- **LocalGatewayRouteTableVirtualInterfaceGroupAssociations** (Any  # complex shape): Information about the associations.
- **NextToken** (str): The token to use to retrieve the next page of results. This value is null when there are no more results to return.

## Implementation

```speclang
def describe_local_gateway_route_table_virtual_interface_group_associations(store, request: dict) -> dict:
    """Describes the associations between virtual interface groups and local gateway route tables."""

    # Auto-generated get handler — verify resource key
    return store.get_resource(request)
```
