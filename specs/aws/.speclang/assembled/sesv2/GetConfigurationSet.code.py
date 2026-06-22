def handler(store, request: dict):
    return store.get_configuration_set(request["ConfigurationSetName"])
