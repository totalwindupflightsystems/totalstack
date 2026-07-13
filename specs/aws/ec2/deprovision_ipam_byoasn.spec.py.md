---
id: "@specs/aws/ec2/deprovision_ipam_byoasn"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_DeprovisionIpamByoasn"
---

# DeprovisionIpamByoasn

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/deprovision_ipam_byoasn
> **spec:implements:** @kind:operation DeprovisionIpamByoasn
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_DeprovisionIpamByoasn.spec.md

Deprovisions your Autonomous System Number (ASN) from your Amazon Web Services account. This action can only be called after any BYOIP CIDR associations are removed from your Amazon Web Services account with DisassociateIpamByoasn . For more information, see Tutorial: Bring your ASN to IPAM in the Amazon VPC IPAM guide .

## Input Shape: DeprovisionIpamByoasnRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| Asn | str | ✓ | An ASN. |
| DryRun | bool |  | Checks whether you have the required permissions for the action, without actually making the request, and provides an er |
| IpamId | Any  # complex shape | ✓ | The IPAM ID. |

## Output Shape: DeprovisionIpamByoasnResult

- **Byoasn** (Any  # complex shape): An ASN and BYOIP CIDR association.

## Implementation

```speclang
def deprovision_ipam_byoasn(store, request: dict) -> dict:
    """Deprovisions your Autonomous System Number (ASN) from your Amazon Web Services account. This action can only be called after any BYOIP CIDR associations are removed from your Amazon Web Services accou"""
    asn = request.get("Asn", "").strip() if isinstance(request.get("Asn"), str) else request.get("Asn")
    if not asn:
        raise ValidationException("Asn is required")
    ipam_id = request.get("IpamId", "").strip() if isinstance(request.get("IpamId"), str) else request.get("IpamId")
    if not ipam_id:
        raise ValidationException("IpamId is required")

    # Auto-generated handler — operation not classified as CRUD
    return store.execute("DeprovisionIpamByoasn", request)
```
