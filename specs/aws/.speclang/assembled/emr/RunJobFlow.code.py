def handler(store, request: dict) -> dict:
    kwargs = {k: v for k, v in request.items() if k != "Name"}
    record = store.run_job_flow(request["Name"], **kwargs)
    return {"JobFlowId": record.Id}
