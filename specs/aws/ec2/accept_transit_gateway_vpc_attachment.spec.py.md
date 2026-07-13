---
id: "@specs/aws/ec2/accept_transit_gateway_vpc_attachment"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_AcceptTransitGatewayVpcAttachment"
---

# AcceptTransitGatewayVpcAttachment

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/accept_transit_gateway_vpc_attachment
> **spec:implements:** @kind:operation AcceptTransitGatewayVpcAttachment
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_AcceptTransitGatewayVpcAttachment.spec.md

Accepts a request to attach a VPC to a transit gateway. The VPC attachment must be in the pendingAcceptance state. Use DescribeTransitGatewayVpcAttachments to view your pending VPC attachment requests. Use RejectTransitGatewayVpcAttachment to reject a VPC attachment request.

## Input Shape: AcceptTransitGatewayVpcAttachmentRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| DryRun | bool |  | Checks whether you have the required permissions for the action, without actually making the request, and provides an er |
| TransitGatewayAttachmentId | Any  # complex shape | ✓ | The ID of the attachment. |

## Output Shape: AcceptTransitGatewayVpcAttachmentResult

- **TransitGatewayVpcAttachment** (Any  # complex shape): The VPC attachment.

## Implementation

```speclang
def accept_transit_gateway_vpc_attachment(store, request: dict) -> dict:
    """Accepts a request to attach a VPC to a transit gateway. The VPC attachment must be in the pendingAcceptance state. Use DescribeTransitGatewayVpcAttachments to view your pending VPC attachment requests"""
    transit_gateway_attachment_id = request.get("TransitGatewayAttachmentId", "").strip() if isinstance(request.get("TransitGatewayAttachmentId"), str) else request.get("TransitGatewayAttachmentId")
    if not transit_gateway_attachment_id:
        raise ValidationException("TransitGatewayAttachmentId is required")

    # Auto-generated handler — operation not classified as CRUD
    return store.execute("AcceptTransitGatewayVpcAttachment", request)
```
