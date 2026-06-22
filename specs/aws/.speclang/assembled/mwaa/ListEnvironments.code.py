def list_environments(store, request: dict) -> dict:
    return store.list_environments(
        request.get("MaxResults"),
        request.get("NextToken"),
    )
