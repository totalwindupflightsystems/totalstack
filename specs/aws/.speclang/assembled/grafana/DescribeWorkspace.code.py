def handler(store, request: dict) -> dict:
    return store.describe_workspace(workspaceId=request["workspaceId"])
