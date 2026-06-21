# spec:trace: aws/lightsail/get_instances.spec.py.md#implementation
# spec:id: @specs/aws/lightsail/get-instances
# spec:generated: DO NOT EDIT — edit the spec instead

def get_instances(store, request: dict) -> dict:
    """Returns information about all Amazon Lightsail virtual private servers, or instances ."""

    # Auto-generated get handler — verify resource key
    return store.get_resource(request)

