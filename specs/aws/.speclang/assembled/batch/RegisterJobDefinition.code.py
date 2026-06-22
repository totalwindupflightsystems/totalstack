def handler(store, request: dict) -> dict:
    return store.register_job_definition(
        job_definition_name=request["jobDefinitionName"],
        type=request["type"],
        container_properties=request.get("containerProperties"),
        node_properties=request.get("nodeProperties"),
        parameters=request.get("parameters"),
        platform_capabilities=request.get("platformCapabilities"),
        propagate_tags=request.get("propagateTags", False),
        retry_strategy=request.get("retryStrategy"),
        timeout=request.get("timeout"),
        tags=request.get("tags"),
    )
