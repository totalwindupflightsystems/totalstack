def handler(store, request: dict) -> dict:
    return store.describe_alert_manager_definition(request["workspaceId"])

