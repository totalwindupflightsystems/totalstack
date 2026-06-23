def handler(store, request: dict) -> dict:
    return store.list_apps(request.get("nextToken"), request.get("maxResults"))
