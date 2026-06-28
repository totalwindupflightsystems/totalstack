def list_locations(store, request: dict) -> dict:
    return store.list_locations(
        MaxResults=request.get("MaxResults"),
        NextToken=request.get("NextToken"),
        Filters=request.get("Filters"),
    )
