def handler(store, request: dict) -> dict:
    return store.create_job_queue(
        job_queue_name=request["jobQueueName"],
        state=request.get("state", "ENABLED"),
        priority=request.get("priority", 1),
        compute_environment_order=request.get("computeEnvironmentOrder", []),
        scheduling_policy_arn=request.get("schedulingPolicyArn", ""),
        tags=request.get("tags"),
    )
