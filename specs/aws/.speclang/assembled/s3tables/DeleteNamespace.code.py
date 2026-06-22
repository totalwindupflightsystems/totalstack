def handler(store, request: dict) -> dict:
    return store.delete_namespace(
        tableBucketARN=request["tableBucketARN"],
        namespace=request["namespace"],
    )
