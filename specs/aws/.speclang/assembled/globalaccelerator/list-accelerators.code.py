def handler(store, request: dict) -> dict:
    return store.list_accelerators(
        MaxResults=request.get("MaxResults"),
        NextToken=request.get("NextToken"),
    )
