def handler(store, request: dict) -> dict:
    return store.list_endpoint_groups(
        ListenerArn=request["ListenerArn"],
        MaxResults=request.get("MaxResults"),
        NextToken=request.get("NextToken"),
    )
