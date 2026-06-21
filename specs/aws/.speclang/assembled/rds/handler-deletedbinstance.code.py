def handler(store, request: dict) -> dict:
    identifier = request["DBInstanceIdentifier"]
    skip = request.get("SkipFinalSnapshot", True)
    return store.delete_instance(identifier, skip_final_snapshot=skip)
