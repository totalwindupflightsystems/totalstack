def handler(store, request: dict) -> dict:
    return store.list_webhooks(request["appId"], request.get("nextToken"), request.get("maxResults"))
