---
id: "@specs/aws/ec2/attach_vpn_gateway"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_AttachVpnGateway"
---

# AttachVpnGateway

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/attach_vpn_gateway
> **spec:implements:** @kind:operation AttachVpnGateway
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_AttachVpnGateway.spec.md

Attaches an available virtual private gateway to a VPC. You can attach one virtual private gateway to one VPC at a time. For more information, see Amazon Web Services Site-to-Site VPN in the Amazon Web Services Site-to-Site VPN User Guide .

## Input Shape: AttachVpnGatewayRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| DryRun | bool |  | Checks whether you have the required permissions for the action, without actually making the request, and provides an er |
| VpcId | Any  # complex shape | ✓ | The ID of the VPC. |
| VpnGatewayId | Any  # complex shape | ✓ | The ID of the virtual private gateway. |

## Output Shape: AttachVpnGatewayResult

- **VpcAttachment** (Any  # complex shape): Information about the attachment.

## Implementation

```speclang
def attach_vpn_gateway(store, request: dict) -> dict:
    """Attaches an available virtual private gateway to a VPC. You can attach one virtual private gateway to one VPC at a time. For more information, see Amazon Web Services Site-to-Site VPN in the Amazon We"""
    vpc_id = request.get("VpcId", "").strip() if isinstance(request.get("VpcId"), str) else request.get("VpcId")
    if not vpc_id:
        raise ValidationException("VpcId is required")
    vpn_gateway_id = request.get("VpnGatewayId", "").strip() if isinstance(request.get("VpnGatewayId"), str) else request.get("VpnGatewayId")
    if not vpn_gateway_id:
        raise ValidationException("VpnGatewayId is required")

    # Auto-generated handler — operation not classified as CRUD
    return store.execute("AttachVpnGateway", request)
```
