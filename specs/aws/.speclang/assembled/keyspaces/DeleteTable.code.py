def handler(store, request: dict) -> dict:
    return store.delete_table(request["keyspaceName"], request["tableName"])

