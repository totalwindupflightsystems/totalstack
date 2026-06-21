# spec:trace: aws/lightsail/get_distributions.spec.py.md#implementation
# spec:id: @specs/aws/lightsail/get-distributions
# spec:generated: DO NOT EDIT — edit the spec instead

def get_distributions(store, request: dict) -> dict:
    """Returns information about one or more of your Amazon Lightsail content delivery network (CDN) distributions."""

    # Auto-generated get handler — verify resource key
    return store.get_resource(request)

