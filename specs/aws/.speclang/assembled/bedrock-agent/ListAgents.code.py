def handler(store, request: dict) -> dict:
    return store.list_agents(
        maxResults=request.get("maxResults"),
        nextToken=request.get("nextToken"))
