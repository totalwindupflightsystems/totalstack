---
id: "@specs/aws/ec2/delete_route_table"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_DeleteRouteTable"
---

# DeleteRouteTable

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/delete_route_table
> **spec:implements:** @kind:operation DeleteRouteTable
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_DeleteRouteTable.spec.md

Deletes the specified route table. You must disassociate the route table from any subnets before you can delete it. You can't delete the main route table.

## Input Shape: DeleteRouteTableRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| DryRun | bool |  | Checks whether you have the required permissions for the action, without actually making the request, and provides an er |
| RouteTableId | Any  # complex shape | ✓ | The ID of the route table. |

## Implementation

```speclang
def delete_route_table(store, request: dict) -> dict:
    """Deletes the specified route table. You must disassociate the route table from any subnets before you can delete it. You can't delete the main route table."""
    route_table_id = request.get("RouteTableId", "").strip() if isinstance(request.get("RouteTableId"), str) else request.get("RouteTableId")

    if not store.route_tables(route_table_id):
        raise ResourceNotFoundException(f"Resource route_table_id not found")
    store.delete_route_tables(route_table_id)
    return {}
```
