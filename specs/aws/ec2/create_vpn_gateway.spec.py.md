---
id: "@specs/aws/ec2/create_vpn_gateway"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_CreateVpnGateway"
---

# CreateVpnGateway

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/create_vpn_gateway
> **spec:implements:** @kind:operation CreateVpnGateway
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_CreateVpnGateway.spec.md

Creates a virtual private gateway. A virtual private gateway is the endpoint on the VPC side of your VPN connection. You can create a virtual private gateway before creating the VPC itself. For more information, see Amazon Web Services Site-to-Site VPN in the Amazon Web Services Site-to-Site VPN User Guide .

## Input Shape: CreateVpnGatewayRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| AmazonSideAsn | int |  | A private Autonomous System Number (ASN) for the Amazon side of a BGP session. If you're using a 16-bit ASN, it must be  |
| AvailabilityZone | str |  | The Availability Zone for the virtual private gateway. |
| DryRun | bool |  | Checks whether you have the required permissions for the action, without actually making the request, and provides an er |
| TagSpecifications | list[Any  # complex shape] |  | The tags to apply to the virtual private gateway. |
| Type | Any  # complex shape | ✓ | The type of VPN connection this virtual private gateway supports. |

## Output Shape: CreateVpnGatewayResult

- **VpnGateway** (Any  # complex shape): Information about the virtual private gateway.

## Implementation

```speclang
def create_vpn_gateway(store, request: dict) -> dict:
    """Creates a virtual private gateway. A virtual private gateway is the endpoint on the VPC side of your VPN connection. You can create a virtual private gateway before creating the VPC itself. For more i"""
    type = request.get("Type", "").strip() if isinstance(request.get("Type"), str) else request.get("Type")
    if not type:
        raise ValidationException("Type is required")

    if store.vpn_gateways(type):
        raise ResourceInUseException(f"Resource type already exists")

    record = {
        "AvailabilityZone": availability_zone,
        "Type": type,
        "TagSpecifications": tag_specifications,
        "AmazonSideAsn": amazon_side_asn,
        "DryRun": dry_run,
    }

    store.vpn_gateways(type, record)

    return {
        "VpnGateway": record.get("VpnGateway", {}),
    }
```
