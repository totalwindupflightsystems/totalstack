def handler(store, request: dict) -> dict:
    return store.list_db_parameter_groups(
        nextToken=request.get("nextToken"),
        maxResults=request.get("maxResults"),
    )
