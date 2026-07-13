---
id: "@specs/aws/ec2/describe_transit_gateway_route_tables"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_DescribeTransitGatewayRouteTables"
---

# DescribeTransitGatewayRouteTables

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/describe_transit_gateway_route_tables
> **spec:implements:** @kind:operation DescribeTransitGatewayRouteTables
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_DescribeTransitGatewayRouteTables.spec.md

Describes one or more transit gateway route tables. By default, all transit gateway route tables are described. Alternatively, you can filter the results.

## Input Shape: DescribeTransitGatewayRouteTablesRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| DryRun | bool |  | Checks whether you have the required permissions for the action, without actually making the request, and provides an er |
| Filters | list[Any  # complex shape] |  | One or more filters. The possible values are: default-association-route-table - Indicates whether this is the default as |
| MaxResults | Any  # complex shape |  | The maximum number of results to return with a single call. To retrieve the remaining results, make another call with th |
| NextToken | str |  | The token for the next page of results. |
| TransitGatewayRouteTableIds | list[Any  # complex shape] |  | The IDs of the transit gateway route tables. |

## Output Shape: DescribeTransitGatewayRouteTablesResult

- **NextToken** (str): The token to use to retrieve the next page of results. This value is null when there are no more results to return.
- **TransitGatewayRouteTables** (list[Any  # complex shape]): Information about the transit gateway route tables.

## Implementation

```speclang
def describe_transit_gateway_route_tables(store, request: dict) -> dict:
    """Describes one or more transit gateway route tables. By default, all transit gateway route tables are described. Alternatively, you can filter the results."""

    # Auto-generated get handler — verify resource key
    return store.get_resource(request)
```
