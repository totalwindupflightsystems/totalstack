def handler(store, request: dict) -> dict:
    return store.create_workspace_service_account(
        workspaceId=request["workspaceId"],
        name=request["name"],
        grafanaRole=request["grafanaRole"],
    )
