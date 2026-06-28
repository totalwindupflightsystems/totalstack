def list_agents(store, request: dict) -> dict:
    return store.list_agents(
        MaxResults=request.get("MaxResults"),
        NextToken=request.get("NextToken"),
    )
