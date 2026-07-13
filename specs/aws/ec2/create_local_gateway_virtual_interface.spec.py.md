---
id: "@specs/aws/ec2/create_local_gateway_virtual_interface"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_CreateLocalGatewayVirtualInterface"
---

# CreateLocalGatewayVirtualInterface

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/create_local_gateway_virtual_interface
> **spec:implements:** @kind:operation CreateLocalGatewayVirtualInterface
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_CreateLocalGatewayVirtualInterface.spec.md

Create a virtual interface for a local gateway.

## Input Shape: CreateLocalGatewayVirtualInterfaceRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| DryRun | bool |  | Checks whether you have the required permissions for the action, without actually making the request, and provides an er |
| LocalAddress | str | ✓ | The IP address assigned to the local gateway virtual interface on the Outpost side. Only IPv4 is supported. |
| LocalGatewayVirtualInterfaceGroupId | Any  # complex shape | ✓ | The ID of the local gateway virtual interface group. |
| OutpostLagId | Any  # complex shape | ✓ | References the Link Aggregation Group (LAG) that connects the Outpost to on-premises network devices. |
| PeerAddress | str | ✓ | The peer IP address for the local gateway virtual interface. Only IPv4 is supported. |
| PeerBgpAsn | int |  | The Autonomous System Number (ASN) of the Border Gateway Protocol (BGP) peer. |
| PeerBgpAsnExtended | int |  | The extended 32-bit ASN of the BGP peer for use with larger ASN values. |
| TagSpecifications | list[Any  # complex shape] |  | The tags to apply to a resource when the local gateway virtual interface is being created. |
| Vlan | int | ✓ | The virtual local area network (VLAN) used for the local gateway virtual interface. |

## Output Shape: CreateLocalGatewayVirtualInterfaceResult

- **LocalGatewayVirtualInterface** (Any  # complex shape): Information about the local gateway virtual interface.

## Implementation

```speclang
def create_local_gateway_virtual_interface(store, request: dict) -> dict:
    """Create a virtual interface for a local gateway."""
    local_address = request.get("LocalAddress", "").strip() if isinstance(request.get("LocalAddress"), str) else request.get("LocalAddress")
    if not local_address:
        raise ValidationException("LocalAddress is required")
    local_gateway_virtual_interface_group_id = request.get("LocalGatewayVirtualInterfaceGroupId", "").strip() if isinstance(request.get("LocalGatewayVirtualInterfaceGroupId"), str) else request.get("LocalGatewayVirtualInterfaceGroupId")
    if not local_gateway_virtual_interface_group_id:
        raise ValidationException("LocalGatewayVirtualInterfaceGroupId is required")
    outpost_lag_id = request.get("OutpostLagId", "").strip() if isinstance(request.get("OutpostLagId"), str) else request.get("OutpostLagId")
    if not outpost_lag_id:
        raise ValidationException("OutpostLagId is required")
    peer_address = request.get("PeerAddress", "").strip() if isinstance(request.get("PeerAddress"), str) else request.get("PeerAddress")
    if not peer_address:
        raise ValidationException("PeerAddress is required")
    vlan = request.get("Vlan", "").strip() if isinstance(request.get("Vlan"), str) else request.get("Vlan")
    if not vlan:
        raise ValidationException("Vlan is required")

    if store.local_gateway_virtual_interfaces(outpost_lag_id):
        raise ResourceInUseException(f"Resource outpost_lag_id already exists")

    record = {
        "LocalGatewayVirtualInterfaceGroupId": local_gateway_virtual_interface_group_id,
        "OutpostLagId": outpost_lag_id,
        "Vlan": vlan,
        "LocalAddress": local_address,
        "PeerAddress": peer_address,
        "PeerBgpAsn": peer_bgp_asn,
        "TagSpecifications": tag_specifications,
        "DryRun": dry_run,
        "PeerBgpAsnExtended": peer_bgp_asn_extended,
    }

    store.local_gateway_virtual_interfaces(outpost_lag_id, record)

    return {
        "LocalGatewayVirtualInterface": record.get("LocalGatewayVirtualInterface", {}),
    }
```
