def handler(store, request: dict) -> dict:
    return store.describe_user(BrokerId=request["BrokerId"], Username=request["Username"])
