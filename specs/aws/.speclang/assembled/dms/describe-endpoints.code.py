def describe_endpoints(store, request: dict) -> dict:
    eps = store.describe_endpoints()
    return {"Endpoints": eps}
