---
id: "@specs/aws/ec2/describe_ipam_pools"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_DescribeIpamPools"
---

# DescribeIpamPools

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/describe_ipam_pools
> **spec:implements:** @kind:operation DescribeIpamPools
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_DescribeIpamPools.spec.md

Get information about your IPAM pools.

## Input Shape: DescribeIpamPoolsRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| DryRun | bool |  | A check for whether you have the required permissions for the action without actually making the request and provides an |
| Filters | list[Any  # complex shape] |  | One or more filters for the request. For more information about filtering, see Filtering CLI output . |
| IpamPoolIds | list[str] |  | The IDs of the IPAM pools you would like information on. |
| MaxResults | Any  # complex shape |  | The maximum number of results to return in the request. |
| NextToken | Any  # complex shape |  | The token for the next page of results. |

## Output Shape: DescribeIpamPoolsResult

- **IpamPools** (Any  # complex shape): Information about the IPAM pools.
- **NextToken** (Any  # complex shape): The token to use to retrieve the next page of results. This value is null when there are no more results to return.

## Implementation

```speclang
def describe_ipam_pools(store, request: dict) -> dict:
    """Get information about your IPAM pools."""

    # Auto-generated get handler — verify resource key
    return store.get_resource(request)
```
