def handler(store, request: dict) -> dict:
    return store.list_backup_vaults(MaxResults=request.get("MaxResults"),NextToken=request.get("NextToken"))
