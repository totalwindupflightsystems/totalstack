---
id: "@specs/aws/ec2/describe_ipv6_pools"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_DescribeIpv6Pools"
---

# DescribeIpv6Pools

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/describe_ipv6_pools
> **spec:implements:** @kind:operation DescribeIpv6Pools
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_DescribeIpv6Pools.spec.md

Describes your IPv6 address pools.

## Input Shape: DescribeIpv6PoolsRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| DryRun | bool |  | Checks whether you have the required permissions for the action, without actually making the request, and provides an er |
| Filters | list[Any  # complex shape] |  | One or more filters. tag :<key> - The key/value combination of a tag assigned to the resource. Use the tag key in the fi |
| MaxResults | Any  # complex shape |  | The maximum number of results to return with a single call. To retrieve the remaining results, make another call with th |
| NextToken | Any  # complex shape |  | The token for the next page of results. |
| PoolIds | list[Any  # complex shape] |  | The IDs of the IPv6 address pools. |

## Output Shape: DescribeIpv6PoolsResult

- **Ipv6Pools** (Any  # complex shape): Information about the IPv6 address pools.
- **NextToken** (Any  # complex shape): The token to use to retrieve the next page of results. This value is null when there are no more results to return.

## Implementation

```speclang
def describe_ipv6_pools(store, request: dict) -> dict:
    """Describes your IPv6 address pools."""

    # Auto-generated get handler — verify resource key
    return store.get_resource(request)
```
