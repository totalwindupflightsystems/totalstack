---
id: "@specs/aws/ec2/get_active_vpn_tunnel_status"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_GetActiveVpnTunnelStatus"
---

# GetActiveVpnTunnelStatus

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/get_active_vpn_tunnel_status
> **spec:implements:** @kind:operation GetActiveVpnTunnelStatus
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_GetActiveVpnTunnelStatus.spec.md

Returns the currently negotiated security parameters for an active VPN tunnel, including IKE version, DH groups, encryption algorithms, and integrity algorithms.

## Input Shape: GetActiveVpnTunnelStatusRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| DryRun | bool |  | Checks whether you have the required permissions for the action, without actually making the request. |
| VpnConnectionId | Any  # complex shape | ✓ | The ID of the VPN connection for which to retrieve the active tunnel status. |
| VpnTunnelOutsideIpAddress | str | ✓ | The external IP address of the VPN tunnel for which to retrieve the active status. |

## Output Shape: GetActiveVpnTunnelStatusResult

- **ActiveVpnTunnelStatus** (Any  # complex shape): Information about the current security configuration of the VPN tunnel.

## Implementation

```speclang
def get_active_vpn_tunnel_status(store, request: dict) -> dict:
    """Returns the currently negotiated security parameters for an active VPN tunnel, including IKE version, DH groups, encryption algorithms, and integrity algorithms."""
    vpn_connection_id = request.get("VpnConnectionId", "").strip() if isinstance(request.get("VpnConnectionId"), str) else request.get("VpnConnectionId")
    if not vpn_connection_id:
        raise ValidationException("VpnConnectionId is required")
    vpn_tunnel_outside_ip_address = request.get("VpnTunnelOutsideIpAddress", "").strip() if isinstance(request.get("VpnTunnelOutsideIpAddress"), str) else request.get("VpnTunnelOutsideIpAddress")
    if not vpn_tunnel_outside_ip_address:
        raise ValidationException("VpnTunnelOutsideIpAddress is required")

    resource = store.active_vpn_tunnel_statuss(vpn_tunnel_outside_ip_address)
    if not resource:
        raise ResourceNotFoundException(f"Resource vpn_tunnel_outside_ip_address not found")
    return {"VpnTunnelOutsideIpAddress": vpn_tunnel_outside_ip_address, **resource}
```
