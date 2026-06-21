# spec:trace: aws/lightsail/get_static_ips.spec.py.md#implementation
# spec:id: @specs/aws/lightsail/get-static-ips
# spec:generated: DO NOT EDIT — edit the spec instead

def get_static_ips(store, request: dict) -> dict:
    """Returns information about all static IPs in the user's account."""

    # Auto-generated get handler — verify resource key
    return store.get_resource(request)

