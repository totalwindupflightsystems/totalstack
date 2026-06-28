def delete_endpoint(store, request: dict) -> dict:
    store.delete_endpoint(request["EndpointIdentifier"])
    return {}
