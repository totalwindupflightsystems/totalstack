def describe_deployment(store, request: dict) -> dict:
    return store.describe_deployment(request["deploymentId"])
