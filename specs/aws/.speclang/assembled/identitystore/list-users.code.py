def handler(store, request: dict) -> dict:
    return store.list_users(request["identityStoreId"], maxResults=request.get("maxResults"), nextToken=request.get("nextToken"))
