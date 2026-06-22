def handler(store, request: dict) -> dict:
    return store.get_type(request["keyspaceName"], request["typeName"])

