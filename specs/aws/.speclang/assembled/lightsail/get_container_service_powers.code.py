# spec:trace: aws/lightsail/get_container_service_powers.spec.py.md#implementation
# spec:id: @specs/aws/lightsail/get-container-service-powers
# spec:generated: DO NOT EDIT — edit the spec instead

def get_container_service_powers(store, request: dict) -> dict:
    """Returns the list of powers that can be specified for your Amazon Lightsail container services. The power specifies the amount of memory, the number of vCPUs, and the base price of the container servic"""

    # Auto-generated get handler — verify resource key
    return store.get_resource(request)

