def handler(store, request: dict) -> dict:
    return store.list_pipelines(
        next_token=request.get("nextToken"),
        max_results=request.get("maxResults"),
    )
