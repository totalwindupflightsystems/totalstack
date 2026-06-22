def handler(store, request: dict) -> dict:
    return store.list_configurations(MaxResults=request.get("MaxResults"), NextToken=request.get("NextToken"))
