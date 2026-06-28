def handler(store, request: dict) -> dict:
    kwargs = {}
    for k in ("alias", "maxResults", "nextToken"):
        if k in request:
            kwargs[k] = request[k]
    return store.list_workspaces(**kwargs)

