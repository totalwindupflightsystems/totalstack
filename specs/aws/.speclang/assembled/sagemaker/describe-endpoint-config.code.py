def describe_endpoint_config(store, request: dict) -> dict:
    return store.describe_endpoint_config(request["EndpointConfigName"])
