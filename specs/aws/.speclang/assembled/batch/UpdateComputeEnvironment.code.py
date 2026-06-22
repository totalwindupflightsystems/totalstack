def handler(store, request: dict) -> dict:
    return store.update_compute_environment(
        compute_environment=request["computeEnvironment"],
        state=request.get("state"),
        compute_resources=request.get("computeResources"),
        service_role=request.get("serviceRole"),
    )
