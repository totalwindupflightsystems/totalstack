---
id: "@specs/aws/ec2/describe_public_ipv4_pools"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_DescribePublicIpv4Pools"
---

# DescribePublicIpv4Pools

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/describe_public_ipv4_pools
> **spec:implements:** @kind:operation DescribePublicIpv4Pools
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_DescribePublicIpv4Pools.spec.md

Describes the specified IPv4 address pools.

## Input Shape: DescribePublicIpv4PoolsRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| Filters | list[Any  # complex shape] |  | One or more filters. tag :<key> - The key/value combination of a tag assigned to the resource. Use the tag key in the fi |
| MaxResults | Any  # complex shape |  | The maximum number of results to return with a single call. To retrieve the remaining results, make another call with th |
| NextToken | Any  # complex shape |  | The token for the next page of results. |
| PoolIds | list[Any  # complex shape] |  | The IDs of the address pools. |

## Output Shape: DescribePublicIpv4PoolsResult

- **NextToken** (str): The token to use to retrieve the next page of results. This value is null when there are no more results to return.
- **PublicIpv4Pools** (Any  # complex shape): Information about the address pools.

## Implementation

```speclang
def describe_public_ipv4_pools(store, request: dict) -> dict:
    """Describes the specified IPv4 address pools."""

    # Auto-generated get handler — verify resource key
    return store.get_resource(request)
```
