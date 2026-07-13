---
id: "@specs/aws/ec2/get_ipam_pool_cidrs"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_GetIpamPoolCidrs"
---

# GetIpamPoolCidrs

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/get_ipam_pool_cidrs
> **spec:implements:** @kind:operation GetIpamPoolCidrs
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_GetIpamPoolCidrs.spec.md

Get the CIDRs provisioned to an IPAM pool.

## Input Shape: GetIpamPoolCidrsRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| DryRun | bool |  | A check for whether you have the required permissions for the action without actually making the request and provides an |
| Filters | list[Any  # complex shape] |  | One or more filters for the request. For more information about filtering, see Filtering CLI output . |
| IpamPoolId | Any  # complex shape | ✓ | The ID of the IPAM pool you want the CIDR for. |
| MaxResults | Any  # complex shape |  | The maximum number of results to return in the request. |
| NextToken | Any  # complex shape |  | The token for the next page of results. |

## Output Shape: GetIpamPoolCidrsResult

- **IpamPoolCidrs** (Any  # complex shape): Information about the CIDRs provisioned to an IPAM pool.
- **NextToken** (Any  # complex shape): The token to use to retrieve the next page of results. This value is null when there are no more results to return.

## Implementation

```speclang
def get_ipam_pool_cidrs(store, request: dict) -> dict:
    """Get the CIDRs provisioned to an IPAM pool."""
    ipam_pool_id = request.get("IpamPoolId", "").strip() if isinstance(request.get("IpamPoolId"), str) else request.get("IpamPoolId")
    if not ipam_pool_id:
        raise ValidationException("IpamPoolId is required")

    resource = store.ipam_pool_cidrss(ipam_pool_id)
    if not resource:
        raise ResourceNotFoundException(f"Resource ipam_pool_id not found")
    return {"IpamPoolId": ipam_pool_id, **resource}
```
