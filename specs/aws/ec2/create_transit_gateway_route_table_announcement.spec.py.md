---
id: "@specs/aws/ec2/create_transit_gateway_route_table_announcement"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_CreateTransitGatewayRouteTableAnnouncement"
---

# CreateTransitGatewayRouteTableAnnouncement

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/create_transit_gateway_route_table_announcement
> **spec:implements:** @kind:operation CreateTransitGatewayRouteTableAnnouncement
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_CreateTransitGatewayRouteTableAnnouncement.spec.md

Advertises a new transit gateway route table.

## Input Shape: CreateTransitGatewayRouteTableAnnouncementRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| DryRun | bool |  | Checks whether you have the required permissions for the action, without actually making the request, and provides an er |
| PeeringAttachmentId | Any  # complex shape | ✓ | The ID of the peering attachment. |
| TagSpecifications | list[Any  # complex shape] |  | The tags specifications applied to the transit gateway route table announcement. |
| TransitGatewayRouteTableId | Any  # complex shape | ✓ | The ID of the transit gateway route table. |

## Output Shape: CreateTransitGatewayRouteTableAnnouncementResult

- **TransitGatewayRouteTableAnnouncement** (Any  # complex shape): Provides details about the transit gateway route table announcement.

## Implementation

```speclang
def create_transit_gateway_route_table_announcement(store, request: dict) -> dict:
    """Advertises a new transit gateway route table."""
    peering_attachment_id = request.get("PeeringAttachmentId", "").strip() if isinstance(request.get("PeeringAttachmentId"), str) else request.get("PeeringAttachmentId")
    if not peering_attachment_id:
        raise ValidationException("PeeringAttachmentId is required")
    transit_gateway_route_table_id = request.get("TransitGatewayRouteTableId", "").strip() if isinstance(request.get("TransitGatewayRouteTableId"), str) else request.get("TransitGatewayRouteTableId")
    if not transit_gateway_route_table_id:
        raise ValidationException("TransitGatewayRouteTableId is required")

    if store.transit_gateway_route_table_announcements(transit_gateway_route_table_id):
        raise ResourceInUseException(f"Resource transit_gateway_route_table_id already exists")

    record = {
        "TransitGatewayRouteTableId": transit_gateway_route_table_id,
        "PeeringAttachmentId": peering_attachment_id,
        "TagSpecifications": tag_specifications,
        "DryRun": dry_run,
    }

    store.transit_gateway_route_table_announcements(transit_gateway_route_table_id, record)

    return {
        "TransitGatewayRouteTableAnnouncement": record.get("TransitGatewayRouteTableAnnouncement", {}),
    }
```
