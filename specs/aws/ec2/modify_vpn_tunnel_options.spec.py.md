---
id: "@specs/aws/ec2/modify_vpn_tunnel_options"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_ModifyVpnTunnelOptions"
---

# ModifyVpnTunnelOptions

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/modify_vpn_tunnel_options
> **spec:implements:** @kind:operation ModifyVpnTunnelOptions
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_ModifyVpnTunnelOptions.spec.md

Modifies the options for a VPN tunnel in an Amazon Web Services Site-to-Site VPN connection. You can modify multiple options for a tunnel in a single request, but you can only modify one tunnel at a time. For more information, see Site-to-Site VPN tunnel options for your Site-to-Site VPN connection in the Amazon Web Services Site-to-Site VPN User Guide .

## Input Shape: ModifyVpnTunnelOptionsRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| DryRun | bool |  | Checks whether you have the required permissions for the action, without actually making the request, and provides an er |
| PreSharedKeyStorage | str |  | Specifies the storage mode for the pre-shared key (PSK). Valid values are Standard (stored in Site-to-Site VPN service)  |
| SkipTunnelReplacement | bool |  | Choose whether or not to trigger immediate tunnel replacement. This is only applicable when turning on or off EnableTunn |
| TunnelOptions | Any  # complex shape | ✓ | The tunnel options to modify. |
| VpnConnectionId | Any  # complex shape | ✓ | The ID of the Amazon Web Services Site-to-Site VPN connection. |
| VpnTunnelOutsideIpAddress | str | ✓ | The external IP address of the VPN tunnel. |

## Output Shape: ModifyVpnTunnelOptionsResult

- **VpnConnection** (Any  # complex shape): Information about the VPN connection.

## Implementation

```speclang
def modify_vpn_tunnel_options(store, request: dict) -> dict:
    """Modifies the options for a VPN tunnel in an Amazon Web Services Site-to-Site VPN connection. You can modify multiple options for a tunnel in a single request, but you can only modify one tunnel at a t"""
    tunnel_options = request.get("TunnelOptions", "").strip() if isinstance(request.get("TunnelOptions"), str) else request.get("TunnelOptions")
    if not tunnel_options:
        raise ValidationException("TunnelOptions is required")
    vpn_connection_id = request.get("VpnConnectionId", "").strip() if isinstance(request.get("VpnConnectionId"), str) else request.get("VpnConnectionId")
    if not vpn_connection_id:
        raise ValidationException("VpnConnectionId is required")
    vpn_tunnel_outside_ip_address = request.get("VpnTunnelOutsideIpAddress", "").strip() if isinstance(request.get("VpnTunnelOutsideIpAddress"), str) else request.get("VpnTunnelOutsideIpAddress")
    if not vpn_tunnel_outside_ip_address:
        raise ValidationException("VpnTunnelOutsideIpAddress is required")

    resource = store.vpn_tunnel_optionss(vpn_tunnel_outside_ip_address)
    if not resource:
        raise ResourceNotFoundException(f"Resource vpn_tunnel_outside_ip_address not found")

    # Update mutable fields
    if "DryRun" in request:
        resource["DryRun"] = dry_run
    if "SkipTunnelReplacement" in request:
        resource["SkipTunnelReplacement"] = skip_tunnel_replacement
    if "PreSharedKeyStorage" in request:
        resource["PreSharedKeyStorage"] = pre_shared_key_storage

    store.vpn_tunnel_optionss(vpn_tunnel_outside_ip_address, resource)
    return resource
```
