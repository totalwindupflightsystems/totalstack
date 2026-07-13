---
id: "@specs/aws/ec2/create_transit_gateway_connect"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_CreateTransitGatewayConnect"
---

# CreateTransitGatewayConnect

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/create_transit_gateway_connect
> **spec:implements:** @kind:operation CreateTransitGatewayConnect
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_CreateTransitGatewayConnect.spec.md

Creates a Connect attachment from a specified transit gateway attachment. A Connect attachment is a GRE-based tunnel attachment that you can use to establish a connection between a transit gateway and an appliance. A Connect attachment uses an existing VPC or Amazon Web Services Direct Connect attachment as the underlying transport mechanism.

## Input Shape: CreateTransitGatewayConnectRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| DryRun | bool |  | Checks whether you have the required permissions for the action, without actually making the request, and provides an er |
| Options | Any  # complex shape | ✓ | The Connect attachment options. |
| TagSpecifications | list[Any  # complex shape] |  | The tags to apply to the Connect attachment. |
| TransportTransitGatewayAttachmentId | Any  # complex shape | ✓ | The ID of the transit gateway attachment. You can specify a VPC attachment or Amazon Web Services Direct Connect attachm |

## Output Shape: CreateTransitGatewayConnectResult

- **TransitGatewayConnect** (Any  # complex shape): Information about the Connect attachment.

## Implementation

```speclang
def create_transit_gateway_connect(store, request: dict) -> dict:
    """Creates a Connect attachment from a specified transit gateway attachment. A Connect attachment is a GRE-based tunnel attachment that you can use to establish a connection between a transit gateway and"""
    options = request.get("Options", "").strip() if isinstance(request.get("Options"), str) else request.get("Options")
    if not options:
        raise ValidationException("Options is required")
    transport_transit_gateway_attachment_id = request.get("TransportTransitGatewayAttachmentId", "").strip() if isinstance(request.get("TransportTransitGatewayAttachmentId"), str) else request.get("TransportTransitGatewayAttachmentId")
    if not transport_transit_gateway_attachment_id:
        raise ValidationException("TransportTransitGatewayAttachmentId is required")

    if store.transit_gateway_connects(transport_transit_gateway_attachment_id):
        raise ResourceInUseException(f"Resource transport_transit_gateway_attachment_id already exists")

    record = {
        "TransportTransitGatewayAttachmentId": transport_transit_gateway_attachment_id,
        "Options": options,
        "TagSpecifications": tag_specifications,
        "DryRun": dry_run,
    }

    store.transit_gateway_connects(transport_transit_gateway_attachment_id, record)

    return {
        "TransitGatewayConnect": record.get("TransitGatewayConnect", {}),
    }
```
