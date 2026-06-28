def handler(store, request: dict) -> dict:
    return store.list_rule_groups(
        MaxResults=request.get("MaxResults"),
        NextToken=request.get("NextToken"),
        Type=request.get("Type"),
    )
