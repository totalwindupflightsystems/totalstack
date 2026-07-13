---
id: "@specs/aws/ec2/search_transit_gateway_routes"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_SearchTransitGatewayRoutes"
---

# SearchTransitGatewayRoutes

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/search_transit_gateway_routes
> **spec:implements:** @kind:operation SearchTransitGatewayRoutes
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_SearchTransitGatewayRoutes.spec.md

Searches for routes in the specified transit gateway route table.

## Input Shape: SearchTransitGatewayRoutesRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| DryRun | bool |  | Checks whether you have the required permissions for the action, without actually making the request, and provides an er |
| Filters | list[Any  # complex shape] | ✓ | One or more filters. The possible values are: attachment.transit-gateway-attachment-id - The id of the transit gateway a |
| MaxResults | Any  # complex shape |  | The maximum number of routes to return. If a value is not provided, the default is 1000. |
| NextToken | str |  | The token for the next page of results. |
| TransitGatewayRouteTableId | Any  # complex shape | ✓ | The ID of the transit gateway route table. |

## Output Shape: SearchTransitGatewayRoutesResult

- **AdditionalRoutesAvailable** (bool): Indicates whether there are additional routes available.
- **NextToken** (str): The token to use to retrieve the next page of results. This value is null when there are no more results to return.
- **Routes** (list[Any  # complex shape]): Information about the routes.

## Implementation

```speclang
def search_transit_gateway_routes(store, request: dict) -> dict:
    """Searches for routes in the specified transit gateway route table."""
    filters = request.get("Filters", "").strip() if isinstance(request.get("Filters"), str) else request.get("Filters")
    if not filters:
        raise ValidationException("Filters is required")
    transit_gateway_route_table_id = request.get("TransitGatewayRouteTableId", "").strip() if isinstance(request.get("TransitGatewayRouteTableId"), str) else request.get("TransitGatewayRouteTableId")
    if not transit_gateway_route_table_id:
        raise ValidationException("TransitGatewayRouteTableId is required")

    items = store.list_search_transit_gateway_routess()
    return {"Routes": list(items.values())}
```
