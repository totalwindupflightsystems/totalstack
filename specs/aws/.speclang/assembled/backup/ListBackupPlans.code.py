def handler(store, request: dict) -> dict:
    return store.list_backup_plans(MaxResults=request.get("MaxResults"),NextToken=request.get("NextToken"))
