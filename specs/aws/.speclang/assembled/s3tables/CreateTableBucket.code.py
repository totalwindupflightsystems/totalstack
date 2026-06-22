def handler(store, request: dict) -> dict:
    return store.create_table_bucket(
        name=request["name"],
        encryptionConfiguration=request.get("encryptionConfiguration"),
        storageClassConfiguration=request.get("storageClassConfiguration"),
        tags=request.get("tags"),
    )
