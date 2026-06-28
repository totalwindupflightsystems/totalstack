def describe_endpoint(store, request: dict) -> dict:
    return store.describe_endpoint(request["EndpointName"])
