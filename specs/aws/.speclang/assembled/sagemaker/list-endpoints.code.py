def list_endpoints(store, request: dict) -> dict:
    eps = store.list_endpoints()
    return {"Endpoints": eps}
