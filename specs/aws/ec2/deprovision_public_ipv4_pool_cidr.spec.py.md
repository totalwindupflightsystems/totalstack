---
id: "@specs/aws/ec2/deprovision_public_ipv4_pool_cidr"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_DeprovisionPublicIpv4PoolCidr"
---

# DeprovisionPublicIpv4PoolCidr

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/deprovision_public_ipv4_pool_cidr
> **spec:implements:** @kind:operation DeprovisionPublicIpv4PoolCidr
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_DeprovisionPublicIpv4PoolCidr.spec.md

Deprovision a CIDR from a public IPv4 pool.

## Input Shape: DeprovisionPublicIpv4PoolCidrRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| Cidr | str | ✓ | The CIDR you want to deprovision from the pool. |
| DryRun | bool |  | A check for whether you have the required permissions for the action without actually making the request and provides an |
| PoolId | Any  # complex shape | ✓ | The ID of the pool that you want to deprovision the CIDR from. |

## Output Shape: DeprovisionPublicIpv4PoolCidrResult

- **DeprovisionedAddresses** (Any  # complex shape): The deprovisioned CIDRs.
- **PoolId** (Any  # complex shape): The ID of the pool that you deprovisioned the CIDR from.

## Implementation

```speclang
def deprovision_public_ipv4_pool_cidr(store, request: dict) -> dict:
    """Deprovision a CIDR from a public IPv4 pool."""
    cidr = request.get("Cidr", "").strip() if isinstance(request.get("Cidr"), str) else request.get("Cidr")
    if not cidr:
        raise ValidationException("Cidr is required")
    pool_id = request.get("PoolId", "").strip() if isinstance(request.get("PoolId"), str) else request.get("PoolId")
    if not pool_id:
        raise ValidationException("PoolId is required")

    # Auto-generated handler — operation not classified as CRUD
    return store.execute("DeprovisionPublicIpv4PoolCidr", request)
```
