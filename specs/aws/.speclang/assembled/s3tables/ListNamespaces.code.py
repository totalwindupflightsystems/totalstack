def handler(store, request: dict) -> dict:
    return store.list_namespaces(
        tableBucketARN=request["tableBucketARN"],
        prefix=request.get("prefix"),
        continuationToken=request.get("continuationToken"),
        maxNamespaces=request.get("maxNamespaces"),
    )
