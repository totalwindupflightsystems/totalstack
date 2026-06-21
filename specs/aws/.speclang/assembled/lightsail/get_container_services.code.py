# spec:trace: aws/lightsail/get_container_services.spec.py.md#implementation
# spec:id: @specs/aws/lightsail/get-container-services
# spec:generated: DO NOT EDIT — edit the spec instead

def get_container_services(store, request: dict) -> dict:
    """Returns information about one or more of your Amazon Lightsail container services."""

    # Auto-generated get handler — verify resource key
    return store.get_resource(request)

