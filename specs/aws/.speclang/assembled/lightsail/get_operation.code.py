# spec:trace: aws/lightsail/get_operation.spec.py.md#implementation
# spec:id: @specs/aws/lightsail/get-operation
# spec:generated: DO NOT EDIT — edit the spec instead

def get_operation(store, request: dict) -> dict:
    """Returns information about a specific operation. Operations include events such as when you create an instance, allocate a static IP, attach a static IP, and so on."""
    operation_id = request.get("operationId", "").strip() if isinstance(request.get("operationId"), str) else request.get("operationId")
    if not operation_id:
        raise ValidationException("operationId is required")

    resource = store.operations(operation_id)
    if not resource:
        raise ResourceNotFoundException("Resource operation_id not found")
    return {"operationId": operation_id, **resource}

