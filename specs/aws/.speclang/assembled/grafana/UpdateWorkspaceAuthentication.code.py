def handler(store, request: dict) -> dict:
    return store.update_workspace_authentication(
        workspaceId=request["workspaceId"],
        authenticationProviders=request["authenticationProviders"],
    )
