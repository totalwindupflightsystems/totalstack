---
id: "@specs/aws/ec2/create_transit_gateway_route_table"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_CreateTransitGatewayRouteTable"
---

# CreateTransitGatewayRouteTable

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/create_transit_gateway_route_table
> **spec:implements:** @kind:operation CreateTransitGatewayRouteTable
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_CreateTransitGatewayRouteTable.spec.md

Creates a route table for the specified transit gateway.

## Input Shape: CreateTransitGatewayRouteTableRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| DryRun | bool |  | Checks whether you have the required permissions for the action, without actually making the request, and provides an er |
| TagSpecifications | list[Any  # complex shape] |  | The tags to apply to the transit gateway route table. |
| TransitGatewayId | Any  # complex shape | ✓ | The ID of the transit gateway. |

## Output Shape: CreateTransitGatewayRouteTableResult

- **TransitGatewayRouteTable** (Any  # complex shape): Information about the transit gateway route table.

## Implementation

```speclang
def create_transit_gateway_route_table(store, request: dict) -> dict:
    """Creates a route table for the specified transit gateway."""
    transit_gateway_id = request.get("TransitGatewayId", "").strip() if isinstance(request.get("TransitGatewayId"), str) else request.get("TransitGatewayId")
    if not transit_gateway_id:
        raise ValidationException("TransitGatewayId is required")

    if store.transit_gateway_route_tables(transit_gateway_id):
        raise ResourceInUseException(f"Resource transit_gateway_id already exists")

    record = {
        "TransitGatewayId": transit_gateway_id,
        "TagSpecifications": tag_specifications,
        "DryRun": dry_run,
    }

    store.transit_gateway_route_tables(transit_gateway_id, record)

    return {
        "TransitGatewayRouteTable": record.get("TransitGatewayRouteTable", {}),
    }
```
