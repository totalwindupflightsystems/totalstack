---
id: "@specs/aws/ec2/delete_vpn_gateway"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_DeleteVpnGateway"
---

# DeleteVpnGateway

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/delete_vpn_gateway
> **spec:implements:** @kind:operation DeleteVpnGateway
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_DeleteVpnGateway.spec.md

Deletes the specified virtual private gateway. You must first detach the virtual private gateway from the VPC. Note that you don't need to delete the virtual private gateway if you plan to delete and recreate the VPN connection between your VPC and your network.

## Input Shape: DeleteVpnGatewayRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| DryRun | bool |  | Checks whether you have the required permissions for the action, without actually making the request, and provides an er |
| VpnGatewayId | Any  # complex shape | ✓ | The ID of the virtual private gateway. |

## Implementation

```speclang
def delete_vpn_gateway(store, request: dict) -> dict:
    """Deletes the specified virtual private gateway. You must first detach the virtual private gateway from the VPC. Note that you don't need to delete the virtual private gateway if you plan to delete and """
    vpn_gateway_id = request.get("VpnGatewayId", "").strip() if isinstance(request.get("VpnGatewayId"), str) else request.get("VpnGatewayId")

    if not store.vpn_gateways(vpn_gateway_id):
        raise ResourceNotFoundException(f"Resource vpn_gateway_id not found")
    store.delete_vpn_gateways(vpn_gateway_id)
    return {}
```
