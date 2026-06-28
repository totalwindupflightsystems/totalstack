def list_tasks(store, request: dict) -> dict:
    return store.list_tasks(
        MaxResults=request.get("MaxResults"),
        NextToken=request.get("NextToken"),
        Filters=request.get("Filters"),
    )
