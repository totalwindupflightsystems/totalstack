def handler(store, request: dict):
    return store.list_configuration_sets()
