---
id: "@specs/aws/ec2/create_route_server_peer"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_CreateRouteServerPeer"
---

# CreateRouteServerPeer

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/create_route_server_peer
> **spec:implements:** @kind:operation CreateRouteServerPeer
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_CreateRouteServerPeer.spec.md

Creates a new BGP peer for a specified route server endpoint. A route server peer is a session between a route server endpoint and the device deployed in Amazon Web Services (such as a firewall appliance or other network security function running on an EC2 instance). The device must meet these requirements: Have an elastic network interface in the VPC Support BGP (Border Gateway Protocol) Can initiate BGP sessions For more information see Dynamic routing in your VPC with VPC Route Server in the Amazon VPC User Guide .

## Input Shape: CreateRouteServerPeerRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| BgpOptions | Any  # complex shape | ✓ | The BGP options for the peer, including ASN (Autonomous System Number) and BFD (Bidrectional Forwarding Detection) setti |
| DryRun | bool |  | A check for whether you have the required permissions for the action without actually making the request and provides an |
| PeerAddress | str | ✓ | The IPv4 address of the peer device. |
| RouteServerEndpointId | Any  # complex shape | ✓ | The ID of the route server endpoint for which to create a peer. |
| TagSpecifications | list[Any  # complex shape] |  | The tags to apply to the route server peer during creation. |

## Output Shape: CreateRouteServerPeerResult

- **RouteServerPeer** (Any  # complex shape): Information about the created route server peer.

## Implementation

```speclang
def create_route_server_peer(store, request: dict) -> dict:
    """Creates a new BGP peer for a specified route server endpoint. A route server peer is a session between a route server endpoint and the device deployed in Amazon Web Services (such as a firewall applia"""
    bgp_options = request.get("BgpOptions", "").strip() if isinstance(request.get("BgpOptions"), str) else request.get("BgpOptions")
    if not bgp_options:
        raise ValidationException("BgpOptions is required")
    peer_address = request.get("PeerAddress", "").strip() if isinstance(request.get("PeerAddress"), str) else request.get("PeerAddress")
    if not peer_address:
        raise ValidationException("PeerAddress is required")
    route_server_endpoint_id = request.get("RouteServerEndpointId", "").strip() if isinstance(request.get("RouteServerEndpointId"), str) else request.get("RouteServerEndpointId")
    if not route_server_endpoint_id:
        raise ValidationException("RouteServerEndpointId is required")

    if store.route_server_peers(route_server_endpoint_id):
        raise ResourceInUseException(f"Resource route_server_endpoint_id already exists")

    record = {
        "RouteServerEndpointId": route_server_endpoint_id,
        "PeerAddress": peer_address,
        "BgpOptions": bgp_options,
        "DryRun": dry_run,
        "TagSpecifications": tag_specifications,
    }

    store.route_server_peers(route_server_endpoint_id, record)

    return {
        "RouteServerPeer": record.get("RouteServerPeer", {}),
    }
```
