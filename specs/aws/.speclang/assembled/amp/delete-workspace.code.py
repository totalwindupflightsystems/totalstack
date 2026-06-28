def handler(store, request: dict) -> dict:
    return store.delete_workspace(request["workspaceId"])

