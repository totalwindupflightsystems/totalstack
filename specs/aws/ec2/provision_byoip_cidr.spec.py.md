---
id: "@specs/aws/ec2/provision_byoip_cidr"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_ProvisionByoipCidr"
---

# ProvisionByoipCidr

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/provision_byoip_cidr
> **spec:implements:** @kind:operation ProvisionByoipCidr
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_ProvisionByoipCidr.spec.md

Provisions an IPv4 or IPv6 address range for use with your Amazon Web Services resources through bring your own IP addresses (BYOIP) and creates a corresponding address pool. After the address range is provisioned, it is ready to be advertised. Amazon Web Services verifies that you own the address range and are authorized to advertise it. You must ensure that the address range is registered to you and that you created an RPKI ROA to authorize Amazon ASNs 16509 and 14618 to advertise the address range. For more information, see Bring your own IP addresses (BYOIP) in the Amazon EC2 User Guide . Provisioning an address range is an asynchronous operation, so the call returns immediately, but the address range is not ready to use until its status changes from pending-provision to provisioned . For more information, see Onboard your address range .

## Input Shape: ProvisionByoipCidrRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| Cidr | str | ✓ | The public IPv4 or IPv6 address range, in CIDR notation. The most specific IPv4 prefix that you can specify is /24. The  |
| CidrAuthorizationContext | Any  # complex shape |  | A signed document that proves that you are authorized to bring the specified IP address range to Amazon using BYOIP. |
| Description | str |  | A description for the address range and the address pool. |
| DryRun | bool |  | Checks whether you have the required permissions for the action, without actually making the request, and provides an er |
| MultiRegion | bool |  | Reserved. |
| NetworkBorderGroup | str |  | If you have Local Zones enabled, you can choose a network border group for Local Zones when you provision and advertise  |
| PoolTagSpecifications | list[Any  # complex shape] |  | The tags to apply to the address pool. |
| PubliclyAdvertisable | bool |  | (IPv6 only) Indicate whether the address range will be publicly advertised to the internet. Default: true |

## Output Shape: ProvisionByoipCidrResult

- **ByoipCidr** (Any  # complex shape): Information about the address range.

## Implementation

```speclang
def provision_byoip_cidr(store, request: dict) -> dict:
    """Provisions an IPv4 or IPv6 address range for use with your Amazon Web Services resources through bring your own IP addresses (BYOIP) and creates a corresponding address pool. After the address range i"""
    cidr = request.get("Cidr", "").strip() if isinstance(request.get("Cidr"), str) else request.get("Cidr")
    if not cidr:
        raise ValidationException("Cidr is required")

    # Auto-generated handler — operation not classified as CRUD
    return store.execute("ProvisionByoipCidr", request)
```
