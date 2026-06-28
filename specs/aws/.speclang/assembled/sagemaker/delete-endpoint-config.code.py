def delete_endpoint_config(store, request: dict) -> dict:
    store.delete_endpoint_config(request["EndpointConfigName"])
    return {}
