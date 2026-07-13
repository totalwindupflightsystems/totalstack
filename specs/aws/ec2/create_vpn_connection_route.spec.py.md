---
id: "@specs/aws/ec2/create_vpn_connection_route"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_CreateVpnConnectionRoute"
---

# CreateVpnConnectionRoute

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/create_vpn_connection_route
> **spec:implements:** @kind:operation CreateVpnConnectionRoute
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_CreateVpnConnectionRoute.spec.md

Creates a static route associated with a VPN connection between an existing virtual private gateway and a VPN customer gateway. The static route allows traffic to be routed from the virtual private gateway to the VPN customer gateway. For more information, see Amazon Web Services Site-to-Site VPN in the Amazon Web Services Site-to-Site VPN User Guide .

## Input Shape: CreateVpnConnectionRouteRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| DestinationCidrBlock | str | ✓ | The CIDR block associated with the local subnet of the customer network. |
| VpnConnectionId | Any  # complex shape | ✓ | The ID of the VPN connection. |

## Implementation

```speclang
def create_vpn_connection_route(store, request: dict) -> dict:
    """Creates a static route associated with a VPN connection between an existing virtual private gateway and a VPN customer gateway. The static route allows traffic to be routed from the virtual private ga"""
    destination_cidr_block = request.get("DestinationCidrBlock", "").strip() if isinstance(request.get("DestinationCidrBlock"), str) else request.get("DestinationCidrBlock")
    if not destination_cidr_block:
        raise ValidationException("DestinationCidrBlock is required")
    vpn_connection_id = request.get("VpnConnectionId", "").strip() if isinstance(request.get("VpnConnectionId"), str) else request.get("VpnConnectionId")
    if not vpn_connection_id:
        raise ValidationException("VpnConnectionId is required")

    if store.vpn_connection_routes(destination_cidr_block):
        raise ResourceInUseException(f"Resource destination_cidr_block already exists")

    record = {
        "DestinationCidrBlock": destination_cidr_block,
        "VpnConnectionId": vpn_connection_id,
    }

    store.vpn_connection_routes(destination_cidr_block, record)

    return {
    }
```
