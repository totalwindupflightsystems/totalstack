---
id: "@specs/aws/ec2/create_transit_gateway_vpc_attachment"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_CreateTransitGatewayVpcAttachment"
---

# CreateTransitGatewayVpcAttachment

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/create_transit_gateway_vpc_attachment
> **spec:implements:** @kind:operation CreateTransitGatewayVpcAttachment
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_CreateTransitGatewayVpcAttachment.spec.md

Attaches the specified VPC to the specified transit gateway. If you attach a VPC with a CIDR range that overlaps the CIDR range of a VPC that is already attached, the new VPC CIDR range is not propagated to the default propagation route table. To send VPC traffic to an attached transit gateway, add a route to the VPC route table using CreateRoute .

## Input Shape: CreateTransitGatewayVpcAttachmentRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| DryRun | bool |  | Checks whether you have the required permissions for the action, without actually making the request, and provides an er |
| Options | Any  # complex shape |  | The VPC attachment options. |
| SubnetIds | list[Any  # complex shape] | ✓ | The IDs of one or more subnets. You can specify only one subnet per Availability Zone. You must specify at least one sub |
| TagSpecifications | list[Any  # complex shape] |  | The tags to apply to the VPC attachment. |
| TransitGatewayId | Any  # complex shape | ✓ | The ID of the transit gateway. |
| VpcId | Any  # complex shape | ✓ | The ID of the VPC. |

## Output Shape: CreateTransitGatewayVpcAttachmentResult

- **TransitGatewayVpcAttachment** (Any  # complex shape): Information about the VPC attachment.

## Implementation

```speclang
def create_transit_gateway_vpc_attachment(store, request: dict) -> dict:
    """Attaches the specified VPC to the specified transit gateway. If you attach a VPC with a CIDR range that overlaps the CIDR range of a VPC that is already attached, the new VPC CIDR range is not propaga"""
    subnet_ids = request.get("SubnetIds", "").strip() if isinstance(request.get("SubnetIds"), str) else request.get("SubnetIds")
    if not subnet_ids:
        raise ValidationException("SubnetIds is required")
    transit_gateway_id = request.get("TransitGatewayId", "").strip() if isinstance(request.get("TransitGatewayId"), str) else request.get("TransitGatewayId")
    if not transit_gateway_id:
        raise ValidationException("TransitGatewayId is required")
    vpc_id = request.get("VpcId", "").strip() if isinstance(request.get("VpcId"), str) else request.get("VpcId")
    if not vpc_id:
        raise ValidationException("VpcId is required")

    if store.transit_gateway_vpc_attachments(subnet_ids):
        raise ResourceInUseException(f"Resource subnet_ids already exists")

    record = {
        "TransitGatewayId": transit_gateway_id,
        "VpcId": vpc_id,
        "SubnetIds": subnet_ids,
        "Options": options,
        "TagSpecifications": tag_specifications,
        "DryRun": dry_run,
    }

    store.transit_gateway_vpc_attachments(subnet_ids, record)

    return {
        "TransitGatewayVpcAttachment": record.get("TransitGatewayVpcAttachment", {}),
    }
```
