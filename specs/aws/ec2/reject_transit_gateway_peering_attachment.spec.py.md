---
id: "@specs/aws/ec2/reject_transit_gateway_peering_attachment"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_RejectTransitGatewayPeeringAttachment"
---

# RejectTransitGatewayPeeringAttachment

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/reject_transit_gateway_peering_attachment
> **spec:implements:** @kind:operation RejectTransitGatewayPeeringAttachment
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_RejectTransitGatewayPeeringAttachment.spec.md

Rejects a transit gateway peering attachment request.

## Input Shape: RejectTransitGatewayPeeringAttachmentRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| DryRun | bool |  | Checks whether you have the required permissions for the action, without actually making the request, and provides an er |
| TransitGatewayAttachmentId | Any  # complex shape | ✓ | The ID of the transit gateway peering attachment. |

## Output Shape: RejectTransitGatewayPeeringAttachmentResult

- **TransitGatewayPeeringAttachment** (Any  # complex shape): The transit gateway peering attachment.

## Implementation

```speclang
def reject_transit_gateway_peering_attachment(store, request: dict) -> dict:
    """Rejects a transit gateway peering attachment request."""
    transit_gateway_attachment_id = request.get("TransitGatewayAttachmentId", "").strip() if isinstance(request.get("TransitGatewayAttachmentId"), str) else request.get("TransitGatewayAttachmentId")
    if not transit_gateway_attachment_id:
        raise ValidationException("TransitGatewayAttachmentId is required")

    # Auto-generated handler — operation not classified as CRUD
    return store.execute("RejectTransitGatewayPeeringAttachment", request)
```
