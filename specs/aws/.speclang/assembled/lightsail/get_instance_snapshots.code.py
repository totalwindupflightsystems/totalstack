# spec:trace: aws/lightsail/get_instance_snapshots.spec.py.md#implementation
# spec:id: @specs/aws/lightsail/get-instance-snapshots
# spec:generated: DO NOT EDIT — edit the spec instead

def get_instance_snapshots(store, request: dict) -> dict:
    """Returns all instance snapshots for the user's account."""

    # Auto-generated get handler — verify resource key
    return store.get_resource(request)

