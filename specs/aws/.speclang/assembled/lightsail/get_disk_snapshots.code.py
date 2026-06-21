# spec:trace: aws/lightsail/get_disk_snapshots.spec.py.md#implementation
# spec:id: @specs/aws/lightsail/get-disk-snapshots
# spec:generated: DO NOT EDIT — edit the spec instead

def get_disk_snapshots(store, request: dict) -> dict:
    """Returns information about all block storage disk snapshots in your AWS account and region."""

    # Auto-generated get handler — verify resource key
    return store.get_resource(request)

