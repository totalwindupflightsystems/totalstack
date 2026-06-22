def handler(store, request: dict) -> dict:
    return store.submit_job(
        job_name=request["jobName"],
        job_queue=request["jobQueue"],
        job_definition=request["jobDefinition"],
        job_id=request.get("jobId"),
        parameters=request.get("parameters"),
        container_overrides=request.get("containerOverrides"),
        array_properties=request.get("arrayProperties"),
        depends_on=request.get("dependsOn"),
        retry_strategy=request.get("retryStrategy"),
        timeout=request.get("timeout"),
        tags=request.get("tags"),
    )
