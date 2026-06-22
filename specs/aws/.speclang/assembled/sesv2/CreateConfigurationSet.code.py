def handler(store, request: dict):
    return store.create_configuration_set(request["ConfigurationSetName"], **{k: v for k, v in request.items() if k != "ConfigurationSetName"})
