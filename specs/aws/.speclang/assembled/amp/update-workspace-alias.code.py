def handler(store, request: dict) -> dict:
    return store.update_workspace_alias(request["workspaceId"], request.get("alias"))

