---
id: "@specs/aws/ec2/create_vpn_concentrator"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_CreateVpnConcentrator"
---

# CreateVpnConcentrator

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/create_vpn_concentrator
> **spec:implements:** @kind:operation CreateVpnConcentrator
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_CreateVpnConcentrator.spec.md

Creates a VPN concentrator that aggregates multiple VPN connections to a transit gateway.

## Input Shape: CreateVpnConcentratorRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| DryRun | bool |  | Checks whether you have the required permissions for the action, without actually making the request, and provides an er |
| TagSpecifications | list[Any  # complex shape] |  | The tags to apply to the VPN concentrator during creation. |
| TransitGatewayId | Any  # complex shape |  | The ID of the transit gateway to attach the VPN concentrator to. |
| Type | Any  # complex shape | ✓ | The type of VPN concentrator to create. |

## Output Shape: CreateVpnConcentratorResult

- **VpnConcentrator** (Any  # complex shape): Information about the VPN concentrator.

## Implementation

```speclang
def create_vpn_concentrator(store, request: dict) -> dict:
    """Creates a VPN concentrator that aggregates multiple VPN connections to a transit gateway."""
    type = request.get("Type", "").strip() if isinstance(request.get("Type"), str) else request.get("Type")
    if not type:
        raise ValidationException("Type is required")

    if store.vpn_concentrators(type):
        raise ResourceInUseException(f"Resource type already exists")

    record = {
        "Type": type,
        "TransitGatewayId": transit_gateway_id,
        "TagSpecifications": tag_specifications,
        "DryRun": dry_run,
    }

    store.vpn_concentrators(type, record)

    return {
        "VpnConcentrator": record.get("VpnConcentrator", {}),
    }
```
