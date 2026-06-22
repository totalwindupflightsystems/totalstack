def handler(store, request: dict) -> dict:
    store.terminate_job_flows(request["JobFlowIds"])
    return {}
