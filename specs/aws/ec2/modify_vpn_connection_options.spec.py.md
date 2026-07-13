---
id: "@specs/aws/ec2/modify_vpn_connection_options"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_ModifyVpnConnectionOptions"
---

# ModifyVpnConnectionOptions

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/modify_vpn_connection_options
> **spec:implements:** @kind:operation ModifyVpnConnectionOptions
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_ModifyVpnConnectionOptions.spec.md

Modifies the connection options for your Site-to-Site VPN connection. When you modify the VPN connection options, the VPN endpoint IP addresses on the Amazon Web Services side do not change, and the tunnel options do not change. Your VPN connection will be temporarily unavailable for a brief period while the VPN connection is updated.

## Input Shape: ModifyVpnConnectionOptionsRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| DryRun | bool |  | Checks whether you have the required permissions for the action, without actually making the request, and provides an er |
| LocalIpv4NetworkCidr | str |  | The IPv4 CIDR on the customer gateway (on-premises) side of the VPN connection. Default: 0.0.0.0/0 |
| LocalIpv6NetworkCidr | str |  | The IPv6 CIDR on the customer gateway (on-premises) side of the VPN connection. Default: ::/0 |
| RemoteIpv4NetworkCidr | str |  | The IPv4 CIDR on the Amazon Web Services side of the VPN connection. Default: 0.0.0.0/0 |
| RemoteIpv6NetworkCidr | str |  | The IPv6 CIDR on the Amazon Web Services side of the VPN connection. Default: ::/0 |
| VpnConnectionId | Any  # complex shape | ✓ | The ID of the Site-to-Site VPN connection. |

## Output Shape: ModifyVpnConnectionOptionsResult

- **VpnConnection** (Any  # complex shape): Information about the VPN connection.

## Implementation

```speclang
def modify_vpn_connection_options(store, request: dict) -> dict:
    """Modifies the connection options for your Site-to-Site VPN connection. When you modify the VPN connection options, the VPN endpoint IP addresses on the Amazon Web Services side do not change, and the t"""
    vpn_connection_id = request.get("VpnConnectionId", "").strip() if isinstance(request.get("VpnConnectionId"), str) else request.get("VpnConnectionId")
    if not vpn_connection_id:
        raise ValidationException("VpnConnectionId is required")

    resource = store.vpn_connection_optionss(vpn_connection_id)
    if not resource:
        raise ResourceNotFoundException(f"Resource vpn_connection_id not found")

    # Update mutable fields
    if "LocalIpv4NetworkCidr" in request:
        resource["LocalIpv4NetworkCidr"] = local_ipv4_network_cidr
    if "RemoteIpv4NetworkCidr" in request:
        resource["RemoteIpv4NetworkCidr"] = remote_ipv4_network_cidr
    if "LocalIpv6NetworkCidr" in request:
        resource["LocalIpv6NetworkCidr"] = local_ipv6_network_cidr
    if "RemoteIpv6NetworkCidr" in request:
        resource["RemoteIpv6NetworkCidr"] = remote_ipv6_network_cidr
    if "DryRun" in request:
        resource["DryRun"] = dry_run

    store.vpn_connection_optionss(vpn_connection_id, resource)
    return resource
```
