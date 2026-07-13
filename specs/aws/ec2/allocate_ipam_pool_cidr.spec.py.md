---
id: "@specs/aws/ec2/allocate_ipam_pool_cidr"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_AllocateIpamPoolCidr"
---

# AllocateIpamPoolCidr

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/allocate_ipam_pool_cidr
> **spec:implements:** @kind:operation AllocateIpamPoolCidr
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_AllocateIpamPoolCidr.spec.md

Allocate a CIDR from an IPAM pool. The Region you use should be the IPAM pool locale. The locale is the Amazon Web Services Region where this IPAM pool is available for allocations. In IPAM, an allocation is a CIDR assignment from an IPAM pool to another IPAM pool or to a resource. For more information, see Allocate CIDRs in the Amazon VPC IPAM User Guide . This action creates an allocation with strong consistency. The returned CIDR will not overlap with any other allocations from the same pool.

## Input Shape: AllocateIpamPoolCidrRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| AllowedCidrs | Any  # complex shape |  | Include a particular CIDR range that can be returned by the pool. Allowed CIDRs are only allowed if using netmask length |
| Cidr | str |  | The CIDR you would like to allocate from the IPAM pool. Note the following: If there is no DefaultNetmaskLength allocati |
| ClientToken | str |  | A unique, case-sensitive identifier that you provide to ensure the idempotency of the request. For more information, see |
| Description | str |  | A description for the allocation. |
| DisallowedCidrs | Any  # complex shape |  | Exclude a particular CIDR range from being returned by the pool. Disallowed CIDRs are only allowed if using netmask leng |
| DryRun | bool |  | A check for whether you have the required permissions for the action without actually making the request and provides an |
| IpamPoolId | Any  # complex shape | ✓ | The ID of the IPAM pool from which you would like to allocate a CIDR. |
| NetmaskLength | int |  | The netmask length of the CIDR you would like to allocate from the IPAM pool. Note the following: If there is no Default |
| PreviewNextCidr | bool |  | A preview of the next available CIDR in a pool. |

## Output Shape: AllocateIpamPoolCidrResult

- **IpamPoolAllocation** (Any  # complex shape): Information about the allocation created.

## Implementation

```speclang
def allocate_ipam_pool_cidr(store, request: dict) -> dict:
    """Allocate a CIDR from an IPAM pool. The Region you use should be the IPAM pool locale. The locale is the Amazon Web Services Region where this IPAM pool is available for allocations. In IPAM, an alloca"""
    ipam_pool_id = request.get("IpamPoolId", "").strip() if isinstance(request.get("IpamPoolId"), str) else request.get("IpamPoolId")
    if not ipam_pool_id:
        raise ValidationException("IpamPoolId is required")

    # Auto-generated handler — operation not classified as CRUD
    return store.execute("AllocateIpamPoolCidr", request)
```
