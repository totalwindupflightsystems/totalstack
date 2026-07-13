---
id: "@specs/aws/ec2/delete_transit_gateway_peering_attachment"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_DeleteTransitGatewayPeeringAttachment"
---

# DeleteTransitGatewayPeeringAttachment

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/delete_transit_gateway_peering_attachment
> **spec:implements:** @kind:operation DeleteTransitGatewayPeeringAttachment
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_DeleteTransitGatewayPeeringAttachment.spec.md

Deletes a transit gateway peering attachment.

## Input Shape: DeleteTransitGatewayPeeringAttachmentRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| DryRun | bool |  | Checks whether you have the required permissions for the action, without actually making the request, and provides an er |
| TransitGatewayAttachmentId | Any  # complex shape | ✓ | The ID of the transit gateway peering attachment. |

## Output Shape: DeleteTransitGatewayPeeringAttachmentResult

- **TransitGatewayPeeringAttachment** (Any  # complex shape): The transit gateway peering attachment.

## Implementation

```speclang
def delete_transit_gateway_peering_attachment(store, request: dict) -> dict:
    """Deletes a transit gateway peering attachment."""
    transit_gateway_attachment_id = request.get("TransitGatewayAttachmentId", "").strip() if isinstance(request.get("TransitGatewayAttachmentId"), str) else request.get("TransitGatewayAttachmentId")

    if not store.transit_gateway_peering_attachments(transit_gateway_attachment_id):
        raise ResourceNotFoundException(f"Resource transit_gateway_attachment_id not found")
    store.delete_transit_gateway_peering_attachments(transit_gateway_attachment_id)
    return {}
```
