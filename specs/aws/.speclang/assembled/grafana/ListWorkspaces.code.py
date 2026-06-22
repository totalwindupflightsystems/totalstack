def handler(store, request: dict) -> dict:
    return store.list_workspaces(nextToken=request.get("nextToken"), maxResults=request.get("maxResults"))
