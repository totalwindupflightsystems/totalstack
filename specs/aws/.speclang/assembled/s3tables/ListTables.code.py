def handler(store, request: dict) -> dict:
    return store.list_tables(
        tableBucketARN=request["tableBucketARN"],
        namespace=request["namespace"],
        prefix=request.get("prefix"),
        continuationToken=request.get("continuationToken"),
        maxTables=request.get("maxTables"),
    )
