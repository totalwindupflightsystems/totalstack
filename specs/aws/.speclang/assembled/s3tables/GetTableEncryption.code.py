def handler(store, request: dict) -> dict:
    return store.get_table_encryption(
        tableBucketARN=request["tableBucketARN"],
        namespace=request["namespace"],
        name=request["name"],
    )
