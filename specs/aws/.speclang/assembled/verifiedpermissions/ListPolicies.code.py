def list_policies(store, request: dict) -> dict:
    return store.list_policies(
        PolicyStoreId=request["PolicyStoreId"],
        MaxResults=request.get("MaxResults"),
        NextToken=request.get("NextToken"),
    )
