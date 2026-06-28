def handler(store, request: dict) -> dict:
    return store.list_instances(maxResults=request.get("maxResults"), nextToken=request.get("nextToken"))
