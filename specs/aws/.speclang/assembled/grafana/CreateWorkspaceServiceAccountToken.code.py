def handler(store, request: dict) -> dict:
    return store.create_workspace_service_account_token(
        workspaceId=request["workspaceId"],
        serviceAccountId=request["serviceAccountId"],
        name=request["name"],
        secondsToLive=request["secondsToLive"],
    )
