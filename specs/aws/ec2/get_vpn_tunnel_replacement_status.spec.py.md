---
id: "@specs/aws/ec2/get_vpn_tunnel_replacement_status"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_GetVpnTunnelReplacementStatus"
---

# GetVpnTunnelReplacementStatus

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/get_vpn_tunnel_replacement_status
> **spec:implements:** @kind:operation GetVpnTunnelReplacementStatus
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_GetVpnTunnelReplacementStatus.spec.md

Get details of available tunnel endpoint maintenance.

## Input Shape: GetVpnTunnelReplacementStatusRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| DryRun | bool |  | Checks whether you have the required permissions for the action, without actually making the request, and provides an er |
| VpnConnectionId | Any  # complex shape | ✓ | The ID of the Site-to-Site VPN connection. |
| VpnTunnelOutsideIpAddress | str | ✓ | The external IP address of the VPN tunnel. |

## Output Shape: GetVpnTunnelReplacementStatusResult

- **CustomerGatewayId** (Any  # complex shape): The ID of the customer gateway.
- **MaintenanceDetails** (Any  # complex shape): Get details of pending tunnel endpoint maintenance.
- **TransitGatewayId** (Any  # complex shape): The ID of the transit gateway associated with the VPN connection.
- **VpnConnectionId** (Any  # complex shape): The ID of the Site-to-Site VPN connection.
- **VpnGatewayId** (Any  # complex shape): The ID of the virtual private gateway.
- **VpnTunnelOutsideIpAddress** (str): The external IP address of the VPN tunnel.

## Implementation

```speclang
def get_vpn_tunnel_replacement_status(store, request: dict) -> dict:
    """Get details of available tunnel endpoint maintenance."""
    vpn_connection_id = request.get("VpnConnectionId", "").strip() if isinstance(request.get("VpnConnectionId"), str) else request.get("VpnConnectionId")
    if not vpn_connection_id:
        raise ValidationException("VpnConnectionId is required")
    vpn_tunnel_outside_ip_address = request.get("VpnTunnelOutsideIpAddress", "").strip() if isinstance(request.get("VpnTunnelOutsideIpAddress"), str) else request.get("VpnTunnelOutsideIpAddress")
    if not vpn_tunnel_outside_ip_address:
        raise ValidationException("VpnTunnelOutsideIpAddress is required")

    resource = store.vpn_tunnel_replacement_statuss(vpn_tunnel_outside_ip_address)
    if not resource:
        raise ResourceNotFoundException(f"Resource vpn_tunnel_outside_ip_address not found")
    return {"VpnTunnelOutsideIpAddress": vpn_tunnel_outside_ip_address, **resource}
```
