def handler(store, request: dict) -> dict:
    return store.delete_rule_groups_namespace(request["workspaceId"], request["name"])

