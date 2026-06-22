def handler(store, request: dict) -> dict:
    return store.delete_table_bucket(
        tableBucketARN=request["tableBucketARN"],
    )
