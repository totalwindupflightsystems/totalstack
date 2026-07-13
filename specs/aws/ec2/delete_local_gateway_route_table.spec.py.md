---
id: "@specs/aws/ec2/delete_local_gateway_route_table"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_DeleteLocalGatewayRouteTable"
---

# DeleteLocalGatewayRouteTable

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/delete_local_gateway_route_table
> **spec:implements:** @kind:operation DeleteLocalGatewayRouteTable
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_DeleteLocalGatewayRouteTable.spec.md

Deletes a local gateway route table.

## Input Shape: DeleteLocalGatewayRouteTableRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| DryRun | bool |  | Checks whether you have the required permissions for the action, without actually making the request, and provides an er |
| LocalGatewayRouteTableId | Any  # complex shape | ✓ | The ID of the local gateway route table. |

## Output Shape: DeleteLocalGatewayRouteTableResult

- **LocalGatewayRouteTable** (Any  # complex shape): Information about the local gateway route table.

## Implementation

```speclang
def delete_local_gateway_route_table(store, request: dict) -> dict:
    """Deletes a local gateway route table."""
    local_gateway_route_table_id = request.get("LocalGatewayRouteTableId", "").strip() if isinstance(request.get("LocalGatewayRouteTableId"), str) else request.get("LocalGatewayRouteTableId")

    if not store.local_gateway_route_tables(local_gateway_route_table_id):
        raise ResourceNotFoundException(f"Resource local_gateway_route_table_id not found")
    store.delete_local_gateway_route_tables(local_gateway_route_table_id)
    return {}
```
