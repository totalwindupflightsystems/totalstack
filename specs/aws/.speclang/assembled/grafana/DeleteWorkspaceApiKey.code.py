def handler(store, request: dict) -> dict:
    return store.delete_workspace_api_key(
        workspaceId=request["workspaceId"],
        keyName=request["keyName"],
    )
