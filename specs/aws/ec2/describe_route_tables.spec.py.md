---
id: "@specs/aws/ec2/describe_route_tables"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_DescribeRouteTables"
---

# DescribeRouteTables

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/describe_route_tables
> **spec:implements:** @kind:operation DescribeRouteTables
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_DescribeRouteTables.spec.md

Describes your route tables. The default is to describe all your route tables. Alternatively, you can specify specific route table IDs or filter the results to include only the route tables that match specific criteria. Each subnet in your VPC must be associated with a route table. If a subnet is not explicitly associated with any route table, it is implicitly associated with the main route table. This command does not return the subnet ID for implicit associations. For more information, see Route tables in the Amazon VPC User Guide .

## Input Shape: DescribeRouteTablesRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| DryRun | bool |  | Checks whether you have the required permissions for the action, without actually making the request, and provides an er |
| Filters | list[Any  # complex shape] |  | The filters. association.gateway-id - The ID of the gateway involved in the association. association.route-table-associa |
| MaxResults | Any  # complex shape |  | The maximum number of items to return for this request. To get the next page of items, make another request with the tok |
| NextToken | str |  | The token returned from a previous paginated request. Pagination continues from the end of the items returned by the pre |
| RouteTableIds | list[Any  # complex shape] |  | The IDs of the route tables. |

## Output Shape: DescribeRouteTablesResult

- **NextToken** (str): The token to include in another request to get the next page of items. This value is null when there are no more items t
- **RouteTables** (list[Any  # complex shape]): Information about the route tables.

## Implementation

```speclang
def describe_route_tables(store, request: dict) -> dict:
    """Describes your route tables. The default is to describe all your route tables. Alternatively, you can specify specific route table IDs or filter the results to include only the route tables that match"""

    # Auto-generated get handler — verify resource key
    return store.get_resource(request)
```
