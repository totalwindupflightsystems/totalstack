def handler(store, request: dict) -> dict:
    return store.list_listeners(
        AcceleratorArn=request["AcceleratorArn"],
        MaxResults=request.get("MaxResults"),
        NextToken=request.get("NextToken"),
    )
