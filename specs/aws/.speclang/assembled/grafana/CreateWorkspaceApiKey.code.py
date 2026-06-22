def handler(store, request: dict) -> dict:
    return store.create_workspace_api_key(
        workspaceId=request["workspaceId"],
        keyName=request["keyName"],
        keyRole=request["keyRole"],
        secondsToLive=request["secondsToLive"],
    )
