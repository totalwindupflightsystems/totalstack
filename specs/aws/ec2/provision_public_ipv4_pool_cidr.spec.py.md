---
id: "@specs/aws/ec2/provision_public_ipv4_pool_cidr"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_ProvisionPublicIpv4PoolCidr"
---

# ProvisionPublicIpv4PoolCidr

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/provision_public_ipv4_pool_cidr
> **spec:implements:** @kind:operation ProvisionPublicIpv4PoolCidr
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_ProvisionPublicIpv4PoolCidr.spec.md

Provision a CIDR to a public IPv4 pool. For more information about IPAM, see What is IPAM? in the Amazon VPC IPAM User Guide .

## Input Shape: ProvisionPublicIpv4PoolCidrRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| DryRun | bool |  | A check for whether you have the required permissions for the action without actually making the request and provides an |
| IpamPoolId | Any  # complex shape | ✓ | The ID of the IPAM pool you would like to use to allocate this CIDR. |
| NetmaskLength | int | ✓ | The netmask length of the CIDR you would like to allocate to the public IPv4 pool. The least specific netmask length you |
| NetworkBorderGroup | str |  | The Availability Zone (AZ) or Local Zone (LZ) network border group that the resource that the IP address is assigned to  |
| PoolId | Any  # complex shape | ✓ | The ID of the public IPv4 pool you would like to use for this CIDR. |

## Output Shape: ProvisionPublicIpv4PoolCidrResult

- **PoolAddressRange** (Any  # complex shape): Information about the address range of the public IPv4 pool.
- **PoolId** (Any  # complex shape): The ID of the pool that you want to provision the CIDR to.

## Implementation

```speclang
def provision_public_ipv4_pool_cidr(store, request: dict) -> dict:
    """Provision a CIDR to a public IPv4 pool. For more information about IPAM, see What is IPAM? in the Amazon VPC IPAM User Guide ."""
    ipam_pool_id = request.get("IpamPoolId", "").strip() if isinstance(request.get("IpamPoolId"), str) else request.get("IpamPoolId")
    if not ipam_pool_id:
        raise ValidationException("IpamPoolId is required")
    netmask_length = request.get("NetmaskLength", "").strip() if isinstance(request.get("NetmaskLength"), str) else request.get("NetmaskLength")
    if not netmask_length:
        raise ValidationException("NetmaskLength is required")
    pool_id = request.get("PoolId", "").strip() if isinstance(request.get("PoolId"), str) else request.get("PoolId")
    if not pool_id:
        raise ValidationException("PoolId is required")

    # Auto-generated handler — operation not classified as CRUD
    return store.execute("ProvisionPublicIpv4PoolCidr", request)
```
