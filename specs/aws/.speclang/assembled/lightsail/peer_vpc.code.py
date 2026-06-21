# spec:trace: aws/lightsail/peer_vpc.spec.py.md#implementation
# spec:id: @specs/aws/lightsail/peer-vpc
# spec:generated: DO NOT EDIT — edit the spec instead

def peer_vpc(store, request: dict) -> dict:
    """Peers the Lightsail VPC with the user's default VPC."""

    # Auto-generated handler — operation not classified as CRUD
    return store.execute("PeerVpc", request)

