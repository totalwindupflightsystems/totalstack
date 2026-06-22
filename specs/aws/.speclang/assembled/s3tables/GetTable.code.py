def handler(store, request: dict) -> dict:
    return store.get_table(
        tableBucketARN=request["tableBucketARN"],
        namespace=request["namespace"],
        name=request["name"],
    )
