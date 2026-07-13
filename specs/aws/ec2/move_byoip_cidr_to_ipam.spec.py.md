---
id: "@specs/aws/ec2/move_byoip_cidr_to_ipam"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_MoveByoipCidrToIpam"
---

# MoveByoipCidrToIpam

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/move_byoip_cidr_to_ipam
> **spec:implements:** @kind:operation MoveByoipCidrToIpam
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_MoveByoipCidrToIpam.spec.md

Move a BYOIPv4 CIDR to IPAM from a public IPv4 pool. If you already have a BYOIPv4 CIDR with Amazon Web Services, you can move the CIDR to IPAM from a public IPv4 pool. You cannot move an IPv6 CIDR to IPAM. If you are bringing a new IP address to Amazon Web Services for the first time, complete the steps in Tutorial: BYOIP address CIDRs to IPAM .

## Input Shape: MoveByoipCidrToIpamRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| Cidr | str | ✓ | The BYOIP CIDR. |
| DryRun | bool |  | A check for whether you have the required permissions for the action without actually making the request and provides an |
| IpamPoolId | Any  # complex shape | ✓ | The IPAM pool ID. |
| IpamPoolOwner | str | ✓ | The Amazon Web Services account ID of the owner of the IPAM pool. |

## Output Shape: MoveByoipCidrToIpamResult

- **ByoipCidr** (Any  # complex shape): The BYOIP CIDR.

## Implementation

```speclang
def move_byoip_cidr_to_ipam(store, request: dict) -> dict:
    """Move a BYOIPv4 CIDR to IPAM from a public IPv4 pool. If you already have a BYOIPv4 CIDR with Amazon Web Services, you can move the CIDR to IPAM from a public IPv4 pool. You cannot move an IPv6 CIDR to"""
    cidr = request.get("Cidr", "").strip() if isinstance(request.get("Cidr"), str) else request.get("Cidr")
    if not cidr:
        raise ValidationException("Cidr is required")
    ipam_pool_id = request.get("IpamPoolId", "").strip() if isinstance(request.get("IpamPoolId"), str) else request.get("IpamPoolId")
    if not ipam_pool_id:
        raise ValidationException("IpamPoolId is required")
    ipam_pool_owner = request.get("IpamPoolOwner", "").strip() if isinstance(request.get("IpamPoolOwner"), str) else request.get("IpamPoolOwner")
    if not ipam_pool_owner:
        raise ValidationException("IpamPoolOwner is required")

    # Auto-generated handler — operation not classified as CRUD
    return store.execute("MoveByoipCidrToIpam", request)
```
