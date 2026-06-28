def delete_deployment(store, request: dict) -> dict:
    store.delete_deployment(request["deploymentId"])
    return {}
