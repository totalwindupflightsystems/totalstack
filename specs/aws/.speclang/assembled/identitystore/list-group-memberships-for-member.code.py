def handler(store, request: dict) -> dict:
    return store.list_group_memberships_for_member(request["identityStoreId"], request["memberId"], maxResults=request.get("maxResults"), nextToken=request.get("nextToken"))
