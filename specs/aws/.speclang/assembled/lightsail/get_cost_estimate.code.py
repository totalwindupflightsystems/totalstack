# spec:trace: aws/lightsail/get_cost_estimate.spec.py.md#implementation
# spec:id: @specs/aws/lightsail/get-cost-estimate
# spec:generated: DO NOT EDIT — edit the spec instead

def get_cost_estimate(store, request: dict) -> dict:
    """Retrieves information about the cost estimate for a specified resource. A cost estimate will not generate for a resource that has been deleted."""
    end_time = request.get("endTime", "").strip() if isinstance(request.get("endTime"), str) else request.get("endTime")
    if not end_time:
        raise ValidationException("endTime is required")
    resource_name = request.get("resourceName", "").strip() if isinstance(request.get("resourceName"), str) else request.get("resourceName")
    if not resource_name:
        raise ValidationException("resourceName is required")
    start_time = request.get("startTime", "").strip() if isinstance(request.get("startTime"), str) else request.get("startTime")
    if not start_time:
        raise ValidationException("startTime is required")

    resource = store.cost_estimates(resource_name)
    if not resource:
        raise ResourceNotFoundException("Resource resource_name not found")
    return {"resourceName": resource_name, **resource}

