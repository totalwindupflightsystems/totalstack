---
id: "@specs/aws/ec2/get_transit_gateway_route_table_associations"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_GetTransitGatewayRouteTableAssociations"
---

# GetTransitGatewayRouteTableAssociations

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/get_transit_gateway_route_table_associations
> **spec:implements:** @kind:operation GetTransitGatewayRouteTableAssociations
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_GetTransitGatewayRouteTableAssociations.spec.md

Gets information about the associations for the specified transit gateway route table.

## Input Shape: GetTransitGatewayRouteTableAssociationsRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| DryRun | bool |  | Checks whether you have the required permissions for the action, without actually making the request, and provides an er |
| Filters | list[Any  # complex shape] |  | One or more filters. The possible values are: resource-id - The ID of the resource. resource-type - The resource type. V |
| MaxResults | Any  # complex shape |  | The maximum number of results to return with a single call. To retrieve the remaining results, make another call with th |
| NextToken | str |  | The token for the next page of results. |
| TransitGatewayRouteTableId | Any  # complex shape | ✓ | The ID of the transit gateway route table. |

## Output Shape: GetTransitGatewayRouteTableAssociationsResult

- **Associations** (list[Any  # complex shape]): Information about the associations.
- **NextToken** (str): The token to use to retrieve the next page of results. This value is null when there are no more results to return.

## Implementation

```speclang
def get_transit_gateway_route_table_associations(store, request: dict) -> dict:
    """Gets information about the associations for the specified transit gateway route table."""
    transit_gateway_route_table_id = request.get("TransitGatewayRouteTableId", "").strip() if isinstance(request.get("TransitGatewayRouteTableId"), str) else request.get("TransitGatewayRouteTableId")
    if not transit_gateway_route_table_id:
        raise ValidationException("TransitGatewayRouteTableId is required")

    resource = store.transit_gateway_route_table_associationss(transit_gateway_route_table_id)
    if not resource:
        raise ResourceNotFoundException(f"Resource transit_gateway_route_table_id not found")
    return {"TransitGatewayRouteTableId": transit_gateway_route_table_id, **resource}
```
