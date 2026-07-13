---
id: "@specs/aws/ec2/replace_transit_gateway_route"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_ReplaceTransitGatewayRoute"
---

# ReplaceTransitGatewayRoute

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/replace_transit_gateway_route
> **spec:implements:** @kind:operation ReplaceTransitGatewayRoute
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_ReplaceTransitGatewayRoute.spec.md

Replaces the specified route in the specified transit gateway route table.

## Input Shape: ReplaceTransitGatewayRouteRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| Blackhole | bool |  | Indicates whether traffic matching this route is to be dropped. |
| DestinationCidrBlock | str | ✓ | The CIDR range used for the destination match. Routing decisions are based on the most specific match. |
| DryRun | bool |  | Checks whether you have the required permissions for the action, without actually making the request, and provides an er |
| TransitGatewayAttachmentId | Any  # complex shape |  | The ID of the attachment. |
| TransitGatewayRouteTableId | Any  # complex shape | ✓ | The ID of the route table. |

## Output Shape: ReplaceTransitGatewayRouteResult

- **Route** (Any  # complex shape): Information about the modified route.

## Implementation

```speclang
def replace_transit_gateway_route(store, request: dict) -> dict:
    """Replaces the specified route in the specified transit gateway route table."""
    destination_cidr_block = request.get("DestinationCidrBlock", "").strip() if isinstance(request.get("DestinationCidrBlock"), str) else request.get("DestinationCidrBlock")
    if not destination_cidr_block:
        raise ValidationException("DestinationCidrBlock is required")
    transit_gateway_route_table_id = request.get("TransitGatewayRouteTableId", "").strip() if isinstance(request.get("TransitGatewayRouteTableId"), str) else request.get("TransitGatewayRouteTableId")
    if not transit_gateway_route_table_id:
        raise ValidationException("TransitGatewayRouteTableId is required")

    # Auto-generated handler — operation not classified as CRUD
    return store.execute("ReplaceTransitGatewayRoute", request)
```
