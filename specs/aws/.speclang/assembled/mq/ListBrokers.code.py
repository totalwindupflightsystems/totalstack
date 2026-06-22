def handler(store, request: dict) -> dict:
    return store.list_brokers(MaxResults=request.get("MaxResults"), NextToken=request.get("NextToken"))
