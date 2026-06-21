# spec:trace: aws/lightsail/unpeer_vpc.spec.py.md#implementation
# spec:id: @specs/aws/lightsail/unpeer-vpc
# spec:generated: DO NOT EDIT — edit the spec instead

def unpeer_vpc(store, request: dict) -> dict:
    """Unpeers the Lightsail VPC from the user's default VPC."""

    # Auto-generated handler — operation not classified as CRUD
    return store.execute("UnpeerVpc", request)

