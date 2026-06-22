def handler(store, request: dict) -> dict:
    return store.list_db_instances_for_cluster(
        dbClusterId=request["dbClusterId"],
        nextToken=request.get("nextToken"),
        maxResults=request.get("maxResults"),
    )
