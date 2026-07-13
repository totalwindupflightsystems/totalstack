---
id: "@specs/aws/ec2/modify_vpn_connection"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_ModifyVpnConnection"
---

# ModifyVpnConnection

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/modify_vpn_connection
> **spec:implements:** @kind:operation ModifyVpnConnection
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_ModifyVpnConnection.spec.md

Modifies the customer gateway or the target gateway of an Amazon Web Services Site-to-Site VPN connection. To modify the target gateway, the following migration options are available: An existing virtual private gateway to a new virtual private gateway An existing virtual private gateway to a transit gateway An existing transit gateway to a new transit gateway An existing transit gateway to a virtual private gateway Before you perform the migration to the new gateway, you must configure the new gateway. Use CreateVpnGateway to create a virtual private gateway, or CreateTransitGateway to create a transit gateway. This step is required when you migrate from a virtual private gateway with static routes to a transit gateway. You must delete the static routes before you migrate to the new gateway. Keep a copy of the static route before you delete it. You will need to add back these routes to the transit gateway after the VPN connection migration is complete. After you migrate to the new gateway, you might need to modify your VPC route table. Use CreateRoute and DeleteRoute to make the changes described in Update VPC route tables in the Amazon Web Services Site-to-Site VPN User Guide . When the new gateway is a transit gateway, modify the transit gateway route table to allow traffic between the VPC and the Amazon Web Services Site-to-Site VPN connection. Use CreateTransitGatewayRoute to add the routes. If you deleted VPN static routes, you must add the static routes to the transit gateway route table. After you perform this operation, the VPN endpoint's IP addresses on the Amazon Web Services side and the tunnel options remain intact. Your Amazon Web Services Site-to-Site VPN connection will be temporarily unavailable for a brief period while we provision the new endpoints.

## Input Shape: ModifyVpnConnectionRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| CustomerGatewayId | Any  # complex shape |  | The ID of the customer gateway at your end of the VPN connection. |
| DryRun | bool |  | Checks whether you have the required permissions for the action, without actually making the request, and provides an er |
| TransitGatewayId | Any  # complex shape |  | The ID of the transit gateway. |
| VpnConnectionId | Any  # complex shape | ✓ | The ID of the VPN connection. |
| VpnGatewayId | Any  # complex shape |  | The ID of the virtual private gateway at the Amazon Web Services side of the VPN connection. |

## Output Shape: ModifyVpnConnectionResult

- **VpnConnection** (Any  # complex shape): Information about the VPN connection.

## Implementation

```speclang
def modify_vpn_connection(store, request: dict) -> dict:
    """Modifies the customer gateway or the target gateway of an Amazon Web Services Site-to-Site VPN connection. To modify the target gateway, the following migration options are available: An existing virt"""
    vpn_connection_id = request.get("VpnConnectionId", "").strip() if isinstance(request.get("VpnConnectionId"), str) else request.get("VpnConnectionId")
    if not vpn_connection_id:
        raise ValidationException("VpnConnectionId is required")

    resource = store.vpn_connections(vpn_connection_id)
    if not resource:
        raise ResourceNotFoundException(f"Resource vpn_connection_id not found")

    # Update mutable fields
    if "TransitGatewayId" in request:
        resource["TransitGatewayId"] = transit_gateway_id
    if "CustomerGatewayId" in request:
        resource["CustomerGatewayId"] = customer_gateway_id
    if "VpnGatewayId" in request:
        resource["VpnGatewayId"] = vpn_gateway_id
    if "DryRun" in request:
        resource["DryRun"] = dry_run

    store.vpn_connections(vpn_connection_id, resource)
    return resource
```
