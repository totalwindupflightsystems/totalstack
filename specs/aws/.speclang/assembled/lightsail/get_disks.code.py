# spec:trace: aws/lightsail/get_disks.spec.py.md#implementation
# spec:id: @specs/aws/lightsail/get-disks
# spec:generated: DO NOT EDIT — edit the spec instead

def get_disks(store, request: dict) -> dict:
    """Returns information about all block storage disks in your AWS account and region."""

    # Auto-generated get handler — verify resource key
    return store.get_resource(request)

