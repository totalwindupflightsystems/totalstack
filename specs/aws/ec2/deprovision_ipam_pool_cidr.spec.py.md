---
id: "@specs/aws/ec2/deprovision_ipam_pool_cidr"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_DeprovisionIpamPoolCidr"
---

# DeprovisionIpamPoolCidr

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/deprovision_ipam_pool_cidr
> **spec:implements:** @kind:operation DeprovisionIpamPoolCidr
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_DeprovisionIpamPoolCidr.spec.md

Deprovision a CIDR provisioned from an IPAM pool. If you deprovision a CIDR from a pool that has a source pool, the CIDR is recycled back into the source pool. For more information, see Deprovision pool CIDRs in the Amazon VPC IPAM User Guide .

## Input Shape: DeprovisionIpamPoolCidrRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| Cidr | str |  | The CIDR which you want to deprovision from the pool. |
| DryRun | bool |  | A check for whether you have the required permissions for the action without actually making the request and provides an |
| IpamPoolId | Any  # complex shape | ✓ | The ID of the pool that has the CIDR you want to deprovision. |

## Output Shape: DeprovisionIpamPoolCidrResult

- **IpamPoolCidr** (Any  # complex shape): The deprovisioned pool CIDR.

## Implementation

```speclang
def deprovision_ipam_pool_cidr(store, request: dict) -> dict:
    """Deprovision a CIDR provisioned from an IPAM pool. If you deprovision a CIDR from a pool that has a source pool, the CIDR is recycled back into the source pool. For more information, see Deprovision po"""
    ipam_pool_id = request.get("IpamPoolId", "").strip() if isinstance(request.get("IpamPoolId"), str) else request.get("IpamPoolId")
    if not ipam_pool_id:
        raise ValidationException("IpamPoolId is required")

    # Auto-generated handler — operation not classified as CRUD
    return store.execute("DeprovisionIpamPoolCidr", request)
```
