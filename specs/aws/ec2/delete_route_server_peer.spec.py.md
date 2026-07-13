---
id: "@specs/aws/ec2/delete_route_server_peer"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_DeleteRouteServerPeer"
---

# DeleteRouteServerPeer

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/delete_route_server_peer
> **spec:implements:** @kind:operation DeleteRouteServerPeer
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_DeleteRouteServerPeer.spec.md

Deletes the specified BGP peer from a route server. A route server peer is a session between a route server endpoint and the device deployed in Amazon Web Services (such as a firewall appliance or other network security function running on an EC2 instance). The device must meet these requirements: Have an elastic network interface in the VPC Support BGP (Border Gateway Protocol) Can initiate BGP sessions

## Input Shape: DeleteRouteServerPeerRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| DryRun | bool |  | A check for whether you have the required permissions for the action without actually making the request and provides an |
| RouteServerPeerId | Any  # complex shape | ✓ | The ID of the route server peer to delete. |

## Output Shape: DeleteRouteServerPeerResult

- **RouteServerPeer** (Any  # complex shape): Information about the deleted route server peer.

## Implementation

```speclang
def delete_route_server_peer(store, request: dict) -> dict:
    """Deletes the specified BGP peer from a route server. A route server peer is a session between a route server endpoint and the device deployed in Amazon Web Services (such as a firewall appliance or oth"""
    route_server_peer_id = request.get("RouteServerPeerId", "").strip() if isinstance(request.get("RouteServerPeerId"), str) else request.get("RouteServerPeerId")

    if not store.route_server_peers(route_server_peer_id):
        raise ResourceNotFoundException(f"Resource route_server_peer_id not found")
    store.delete_route_server_peers(route_server_peer_id)
    return {}
```
