---
id: "@specs/aws/ec2/disassociate_ipam_byoasn"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_DisassociateIpamByoasn"
---

# DisassociateIpamByoasn

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/disassociate_ipam_byoasn
> **spec:implements:** @kind:operation DisassociateIpamByoasn
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_DisassociateIpamByoasn.spec.md

Remove the association between your Autonomous System Number (ASN) and your BYOIP CIDR. You may want to use this action to disassociate an ASN from a CIDR or if you want to swap ASNs. For more information, see Tutorial: Bring your ASN to IPAM in the Amazon VPC IPAM guide .

## Input Shape: DisassociateIpamByoasnRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| Asn | str | ✓ | A public 2-byte or 4-byte ASN. |
| Cidr | str | ✓ | A BYOIP CIDR. |
| DryRun | bool |  | Checks whether you have the required permissions for the action, without actually making the request, and provides an er |

## Output Shape: DisassociateIpamByoasnResult

- **AsnAssociation** (Any  # complex shape): An ASN and BYOIP CIDR association.

## Implementation

```speclang
def disassociate_ipam_byoasn(store, request: dict) -> dict:
    """Remove the association between your Autonomous System Number (ASN) and your BYOIP CIDR. You may want to use this action to disassociate an ASN from a CIDR or if you want to swap ASNs. For more informa"""
    asn = request.get("Asn", "").strip() if isinstance(request.get("Asn"), str) else request.get("Asn")
    if not asn:
        raise ValidationException("Asn is required")
    cidr = request.get("Cidr", "").strip() if isinstance(request.get("Cidr"), str) else request.get("Cidr")
    if not cidr:
        raise ValidationException("Cidr is required")

    # Auto-generated handler — operation not classified as CRUD
    return store.execute("DisassociateIpamByoasn", request)
```
