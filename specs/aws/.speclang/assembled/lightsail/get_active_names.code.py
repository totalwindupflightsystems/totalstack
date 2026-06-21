# spec:trace: aws/lightsail/get_active_names.spec.py.md#implementation
# spec:id: @specs/aws/lightsail/get-active-names
# spec:generated: DO NOT EDIT — edit the spec instead

def get_active_names(store, request: dict) -> dict:
    """Returns the names of all active (not deleted) resources."""

    # Auto-generated get handler — verify resource key
    return store.get_resource(request)

