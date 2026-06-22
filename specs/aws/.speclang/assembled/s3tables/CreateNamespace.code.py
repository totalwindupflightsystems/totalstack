def handler(store, request: dict) -> dict:
    return store.create_namespace(
        tableBucketARN=request["tableBucketARN"],
        namespace=request["namespace"],
    )
