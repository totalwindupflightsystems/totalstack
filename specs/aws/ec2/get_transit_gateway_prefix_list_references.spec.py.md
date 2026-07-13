---
id: "@specs/aws/ec2/get_transit_gateway_prefix_list_references"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_GetTransitGatewayPrefixListReferences"
---

# GetTransitGatewayPrefixListReferences

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/get_transit_gateway_prefix_list_references
> **spec:implements:** @kind:operation GetTransitGatewayPrefixListReferences
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_GetTransitGatewayPrefixListReferences.spec.md

Gets information about the prefix list references in a specified transit gateway route table.

## Input Shape: GetTransitGatewayPrefixListReferencesRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| DryRun | bool |  | Checks whether you have the required permissions for the action, without actually making the request, and provides an er |
| Filters | list[Any  # complex shape] |  | One or more filters. The possible values are: attachment.resource-id - The ID of the resource for the attachment. attach |
| MaxResults | Any  # complex shape |  | The maximum number of results to return with a single call. To retrieve the remaining results, make another call with th |
| NextToken | str |  | The token for the next page of results. |
| TransitGatewayRouteTableId | Any  # complex shape | ✓ | The ID of the transit gateway route table. |

## Output Shape: GetTransitGatewayPrefixListReferencesResult

- **NextToken** (str): The token to use to retrieve the next page of results. This value is null when there are no more results to return.
- **TransitGatewayPrefixListReferences** (Any  # complex shape): Information about the prefix list references.

## Implementation

```speclang
def get_transit_gateway_prefix_list_references(store, request: dict) -> dict:
    """Gets information about the prefix list references in a specified transit gateway route table."""
    transit_gateway_route_table_id = request.get("TransitGatewayRouteTableId", "").strip() if isinstance(request.get("TransitGatewayRouteTableId"), str) else request.get("TransitGatewayRouteTableId")
    if not transit_gateway_route_table_id:
        raise ValidationException("TransitGatewayRouteTableId is required")

    resource = store.transit_gateway_prefix_list_referencess(transit_gateway_route_table_id)
    if not resource:
        raise ResourceNotFoundException(f"Resource transit_gateway_route_table_id not found")
    return {"TransitGatewayRouteTableId": transit_gateway_route_table_id, **resource}
```
