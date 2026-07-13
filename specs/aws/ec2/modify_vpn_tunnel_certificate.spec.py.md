---
id: "@specs/aws/ec2/modify_vpn_tunnel_certificate"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_ModifyVpnTunnelCertificate"
---

# ModifyVpnTunnelCertificate

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/modify_vpn_tunnel_certificate
> **spec:implements:** @kind:operation ModifyVpnTunnelCertificate
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_ModifyVpnTunnelCertificate.spec.md

Modifies the VPN tunnel endpoint certificate.

## Input Shape: ModifyVpnTunnelCertificateRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| DryRun | bool |  | Checks whether you have the required permissions for the action, without actually making the request, and provides an er |
| VpnConnectionId | Any  # complex shape | ✓ | The ID of the Amazon Web Services Site-to-Site VPN connection. |
| VpnTunnelOutsideIpAddress | str | ✓ | The external IP address of the VPN tunnel. |

## Output Shape: ModifyVpnTunnelCertificateResult

- **VpnConnection** (Any  # complex shape): Information about the VPN connection.

## Implementation

```speclang
def modify_vpn_tunnel_certificate(store, request: dict) -> dict:
    """Modifies the VPN tunnel endpoint certificate."""
    vpn_connection_id = request.get("VpnConnectionId", "").strip() if isinstance(request.get("VpnConnectionId"), str) else request.get("VpnConnectionId")
    if not vpn_connection_id:
        raise ValidationException("VpnConnectionId is required")
    vpn_tunnel_outside_ip_address = request.get("VpnTunnelOutsideIpAddress", "").strip() if isinstance(request.get("VpnTunnelOutsideIpAddress"), str) else request.get("VpnTunnelOutsideIpAddress")
    if not vpn_tunnel_outside_ip_address:
        raise ValidationException("VpnTunnelOutsideIpAddress is required")

    resource = store.vpn_tunnel_certificates(vpn_tunnel_outside_ip_address)
    if not resource:
        raise ResourceNotFoundException(f"Resource vpn_tunnel_outside_ip_address not found")

    # Update mutable fields
    if "DryRun" in request:
        resource["DryRun"] = dry_run

    store.vpn_tunnel_certificates(vpn_tunnel_outside_ip_address, resource)
    return resource
```
