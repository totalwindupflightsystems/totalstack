# spec:trace: aws/lightsail/get_regions.spec.py.md#implementation
# spec:id: @specs/aws/lightsail/get-regions
# spec:generated: DO NOT EDIT — edit the spec instead

def get_regions(store, request: dict) -> dict:
    """Returns a list of all valid regions for Amazon Lightsail. Use the include availability zones parameter to also return the Availability Zones in a region."""

    # Auto-generated get handler — verify resource key
    return store.get_resource(request)

