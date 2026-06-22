def handler(store, request: dict) -> dict:
    return store.create_compute_environment(
        compute_environment_name=request["computeEnvironmentName"],
        type=request["type"],
        service_role=request["serviceRole"],
        compute_resources=request.get("computeResources"),
        state=request.get("state", "ENABLED"),
        tags=request.get("tags"),
    )
