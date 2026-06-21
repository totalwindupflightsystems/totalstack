# spec:trace: aws/lightsail/get_key_pairs.spec.py.md#implementation
# spec:id: @specs/aws/lightsail/get-key-pairs
# spec:generated: DO NOT EDIT — edit the spec instead

def get_key_pairs(store, request: dict) -> dict:
    """Returns information about all key pairs in the user's account."""

    # Auto-generated get handler — verify resource key
    return store.get_resource(request)

