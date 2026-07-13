---
id: "@specs/aws/ec2/delete_transit_gateway_route"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_DeleteTransitGatewayRoute"
---

# DeleteTransitGatewayRoute

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/delete_transit_gateway_route
> **spec:implements:** @kind:operation DeleteTransitGatewayRoute
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_DeleteTransitGatewayRoute.spec.md

Deletes the specified route from the specified transit gateway route table.

## Input Shape: DeleteTransitGatewayRouteRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| DestinationCidrBlock | str | ✓ | The CIDR range for the route. This must match the CIDR for the route exactly. |
| DryRun | bool |  | Checks whether you have the required permissions for the action, without actually making the request, and provides an er |
| TransitGatewayRouteTableId | Any  # complex shape | ✓ | The ID of the transit gateway route table. |

## Output Shape: DeleteTransitGatewayRouteResult

- **Route** (Any  # complex shape): Information about the route.

## Implementation

```speclang
def delete_transit_gateway_route(store, request: dict) -> dict:
    """Deletes the specified route from the specified transit gateway route table."""
    destination_cidr_block = request.get("DestinationCidrBlock", "").strip() if isinstance(request.get("DestinationCidrBlock"), str) else request.get("DestinationCidrBlock")
    transit_gateway_route_table_id = request.get("TransitGatewayRouteTableId", "").strip() if isinstance(request.get("TransitGatewayRouteTableId"), str) else request.get("TransitGatewayRouteTableId")

    if not store.transit_gateway_routes(destination_cidr_block):
        raise ResourceNotFoundException(f"Resource destination_cidr_block not found")
    store.delete_transit_gateway_routes(destination_cidr_block)
    return {}
```
