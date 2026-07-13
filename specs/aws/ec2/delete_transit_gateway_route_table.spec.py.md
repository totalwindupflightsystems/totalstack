---
id: "@specs/aws/ec2/delete_transit_gateway_route_table"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_DeleteTransitGatewayRouteTable"
---

# DeleteTransitGatewayRouteTable

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/delete_transit_gateway_route_table
> **spec:implements:** @kind:operation DeleteTransitGatewayRouteTable
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_DeleteTransitGatewayRouteTable.spec.md

Deletes the specified transit gateway route table. If there are any route tables associated with the transit gateway route table, you must first run DisassociateRouteTable before you can delete the transit gateway route table. This removes any route tables associated with the transit gateway route table.

## Input Shape: DeleteTransitGatewayRouteTableRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| DryRun | bool |  | Checks whether you have the required permissions for the action, without actually making the request, and provides an er |
| TransitGatewayRouteTableId | Any  # complex shape | ✓ | The ID of the transit gateway route table. |

## Output Shape: DeleteTransitGatewayRouteTableResult

- **TransitGatewayRouteTable** (Any  # complex shape): Information about the deleted transit gateway route table.

## Implementation

```speclang
def delete_transit_gateway_route_table(store, request: dict) -> dict:
    """Deletes the specified transit gateway route table. If there are any route tables associated with the transit gateway route table, you must first run DisassociateRouteTable before you can delete the tr"""
    transit_gateway_route_table_id = request.get("TransitGatewayRouteTableId", "").strip() if isinstance(request.get("TransitGatewayRouteTableId"), str) else request.get("TransitGatewayRouteTableId")

    if not store.transit_gateway_route_tables(transit_gateway_route_table_id):
        raise ResourceNotFoundException(f"Resource transit_gateway_route_table_id not found")
    store.delete_transit_gateway_route_tables(transit_gateway_route_table_id)
    return {}
```
