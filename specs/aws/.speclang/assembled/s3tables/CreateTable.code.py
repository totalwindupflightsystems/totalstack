def handler(store, request: dict) -> dict:
    return store.create_table(
        tableBucketARN=request["tableBucketARN"],
        namespace=request["namespace"],
        name=request["name"],
        format=request.get("format", "ICEBERG"),
        encryptionConfiguration=request.get("encryptionConfiguration"),
        tableType=request.get("tableType", "customer"),
    )
