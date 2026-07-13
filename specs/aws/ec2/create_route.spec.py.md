---
id: "@specs/aws/ec2/create_route"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_CreateRoute"
---

# CreateRoute

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/create_route
> **spec:implements:** @kind:operation CreateRoute
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_CreateRoute.spec.md

Creates a route in a route table within a VPC. You must specify either a destination CIDR block or a prefix list ID. You must also specify exactly one of the resources from the parameter list. When determining how to route traffic, we use the route with the most specific match. For example, traffic is destined for the IPv4 address 192.0.2.3 , and the route table includes the following two IPv4 routes: 192.0.2.0/24 (goes to some target A) 192.0.2.0/28 (goes to some target B) Both routes apply to the traffic destined for 192.0.2.3 . However, the second route in the list covers a smaller number of IP addresses and is therefore more specific, so we use that route to determine where to target the traffic. For more information about route tables, see Route tables in the Amazon VPC User Guide .

## Input Shape: CreateRouteRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| CarrierGatewayId | Any  # complex shape |  | The ID of the carrier gateway. You can only use this option when the VPC contains a subnet which is associated with a Wa |
| CoreNetworkArn | Any  # complex shape |  | The Amazon Resource Name (ARN) of the core network. |
| DestinationCidrBlock | str |  | The IPv4 CIDR address block used for the destination match. Routing decisions are based on the most specific match. We m |
| DestinationIpv6CidrBlock | str |  | The IPv6 CIDR block used for the destination match. Routing decisions are based on the most specific match. |
| DestinationPrefixListId | Any  # complex shape |  | The ID of a prefix list used for the destination match. |
| DryRun | bool |  | Checks whether you have the required permissions for the action, without actually making the request, and provides an er |
| EgressOnlyInternetGatewayId | Any  # complex shape |  | [IPv6 traffic only] The ID of an egress-only internet gateway. |
| GatewayId | Any  # complex shape |  | The ID of an internet gateway or virtual private gateway attached to your VPC. |
| InstanceId | Any  # complex shape |  | The ID of a NAT instance in your VPC. The operation fails if you specify an instance ID unless exactly one network inter |
| LocalGatewayId | Any  # complex shape |  | The ID of the local gateway. |
| NatGatewayId | Any  # complex shape |  | [IPv4 traffic only] The ID of a NAT gateway. |
| NetworkInterfaceId | Any  # complex shape |  | The ID of a network interface. |
| OdbNetworkArn | Any  # complex shape |  | The Amazon Resource Name (ARN) of the ODB network. |
| RouteTableId | Any  # complex shape | ✓ | The ID of the route table for the route. |
| TransitGatewayId | Any  # complex shape |  | The ID of a transit gateway. |
| VpcEndpointId | Any  # complex shape |  | The ID of a VPC endpoint. Supported for Gateway Load Balancer endpoints only. |
| VpcPeeringConnectionId | Any  # complex shape |  | The ID of a VPC peering connection. |

## Output Shape: CreateRouteResult

- **Return** (bool): Returns true if the request succeeds; otherwise, it returns an error.

## Implementation

```speclang
def create_route(store, request: dict) -> dict:
    """Creates a route in a route table within a VPC. You must specify either a destination CIDR block or a prefix list ID. You must also specify exactly one of the resources from the parameter list. When de"""
    route_table_id = request.get("RouteTableId", "").strip() if isinstance(request.get("RouteTableId"), str) else request.get("RouteTableId")
    if not route_table_id:
        raise ValidationException("RouteTableId is required")

    if store.routes(route_table_id):
        raise ResourceInUseException(f"Resource route_table_id already exists")

    record = {
        "DestinationPrefixListId": destination_prefix_list_id,
        "VpcEndpointId": vpc_endpoint_id,
        "TransitGatewayId": transit_gateway_id,
        "LocalGatewayId": local_gateway_id,
        "CarrierGatewayId": carrier_gateway_id,
        "CoreNetworkArn": core_network_arn,
        "OdbNetworkArn": odb_network_arn,
        "DryRun": dry_run,
        "RouteTableId": route_table_id,
        "DestinationCidrBlock": destination_cidr_block,
        "GatewayId": gateway_id,
        "DestinationIpv6CidrBlock": destination_ipv6_cidr_block,
        "EgressOnlyInternetGatewayId": egress_only_internet_gateway_id,
        "InstanceId": instance_id,
        "NetworkInterfaceId": network_interface_id,
        "VpcPeeringConnectionId": vpc_peering_connection_id,
        "NatGatewayId": nat_gateway_id,
    }

    store.routes(route_table_id, record)

    return {
        "Return": record.get("Return", {}),
    }
```
