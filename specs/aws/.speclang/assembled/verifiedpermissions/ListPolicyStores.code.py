def list_policy_stores(store, request: dict) -> dict:
    return store.list_policy_stores(
        MaxResults=request.get("MaxResults"),
        NextToken=request.get("NextToken"),
    )
