---
id: "@specs/aws/ec2/describe_transit_gateway_policy_tables"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_DescribeTransitGatewayPolicyTables"
---

# DescribeTransitGatewayPolicyTables

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/describe_transit_gateway_policy_tables
> **spec:implements:** @kind:operation DescribeTransitGatewayPolicyTables
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_DescribeTransitGatewayPolicyTables.spec.md

Describes one or more transit gateway route policy tables.

## Input Shape: DescribeTransitGatewayPolicyTablesRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| DryRun | bool |  | Checks whether you have the required permissions for the action, without actually making the request, and provides an er |
| Filters | list[Any  # complex shape] |  | The filters associated with the transit gateway policy table. |
| MaxResults | Any  # complex shape |  | The maximum number of results to return with a single call. To retrieve the remaining results, make another call with th |
| NextToken | str |  | The token for the next page of results. |
| TransitGatewayPolicyTableIds | list[Any  # complex shape] |  | The IDs of the transit gateway policy tables. |

## Output Shape: DescribeTransitGatewayPolicyTablesResult

- **NextToken** (str): The token for the next page of results.
- **TransitGatewayPolicyTables** (list[Any  # complex shape]): Describes the transit gateway policy tables.

## Implementation

```speclang
def describe_transit_gateway_policy_tables(store, request: dict) -> dict:
    """Describes one or more transit gateway route policy tables."""

    # Auto-generated get handler — verify resource key
    return store.get_resource(request)
```
