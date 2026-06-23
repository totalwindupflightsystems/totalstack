def handler(store, request: dict) -> dict:
    return store.list_domain_associations(request["appId"], request.get("nextToken"), request.get("maxResults"))
