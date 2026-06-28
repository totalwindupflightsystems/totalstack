def handler(store, request: dict) -> dict:
    return store.describe_endpoint_group(request["EndpointGroupArn"])
