def handler(store, request: dict) -> dict:
    return store.list_groups(request["identityStoreId"], maxResults=request.get("maxResults"), nextToken=request.get("nextToken"))
