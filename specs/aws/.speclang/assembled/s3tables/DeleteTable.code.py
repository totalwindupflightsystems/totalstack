def handler(store, request: dict) -> dict:
    return store.delete_table(
        tableBucketARN=request["tableBucketARN"],
        namespace=request["namespace"],
        name=request["name"],
    )
