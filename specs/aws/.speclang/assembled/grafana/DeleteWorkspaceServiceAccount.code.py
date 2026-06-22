def handler(store, request: dict) -> dict:
    return store.delete_workspace_service_account(
        workspaceId=request["workspaceId"],
        serviceAccountId=request["serviceAccountId"],
    )
