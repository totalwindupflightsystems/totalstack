---
id: "@specs/aws/ec2/provision_ipam_pool_cidr"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_ProvisionIpamPoolCidr"
---

# ProvisionIpamPoolCidr

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/provision_ipam_pool_cidr
> **spec:implements:** @kind:operation ProvisionIpamPoolCidr
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_ProvisionIpamPoolCidr.spec.md

Provision a CIDR to an IPAM pool. You can use this action to provision new CIDRs to a top-level pool or to transfer a CIDR from a top-level pool to a pool within it. For more information, see Provision CIDRs to pools in the Amazon VPC IPAM User Guide .

## Input Shape: ProvisionIpamPoolCidrRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| Cidr | str |  | The CIDR you want to assign to the IPAM pool. Either "NetmaskLength" or "Cidr" is required. This value will be null if y |
| CidrAuthorizationContext | Any  # complex shape |  | A signed document that proves that you are authorized to bring a specified IP address range to Amazon using BYOIP. This  |
| ClientToken | str |  | A unique, case-sensitive identifier that you provide to ensure the idempotency of the request. For more information, see |
| DryRun | bool |  | A check for whether you have the required permissions for the action without actually making the request and provides an |
| IpamExternalResourceVerificationTokenId | Any  # complex shape |  | Verification token ID. This option only applies to IPv4 and IPv6 pools in the public scope. |
| IpamPoolId | Any  # complex shape | ✓ | The ID of the IPAM pool to which you want to assign a CIDR. |
| NetmaskLength | int |  | The netmask length of the CIDR you'd like to provision to a pool. Can be used for provisioning Amazon-provided IPv6 CIDR |
| VerificationMethod | Any  # complex shape |  | The method for verifying control of a public IP address range. Defaults to remarks-x509 if not specified. This option on |

## Output Shape: ProvisionIpamPoolCidrResult

- **IpamPoolCidr** (Any  # complex shape): Information about the provisioned CIDR.

## Implementation

```speclang
def provision_ipam_pool_cidr(store, request: dict) -> dict:
    """Provision a CIDR to an IPAM pool. You can use this action to provision new CIDRs to a top-level pool or to transfer a CIDR from a top-level pool to a pool within it. For more information, see Provisio"""
    ipam_pool_id = request.get("IpamPoolId", "").strip() if isinstance(request.get("IpamPoolId"), str) else request.get("IpamPoolId")
    if not ipam_pool_id:
        raise ValidationException("IpamPoolId is required")

    # Auto-generated handler — operation not classified as CRUD
    return store.execute("ProvisionIpamPoolCidr", request)
```
