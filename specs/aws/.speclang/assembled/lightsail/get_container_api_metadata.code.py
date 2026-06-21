# spec:trace: aws/lightsail/get_container_api_metadata.spec.py.md#implementation
# spec:id: @specs/aws/lightsail/get-container-api-metadata
# spec:generated: DO NOT EDIT — edit the spec instead

def get_container_api_metadata(store, request: dict) -> dict:
    """Returns information about Amazon Lightsail containers, such as the current version of the Lightsail Control (lightsailctl) plugin."""

    # Auto-generated get handler — verify resource key
    return store.get_resource(request)

