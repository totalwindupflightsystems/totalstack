---
id: "@specs/aws/ec2/get_associated_ipv6_pool_cidrs"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_GetAssociatedIpv6PoolCidrs"
---

# GetAssociatedIpv6PoolCidrs

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/get_associated_ipv6_pool_cidrs
> **spec:implements:** @kind:operation GetAssociatedIpv6PoolCidrs
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_GetAssociatedIpv6PoolCidrs.spec.md

Gets information about the IPv6 CIDR block associations for a specified IPv6 address pool.

## Input Shape: GetAssociatedIpv6PoolCidrsRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| DryRun | bool |  | Checks whether you have the required permissions for the action, without actually making the request, and provides an er |
| MaxResults | Any  # complex shape |  | The maximum number of results to return with a single call. To retrieve the remaining results, make another call with th |
| NextToken | Any  # complex shape |  | The token for the next page of results. |
| PoolId | Any  # complex shape | ✓ | The ID of the IPv6 address pool. |

## Output Shape: GetAssociatedIpv6PoolCidrsResult

- **Ipv6CidrAssociations** (Any  # complex shape): Information about the IPv6 CIDR block associations.
- **NextToken** (str): The token to use to retrieve the next page of results. This value is null when there are no more results to return.

## Implementation

```speclang
def get_associated_ipv6_pool_cidrs(store, request: dict) -> dict:
    """Gets information about the IPv6 CIDR block associations for a specified IPv6 address pool."""
    pool_id = request.get("PoolId", "").strip() if isinstance(request.get("PoolId"), str) else request.get("PoolId")
    if not pool_id:
        raise ValidationException("PoolId is required")

    resource = store.associated_ipv6_pool_cidrss(pool_id)
    if not resource:
        raise ResourceNotFoundException(f"Resource pool_id not found")
    return {"PoolId": pool_id, **resource}
```
