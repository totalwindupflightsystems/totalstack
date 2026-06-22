def handler(store, request: dict) -> dict:
    return store.get_keyspace(request["keyspaceName"])

