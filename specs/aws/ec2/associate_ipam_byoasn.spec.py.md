---
id: "@specs/aws/ec2/associate_ipam_byoasn"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_AssociateIpamByoasn"
---

# AssociateIpamByoasn

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/associate_ipam_byoasn
> **spec:implements:** @kind:operation AssociateIpamByoasn
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_AssociateIpamByoasn.spec.md

Associates your Autonomous System Number (ASN) with a BYOIP CIDR that you own in the same Amazon Web Services Region. For more information, see Tutorial: Bring your ASN to IPAM in the Amazon VPC IPAM guide . After the association succeeds, the ASN is eligible for advertisement. You can view the association with DescribeByoipCidrs . You can advertise the CIDR with AdvertiseByoipCidr .

## Input Shape: AssociateIpamByoasnRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| Asn | str | ✓ | A public 2-byte or 4-byte ASN. |
| Cidr | str | ✓ | The BYOIP CIDR you want to associate with an ASN. |
| DryRun | bool |  | Checks whether you have the required permissions for the action, without actually making the request, and provides an er |

## Output Shape: AssociateIpamByoasnResult

- **AsnAssociation** (Any  # complex shape): The ASN and BYOIP CIDR association.

## Implementation

```speclang
def associate_ipam_byoasn(store, request: dict) -> dict:
    """Associates your Autonomous System Number (ASN) with a BYOIP CIDR that you own in the same Amazon Web Services Region. For more information, see Tutorial: Bring your ASN to IPAM in the Amazon VPC IPAM """
    asn = request.get("Asn", "").strip() if isinstance(request.get("Asn"), str) else request.get("Asn")
    if not asn:
        raise ValidationException("Asn is required")
    cidr = request.get("Cidr", "").strip() if isinstance(request.get("Cidr"), str) else request.get("Cidr")
    if not cidr:
        raise ValidationException("Cidr is required")

    # Auto-generated handler — operation not classified as CRUD
    return store.execute("AssociateIpamByoasn", request)
```
