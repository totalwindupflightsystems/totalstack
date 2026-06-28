def handler(store, request: dict) -> dict:
    return store.delete_endpoint_group(request["EndpointGroupArn"])
