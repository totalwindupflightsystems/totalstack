def handler(store, request: dict):
    return store.delete_configuration_set(request["ConfigurationSetName"])
