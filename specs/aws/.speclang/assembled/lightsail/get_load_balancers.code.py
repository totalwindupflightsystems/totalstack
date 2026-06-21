# spec:trace: aws/lightsail/get_load_balancers.spec.py.md#implementation
# spec:id: @specs/aws/lightsail/get-load-balancers
# spec:generated: DO NOT EDIT — edit the spec instead

def get_load_balancers(store, request: dict) -> dict:
    """Returns information about all load balancers in an account."""

    # Auto-generated get handler — verify resource key
    return store.get_resource(request)

