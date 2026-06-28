def list_endpoint_configs(store, request: dict) -> dict:
    configs = store.list_endpoint_configs()
    return {"EndpointConfigs": configs}
