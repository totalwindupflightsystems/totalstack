def handler(store, request: dict) -> dict:
    return store.get_table_bucket_maintenance_configuration(
        tableBucketARN=request["tableBucketARN"],
    )
