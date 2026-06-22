def handler(store, request: dict) -> dict:
    return store.create_workspace(
        accountAccessType=request["accountAccessType"],
        permissionType=request["permissionType"],
        authenticationProviders=request["authenticationProviders"],
        workspaceName=request.get("workspaceName"),
        workspaceDescription=request.get("workspaceDescription"),
        workspaceRoleArn=request.get("workspaceRoleArn"),
        organizationRoleName=request.get("organizationRoleName"),
        workspaceDataSources=request.get("workspaceDataSources"),
        grafanaVersion=request.get("grafanaVersion"),
        tags=request.get("tags"),
        clientToken=request.get("clientToken"),
    )
