---
id: "@specs/aws/ec2/delete_route"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_DeleteRoute"
---

# DeleteRoute

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/delete_route
> **spec:implements:** @kind:operation DeleteRoute
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_DeleteRoute.spec.md

Deletes the specified route from the specified route table.

## Input Shape: DeleteRouteRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| DestinationCidrBlock | str |  | The IPv4 CIDR range for the route. The value you specify must match the CIDR for the route exactly. |
| DestinationIpv6CidrBlock | str |  | The IPv6 CIDR range for the route. The value you specify must match the CIDR for the route exactly. |
| DestinationPrefixListId | Any  # complex shape |  | The ID of the prefix list for the route. |
| DryRun | bool |  | Checks whether you have the required permissions for the action, without actually making the request, and provides an er |
| RouteTableId | Any  # complex shape | ✓ | The ID of the route table. |

## Implementation

```speclang
def delete_route(store, request: dict) -> dict:
    """Deletes the specified route from the specified route table."""
    route_table_id = request.get("RouteTableId", "").strip() if isinstance(request.get("RouteTableId"), str) else request.get("RouteTableId")

    if not store.routes(route_table_id):
        raise ResourceNotFoundException(f"Resource route_table_id not found")
    store.delete_routes(route_table_id)
    return {}
```
