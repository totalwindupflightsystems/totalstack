def handler(store, request: dict) -> dict:
    return store.list_types(request["keyspaceName"])

