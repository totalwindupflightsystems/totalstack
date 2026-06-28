def handler(store, request: dict) -> dict:
    return store.delete_alert_manager_definition(request["workspaceId"])

