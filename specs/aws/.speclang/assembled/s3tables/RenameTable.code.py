def handler(store, request: dict) -> dict:
    return store.rename_table(
        tableBucketARN=request["tableBucketARN"],
        namespace=request["namespace"],
        name=request["name"],
        newName=request["newName"],
    )
