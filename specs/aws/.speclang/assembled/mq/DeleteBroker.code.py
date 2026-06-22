def handler(store, request: dict) -> dict:
    return store.delete_broker(BrokerId=request["BrokerId"])
