def handler(store, request: dict) -> dict:
    return store.list_db_clusters(
        nextToken=request.get("nextToken"),
        maxResults=request.get("maxResults"),
    )
