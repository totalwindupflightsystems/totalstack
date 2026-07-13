---
id: "@specs/aws/ec2/create_transit_gateway_route"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_CreateTransitGatewayRoute"
---

# CreateTransitGatewayRoute

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/create_transit_gateway_route
> **spec:implements:** @kind:operation CreateTransitGatewayRoute
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_CreateTransitGatewayRoute.spec.md

Creates a static route for the specified transit gateway route table.

## Input Shape: CreateTransitGatewayRouteRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| Blackhole | bool |  | Indicates whether to drop traffic that matches this route. |
| DestinationCidrBlock | str | ✓ | The CIDR range used for destination matches. Routing decisions are based on the most specific match. |
| DryRun | bool |  | Checks whether you have the required permissions for the action, without actually making the request, and provides an er |
| TransitGatewayAttachmentId | Any  # complex shape |  | The ID of the attachment. |
| TransitGatewayRouteTableId | Any  # complex shape | ✓ | The ID of the transit gateway route table. |

## Output Shape: CreateTransitGatewayRouteResult

- **Route** (Any  # complex shape): Information about the route.

## Implementation

```speclang
def create_transit_gateway_route(store, request: dict) -> dict:
    """Creates a static route for the specified transit gateway route table."""
    destination_cidr_block = request.get("DestinationCidrBlock", "").strip() if isinstance(request.get("DestinationCidrBlock"), str) else request.get("DestinationCidrBlock")
    if not destination_cidr_block:
        raise ValidationException("DestinationCidrBlock is required")
    transit_gateway_route_table_id = request.get("TransitGatewayRouteTableId", "").strip() if isinstance(request.get("TransitGatewayRouteTableId"), str) else request.get("TransitGatewayRouteTableId")
    if not transit_gateway_route_table_id:
        raise ValidationException("TransitGatewayRouteTableId is required")

    if store.transit_gateway_routes(destination_cidr_block):
        raise ResourceInUseException(f"Resource destination_cidr_block already exists")

    record = {
        "DestinationCidrBlock": destination_cidr_block,
        "TransitGatewayRouteTableId": transit_gateway_route_table_id,
        "TransitGatewayAttachmentId": transit_gateway_attachment_id,
        "Blackhole": blackhole,
        "DryRun": dry_run,
    }

    store.transit_gateway_routes(destination_cidr_block, record)

    return {
        "Route": record.get("Route", {}),
    }
```
