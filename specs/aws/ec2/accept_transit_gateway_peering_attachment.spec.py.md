---
id: "@specs/aws/ec2/accept_transit_gateway_peering_attachment"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_AcceptTransitGatewayPeeringAttachment"
---

# AcceptTransitGatewayPeeringAttachment

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/accept_transit_gateway_peering_attachment
> **spec:implements:** @kind:operation AcceptTransitGatewayPeeringAttachment
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_AcceptTransitGatewayPeeringAttachment.spec.md

Accepts a transit gateway peering attachment request. The peering attachment must be in the pendingAcceptance state.

## Input Shape: AcceptTransitGatewayPeeringAttachmentRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| DryRun | bool |  | Checks whether you have the required permissions for the action, without actually making the request, and provides an er |
| TransitGatewayAttachmentId | Any  # complex shape | ✓ | The ID of the transit gateway attachment. |

## Output Shape: AcceptTransitGatewayPeeringAttachmentResult

- **TransitGatewayPeeringAttachment** (Any  # complex shape): The transit gateway peering attachment.

## Implementation

```speclang
def accept_transit_gateway_peering_attachment(store, request: dict) -> dict:
    """Accepts a transit gateway peering attachment request. The peering attachment must be in the pendingAcceptance state."""
    transit_gateway_attachment_id = request.get("TransitGatewayAttachmentId", "").strip() if isinstance(request.get("TransitGatewayAttachmentId"), str) else request.get("TransitGatewayAttachmentId")
    if not transit_gateway_attachment_id:
        raise ValidationException("TransitGatewayAttachmentId is required")

    # Auto-generated handler — operation not classified as CRUD
    return store.execute("AcceptTransitGatewayPeeringAttachment", request)
```
