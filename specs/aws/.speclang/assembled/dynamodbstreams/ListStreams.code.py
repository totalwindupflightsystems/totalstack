def handler(store, request: dict) -> dict:
    return store.list_streams(
        TableName=request.get("TableName"),
        Limit=request.get("Limit"),
        ExclusiveStartStreamArn=request.get("ExclusiveStartStreamArn"),
    )
