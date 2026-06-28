def handler(store, request: dict) -> dict:
    kwargs = {}
    for k in ("name", "maxResults", "nextToken"):
        if k in request:
            kwargs[k] = request[k]
    return store.list_rule_groups_namespaces(request["workspaceId"], **kwargs)

