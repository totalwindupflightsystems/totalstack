def handler(store, request: dict) -> dict:
    return store.get_table(request["keyspaceName"], request["tableName"])

