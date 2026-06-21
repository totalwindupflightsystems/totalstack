# spec:trace: aws/lightsail/is_vpc_peered.spec.py.md#implementation
# spec:id: @specs/aws/lightsail/is-vpc-peered
# spec:generated: DO NOT EDIT — edit the spec instead

def is_vpc_peered(store, request: dict) -> dict:
    """Returns a Boolean value indicating whether your Lightsail VPC is peered."""

    # Auto-generated handler — operation not classified as CRUD
    return store.execute("IsVpcPeered", request)

