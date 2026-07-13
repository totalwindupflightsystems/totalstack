---
id: "@specs/aws/ec2/delete_transit_gateway_prefix_list_reference"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_DeleteTransitGatewayPrefixListReference"
---

# DeleteTransitGatewayPrefixListReference

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/delete_transit_gateway_prefix_list_reference
> **spec:implements:** @kind:operation DeleteTransitGatewayPrefixListReference
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_DeleteTransitGatewayPrefixListReference.spec.md

Deletes a reference (route) to a prefix list in a specified transit gateway route table.

## Input Shape: DeleteTransitGatewayPrefixListReferenceRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| DryRun | bool |  | Checks whether you have the required permissions for the action, without actually making the request, and provides an er |
| PrefixListId | Any  # complex shape | ✓ | The ID of the prefix list. |
| TransitGatewayRouteTableId | Any  # complex shape | ✓ | The ID of the route table. |

## Output Shape: DeleteTransitGatewayPrefixListReferenceResult

- **TransitGatewayPrefixListReference** (Any  # complex shape): Information about the deleted prefix list reference.

## Implementation

```speclang
def delete_transit_gateway_prefix_list_reference(store, request: dict) -> dict:
    """Deletes a reference (route) to a prefix list in a specified transit gateway route table."""
    prefix_list_id = request.get("PrefixListId", "").strip() if isinstance(request.get("PrefixListId"), str) else request.get("PrefixListId")
    transit_gateway_route_table_id = request.get("TransitGatewayRouteTableId", "").strip() if isinstance(request.get("TransitGatewayRouteTableId"), str) else request.get("TransitGatewayRouteTableId")

    if not store.transit_gateway_prefix_list_references(transit_gateway_route_table_id):
        raise ResourceNotFoundException(f"Resource transit_gateway_route_table_id not found")
    store.delete_transit_gateway_prefix_list_references(transit_gateway_route_table_id)
    return {}
```
