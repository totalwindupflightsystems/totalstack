def handler(store, request: dict) -> dict:
    steps = store.add_job_flow_steps(
        request["JobFlowId"], request["Steps"],
        ExecutionRoleArn=request.get("ExecutionRoleArn"))
    return {"StepIds": [s.Id for s in steps]}
