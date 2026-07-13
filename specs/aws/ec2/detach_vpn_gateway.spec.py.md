---
id: "@specs/aws/ec2/detach_vpn_gateway"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_DetachVpnGateway"
---

# DetachVpnGateway

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/detach_vpn_gateway
> **spec:implements:** @kind:operation DetachVpnGateway
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_DetachVpnGateway.spec.md

Detaches a virtual private gateway from a VPC. You do this if you're planning to turn off the VPC and not use it anymore. You can confirm a virtual private gateway has been completely detached from a VPC by describing the virtual private gateway (any attachments to the virtual private gateway are also described). You must wait for the attachment's state to switch to detached before you can delete the VPC or attach a different VPC to the virtual private gateway.

## Input Shape: DetachVpnGatewayRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| DryRun | bool |  | Checks whether you have the required permissions for the action, without actually making the request, and provides an er |
| VpcId | Any  # complex shape | ✓ | The ID of the VPC. |
| VpnGatewayId | Any  # complex shape | ✓ | The ID of the virtual private gateway. |

## Implementation

```speclang
def detach_vpn_gateway(store, request: dict) -> dict:
    """Detaches a virtual private gateway from a VPC. You do this if you're planning to turn off the VPC and not use it anymore. You can confirm a virtual private gateway has been completely detached from a """
    vpc_id = request.get("VpcId", "").strip() if isinstance(request.get("VpcId"), str) else request.get("VpcId")
    if not vpc_id:
        raise ValidationException("VpcId is required")
    vpn_gateway_id = request.get("VpnGatewayId", "").strip() if isinstance(request.get("VpnGatewayId"), str) else request.get("VpnGatewayId")
    if not vpn_gateway_id:
        raise ValidationException("VpnGatewayId is required")

    # Auto-generated handler — operation not classified as CRUD
    return store.execute("DetachVpnGateway", request)
```
