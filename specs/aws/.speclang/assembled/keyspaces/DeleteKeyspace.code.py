def handler(store, request: dict) -> dict:
    return store.delete_keyspace(request["keyspaceName"])

