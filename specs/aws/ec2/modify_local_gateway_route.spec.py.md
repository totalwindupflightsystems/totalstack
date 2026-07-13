---
id: "@specs/aws/ec2/modify_local_gateway_route"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_ModifyLocalGatewayRoute"
---

# ModifyLocalGatewayRoute

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/modify_local_gateway_route
> **spec:implements:** @kind:operation ModifyLocalGatewayRoute
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_ModifyLocalGatewayRoute.spec.md

Modifies the specified local gateway route.

## Input Shape: ModifyLocalGatewayRouteRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| DestinationCidrBlock | str |  | The CIDR block used for destination matches. The value that you provide must match the CIDR of an existing route in the  |
| DestinationPrefixListId | Any  # complex shape |  | The ID of the prefix list. Use a prefix list in place of DestinationCidrBlock . You cannot use DestinationPrefixListId a |
| DryRun | bool |  | Checks whether you have the required permissions for the action, without actually making the request, and provides an er |
| LocalGatewayRouteTableId | Any  # complex shape | ✓ | The ID of the local gateway route table. |
| LocalGatewayVirtualInterfaceGroupId | Any  # complex shape |  | The ID of the virtual interface group. |
| NetworkInterfaceId | Any  # complex shape |  | The ID of the network interface. |

## Output Shape: ModifyLocalGatewayRouteResult

- **Route** (Any  # complex shape): Information about the local gateway route table.

## Implementation

```speclang
def modify_local_gateway_route(store, request: dict) -> dict:
    """Modifies the specified local gateway route."""
    local_gateway_route_table_id = request.get("LocalGatewayRouteTableId", "").strip() if isinstance(request.get("LocalGatewayRouteTableId"), str) else request.get("LocalGatewayRouteTableId")
    if not local_gateway_route_table_id:
        raise ValidationException("LocalGatewayRouteTableId is required")

    resource = store.local_gateway_routes(local_gateway_route_table_id)
    if not resource:
        raise ResourceNotFoundException(f"Resource local_gateway_route_table_id not found")

    # Update mutable fields
    if "DestinationCidrBlock" in request:
        resource["DestinationCidrBlock"] = destination_cidr_block
    if "LocalGatewayVirtualInterfaceGroupId" in request:
        resource["LocalGatewayVirtualInterfaceGroupId"] = local_gateway_virtual_interface_group_id
    if "NetworkInterfaceId" in request:
        resource["NetworkInterfaceId"] = network_interface_id
    if "DryRun" in request:
        resource["DryRun"] = dry_run
    if "DestinationPrefixListId" in request:
        resource["DestinationPrefixListId"] = destination_prefix_list_id

    store.local_gateway_routes(local_gateway_route_table_id, resource)
    return resource
```
