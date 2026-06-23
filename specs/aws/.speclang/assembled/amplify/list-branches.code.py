def handler(store, request: dict) -> dict:
    return store.list_branches(request["appId"], request.get("nextToken"), request.get("maxResults"))
