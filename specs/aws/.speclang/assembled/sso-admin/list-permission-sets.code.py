def handler(store, request: dict) -> dict:
    return store.list_permission_sets(request["instanceArn"], maxResults=request.get("maxResults"), nextToken=request.get("nextToken"))
