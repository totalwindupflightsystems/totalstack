---
id: "@specs/aws/ec2/enable_transit_gateway_route_table_propagation"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_EnableTransitGatewayRouteTablePropagation"
---

# EnableTransitGatewayRouteTablePropagation

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/enable_transit_gateway_route_table_propagation
> **spec:implements:** @kind:operation EnableTransitGatewayRouteTablePropagation
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_EnableTransitGatewayRouteTablePropagation.spec.md

Enables the specified attachment to propagate routes to the specified propagation route table.

## Input Shape: EnableTransitGatewayRouteTablePropagationRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| DryRun | bool |  | Checks whether you have the required permissions for the action, without actually making the request, and provides an er |
| TransitGatewayAttachmentId | Any  # complex shape |  | The ID of the attachment. |
| TransitGatewayRouteTableAnnouncementId | Any  # complex shape |  | The ID of the transit gateway route table announcement. |
| TransitGatewayRouteTableId | Any  # complex shape | ✓ | The ID of the propagation route table. |

## Output Shape: EnableTransitGatewayRouteTablePropagationResult

- **Propagation** (Any  # complex shape): Information about route propagation.

## Implementation

```speclang
def enable_transit_gateway_route_table_propagation(store, request: dict) -> dict:
    """Enables the specified attachment to propagate routes to the specified propagation route table."""
    transit_gateway_route_table_id = request.get("TransitGatewayRouteTableId", "").strip() if isinstance(request.get("TransitGatewayRouteTableId"), str) else request.get("TransitGatewayRouteTableId")
    if not transit_gateway_route_table_id:
        raise ValidationException("TransitGatewayRouteTableId is required")

    resource = store.enable_transit_gateway_route_table_propagations(transit_gateway_route_table_id)
    if not resource:
        raise ResourceNotFoundException(f"Resource transit_gateway_route_table_id not found")

    # Update mutable fields
    if "TransitGatewayAttachmentId" in request:
        resource["TransitGatewayAttachmentId"] = transit_gateway_attachment_id
    if "DryRun" in request:
        resource["DryRun"] = dry_run
    if "TransitGatewayRouteTableAnnouncementId" in request:
        resource["TransitGatewayRouteTableAnnouncementId"] = transit_gateway_route_table_announcement_id

    store.enable_transit_gateway_route_table_propagations(transit_gateway_route_table_id, resource)
    return resource
```
