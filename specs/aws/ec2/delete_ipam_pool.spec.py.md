---
id: "@specs/aws/ec2/delete_ipam_pool"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_DeleteIpamPool"
---

# DeleteIpamPool

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/delete_ipam_pool
> **spec:implements:** @kind:operation DeleteIpamPool
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_DeleteIpamPool.spec.md

Delete an IPAM pool. You cannot delete an IPAM pool if there are allocations in it or CIDRs provisioned to it. To release allocations, see ReleaseIpamPoolAllocation . To deprovision pool CIDRs, see DeprovisionIpamPoolCidr . For more information, see Delete a pool in the Amazon VPC IPAM User Guide .

## Input Shape: DeleteIpamPoolRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| Cascade | bool |  | Enables you to quickly delete an IPAM pool and all resources within that pool, including provisioned CIDRs, allocations, |
| DryRun | bool |  | A check for whether you have the required permissions for the action without actually making the request and provides an |
| IpamPoolId | Any  # complex shape | ✓ | The ID of the pool to delete. |

## Output Shape: DeleteIpamPoolResult

- **IpamPool** (Any  # complex shape): Information about the results of the deletion.

## Implementation

```speclang
def delete_ipam_pool(store, request: dict) -> dict:
    """Delete an IPAM pool. You cannot delete an IPAM pool if there are allocations in it or CIDRs provisioned to it. To release allocations, see ReleaseIpamPoolAllocation . To deprovision pool CIDRs, see De"""
    ipam_pool_id = request.get("IpamPoolId", "").strip() if isinstance(request.get("IpamPoolId"), str) else request.get("IpamPoolId")

    if not store.ipam_pools(ipam_pool_id):
        raise ResourceNotFoundException(f"Resource ipam_pool_id not found")
    store.delete_ipam_pools(ipam_pool_id)
    return {}
```
