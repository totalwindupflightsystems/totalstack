def handler(store, request: dict) -> dict:
    return store.list_firewalls(
        MaxResults=request.get("MaxResults"),
        NextToken=request.get("NextToken"),
        VpcIds=request.get("VpcIds"),
    )
