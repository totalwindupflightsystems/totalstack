---
id: "@specs/aws/ec2/delete_transit_gateway_connect_peer"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_DeleteTransitGatewayConnectPeer"
---

# DeleteTransitGatewayConnectPeer

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/delete_transit_gateway_connect_peer
> **spec:implements:** @kind:operation DeleteTransitGatewayConnectPeer
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_DeleteTransitGatewayConnectPeer.spec.md

Deletes the specified Connect peer.

## Input Shape: DeleteTransitGatewayConnectPeerRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| DryRun | bool |  | Checks whether you have the required permissions for the action, without actually making the request, and provides an er |
| TransitGatewayConnectPeerId | Any  # complex shape | ✓ | The ID of the Connect peer. |

## Output Shape: DeleteTransitGatewayConnectPeerResult

- **TransitGatewayConnectPeer** (Any  # complex shape): Information about the deleted Connect peer.

## Implementation

```speclang
def delete_transit_gateway_connect_peer(store, request: dict) -> dict:
    """Deletes the specified Connect peer."""
    transit_gateway_connect_peer_id = request.get("TransitGatewayConnectPeerId", "").strip() if isinstance(request.get("TransitGatewayConnectPeerId"), str) else request.get("TransitGatewayConnectPeerId")

    if not store.transit_gateway_connect_peers(transit_gateway_connect_peer_id):
        raise ResourceNotFoundException(f"Resource transit_gateway_connect_peer_id not found")
    store.delete_transit_gateway_connect_peers(transit_gateway_connect_peer_id)
    return {}
```
