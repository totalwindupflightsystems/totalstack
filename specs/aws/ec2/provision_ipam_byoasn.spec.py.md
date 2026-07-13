---
id: "@specs/aws/ec2/provision_ipam_byoasn"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_ProvisionIpamByoasn"
---

# ProvisionIpamByoasn

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/provision_ipam_byoasn
> **spec:implements:** @kind:operation ProvisionIpamByoasn
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_ProvisionIpamByoasn.spec.md

Provisions your Autonomous System Number (ASN) for use in your Amazon Web Services account. This action requires authorization context for Amazon to bring the ASN to an Amazon Web Services account. For more information, see Tutorial: Bring your ASN to IPAM in the Amazon VPC IPAM guide .

## Input Shape: ProvisionIpamByoasnRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| Asn | str | ✓ | A public 2-byte or 4-byte ASN. |
| AsnAuthorizationContext | Any  # complex shape | ✓ | An ASN authorization context. |
| DryRun | bool |  | Checks whether you have the required permissions for the action, without actually making the request, and provides an er |
| IpamId | Any  # complex shape | ✓ | An IPAM ID. |

## Output Shape: ProvisionIpamByoasnResult

- **Byoasn** (Any  # complex shape): An ASN and BYOIP CIDR association.

## Implementation

```speclang
def provision_ipam_byoasn(store, request: dict) -> dict:
    """Provisions your Autonomous System Number (ASN) for use in your Amazon Web Services account. This action requires authorization context for Amazon to bring the ASN to an Amazon Web Services account. Fo"""
    asn = request.get("Asn", "").strip() if isinstance(request.get("Asn"), str) else request.get("Asn")
    if not asn:
        raise ValidationException("Asn is required")
    asn_authorization_context = request.get("AsnAuthorizationContext", "").strip() if isinstance(request.get("AsnAuthorizationContext"), str) else request.get("AsnAuthorizationContext")
    if not asn_authorization_context:
        raise ValidationException("AsnAuthorizationContext is required")
    ipam_id = request.get("IpamId", "").strip() if isinstance(request.get("IpamId"), str) else request.get("IpamId")
    if not ipam_id:
        raise ValidationException("IpamId is required")

    # Auto-generated handler — operation not classified as CRUD
    return store.execute("ProvisionIpamByoasn", request)
```
