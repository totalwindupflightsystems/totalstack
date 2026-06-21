# spec:trace: aws/lightsail/get_operations.spec.py.md#implementation
# spec:id: @specs/aws/lightsail/get-operations
# spec:generated: DO NOT EDIT — edit the spec instead

def get_operations(store, request: dict) -> dict:
    """Returns information about all operations. Results are returned from oldest to newest, up to a maximum of 200. Results can be paged by making each subsequent call to GetOperations use the maximum (last"""

    # Auto-generated get handler — verify resource key
    return store.get_resource(request)

