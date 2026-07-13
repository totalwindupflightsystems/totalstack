---
id: "@specs/aws/ec2/create_local_gateway_route"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_CreateLocalGatewayRoute"
---

# CreateLocalGatewayRoute

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/create_local_gateway_route
> **spec:implements:** @kind:operation CreateLocalGatewayRoute
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_CreateLocalGatewayRoute.spec.md

Creates a static route for the specified local gateway route table. You must specify one of the following targets: LocalGatewayVirtualInterfaceGroupId NetworkInterfaceId

## Input Shape: CreateLocalGatewayRouteRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| DestinationCidrBlock | str |  | The CIDR range used for destination matches. Routing decisions are based on the most specific match. |
| DestinationPrefixListId | Any  # complex shape |  | The ID of the prefix list. Use a prefix list in place of DestinationCidrBlock . You cannot use DestinationPrefixListId a |
| DryRun | bool |  | Checks whether you have the required permissions for the action, without actually making the request, and provides an er |
| LocalGatewayRouteTableId | Any  # complex shape | ✓ | The ID of the local gateway route table. |
| LocalGatewayVirtualInterfaceGroupId | Any  # complex shape |  | The ID of the virtual interface group. |
| NetworkInterfaceId | Any  # complex shape |  | The ID of the network interface. |

## Output Shape: CreateLocalGatewayRouteResult

- **Route** (Any  # complex shape): Information about the route.

## Implementation

```speclang
def create_local_gateway_route(store, request: dict) -> dict:
    """Creates a static route for the specified local gateway route table. You must specify one of the following targets: LocalGatewayVirtualInterfaceGroupId NetworkInterfaceId"""
    local_gateway_route_table_id = request.get("LocalGatewayRouteTableId", "").strip() if isinstance(request.get("LocalGatewayRouteTableId"), str) else request.get("LocalGatewayRouteTableId")
    if not local_gateway_route_table_id:
        raise ValidationException("LocalGatewayRouteTableId is required")

    if store.local_gateway_routes(local_gateway_route_table_id):
        raise ResourceInUseException(f"Resource local_gateway_route_table_id already exists")

    record = {
        "DestinationCidrBlock": destination_cidr_block,
        "LocalGatewayRouteTableId": local_gateway_route_table_id,
        "LocalGatewayVirtualInterfaceGroupId": local_gateway_virtual_interface_group_id,
        "DryRun": dry_run,
        "NetworkInterfaceId": network_interface_id,
        "DestinationPrefixListId": destination_prefix_list_id,
    }

    store.local_gateway_routes(local_gateway_route_table_id, record)

    return {
        "Route": record.get("Route", {}),
    }
```
