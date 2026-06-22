def handler(store, request: dict) -> dict:
    return store.update_job_queue(
        job_queue=request["jobQueue"],
        state=request.get("state"),
        priority=request.get("priority"),
        compute_environment_order=request.get("computeEnvironmentOrder"),
        scheduling_policy_arn=request.get("schedulingPolicyArn"),
    )
