---
id: "@specs/aws/ec2/release_ipam_pool_allocation"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_ReleaseIpamPoolAllocation"
---

# ReleaseIpamPoolAllocation

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/release_ipam_pool_allocation
> **spec:implements:** @kind:operation ReleaseIpamPoolAllocation
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_ReleaseIpamPoolAllocation.spec.md

Release an allocation within an IPAM pool. The Region you use should be the IPAM pool locale. The locale is the Amazon Web Services Region where this IPAM pool is available for allocations. You can only use this action to release manual allocations. To remove an allocation for a resource without deleting the resource, set its monitored state to false using ModifyIpamResourceCidr . For more information, see Release an allocation in the Amazon VPC IPAM User Guide . All EC2 API actions follow an eventual consistency model.

## Input Shape: ReleaseIpamPoolAllocationRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| Cidr | str | ✓ | The CIDR of the allocation you want to release. |
| DryRun | bool |  | A check for whether you have the required permissions for the action without actually making the request and provides an |
| IpamPoolAllocationId | Any  # complex shape | ✓ | The ID of the allocation. |
| IpamPoolId | Any  # complex shape | ✓ | The ID of the IPAM pool which contains the allocation you want to release. |

## Output Shape: ReleaseIpamPoolAllocationResult

- **Success** (bool): Indicates if the release was successful.

## Implementation

```speclang
def release_ipam_pool_allocation(store, request: dict) -> dict:
    """Release an allocation within an IPAM pool. The Region you use should be the IPAM pool locale. The locale is the Amazon Web Services Region where this IPAM pool is available for allocations. You can on"""
    cidr = request.get("Cidr", "").strip() if isinstance(request.get("Cidr"), str) else request.get("Cidr")
    if not cidr:
        raise ValidationException("Cidr is required")
    ipam_pool_allocation_id = request.get("IpamPoolAllocationId", "").strip() if isinstance(request.get("IpamPoolAllocationId"), str) else request.get("IpamPoolAllocationId")
    if not ipam_pool_allocation_id:
        raise ValidationException("IpamPoolAllocationId is required")
    ipam_pool_id = request.get("IpamPoolId", "").strip() if isinstance(request.get("IpamPoolId"), str) else request.get("IpamPoolId")
    if not ipam_pool_id:
        raise ValidationException("IpamPoolId is required")

    # Auto-generated handler — operation not classified as CRUD
    return store.execute("ReleaseIpamPoolAllocation", request)
```
