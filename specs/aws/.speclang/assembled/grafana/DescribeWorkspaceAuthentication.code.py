def handler(store, request: dict) -> dict:
    return store.describe_workspace_authentication(workspaceId=request["workspaceId"])
