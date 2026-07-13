---
id: "@specs/aws/ec2/advertise_byoip_cidr"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_AdvertiseByoipCidr"
---

# AdvertiseByoipCidr

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/advertise_byoip_cidr
> **spec:implements:** @kind:operation AdvertiseByoipCidr
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_AdvertiseByoipCidr.spec.md

Advertises an IPv4 or IPv6 address range that is provisioned for use with your Amazon Web Services resources through bring your own IP addresses (BYOIP). You can perform this operation at most once every 10 seconds, even if you specify different address ranges each time. We recommend that you stop advertising the BYOIP CIDR from other locations when you advertise it from Amazon Web Services. To minimize down time, you can configure your Amazon Web Services resources to use an address from a BYOIP CIDR before it is advertised, and then simultaneously stop advertising it from the current location and start advertising it through Amazon Web Services. It can take a few minutes before traffic to the specified addresses starts routing to Amazon Web Services because of BGP propagation delays.

## Input Shape: AdvertiseByoipCidrRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| Asn | str |  | The public 2-byte or 4-byte ASN that you want to advertise. |
| Cidr | str | ✓ | The address range, in CIDR notation. This must be the exact range that you provisioned. You can't advertise only a porti |
| DryRun | bool |  | Checks whether you have the required permissions for the action, without actually making the request, and provides an er |
| NetworkBorderGroup | str |  | If you have Local Zones enabled, you can choose a network border group for Local Zones when you provision and advertise  |

## Output Shape: AdvertiseByoipCidrResult

- **ByoipCidr** (Any  # complex shape): Information about the address range.

## Implementation

```speclang
def advertise_byoip_cidr(store, request: dict) -> dict:
    """Advertises an IPv4 or IPv6 address range that is provisioned for use with your Amazon Web Services resources through bring your own IP addresses (BYOIP). You can perform this operation at most once ev"""
    cidr = request.get("Cidr", "").strip() if isinstance(request.get("Cidr"), str) else request.get("Cidr")
    if not cidr:
        raise ValidationException("Cidr is required")

    # Auto-generated handler — operation not classified as CRUD
    return store.execute("AdvertiseByoipCidr", request)
```
