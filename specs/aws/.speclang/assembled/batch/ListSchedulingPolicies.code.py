def handler(store, request: dict) -> dict:
    return store.list_scheduling_policies(
        max_results=request.get("maxResults"),
        next_token=request.get("nextToken"),
    )
