def handler(store, request: dict) -> dict:
    return store.update_workspace(
        workspaceId=request["workspaceId"],
        accountAccessType=request.get("accountAccessType"),
        permissionType=request.get("permissionType"),
        workspaceName=request.get("workspaceName"),
        workspaceDescription=request.get("workspaceDescription"),
        workspaceRoleArn=request.get("workspaceRoleArn"),
        organizationRoleName=request.get("organizationRoleName"),
        workspaceDataSources=request.get("workspaceDataSources"),
        workspaceNotificationDestinations=request.get("workspaceNotificationDestinations"),
        workspaceOrganizationalUnits=request.get("workspaceOrganizationalUnits"),
        stackSetName=request.get("stackSetName"),
        vpcConfiguration=request.get("vpcConfiguration"),
        removeVpcConfiguration=request.get("removeVpcConfiguration"),
        networkAccessControl=request.get("networkAccessControl"),
        removeNetworkAccessControl=request.get("removeNetworkAccessControl"),
    )
