---
id: "@specs/aws/ec2/delete_transit_gateway_vpc_attachment"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_DeleteTransitGatewayVpcAttachment"
---

# DeleteTransitGatewayVpcAttachment

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/delete_transit_gateway_vpc_attachment
> **spec:implements:** @kind:operation DeleteTransitGatewayVpcAttachment
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_DeleteTransitGatewayVpcAttachment.spec.md

Deletes the specified VPC attachment.

## Input Shape: DeleteTransitGatewayVpcAttachmentRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| DryRun | bool |  | Checks whether you have the required permissions for the action, without actually making the request, and provides an er |
| TransitGatewayAttachmentId | Any  # complex shape | ✓ | The ID of the attachment. |

## Output Shape: DeleteTransitGatewayVpcAttachmentResult

- **TransitGatewayVpcAttachment** (Any  # complex shape): Information about the deleted VPC attachment.

## Implementation

```speclang
def delete_transit_gateway_vpc_attachment(store, request: dict) -> dict:
    """Deletes the specified VPC attachment."""
    transit_gateway_attachment_id = request.get("TransitGatewayAttachmentId", "").strip() if isinstance(request.get("TransitGatewayAttachmentId"), str) else request.get("TransitGatewayAttachmentId")

    if not store.transit_gateway_vpc_attachments(transit_gateway_attachment_id):
        raise ResourceNotFoundException(f"Resource transit_gateway_attachment_id not found")
    store.delete_transit_gateway_vpc_attachments(transit_gateway_attachment_id)
    return {}
```
