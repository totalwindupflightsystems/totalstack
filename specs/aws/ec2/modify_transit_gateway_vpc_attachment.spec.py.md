---
id: "@specs/aws/ec2/modify_transit_gateway_vpc_attachment"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_ModifyTransitGatewayVpcAttachment"
---

# ModifyTransitGatewayVpcAttachment

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/modify_transit_gateway_vpc_attachment
> **spec:implements:** @kind:operation ModifyTransitGatewayVpcAttachment
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_ModifyTransitGatewayVpcAttachment.spec.md

Modifies the specified VPC attachment.

## Input Shape: ModifyTransitGatewayVpcAttachmentRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| AddSubnetIds | list[Any  # complex shape] |  | The IDs of one or more subnets to add. You can specify at most one subnet per Availability Zone. |
| DryRun | bool |  | Checks whether you have the required permissions for the action, without actually making the request, and provides an er |
| Options | Any  # complex shape |  | The new VPC attachment options. |
| RemoveSubnetIds | list[Any  # complex shape] |  | The IDs of one or more subnets to remove. |
| TransitGatewayAttachmentId | Any  # complex shape | ✓ | The ID of the attachment. |

## Output Shape: ModifyTransitGatewayVpcAttachmentResult

- **TransitGatewayVpcAttachment** (Any  # complex shape): Information about the modified attachment.

## Implementation

```speclang
def modify_transit_gateway_vpc_attachment(store, request: dict) -> dict:
    """Modifies the specified VPC attachment."""
    transit_gateway_attachment_id = request.get("TransitGatewayAttachmentId", "").strip() if isinstance(request.get("TransitGatewayAttachmentId"), str) else request.get("TransitGatewayAttachmentId")
    if not transit_gateway_attachment_id:
        raise ValidationException("TransitGatewayAttachmentId is required")

    resource = store.transit_gateway_vpc_attachments(transit_gateway_attachment_id)
    if not resource:
        raise ResourceNotFoundException(f"Resource transit_gateway_attachment_id not found")

    # Update mutable fields
    if "AddSubnetIds" in request:
        resource["AddSubnetIds"] = add_subnet_ids
    if "RemoveSubnetIds" in request:
        resource["RemoveSubnetIds"] = remove_subnet_ids
    if "Options" in request:
        resource["Options"] = options
    if "DryRun" in request:
        resource["DryRun"] = dry_run

    store.transit_gateway_vpc_attachments(transit_gateway_attachment_id, resource)
    return resource
```
