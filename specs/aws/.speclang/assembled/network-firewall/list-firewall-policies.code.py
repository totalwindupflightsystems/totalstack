def handler(store, request: dict) -> dict:
    return store.list_firewall_policies(
        MaxResults=request.get("MaxResults"),
        NextToken=request.get("NextToken"),
    )
