def handler(store, request: dict) -> dict:
    return store.delete_workspace_service_account_token(
        workspaceId=request["workspaceId"],
        serviceAccountId=request["serviceAccountId"],
        tokenId=request["tokenId"],
    )
