---
id: "@specs/aws/ec2/create_client_vpn_route"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_CreateClientVpnRoute"
---

# CreateClientVpnRoute

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/create_client_vpn_route
> **spec:implements:** @kind:operation CreateClientVpnRoute
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_CreateClientVpnRoute.spec.md

Adds a route to a network to a Client VPN endpoint. Each Client VPN endpoint has a route table that describes the available destination network routes. Each route in the route table specifies the path for traﬃc to speciﬁc resources or networks.

## Input Shape: CreateClientVpnRouteRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| ClientToken | str |  | Unique, case-sensitive identifier that you provide to ensure the idempotency of the request. For more information, see E |
| ClientVpnEndpointId | Any  # complex shape | ✓ | The ID of the Client VPN endpoint to which to add the route. |
| Description | str |  | A brief description of the route. |
| DestinationCidrBlock | str | ✓ | The IPv4 address range, in CIDR notation, of the route destination. For example: To add a route for Internet access, ent |
| DryRun | bool |  | Checks whether you have the required permissions for the action, without actually making the request, and provides an er |
| TargetVpcSubnetId | Any  # complex shape | ✓ | The ID of the subnet through which you want to route traffic. The specified subnet must be an existing target network of |

## Output Shape: CreateClientVpnRouteResult

- **Status** (Any  # complex shape): The current state of the route.

## Implementation

```speclang
def create_client_vpn_route(store, request: dict) -> dict:
    """Adds a route to a network to a Client VPN endpoint. Each Client VPN endpoint has a route table that describes the available destination network routes. Each route in the route table specifies the path"""
    client_vpn_endpoint_id = request.get("ClientVpnEndpointId", "").strip() if isinstance(request.get("ClientVpnEndpointId"), str) else request.get("ClientVpnEndpointId")
    if not client_vpn_endpoint_id:
        raise ValidationException("ClientVpnEndpointId is required")
    destination_cidr_block = request.get("DestinationCidrBlock", "").strip() if isinstance(request.get("DestinationCidrBlock"), str) else request.get("DestinationCidrBlock")
    if not destination_cidr_block:
        raise ValidationException("DestinationCidrBlock is required")
    target_vpc_subnet_id = request.get("TargetVpcSubnetId", "").strip() if isinstance(request.get("TargetVpcSubnetId"), str) else request.get("TargetVpcSubnetId")
    if not target_vpc_subnet_id:
        raise ValidationException("TargetVpcSubnetId is required")

    if store.client_vpn_routes(destination_cidr_block):
        raise ResourceInUseException(f"Resource destination_cidr_block already exists")

    record = {
        "ClientVpnEndpointId": client_vpn_endpoint_id,
        "DestinationCidrBlock": destination_cidr_block,
        "TargetVpcSubnetId": target_vpc_subnet_id,
        "Description": description,
        "ClientToken": client_token,
        "DryRun": dry_run,
    }

    store.client_vpn_routes(destination_cidr_block, record)

    return {
        "Status": record.get("Status", {}),
    }
```
