---
id: "@specs/aws/ec2/delete_transit_gateway_route_table_announcement"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_DeleteTransitGatewayRouteTableAnnouncement"
---

# DeleteTransitGatewayRouteTableAnnouncement

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/delete_transit_gateway_route_table_announcement
> **spec:implements:** @kind:operation DeleteTransitGatewayRouteTableAnnouncement
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_DeleteTransitGatewayRouteTableAnnouncement.spec.md

Advertises to the transit gateway that a transit gateway route table is deleted.

## Input Shape: DeleteTransitGatewayRouteTableAnnouncementRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| DryRun | bool |  | Checks whether you have the required permissions for the action, without actually making the request, and provides an er |
| TransitGatewayRouteTableAnnouncementId | Any  # complex shape | ✓ | The transit gateway route table ID that's being deleted. |

## Output Shape: DeleteTransitGatewayRouteTableAnnouncementResult

- **TransitGatewayRouteTableAnnouncement** (Any  # complex shape): Provides details about a deleted transit gateway route table.

## Implementation

```speclang
def delete_transit_gateway_route_table_announcement(store, request: dict) -> dict:
    """Advertises to the transit gateway that a transit gateway route table is deleted."""
    transit_gateway_route_table_announcement_id = request.get("TransitGatewayRouteTableAnnouncementId", "").strip() if isinstance(request.get("TransitGatewayRouteTableAnnouncementId"), str) else request.get("TransitGatewayRouteTableAnnouncementId")

    if not store.transit_gateway_route_table_announcements(transit_gateway_route_table_announcement_id):
        raise ResourceNotFoundException(f"Resource transit_gateway_route_table_announcement_id not found")
    store.delete_transit_gateway_route_table_announcements(transit_gateway_route_table_announcement_id)
    return {}
```
