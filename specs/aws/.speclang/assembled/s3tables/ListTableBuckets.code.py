def handler(store, request: dict) -> dict:
    return store.list_table_buckets(
        prefix=request.get("prefix"),
        continuationToken=request.get("continuationToken"),
        maxBuckets=request.get("maxBuckets"),
        type=request.get("type"),
    )
