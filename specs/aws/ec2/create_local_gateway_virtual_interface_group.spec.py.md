---
id: "@specs/aws/ec2/create_local_gateway_virtual_interface_group"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_CreateLocalGatewayVirtualInterfaceGroup"
---

# CreateLocalGatewayVirtualInterfaceGroup

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/create_local_gateway_virtual_interface_group
> **spec:implements:** @kind:operation CreateLocalGatewayVirtualInterfaceGroup
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_CreateLocalGatewayVirtualInterfaceGroup.spec.md

Create a local gateway virtual interface group.

## Input Shape: CreateLocalGatewayVirtualInterfaceGroupRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| DryRun | bool |  | Checks whether you have the required permissions for the action, without actually making the request, and provides an er |
| LocalBgpAsn | int |  | The Autonomous System Number(ASN) for the local Border Gateway Protocol (BGP). |
| LocalBgpAsnExtended | int |  | The extended 32-bit ASN for the local BGP configuration. |
| LocalGatewayId | Any  # complex shape | ✓ | The ID of the local gateway. |
| TagSpecifications | list[Any  # complex shape] |  | The tags to apply to the local gateway virtual interface group when the resource is being created. |

## Output Shape: CreateLocalGatewayVirtualInterfaceGroupResult

- **LocalGatewayVirtualInterfaceGroup** (Any  # complex shape): Information about the created local gateway virtual interface group.

## Implementation

```speclang
def create_local_gateway_virtual_interface_group(store, request: dict) -> dict:
    """Create a local gateway virtual interface group."""
    local_gateway_id = request.get("LocalGatewayId", "").strip() if isinstance(request.get("LocalGatewayId"), str) else request.get("LocalGatewayId")
    if not local_gateway_id:
        raise ValidationException("LocalGatewayId is required")

    if store.local_gateway_virtual_interface_groups(local_gateway_id):
        raise ResourceInUseException(f"Resource local_gateway_id already exists")

    record = {
        "LocalGatewayId": local_gateway_id,
        "LocalBgpAsn": local_bgp_asn,
        "LocalBgpAsnExtended": local_bgp_asn_extended,
        "TagSpecifications": tag_specifications,
        "DryRun": dry_run,
    }

    store.local_gateway_virtual_interface_groups(local_gateway_id, record)

    return {
        "LocalGatewayVirtualInterfaceGroup": record.get("LocalGatewayVirtualInterfaceGroup", {}),
    }
```
