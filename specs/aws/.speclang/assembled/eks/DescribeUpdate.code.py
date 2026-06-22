def handler(store, request: dict) -> dict:
    return store.describe_update(
        name=request["name"],
        updateId=request["updateId"])
