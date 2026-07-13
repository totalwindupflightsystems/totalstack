---
id: "@specs/aws/ec2/search_local_gateway_routes"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_SearchLocalGatewayRoutes"
---

# SearchLocalGatewayRoutes

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/search_local_gateway_routes
> **spec:implements:** @kind:operation SearchLocalGatewayRoutes
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_SearchLocalGatewayRoutes.spec.md

Searches for routes in the specified local gateway route table.

## Input Shape: SearchLocalGatewayRoutesRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| DryRun | bool |  | Checks whether you have the required permissions for the action, without actually making the request, and provides an er |
| Filters | list[Any  # complex shape] |  | One or more filters. prefix-list-id - The ID of the prefix list. route-search.exact-match - The exact match of the speci |
| LocalGatewayRouteTableId | Any  # complex shape | ✓ | The ID of the local gateway route table. |
| MaxResults | Any  # complex shape |  | The maximum number of results to return with a single call. To retrieve the remaining results, make another call with th |
| NextToken | str |  | The token for the next page of results. |

## Output Shape: SearchLocalGatewayRoutesResult

- **NextToken** (str): The token to use to retrieve the next page of results. This value is null when there are no more results to return.
- **Routes** (list[Any  # complex shape]): Information about the routes.

## Implementation

```speclang
def search_local_gateway_routes(store, request: dict) -> dict:
    """Searches for routes in the specified local gateway route table."""
    local_gateway_route_table_id = request.get("LocalGatewayRouteTableId", "").strip() if isinstance(request.get("LocalGatewayRouteTableId"), str) else request.get("LocalGatewayRouteTableId")
    if not local_gateway_route_table_id:
        raise ValidationException("LocalGatewayRouteTableId is required")

    items = store.list_search_local_gateway_routess()
    return {"Routes": list(items.values())}
```
