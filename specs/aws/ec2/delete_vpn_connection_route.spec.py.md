---
id: "@specs/aws/ec2/delete_vpn_connection_route"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_DeleteVpnConnectionRoute"
---

# DeleteVpnConnectionRoute

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/delete_vpn_connection_route
> **spec:implements:** @kind:operation DeleteVpnConnectionRoute
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_DeleteVpnConnectionRoute.spec.md

Deletes the specified static route associated with a VPN connection between an existing virtual private gateway and a VPN customer gateway. The static route allows traffic to be routed from the virtual private gateway to the VPN customer gateway.

## Input Shape: DeleteVpnConnectionRouteRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| DestinationCidrBlock | str | ✓ | The CIDR block associated with the local subnet of the customer network. |
| VpnConnectionId | Any  # complex shape | ✓ | The ID of the VPN connection. |

## Implementation

```speclang
def delete_vpn_connection_route(store, request: dict) -> dict:
    """Deletes the specified static route associated with a VPN connection between an existing virtual private gateway and a VPN customer gateway. The static route allows traffic to be routed from the virtua"""
    destination_cidr_block = request.get("DestinationCidrBlock", "").strip() if isinstance(request.get("DestinationCidrBlock"), str) else request.get("DestinationCidrBlock")
    vpn_connection_id = request.get("VpnConnectionId", "").strip() if isinstance(request.get("VpnConnectionId"), str) else request.get("VpnConnectionId")

    if not store.vpn_connection_routes(destination_cidr_block):
        raise ResourceNotFoundException(f"Resource destination_cidr_block not found")
    store.delete_vpn_connection_routes(destination_cidr_block)
    return {}
```
