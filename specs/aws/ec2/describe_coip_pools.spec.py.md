---
id: "@specs/aws/ec2/describe_coip_pools"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_DescribeCoipPools"
---

# DescribeCoipPools

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/describe_coip_pools
> **spec:implements:** @kind:operation DescribeCoipPools
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_DescribeCoipPools.spec.md

Describes the specified customer-owned address pools or all of your customer-owned address pools.

## Input Shape: DescribeCoipPoolsRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| DryRun | bool |  | Checks whether you have the required permissions for the action, without actually making the request, and provides an er |
| Filters | list[Any  # complex shape] |  | One or more filters. coip-pool.local-gateway-route-table-id - The ID of the local gateway route table. coip-pool.pool-id |
| MaxResults | Any  # complex shape |  | The maximum number of results to return with a single call. To retrieve the remaining results, make another call with th |
| NextToken | str |  | The token for the next page of results. |
| PoolIds | Any  # complex shape |  | The IDs of the address pools. |

## Output Shape: DescribeCoipPoolsResult

- **CoipPools** (Any  # complex shape): Information about the address pools.
- **NextToken** (str): The token to use to retrieve the next page of results. This value is null when there are no more results to return.

## Implementation

```speclang
def describe_coip_pools(store, request: dict) -> dict:
    """Describes the specified customer-owned address pools or all of your customer-owned address pools."""

    # Auto-generated get handler — verify resource key
    return store.get_resource(request)
```
