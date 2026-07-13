---
id: "@specs/aws/ec2/create_transit_gateway_connect_peer"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_CreateTransitGatewayConnectPeer"
---

# CreateTransitGatewayConnectPeer

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/create_transit_gateway_connect_peer
> **spec:implements:** @kind:operation CreateTransitGatewayConnectPeer
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_CreateTransitGatewayConnectPeer.spec.md

Creates a Connect peer for a specified transit gateway Connect attachment between a transit gateway and an appliance. The peer address and transit gateway address must be the same IP address family (IPv4 or IPv6). For more information, see Connect peers in the Amazon Web Services Transit Gateways Guide .

## Input Shape: CreateTransitGatewayConnectPeerRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| BgpOptions | Any  # complex shape |  | The BGP options for the Connect peer. |
| DryRun | bool |  | Checks whether you have the required permissions for the action, without actually making the request, and provides an er |
| InsideCidrBlocks | list[str] | ✓ | The range of inside IP addresses that are used for BGP peering. You must specify a size /29 IPv4 CIDR block from the 169 |
| PeerAddress | str | ✓ | The peer IP address (GRE outer IP address) on the appliance side of the Connect peer. |
| TagSpecifications | list[Any  # complex shape] |  | The tags to apply to the Connect peer. |
| TransitGatewayAddress | str |  | The peer IP address (GRE outer IP address) on the transit gateway side of the Connect peer, which must be specified from |
| TransitGatewayAttachmentId | Any  # complex shape | ✓ | The ID of the Connect attachment. |

## Output Shape: CreateTransitGatewayConnectPeerResult

- **TransitGatewayConnectPeer** (Any  # complex shape): Information about the Connect peer.

## Implementation

```speclang
def create_transit_gateway_connect_peer(store, request: dict) -> dict:
    """Creates a Connect peer for a specified transit gateway Connect attachment between a transit gateway and an appliance. The peer address and transit gateway address must be the same IP address family (I"""
    inside_cidr_blocks = request.get("InsideCidrBlocks", "").strip() if isinstance(request.get("InsideCidrBlocks"), str) else request.get("InsideCidrBlocks")
    if not inside_cidr_blocks:
        raise ValidationException("InsideCidrBlocks is required")
    peer_address = request.get("PeerAddress", "").strip() if isinstance(request.get("PeerAddress"), str) else request.get("PeerAddress")
    if not peer_address:
        raise ValidationException("PeerAddress is required")
    transit_gateway_attachment_id = request.get("TransitGatewayAttachmentId", "").strip() if isinstance(request.get("TransitGatewayAttachmentId"), str) else request.get("TransitGatewayAttachmentId")
    if not transit_gateway_attachment_id:
        raise ValidationException("TransitGatewayAttachmentId is required")

    if store.transit_gateway_connect_peers(transit_gateway_attachment_id):
        raise ResourceInUseException(f"Resource transit_gateway_attachment_id already exists")

    record = {
        "TransitGatewayAttachmentId": transit_gateway_attachment_id,
        "TransitGatewayAddress": transit_gateway_address,
        "PeerAddress": peer_address,
        "BgpOptions": bgp_options,
        "InsideCidrBlocks": inside_cidr_blocks,
        "TagSpecifications": tag_specifications,
        "DryRun": dry_run,
    }

    store.transit_gateway_connect_peers(transit_gateway_attachment_id, record)

    return {
        "TransitGatewayConnectPeer": record.get("TransitGatewayConnectPeer", {}),
    }
```
