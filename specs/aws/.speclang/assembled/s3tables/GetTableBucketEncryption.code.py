def handler(store, request: dict) -> dict:
    return store.get_table_bucket_encryption(
        tableBucketARN=request["tableBucketARN"],
    )
