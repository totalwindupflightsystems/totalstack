def handler(store, request: dict) -> dict:
    return store.describe_rule_groups_namespace(request["workspaceId"], request["name"])

