def list_identity_sources(store, request: dict) -> dict:
    return store.list_identity_sources(
        PolicyStoreId=request["PolicyStoreId"],
        MaxResults=request.get("MaxResults"),
        NextToken=request.get("NextToken"),
    )
