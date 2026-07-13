---
id: "@specs/aws/ec2/replace_vpn_tunnel"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_ReplaceVpnTunnel"
---

# ReplaceVpnTunnel

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/replace_vpn_tunnel
> **spec:implements:** @kind:operation ReplaceVpnTunnel
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_ReplaceVpnTunnel.spec.md

Trigger replacement of specified VPN tunnel.

## Input Shape: ReplaceVpnTunnelRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| ApplyPendingMaintenance | bool |  | Trigger pending tunnel endpoint maintenance. |
| DryRun | bool |  | Checks whether you have the required permissions for the action, without actually making the request, and provides an er |
| VpnConnectionId | Any  # complex shape | ✓ | The ID of the Site-to-Site VPN connection. |
| VpnTunnelOutsideIpAddress | str | ✓ | The external IP address of the VPN tunnel. |

## Output Shape: ReplaceVpnTunnelResult

- **Return** (bool): Confirmation of replace tunnel operation.

## Implementation

```speclang
def replace_vpn_tunnel(store, request: dict) -> dict:
    """Trigger replacement of specified VPN tunnel."""
    vpn_connection_id = request.get("VpnConnectionId", "").strip() if isinstance(request.get("VpnConnectionId"), str) else request.get("VpnConnectionId")
    if not vpn_connection_id:
        raise ValidationException("VpnConnectionId is required")
    vpn_tunnel_outside_ip_address = request.get("VpnTunnelOutsideIpAddress", "").strip() if isinstance(request.get("VpnTunnelOutsideIpAddress"), str) else request.get("VpnTunnelOutsideIpAddress")
    if not vpn_tunnel_outside_ip_address:
        raise ValidationException("VpnTunnelOutsideIpAddress is required")

    # Auto-generated handler — operation not classified as CRUD
    return store.execute("ReplaceVpnTunnel", request)
```
