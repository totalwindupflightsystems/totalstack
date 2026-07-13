---
id: "@specs/aws/ec2/delete_local_gateway_route"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_DeleteLocalGatewayRoute"
---

# DeleteLocalGatewayRoute

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/delete_local_gateway_route
> **spec:implements:** @kind:operation DeleteLocalGatewayRoute
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_DeleteLocalGatewayRoute.spec.md

Deletes the specified route from the specified local gateway route table.

## Input Shape: DeleteLocalGatewayRouteRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| DestinationCidrBlock | str |  | The CIDR range for the route. This must match the CIDR for the route exactly. |
| DestinationPrefixListId | Any  # complex shape |  | Use a prefix list in place of DestinationCidrBlock . You cannot use DestinationPrefixListId and DestinationCidrBlock in  |
| DryRun | bool |  | Checks whether you have the required permissions for the action, without actually making the request, and provides an er |
| LocalGatewayRouteTableId | Any  # complex shape | ✓ | The ID of the local gateway route table. |

## Output Shape: DeleteLocalGatewayRouteResult

- **Route** (Any  # complex shape): Information about the route.

## Implementation

```speclang
def delete_local_gateway_route(store, request: dict) -> dict:
    """Deletes the specified route from the specified local gateway route table."""
    local_gateway_route_table_id = request.get("LocalGatewayRouteTableId", "").strip() if isinstance(request.get("LocalGatewayRouteTableId"), str) else request.get("LocalGatewayRouteTableId")

    if not store.local_gateway_routes(local_gateway_route_table_id):
        raise ResourceNotFoundException(f"Resource local_gateway_route_table_id not found")
    store.delete_local_gateway_routes(local_gateway_route_table_id)
    return {}
```
