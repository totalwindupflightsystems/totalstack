def handler(store, request: dict) -> dict:
    return store.describe_broker(BrokerId=request["BrokerId"])
