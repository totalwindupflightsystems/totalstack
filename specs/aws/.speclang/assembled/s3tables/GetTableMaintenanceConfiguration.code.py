def handler(store, request: dict) -> dict:
    return store.get_table_maintenance_configuration(
        tableBucketARN=request["tableBucketARN"],
        namespace=request["namespace"],
        name=request["name"],
    )
