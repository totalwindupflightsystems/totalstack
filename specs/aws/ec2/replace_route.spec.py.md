---
id: "@specs/aws/ec2/replace_route"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_ReplaceRoute"
---

# ReplaceRoute

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/replace_route
> **spec:implements:** @kind:operation ReplaceRoute
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_ReplaceRoute.spec.md

Replaces an existing route within a route table in a VPC. You must specify either a destination CIDR block or a prefix list ID. You must also specify exactly one of the resources from the parameter list, or reset the local route to its default target. For more information, see Route tables in the Amazon VPC User Guide .

## Input Shape: ReplaceRouteRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| CarrierGatewayId | Any  # complex shape |  | [IPv4 traffic only] The ID of a carrier gateway. |
| CoreNetworkArn | Any  # complex shape |  | The Amazon Resource Name (ARN) of the core network. |
| DestinationCidrBlock | str |  | The IPv4 CIDR address block used for the destination match. The value that you provide must match the CIDR of an existin |
| DestinationIpv6CidrBlock | str |  | The IPv6 CIDR address block used for the destination match. The value that you provide must match the CIDR of an existin |
| DestinationPrefixListId | Any  # complex shape |  | The ID of the prefix list for the route. |
| DryRun | bool |  | Checks whether you have the required permissions for the action, without actually making the request, and provides an er |
| EgressOnlyInternetGatewayId | Any  # complex shape |  | [IPv6 traffic only] The ID of an egress-only internet gateway. |
| GatewayId | Any  # complex shape |  | The ID of an internet gateway or virtual private gateway. |
| InstanceId | Any  # complex shape |  | The ID of a NAT instance in your VPC. |
| LocalGatewayId | Any  # complex shape |  | The ID of the local gateway. |
| LocalTarget | bool |  | Specifies whether to reset the local route to its default target ( local ). |
| NatGatewayId | Any  # complex shape |  | [IPv4 traffic only] The ID of a NAT gateway. |
| NetworkInterfaceId | Any  # complex shape |  | The ID of a network interface. |
| OdbNetworkArn | Any  # complex shape |  | The Amazon Resource Name (ARN) of the ODB network. |
| RouteTableId | Any  # complex shape | ✓ | The ID of the route table. |
| TransitGatewayId | Any  # complex shape |  | The ID of a transit gateway. |
| VpcEndpointId | Any  # complex shape |  | The ID of a VPC endpoint. Supported for Gateway Load Balancer endpoints only. |
| VpcPeeringConnectionId | Any  # complex shape |  | The ID of a VPC peering connection. |

## Implementation

```speclang
def replace_route(store, request: dict) -> dict:
    """Replaces an existing route within a route table in a VPC. You must specify either a destination CIDR block or a prefix list ID. You must also specify exactly one of the resources from the parameter li"""
    route_table_id = request.get("RouteTableId", "").strip() if isinstance(request.get("RouteTableId"), str) else request.get("RouteTableId")
    if not route_table_id:
        raise ValidationException("RouteTableId is required")

    # Auto-generated handler — operation not classified as CRUD
    return store.execute("ReplaceRoute", request)
```
