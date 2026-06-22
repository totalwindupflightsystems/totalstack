def handler(store, request: dict) -> dict:
    return store.list_users(BrokerId=request["BrokerId"], MaxResults=request.get("MaxResults"), NextToken=request.get("NextToken"))
