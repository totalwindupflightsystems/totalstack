def handler(store, request: dict) -> dict:
    return store.get_namespace(
        tableBucketARN=request["tableBucketARN"],
        namespace=request["namespace"],
    )
