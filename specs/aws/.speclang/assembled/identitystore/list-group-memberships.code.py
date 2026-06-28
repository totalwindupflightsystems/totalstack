def handler(store, request: dict) -> dict:
    return store.list_group_memberships(request["identityStoreId"], request["groupId"], maxResults=request.get("maxResults"), nextToken=request.get("nextToken"))
