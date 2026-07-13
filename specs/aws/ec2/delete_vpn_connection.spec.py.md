---
id: "@specs/aws/ec2/delete_vpn_connection"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_DeleteVpnConnection"
---

# DeleteVpnConnection

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/delete_vpn_connection
> **spec:implements:** @kind:operation DeleteVpnConnection
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_DeleteVpnConnection.spec.md

Deletes the specified VPN connection. If you're deleting the VPC and its associated components, we recommend that you detach the virtual private gateway from the VPC and delete the VPC before deleting the VPN connection. If you believe that the tunnel credentials for your VPN connection have been compromised, you can delete the VPN connection and create a new one that has new keys, without needing to delete the VPC or virtual private gateway. If you create a new VPN connection, you must reconfigure the customer gateway device using the new configuration information returned with the new VPN connection ID. For certificate-based authentication, delete all Certificate Manager (ACM) private certificates used for the Amazon Web Services-side tunnel endpoints for the VPN connection before deleting the VPN connection.

## Input Shape: DeleteVpnConnectionRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| DryRun | bool |  | Checks whether you have the required permissions for the action, without actually making the request, and provides an er |
| VpnConnectionId | Any  # complex shape | ✓ | The ID of the VPN connection. |

## Implementation

```speclang
def delete_vpn_connection(store, request: dict) -> dict:
    """Deletes the specified VPN connection. If you're deleting the VPC and its associated components, we recommend that you detach the virtual private gateway from the VPC and delete the VPC before deleting"""
    vpn_connection_id = request.get("VpnConnectionId", "").strip() if isinstance(request.get("VpnConnectionId"), str) else request.get("VpnConnectionId")

    if not store.vpn_connections(vpn_connection_id):
        raise ResourceNotFoundException(f"Resource vpn_connection_id not found")
    store.delete_vpn_connections(vpn_connection_id)
    return {}
```
