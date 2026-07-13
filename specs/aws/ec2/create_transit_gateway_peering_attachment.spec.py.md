---
id: "@specs/aws/ec2/create_transit_gateway_peering_attachment"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_CreateTransitGatewayPeeringAttachment"
---

# CreateTransitGatewayPeeringAttachment

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/create_transit_gateway_peering_attachment
> **spec:implements:** @kind:operation CreateTransitGatewayPeeringAttachment
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_CreateTransitGatewayPeeringAttachment.spec.md

Requests a transit gateway peering attachment between the specified transit gateway (requester) and a peer transit gateway (accepter). The peer transit gateway can be in your account or a different Amazon Web Services account. After you create the peering attachment, the owner of the accepter transit gateway must accept the attachment request.

## Input Shape: CreateTransitGatewayPeeringAttachmentRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| DryRun | bool |  | Checks whether you have the required permissions for the action, without actually making the request, and provides an er |
| Options | Any  # complex shape |  | Requests a transit gateway peering attachment. |
| PeerAccountId | str | ✓ | The ID of the Amazon Web Services account that owns the peer transit gateway. |
| PeerRegion | str | ✓ | The Region where the peer transit gateway is located. |
| PeerTransitGatewayId | Any  # complex shape | ✓ | The ID of the peer transit gateway with which to create the peering attachment. |
| TagSpecifications | list[Any  # complex shape] |  | The tags to apply to the transit gateway peering attachment. |
| TransitGatewayId | Any  # complex shape | ✓ | The ID of the transit gateway. |

## Output Shape: CreateTransitGatewayPeeringAttachmentResult

- **TransitGatewayPeeringAttachment** (Any  # complex shape): The transit gateway peering attachment.

## Implementation

```speclang
def create_transit_gateway_peering_attachment(store, request: dict) -> dict:
    """Requests a transit gateway peering attachment between the specified transit gateway (requester) and a peer transit gateway (accepter). The peer transit gateway can be in your account or a different Am"""
    peer_account_id = request.get("PeerAccountId", "").strip() if isinstance(request.get("PeerAccountId"), str) else request.get("PeerAccountId")
    if not peer_account_id:
        raise ValidationException("PeerAccountId is required")
    peer_region = request.get("PeerRegion", "").strip() if isinstance(request.get("PeerRegion"), str) else request.get("PeerRegion")
    if not peer_region:
        raise ValidationException("PeerRegion is required")
    peer_transit_gateway_id = request.get("PeerTransitGatewayId", "").strip() if isinstance(request.get("PeerTransitGatewayId"), str) else request.get("PeerTransitGatewayId")
    if not peer_transit_gateway_id:
        raise ValidationException("PeerTransitGatewayId is required")
    transit_gateway_id = request.get("TransitGatewayId", "").strip() if isinstance(request.get("TransitGatewayId"), str) else request.get("TransitGatewayId")
    if not transit_gateway_id:
        raise ValidationException("TransitGatewayId is required")

    if store.transit_gateway_peering_attachments(transit_gateway_id):
        raise ResourceInUseException(f"Resource transit_gateway_id already exists")

    record = {
        "TransitGatewayId": transit_gateway_id,
        "PeerTransitGatewayId": peer_transit_gateway_id,
        "PeerAccountId": peer_account_id,
        "PeerRegion": peer_region,
        "Options": options,
        "TagSpecifications": tag_specifications,
        "DryRun": dry_run,
    }

    store.transit_gateway_peering_attachments(transit_gateway_id, record)

    return {
        "TransitGatewayPeeringAttachment": record.get("TransitGatewayPeeringAttachment", {}),
    }
```
