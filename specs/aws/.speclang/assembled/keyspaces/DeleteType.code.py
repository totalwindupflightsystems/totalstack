def handler(store, request: dict) -> dict:
    return store.delete_type(request["keyspaceName"], request["typeName"])

